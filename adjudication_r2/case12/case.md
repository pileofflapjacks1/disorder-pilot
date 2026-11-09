# Case 12

Two models of the same crystal and the same data. `deposited` is the published model; `candidate` adds disorder that the published model does not have. Open each `.res` in Olex2; each has a matching `.hkl` beside it.

| | deposited | candidate |
|---|---|---|
| R1 | 0.0515 | 0.0474 |
| wR2 | 0.1194 | 0.1127 |
| GooF | 1.16 | 1.08 |
| parameters | 241 | 254 |
| largest Fo−Fc peak (e/Å³) | 0.61 | 0.43 |
| deepest hole (e/Å³) | -0.60 | -0.53 |

**Hamilton R-test** (on wR2, an approximation; the candidate extends the deposited model, so the models are nested):
13 extra parameters, R ratio 1.0593, p = 5.1e-56.

**Candidate atoms with no counterpart in the published disorder.** ρ is the Fo−Fc density at the atom position in the *deposited* model's difference map (map rms 0.096 e/Å³):

| atom | el | PART | occ | Ueq | ρ (e/Å³) | ρ/rms | nearest deposited atom (Å) |
|---|---|---|---|---|---|---|---|
| O2 | O | 1 | 0.944 | 0.0487 | 0.16 | 1.6 | O2 0.02 |
| O901 | O | 2 | 0.056 | 0.0318 | 0.29 | 3.0 | O2 0.7 |
| O3 | O | 1 | 0.944 | 0.0438 | 0.16 | 1.6 | O3 0.02 |
| O902 | O | 2 | 0.056 | 0.0115 | 0.35 | 3.6 | O3 0.67 |
| P1 | P | 1 | 0.944 | 0.0221 | 0.08 | 0.9 | P1 0.0 |
| P901 | P | 2 | 0.056 | 0.5658 | 0.08 | 0.8 | P1 0.21 |

Things to check: whether the deposited residual density at these positions is chemically sensible, whether the split geometry is reasonable, whether the ADPs of both parts look physical, and whether the density could be an artefact (absorption, series termination near heavy atoms, twinning).
