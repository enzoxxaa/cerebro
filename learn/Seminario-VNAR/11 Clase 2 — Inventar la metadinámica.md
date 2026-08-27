---
tipo: clase
proyecto: seminario
fecha: 2026-08-26
clase: 2
nodos: [M1, N3, N4]
hebras: [metadinámica, termodinámica estadística]
modo: socrático
estado: en curso
resumen: "Clase 2: derivar la metadinámica desde cero — qué hace un sesgo, el problema del huevo y la gallina, el sesgo adaptativo, y por qué hace falta well-tempered"
tags:
  - seminario
  - clase
  - metadinamica
---

# 11 · Clase 2 — Inventar la metadinámica

← [[00 MOC — Seminario VNAR]] · anterior: [[10 Clase 1 — El problema y el pivote]]

**Nodos:** demoler **M1** + `N3` (molde negativo) + `N4` (well-tempered, $\gamma$).
**Modo:** socrático. El objetivo no es que sepas qué es la metadinámica — es que la **reinventes**.

---

## 0 · Dónde estamos

De la Clase 1, el problema quedó planteado con precisión quirúrgica:

| Restricción                                    | Origen                                   |
| ---------------------------------------------- | ---------------------------------------- |
| Hay que cruzar barreras de $\approx 40$ kJ/mol | `R1` — con 100 ns solo llegas a ~22      |
| Esperando mucho menos de $150\ \mu$s por cruce | Q2                                       |
| Sin destruir las poblaciones al hacerlo        | **M3** — $\hat F = F - RT\ln(w_i/\pi_i)$ |

Esa tercera línea es la que hace el problema difícil. Acelerar es fácil si no te importa arruinar la termodinámica. **Acelerar y poder volver** es el problema real.

> [!question] Piénsalo antes de seguir leyendo *(no es un quiz — no hay una única respuesta)*
> Tienes un sistema atrapado en un pozo del que tardaría $150\ \mu$s en salir. Solo puedes simular 100 ns. **Enumera las palancas que existen.** ¿Qué puedes tocar?
>
> Literalmente hay pocas: la temperatura, el potencial, la masa, la geometría de la caja, y el número de copias del sistema. Nada más — eso es todo lo que un integrador de MD conoce.

---

## 1 · Palanca 1: la temperatura *(demolición de M1)*

Es la primera que a casi todo el mundo se le ocurre, y **es una idea legítima**. Vamos a evaluarla en serio antes de descartarla, porque entender exactamente por qué **no** es la metadinámica es lo que hace que la metadinámica se entienda.

### 1.1 · ¿Funciona? Sí

Simplificando a un paisaje de energía potencial $\Delta U^{\ddagger}$, la tasa a temperatura $T'$ es

