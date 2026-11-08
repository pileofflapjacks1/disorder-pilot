# Baseline B2 (round-2 candidate): results on the pilot tasks

*2026-11-06 to 2026-11-08. Tuning and development only. These are the pilot's 40 sample and 3 dev tasks, already used and published, so none of these numbers is a test result. B2 will be frozen in the round-2 preregistration and tested only on fresh tasks.*

B2 is in `tools/system_b2.py`. It is the pilot's rule-based baseline B (`tools/system_b.py`, unchanged) plus fixes for B's documented failures (`RESULTS_B.md`) and a floor of plausibility gates on every split it accepts. The full list is in the file's docstring:

- **Fourier-ripple filter:** ignores peaks within 1.3 Å of atoms heavier than Cl.
- **Peak window:** 0.4–1.6 Å. The range is CrystalPilot's idea; no code was taken.
- **Tries:** up to 5 clusters.
- **No riding H on the minor part.** This fixes B's engine crash.
- **Gates (v2, calibrated below):**
  - minor occupancy ≥ 0.05;
  - minor Ueq between 0.005 and 6× the median heavy-atom Ueq;
  - no NPD atoms;
  - minor occupancy stable within 0.10 when re-refined from a 0.5 start.

## Result (pilot sample, 10 tasks per type)

| | group_small | group_large | discrete | All disordered | Disordered FP structures | Control FP | Median ΔR1 |
|---|---|---|---|---|---|---|---|
| B | 4/11 | 3/11 | 2/14 | 9/36 (0.25) | 10/29 | 2/10 | +0.004 |
| B2 v1 (strict gates) | 2/11 | 2/11 | 1/14 | 5/36 (0.14) | 1/29 | 1/10 | +0.008 |
| **B2 v2 (calibrated)** | 5/11 | 2/11 | 4/14 | **11/36 (0.31)** | 10/29 | **1/10** | +0.006 |
| C (agent) | 8/11 | 5/11 | 7/14 | 20/36 (0.56) | 7/29 | 3/10 | +0.003 |

On the 3 dev tasks, every B2 version has no detections and one false positive (2312809, Cl), the same as B.

**Reading:**
- **B2 v2 is a modestly stronger baseline than B.** It detects 2 more sites, with the same number of false-positive disordered structures and one fewer control false positive.
- **The only remaining control false positive is 2312969.** It is the ester group the expert scored "pretty much even" (adjudication case 08), and the strongest candidate for disorder missing from the deposited model.
- **Against B2 v2, C's lead is 0.25 (9/36 sites).** Against B it was 0.31. Both are above the preregistered GO margin of 0.15, but these are pilot tasks, not a test.
- **A SIMU restraint on the minor part (option `MINOR_U='simu'`) did not help.** It was tried on v1 and rescued none of its rejected splits. The default stays at no ADP restraint, as in B.

## How the gates were calibrated

### v1 failed calibration

v1's gates were set by judgement:
- occupancy ≥ 0.08;
- Ueq up to 3× the median;
- at most 25% of the minor atoms' bonds more than 0.10 Å off the partner atom's matching bond.

These gates kept false positives low (1/29), but the low count turned out to be mostly over-strictness. The check was **plausible detection** (`tools/plausible.py`): a site counts only if it is detected and its matched minor atoms pass the gates. Its rule was written before any C result was computed.

The same check was then run on the deposited models: the experts' own published disorder, scored as system `T`, re-refined with the EADP, EXYZ and SAME restraints the engine doesn't support stripped out, as in the adjudication. **Only 12 of 38 published sites passed.** A gate that rejects two thirds of real disorder cannot measure plausibility.

A side correction: an earlier draft of this file said four of the five sites v1 lost from B came from implausible models. That draft had looked at B2's own trial splits, not B's accepted models. 7 of B's 9 detected sites pass even the v1 checks.

### v2 calibration (`tools/calibrate_gates.py`, `calibration/gates_features.json`)

**Positives:** the 65 minor parts in the deposited models, read *as published* (not re-refined), so stripped restraints cannot distort them. Only pilot tasks that can never enter round 2 were used: the sample, dev, ineligible and low-signal tasks.

**Negatives:** the 7 candidate splits the expert judged `overfit` in the blinded adjudication.

| Gate set | Deposited sites passing | Overfit splits rejected |
|---|---|---|
| v1 (occupancy 0.08, Ueq ≤ 3×, geometry ≤ 25% at 0.10 Å) | 40/65 | 4/7 (05, 06, 09, 10) |
| v2 + v1's geometry gate | 54/65 | 3/7 (05, 06, 10) |
| **v2 (occupancy 0.05, Ueq ≤ 6×, no geometry gate)** | **64/65** | **2/7** (cases 05 and 06) |

- **The geometry gate was dropped.** At its strictest it catches one more overfit split (case 10) but rejects 10 more published sites; any looser setting catches nothing extra. Almost all the overfit splits have normal-looking bond lengths.
- **v2 catches only the clearly non-physical splits:** case 05 (minor Ueq around 0.9 Å²) and case 06 (4% occupancy).
- **The other five overfit splits pass every number these rules check.** The expert's rejection of them rested on what the rules do not see: the density, the chemistry, and how the model looks overall.
- n = 7 negatives from one expert. The thresholds were chosen on this set, so their reject rate is optimistic if anything.

### Plausible detection with v2 gates (pilot sample)

| System | Detected | Detected and plausible |
|---|---|---|
| B | 9/36 | 8/36 |
| B2 v2 | 11/36 | 11/36 |
| C (agent) | 20/36 | 19/36 |
| Deposited models, re-refined (sample + dev) | 38/39 | 34/38 |

- **Almost every detection is a physically sensible model.** C's one failure is 2312993, the unstable task whose refinement does not reproduce (`RESULTS_B.md`). B's one failure is 2243569, a Cl with a non-physical ADP.
- **The deposited models' 4 failures come from re-refinement.** These sites pass when read as published (64/65), which points to the stripped restraints.

## Conclusions for round 2

1. **Use B2 v2 as the baseline,** frozen with its file hash. Report B as well, and apply the GO rule against the higher of the two detection rates.
2. **Report plausible detection as a secondary metric,** with this calibration attached. It is a floor against non-physical models, not evidence that disorder is real.
3. **Simple rules do not separate real disorder from overfit disorder,** just as R1 could not in the adjudication: 5 of 7 expert-overfit splits pass every gate. Blinded expert adjudication of R1-lowering false positives stays in the protocol.
4. **Cost:** B2 averages about 3.6 min per structure on the laptop, including scoring. There is no API cost.
