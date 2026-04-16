---
tipo: manuscrito
estado: en-desarrollo
rol-enzo: simulaciones MD + análisis
coautores: [Amatista San Martín, Enzo Cevo, Boris Weiss-López, Diego Muñoz-Gacitúa]
herramienta: GROMACS 2021.1, OPLS-aa, TIP4P, MDAnalysis
sistema: SDS/DeOH/KCl bicelle (DNLLC) — 274 SDS, 80 DeOH, 15543 waters
aminoacidos: [ALA, GLU, LEU, MET]
duracion-prod: 200 ns NPT por AA
tema: Localización, orientación y dinámica de aminoácidos en bicapa discótica (membrane mimetic), complementario a 2H-NMR
fuente: PAPER_AA_DYNAMICS_v3.pdf (extraído con pdftotext)
---

# Location, Average Orientation and Dynamics of Amino Acids in a Membrane Mimetic: ²H-NMR and Molecular Dynamics Study


Amatista San Martín*, Enzo Cevo, Boris Weiss-López, Diego Muñoz-Gacitúa

Abstract


A better knowledge about the behavior of amino acids (AA) when dissolved in cell
membranes is crucial to understand AA passive transport mechanisms. However, the average
orientation, distribution, and dynamics of most AA at the lipid bilayer and interface remains
poorly characterized. In this paper, we have investigated the behavior of four AA (ALA,
LEU, GLU and MET), when dissolved in a discotic bicellar lyotropic liquid crystal
membrane mimetics. This membrane was based of sodium dodecyl sulfate (SDS) and
decanol (DeOH). For this purpose, we have used a combination of ²H-NMR spectroscopy
and all-atom Molecular Dynamics simulations (MD). ²H-NMR of deuterated AA confirmed
that all four molecules are strongly associated to both bilayer aggregates, exhibiting
significant splittings, revealing that all AA induce bilayer disorder, with the most
hydrophobic causing the largest perturbation. MD provides an explanation for these findings.
All AA anchor to the interface via their zwitterion, however their side chains adopt different
preferential orientations, based on a hydrophobic/hydrophilic balance. ALA has the smallest
size hydrophobic chain and do not perturb the equilibrium dynamics of the aggregate. LEU
and MET contain more hydrophobic sidechain and penetrate deeper into the hydrophobic
core. GLU remains at the interface, strongly anchored by the zwitterion and the carboxylate
groups. The results show that passive AA-membrane association is governed by electrostatic
anchoring of the zwitterion to the interface and hydrophobic/hydrophilic partitioning of the
side chain.

1. Introduction

Cell membrane, mostly composed of phospholipid bilayers, is a natural barrier that control
the passage of essential molecules in and out the cytosol [1]. Among these molecules, amino
acids (AA) are the fundamental building blocks for protein synthesis. Due to their
zwitterionic nature at physiological pH, AA are generally hydrophilic, and their transport
across the hydrophobic membrane core is energetically unfavorable. However, the occurrence
of AA transport driven by electrochemical and concentration gradients, cannot be entirely
dismissed [3]. Understanding the fundamental non-facilitated interactions of AA with lipid
membranes is crucial for a complete picture of cellular homeostasis and has implications in
drug delivery and peptide-membrane interactions [4, 5].

Despite that several studies have investigated AA-membrane interactions [5a, 6, 7], specific
details about average orientation, dynamics, and spatial distribution within the membrane,
remains poorly characterized [ ]. It is hypothesized that these properties are strongly
dependent on the different physicochemical properties of each AA side chain such as charge,
hydrophobicity, size, etc.
A study of these phenomena in cell membranes is a very complex task, due to their wide
compositional heterogeneity [8]. Therefore, membrane mimetics, such as micelles, bicelles,
and vesicles, have been widely employed for these purposes [8]. These simplified models
replicate the fundamental anisotropic environment of a biological membrane, allowing for
more controlled investigations [9]. In this context, discotic nematic lyotropic liquid crystals
(DNLLC), such as those formed by a mixture of sodium dodecyl sulfate (SDS) and
decan-1-ol (DeOH), dissolved in a water-salt solution, are simplified models that form
stable nematic discotic bilayer aggregates, which mimic the planar aqueous interface and
the hydrophobic bilayer [10]. These bicelles spontaneously orient in external magnetic
fields, with the symmetry axis of the disk perpendicular to the direction of the field, giving
rise to 2H-NMR quadrupole splittings [10a].

