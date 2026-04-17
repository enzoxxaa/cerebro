---
tipo: manuscrito
estado: borrador-avanzado
rol-enzo: simulaciones MD + análisis MMPBSA + análisis de mutantes in silico
coautores: [incluye comentarios EC12 — Enzo Cevo autor/colaborador en sección de MD]
herramienta: AMBER24, ff19SB, GAFF, Propka, PDB2PQR, MMPBSA
sistema: MttPFK/GK (Methanothermococcus thermolithotrophicus) — riboquinasa bifuncional ADP-dependiente
ligandos: [ADP/ADPbs, AMP, glucosa, F6P, Mg2+]
tecnicas: Cristalografía X (MANACA beamline, SIRIUS LNLS) + MD 5 réplicas x 400 ns + MMPBSA + mutagénesis dirigida (Y56A, R58A, R58E, H72A, S275A)
tema: Base estructural de la activación alostérica por AMP en quinasa de azúcares bifuncional arqueal. Identificación de un nuevo sitio alostérico y conformación "super-cerrada" estabilizada por AMP.
relevancia-bioinfo: altísima — allostery, dinámica de proteínas, diseño racional de mutantes, MMPBSA, archaea, metabolismo no convencional
fuente: Borrador - Paper2.pdf (extraído con pdftotext)
---

# Structural Basis for AMP-Dependent Allosteric Activation of a Bifunctional ADP-Dependent PFK/GK from *Methanothermococcus thermolithotrophicus*

(proponer más títulos)

Identification of a novel allosteric site for AMP in the bifunctional ADP-dependent
phosphofructokinase/glucokinase from Methanothermococcus thermolithotrophicus
and the structural basis of its activation.

Discovery of a Novel Allosteric AMP-Binding Site and Activation Mechanism in the                   Formatted: English (United States), Highlight
Bifunctional     ADP-Dependent       PFK/GK       from     Methanothermococcus
thermolithotrophicus.

Structural Basis for AMP-Dependent Allosteric Activation of a Bifunctional ADP-
Dependent PFK/GK from Methanothermococcus thermolithotrophicus.


running title of 50 characters or less;
novel allosteric site in an archaeal sugar kinase
AMP allosteric site in an archaeal sugar kinase

abstract of no more than 250 words, followed by (b) four to ten keywords or short phrases for
indexing that reflect the content and major thrust of the paper, and (c) a 50-75-word
statement, written for a broader audience, outlining the importance and/or impact of the work
presented in the manuscript

