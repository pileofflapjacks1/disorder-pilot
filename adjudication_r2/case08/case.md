# Case 08

Two models of the same crystal and the same data. `deposited` is the published model; `candidate` adds disorder that the published model does not have. Open each `.res` in Olex2; each has a matching `.hkl` beside it.

| | deposited | candidate |
|---|---|---|
| R1 | 0.0236 | 0.0236 |
| wR2 | 0.0644 | 0.0660 |
| GooF | 1.09 | 1.12 |
| parameters | 154 | 148 |
| largest Fo−Fc peak (e/Å³) | 0.40 | 0.41 |
| deepest hole (e/Å³) | -0.31 | -0.28 |

**Hamilton R-test** (on wR2, an approximation; **not nested**: the deposited model already contains other disorder, so treat this as indicative only):
-6 extra parameters, R ratio 0.9765, no improvement to test.

**Candidate atoms with no counterpart in the published disorder.** ρ is the Fo−Fc density at the atom position in the *deposited* model's difference map (map rms 0.064 e/Å³):

| atom | el | PART | occ | Ueq | ρ (e/Å³) | ρ/rms | nearest deposited atom (Å) |
|---|---|---|---|---|---|---|---|
| Cl1 | CL | 1 | 0.940 | 0.0331 | -0.09 | -1.3 | CL1 0.01 |
| Cl91 | CL | 2 | 0.060 | 0.0339 | 0.01 | 0.2 | CL1 0.35 |

Things to check: whether the deposited residual density at these positions is chemically sensible, whether the split geometry is reasonable, whether the ADPs of both parts look physical, and whether the density could be an artefact (absorption, series termination near heavy atoms, twinning).
