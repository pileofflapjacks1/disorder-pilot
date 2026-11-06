# Baseline B2 (round-2 candidate): results on the pilot tasks

*2026-11-06. Tuning and development only. These are the pilot's 40 sample and 3 dev tasks, already used and published, so these numbers are not a test result. B2 will be frozen and tested only on fresh round-2 tasks.*

B2 is in `tools/system_b2.py`. It is the pilot's rule-based baseline B (`tools/system_b.py`, unchanged) plus fixes for B's documented failures (`RESULTS_B.md`) and plausibility gates on every split it accepts. The full list is in the file's docstring:

- **Fourier-ripple filter:** ignores peaks within 1.3 Å of atoms heavier than Cl.
- **Peak window:** 0.4–1.6 Å. The range is CrystalPilot's idea; no code was taken.
- **Tries:** up to 5 clusters.
- **No riding H on the minor part.** This fixes B's engine crash.
- **Acceptance gates:** bond geometry vs the partner atoms, sensible minor-part Ueq, occupancy stability from a 0.5 start, and minor occupancy ≥ 0.08.

## Result (pilot sample, 10 tasks per type)

| | group_small | group_large | discrete | All disordered | Disordered FP structures | Control FP | Median ΔR1 |
|---|---|---|---|---|---|---|---|
| B | 4/11 | 3/11 | 2/14 | **9/36 (0.25)** | 10/29 | 2/10 | +0.004 |
| **B2** | 2/11 | 2/11 | 1/14 | **5/36 (0.14)** | **1/29** | **1/10** | +0.008 |
| C (agent) | 8/11 | 5/11 | 7/14 | 20/36 (0.56) | 7/29 | 3/10 | +0.003 |

The 3 dev tasks are unchanged for B2: no detections, and one false positive (2312809, Cl), the same as B's.

## Reading

1. **B2 trades recall for precision.** False-positive structures fall from 10 to 1 among the disordered tasks and from 2 to 1 among the controls. Detection falls from 9 to 5 sites.
2. **Some of the lost detections were real.** This corrects an earlier draft, which said four of the five lost sites came from implausible models. That draft wrongly looked at B2's own trial splits rather than B's accepted models. On B's actual models, 7 of its 9 detected sites pass the plausibility checks below, so B2's lower detection is partly a real loss. One site went the other way: in 2312714, B2 found a site B missed.
3. **The only remaining control false positive is 2312969.** It is the ester group the expert scored "pretty much even" (adjudication case 08), and the strongest candidate for disorder missing from the deposited model.
4. **A SIMU restraint on the minor part (option `MINOR_U='simu'`) did not rescue the rejected splits.** Their ADPs became more reasonable, but their geometry still failed (0.53 and 0.40 of bonds flagged). The default stays at no ADP restraint, as in B.

## What this means for round 2

- **The detection metric scores positions only.** A site counts as detected when its atoms are in the right places, whatever their ADPs or geometry. The section below tests whether a plausibility check can fix that. It cannot, as defined.
- B2 is a **stricter** baseline, not one that detects more. It has lower detection than B, so against B2 the preregistered GO threshold (C − B ≥ 0.15) would be *easier* to meet. That cuts against the point of a stronger baseline. Options for the preregistration (Joe's decision):
  1. Report both B and B2, and apply the GO rule against the higher of the two detection rates.
  2. Add a co-primary **plausible detection** metric, a detected site whose split also passes B2's gates, and apply it to every system, including C. This would also make C's numbers comparable on plausibility.
- **Cost:** B2 averages about 3.6 min per structure on the laptop, including scoring. There is no API cost.

## Plausible detection: failed calibration (2026-11-06)

**The rule** is in `tools/plausible.py` and was written before it was computed for C. A detected site is *plausible* if its matched minor atoms, in the re-refined submission, pass B2's gates with B2's thresholds:
- occupancy ≥ 0.08;
- Ueq between 0.005 and 3× the median, and no NPD atoms;
- at most 25% of their bonds flagged for geometry (more than 0.10 Å off the partner's matching bond).

**The calibration** ran the same check on the deposited models, the experts' own published disorder. They were scored as system `T`, with EADP, EXYZ and SAME stripped where the engine does not support them, as the adjudication did.

| Variant (post hoc, pilot data) | Deposited sites passing | B (sample) | B2 | C |
|---|---|---|---|---|
| **As defined** | **12/38** | 7/9 | 5/5 | 11/20 |
| ADP + occupancy only | 27/38 | 8/9 | 5/5 | 15/20 |
| Geometry ≤ 0.5 + ADP | 15/38 | 8/9 | 5/5 | 12/20 |
| Geometry only (≤ 0.25) | 15/38 | 7/9 | 5/5 | 13/20 |

**Reading:**
- **As defined, the check rejects 26 of 38 published disorder sites.** It cannot serve as a measure of plausibility. No variant passes even three quarters of the deposited sites.
- **Part of the ADP failure is an artefact.** Stripping the deposited EADP and SAME restraints lets those minor atoms refine freely.
- **The same applies to B2's acceptance gates.** They would reject most published disorder, so B2's low false-positive rate is partly over-strictness, not skill.
- **Simple geometric and ADP rules do not separate real disorder from overfit disorder, just as R1 could not in the adjudication.** Judging disorder still needs expert review.

**Recommendation for round 2:**
- Keep raw detection as the primary metric, with the GO rule applied against the higher of B's and B2's detection rates.
- Report plausibility only as a descriptive, exploratory metric, with this calibration attached.
- Keep blinded expert adjudication for false positives that lower R1.
- B2's gates should be re-calibrated against deposited models before B2 is frozen. On the pilot data the ADP + occupancy variant comes closest; it passes 27 of the 38 deposited sites.
