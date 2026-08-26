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

✅ **SONDEO CERRADO.** 7 preguntas respondidas: 2 aciertos, 2 fallos con misconcepción, 3 «no lo sé». El borde está localizado en las cinco hebras.

| Hebra                         | Suelo (lo que sí)                                       | Techo (donde se acaba)                                             | Estado                       |
| ----------------------------- | ------------------------------------------------------- | ------------------------------------------------------------------ | ---------------------------- |
| **MD clásica**                | **ensembles y barostatos** — Berendsen vs NpT, correcto  | no se alcanzó                                                       | 🟢 **sólido — es la base**   |
| **Inmunología estructural**   | **selección conformacional**, y por qué implica poblaciones | **anatomía del VNAR sin sondear** — CDR2 ausente, HV2/HV4          | 🟡 marco sí, anatomía por ver |
| **Termodinámica estadística** | Boltzmann como fórmula                                   | **$-k_BT\ln P$ de datos sesgados** — cree que sigue siendo $F$      | 🟠 misconcepción localizada  |
| **Metadinámica**              | ninguno — falla en el mecanismo base                     | cree que **sube la temperatura** — confunde con REMD                | 🔵 **construir desde cero**  |
| **tICA / MSM**                | ninguno — por debajo de «qué estima un MSM»              | no hubo ningún acierto                                              | 🔵 **construir desde cero**  |

> [!success] EL DIAGNÓSTICO — una sola línea de fractura explica las 7 respuestas
> No es «sabe unas cosas y otras no» de forma dispersa. Hay **un corte limpio**, y cae en el mismo sitio cada vez:
>
> | ✅ Tiene | ❌ No tiene |
> |---|---|
> | Cómo se **produce** una trayectoria correcta | Qué se puede **inferir** de un conjunto de trayectorias |
> | Termostatos, barostatos, ensembles, restricciones | Sesgo adaptativo, estimadores, lag times, reponderación |
> | La **física** de la simulación | La **estadística** del muestreo |
> | La **pregunta biológica** — selección conformacional | El **puente** entre ambas |
>
> Tienes los dos extremos firmes y **el centro vacío**. Y el centro vacío es, exactamente, la metodología de este paper.
>
> **Por qué esto es la mejor posición posible para aprender esto:** no hay que convencerte de la física (la sabes) ni de por qué importa la biología (la sabes). Solo hay que tender el puente — y va a quedar anclado en roca por los dos lados.
>
> **Y por qué es la mejor posición para criticarlo:** A1, A3, A4 y A6 son **todos** errores de inferencia, no de física. Cuando la capa esté instalada, no habrá que memorizar las críticas: van a resultar obvias.

### Las tres misconcepciones a desalojar

Un hueco se rellena; una creencia equivocada hay que **demolerla primero**, o el conocimiento nuevo se apila encima y no se sostiene. Salieron tres, y cada una bloquea una parte del paper:

| # | Creencia actual | Qué bloquea |
|---|---|---|
| **M1** | «metadinámica = subir la temperatura» | Sin *sesgo adaptativo* no se entiende por qué el sesgo **mide** $F$, ni por qué existe *well-tempered*, ni por qué hay que **elegir CVs** — y ahí vive el ataque A2 |
| **M2** | «$\tau$ es el tiempo de residencia del sistema» | Si $\tau$ fuese físico **no habría nada que validar**: adiós al test de Chapman–Kolmogorov y al ataque A4 |
| **M3** | «$-k_BT\ln P$ es la energía libre» | Es el nodo pivote: sin él, ni el MSM parece necesario ni el ataque A6 es visible |

> [!important] Lectura de la hebra tICA/MSM
> Tres preguntas, **cero aciertos**, bajando en dificultad cada vez. No se encontró suelo ni siquiera en la pregunta más básica (*¿qué estima un MSM?*). La hebra **no tiene borde que localizar: empieza en cero.**
>
> Dos matices que sí importan para cómo enseñar:
> 1. **Dos de tres fueron «no lo sé»**, no respuestas equivocadas. Es un **hueco limpio**: no hay modelo erróneo que desalojar, solo terreno vacío donde construir. Eso es mucho más fácil de enseñar que una convicción equivocada.
> 2. **La única respuesta arriesgada sí reveló una misconcepción concreta** y hay que atacarla explícitamente → ver abajo.
>
> **Consecuencia para el [[01 Plan de aprendizaje|plan]]:** las clases 4 y 5 no pueden ser un repaso. Tienen que construir el MSM desde su definición, y hay que añadir una clase previa de tICA. El resto del plan se sostiene.

