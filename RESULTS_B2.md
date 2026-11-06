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
2. **Most of the lost detections were not physical models.** B2 lost 5 sites that B detected, one in each of 5 structures.
   - **Four were implausible:** 2243634, 2243977, 2243801 and 2243569. B's accepted split had impossible minor-part ADPs (Ueq up to 1.0, or 0.0001 Å²), more than 25% of its bonds off from the partner geometry, or both. Two of these, 2243801 and 2243569, are adjudication cases 04 and 05, which the expert judged overfit.
   - **One was a narrow loss:** 2243827. Its geometry was fine (13% of bonds flagged), but the minor occupancy was 0.07, below the 0.08 floor, and one minor Ueq was just above 3× the median.
   - **One went the other way:** in 2312714, B2 found a site B missed.
3. **The only remaining control false positive is 2312969.** It is the ester group the expert scored "pretty much even" (adjudication case 08), and the strongest candidate for disorder missing from the deposited model.
4. **A SIMU restraint on the minor part (option `MINOR_U='simu'`) did not rescue the rejected splits.** Their ADPs became more reasonable, but their geometry still failed (0.53 and 0.40 of bonds flagged). The default stays at no ADP restraint, as in B.

## What this means for round 2

- **The detection metric rewards implausible models.** A site counts as detected when its atoms are in the right places, even if their ADPs are impossible. B's pilot score includes such credit, and C's may too; C was not checked.
- B2 is a **stricter** baseline, not one that detects more. It has lower detection than B, so against B2 the preregistered GO threshold (C − B ≥ 0.15) would be *easier* to meet. That cuts against the point of a stronger baseline. Options for the preregistration (Joe's decision):
  1. Report both B and B2, and apply the GO rule against the higher of the two detection rates.
  2. Add a co-primary **plausible detection** metric, a detected site whose split also passes B2's gates, and apply it to every system, including C. This would also make C's numbers comparable on plausibility.
- **Cost:** B2 averages about 3.6 min per structure on the laptop, including scoring. There is no API cost.
