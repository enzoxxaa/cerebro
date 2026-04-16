---
tipo: manuscrito
estado: en-desarrollo
rol-enzo: simulaciones MD + análisis de penetración en cristal líquido
coautores: [Fernanda Llana, Federico Bravo, Enzo Cevo, María Cecilia, Igor O. Osorio-Román, Boris Weiss-López, Benedetta M. Squeo, Camilo Segura]
herramienta: GROMACS, MD all-atom
sistema: TTAB/DeOH/NaBr — cristal líquido liotrópico
luminogenos: [TTG, TTC, TTY, TTO]
tema: Control del substituyente sobre la penetración de luminógenos AIE (aggregation-induced emission) en medios de cristal líquido. Fotofísica en solución + localización/penetración por MD.
colaboracion-internacional: CNR-SCITEC Milán (Italia), UACh, UChile
fuente: Paper_AIE_LCs_Cevo_v4.docx-1.pdf (extraído con pdftotext)
---

# Substituent-Controlled Penetration of AIE Luminogens into Liquid Crystal Media

Weiss-López1, Benedetta M. Squeo2*, and Camilo Segura1*


1
Departamento de Química, Facultad de Ciencias, Universidad de Chile, Las Palmeras 3425, Ñuñoa,

Región Metropolitana, Chile.

2
Istituto di Scienze e Tecnologie Chimiche (SCITEC), Consiglio Nazionale delle Ricerche (CNR), Via A.

Corti, 20133, Milan, Italy.

3
Instituto de Ciencias Químicas, Facultad de Ciencias, Universidad Austral de Chile. Rector Eduardo

Morales 33, Valdivia, 509000, Chile



Keywords: Aggregation-induced emission; Liquid crystals, Molecular dynamics, Substituent effects,



Abstract



1. Introduction

Aggregation‐induced emission (AIE) has emerged as one of the most influential design paradigms for

modern luminogens because it reverses a long‐standing limitation of conventional fluorophores:

aggregation‐caused quenching (ACQ). In typical π-conjugated dyes, intermolecular π–π stacking and

exciton coupling often open non-radiative decay channels, suppressing emission in the condensed phase

where many real devices operate. In contrast, AIE‐active molecules are weakly emissive in dilute

solution but become strongly luminescent upon aggregation or confinement, enabling high brightness in

solids, films, and nanostructures. Since the first reports formalizing the AIE concept in the early 2000´s,

this phenomenon has rapidly expanded into a broad materials platform for optoelectronics, sensing,
bioimaging, and stimuli‐responsive systems, largely because aggregation is no longer treated as a

drawback but as the operating state of the emitter.

Mechanistically, AIE is most commonly rationalized through the restriction of intramolecular motion

(RIM) model, which unifies restriction of intramolecular rotations and vibrations as the key factor

suppressing non-radiative deactivation. In solution, multiple phenyl rotors, flexible heteroaromatic

linkers, and donor–acceptor torsions dissipate the excited-state energy through internal conversion. When

the same chromophores are immobilized by aggregation, crystallization, viscous media, or host–guest

confinement, these motions are hindered and radiative decay is enhanced. This structure–property

relationship is especially attractive because it connects straightforward molecular modifications (steric

bulk, electronic substituents, conjugation length, polarity) with practical emission performance under

realistic conditions.

Liquid crystals (LC´s) provide a particularly powerful environment to interrogate and exploit AIE. LC

phases combine molecular mobility with long-range orientational order, yielding anisotropic optical and

mechanical responses that can be tuned by temperature, composition, and external fields. Beyond their

role in display technology, LCs are increasingly used as adaptive soft materials, where controlled

organization at the nanometer–micrometer scale can regulate diffusion, polarity, and local viscosity. In

this context, coupling AIE luminogens with LC media offers a dual advantage: (i) AIE emission can be

amplified by confinement within ordered domains, while (ii) the LC host can act as a “molecular

amplifier” of subtle interactions by translating them into macroscopic optical signatures such as

polarization dependence, spectral shifts, or phase‐dependent emission changes.

From a functional perspective, AIE–LC hybrids have been explored for smart luminescent materials,

optical reporting of phase transitions, mechanochromic and thermoresponsive platforms, and anisotropic

emitters where the emission intensity or polarization can be modulated by LC ordering. Importantly, LCs

can also help disentangle whether enhanced emission arises primarily from aggregation packing, local

viscosity, microenvironment polarity, or specific host–guest interactions. This is particularly relevant for
push–pull AIEgens, where intramolecular charge transfer (ICT) states are sensitive to local dielectric

response and to competing non-radiative pathways such as twisted intramolecular charge transfer. Thus,

embedding AIE luminogens in LC phases is not only an applied strategy for device-oriented materials,

but also a mechanistic tool to resolve how molecular structure determines localization, orientation, and

emissive efficiency inside complex soft matter.

Lyotropic LC systems, formed by amphiphiles in water with cosurfactants (e.g., long-chain alcohols), are

especially appealing as model membranes because they self-assemble into lamellar arrangements that

mimic key aspects of biological and synthetic bilayers while remaining experimentally accessible and

