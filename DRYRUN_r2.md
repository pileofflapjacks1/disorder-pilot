# Round 2: harness dry run and B vs B2 (exploratory, no API cost)

*2026-11-12. Neither part is preregistered or changes the protocol. No model was called, and nothing was written to `tasks/<id>/C`, so C still counts as not run.*

## 1. Dry run of C's harness (`tools/dryrun_c_tools.py`, `dryrun_r2.jsonl`)

On each of the 84 round-2 tasks (80 sample and 4 dev), the frozen `xtal_mcp.py` server was set up exactly as `run_c.py` sets it up. A do-nothing agent was then scripted through every tool:
- `status`, `atoms`, `peaks`;
- `near` at the top peak;
- `show`, then `set` with the unchanged model;
- `refine`, `undo`, `submit`.

The submission was scored with the frozen scorer and compared with A.

**Results:**
- **82/84 tasks pass.** All 9 tools respond, nothing is rejected, and the unchanged submission scores the same as A: the same detections, the same false-positive flag, and R1 within 0.0005.
- **2 tasks fail: 2240538 and 2241940.** These are the two unscoreable tasks the amendment drops. Every tool that refines fails on them, including `submit`, so an agent couldn't even submit. Dropping them is the right call.
- **Three tasks are slow enough to matter. All are discrete and all are in the sample:**

  | Task | Position in sample | One `refine` | Initial `status` | Whole dry run |
  |---|---|---|---|---|
  | 2241451 | 1 | 13 min | 12 min | 37 min |
  | 2242115 | 2 | 15 min | 31 min | 57 min |
  | 2243396 | 14 | 15 min | 36 min | 59 min |

  - `run_c.py` gives the agent 1 hour in total. On these tasks, an agent can afford about 2–3 refinements before the timeout, and then it is scored on its last model.
  - This is the frozen behaviour. A timeout is not an infrastructure failure under the preregistration, so it is not rerun.
  - The pilot's longest C run was 28 minutes.
  - Two of these tasks fall within n = 10, and all three within n = 15. Expect C to be handicapped on them. B and B2 had no time limit.
  - **For the amendment:** worth recording, before any C run, that this was known. My suggestion is to disclose it and change nothing; any timeout change would alter a frozen file.
- **Everywhere else the harness is fast:** a median of 17 s for the whole sequence, and 285 s at the 90th percentile.
- **Not covered:** the `claude` CLI and its MCP client, since they would need the model. The dev smoke test is still needed for that.

## 2. Why B beats B2 on fresh tasks

The comparison is site by site, on the 66 disordered sites after the amendment's drops; a crash counts as not detected.

| | B2 detected | B2 missed |
|---|---|---|
| **B detected** | 17 | **11** |
| **B missed** | **6** | 32 |

**Where only B found the site (11).** In all 11, B2 tried a cluster containing B's atoms, but rejected the split:
- **9 failed the Ueq gate:**
  - in 5, at least one minor atom refined to Ueq 0.0001, B2's lower bound;
  - in 4 more, the only failure was a minor atom with Ueq between 0.28 and 1.0 Å², more than 6× the median.
- **1 had non-positive-definite ADPs (2312304).** B2's larger 10-atom cluster went NPD, while B's 6-atom split refined fine.
- **1 was below the occupancy floor (2312505):** minor occupancy 0.057.

B's accepted splits on these sites look sensible:
- **10 of 11 pass the plausibility check.** The exception is 2241451, where C80 fails it.
- **Median occupancy error 0.05.**

So B2's gates throw away real detections. The ADPs go bad in B2's own trial refinement, which runs without ADP restraints on the minor part, and that happens more often on fresh tasks than the calibration on deposited models suggested.

**Where only B2 found the site (6).**
- In 5, B accepted splits of only 1–2 atoms that B2 also split. Those covered under 50% of the minor atoms, so the site isn't counted as detected.
- In 1 (2243234), B's larger cluster crashed the engine (the riding-H bug), and its 1-atom fallback wasn't enough.

B2's wider peak window and extra tries are what pay off here.

**Reading.** B2's fixes help on their own: the wider window, more tries, and no riding-H crash. Its v2 gates then cost more than those fixes gain, so on these tasks B2's net effect against B is negative. This is post hoc and changes nothing; B is the comparator under the preregistered rule. If there is ever a round 3, the lesson is to calibrate gates on the *system's own* trial refinements of known-real minor parts, not on deposited models read as published.
