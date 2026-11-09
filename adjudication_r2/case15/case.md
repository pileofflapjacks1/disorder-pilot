# Case 15

Two models of the same crystal and the same data. `deposited` is the published model; `candidate` adds disorder that the published model does not have. Open each `.res` in Olex2; each has a matching `.hkl` beside it.

| | deposited | candidate |
|---|---|---|
| R1 | 0.0646 | 0.0606 |
| wR2 | 0.1752 | 0.1660 |
| GooF | 0.93 | 0.88 |
| parameters | 712 | 726 |
| largest Fo−Fc peak (e/Å³) | 1.34 | 0.99 |
| deepest hole (e/Å³) | -0.58 | -0.59 |

**Hamilton R-test** (on wR2, an approximation; the candidate extends the deposited model, so the models are nested):
14 extra parameters, R ratio 1.0551, p = 5e-212.

**Candidate atoms with no counterpart in the published disorder.** ρ is the Fo−Fc density at the atom position in the *deposited* model's difference map (map rms 0.128 e/Å³):

| atom | el | PART | occ | Ueq | ρ (e/Å³) | ρ/rms | nearest deposited atom (Å) |
|---|---|---|---|---|---|---|---|
| S1 | S | 1 | 0.944 | 0.0505 | 0.35 | 2.7 | S1 0.02 |
| S901 | S | 2 | 0.056 | 0.0124 | 0.86 | 6.7 | S1 0.56 |
| S2 | S | 1 | 0.904 | 0.0428 | 0.42 | 3.3 | S2 0.04 |
| S902 | S | 2 | 0.096 | 0.0160 | 0.72 | 5.6 | S2 0.43 |
| C9 | C | 1 | 0.904 | 0.0440 | 0.18 | 1.4 | C9 0.03 |
| C901 | C | 2 | 0.096 | 0.0171 | 0.06 | 0.5 | C9 0.33 |

Things to check: whether the deposited residual density at these positions is chemically sensible, whether the split geometry is reasonable, whether the ADPs of both parts look physical, and whether the density could be an artefact (absorption, series termination near heavy atoms, twinning).
