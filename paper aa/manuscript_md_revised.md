# Parte MD revisada — CP-ART-07-2026-002807.R1

Texto de reemplazo para las secciones **2.4 (Métodos MD)** y **3.2 (Resultados
MD)**, más la lista de figuras y las frases del proof que hay que corregir.

Está en inglés donde va texto del paper y en español donde te hablo a vos.
Generado el 2026-09-01 desde `revision_pccp/`. Cada número sale de un CSV; la
referencia `Dnn` apunta a la entrada de `NOTAS_DISCREPANCIAS.md` que lo sostiene.

> **No toca:** Introducción, 2.1–2.3, Conclusiones (salvo las dos frases marcadas
> abajo) ni las respuestas de Amatista.

---

## 0. Mapa de figuras: qué reemplaza a qué

| Nueva | Contenido | Archivo | Qué pasa con la vieja |
|---|---|---|---|
| **1** | Espectros ²H-NMR S1–S5 | *(de Amatista, sin cambio)* | Fig 1 se mantiene |
| **2** | Espectros ²H-NMR S6–S9 | *(de Amatista, sin cambio)* | Fig 2 se mantiene |
| **3** | Parámetros de orden: MD vs experimento y ΔS_CD | `results/fig/pub/fig_order_parameters.pdf` | **nueva** — responde R1 sobre la Fig. 1 |
| **4** | Perfiles de densidad, 2×2 | `results/fig/pub/fig_density.pdf` | **fusiona Figs 3 y 4** |
| **5** | RDF, 2×2 | `results/fig/pub/fig_rdf.pdf` | **fusiona Figs 5, 6, 7 y 8** |
| **6** | Orientación y estados | `results/fig/pub/fig_orientation.pdf` | **nueva** |
| **7** | Snapshots representativos | `results/fig/pub/fig_snapshots.pdf` | **nueva** — responde R2-6 |
| **8** | Dinámica reorientacional | `results/fig/pub/fig_dynamics.pdf` | **nueva** — responde R2-4 y R2-5 |

Se ganan tres páginas fusionando cuatro RDF en uno y dos figuras de densidad en
una, y se gastan en las tres nuevas. Los RDF **se quedan en el texto principal**.

### Suplementario

| # | Contenido | Archivo |
|---|---|---|
| S1 | Convergencia de área y espesor | `figS_convergence.pdf` |
| S2 | Perfiles S_CD experimentales de las cinco muestras | `figS_exp_scd.pdf` |
| S3 | Gauche, MSD y puentes de hidrógeno | `figS_structure.pdf` |
| S4 | S_CD de los aminoácidos, MD vs Tabla S2 | `figS_aa_scd.pdf` |
| S5 | Nomenclatura atómica | `figS_atom_labels.pdf` |
| Tabla S1 | Splittings de SDS-d₂₅ — **numeración corregida** (D1), S4/S5 sin cruzar (D2), unidades en Hz (D7) | — |
| Tabla S2 | Splittings de los AA — unidades en Hz (D7) | — |
| Tabla S3 | τ resuelto por carbono, los cinco sistemas | `results/csv/tau_stats.csv` |
| Tabla S4 | Δν_Q calculado con y sin AA, contra el experimento | `results/csv/dnuq_md_vs_exp.csv` |
| Tabla S5 | Escalas de hidrofobicidad publicadas vs observables de MD, con las correlaciones de rango | `results/csv/hydrophobicity.csv` |

**Tablas 1 y 2 salen del texto principal**: R1 pidió quitarlas y Amatista ya
respondió que las composiciones se integran a la prosa de 2.2.

**Tabla 3 se reemplaza** por la Tabla 1 nueva (abajo, en 3.2.2).

---

## 1. Sección 2.4 — Molecular Dynamics Simulations *(reemplazo completo)*

> Los tres párrafos de composición y parámetros se conservan casi iguales; lo que
> cambia está **en negrita**. La subsección "Calculation of NMR observables" es
> nueva y no tiene equivalente en el proof.

### 2.4.1 System composition and force field

All molecular dynamics simulations and trajectory analyses were performed with
GROMACS 2021.1. A membrane-mimetic bilayer patch was assembled with PACKMOL and
comprised 274 SDS and 80 1-decanol molecules (SDS:DeOH molar ratio 3.43, close to
the experimental value 3.28; the difference arises from rounding to integer
molecule counts), arranged as two apposed leaflets **containing 141 and 133
surfactant molecules respectively**. The aggregate was solvated with **15 552
TIP4P water molecules (15 548 in the amino-acid-containing systems)** and
neutralised with 274 Na⁺ counter-ions, together with 62 KCl ion pairs. A single
amino-acid molecule was added to the aqueous phase of each system, giving four
independent simulation boxes plus one amino-acid-free control. The initial box
measured 6.717 × 6.717 × 13.542 nm³ under three-dimensional periodic boundary
conditions, yielding an effectively infinite lamellar bilayer normal to *z*.

