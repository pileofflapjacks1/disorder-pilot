"""Run run_ref_A.py over a queue, 4 at a time, with a per-task wall-time cap.

run_queue.py ROOT QUEUE LOG [CAP_SECONDS]   a task over the cap is killed and logged as "ERROR Timeout", which
select.py treats as ineligible (the pilot's Amendment 2 rule, with the cap set before the run).
"""
import sys, subprocess, os
from concurrent.futures import ThreadPoolExecutor

root, queue, log = sys.argv[1], sys.argv[2], sys.argv[3]
cap = int(sys.argv[4]) if len(sys.argv) > 4 else 3600
here = os.path.dirname(os.path.abspath(__file__))
ids = [l.strip() for l in open(queue) if l.strip()]


def run(i):
    try:
        out = subprocess.run([sys.executable, here + '/run_ref_A.py', root, i], capture_output=True, text=True, timeout=cap).stdout
    except subprocess.TimeoutExpired:
        out = '%s ERROR Timeout: reference + A did not finish in %d s\n' % (i, cap)
    with open(log, 'a') as f: f.write(out)
    return i


with ThreadPoolExecutor(4) as ex:
    for k, _ in enumerate(ex.map(run, ids), 1):
        if k % 10 == 0: print('%d/%d done' % (k, len(ids)), flush=True)
print('all %d done' % len(ids))
