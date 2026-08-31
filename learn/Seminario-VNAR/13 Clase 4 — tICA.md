---
tipo: clase
proyecto: seminario
fecha: 2026-08-29
clase: 4
nodos: [N8, N9]
hebras: [tICA/MSM]
modo: expositivo
estado: en curso
resumen: "Clase 4: MD sembrada sin sesgo, y la derivación completa de tICA — el problema de autovalores generalizado, por qué encuentra lo lento y no lo amplio, y su conexión con el operador de transferencia que se retomará en el MSM"
tags:
  - seminario
  - clase
  - tica
---

# 13 · Clase 4 — tICA

← [[00 MOC — Seminario VNAR]] · anterior: [[12 Clase 3 — El precio]]

**Nodos:** `N8` (MD sembrada sin sesgo) → `N9` (tICA: lo lento, no lo amplio).

```mermaid
graph TD
    N7["N7 · tirar F y cinetica<br/>quedarse las estructuras"] --> N8["N8 · clustering + MD<br/>sembrada sin sesgo"]
    N8 --> N9["N9 · tICA: encontrar<br/>lo lento, no lo amplio"]
    N9 --> C5["Clase 5 · MSM"]
    style N9 fill:#1f6f3f,color:#fff
```

---

## 1 · `N8` — De vuelta a MD sin sesgo

### Motivación

En la Clase 3 decidimos algo drástico: tirar la energía libre y la cinética de la metadinámica, y quedarnos **solo con las estructuras** que visitó. Pregunta obvia: ¿qué se hace con un microsegundo de trayectoria sesgada llena de estructuras?

### Establecer

No se puede analizar cada frame — son millones. Se **resume**:

1. **Clustering jerárquico** (*average linkage*, `cpptraj`), corte de distancia **1.3 Å** → reduce el microsegundo a un puñado de representantes estructuralmente distintos.
2. Cada representante se re-equilibra y se lanza a **100 ns de MD sin sesgo** (AMBER 20, `pmemd.cuda`).

### Conectar

El resultado son muchas trayectorias **cortas y físicas** — sin sesgo, así que dentro de cada una la dinámica es real. Pero heredan un problema que ya conoces exactamente:

$$
\hat F(s) = F(s) - RT\ln\frac{w_i}{\pi_i}
$$

El número de clusters por región fija $w_i$, y nada garantiza $w_i=\pi_i$. **Ese problema sigue vivo** — y es precisamente lo que el MSM (Clase 5) va a reparar. Antes de llegar ahí, hace falta **organizar** estas trayectorias de alguna forma manejable: eso es tICA.

---

> [!question] **Q1 · N8** — Después del clustering y la MD sembrada sin sesgo, ¿qué tienen exactamente estas nuevas trayectorias?
>
> **a)** Física local correcta dentro de cada una, pero pesos de siembra $w_i$ que en general no son $\pi_i$
> **b)** Las poblaciones de equilibrio correctas, porque ya no hay sesgo
> **c)** El mismo problema que las trayectorias de metadinámica: dinámica no física
> **d)** Trayectorias demasiado cortas para tener ninguna física correcta

> [!success]- Respuesta Q1 → **a) Física correcta, pesos aún mal** ✓
> Estas trayectorias son MD **sin sesgo** — dentro de cada una la dinámica es real. Eso las distingue de las trayectorias de metadinámica, donde $V(s,t)$ deformaba activamente la dinámica.
> Pero heredan el problema de **cómo se sembraron**: el número de clusters por región fija $w_i$, y nada garantiza $w_i=\pi_i$.
> **Física correcta dentro de la cuenca, incapaz aún de decirte las poblaciones entre cuencas.** Ahí arranca tICA.

---

## 2 · `N9` — tICA: encontrar lo lento, no lo amplio

### 2.1 · Motivación

Tienes cientos de trayectorias cortas, cada una viviendo en un espacio de **muchas** coordenadas — las torsiones $\psi$ de CDR1, CDR3 y HV2, más sus combinaciones. Para poder *ver* algo — como los paisajes de la Fig. 3 y la Fig. 4 — hace falta **proyectar a 2 dimensiones**. La pregunta es sobre qué proyectar.

### 2.2 · La respuesta ingenua, y por qué falla

Lo primero que se le ocurre a cualquiera: **PCA**, la dirección de mayor varianza.