Experimental techniques, such as 2H-NMR spectroscopy, provides valuable information on
average molecular order [11] and rigidity. Besides, Molecular Dynamics simulations (MD)
offers a unique classical mechanics representation of the complete system at atomistic
resolution [11]. MD allows for the direct observation of molecular motions, the calculation of
interaction energies, and the characterization of spatial distributions as a function of time,
among others [11].

In this paper we have used 2 H-NMR spectroscopy and all-atom MD simulations to
investigate the behavior of four AA with different side chain properties: glutamic acid
(GLU-d5, anionic), leucine (LEU-d3, hydrophobic), methionine (MET-d3, hydrophobic), and
alanine (ALA-d3, small nonpolar), when dissolved in a SDS/DeOH/KCl/H2O DNLLC
solution. Our goal is to provide a description of their average orientation, spatial distribution,
and dynamics, when dissolved in the model membrane, providing insights on the role of the
AA side chain in passive transport mechanism.

2 . Materials and Methods

2.1 ​. Materials
SDS, SDS-d25, KCl, AA and deuterated AA were all purchased from Sigma-Aldrich and used
as received. Chromatographic grade water and deuterated water (D2O) were purchased from
Merck and used as received.

2.2 ​. Sample Preparation
The membrane mimetic consists of a mixture of SDS, DeOH and KCl, all dissolved in H2O.
Table 1 shows the amount of each component in all samples. A series of 2H-NMR
experiments, samples S1 to S5, were conducted to probe the membrane order
modifications when adding non-deuterated AA to the mesophase containing small amounts
of SDS-d25 The amount of AA added in S2-S5 are shown in Table 2. Samples S6 to S9 were
prepared to probe the AA themselves and consisted of selectively deuterated AA added to the
liquid crystal containing only non-deuterated SDS. Control sample containing no AA (S1)
was also prepared.
Table 1: Composition of the mesophase for S1-S5.
Component Molality (mol⋅kg-1)
SDS             1.746
DeOH             0.533
KCl             0.261
SDS-d25           0.062

Table 2: Amount of AA added in S2-S5.
Sample     Amino     Molality​(mol⋅kg-1)
Acid
1          —               —
2         ALA            0.071
3         GLU            0.093
4         LEU            0.070
5        MET             0.084

All samples were homogenized on a slow rotatory agitator for at least 24 hours at 37 °C to
ensure phase stability and homogeneity. The formation of the nematic liquid crystal phase
was confirmed by observing sample birefringence in between two crossed light polarizers,
before samples were transferred to 5 mm NMR tubes.

2.3 ​. ²H-NMR Spectroscopy
All ²H-NMR spectra were acquired in a 400 MHz Bruker Avance multinuclear spectrometer,
at the Universidad de Santiago de Chile, operating at a 2H frequency of 61.422 MHz. The
sample temperature was maintained at 37 °C in all measurements. Quadrupole splitting were
measured from the separation between the two peaks of each Pake doublet. Assignments
were performed using peak integrals and the assumption that the deuterium located closer to
the bilayer center should show higher mobility and smaller splittings.

2.4 ​. Molecular Dynamics (MD) Simulations
All MD simulations and analysis were performed using the package GROMACS 2021.1
(ref1). Packmol (ref2) was used to setup a bilayer mimetic composed of 274 SDS, 80 DeOH,
274 Na⁺, 62 K⁺, 62 Cl⁻ and 15,543 water molecules. The Optimize Potential for Liquid
Simulations-all atoms (OPLS-aa) force field was used for all organic molecules and ions, and
the TIP4P model was used for water (ref3, ref4). Temperature was controlled with the
V-rescale thermostat (τ       = 0.1 ps, Tₐₑₑ = 310 K, 37 °C) and pressure with the
Parrinello-Rahman semi-isotropic barostat (τₚ = 2.0 ps, Pₐₑₑ = 1 bar) (ref5, ref6). A time step
of 2 fs was used, with H-bond lengths constrained by the LINCS algorithm. Electrostatic and
van der Waals interactions were both treated with Particle Mesh Ewald (PME) with a
real-space cutoff of 1.3 nm. The assembled system was first subjected to energy
minimization, followed by 200 ps NVT and 1 ns NPT equilibration. A 200 ns NPT
production run was then calculated for each amino acid, from which all analyses were
performed. The MDAnalysis Python library (ref) was used for post-processing and analysis
of the production trajectories, including the calculation of mass density profiles along the
bilayer normal and radial distribution functions.
3. Results and discussion

