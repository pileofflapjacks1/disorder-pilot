# Case 07

Two models of the same crystal and the same data. `deposited` is the published model; `candidate` adds disorder that the published model does not have. Open each `.res` in Olex2; each has a matching `.hkl` beside it.

| | deposited | candidate |
|---|---|---|
| R1 | 0.0573 | 0.0565 |
| wR2 | 0.1326 | 0.1307 |
| GooF | 1.03 | 1.01 |
| parameters | 615 | 560 |
| largest Fo−Fc peak (e/Å³) | 1.34 | 1.76 |
| deepest hole (e/Å³) | -1.39 | -1.55 |

**Hamilton R-test** (on wR2, an approximation; **not nested**: the deposited model already contains other disorder, so treat this as indicative only):
-55 extra parameters, R ratio 1.0143, no improvement to test.

**Candidate atoms with no counterpart in the published disorder.** ρ is the Fo−Fc density at the atom position in the *deposited* model's difference map (map rms 0.192 e/Å³):

| atom | el | PART | occ | Ueq | ρ (e/Å³) | ρ/rms | nearest deposited atom (Å) |
|---|---|---|---|---|---|---|---|
| C903 | C | 2 | 0.246 | 0.1459 | -0.22 | -1.1 | C46 0.07 |

Things to check: whether the deposited residual density at these positions is chemically sensible, whether the split geometry is reasonable, whether the ADPs of both parts look physical, and whether the density could be an artefact (absorption, series termination near heavy atoms, twinning).