> [!question] Antes de seguir — piénsalo
> Imagina dos grados de libertad en el mismo lazo: uno es la punta del lazo **agitándose** con amplitud grande (varía mucho, se relaja en $\sim$10 ps). El otro es un **cambio conformacional real** entre dos cuencas, con amplitud pequeña pero que tarda $\sim$10 µs en revertirse. ¿Cuál elige PCA como componente principal? ¿Es la que te interesa?

PCA **no distingue entre rápido y lento** — solo mide cuánto se mueve una coordenada, no cuánto tarda en "olvidar" de dónde vino. La punta agitándose tiene más varianza y gana, aunque sea irrelevante para separar estados metaestables.

> [!important] Lo que hace falta
> No una dirección de **mucho movimiento**. Una dirección que **tarde en decorrelacionarse** — que hoy y dentro de un rato $\tau$ sigan pareciéndose. Eso es *lento* en el sentido que importa.

### 2.3 · Formalizar "tarda en decorrelacionarse"

Sea $\mathbf{x}(t)\in\mathbb{R}^d$ el vector de *features* en el tiempo $t$ (las torsiones, ya centradas: $\langle\mathbf{x}\rangle=0$). Busca la combinación lineal $y(t) = \mathbf{v}^\top\mathbf{x}(t)$ con la **autocorrelación a un lag $\tau$** más alta:

$$
\rho(\mathbf{v},\tau) \;=\; \frac{\langle y(t)\,y(t+\tau)\rangle}{\langle y(t)^2\rangle}
$$

### 2.4 · La derivación, paso a paso

**Paso 1** — sustituye $y(t)=\mathbf{v}^\top\mathbf{x}(t)$ en el numerador. Como $y(t)y(t+\tau)$ es un escalar, se puede escribir como una forma cuadrática:

$$
y(t)\,y(t+\tau) = \big(\mathbf{v}^\top\mathbf{x}(t)\big)\big(\mathbf{x}(t+\tau)^\top\mathbf{v}\big) = \mathbf{v}^\top\, \mathbf{x}(t)\mathbf{x}(t+\tau)^\top\, \mathbf{v}
$$

**Paso 2** — toma valor esperado. Usando estacionariedad (no depende de $t$, solo de $\tau$):

$$
\langle y(t)y(t+\tau)\rangle = \mathbf{v}^\top \underbrace{\langle\mathbf{x}(t)\mathbf{x}(t+\tau)^\top\rangle}_{\displaystyle C(\tau)}\, \mathbf{v}
$$

$C(\tau)$ es la **matriz de covarianza desfasada**: en la posición $(i,j)$ guarda cuánto covarían la feature $i$ ahora con la feature $j$ dentro de $\tau$.

**Paso 3** — el denominador es el caso particular $\tau=0$:

$$
\langle y(t)^2\rangle = \mathbf{v}^\top \underbrace{\langle\mathbf{x}(t)\mathbf{x}(t)^\top\rangle}_{\displaystyle C(0)}\, \mathbf{v}
$$

$C(0)$ es la covarianza **instantánea** — exactamente la matriz que usa PCA.

$$
\rho(\mathbf{v},\tau) = \frac{\mathbf{v}^\top C(\tau)\,\mathbf{v}}{\mathbf{v}^\top C(0)\,\mathbf{v}}
$$

> [!important] Ya se ve la diferencia con PCA
> PCA maximiza $\mathbf{v}^\top C(0)\mathbf{v}$ solo — el numerador de tICA es $C(\tau)$, no $C(0)$: **premia que la señal sobreviva** un tiempo $\tau$, no que sea grande ahora.

### 2.5 · Maximizar el cociente

Es un cociente de Rayleigh generalizado. Deriva respecto a $\mathbf{v}$ e iguala a cero. Con $f=\mathbf{v}^\top C(\tau)\mathbf{v}$, $g=\mathbf{v}^\top C(0)\mathbf{v}$:

$$
\nabla\rho = \frac{g\,\nabla f - f\,\nabla g}{g^2} = 0 \;\;\Longrightarrow\;\; g\,\nabla f = f\,\nabla g
$$

Usando $\nabla(\mathbf{v}^\top A\mathbf{v}) = 2A\mathbf{v}$ para $A$ simétrica *(por eso $C(\tau)$ se simetriza en la práctica — ver aviso abajo)*:

$$
g\cdot 2C(\tau)\mathbf{v} = f\cdot 2C(0)\mathbf{v} \;\;\Longrightarrow\;\; C(\tau)\,\mathbf{v} = \frac{f}{g}\,C(0)\,\mathbf{v}
$$

Y $f/g = \rho(\mathbf{v},\tau)$ por definición. Llamando $\lambda\equiv\rho$:

$$
\boxed{\;C(\tau)\,\mathbf{v} = \lambda\, C(0)\,\mathbf{v}\;}
$$

> [!success] El problema de autovalores generalizado, y lo que significa
> Es exactamente el mismo tipo de ecuación que $A\mathbf{v}=\lambda\mathbf{v}$, salvo que ahora hay **dos** matrices. El autovector de **mayor** $\lambda$ es la dirección de máxima autocorrelación — y $\lambda$ mismo **es** el valor de esa autocorrelación en el óptimo.

> [!warning] Detalle técnico — por qué se simetriza $C(\tau)$
> $\langle\mathbf{x}(t)\mathbf{x}(t+\tau)^\top\rangle$ no es simétrica en general. PyEMMA la simetriza: $C(\tau)\to\frac{1}{2}[C(\tau)+C(\tau)^\top]$. Eso equivale a asumir que el proceso es **reversible** — la misma propiedad de balance detallado que vas a necesitar para estimar el MSM en la Clase 5. No es casualidad: es el mismo supuesto reapareciendo.

---

> [!question] **Q2 · N9** — ¿Por qué tICA maximiza $\mathbf{v}^\top C(\tau)\mathbf{v} / \mathbf{v}^\top C(0)\mathbf{v}$ en vez de maximizar solo $\mathbf{v}^\top C(0)\mathbf{v}$ (PCA)?
>
> **a)** Porque el cociente premia que la señal siga correlacionada tras un tiempo $\tau$, no solo que tenga amplitud grande ahora
> **b)** Porque $C(\tau)$ siempre da valores más grandes que $C(0)$, así que el cociente es más fácil de maximizar
> **c)** Porque $C(0)$ no es invertible cuando hay muchas features correlacionadas
> **d)** Porque maximizar solo $C(0)$ requiere más datos que maximizar el cociente

> [!success]- Respuesta Q2 → **a) Premia la persistencia, no la amplitud** ✓
> $C(\tau)$ mide cuánto covaría la señal *ahora* con la señal *dentro de $\tau$*. Una coordenada que se agita rápido tendrá $C(\tau)$ chico (ya se decorrelacionó) aunque $C(0)$ sea enorme. Una coordenada lenta mantiene $C(\tau)$ casi tan grande como $C(0)$. El cociente **es** la definición operativa de "lento".
> (b) es falsa en general — la autocorrelación decae con el tiempo, no crece. (c)/(d) son preocupaciones reales pero no la razón de diseño del método.

---

## 2.4 bis · El álgebra lineal, desde cero

*Pediste más detalle aquí — vamos despacio. Dos piezas: qué es una forma cuadrática y de dónde sale su gradiente, y qué significa que un problema de autovalores sea "generalizado".*

### Pieza 1 · ¿Qué es $\mathbf{v}^\top A\mathbf{v}$?

Para $\mathbf{v}\in\mathbb{R}^d$ y $A$ una matriz $d\times d$, la expresión $\mathbf{v}^\top A\mathbf{v}$ es un **número** (una matriz $1\times1$), y se calcula sumando sobre todos los pares de índices:

$$
\mathbf{v}^\top A \mathbf{v} \;=\; \sum_{i=1}^d\sum_{j=1}^d v_i\, A_{ij}\, v_j
$$

**Ejemplo concreto en 2D.** Sea $\mathbf{v}=(v_1,v_2)^\top$ y $A=\begin{pmatrix}a&b\\c&d\end{pmatrix}$. Multiplicando término a término:

$$
\mathbf{v}^\top A\mathbf{v} = a\,v_1^2 + (b+c)\,v_1v_2 + d\,v_2^2
$$

Si $A$ es simétrica ($b=c$), esto es $a v_1^2 + 2b\,v_1v_2 + d v_2^2$ — la misma **forma cuadrática** de precálculo, $ax^2+bxy+cy^2$, escrita con matrices.