Abstract
Although allostery is widely recognized as a central mechanism for regulating cellular pro-        Formatted: Font: (Default) Arial, 11 pt, English (United
cesses, its role in archaeal enzymes remains poorly explored. A notable exception is the bi-       States)
functional ADP-dependent glucokinase/phosphofructokinase (GK/PFK) found in methano-
genic archaea of the Methanobacteriota phylum. In these enzymes, AMP is a reaction prod-           Formatted: Font: (Default) Arial, 11 pt, Italic, English
uct and would therefore be expected to inhibit catalysis; however, it instead activates both       (United States)
GK and PFK activities, implying the existence of a distinct allosteric regulatory site unique to   Formatted: Font: (Default) Arial, 11 pt, English (United
bifunctional ADP-dependent kinases.                                                                States)
Here, we report two atomic-resolution X-ray crystal structures of the bifunctional ADP-            Formatted: Font: (Default) Arial, 11 pt, English (United
GK/PFK from Methanothermococcus thermolithotrophicus. Both structures contain ADP and              States)
either glucose or fructose-6-phosphate bound at the active site and, for the first time within     Formatted: Font: (Default) Arial, 11 pt, English (United
this enzyme family, reveal AMP bound at a previously unidentified site. To functionally char-      States)
acterize this site, we combined activation-specificity assays, molecular dynamics simula-
tions, and site-directed mutagenesis. These analyses demonstrate that the allosteric site ex-
hibits complex specificity for AMP, with contributions from both the phosphate and adenine
moieties. While earlier studies showed that bifunctional ADP-dependent kinases transition
between open and closed conformations upon substrate binding, our simulations of the ter-          Formatted: Font: (Default) Arial, 11 pt, English (United
nary sugar–MgADP–AMP complex reveal the formation of a super-closed conformation. In               States)
this state, AMP stabilizes the enzyme and promotes the productive alignment of substrates
and catalytic residues, providing a mechanistic basis for AMP-dependent activation. Poner
resultados de dinámica y de mutantes. Completer estructura
Although allostery has been widely recognized as crucial for regulating cellular processes, its
presence in archaeal enzymes has been rarely addressed. One of the few cases is the
bifunctional Glucokinase/Phosphofructokinase (GK/PFK) ADP-dependent sugar kinases
present in methanogenic archaea of the Methanobacteriota phylum. In these enzymes, AMP
is a reaction product, so it would be expected to inhibit enzyme activity. Nonetheless, AMP
also activates both GK and PFK activities, suggesting the presence of an allosteric
regulatory site unique to bifunctional ADP-dependent kinases.
In this work, we report two novel atomic-resolution cuanto? structures of the bifunctional        Formatted: Font color: Background 1, English (United
ADP-PFK/GK enzyme from Methanothermococcus thermolithotrophicus, determined by X-                 States), Highlight
ray crystallography. Both structures have ADP and either glucose or F6P at the active site,       Commented [IA1]: GK: adenosine-5’-phosphosulfate
and, for the first time in available structures of this family of enzymes, AMP was found in a     PFK: ADPBS
Both structures have ADP analogues
novel binding site. To characterize this site, we performed activation-specificity assays,
molecular dynamics simulations, and site-directed mutagenesis. Our results show that the
allosteric site exhibits complex specificity for AMP, determined by both its phosphate group
and the adenine moiety. Previous studies reported that bifunctional enzymes adopt two
conformations (open and closed), with substrate binding required to achieve the closed
conformation. Molecular dynamics simulations of the novel allosteric complex (sugar–
MgADP–AMP) revealed that the allosteric site is only formed in a super-closed conformation,
where AMP stabilizes this state and promotes the productive alignment of substrates and
active-site residues.

Methanogenic archaea, belonging to the Euryarchaeota phylum, present bifunctional
ADP-dependent sugar kinases in their modified glycolytic pathway. These enzymes catalyze          Commented [VG2]: Parece introducción
the phosphorylation of glucose and fructose-6-phosphate using ADP instead of ATP, as
classically described for glycolysis. Structurally, these monomeric enzymes belong to the
ribokinase superfamily and have a strongly conserved major domain with a Rossman fold,
connected to a smaller lid-like domain by a hinge. Both transfer reactions take place in the
same active site, located between the major and minor domains. In previous works, AMP
activation has been reported for these enzymes, and their conservation and activation
mechanism were studied within the evolution of bifunctional ADP-dependent sugar kinases.
Previously, it was suggested that AMP activation in bifunctional enzymes must occur through
an allosteric site, as it is one of the reaction products, while AMP causes inhibition in the
specific ADP-dependent sugar kinases from Thermococcales.

four to ten keywords: allosteric regulation, bifunctional archaeal sugar kinase, methanogenic
archaea, X-ray structure determination, identification of novel allosteric site.

50-75-word statement, written for a broader audience, outlining the importance and/or
impact of the work presented in the manuscript
Introduction

