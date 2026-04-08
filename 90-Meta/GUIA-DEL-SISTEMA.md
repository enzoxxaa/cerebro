---
tipo: meta
tags:
  - sistema
  - documentacion-interna
---

# Guía del Sistema — Cerebro

> Documento interno de referencia. Explica la arquitectura completa del vault, dónde va cada cosa y cómo fluye la información desde el cluster y desde local.

---

## 1. Mapa mental de la estructura

```
cerebro/
│
├── 00-Inbox/               ← TODO entra aquí primero
│   ├── cluster/            ← notas del cluster (vía git push)
│   └── personal/           ← notas rápidas manuales
│
├── 10-Proyectos/           ← trabajo activo con objetivo y fecha
│   ├── P01-Bilayer-Paper/
│   └── P02-Fondecyt-PMMA/
│
├── 20-Areas/               ← responsabilidades continuas sin fin
│   ├── investigacion/
│   └── clases-particulares/   ← ISLA SEPARADA, no cruzar wikilinks
│
├── 30-Recursos/            ← referencia: papers, conceptos, métodos
│
├── 40-Archivo/             ← proyectos y alumnos terminados
│
├── 50-Diario/              ← daily notes (auto-generadas)
│
└── 90-Meta/                ← el sistema en sí mismo
    ├── plantillas/
    ├── bases/              ← vistas .base (Obsidian Bases)
    ├── automatizacion/
    └── GUIA-DEL-SISTEMA.md ← este archivo
```

---

## 2. Regla fundamental de separación

```
#investigacion  ←→  #tutoria
```

Estas dos esferas **nunca se cruzan**. No hay wikilinks entre `20-Areas/clases-particulares/` y cualquier nota de investigación. Las bases y vistas tampoco mezclan ambos mundos. Si una nota no tiene claro a cuál pertenece, va a `00-Inbox/personal/` y se clasifica manualmente.

---

## 3. Dónde va cada tipo de fichero

### 3.1 Desde el cluster (vía git)

| Qué pasó en el cluster | Tipo de nota | Destino final (tras procesar) |
|---|---|---|
| Corrí una simulación MD | `sesion` | `10-Proyectos/P0X/sesiones/` |
| Analicé resultados (RDF, RMSD, etc.) | `sesion` | `10-Proyectos/P0X/sesiones/` |
| Encontré un error y lo resolví | `sesion` (actividad: debug) | `10-Proyectos/P0X/sesiones/` |
| Leí un paper durante el trabajo | `literatura` | `30-Recursos/literatura-md/` |
| Tuve una idea de análisis/figura | `intake` | queda en inbox hasta clasificar |

**El flujo es siempre**:
1. Escribes el `.md` con el frontmatter correcto
2. Lo dejas en `00-Inbox/cluster/`
3. Haces `git push`
4. La máquina local lo recibe y el script lo mueve automáticamente

### 3.2 Desde local (manual en Obsidian)

| Situación | Tipo de nota | Dónde crearla directamente |
|---|---|---|
| Sesión de tutoría con Martina o Máximo | `sesion-tutoria` | `20-Areas/clases-particulares/{Alumno}/sesiones/` |
| Leer un paper en casa | `literatura` | `30-Recursos/literatura-md/` |
| Idea rápida sin clasificar | `intake` | `00-Inbox/personal/` |
| Concepto que quiero documentar | `concepto` | `30-Recursos/conceptos/` |
| Protocolo reutilizable (GROMACS, etc.) | libre | `20-Areas/investigacion/protocolos/` |
| Daily note | `diario` | se crea sola con Cmd+P → "Open today's daily note" |

### 3.3 Ficheros no-markdown

| Tipo de fichero | Dónde |
|---|---|
| Imágenes, capturas, figuras | `30-Recursos/adjuntos/` (Obsidian lo hace automático) |
| Scripts Python de análisis | No van en el vault — viven en el cluster |
| Datos de simulación (.xtc, .tpr, etc.) | No van en el vault — viven en el cluster |
| PDFs de papers | Opcional en `30-Recursos/adjuntos/` pero pesados; mejor solo el DOI en la nota |

---

## 4. Frontmatter obligatorio por tipo

Cada nota DEBE tener como mínimo estos campos para que el sistema funcione.

### `sesion` (cluster o local)
```yaml
---
tipo: sesion
proyecto: P01-Bilayer        # o P02-Fondecyt
fecha: 2026-04-08
actividad: simulacion        # simulacion | analisis | escritura | debug | reunion
sistema: cluster             # cluster | local
herramienta: GROMACS         # GROMACS | AMBER | Python | VMD
resumen: "Frase corta"
siguiente-paso: "Qué viene"
estado: sin-procesar         # ← el script lo cambia a "procesado" al moverlo
tags: [sesion, investigacion]
---
```

