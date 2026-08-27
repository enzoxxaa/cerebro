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

> [!success]- Respuesta Q1 → **a) $\approx -6$ kJ/mol** ✓
> $$\frac{P}{1-P} = \frac{0.92}{0.08} = 11.5, \qquad \ln 11.5 = 2.442$$
> $$\Delta G = -2.494 \times 2.442 = -6.09\ \text{kJ/mol} = -2.4\,RT$$
>
> El estado competente de E06 es solo **6 kJ/mol** más estable que *todo el resto del espacio conformacional junto*. Un 92 % suena aplastante; en energía es modesto.
>
> **Ahora el cálculo completo.** Para huE06 v1.1, con $P = 0.16$:
> $$\Delta G' = -2.494\,\ln\frac{0.16}{0.84} = -2.494 \times (-1.658) = +4.13\ \text{kJ/mol}$$
> $$\boxed{\;\Delta\Delta G = 4.13 - (-6.09) = 10.2\ \text{kJ/mol} \approx 2.4\ \text{kcal/mol}\;}$$
>
> Ese es **el resultado central del paper expresado en energía**. Corta en dos direcciones y hay que manejar las dos:
>
> | A favor | En contra |
> |---|---|
> | 10 kJ/mol es una magnitud razonable para unas pocas mutaciones puntuales. El resultado es físicamente plausible. | 10 kJ/mol es **comparable a la incertidumbre de ff14SB** en energías libres conformacionales acumuladas sobre lazos de 10–15 residuos. La conclusión vive **dentro** de la barra de error del campo de fuerza. → ataque **A11** |
>
> **La lección transferible.** La relación $P \leftrightarrow \Delta G$ es logística: **comprime energías y expande porcentajes.**
> $$P = \frac{1}{1+e^{\beta\Delta G}}$$
> Un cambio de $4\,RT$ se presenta como «92 % se derrumba a 16 %». Las dos descripciones son correctas; la segunda es más dramática. Saber traducir entre ellas es lo que te deja juzgar si un efecto es grande **de verdad**.

---

## 2 · Por qué la MD no puede visitar lo que debería

### Motivación

Ya sabes *qué* hay que medir: el cociente $P_A/P_B$. La pregunta obvia es por qué no basta con correr MD y contar frames. Hay que verlo **con números**, no con «es que es lento».

### 2.1 · La tasa de cruce

El resultado estructural es que la tasa depende **exponencialmente** de la barrera. En teoría del estado de transición:

$$
k_{\text{TST}} \;=\; \frac{k_BT}{h}\; e^{-\beta \Delta G^{\ddagger}}
$$

con el prefactor universal a 300 K:

$$
\frac{k_BT}{h} \;=\; \frac{1.381\times10^{-23}\times 300}{6.626\times10^{-34}} \;=\; 6.25\times10^{12}\ \text{s}^{-1}
$$

TST asume tres cosas: (i) **no hay recruzamiento** de la superficie divisoria, (ii) el pozo reactivo está **equilibrado**, (iii) dinámica clásica. En disolvente, (i) falla — el solvente empuja al sistema de vuelta. Se corrige con un **coeficiente de transmisión** $\kappa \le 1$:

$$
k \;=\; \kappa\,\frac{k_BT}{h}\,e^{-\beta\Delta G^{\ddagger}}
$$

En el régimen de fricción alta, Kramers da la forma explícita del prefactor:

$$
k_{\text{Kramers}} \;=\; \frac{\sqrt{U''(x_{\min})\,\big|U''(x_{\max})\big|}}{2\pi\,\gamma}\; e^{-\beta\Delta U^{\ddagger}}, \qquad \kappa \propto \frac{1}{\gamma}
$$

> [!important] La estructura del problema, que es lo único que hay que retener
> El prefactor varía **2–3 órdenes de magnitud** entre sistemas. El exponencial varía **dieciséis** órdenes en el rango de barreras que nos interesa.
> Por eso **el prefactor casi da igual y la barrera lo es todo**: usar TST como cota superior es suficiente para decidir si algo se cruza o no.

### 2.2 · Cuántos cruces esperas

Los cruces son un proceso de Poisson de tasa $k$. En un tiempo $t$, el número esperado es

$$
\langle n \rangle \;=\; k\,t
\qquad\text{y}\qquad
P(\text{al menos un cruce}) \;=\; 1 - e^{-kt}
$$