3.1. ²H-NMR Spectroscopy

Figure 1 display the ²H-NMR spectra from DeOH-d25 in the aggregate and all measured
quadrupole splittings can be found in supporting information. Figure 2 shows the ²H-NMR
spectra of deuterated AA, along with the measured quadrupole splittings. in which the
splittings show that all AA are strongly associated to the aggregate, affecting their integrity
by modifying their mobility. However, the magnitude of this perturbation depends on the AA
side chain properties.




Figure 1: ²H-NMR spectra of S1-S5.
Figure 2: ²H-NMR spectra of S6-S9.

ALA produces virtually no perturbation in the dynamics of the aggregate. This is no surprise
since it has the smallest hydrophobic side chain and does not incorporate into the interior of
the bilayer; hence, it remains anchored to the interface, stabilized by electrostatic interactions
with the zwitterion.

GLU exhibits small modifications in the quadrupolar splittings of the hydrophobic interior of
the bilayer, owing to its hydrophilic side chain. This interaction keeps GLU on the upper
layers of the membrane, anchored by electrostatic interactions of the zwitterion in addition of
the carboxylate groups with the interface.

In contrast, LEU and MET both possesses more hydrophobic and longer side chains. The
2
H-NMR spectra from SDS-d25 in the presence of these amino acids are remarkably similar.
With the addition of LEU and MET the quadrupole splittings of the deuterium atoms attached
to C1 to C4, those closer to the hydrophilic head group of SDS, experience the most
significant decrease. This indicates that LEU and MET perturb the interfacial order by
anchoring through electrostatic interactions. The hydrophobic side chains of both, LEU and
MET, appear to be orienting towards the interior of the bilayer inducing disorder that
propagates to the interior of the bilayer, and, consequently, modifying the quadrupole
splittings of these regions.
3.2 Molecular Dynamics Simulations

MD simulations provide a simple interpretation of the experimental observations. All AA
were initially positioned in the water phase and spontaneously diffused to the interior of the
aggregate, anchoring at the interface via electrostatic interactions with the zwitterion. By
calculating partial density profiles (PDP) along the axis perpendicular to the bilayer plane
(Z-axis), we characterized the average location and orientation of each AA within the
aggregate.

3.2.1. Spatial Distribution and Interfacial Anchoring

To further quantify the degree of penetration and the average orientation of the AAs within
the SDS/DeOH aggregate, we analyzed the distance between the center of the bilayer (Z=0)
and the maximum partial density of the zwitterionic carboxyl group (ZCG) and the side-chain
terminus (ZLC). The displacement parameter, ∆Z = ZCG - ZLC, serves as a direct indicator of
the orientation vector relative to the bilayer normal.

Table 3. Maximum partial density positions (Z) and calculated displacement (∆Z) for the
studied amino acids.
Amino Acid ZCG​(nm) ZLC​(nm) ΔZ (nm)           Orientation
ALA           1.760          1.760  0.000      Parallel
GLU           1.739          1.739  0.000      Parallel
MET           1.428         0.908*  0.520 Tilted/Penetrating
LEU           1.430          0.910  0.520 Tilted/Penetrating
*Main peak closer to the bilayer core.

