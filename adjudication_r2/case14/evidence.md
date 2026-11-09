# Case 14: evidence sheet

*Computed checks, the same for every case. This sheet makes no judgement; it lists what to look at. Thresholds are given in each section.*

## Flags (0)

- none

## Geometry of the candidate atoms
Bonds within the same part or to PART 0. Each is compared with the matching same-element bond of the atom's other-part partner (flagged above 0.10 Å), or with the covalent-radius sum when there is no partner (flagged above 0.25 Å). Contacts under 0.75× the covalent sum are flagged. Rigid-bond (Hirshfeld) differences above 0.005 Å² are flagged.

| bond | d (Å) | expected (Å) | basis | Hirshfeld ΔU (Å²) | flag |
|---|---|---|---|---|---|
| Cl1–C2 | 1.733 | 1.696 | partner Cl91 | 0.0011 |  |
| Cl91–C2 | 1.696 | 1.733 | partner Cl1 | – |  |

## ADPs
Flags: non-positive-definite, largest/smallest axis ratio > 5, Ueq > 0.15 or < 0.005 Å².

| atom | PART | occ | Ueq | U1/U3 |
|---|---|---|---|---|
| Cl1 | 1 | 0.938 | 0.0639 | 3.38 |
| Cl91 | 2 | 0.062 | 0.0471 | iso |

## Density in the deposited model's difference map
In multiples of the map rms (0.058 e/Å³). "Midpoint" is the density halfway to the nearest same-element atom of the other part. A midpoint value close to the atom value suggests smeared density (libration) rather than two discrete sites. Atoms 0.5–1.4 Å from an atom heavier than Cl sit at typical Fourier-ripple distances.

| atom | ρ/rms at atom | partner | split (Å) | ρ/rms at midpoint | heavy atom nearby |
|---|---|---|---|---|---|
| Cl1 | 1.9 | Cl91 | 0.63 | -4.2 |  |
| Cl91 | 4.8 | Cl1 | 0.63 | -4.2 |  |

## Stability
The candidate re-refined twice from start positions displaced by 0.10 Å, and once with RIGU + SIMU on the anisotropic candidate atoms. An engine failure in a run is shown as not available and is not flagged. Flagged when the minor occupancy changes by more than 0.05 or the atoms end more than 0.2 Å from their candidate positions. Baseline minor occupancy: 0.062.

| run | R1 | wR2 | minor occ | max shift (Å) | NPD |
|---|---|---|---|---|---|
| perturbed seed 1 | 0.0353 | 0.0962 | 0.062 | 0.01 | – |
| perturbed seed 2 | 0.0353 | 0.0962 | 0.061 | 0.02 | – |
| RIGU + SIMU on the anisotropic candidate atoms | not available (not run: fewer than two candidate atoms are anisotropic) |||||
