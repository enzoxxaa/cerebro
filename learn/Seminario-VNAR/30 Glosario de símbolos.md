---
tipo: intake
proyecto: general
fecha: 2026-08-27
resumen: "Glosario de toda la notación del seminario: qué es cada símbolo, de qué tipo es, y dónde apareció"
tags:
  - seminario
  - glosario
origen: personal
estado: sin-procesar
prioridad: media
etiquetas-sugeridas: []
resumen-breve: ""
---

# 30 · Glosario de símbolos

← [[00 MOC — Seminario VNAR]]

> [!tip] Cómo usarlo
> La columna **«Tipo»** es la más útil. La mayoría de la confusión con estas fórmulas no viene del álgebra: viene de perder de vista **si algo es un número, una función, o un vector de 90 000 componentes**. Si te pierdes en una ecuación, mira primero el tipo de cada pieza.

---

## ⭐ Los dos que hay que separar sí o sí

| Símbolo | Qué es | Tipo |
|---|---|---|
| $\mathbf{r}$ | **Una configuración completa** del sistema: las coordenadas $(x,y,z)$ de **todos** los átomos, a la vez | Vector de $3N$ números. Con $N \approx 30\,000$ átomos → **$\approx 90\,000$ números** |
| $s$ | **Un valor de la variable colectiva.** Por ejemplo «el ángulo $\psi$ del residuo 27 vale $-1.2$ rad» | **Un solo número** |

$$\mathbf{r} \in \mathbb{R}^{3N} \qquad\qquad s \in \mathbb{R}$$

> [!important] La relación entre los dos
> $$\xi:\;\mathbb{R}^{3N}\;\longrightarrow\;\mathbb{R}, \qquad \mathbf{r}\;\longmapsto\; s=\xi(\mathbf{r})$$
> $\xi$ (xi) es la **función** que aplasta 90 000 números en 1. Es **masivamente muchos-a-uno**: hay un número astronómico de configuraciones $\mathbf{r}$ distintas que dan **el mismo** $s$ — todas las posiciones posibles del agua, todas las vibraciones, todo el resto de la proteína.
>
> **Regla mnemotécnica:** $\mathbf{r}$ es el **mundo entero**. $s$ es **lo único que decidiste mirar**.

---

## Termodinámica

| Símbolo | Qué es | Tipo | Nota |
|---|---|---|---|
| $N$ | número de átomos | entero | $\sim 30\,000$ aquí |
| $T$ | temperatura | número | 300 K |
| $k_B$ | constante de Boltzmann | constante | $1.381\times10^{-23}$ J/K — **por partícula** |
| $R$ | constante de los gases | constante | $8.314$ J/(mol·K) — **por mol**. $R = N_A k_B$ |
| $\beta$ | «inversa de la temperatura» | número | $\beta \equiv 1/k_BT$. Aparece siempre como $\beta\times$energía, que es adimensional |
| $RT$ | escala térmica molar | número | **$2.494$ kJ/mol a 300 K** — la constante más usada del curso |
| $U(\mathbf{r})$ | **energía potencial** de una configuración | Función $\mathbb{R}^{3N}\to\mathbb{R}$ | Lo que calcula el campo de fuerza. **Es microscópica: no tiene entropía dentro** |
| $Z$ | **función de partición** | **Un número.** No una función | $Z=\int e^{-\beta U(\mathbf{r})}d\mathbf{r}$. Ver abajo ⬇ |
| $p(\mathbf{r})$ | densidad de probabilidad sobre configuraciones | Función de $\mathbf{r}$ | $p(\mathbf{r})=e^{-\beta U(\mathbf{r})}/Z$ |
| $p(s)$, $p_{\text{eq}}(s)$ | densidad **marginal** sobre la CV | Función de $s$ | Se obtiene integrando todo lo demás |
| $F(s)$ | **energía libre / PMF** a lo largo de la CV | Función de $s$ | $F\equiv -RT\ln p(s)+C$. **Sí tiene entropía dentro** |
| $\Delta G$ | diferencia entre dos **mínimos** | número | Controla **poblaciones** |
| $\Delta G^{\ddagger}$ | diferencia mínimo → **cima** | número | Controla **velocidades** |

### 🔍 Sobre $Z$ — por qué casi nunca importa

$Z$ es **un solo número**: la suma de $e^{-\beta U}$ sobre *todas* las configuraciones posibles del universo del sistema. Su único trabajo es que las probabilidades sumen 1.

$$p(\mathbf{r}) = \frac{e^{-\beta U(\mathbf{r})}}{Z} \quad\Longrightarrow\quad \int p(\mathbf{r})\,d\mathbf{r} = 1 \;\;✓$$

**No depende de $\mathbf{r}$ ni de $s$.** Es una constante. Por eso:
- En **cocientes** ($P_A/P_B$) **se cancela** → nunca hay que calcularlo.
- Cuando escribimos $\propto$ ("proporcional a"), lo que estamos haciendo es **tirar $Z$ a la basura** porque no aporta dependencia.

