# Round 2, staging step 2: baseline-only results (A, B, B2)

*2026-11-08. Laptop only, no API spend. C has not run, so there is no decision here. Everything was run with the frozen files in `PREREGISTRATION_round2.md`; no system or scorer was changed. Produced by `tools/run_r2_baselines.sh` and `tools/aggregate_r2.py ROOT n` (`results_r2_n{10,15,20}.json`). The run log is `r2_baselines.log`.*

## Detection on the disordered sample (n = 20 per type)

| System | group_small | group_large | discrete | All disordered | Plausible | Disordered FP structures | Control FP | Median ΔR1 |
|---|---|---|---|---|---|---|---|---|
| A | 0/26 | 0/20 | 0/20 | 0/66 | 0 | 1 (artefact, below) | 0/20 | +0.008 |
| **B** | 15/26 | 4/20 | 9/19 | **28/65 (0.43)** | 26 | 19/57 | 5/20 | +0.002 |
| B2 v2 | 10/26 | 7/19 | 6/20 | 23/65 (0.35) | 21 | 16/57 | 3/20 | +0.004 |

The best baseline is **B** at every n, which is the rate the GO rule compares C against:

| n per type | B | B2 | B control FP | B2 control FP | GO needs C ≥ |
|---|---|---|---|---|---|
| 10 | 14/31 (0.45) | 11/31 (0.35) | 3/10 | 3/10 | 0.60 |
| 15 | 22/49 (0.45) | 17/49 (0.35) | 4/15 | 3/15 | 0.60 |
| 20 | 28/65 (0.43) | 23/65 (0.35) | 5/20 | 3/20 | 0.58 |

Dev tasks (smoke test only): B detects 1 of the 3 disordered sites and has 1 false positive. B2 and A detect nothing and have no false positives.

## What this says

1. **B2 did not turn out to be the stronger baseline on fresh tasks.**
   - On the pilot tasks, B2 was tuned on them and led B by 11/36 to 9/36.
   - On round 2 it trails B by 0.08 (23/65 against 28/65), and most of the gap is in group_small.
   - B2's tuning on the pilot did not carry over. The preregistration anticipated this: the GO rule compares C with whichever baseline is higher.
2. **The baselines do much better here than in the pilot:** B scores 0.43 here and scored 0.25 on the pilot.
   - Round-2 tasks look easier for rules. With the 0.15 margin, C now needs a detection rate of about 0.58–0.60, slightly above its pilot rate of 0.56.
   - This changes the expected payoff of spending on C. The pilot power estimate (0.68–0.93) assumed a gap of about 0.25 and is now optimistic.
3. **The baselines alone have a high control false-positive count:** B 25% and B2 15%, against C's 20% bar.
   - Every control false positive from either baseline lowers R1, by between −0.0027 and −0.0042.
   - This points to disorder the depositors didn't model, or to a definition that catches small R1 gains. Either reading favours [D2] option a, adjudicated, but that is your call.

## Failures (reported, not fixed)

| Task | Type | What failed | Effect |
|---|---|---|---|
| 2240538 | group_large | A's refined model has a solvent C with U11 = 28. Every re-refinement of it fails (free-variable IndexError). | Unscoreable for A, B and B2. C would start from the same model. |
| 2241940 | discrete | Refining A's model again fails Cholesky (singular normal matrix). | Unscoreable for A, B and B2. Same for C. |
| 2243293 | discrete | B: the known riding-H `ArgumentError` (RESULTS_B.md), this time on the base model. | Missing for B only. |
| 2242911 | group_large | B2 accepted a split whose minor C16 has non-physical ADPs (U11 = 4.2). The scorer can't parse the output. | Missing for B2 only. |

- `aggregate_r2.py` drops a missing task from that system's rate, so B and B2 are each rated on 57 tasks with 65 sites. The two tasks that fail for every system are excluded for all of them.
- Counting each one-system failure as zero detections instead gives B 28/66 and B2 23/66. B stays the best baseline either way.
- **Before C runs,** the amendment should say how the two unscoreable tasks and any C crash are handled. My suggestion is to drop 2240538 and 2241940 for all systems, and to count a crash as zero detections for the system that crashed.

## Protocol deviations

- **A had not run on 3 controls** (2312869, 2312967, 2313070). They had a reference refinement but no A output, so B had no input model, which contradicts the preregistration's statement that A had run on every pool task. I ran the frozen `run_ref_A.py` on them, then B and B2. None of the three has a false positive from any system.
- **Sanity check "A has 0 false positives" fails at n = 20.**
  - It fails on 2312146, a group_small task. The major-part atom S4 keeps its fixed partial occupancy from the input, but drifts about 0.3 Å during refinement. That is more than `score.py`'s 0.1 Å tolerance for "already partial in the input", so it's flagged.
  - This is a scorer artefact. It is also the only atom in B2's false positive on that task; B's false positive there flags 10 other atoms as well.
  - The check passes at n = 10 and n = 15.

## Next (protocol step 3): adjudication

As preregistered, B2's false positives with ΔR1 < 0 go to blinded adjudication. There are 7:
- controls 2241546, 2242356 and 2242750;
- group_large 2243063 and 2241666;
- discrete 2240666 and 2241657.

Since B, not B2, is now the best baseline, B's 11 R1-lowering false positives are adjudicated as well, as an extension recorded in the pre-C amendment. That's 5 controls, two of them not in B2's list (2241198 and 2241613), and 6 disordered tasks.

*Correction:* an earlier version of this section said 6 and 10. Rounding to 4 decimals had hidden two cases with ΔR1 just below zero: 2241657 (B2, −0.00001) and 2243543 (B, −0.00004). The rule is ΔR1 < 0, so both are included. In effect their R1 is unchanged.

The packs are in `adjudication_r2/`, built by `tools/adjudicate_r2.py` as 18 shuffled cases.
