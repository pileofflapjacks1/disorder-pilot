# Case 13

Two models of the same crystal and the same data. `deposited` is the published model; `candidate` adds disorder that the published model does not have. Open each `.res` in Olex2; each has a matching `.hkl` beside it.

| | deposited | candidate |
|---|---|---|
| R1 | 0.0516 | 0.0489 |
| wR2 | 0.1410 | 0.1339 |
| GooF | 1.03 | 0.98 |
| parameters | 243 | 268 |
| largest Fo−Fc peak (e/Å³) | 0.69 | 0.70 |
| deepest hole (e/Å³) | -0.24 | -0.26 |

**Hamilton R-test** (on wR2, an approximation; the candidate extends the deposited model, so the models are nested):
25 extra parameters, R ratio 1.0527, p = 3.2e-68.

**Candidate atoms with no counterpart in the published disorder.** ρ is the Fo−Fc density at the atom position in the *deposited* model's difference map (map rms 0.056 e/Å³):

| atom | el | PART | occ | Ueq | ρ (e/Å³) | ρ/rms | nearest deposited atom (Å) |
|---|---|---|---|---|---|---|---|
| C4 | C | 1 | 0.944 | 0.0190 | 0.07 | 1.2 | C4 0.0 |
| C901 | C | 2 | 0.056 | 1.0000 | -0.05 | -0.8 | C4 1.17 |
| C5 | C | 1 | 0.944 | 0.0223 | 0.03 | 0.5 | C5 0.0 |
| C902 | C | 2 | 0.056 | 0.0309 | 0.40 | 7.0 | C4 0.85 |
| C6 | C | 1 | 0.944 | 0.0261 | 0.01 | 0.2 | C6 0.01 |
| C903 | C | 2 | 0.056 | 0.0108 | 0.38 | 6.7 | C6 0.71 |
| C7 | C | 1 | 0.944 | 0.0263 | 0.06 | 1.0 | C7 0.0 |
| C904 | C | 2 | 0.056 | 0.0813 | 0.01 | 0.2 | C7 0.36 |
| C8 | C | 1 | 0.944 | 0.0253 | 0.02 | 0.3 | C8 0.01 |
| C905 | C | 2 | 0.056 | 0.0285 | 0.15 | 2.7 | C8 0.53 |
| C9 | C | 1 | 0.944 | 0.0236 | -0.00 | -0.1 | C9 0.0 |
| C906 | C | 2 | 0.056 | 0.0245 | 0.32 | 5.7 | C4 0.72 |

Things to check: whether the deposited residual density at these positions is chemically sensible, whether the split geometry is reasonable, whether the ADPs of both parts look physical, and whether the density could be an artefact (absorption, series termination near heavy atoms, twinning).