Allostery is a fundamental mechanism by which proteins transmit information and exert
regulatory control, enabling precise modulation of biological activity. Often referred to as the
“second secret of life” (Monod 1972), it plays a central role in key biological processes such         Commented [VG3]: Monod J. 1972. Chance and
necessity: an essay on the natural philosophy of modern
as metabolic regulation, transcription, and signal transduction. This mechanism entails the            biology. New York, 641 NY: Vintage Books
binding of a small molecule to a site distinct from the active site, triggering conformational
changes that modulate protein function. While allostery has been extensively characterized
in bacterial and eukaryotic enzymes, it remains significantly understudied in archaea. Even
more, it was initially assumed not to be present in enzymes from these organisms, but
instead, it was claimed that regulation would occur mainly at the transcriptional level (Bräsen
et al. 2014). However, some allosteric effectors are reported for archaeal enzymes, such as            Commented [VG4]: Bräsen C, Esser D, Rauch B, Siebers
B. 2014. Carbohydrate Metabolism in Archaea: Current
activation by 3-phosphoglycerate (3PG) or AMP in the pyruvate kinases of Thermoproteales               Insights into 566 Unusual Enzymes and Pathways and Their
Regulation. Microbiol Mol Biol Rev [Internet] 78:89–567
and Methanococcales (Johnsen 2019) and inhibition by CTP in Aspartate transcarbamylase                 175. Available from:
of P. abyssi (doi:10.1111/j.1742-4658.2005.04678.x). Also, we reported that AMP activates              https://journals.asm.org/doi/10.1128/MMBR.00041-13
Commented [VG5]: Johnsen U, Reinhardt A, Landan G,
the bifunctional ADP-dependent PFK/GK enzyme from the methanogenic organism                            Tria FDK, Turner JM, Davies C, Schönheit P. 2019. New
Methanococcus maripaludis (MmPFK/GK). Moreover, a comprehensive kinetic and                            views on an old 622 enzyme: allosteric regulation and
evolution of archaeal pyruvate kinases. The FEBS Journal
evolutionary analysis of this metabolic trait revealed that it is linked to bifunctionality and that   623 [Internet] 286:2471–2489. Available from: 624
https://febs.onlinelibrary.wiley.com/doi/10.1111/febs.14837
its kinetic mechanism varies widely across evolution. Since allostery initiates and propagates
Commented [VG6]: Aspartate transcarbamylase from the
by breaking existing interactions in one state and gaining new interactions in the other, a            hyperthermophilicarchaeon Pyrococcus abyssiInsights into
cooperative and allosteric mechanismsSigrid Van Boxstael 1,
comprehensive understanding of allostery requires uncovering the precise location of                   Dominique Maes2,3 and Raymond Cunin.
FEBS Journal 272 (2005) 2670–2683
allosteric sites and the structural and functional consequences they exert on the orthosteric
Commented [VG7]: Vallejos‐Baccelliere G, Kaufman SB,
(active) site. In the case of archaeal bifunctional ADP-dependent PFK/GK enzymes,                      González‐Lebrero RM, Castro‐Fernandez V, Guixé V. 2022.
671 Characterisation of kinetics, substrate inhibition and
determining the allosteric site at the structural level remains elusive despite several attempts       product activation by AMP of bifunctional 672 ADP
‐dependent glucokinase/phosphofructokinase from
to identify it using bioinformatics approaches.                                                        Methanococcus maripaludis. The FEBS 673 Journal
[Internet] 289:7519–7536. Available from: 674
The bifunctional ADP-dependent sugar kinases catalyze the phosphorylation of glucose and               https://febs.onlinelibrary.wiley.com/doi/10.1111/febs.16557
fructose-6-phosphate using ADP rather than ATP at the same active site. These enzymes                  Commented [IA8]: Omitiría esto
belong to the Ribokinase superfamily and have a strongly conserved major domain with a
Rossman fold, connected to a smaller lid-like domain by a hinge, with the active site located
Commented [VG9]: Specificity evolution of the ADP-
between them (Merino Guixé). Comparison of the structure of an ancestral bifunctional ADP-             dependent sugar kinase family – in silico studies of the
glucokinase⁄phosphofructokinase bifunctional enzyme from
dependent enzyme across different ligation states reveals that the enzyme predominantly                Methanocaldococcus jannaschii
populates two conformations (open and closed) and that binding of both substrates is                   Felipe Merino and Victoria Guixe
FEBS Journal 275 (2008) 4033–4044
required to achieve the closed conformation (Muñoz et al.). This scenario differs from the             Commented [VG10]: Rivas-Pardo, J. A., Herrera-
conformational landscape observed for GK-specific enzymes, in which each substrate                     Morande, A., Castro-Fernandez, V., Fernandez,
F. J., Vega, M. C., and Guixé, V. (2013) Crystal structure,
independently triggers sequential domain closure, yielding three conformational states                 SAXS and
kinetic mechanism of hyperthermophilic ADP-dependent
(open, semi-closed, and closed) that correlate with the enzyme's kinetic mechanism. (Rivas-            glucokinase
from Thermococcus litoralis reveal a conserved mechanism
Pardo et al). Since only bifunctional ADP-dependent sugar kinases are activated by AMP,                for catalysis.
PLoS One 8, e66687
whereas specific GK or PFK enzymes are not, the impact of AMP on the structural changes
provoked by substrates is essential to understand the structural basis of the allosteric
regulation.
To identify this allosteric site, we employed the bifunctional ADP-PFK/GK enzyme from the
methanogenic organism Methanothermococcus thermolithotrophicus. We determined the
high-resolution structure of this enzyme by X-ray crystallography, with AMP bound at the
allosteric site and ADP together with either glucose or F6P bound at the active site. Assays
assessing allosteric site specificity revealed a complex pattern governed by both the
phosphate moiety and the adenine base. Molecular dynamics simulations of the allosteric
complex (Sugar–MgADP–AMP) indicated that the allosteric site is formed exclusively in a
super-closed conformation, which is stabilized by the allosteric effector AMP. This
stabilization promotes a catalytically competent alignment of the substrates and active-site
side chains. Understanding allosteric control in archaeal proteins, particularly in
methanogenic organisms, will reveal novel regulatory strategies and open new venues for
biotechnological applications.
Methodology

