"""G25：配套族缺失检测。

用户裁定（2026-11-09）：prompt 说了要查 exp_siblings，但 agent 实测调用 0 次。
靠 prompt 约束不可靠，改成判据强制。

判据逻辑：
  1. 扫产物里的每个族，用 exp_siblings 查它的配套族
  2. 如果配套族（confidence=high）一个都没出现在产物里 → 报 warn
  3. 列出「该配但没配」的具体族名

背景实测（4 轮全量，34 个族完备 40-99% 的工单）：
  缺失族 TOP：
    ADD FILTERIPV6      8 个工单  ← exp_siblings(ADD FILTER) 能查出
    ADD USERPROFILE     8 个工单  ← exp_siblings(ADD URR) 能查出
    SET URRGRPBINDING   7 个工单  ← exp_siblings(ADD URR) 能查出
    ADD RULEBINDING     6 个工单  ← exp_siblings(ADD RULE) 能查出
    ADD FLTBINDFLOWF    6 个工单  ← exp_siblings(ADD FILTER) 能查出

  实测 NC20260831000131：exp_siblings 调用 0 次（53 次 EXP 全是查明细）
"""
import re
from pathlib import Path

# 只关心 ADD 类的配套关系（SET/MOD 属性族由同名前缀判据覆盖）
ADD_RE = re.compile(r'^ADD\s+([A-Za-z0-9_]+)\s*[:：]', re.I)

# 配套族很少的族不必强制（避免噪音）
MIN_FAMILY_COUNT = 2


def _parse_prod_families(mml_text):
    """产物里出现的族（不带动词）。"""
    fams = set()
    for line in mml_text.split('\n'):
        s = line.split('//')[0].strip()
        m = ADD_RE.match(s)
        if m:
            fams.add(m.group(1).upper())
    return fams


def _parse_all_families(mml_text):
    """产物里出现的所有族（含 SET/MOD/RMV，带动词）。"""
    out = set()
    for line in mml_text.split('\n'):
        s = line.split('//')[0].strip()
        m = re.match(r'^(ADD|RMV|MOD|SET)\s+([A-Za-z0-9_]+)', s, re.I)
        if m:
            out.add(f'{m.group(1).upper()} {m.group(2).upper()}')
            out.add(m.group(2).upper())
    return out


def check_sibling_missing(mml_text, exp_text, session_dir=None, max_report=8):
    """G25：检测「有配套族但没配」。

    Returns {
      ok, skipped, n_checked, missing: [{family, siblings: [...]}]
    }
    """
    if not mml_text or not exp_text:
        return {'ok': True, 'skipped': True, 'reason': '缺 mml 或 EXP'}

    try:
        import sys
        _here = str(Path(__file__).resolve().parent)
        if _here not in sys.path:
            sys.path.insert(0, _here)
        _mcp = str(Path(__file__).resolve().parent.parent / 'mcp')
        if _mcp not in sys.path:
            sys.path.insert(0, _mcp)
        import mcp_exp as E
    except Exception as e:
        return {'ok': True, 'skipped': True, 'reason': f'导入 mcp_exp 失败: {e}'}

    prod_fams = _parse_prod_families(mml_text)
    prod_all = _parse_all_families(mml_text)
    if not prod_fams:
        return {'ok': True, 'skipped': True, 'reason': '产物无 ADD 命令'}

    # 找 EXP 路径（从会话目录的 uploads 里）
    exp_path = None
    if session_dir:
        d = Path(session_dir)
        for pat in ('uploads_text/EXPMML*.md', 'uploads/EXPMML*.txt',
                    'uploads_text/*.md'):
            hits = sorted(d.glob(pat))
            if hits:
                exp_path = hits[0]
                break
    if not exp_path or not exp_path.exists():
        return {'ok': True, 'skipped': True, 'reason': '找不到 EXP 文件'}

    # 只查产物里出现次数够的族（避免给太冷门的族报警）
    targets = sorted(prod_fams)[:20]

    missing = []
    n_checked = 0
    for fam in targets:
        try:
            r = E.tool_exp_siblings({'path': str(exp_path), 'families': [f'ADD {fam}']})
            info = (r.get('families') or {}).get(fam) or {}
            sibs = info.get('siblings') or []
            if not sibs:
                continue
            n_checked += 1
            # 只看 high 置信度的配套族
            high = [s for s in sibs if s.get('confidence') == 'high']
            if not high:
                continue
            # 哪些配套族产物里完全没有
            absent = [s['family'] for s in high
                      if s['family'].upper() not in prod_all]
            if absent:
                missing.append({
                    'family': fam,
                    'count': info.get('count'),
                    'siblings': absent[:6],
                })
        except Exception:
            continue
        if len(missing) >= max_report:
            break

    return {
        'ok': not missing,
        'skipped': False,
        'n_checked': n_checked,
        'n_missing': len(missing),
        'missing': missing[:max_report],
        'note': ('这些族在现网里有配套族（exp_siblings 判据），'
                 '但产物里一个都没配。如果是有意不配，请写进方案澄清说明原因。'),
    }
