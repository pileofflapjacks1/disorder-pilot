# Case 03

Two models of the same crystal and the same data. `deposited` is the published model; `candidate` adds disorder that the published model does not have. Open each `.res` in Olex2; each has a matching `.hkl` beside it.

| | deposited | candidate |
|---|---|---|
| R1 | 0.0179 | 0.0164 |
| wR2 | 0.0430 | 0.0390 |
| GooF | 1.12 | 1.02 |
| parameters | 83 | 86 |
| largest Fo−Fc peak (e/Å³) | 3.59 | 1.82 |
| deepest hole (e/Å³) | -1.53 | -1.31 |

**Hamilton R-test** (on wR2, an approximation; the candidate extends the deposited model, so the models are nested):
3 extra parameters, R ratio 1.1020, p = 2.3e-65.

**Candidate atoms with no counterpart in the published disorder.** ρ is the Fo−Fc density at the atom position in the *deposited* model's difference map (map rms 0.338 e/Å³):

| atom | el | PART | occ | Ueq | ρ (e/Å³) | ρ/rms | nearest deposited atom (Å) |
|---|---|---|---|---|---|---|---|
| Se1 | SE | 1 | 0.478 | 0.0099 | -0.20 | -0.6 | SE1 0.0 |
| Se1B | SE | 2 | 0.022 | 0.0068 | 3.44 | 10.2 | H2 1.45 |

Things to check: whether the deposited residual density at these positions is chemically sensible, whether the split geometry is reasonable, whether the ADPs of both parts look physical, and whether the density could be an artefact (absorption, series termination near heavy atoms, twinning).