composition-tunable. Small changes in solute polarity, hydrogen-bonding ability, and steric profile may

determine whether a molecule partitions into the aqueous region, the interfacial headgroup environment,

or the hydrophobic interior, directly impacting both photophysics and dynamics.

In this work, we investigate a family of structurally related AIE‐active donor–acceptor luminogens

bearing thiophene-aldehyde acceptor motifs and systematically varied substituents and conjugation

lengths, and we correlate their solution photophysics (absorption/emission spectra, molar extinction

coefficients, quantum yields, Stokes shifts, and excited‐state lifetimes) with their emission behavior

inside lyotropic liquid crystalline environments. By combining spectroscopic characterization with

structural descriptors of localization and membrane penetration, the central objective is to establish how

substituent selection governs solute partitioning and confinement within LC assemblies, ultimately

providing design rules for AIE luminogens tailored for anisotropic soft materials and LC‐enabled

photonic applications.


2. Experimental


2.1 Reagents


4-bromotriphenylamine (TCI, 99%), 9-(4-Bromophenyl)-9H-carbazole (Thermo Scientific Chemicals,

98%), 4-Bromo-4',4''-dimethoxytriphenylamine (TCI, >98%), 5-formylthiophene-2-boronic acid (TCI,
98.8%),       5'-Formyl-2,2'-bithiophene-5-boronic        acid       (TCI,          85        to       108%)

tetrakis(triphenylphosphine)palladium(0) (TCI, 99.9%), chloroform (CHCl3, Sigma Aldrich), ethyl acetate

(AcOEt, Sigma Aldrich), hexane (Sigma Aldrich), toluene (Sigma Aldrich), dichloromethane (DCM,

Sigma Aldrich), tetrahydrofuran (THF, Sigma Aldrich), acetonitrile (ACN, Sigma Aldrich), dimethyl

sulfoxide (DMSO, Sigma Aldrich), acetone (Sigma Aldrich), ethanol (EtOH, Sigma Aldrich), methanol

(MeOH, Sigma Aldrich), potassium carbonate (K₂CO₃, Merck), tetradecyltrimethylammonium bromide

(TTAB, ≥98%, Sigma Aldrich), sodium bromide (NaBr, >99%, Sigma Aldrich) and decanol (DeOH,

Sigma Aldrich) were commercially available and utilized as received. Deuterated chloroform (CDCl3,

Sigma Aldrich) served as the solvent for 1H-NMR analysis.


2.2 Synthesis of AIE luminogens


The compounds utilized in this research were synthesized following protocols previously reported in the

literature, based on a Suzuki–Miyaura cross-coupling reaction. Scheme 1 summarizes the synthesis of the

compounds and provides the corresponding abbreviations used to refer to each molecule throughout the

manuscript.   As   a   representative   example,     to     synthesize   TTG,   a        mixture   comprising

4-bromotriphenylamine (389 mg, 1.2 mmol), 5-formylthiophene-2-boronic acid (156 mg, 1.0 mmol),

Pd(PPh3)4 (58 mg, 0.05 mmol), THF (20 mL), and a 2 M aqueous solution of K2CO3 (1.6 mL) was placed

under a nitrogen atmosphere and refluxed for 12 hours. Upon completion of the reaction, 20 mL of water

was added, and the mixture was extracted thrice using 20 mL aliquots of DCM. The organic phases were

combined, dried over anhydrous Na₂SO₄, and concentrated under reduced pressure at room temperature.

The crude product underwent purification using column chromatography on silica gel, with chloroform as

the eluent. The identical synthesis method was employed for TTC, TTY and TTO, using the

corresponding compounds as starting reagent. All molecules were fully characterized using 1H and 13C

NMR spectroscopy, as well as mass spectrometry (MS), as illustrated in Supporting Information Figures

S1 to S6.
Scheme 1: Synthetic procedure for the preparation of AIEgens


2.3 Preparation of the Lyotropic Liquid-Crystalline Samples


To form the liquid-crystalline phase, TTAB (1027 mg, 3.055 mmol), NaBr (532 mg, 5.170 mmol), DeOH

(230 µL, 1.205 mmol), and H2O (2.5 mL, 139.0 mmol) were combined and centrifuged at 3000 rpm for 2

min until a transparent mixture was obtained. Subsequently, 200 µL of the prepared liquid crystal were

transferred to a vial and supplemented with 300 µg of the AIE luminogen. The suspension was mixed

until complete dissolution and then centrifuged at 7000 rpm for 2 min to remove any undissolved

crystalline residues. Finally, 100 µL of the resulting mixture were sandwiched between two glass slides

(15 mm × 10 mm) for optical measurements.


2.4 Fluorescence Polarization Measurements and G-Factor Calibration


To investigate the emission polarization of the luminogens, the fluorescence spectrophotometer was first

calibrated to determine the G-factor as a function of wavelength. The optical configuration corresponded

to a front-face excitation geometry, in accordance with standard requirements for polarization
measurements (Figure S1). For this purpose, three reference fluorophores exhibiting near-zero

