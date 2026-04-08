#!/usr/bin/env python3
"""
procesar_inbox.py — Procesa notas crudas del inbox y las mueve a su destino.

Uso:
    python3 procesar_inbox.py [--dry-run] [--no-git]

Opciones:
    --dry-run   Muestra qué haría sin mover ni modificar nada.
    --no-git    No hace git commit al final.
"""

import os
import re
import sys
import shutil
import subprocess
from datetime import datetime
from pathlib import Path

# ── Configuración ──────────────────────────────────────────────────────────────

VAULT = Path(__file__).parent.parent.parent  # raíz del vault

INBOX_DIRS = [
    VAULT / "00-Inbox" / "cluster",
    VAULT / "00-Inbox" / "personal",
    VAULT / "00-Inbox",  # raíz del inbox también
]

# Mapeo tipo+proyecto → carpeta destino
DESTINOS = {
    ("sesion", "P01-Bilayer"): VAULT / "10-Proyectos/P01-Bilayer-Paper/sesiones",
    ("sesion", "P01"):         VAULT / "10-Proyectos/P01-Bilayer-Paper/sesiones",
    ("sesion", "P02-Fondecyt"):VAULT / "10-Proyectos/P02-Fondecyt-PMMA/sesiones",
    ("sesion", "P02"):         VAULT / "10-Proyectos/P02-Fondecyt-PMMA/sesiones",
    ("literatura", None):      VAULT / "30-Recursos/literatura-md",
    ("concepto", None):        VAULT / "30-Recursos/conceptos",
}

# Índices de proyecto para agregar wikilinks
INDICES = {
    "P01-Bilayer": VAULT / "10-Proyectos/P01-Bilayer-Paper/_indice.md",
    "P01":         VAULT / "10-Proyectos/P01-Bilayer-Paper/_indice.md",
    "P02-Fondecyt":VAULT / "10-Proyectos/P02-Fondecyt-PMMA/_indice.md",
    "P02":         VAULT / "10-Proyectos/P02-Fondecyt-PMMA/_indice.md",
}

# ── Helpers ────────────────────────────────────────────────────────────────────

def parse_frontmatter(content: str) -> dict:
    """Parsea el bloque YAML frontmatter de un archivo .md."""
    fm = {}
    if not content.startswith("---"):
        return fm
    end = content.find("\n---", 3)
    if end == -1:
        return fm
    block = content[3:end].strip()
    for line in block.splitlines():
        if ":" in line and not line.strip().startswith("-"):
            key, _, val = line.partition(":")
            key = key.strip()
            val = val.strip().strip('"').strip("'")
            # Normalizar listas inline simples [a, b]
            if val.startswith("[") and val.endswith("]"):
                val = [v.strip().strip('"') for v in val[1:-1].split(",") if v.strip()]
            fm[key] = val
    return fm

def update_frontmatter_estado(path: Path, dry_run: bool) -> None:
    """Cambia estado: sin-procesar → procesado en el archivo."""
    content = path.read_text(encoding="utf-8")
    now = datetime.now().strftime("%Y-%m-%d")
    new_content = re.sub(
        r"^(estado:\s*)sin-procesar",
        f"\\1procesado\nfecha-procesado: {now}",
        content,
        flags=re.MULTILINE,
    )
    if not dry_run:
        path.write_text(new_content, encoding="utf-8")

def append_wikilink_to_indice(indice_path: Path, note_name: str, dry_run: bool) -> None:
    """Agrega [[note_name]] en la sección 'Sesiones de trabajo' del _indice.md."""
    if not indice_path.exists():
        return
    content = indice_path.read_text(encoding="utf-8")
    marker = "## Sesiones de trabajo"
    if marker not in content:
        return
    wikilink = f"- [[{note_name}]]"
    if wikilink in content:
        return  # ya existe, no duplicar
    new_content = content.replace(
        marker,
        f"{marker}\n{wikilink}",
    )
    if not dry_run:
        indice_path.write_text(new_content, encoding="utf-8")
    print(f"  → wikilink agregado en {indice_path.name}")

