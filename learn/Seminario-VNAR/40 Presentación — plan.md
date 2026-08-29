---
tipo: plan
proyecto: seminario
fecha: 2026-08-29
resumen: "Plan de la presentación LaTeX/Beamer «Inventando la metadinámica» — mapeo de las Clases 0-3 a estructura de charla, con ecuaciones y figuras clave"
tags:
  - seminario
  - presentacion
  - latex
---

# 40 · Presentación — plan

← [[00 MOC — Seminario VNAR]]

> [!warning] Alcance de esta nota
> Cubre **solo lo dado en clase hasta ahora**: Clase 0 (VNAR), Clase 1 (el pivote), Clase 2 (inventar la metadinámica), Clase 3 (el precio). **Nada de tICA/MSM/munición** — eso es Clases 4-6, aún no impartidas. Cuando se den, esta nota se extiende.

> [!info] Entorno verificado
> `pdflatex`, `xelatex`, `lualatex`, `latexmk`, `beamer.cls`, `tikz.sty` — todo instalado (TeX Live 2026, Arch). Sin bloqueos para compilar.

---

## Título y tesis

**«Inventando la metadinámica»**
*Metodología de Fernández-Quintero et al. 2022 (Liedl) — humanización de VNARs de tiburón*

La tesis narrativa: en vez de presentar la metadinámica como una caja negra que el paper usa, la charla **la reconstruye desde el problema que resuelve** — mismo orden que las clases (problema → solución → precio), no el orden cronológico del pipeline (metaD → cluster → MD). Eso es lo que hace que el título funcione literalmente: la audiencia no *escucha sobre* metadinámica, la *inventa* contigo.

---

## Estructura propuesta — 5 bloques

Cada bloque lista: **de qué clase sale** · **la idea que tiene que sobrevivir el viaje a una slide** · **ecuaciones candidatas** · **figura candidata**.

### Bloque 0 · El sistema (Clase 0)
**De dónde sale:** [[05 Clase 0 — El VNAR]]
**Idea:** un VNAR es el dominio de unión más pequeño que existe — 2 CDRs, no 6 — y aun así une con alta afinidad. Humanizar toca el framework, no las CDRs. Pregunta que deja abierta: *¿cómo se comprueba computacionalmente si eso cambió algo?*

| | |
|---|---|
| Figuras | `fig1-vnar-estructura.png` (CDR1/CDR3/HV2/HV4 marcados) · `fig2-alineamiento-hidrofobicidad.png` (motivo `RKN`, E06 vs DPK9) |
| Ecuaciones | ninguna — bloque puramente estructural |
| Duración estimada | 2-3 slides, ritmo rápido |

### Bloque 1 · El problema (Clase 1)
**De dónde sale:** [[10 Clase 1 — El problema y el pivote]]
**Idea:** las poblaciones son pesos de Boltzmann; las barreras de los lazos CDR (~25-45 kJ/mol) están fuera del alcance de 100 ns de MD (~22 kJ/mol). El titular «92 %→16 %» son en realidad ~10 kJ/mol — comparables al error del campo de fuerza.

| | |
|---|---|
| Figuras | `fig4-msm-poblaciones.png` (92.6 % / 7.4 % de E06 — ojo: viene del MSM, se usa aquí solo como *resultado a explicar*, no se explica el MSM) |
| Ecuaciones clave | $\dfrac{P_A}{P_B}=e^{-\beta\Delta G}$ · $RT\approx2.5$ kJ/mol · $k=\kappa\frac{k_BT}{h}e^{-\beta\Delta G^\ddagger}$ |
| Ecuación opcional (backup) | $\hat F(s)=F(s)-RT\ln\frac{w_i}{\pi_i}$ — la demolición de M3; potente pero densa para slide principal |
| Duración estimada | 3-4 slides |

### Bloque 2 · Inventar la metadinámica (Clase 2) — **el corazón de la charla**
**De dónde sale:** [[11 Clase 2 — Inventar la metadinámica]]
**Idea:** no se puede calentar globalmente (destruye la proteína, cuesta reponderar) ni esperar. La única palanca limpia es sesgar el potencial **sobre la CV**. El sesgo óptimo es un molde negativo de $F$ — pero calcularlo requiere conocer $F$. La metadinámica resuelve ese huevo-y-gallina depositando sesgo adaptativo. Sin freno, no converge (*overfilling*); *well-tempered* introduce el freno con $\gamma$.

| | |
|---|---|
| Figuras | diagrama propio de «arena llenando un pozo» (no existe — candidato para TikZ/mermaid, ver preguntas de diseño) |
| Ecuaciones clave | $F_V(s)=F(s)+V(s)$ · $V^{\text{ideal}}=-F$ · $\dfrac{\partial V}{\partial t}\propto e^{-\beta[F+V]}$ · $V\to-\frac{\gamma-1}{\gamma}F$ · $F_V=F/\gamma$ |
| Números del paper | $\gamma=10$, altura 10 kJ/mol, ancho 0.3 rad, cada 2 ps, 1 µs · barrera 40→4 kJ/mol, aceleración $\approx1.9\times10^6$ |
| Duración estimada | 5-6 slides — es el bloque con más peso |