Y el tiempo de espera medio es $\tau = 1/k$.

---

> [!question] **Q2 · R1** — Haz tú la cuenta
> Barrera $\Delta G^{\ddagger} = 40$ kJ/mol, $T = 300$ K, trayectoria de $t = 100$ ns $= 10^{-7}$ s.
> Usa **TST sin corregir** ($\kappa = 1$), es decir la **estimación más generosa posible**.
>
> $$\beta\Delta G^{\ddagger} = \frac{40000}{2494} = 16.04 \qquad e^{-16.04} = 1.08\times10^{-7}$$
>
> ¿Cuánto vale $\langle n \rangle = k\,t$, el número esperado de cruces?
>
> **a)** $\approx 7\times10^{-2}$
> **b)** $\approx 7$
> **c)** $\approx 7\times10^{2}$
> **d)** $\approx 7\times10^{-5}$

> [!success]- Respuesta Q2 → **a) $\approx 7\times10^{-2}$** ✓
> $$k_{\text{TST}} = 6.25\times10^{12} \times 1.08\times10^{-7} = 6.75\times10^{5}\ \text{s}^{-1}$$
> $$\tau_{\text{TST}} = 1/k = 1.48\ \mu\text{s}, \qquad \langle n\rangle = k\,t = 6.75\times10^{5}\times10^{-7} = 0.0675$$
>
> Y eso es la **cota superior**. Con $\kappa \sim 10^{-2}$ realista para lazos en agua: $\langle n\rangle \approx 7\times10^{-4}$ y $\tau \approx 150\ \mu$s.
>
> **Comprobación de consistencia:** ese rango µs–ms coincide con el título de otro paper del propio grupo, *«Transitions of CDR-L3 Loop Canonical Cluster Conformations on the Micro-to-Millisecond Timescale»*. TST y la literatura del grupo concuerdan.
>
> **La frontera de la MD.** ¿Qué barrera da $\langle n\rangle \approx 1$ en 100 ns? Necesitas $k \approx 10^7\ \text{s}^{-1}$, y con $\kappa = 10^{-2}$:
> $$e^{-\beta\Delta G^\ddagger} = \frac{10^{9}}{6.25\times10^{12}} = 1.6\times10^{-4} \;\Rightarrow\; \beta\Delta G^\ddagger = 8.74 \;\Rightarrow\; \Delta G^\ddagger \approx 22\ \text{kJ/mol}$$
> **100 ns de MD te compran barreras de hasta ~22 kJ/mol y nada más.** Las transiciones de lazos CDR viven entre ~25 y ~45. No falta «un poco» de tiempo: faltan órdenes de magnitud.

---

## 2 bis · Dos preguntas de Enzo

### 🅰 ¿Todo esto asume NVT? El paper corre NpT

Buena captura: escribí $p(\mathbf{r}) \propto e^{-\beta U}$, que es **canónico (NVT)**, y el paper simula en **NpT**. Hay que hacerlo bien.

#### El ensemble correcto

En NpT el volumen fluctúa, así que es una variable más sobre la que integrar. La función de partición isotérmica-isobárica es

$$
\Delta(N,p,T) \;=\; \int_0^{\infty} \!dV\; e^{-\beta pV} \, Z(N,V,T),
\qquad
Z(N,V,T) = \int_{V} e^{-\beta U(\mathbf{r})}\, d\mathbf{r}
$$

Sustituyendo $Z$ dentro, el peso estadístico de una configuración concreta $(\mathbf{r}, V)$ es

$$
p(\mathbf{r}, V) \;\propto\; e^{-\beta\left[\,U(\mathbf{r}) \;+\; pV\,\right]}
$$

Es decir: **la única modificación es $U \to U + pV$.** El potencial termodinámico deja de ser Helmholtz $A = -RT\ln Z$ y pasa a ser Gibbs $G = -RT\ln\Delta$.

Rehaciendo §1.3 con este peso, el cociente de poblaciones queda

$$
\frac{P_A}{P_B} \;=\; e^{-\beta\left[\,\Delta U_{AB} \;+\; p\,\Delta V_{AB}\,\right]}
$$

donde $\Delta V_{AB} = \langle V\rangle_A - \langle V\rangle_B$ es la diferencia de **volumen medio** entre los dos estados.

#### ¿Cuánto vale ese término nuevo?

Ojo con el error de bulto: **no** importa $pV$ de la caja entera, sino $p\,\Delta V$ **entre confórmeros**. Vamos con números.

