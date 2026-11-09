# Case 09

Two models of the same crystal and the same data. `deposited` is the published model; `candidate` adds disorder that the published model does not have. Open each `.res` in Olex2; each has a matching `.hkl` beside it.

| | deposited | candidate |
|---|---|---|
| R1 | 0.0500 | 0.0481 |
| wR2 | 0.1274 | 0.1232 |
| GooF | 1.06 | 1.02 |
| parameters | 650 | 611 |
| largest Fo−Fc peak (e/Å³) | 1.27 | 0.66 |
| deepest hole (e/Å³) | -1.50 | -1.32 |

**Hamilton R-test** (on wR2, an approximation; **not nested**: the deposited model already contains other disorder, so treat this as indicative only):
-39 extra parameters, R ratio 1.0343, no improvement to test.

**Candidate atoms with no counterpart in the published disorder.** ρ is the Fo−Fc density at the atom position in the *deposited* model's difference map (map rms 0.093 e/Å³):

| atom | el | PART | occ | Ueq | ρ (e/Å³) | ρ/rms | nearest deposited atom (Å) |
|---|---|---|---|---|---|---|---|
| Cl1 | CL | 1 | 0.830 | 0.0622 | 0.09 | 1.0 | CL1 0.08 |
| Cl91 | CL | 2 | 0.170 | 0.0444 | 0.64 | 6.9 | CL1 0.6 |

Things to check: whether the deposited residual density at these positions is chemically sensible, whether the split geometry is reasonable, whether the ADPs of both parts look physical, and whether the density could be an artefact (absorption, series termination near heavy atoms, twinning).