### Bloque 3 · El precio (Clase 3)
**De dónde sale:** [[12 Clase 3 — El precio]]
**Idea:** el sesgo comprime la cinética de forma **no uniforme** ($\alpha=e^{\beta\Delta G^\ddagger(\gamma-1)/\gamma}$) — cuatro órdenes de magnitud de separación temporal quedan en un factor 3. Y solo empuja sobre las CVs elegidas: todo lo ortogonal (ej. HV2) queda sin ayuda. La jugada del pipeline: **tirar $F$ y la cinética, quedarse solo con las estructuras** — eso desactiva ambas facturas de golpe, a costa de heredar un problema distinto (los pesos de siembra).

| | |
|---|---|
| Figuras | ninguna nueva — se apoya en la lógica, no en datos |
| Ecuaciones clave | $\alpha=e^{\beta\Delta G^\ddagger\frac{\gamma-1}{\gamma}}$ · $\dfrac{\tau_A^V}{\tau_B^V}=\left(\dfrac{\tau_A}{\tau_B}\right)^{1/\gamma}$ |
| Cita | Biswas, Lickert & Stock (2018) — «being only used to generate initial conformations…» |
| Duración estimada | 3-4 slides |

### Cierre — gancho, no resolución
Termina en el punto exacto donde el material actual se detiene: **tenemos estructuras diversas, no todavía las poblaciones correctas.** Un slide de «lo que viene» (MD sembrada → MSM) sin desarrollarlo — dejarlo como pregunta abierta es coherente con el propio arco narrativo del curso y evita prometer contenido que aún no está enseñado.

---

## El hilo narrativo en una frase por bloque

1. *Este bicho diminuto une con alta afinidad — ¿cambió su ensemble al humanizarlo?*
2. *No se puede medir eso con MD directa: las barreras son demasiado altas.*
3. *Entonces… inventemos la metadinámica.* ← título de la charla, clímax del argumento
4. *Pero ese arreglo tiene una factura — y el pipeline la paga tirando lo que no necesita.*
5. *(gancho) Quedan estructuras sin pesos correctos. Eso es la próxima pieza.*

---

## ✅ Decisiones de diseño

| Pregunta | Decisión |
|---|---|
| Formato | **Ambos** — `slides.tex` (Beamer, para presentar) + `handout.tex` (article, derivaciones completas de respaldo) |
| Duración | **Media** — 20-25 min, ~18-22 slides |
| Figuras conceptuales | **Subagente `svg-maker` primero** (function plots, coordenadas exactas); **fallback a TikZ propio** si falla por cuota |

## Estructura de archivos

```
Seminario-VNAR/presentacion/
├── macros.tex        — comandos compartidos (\Delta G, \RT, \kB…)
├── slides.tex        — Beamer, tema sobrio propio
├── handout.tex       — article, derivaciones completas
├── figs/              — diagramas conceptuales nuevos (svg-maker / TikZ)
└── build.sh          — compila ambos con latexmk
```
Figuras del paper: referenciadas directo desde `../assets/` (sin duplicar).

## Bitácora del diagrama conceptual (Bloque 2)

- ❌ **`svg-maker` falló** — mismo `400 out of extra usage` que Scout. Cupo de suscripción agotado también para subagentes en este momento.
- ✅ **TikZ a mano en `figs/molde-negativo.tex`** — 3 paneles (paisaje real → sesgo acumulándose con forma invertida → efecto neto plano), compilado y **verificado visualmente** antes de incrustarlo, mismo estándar de «nunca publicar sin mirar» que sigue `svg-maker`. Reutilizado en ambos documentos viá `\input`.

## ✅ Estado final — ambos documentos compilan limpio

| Archivo | Qué es | Páginas | Estado |
|---|---|---|---|
| `presentacion/slides.tex` | Beamer 16:9, tema sobrio propio (sin símbolos de navegación, paleta azul/naranja) | **19** | ✅ compila sin errores |
| `presentacion/handout.tex` | Article, derivaciones completas con índice, cajas de resultado/aviso | **5** | ✅ compila sin errores, 0 overfull hbox |
| `presentacion/figs/molde-negativo.tex` | Diagrama TikZ de 3 paneles, reutilizado en ambos | — | ✅ verificado visualmente |
| `presentacion/build.sh` | Compila los dos con 2 pasadas + limpia auxiliares | — | ✅ probado |

**Cobertura exacta:** Bloque 0 (VNAR) · Bloque 1 (el problema, Boltzmann + TST) · Bloque 2 (inventar la metadinámica — el núcleo, con el diagrama del molde negativo) · Bloque 3 (el precio — cinética comprimida, CVs como elección, la jugada de tirar $F$). **Cierra en gancho**, sin entrar a tICA/MSM — tal como se pidió.

> [!warning] Pendiente de pulido menor
> El slide «El resultado que hay que poder explicar» usa `fig4-msm-poblaciones.png` completa (4 paneles A-D), pero el texto solo discute E06 y v1.1. Se ve un poco denso a tamaño de proyección. Mejora fácil pendiente: recortar la figura a solo los paneles A y B antes de la charla.