def git_commit(moved_files: list[Path], updated_indices: list[Path], dry_run: bool) -> None:
    """Hace git add + commit de los archivos procesados."""
    if dry_run or not moved_files:
        return
    files_to_add = [str(f.relative_to(VAULT)) for f in moved_files + updated_indices]
    try:
        subprocess.run(["git", "add"] + files_to_add, cwd=VAULT, check=True)
        n = len(moved_files)
        date_str = datetime.now().strftime("%Y-%m-%d %H:%M")
        msg = f"procesar: inbox {date_str} ({n} {'archivo' if n == 1 else 'archivos'})"
        subprocess.run(["git", "commit", "-m", msg], cwd=VAULT, check=True)
        print(f"\n✓ Git commit: {msg}")
    except subprocess.CalledProcessError as e:
        print(f"[AVISO] Error en git: {e}")

# ── Lógica principal ───────────────────────────────────────────────────────────

def determinar_destino(fm: dict) -> tuple[Path | None, Path | None]:
    """Devuelve (carpeta_destino, indice_path) según el frontmatter."""
    tipo = fm.get("tipo", "").strip()
    proyecto = fm.get("proyecto", "").strip()
    alumno = fm.get("alumno", "").strip()

    # Sesión de tutoría
    if tipo == "sesion-tutoria":
        if alumno:
            destino = VAULT / f"20-Areas/clases-particulares/{alumno}/sesiones"
        else:
            destino = VAULT / "20-Areas/clases-particulares"
        return destino, None

    # Sesión de investigación
    if tipo == "sesion":
        for key in [(tipo, proyecto), (tipo, proyecto.split("-")[0] if "-" in proyecto else None)]:
            if key in DESTINOS:
                indice = INDICES.get(proyecto)
                return DESTINOS[key], indice
        return None, None  # proyecto no reconocido → dejar en inbox

    # Literatura y conceptos
    key = (tipo, None)
    if key in DESTINOS:
        return DESTINOS[key], None

    return None, None  # tipo no clasificable

def procesar_archivo(md_path: Path, dry_run: bool) -> tuple[Path | None, Path | None]:
    """Procesa un archivo del inbox. Devuelve (destino, indice) si fue movido."""
    content = md_path.read_text(encoding="utf-8")
    fm = parse_frontmatter(content)

    estado = fm.get("estado", "").strip()
    if estado != "sin-procesar":
        return None, None

    destino_dir, indice_path = determinar_destino(fm)

    if destino_dir is None:
        print(f"  [PENDIENTE] {md_path.name} — tipo/proyecto no reconocido, queda en inbox")
        return None, None

    destino_file = destino_dir / md_path.name

    print(f"  → {md_path.name}")
    print(f"     origen:  {md_path.parent.relative_to(VAULT)}")
    print(f"     destino: {destino_file.relative_to(VAULT)}")

    if not dry_run:
        destino_dir.mkdir(parents=True, exist_ok=True)
        shutil.move(str(md_path), str(destino_file))
        update_frontmatter_estado(destino_file, dry_run=False)

    if indice_path:
        note_name = md_path.stem
        append_wikilink_to_indice(indice_path, note_name, dry_run)
        return destino_file, indice_path

    return destino_file, None

def main():
    dry_run = "--dry-run" in sys.argv
    no_git  = "--no-git" in sys.argv

    if dry_run:
        print("=== MODO DRY-RUN (sin cambios) ===\n")

    moved_files = []
    updated_indices = []
    processed = 0

    # Recopilar todos los .md del inbox (sin entrar en subdirectorios ya procesados)
    inbox_root = VAULT / "00-Inbox"
    all_md = sorted(inbox_root.rglob("*.md"))

    print(f"Revisando {len(all_md)} archivos en 00-Inbox...\n")

    for md_path in all_md:
        dest, indice = procesar_archivo(md_path, dry_run)
        if dest:
            moved_files.append(dest)
            processed += 1
        if indice and indice not in updated_indices:
            updated_indices.append(indice)

    if processed == 0:
        print("Inbox vacío o sin archivos sin-procesar.")
    else:
        print(f"\n✓ {processed} archivo(s) procesado(s).")
        if not no_git:
            git_commit(moved_files, updated_indices, dry_run)

if __name__ == "__main__":
    main()