Gene synthesis, protein expression, and purification.
The gene encoding MttPFK/GK (GenBank XMX98500.1) was codon-optimized for
expression in E. coli, synthesized by Genscript (Piscataway, NJ), and cloned into the
modified pET28 vector (pET-TEV-mttpfkgk) containing an N-terminal His-tag. E. coli
BL21(DE3) cells transformed with this plasmid were grown in LB medium containing 35
µg/mL kanamycin at 37 °C until OD₆ ₀ ₀ reached 0.6 - 0.8. Protein expression was induced
overnight with 1 mM IPTG. Cells were harvested by centrifugation (6,000 rpm, 20 min, 4 °C),
resuspended in Buffer A (50 mM Tris-HCl pH 7.8, 500 mM NaCl, 20 mM imidazole, 5 mM
MgCl₂ ), and lysed on ice by sonication (Digital Sonifier 450; total 4 min, 20 s pulses with 1
min intervals). The lysate was clarified by centrifugation (18,000 rpm, 20 min, 4 °C), and the
supernatant was loaded onto a 5 mL HisTrap column (GE Healthcare) equilibrated with
Buffer A. After washing with 10 column volumes of Buffer A, protein was eluted using a
linear gradient to Buffer B (50 mM Tris-HCl pH 7.8, 500 mM NaCl, 500 mM imidazole, 5 mM
MgCl₂ ) in an Äkta Prime Plus chromatography system (GE Healthcare). Protein elution was
monitored at 280 nm, and fractions containing the protein were pooled and stored in elution
buffer (NaCl 500 mM, Tris-HCl 50 mM, and imidazole 500 mM).

