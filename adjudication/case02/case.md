# Case 02

Two models of the same crystal and the same data. `deposited` is the published model; `candidate` adds disorder that the published model does not have. Open each `.res` in Olex2; each has a matching `.hkl` beside it.

| | deposited | candidate |
|---|---|---|
| R1 | 0.0695 | 0.0537 |
| wR2 | 0.2066 | 0.1814 |
| GooF | 1.13 | 1.00 |
| parameters | 62 | 69 |
| largest Fo−Fc peak (e/Å³) | 11.59 | 6.52 |
| deepest hole (e/Å³) | -3.56 | -3.32 |

**Hamilton R-test** (on wR2, an approximation; the candidate extends the deposited model, so the models are nested):
7 extra parameters, R ratio 1.1388, p = 2.7e-56.

**Candidate atoms with no counterpart in the published disorder.** ρ is the Fo−Fc density at the atom position in the *deposited* model's difference map (map rms 0.629 e/Å³):

| atom | el | PART | occ | Ueq | ρ (e/Å³) | ρ/rms | nearest deposited atom (Å) |
|---|---|---|---|---|---|---|---|
| Au3 | AU | 0 | 0.041 | 0.0310 | 10.53 | 16.7 | CL1 1.21 |
| Au4 | AU | 0 | 0.041 | 0.0327 | 10.34 | 16.4 | AU2 1.21 |

Things to check: whether the deposited residual density at these positions is chemically sensible, whether the split geometry is reasonable, whether the ADPs of both parts look physical, and whether the density could be an artefact (absorption, series termination near heavy atoms, twinning).
