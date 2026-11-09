# Case 02: evidence sheet

*Computed checks, the same for every case. This sheet makes no judgement; it lists what to look at. Thresholds are given in each section.*

## Flags (3)

- Cl3–C19 +0.14 Å vs partner Cl91
- Cl91–Cl2 +0.42 Å vs covalent sum
- Cl91–C19 -0.14 Å vs partner Cl3

## Geometry of the candidate atoms
Bonds within the same part or to PART 0. Each is compared with the matching same-element bond of the atom's other-part partner (flagged above 0.10 Å), or with the covalent-radius sum when there is no partner (flagged above 0.25 Å). Contacts under 0.75× the covalent sum are flagged. Rigid-bond (Hirshfeld) differences above 0.005 Å² are flagged.

| bond | d (Å) | expected (Å) | basis | Hirshfeld ΔU (Å²) | flag |
|---|---|---|---|---|---|
| Cl1–C19 | 1.769 | 1.722 | partner Cl92 | 0.0018 |  |
| Cl3–C19 | 1.792 | 1.649 | partner Cl91 | 0.0038 | +0.14 Å vs partner Cl91 |
| Cl91–Cl2 | 2.405 | 1.98 | covalent sum | – | +0.42 Å vs covalent sum |
| Cl91–C19 | 1.649 | 1.792 | partner Cl3 | – | -0.14 Å vs partner Cl3 |
| Cl92–C19 | 1.722 | 1.769 | partner Cl1 | – |  |

## ADPs
Flags: non-positive-definite, largest/smallest axis ratio > 5, Ueq > 0.15 or < 0.005 Å².

| atom | PART | occ | Ueq | U1/U3 |
|---|---|---|---|---|
| Cl1 | 1 | 0.942 | 0.0447 | 2.94 |
| Cl92 | 2 | 0.058 | 0.0540 | iso |
| Cl3 | 1 | 0.922 | 0.0518 | 3.38 |
| Cl91 | 2 | 0.078 | 0.0536 | iso |

## Density in the deposited model's difference map
In multiples of the map rms (0.088 e/Å³). "Midpoint" is the density halfway to the nearest same-element atom of the other part. A midpoint value close to the atom value suggests smeared density (libration) rather than two discrete sites. Atoms 0.5–1.4 Å from an atom heavier than Cl sit at typical Fourier-ripple distances.

| atom | ρ/rms at atom | partner | split (Å) | ρ/rms at midpoint | heavy atom nearby |
|---|---|---|---|---|---|
| Cl1 | 3.0 | Cl92 | 0.57 | -0.7 |  |
| Cl92 | 2.0 | Cl1 | 0.57 | -0.7 |  |
| Cl3 | 2.8 | Cl91 | 0.65 | -5.0 |  |
| Cl91 | 4.2 | Cl3 | 0.65 | -5.0 |  |

## Stability
The candidate re-refined twice from start positions displaced by 0.10 Å, and once with RIGU + SIMU on the anisotropic candidate atoms. An engine failure in a run is shown as not available and is not flagged. Flagged when the minor occupancy changes by more than 0.05 or the atoms end more than 0.2 Å from their candidate positions. Baseline minor occupancy: 0.058.

| run | R1 | wR2 | minor occ | max shift (Å) | NPD |
|---|---|---|---|---|---|
| perturbed seed 1 | 0.0440 | 0.1251 | 0.052 | 0.05 | – |
| perturbed seed 2 | 0.0440 | 0.1251 | 0.052 | 0.05 | – |
| RIGU + SIMU on the anisotropic candidate atoms | 0.0438 | 0.1247 | 0.058 | 0.00 | – |