> [!danger] Misconcepción detectada — «el lag time es una propiedad del sistema»
> Al preguntar qué es $\tau$, eligió **«el tiempo medio que el sistema permanece en un estado»**. Eso no es un despiste: es tratar $\tau$ como algo que el sistema **tiene**, en lugar de un **parámetro que el analista elige**.
>
> Por qué hay que desalojarlo antes de seguir: si $\tau$ fuera una propiedad física, **no habría nada que validar**. No haría falta el test de Chapman–Kolmogorov, ni barrer el lag, ni preocuparse de que 100 ns / 15 ns ≈ 6.7. Toda la superficie de crítica del paper en esta hebra ([[22 Superficie de ataque#🟠 A4 — Trayectorias de 100 ns con un lag de 15 ns|A4]]) **es invisible desde esa creencia**.
> → La clase del MSM debe empezar por: *¿qué decide el analista y qué decide la física?*

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

| Fecha      | Pregunta                                  | Respuesta   | ✓/✗ | Qué revela                                                                                                                                                                                                                                      |
| ---------- | ----------------------------------------- | ----------- | --- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| 2026-08-26 | MT-2 · qué distribución muestrea WT-metaD | *cancelada* | —   | —                                                                                                                                                                                                                                               |
| 2026-08-26 | **MS-2 · qué maximiza tICA**              | «no lo sé»  | ⬜   | Hueco genuino, sin misconcepción. La distinción **tICA (lo lento) vs PCA (lo amplio)** no está instalada. Nodo **obligatorio**: el paper proyecta todos sus paisajes sobre tICs, así que sin esto la Fig. 3 no se puede leer ni criticar. |
| 2026-08-26 | **MS-1 · qué es el lag time $\tau$**       | «tiempo de residencia» | ✗ | **Misconcepción, no hueco.** Trata $\tau$ como propiedad del sistema y no como parámetro elegido. Hay que desalojarla explícitamente: sin ella no se ve por qué un MSM necesita validación. |
| 2026-08-26 | **MS-0 · qué estima un MSM**              | «no lo sé»  | ⬜   | Suelo no encontrado ni en la pregunta más básica de la hebra. Falta el nodo central: **todo sale de $T(\tau)$** — $\pi$ de su autovector, los tiempos de sus autovalores. Sin eso no hay defensa **ni** ataque posible. |
| 2026-08-26 | **MD-2 · Langevin + Berendsen, ¿cuál es la objeción?** | «Berendsen no reproduce las fluctuaciones de volumen del NpT» | ✓ | **Acierto en pregunta alta.** Distingue *media* de *fluctuación* en un ensemble, y sabe que Langevin sí preserva Boltzmann. **Este es el suelo firme del curso.** |
| 2026-08-26 | **TE-4 · ¿qué es $-k_BT\ln P$ de trayectorias sembradas?** | «la energía libre proyectada» | ✗ | **La misconcepción clave.** Cree que el histograma *es* $F$. No ve que $F=-k_BT\ln P$ exige que $P$ sea **de equilibrio**. Es exactamente el nodo del que dependen [[22 Superficie de ataque#🟠 A6\|A6]] y toda la justificación de por qué hace falta un MSM. |
| 2026-08-26 | **MT-3 · qué significa $\gamma = 10$** | «no lo sé» | ⬜ | Techo en metadinámica: los **parámetros** del método no están. Falta el nodo $V(s)\to-\frac{\gamma-1}{\gamma}F(s)$ y la barrera residual $F/\gamma$. Sin él no se entiende **por qué** esta etapa existe. |
| 2026-08-26 | **MT-1 · mecanismo de la metadinámica** | «aumenta la temperatura» | ✗ | **Segunda misconcepción, y en la base.** Confunde metadinámica con REMD/annealing. No está la idea de **sesgo adaptativo acumulado**. Hay que instalarla antes de cualquier parámetro. |
| 2026-08-26 | **IN-3 · qué afirma la selección conformacional** | «un confórmero ya poblado antes del ligando» | ✓ | **Acierto, y es el techo del curso.** Ya entiende por qué *la población del estado competente* es la medida de interés. **Ojo:** esto valida el *marco*, no la *anatomía del VNAR*, que quedó sin sondear — y el ataque A2 depende de ella. La Clase 0 se mantiene. |

---

## Sondeo cerrado

No hay más preguntas de diagnóstico. → [[01 Plan de aprendizaje]] (revisado con estos datos).