Sea $\Delta V = 20\ \text{cm}^3/\text{mol}$ — una cota **muy** generosa para un reordenamiento de lazos (para referencia, el volumen molar del agua es $18\ \text{cm}^3/\text{mol}$, así que esto es como desplazar ~1 molécula de agua por proteína).

Paso a unidades SI:
$$
\Delta V = 20\ \tfrac{\text{cm}^3}{\text{mol}} = 20 \times 10^{-6}\ \tfrac{\text{m}^3}{\text{mol}}
$$

Y $p = 1\ \text{atm} = 101325\ \text{Pa}$. Como $1\ \text{Pa}\cdot\text{m}^3 = 1\ \text{J}$:

$$
p\,\Delta V \;=\; 101325 \times 20\times10^{-6} \;=\; 2.03\ \tfrac{\text{J}}{\text{mol}} \;=\; 0.002\ \tfrac{\text{kJ}}{\text{mol}}
$$

Comparado con la escala térmica:

$$
\frac{p\,\Delta V}{RT} \;=\; \frac{2.03}{2494} \;\approx\; 8\times10^{-4}
$$

> [!success] Conclusión rigurosa
> $$p\,\Delta V \;\sim\; 10^{-3}\,RT \quad\Longrightarrow\quad \text{NVT y NpT dan las mismas poblaciones}$$
> A presión ambiente el término $p\Delta V$ es **cuatro órdenes de magnitud menor** que las diferencias de energía libre que discutimos ($\approx 6$ kJ/mol). La derivación canónica vale tal cual, y la distinción $G$ vs $A$ es irrelevante aquí.

**¿Cuándo dejaría de valer?** Despejando $p$ para que $p\Delta V \approx RT$:
$$
p \;\approx\; \frac{RT}{\Delta V} \;=\; \frac{2494}{20\times10^{-6}} \;=\; 1.25\times10^{8}\ \text{Pa} \;\approx\; \mathbf{1200\ atm}
$$
Por eso la biofísica de alta presión trabaja en kbar: es la presión a la que $p\Delta V$ empieza a competir con $RT$. A 1 atm, no.

> [!warning] Dónde el ensemble **sí** importa, y no hay que confundirlo
> Lo anterior dice que **NVT y NpT dan las mismas poblaciones medias**. No dice que dé igual cómo implementes el barostato.
> El barostato de **Berendsen** —el que usa el paper en producción— reproduce la presión media pero **suprime las fluctuaciones de volumen**, así que no muestrea el NpT correcto. Eso afecta a $\langle\delta V^2\rangle$ y por tanto a la compresibilidad, no a $P_A/P_B$.
> **Termodinámica conformacional: intacta. Rigor formal del ensemble: comprometido.** Son dos afirmaciones distintas y conviene no mezclarlas al criticar.

---

### 🅱 «Dijimos $\Delta G = -6$ kJ/mol, pero luego barreras de 20–40». ¿No se contradice?

**No, y esta es probablemente la distinción más importante de toda la clase.** Son dos cantidades **diferentes**, medidas entre puntos distintos del mismo perfil.

#### El perfil, con los dos números marcados

```
   F(s)
     ▲
     │                    ╭───────╮   ← cima:  F(s‡)
     │                  ╱           ╲
     │                ╱               ╲
     │  ΔG‡ ≈ 25–45 ╱                   ╲
     │   ↕        ╱                       ╲
     │          ╱                           ╲
     │ ╲______╱                               ╲______╱
     │    A                                       B     ↕  ΔG ≈ 6
     │  F(s_A)                                  F(s_B)
     └──────────────────────────────────────────────────▶ s
```

$$
\underbrace{\Delta G \;=\; F(s_B) - F(s_A)}_{\text{entre los dos FONDOS}}
\qquad\qquad
\underbrace{\Delta G^{\ddagger} \;=\; F(s^{\ddagger}) - F(s_A)}_{\text{del fondo a la CIMA}}
$$

| | $\Delta G$ | $\Delta G^{\ddagger}$ |
|---|---|---|
| Se mide entre | mínimo ↔ mínimo | mínimo ↔ cima |
| Controla | **poblaciones** | **velocidades** |
| Es | **termodinámica** | **cinética** |
| Aquí vale | $\approx 6$ kJ/mol | $\approx 25\text{–}45$ kJ/mol |
| Aparece en | $P_A/P_B = e^{-\beta\Delta G}$ | $k = \kappa\frac{k_BT}{h}e^{-\beta\Delta G^{\ddagger}}$ |

