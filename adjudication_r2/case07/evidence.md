# Case 07: evidence sheet

*Computed checks, the same for every case. This sheet makes no judgement; it lists what to look at. Thresholds are given in each section.*

## Flags (7)

- C33–C32 rigid-bond test 0.0117
- C33–C34 rigid-bond test 0.0246
- C33–C37 rigid-bond test 0.0205
- C34–C33 rigid-bond test 0.0246
- C37–C33 rigid-bond test 0.0205
- C907–C35 +0.22 Å vs partner C34
- C906 Ueq 0.0001 (very small)

## Geometry of the candidate atoms
Bonds within the same part or to PART 0. Each is compared with the matching same-element bond of the atom's other-part partner (flagged above 0.10 Å), or with the covalent-radius sum when there is no partner (flagged above 0.25 Å). Contacts under 0.75× the covalent sum are flagged. Rigid-bond (Hirshfeld) differences above 0.005 Å² are flagged.

| bond | d (Å) | expected (Å) | basis | Hirshfeld ΔU (Å²) | flag |
|---|---|---|---|---|---|
| C33–C32 | 1.533 | 1.56 | partner C906 | 0.0117 | rigid-bond test 0.0117 |
| C33–C34 | 1.512 | 1.56 | partner C906 | 0.0246 | rigid-bond test 0.0246 |
| C33–C37 | 1.520 | 1.56 | partner C906 | 0.0205 | rigid-bond test 0.0205 |
| C33–O4 | 1.435 | 1.357 | partner C906 | 0.0003 |  |
| C34–C33 | 1.512 | 1.611 | partner C907 | 0.0246 | rigid-bond test 0.0246 |
| C34–C35 | 1.528 | 1.611 | partner C907 | 0.0011 |  |
| C37–C33 | 1.520 | 1.56 | partner C908 | 0.0205 | rigid-bond test 0.0205 |
| C906–C32 | 1.566 | 1.52 | partner C33 | – |  |
| C906–C907 | 1.476 | 1.52 | partner C33 | – |  |
| C906–C908 | 1.560 | 1.52 | partner C33 | – |  |
| C906–O4 | 1.357 | 1.435 | partner C33 | – |  |
| C907–C906 | 1.476 | 1.52 | partner C34 | – |  |
| C907–C35 | 1.745 | 1.52 | partner C34 | – | +0.22 Å vs partner C34 |
| C908–C906 | 1.560 | 1.52 | partner C37 | – |  |

## ADPs
Flags: non-positive-definite, largest/smallest axis ratio > 5, Ueq > 0.15 or < 0.005 Å².

| atom | PART | occ | Ueq | U1/U3 |
|---|---|---|---|---|
| C33 | 1 | 0.828 | 0.0439 | 2.59 |
| C906 | 2 | 0.172 | 0.0001 | iso |
| C34 | 1 | 0.828 | 0.0371 | 3.77 |
| C907 | 2 | 0.172 | 0.0512 | iso |
| C37 | 1 | 0.828 | 0.0346 | 2.74 |
| C908 | 2 | 0.172 | 0.0247 | iso |

## Density in the deposited model's difference map
In multiples of the map rms (0.076 e/Å³). "Midpoint" is the density halfway to the nearest same-element atom of the other part. A midpoint value close to the atom value suggests smeared density (libration) rather than two discrete sites. Atoms 0.5–1.4 Å from an atom heavier than Cl sit at typical Fourier-ripple distances.

| atom | ρ/rms at atom | partner | split (Å) | ρ/rms at midpoint | heavy atom nearby |
|---|---|---|---|---|---|
| C33 | -0.5 | C906 | 0.18 | -0.1 |  |
| C906 | 0.3 | C33 | 0.18 | -0.1 |  |
| C34 | 0.7 | C907 | 1.34 | -1.2 |  |
| C907 | 6.6 | C34 | 1.34 | -1.2 |  |
| C37 | 1.9 | C908 | 1.17 | -2.3 |  |
| C908 | 9.4 | C37 | 1.17 | -2.3 |  |

## Stability
The candidate re-refined twice from start positions displaced by 0.10 Å, and once with RIGU + SIMU on the anisotropic candidate atoms. An engine failure in a run is shown as not available and is not flagged. Flagged when the minor occupancy changes by more than 0.05 or the atoms end more than 0.2 Å from their candidate positions. Baseline minor occupancy: 0.172.

| run | R1 | wR2 | minor occ | max shift (Å) | NPD |
|---|---|---|---|---|---|
| perturbed seed 1 | 0.0480 | 0.1249 | 0.173 | 0.06 | – |
| perturbed seed 2 | 0.0480 | 0.1249 | 0.173 | 0.06 | – |
| RIGU + SIMU on the anisotropic candidate atoms | 0.0479 | 0.1248 | 0.172 | 0.13 | – |
