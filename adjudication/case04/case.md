# Case 04

Two models of the same crystal and the same data. `deposited` is the published model; `candidate` adds disorder that the published model does not have. Open each `.res` in Olex2; each has a matching `.hkl` beside it.

| | deposited | candidate |
|---|---|---|
| R1 | 0.0670 | 0.0667 |
| wR2 | 0.1963 | 0.1980 |
| GooF | 1.03 | 1.04 |
| parameters | 202 | 177 |
| largest Fo−Fc peak (e/Å³) | 0.49 | 0.49 |
| deepest hole (e/Å³) | -0.48 | -0.47 |

**Hamilton R-test** (on wR2, an approximation; **not nested**: the deposited model already contains other disorder, so treat this as indicative only):
-25 extra parameters, R ratio 0.9913, no improvement to test.

**Candidate atoms with no counterpart in the published disorder.** ρ is the Fo−Fc density at the atom position in the *deposited* model's difference map (map rms 0.092 e/Å³):

| atom | el | PART | occ | Ueq | ρ (e/Å³) | ρ/rms | nearest deposited atom (Å) |
|---|---|---|---|---|---|---|---|
| O2 | O | 1 | 0.861 | 0.1132 | -0.06 | -0.6 | O2 0.03 |
| O902 | O | 2 | 0.139 | 0.1098 | 0.35 | 3.8 | O2 1.04 |

Things to check: whether the deposited residual density at these positions is chemically sensible, whether the split geometry is reasonable, whether the ADPs of both parts look physical, and whether the density could be an artefact (absorption, series termination near heavy atoms, twinning).
