# Response to referees — MD-side comments (Enzo)

CP-ART-07-2026-002807.R1

Texto en inglés, listo para pegar en la carta. Los `[...]` son los únicos
huecos que tienes que llenar. Todos los números salen de tu Tabla 1 y de las
Figuras 3, 7 y 8 del manuscrito revisado.

---

## Referee 1 — comment 4

> *Fig. 1. Authors could plot order parameter profiles and difference order
> profiles to indicate the perturbations induced by inserting the respective
> amino acids.*

We thank the Reviewer for this suggestion, which we have adopted in full. A new
figure (Figure 3 of the revised manuscript) now presents the order parameter
data in the form requested, in three panels.

Panel (a) gives the absolute |S_CD| profile along the SDS chain for the
amino-acid-free control, comparing the ²H-NMR values of Table S1 with the
simulated profile. We note that Table S1 lists twelve rows per sample but only
seven distinct values, several carbons sharing a splitting to the hertz, so the
experimental values are drawn across the carbons that report each of them and
the simulated profile is averaged over the same groups. At that resolution the
two profiles correlate at r = 0.992, against 0.960 carbon by carbon. We also
state explicitly that the agreement is in shape rather than in amplitude: the
simulation overestimates the plateau by a factor of 1.14–1.21 and
underestimates the terminal methyl by 0.68, i.e. it produces a steeper order
gradient along the chain. We report this as a limitation of the force field
rather than absorbing it into an adjusted quadrupolar coupling constant, and we
note that every quantity used subsequently to compare systems is a difference
against the control, so that a multiplicative offset cancels to first order.

Panels (b) and (c) are the difference profiles the Reviewer asks for: the change
in |S_CD| on adding each amino acid, measured and simulated, drawn on a common
vertical scale, with a right-hand axis converting ΔS_CD to a change in
quadrupolar splitting through Δν_Q = (3/8)·(e²qQ/h)·S_CD. Both panels carry the
±√2σ noise band of the control, defined as the difference between two
independent amino-acid-free runs, so that the significance of each change can be
read directly. Because the degeneracy pattern of Table S1 differs between
samples, each difference is drawn on the common refinement of the sample and
control groupings.

We should state plainly what these panels show. The measured changes fall
outside the control noise band for GLU, LEU and MET, whereas every simulated
point falls inside it; only for ALA do measurement and simulation agree that
nothing happens. This discrepancy is discussed in a new Section 3.2.5, together
with the stoichiometric difference between simulation and experiment that we
believe explains it.

---

## Referee 1 — comment 6

> *One could also discuss the polarity of the amino acids with respect to their
> membrane binding. A useful measure could be hydrophobicity scales (PMID:
> 8836100) or logP values (partition coefficients between octanol and water).*

We thank the Reviewer for this suggestion and have added the comparison to
Section 3.2.2, together with a new Supporting Information table. It provides an
independent, experimentally grounded ordering against which our simulated
ordering can be tested, and it also clarifies a point that we had not previously
separated.

The Wimley–White interfacial scale, obtained from partitioning of host–guest
peptides into POPC interfaces, is the appropriate one here because it measures
transfer *to an interface* rather than to a hydrocarbon core, which is the
situation of our system. It ranks the four side chains studied here as
LEU (−0.56 ± 0.04 kcal mol⁻¹) > MET (−0.23 ± 0.06) > ALA (+0.17 ± 0.06) >
GLU⁻ (+2.02 ± 0.11), the anionic glutamate side chain being the only one for
which interfacial transfer is unfavourable. The octanol scale of the same work
gives the same ranking (−1.25, −0.67, +0.50 and +3.63 kcal mol⁻¹), as do the
octanol–water π values of Fauchère and Pliška (+1.70, +1.23, +0.31 and −0.64).

This is precisely the ordering returned by our simulations. Taking the
Wimley–White interfacial values as the reference, the Spearman rank correlation
with the contact fraction is −1.00, with the number of hydrogen bonds to water
+1.00, with the lateral diffusion coefficient +1.00 and with the residual
orientational order of the Cα→side-chain axis −1.00; the depth of the side-chain
density maximum gives +0.80, the single inversion being the one between LEU and
MET, which our own data do not resolve either (their side-chain termini sit at
0.66 half-thicknesses in both cases). We should be clear that these five
quantities are not independent tests of the same hypothesis — they are different
physical measurements of a common underlying property — but they are computed
from different observables with different error sources, and they agree with an
experimental scale that was determined on a different membrane system by a
different technique.

