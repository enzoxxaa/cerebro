---
tipo: clase
proyecto: seminario
fecha: 2026-08-26
clase: 3
nodos: [N5, N6, N7]
hebras: [metadinámica, termodinámica estadística]
modo: expositivo
estado: en curso
resumen: "Clase 3: las dos facturas de la metadinámica — la cinética destruida (y cuantificada) y las CVs elegidas; y la decisión de diseño que las paga"
tags:
  - seminario
  - clase
  - metadinamica
---

# 12 · Clase 3 — El precio

← [[00 MOC — Seminario VNAR]] · anterior: [[11 Clase 2 — Inventar la metadinámica]]

**Nodos:** `N5` (las CVs son una elección) · `N6` (la cinética muere) · `N7` (tirar la termo, quedarse las estructuras).

---

## 0 · Dos facturas pendientes

De la Clase 2 salimos con el paisaje aplanado y las barreras cruzadas $1.9\times10^{6}$ veces más rápido. Pero quedaron dos deudas, y **las dos son ataques**:

| Factura | Qué se rompió | Nodo |
|---|---|---|
| **1** | Los **tiempos** de la trayectoria sesgada no son físicos | `N6` |
| **2** | Elegimos unas CVs; **todo lo ortogonal quedó sin muestrear** | `N5` |

