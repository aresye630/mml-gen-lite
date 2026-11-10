"""G23 扩展：ADD 已存在对象 + 参数差异检测。

背景演进：
  2026-11-08 用户裁定：ADD 一个 EXP 里已存在的主键，几乎肯定是应该用 MOD。
    但不能自动改，只提示。
  2026-11-10 用户以 NC20260803001614 为锚点提出：
    「意图写新增 Host 约14个，实测现网 14 个名称全部已存在，
       agent 直接跳过（不新增、不改），但 GT 里有 3 条 MOD HOST
       （域名从 *.x.* 改成三层 *.x）—— 这才是本次变更的核心」

  所以 G23 要区分三种情况：
    A. 产物 ADD，EXP 已存在，参数完全一致   → 冗余（应删除该 ADD）
    B. 产物 ADD，EXP 已存在，参数有差异     → 应用 MOD
    C. 产物里完全没有，EXP 已存在，但意图要求改动 → 应补 MOD（这个是 G29 的范畴）

本文件负责 A 和 B。
"""
import re
from collections import defaultdict

# 各族的定义参数（主键）
DEFINING_PARAMS = {
    'HOST': ('HOSTNAME',),
    'FILTER': ('FILTERNAME',),
    'FILTERIPV6': ('FILTERNAME',),
    'FLOWFILTER': ('FLOWFILTERNAME',),
    'L7FILTER': ('L7FILTERNAME',),
    'POOL': ('POOLNAME',),
    'POOLGROUP': ('POOLGROUPNAME',),
    'APN': ('APN',),
    'URR': ('URRNAME',),
    'URRGROUP': ('URRGROUPNAME',),
    'RULE': ('RULENAME',),
    'USERPROFILE': ('USERPROFILENAME',),
    'PCCPOLICYGRP': ('PCCPOLICYGRPNAME',),
    'INTERFACE': ('IFNAME',),
    'NTPSVR': ('SVRNAME',),
    'SECTION': ('POOLNAME', 'SECTIONNUM'),
    'TAIRANGELIST': ('NFINSTANCENAME',),
    'UPAREABINDN2TAI': ('AREANAME', 'N2BEGINTAI'),
    'IPFARM': ('IPFARMNAME',),
    'IPFARMSERVER': ('SERVERNAME',),
    # ★ 2026-11-10：绑定类族都是复合主键
    #   实测 EXP 里 FLTBINDFLOWF 4790 条，同一个 FLOWFILTERNAME 绑多个 FILTERNAME，
    #   只用 FLOWFILTERNAME 当主键会把「不同绑定」误判成「参数有差异」
    'FLTBINDFLOWF': ('FLOWFILTERNAME', 'FILTERNAME'),
    'PROTBINDFLOWF': ('FLOWFILTERNAME', 'PROTOCOLNAME'),
    'RULEBINDING': ('USERPROFILENAME', 'RULENAME'),
    'URRGRPBINDING': ('USERPROFILENAME',),
    'POOLBINDGROUP': ('POOLGROUPNAME', 'POOLNAME'),
    'POOLGRPMAP': ('POOLGROUPNAME', 'APN'),
    'SPECURRGRPLIST': ('URRGROUPNAME',),
    'USERSELPLCY': ('POLICYNAME',),
    'USERSELATTR': ('NAME',),
}


def _parse_cmds(text):
    """解析 MML 文本 → [(line_no, verb, family, {param: value}, raw)]。"""
    out = []
    for ln, line in enumerate(text.split('\n'), 1):
        s = line.split('//')[0].strip()
        if not s or s.startswith(('/*', '#', '*')):
            continue
        s = s.rstrip(';').strip()
        m = re.match(r'^(ADD|RMV|MOD|SET)\s+([A-Za-z0-9_]+)\s*[:：]\s*(.*)$', s, re.I | re.S)
        if not m:
            continue
        verb = m.group(1).upper()
        fam = m.group(2).upper()
        params = {}
        for pm in re.finditer(r'([A-Za-z][A-Za-z0-9_]*)\s*=\s*("([^"]*)"|[^,;]+)', m.group(3)):
            k = pm.group(1).upper()
            v = pm.group(3) if pm.group(3) is not None else pm.group(2).strip()
            params[k] = v.strip()
        out.append((ln, verb, fam, params, line.strip()))
    return out