The correspondence supports our central claim: the common zwitterionic backbone
fixes the anchoring point at the interface, while the hydrophobic/hydrophilic
balance of the side chain alone determines how far, and in which direction, the
residue projects from it. The published scales are in fact the natural reference
for exactly this decomposition, since they were determined for side-chain
contributions with the peptide backbone held constant.

**Binding and perturbation are not the same ordering, and the comparison makes
that explicit.** The scales and the simulations agree on how strongly each
residue associates with the interface, LEU > MET > ALA > GLU⁻. The measured
perturbation of the chain order follows a different sequence,
LEU (−1548 Hz) > MET (−1534) > GLU (−1256) ≫ ALA (−93), averaged over C1–C11;
normalising by the molality of each sample, which is not the same for the four
(0.070–0.093 mol kg⁻¹), does not change it. ALA and GLU therefore exchange
places between the two orderings, and we now discuss this rather than leaving it
implicit.

We interpret it as two distinct mechanisms. Leucine and methionine perturb the
chains because they insert into them, and for those two the perturbation follows
hydrophobicity as expected. Alanine associates well but its side chain is a
single methyl group that occupies essentially no volume in the chain region, so
it binds without perturbing. Glutamate is the converse: it is the least
associated of the four and does not insert, yet it is the only charged species in
the set, and the Wimley–White values themselves localise its distinctiveness in
that charge — the neutral form of the same side chain has ΔG_wif = −0.01 ±
0.15 kcal mol⁻¹, close to alanine, against +2.02 for the anion. At the
experimental molality, an anionic solute and its counter-ions at an already
anionic sulfate interface modify the ionic environment of the head-group region,
and hence the head-group area and the chain order, without requiring insertion.
Our simulations, with one solute per 274 surfactants, are not constructed to
capture a collective electrostatic effect of that kind, and we present this as a
hypothesis consistent with the data rather than as a demonstrated mechanism.

## Referee 2 — comment 4

> *No analysis of molecular motions is presented, despite the manuscript title
> referring to the "dynamics of amino acids in a membrane mimetic". The authors
> should provide characteristic correlation times for the amino acids,
> particularly for atomic motions that influence the observed quadrupolar
> splittings. These times should then be related to the changes observed in the
> NMR spectra.*

We agree that the original manuscript did not deliver the dynamical analysis its
title announced, and we thank the Reviewer for pressing the point. A new Section
3.2.4 and a new figure (Figure 8) address it.

Reorientational dynamics are characterised through the second-rank correlation
function C(t) = ⟨P₂(u(0)·u(t))⟩, computed for the real C–H bond vectors read from
the topology and for the molecular axes, and averaged over five 20 ns blocks of
the 100–200 ns window. We report two methodological points that bear on how the
resulting times should be read. First, with the director fixed along the bilayer
normal, C(t) does not decay to zero but to a plateau equal to S_CD²; the square
root of that plateau reproduces the directly averaged order-parameter profile of
Figure 3a to within 0.001 at all twelve chain positions, which is an independent
check on both quantities by a completely different route. Second, the first
measurable lag is 20 ps and between 59 % and 99 % of the decay occurs below it,
so every correlation time reported here is the resolved, slow component and
therefore an upper bound on τ_c. We label it as such throughout rather than
quoting it as τ_c.

For the amino acids, correlation times of the Cα→side-chain axis are 374 ± 35 ps
(ALA), 451 ± 160 ps (GLU), 552 ± 78 ps (LEU) and 594 ± 92 ps (MET), and are
collected in Table 1. The four are indistinguishable within their errors: what
separates the amino acids is not the decay time but the plateau, i.e. the
fraction of orientation retained — LEU 0.64, MET 0.40, ALA 0.06, GLU 0.00.
Glutamic acid decays to zero, that is, it reorients isotropically, as a free
solute in water would. This ordering is identical to the one given independently
by the contact fraction, the immersion depth, the hydrogen bonding and the
lateral diffusion coefficient.

The relation to the NMR observables is made explicit in Figure 8d, which places
all eighteen deuterated groups of the study against the NMR time scale. The
largest splitting in the data set, 14 485 Hz, sets the most demanding scale at
1/Δν_Q = 69 µs, while the slowest of the eighteen C–D vectors reorients in
393 ps — more than 10⁵ times faster. This is what licenses interpreting the
measured splittings through the residual order parameter alone, and it is a
statement about an inequality: the motions that the 20 ps sampling does not
resolve are faster still, so they lie further inside the fast-motion limit and
cannot overturn the conclusion.