polarization in solution, Quinine sulfate, Dansyl amide and Tris(2,2′-bipyridyl)dichlororuthenium(II)

hexahydrate, were employed. Under these conditions, the G-factor was calculated using Equation (1):


𝐼 (λ)
𝐺(λ) = 𝐼𝐻𝑉(λ) \\\\\(1\\\\\)
𝐻𝐻

where 𝐼𝐻𝑉 and 𝐼𝐻𝐻 correspond to the emission intensities detected with the emission polarizer set vertical

(V) or horizontal (H), respectively, while keeping the excitation polarization horizontal (H).


The wavelength-dependent G-factors were subsequently used to determine the polarization of the

luminogens in ethyl acetate and in the liquid-crystalline medium. Briefly, samples were excited

with horizontally     polarized     light,         and       the   emission   was   collected    in   both

the parallel and perpendicular channels. The steady-state polarization was calculated according to

Equation (2):


𝐼    (λ)−𝐺(λ)𝐼 (λ)
𝑃(λ) = 𝐼𝐻𝐻(λ)+𝐺(λ)𝐼𝐻𝑉(λ) \\\\\(2\\\\\)
𝐻𝐻             𝐻𝑉

2.5 Characterization

1
H and 13C NMR spectra were obtained using a Bruker Avance 400 MHz multidimensional NMR

spectrometer. Mass spectrometry (MS) was conducted with a SCIEX TQ™ 4500 mass spectrometer.

Polarized optical microscopy (POM) images were acquired using a XXXX microscope equipped with two

crossed polarizers at 10× magnification. UV-visible absorption spectra were acquired using a

Hewlett-Packard 8452A diode array spectrophotometer. Steady-state fluorescence measurements were

conducted using the ISS PC1. To record the emission spectra of the luminogens in ethyl acetate and in the

liquid-crystalline samples, measurements were performed using a front-face detection geometry. For

TTC, TTN, and TTG, excitation (for both polarized and unpolarized experiments) was provided by a

xenon (Xe) lamp at 370 nm, 380 nm, and 400 nm, respectively. For TTY and TTO, excitation (for both

polarized and unpolarized experiments) was provided by a 445 nm diode laser.
2.6 Molecular dynamics calculation


All-atom molecular dynamics (MD) simulations were performed using GROMACS 2025.4 (Abraham et

al., 2015) with the OPLS-AA force field and SPC/E explicit water model. The initial bilayer

configuration was adapted from the lyotropic lamellar system described by Montecinos et al. (2007),

consisting of 192 tetradecyltrimethylammonium (TTAB) surfactant molecules and 96 1-decanol (DeOH)

cosurfactant molecules arranged in a symmetric bilayer (96 TTAB + 48 DeOH per leaflet), yielding a

TTAB:DeOH molar ratio of 2:1, consistent with the experimental composition (Section 2.3). The initial

atomic coordinates of the bilayer were generated using PACKMOL (Martínez et al., 2009), which places

molecules in the simulation box according to geometric constraints while avoiding atomic overlaps. The

bilayer was placed in a simulation box of approximately 7.0 × 7.0 nm in the XY plane and solvated with

SPC/E water molecules using gmx solvate. Charge neutralization was achieved by adding 192 Br⁻

counterions via gmx genion, and an additional excess of NaBr was introduced to reproduce the

experimental ionic strength.


Each luminogen (TTG, TTC, TTN, TTY, or TTO) was inserted individually into the aqueous phase of the

solvated bilayer system, yielding five independent simulation systems. The OPLS-AA topology for each

luminogen was generated using the LigParGen server (Dodda et al., 2017). Energy minimization was

performed using the steepest descent algorithm (50,000 steps, force tolerance = 800 kJ mol⁻¹ nm⁻¹) with

PME electrostatics and a real-space cutoff of 1.0 nm. The system was then equilibrated for 1 ns under

NPT conditions (dt = 1 fs) at 300 K using the V-rescale thermostat (τT = 0.5 ps) and the C-rescale barostat

in semiisotropic mode (P = 1 bar, τp = 5.0 ps), with separate temperature coupling groups for the bilayer ,

water and ion phase. Periodic boundary conditions were applied in all directions.


Production runs were carried out for 200 ns (dt = 2 fs) under the same NPT ensemble. Electrostatic

interactions were treated with the particle-mesh Ewald (PME) method, and van der Waals interactions

were computed using PME-LJ (rvdw = 1.3 nm) to ensure accurate long-range dispersion treatment in the
heterogeneous bilayer environment. Coordinates were saved every 10 ps for analysis. All five simulations

reached the full 200 ns production target.


Analysis was performed using MDAnalysis 2.7 (Michaud-Agrawal et al., 2011) with in-house Python

scripts. The following observables were computed over the full production trajectory: (i) mass-density

profiles along the bilayer normal (Z), decomposed into TTAB headgroups, TTAB tails, decanol OH,

decanol chains, decanol tails, water, and Br⁻ ions; (ii) the distance between the luminogen center of mass

and the bilayer midplane, dCOM(t), and the membrane residence fraction fmem, defined as the fraction of

