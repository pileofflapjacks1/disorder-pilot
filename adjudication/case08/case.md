# Case 08

Two models of the same crystal and the same data. `deposited` is the published model; `candidate` adds disorder that the published model does not have. Open each `.res` in Olex2; each has a matching `.hkl` beside it.

| | deposited | candidate |
|---|---|---|
| R1 | 0.0393 | 0.0287 |
| wR2 | 0.1053 | 0.0788 |
| GooF | 1.05 | 0.78 |
| parameters | 537 | 562 |
| largest Fo−Fc peak (e/Å³) | 1.69 | 1.28 |
| deepest hole (e/Å³) | -0.73 | -0.46 |

**Hamilton R-test** (on wR2, an approximation; the candidate extends the deposited model, so the models are nested):
25 extra parameters, R ratio 1.3353, p = 0.

**Candidate atoms with no counterpart in the published disorder.** ρ is the Fo−Fc density at the atom position in the *deposited* model's difference map (map rms 0.065 e/Å³):

| atom | el | PART | occ | Ueq | ρ (e/Å³) | ρ/rms | nearest deposited atom (Å) |
|---|---|---|---|---|---|---|---|
| O1 | O | 1 | 0.811 | 0.0249 | 0.10 | 1.5 | O1 0.06 |
| O901 | O | 2 | 0.189 | 0.0249 | 0.44 | 6.9 | O1 0.61 |
| O2 | O | 1 | 0.811 | 0.0388 | 0.23 | 3.6 | O2 0.05 |
| O902 | O | 2 | 0.189 | 0.0298 | 1.18 | 18.2 | O2 0.87 |
| C20 | C | 1 | 0.811 | 0.0268 | 0.01 | 0.1 | C20 0.05 |
| C901 | C | 2 | 0.189 | 0.0104 | 0.03 | 0.4 | C20 0.18 |
| C21 | C | 1 | 0.811 | 0.0312 | 0.12 | 1.9 | C21 0.02 |
| C902 | C | 2 | 0.189 | 0.0261 | 0.90 | 13.9 | C21 0.83 |
| C23 | C | 1 | 0.811 | 0.0465 | -0.04 | -0.7 | C23 0.03 |
| C903 | C | 2 | 0.189 | 0.0445 | 1.12 | 17.3 | H21 0.13 |
| C24 | C | 1 | 0.811 | 0.0394 | -0.17 | -2.6 | C24 0.01 |
| C904 | C | 2 | 0.189 | 0.0511 | 0.31 | 4.8 | C21 0.72 |

Things to check: whether the deposited residual density at these positions is chemically sensible, whether the split geometry is reasonable, whether the ADPs of both parts look physical, and whether the density could be an artefact (absorption, series termination near heavy atoms, twinning).
