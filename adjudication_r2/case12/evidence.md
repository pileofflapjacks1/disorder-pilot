# Case 12: evidence sheet

*Computed checks, the same for every case. This sheet makes no judgement; it lists what to look at. Thresholds are given in each section.*

## Flags (4)

- O2–P1 rigid-bond test 0.0078
- P1–O1 rigid-bond test 0.0053
- P1–O2 rigid-bond test 0.0078
- P901 Ueq 0.566

## Geometry of the candidate atoms
Bonds within the same part or to PART 0. Each is compared with the matching same-element bond of the atom's other-part partner (flagged above 0.10 Å), or with the covalent-radius sum when there is no partner (flagged above 0.25 Å). Contacts under 0.75× the covalent sum are flagged. Rigid-bond (Hirshfeld) differences above 0.005 Å² are flagged.

| bond | d (Å) | expected (Å) | basis | Hirshfeld ΔU (Å²) | flag |
|---|---|---|---|---|---|
| O2–P1 | 1.510 | 1.525 | partner O901 | 0.0078 | rigid-bond test 0.0078 |
| O3–P1 | 1.502 | 1.516 | partner O902 | 0.0048 |  |
| O901–P901 | 1.525 | 1.51 | partner O2 | – |  |
| O902–P901 | 1.516 | 1.502 | partner O3 | – |  |
| P1–O1 | 1.562 | 1.522 | partner P901 | 0.0053 | rigid-bond test 0.0053 |
| P1–O2 | 1.510 | 1.522 | partner P901 | 0.0078 | rigid-bond test 0.0078 |
| P1–O3 | 1.502 | 1.522 | partner P901 | 0.0048 |  |
| P1–O4 | 1.498 | 1.522 | partner P901 | 0.0012 |  |
| P901–O1 | 1.599 | 1.506 | partner P1 | – |  |
| P901–O901 | 1.525 | 1.506 | partner P1 | – |  |
| P901–O902 | 1.516 | 1.506 | partner P1 | – |  |
| P901–O4 | 1.520 | 1.506 | partner P1 | – |  |

## ADPs
Flags: non-positive-definite, largest/smallest axis ratio > 5, Ueq > 0.15 or < 0.005 Å².

| atom | PART | occ | Ueq | U1/U3 |
|---|---|---|---|---|
| O2 | 1 | 0.944 | 0.0487 | 4.26 |
| O901 | 2 | 0.056 | 0.0318 | iso |
| O3 | 1 | 0.944 | 0.0438 | 2.07 |
| O902 | 2 | 0.056 | 0.0116 | iso |
| P1 | 1 | 0.944 | 0.0221 | 2.21 |
| P901 | 2 | 0.056 | 0.5659 | iso |

## Density in the deposited model's difference map
In multiples of the map rms (0.096 e/Å³). "Midpoint" is the density halfway to the nearest same-element atom of the other part. A midpoint value close to the atom value suggests smeared density (libration) rather than two discrete sites. Atoms 0.5–1.4 Å from an atom heavier than Cl sit at typical Fourier-ripple distances.

| atom | ρ/rms at atom | partner | split (Å) | ρ/rms at midpoint | heavy atom nearby |
|---|---|---|---|---|---|
| O2 | 1.6 | O901 | 0.72 | -1.6 |  |
| O901 | 3.0 | O2 | 0.72 | -1.6 |  |
| O3 | 1.6 | O902 | 0.69 | -0.8 |  |
| O902 | 3.6 | O3 | 0.69 | -0.8 |  |
| P1 | 0.9 | P901 | 0.21 | 1.0 |  |
| P901 | 0.8 | P1 | 0.21 | 1.0 |  |

## Stability
The candidate re-refined twice from start positions displaced by 0.10 Å, and once with RIGU + SIMU on the anisotropic candidate atoms. An engine failure in a run is shown as not available and is not flagged. Flagged when the minor occupancy changes by more than 0.05 or the atoms end more than 0.2 Å from their candidate positions. Baseline minor occupancy: 0.056.

| run | R1 | wR2 | minor occ | max shift (Å) | NPD |
|---|---|---|---|---|---|
| perturbed seed 1 | 0.0476 | 0.1133 | 0.055 | 0.04 | – |
| perturbed seed 2 | 0.0476 | 0.1133 | 0.055 | 0.04 | – |
| RIGU + SIMU on the anisotropic candidate atoms | 0.0474 | 0.1127 | 0.057 | 0.01 | – |
