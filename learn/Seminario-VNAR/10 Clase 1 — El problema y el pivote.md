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

> [!success]- Respuesta Q3 → **a) $\approx 100\ \%$ A** ✓
> Las poblaciones **verdaderas** son 50/50 ($\Delta G = 0$), pero tu simulación dirá 100/0.
> $$\beta\Delta G^\ddagger = \tfrac{60000}{2494} = 24.1,\quad e^{-24.1} = 3.4\times10^{-11},\quad k = 213\ \text{s}^{-1},\quad \langle n\rangle = 2.1\times10^{-5}$$
> Dos cruces por cada cien mil trayectorias.
>
> **Y la simulación no te avisa.** Ni error, ni warning, ni señal. Obtienes una trayectoria válida, un histograma limpio, y un resultado 100 % equivocado.
>
> Sobre (d): mantén separados los **dos ejes de error**, porque determinan qué ataque estás lanzando.
>
> | Eje | Qué falla | Ataque |
> |---|---|---|
> | **Modelo** | el campo de fuerza da un $\Delta G$ equivocado | **A11** |
> | **Muestreo** | aunque $\Delta G$ fuese exacto, no lo mides | **A1**, **A2** |
>
> Este ejercicio aislaba el segundo poniendo el primero a cero por construcción.

**Nodo `N1` instalado.**

---

## 3 · EL PIVOTE — cuándo un histograma *no* es una energía libre

### Motivación

Acabas de ver que el histograma de **una** trayectoria puede mentir. La reacción natural es: *«vale, entonces uso muchas trayectorias, sembradas por todo el paisaje».* Que es exactamente lo que hace el paper.

La pregunta es si eso arregla el problema. Vamos a derivarlo, porque la respuesta es **no**, y de forma muy precisa.

### 3.1 · Montaje

Particionamos el espacio de la CV en $M$ cuencas metaestables $B_1,\dots,B_M$. Hay dos escalas de tiempo:

$$
\tau_{\text{loc}} \;\ll\; T \;\ll\; \tau_{\text{esc}}
$$

- $\tau_{\text{loc}}$: relajarse **dentro** de una cuenca — rápido (ps–ns)
- $T = 100$ ns: la longitud de cada trayectoria sembrada
- $\tau_{\text{esc}}$: escapar de la cuenca — lento (µs–ms), como calculaste en Q2

Este régimen **es** el de la MD sembrada del paper.

### 3.2 · Descomponer el equilibrio verdadero

Por la ley de probabilidad total, la densidad de equilibrio se descompone **exactamente** en contribuciones por cuenca:

$$
p_{\text{eq}}(s) \;=\; \sum_{i=1}^{M} \pi_i\,\rho_i(s)
$$

donde cada pieza tiene un significado limpio:

$$
\pi_i \;\equiv\; \int_{B_i} p_{\text{eq}}(s)\,ds \;=\; \frac{Z_i}{Z}
\qquad\text{(peso de Boltzmann verdadero de la cuenca }i)
$$

$$
\rho_i(s) \;\equiv\; \frac{p_{\text{eq}}(s)\,\mathbb{1}[s\in B_i]}{\pi_i}
\qquad\text{(forma de la cuenca }i\text{, normalizada: }\textstyle\int\rho_i = 1)
$$

Léelo así: **$\rho_i$ es la *forma* del pozo, $\pi_i$ es su *peso*.** El equilibrio es la suma de las formas, cada una pesada por su $\pi_i$.

### 3.3 · Qué produce en realidad la MD sembrada

Lanzas $N_i$ trayectorias en la cuenca $i$, con $N = \sum_i N_i$ en total. Por el régimen de §3.1:

- Como $T \gg \tau_{\text{loc}}$, cada trayectoria **sí** se equilibra dentro de su cuenca → muestrea $\rho_i$ **correctamente** ✅
- Como $T \ll \tau_{\text{esc}}$, **ninguna** trayectoria escapa → la asignación a cuencas queda **congelada** ❌

Juntando todos los frames con **igual peso** —que es lo que hace un histograma— la densidad empírica converge a

$$
\hat p(s) \;=\; \sum_{i=1}^{M} w_i\,\rho_i(s),
\qquad
w_i \;\equiv\; \frac{N_i}{N}
$$

### 3.4 · La comparación

$$
p_{\text{eq}}(s) = \sum_i \pi_i\,\rho_i(s)
\qquad\text{vs.}\qquad
\hat p(s) = \sum_i w_i\,\rho_i(s)
$$

**Las formas $\rho_i$ son idénticas. Solo cambian los pesos.** Y por tanto:

$$
\hat p = p_{\text{eq}} \iff w_i = \pi_i \quad \forall i
$$

O sea: el histograma es correcto **si y solo si sembraste exactamente en las proporciones de Boltzmann** — que son justo las que estabas intentando medir. Circular.

### 3.5 · El error, explícito