$$
k(T') = \kappa\,\frac{k_B T'}{h}\, e^{-\Delta U^{\ddagger}/RT'}
$$

Con $\Delta U^{\ddagger} = 40$ kJ/mol, comparemos 300 K y 600 K paso a paso:

$$
\textbf{300 K:}\quad RT = 2.494 \Rightarrow \frac{40}{2.494} = 16.04 \Rightarrow e^{-16.04} = 1.08\times10^{-7}
$$
$$
k_{300} = 6.25\times10^{12}\times 1.08\times10^{-7} = 6.75\times10^{5}\ \text{s}^{-1}
$$

$$
\textbf{600 K:}\quad RT' = 4.988 \Rightarrow \frac{40}{4.988} = 8.02 \Rightarrow e^{-8.02} = 3.28\times10^{-4}
$$
$$
k_{600} = 1.25\times10^{13}\times 3.28\times10^{-4} = 4.10\times10^{9}\ \text{s}^{-1}
$$

$$
\frac{k_{600}}{k_{300}} = \frac{4.10\times10^{9}}{6.75\times10^{5}} \approx \mathbf{6000\times}
$$

**Sí funciona.** Duplicar $T$ acelera cuatro órdenes de magnitud. La idea no es tonta.

### 1.2 · ¿Por qué no sirve aquí? Tres razones, y ninguna es trivial

> [!danger] Razón 1 · Acelera **todo**, indiscriminadamente
> El factor $e^{-\Delta U^{\ddagger}/RT'}$ se aplica a **cualquier** barrera del sistema. No hay forma de acelerar la torsión de CDR3 sin acelerar también el desplegamiento de las hebras β, la evaporación del agua y la rotura de los puentes de hidrógeno del núcleo.
> A 600 K no tienes un VNAR con lazos móviles: tienes un VNAR **desnaturalizado**. Y las poblaciones conformacionales de una proteína desplegada no te dicen nada sobre la plegada.

> [!danger] Razón 2 · Muestreas la distribución **equivocada**, y volver es caro
> A $T'$ obtienes $p_{T'} \propto e^{-\beta' U}$, pero quieres $p_T \propto e^{-\beta U}$. Reponderar requiere pesos
> $$w(\mathbf{r}) \;\propto\; \frac{e^{-\beta U}}{e^{-\beta' U}} \;=\; e^{-(\beta - \beta')\,U(\mathbf{r})}$$
> El problema: $U$ es **extensiva** — crece con el número de átomos. Tu sistema tiene ~30 000 átomos, así que $U \sim 10^5$ kJ/mol y sus fluctuaciones $\sigma_U \sim \sqrt{N}$ son enormes. Un peso $e^{-\Delta\beta\,U}$ con $U$ fluctuando así tiene **varianza exponencialmente grande**: en la práctica un puñado de frames se lleva todo el peso y el resto no cuenta.
> Este es exactamente el motivo por el que **REMD existe**: en vez de un salto grande de temperatura, monta una **escalera** de réplicas con saltos pequeños, donde los solapamientos sí son manejables. El precio es que el número de réplicas escala como $\sqrt{N_{\text{átomos}}}$.

> [!danger] Razón 3 · No puedes **apuntar**
> La temperatura es un escalar global. No tiene forma de saber que a ti te interesan $\psi_{\text{CDR1}}$ y $\psi_{\text{CDR3}}$ y nada más.

### 1.3 · El veredicto sobre M1

> [!warning] Demolición de M1 — con precisión
> «Subir la temperatura» **no es** la metadinámica. Es otro método, con nombre propio: **replica exchange MD (REMD / parallel tempering)**.
>
> Y no es un método inferior — tiene una virtud enorme que la metadinámica **no** tiene: **no hay que elegir variables colectivas.** Guárdate eso, porque es la base del ataque [[01 Plan de aprendizaje#4. De qué nodo sale cada crítica|A10]]: toda la vulnerabilidad de A2 (HV2 sin sesgar) existe *porque* la metadinámica obliga a comprometerse con unas CVs de antemano. REMD no tiene ese problema.
>
> Son **dos filosofías distintas** para el mismo problema:
>
> | | REMD | Metadinámica |
> |---|---|---|
> | Qué modifica | la **temperatura** | el **potencial** |
> | Selectividad | ninguna (global) | dirigida a las CVs |
> | ¿Elegir CVs? | **no** | **sí** — y ahí está el riesgo |
> | Coste | $\propto\sqrt{N_{\text{átomos}}}$ réplicas | una sola trayectoria |
> | Reponderar | pesos de varianza alta | el sesgo se conoce exactamente |

---

## 2 · Palanca 2: el potencial. ¿Qué hace exactamente un sesgo?

Descartada la temperatura, la única otra palanca que toca la termodinámica es $U$ misma. Añadamos un término y **derivemos** qué pasa — sin suponer nada.

### 2.1 · El montaje

Añadimos al potencial un término que depende de $\mathbf{r}$ **solo a través de la CV**:

$$
U_V(\mathbf{r}) \;=\; U(\mathbf{r}) \;+\; V\big(\xi(\mathbf{r})\big)
$$

Que dependa solo de $\xi$ es la condición crucial, y ahora verás por qué.

### 2.2 · La derivación, paso a paso

Aplicamos la definición de densidad marginal (Clase 1 §1.2) al sistema sesgado:

$$
p_V(s) \;=\; \frac{1}{Z_V}\int e^{-\beta\left[\,U(\mathbf{r}) + V(\xi(\mathbf{r}))\,\right]}\;\delta\!\big(\xi(\mathbf{r}) - s\big)\; d\mathbf{r}
$$

**Paso 1** — separar la exponencial, usando $e^{a+b} = e^a e^b$:

$$
p_V(s) \;=\; \frac{1}{Z_V}\int e^{-\beta U(\mathbf{r})}\; e^{-\beta V(\xi(\mathbf{r}))}\;\delta\!\big(\xi(\mathbf{r}) - s\big)\, d\mathbf{r}
$$

**Paso 2** — *el truco*. La delta $\delta(\xi(\mathbf{r}) - s)$ anula el integrando salvo donde $\xi(\mathbf{r}) = s$. Luego **en todo el dominio que sobrevive**, $V(\xi(\mathbf{r})) = V(s)$: una constante. Y una constante sale de la integral:

$$
p_V(s) \;=\; \frac{e^{-\beta V(s)}}{Z_V}\int e^{-\beta U(\mathbf{r})}\;\delta\!\big(\xi(\mathbf{r}) - s\big)\, d\mathbf{r}
$$

**Paso 3** — reconocer que la integral que queda es, por definición, $Z \cdot p_{\text{eq}}(s)$:

$$
p_V(s) \;=\; \frac{Z}{Z_V}\; e^{-\beta V(s)}\; p_{\text{eq}}(s)
$$

Como $Z/Z_V$ no depende de $s$, es solo normalización:

$$
\boxed{\;p_V(s) \;\propto\; p_{\text{eq}}(s)\; e^{-\beta V(s)}\;}
$$

### 2.3 · La misma ecuación, en energías libres

Toma $-RT\ln$ de ambos lados. Usando $\ln(ab) = \ln a + \ln b$ y $\ln e^{x} = x$:

$$
-RT\ln p_V(s) \;=\; \underbrace{-RT\ln p_{\text{eq}}(s)}_{F(s)} \;\underbrace{-\,RT\cdot\left(-\beta V(s)\right)}_{+\,V(s)} \;+\;\text{const}
$$

$$
\boxed{\;F_V(s) \;=\; F(s) \;+\; V(s) \;+\;\text{const}\;}
$$

> [!success] Nodo `N3` — la relación fundamental de todo el muestreo sesgado
> **El paisaje que el sistema siente es, literalmente, el verdadero más el sesgo.** Se suman punto a punto.
>
> Y fíjate en el contraste con la temperatura: aquí el sesgo $V(s)$ es una función **que tú escribes y conoces exactamente**. No hay que estimarlo, no fluctúa con $N$, no tiene varianza. Por eso volver del mundo sesgado al real es barato — y por eso esta palanca es la buena.

---

> [!question] **Q1 · N3** — De $F_V(s) = F(s) + V(s)$: ¿qué sesgo $V(s)$ hace que el sistema muestree **uniformemente** la CV, sin barreras de ningún tipo?
>
> **a)** $V(s) = -F(s)$
> **b)** $V(s) = +F(s)$
> **c)** $V(s) = -\dfrac{1}{F(s)}$
> **d)** $V(s) = e^{-\beta F(s)}$
EOF
echo OK
> [!success]- Respuesta Q1 → **a) $V(s) = -F(s)$** ✓
> $$F_V(s) = F(s) + V(s) = F(s) - F(s) = 0$$
> Paisaje efectivo **plano**. Sin mínimos ni barreras: el sistema difunde libremente por la CV.
>
> **El sesgo es un molde negativo del paisaje.** Donde $F$ tiene un pozo, $V$ pone un montículo que lo rellena; donde $F$ tiene una cima, $V$ pone un hueco.
>
> Y ahora fíjate en lo que apareció **solo**, sin que nadie lo introdujera. La misma ecuación leída al revés:
> $$V(s) = -F(s) \qquad\Longleftrightarrow\qquad F(s) = -V(s)$$
>
> > [!success] El sesgo óptimo no es solo una herramienta de aceleración: **es una medida de $F$**
> > Si logras construir el sesgo que aplana el paisaje, entonces **ya conoces el paisaje**: está en el sesgo, cambiado de signo.
> > **Acelerar y medir resultan ser la misma operación.** Eso no hay que memorizarlo — es una línea de álgebra.
>
> **Pero** para construir $V=-F$ necesitas conocer $F$… que es justo lo que no sabes. **Huevo y gallina.** Resolver eso es la metadinámica.
>
> Sobre **(b)**: $V=+F$ duplicaría el paisaje, los pozos serían el doble de profundos y quedarías **más** atrapado. El signo importa.

