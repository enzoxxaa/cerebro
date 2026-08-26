---
tipo: clase
proyecto: seminario
fecha: 2026-08-26
clase: 1
nodos: [R1, R2, N1, M3]
hebras: [termodinámica estadística, MD clásica]
modo: socrático
estado: en curso
resumen: "Clase 1: derivación rigurosa de la población de equilibrio y del PMF; por qué la MD sola no basta; y la demolición de M3 — un histograma sesgado no es una energía libre"
tags:
  - seminario
  - clase
---

# 10 · Clase 1 — El problema y el pivote

← [[00 MOC — Seminario VNAR]] · anterior: [[05 Clase 0 — El VNAR]] · [[01 Plan de aprendizaje]]

**Nodos:** `R1` `R2` `N1` + **demolición de M3** — el pivote de todo el curso.

> [!abstract] Convenios de notación, fijados de una vez
> $\beta \equiv 1/k_BT$ · $\mathbf{r} \in \mathbb{R}^{3N}$ la configuración · $U(\mathbf{r})$ la energía potencial · $\xi(\mathbf{r})$ una variable colectiva (CV) escalar, con valor $s$.
> Trabajo con **energías molares**, así que uso $RT$ donde en formulación por partícula iría $k_BT$. Son la misma cantidad en unidades distintas: $R = N_A k_B$.

---

## 1 · Qué es exactamente una «población»

### Motivación

La conclusión entera del paper es un número de población: **92 % → 16 %**. Antes de discutir cómo se calcula, hay que definir con precisión **qué es**. Si «población» queda vago, ninguna crítica posterior se sostiene — y las críticas fuertes contra este paper son todas sobre si ese número significa lo que dicen que significa.

### 1.1 · El punto de partida

En el ensemble canónico $(N,V,T)$, la densidad de probabilidad sobre configuraciones es

$$
p(\mathbf{r}) \;=\; \frac{e^{-\beta U(\mathbf{r})}}{Z},
\qquad
Z \;=\; \int e^{-\beta U(\mathbf{r})}\, d\mathbf{r}
$$

> [!success] Verdad incondicional `R2`
> Esto **no se deriva aquí**: es la definición del ensemble canónico. Lo tomamos al pie de la letra. Todo lo demás en esta clase se deduce de ello.

### 1.2 · Proyectar sobre una coordenada: el PMF

Nunca miramos $\mathbb{R}^{3N}$; miramos una CV. En el paper, torsiones $\psi$ de los lazos. La densidad **marginal** de la CV se obtiene integrando todo lo demás:

$$
p(s) \;=\; \frac{1}{Z}\int e^{-\beta U(\mathbf{r})}\,\delta\!\big(\xi(\mathbf{r}) - s\big)\, d\mathbf{r}
\;=\; \big\langle\, \delta(\xi(\mathbf{r}) - s) \,\big\rangle
$$

Y se **define** la energía libre a lo largo de $\xi$ — el *potential of mean force* — como

$$
\boxed{\;F(s) \;\equiv\; -RT\ln p(s) \;+\; C\;}
$$

Tres precisiones que hay que tener claras, porque las tres se usan después:

1. **$C$ es arbitraria.** Solo tienen sentido las *diferencias* de $F$. Cualquier afirmación sobre el valor absoluto de un PMF es vacía.
2. **El nombre no es decorativo.** Se llama *potencial de fuerza media* porque satisface
   $$-\frac{dF}{ds} \;=\; \left\langle\, -\frac{\partial U}{\partial \xi} \,\right\rangle_{\xi = s}$$
   es decir, su gradiente es la fuerza media sobre la CV promediada sobre todo lo demás.
3. **Depende de la medida.** $p(s)$ es una densidad *respecto a una medida*. Para un ángulo diedro la medida natural $d\phi$ es plana y no hay jacobiano — **cosa que juega a favor del paper**, porque usan diedros. Si la CV fuera una distancia $r$ en 3D habría que descontar el término $4\pi r^2$, y olvidarlo es un error clásico.

### 1.3 · De la densidad a la población de un estado

Un macroestado $A$ es una **región** del espacio de la CV. Su probabilidad es simplemente la integral de la densidad ahí:

$$
P_A \;=\; \int_A p(s)\, ds \;=\; \frac{Z_A}{Z},
\qquad
Z_A \;\equiv\; \int e^{-\beta U(\mathbf{r})}\;\mathbb{1}\big[\xi(\mathbf{r}) \in A\big]\, d\mathbf{r}
$$

Definiendo la energía libre del macroestado como $G_A \equiv -RT\ln Z_A$, el cociente de poblaciones sale de inmediato:

$$
\frac{P_A}{P_B} \;=\; \frac{Z_A}{Z_B} \;=\; e^{-\beta\,(G_A - G_B)}
\qquad\Longleftrightarrow\qquad
\boxed{\;\Delta G_{AB} \;=\; -RT\,\ln\frac{P_A}{P_B}\;}
$$

Nota que $Z$ se ha cancelado. Por eso los **cocientes** de poblaciones son mucho más robustos que las poblaciones absolutas: no requieren conocer la función de partición total.

### 1.4 · La constante que hay que tener en la cabeza

$$
RT \;=\; 8.314\ \tfrac{\text{J}}{\text{mol·K}} \times 300\ \text{K} \;=\; 2494\ \tfrac{\text{J}}{\text{mol}} \;\approx\; \mathbf{2.5\ \text{kJ/mol}}
$$

Regla práctica: **un factor $e$ en población cuesta $2.5$ kJ/mol; un factor 10 cuesta $RT\ln 10 \approx 5.7$ kJ/mol.**

---

> [!question] **Q1 · R2** — Aplicación directa
> El paper reporta que en el parent **E06** el estado competente tiene una probabilidad $P = 0.92$.
>
> Tratándolo como una partición binaria «estado competente **vs.** todo lo demás», ¿cuánto vale
> $$\Delta G \;=\; G_{\text{competente}} - G_{\text{resto}} \;=\; -RT\ln\frac{P}{1-P}\ ?$$
>
> **a)** $\approx -6$ kJ/mol
> **b)** $\approx -25$ kJ/mol
> **c)** $\approx -2.5$ kJ/mol
> **d)** $\approx -60$ kJ/mol
>
> *(el signo negativo significa «más estable». Responde en el terminal.)*
