# Case 18

Two models of the same crystal and the same data. `deposited` is the published model; `candidate` adds disorder that the published model does not have. Open each `.res` in Olex2; each has a matching `.hkl` beside it.

| | deposited | candidate |
|---|---|---|
| R1 | 0.0646 | 0.0606 |
| wR2 | 0.1752 | 0.1659 |
| GooF | 0.93 | 0.88 |
| parameters | 712 | 726 |
| largest Fo−Fc peak (e/Å³) | 1.34 | 0.99 |
| deepest hole (e/Å³) | -0.58 | -0.59 |

**Hamilton R-test** (on wR2, an approximation; the candidate extends the deposited model, so the models are nested):
14 extra parameters, R ratio 1.0556, p = 5.8e-214.

**Candidate atoms with no counterpart in the published disorder.** ρ is the Fo−Fc density at the atom position in the *deposited* model's difference map (map rms 0.128 e/Å³):

| atom | el | PART | occ | Ueq | ρ (e/Å³) | ρ/rms | nearest deposited atom (Å) |
|---|---|---|---|---|---|---|---|
| S1 | S | 1 | 0.944 | 0.0505 | 0.35 | 2.7 | S1 0.02 |
| S901 | S | 2 | 0.056 | 0.0124 | 0.86 | 6.7 | S1 0.56 |
| S2 | S | 1 | 0.920 | 0.0429 | 0.42 | 3.3 | S2 0.03 |
| S902 | S | 2 | 0.080 | 0.0121 | 0.79 | 6.2 | S2 0.46 |
| C9 | C | 1 | 0.920 | 0.0429 | 0.18 | 1.4 | C9 0.03 |
| C901 | C | 2 | 0.080 | 0.0221 | 0.04 | 0.3 | C9 0.39 |

Things to check: whether the deposited residual density at these positions is chemically sensible, whether the split geometry is reasonable, whether the ADPs of both parts look physical, and whether the density could be an artefact (absorption, series termination near heavy atoms, twinning).
