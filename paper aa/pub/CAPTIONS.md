# Figure captions (English)

Draft captions for the publication figures in this directory. Everything that
used to sit inside the panels — titles, method notes, caveats — lives here.
Numbering is provisional: the submitted manuscript already has Figures 1–8, so
these will be renumbered when the revised figure list is fixed.

All molecular dynamics quantities are averaged over the 100–200 ns window with
block averaging (5 blocks of 20 ns); error bars are the standard error over
blocks. Lengths are in nm.

---

## `fig_order_parameters` — order parameter profiles

**Figure X.** Deuterium order parameters of the SDS chain.
(a) Absolute order parameter |S_CD| per chain position for the amino-acid-free
control (S1). Black circles are the MD value for each carbon; the black dashed
segments are the MD value averaged over the carbons that share one experimental
value. Red segments are the ²H NMR values (Table S1), each drawn across the
carbons that report it: the table gives **seven distinct splittings** for the
twelve carbons, so C1–C4, C5–C6 and C7–C8 are not independent measurements.
Compared at that resolution, MD and experiment correlate with r = 0.992 (against
0.960 carbon by carbon); MD overestimates the plateau by a factor of 1.14–1.21
and underestimates the terminal methyl by 0.68, i.e. it has a steeper order
gradient along the chain rather than a uniform offset.
(b) Change in |S_CD| on adding one amino acid, from ²H NMR. The degeneracy
pattern of Table S1 is not the same in every sample (S1 and S2 group C5–C6 and
C7–C8; S3 groups C5–C8; S4 and S5 group C5–C7), so each difference is drawn on
the common refinement of the sample and the control groupings.
(c) The same quantity from MD, on the same vertical scale. The grey band in both
panels is the ±√2σ noise of the control, i.e. the difference between two
independent runs that contain no amino acid. The experimental points for GLU,
LEU and MET fall an order of magnitude outside that band, while every MD point
lies inside it. ALA is the exception in the experiment as well: its measured
effect (−0.0015 averaged over C1–C11) is within the noise, so for ALA the
simulation and the measurement agree that nothing happens.
The right axis converts ΔS_CD to a change in quadrupolar splitting through
Δν_Q = (3/8)·QCC·S_CD with QCC = 167 kHz.

**Open point.** Table S1 reports seven distinct values per sample; whether the
repeated entries correspond to genuinely unresolved lines or to separate
assignments that coincide is not stated in the manuscript and should be confirmed
with the NMR authors before the caption commits to either wording.

**Note for the text.** At one amino acid per 274 SDS — twelve times below the
experimental stoichiometry — the simulations cannot reproduce the magnitude of
the measured disordering, and panel (c) says so explicitly rather than leaving
it implied.

---

## `fig_dynamics` — reorientational dynamics and the fast-motion limit

**Figure X.** Reorientational correlation of the C–H (C–D) vectors and of the
molecular axes. All correlation times are the resolved integral `tau_cut` of
`tau_blocks.py`, averaged over five 20 ns blocks; error bars are the standard
error over blocks.
(a) C(t) = ⟨P₂(u(0)·u(t))⟩ for four representative carbons of SDS in the
control. The shaded band is the region below the first measurable lag (20 ps):
the dotted segments join C(0) = 1 to the first computed point, so the fraction
of the decay that the 20 ps sampling cannot resolve — between 59 % and 99 %,
growing towards the chain terminus — is visible rather than implied. Each curve
settles on a plateau equal to S_CD²; the square root of that plateau reproduces
the profile of the order-parameter figure to within 0.001, an independent check.
(b) The same function for the molecular axes: C1→C12 for SDS and Cα→side chain
for each amino acid. These are not C–D vectors, so their plateau is the squared
order parameter of that axis, not S_CD². What the panel shows is the plateau,
not the decay time: LEU 0.64, MET 0.40, ALA 0.06, GLU 0.00, i.e. the same
hydrophobicity ranking given independently by the contact fraction, the
immersion depth, the hydrogen bonding and the lateral diffusion. GLU decays to
zero — it reorients isotropically, like a free solute in water.
(c) Resolved correlation time per chain position, control and the four
amino-acid systems. The chain becomes threefold more mobile from C1 (203 ± 4 ps,
next to the sulfate) to C12 (68 ± 5 ps): τ and S_CD fall together, and the step
at C3/C4 reproduces the alternation already present in the order-parameter
profile. The five systems superimpose — no difference exceeds 2.1 σ and the
largest is +8 % — so at this stoichiometry the amino acid changes neither the
degree of order of the chain nor the rate at which it reorients.
(d) All eighteen deuterated groups against the NMR time scale 1/Δν_Q = 69 µs set
by the largest splitting in the data set (14.485 kHz). The slowest group is more
than 10⁵ times faster.

