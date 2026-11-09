# Case 18: evidence sheet

*Computed checks, the same for every case. This sheet makes no judgement; it lists what to look at. Thresholds are given in each section.*

## Flags (4)

- S1–C8 -0.23 Å vs partner S901
- S2–C8 -0.17 Å vs partner S902
- S901–C8 +0.23 Å vs partner S1
- S902–C8 +0.25 Å vs partner S2

## Geometry of the candidate atoms
Bonds within the same part or to PART 0. Each is compared with the matching same-element bond of the atom's other-part partner (flagged above 0.10 Å), or with the covalent-radius sum when there is no partner (flagged above 0.25 Å). Contacts under 0.75× the covalent sum are flagged. Rigid-bond (Hirshfeld) differences above 0.005 Å² are flagged.

| bond | d (Å) | expected (Å) | basis | Hirshfeld ΔU (Å²) | flag |
|---|---|---|---|---|---|
| C9–S2 | 1.823 | 1.773 | partner C901 | 0.0012 |  |
| C9–C10 | 1.533 | 1.502 | partner C901 | 0.002 |  |
| C901–S902 | 1.773 | 1.823 | partner C9 | – |  |
| C901–C10 | 1.502 | 1.533 | partner C9 | – |  |
| S1–C8 | 1.665 | 1.891 | partner S901 | 0.0073 | -0.23 Å vs partner S901 |
| S2–C8 | 1.723 | 1.897 | partner S902 | 0.0057 | -0.17 Å vs partner S902 |
| S2–C9 | 1.823 | 1.897 | partner S902 | 0.0012 |  |
| S901–C8 | 1.891 | 1.665 | partner S1 | – | +0.23 Å vs partner S1 |
| S902–C8 | 2.021 | 1.773 | partner S2 | – | +0.25 Å vs partner S2 |
| S902–C901 | 1.773 | 1.773 | partner S2 | – |  |

## ADPs
Flags: non-positive-definite, largest/smallest axis ratio > 5, Ueq > 0.15 or < 0.005 Å².

| atom | PART | occ | Ueq | U1/U3 |
|---|---|---|---|---|
| S1 | 1 | 0.944 | 0.0505 | 3.3 |
| S901 | 2 | 0.056 | 0.0123 | iso |
| S2 | 1 | 0.920 | 0.0429 | 2.56 |
| S902 | 2 | 0.080 | 0.0119 | iso |
| C9 | 1 | 0.920 | 0.0429 | 2.57 |
| C901 | 2 | 0.080 | 0.0220 | iso |

## Density in the deposited model's difference map
In multiples of the map rms (0.128 e/Å³). "Midpoint" is the density halfway to the nearest same-element atom of the other part. A midpoint value close to the atom value suggests smeared density (libration) rather than two discrete sites. Atoms 0.5–1.4 Å from an atom heavier than Cl sit at typical Fourier-ripple distances.

| atom | ρ/rms at atom | partner | split (Å) | ρ/rms at midpoint | heavy atom nearby |
|---|---|---|---|---|---|
| S1 | 2.7 | S901 | 0.58 | 3.3 |  |
| S901 | 6.7 | S1 | 0.58 | 3.3 |  |
| S2 | 3.3 | S902 | 0.5 | 3.6 |  |
| S902 | 6.2 | S2 | 0.5 | 3.6 |  |
| C9 | 1.4 | C901 | 0.41 | 1.1 |  |
| C901 | 0.3 | C9 | 0.41 | 1.1 |  |

## Stability
The candidate re-refined twice from start positions displaced by 0.10 Å, and once with RIGU + SIMU on the anisotropic candidate atoms. An engine failure in a run is shown as not available and is not flagged. Flagged when the minor occupancy changes by more than 0.05 or the atoms end more than 0.2 Å from their candidate positions. Baseline minor occupancy: 0.056.

| run | R1 | wR2 | minor occ | max shift (Å) | NPD |
|---|---|---|---|---|---|
| perturbed seed 1 | 0.0612 | 0.1671 | 0.1 | 0.14 | – |
| perturbed seed 2 | 0.0612 | 0.1671 | 0.098 | 0.13 | – |
| RIGU + SIMU on the anisotropic candidate atoms | 0.0606 | 0.1659 | 0.056 | 0.01 | – |