**Two features of this composition should be stated explicitly.** First, the
simulated box contains 56.8 water molecules per surfactant against 30.7 in the
experimental mesophase, i.e. **54 % of the experimental amphiphile molality**;
the SDS:DeOH ratio is reproduced but the water content, which in a lyotropic
lamellar phase fixes the interlamellar spacing and the interfacial water
activity, is not. Second, the **6 % leaflet imbalance** (141 vs 133) makes the
more crowded leaflet measurably more ordered, by up to 0.03 in |S_CD| at C9. Both
are systematic and identical across the five boxes, so they **cancel in every
control-referenced difference** reported here; they are stated because the
absolute per-leaflet values are not interchangeable.

*(Referee-facing: esto es **D7** y **D8**, más el desbalance de monocapas que
salió en la sesión de curado. Declararlo nosotros es mucho mejor que que lo
encuentre R2, que ya reclamó rigor.)*

### 2.4.2 Simulation protocol

The all-atom OPLS-AA force field was used for SDS, DeOH, the amino acids and the
ions, with SDS parameters following the reparametrisation validated for anionic
surfactants in concentrated electrolyte; water was the four-site TIP4P model.
Glutamic acid was modelled in its physiological form (net charge −1 on the
side-chain carboxylate); ALA, LEU and MET as neutral zwitterions.

Equations of motion were integrated with the leap-frog algorithm and a 2 fs time
step. Bonds involving hydrogen were constrained with LINCS (expansion order 4).
Non-bonded interactions used the Verlet cut-off scheme with the neighbour list
updated every 50 steps. **Both electrostatic and Lennard-Jones interactions were
treated with Particle-Mesh Ewald (`coulombtype = PME`, `vdwtype = PME`), with a
real-space cut-off of 1.3 nm for both, interpolation order 4, Fourier grid
spacing 0.16 nm, `ewald-rtol = 1 × 10⁻⁵`, `ewald-rtol-lj = 1 × 10⁻³` and
geometric LJ-PME combination rule.** Temperature was held at 310 K with the
velocity-rescale thermostat (τ_T = 0.1 ps), coupling the water-and-ions group and
the C10/DS/amino-acid group to separate baths. Pressure was held at 1 bar with
the Parrinello–Rahman barostat applied semi-isotropically (τ_P = 2.0 ps,
compressibility 4.5 × 10⁻⁵ bar⁻¹).

Each system was energy-minimised, equilibrated for 1 ns in the NPT ensemble and
propagated for 200 ns of NPT production, with coordinates saved every 20 ps
(10 001 frames).

> **Frase eliminada.** El proof dice *"treated with the ParticleMesh Ewald (PME)
> method for the dispersion term with a real-space cut-off…"* — la afirmación es
> correcta (el `.mdp` real usa `vdwtype = PME`, o sea LJ-PME de verdad) pero la
> sintaxis está rota y faltan dos parámetros. También sale **`DispCorr =
> EnerPres`**: con LJ-PME la corrección analítica de dispersión no aporta nada y
> mencionarla confunde. Ver **D7**.

### 2.4.3 Analysis window *(subsección nueva)*

**All results reported here are averaged over the 100–200 ns interval of each
trajectory, in five 20 ns blocks; error bars are standard errors over blocks. The
first 100 ns are discarded for two independent reasons.**

**In the control, the bilayer is not equilibrated before ≈100 ns**: the area per
surfactant stays near 0.355 nm² and then contracts to 0.336 nm² between 85 and
95 ns, with a matching step in the sulfur–sulfur thickness (Fig. S1). The four
amino-acid-containing systems, which were assembled from an already contracted
configuration, are stationary from the start (differences between the first and
second halves of 0.2–1.1 σ, against 5.4 σ for the control). **In the
amino-acid-containing systems the solute itself is not equilibrated**: all four
amino acids were placed in the aqueous phase and adsorb over the first tens of
nanoseconds. Methionine makes **no contact whatsoever with the aggregate during
the first 25 ns**, and leucine is bound in only half of that interval. Averaging
over the full trajectory therefore mixes the adsorption transient into the
result: it shifts the methionine contact fraction from 0.97 to 0.85 and its mean
depth from 1.03 to 1.34 half-thicknesses.

*(**D4** + **D20**. El proof no declara ninguna ventana en Métodos y la Tabla 3
dice "final 150 ns"; los scripts que produjeron las Figs 3–8 usaban de hecho la
trayectoria completa, y para MET una parcial de 92 ns — ver el bloque de frases a
corregir.)*

### 2.4.4 Calculation of NMR observables from the simulations *(subsección nueva)*

Deuterium order parameters were obtained from the **real C–H bond vectors** read
from the topology, without reconstructing deuterium positions:

  S_CD = ⟨(3 cos²θ − 1)/2⟩