> [!important] El significado que vas a usar sin parar
> Si $A=C(0)$ es una matriz de covarianza y $\mathbf{v}$ es un vector unitario, $\mathbf{v}^\top C(0)\mathbf{v}$ es literalmente **la varianza de los datos proyectados sobre la dirección $\mathbf{v}$**. Maximizar eso sobre todas las direcciones $\mathbf{v}$ es, por definición, **encontrar la primera componente principal — PCA**.
> Es la misma construcción algebraica; lo único que cambia entre PCA y tICA es *qué* matriz va en el numerador.

### Pieza 2 · De dónde sale $\nabla(\mathbf{v}^\top A\mathbf{v}) = 2A\mathbf{v}$

No lo tomes prestado — derívalo. Sea $h(\mathbf{v}) = \mathbf{v}^\top A \mathbf{v} = \sum_i\sum_j v_iA_{ij}v_j$. Quieres $\dfrac{\partial h}{\partial v_k}$, para cada coordenada $k$.

**Paso 1** — en la suma doble, $v_k$ aparece en **dos** lugares distintos: una vez como el factor $v_i$ (cuando $i=k$), y otra vez como el factor $v_j$ (cuando $j=k$). Deriva cada aparición por separado (regla del producto), tratando las demás $v$ como constantes:

$$
\frac{\partial h}{\partial v_k} = \underbrace{\sum_j A_{kj}v_j}_{\text{de la aparición } i=k} \;+\; \underbrace{\sum_i v_i A_{ik}}_{\text{de la aparición } j=k}
$$

**Paso 2** — reconoce cada suma. La primera es la componente $k$ del vector $A\mathbf{v}$. La segunda es la componente $k$ de $A^\top\mathbf{v}$ (porque suma $v_i$ contra la columna $k$ de $A$, que es la fila $k$ de $A^\top$):

$$
\frac{\partial h}{\partial v_k} = (A\mathbf{v})_k + (A^\top\mathbf{v})_k
$$

**Paso 3** — junta las $d$ componentes en un vector:

$$
\nabla h(\mathbf{v}) = A\mathbf{v} + A^\top\mathbf{v} = (A+A^\top)\mathbf{v}
$$

**Y aquí aparece, derivada y no asumida, la razón de simetrizar:** si $A=A^\top$ (simétrica), entonces $A+A^\top=2A$, y

$$
\boxed{\nabla(\mathbf{v}^\top A\mathbf{v}) = 2A\mathbf{v} \qquad \text{(solo si } A \text{ es simétrica)}}
$$

Si $A$ **no** fuera simétrica, el gradiente sería $(A+A^\top)\mathbf{v}$ — una fórmula más fea, y el problema de optimización ya no se reduciría limpiamente a un problema de autovalores. **Ésa** es la razón real de simetrizar $C(\tau)\to\frac12[C(\tau)+C(\tau)^\top]$: no es cosmético, es lo que hace que el Paso siguiente funcione.

### Pieza 3 · Ordinario vs. generalizado — qué significa la segunda matriz

Un problema de autovalores **ordinario** es $A\mathbf{v}=\lambda\mathbf{v}$: buscas direcciones que $A$ no rota, solo estira por un factor $\lambda$.

El de tICA es **generalizado**: $C(\tau)\mathbf{v} = \lambda\, C(0)\mathbf{v}$. Dice algo ligeramente distinto: *aplicar $C(\tau)$ a $\mathbf{v}$ da la misma dirección que aplicar $C(0)$ a $\mathbf{v}$*, solo reescalada por $\lambda$.

**¿Por qué no es simplemente un problema ordinario?** Porque hay una matriz de fondo, $C(0)$, que primero hay que "deshacer". Imagina un cambio de variable que **blanquea** los datos — que hace que la covarianza instantánea sea la identidad:

$$
\mathbf{w} \equiv C(0)^{-1/2}\,\mathbf{x}
\qquad\Longrightarrow\qquad
\langle \mathbf{w}\mathbf{w}^\top\rangle = C(0)^{-1/2}\,C(0)\,C(0)^{-1/2} = I
$$

