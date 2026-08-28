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