The same argument settles a point raised by the Reviewer in comment 8. The two
methionine states we report interconvert 51 times over the analysis window, with
mean dwell times of 2.1 and 1.6 ns. An exchange rate of ≈5 × 10⁸ s⁻¹ is five to
six orders of magnitude inside the fast-exchange limit, so the two states cannot
give rise to two resolved doublets; they contribute a single
population-weighted splitting.

---

## Referee 2 — comment 5

> *It would also be appropriate to provide order parameters and correlation times
> for the SDS chain segments in both the absence and presence of amino acids,
> followed by a discussion of how amino acid binding and penetration affect
> membrane dynamics. These quantities should be analysed in relation to the
> correlation times of the penetrating amino acids.*

These quantities are now reported for all five systems. Order parameters per
chain position, with and without each amino acid, are given in Figure 3 and
Table S1; resolved correlation times per chain position, for the control and the
four amino-acid systems, are given in Figure 8c and tabulated in Table S3.

For the control, the resolved correlation time falls monotonically from
203 ± 4 ps at C1, adjacent to the sulfate, to 68 ± 5 ps at the terminal methyl,
a threefold increase in mobility that tracks the decay of S_CD over the same
positions and shows the same step at C3/C4 that the order parameter shows in
Figure 3a. Separating the two time scales of the surfactant, local C–H
reorientation averaged over C1–C11 has a resolved time of 151 ± 1 ps, while
reorientation of the molecular long axis (C1→C12) is slower at 486 ± 6 ps, with
a residual order parameter of 0.76; only 21 % of the latter decay falls below
the sampling interval, which makes it the best-determined dynamical quantity in
the set.

On the question the Reviewer actually asks — how amino acid binding and
penetration affect membrane dynamics — we must report a negative result. At the
stoichiometry of the simulations the amino acids do not measurably change any of
this. In Figure 8c the five curves superimpose: no difference between the control
and any amino-acid system exceeds 2.1 σ at any chain position, and none is
larger than 9 % in magnitude. Four further observables agree that the simulated
membrane does not respond: ΔS_CD (Figure 3c), the gauche fraction per dihedral
(Figure S3b), the surfactant lateral diffusion coefficient (Figure S3c) and the
area per surfactant.

We have chosen to state this rather than to present a weaker effect as a real
one, and we have added a new Section 3.2.5 setting out why. The simulations
contain one amino acid per 274 surfactants, a mole fraction of 0.0036 against
0.040–0.053 in the experiment, roughly twelve times below the experimental
stoichiometry. The measured disordering is therefore a collective effect at
finite amino-acid concentration that a single-solute simulation is not
constructed to reproduce, and we no longer claim that it does: the sentence in
the Conclusions offering the simulations as a direct atomistic explanation for
the decrease in the quadrupolar splittings has been removed.

What the simulations do constrain, and what we now restrict our claims to, are
location and orientation — the contact fractions, immersion depths, angular
distributions and state populations of Table 1 and Figures 4 to 7 — none of
which scales with amino-acid concentration in the same way. Relating these to
the dynamics as the Reviewer suggests, the residual orientational order of the
Cα→side-chain axis (LEU 0.64, MET 0.40, ALA 0.06, GLU 0.00) reproduces the
insertion-depth ordering exactly, so the amino acids that penetrate are also the
ones whose motion is orientationally restricted by the chain region that hosts
them, while the amino acid that does not penetrate reorients isotropically.

---

## Referee 2 — comment 6

> *For each amino acid, the authors should provide a representative snapshot
> illustrating its characteristic location and orientation within the bilayer.*

We thank the Reviewer for this suggestion. These are now given as Figure 7.

Rather than selecting configurations by eye, we classified every bound frame by
k-means on three coordinates — the depth of Cα, the depth of the side-chain
terminal atom and cos θ — choosing the number of states by mean silhouette, and
we show the frame closest to each cluster centroid. The five panels share
camera, scale and coordinate origin (z = 0 at the hydrophobic centre, +z towards
the water of the host monolayer), so that depths are directly comparable between
them; the dashed line marks the mean sulfate plane of each configuration, and the
slab is cut 0.3 nm in front of and 1.6 nm behind the amino acid so that no head
group overlaps it.

Panels (a) to (c) show ALA, GLU and LEU, and panels (d) and (e) the two states of
MET. We give the fraction of bound frames each configuration represents, and
where the clustering has split a single physical state we say so: for LEU the
three clusters differ only in the depth of Cα and all place the side chain in the
core, so panel (c) represents 100 % of the bound frames rather than the 45 % held
by its own cluster; for GLU two of the three clusters point the side chain at the
water, together 85 %.