*(Aquí $C(0)^{-1/2}$ es la raíz cuadrada de la matriz — existe y es simétrica porque $C(0)$ es una covarianza, sim\'etrica y positiva.)*

En las coordenadas blanqueadas $\mathbf{w}$, la covarianza desfasada se transforma igual:

$$
\tilde C(\tau) \equiv \langle\mathbf{w}(t)\mathbf{w}(t+\tau)^\top\rangle = C(0)^{-1/2}\,C(\tau)\,C(0)^{-1/2}
$$

y **sigue siendo simétrica** (conjugar una matriz simétrica por otra simétrica preserva la simetría). Ahora, en el espacio blanqueado, buscar la dirección de mayor autocorrelación es un problema **ordinario**:

$$
\tilde C(\tau)\,\mathbf{u} = \lambda\,\mathbf{u}
$$

> [!success] La imagen completa, en una frase
> **tICA = blanquear con $C(0)$ (borrar el sesgo de PCA hacia "mucha amplitud") y luego diagonalizar $C(\tau)$ (encontrar lo que persiste).** El problema generalizado $C(\tau)\mathbf{v}=\lambda C(0)\mathbf{v}$ es exactamente esos dos pasos comprimidos en una sola ecuación — se resuelve así en la práctica por estabilidad numérica, sin blanquear explícitamente, pero la intuición es esa.

Por el teorema espectral (matrices simétricas tienen autovalores reales y autovectores ortogonales), $\tilde C(\tau)$ tiene $\lambda$ reales garantizados — y por tanto también el problema generalizado original.

---

> [!question] **Q3 · álgebra lineal** — Si $A$ **no** fuera simétrica, ¿qué le pasaría a la derivación de la Clase 2 (Paso 2, donde $V(\xi(\mathbf{r}))$ salía de la integral) y a esta de tICA (el gradiente $=2A\mathbf{v}$)?
>
> **a)** Son problemas distintos: la de Clase 2 no depende de simetría; la de tICA sí, y sin ella el gradiente sería $(A+A^\top)\mathbf{v}$, más complicado
> **b)** Ambas dejarían de funcionar exactamente igual, porque las dos dependen de la misma propiedad de simetría
> **c)** Ninguna de las dos depende de la simetría de ninguna matriz
> **d)** La de Clase 2 fallaría; la de tICA seguiría dando $2A\mathbf{v}$ sin cambios

> [!success]- Respuesta Q3 → **a) Son problemas distintos** ✓
> La derivación de la Clase 2 es **combinatoria**: depende solo de que $V$ sea constante en el dominio filtrado por la delta. $V$ ni siquiera es una matriz — esa derivación no sabe qué es simetría.
> La de tICA sí depende de simetría, de forma concreta: dedujiste que $\nabla(\mathbf{v}^\top A\mathbf{v}) = (A+A^\top)\mathbf{v}$ en general, y colapsa a $2A\mathbf{v}$ solo si $A=A^\top$.
> **La trampa útil de esta pregunta:** dos derivaciones pueden *parecerse* (ambas "simplifican una expresión") corriendo sobre maquinaria completamente distinta. Vale la pena parar a mirar *qué* está haciendo cada paso, no solo que "algo se simplificó".

---

## 2.5 · Cerrando la maximización

Con las tres piezas del §2.4 bis ya en mano, el argumento del §2.3 queda completo y sólido: maximizar $\rho(\mathbf{v},\tau)=\dfrac{\mathbf{v}^\top C(\tau)\mathbf{v}}{\mathbf{v}^\top C(0)\mathbf{v}}$ por cálculo directo da

$$
\nabla\rho=0 \;\;\Longrightarrow\;\; C(\tau)\mathbf{v} = \frac{\mathbf{v}^\top C(\tau)\mathbf{v}}{\mathbf{v}^\top C(0)\mathbf{v}}\,C(0)\mathbf{v} = \lambda\,C(0)\mathbf{v}
$$

con $\lambda=\rho(\mathbf{v},\tau)$ el valor de la autocorrelación en el óptimo. El autovector de mayor $\lambda$ es la **primera componente independiente en el tiempo**; el segundo mayor, la segunda; etc.

---

## 3 · La conexión que se retomará en la Clase 5

### Motivación

Ya sabes construir $\lambda$. Pregunta: ¿qué **significa** $\lambda$ físicamente, más allá de "la autocorrelación óptima"?

### Establecer

Si un modo se relaja exponencialmente con tiempo característico $t_{\text{relax}}$ — es decir $y(t)\sim y(0)\,e^{-t/t_{\text{relax}}}$ — entonces su autocorrelación a lag $\tau$ es, tomando el promedio estacionario,

$$
\rho(\tau) = \frac{\langle y(t)y(t+\tau)\rangle}{\langle y(t)^2\rangle} = e^{-\tau/t_{\text{relax}}}
$$

