# Case 14

Two models of the same crystal and the same data. `deposited` is the published model; `candidate` adds disorder that the published model does not have. Open each `.res` in Olex2; each has a matching `.hkl` beside it.

| | deposited | candidate |
|---|---|---|
| R1 | 0.0386 | 0.0353 |
| wR2 | 0.1041 | 0.0961 |
| GooF | 1.04 | 0.96 |
| parameters | 162 | 167 |
| largest Fo−Fc peak (e/Å³) | 0.59 | 0.33 |
| deepest hole (e/Å³) | -0.67 | -0.42 |

**Hamilton R-test** (on wR2, an approximation; the candidate extends the deposited model, so the models are nested):
5 extra parameters, R ratio 1.0834, p = 6.4e-91.

**Candidate atoms with no counterpart in the published disorder.** ρ is the Fo−Fc density at the atom position in the *deposited* model's difference map (map rms 0.058 e/Å³):

| atom | el | PART | occ | Ueq | ρ (e/Å³) | ρ/rms | nearest deposited atom (Å) |
|---|---|---|---|---|---|---|---|
| Cl1 | CL | 1 | 0.938 | 0.0639 | 0.11 | 1.9 | CL1 0.02 |
| Cl91 | CL | 2 | 0.062 | 0.0471 | 0.28 | 4.8 | CL1 0.61 |

Things to check: whether the deposited residual density at these positions is chemically sensible, whether the split geometry is reasonable, whether the ADPs of both parts look physical, and whether the density could be an artefact (absorption, series termination near heavy atoms, twinning).