La 2 ya la viste en versión mecánica ([[11 Clase 2 — Inventar la metadinámica#3 bis|Clase 2 §3 bis]]: el 99.7 % de los átomos no recibió fuerza). Aquí la cuantificamos, y luego vemos cómo el paper paga ambas.

---

## 1 · Factura 1 — la cinética, y por qué es peor de lo que parece

### 1.1 · El cálculo básico

Sin sesgo, el tiempo de escape de un pozo es

$$
\tau \;=\; \frac{1}{\kappa}\,\frac{h}{k_BT}\; e^{+\beta\Delta G^{\ddagger}}
$$

Con well-tempered convergida, la barrera efectiva es $\Delta G^{\ddagger}/\gamma$ ([[11 Clase 2 — Inventar la metadinámica#4.5|Clase 2 §4.5]]), así que

$$
\tau_V \;=\; \frac{1}{\kappa}\,\frac{h}{k_BT}\; e^{+\beta\Delta G^{\ddagger}/\gamma}
$$

El **factor de aceleración** es el cociente. Dividiendo, el prefactor se cancela y las exponenciales se restan:

$$
\alpha \;\equiv\; \frac{\tau}{\tau_V} \;=\; \exp\!\left[\beta\Delta G^{\ddagger} - \frac{\beta\Delta G^{\ddagger}}{\gamma}\right] \;=\; \boxed{\;e^{\,\beta\Delta G^{\ddagger}\frac{\gamma-1}{\gamma}}\;}
$$

### 1.2 · Y aquí está el problema: $\alpha$ **no es una constante**

Depende de $\Delta G^{\ddagger}$. Cada transición se acelera **por un factor distinto**. Con $\gamma = 10$, o sea $\frac{\gamma-1}{\gamma} = 0.9$:

| $\Delta G^{\ddagger}$ | $\beta\Delta G^{\ddagger}$ | $\alpha = e^{0.9\,\beta\Delta G^{\ddagger}}$ |
|---|---|---|
| 15 kJ/mol | 6.01 | $e^{5.41} \approx 2.2\times10^{2}$ |
| 25 kJ/mol | 10.02 | $e^{9.02} \approx 8.3\times10^{3}$ |
| 40 kJ/mol | 16.04 | $e^{14.4} \approx 1.8\times10^{6}$ |

**Las barreras altas se aceleran ocho mil veces más que las bajas.**

> [!danger] `N6` — no es que los tiempos estén mal escalados: es que están **reordenados**
> Si solo hubiera un factor global, bastaría multiplicar por él y listo. Pero como $\alpha$ depende de la barrera, **el orden relativo de los procesos se comprime**.

### 1.3 · Cuantificar la compresión

Toma dos transiciones $A$ y $B$. Sin sesgo:

$$
\frac{\tau_A}{\tau_B} \;=\; e^{\beta\left(\Delta G^{\ddagger}_A - \Delta G^{\ddagger}_B\right)}
$$

Con sesgo, cada barrera se divide por $\gamma$:

$$
\frac{\tau_A^V}{\tau_B^V} \;=\; e^{\beta\left(\Delta G^{\ddagger}_A - \Delta G^{\ddagger}_B\right)/\gamma}
\;=\; \left[e^{\beta\left(\Delta G^{\ddagger}_A - \Delta G^{\ddagger}_B\right)}\right]^{1/\gamma}
$$

$$
\boxed{\;\frac{\tau_A^V}{\tau_B^V} \;=\; \left(\frac{\tau_A}{\tau_B}\right)^{1/\gamma}\;}
$$

> [!success] Mira la simetría con la Clase 2
> $$\text{poblaciones:}\quad p_V \;=\; p_{\text{eq}}^{\,1/\gamma}
> \qquad\qquad
> \text{tiempos:}\quad \frac{\tau_A^V}{\tau_B^V} \;=\; \left(\frac{\tau_A}{\tau_B}\right)^{1/\gamma}$$
> **El mismo exponente $1/\gamma$ comprime las dos cosas.** No es coincidencia: ambas son consecuencia de que el sesgo reescala el paisaje por $\gamma$. Una sola idea, dos manifestaciones.

---

> [!question] **Q1 · N6** — En el sistema real, la transición $A$ tarda **23 000 veces más** que la $B$. Corres well-tempered con $\gamma = 10$. En la trayectoria sesgada, ¿cuántas veces más tarda $A$ que $B$?
>
> **a)** $\approx 2.7$ veces
> **b)** $\approx 230$ veces
> **c)** $\approx 2300$ veces
> **d)** $\approx 23\,000$ veces — el cociente no cambia

> [!success]- Respuesta Q1 → **a) $\approx 2.7$ veces** ✓
> El cociente **se eleva a $1/\gamma$**, no se divide por $\gamma$:
> $$(23\,000)^{1/10}: \quad \ln 23\,000 = 10.04 \;\to\; \frac{10.04}{10} = 1.004 \;\to\; e^{1.004} = 2.7$$
>
> **Cuatro órdenes de magnitud reducidos a un factor 2.7.** Prácticamente indistinguibles.
>
> La opción **(c) 2300** era el error diagnóstico: dividir por $\gamma$ en vez de elevar a $1/\gamma$. El origen de la forma correcta: **$\gamma$ divide la barrera, y la barrera vive en el exponente.** Dividir en el exponente $=$ tomar la raíz $\gamma$-ésima fuera.
>
> > [!danger] La consecuencia que importa
> > La metadinámica no solo hace los tiempos **incorrectos**: los hace **indistinguibles**. Aplasta cuatro órdenes de magnitud a un factor 3.
> > Y esto **no es un efecto secundario, es el mecanismo**: la metadinámica funciona *porque* borra la separación de escalas temporales. Es literalmente su objetivo.

---

## 2 · ¿Se puede recuperar la cinética? Sí — pero no así

Sería deshonesto decir «el sesgo mata la cinética, fin». **Existe** un método para recuperarla, y hay que conocerlo porque es una pregunta probable en la lab meeting.

> [!quote] Tiwary P, Parrinello M. **From metadynamics to dynamics.** *Phys. Rev. Lett.* **111**:230602 (2013). [DOI](https://doi.org/10.1103/PhysRevLett.111.230602) · PMID 24476246 · **353 citas**
> *«Here we extend its scope by introducing a simple yet powerful method for calculating the rates of transition between different metastable states. The method does not rely on a previous knowledge of the transition states or reaction coordinates, as long as collective variables are known that can distinguish between the various stable minima… we demonstrate that our method recovers the correct escape rates out of these stable states and also **preserves the correct sequence of state-to-state transitions**.»*

### La idea: *infrequent metadynamics*

Si el sesgo se deposita **tan raramente** que casi no se acumula en la región del estado de transición, entonces el sistema sigue cruzando por el cuello de botella verdadero, y el tiempo real se recupera con un **factor de aceleración medido**:

$$
\alpha \;=\; \left\langle e^{\,\beta V(s,t)}\right\rangle_{\text{sesgada}}
\qquad\Longrightarrow\qquad
\tau_{\text{real}} \;=\; \alpha \cdot t_{\text{simulado}}
$$

En vez de *predecir* la aceleración a partir de $\gamma$, se **mide** promediando el sesgo que el sistema fue sintiendo.

### Por qué el paper no puede usarlo

Requiere un régimen **opuesto** al que corrieron:

| Requisito de *infrequent metaD* | Lo que hace el paper |
|---|---|
| Deposición **muy espaciada**, para no contaminar el estado de transición | cada **2 ps** — 500 000 gaussianas en 1 µs |
| Sesgo **casi nulo** en la barrera | el objetivo explícito es **rellenarlo todo** |
| Muchos eventos de escape independientes, validados con test de Poisson | una sola trayectoria continua |

> [!note] Esto **no** es un error del paper — es una elección de régimen
> Hay dos modos de usar metadinámica, y son incompatibles:
>
> | Modo | Objetivo | Deposición | ¿Da cinética? |
> |---|---|---|---|
> | **Exploración** ← el paper | barrer el paisaje, generar estructuras | rápida | **no** |
> | **Cinético** (*infrequent*) | medir tasas | lenta | sí |
>
> El paper eligió **exploración**, que es lo correcto para su objetivo. Pero esa elección **crea una obligación**: si quieres cinética, tienes que sacarla de otro sitio.
> **Ese «otro sitio» es el MSM.** La necesidad del MSM no es estética: es la factura de esta decisión.

---

## 3 · Factura 2 — las CVs, y el problema que no se ve

### 3.1 · El mecanismo, ya lo tienes

De [[11 Clase 2 — Inventar la metadinámica#3 bis|Clase 2 §3 bis]]: el sesgo es **constante sobre cada rebanada** $\Sigma_s$, luego no empuja en ninguna dirección **dentro** de la rebanada. Un grado de libertad lento ortogonal a $\xi$ recibe **ayuda cero**.

### 3.2 · La consecuencia sobre $F(s)$

Toda la derivación de la Clase 2 supuso implícitamente algo que nunca dijimos en voz alta:

> [!important] La suposición oculta
> Que **todo lo ortogonal a $\xi$ se equilibra rápido**, en la escala de tiempo de la metadinámica.

Si eso falla, la marginal $p(s)$ que mides **no** es la marginal de equilibrio: dentro de cada rebanada el sistema se quedó atrapado en el subestado donde entró. Es **exactamente la patología de la Clase 1** —$\hat F = F - RT\ln(w_i/\pi_i)$— pero ahora **dentro** de cada valor de la CV, en vez de entre cuencas.

### 3.3 · Cómo se detecta: histéresis

La señal es que **el resultado depende de la historia**. Dos réplicas independientes, o dos mitades de la misma trayectoria, convergen a $F(s)$ **distintos** — porque cada una quedó atrapada en un subestado ortogonal diferente.

Ésa es *la* prueba estándar de convergencia de una metadinámica, y es barata: correr dos veces.

> [!danger] Y aquí está el agujero concreto en el paper
> **Una sola metadinámica de 1 µs por sistema. Sin réplicas. Sin test de histéresis. Sin curva de convergencia del sesgo.**
> No es que el resultado sea incorrecto — es que **no hay ninguna forma de saberlo**. El diagnóstico no se hizo.
>
> Es cierto que, como veremos en §4, el paper **no usa** el $F(s)$ de la metadinámica, lo cual quita fuerza a esta crítica. Pero no la elimina: si un grado de libertad ortogonal está atrapado, entonces **las estructuras generadas tampoco cubren el espacio**, y eso sí contamina todo lo que viene después.

---

> [!question] **Q2 · N5** — El paper corrió **una sola** metadinámica de 1 µs por sistema, sin réplicas. ¿Cuál es la consecuencia metodológica?
>
> **a)** No hay forma de detectar histéresis, que es la señal de un grado de libertad lento omitido de las CVs
> **b)** El sesgo no puede converger si solo hay una trayectoria
> **c)** El factor $\gamma$ deja de ser aplicable con una sola réplica
> **d)** No se puede calcular la barrera efectiva $F/\gamma$