frames in which the luminogen COM lies within the headgroup boundary (determined dynamically from

the 10th/90th percentile of the N0E headgroup positions in each frame); (iii) radial distribution functions

(RDFs) between key luminogen atoms and their interaction partners: ghyd(r) between the luminogen

central nitrogen and all aliphatic carbons of TTAB chains and decanol, gelec(r) between the luminogen

aldehyde oxygen and the TTAB quaternary nitrogen (N0E), gDeOH(r) between the luminogen oxygen and

the decanol hydroxyl oxygen, and gsol(r) between the luminogen oxygen and water oxygen atoms; (iv) the

tilt angle θ between the molecular long axis (defined by the N→O vector) and the membrane normal (Z);

and (v) the second-rank orientational autocorrelation function C2(t) = ⟨P2[û(t)·û(0)]⟩, where P2 is the

second Legendre polynomial and û is the unit vector along the molecular axis. The rotational correlation

time τc was defined as the lag time at which C2(t) decays to 1/e of its initial value. Coordination numbers

Nhyd and Nelec were obtained by integrating the corresponding RDF up to a cutoff of rc = 0.5 nm.




3. Results and Discussion


3.1. Spectral and Macroscopic Characterization of AIE Luminogens in the Lyotropic LC
A first indication of how substituent engineering controls the behavior of the AIE luminogens in the

lyotropic TTAB/decanol/water system is provided by their steady-state optical response in the

liquid-crystalline (LC) medium, benchmarked against the corresponding photophysics in ethyl acetate

(EtOAc). In EtOAc, the luminogens display well-defined absorption and donor–acceptor emission

profiles characteristic of push–pull systems, where the emission energy is governed by the extent of

excited-state relaxation and the local polarity experienced by the emitting state. Because EtOAc provides

an isotropic environment of intermediate polarity, it constitutes a useful reference to assess whether the

LC host exposes the luminogens to a more hydrophobic (less polar) or more hydrated/interfacial (more

polar) microenvironment. The absorption and emission spectra acquired in EtOAc are therefore presented

in the Supporting Information (Figure S2).

In the LC medium, the absorption spectra of the luminogens (Figure 1a) remain broadly comparable in

shape and band positions across the series, suggesting that the chromophores are effectively dispersed at

the loading employed and that the ground-state electronic structure is not drastically perturbed by the

host. In contrast, the emission response is highly sensitive to the LC microenvironment and reveals clear

substituent-dependent trends (Figure 1b). Notably, TTG, TTC, and TTN exhibit a discernible blue shift of

the emission maximum relative to EtOAc (Figure 1b vs. Figure S2), consistent with these luminogens

residing, on average, in a less polar region of the LC assembly than EtOAc, most plausibly within the

membrane-like hydrophobic domain (or a low-dielectric interfacial region with limited water access). For

donor-acceptor luminogens, such blue shifts are commonly associated with reduced stabilization of a

relaxed charge-transfer–like emissive state in lower-dielectric environments. By contrast, TTY and TTO

display LC emission profiles that closely resemble their spectra in EtOAc (Figure 1b and Figure S2),

suggesting that their dominant emitting populations experience a comparatively more polar/hydrated

microenvironment within the lyotropic system. Importantly, this spectral partitioning, blue-shifted vs

EtOAc-like emission, already anticipates the central mechanistic theme of this work: small structural
changes (nitro vs methoxy substitution, donor identity, and π-bridge extension) can shift the balance

between hydrophobic partitioning and interfacial/aqueous preference in the LC host.




Figure 1. Spectra of AIE luminogens in the lyotropic LC (a) UV-vis absorption spectra of TTG, TTC,

TTN,    TTY,   and   TTO     recorded   in the TTAB/decanol/water        lyotropic LC. (b) Steady-state

photoluminescence spectra of the same samples in the LC.

Beyond spectroscopy, we verified that the LC phase is preserved after luminogen addition and that all

prepared samples are suitable for polarization experiments. Figure 2 summarizes the visual

characterization of the LC systems. Polarized optical microscopy (POM) images acquired under crossed

polarizers (Figure 2a) show birefringent textures for the neat LC as well as for each luminogen-doped

sample, confirming the presence of a liquid-crystalline mesophase and indicating that luminogen

incorporation does not disrupt LC formation under the preparation conditions used. Complementary

macroscopic photographs under ambient light (Figure 2b) show that all samples are transparent,

consistent with minimal scattering and the absence of macroscopic phase separation or large undissolved

particles. Under UV illumination (Figure 2c), pronounced differences emerge: TTG, TTC, and TTN

display bright luminescence, whereas TTO and TTY exhibit comparatively weak fluorescence. For

AIE-active systems, enhanced emission in structured media is commonly associated with restriction of

intramolecular motion (RIM), whereby confinement within an ordered host suppresses non-radiative
deactivation pathways. Accordingly, the strong UV emission observed for TTG, TTC, and TTN (Figure

2c) is consistent with more effective incorporation and confinement within the LC assembly. Conversely,

the weak response of TTO and TTY (Figure 2c) suggests that these luminogens experience lower

confinement, consistent with a larger fraction residing in more fluid, hydrated regions where