def _cmd_key(fam, params):
    """提取命令的主键值。"""
    keys = DEFINING_PARAMS.get(fam)
    if keys:
        vals = []
        for k in keys:
            if k in params:
                vals.append(params[k])
            else:
                return None
        return '|'.join(vals).upper() if vals else None
    # 未知族：用第一个参数
    if not params:
        return None
    return next(iter(params.values())).upper()


def _same_params(p1, p2):
    """两组参数是否完全一致（忽略顺序和大小写）。"""
    if set(p1.keys()) != set(p2.keys()):
        return False
    return all(str(p1[k]).strip().upper() == str(p2[k]).strip().upper()
               for k in p1)


def _diff_params(p1, p2):
    """返回参数差异 [(param, 产物值, 现网值)]。"""
    diffs = []
    for k in set(p1) | set(p2):
        v1 = str(p1.get(k, '')).strip()
        v2 = str(p2.get(k, '')).strip()
        if v1.upper() != v2.upper():
            diffs.append((k, v1, v2))
    return diffs


def check_add_existing(mml_text, exp_text, max_report=10):
    """G23：检测 ADD 了 EXP 里已存在的对象。

    Returns {
      ok: bool,
      n_conflict: int,
      n_identical: int,      # 参数完全一致的冗余 ADD
      n_diff: int,           # 参数有差异（应用 MOD 却用了 ADD）
      conflicts: [...],
      diffs: [{family, key, line, exp_line, changes}],
      note: str,
    }
    """
    if not mml_text or not exp_text:
        return {'ok': True, 'skipped': True, 'reason': '缺 mml 或 EXP'}

    # 1) 建 EXP 索引：族 → {主键值: (line, params)}
    exp_defs = defaultdict(dict)
    for ln, v, f, params, raw in _parse_cmds(exp_text):
        if v != 'ADD' or not params:
            continue
        key = _cmd_key(f, params)
        if key:
            exp_defs[f].setdefault(key, (ln, params))

    if not exp_defs:
        return {'ok': True, 'skipped': True, 'reason': 'EXP 无 ADD 定义'}

    # 2) 扫产物
    conflicts = []      # 参数完全一致（冗余）
    diffs = []          # 参数有差异（该用 MOD）

    for ln, v, f, params, raw in _parse_cmds(mml_text):
        if v != 'ADD':
            continue
        key = _cmd_key(f, params)
        if not key or key not in exp_defs.get(f, {}):
            continue
        exp_ln, exp_params = exp_defs[f][key]

        if _same_params(params, exp_params):
            conflicts.append({
                'family': f, 'key': key, 'line': ln, 'exp_line': exp_ln,
            })
        else:
            ch = _diff_params(params, exp_params)
            diffs.append({
                'family': f, 'key': key, 'line': ln, 'exp_line': exp_ln,
                'changes': ch[:5],
                'n_changes': len(ch),
            })

    ok = not conflicts and not diffs
    result = {
        'ok': ok,
        'skipped': False,
        'n_conflict': len(conflicts),
        'n_identical': len(conflicts),
        'n_diff': len(diffs),
        'conflicts': conflicts[:max_report],
        'diffs': diffs[:max_report],
    }

    if conflicts or diffs:
        parts = []
        if diffs:
            parts.append(
                f'{len(diffs)} 条 ADD 的是 EXP 已存在但**参数有差异**的对象，'
                f'应该用 MOD')
        if conflicts:
            parts.append(
                f'{len(conflicts)} 条 ADD 的对象在 EXP 里完全一致，属冗余')
        result['note'] = '；'.join(parts)

    return result


# ─────────────── 兼容旧接口 ───────────────
def _iter_exp(text):
    for ln, v, f, params, raw in _parse_cmds(text):
        yield ln, v, f, params


def _first_param_value(s):
    m = re.search(r'=\s*("([^"]*)"|[^,;]+)', s)
    if not m:
        return None
    return m.group(2) if m.group(2) is not None else m.group(1).strip()


if __name__ == '__main__':
    import json
    import sys
    mml = open(sys.argv[1], encoding='utf-8').read() if len(sys.argv) > 1 else ''
    exp = open(sys.argv[2], encoding='utf-8').read() if len(sys.argv) > 2 else ''
    print(json.dumps(check_add_existing(mml, exp), ensure_ascii=False, indent=1))
