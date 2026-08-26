---
tipo: referencia
proyecto: seminario
fecha: 2026-08-26
resumen: "Cosas que hay que comprobar antes del lab meeting, y afirmaciones que NO deben citarse como están"
tags:
  - seminario
  - pendientes
---

# 99 · Pendientes de verificación

← [[00 MOC — Seminario VNAR]]

> [!warning] Regla
> Nada de esta lista debe decirse en la charla como hecho establecido hasta cerrarse. Un número mal citado en una lab meeting cuesta más credibilidad que un «no lo comprobé».

## 🔴 Abiertos

### 1. Número de hebras β del VNAR — **no citar ninguna cifra**
Surgió en [[05 Clase 0 — El VNAR]] y lo detectó Enzo: la review de Liu et al. (PMC9720397) dice que un VHH tiene **9** hebras («4 + 5») y que el VNAR, tras perder C′ y C′′, tiene **8**. Pero $9-2=7$. **La fuente se contradice.**

Causa raíz encontrada en la fuente primaria — el conteo del plegamiento IgV es **genuinamente ambiguo**:
> *«In IgVs, unlike IgCs, the A strand splits in two … and participates to the two sheets A B E D and A′|G F C C′|C′′.»*
> — Youkharibache, *Biomolecules* **11**:1290 (2021), PMC8470474

Según cuentes la hebra A partida como **una** o como **dos** (A y A′), el dominio tiene 9 o 10. Ninguna de las dos reconcilia el «8» de la review.

- ✅ **Sí es seguro decir:** el VNAR carece de CDR2 porque le falta la región C′/C′′ que la sostiene; es el dominio de unión a antígeno más pequeño conocido de forma natural.
- ❌ **No decir:** «tiene 8 hebras».
- **Para cerrar:** ir a una estructura VNAR real (`4HGK`, o 2CDQ/1SQ2) y contar hebras en DSSP.

### 2. Número de clusters/semillas por variante
La Tabla 1 solo publica tiempo agregado; el texto remite a la tabla para el nº de clusters, que **no está**. La reconstrucción en [[20 Paper — parámetros exactos]] es aritmética propia. → mirar la SI.

### 3. ¿La Fig. 3A está reponderada por el MSM?
Si son histogramas crudos del pool sembrado, no son energías libres (ataque **A6**). El paper no lo dice. → SI, o los papers de 2019–2020 del grupo que reutilizan la figura.

### 4. Factor de viscosidad de TIP3P
Para el ataque **A7** hace falta el número exacto y su fuente. Sé el signo (TIP3P es **menos** viscoso → dinámica **acelerada** → tiempos del MSM demasiado rápidos), pero **no citar un factor concreto sin fuente**.

### 5. ¿Tiene `4HGK` un disulfuro interloop CDR1–CDR3?
Los VNAR de mielga aparecen clasificados como Tipo II (Cys no canónicas en CDR1 **y** CDR3, con disulfuro interloop) y también como Tipo IIB (sin ellas). **Si E06 es Tipo II**, sus dos loops están atados covalentemente — y son justo los dos que el paper elige como CVs de metadinámica. Sesgar dos lazos unidos por un enlace covalente no es lo mismo que sesgar dos independientes.
→ **Potencialmente el mejor punto de la charla.** Mirar el PDB directamente.

### 6. Biswas et al. 2018 — ¿qué longitud mínima de trayectoria recomiendan?
El abstract dice que discuten «the minimal number and length of short MD trajectories». Si dan una cifra y el paper de Liedl no la cumple, el ataque **A4** deja de ser cualitativo. Paywalled en ACS → buscar preprint o repositorio institucional.

### 7. Estimador del MSM: ¿máxima verosimilitud o bayesiano?
El paper solo dice «PyEMMA 2». Importa para **A3**: si usaron `BayesianMSM`, tenían las barras de error y no las publicaron; si usaron ML, ni las calcularon.

### 8. ¿Por qué Vκ1 (DPK9) como plantilla de humanización de un VNAR?
Es una cadena **ligera**, y un VNAR es de cadena pesada. Presumiblemente por similitud de secuencia, pero **no verificado**. Pregunta muy probable en la lab meeting → mirar Kovalenko et al.

## ✅ Cerrados

- **Genealogía del protocolo** — confirmada en OpenAlex, 7 papers previos del grupo (2019–2022).
- **Biswas, Lickert & Stock 2018 justifica el diseño** — abstract confirmado vía Europe PMC: la metadinámica se usa *solo* para generar conformaciones iniciales.
- **VNAR carece de CDR2, compensado por HV2/HV4** — confirmado, PMC9720397.
- **HV2 está en el MSM pero no en las CVs** — confirmado citando el propio paper, dos secciones.
