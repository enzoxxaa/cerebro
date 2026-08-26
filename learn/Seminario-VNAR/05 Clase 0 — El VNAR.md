---
tipo: clase
proyecto: seminario
fecha: 2026-08-26
clase: 0
nodos: [R4]
hebras: [inmunología estructural]
modo: expositivo
estado: en curso
resumen: "Clase 0: anatomía del VNAR — qué le falta, con qué lo compensa, y por qué eso convierte el ataque A2 en demoledor"
tags:
  - seminario
  - clase
---

# 05 · Clase 0 — El VNAR

← [[00 MOC — Seminario VNAR]] · [[01 Plan de aprendizaje]] · siguiente: [[10 Clase 1 — Por qué la MD sola no basta]]

**Nodo:** `R4` del [[01 Plan de aprendizaje#3. Mapa de dependencias v2|mapa]].
**Fuente verificada:** Liu, Lin, Cao, Wang & Sui, *Front. Immunol.* **13**:1059771 (2022), PMC9720397, open access. Más los datos del propio paper.

---

## Por qué esta clase no es contexto decorativo

El sondeo confirmó que ya tienes el marco: **selección conformacional** — el antígeno captura un confórmero que ya estaba poblado, así que la afinidad depende de cuánto se puebla el estado competente. Eso es el techo del curso y está firme.

Lo que falta es la **anatomía**. Y no la necesitas para "dar contexto en la intro de la charla": la necesitas porque **de ella depende el ataque más fuerte que tienes contra el paper**.

Adelanto el destino para que sepas hacia dónde vamos, porque toda esta clase existe para poder decir esta frase con autoridad:

> [!danger] Adónde lleva esta clase
> El paper sesgó con metadinámica las torsiones de **CDR1 y CDR3**. Pero metió **HV2** en el tICA y en el MSM — y le atribuye a HV2 la pérdida de afinidad de la variante humanizada.
>
> Si HV2 fuera un loop periférico cualquiera, eso sería un descuido menor.
> Al terminar esta clase vas a saber por qué **no lo es**.

---

## 1 · Qué es un IgNAR, y qué es un VNAR

Los peces cartilaginosos —tiburones, rayas— son los organismos vivos **filogenéticamente más antiguos con un sistema inmune adaptativo basado en inmunoglobulinas**. Y produjeron una solución rarísima.

El **IgNAR** (*Immunoglobulin New Antigen Receptor*, descrito en 1995) es un anticuerpo natural **de solo cadena pesada**: no tiene cadena ligera en absoluto. Es un homodímero donde cada cadena aporta **un dominio variable** y **cinco dominios constantes**.

El dominio variable aislado —la parte que reconoce al antígeno— es el **VNAR**. Eso es lo que simula el paper.

> [!info] La familia de dominios de unión, para situarte
> | | Origen | Cadenas que forman el sitio | Nº de CDRs |
> |---|---|---|---|
> | **Fv / Fab** | mamífero convencional | VH **+** VL | 6 |
> | **VHH** («nanobody») | camélidos, solo cadena pesada | VH sola | 3 |
> | **VNAR** | tiburón, solo cadena pesada | VNAR solo | **2** |

Fíjate en la última columna, porque ahí está toda la historia.

Un Fv convencional construye su paratopo con **seis** loops repartidos entre dos dominios. Un nanobody prescinde de la cadena ligera y se queda con **tres**. Y el VNAR se queda con **dos** — es el **dominio de unión a antígeno más pequeño que existe de forma natural**.

Y aun así une HSA con alta afinidad. Esa es la tensión que hay que resolver: **¿cómo une algo tan bien con tan poco?**

---

> [!question] **Q1 · R4** — ¿Cuántos CDRs aporta el sitio de unión en cada caso?
>
> **a)** Fv convencional 6 · VHH 3 · VNAR 2
> **b)** Fv convencional 6 · VHH 3 · VNAR 3
> **c)** Fv convencional 6 · VHH 6 · VNAR 3
> **d)** Fv convencional 3 · VHH 3 · VNAR 2
>
> *(responde en el terminal — la explicación se añade aquí abajo al contestar)*