> [!success]- Respuesta Q2 → **a) No hay forma de detectar histéresis** ✓
> Es *la* prueba estándar de convergencia en metadinámica, y es barata: corres dos veces y comparas.
>
> **Fíjate en la forma exacta de la crítica**, que es la que hay que usar en la charla: no es *«el resultado está mal»*, es ***«no hay manera de saber si está bien»***. Mucho más difícil de contestar, porque es cierto por construcción.
>
> Sobre **(b)**: el sesgo **sí** converge con una sola trayectoria — es lo normal, y es lo que garantiza well-tempered. Una réplica basta para **converger**; hacen falta dos para **verificar** que convergió. Esa distinción es el núcleo de la pregunta.

---

## 4 · `N7` — La decisión que paga las dos facturas

### 4.1 · El balance

Pon sobre la mesa lo que la metadinámica te ofrece y en qué estado está cada cosa:

| Producto | Estado | Por qué |
|---|---|---|
| **Energía libre $F(s)$** | ⚠️ solo **proyectada** en las CVs, y sin verificar convergencia | §3 |
| **Cinética** | ❌ **destruida**, y de forma no uniforme | §1 |
| **Conjunto de estructuras** | ✅ **diverso y útil** | es lo que la metadinámica hace bien |

### 4.2 · El movimiento