**Note for the text.** These are resolved times, i.e. upper bounds on τ_c: the
first measurable lag is 20 ps and most of the decay occurs below it, as panel
(a) shows. The unresolved motions are *faster*, so they sit further inside the
fast-motion limit and the inequality does not depend on them. That is what
licenses interpreting the splittings through the residual order parameter alone
— and it also means the quantity plotted in (c) and (d) must be described as the
resolved (slow) component, not as τ_c without qualification.

**Note for the text.** The correlation times of the amino acids come from a
single molecule per box: the standard errors are 12–137 ps on means of 85–594 ps,
and where the integral and the biexponential fit disagree (GLU, LEU) the value is
not determined. They are reported as upper bounds, never as measurements.

---

## `fig_orientation` — location and orientation of the amino acids

**Figure X.** Orientation of the amino acid side chain in the aggregate, from the
frames in which the amino acid is in contact with it (heavy-atom cutoff 0.4 nm).
(a) Distribution of the angle θ between the Cα→side-chain vector and the outward
normal of the host monolayer, divided by sin θ so that an isotropic distribution
is flat (dotted line). θ = 0 points into water, θ = 180° into the hydrophobic
core. Vectors: ALA Cα→Cβ, GLU Cα→Cδ, LEU Cα→Cγ, MET Cα→Sδ. f_b is the fraction
of frames in contact with the aggregate. LEU has strictly zero population below
120°: its side chain is always in the core.
(b) Every bound frame of the MET trajectory in the plane of Cα depth and side
chain orientation, coloured by k-means cluster; filled circles are the cluster
centroids and the percentages are their populations.
(c) Mean silhouette against the number of clusters k. MET is the only one of the
four with a well-separated two-state partition (0.65 at k = 2, against 0.37–0.48
for the others), which is what supports the two-state description rather than a
choice of representative snapshots.

---

## `fig_snapshots` — representative configurations

**Figure X.** Cross-sections of the aggregate showing the most populated state of
each amino acid (a–c), and the two states of MET (d, e). The first percentage is
the fraction of bound frames assigned to that cluster. Where a second line
appears, the clustering has split one physical state: for LEU the three clusters
differ in the depth of Cα but all place the side chain in the core, so the
configuration shown is representative of 100 % of the bound frames and not of the
45 % that its own cluster holds; for GLU two of the three clusters point the side
chain at the water, together 85 %. ALA and MET carry no second line because there
the clusters are genuinely distinct orientations — which is the point of the
MET panel pair.

Each panel is the frame closest to its cluster centroid — k-means on the depth of
Cα, the depth of the side-chain terminal atom and cos θ, with k chosen by mean
silhouette — and not a snapshot selected by eye. The five panels share camera,
scale and coordinate origin: z = 0 at the hydrophobic centre and +z towards the
water of the monolayer that hosts the amino acid, so depths are directly
comparable between panels. The dashed line marks the mean sulfate plane of that
configuration. The slab is taken 0.3 nm in front of the amino acid and 1.6 nm
behind it, so that no head group overlaps it. Water is drawn only up to 1.1 nm
beyond the sulfate plane and counter-ions only within 0.5 nm of a sulfate oxygen.