with θ the angle between the C–H vector and the bilayer normal, averaged over the
274 surfactants, both leaflets and all frames of the window. Because the
trajectories are all-atom, all **twelve** chain positions are accessible,
including C1 and the terminal methyl — the two most informative ends, which a
united-atom reconstruction cannot reach. Averaging P₂ over the three real C–H
vectors of a freely rotating CD₃ already contains the P₂(cos 109.47°) = −1/3
methyl factor, so no additional correction is applied to the simulated values;
the inverse correction is applied when converting an experimental CD₃ splitting
to the order parameter of the C–C axis.

Order parameters were converted to the experimental observable through

  Δν_Q = (3/8)(e²qQ/h)|S_CD| = 62 625 Hz × |S_CD|

with e²qQ/h = 167 kHz for an aliphatic C–D bond. The factor 3/8 rather than 3/4
follows from the discotic nematic mesophase aligning with its symmetry axis
**perpendicular** to B₀, so that P₂(cos θ_DB) = −1/2.

Reorientational dynamics were characterised by the second-rank correlation
function C(t) = ⟨P₂(**u**(0)·**u**(t))⟩ of the same C–H vectors, computed by FFT
from the tensor decomposition Q_ab = u_a u_b − δ_ab/3. With the director fixed
along the bilayer normal C(t) does not decay to zero but to a plateau equal to
S_CD², which provides an independent check on the order parameters: the square
root of the plateau reproduces the directly averaged profile to within 0.001 at
all twelve positions. Correlation times are reported as the **resolved integral
of the excess over the plateau up to a 2 ns cut-off**. Because the first
measurable lag is 20 ps and between 59 % and 99 % of the decay occurs below it,
these are **upper bounds** on τ_c, and are labelled as the resolved (slow)
component throughout.

*(**D16**: el estimador anterior integraba solo los lags con exceso positivo, lo
que rectifica el ruido de la cola; inflaba τ entre 1.4× y 14.8× y producía
diferencias entre sistemas que cambian de signo al mover la ventana del plateau.
No cites nada de `tau_summary.csv`; usá `tau_stats.csv`.)*

---

## 2. Sección 3.2 — Molecular Dynamics Simulations *(reemplazo completo)*

> Las referencias a figura van tejidas en la prosa, como en el resto del paper
> (*"Figure 4 displays…"*, *"For MET (Figure 4d)…"*). Los paneles de las figuras
> nuevas son: **Fig. 3** (a) perfil absoluto, (b) Δ experimental, (c) Δ simulado ·
> **Figs. 4 y 5** (a) ALA, (b) GLU, (c) LEU, (d) MET · **Fig. 6** (a) P(θ),
> (b) estados de MET, (c) silueta · **Fig. 7** (a) ALA, (b) GLU, (c) LEU,
> (d, e) los dos estados de MET · **Fig. 8** (a) C(t) de la cadena, (b) ejes
> moleculares, (c) τ por carbono, (d) límite de movimiento rápido.

### 3.2.1 Validation against the experimental order profile

*Texto nuevo. No existe en el proof y es la mejor respuesta a R2-1, "por qué este
sistema y este campo de fuerza".*

Before interpreting the amino-acid results we establish what the simulations
reproduce. **Figure 3a** compares the simulated chain order profile of the
amino-acid-free control with the ²H-NMR values of Table S1. Table S1 lists twelve
rows per sample but only **seven distinct values**: within each sample several
carbons share a splitting to the hertz (14 485 Hz repeated four times in the
control), which can only mean that those lines are not resolved. The red segments
of Figure 3a are therefore drawn across the carbons that report each value, and
the black dashed segments are the simulated profile averaged over the same
groups. Compared at that resolution the two correlate at **r = 0.992**, against
0.960 carbon by carbon.

The agreement is in shape, not in amplitude. Figure 3a shows that the simulation
overestimates the plateau by a factor of 1.14–1.21 and underestimates the
terminal methyl by 0.68: **a steeper order gradient along the chain rather than a
uniform offset**. We report this as a known limitation of the force field rather
than adjusting the quadrupolar coupling constant to absorb it. Since every
quantity used below to compare systems is a difference against the control, a
multiplicative offset cancels to first order.

The simulated profile in Figure 3a is **not smooth**: |S_CD| alternates between
C1 and C4 (0.301, 0.243, 0.221, 0.290) before decaying monotonically to the
terminal methyl. This is a property of the chain, not of the analysis. The two
hydrogens of every methylene agree to within 0.0013, and from C5 outwards the
free-rotation relation S_CD = −S_axis/2 holds to within 0.0025, so the structure
lies in the backbone conformation, whose gauche populations (Figure S3a) show the
same damped alternation near the anchored head group. The experiment cannot
resolve it because C1–C4 fall within the unresolved plateau of Table S1 — which
is precisely the region where the simulation has its structure.

