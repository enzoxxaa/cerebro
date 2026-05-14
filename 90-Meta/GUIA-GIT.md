---
tipo: guia
tema: git
proyecto: vault
fecha: 2026-05-13
tags:
  - meta
  - git
  - workflow
---

# Guía de Git para el Segundo Cerebro

Referencia rápida para mantener el vault sincronizado entre máquinas (local + cluster) usando GitHub.

> **Repositorio:** `git@github.com:enzoxxaa/cerebro.git`
> **Ruta local (Omarchy):** `~/Documents/SegundoCerebro`
> **Branch principal:** `main`

---

## 1. Setup inicial en una máquina nueva

Pasos que ya están hechos en Omarchy. Documentados aquí para cuando montes el vault en otra máquina.

```bash
# 1. Instalar git (en Arch ya viene de base, en Debian/Ubuntu: sudo apt install git)
git --version

# 2. Configurar identidad
git config --global user.name  "enzoxxaa"
git config --global user.email "enxoda@gmail.com"

# 3. Generar clave SSH (sin passphrase para que Obsidian-Git no la pida)
ssh-keygen -t ed25519 -C "enxoda@gmail.com" -f ~/.ssh/id_ed25519 -N ""

# 4. Copiar la clave pública y pegarla en https://github.com/settings/keys
cat ~/.ssh/id_ed25519.pub

# 5. Verificar conexión
ssh -T git@github.com   # debería decir "Hi enzoxxaa!"

# 6. Clonar el vault
git clone git@github.com:enzoxxaa/cerebro.git ~/Documents/SegundoCerebro
```

### Config global recomendada (ya activa en Omarchy)

```bash
git config --global pull.rebase true            # pull = fetch + rebase, no merge
git config --global push.autoSetupRemote true   # primer push no necesita -u
git config --global rerere.enabled true         # recuerda resoluciones de conflicto
git config --global init.defaultBranch main     # OJO: en Omarchy está en "master"
```

> **Nota:** En esta máquina `init.defaultBranch=master`. No afecta a `cerebro` (que es `main`), pero conviene cambiarlo si vas a iniciar repos nuevos.

---

## 2. Flujo diario (lo único que tenés que recordar)

### Antes de empezar a editar

```bash
cd ~/Documents/SegundoCerebro
git pull
```

### Después de editar

```bash
git status              # ver qué cambió
git add .               # marcar todo para commitear
git commit -m "docs: descripción breve"
git push
```

Si seguís el patrón de **conventional commits** (lo que ya usás en este repo):

| Prefijo    | Cuándo usarlo                                 |
| ---------- | --------------------------------------------- |
| `docs:`    | Notas nuevas o editadas (lo más común)        |
| `feat:`    | Nuevas plantillas, scripts, automatizaciones  |
| `fix:`     | Corregir errores, links rotos, typos          |
| `chore:`   | Mantenimiento (gitignore, configs)            |
| `cluster:` | Commits hechos desde el cluster universitario |

---

## 3. Comandos esenciales

### Ver estado

```bash
git status              # qué archivos cambiaron
git diff                # qué líneas cambiaron (sin staging)
git diff --staged       # qué cambios están listos para commit
git log --oneline -10   # últimos 10 commits
git log --oneline --graph --all   # historial visual con ramas
```

### Aliases ya configurados en esta máquina

| Alias    | Comando completo |
|----------|------------------|
| `git st` | `git status`     |
| `git co` | `git checkout`   |
| `git br` | `git branch`     |
| `git ci` | `git commit`     |

### Staging selectivo

```bash
git add archivo.md              # un archivo
git add 10-Proyectos/           # una carpeta
git add -p                      # interactivo, fragmento por fragmento
git restore --staged archivo.md # sacar del staging
```

---

## 4. Resolver conflictos (sucede si editás en local y cluster a la vez)

Cuando `git pull` falla con conflicto:

```bash
git status              # te dice qué archivos están "both modified"
```

Abrí el archivo en Obsidian o tu editor. Vas a ver:

```
<<<<<<< HEAD
Texto de tu máquina local
=======
Texto que venía del remoto
>>>>>>> origin/main
```

1. Editá manualmente: dejá el texto que querés conservar y borrá las marcas `<<<<<<<`, `=======`, `>>>>>>>`.
2. Guardá el archivo.
3. Marcalo como resuelto y continuá:

```bash
git add archivo-en-conflicto.md
git rebase --continue   # si fue durante un pull (rebase está activo por config)
# o
git commit              # si fue durante un merge
```

Si la cosa se va de las manos:

```bash
git rebase --abort      # vuelve al estado antes del pull
```

### Prevención

- **Siempre `git pull` antes de empezar a editar.**
- Si trabajás en cluster y local el mismo día, hacé push apenas termines en una máquina antes de pasar a la otra.

---

## 5. Deshacer cosas

### Descartar cambios no commiteados

```bash
git restore archivo.md          # un archivo
git restore .                   # todos (CUIDADO, no se puede deshacer)
```

### Deshacer el último commit (sin perder los cambios)