Crystallization, data collection, and structure determination
Initial crystallization screening was performed using an ARI Gryphon robot (Art
Robbins Instruments LLC) by the sitting-drop vapor-diffusion method. For optimization,
hanging-drop trials were set up by mixing 2 μL of protein solution (20 mg/mL supplemented
with 100 mM glucose, 5 mM AMP, and 5 mM MgCl₂ ) and 2 μL of reservoir solution (2.4 M
ammonium sulfate, 0.1 M DL-malic acid pH 5.5) at 25 °C. Prior to flash-freezing, crystals
were briefly transferred to a cryoprotectant solution containing 25% glycerol and 5%
Santovac, then flash-cooled in liquid nitrogen at room temperature.
Condiciones F6P: 1 mM F6P, 5 mM AMP, 5 mM ADPβs, 10 mM MgCl 2.
Cristalizacion: 0,1 mM DL-malic acid pH 5, 2,4 mM ammonium sulfate. Cryo glicerol 25% +
Santovac 5
Diffraction data were collected remotely on the MANACA beamline at the SIRIUS
fourth-generation synchrotron (LNLS, Campinas, Brazil) using a PILATUS 2M detector at a
wavelength of 0.977 Å. A total of 3,600 images were recorded with an oscillation range of
0.1° per frame at 100 K. The diffraction data were processed using autoPROC version 1.0.5
(Vonrhein et al., 2011).
Indexing and integration were performed with XDS version 20250119, build
20250714 (Kabsch, 2010), the space-group hypothesis was obtained by POINTLESS
version 1.13.6 (Evans, 2006). Based on the most probable unit-cell parameters from
POINTLESS, the dataset was iteratively reindexed and reintegrated with XDS. Scaling and
merging were performed with AIMLESS version 0.8.2 (Evans, 2013) using the autoPROC
scaling module. Phases were determined by molecular replacement using Phaser version
2.8.3 (McCoy et al., 2007) within the CCP4i2 suite (Potterton, 2018), employing the
monomer predicted by AlphaFold2 (Jumper et al., 2021) as the search model for
MttPFK/GK. Automated refinement was performed with Refmac5 (Kovalevskiy, 2018) and
interactive model building and ligand placement were performed in Coot (Emsley, 2010).
Statistics for data collection and refinement are summarized in Table SX.
Determination of enzyme activity and kinetic parameters
GK and PFK activities were measured using coupled reactions to monitor NADH
production or consumption at 340 nm, as described previously (Vallejos‐ Baccelliere, 2020).
For the PFK assay, rabbit aldolase, triose phosphate isomerase, and α‐ glycerophosphate
dehydrogenase (all from Sigma-Aldrich) were included as auxiliary enzymes. For the GK
assay, glucose-6-phosphate dehydrogenase from Leuconostoc mesenteroides was used.
Each assay was conducted with 1 mM free Mg²⁺ and 50 mM buffer (PIPES-NaOH, pH 6.5
for PFK; HEPES-NaOH, pH 7.8 for GK). Substrate concentrations were either varied or set
at their respective Kₘ values for glucose, fructose-6-phosphate, or ADP-Mg, depending on
the assay. Effector molecules (AMP, deoxy-AMP, IMP, GMP, CMP, TMP, and adenosine)
were tested at several concentrations.                                                            Commented [11]: evaluar si es necsario agregar detalle de
ajustes en cinetica
Molecular dynamics simulations
MttPFK/GK structures (PDB IDs) were used as initial coordinates to prepare two
molecular dynamics systems. First, the protonation states of the GK (pH 7.8) and PFK (pH
6.5) systems were determined using the Propka software available on the PDB2PQR web
server. Topology and coordinate files were created with the tLEaP, the ff19SB force field
was used to obtain protein parameters. For the ADP and Mg +2 parameters, they were
obtained from the Amber parameter database of Richard Bryce´s group, whereas for
glucose, fructose-6-phosphate, and AMP, the parameters were derived with Antechamber
using the GAFF force field. The final models were immersed in a truncated octahedral TIP3P
water box extending 12 Å from the protein surface, and counterions (Na+/Cl-) were added to
ensure electroneutrality.
The energy minimization protocol was adapted from Cea et al. (2024) and consisted
of five consecutive steps, with a harmonic positional restraint gradient applied to the heavy
atoms of the protein and ligands to separate the solvent from the system. The first 2,000
steps were performed using the steepest descent algorithm, and the remaining steps were
performed using the conjugate gradient method. The positional restraint of the first stage
was 10 kcal/mol; for the next stage, it was 5 kcal/mol, and then, it was reduced to 1 and 0.1
kcal/mol (5,000 total steps for each) up to the final 20,000 step minimization without a
restraint. The minimization protocol was run on a 64-core Linux server.
Molecular dynamics equilibration and production were performed in AMBER24, with
the ff19SB force field. The final minimized models were equilibrated in NVT conditions in 3
stages, the first two were 200 ps, with 2.0 and 0.5 kcal/mol restrictions on the heavy atoms
of the protein and ligands, respectively, with 160 ps for a 0-298.15 K temperature ramp, and
the final 40 ps to equilibrate the system at 298.15 K. The final equilibration was 400 ps, with
a 0.2 kcal restriction on the ligands to maintain the crystallographic arrangement.


