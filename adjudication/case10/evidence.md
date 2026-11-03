# Case 10: evidence sheet

*Computed checks, the same for every case. This sheet makes no judgement; it lists what to look at. Thresholds are given in each section.*

## Flags (4)

- Cl2–Fe2 +0.11 Å vs partner Cl2B
- Cl2B–Fe2 -0.11 Å vs partner Cl2
- perturbed seed 1: atoms moved up to 0.33 Å
- perturbed seed 2: atoms moved up to 0.32 Å

## Geometry of the candidate atoms
Bonds within the same part or to PART 0. Each is compared with the matching same-element bond of the atom's other-part partner (flagged above 0.10 Å), or with the covalent-radius sum when there is no partner (flagged above 0.25 Å). Contacts under 0.75× the covalent sum are flagged. Rigid-bond (Hirshfeld) differences above 0.005 Å² are flagged.

| bond | d (Å) | expected (Å) | basis | Hirshfeld ΔU (Å²) | flag |
|---|---|---|---|---|---|
| Cl1–Fe2 | 2.216 | 2.259 | partner Cl1B | 0.0039 |  |
| Cl1B–Fe2 | 2.259 | 2.216 | partner Cl1 | – |  |
| Cl2–Fe2 | 2.239 | 2.127 | partner Cl2B | 0.002 | +0.11 Å vs partner Cl2B |
| Cl2B–Fe2 | 2.127 | 2.239 | partner Cl2 | – | -0.11 Å vs partner Cl2 |
| Cl3–Fe2 | 2.202 | 2.238 | partner Cl3B | 0.0022 |  |
| Cl3B–Fe2 | 2.238 | 2.202 | partner Cl3 | – |  |

## ADPs
Flags: non-positive-definite, largest/smallest axis ratio > 5, Ueq > 0.15 or < 0.005 Å².

| atom | PART | occ | Ueq | U1/U3 |
|---|---|---|---|---|
| Cl1 | 1 | 0.896 | 0.0591 | 1.97 |
| Cl2 | 1 | 0.896 | 0.0725 | 2.78 |
| Cl3 | 1 | 0.896 | 0.0630 | 1.56 |
| Cl1B | 2 | 0.104 | 0.0342 | iso |
| Cl2B | 2 | 0.104 | 0.1006 | iso |
| Cl3B | 2 | 0.104 | 0.0502 | iso |

## Density in the deposited model's difference map
In multiples of the map rms (0.131 e/Å³). "Midpoint" is the density halfway to the nearest same-element atom of the other part. A midpoint value close to the atom value suggests smeared density (libration) rather than two discrete sites. Atoms 0.5–1.4 Å from an atom heavier than Cl sit at typical Fourier-ripple distances.

| atom | ρ/rms at atom | partner | split (Å) | ρ/rms at midpoint | heavy atom nearby |
|---|---|---|---|---|---|
| Cl1 | 3.4 | Cl1B | 0.55 | 1.7 |  |
| Cl2 | 0.7 | Cl2B | 0.96 | -0.6 |  |
| Cl3 | 0.7 | Cl3B | 0.6 | -1.0 |  |
| Cl1B | 3.1 | Cl1 | 0.55 | 1.7 |  |
| Cl2B | 7.3 | Cl2 | 0.96 | -0.6 |  |
| Cl3B | 3.5 | Cl3 | 0.6 | -1.0 |  |

## Stability
The candidate re-refined twice from start positions displaced by 0.10 Å, and once with RIGU + SIMU on the anisotropic candidate atoms. An engine failure in a run is shown as not available and is not flagged. Flagged when the minor occupancy changes by more than 0.05 or the atoms end more than 0.2 Å from their candidate positions. Baseline minor occupancy: 0.104.

| run | R1 | wR2 | minor occ | max shift (Å) | NPD |
|---|---|---|---|---|---|
| perturbed seed 1 | 0.0772 | 0.2323 | 0.152 | 0.33 | – |
| perturbed seed 2 | 0.0771 | 0.2319 | 0.149 | 0.32 | – |
| RIGU + SIMU on the anisotropic candidate atoms | 0.0747 | 0.2258 | 0.104 | 0.00 | – |