---

## 2.2 bis · Desmontando el «truco» de la delta

*Duda de Enzo, y es la duda correcta: el Paso 2 es donde está toda la sustancia.*

### El nudo real: $\mathbf{r}$ contra $s$

Antes del álgebra, hay que tener clarísimo que **son objetos de naturaleza distinta**:

| | $\mathbf{r}$ | $s$ |
|---|---|---|
| Qué es | la configuración **completa** del sistema | el valor de **una** variable colectiva |
| Tamaño | $3N \approx 90\,000$ números | **1** número |
| Contiene | posición de cada átomo: proteína, aguas, todo | p. ej. «$\psi_{27} = -1.2$ rad» |

Y están unidos por la **función** $\xi$:

$$
\xi:\;\mathbb{R}^{3N}\;\longrightarrow\;\mathbb{R},
\qquad
\mathbf{r}\;\longmapsto\;s=\xi(\mathbf{r})
$$

> [!important] $\xi$ es masivamente **muchos-a-uno**
> Un número astronómico de configuraciones $\mathbf{r}$ distintas dan **el mismo** $s$: todas las posiciones posibles de las aguas, todas las vibraciones, todo el resto de la proteína — con tal de que ese ángulo valga $-1.2$ rad.
> **$\mathbf{r}$ es el mundo entero. $s$ es lo único que decidiste mirar.**

