> **Verification (2026-11-02, citation-verifier, checked against the local CIFs and the live sources):** all five priority claims hold (cases 01, 02, 03, 06, 10), and spot checks of the other cases found nothing wrong. Corrections:
> - **Case 02:** the CIF contradicts itself. `_exptl_absorpt_correction_type` says "multi-scan", but the process details describe Gaussian integration in STOE X-Red32.
> - **Case 03:** the major Se2 occupancy is 1. The value 0.5 is only the SHELX site factor for the special position. The Nd paper's author order is Schmidt, Dityat'yev, Dolgikh (Crossref).
> - **Case 10:** the comparison table has 8 entries, not 9. COD 2242171 is a neutral [Fe2Cl4O(C26H28N4)] complex, not [Fe2OCl6]2-. The exact abstract quote about the linear O atom could not be verified.

# Literature and database evidence for adjudication (SEALED)

*Compiled 2026-11-02. Evidence only, no verdicts. Atom labels are the ORIGINAL (deposited CIF) labels unless marked "task". Unverified or uncertain items are marked **[uncertain]**.*

## General notes that apply to every case

- **None of the nine COD CIFs has `_refine_special_details` or any checkCIF `_vrf_` response items.** I grepped every file for `special_details`, `_vrf_` and "disorder". The only hits were the `_atom_site_disorder_*` loop headers. The COD copies carry no author refinement remarks beyond the embedded SHELXL `.res` (REM lines, restraints, PART/FVAR) and the Q-peak list. They also have no `_publ_section_exptl_refinement` text.
- **Residual peaks.** The "Q peak" positions below come from the authors' embedded `.res` (their final SHELXL Fourier peaks). I computed the distances to the nearest atoms myself, with the space-group symmetry, using `/private/tmp/.../scratchpad/res.py`.
- **Publisher pages could not be read.** journals.iucr.org returned HTTP 403 to automated fetches and I did not try to get around that. Full text was read only where the paper is open access in PubMed Central / Europe PMC (cases 01, 04, 05, 06). For the other papers I read only the abstract, from Europe PMC.
- **Database coverage.** "Other determinations" means a search of COD only, through its JSON search API (formula and text search). I had no CSD/ICSD access, so CSD-only determinations would be missed.

---

## Case 01: COD 2312281 (izbt·2,5-dihydroxybenzoic acid cocrystal)

