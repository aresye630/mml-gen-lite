#!/usr/bin/env python3
"""用 det_check 的归一化口径比对两棵产物树。用法: norm_cmp2.py <A> <B>"""
import difflib
import json
import sys
from pathlib import Path

sys.path.insert(0, '/opt/expgv/scripts')
import det_check as D


def norm(raw, name):
    txt = raw.decode('utf-8', 'replace')
    if name in D.NONDET_PATHS:
        try:
            obj = json.loads(txt)
        except Exception:
            return txt
        keys = D.NONDET_PATHS[name]

        def scrub(n):
            if isinstance(n, dict):
                return {k: ('<NONDET>' if k in keys else scrub(v))
                        for k, v in n.items()}
            if isinstance(n, list):
                return [scrub(x) for x in n]
            return n
        return json.dumps(scrub(obj), sort_keys=True, ensure_ascii=False)
    for rx in D.NONDET_TEXT_RE:
        txt = rx.sub('<NONDET>', txt)
    return txt


a, b = sys.argv[1], sys.argv[2]
fa, fb = Path(a), Path(b)
da = {str(p.relative_to(fa)): norm(p.read_bytes(), p.name)
      for p in fa.rglob('*') if p.is_file()}
db = {str(p.relative_to(fb)): norm(p.read_bytes(), p.name)
      for p in fb.rglob('*') if p.is_file()}
print(f'  A={a} ({len(da)} 个)')
print(f'  B={b} ({len(db)} 个)')
print(f'  仅A: {sorted(set(da) - set(db))[:5]}')
print(f'  仅B: {sorted(set(db) - set(da))[:5]}')
diff = [k for k in set(da) & set(db) if da[k] != db[k]]
print(f'  内容不同（归一化后）: {len(diff)}')
for k in diff[:2]:
    for ln in list(difflib.unified_diff(da[k].splitlines(), db[k].splitlines(),
                                        lineterm=''))[:10]:
        print('    ' + ln[:140])
print('  →', '✓ 一致' if not diff and set(da) == set(db) else '✗ 有差异')
sys.exit(0 if not diff and set(da) == set(db) else 1)