*(Es la misma forma que ya usaste en la Clase 1 para tiempos de espera exponenciales — no es una coincidencia notacional, es el mismo tipo de relajación.)*

Como $\lambda$ **es** $\rho(\tau)$ en el óptimo:

$$
\lambda = e^{-\tau/t_{\text{relax}}} \;\;\Longrightarrow\;\; \ln\lambda = -\frac{\tau}{t_{\text{relax}}} \;\;\Longrightarrow\;\; \boxed{t_{\text{relax}} = -\frac{\tau}{\ln\lambda}}
$$

### Conectar

> [!important] La misma fórmula reaparece
> $t=-\tau/\ln\lambda$ es exactamente la fórmula de **tiempos implícitos** que vuelve a aparecer, sin cambiar ni un símbolo, cuando construyas el MSM en la Clase 5. No es casualidad notacional — hay una razón matemática profunda, y vale la pena verla ahora.

Verificado en la literatura: tICA (bajo el nombre **VAC**, *variational approach to conformational dynamics*, Noé \& Nüske) y el MSM son **dos aproximaciones del mismo objeto**: el **operador de transferencia** de la dinámica subyacente — el operador que propaga una distribución de probabilidad un tiempo $\tau$ hacia adelante. tICA lo aproxima con una base de funciones **lineales** (las combinaciones $\mathbf{v}^\top\mathbf{x}$); el MSM lo aproxima con una base de funciones **indicador** (una por microestado). Distinta base, mismo operador — por eso ambos autovalores se traducen a tiempos con la misma fórmula.

> [!success] Por qué esto no es trivia
> Es la razón estructural de que el pipeline tenga sentido encadenar tICA $\to$ MSM: no son dos técnicas pegadas con cinta — son **dos aproximaciones sucesivas y cada vez más finas del mismo objeto matemático**.

\Fuente{Nüske, tesis doctoral FU Berlin (2017); Pérez-Hernández \& Noé, \textit{JCTC} \textbf{12}:6118 (2016) — verificado.}

---

> [!question] **Q4 · N9** — Con $\lambda=0.7$ y un lag $\tau=10$ ns, ¿cuál es el tiempo característico del modo?
>
> **a)** $\approx 28$ ns
> **b)** $\approx 7$ ns
> **c)** $\approx 10$ ns
> **d)** $\approx 3.5$ ns

> [!success]- Respuesta Q4 → **a) $\approx 28$ ns** ✓
> $$\ln(0.7)=-0.357 \;\;\Longrightarrow\;\; t = \frac{-10}{-0.357} = 28.0\ \text{ns}$$
> **Dirección del efecto, contraintuitiva la primera vez:** $\lambda$ cerca de 1 (poco decaimiento en un lag) $\Rightarrow$ tiempo **largo** — memoria persistente. $\lambda$ cerca de 0 $\Rightarrow$ tiempo **corto** — memoria que se pierde rápido dentro de la ventana de observación.
> Vas a reusar esta lectura sin cambiar nada cuando el MSM reporte sus propios autovalores en la Clase 5.

---

## 4 · Las features del paper, y la asimetría que ya conocías

Con la maquinaria completa, los detalles concretos del paper se leen directo:

|                 |                                                       |
| --------------- | ----------------------------------------------------- |
| **Features**    | torsiones de *backbone* de **CDR1, CDR3 y HV2**       |
| **Lag de tICA** | **10 ns** — distinto del lag del MSM (15 ns, Clase 5) |
| Software        | PyEMMA 2                                              |

> [!danger] La asimetría, ahora vista desde tICA
> En la Clase 2 estableciste, mecánicamente, que el sesgo de metadinámica **solo empujó** átomos de CDR1 y CDR3 ($\nabla_{\mathbf{r}_i}\xi=\mathbf{0}$ para todo lo demás). HV2 corrió MD clásica pura.
>
> Ahora ves la otra mitad: **HV2 sí es una *feature* de tICA.** Entra en $\mathbf{x}(t)$, contribuye a $C(\tau)$ y $C(0)$, y por tanto a qué dirección $\mathbf{v}$ resulta "la más lenta". Si el movimiento verdaderamente lento de HV2 nunca se visitó — porque nadie lo sesgó — **tICA no puede encontrarlo**: solo puede ordenar por lentitud lo que efectivamente está en los datos.
>
> Es la misma vulnerabilidad de siempre (`N5`, elegir CVs), vista ahora en la etapa de análisis en vez de en la de muestreo.