Amino-acid carbons carry the colour of the panel; N, O and S follow the standard
CPK code. The palette is chosen so that no amino-acid colour can be confused with
a heteroatom.

---

## `figS_convergence` — equilibration (Supporting Information)

**Figure SX.** Area per SDS (a) and sulfur–sulfur bilayer thickness (b) against
time for the five systems. Thin traces are per-frame values, thick traces a 25-
frame moving average. The shaded region is discarded from all analysis: the
control is still contracting until ≈100 ns, and over the 50–200 ns window used
originally its residual drift produces an apparent ΔS_CD of +0.010 that
correlates with the drift in area at R² = 0.997. All results reported here use
100–200 ns.

---

## `figS_structure` — quantitative structural and dynamic metrics (SI)

**Figure SX.** (a) Gauche fraction of each C–C–C–C dihedral of the SDS chain; the
five curves superimpose. (b) The same quantity as a difference against the
control: all four amino acids are zero within one standard error (|Δ| ≤ 0.0013).
(c) Lateral mean-square displacement of the host amphiphiles and of all four
amino acids, computed with the centre of mass of each monolayer removed
separately; the shaded region is the fitting window, where the log–log slope is
0.83–1.02, i.e. normal diffusion. The ordering GLU ≫ ALA > MET > LEU is the exact
inverse of the contact fraction. The amino-acid traces come from one molecule per
box and are indicative, as stated in the panel. (d) Hydrogen bonds of the
amino acid per frame, with the aggregate (sulfate plus decanol hydroxyl) and with
water; criterion d(D···A) ≤ 0.35 nm and ∠D–H···A ≥ 150°.

**Note for the text.** Panels (a) and (b) confirm through a non-orientational
observable what the order parameters already show: at this stoichiometry the
amino acids do not measurably disorder the chains. In (d), the bonds to the
aggregate come almost entirely from the ammonium group, which all four amino
acids share, so that comparison is like for like; the water column is not, since
GLU carries four acceptor oxygens against two for the others.

All quantities in (d) come from a single amino-acid molecule per box and are
reported as indicative. What makes the ranking defensible is that four
independent observables — contact fraction, orientation, hydrogen bonding and
lateral diffusion — give the same order, LEU > MET > ALA > GLU.

---

## `figS_atom_labels` — atom naming (SI)

**Figure SX.** Heavy-atom naming of the four amino acids, as used throughout the
text and figures. Carbons carry the colour of the amino acid, N, O and S the
standard CPK code; hydrogens are omitted. Boxed bold labels mark the deuterated
positions of the ²H-labelled compounds (ALA-d₄: Cβ; GLU-d₅: Cβ and Cγ; LEU-d₃:
Cδ1 and Cδ2; MET-d₃: Cε), i.e. the vectors whose reorientational correlation
functions are shown in the dynamics figure. The dashed arrow is the Cα→side-chain
vector whose angle with the monolayer normal defines θ in the orientation figure;
the pair is repeated at the lower right of each panel.

Each panel is a real frame of the corresponding trajectory, selected together
with the viewing direction so that no two non-bonded heavy atoms overlap in
projection (minimum projected separation 2.18–2.30 Å). The conformations shown
are therefore chosen for legibility of the naming and are not representative of
the populated states, which are given in the snapshot figure. All four panels
share the same length scale.

---

## `figS_exp_scd` — experimental order parameter profiles (SI)