#### Son lógicamente independientes

Basta ver que puedes construir cualquier combinación:

- $\Delta G = 0$ y $\Delta G^{\ddagger} = 100$ kJ/mol → dos estados **igual de poblados** que **jamás** interconvierten.
- $\Delta G = 20$ y $\Delta G^{\ddagger} = 21$ kJ/mol → poblaciones muy desiguales que se **equilibran rapidísimo**.

La única restricción geométrica es $\Delta G^{\ddagger} \ge \max(0, \Delta G)$: la cima no puede estar por debajo de ninguno de los dos fondos. Nada más. **Saber la profundidad relativa de dos pozos no te dice nada sobre la altura del muro entre ellos.**

#### La relación que sí existe: balance detallado

Aunque sean independientes, están ligadas por una identidad exacta. Escribe las dos tasas desde el **mismo** estado de transición:

$$
k_{A\to B} = \kappa\,\frac{k_BT}{h}\,e^{-\beta\left[F(s^{\ddagger}) - F(s_A)\right]}
\qquad
k_{B\to A} = \kappa\,\frac{k_BT}{h}\,e^{-\beta\left[F(s^{\ddagger}) - F(s_B)\right]}
$$

Divide. El prefactor $\kappa\,k_BT/h$ se cancela, y usando $e^{x}/e^{y} = e^{x-y}$:

$$
\frac{k_{A\to B}}{k_{B\to A}}
= \exp\!\Big(\!-\beta\big[F(s^{\ddagger}) - F(s_A)\big] + \beta\big[F(s^{\ddagger}) - F(s_B)\big]\Big)
$$

Dentro del exponente, $-\beta F(s^{\ddagger})$ y $+\beta F(s^{\ddagger})$ **se cancelan**:

$$
= \exp\!\Big(\beta F(s_A) - \beta F(s_B)\Big)
= e^{-\beta\left[F(s_B) - F(s_A)\right]}
$$

$$
\boxed{\;\frac{k_{A\to B}}{k_{B\to A}} \;=\; e^{-\beta \Delta G} \;=\; \frac{P_B}{P_A}\;}
$$

> [!important] Lee lo que acaba de pasar
> **$F(s^{\ddagger})$ desapareció.** La altura de la barrera **no aparece** en el cociente.
> Traducido: la barrera controla **cuánto tardas** en llegar al equilibrio, pero **no dónde está** el equilibrio. Puedes subir el muro todo lo que quieras: las poblaciones finales no cambian, solo tardas más en alcanzarlas.

#### Y ahora, por qué este sistema es el caso difícil

Junta los dos números del paper:

$$
\Delta G \approx 6\ \text{kJ/mol} \;=\; 2.4\,RT
\qquad\text{(pozos POCO PROFUNDOS)}
$$
$$
\Delta G^{\ddagger} \approx 25\text{–}45\ \text{kJ/mol} \;=\; 10\text{–}18\,RT
\qquad\text{(muros MUY ALTOS)}
$$

> [!danger] La combinación es lo peor de ambos mundos
> **Termodinámica somera** ⇒ las poblaciones están finamente balanceadas, así que un error de 2–3 kJ/mol del campo de fuerza **cambia la respuesta**. → ataque **A11**
> **Cinética lenta** ⇒ el sistema no se equilibra solo en tiempos accesibles, así que **no puedes medir esas poblaciones con MD directa**. → nodo `N1`
>
> Necesitas **alta precisión sobre un número pequeño**, obtenida de un sistema que **se niega a equilibrarse**.
>
> Ahí está la justificación de todo el pipeline — y también toda su superficie de ataque. No era una contradicción: **era el planteamiento del problema.**

---

> [!question] **Q3** — Un sistema tiene dos confórmeros con $\Delta G = 0$ exactamente, separados por una barrera de $\Delta G^{\ddagger} = 60$ kJ/mol. Corres 100 ns de MD partiendo del confórmero $A$. ¿Qué poblaciones mides?
>
> **a)** $\approx 100\ \%$ A, $0\ \%$ B
> **b)** $\approx 50\ \%$ A, $50\ \%$ B
> **c)** $\approx 100\ \%$ B, $0\ \%$ A
> **d)** Depende del campo de fuerza, no se puede saber
