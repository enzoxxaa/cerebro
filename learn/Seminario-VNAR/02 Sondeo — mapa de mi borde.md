---
tipo: sondeo
proyecto: seminario
fecha: 2026-08-26
resumen: "Registro del sondeo diagnóstico: dónde está el borde de mi conocimiento en cada hebra"
tags:
  - seminario
  - sondeo
---

# 02 · Sondeo — mapa de mi borde

← [[00 MOC — Seminario VNAR]] · [[01 Plan de aprendizaje]]

> [!abstract] Para qué sirve esta nota
> No se puede enseñar en la zona de desarrollo próximo sin saber dónde están sus bordes. Un borde está **localizado** solo cuando está **acotado por los dos lados**: algo de ese nivel que aciertas (**suelo**) y algo que falla o no sabes (**techo**). El borde vive entre los dos.
> Todo acertado **no** significa "listo" — significa que las preguntas eran fáciles. Aquí se registra el resultado y se actualiza a medida que avanzamos.

## Estado

🔴 **Sin empezar.** El primer quiz (well-tempered → $P(s)^{1/\gamma}$) fue cancelado, así que no hay ni un dato.

| Hebra                         | Suelo (lo que sí) | Techo (donde se acaba) | Estado |
| ----------------------------- | ----------------- | ---------------------- | ------ |
| **MD clásica**                | —                 | —                      | 🔴     |
| **Termodinámica estadística** | —                 | —                      | 🔴     |
| **Metadinámica**              | —                 | —                      | 🔴     |
| **tICA / MSM**                | —                 | —                      | 🔴     |
| **Inmunología estructural**   | —                 | —                      | 🔴     |

**Conjetura de partida** (a corregir, no a asumir): P01 en el vault es MD de bicapas con GROMACS/AMBER/VMD → **MD clásica probablemente sólida**. Metadinámica a nivel de "sé qué hace, no los detalles". tICA/MSM más flojo. Termo estadística funcional. Inmunología estructural nueva.

---

## Estrategia: búsqueda binaria

- Aciertas → **subo la dificultad de golpe**, no de a poquito. Inchar es perder tiempo.
- Fallas → el borde queda acotado por arriba, y **estrecho** para fijar dónde está exactamente.
- Un fallo **no** es señal de empezar a enseñar: primero hay que caracterizarlo. ¿Descuido, hueco aislado, o **concepción errónea sistemática**? Las últimas hay que desalojarlas, no rellenarlas.

---

## Preguntas preparadas

Están aquí para que veas el nivel al que apunto. **No las respondas leyendo** — pierden todo su valor diagnóstico. El punto es que si algo aquí ya te parece trivial, dímelo y subo el listón antes de empezar.

### Hebra: MD clásica
Empiezo **alto**, asumiendo que la dominas.

| # | Nivel | Sobre qué |
|---|---|---|
| MD-1 | alto | Qué hace SHAKE y por qué habilita un paso de 2 fs — y qué te impide subir a 4 fs |
| MD-2 | alto | Berendsen vs Langevin: cuál muestrea un ensemble correcto y cuál no |
| MD-3 | muy alto | Neutralizar con **carga de fondo uniforme** vs contraiones explícitos: qué se rompe |
| MD-4 | muy alto | Por qué TIP3P sesga **tiempos** de transición y en qué dirección |

### Hebra: Termodinámica estadística
Es la hebra que **más carga** el paper, y la que más se suele dar por sabida.

| # | Nivel | Sobre qué |
|---|---|---|
| TE-1 | medio | Cuánto vale $RT$ a 300 K, y qué población relativa implica una barrera de 20 kJ/mol |
| TE-2 | alto | Diferencia entre **energía libre** y **energía potencial** en un perfil proyectado |
| TE-3 | alto | Qué significa que una proyección sobre una CV tenga un grado de libertad lento **ortogonal** |
| TE-4 | muy alto | Por qué $-k_BT\ln P$ de un histograma de trayectorias sembradas **no** es una energía libre |

> TE-4 es el corazón de [[22 Superficie de ataque#🟠 A6 — ¿Las "superficies de energía libre" de la Fig. 3A están reponderadas?|A6]]. Si lo tienes, la crítica más sofisticada del paper te sale sola.

### Hebra: Metadinámica

| # | Nivel | Sobre qué |
|---|---|---|
| MT-1 | medio | Qué hace el sesgo acumulado y por qué la metadinámica **estándar** no converge |
| MT-2 | alto | Qué distribución muestrea WT-metaD convergida *(el quiz cancelado)* |
| MT-3 | alto | Qué significa $\gamma = 10$ a 300 K en Kelvin y en kJ/mol de barrera efectiva |
| MT-4 | muy alto | Cómo se recupera $F(s)$ del sesgo, y por qué solo vale **proyectado en las CVs** |

### Hebra: tICA / MSM
Sospecho que aquí está el borde más bajo, y es la hebra que más peso tiene en las críticas.

| # | Nivel | Sobre qué |
|---|---|---|
| MS-1 | bajo-medio | Qué es un lag time y qué se supone que hace un MSM |
| MS-2 | medio | Qué optimiza tICA — y por qué no es lo mismo que PCA |
| MS-3 | alto | De dónde sale $\pi$, y por qué **no** depende de dónde empezaron las trayectorias |
| MS-4 | alto | Qué comprueba el test de Chapman–Kolmogorov, y qué lo hace fallar |
| MS-5 | muy alto | Por qué trayectorias de 100 ns con lag de 15 ns es un margen problemático |

> MS-3 es el nodo **N9** del [[01 Plan de aprendizaje#2. Mapa de dependencias|mapa]]. Es la pieza que hace legítimo todo el pipeline: si no está firme, no hay defensa posible.

### Hebra: Inmunología estructural

| # | Nivel | Sobre qué |
|---|---|---|
| IN-1 | bajo | Qué es un CDR y qué es un paratopo |
| IN-2 | medio | Qué le falta a un VNAR que sí tiene un VHH — y con qué lo compensa |
| IN-3 | alto | Qué es **selección conformacional** frente a ajuste inducido, y por qué el marco elegido decide qué observable importa |

> IN-3 no es trivia: **es el motivo de que la pregunta "¿cuál es la población de cada estado?" sea *la* pregunta del paper** y no un detalle técnico.

---

## Registro de respuestas

*(se rellena a medida que avanzamos)*

| Fecha | Pregunta | Respuesta | ✓/✗ | Qué revela |
|---|---|---|---|---|
| 2026-08-26 | MT-2 | *cancelada* | — | — |