### `sesion-tutoria`
```yaml
---
tipo: sesion-tutoria
alumno: Martina              # Martina | Maximo
fecha: 2026-04-08
materia: Matemáticas
tema: "Ecuaciones de 2do grado"
pago-registrado: false       # ← cambiar a true cuando se pague
estado: sin-procesar         # si la dejas en inbox; omitir si la creas directo en destino
tags: [tutoria, clases-particulares]
---
```

### `literatura`
```yaml
---
tipo: literatura
titulo: "Título del paper"
doi: "10.xxxx/xxxxxx"
estado-lectura: por-leer     # por-leer | en-progreso | leido
relevancia: P01              # P01 | P02 | general
estado: sin-procesar
tags: [literatura, investigacion]
---
```

### `intake` (nota cruda sin clasificar)
```yaml
---
tipo: intake
origen: cluster              # cluster | personal | reunion | lectura
proyecto: P01-Bilayer        # o "general" si no sabes aún
fecha: 2026-04-08
estado: sin-procesar
prioridad: media             # alta | media | baja
resumen-breve: "Una línea"
---
```

---

## 5. Convención de nombres de archivo

```
YYYY-MM-DD_ORIGEN_descripcion-en-kebab-case.md
```

| Campo | Valores | Ejemplos |
|---|---|---|
| `YYYY-MM-DD` | fecha del contenido, no de creación | `2026-04-08` |
| `ORIGEN` | `cluster` / `local` / `personal` | |
| `descripcion` | kebab-case, sin acentos, máx 5 palabras | `equilibrado-bicapa-TTG` |

**Ejemplos reales:**
```
2026-04-08_cluster_equilibrado-bicapa-TTG.md
2026-04-08_cluster_analisis-RDF-TTC-TTO.md
2026-04-08_local_sesion-Martina-trigonometria.md
2026-04-09_cluster_debug-mdrun-PMMA-run3.md
2026-04-09_personal_idea-figura-concentrador.md
```

Las notas de `10-Proyectos/` o `20-Areas/` creadas directamente (no desde inbox) pueden usar nombre libre, pero se recomienda el mismo formato para sesiones.

---

## 6. El pipeline de automatización

### 6.1 Ruta desde el cluster hasta Obsidian

```
[Cluster]                   [GitHub]               [Local]
    │                           │                      │
    │  1. escribes el .md       │                      │
    │  2. lo dejas en           │                      │
    │     00-Inbox/cluster/     │                      │
    │  3. git push ────────────►│                      │
    │                           │   4. obsidian-git    │
    │                           │      pull (≤5 min) ──►│
    │                           │                      │
    │                           │   5. hook post-merge │
    │                           │      dispara el      │
    │                           │      script ─────────►│
    │                           │                      │  6. script mueve
    │                           │                      │     el .md a su
    │                           │                      │     destino final
    │                           │                      │  7. wikilink en
    │                           │◄── git push (10min) ─│     _indice.md
```

### 6.2 Lo que hace `procesar_inbox.py`

1. Escanea todo `00-Inbox/` buscando `.md` con `estado: sin-procesar`
2. Lee el frontmatter de cada uno
3. Determina el destino según `tipo` + `proyecto` (o `alumno`)
4. Mueve el archivo al destino
5. Cambia `estado: sin-procesar` → `estado: procesado` + agrega `fecha-procesado`
6. Si es una sesión de proyecto, agrega `- [[nombre-del-archivo]]` en la sección **Sesiones de trabajo** del `_indice.md` correspondiente
7. Si el tipo no se reconoce, deja la nota en el inbox y avisa por consola

### 6.3 Cuándo se ejecuta automáticamente

- Después de cada `git pull` exitoso (hook `.git/hooks/post-merge`)
- obsidian-git hace pull cada 5 minutos con Obsidian abierto

### 6.4 Cómo ejecutarlo manualmente

```bash
cd ~/Documentos/GitHub/cerebro

# Ver qué haría sin hacer cambios
python3 90-Meta/automatizacion/procesar_inbox.py --dry-run

# Ejecutar normalmente (con git commit al final)
python3 90-Meta/automatizacion/procesar_inbox.py

# Ejecutar sin hacer git commit (útil para pruebas)
python3 90-Meta/automatizacion/procesar_inbox.py --no-git
```

---

## 7. Flujo del día a día

### Mañana (máquina local)

```
1. Abrir Obsidian
   → obsidian-git hace pull automático al abrir
   → si llegan notas del cluster, el hook las procesa

2. Abrir la daily note
   Cmd+P → "Open today's daily note"
   → se crea en 50-Diario/2026/04/2026-04-08.md usando la plantilla

3. Revisar el inbox
   → abrir 90-Meta/bases/inbox.base
   → ver si quedó algo sin-procesar que necesite clasificación manual
```

### Durante el día en el cluster

