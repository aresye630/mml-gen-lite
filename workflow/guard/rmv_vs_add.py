"""G30：规划表说要删除的族，产物却配成了 ADD（或完全没有 RMV）。

★ 2026-11-11 重写（用户批准）

原版缺陷（实测 NC20260820000552）：
  靠 BIZ_TO_FAM_HINT 里 16 个硬编码业务词把「删除 XXX」映射到族名，
  实测该工单 13 条删除项只识别出 1 条（7.7%），而且认错了族
  （「SGW-U与SGW-C侧S11接口的绑定关系」→ INTERFACE，实际是 UPBINDS11）。

  硬编码业务词表也违反「禁止硬编码」红线。

新版做法（不依赖业务词表）：
  数据源换成「命令族规划.md」——它是 agent 自己对本次变更的理解，
  列里有「动作」和「命令族」，是最可靠的意图落地形式。

  判据：
    1. 读规划表，取「动作」列含 删除/RMV 的行 → 得到 (族, 状态)
       跳过「状态=跳过」的行（agent 已声明不配）
    2. 读产物 mml，得到每个族实际用了哪些动词
    3. 比对：
       A. 规划说删，产物该族只有 ADD           → 方向反了（高危）
       B. 规划说删，产物完全没有该族            → 漏删
       C. 规划说删，产物该族有 RMV             → 正常
    4. 可选：用 intent_text 交叉验证（两处都说删才报，降低误报）

  级别：warn（不阻断）
    —— 用户决定：先只改检测，观察误报率再决定是否升 fatal。
"""
import re
from pathlib import Path

# 规划表「动作」列里表示删除的写法
RMV_ACTION_WORDS = ('删除', '移除', '去除', 'RMV', 'DEL')

# 状态列里表示「确定不配」的写法（这些行不检查）
# ★ 2026-11-11：不含「待定」
#   实测 NC20260824002020：POOL/SECTION/POOLGROUP 等在规划表里是「删除 + 待定」，
#   原先把它当跳过 → 漏报 5 族。待定说明 agent 想删但没把握，
#   产物却配成了 ADD，仍是方向反了，必须报出来。
SKIP_STATUS_WORDS = ('跳过', '不配', '不做', '取消', '不适用')


def parse_plan_rmv_rows(plan_text):
    """从规划表提取「动作=删除」的行。

    按表头定位列，不硬编码索引。支持：
      · 有「状态」列和没有「状态」列两种表结构
      · 「命令族」列是裸族名或「RMV XXX」带动词

    Returns [{biz, family, action, status}]
    """
    out = []
    if not plan_text:
        return out

    lines = plan_text.split('\n')
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line.startswith('|'):
            i += 1
            continue

        header = [c.strip() for c in line.strip().strip('|').split('|')]
        if '命令族' not in header:
            i += 1
            continue

        def col(*names):
            for n in names:
                if n in header:
                    return header.index(n)
            return None

        fam_i = col('命令族')
        act_i = col('动作', '动词', '操作')
        biz_i = col('业务对象', '数据清单表', '对象')
        st_i = col('状态')
        ncol = len(header)

        i += 1
        # 跳过分隔行
        if i < len(lines) and re.fullmatch(r'[|\s\-:]+', lines[i].strip()):
            i += 1

        while i < len(lines):
            row = lines[i].strip()
            if not row.startswith('|'):
                break
            cells = [c.strip() for c in row.strip().strip('|').split('|')]
            if len(cells) >= ncol:
                fam_cell = cells[fam_i] if fam_i is not None and fam_i < len(cells) else ''
                act = cells[act_i] if act_i is not None and act_i < len(cells) else ''
                biz = cells[biz_i] if biz_i is not None and biz_i < len(cells) else ''
                status = cells[st_i] if st_i is not None and st_i < len(cells) else ''

                # 动作判定：动作列或族名单元格里带删除词
                is_rmv = any(w in act.upper() for w in (w.upper() for w in RMV_ACTION_WORDS))
                if not is_rmv:
                    is_rmv = any(w in fam_cell.upper() for w in ('RMV', 'DEL'))

                if is_rmv:
                    # 解析族名（可能带动词）
                    for part in re.split(r'[/,、]', fam_cell):
                        t = part.strip().upper()
                        m = re.match(r'^(?:ADD|RMV|MOD|SET|DEL)\s+([A-Z][A-Z0-9_]{2,})$', t)
                        fam = m.group(1) if m else (
                            t if re.fullmatch(r'[A-Z][A-Z0-9_]{2,}', t) else None)
                        if fam:
                            out.append({'biz': biz[:40], 'family': fam,
                                        'action': act[:20], 'status': status[:20]})
            i += 1
        i += 1

    return out