intramolecular motions remain comparatively unrestricted and emission is less efficient.




Figure 2. Visual characterization of the lyotropic LC samples (a) POM images of the neat LC and LC

samples doped with TTG, TTC, TTN, TTY, and TTO (10x magnification). (b) Photographs of the

corresponding samples under ambient light. (c) Photographs of the same samples under UV

illumination (UV wavelength 365 nm).


Taken together, the LC spectral shifts (Figure 1b) relative to EtOAc (Figure S2) and the visual/POM

characterization (Figure 2) converge on a coherent picture: TTG, TTC, and TTN preferentially sample

less polar and more confining regions of the lyotropic LC (consistent with deeper partitioning and

stronger AIE-type enhancement), whereas TTY and TTO are more compatible with polar

microenvironments and/or are less effectively confined. This experimental classification provides a direct

basis for interpreting the polarization spectra (Section 3.2) and motivates the molecular dynamics analysis
(Section 3.3), where localization, penetration depth, and host–guest interactions are quantified to

rationalize why specific substituents favor or hinder insertion into the membrane-like LC domains.


3.2. Polarization Spectral Dependence


Steady-state fluorescence polarization spectra were collected as a function of emission wavelength to

probe how molecular structure and microenvironment control the orientational dynamics of the AIE

luminogens in isotropic versus anisotropic media. Measurements were performed in EtOAc as an

isotropic reference and in the lyotropic TTAB/decanol/water LC as an anisotropic host. In addition,

polarization was recorded under external alignment conditions (“LC + magnetic field”) to evaluate how

macroscopic ordering impacts the optical anisotropy of the embedded luminogens.


In EtOAc, the polarization values remain low across the emission band for all compounds (Figure S2),

consistent with fast rotational diffusion in an isotropic fluid and confirming that the enhanced polarization

observed in the LC does not arise from an intrinsic property of the chromophores but from the anisotropic

constraints imposed by the host.


In the main text, we highlight the strong contrast between TTG and TTO by presenting their

wavelength-dependent polarization in the LC with and without magnetic alignment (Figure 3). TTG

displays a pronounced polarization response in the LC (Figure 3a), reaching a maximum polarization of P

= 0.346 at 450 nm in the absence of the magnetic field, which increases to P = 0.583 at 450 nm under

magnetic alignment. Across the emission band, TTG exhibits a clear spectral decay of polarization toward

longer wavelengths (e.g., from P = 0.346 at 450 nm to P = 0.118 at 590 nm without the field; and from P

= 0.583 at 450 nm to P = 0.176 at 590 nm under the field), indicating progressive depolarization toward

the red edge of the spectrum.


In contrast, TTO exhibits substantially lower polarization in the LC (Figure 3b). Within the main emission

window where the signal is robust, the maximum polarization is P = 0.171 at 510 nm without magnetic
alignment and P = 0.090 at 510 nm under magnetic alignment, followed by a rapid decrease toward

longer wavelengths (e.g., P = 0.068 at 590 nm without the field and P = 0.012 at 590 nm under the field).

Overall, the TTG vs TTO comparison (Figure 3) provides a clear experimental contrast between a system

that exhibits strong LC-induced anisotropy (TTG) and one that remains weakly polarized (TTO),

consistent with markedly different degrees of orientational confinement within the lyotropic assembly.


A key feature observed for the LC samples is the wavelength dependence of polarization, where the

short-wavelength side of the emission band typically presents higher polarization and the red side

becomes progressively depolarized (Figure 3). This behavior can be rationalized by considering that these

donor–acceptor luminogens can emit from excited-state populations with different degrees of relaxation.

The blue side of the emission is consistent with a less-relaxed, locally excited (LE-like) contribution that

retains stronger orientational memory with respect to the initially excited transition dipole. In contrast, the

red tail increasingly reflects a relaxed intramolecular charge-transfer (ICT-like) population formed after

internal reorganization of the molecule and its microenvironment. The lower polarization at longer

wavelengths is therefore attributed to enhanced orientational relaxation during excited-state evolution (LE

→ ICT conversion) and/or changes in the direction of the emitting transition dipole associated with

intramolecular torsion and charge redistribution, such that the red-shifted emission effectively averages

out the initial excitation anisotropy.
Figure 3. Wavelength-dependent steady-state fluorescence polarization of (a) TTG and (b) TTO in the

TTAB/decanol/water LC, measured without and with magnetic alignment (“LC + magnet”).


For the remaining luminogens, the LC polarization spectra are compiled in the Supporting Information

(Figure S3). Importantly, TTC and TTN display polarization trends qualitatively similar to TTG—i.e.,

they are clearly polarized in the LC, yet with lower magnitudes than TTG—whereas TTY behaves closer

to TTO, exhibiting comparatively weak polarization approaching depolarized emission over most of the

band. Together with the EtOAc control data (Figure S2), these results establish two experimentally

distinct regimes: (i) luminogens that remain significantly polarized in the LC (TTG, with TTC/TTN as

lower-polarization analogues) and (ii) luminogens that are weakly polarized in the LC (TTO, with TTY

showing a similar near-depolarized response).