The PDP for ALA (Figure 3A) shows that the methyl group (Cβ) and the α-carboxyl carbon
(C) reach nearly identical maximum densities at the same distance from the bilayer center
(~1.7 nm), indicating that the Cα–Cβ axis lies approximately parallel to the bilayer plane.
This flat orientation confines ALA entirely to the interfacial layer, consistent with the
negligible perturbation observed in the ²H-NMR spectra. The sharp water density drop at the
same Z position confirms that ALA resides at the bilayer–water boundary. For GLU (Figure
3B), both the α-carboxyl (C) and the lateral-chain carboxylate carbon (Cδ) are located at the
same interfacial depth (ΔZ ≈ 0). Combined with the strong Na⁺ coordination revealed by the
RDF (Section 3.2.2), this indicates that GLU is doubly anchored at the surface — via its
zwitterion and its side-chain carboxylate — and is therefore unable to insert into the
hydrophobic core, explaining the minor perturbation in sample S3.
Figure 3. (A) Partial density of the ALA methyl carbon (Cβ, solid blue) and α-carboxyl
carbon (C, dashed red) as a function of distance from the bilayer center, overlaid on bilayer
component densities. (B) Corresponding profiles for the GLU lateral-chain carboxyl carbon
(Cδ, solid blue) and α-carboxyl carbon (C, dashed red).

For ALA and GLU, the displacement ΔZ is null (Table 3), demonstrating that both the
backbone and the side chain are confined to the same interfacial plane. The absence of
penetration explains the minimal impact of ALA on the SDS-d₂₅ quadrupolar splittings. In the
case of GLU, its hydrophilic nature and the presence of a second carboxylate group
reinforces its anchoring at the aqueous interface, preventing any insertion into the
hydrophobic core.
Figure 5. (A) [PLACEHOLDER — MET density figure pending completion of the 200 ns
production trajectory. Pre-computed analysis confirms a bimodal side-chain (SD) distribution
at approximately 0.91 nm and 1.95 nm from the bilayer center.] (B) Partial density of the
LEU branch-point carbon (Cγ, solid blue) and α-carboxyl carbon (C, dashed red), overlaid on
bilayer component densities.

Figure 5 displays the density profiles of LEU and MET. LEU (panel B) exhibits a clear
spatial separation between the backbone anchor (α-carboxyl C, ~1.4 nm) and the side-chain
terminus (Cγ, ~0.91 nm), yielding ΔZ ≈ 0.52 nm. This displacement places the isobutyl group
within the C1–C4 region of the SDS chains, the same region that exhibits the largest decrease
in quadrupolar splittings in sample S4. The overlap of the Cγ density with the SDS chain
density confirms direct hydrophobic contact. For MET (panel A), pre-computed density data
indicate a bimodal distribution of the thioether sulfur (SD) at ~0.91 nm and ~1.95 nm from
the bilayer center, suggesting a dynamic equilibrium between a buried and an interfacial
conformation. Full quantitative analysis is pending [PLACEHOLDER]. Qualitatively, MET
behavior parallels LEU, consistent with the nearly identical ²H-NMR spectra of samples S4
and S5.

The penetration of approximately 0.5 nm by both LEU and MET places their side chains in
direct contact with the C1–C4 region of SDS, providing a clear structural explanation for the
decrease in quadrupolar splittings observed in samples S4 and S5. The magnitude of
perturbation is similar for both AA, as confirmed by the nearly identical ²H-NMR spectra,
consistent with the comparable depth of insertion derived from the density profiles.
3.2.2. Radial Distribution Functions

To complement the PDP analysis, radial distribution functions (RDF) were calculated using
the gmx rdf tool to characterize the local coordination environment of each AA side chain
with respect to the bilayer components and the aqueous solvent. For each amino acid, the
RDF reference atom was chosen as the side-chain terminus or the most chemically distinctive
atom: Cα for ALA, OE1 (side-chain carboxylate oxygen) for GLU, Cγ (branch-point carbon)
for LEU, and SD (thioether sulfur) for MET. The target groups were selected to probe the
relevant interactions at each location: for ALA, the targets were the SDS sulfur headgroup
(S), the SDS alkyl chain carbons (C1–C12), and water oxygen (OW); for GLU, the targets
were Na⁺ counterions and water oxygen; for LEU, the SDS chain was divided into an upper
segment (C2–C8) and a lower tail segment (C9–C12), along with water oxygen, to resolve
the depth of hydrophobic contact. These functions (Figures 7–10) provide direct evidence of
the molecular-level interactions that govern the preferential location and orientation of each
AA.
Figure 7. RDF of the ALA α-carbon (Cα) relative to the SDS sulfur headgroup (S, orange
solid), SDS chain carbons C1–C12 (dark orange dashed), and water oxygen (OW, blue
dotted).
Figure 8. RDF of the GLU side-chain carboxylate oxygen (OE₁) relative to Na⁺ (purple solid)
and water oxygen (OW, blue dashed).

