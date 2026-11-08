"""新增判据 G23：ADD 已存在对象检测。

背景（2026-11-08 用户裁定）：
  配置生成场景下，ADD 一个 EXP 里已存在的主键，几乎肯定是应该用 MOD。
  但不能自动改（用户可能故意覆盖），要：
    · 判据里提示（warn，不阻断）
    · 在 mml 对应行加注释，让用户明确知道 agent 是「明知已存在还 ADD」

检测方式：
  对每条 ADD 命令，提取主键值，查 EXP 里该族是否已有同主键定义。
"""
import re
from collections import defaultdict


def check_add_existing(mml_text, exp_text, max_report=10):
    """G23：检测 ADD 了 EXP 里已存在的对象。

    Returns {
      ok: bool,              # 无冲突
      n_conflict: int,
      conflicts: [{family, key, line, exp_line}],
      note: str,
    }
    """
    if not mml_text or not exp_text:
        return {'ok': True, 'skipped': True, 'reason': '缺 mml 或 EXP'}

    # 1) 建 EXP 索引：族 → {主键值}
    exp_defs = defaultdict(set)
    exp_lines = defaultdict(dict)     # 族 → {主键值: 行号}
    for ln, v, f, params in _iter_exp(exp_text):
        if v != 'ADD' or not params:
            continue
        key = next(iter(params.values()))
        if key:
            exp_defs[f].add(key.upper())
            exp_lines[f].setdefault(key.upper(), ln)

    if not exp_defs:
        return {'ok': True, 'skipped': True, 'reason': 'EXP 无 ADD 定义'}

    # 2) 扫产物的 ADD
    conflicts = []
    for ln, line in enumerate(mml_text.split('\n'), 1):
        s = line.split('//')[0].strip().rstrip(';').strip()
        m = re.match(r'^ADD\s+([A-Za-z0-9_]+)\s*[:：]\s*(.*)$', s, re.I | re.S)
        if not m:
            continue
        fam = m.group(1).upper()
        first = _first_param_value(m.group(2))
        if not first:
            continue
        fu = first.upper()
        if fu in exp_defs.get(fam, set()):
            conflicts.append({
                'family': fam,
                'key': first,
                'line': ln,
                'exp_line': exp_lines[fam].get(fu),
            })
            if len(conflicts) >= 200:
                break

    n = len(conflicts)
    return {
        'ok': n == 0,
        'n_conflict': n,
        'conflicts': conflicts[:max_report],
        'note': ('ADD 已存在对象：配置生成场景下通常应改用 MOD。'
                 '如果是有意覆盖，可忽略此提示。'),
    }


def _first_param_value(rest):
    """从参数串里取第一个参数的值。"""
    rest = rest.strip()
    cur = ''
    for ch in rest:
        if ch == ',':
            break
        cur += ch
    if '=' not in cur:
        return ''
    v = cur.split('=', 1)[1].strip()
    if len(v) >= 2 and v[0] == '"' and v[-1] == '"':
        v = v[1:-1]
    return v


def _iter_exp(exp_text):
    """解析 EXP（复用 guard 的 _iter_cmds）。"""
    import sys
    from pathlib import Path as _P
    _here = _P(__file__).resolve().parent
    if str(_here) not in sys.path:
        sys.path.insert(0, str(_here))
    import guard as G
    return G._iter_cmds(exp_text)


def annotate_mml(mml_text, conflicts):
    """在 mml 对应行加注释，说明「该对象 EXP 已存在」。

    用户裁定：不自动改成 MOD，只在产物里显式标注，让人看到 agent 的判断。
    """
    if not conflicts:
        return mml_text

    by_line = {c['line']: c for c in conflicts}
    out = []
    for ln, line in enumerate(mml_text.split('\n'), 1):
        c = by_line.get(ln)
        if c and '//' not in line.split(';')[0]:
            # 在分号后加注释
            if line.rstrip().endswith(';'):
                line = line.rstrip() + f"   // ⚠ EXP 已有 {c['family']}:{c['key']}（L{c['exp_line']}），本次用 ADD"
            else:
                line = line.rstrip() + f"   // ⚠ EXP 已有 {c['family']}:{c['key']}（L{c['exp_line']}），本次用 ADD"
        out.append(line)
    return '\n'.join(out)