**Figure SX.** ²H NMR order parameters of the SDS chain in the four
amino-acid-containing samples, obtained from the quadrupolar splittings of
Table S1 through |S_CD| = Δν_Q / (3/8 · QCC) with QCC = 167 kHz and the director
perpendicular to B₀, i.e. |S_CD| = Δν_Q / 62 625 Hz. Carbon numbering is inverted
with respect to the printed table (C1 adjacent to the sulfate, C12 the terminal
methyl), which is the assignment consistent with the chain order profile.
(a) Absolute profiles, with the amino-acid-free control (S1, dashed black) for
reference; the right axis is the corresponding splitting. Each value is drawn as
a segment spanning the carbons that share one line, since Table S1 resolves seven
lines per sample and the degeneracy pattern differs between samples (S1 and S2
group C1–C4, C5–C6 and C7–C8; S3 groups C1–C3 and C5–C8; S4 and S5 group C1–C4
and C6–C8). LEU and MET differ by at most 0.0005 at every position, far below the
line width, and are therefore plotted as a wide green trace with the pink one on
top: wherever a green halo is visible the two samples coincide.
(b) The same data as a ratio to the control. The effect is close to
multiplicative rather than localised: LEU and MET reduce the order parameter by a
nearly constant factor along the whole chain (0.881 ± 0.012 and 0.883 ± 0.013
averaged over the twelve positions), GLU by 0.906 ± 0.021, and ALA is
indistinguishable from the control (0.993 ± 0.003).

**Note for the text.** Panel (b) is the argument against localising the amino
acid by the region of the chain it perturbs: within the resolution of Table S1
the disordering is proportional along the whole chain, so the profile shape does
not by itself place the molecule at any particular depth. That placement comes
from the simulations, not from the splittings.

Source data: `results/csv/exp_scd_tabla_S1.csv`.

---

## `figS_aa_scd` — amino acid order parameters, MD vs ²H NMR (SI)

**Figure SX.** Order parameters of the amino acids themselves.
(a) |S_CD| from MD for every non-exchangeable C–H position of the four amino
acids (the ammonium protons exchange with water and cannot be labelled); hatched
bars are methyl groups, whose value already includes the averaging by CD₃
rotation and is therefore directly comparable with the observed splitting. The
right axis is the corresponding quadrupolar splitting. Error bars are standard
errors of the time average corrected for autocorrelation, σ√(2τ_int/T), where
τ_int is the integrated correlation time of the P₂ series itself; the number of
statistically independent samples is 52–775, not the 5000 frames.
(b) The same on the scale of the positions the experiment reports, with the
²H NMR splittings of Table S2 (red). MET-d₃ and LEU-d₃ carry three deuterons out
of eight and ten available positions and are therefore site-specific methyl
labels; ALA-d₄ and GLU-d₅ carry four and five out of four and five, i.e. they are
perdeuterated at every non-exchangeable position. The five GLU-d₅ splittings are
listed without assignment in the manuscript and are drawn as dashed levels across
the whole GLU group.
(c) Cumulative time average of S_CD for the labelled methyls over the analysis
window, with the experimental values for comparison.

**Note for the text.** Only MET agrees quantitatively: 1.09 ± 0.31 kHz from MD
against 0.79 kHz measured, i.e. within one standard error. ALA is consistent but
uninformative, since the uncertainty of the simulation is larger than the
measured splitting itself. LEU disagrees by a factor of 4.5–5 and by six standard
errors. Panel (c) identifies the cause as sampling rather than force field: the
two chemically equivalent methyls of LEU converge to order parameters of opposite
sign (+0.042 and −0.046), which cannot happen in a converged ensemble average,
and the backbone positions of LEU reach |S_CD| ≈ 0.31, larger than the plateau of
the surfactant chain that hosts it. Both are signatures of a single solute
molecule that does not reorient within 100 ns. With one amino acid per box the
average is purely temporal, so the accessible statistics are set by the number of
independent reorientations and not by the length of the trajectory. The
simulations therefore constrain the *location and orientation* of the amino acid,
which is what the clustering and contact analyses report, but they cannot be
asked to reproduce its splittings.

Source data: `results/csv/aa_scd.csv`, `results/csv/aa_scd_per_H.csv`,
`results/csv/aa_scd_running.csv`.