For ALA (Figure 7), the dominant feature is an intense first peak with water at r ≈ 0.28 nm,
confirming full solvation of the α-carbon at the interface. The SDS sulfur peak at slightly
larger distances reflects proximity of the zwitterion to the SDS headgroup layer, consistent
with the surface-parallel orientation from the PDP.​
The GLU RDF (Figure 8) is dominated by a sharp coordination peak with Na⁺ at r ≈ 0.25 nm,
arising from direct ion pairing between the side-chain carboxylate (O₌₁) and the sodium
counterions concentrated at the SDS headgroup region. This strong ionic interaction —
occurring at the same interfacial depth as the α-carboxyl anchor — confirms the
double-anchoring mechanism that prevents any GLU insertion into the hydrophobic core.
Figure 9. RDF of the LEU branch-point carbon (Cγ) relative to SDS chain carbons C2–C8
(dark orange solid), SDS tail carbons C9–C12 (brown dashed), and water oxygen (OW, blue
dotted).

Figure 10. [PLACEHOLDER — RDF computed with MET Cγ as provisional reference; will
be recomputed with MET SD (thioether sulfur) as reference upon completion of the 200 ns
trajectory. Targets: SDS C2–C8, SDS C9–C12, and water.]

The LEU RDF (Figure 9) shows a clear reversal relative to ALA: water coordination is
suppressed, while structured peaks with SDS chain (C2–C8) and tail (C9–C12) carbons
appear at r < 0.6 nm, indicating that Cγ resides in a predominantly hydrophobic environment.
The first peak with the SDS chain segment at r ≈ 0.42 nm is particularly prominent,
consistent with the PDP result placing Cγ at 0.91 nm within the C1–C8 region of the SDS
monolayer. The broader, lower-intensity contact with the tail segment suggests that the
isobutyl group does not penetrate as far as the terminal methyls of SDS, but maintains partial
contact with the deeper hydrophobic region.​
For MET, preliminary RDF analysis using Cγ as reference (Figure 10, provisional) shows a
coordination environment intermediate between the interfacial (ALA/GLU) and deeply
buried (LEU) regimes, consistent with the bimodal distribution observed in the density
profile. The final RDF with SD as reference will be reported upon completion of the 200 ns
trajectory [PLACEHOLDER].

4. Conclusions

In this study, the behavior of four amino acids with distinct side-chain properties was
successfully characterized within an SDS/DeOH-based membrane mimetic using a
combination of 2H-NMR spectroscopy and all-atom molecular dynamics simulations. The
results demonstrate that all studied amino acids associate strongly with the liquid crystal
aggregate, predominantly locating at the bilayer interface. This association is fundamentally
governed by the electrostatic anchoring of the zwitterionic group to the hydrophilic region of
the membrane. While the interfacial anchoring is common to all species, the preferential
orientation of the side chains is strictly dependent on their hydrophobic or hydrophilic
balance. Specifically, alanine and glutamic acid maintain an orientation parallel to the bilayer
plane, remaining confined to the interface without perturbing the equilibrium dynamics of the
hydrophobic core. In contrast, leucine and methionine exhibit significant penetration into the
membrane interior, with their hydrophobic side chains reaching a depth of approximately 0.9
nm from the bilayer center. This insertion induces a structural disorder in the SDS acyl chains
that propagates toward the bilayer interior, providing a clear atomistic explanation for the
decrease in quadrupole splittings observed in the NMR spectra. Ultimately, these findings
provide a detailed picture of the non-facilitated interactions between amino acids and lipid
membranes, highlighting how side-chain partitioning modulates the structural integrity and
dynamics of the lipid environment.
