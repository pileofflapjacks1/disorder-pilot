# Case 04: evidence sheet

*Computed checks, the same for every case. This sheet makes no judgement; it lists what to look at. Thresholds are given in each section.*

## Flags (0)

- none

## Geometry of the candidate atoms
Bonds within the same part or to PART 0. Each is compared with the matching same-element bond of the atom's other-part partner (flagged above 0.10 Å), or with the covalent-radius sum when there is no partner (flagged above 0.25 Å). Contacts under 0.75× the covalent sum are flagged. Rigid-bond (Hirshfeld) differences above 0.005 Å² are flagged.

| bond | d (Å) | expected (Å) | basis | Hirshfeld ΔU (Å²) | flag |
|---|---|---|---|---|---|
| O2–C6 | 1.264 | 1.335 | partner O902 | 0.0025 |  |
| O902–C6 | 1.335 | 1.264 | partner O2 | – |  |

## ADPs
Flags: non-positive-definite, largest/smallest axis ratio > 5, Ueq > 0.15 or < 0.005 Å².

| atom | PART | occ | Ueq | U1/U3 |
|---|---|---|---|---|
| O2 | 1 | 0.861 | 0.1132 | 3.93 |
| O902 | 2 | 0.139 | 0.1098 | iso |

## Density in the deposited model's difference map
In multiples of the map rms (0.092 e/Å³). "Midpoint" is the density halfway to the nearest same-element atom of the other part. A midpoint value close to the atom value suggests smeared density (libration) rather than two discrete sites. Atoms 0.5–1.4 Å from an atom heavier than Cl sit at typical Fourier-ripple distances.

| atom | ρ/rms at atom | partner | split (Å) | ρ/rms at midpoint | heavy atom nearby |
|---|---|---|---|---|---|
| O2 | -0.6 | O902 | 1.07 | -1.8 |  |
| O902 | 3.8 | O2 | 1.07 | -1.8 |  |

## Stability
The candidate re-refined twice from start positions displaced by 0.10 Å, and once with RIGU + SIMU on the anisotropic candidate atoms. An engine failure in a run is shown as not available and is not flagged. Flagged when the minor occupancy changes by more than 0.05 or the atoms end more than 0.2 Å from their candidate positions. Baseline minor occupancy: 0.139.

| run | R1 | wR2 | minor occ | max shift (Å) | NPD |
|---|---|---|---|---|---|
| perturbed seed 1 | 0.0667 | 0.1980 | 0.137 | 0.03 | – |
| perturbed seed 2 | 0.0667 | 0.1980 | 0.138 | 0.03 | – |
| RIGU + SIMU on the anisotropic candidate atoms | not available (not run: fewer than two candidate atoms are anisotropic) |||||