> [!success] `N7` — la jugada central del pipeline
> **Tirar $F(s)$. Tirar la cinética. Quedarse solo con las estructuras.**
>
> La metadinámica pasa de ser un método de medida a ser un **generador de conformaciones diversas**. Nada más.

### 4.3 · Por qué esto es inteligente y no una renuncia

Porque **desactiva las dos facturas de golpe**:

| Factura | ¿Sigue doliendo? |
|---|---|
| **1 · Cinética destruida** | ❌ Da igual — no vamos a usar esos tiempos |
| **2 · $F$ mal proyectada / sin convergencia verificada** | ❌ Da igual — no vamos a usar esa $F$ |

Y sobre todo: **la convergencia deja de ser un requisito.** No necesitas que la metadinámica converja; solo necesitas que **haya pasado por sitios variados**. Es un listón infinitamente más bajo.

Eso no es una racionalización *a posteriori* — es el argumento explícito de la referencia metodológica que el paper cita:

> [!quote] Biswas M, Lickert B, Stock G. *Metadynamics Enhanced Markov Modeling of Protein Dynamics.* **J. Phys. Chem. B** 122:5508 (2018) · **50 citas** · ref. 68 del paper
> *«To obtain well-distributed initial structures for the short trajectories, it is proposed to employ metadynamics MD, which quickly sweeps through the entire free energy landscape of interest. **Being only used to generate initial conformations, the implementation of metadynamics can be simple and fast.**»*

> [!tip] Munición defensiva — guárdate esto para la charla
> Si alguien ataca con *«vuestra metadinámica no está convergida»*, la respuesta es que **no necesita estarlo**, y está publicado. Ese ataque no funciona contra este diseño.
> Lo cual te dice también dónde **sí** hay que atacar: no en la convergencia, sino en **qué se hereda**.

### 4.4 · Lo que sí se hereda

Tirar $F$ y la cinética no te deja con las manos limpias. Del conjunto de estructuras heredas **una cosa**, y es justo la peligrosa:

$$
\text{clustering a 1.3 Å} \;\longrightarrow\; \text{semillas} \;\longrightarrow\; \text{los pesos } w_i
$$

Y de la Clase 1 §3.5 ya sabes exactamente qué hacen esos pesos:

$$
\hat F(s) \;=\; F(s) \;-\; RT\ln\frac{w_i}{\pi_i}
$$

> [!danger] El balance final del pipeline hasta aquí
> **Facturas pagadas:** cinética destruida ✅ · $F$ mal proyectada ✅ — ambas descartadas por diseño.
> **Factura que queda viva:** los pesos de siembra $w_i \ne \pi_i$.
>
> **Y ésa es exactamente, y únicamente, la que el MSM está diseñado para pagar.**
>
> Ahí está la elegancia del pipeline, y conviene poder enunciarla así en una frase:
> > *Usa la metadinámica para lo único que hace de forma robusta —encontrar estructuras diversas— y repara con el MSM lo único que eso rompe: los pesos.*

### 4.5 · Pero el problema de las CVs **sobrevive**

Cuidado con sobreextender el argumento de §4.3. Tirar $F$ elimina la factura *termodinámica* de las CVs, pero **no** la estructural:

$$
\text{CVs} \;\to\; \text{qué regiones se visitan} \;\to\; \text{qué estructuras existen} \;\to\; \text{qué semillas hay}
$$

**Un MSM solo puede reponderar los estados que alguien visitó.** Si HV2 nunca se sesgó y sus estados lentos no se visitaron, **no hay $\pi_i$ que los rescate: sencillamente no están en el modelo.**

> [!important] Por qué A2 es el ataque más fuerte
> Todas las demás críticas apuntan a números que podrían recalcularse mejor. **A2 apunta a estados que no existen en los datos.** Ningún análisis posterior arregla un estado que nunca se muestreó.

---

> [!question] **Q3 · N7** — ¿Cuál es la consecuencia más importante de usar la metadinámica **solo** como generador de estructuras?
>
> **a)** Que la convergencia de la metadinámica deja de ser un requisito
> **b)** Que el valor de $\gamma$ deja de importar y podría usarse cualquiera
> **c)** Que la elección de CVs deja de condicionar el resultado
> **d)** Que la cinética se puede recuperar del sesgo acumulado
