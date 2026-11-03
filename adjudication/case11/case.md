# Case 11

Two models of the same crystal and the same data. `deposited` is the published model; `candidate` adds disorder that the published model does not have. Open each `.res` in Olex2; each has a matching `.hkl` beside it.

| | deposited | candidate |
|---|---|---|
| R1 | 0.0393 | 0.0251 |
| wR2 | 0.1053 | 0.0687 |
| GooF | 1.05 | 0.68 |
| parameters | 537 | 565 |
| largest Fo−Fc peak (e/Å³) | 1.69 | 0.30 |
| deepest hole (e/Å³) | -0.73 | -0.34 |

**Hamilton R-test** (on wR2, an approximation; the candidate extends the deposited model, so the models are nested):
28 extra parameters, R ratio 1.5329, p = 0.

**Candidate atoms with no counterpart in the published disorder.** ρ is the Fo−Fc density at the atom position in the *deposited* model's difference map (map rms 0.065 e/Å³):

| atom | el | PART | occ | Ueq | ρ (e/Å³) | ρ/rms | nearest deposited atom (Å) |
|---|---|---|---|---|---|---|---|
| O1 | O | 1 | 0.807 | 0.0246 | 0.10 | 1.5 | O1 0.06 |
| O2 | O | 1 | 0.807 | 0.0383 | 0.24 | 3.6 | O2 0.05 |
| C21 | C | 1 | 0.807 | 0.0310 | 0.12 | 1.9 | C21 0.02 |
| C22 | C | 1 | 0.807 | 0.0423 | -0.19 | -2.9 | C22 0.0 |
| C23 | C | 1 | 0.807 | 0.0455 | -0.04 | -0.7 | C23 0.02 |
| C24 | C | 1 | 0.807 | 0.0394 | -0.16 | -2.5 | C24 0.02 |
| O1B | O | 2 | 0.193 | 0.0246 | 0.41 | 6.3 | O1 0.59 |
| O2B | O | 2 | 0.193 | 0.0317 | 1.16 | 18.0 | O2 0.87 |
| C21B | C | 2 | 0.193 | 0.0286 | 0.93 | 14.4 | C21 0.85 |
| C22B | C | 2 | 0.193 | 0.0509 | 1.16 | 18.0 | H23 1.08 |
| C23B | C | 2 | 0.193 | 0.0440 | 1.14 | 17.6 | H21 0.14 |
| C24B | C | 2 | 0.193 | 0.0486 | 0.30 | 4.7 | C21 0.71 |

Things to check: whether the deposited residual density at these positions is chemically sensible, whether the split geometry is reasonable, whether the ADPs of both parts look physical, and whether the density could be an artefact (absorption, series termination near heavy atoms, twinning).
