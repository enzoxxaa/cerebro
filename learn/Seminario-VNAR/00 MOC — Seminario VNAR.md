---
tipo: moc
proyecto: seminario
fecha: 2026-08-26
resumen: "Índice del seminario sobre Fernández-Quintero et al. 2022 (VNAR humanization, Liedl): metadinámica → clustering → MD sembrada → MSM"
tags:
  - seminario
  - moc
  - metadinamica
  - MSM
---

# 🦈 Seminario — VNAR humanization (Liedl 2022)

> [!info] El paper
> Fernández-Quintero ML, Fischer A-LM, Kokot J, Waibl F, Seidler CA, **Liedl KR**.
> **The influence of antibody humanization on shark variable domain (VNAR) binding site ensembles.**
> *Front. Immunol.* **13**:953917 (2022) · DOI [10.3389/fimmu.2022.953917](https://doi.org/10.3389/fimmu.2022.953917)
> **20 citas** (OpenAlex, consultado 2026-08-26) · PDF local: `../fimmu-13-953917.pdf`

**Encargo:** presentar en lab meeting con **énfasis metodológico** (metadinámica + MD clásica).
**Objetivo real:** poder (a) defender por qué el pipeline tiene sentido y (b) señalar dónde es vulnerable.

---

## Cómo está organizado esto

| Nota | Qué es | Estado |
|---|---|---|
| [[01 Plan de aprendizaje]] | El plan de clase + mapas de dependencias | 🟡 **esperando tu OK** |
| [[02 Sondeo — mapa de mi borde]] | Dónde está mi borde en cada hebra | 🔴 pendiente |
| [[10 Clase 1 — Por qué la MD sola no basta]] | Clase con quiz embebido | 🟢 borrador listo |
| [[20 Paper — parámetros exactos]] | Todos los parámetros del pipeline, verbatim | 🟢 |
| [[21 Defensa del pipeline]] | Munición para (a) | 🟢 |
| [[22 Superficie de ataque]] | Munición para (b) — 10 críticas ordenadas | 🟢 |
| [[23 Fondo — qué es un VNAR]] | Inmunología estructural mínima | 🟢 |
| [[24 Referencias verificadas]] | Refs confirmadas contra OpenAlex / Europe PMC | 🟢 |
| [[99 Pendientes de verificación]] | Lo que falta comprobar antes de la charla | 🟠 6 abiertos |

```mermaid
graph LR
    MOC["00 MOC"] --> PLAN["01 Plan"]
    PLAN --> SON["02 Sondeo"]
    SON --> C1["10 Clase 1"]
    C1 --> CN["Clases 2..n"]
    PAPER["20 Parametros"] --> DEF["21 Defensa"]
    PAPER --> ATK["22 Ataque"]
    VNAR["23 VNAR"] --> ATK
    REF["24 Referencias"] --> DEF
    REF --> ATK
    DEF --> CN
    ATK --> CN
    ATK --> PEND["99 Pendientes"]
```

---

## El paper en un párrafo

Un VNAR de mielga (*Squalus acanthias*), **parent E06**, une albúmina humana (HSA) con alta afinidad. Lo humanizan progresivamente (**huE06 v1.1 → v1.2 → v1.4**), y una variante extra (**v1.10**) **revierte** el motivo `RKN`. Comparan contra la línea germinal humana **DPK9** (Vκ1). Hallazgo: humanizar no solo baja la afinidad, **desplaza las poblaciones del ensemble** — el estado que coincide con el cristal del complejo cae de **92 %** (E06) a **16 %** (v1.1 y v1.4), y v1.10 lo recupera. Marco conceptual: **selección conformacional** — el antígeno elige un confórmero ya poblado, así que perder afinidad = despoblar el estado competente.

## La tensión metodológica central

> [!abstract] Todo el seminario cuelga de esta frase
> Metadinámica **destruye la cinética** para ganar ergodicidad. El MSM la **reconstruye**.
> **¿Por qué eso es legítimo?**

Cada crítica de [[22 Superficie de ataque]] es una forma de preguntar si se cumplen las condiciones que hacen legítimo ese intercambio. Por eso el plan construye la tensión primero.

## Las tres de mayor impacto

Si solo te queda tiempo para tres cosas en la charla:

1. 🔴 [[22 Superficie de ataque#🔴 A1 — El muestreo está confundido con el observable|A1]] — el corte de clustering fijo hace que el sistema "rígido" reciba **3.6× menos muestreo** que el "flexible", y los observables reportados crecen con el muestreo.
2. 🔴 [[22 Superficie de ataque#🔴 A2 — HV2 entra en el MSM pero nunca se sesgó en la metadinámica|A2]] — **HV2 nunca se sesgó**, pero está en el MSM y sostiene la conclusión biológica.
3. 🔴 [[22 Superficie de ataque#🔴 A3 — Ni una barra de error|A3]] — **92 % vs 16 %** sin un solo intervalo de confianza, teniendo `BayesianMSM` gratis en PyEMMA.

Y la carta de defensa más fuerte: [[21 Defensa del pipeline#Esto no es un protocolo ad hoc|Biswas, Lickert & Stock 2018]] dice explícitamente que la metadinámica se usa *solo* para generar conformaciones iniciales — así que "vuestra metadinámica no converge" **no es una objeción válida**.

---

## Infraestructura de la sesión

El subagente `researcher` está caído (`400 out of extra usage`, la cuota que anticipa `../SETUP.md`). Las verificaciones de estas notas se hicieron con `web_search` / `web_fetch` **directamente desde la sesión principal**, que sí los tiene cargados. Backends usados: OpenAlex (citas + DOI), Europe PMC (abstracts), fetch de PMC en HTML.

Para volcar la transcripción de la sesión a Obsidian: `/md-log Presentación seminario.md` (rellena hacia atrás).
