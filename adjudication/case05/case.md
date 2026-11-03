# Case 05

Two models of the same crystal and the same data. `deposited` is the published model; `candidate` adds disorder that the published model does not have. Open each `.res` in Olex2; each has a matching `.hkl` beside it.

| | deposited | candidate |
|---|---|---|
| R1 | 0.0450 | 0.0381 |
| wR2 | 0.1186 | 0.1009 |
| GooF | 1.10 | 0.93 |
| parameters | 501 | 486 |
| largest Fo−Fc peak (e/Å³) | 0.99 | 0.96 |
| deepest hole (e/Å³) | -0.99 | -0.97 |

**Hamilton R-test** (on wR2, an approximation; **not nested**: the deposited model already contains other disorder, so treat this as indicative only):
-15 extra parameters, R ratio 1.1751, no improvement to test.

**Candidate atoms with no counterpart in the published disorder.** ρ is the Fo−Fc density at the atom position in the *deposited* model's difference map (map rms 0.088 e/Å³):

| atom | el | PART | occ | Ueq | ρ (e/Å³) | ρ/rms | nearest deposited atom (Å) |
|---|---|---|---|---|---|---|---|
| Cl91 | CL | 2 | 0.369 | 0.9443 | -0.30 | -3.3 | CL5 0.65 |

Things to check: whether the deposited residual density at these positions is chemically sensible, whether the split geometry is reasonable, whether the ADPs of both parts look physical, and whether the density could be an artefact (absorption, series termination near heavy atoms, twinning).
