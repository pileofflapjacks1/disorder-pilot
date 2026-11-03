# Case 01: evidence sheet

*Computed checks, the same for every case. This sheet makes no judgement; it lists what to look at. Thresholds are given in each section.*

## Flags (5)

- C26A–C24 +0.11 Å vs partner C26B
- C26A–C27A rigid-bond test 0.0191
- C26B–C24 -0.14 Å vs partner C26A
- C26B–C27B rigid-bond test 0.0085
- C27B–C26B rigid-bond test 0.0085

## Geometry of the candidate atoms
Bonds within the same part or to PART 0. Each is compared with the matching same-element bond of the atom's other-part partner (flagged above 0.10 Å), or with the covalent-radius sum when there is no partner (flagged above 0.25 Å). Contacts under 0.75× the covalent sum are flagged. Rigid-bond (Hirshfeld) differences above 0.005 Å² are flagged.

| bond | d (Å) | expected (Å) | basis | Hirshfeld ΔU (Å²) | flag |
|---|---|---|---|---|---|
| C26A–C24 | 1.562 | 1.448 | partner C26B | 0.0131 | +0.11 Å vs partner C26B |
| C26A–C27A | 1.528 | 1.448 | partner C26B | 0.0191 | rigid-bond test 0.0191 |
| C26B–C24 | 1.408 | 1.545 | partner C26A | 0.0036 | -0.14 Å vs partner C26A |
| C26B–C27B | 1.488 | 1.545 | partner C26A | 0.0085 | rigid-bond test 0.0085 |
| C27B–C26B | 1.488 | 1.545 | partner C26A | 0.0085 | rigid-bond test 0.0085 |

## ADPs
Flags: non-positive-definite, largest/smallest axis ratio > 5, Ueq > 0.15 or < 0.005 Å².

| atom | PART | occ | Ueq | U1/U3 |
|---|---|---|---|---|
| C26A | 1 | 0.704 | 0.0528 | 1.65 |
| C26B | 2 | 0.296 | 0.0590 | 1.33 |
| C27B | 2 | 0.296 | 0.0726 | 1.31 |

## Density in the deposited model's difference map
In multiples of the map rms (0.085 e/Å³). "Midpoint" is the density halfway to the nearest same-element atom of the other part. A midpoint value close to the atom value suggests smeared density (libration) rather than two discrete sites. Atoms 0.5–1.4 Å from an atom heavier than Cl sit at typical Fourier-ripple distances.

| atom | ρ/rms at atom | partner | split (Å) | ρ/rms at midpoint | heavy atom nearby |
|---|---|---|---|---|---|
| C26A | 3.1 | C26B | 0.6 | -0.7 |  |
| C26B | 2.6 | C26A | 0.6 | -0.7 |  |
| C27B | 16.7 | C26A | 1.05 | 1.3 |  |

## Stability
The candidate re-refined twice from start positions displaced by 0.10 Å, and once with RIGU + SIMU on the anisotropic candidate atoms. An engine failure in a run is shown as not available and is not flagged. Flagged when the minor occupancy changes by more than 0.05 or the atoms end more than 0.2 Å from their candidate positions. Baseline minor occupancy: 0.296.

| run | R1 | wR2 | minor occ | max shift (Å) | NPD |
|---|---|---|---|---|---|
| perturbed seed 1 | 0.0608 | 0.1850 | 0.296 | 0.00 | – |
| perturbed seed 2 | 0.0608 | 0.1851 | 0.296 | 0.00 | – |
| RIGU + SIMU on the anisotropic candidate atoms | 0.0607 | 0.1849 | 0.291 | 0.00 | – |
