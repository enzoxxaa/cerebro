# Instrucciones para Claude Code — Sesión del Cluster

Este archivo describe cómo la sesión de Claude Code del cluster universitario debe interactuar con este vault de Obsidian.

## Tu rol

Eres el lado del cluster del sistema de segundo cerebro. Tu función es **documentar el progreso de simulaciones y análisis** depositando notas en el inbox del vault. La sesión local de Claude Code en la máquina personal procesa y organiza esas notas.

## Proyectos activos

### P01 — Luminógenos en Bicapa TTAB/DeOH
- **Repo en cluster:** `~/aie-lc-bilayer/`
- **Luminógenos:** TTG, TTC, TTN, TTY, TTO
- **Estado:** Análisis final + escritura del paper
- **Índice en vault:** `10-Proyectos/P01-Bilayer-Paper/_indice.md`

### P02 — Fondecyt Iniciación: Concentrador Solar en PMMA
- **Estado:** Simulaciones iniciales
- **Índice en vault:** `10-Proyectos/P02-Fondecyt-PMMA/_indice.md`

## Cómo depositar una nota de sesión

### Paso 1: Crear el archivo

Nombre del archivo: `YYYY-MM-DD_cluster_descripcion-corta.md`

Ejemplos:
- `2026-04-08_cluster_equilibrado-bicapa-TTG.md`
- `2026-04-08_cluster_analisis-RDF-TTC.md`
- `2026-04-08_cluster_error-mdrun-PMMA.md`

### Paso 2: Frontmatter mínimo requerido

```yaml
---
tipo: sesion
proyecto: P01-Bilayer
fecha: YYYY-MM-DD
duracion-h: 2
actividad: simulacion
sistema: cluster
herramienta: GROMACS
resumen: "Descripción breve de lo que se hizo"
siguiente-paso: "Qué viene después"
tags:
  - sesion
  - investigacion
---
```

Valores válidos:
- `proyecto`: `P01-Bilayer` | `P02-Fondecyt`
- `actividad`: `simulacion` | `analisis` | `escritura` | `debug` | `reunion`
- `herramienta`: `GROMACS` | `AMBER` | `Python` | `VMD`

### Paso 3: Depositar y hacer push

```bash
# Desde ~/cerebro-vault/ (clon local del vault en el cluster)
git add 00-Inbox/cluster/YYYY-MM-DD_cluster_descripcion.md
git commit -m "cluster: sesion YYYY-MM-DD descripcion"
git push origin main
```

## Plantilla de sesión completa

Ver: `90-Meta/plantillas/sesion-cluster.md`

## Lo que NO debes tocar

- `20-Areas/clases-particulares/` — zona privada de tutorías, no relacionada con investigación
- `.obsidian/` — configuración local de Obsidian
- `40-Archivo/` — proyectos terminados, no modificar

## Clonar el vault en el cluster (primera vez)

```bash
git clone https://github.com/enzoxxaa/cerebro.git ~/cerebro-vault
cd ~/cerebro-vault
git config user.email "tu@email.com"
git config user.name "Enzo (cluster)"
```

## Lectura de respuestas

La sesión local puede dejar notas de respuesta en `00-Inbox/cluster/` con el prefijo `RESPUESTA_`. Si aparecen archivos con ese prefijo en tu próximo pull, léelos — pueden contener feedback, preguntas o indicaciones sobre las notas que depositaste.