Figures 3b and 3c compare the effect of adding one amino acid, measured and
simulated, on the same vertical scale; they are discussed in Section 3.2.5.

*(**D6**, **D13**, **D19**. El párrafo del zigzag es opcional: es honesto y se
adelanta a la pregunta obvia, pero si falta espacio va al SI.)*

### 3.2.2 Location and anchoring

All four amino acids were placed in the aqueous phase and spontaneously
associated with the aggregate, anchoring at the interface through their
zwitterionic backbone. Their side chains then behave very differently. **Figure 4
displays the partial density profiles of the four systems** and **Figure 5 the
corresponding radial distribution functions**; Table 1 collects the quantities
extracted from them together with the orientational and dynamical measures of the
following sections. What emerges is a single ordering of association with the
aggregate, **LEU > MET > ALA > GLU**, reproduced by four observables that share
neither definition nor error source: the contact fraction, the immersion depth,
the hydrogen bonding and the lateral diffusion coefficient.

Leucine and methionine bury their side chains within the chain region, 1.14 and
1.02 nm from the bilayer centre, while alanine and glutamic acid keep theirs at or
beyond the sulfate plane, at 1.74 and 1.98 nm. Between the two inserted residues
the ordering is not resolved and the two measures disagree in the third digit: the
leucine backbone sits deeper (Cα at 0.93 against 1.03 half-thicknesses) whereas
the longer methionine side chain reaches marginally further in, and the two
side-chain termini are indistinguishable in the clustering, at 0.66
half-thicknesses for both. What is robust is the separation between the pair that
inserts and the pair that does not.

**Tabla 1 (reemplaza la Tabla 3).** Fuente: `results/csv/table_main.csv`.
Versión lista para pegar en el Drive: **`manuscript/Table1.docx`**
(`python3 src/table_docx.py`). Ahí el pie va arriba, como en PCCP, y
los valores extremos de cada fila van en negrita.

| | ALA | GLU | LEU | MET |
|---|---|---|---|---|
| Contact fraction *f*_b | 0.93 ± 0.03 | **0.65 ± 0.12** | 1.00 ± 0.00 | 0.97 ± 0.01 |
| Side-chain density maximum / nm | 1.74 | 1.98 | 1.14 | **1.02** |
| ⟨θ⟩ / degrees | 73 | 62 | 152 | 106 |
| States (populations / %) | 2 (75/25) | 3 (44/41/15) | 3 (45/42/13) | **2 (57/43)** |
| H-bonds with the aggregate | 1.11 ± 0.10 | **0.83 ± 0.24** | 1.22 ± 0.04 | 1.27 ± 0.05 |
| H-bonds with water | 3.96 ± 0.12 | **9.42 ± 0.57** | 2.92 ± 0.20 | 3.41 ± 0.24 |
| *D*_lat / 10⁻⁷ cm² s⁻¹ | 19.2 | **58.7** | 4.1 | 7.9 |
| τ of the Cα→side-chain axis / ps | 374 ± 35 | 451 ± 160 | 552 ± 78 | 594 ± 92 |
| Mean Δν_Q, simulated / Hz | +69 | +107 | +66 | −21 |
| Mean Δν_Q, measured / Hz | −93 | −1256 | −1548 | −1534 |

*All amino-acid quantities come from a single molecule per box and are used as an
ordering, not as values; see Section 3.2.5.*

**Leucine and methionine insert into the chain region.** In Figure 4c the
side-chain branch carbon of LEU peaks at 1.14 nm from the bilayer centre while
its α-carboxyl anchor remains at 1.50 nm, a displacement of 0.36 nm; the
corresponding profiles for MET (Figure 4d) place the thioether sulfur at 1.02 nm
against 1.54 nm for the anchor, a displacement of 0.52 nm. In both panels the
side-chain density overlaps the grey C1–C4 and C5–C8 curves, confirming direct
contact with the surfactant chains. **Figures 5c and 5d make the same point
locally**: the first peak with the C2–C8 segment reaches g(r) = 8.4 ± 0.3 for LEU
and 4.8 ± 1.5 for MET at r ≈ 0.5 nm, while water coordination is suppressed to
0.5 and 0.7, i.e. **below** bulk density. Neither reaches the terminal methyl
region — contact with C9–C12 in Figures 5c and 5d is weaker and develops only as
a smooth monotonic rise, so the side chains stop within the upper half of the
monolayer.

**Alanine remains at the interface.** In Figure 4a its methyl carbon and its
α-carboxyl carbon peak at essentially the same depth, 1.74 and 1.70 nm, so the
Cα–Cβ axis lies close to the interfacial plane; the sharp fall of the water
density at the same position places ALA at the bilayer–water boundary. The
coordination environment in **Figure 5a** is dominated by the **sulfate head
group**, g(r) = 11.2 ± 0.8 at 0.44 nm, with water at approximately bulk density
(maximum 1.5) and no contact with the chain below 0.7 nm. Alanine is therefore
not a solvated species that happens to lie nearby: it is electrostatically bound
at the head-group layer, consistent with a contact fraction of 0.93.