Tomemos $s$ dentro de la cuenca $i$. La «energía libre» que sale del histograma es

$$
\hat F(s) \;=\; -RT\ln\hat p(s) \;=\; -RT\ln\big[\,w_i\,\rho_i(s)\,\big]
$$

Usando $\ln(ab) = \ln a + \ln b$:

$$
\hat F(s) \;=\; -RT\ln \rho_i(s) \;-\; RT\ln w_i
$$

La verdadera, por el mismo camino:

$$
F(s) \;=\; -RT\ln\big[\,\pi_i\,\rho_i(s)\,\big] \;=\; -RT\ln\rho_i(s) \;-\; RT\ln \pi_i
$$

Resta las dos. El término $-RT\ln\rho_i(s)$ **se cancela**:

$$
\hat F(s) - F(s) \;=\; -RT\ln w_i + RT\ln\pi_i \;=\; -RT\ln\frac{w_i}{\pi_i}
$$

$$
\boxed{\;\hat F(s) \;=\; F(s) \;-\; RT\ln\frac{w_i}{\pi_i}\,,\qquad s \in B_i\;}
$$

### 3.6 · Leer el resultado — tres propiedades

> [!important] 1 · El error es **constante dentro de cada cuenca**
> No depende de $s$, solo de $i$. Por tanto **la forma de cada pozo es correcta**: curvatura, anchura, subestructura, todo bien. Si solo te interesa un mínimo aislado, el histograma sirve.

> [!important] 2 · El error **cambia de una cuenca a otra**
> Y las profundidades *relativas* entre pozos son exactamente lo que significa «la población del estado X». **Justo lo que el paper reporta es lo que está mal.**

> [!danger] 3 · El error **NO decrece con más muestreo**
> Si $N\to\infty$ manteniendo las proporciones $w_i$, el sesgo $-RT\ln(w_i/\pi_i)$ **se queda igual**. No es ruido estadístico: es **sesgo sistemático**.
> Simular más hace la respuesta equivocada **más nítida**, no más correcta. Las barras de error se encogen alrededor del número incorrecto.

### 3.7 · Cuánto vale esto en el caso del paper

Supón que la verdad es $\pi_A = 0.92$, $\pi_B = 0.08$ (el resultado de E06), pero sembraste mitad y mitad: $w_A = w_B = 0.5$.

$$
\text{Error en } A: \; -RT\ln\frac{0.5}{0.92} = -2.494\ln(0.543) = -2.494\times(-0.610) = +1.52\ \text{kJ/mol}
$$
$$
\text{Error en } B: \; -RT\ln\frac{0.5}{0.08} = -2.494\ln(6.25) = -2.494\times(1.833) = -4.57\ \text{kJ/mol}
$$
$$
\text{Error en }\Delta G_{AB} = (-4.57) - (+1.52) = -6.09\ \text{kJ/mol}
$$

Comprobación: tu histograma diría 50/50, es decir $\Delta G = 0$, cuando la verdad es $-6.09$ kJ/mol. El error es **exactamente** el efecto completo. ✅ Cuadra.

> [!danger] Y ahora la magnitud
> Ese error de **6 kJ/mol** es del mismo tamaño que **toda la señal que el paper reporta** ($\Delta\Delta G \approx 10$ kJ/mol, Q1).
> No es una corrección de segundo orden. Es **la señal entera**.

### 3.8 · ¿Y cómo se sembró aquí?

En el paper, $w_i$ lo fija esta cadena:

$$
\text{trayectoria de metadinámica (sesgada)} \;\to\; \text{clustering jerárquico a 1.3 Å} \;\to\; \text{1 semilla por cluster}
$$

Un corte de clustering fijo devuelve **aproximadamente una semilla por conformación distinta**, independientemente de lo poblada que esté. Es decir, $w_i$ está mucho más cerca de ser **uniforme sobre confórmeros distintos** que de ser $\pi_i$.

En cualquier caso: $w \ne \pi$, **por construcción y deliberadamente** — la metadinámica se usó precisamente para *aplanar* el paisaje.

> [!success] El pivote, en una frase
> $$F(s) = -RT\ln p(s) \quad\text{exige que } p \text{ sea } p_{\text{eq}}.$$
> La MD sembrada produce $\hat p \ne p_{\text{eq}}$ **por diseño**. Luego $-RT\ln\hat p$ **no es una energía libre**: es el paisaje verdadero con cada pozo desplazado verticalmente según cuánto sembraste en él.
>
> **Y de aquí sale, ya derivado, todo lo demás del curso:**
> - **Por qué el MSM no es opcional** → estima $\pi_i$ de las *tasas* de transición (dinámica local sin sesgo) y reponderá $w_i \to \pi_i$. Es literalmente el único paso que arregla esto.
> - **El ataque A6** → si la Fig. 3A es histograma crudo, sus profundidades relativas codifican dónde cayeron los clusters.
> - **El ataque A1** → si además $w_i$ depende del sistema (11.9 µs vs 43.1 µs), el sesgo es **distinto para cada variante**, y estás comparando peras con manzanas.

