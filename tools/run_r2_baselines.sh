#!/bin/bash
# Round-2 staging step 2 (PREREGISTRATION_round2.md): B and B2, then scoring of A, B, B2 and plausibility of B, B2.
# run_r2_baselines.sh ROOT IDS_FILE   4 tasks in parallel; one log line per task and system in r2_baselines.log
cd "$1" || exit 1
cat "$2" | xargs -P 4 -n 1 sh -c '
  for S in B B2; do [ -f tasks/$0/$S/score.json ] || env/bin/python tools/system_$(echo $S | tr A-Z a-z).py $PWD $0; done
  for S in A B B2; do [ -f tasks/$0/$S/score.json ] || env/bin/python tools/score.py $PWD $S $0; done
  for S in B B2; do [ -f tasks/$0/$S/plausible.json ] || env/bin/python tools/plausible.py $PWD $S $0; done' >> r2_baselines.log 2>&1
echo done