Site-directed mutagenesis
Primers to introduce Y56A, R58A, R58E, H72A, and S275A substitutions in pET-
TEV-mttpfkgk were designed in SnapGene (Table X) and synthesized by Macrogen
(empresa). Mutagenesis was performed using the QuikChange II-E kit (Agilent
Technologies) with 30 PCR cycles (95 °C × 20 s; annealing at Tₘ –5 °C × 20 s; 72 °C × 6
min), followed by DpnI digestion (1 h at 37 °C) to eliminate parental template. For R58A and
S275A, two additional rounds of PCR were carried out first with extended extension times (7
min) and then using Phusion High-Fidelity polymerase (98 °C × 10 s; 58 °C × 20 s; 72 °C × 6
min; 30 cycles). DpnI-treated products were transformed into DH5α, plated on LB-kanamycin
(35 µg/mL), and single colonies were grown overnight in LB + kanamycin. Plasmids were
purified (AccuPrep Mini, Bioneer) and sequenced with T7 primers to confirm each point
mutation.
Results




Figura 1: estructuras cristalográficas de MttPFK. En A, la estructura resuelta en complejo
con glucosa y adenosina en el sitio activo con una molécula de AMP en el sitio alostérico.
En B, un acercamiento al sitio alostérico y al sitio activo. En C, la estructura resuelta en
complejo con F6P y ADPbs en el sitio activo con una molécula de AMP en el sitio alostérico.
En D, un acercamiento al sitio alostérico y al sitio activo. En F, la superposición de ambas
estructuras en el sitio alosterico, mostrando las cadenas laterales que están alrededor del
ligando.


Apuntes Fig 1.

Introduccion a cristalografia y modelo generado. riboquinasa bifuncional con glc y f6p en el
sitio activo (Figura S1 mostrando el E72 de mtt), el cual ha sido caracterizado previamente
(paper profe victor ancMT).
Hablar del fenomeno de activacion por AMP descrito (paper maripaludis y AMP), y hablar de
la molécula de AMP encontrada, que es consistente con lo descrito anteriormente
(describirlo).
Punto de posicion super cerrada.
Table 1. Data collection, processing and refinement statistics for MttPFK/GK structures.
Statistics for the highest-resolution shell are shown in parentheses.
BGC-AMP-ADX                          F6P-AMP-AT4
PDB ID                           TBD                                  TBD
Wavelength                                          0.9772 Å
Space group                           C2                                  C2
Unit cell            (a,b,c) = (87.51, 88.01, 77.30) Å    (a,b,c) = (87.41, 87.99, 77.23) Å
(α,β,γ) = (90, 99.25, 90)°           (α,β,γ) = (90, 98.97, 90)°
Data collection statistics
Resolution range      38.15 - 1.17 Å (1.18 – 1.17 Å)       38.11 – 1.54 Å (1.55 – 1.54 Å)
Total reflections            1273776 5(26427)                      438403 (14661)
Unique reflections             191406 (5606)                        83787 (2752)
Multiplicity                       6.7 (4.7)                           5.2 (5.3)
Completeness                 97.77% (82.73%)                     96.78 % (89.79 %)
Mean I/σ(I)                     10.92 (0.69)                          8.31 (0.96)
Rpim                          0.02087 (0.809)                     0.04494 (0.8456)
CC1/2                           0.999 (0.308)                       0.996 (0.348)
CC*                               1 (0.686)                         0.999 (0.718)
Wilson B-Factor                   15.49 Å2                             16.47 Å2
Global refinement statistics
Rwork/Rfree                    0.1293/0.1512                        0.1492/0.1825
R.m.s deviations
Bond lengths                   0.011 Å                              0.018 Å
Bond angles                     1.62°                                1.87°
Ramachandran
Favored                        99.13%                               99.12%
Allowed                        0.87%                                 0.88%
Outliers                         0%                                    0%
B-Factors
Average                        21.70 Å2                            26.07 Å2
Protein                        19.89 Å2                            24.88 Å2
Ligands                        25.42 Å2                            29.67 Å2
Rotamer outliers                  0.23%                               0.71%
Clashscore                         2.13                                2.36
Figure 2. MttPFK/GK allosteric site specificity. A) Relative GK activity at 0.5 (light blue)
and 5.0 (gray) mM of added AMP/AMP-like molecules or nucleotides monophosphate
(baselines 100% at 0 mM added AMP). B) Relative GK activity from 0 to 10 mM of each
effector tested, grouped into AMP-like molecules, purines, and pyrimidines. AMP was
included in all groups as a reference. C) Relative PFK activity at 0.5 (light blue) and 5.0
(gray) mM of added AMP/AMP-like molecules and a nucleotide monophosphate (baselines
100% at 0 mM added AMP). D) Relative PFK activity from 0 to 10 mM of each effector
tested, grouped into AMP-like molecules, purines, and pyrimidines. AMP was included in all
groups as a reference.