**Publication.** Scheepers & Lemmerer, "The synthesis and characterization of a series of cocrystals of an isoniazid derivative with butan-2-one and propan-2-one", *Acta Cryst.* C79 (2023) 365–373. DOI [10.1107/S2053229623007179](https://doi.org/10.1107/S2053229623007179). Open access as [PMC10561595](https://pmc.ncbi.nlm.nih.gov/articles/PMC10561595/).

**What the authors' CIF says:**
- No `_refine_special_details` and no `_vrf_` items.
- `_refine_diff_density_max 1.331`, `_refine_diff_density_min -0.676`, R1(gt) 0.0675, T = 123 K.
- The deposited model disorders the **terminal methyl, not C26**:
  - C27A (occupancy FVAR 3 = 0.773) and C27B (0.227).
  - Restraints `SADI 0.01 C26 C27A C26 C27B`, `SIMU 0.02 0.04 2 C26 C27A C27B` and `DELU 0.005 0.005 C26 C27A C27B`.
  - C26 is a single site with U33 = 0.121 (U11 0.055, U22 0.060).
  - Bond lengths: C26–C27A 1.450(6) Å, C26–C27B 1.419(11) Å.
- In the same .res, the other izbt molecule's ethyl group (task C36/C37) is also split (C9/C10 pair, PART 1/2).
- **Largest residual peak:** Q1 = 1.33 e/Å³. It sits 0.33 Å from H26B, 1.12 Å from C26 and 1.89 Å from C27A. Q2 = 0.67 e/Å³ is 0.83 Å from C26 and 1.12 Å from C27A.
  - So the two largest deposited peaks are both on this C26 methylene.
  - The candidate's extra atom (task C27B, at "H24 0.31 Å") sits at the Q1 position.

**What the paper says.** Quoting the PMC full text, section "Crystal structure of izbt–2,5-dhba":

> "A disorder model exists where the methylene group of one of the izbt molecules has been split into two different sites (C26A and C26B)."

- **The paper text and the deposited model disagree.** The text describes a split of the CH2 group (C26A/C26B). The deposited CIF has C26 unsplit and the CH3 split (C27A/C27B).
- I cannot tell from public material which one the authors intended. The CIF in COD is `dv3024sup1.cif`, block `izbt25dhba`.

**Other determinations.**
- **Same compound.** COD formula search C17H19N3O5 found no other determination of izbt·2,5-dhba.
- **The izbt ethyl group in other structures:**
  - [COD 2312278](https://www.crystallography.net/cod/2312278.html) (izbt·2,4-dhba, same paper) disorders **both ethyl carbons**, C9A/C10A 0.681(9) and C9B/C10B 0.319(9). The paper says "two C atoms (C9 and C10) of the alkyl portion of izbt were split over two different positions".
  - Ordered izbt ethyl groups:
    - [2312277](https://www.crystallography.net/cod/2312277.html) (1-naphthoic acid)
    - [2312280](https://www.crystallography.net/cod/2312280.html) (2-chloro-4-nitrobenzoic acid)
    - [7206494](https://www.crystallography.net/cod/7206494.html) and [7212466](https://www.crystallography.net/cod/7212466.html) (3-hydroxybenzoic acid, CrystEngComm 2010/2011)
    - [8104589](https://www.crystallography.net/cod/8104589.html) (hydrate)
    - [8104675](https://www.crystallography.net/cod/8104675.html) (2-hydroxybenzoic acid)
  - [2021460](https://www.crystallography.net/cod/2021460.html) (4-tert-butylbenzoic acid cocrystal) has disorder only in the tert-butyl group of the acid; its izbt ethyl is ordered.

---

## Case 02: COD 2312879 (bis(4-cyanothiazole)gold(I) tetrachloridoaurate(III))

**Publication.** Ejnik, Ponikiewski, Bruździak & Dołęga, "Aurophilic interactions in a mixed-valent Au^I/III 4-cyanothiazole complex", *Acta Cryst.* B82 (2026) 433–438. DOI [10.1107/S2052520626006529](https://doi.org/10.1107/S2052520626006529).
- Not open access, so I read only the abstract ([Europe PMC 42454695](https://europepmc.org/article/MED/42454695)).
- The abstract reports Au^I···Au^III = 3.294(4) Å and says nothing about residual density or disorder. **I could not read the paper's refinement section.**

**What the authors' CIF says:**
- No `_refine_special_details` and no `_vrf_` items. The space group is C2/m.
- Au1 is at (0, ½, ½) and Au2 at (0, 0, ½), both on 2/m sites.
- `_refine_diff_density_max 11.609` and `_refine_diff_density_min -3.721`. The .res gives a 1-sigma level of 0.688.
- R1 0.0695, wR2 0.2056, 63 parameters, 1 restraint (`DFIX 1.360 0.002 c2 c3`).
- Three reflections are OMITted: −5 1 3, −5 3 3 and 2 0 2.
- Weighting `WGHT 0.1363 27.79`.
- Absorption: μ = 19.617 mm⁻¹ (Mo Kα), crystal 0.13 × 0.13 × 0.12 mm, STOE IPDS 2T, `_exptl_absorpt_correction_type multi-scan`. The reported T_min and T_max are **both 1.0000**.
- **Peak list (distances computed with symmetry):**

| peak | height (e/Å³) | position |
|---|---|---|
| Q1 | 11.61 | 1.20 Å from Au1 and 1.21 Å from Cl1 |
| Q2 | 11.46 | 1.20 Å from Au2 |
| Q3 | 6.83 | 1.36 Å from H1, 2.02 Å from C1, 2.18 Å from Cl1 |
| Q4 | 6.75 | 0.98 Å from Cl1 |
| Q5 | 2.55 | 1.22 Å from Au1 |
| Q6 | 2.33 | 1.17 Å from Au2 |

- Q1 and Q2 are displaced from Au1 and Au2 by the same fractional vector, about (−0.093, 0, −0.007). Q5 and Q6 are displaced from the Au atoms along b.

**Other determinations.**
- COD formula search C8H4Au2Cl4N4S2 and text search "4-cyanothiazole" each return only 2312879. I found no other determination.

**Generic: Au "ghost" peaks about 1.2 Å from Au.**
- **No literature found** that quantifies how common residual maxima about 1.2 Å from Au are, or assigns them specifically.
- The explanations I found are depositors' checkCIF responses to PLAT971/972 alerts (residual density near heavy atoms). These are not peer-reviewed. Examples:
  - one attributes peaks near Os to "significant absorption effects" that "can not be corrected completely";
  - another attributes peaks near Pb to "fourier termination ripples".
  - Both are search-result snippets, not verified verbatim **[uncertain]**: [example responses (RSC suppdata)](https://www.rsc.org/suppdata/c7/dt/c7dt01098b/c7dt01098b3.pdf), [Research Square checkCIF report](https://assets-eu.researchsquare.com/files/rs-8897604/v1/8a7e42878f7aae544f4c732e.pdf).
- Absorption residuals, series termination, and a minor twin or displaced domain are standard textbook causes of heavy-atom satellite peaks. Examples: Müller (ed.), *Crystal Structure Refinement*, IUCr/OUP 2006, chapters on disorder and twinning.
  - That book is cited from memory and **not checked for a specific statement [uncertain]**.

---

## Case 03: COD 2312981 (Yb selenite–selenate hydrate)

**Publication.** Jones & Ling, "Synthesis and structural characterization of rare-earth selenates: Yb2(SeO3)(SeO4)2(H2O)2, Yb(HSeO3)(SeO4), and Tm2(SeO4)3(H2O)4·H2O", *Acta Cryst.* C82 (2026) 331–335. DOI [10.1107/S2053229626005449](https://doi.org/10.1107/S2053229626005449).
- Not open access. The abstract ([Europe PMC 42244385](https://europepmc.org/article/MED/42244385)) does not mention disorder. **I could not read the full text.**

**What the authors' CIF says:**
- No `_refine_special_details` and no `_vrf_` items. Space group C2/c, T = 293 K.
- `_refine_diff_density_max 2.617` and `_refine_diff_density_min -0.976` (1-sigma 0.201). R1 0.0170.
- μ = 29.03 mm⁻¹ (Mo Kα), multi-scan correction, T_min/T_max 0.440/1.000.
- **Largest peak.** Q1 = 2.62 e/Å³ at (0, 0.1592, 0.75), which is **on the twofold axis**. It is:
  - 2.20 Å from the selenate Se2 (task "Se1") along b;
  - 1.28 Å from water H2B, 1.74 Å from O4 and 2.05 Å from O2.
  - The deposited Se2 is at (½, 0.3375, ¾) with occupancy 0.5 (site symmetry 2).
- Q2 = 1.48 e/Å³ is 1.56 Å from Se1 (the selenite).
- **Inconsistency between the title and the model:**
  - Title and `_chemical_formula_iupac`: Yb2(SeO3)(SeO4)2(H2O)2.
  - Formula sum H4O12Se3Yb2 and the refined model: Se1 is on a general position and bonded to 3 O (selenite, ×2 per formula unit); Se2 is on the twofold axis and bonded to 4 O (selenate, ×1). The model is therefore Yb2(SeO3)2(SeO4)(H2O)2.
  - This is an observation only; it is not established that it matters for the disorder question.

**Other determinations of the same structure type (strongly relevant).**
- [COD 1535194](https://www.crystallography.net/cod/1535194.html): Berdonosov, Schmidt, Dolgikh, Dityat'yev, Lightfoot & Ruck, Nd2(SeO3)2(SeO4)·2H2O, *Z. Anorg. Allg. Chem.* 630 (2004) 1395–1400, DOI [10.1002/zaac.200400109](https://doi.org/10.1002/zaac.200400109).
  - Same space group C2/c, with a analogous cell (a 12.276, b 7.078, c 13.329 Å, β 104.28°).
  - **The COD CIF refines the selenate Se on the twofold axis as split:**
    - `Se2` at (0.5, 0.15675, 0.25), occupancy **0.962**;
    - `Se3` at (0.5, −0.1565, 0.25), occupancy **0.04**.
  - The Se2···Se3 separation along b is about 0.3133 × 7.078 = **2.22 Å** (my calculation).
  - That is the same geometry as the candidate's minor Se: about 4% of the site, 2.2 Å from the selenate Se, on the twofold axis.
  - The paper's abstract (via Crossref) describes the compound as "an ordered variant of the corresponding erbium compound". The deposited COD CIF nevertheless contains the 0.962/0.04 Se split.
- [COD 1536885](https://www.crystallography.net/cod/1536885.html): Feng & Mao, Nd2(SeO4)(SeO3)2(H2O)2, *J. Alloys Compd.* 388 (2005) 23–27, DOI [10.1016/j.jallcom.2004.06.091](https://doi.org/10.1016/j.jallcom.2004.06.091).
  - Same structure type. Se2 is on the twofold axis at occupancy 1. **No minor Se modelled.**
- Erbium analogue, Er(SeO3)(SeO4)1/2·H2O: Morris, Wilkinson & Cheetham, *Inorg. Chem.* 31 (1992) 4774–4777, DOI [10.1021/ic00049a012](https://doi.org/10.1021/ic00049a012).
  - Not in COD under the formulas I tried. **I could not access it, so I do not know what disorder it models** (the Nd paper calls the Nd compound the "ordered variant", implying the Er structure has some disorder **[uncertain]**).
- COD has no other Yb or other-Ln analogue under the H4 Ln2 O12 Se3 formula (I tried 19 elements).

**Generic: selenate on a twofold axis.** I found nothing beyond the Nd analogue above.

---

## Case 04: COD 2243801 (tetrapropionic acid, polymorph H4L1_B)

**Publication.** Pacifico & Stoeckli-Evans, *Acta Cryst.* E77 (2021) 480–490. DOI [10.1107/S2056989021003479](https://doi.org/10.1107/S2056989021003479). Open access as [PMC8100264](https://pmc.ncbi.nlm.nih.gov/articles/PMC8100264/).

**What the authors' CIF says:**
- No `_refine_special_details` and no `_vrf_` items. T = 293 K, IPDS2.
- R1 0.0711, wR2 0.2078, 173 parameters, 6 restraints.
- `_refine_diff_density_max 0.469` and `_refine_diff_density_min -0.388`.
- **Deposited disorder** is only on the *other* side chain: C8/C9/C10/O3/O4 at 0.821(6) and the B set at 0.179(6), with EADP and DFIX restraints.
- **O2** (the carboxyl OH, O2–H2O, of the ordered C6 side chain) is anisotropic: U11 0.085, U22 0.190, U33 0.162, U23 0.122. The bonded O1 has U values 0.079 to 0.093.
- **Peaks:**
  - Q1 (0.47 e/Å³) is 1.10 Å from O3 (the disordered chain).
  - Q2 (0.46 e/Å³) is **1.27 Å from O2** and 1.10 Å from H2O.
  - All other peaks are ≤ 0.25 e/Å³.

**What the paper says** (PMC full text):
- "The crystals were of poor quality with one CH2—CH2—CO2H side chain (atoms C8/C8B, C9/C9B, C10/C10B, O3/O3B, O4/O4B) of the centrosymmetric molecule being positionally disordered".
- "For H4L1_B, the –CO2H H atoms were difficult to locate, probably due to the poor quality of the crystal and the disorder in the side chain".
- No disorder is mentioned for O2 or the C6 carboxyl group.

**Other determinations.** [COD 2243800](https://www.crystallography.net/cod/2243800.html), polymorph H4L1_A from the same paper, is fully ordered. Its O2 U values are 0.032 to 0.049. It is a different polymorph, so not the same crystal environment. I found no other H4L1_B determination.

---

## Case 05: COD 2243569 ([FeCl2(BPE)2]·2CH2Cl2)

**Publication.** *Acta Cryst.* E76 (2020) 1525–1527. DOI [10.1107/S2056989020011160](https://doi.org/10.1107/S2056989020011160). Open access as [PMC7472749](https://pmc.ncbi.nlm.nih.gov/articles/PMC7472749/). The CCDC number given in the paper is 2023248.

**What the authors' CIF says:**
- No `_refine_special_details` and no `_vrf_` items. Space group P4₃2₁2, c = 52.45 Å, T = 150 K.
- `_refine_diff_density_max 0.389` and `_refine_diff_density_min -0.651`. R1 0.0425.
- **Deposited model: CH2Cl2 already split in two parts.**
  - PART 1: Cl2, Cl3, C1S at FVAR 2 = 0.700.
  - PART 2: Cl4, **Cl5**, C2S at 0.300.
  - Restraint `SIMU 0.01 Cl2 > C2S`.
- Cl5 is very anisotropic, with U11 0.201 and U22 0.225. It lies 1.16 Å from Cl3 and 0.71 Å from C1S, so the two components overlap.
- Peaks are all ≤ 0.26 e/Å³:
  - Q1 (0.26) is 1.04 Å from C2S, 1.14 Å from Cl3 and 1.55 Å from Cl5;
  - Q2 (0.23) is 1.09 Å from Cl2 and 1.62 Å from Cl5.

**What the paper says** (PMC):
- "The asymmetric unit contains one CH2Cl2 solvent molecule, which is disordered over two sets of sites with refined occupancies in the ratio 0.700 (6):0.300 (6)."
- "The major component of the disordered CH2Cl2 solvent molecule was refined without restraints while the minor component was restrained to have similar geometry and anisotropic displacement parameters to the major component using the SAME and SADI instructions in SHELXL".
- Nothing is said about a third component.

**Candidate note** (from case05/case.md): the candidate's Cl91 has Ueq 0.944 Å² and occupancy 0.369, 0.65 Å from Cl5.

**Other determinations.** COD formula and text searches ("binaphthylphosphonito", C86H60Cl6FeO8P4) return only 2243569. I found none.

**Generic: CH2Cl2 solvent disorder.**
- Werner & Swift, "Organic solvates in the Cambridge Structural Database", *CrystEngComm* 23 (2021) 1555–1565, DOI [10.1039/D0CE01749C](https://doi.org/10.1039/D0CE01749C) ([NSF PAR record](https://par.nsf.gov/biblio/10269327)).
  - It is a CSD survey of solvates that discusses disorder. I could not confirm a solvent-specific disorder rate.
  - A search snippet saying "a significant fraction of solvates exhibit disorder" is **not verified verbatim [uncertain]**.
- Crude count from this project's own 1,500-entry COD sample: 11 CIFs list CH2Cl2 in the moiety formula, and 5 of them have at least one Cl atom in a disorder group.
  - This is my own count and imprecise: the disordered Cl may not belong to the CH2Cl2 in every case.

---

## Case 06: COD 2312115 (M4Au12Ag32(p-MBA)30 cluster)

**Publication.** *Acta Cryst.* E74 (2018) 987–993. DOI [10.1107/S2056989018008393](https://doi.org/10.1107/S2056989018008393). Open access as [PMC6038627](https://pmc.ncbi.nlm.nih.gov/articles/PMC6038627/).

**What the authors' CIF says:**
- No `_refine_special_details` and no `_vrf_` items. Space group R-3c, c = 124.08 Å, Cu Kα.
- μ = 18.65 mm⁻¹, multi-scan correction, T 0.565/0.752. T = 100 K.
- `_refine_diff_density_max 2.544` and `_refine_diff_density_min -1.523`. R1 0.0398.
- **Peaks:**
  - **Q1 = 2.54 e/Å³ at 0.99 Å from Ag6**;
  - **Q2 = 2.45 e/Å³ at 0.92 Å from Ag5**;
  - Q3 and Q5 (about 1.5 to 1.7 e/Å³) are near carboxylate O1/O2;
  - Q4 (1.59) is 1.0 Å from S5.
- Ag5 and Ag6 are each three-coordinate to S (Ag–S about 2.49 to 2.53 Å), with Ag5···Ag6 2.99 Å. These look like the Ag atoms of the Ag2(SR)5 "mount" units **[uncertain]**: my reading of the coordination, not stated in the CIF.

**What the paper says** (PMC, Refinement section):
- "The Au, Ag and S atoms were ordered; however three out of the five crystallographically independent ligands in the asymmetric unit cell were disordered over two sets of sites."
- "It is common for MPCs to have a high amount of residual electron density observed in the metal core." The same section adds that the cations and solvent were not identified (highest residue 2.55 e Å⁻³).
- The supplementary refinement text gives the largest difference peak as 2.547 e⁻/Å³ and the largest hole as −1.528 e/Å³, "with an RMS deviation of 0.253 e/Å³".

**Other determinations.**
- COD text searches ("Ag44", "Au12Ag32", "mercaptobenzoic") found no other Ag44 or Au12Ag32 cluster structure.
- The paper cites the Ag44(p-MBA)30 structure (Desireddy et al., *Nature* 2013) and the Au12Ag32(SPhF2)30 and Ag44(SPhF2)30 structures (Yang et al., *Nat. Commun.* 2013). These are presumably in the CSD, which I could not search. **I could not check whether any of them model split mount-Ag sites.**

---

## Cases 07 and 09: COD 2312661 (dinuclear Zn Schiff-base complex · 0.5 bis(2-aminophenyl) disulfide)

**Publication.** Anaya-Avila, Muñoz-Granados, Andrade-López, Alvarado-Rodríguez & Martínez-Otero, *Acta Cryst.* C80 (2024) 698–706. DOI [10.1107/S205322962400946X](https://doi.org/10.1107/S205322962400946X).
- Not open access. The abstract ([Europe PMC 39365564](https://europepmc.org/article/MED/39365564)) says complex 6 "cocrystallized with one molecule of bis(2-aminophenyl) disulfide" and does not mention disorder. **I could not read the full text.**

**What the authors' CIF says:**
- No `_refine_special_details` and no `_vrf_` items. T = 295 K.
- `_refine_diff_density_max 0.621` and `_refine_diff_density_min -0.797`. R1 0.0555.
- **The (2-APS)2 half-molecule is already two-part disordered in the deposited model.** The S3–S3 disulfide bond is about an inversion centre.
  - PART 1: S3, N5, C49–C54 at FVAR 2 = 0.302.
  - PART 2: S3A, N5A, C49A–C54A at 0.698.
  - Restraints: `SIMU 0.005 0.01 2 S3 > C54A`, `FLAT S3 N5 C49 C50 C51 C52 C53 C54`, `RIGU S3 > C54A`, `SAME 0.02 0.04 C50 > C54 C49` and `SAME 0.001 0.001 S3 > C54`.
  - All ring atoms have Ueq about 0.08 to 0.11.
- **C54** (task C46) is the ring carbon ortho to the S-bearing C49 on the side opposite the NH2. **H54** (task H38) is its H atom. Both are in the minor PART 1.
  - C54 lies 0.95 Å from C54A and 0.99 Å from C49A.
  - The NH2 is N5 on C50. An extra N at H54 would correspond to NH2 at the other ortho position, i.e. a ring flip. That is my geometric reading **[uncertain]**.
- **Peaks:**
  - Q1 (0.62) is 0.68 Å from S3;
  - Q2 (0.51) is 0.69 Å from S3 and 0.75 Å from S3A;
  - Q3 (0.37) is 1.16 Å from S1 and 1.23 Å from Zn2.
  - No deposited peak lies near C54 or H54.

**Other determinations of bis(2-aminophenyl) disulfide (2,2'-diaminodiphenyl disulfide).** Both are ordered, with no disorder groups:
- [COD 2225121](https://www.crystallography.net/cod/2225121.html), Pbca, 100 K, Acta E 2010;
- [COD 2006371](https://www.crystallography.net/cod/2006371.html), hemihydrate, I2/a, 295 K, Acta C 1997.

Neither is the same environment, since here the molecule is a cocrystal guest.

---

## Cases 08 and 11: COD 2312969 ((TBTP)2[MnCl4], TBTP = (tert-butoxycarbonyl)methyltriphenylphosphonium)

In the pilot this entry is an ordered **control**: the deposited model has no disorder anywhere.

**Publication.** Jiao, Liu & Dong, "Synthesis, crystal structure and green luminescence of a novel manganese(II)-based hybrid: bis[(tert-butoxycarbonyl)methyltriphenylphosphonium] tetrachloridomanganate(II)", *Acta Cryst.* C82 (2026) 534–541. DOI [10.1107/S205322962600731X](https://doi.org/10.1107/S205322962600731X).
- Not open access. The abstract ([Europe PMC 42554698](https://europepmc.org/article/MED/42554698)) does not mention disorder. **I could not read the full text.**

**What the authors' CIF says:**
- No `_refine_special_details` and no `_vrf_` items. P2₁/n, T = 150 K.
- `_refine_diff_density_max 1.413` and `_refine_diff_density_min -0.586`. R1 0.0387.
- No PART instructions.
- **The five largest residual peaks all surround this tert-butyl ester:**

| peak | height (e/Å³) | position |
|---|---|---|
| Q1 | 1.41 | 1.03 Å from O2, 1.27 Å from C20 |
| Q2 | 1.15 | 1.09 Å from H23B, 1.73 Å from C23 |
| Q3 | 0.99 | 0.86 Å from O1 |
| Q4 | 0.99 | 0.86 Å from C23, 0.99 Å from C21 |
| Q5 | 0.56 | 0.93 Å from C21, 1.10 Å from C24 |
| Q6 | 0.30 | elsewhere |

- ADPs: O2 has U11 0.064 and U22 0.090. C21 has U11 0.078. C22, C23 and C24 have U11 0.06 to 0.08.
- The candidate's minor-part atoms (case08/case11 case.md) sit on deposited density of 0.9 to 1.2 e/Å³.

**Other determinations.**
- COD has no other structure containing this cation. I tried text "butoxycarbonyl)methyl", "tert-butoxy-2-oxoethyl" and "TBTP".
- I also tried these formulas: bromide, chloride and iodide salts; the ylide C24H25O2P; and the [MBr4]/[MCl4] analogues with Mn, Co, Zn and Cu. A web search also found no other crystal structure; the bromide salt is commercial, CAS 59159-39-6.

**Generic: tert-butyl group disorder.**
- I found **no quantitative survey** of tert-butyl or tert-butyl ester disorder frequency.
- Frey, Khan & Knobler on thermal motion of tert-butyl groups (*Acta Cryst.* B, 2010) analyses ADPs and libration, not disorder frequency **[citation details not verified]**: [record](https://cris.biu.ac.il/en/publications/thermal-motion-of-tert-butyl-groups-iii-tert-butyl-substituents-i/).
- Rotational two- or three-site disorder of tert-butyl groups appears routinely in individual reports. Within this case's own COD neighbourhood, [COD 2021460](https://www.crystallography.net/cod/2021460.html) models a two-part tert-butyl split at 0.728/0.272.

---

## Case 10: COD 2312471 ([Fe(Bn-trz)4(MeCN)2][Fe2OCl6]·2MeCN)

**Publication.** Pacholski, Durka & Buchalski, *Acta Cryst.* C80 (2024) 148–152. DOI [10.1107/S2053229624002973](https://doi.org/10.1107/S2053229624002973).
- Not open access. The abstract ([Europe PMC 38607673](https://europepmc.org/article/MED/38607673)) highlights "an interesting anion with a linear geometry of the O atom" and does not mention disorder. **I could not read the full text.**

**What the authors' CIF says:**
- No `_refine_special_details` and no `_vrf_` items. P-1, Z = 1, T = 120 K.
- `_refine_diff_density_max 1.388` and `_refine_diff_density_min -0.964`. R1 0.0795.
- Deposited disorder is only at C9A/C10A vs C9B/C10B (occupancy 0.466 minor). The FeCl3 group is ordered.
- **The bridging O1 lies on the inversion centre (½, 0, ½),** so Fe2–O1–Fe2' = 180.00° is imposed by symmetry.
  - Fe–O is 1.7349(7) Å.
  - O1 is strongly anisotropic: U11 0.094, U22 0.149, U33 0.056.
- Cl atoms are also anisotropic:
  - Cl1: U22 0.104;
  - Cl2: U11 0.120;
  - Cl3: U33 0.091.
- Angles: O–Fe–Cl 108.3°, 109.3° and 115.5°; Cl–Fe–Cl 105.5° to 111.7°.
- **Peaks.** Each of the three terminal Cl atoms has a nearby deposited peak:
  - Q1 = 1.39 e/Å³ at 0.94 Å from Cl3;
  - Q2 = 1.05 at 1.22 Å from Cl2;
  - Q4 = 0.90 at 0.83 Å from Cl1.
  - Q3 and Q5 (0.92 and 0.84) are in a benzyl ring (C15–C20).

**Other determinations of [Fe2OCl6]2- in COD.** Searches on "trichloridoferrate" and "oxido-bis[trichlorido" found 9 entries:

| COD | Fe–O–Fe | site of O | disorder modelled in anion? |
|---|---|---|---|
| [2016582](https://www.crystallography.net/cod/2016582.html) | 180° | inversion centre | none (O1 U22 0.124) |
| [2226760](https://www.crystallography.net/cod/2226760.html) | 180° | inversion centre | none |
| [2232491](https://www.crystallography.net/cod/2232491.html) | 180° | −3 site (R-3) | none |
| [7058115](https://www.crystallography.net/cod/7058115.html) | 154.5(8)° | O1 at **occupancy 0.5**, split off the inversion centre | bridging O disordered; Cl ordered |
| [2220245](https://www.crystallography.net/cod/2220245.html) | 160.6(4)° | general | none (solvent ethanol disordered) |
| [2231395](https://www.crystallography.net/cod/2231395.html) | 158.4(3)° | general | none |
| [2235024](https://www.crystallography.net/cod/2235024.html) | 142.7(2)° and 160.8(2)° | general | none |
| [2242171](https://www.crystallography.net/cod/2242171.html) | 150.3(1)° | general (asymmetric Fe–O–FeCl3) | only CHCl3 solvent Cl disordered |

- **None of these COD entries models rotational disorder of the terminal FeCl3 chlorines.** One (7058115) models the bridging O as disordered off the inversion centre.
- Papers on the linear anions say the linear geometry is imposed by site symmetry:
  - 2232491 ([PMC3246982](https://pmc.ncbi.nlm.nih.gov/articles/PMC3246982/)): "Fe and O atoms in special positions … that force the Fe—O—Fe angle to be linear and the anion to adopt a staggered conformation".
  - 2226760 ([PMC3006938](https://pmc.ncbi.nlm.nih.gov/articles/PMC3006938/)) gives Fe–O 1.7545 Å against a "CSD average of 1.758 Å for similar anions". This figure comes from a search summary; I saw the "1.758 Å … reported in the CSD" fragment in the PMC text.
- A 1998 benzyltrimethylammonium salt reportedly has both "angular" and "linear" [Fe2OCl6]2- conformers in one crystal ([UAB portal record](https://portalrecerca.uab.cat/en/publications/crystal-and-molecular-structure-of-bzlmesub3subnsub2subsupsupfesu/)). This is **from a search summary and not verified [uncertain]**.
- **I found no paper that quantifies how often terminal Cl disorder occurs in [Fe2OCl6]2-.**

---

## Things I could not do

- I could not read full texts on journals.iucr.org (HTTP 403), Wiley, Elsevier or ACS. This affects the papers for cases 02, 03, 07/09, 08/11 and 10, and the Nd/Er analogue papers.
- I had no CSD or ICSD searches, so CSD-only determinations, including the Ag44/Au12Ag32 cluster structures, are unchecked.
- The COD CIFs contain no checkCIF responses. The original IUCr supplementary CIFs may hold more; for example, IUCr CIFs sometimes keep `_vrf_` blocks that COD strips **[uncertain whether COD strips them]**.