3.3 Molecular dynamics insights


To elucidate the structural origin of the markedly different photophysical and polarization responses

across the AIE luminogens, we performed atomistic MD simulations of the TTAB/NaBr/DeOH/H₂O

lyotropic LC bilayer in the presence of each luminogen (200 ns production for each luminogen, see
Section 2.6). The simulations were analyzed to determine the extent of solute partitioning into the

membrane-like region and the dominant noncovalent interactions stabilizing (or preventing) insertion.

The LC structure was first characterized through mass-density profiles along the membrane normal (Z),

which define the aqueous phase, the TTAB headgroup region, and the hydrophobic slab enriched in

decanol tails. To enable direct visual comparison across all luminogens, a single reference bilayer density

was computed by averaging the profiles from all five simulations (Figure 4a–b). The solute localization

was then overlaid as the individual density profiles of the luminogen nitrogen and oxygen atoms,

separating emitters (TTG, TTC, TTN; Figure 4a) from non-emitters (TTY, TTO; Figure 4b). TTG and

TTC show pronounced density peaks within the hydrophobic core of the bilayer, confirming persistent

embedding. In contrast, TTY and TTO exhibit density maxima in the aqueous region, with only weak

shoulders at the interface.

The extent of membrane insertion was quantified by the fraction of simulation time spent within the

membrane region (fmem) and the mean center-of-mass distance from the bilayer midplane (dCOM). The

headgroup boundary used to define fmem was computed dynamically in each frame from the positions of

the TTAB quaternary nitrogens (see Section 2.6). TTG yielded fmem = 0.80 with dCOM = 0.61 ± 0.42 nm,

and TTC gave fmem = 0.77 with dCOM = 0.74 ± 0.38 nm, confirming that both luminogens reside

predominantly within the bilayer interior (Figure 5a). In contrast, TTY showed fmem = 0.02 and dCOM =

1.45 ± 0.27 nm, while TTO gave fmem = 0.09 and dCOM = 1.22 ± 0.33 nm, indicating that these luminogens

remain almost entirely in the aqueous phase. TTN yielded fmem = 0.27 with dCOM = 1.05 ± 0.37 nm, placing

it in an intermediate regime between the deeply embedded (TTG, TTC) and the aqueous-phase (TTY,

TTO) luminogens.

We next decomposed the interaction landscape into two complementary contributions. Hydrophobic

packing was quantified from the RDF between the luminogen central nitrogen and all aliphatic carbons of

TTAB chains and decanol, ghyd(r), with the corresponding coordination number Nhyd integrated to rc = 0.5

nm (Figure 5d). For TTG, Nhyd = 4.7, reflecting dense packing of the conjugated core within the alkyl
environment, consistent with the well-established role of van der Waals contacts as the primary

thermodynamic driver of small-molecule partitioning into lipid bilayer interiors (Stouch, 1997; Redmill &

McCabe, 2010). TTC shows Nhyd = 4.0, slightly lower but still consistent with significant embedding. In

contrast, TTO yields Nhyd = 1.9 and TTY gives Nhyd = 2.7, confirming substantially weaker hydrophobic

contacts. TTN gives Nhyd = 2.2, intermediate between the embedded and aqueous groups, consistent with

its partial interfacial localization.

Electrostatic interactions were assessed from the RDF between the luminogen aldehyde oxygen and the

TTAB cationic headgroup nitrogen, gelec(r). The corresponding coordination numbers are modest across

all systems (Nelec ≈ 0.1–0.4 at rc = 0.5 nm), indicating that direct ion–dipole contacts between the

luminogen and TTAB headgroups are not the primary stabilization mechanism. Rather, the driving force

for insertion is dominated by hydrophobic matching of the conjugated core with the alkyl slab, a

mechanism well established in the membrane biophysics literature for transmembrane solutes

(Kandasamy & Larson, 2006).

Nonbonded       energy     decomposition   (Lennard-Jones    and    Coulombic     contributions   between

luminogen–membrane and luminogen–solvent groups) is in preparation via GROMACS energy group

reruns and will be included in the final manuscript.

Together, these metrics reveal that embedded luminogens (TTG, TTC) benefit from strong hydrophobic

packing of the donor–acceptor conjugated core inside the decanol-rich slab. TTN occupies an

intermediate position (fmem = 0.27, Nhyd = 2.2), spending significant time at the interface but without the

sustained deep embedding characteristic of TTG and TTC. Conversely, TTY and TTO are stabilized

predominantly by solvation in the aqueous phase, where the methoxy and dimethylamino substituents

enhance hydrophilicity and compete effectively against insertion.

Orientational bias and restricted rotational dynamics. Because fluorescence polarization depends critically

on rotational mobility and orientational constraints, we analyzed the tilt angle distribution of each

luminogen relative to the membrane normal (Z) and the decay of the rotational autocorrelation function
C2(t) (Figure 5b–c). TTG displays a sharp tilt distribution centered at θ = 165 ± 16°, indicating strong

preferential alignment roughly antiparallel to the membrane normal. TTC shows a similar but slightly