> **Frase que hay que reemplazar.** El proof dice: *"For ALA (Figure 5), the
> dominant feature is an intense first peak with water at r ≈ 0.28 nm, confirming
> full solvation of the α-carbon at the interface."* **Las dos mitades son
> falsas**: g(r) vale exactamente cero por debajo de 0.29 nm (un carbono y un
> oxígeno de agua no se acercan más), y el rasgo dominante es el sulfato, quince
> veces más intenso que el agua. La lectura correcta **refuerza** la tesis del
> paper. Ver **D21.3**.

**Glutamic acid is the least associated of the four**, not the most anchored.
Figure 5b shows the sharp ion-pairing peak between its side-chain carboxylate and
sodium, g(r) = 32 at 0.23 nm, that the previous version of this work interpreted
as a second anchor. The remaining series of the same panel show that the pairing
happens *in the aqueous layer*: GLU has no hydrophobic contact at all, with the
C2–C8 curve below 1.5 and the C9–C12 curve below bulk density throughout. Figure
4b is consistent — both the side-chain and the backbone carbon peak outside the
sulfate plane, at 1.98 and 1.74 nm. GLU makes the fewest hydrogen bonds with the
aggregate of the four (0.83, and none at all in half the frames), makes 9.4 with
water, diffuses laterally 34 times faster than the surfactant that hosts it
(Figure S3c), and is in contact with the aggregate only **65 % of the time**.

> **Frase que hay que reemplazar.** El proof afirma que GLU *"is doubly anchored
> at the surface — via both its zwitterion and its side-chain carboxylate — and
> is therefore unable to insert into the hydrophobic core."* La conclusión (no se
> inserta) es correcta; el mecanismo es el contrario. La cadena lateral cargada
> **prefiere el agua**, y esa preferencia es lo que la mantiene afuera. Ver
> **D9** y **D11**.

**Comparison with published hydrophobicity scales** *(párrafo nuevo, responde
R1-6; ver Tabla S5)*

The ordering just described can be tested against experimental scales determined
on a different membrane system by a different technique. The Wimley–White
interfacial scale is the appropriate reference, since it measures transfer to an
interface rather than to a hydrocarbon core, and it ranks the four side chains
LEU (−0.56 ± 0.04 kcal mol⁻¹) > MET (−0.23 ± 0.06) > ALA (+0.17 ± 0.06) >
GLU⁻ (+2.02 ± 0.11); the octanol scale and the octanol–water π values of Fauchère
and Pliška give the same ranking. Against those values the Spearman rank
correlation of our contact fraction is −1.00, of the hydrogen bonds to water
+1.00, of the lateral diffusion coefficient +1.00 and of the residual
orientational order of the Cα→side-chain axis −1.00; the depth of the side-chain
density maximum gives +0.80, the single inversion being the LEU/MET pair that our
own data do not resolve either. These five quantities are not independent tests
of one hypothesis, but they are computed from different observables with
different error sources and they agree with an independent experimental scale.
The correspondence is what one expects if the common zwitterionic backbone fixes
the anchoring point and the side chain alone sets the projection from it — which
is what the published scales measure, having been determined with the peptide
backbone held constant.

### 3.2.3 Orientation and populated states

*Responde R2-6 (snapshot representativo por AA) y R2-8 (evidencia de la
bimodalidad de MET).*

Methods declared a distribution of the orientation angle between the Cα→side-chain
vector and the bilayer normal but never showed it. **Figure 6a displays these
distributions**, restricted to the frames in which the amino acid is in contact
with the aggregate and corrected for the sin θ phase-space volume, so that an
isotropic distribution would be flat. They separate the four cleanly. **Leucine
has strictly zero population below 120°**: its side chain points into the core in
every bound frame. Methionine is broad and bimodal with a bias towards the core,
while alanine and glutamic acid orient their side chains towards water
(θ ≈ 45–75°).

Rather than selecting snapshots by eye, every bound frame was classified by
k-means on the depth of Cα, the depth of the side-chain terminal atom and cos θ,
with the number of states chosen by mean silhouette. **Figure 6c shows that
methionine is the only one of the four with a genuinely two-state partition**:
silhouette 0.655 at k = 2, against 0.37–0.48 for the others, which is what
distinguishes a real two-state system from a unimodal cloud cut in two. The two
methionine states are resolved in **Figure 6b**, populated 57 % and 43 %: in the
first the Cα sits below the sulfate plane with the thioether inserted (θ = 146°),
in the second it lies outside the plane with the thioether solvated (θ = 54°).

