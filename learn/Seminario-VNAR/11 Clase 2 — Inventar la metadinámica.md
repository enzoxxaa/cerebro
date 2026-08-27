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