---

> [!question] **Q4 · demolición de M3** — Según $\hat F(s) = F(s) - RT\ln(w_i/\pi_i)$, ¿qué parte del histograma crudo es correcta y cuál no?
>
> **a)** La forma de cada mínimo es correcta; las profundidades relativas entre mínimos son incorrectas
> **b)** Las profundidades relativas son correctas; la forma de cada mínimo está distorsionada
> **c)** Todo es incorrecto por un factor que decrece al aumentar el número de frames
> **d)** Todo es correcto salvo una constante aditiva global

> [!success]- Respuesta Q4 → **a) Forma correcta, profundidades relativas incorrectas** ✓
> Sale de **leer** la fórmula $\hat F(s) = F(s) - RT\ln(w_i/\pi_i)$:
>
> | El error… | Consecuencia |
> |---|---|
> | **no** depende de $s$ | dentro de una cuenca es constante → **la forma del pozo se conserva** |
> | **sí** depende de $i$ | cambia entre cuencas → **las profundidades relativas se desplazan** |
>
> Por qué las otras tres son errores distintos e importantes:
>
> - **(c) «decrece con más frames»** — el error conceptual grave: confunde **sesgo sistemático** con **ruido estadístico**. Con $N\to\infty$ a proporciones $w_i$ fijas, el término no se mueve. Más simulación estrecha las barras de error **alrededor del número equivocado** — peor que inútil, porque da confianza injustificada.
> - **(d) «una constante global»** — tentador, porque es cierto que $F$ está definida salvo constante (§1.2). Pero aquí hay **una constante distinta por cuenca**. Una global es inofensiva; $M$ distintas destruyen justo la comparación que importa.
> - **(b)** invierte el resultado.

> [!success] **M3 demolida.**
> Ya no necesitas *creer* que hace falta un MSM. Puedes **derivar** que hace falta: es el único paso del pipeline capaz de convertir $w_i$ en $\pi_i$.

---

## Resumen — Clase 1

### Resultados

$$
p(\mathbf{r}) = \frac{e^{-\beta U}}{Z}
\;\longrightarrow\;
F(s) \equiv -RT\ln p(s) + C
\;\longrightarrow\;
\Delta G_{AB} = -RT\ln\frac{P_A}{P_B}
$$

$$
k = \kappa\,\frac{k_BT}{h}\,e^{-\beta\Delta G^{\ddagger}}
\qquad
\frac{k_{A\to B}}{k_{B\to A}} = e^{-\beta\Delta G}
\qquad
\boxed{\hat F(s) = F(s) - RT\ln\frac{w_i}{\pi_i}}
$$

### Números para llevarse

| Cantidad | Valor |
|---|---|
| $RT$ a 300 K | **2.494 kJ/mol** |
| $k_BT/h$ a 300 K | $6.25\times10^{12}\ \text{s}^{-1}$ |
| Coste de un factor 10 en población | $RT\ln 10 = 5.7$ kJ/mol |
| $\Delta G$ del estado competente (E06) | $-6.1$ kJ/mol |
| **$\Delta\Delta G$ del efecto completo (E06 → v1.1)** | **10.2 kJ/mol** |
| Barrera máxima cruzable en 100 ns | $\approx 22$ kJ/mol |
| Barreras reales de lazos CDR | $25\text{–}45$ kJ/mol |
| $p\Delta V$ a 1 atm | $\sim 10^{-3}\,RT$ → **despreciable** |

### Nodos

| Nodo | Contenido | ✓ |
|---|---|---|
| `R2` | poblaciones $=$ pesos de Boltzmann; PMF por marginalización | Q1 |
| — | NpT ≡ NVT para poblaciones a 1 atm | 🅰 |
| — | **$\Delta G$ y $\Delta G^\ddagger$ son independientes**; la barrera se cancela en el balance detallado | 🅱 |
| `R1` | $\tau \sim e^{+\beta\Delta G^\ddagger}$; 100 ns compran ~22 kJ/mol | Q2 |
| `N1` | MD sola ⇒ poblaciones $=$ estructura inicial | Q3 |
| **M3** | **demolida**: el sesgo de siembra es sistemático, no estadístico | Q4 |

> [!abstract] Adónde va esto — Clase 2
> Problema perfectamente planteado: **hay que cruzar barreras de 40 kJ/mol sin esperar 150 µs por cruce, y sin que el remedio destruya las poblaciones.**
> La Clase 2 es socrática y arranca demoliendo **M1** (*«metadinámica = subir la temperatura»*) con una sola pregunta:
> *Si no puedes bajar la barrera cambiando la física, ni esperar a que se cruce sola… ¿qué te queda?*