### Qué hace realmente $\delta(\xi(\mathbf{r}) - s)$

Es un **filtro**, y nada más. La forma más honesta de leerlo es en versión discreta:

$$
\int f(\mathbf{r})\;\delta\big(\xi(\mathbf{r})-s\big)\,d\mathbf{r}
\qquad\Longleftrightarrow\qquad
\sum_{\substack{\mathbf{r}\ \text{tales que}\\ \xi(\mathbf{r})=s}} f(\mathbf{r})
$$

O sea: **«suma $f$ solo sobre las configuraciones cuyo valor de CV es exactamente $s$»**. La delta es notación para restringir el dominio.

### Y ahora el paso, en versión discreta

Queremos ver por qué $V$ sale de la integral. Escribimos la suma **solo** sobre el conjunto que sobrevive al filtro:

$$
\sum_{\substack{\mathbf{r}:\;\xi(\mathbf{r})=s}} e^{-\beta U(\mathbf{r})}\; e^{-\beta V(\xi(\mathbf{r}))}
$$

Mira el segundo factor. Estamos sumando **solo** sobre $\mathbf{r}$ con $\xi(\mathbf{r})=s$. Luego, **para cada uno de esos términos**:

$$
V(\xi(\mathbf{r})) \;=\; V(s)
$$

No es una aproximación: es sustituir $\xi(\mathbf{r})$ por su valor, que el filtro ya fijó. Y $V(s)$ **no contiene $\mathbf{r}$** — es el mismo número en todos los términos de la suma. Un factor común sale fuera:
t
$$
\sum_{\mathbf{r}:\;\xi(\mathbf{r})=s} e^{-\beta U(\mathbf{r})}\,e^{-\beta V(s)}
\;=\;
e^{-\beta V(s)}\sum_{\mathbf{r}:\;\xi(\mathbf{r})=s} e^{-\beta U(\mathbf{r})}
$$

Es exactamente $\sum_i a_i c = c\sum_i a_i$. Nada más profundo que eso.

