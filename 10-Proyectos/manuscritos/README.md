---
tipo: indice
descripcion: "Índice de manuscritos en desarrollo donde Enzo participa en la parte de MD y análisis"
contexto: "Convertidos de PDF a MD para que sean accesibles desde la web (los PDF están en .gitignore)"
---

# Manuscritos en desarrollo — participación de Enzo Cevo

Tres manuscritos en desarrollo donde participo en la parte de **Dinámica Molecular (MD) y análisis**. Estos `.md` son reemplazos accesibles online de los PDF (excluidos del repo por tamaño).

## 1. `PAPER_AA_DYNAMICS_v3.md`
**Título:** *Location, Average Orientation and Dynamics of Amino Acids in a Membrane Mimetic: ²H-NMR and Molecular Dynamics Study*
**Rol:** simulaciones MD all-atom (GROMACS 2021.1 / OPLS-aa / TIP4P), 200 ns por AA; análisis con MDAnalysis (PDP, RDF).
**Hallazgo:** ALA/GLU permanecen paralelos en la interfaz; LEU/MET penetran ~0.5 nm al core hidrofóbico. MD explica atomísticamente las observaciones de 2H-NMR.
**Coautores:** Amatista San Martín, Enzo Cevo, Boris Weiss-López, Diego Muñoz-Gacitúa.

## 2. `Paper_AIE_LCs_Cevo_v4.md`
**Título:** *Substituent-Controlled Penetration of AIE Luminogens into Liquid Crystal Media*
**Rol:** MD de luminógenos AIE (TTG/TTC/TTY/TTO) en cristal líquido liotrópico TTAB/DeOH; análisis de penetración/localización y correlación con fotofísica.
**Relevancia:** colaboración internacional con CNR-SCITEC (Milán), Universidad Austral y UChile.
**Coautores:** Fernanda Llana, Federico Bravo, **Enzo Cevo**, María Cecilia, Igor Osorio-Román, Boris Weiss-López, Benedetta M. Squeo, Camilo Segura.

## 3. `Borrador_Paper2_MttPFK-GK.md`
**Título:** *Structural Basis for AMP-Dependent Allosteric Activation of a Bifunctional ADP-Dependent PFK/GK from Methanothermococcus thermolithotrophicus*
**Rol:** MD de proteína (AMBER24 / ff19SB), 5 réplicas × 400 ns; análisis MMPBSA; diseño y simulación in silico de mutantes (Y56A, R58A).
**Hallazgo clave:** AMP estabiliza una conformación "super-cerrada" catalíticamente competente; mutantes colapsan a estado hiper-cerrado no productivo que atrapa substratos.
**Relevancia para bioinformática/UNAB:** **ALTÍSIMA** — allostery, dinámica de proteínas, MMPBSA, validación in silico de mutantes, archaea.

---

## Cómo se usan estos archivos

Estos `.md` existen para que agentes remotos (p. ej. `/ultraplan` en web) puedan acceder al contenido de los manuscritos sin necesidad del PDF binario. Son *snapshots* del texto plano extraído con `pdftotext`; los PDF originales permanecen en `/10-Proyectos/manuscritos/` localmente pero no se suben al repo (`.gitignore`).