In parallel with the crystallography assays and the model refinement, we tested whether both
reactions of MttPFK/GK were activated by a battery of AMP-related effectors. We measured
both activities in the absence of added AMP or other effectors to establish a relative baseline
and then measured activity at concentrations of effectors ranging from 0.1 to 10.0 mM.

First, we evaluated a panel of AMP analogs, including cyclic AMP (cAMP), 2′-deoxy-AMP,
and adenosine, to determine which structural features of AMP are critical for activation of
both GK and PFK activities. As shown in Figure 2, AMP and 2′-deoxy-AMP produced the
strongest activation, with maximal effects observed between 0.5 and 1.0 mM. At higher
concentrations, activation declined, consistent with the expected product inhibition by AMP.
In contrast, neither cAMP nor adenosine elicited detectable activation, indicating that the
phosphate group is the key structural determinant of allosteric activation. Consistent with this
conclusion, both crystallographic structures of MttPFK/GK show that residues surrounding
the AMP-binding site are predominantly positively charged and interact directly with the
phosphate moiety (R58, K279, R282, and H308).




Following these experiments, we examined purine and pyrimidine monophosphates to
assess whether variations in the nitrogenous base influence allosteric activation. None of the
tested effectors produced significant activation of either GK or PFK activities at low
concentrations; however, modest activation was observed at 5.0 mM and above. Although
such concentrations are unlikely to be physiologically relevant, these results indicate that
enzyme activation can be induced by saturating levels of different monophosphate
nucleotides. This behavior suggests that the allosteric site can accommodate nonspecific
binding of alternative nucleotides under forced conditions, leading to activation.

Notably, this nonspecific activation at high nucleotide concentrations was observed
predominantly with the GK reaction, suggesting that the two catalytic activities may differ in
their communication pathways between the allosteric and active sites. Moreover, the
presence of fructose-6-phosphate may modulate the conformational dynamics of the active
site, thereby influencing the coupling between the active and allosteric sites.
[analysis of crystallographic structures, active site, conformations]
GK avg RMSD = 2.73 ± 0.30 Å
PFK avg RMSD = 2.56 ± 0.26 Å


To gain further insight into the allosteric mechanism and interactions between MttPFK/GK
and AMP, we performed all-atom molecular dynamics simulations (MD) of both GK and PFK
allosteric complexes. Five replicates per system, totaling 2 µs of simulation time, allowed us
to examine the conformational dynamics of the overall structure, as well as the different
amino acids involved in interactions with AMP at the allosteric site.

Firstly, to measure the deviation during the simulation from the starting closed conformation
observed in the crystallographic structure, the backbone RMSD was calculated. Overall, the
GK complex presented a slightly higher average RMSD value (2.73 ± 0.30 Å), whereas the
PFK complex was lower and presented fewer deviations, 2.56 ± 0.26 Å, across all five
replicates. These values suggest that in both complexes, there are no major changes
relative to the starting conformation. If we look at individual replicates, in the GK complex,
there are two replicates with an overall higher RMSD value (replicate 1 and 5), these two
replicates increase the overall RMSD for the GK set of simulations, but still present an
average RMSD below 3.5 Å. Regarding the PFK replicates, RMSD across replicates is more
homogeneous, and only replicates two and three present single spikes above 3.5 Å.




To identify molecular interactions between AMP and the allosteric site and estimate their
magnitudes, we performed MMPBSA analysis of all replicates. This endpoint-free energy
calculation method is widely used to estimate binding free energy and enables rapid,
accurate estimates from molecular dynamics simulations, if interactions remain stable
throughout the trajectory. Additionally, this method can calculate the individual energy
contributions of single amino acids to ligand binding, a useful approach for in-silico
exploration before performing site-directed mutagenesis.