broader distribution at θ = 161 ± 24°. In contrast, TTO exhibits a nearly isotropic distribution centered at

θ = 96 ± 58°, and TTY shows an intermediate distribution at θ = 125 ± 29°. TTN adopts a distinctive tilt

of θ = 50 ± 32°, markedly different from the other luminogens and roughly perpendicular to the

membrane surface, suggesting that when TTN approaches the bilayer interface it orients with its long axis

nearly parallel to the membrane plane rather than inserting end-on.

The rotational correlation function C2(t) provides a direct probe of rotational freedom. For TTG and TTC,

C2(t) shows no measurable decay over the accessible 100 ns lag window, with plateau values of S2 = 0.74

and 0.69, respectively (τc >> 100 ns; Figure 5c). This essentially frozen rotational diffusion is consistent

with the high fluorescence polarization observed experimentally. Analogous behavior has been reported

for fluorescent probes embedded in gel-phase phospholipid bilayers, where rotational correlation times

exceeding hundreds of nanoseconds have been measured both experimentally and via MD simulation

(Muddana et al., 2011; Davenport et al., 1985). The present plateau values indicate that the gel-phase

bilayer imposes severe steric confinement on the embedded luminogens. In contrast, TTO and TTY

exhibit rapid initial decorrelation with τc = 4.5 ns and 9.1 ns, respectively, and low plateau values (S2 =

0.27 and 0.16), consistent with the near-depolarized emission observed experimentally for these

aqueous-phase luminogens and with the short rotational correlation times typically reported for freely

tumbling molecular rotors in low-viscosity environments (Steinmark et al., 2020). TTN shows τc = 67 ns

with a moderate plateau (S2 ≈ 0.13), an intermediate behavior: its rotational diffusion is substantially

slower than the aqueous-phase luminogens but does not reach the essentially frozen regime of TTG and

TTC, consistent with partial but not persistent embedding.

Overall, the MD results support a unified mechanistic picture: TTG and TTC partition into the LC

membrane and remain embedded due to effective hydrophobic matching between their conjugated cores

and the alkyl slab. Once inserted, the gel-phase environment restricts rotational motion (τc >> 100 ns) and
imposes orientational bias (θ ≈ 163–165°), thereby enhancing AIE emission through what may be termed

extrinsic RIM—an environment-imposed restriction analogous to the confinement effects reported for

AIE luminogens in liquid crystalline matrices (Hisano et al., 2022; Xu et al., 2020)—and fluorescence

polarization through orientational alignment. TTN presents an instructive intermediate case: despite being

classified as an emitter, its membrane residence is modest (fmem = 0.27) and its orientation (θ ≈ 50°) differs

markedly from the deeply embedded luminogens, yet its rotational correlation time (τc = 67 ns) is

substantially longer than those of TTY and TTO, suggesting that even transient interfacial association

provides meaningful rotational restriction. TTY and TTO, in contrast, remain largely solvated in water

(fmem < 0.1, dCOM > 1.2 nm) with rapid rotational diffusion (τc ≈ 4–9 ns), leading to weaker restriction,

reduced polarization, and diminished AIE activation within the LC system. Importantly, TTC shows the

strongest emission experimentally despite slightly lower membrane residence than TTG (fmem = 0.77 vs

0.80), which can be attributed to the intrinsic rigidity of the carbazole donor moiety—a structurally planar

unit whose fused tricyclic framework inherently limits intramolecular torsional freedom (Chen et al.,

2015)—the restricted intramolecular rotation is partially built into the molecular architecture (intrinsic

RIM), such that even moderate membrane confinement is sufficient to fully activate AIE. This dual RIM

mechanism—intrinsic (molecular rigidity) plus extrinsic (membrane confinement)—extends the classical

RIM paradigm (Zhang et al., 2021; Zhao et al., 2020) to heterogeneous soft-matter hosts and provides a

design principle for optimizing AIE luminogens in ordered media.
Figure 4. Mass-density profiles along the bilayer normal (Z) for the TTAB/DeOH/H₂O lyotropic LC

system with overlaid luminogen atom densities. The bilayer density (TTAB headgroups, chains, and tails;

DeOH hydroxyl, chains, and tails; water; Br⁻) represents the average across all five simulation systems.

(a) Emitters (TTG, TTC, TTN): solid lines show the nitrogen atom density and dashed lines show the

oxygen atom density for each luminogen, confirming localization within the hydrophobic core. (b)

Non-emitters (TTY, TTO): the same atom-specific densities reveal predominant residence in the aqueous

phase with only transient interfacial contacts.
Figure 5. Comparative molecular dynamics analysis of AIE luminogens in the lyotropic LC bilayer. (a)

Time evolution of the luminogen center-of-mass distance from the bilayer midplane, ZCOM(t); gray dashed

lines indicate the mean headgroup boundary. (b) Tilt angle distributions of the molecular long axis (N→O

vector) relative to the membrane normal, computed over the full trajectory (second half for equilibrated

systems). (c) Second-rank orientational autocorrelation function C2(t); embedded luminogens (TTG,

TTC) show no measurable decay (τc >> 100 ns), while aqueous-phase luminogens (TTY, TTO)