**Figure 7 shows the representative configuration of each amino acid** — the
frame closest to its cluster centroid, not a snapshot chosen by eye — with ALA,
GLU and LEU in Figures 7a to 7c and the two methionine states in Figures 7d and
7e. The five panels share camera, scale and coordinate origin, so depths are
directly comparable between them, and the dashed line marks the mean sulfate
plane of each configuration. The three
clusters found for LEU differ only in the depth of Cα and all place the side
chain in the core, so the configuration of Figure 7c is representative of 100 %
of its bound frames rather than of the 45 % held by its own cluster; the same
applies to GLU in Figure 7b, where two of three clusters point the side chain at
the water.

**The density profile says the same thing independently.** In Figure 4d the
methionine sulfur distribution has two maxima, at 1.02 and 1.98 nm, carrying
**55 % and 45 %** of the density — against 57/43 from the clustering, by a method
that shares neither definition nor error source with it. Applying a prominence
criterion makes the statement quantitative: the second methionine maximum has a
prominence of **70 % of the profile maximum**, whereas the shoulders visible in
Figures 4a–4c reach at most 4 %. **Only methionine is bimodal**, and this can now
be stated with a number rather than read off a curve.

The two methionine states interconvert 51 times over the analysis window, with
mean dwell times of 2.1 and 1.6 ns — between 7 and 24 times slower than the
corresponding interconversions of the other three amino acids. They are therefore
**kinetically as well as geometrically separated**. On the NMR time scale,
however, an exchange rate of ≈5 × 10⁸ s⁻¹ is five to six orders of magnitude
inside the fast-exchange limit, so the two states cannot give rise to two
distinct doublets: they contribute a single population-weighted splitting.

> **Coordinar con Amatista.** La respuesta a R1 sobre la Figura 2 atribuye el par
> interno/externo de MET a *"two slowly exchanging interfacial orientations"*. El
> MD lo contradice: el intercambio es rápido por cinco órdenes. Además la Tabla
> S2 lista **un solo** splitting para MET-d₃ (788 Hz), o sea el segundo doblete
> no está en el SI. La explicación simple y coherente con lo que la misma
> respuesta dice de ALA/LEU/GLU es que el par interno sea el D₂O parcialmente
> orientado. **Hay que cerrarlo antes de mandar**: R2-8 pregunta literalmente por
> la evidencia de RMN, y la respuesta honesta es que la evidencia la da el MD.

### 3.2.4 Effect of the amino acids on membrane dynamics

*Responde R2-4 y R2-5. Todo el contenido es nuevo.*

**Figure 8 characterises the reorientational dynamics of the aggregate.** Figure
8a shows the correlation function C(t) = ⟨P₂(**u**(0)·**u**(t))⟩ for four
representative carbons of the control. The curves do not decay to zero but to a
plateau equal to S_CD², whose square root reproduces the profile of Figure 3a to
within 0.001 — an independent check on the order parameters by a completely
different route. The shaded band at short times marks the region below the first
measurable lag of 20 ps, where between 59 % and 99 % of the decay occurs; every
correlation time reported here is therefore the **resolved, slow component**, an
upper bound on τ_c.

**Figure 8c gives the mobility gradient along the chain.** The resolved
correlation time falls monotonically from **203 ± 4 ps at C1**, next to the
sulfate, to **68 ± 5 ps at the terminal methyl** — a threefold increase in
mobility, tracking the decay of S_CD over the same positions, with the same step
at C3/C4 that Figure 3a shows in the order parameter. The gradient is if anything
understated, since the unresolved fraction grows from 59 % to 99 % along the same
path.

**Figure 8b separates two time scales for the surfactant.** Local C–H
reorientation, averaged over the C1–C11 methylenes, has a resolved time of
**151 ± 1 ps**. Reorientation of the **molecular long axis** (C1→C12, black curve)
is slower, **486 ± 6 ps**, and its plateau corresponds to a residual order
parameter of 0.76; only 21 % of its decay falls below the sampling interval,
which makes it the best-determined dynamical quantity in the set.

**The amino acids do not measurably change any of this.** In Figure 8c the five
curves superimpose: no difference between the control and any amino-acid system
exceeds 2.1 σ, at any chain position or for either aggregate quantity, and none is
larger than 9 % in magnitude. This joins three other observables that give zero
within one standard error at this stoichiometry — the order parameter profile
(Figure 3c), the gauche fraction per dihedral (Figure S3b), and the lateral
diffusion coefficient of the surfactant (Figure S3c).

**Figure 8d places all eighteen deuterated groups against the NMR time scale.**
The largest splitting in the data set, 14 485 Hz, sets the most demanding scale at
1/Δν_Q = 69 µs; the slowest group reorients in 393 ps, more than **10⁵ times
faster**. This is what licenses interpreting the splittings through the residual
order parameter alone, and it is a statement about an inequality: the motions that
the 20 ps sampling does not resolve are *faster*, so they lie further inside the
limit and cannot overturn the conclusion.