### La analogía que lo fija

> [!tip] Estudiantes y matrícula
> - $\mathbf{r}$ = **un estudiante concreto** (con su nombre, edad, notas… muchísima información)
> - $\xi$ = la función **«¿en qué curso estás?»** — aplasta todo un estudiante a un número
> - $s = 3$ → **tercer curso**
> - $\delta(\xi(\mathbf{r}) - 3)$ = **filtra: quédate solo con los de tercero**
> - $U(\mathbf{r})$ = **la nota media** de ese estudiante → distinta para cada uno ❌ no sale de la suma
> - $V(\xi(\mathbf{r}))$ = **la matrícula de su curso** → ¡todos los de tercero pagan **lo mismo**! ✅ sale de la suma
>
> «Suma la matrícula de todos los de tercero» $=$ «matrícula de tercero» $\times$ «cuántos de tercero hay».
>
> **Eso es el Paso 2.** $V$ sale porque es constante **dentro del grupo seleccionado**, aunque varíe entre grupos.

### Por qué esto es la condición de diseño de todo el método

Recuerda cómo definimos el sesgo:

$$U_V(\mathbf{r}) = U(\mathbf{r}) + V\big(\xi(\mathbf{r})\big)$$

$V$ depende de $\mathbf{r}$ **solo a través de $\xi$**. Si hubiéramos permitido un sesgo general $V(\mathbf{r})$ —distinto para cada configuración— el Paso 2 **sería imposible**, no habría factor común, y no existiría la relación limpia $F_V = F + V$.

> [!success] En una frase
> **La razón de que la metadinámica funcione es que el sesgo se define sobre la CV y no sobre las coordenadas.** Esa restricción es lo que hace que el sesgo se pueda separar exactamente, y por tanto quitar exactamente después.

→ Notación completa en [[30 Glosario de símbolos]].

---

> [!question] **Q2 · comprensión del Paso 2** — ¿Por qué $V(\xi(\mathbf{r}))$ puede salir de la integral y $e^{-\beta U(\mathbf{r})}$ no?
>
> **a)** Porque la delta fuerza $\xi(\mathbf{r})=s$, y entonces $V(\xi(\mathbf{r}))$ vale $V(s)$ en todo el dominio que sobrevive
> **b)** Porque $V$ no depende de las coordenadas atómicas, sino solo del tiempo de simulación
> **c)** Porque $V$ es un potencial externo, y los potenciales externos son constantes en cualquier integral
> **d)** Porque el valor medio de $V$ sobre el dominio de integración es igual a $V(s)$

---

## 3 · Resolver el huevo y la gallina

### 3.1 · El callejón

Queremos $V = -F$. Para construirlo necesitamos $F$. Pero $F$ es lo que queremos medir.

**Salida:** no construir $V$ de golpe. **Construirlo poco a poco, usando lo único que sí tenemos: por dónde ha pasado el sistema.**

### 3.2 · La receta

Cada $\tau_G$ pasos, deposita una gaussiana centrada en **donde está el sistema ahora**:

