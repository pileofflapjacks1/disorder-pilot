# Case 17: evidence sheet

*Computed checks, the same for every case. This sheet makes no judgement; it lists what to look at. Thresholds are given in each section.*

## Flags (1)

- C904–C903 +0.28 Å vs covalent sum

## Geometry of the candidate atoms
Bonds within the same part or to PART 0. Each is compared with the matching same-element bond of the atom's other-part partner (flagged above 0.10 Å), or with the covalent-radius sum when there is no partner (flagged above 0.25 Å). Contacts under 0.75× the covalent sum are flagged. Rigid-bond (Hirshfeld) differences above 0.005 Å² are flagged.

| bond | d (Å) | expected (Å) | basis | Hirshfeld ΔU (Å²) | flag |
|---|---|---|---|---|---|
| C904–O901 | 1.590 | 1.43 | covalent sum | – |  |
| C904–C903 | 1.817 | 1.54 | covalent sum | – | +0.28 Å vs covalent sum |

## ADPs
Flags: non-positive-definite, largest/smallest axis ratio > 5, Ueq > 0.15 or < 0.005 Å².

| atom | PART | occ | Ueq | U1/U3 |
|---|---|---|---|---|
| Cl1 | 1 | 0.827 | 0.0620 | 3.48 |
| Cl91 | 2 | 0.173 | 0.0450 | iso |
| C904 | 2 | 0.353 | 0.1009 | iso |

## Density in the deposited model's difference map
In multiples of the map rms (0.093 e/Å³). "Midpoint" is the density halfway to the nearest same-element atom of the other part. A midpoint value close to the atom value suggests smeared density (libration) rather than two discrete sites. Atoms 0.5–1.4 Å from an atom heavier than Cl sit at typical Fourier-ripple distances.

| atom | ρ/rms at atom | partner | split (Å) | ρ/rms at midpoint | heavy atom nearby |
|---|---|---|---|---|---|
| Cl1 | 1.0 | Cl91 | 0.68 | -10.1 |  |
| Cl91 | 6.8 | Cl1 | 0.68 | -10.1 |  |
| C904 | 4.3 | – | – | – |  |

## Stability
The candidate re-refined twice from start positions displaced by 0.10 Å, and once with RIGU + SIMU on the anisotropic candidate atoms. An engine failure in a run is shown as not available and is not flagged. Flagged when the minor occupancy changes by more than 0.05 or the atoms end more than 0.2 Å from their candidate positions. Baseline minor occupancy: 0.173.

| run | R1 | wR2 | minor occ | max shift (Å) | NPD |
|---|---|---|---|---|---|
| perturbed seed 1 | 0.0484 | 0.1241 | 0.174 | 0.04 | – |
| perturbed seed 2 | 0.0485 | 0.1242 | 0.174 | 0.05 | – |
| RIGU + SIMU on the anisotropic candidate atoms | not available (not run: fewer than two candidate atoms are anisotropic) |||||