The amino acids themselves are shown as the coloured curves of Figure 8b.
Correlation times for their molecular axes span 374–594 ps and the four are
indistinguishable within their errors; what distinguishes them is not the decay
time but the **plateau** — the fraction of orientation retained: LEU 0.64, MET
0.40, ALA 0.06, GLU 0.00. Glutamic acid decays to zero, i.e. it reorients
isotropically, like a free solute in water. This ordering is identical to the one
given by the contact fraction, the immersion depth, the hydrogen bonding and the
lateral diffusion of Table 1.

### 3.2.5 Scope and limitations *(subsección nueva, obligatoria)*

The simulations contain **one amino acid per 274 surfactants**, a mole fraction of
0.0036 against 0.040–0.053 in the experiment — roughly twelve times below the
experimental stoichiometry. Two consequences follow, and both are stated rather
than left implied.

**The simulations do not reproduce the measured disordering.** This is the
comparison of Figures 3b and 3c, drawn on a common vertical scale. The measured
changes of Figure 3b fall well outside the grey band of control noise for GLU, LEU
and MET; every simulated point in Figure 3c lies inside it. In absolute terms, the
calculated splittings change by at most +159 Hz at any single chain position on
adding an amino acid — +107 Hz averaged over C1–C11 for glutamic acid, the largest
of the four — with no point exceeding 1.0 σ and no consistent sign, while the
measurements fall by up to 2142 Hz. Five independent observables agree that the
simulated membrane does not respond at this concentration: ΔS_CD, the gauche
fraction, the surfactant lateral diffusion coefficient, the resolved correlation
times, and the area per surfactant. **Alanine is the exception in the experiment
as well**: its measured effect, −0.7 % over C1–C11, also lies within the noise
band of Figure 3b, so for ALA the simulation and the measurement agree that
nothing happens. The disagreement concerns GLU, LEU and MET.

**Association and perturbation are not the same ordering.** The scales and the
simulations agree on how strongly each residue associates with the interface,
LEU > MET > ALA > GLU⁻. The measured perturbation of the chain order follows a
different sequence, LEU (−1548 Hz) > MET (−1534) > GLU (−1256) ≫ ALA (−93)
averaged over C1–C11, and normalising by the molality of each sample, which
ranges from 0.070 to 0.093 mol kg⁻¹, does not change it. ALA and GLU exchange
places between the two orderings, and we read this as two distinct mechanisms.
Leucine and methionine perturb the chains because they insert into them, and
there the perturbation does follow hydrophobicity. Alanine associates well but
its side chain is a single methyl group occupying essentially no volume in the
chain region, so it binds without perturbing. Glutamate is the converse: it is
the least associated of the four and does not insert, but it is the only charged
species in the set, and the Wimley–White values localise its distinctiveness in
that charge — the neutral side chain gives ΔG_wif = −0.01 ± 0.15 kcal mol⁻¹,
close to alanine, against +2.02 for the anion. At the experimental molality an
anionic solute and its counter-ions at an already anionic sulfate interface will
modify the ionic environment of the head-group region, and hence the head-group
area and the chain order, without requiring insertion. A single solute per 274
surfactants cannot reproduce a collective electrostatic effect of that kind, and
we offer this as a hypothesis consistent with the data rather than as a
demonstrated mechanism.

**What the simulations do constrain is location and orientation** — the contact
fractions, immersion depths, angular distributions and state populations of
Table 1 and Figures 4 to 7 — none of which depends on the amino-acid
concentration in the same way. Statistical uncertainties for single-molecule
quantities are governed by the number of independent reorientations rather than by
the number of frames, which is why these are reported as an ordering across the
four amino acids rather than as values.

> **Frase que hay que eliminar de las Conclusiones.** *"This insertion induces
> structural disorder that propagates toward the bilayer interior, providing a
> direct atomistic explanation for the decrease in quadrupolar splittings observed
> in the ²H-NMR spectra of samples S4 and S5."* Estas simulaciones **no** muestran
> ese desorden. La ubicación y la orientación sí se sostienen; la explicación de
> la caída de los splittings, no. Ver **D5**, **D10**, **D14** y **D17**.

---


## 3. Frases del proof a corregir, en orden de página