def parse_prod_verbs(mml_text):
    """产物里每个族用了哪些动词：{family: set(verbs)}"""
    out = {}
    for line in mml_text.split('\n'):
        s = line.split('//')[0].strip()
        if not s or s.startswith(('/*', '#', '*')):
            continue
        m = re.match(r'^(ADD|RMV|MOD|SET)\s+([A-Za-z0-9_]+)', s, re.I)
        if m:
            out.setdefault(m.group(2).upper(), set()).add(m.group(1).upper())
    return out


def parse_prod_counts(mml_text):
    """产物里每个族每个动词多少条：{family: {verb: n}}"""
    out = {}
    for line in mml_text.split('\n'):
        s = line.split('//')[0].strip()
        if not s or s.startswith(('/*', '#', '*')):
            continue
        m = re.match(r'^(ADD|RMV|MOD|SET)\s+([A-Za-z0-9_]+)', s, re.I)
        if m:
            fam, verb = m.group(2).upper(), m.group(1).upper()
            d = out.setdefault(fam, {})
            d[verb] = d.get(verb, 0) + 1
    return out


def _status_skipped(status):
    return any(w in status for w in SKIP_STATUS_WORDS)


def check_rmv_vs_add(sess_dir=None, intent_text='', mml_text='', plan_text=''):
    """G30：规划表说要删除的族，产物却配成了 ADD 或漏删。

    Returns {
      ok: bool,
      skipped: bool,
      n_plan_rmv: int,          # 规划表里「动作=删除」的族数（已排除跳过的）
      reversed: [{biz, family, action, prod_verbs, n_add}],  # 方向反了
      missed: [{biz, family, action}],                        # 漏删
      no_mml: bool,             # 产物无该族时的额外标记
    }
    """
    # 产物可能在这两个位置（容器内是 analysis_code/，评估采集出来是根目录）
    bases = []
    if sess_dir:
        sd = Path(sess_dir)
        bases = [sd / 'analysis_code', sd]

    def _find(name):
        for b in bases:
            p = b / name
            if p.exists():
                return p.read_text(encoding='utf-8', errors='replace')
        return ''

    if not plan_text:
        plan_text = _find('命令族规划.md')
    if not mml_text:
        mml_text = _find('mml.txt')

    # 规划表是主数据源；没有规划表时退回意图文本解析不了族，直接 skip
    if not plan_text:
        return {'ok': True, 'skipped': True, 'reason': '缺命令族规划.md',
                'n_plan_rmv': 0, 'reversed': [], 'missed': []}
    if not mml_text:
        return {'ok': True, 'skipped': True, 'reason': '缺 mml.txt',
                'n_plan_rmv': 0, 'reversed': [], 'missed': []}

    plan_rows = parse_plan_rmv_rows(plan_text)
    # 排除 agent 已声明跳过的行
    plan_rows = [r for r in plan_rows if not _status_skipped(r['status'])]

    if not plan_rows:
        return {'ok': True, 'skipped': True,
                'reason': '规划表里没有「动作=删除」的行（或全部标记跳过）',
                'n_plan_rmv': 0, 'reversed': [], 'missed': []}

    prod_verbs = parse_prod_verbs(mml_text)
    prod_counts = parse_prod_counts(mml_text)

    reversed_list = []
    missed_list = []
    seen = set()

    for r in plan_rows:
        fam = r['family']
        if fam in seen:
            continue
        seen.add(fam)

        pv = prod_verbs.get(fam)
        if not pv:
            missed_list.append({'biz': r['biz'], 'family': fam,
                                'action': r['action'], 'why': '产物无此族'})
            continue

        if 'RMV' in pv:
            continue   # 有 RMV，正常

        if 'ADD' in pv:
            reversed_list.append({
                'biz': r['biz'], 'family': fam, 'action': r['action'],
                'prod_verbs': sorted(pv),
                'n_add': (prod_counts.get(fam) or {}).get('ADD', 0),
            })
        else:
            # 有 MOD/SET 但没 RMV/ADD，不算方向反，但提示
            missed_list.append({'biz': r['biz'], 'family': fam,
                                'action': r['action'],
                                'why': f"只有 {'/'.join(sorted(pv))}，无 RMV"})

    return {
        'ok': not reversed_list and not missed_list,
        'skipped': False,
        'n_plan_rmv': len(plan_rows),
        'reversed': reversed_list[:10],
        'missed': missed_list[:10],
    }


if __name__ == '__main__':
    import json
    import sys
    sd = sys.argv[1] if len(sys.argv) > 1 else '.'
    print(json.dumps(check_rmv_vs_add(sess_dir=sd), ensure_ascii=False, indent=1))