decorrelate rapidly (τc = 4–9 ns). (d) Hydrophobic RDF ghyd(r) between the luminogen central nitrogen

and aliphatic carbons of TTAB chains and decanol, with coordination numbers Nhyd integrated to rc = 0.5

nm.
Acknowledgements



Funding sources



References

Abraham, M. J., Murtola, T., Schulz, R., Páll, S., Smith, J. C., Hess, B., & Lindahl, E. (2015).

GROMACS: High performance molecular simulations through multi-level parallelism from laptops to

supercomputers. SoftwareX, 1–2, 19–25. https://doi.org/10.1016/j.softx.2015.06.001

​   Chen, G., Li, W., Zhou, T., Peng, Q., Zhai, D., Li, H., Yuan, W. Z., Zhang, Y., & Tang, B. Z. (2015).

Conjugation-Induced Rigidity in Twisting Molecules: Filling the Gap Between Aggregation-Caused

Quenching and Aggregation-Induced Emission. Advanced materials (Deerfield Beach, Fla.), 27(30),

4496–4501. https://doi.org/10.1002/adma.201501981

Davenport, L., Dale, R. E., Bisby, R. H., & Cundall, R. B. (1985). Transverse location of the fluorescent

probe 1,6-diphenyl-1,3,5-hexatriene in model lipid bilayer membrane systems by resonance excitation

energy transfer. Biochemistry, 24(15), 4097–4108. https://doi.org/10.1021/bi00336a044

​   Dodda, L. S., Cabeza de Vaca, I., Tirado-Rives, J., & Jorgensen, W. L. (2017). LigParGen web server:

An automatic OPLS-AA parameter generator for organic ligands. Nucleic Acids Research, 45(W1),

W331–W336. https://doi.org/10.1093/nar/gkx312

​   Hisano, K., Tsutsumi, O., & Panthai, S. (2022). Liquid crystalline aggregation-induced emission

luminogens for optical displays. In Y. Tang (Ed.), Aggregation-Induced Emission (pp. 373–395).

Elsevier. https://doi.org/10.1016/B978-0-12-824335-0.00008-8

​   Kandasamy, S. K., & Larson, R. G. (2006). Molecular dynamics simulations of model trans-membrane

peptides in lipid bilayers: A systematic investigation of hydrophobic mismatch. Biophysical Journal,

90(7), 2326–2343. https://doi.org/10.1529/biophysj.105.073395
​   Martínez, L., Andrade, R., Birgin, E. G., & Martínez, J. M. (2009). PACKMOL: A package for building

initial configurations for molecular dynamics simulations. Journal of Computational Chemistry, 30(13),

2157–2164. https://doi.org/10.1002/jcc.21224

​   Michaud-Agrawal, N., Denning, E. J., Woolf, T. B., & Beckstein, O. (2011). MDAnalysis: A toolkit for

the analysis of molecular dynamics simulations. Journal of Computational Chemistry, 32(10),

2319–2327. https://doi.org/10.1002/jcc.21787

​   Muddana, H. S., Gullapalli, R. R., Manias, E., & Butler, P. J. (2011). Atomistic simulation of lipid and

DiI dynamics in membrane bilayers under tension. Physical Chemistry Chemical Physics, 13(4),

1368–1378. https://doi.org/10.1039/c0cp00430h

​   Redmill, P. S., & McCabe, C. (2010). Molecular dynamics study of the behavior of selected nanoscale

building blocks in a gel-phase lipid bilayer. The Journal of Physical Chemistry B, 114(28), 9165–9172.

https://doi.org/10.1021/jp1039942

​   Steinmark, I. E., James, A. L., Sherpa, R.-D., Sheridan, P. H., & Sherpa, D. (2020). Time-resolved

fluorescence anisotropy of a molecular rotor resolves microscopic viscosity parameters in complex

environments. Small, 16(18), 1907139. https://doi.org/10.1002/smll.201907139

​   Stouch, T. R. (1997). Solute transport and partitioning in lipid bilayers: Molecular dynamics

simulations. In J. Texter (Ed.), Amphiphiles at Interfaces (Progress in Colloid & Polymer Science, Vol.

103, pp. 116–120). Steinkopff.

​   Xu, S., Duan, Y., & Liu, B. (2020). Precise molecular design for high-performance luminogens with

aggregation-induced         emission.        Advanced          Materials,        32(1),       1903530.

https://doi.org/10.1002/adma.201903530

​   Zhang, J., Zhang, H., Lam, J. W. Y., & Tang, B. Z. (2021). Restriction of intramolecular motion (RIM):

Investigating AIE mechanism from experimental and theoretical studies. Chemical Research in Chinese

Universities, 37(1), 1–15. https://doi.org/10.1007/s40242-021-0381-6
​   Zhao, Z., Zhang, H., Lam, J. W. Y., & Tang, B. Z. (2020). Aggregation-induced emission: New vistas at

the   aggregate   level.   Angewandte     Chemie     International   Edition,   59(25),   9888–9907.

https://doi.org/10.1002/anie.201916729