| Pág. | Dice | Debe decir / acción | Ref. |
|---|---|---|---|
| 6 | `≈15 540 TIP4P water molecules [37]. and neutralized/ionized to reproduce : 274 Na⁺ … 62 KCl..` | 15 552 (control) / 15 548 (con AA); puntuación arreglada | D7 |
| 6 | `Both electrostatic and Lennard-Jones … PME method for the dispersion term` | reescrito en 2.4.2; agregar `lj-pme-comb-rule` y `ewald-rtol-lj` | D7 |
| 6 | `DispCorr = EnerPres` | quitar: con LJ-PME no aporta | D7 |
| 7 | `table 1 from Supporting Information` | Tabla S1 | D7 |
| 9 | Tabla 3 completa | reemplazada por la Tabla 1 nueva | D21 |
| 10 | GLU *"doubly anchored … unable to insert"* | reescrito en 3.2.2 | D9, D11 |
| 13 | *"both measurements place the isobutyl group within the C1–C4 region … the same region that shows the largest decrease"* | la caída es **uniforme** (~10–12 %), no localizada; y con la numeración corregida C1–C4 es la región proximal a la cabeza | D1, D3 |
| 15 | ALA *"intense first peak with water at r ≈ 0.28 nm … full solvation"* | reescrito en 3.2.2 | D21.3 |
| 16 | MET *"secondary, lower-intensity peak"*, *"buried state dominating"* | 55 % / 45 %: la asimetría es mucho menor | D21.2 |
| 17 | *"the quadrupole splittings … attached to C1–C4 … show the most significant decrease"* | reemplazar por el perfil ΔS_CD de la Fig. 3 | D3 |
| 18 | Conclusiones: *"providing a direct atomistic explanation…"* | eliminar | D5 |
| 18 | Conclusiones: `remaining confined to the interface- ALA do not perturb` | frase rota | D7 |
| 18, 22 | Data Availability duplicada | dejar una | D7 |
| Abstract | `strongly associated to the bilayer ag, exhibiting` · `alkyl -chain` | fragmentos cortados; **verificar qué versión se envió**, en `manuscript_v2.md` ya está arreglada | D7 |
| SI | Caption Tabla S1: "in kHz" con valores en Hz; *"Series A samples (System 1, PL-free)"* | corregir unidades; el subtítulo es residuo de otro paper | D7 |
| SI | Tabla S1: encabezados `S4 (MET)` y `5 (LEU)` | cruzados respecto de la Tabla 2 del texto | D2 |
| SI | Tabla S1: numeración de carbonos | **invertida** — pendiente de confirmar con Amatista | D1 |

---

## 4. Pies de figura

Los pies en inglés, listos para pegar, están en
`results/fig/pub/CAPTIONS.md`. La correspondencia con la numeración nueva es la
tabla de la Sección 0. Los de `fig_density` y `fig_rdf` son nuevos y están abajo.

**Figure 4.** Partial mass density profiles along the bilayer normal, averaged
over 100–200 ns in five 20 ns blocks. Shaded band: water. Grey curves: the SDS
sulfate head group and the C1–C4, C5–C8 and C9–C12 chain segments (left axis).
Coloured curves (right axis, common to the four panels): the side-chain reference
atom (solid, with the block standard error shaded) and the α-carboxyl carbon
(dashed) of each amino acid. Labels give the position of each detected maximum in
nm. Methionine is the only amino acid whose side-chain distribution is bimodal;
percentages give the fraction of the density assigned to each maximum, in
agreement with the 57/43 populations obtained independently by clustering.

**Figure 5.** Radial distribution functions of the side-chain reference atom of
each amino acid with the bilayer and the solvent, averaged over 100–200 ns in
five 20 ns blocks; shaded bands are standard errors over blocks. The four series
are the same in every panel so that the environments can be compared directly;
Na⁺ is shown only for glutamic acid, where it is the dominant feature. The dotted
line marks bulk density. Reference atoms: ALA Cβ, GLU Oε1, LEU Cγ, MET Sδ.

---

## 5. Qué queda abierto

**Bloqueado por Amatista** — marcar `[PENDIENTE]` donde haga falta:

1. **Numeración de carbonos de la Tabla S1** (D1). El MD dice que está invertida:
   r = −0.46 tal como está impresa contra +0.96 invertida. Toda la Fig. 1 y la
   Sección 3.1 dependen de esto.
2. **Asignación de los 5 splittings de GLU-d₅**. Sin ella no se completa R2-3 ni
   R2-7. La hipótesis del MD es {HA, HB1, HB2, HG1, HG2} (D15).
3. **El segundo doblete de MET** (arriba, 3.2.3).
4. **¿ALA-d₄ es perdeuterado?** El MD predice 9.7 kHz para Cα, que sería la línea
   más grande del espectro, y la Tabla S2 lista una sola (D15).
5. **¿C7/C8 rompe degeneración de verdad o es solapamiento?** Hoy C7 es donde
   está el máximo de la caída (D3).

**Hecho desde entonces:** la discusión de polaridad contra escalas de
hidrofobicidad que pide el Referee 1 (Wimley–White, PMID 8836100) está en el
párrafo nuevo al final de 3.2.2, en el bloque nuevo de 3.2.5 y en la Tabla S5.
Ya no queda ningún comentario asignado a vos sin responder.