$$
V(s,t) \;=\; \sum_{\substack{t' = \tau_G,\,2\tau_G,\,\dots \\ t' < t}} W \,\exp\!\left[-\frac{\big(s - \xi(\mathbf{r}(t'))\big)^2}{2\sigma^2}\right]
$$

Léelo literalmente: **el sistema va dejando arena donde pisa.** Los tres parámetros son los del paper:

| Símbolo | Qué es | Valor en el paper |
|---|---|---|
| $W$ | altura de cada gaussiana | 10 kJ/mol |
| $\sigma$ | anchura | 0.3 rad |
| $\tau_G$ | cada cuánto se deposita | 1000 pasos $\times$ 2 fs $=$ **2 ps** |

### 3.3 · ¿Por qué converge a $-F$? El bucle de realimentación

Aquí está el argumento, y es puramente auto-consistente.

La arena se deposita **donde está el sistema**. Y la probabilidad de que el sistema esté en $s$ es $p_V(s)$ — la distribución **sesgada**, porque el sesgo ya construido influye en dónde está ahora. Luego la tasa de deposición en cada punto es:

$$
\frac{\partial V(s,t)}{\partial t} \;\propto\; p_V(s,t) \;\propto\; p_{\text{eq}}(s)\,e^{-\beta V(s,t)}
$$

y usando $p_{\text{eq}} \propto e^{-\beta F}$:

$$
\boxed{\;\frac{\partial V(s,t)}{\partial t} \;\propto\; e^{-\beta\left[\,F(s) \,+\, V(s,t)\,\right]}\;}
$$

Esta ecuación **es** la metadinámica. Y contiene su propia solución:

- Donde $F$ es **bajo** (pozo profundo) → el sistema pasa **mucho** tiempo → se deposita **rápido** → $V$ sube deprisa ahí.
- Donde $F$ es **alto** (cima) → el sistema pasa **poco** tiempo → se deposita **despacio**.
- Conforme $V$ crece en el pozo, la suma $F+V$ sube ahí, y la tasa de deposición **cae**.

**El bucle se autorregula.** Y se detiene exactamente cuando la tasa es la misma en todas partes:

$$
\frac{\partial V}{\partial t}\ \text{independiente de } s
\iff
F(s)+V(s) = \text{const}
\iff
V(s) = -F(s) + \text{const}
$$

> [!success] Nodo `N3` — el molde negativo
> El método converge **al sesgo que buscábamos**, y lo hace sin conocer $F$ de antemano. La realimentación hace el trabajo.
> Y como $V \to -F$, el sesgo acumulado **es la medida** de la energía libre.

### 3.4 · Pero hay un problema serio: la deposición nunca para

Mira otra vez la ecuación. Cuando el paisaje ya está plano, $\partial V/\partial t$ es **la misma en todas partes** — pero **no es cero**. La arena sigue cayendo, al ritmo constante $W/\tau_G$.

¿Qué pasa entonces? $V$ sigue creciendo de forma aproximadamente uniforme. En principio un desplazamiento uniforme es inofensivo (no cambia las fuerzas). En la práctica **no lo es**, y por dos motivos:

1. **El sistema se escapa.** Con el paisaje relevante ya relleno, el sistema empieza a subir a regiones de $F$ altísimo — conformaciones absurdas, lazos estirados, contactos rotos. Y una vez allí, deposita arena **también allí**, lo que lo empuja aún más lejos.
2. **El sesgo nunca se estabiliza.** $V(s,t)$ oscila alrededor de $-F(s) + c(t)$, y esas oscilaciones **no se amortiguan**. No hay un instante en el que puedas decir «ya convergió, leo $F = -V$».

### 3.5 · La magnitud del desastre, con los números del paper

$$
\text{Tasa de deposición} = \frac{W}{\tau_G} = \frac{10\ \text{kJ/mol}}{2\ \text{ps}}
$$

En la simulación de $1\ \mu\text{s} = 10^{6}$ ps que corre el paper, el número de gaussianas es

$$
\frac{10^{6}\ \text{ps}}{2\ \text{ps}} = 500\,000\ \text{gaussianas}
$$

Si **todas** cayeran a altura completa, el sesgo total acumulado sería

$$
500\,000 \times 10\ \tfrac{\text{kJ}}{\text{mol}} = 5\times10^{6}\ \tfrac{\text{kJ}}{\text{mol}}
$$

> [!danger] Compara con la barrera que querías cruzar: **40 kJ/mol**
> $$\frac{5\times10^{6}}{40} \approx 125\,000$$
> Depositarías **ciento veinticinco mil veces** la altura de la barrera. Eso no es rellenar un pozo: es sepultar la proteína bajo una montaña de sesgo y mandarla a explorar geometrías que no existen.
>
> **Por eso la metadinámica estándar no se usa así, y por eso hace falta well-tempered.** No es un refinamiento cosmético: sin él, estos parámetros son inservibles.

---

> [!question] **Q3 · N3** — ¿Cuál es el problema de la metadinámica **estándar** (gaussianas de altura fija)?
>
> **a)** El sesgo nunca deja de crecer, así que el sistema acaba explorando regiones irrelevantes de alta energía
> **b)** El sesgo converge, pero a un múltiplo incorrecto de $F$
> **c)** El sesgo deja de depositarse al alcanzar la altura de la barrera más alta
> **d)** El sesgo empuja al sistema hacia el mínimo global y lo deja atrapado ahí

---

## 3 bis · «El sesgo depende de $\mathbf{r}$ solo a través de la CV» — qué significa

*Duda de Enzo. Es la condición estructural del método entero, así que vale la pena verla desde tres ángulos.*

### Ángulo 1 · Es una composición de funciones

$V$ **no es** una función del sistema. Es una función de **un solo número**. Para aplicarla a una configuración hay que hacer dos pasos:

$$
\mathbf{r} \;\xrightarrow{\;\;\xi\;\;}\; s \;\xrightarrow{\;\;V\;\;}\; \text{energía}
$$

$$
\underbrace{\mathbf{r}}_{90\,000\ \text{números}} \;\longrightarrow\; \underbrace{s}_{1\ \text{número}} \;\longrightarrow\; \underbrace{V(s)}_{1\ \text{número}}
$$

**El cuello de botella es $s$.** Toda la información de la configuración tiene que pasar por ese único número antes de que $V$ pueda opinar. Si dos configuraciones dan el mismo $s$, $V$ **no puede distinguirlas** — le llegó exactamente la misma entrada.

Compáralo con lo que **no** hacemos:

| | $V(\xi(\mathbf{r}))$ — lo que se hace | $V(\mathbf{r})$ — lo que **no** se hace |
|---|---|---|
| Dominio | $\mathbb{R}$ (1 dimensión) | $\mathbb{R}^{3N}$ (90 000 dimensiones) |
| ¿Distingue dos $\mathbf{r}$ con el mismo $s$? | **No puede** | Sí |
| ¿Se puede almacenar? | Sí — una rejilla 1D | **No** — maldición de la dimensionalidad |
| ¿Sale de la integral? | **Sí** (Paso 2) | No |

### Ángulo 2 · El sesgo es constante sobre «rebanadas»

La función $\xi$ **rebana** el espacio de configuraciones en hipersuperficies, una por cada valor de $s$:

$$
\Sigma_s \;=\; \{\,\mathbf{r} \;:\; \xi(\mathbf{r}) = s\,\}
$$

Cada rebanada $\Sigma_s$ contiene un número astronómico de configuraciones distintas. Y la regla es:

> [!important] **El sesgo asigna un único valor a cada rebanada entera.**
> Todo lo que vive en $\Sigma_s$ recibe **exactamente** $V(s)$. Sin excepciones, sin gradaciones dentro de la rebanada.

> [!tip] Analogía: la altitud
> Sea $\xi$ = **altitud** sobre una cordillera, y $V$ un sesgo que depende solo de la altitud.
> Entonces **todos los puntos a 2000 m reciben el mismo valor**: la cara norte, la cara sur, el fondo del valle contiguo. $V$ no sabe *dónde* estás; solo sabe *a qué altura*.
> Un sesgo general $V(\mathbf{r})$ sí podría dar valores distintos a dos puntos ambos a 2000 m. Ese es justo el poder que renunciamos.

### Ángulo 3 · El más concreto: ¿sobre qué átomos empuja?

Esta es la versión que lo vuelve tangible. La fuerza que el sesgo ejerce sobre el átomo $i$ es menos el gradiente, y por **regla de la cadena**:

$$
\mathbf{f}_i^{\,\text{sesgo}}
\;=\; -\nabla_{\mathbf{r}_i} V\big(\xi(\mathbf{r})\big)
\;=\; \underbrace{-\frac{dV}{ds}\bigg|_{s=\xi(\mathbf{r})}}_{\text{escalar: pendiente del sesgo}} \;\cdot\; \underbrace{\nabla_{\mathbf{r}_i}\,\xi(\mathbf{r})}_{\text{vector: cuánto cambia la CV si muevo el átomo } i}
$$

Ahora mira el segundo factor y hazte la pregunta clave:

> **¿Cuánto cambia $\psi_{\text{CDR3}}$ si muevo una molécula de agua? ¿O un átomo de HV2?**
>
> **Nada. Exactamente nada.** $\nabla_{\mathbf{r}_i}\xi = \mathbf{0}$.

En el paper la CV se construye con torsiones $\psi$, y cada $\psi$ queda determinada por **4 átomos** (N, CA, C del residuo y N del siguiente). Para **cualquier otro átomo del sistema** — las ~29 000 aguas, HV2, HV4, el framework entero — el gradiente es cero y por tanto:

$$
\boxed{\;\mathbf{f}_i^{\,\text{sesgo}} = \mathbf{0}\quad \text{para todo átomo que no defina la CV}\;}
$$

> [!success] Esto es literalmente lo que significa la frase
> «El sesgo depende de $\mathbf{r}$ solo a través de la CV» $=$ **el sesgo solo empuja los átomos que definen la CV. Todos los demás no reciben ninguna fuerza extra.**
> No es una sutileza formal. Es una afirmación mecánica sobre qué átomos sienten el algoritmo.

### Por qué aceptamos esta restricción

| Motivo | Explicación |
|---|---|
| **Matemático** | Solo así $V$ sale exacto de la integral (Paso 2) → $F_V = F+V$ es una **igualdad**, no una aproximación → el sesgo se puede quitar exactamente después |
| **Práctico** | No puedes construir ni almacenar una función en 90 000 dimensiones. En 1–2 dimensiones, sí: una rejilla y unas gaussianas |
| **Y aquí el precio** | ⬇ |

> [!danger] La misma restricción es la vulnerabilidad — versión dura de A2
> Si el sesgo es **constante sobre cada rebanada** $\Sigma_s$, entonces **no empuja en ninguna dirección contenida dentro de la rebanada**.
>
> Cualquier grado de libertad lento que varíe **dentro** de $\Sigma_s$ recibe **ayuda cero**. La metadinámica es ciega a él por construcción — no «poco eficaz»: **ciega**.
>
> **Y HV2 es exactamente eso.** Las CVs del paper son $\psi$ de CDR1 y CDR3. La conformación de HV2 varía libremente dentro de cada rebanada. Luego:
>
> $$\mathbf{f}^{\,\text{sesgo}}_{\text{átomos de HV2}} = \mathbf{0}$$
>
> Y ahora puedes formular A2 en su forma más fuerte, que ya no es estadística sino mecánica:
>
> > *«Los átomos de HV2 no recibieron ni una sola fuerza de sesgo en todo el microsegundo de metadinámica. Su muestreo es, exactamente, el de MD clásica — que en la Clase 1 vimos que compra barreras de hasta 22 kJ/mol. ¿Sobre qué se apoya que HV2 esté convergido?»*

> [!note] Sé justo: el contraargumento existe
> Los átomos de HV2 no sienten fuerza de sesgo **directa**, pero sí están **acoplados mecánicamente**: si CDR1 y CDR3 se reorganizan violentamente, HV2 se ve arrastrado por contactos estéricos y por la cadena principal. Así que recibe *algo* de muestreo extra, indirecto.
> Esa es la defensa honesta del paper, y hay que reconocerla. Pero la carga de la prueba sigue de su lado: **el acoplamiento indirecto no es un argumento, es una hipótesis** — y es comprobable (correr una metadinámica de control incluyendo $\psi_{\text{HV2}}$ y ver si aparecen estados nuevos). El paper no lo hace.

---

> [!question] **Q4 · 3 bis** — En la metadinámica del paper, ¿qué fuerza de sesgo siente un átomo del lazo HV2?
>
> **a)** Exactamente cero
> **b)** Una fuerza pequeña pero no nula, decreciente con la distancia a las CDR
> **c)** La misma que un átomo de CDR1, porque el sesgo actúa sobre todo el sistema
> **d)** Una fuerza proporcional al sesgo acumulado $V(s)$ en ese instante