```bash
git reset --soft HEAD~1         # los cambios vuelven a staging
git reset HEAD~1                # los cambios vuelven a working tree
```

### Deshacer el último commit (perdiendo cambios)

```bash
git reset --hard HEAD~1         # destructivo, sólo si estás seguro
```

### Recuperar algo que pensabas que estaba perdido

```bash
git reflog                      # historial COMPLETO de HEAD, incluso de cosas reseteadas
git checkout <hash-del-reflog>  # te lleva ahí
```

> Git casi nunca pierde nada. Si commiteaste alguna vez, está en el reflog (al menos 90 días).

### Ver una versión vieja de un archivo

```bash
git log --oneline archivo.md           # ver commits que tocaron el archivo
git show <hash>:archivo.md             # ver cómo era el archivo en ese commit
git show <hash>:archivo.md > /tmp/x    # guardarlo a un archivo temporal
```

---

## 6. Sincronización entre local y cluster

El flujo asumido es: editás notas en **local**, generás resultados/sesiones en el **cluster**. Ambos hacen commit+push al mismo `main`.

### En local (al empezar el día)

```bash
cd ~/Documents/SegundoCerebro
git pull
```

### En el cluster (al final de una sesión)

```bash
cd ~/cerebro-vault
git pull                # primero, para no chocar
git add 00-Inbox/cluster/2026-05-13_cluster_*.md
git commit -m "cluster: sesion 2026-05-13 descripcion"
git push
```

### Si push falla con "rejected, non-fast-forward"

Significa que el remoto avanzó desde tu último pull. Solución:

```bash
git pull       # con rebase activado, va a reaplicar tus commits sobre los nuevos
git push
```

---

## 7. Plugin Obsidian-Git (los commits "vault backup")

El historial muestra commits del tipo `vault backup: 2026-04-18 14:14:17`. Esos los hace automáticamente el plugin **Obsidian Git** dentro de la app.

### Configuración recomendada del plugin

- **Auto pull on startup:** ON
- **Auto push interval:** 5–15 min
- **Auto commit-and-sync:** ON con intervalo razonable (10 min)
- **Commit message:** `vault backup: {{date}}` (formato actual)

### Cuándo NO confiar sólo en el plugin

- Cuando vas a hacer cambios estructurales grandes (renombrar carpetas, reorganizar PARA).
- Cuando trabajás simultáneamente desde local y cluster — el plugin sólo corre en local.

En esos casos, hacé los commits a mano con mensajes descriptivos (`docs:`, `feat:`, `chore:`).

---

## 8. Branches (uso opcional)

Para experimentos grandes que no quieras mezclar con `main` aún:

```bash
git switch -c experimento-zettelkasten   # crear y moverse a la rama
# ... editás cosas ...
git add . && git commit -m "feat: pruebo estructura zettel"
git push                                 # push.autoSetupRemote la sube sola

# Cuando quieras integrarla:
git switch main
git merge experimento-zettelkasten
git push

# O descartarla:
git branch -D experimento-zettelkasten
```

Para el día a día del vault probablemente no las necesites — `main` directo es lo más simple.

---

## 9. Tags (snapshots con nombre)

Útil para marcar hitos del sistema (ej. fin de tesis, cierre de proyecto).

```bash
git tag -a v1-fin-bilayer -m "Estado del vault al cerrar paper P01"
git push --tags

# Ver tags
git tag

# Volver a ver el estado de un tag (sin modificar main)
git checkout v1-fin-bilayer
git switch main          # para volver
```

---

## 10. Cheatsheet de emergencia

| Quiero...                                          | Comando                                          |
|----------------------------------------------------|--------------------------------------------------|
| Ver qué cambió                                     | `git status` / `git diff`                        |
| Subir cambios                                      | `git add . && git commit -m "..." && git push`   |
| Bajar cambios                                      | `git pull`                                       |
| Deshacer cambios sin commitear                     | `git restore <archivo>`                          |
| Cancelar el último commit (mantener cambios)       | `git reset --soft HEAD~1`                        |
| Ver historial                                      | `git log --oneline --graph -20`                  |
| Recuperar algo borrado                             | `git reflog` → `git checkout <hash>`             |
| Abortar un pull con conflictos                     | `git rebase --abort`                             |
| Ver quién tocó una línea                           | `git blame archivo.md`                           |
| Buscar texto en todo el historial                  | `git log -S "texto" --all`                       |

---

## 11. Cosas que NO hacer

- `git push --force` en `main`. Reescribe historia y rompe el clon del cluster.
- `git reset --hard` sin haber hecho `git status` antes.
- Commitear PDFs o archivos grandes (ya está ignorado en `.gitignore`, pero ojo si lo editás).
- Commitear `.obsidian/workspace.json` (también ignorado — cambia cada vez que abrís Obsidian).
- Editar los mismos archivos en local y cluster sin haber pulled antes.

---

## 12. Referencias

- [Pro Git book (gratis, oficial)](https://git-scm.com/book/es/v2)
- [Oh Shit, Git!?!](https://ohshitgit.com/es) — recetas para salir de líos
- `git help <comando>` — manual oficial offline
