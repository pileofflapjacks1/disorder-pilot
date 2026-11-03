# Case 06

Two models of the same crystal and the same data. `deposited` is the published model; `candidate` adds disorder that the published model does not have. Open each `.res` in Olex2; each has a matching `.hkl` beside it.

| | deposited | candidate |
|---|---|---|
| R1 | 0.0399 | 0.0380 |
| wR2 | 0.1419 | 0.1388 |
| GooF | 1.07 | 1.04 |
| parameters | 363 | 376 |
| largest Fo−Fc peak (e/Å³) | 2.89 | 1.89 |
| deepest hole (e/Å³) | -1.70 | -1.52 |

**Hamilton R-test** (on wR2, an approximation; **not nested**: the deposited model already contains other disorder, so treat this as indicative only):
13 extra parameters, R ratio 1.0221, p = 1e-114.

**Candidate atoms with no counterpart in the published disorder.** ρ is the Fo−Fc density at the atom position in the *deposited* model's difference map (map rms 0.271 e/Å³):

| atom | el | PART | occ | Ueq | ρ (e/Å³) | ρ/rms | nearest deposited atom (Å) |
|---|---|---|---|---|---|---|---|
| Ag5 | AG | 1 | 0.911 | 0.0396 | -0.03 | -0.1 | AG5 0.02 |
| Ag5B | AG | 2 | 0.089 | 0.0555 | 0.54 | 2.0 | AG5 0.54 |
| Ag6 | AG | 1 | 0.960 | 0.0416 | -0.01 | -0.0 | AG6 0.01 |
| Ag6B | AG | 2 | 0.040 | 0.0277 | 1.96 | 7.2 | AG6 0.75 |

Things to check: whether the deposited residual density at these positions is chemically sensible, whether the split geometry is reasonable, whether the ADPs of both parts look physical, and whether the density could be an artefact (absorption, series termination near heavy atoms, twinning).