Calcular $Z$ es imposible en la práctica. **La buena noticia es que casi nunca hace falta.**

---

## La delta de Dirac — el símbolo que más confunde

| Símbolo | Qué es | Tipo |
|---|---|---|
| $\delta(x)$ | **Un filtro.** Vale $0$ salvo cuando $x=0$, e integra a 1 | «función» generalizada |

**Para qué se usa aquí.** La expresión

$$\int f(\mathbf{r})\;\delta\big(\xi(\mathbf{r}) - s\big)\; d\mathbf{r}$$

se lee, literalmente:

> «Suma $f(\mathbf{r})$ **solo sobre aquellas configuraciones $\mathbf{r}$ cuyo valor de CV sea exactamente $s$**.»

Versión discreta, que es la que conviene tener en la cabeza:

$$\int f(\mathbf{r})\,\delta\big(\xi(\mathbf{r})-s\big)\,d\mathbf{r}
\qquad\Longleftrightarrow\qquad
\sum_{\substack{\mathbf{r}\ \text{tales que}\\ \xi(\mathbf{r})\,=\,s}} f(\mathbf{r})$$

**La delta no es más que una notación para «restringe la suma a los $\mathbf{r}$ que cumplen $\xi(\mathbf{r})=s$».** Nada más.

---

## Muestreo sesgado y metadinámica

| Símbolo | Qué es | Tipo | Dónde |
|---|---|---|---|
| $\xi$ | la **función** variable colectiva | $\mathbb{R}^{3N}\to\mathbb{R}$ | Clase 1 §1.2 |
| $V(s)$ | **potencial de sesgo** — lo que añadimos a $U$ | Función de $s$ | Clase 2 §2 |
| $p_V(s)$ | densidad de la CV en el sistema **sesgado** | Función de $s$ | Clase 2 §2.2 |
| $F_V(s)$ | energía libre efectiva sesgada | Función de $s$ | $F_V = F + V$ |
| $\gamma$ | **biasfactor** de well-tempered | número | **10** en el paper |
| $\Delta T$ | «temperatura extra» de la CV | número | $\gamma = (T+\Delta T)/T$ → $\Delta T = 2700$ K |
| $W$ | altura de cada gaussiana depositada | energía | **10 kJ/mol** |
| $\sigma$ | anchura de cada gaussiana | mismas unidades que $s$ | **0.3 rad** |
| $\tau_G$ | intervalo entre deposiciones | tiempo | cada **1000 pasos** |
| $\kappa$ | coeficiente de transmisión | número $\le 1$ | corrige el recruzamiento en TST |

---

## Sembrado, MSM y estadística *(Clases 4–5)*

| Símbolo | Qué es | Tipo | Dónde |
|---|---|---|---|
| $B_i$ | cuenca metaestable $i$ | región del espacio de CV | Clase 1 §3.1 |
| $\pi_i$ | **peso de Boltzmann verdadero** de la cuenca $i$ | número, $\sum_i\pi_i=1$ | Lo que quieres medir |
| $w_i = N_i/N$ | **fracción de trayectorias sembradas** en la cuenca $i$ | número, $\sum_i w_i=1$ | Lo que tú impusiste |
| $\rho_i(s)$ | **forma** normalizada del pozo $i$ | Función de $s$, $\int\rho_i=1$ | Clase 1 §3.2 |
| $\hat p$, $\hat F$ | estimaciones **empíricas** (el «sombrero» = «medido, no verdadero») | Funciones de $s$ | Clase 1 §3.5 |
| $\tau$ | **lag time** del MSM | tiempo | **15 ns** en el paper. **Lo eliges tú** |
| $T(\tau)$ | matriz de transición | matriz $M\times M$ | Clase 5 |
| $\lambda_i$ | autovalores de $T(\tau)$ | números | $t_i = -\tau/\ln\lambda_i$ |

> [!warning] Colisión de notación — ojo
> $T$ se usa para **temperatura** y para la **matriz de transición** $T(\tau)$. Y $\tau$ se usa para **tiempo de espera** ($\tau = 1/k$) y para **lag time**. Son convenios estándar y chocan; el contexto los distingue. En estas notas la matriz siempre lleva su argumento: $T(\tau)$.

---

## Las tres ecuaciones maestras hasta ahora

$$\textbf{1 · Boltzmann}\qquad p(\mathbf{r}) = \frac{e^{-\beta U(\mathbf{r})}}{Z}$$

$$\textbf{2 · Un sesgo se suma al paisaje}\qquad F_V(s) = F(s) + V(s)$$

$$\textbf{3 · Sembrar sesga las profundidades}\qquad \hat F(s) = F(s) - RT\ln\frac{w_i}{\pi_i}$$