---

> [!question] **Q5 · cierre de Clase 4** — Si el movimiento lento de HV2 nunca se muestreó porque nunca se sesgó, ¿qué le pasa a la proyección tICA?
>
> **a)** tICA no puede encontrar ese modo — solo puede ordenar por lentitud los movimientos que sí están en los datos
> **b)** tICA lo reconstruye igual, porque no depende de qué se sesgó en la metadinámica
> **c)** tICA falla catastróficamente y no converge en absoluto
> **d)** tICA lo detecta como el modo más lento de todos, precisamente por estar submuestreado

> [!success]- Respuesta Q5 → **a) No puede encontrar ese modo** ✓
> tICA es puramente **estadístico** sobre los datos que existen: construye $C(\tau)$ y $C(0)$ de los frames simulados. Si un movimiento de HV2 nunca ocurrió, no hay variación de ese tipo para que $C(\tau)$ la capture. tICA no inventa modos — solo **ordena por lentitud** lo que sí está presente.
>
> Conecta con la Clase 3: un modelo posterior "solo puede reponderar los estados que alguien visitó". Aquí la versión es: **solo puede ordenar lo que alguien visitó.**
>
> El error es más peligroso que un fallo obvio: **todo converge, todo compila** — y aun así falta información. Nada en el output de tICA te avisa.

---

## Resumen — Clase 4

### La cadena de razonamiento

$$
\text{PCA maximiza } \mathbf{v}^\top C(0)\mathbf{v}
\;\xrightarrow{\text{no distingue lento de amplio}}\;
\text{tICA maximiza } \frac{\mathbf{v}^\top C(\tau)\mathbf{v}}{\mathbf{v}^\top C(0)\mathbf{v}}
\;\xrightarrow{\nabla\rho=0}\;
C(\tau)\mathbf{v}=\lambda C(0)\mathbf{v}
\;\xrightarrow{\lambda=e^{-\tau/t}}\;
t=-\frac{\tau}{\ln\lambda}
$$

### Resultados

| | Fórmula |
|---|---|
| Autocorrelación a maximizar | $\rho(\mathbf{v},\tau) = \mathbf{v}^\top C(\tau)\mathbf{v} \,/\, \mathbf{v}^\top C(0)\mathbf{v}$ |
| Problema de autovalores | $C(\tau)\mathbf{v}=\lambda C(0)\mathbf{v}$ |
| Gradiente de una forma cuadrática | $\nabla(\mathbf{v}^\top A\mathbf{v}) = (A+A^\top)\mathbf{v}$, $=2A\mathbf{v}$ si $A$ simétrica |
| Blanqueo | $\mathbf{w}=C(0)^{-1/2}\mathbf{x} \Rightarrow \tilde C(\tau)\mathbf{u}=\lambda\mathbf{u}$ (ordinario) |
| Tiempo característico | $t=-\tau/\ln\lambda$ — misma fórmula que reaparecerá en el MSM |

### Nodos

| Nodo | Contenido | ✓ |
|---|---|---|
| `N8` | MD sembrada sin sesgo; hereda $w_i\ne\pi_i$ | Q1 |
| `N9` | tICA: autocorrelación, no varianza; problema generalizado; conexión VAC↔MSM | Q2, Q3, Q4, Q5 |

### Álgebra y cálculo reforzados a pedido

- Forma cuadrática $\mathbf{v}^\top A\mathbf{v}$ desde cero, con el caso 2D explícito
- Gradiente de una forma cuadrática, derivado componente a componente
- Por qué "generalizado" — el blanqueo con $C(0)^{-1/2}$ como ordinario disfrazado
- Derivación de $t=-\tau/\ln\lambda$ desde la relajación exponencial (Clase 1 revisitada)

> [!abstract] Adónde va esto — Clase 5
> Ya sabes proyectar el paisaje sobre lo lento. Falta convertir esa proyección en **poblaciones y tiempos de verdad**: el Markov State Model. Ahí se demuele **M2** («$\tau$ es una propiedad del sistema» — no, es una perilla que eliges tú), se construye $T(\tau)$, y se cierra el nodo más importante del curso: por qué $\pi$ **no depende de dónde sembraste**.
