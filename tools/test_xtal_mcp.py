"""Regression test for the xtal MCP server's undo (pilot bug: undo after set -> refine left the edit in place).

test_xtal_mcp.py ROOT   replays task 2312879's set -> refine -> undo through the JSON-RPC server and checks that
undo returns the starting model; also checks set -> undo and undo with nothing to undo.
"""
import sys, os, json, shutil, subprocess, tempfile

root = sys.argv[1]
task = root + '/tasks/2312879'
edit = json.load(open(task + '/C/history.json'))[1]          # the split model the agent `set` in the pilot


def server(state):
    env = dict(os.environ, XTAL_STATE=state)
    return subprocess.Popen([sys.executable, root + '/tools/xtal_mcp.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                            stderr=subprocess.DEVNULL, text=True, env=env)


def call(p, k, name, args=None):
    p.stdin.write(json.dumps(dict(jsonrpc='2.0', id=k, method='tools/call', params=dict(name=name, arguments=args or {}))) + '\n')
    p.stdin.flush()
    return json.loads(p.stdout.readline())['result']['content'][0]['text']


def fresh():
    d = tempfile.mkdtemp(prefix='xtal_test_')
    shutil.copy(task + '/input/model_refined.res', d + '/model.res'); shutil.copy(task + '/input/data.hkl', d + '/data.hkl')
    return d


def current(d): return json.load(open(d + '/history.json'))[-1]


fails = 0
def check(name, ok, detail=''):
    global fails; fails += not ok
    print('%s  %s %s' % ('PASS' if ok else 'FAIL', name, detail))


# 1. the pilot's failing sequence
d = fresh(); start = open(d + '/model.res').read(); p = server(d)
r_set = call(p, 1, 'set', {'res': edit}); r_ref = call(p, 2, 'refine'); r_undo = call(p, 3, 'undo')
check('set -> refine -> undo returns the starting model', current(d) == start, '| ' + r_undo)
check('replies name the current version', 'now version' in r_set and 'now version' in r_ref and 'now version' in r_undo)
check('nothing left to undo', call(p, 4, 'undo').startswith('nothing to undo'))
p.terminate(); shutil.rmtree(d)

# 2. set -> undo without a refine
d = fresh(); start = open(d + '/model.res').read(); p = server(d)
call(p, 1, 'set', {'res': edit}); call(p, 2, 'undo')
check('set -> undo returns the starting model', current(d) == start)
p.terminate(); shutil.rmtree(d)

# 3. two edits: undo removes only the last one
d = fresh(); p = server(d)
call(p, 1, 'set', {'res': edit}); after_first = current(d); call(p, 2, 'refine'); refined_first = current(d)
call(p, 3, 'set', {'res': edit}); call(p, 4, 'refine'); call(p, 5, 'undo')
check('second undo target is the refined first edit', current(d) == refined_first and refined_first != after_first)
p.terminate(); shutil.rmtree(d)

print('%d failure(s)' % fails); sys.exit(1 if fails else 0)