Methionine is shown in two panels because it is the only one of the four for
which the two states are genuinely distinct rather than a unimodal distribution
cut in two. This is supported in Figure 6: the mean silhouette is 0.655 at k = 2
for MET against 0.37–0.48 for the other three, and the two states, populated
57 % and 43 %, differ both in the depth of Cα and in the orientation of the
thioether (θ = 146° inserted, θ = 54° solvated). The partial density profile of
Figure 4d gives the same split independently, 55 % and 45 %, by a method sharing
neither definition nor error source with the clustering; applying a prominence
criterion, the second methionine maximum reaches 70 % of the profile maximum,
whereas the shoulders visible for the other three amino acids reach at most 4 %.

---

## Notas para ti, no van en la carta

1. **Los `[...]` de Wimley–White y logP ya están llenos**, con valores traídos de
   la fuente, no de memoria:
   - Escala interfacial y de octanol: `blanco.biomol.uci.edu/hydrophobicity_scales.html`,
     que es la página del propio laboratorio de Stephen White (Tabla 1 de Nat.
     Struct. Biol. 3:842, 1996 = PMID 8836100).
   - π de Fauchère–Pliška: ExPASy ProtScale, `Hphob.Fauchere.html`
     (Eur. J. Med. Chem. 18:369–375, 1983).
   - Todo reproducible con `python3 src/hydrophobicity.py` →
     `results/csv/hydrophobicity.csv`.

2. **Referencias de las escalas, en Vancouver** (detalle y versión RSC en D22):

   1. Wimley WC, White SH. Experimentally determined hydrophobicity scale for
      proteins at membrane interfaces. Nat Struct Biol. 1996;3(10):842-8.
   2. Wimley WC, Creamer TP, White SH. Solvation energies of amino acid side
      chains and backbone in a family of host-guest pentapeptides. Biochemistry.
      1996;35(16):5109-24.
   3. Fauchère JL, Pliška V. Hydrophobic parameters π of amino-acid side chains
      from the partitioning of N-acetyl-amino-acid amides. Eur J Med Chem.
      1983;18:369-75.

   La 2 solo hace falta si citas los valores de octanol.

3. **La frase pendiente sobre GLU cambió de forma.** Mi propuesta anterior
   (efecto colectivo por fuerza iónica) sigue en pie, pero ahora está apoyada en
   un dato en vez de ser una conjetura suelta: **la propia escala de
   Wimley–White localiza la rareza de GLU en su carga.** El glutámico neutro da
   ΔG_wif = −0.01, casi igual que ALA (+0.17); el anión da +2.02. O sea lo que
   lo hace desfavorable es la carga, y la carga es también el mecanismo
   plausible de su perturbación. Las dos mitades del argumento pasan a apoyarse
   en la misma propiedad. Igual va marcada como hipótesis.

4. **El punto que faltaba, y que es el aporte real de esta comparación:**
   unión y perturbación **no son el mismo ordenamiento**. Las escalas y el MD
   coinciden en la unión (LEU > MET > ALA > GLU), pero la perturbación medida va
   LEU > MET > GLU ≫ ALA. ALA y GLU se cruzan. Antes esto se leía como "una
   excepción que no explicamos"; ahora se lee como dos mecanismos distintos, que
   es un argumento y no una disculpa. Vale la pena que lo revises con Boris
   porque es lo más interpretativo de toda la respuesta.

5. **Normalizar por molalidad no cambia el orden**, lo verifiqué: las molalidades
   son 0.070 (LEU), 0.084 (MET), 0.093 (GLU) y 0.071 (ALA), y por unidad de
   molalidad queda LEU −22 100 > MET −18 300 > GLU −13 500 ≫ ALA −1 300 Hz. Lo
   menciono en la carta en una cláusula para adelantarme a la objeción, sin
   darle más peso del que tiene.

6. **Antes de mandar**, cierra con Amatista: numeración de carbonos de la Tabla
   S1, el segundo doblete de MET (su respuesta a R1 dice intercambio lento y tu
   MD dice rápido por cinco órdenes — no pueden ir las dos), y la contradicción
   entre f_b ≈ 1 en tu Tabla 1 y la "low bound fraction" de la Sección 3.1.

7. **Verificado contra los CSV:** todos los números que ya traía el documento
   (r = 0.992, factores 1.14–1.21 y 0.68, los τ, 51 interconversiones, 55/45,
   silueta 0.655, prominencia 70 %, 2.1 σ, 9 %, 393 ps, 10⁵) están bien. No
   toqué nada de eso.