The MMPBSA analysis revealed that, as expected, AMP exhibits an attractive interaction
(negative binding free energy) with the allosteric site in MttPFK/GK. In the GK complex, an
average of -10.70 ± 5.35 kcal/mol was determined, and, interestingly, we observe a
correlation between the lower interaction energy replicates and those that showed higher
RMSD fluctuations. On the other hand, in the PFK complex, the average interaction energy
was -8.08 ± 1.86 kcal/mol, with a lower standard deviation, in agreement with the observed
RMSD values for this set of simulations.

Resultados de MMPBSA de los aminoácidos individuales

Resultados de simulación de las mutantes
Figure 4. Structural and energetic impact of allosteric site mutations on MttPFK/GK
dynamics. The top panels (A–C) correspond to the Glucokinase (GK) complex, and the
bottom panels (D–F) correspond to the Phosphofructokinase (PFK) complex. (A, D)
Backbone RMSD evolution. Stability of Y56A (green) and R58A (red) mutants over 400 ns.
Solid lines represent the mean RMSD calculated from five independent replicates, while
shaded regions indicate the standard deviation (±SD). (B, E) Ligand interaction energy
comparison. Binding free energies (MMPBSA) calculated for the allosteric effector (AMP),
the sugar substrate (Glucose/F6P), and the nucleotide substrate (ADP). Data represent the
mean ± SD of five replicates. Statistical significance was determined using an unpaired t-test
(P < 0.05, **P < 0.01, **P < 0.001; ns, not significant). (C, F) Inter-domain angle distribution.
Kernel density estimates (KDE) showing the conformational sampling of the domain closure
angle. Distributions aggregate data from all frames across five replicates for the WT (blue),
Y56A (green), and R58A (red) systems, illustrating the population shift relative to the WT
catalytically competent closed state.                                                               Commented [EC12]: Modificar




In silico validation of the allosteric site: Mutations induce conformational rigidity and
substrate trapping.
To determine the functional role of the key residues identified in the crystallographic
structure, we performed MD simulations of the Y56A and R58A mutants in both GK and PFK
complexes.



Structural stability and backbone dynamics

The backbone RMSD evolution revealed distinct dynamic behaviors for the two catalytic
centers (Fig. 4A and 4D). In the PFK complex (Fig. 4D), both Y56A and R58A mutants
exhibited remarkably low RMSD values (< 1.5 Å) and high stability throughout the 400 ns
trajectory. This indicates that, rather than unfolding or destabilizing, the mutations render the
PFK scaffold exceptionally rigid. In contrast, the GK complex (Fig. 4A) displayed higher
overall mobility. Notably, the Y56A mutant in GK showed a significant increase in structural
fluctuations (large standard deviation) during the latter half of the simulation, suggesting a
loss of conformational restraint in this domain compared to the R58A mutant.

Energetic impact: Loss of regulation and substrate over-stabilization

The MMPBSA analysis confirmed the critical role of these residues in effector binding while
revealing an unexpected impact on the active site. In both complexes (Fig. 4B and 4E), the
R58A mutation completely abolished the affinity for AMP, resulting in repulsive (positive)
interaction energies. However, the uncoupling of the allosteric site led to a significant
strengthening of interactions at the active site. In the PFK complex, the mutants exhibited
substantially stronger interaction energies (more negative values) for both the substrate
(F6P) and ADP compared to the WT (Fig. 4E). For instance, the interaction energy for ADP
dropped to nearly -40 kcal/mol in the mutants, compared to roughly -15 kcal/mol in the WT.
A similar "trapping" effect was observed in the GK complex, particularly for the Y56A mutant,
which showed a marked increase in interaction strength with ADP (Fig. 4B).

Conformational locking

To understand the structural basis of this rigidity and energetic trapping, we analyzed the
inter-domain angle distributions (Fig. 4C and 4F). While the WT enzyme (blue) samples a
defined population corresponding to the catalytically competent state, the mutants displayed
a clear population shift toward smaller inter-domain angles (left-shifted distributions). This
effect was particularly pronounced in the PFK complex (Fig. 4F), where the Y56A and R58A
mutants adopted a hyper-closed conformation. Collectively, these results suggest that the
mutations do not merely prevent activation but cause the enzyme to collapse into a rigid,
non-productive state where substrates are bound too tightly, likely inhibiting the necessary
dynamics for catalytic turnover.


Discussion