```
1. Trabajas con GROMACS/AMBER/Python
2. Al terminar algo significativo, creas la nota:

   cp ~/cerebro-vault/90-Meta/plantillas/sesion-cluster.md \
      ~/cerebro-vault/00-Inbox/cluster/2026-04-08_cluster_descripcion.md

3. Editas el .md con los detalles de la sesión
4. Push:
   cd ~/cerebro-vault
   git add 00-Inbox/cluster/2026-04-08_cluster_descripcion.md
   git commit -m "cluster: sesion 2026-04-08 descripcion"
   git push origin main
```

### Tutoría (local)

```
1. Crear nota directamente en destino final:
   20-Areas/clases-particulares/Martina/sesiones/2026-04-08_local_sesion-Martina-tema.md

   O usando la plantilla desde Obsidian:
   Cmd+P → "Insert template" → sesion-tutoria

2. Rellenar el frontmatter y el contenido
3. Al cobrar: cambiar pago-registrado: false → true
```

### Noche

```
1. obsidian-git hace commit+push automático cada 10 minutos
   → no necesitas hacer nada manualmente
2. Cerrar la daily note con el bloque de cierre
```

---

## 8. Las Bases (vistas de base de datos)

Abrir desde `90-Meta/bases/`. Son vistas dinámicas sobre el vault completo.

| Base | Qué muestra |
|---|---|
| `inbox.base` | Todas las notas con `estado: sin-procesar` — lo que está pendiente de procesar |
| `proyectos-activos.base` | Proyectos con `estado: activo` — tabla de seguimiento |
| `sesiones-tutoria.base` | Todas las sesiones de tutoría + vista de pagos pendientes |
| `literatura.base` | Papers por leer / leídos, agrupados por relevancia y proyecto |

**Para embeber una base en otra nota** (ej: en el `_indice.md` de un proyecto):
```
![[90-Meta/bases/proyectos-activos.base]]
```

---

## 9. Las Plantillas

Ubicación: `90-Meta/plantillas/`

| Plantilla | Cuándo usarla |
|---|---|
| `diario.md` | Daily note — se aplica automáticamente |
| `sesion-cluster.md` | Cada vez que documentas trabajo en el cluster |
| `sesion-tutoria.md` | Cada clase con Martina o Máximo |
| `literatura.md` | Cada paper que quieras registrar |
| `proyecto.md` | Al iniciar un nuevo proyecto |
| `intake.md` | Nota rápida sin clasificar |

**Cómo insertar una plantilla en Obsidian:**
```
Cmd+P → "Insertar plantilla" → seleccionar
```

---

## 10. El `CLAUDE.md` y el protocolo del cluster

`CLAUDE.md` (en la raíz del vault) es el contrato entre esta sesión de Claude y la sesión del cluster. La sesión del cluster lo lee para saber:
- Qué proyectos están activos y cuáles son sus repos en el cluster
- Exactamente dónde depositar notas (`00-Inbox/cluster/`)
- El frontmatter mínimo requerido
- Qué carpetas no tocar (`clases-particulares/`, `.obsidian/`)

**Para comunicar algo a la sesión del cluster** (feedback, instrucción, resultado de análisis), puedes dejar un archivo en:
```
00-Inbox/cluster/RESPUESTA_2026-04-08_descripcion.md
```
La sesión del cluster lo verá en su próximo `git pull`.

---

## 11. Índices de proyectos (`_indice.md`)

Cada proyecto tiene un `_indice.md` que actúa como **hub central**. El script lo actualiza automáticamente al procesar sesiones, pero tú también puedes editarlo manualmente para:
- Cambiar la `fase` actual
- Agregar literatura clave (`[[nombre-del-paper]]`)
- Registrar decisiones importantes
- Cambiar `estado: activo` → `estado: terminado` cuando finalice

| Índice | Ruta |
|---|---|
| P01 — Bilayer | `10-Proyectos/P01-Bilayer-Paper/_indice.md` |
| P02 — Fondecyt | `10-Proyectos/P02-Fondecyt-PMMA/_indice.md` |

---

## 12. Cheatsheet de comandos

### Local
```bash
# Procesar inbox manualmente
python3 ~/Documentos/GitHub/cerebro/90-Meta/automatizacion/procesar_inbox.py

# Ver qué hay en el inbox
ls ~/Documentos/GitHub/cerebro/00-Inbox/cluster/
ls ~/Documentos/GitHub/cerebro/00-Inbox/personal/

# Estado del vault en git
cd ~/Documentos/GitHub/cerebro && git status
```

### Cluster (`~/cerebro-vault/`)
```bash
# Actualizar el vault local del cluster
cd ~/cerebro-vault && git pull

# Depositar una nota nueva
cp ~/cerebro-vault/90-Meta/plantillas/sesion-cluster.md \
   ~/cerebro-vault/00-Inbox/cluster/$(date +%Y-%m-%d)_cluster_DESCRIPCION.md
# ... editar el .md ...
cd ~/cerebro-vault
git add 00-Inbox/cluster/$(date +%Y-%m-%d)_cluster_DESCRIPCION.md
git commit -m "cluster: sesion $(date +%Y-%m-%d) DESCRIPCION"
git push origin main
```
