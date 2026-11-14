"""G26：规划表 vs params.csv 一致性检测。

用户裁定思路（2026-11-09）：
  规划表是 agent 自己写的，用它来校验自己的产物 —— 逻辑闭环，
  比再写一条 prompt 可靠。

实测背景：
  NC20260820000552（GT 341 条）：
    规划表里列了 BSFIPRANGEBIND / TAIRANGELIST / UPBINDS11 等族
    params.csv 里一个组都没有（只有 MOD APN / RMV EPRPDYNIP）
    → 命令数只有 2%
  87 工单里 41 个属于「csv 本身就不夠」，这是主要矛盾。

判据：
  1. 从「命令族规划.md」的表格里提取规划的族（命令族列）
  2. 从 params.csv 的「命令族」列提取实际配置的族
  3. 规划了但 csv 里没有 → fatal（说明漏配）
  4. 只对状态为「确认」或「★人工调整」的行检查（跳过 / 待定不算）
"""
import csv
import io
import re
from collections import Counter
from pathlib import Path

# 规划表里「命令族」列的格式：ADD POOL / MOD SECTION / SET URRGRPBINDING
FAM_RE = re.compile(r'\b(ADD|RMV|MOD|SET)\s+([A-Z][A-Z0-9_]+)\b')

# 不需要在 params.csv 出现的族（执行类命令，无参数对象）
EXEC_ONLY_FAMS = {
    'REFRESHSRV',   # SET REFRESHSRV:REFRESHTYPE=ALL; 只有开关
}


def parse_plan_table(plan_text):
    """从规划表提取 (族名, 状态, 对象数量)。

    ★★ 2026-11-13 重写：按表头名定位列，不再硬编码列号
    ---------------------------------------------------
    原实现假设固定 9 列布局，但实际规划表有两种形态：

      A. 9 列（带「动作」列）：
         | # | 数据清单表 | 业务对象 | 对象数量 | 现网已有 | 命令族 | 动作 | 判断依据 | 状态 |
           命令族列=裸族名（N2TACID），动作列=MOD

      B. 9 列（无「动作」列，动词写在命令族里）：
         | # | 容器自愈控制 | 容器自愈总开关 | 1 | 1 | SET PODHEALCTRL（UEG） | 待定：... | 第1075行... | 待定 |
           命令族列=SET PODHEALCTRL（UEG）

    原实现按固定下标取 body[5]（命令族）、body[8]（状态），
    在形态 B 下 body[5] 其实是「待定：目标值...」列，
    导致 family 被解析成 "1"、状态错位。
    实测误报：NC20260913000295 正常单被报 9 处 violated。

    新实现：先找表头行，按列名建索引；找不到表头才退回旧的下标法。
    """
    lines = [l.strip() for l in plan_text.split('\n')]

    # ── 1) 找表头行并建列索引 ─────────────────────────────
    def _find_col(header_cells, *names):
        for nm in names:
            for idx, h in enumerate(header_cells):
                if nm in h:
                    return idx
        return None

    col = {}
    for line in lines:
        if not line.startswith('|'):
            continue
        cells = [c.strip() for c in line.split('|')][1:-1]
        joined = ''.join(cells)
        # 表头特征：同时含「命令族」和「状态」
        if '命令族' in joined and '状态' in joined:
            col = {
                'family': _find_col(cells, '命令族', '族'),
                'status': _find_col(cells, '状态'),
                'qty': _find_col(cells, '对象数量', '数量'),
                'action': _find_col(cells, '动作'),
            }
            break

    out = []
    for line in lines:
        if not line.startswith('|'):
            continue
        cells = [c.strip() for c in line.split('|')][1:-1]
        if len(cells) < 5:
            continue
        # 跳过分隔行 |---|---|
        if all(re.fullmatch(r':?-+:?', c) for c in cells if c):
            continue
        # 跳过表头行本身
        if any('命令族' in c for c in cells):
            continue

        # ── 2) 取列（有表头按名取，无表头退回旧下标）────────
        if col.get('family') is not None and col['family'] < len(cells):
            fam_cell = cells[col['family']]
            status_cell = (cells[col['status']]
                           if col.get('status') is not None and col['status'] < len(cells)
                           else cells[-1])
            qty_cell = (cells[col['qty']]
                        if col.get('qty') is not None and col['qty'] < len(cells)
                        else '')
            action_cell = (cells[col['action']]
                           if col.get('action') is not None and col['action'] < len(cells)
                           else '')
        else:
            # 旧下标法（形态 A）
            if len(cells) < 9:
                continue
            fam_cell = cells[5]
            status_cell = cells[8]
            qty_cell = cells[3]
            action_cell = cells[6] if len(cells) > 6 else ''

        # ── 3) 从「动作」列（若独立存在）提动词 ──────────────
        verb = ''
        if action_cell:
            for v in ('ADD', 'MOD', 'RMV', 'SET'):
                if re.search(rf'\b{v}\b', action_cell.upper()):
                    verb = v
                    break

        # ── 4) 从命令族列提族名 ────────────────────────────
        fams_in_cell = []
        for m in FAM_RE.finditer(fam_cell):
            _v = m.group(1).upper()
            _f = m.group(2).upper()
            fams_in_cell.append(f'{_v} {_f}')
        if not fams_in_cell:
            # 裸族名：全大写+下划线，用 / 或 , 分隔
            for part in re.split(r'[/,、]', fam_cell):
                t = part.strip().upper()
                if re.fullmatch(r'[A-Z][A-Z0-9_]{2,}', t):
                    fams_in_cell.append(f'{verb} {t}' if verb else t)

        if not fams_in_cell:
            continue

        st = status_cell.strip()
        try:
            qty = int(re.sub(r'[^\d]', '', qty_cell) or '0')
        except Exception:
            qty = 0

        for _f in fams_in_cell:
            out.append({'family': _f, 'status': st, 'qty': qty})

    return out


def parse_csv_families(csv_text):
    """从 params.csv 提取族 → 组数。"""
    rows = list(csv.DictReader(io.StringIO(csv_text)))
    fams = Counter()
    groups = {}
    for r in rows:
        fam = (r.get('命令族') or '').strip()
        grp = (r.get('组') or '').strip()
        if not fam:
            continue
        fams[fam] += 1
        if grp:
            groups.setdefault(fam, set()).add(grp)
    return fams, groups


def check_plan_vs_csv(sess_dir):
    """检查规划表与 params.csv 的一致性。

    Returns:
      {
        'ok': bool,
        'missing': [{family, status, qty}],   # 规划了但 csv 没有
        'count_mismatch': [{family, planned, actual}],  # 数量差太多
        'skipped': bool,
        'reason': str,
      }
    """
    adir = Path(sess_dir) / 'analysis_code'
    plan_p = adir / '命令族规划.md'
    csv_p = adir / 'params.csv'

    if not plan_p.exists():
        return {'ok': True, 'skipped': True, 'reason': '无规划表（非两阶段流程）',
                'missing': [], 'count_mismatch': []}
    if not csv_p.exists():
        return {'ok': True, 'skipped': True, 'reason': '无 params.csv',
                'missing': [], 'count_mismatch': []}

    plan_text = plan_p.read_text(encoding='utf-8', errors='replace')
    csv_text = csv_p.read_text(encoding='utf-8', errors='replace')

    planned = parse_plan_table(plan_text)
    csv_fams, csv_groups = parse_csv_families(csv_text)

    if not planned:
        return {'ok': True, 'skipped': True, 'reason': '规划表里没解析出族',
                'missing': [], 'count_mismatch': []}

    # 只看「确认」和「★人工调整」的行
    must_do = [x for x in planned
               if ('确认' in x['status'] or '人工调整' in x['status'])
               and '跳过' not in x['status']]

    missing, count_mismatch = [], []
    for x in must_do:
        fam = x['family']
        bare = fam.split(' ', 1)[1]
        if bare in EXEC_ONLY_FAMS:
            continue

        # csv 里的族名可能是裸名（POOL）或带动词（MOD POOL）
        actual = csv_fams.get(fam, 0) or csv_fams.get(bare, 0)
        if actual == 0:
            missing.append({'family': fam, 'status': x['status'], 'qty': x['qty']})
            continue

        # 数量校验：规划 qty > 0 时，csv 组数不应少于 qty 的 50%
        n_groups = len(csv_groups.get(fam, set()) | csv_groups.get(bare, set()))
        if x['qty'] > 0 and n_groups < x['qty'] * 0.5:
            count_mismatch.append({'family': fam, 'planned': x['qty'],
                                   'actual': n_groups})

    # ★ 2026-11-13 新增反向检查：规划标「跳过」但 csv 里却配了
    #
    #   实测 NC20260814000425（膨胀 162x）：
    #     规划表 #14「位置区分配开关 160 条」状态=不配（已存在且一致）→ 跳过
    #     但阶段2 agent 又主动重发了 160 条（理由：文档说 INHERIT 时按全局开关生效）
    #     → 产物 162 条，GT 只要 1 条
    #
    #   问题：agent 自我矛盾（规划说不配，实际又配），且 G26 只查单向抓不到
    #
    #   判据：状态含「跳过」的行，如果该族在 csv 里有大量组（>= 3 组），报警
    #   分级：warn（不是配置错误，但会让产物膨胀，需人工确认是否有意重发）
    # ★★ 2026-11-13 用户裁定：规划表标「跳过」/「待定」的族，产物里不许出现
    #   「拿 agent 自己写的规划表校验它自己产物」应该做成硬约束，不只是 warn。
    #
    #   实测两类膨胀都靠这条堵：
    #     NC20260814000425（162x）：规划 #14 状态=跳过，阶段2 重发 160 条
    #     NC20260814001250（4.0x）：规划 #31-35 状态=待定，阶段2 自建 8 族接口
    #
    #   例外（不判）：
    #     · EXEC_ONLY_FAMS：执行类命令族（REFRESHSRV 等），不受对象状态约束
    #     · 规划表里没写族名（family 为空或是「无」）的行
    #     · 状态里同时含「确认」的行（agent 既标跳过又标确认，以确认为准）
    # ★★ 2026-11-13 区分「跳过」和「待定」的语义（实测后修正）
    #
    #   「跳过」= agent 明确决定不配 → 产物里出现就是自相矛盾 → fatal
    #   「待定」= agent 自己也不确定 → 产物里出现说明它做了选择 → 只 warn
    #
    #   实测依据：NC20260913000295（正常单，100% 覆盖）的 9 行全是「待定」，
    #     语义是「目标值=ENABLE 则跳过；=DISABLE 则 MOD」—— agent 不知道目标值，
    #     阶段2 按现网值配了。这不是矛盾，是信息不足下的合理选择。
    #     如果也当 fatal，会把正常单误判成失败。
    def _collect(status_kw):
        rows = [x for x in planned
                if status_kw in x['status'] and '确认' not in x['status']
                and '人工调整' not in x['status']]
        got = []
        for x in rows:
            fam = x['family']
            if not fam or fam in ('无', '-'):
                continue
            bare = fam.split(' ', 1)[1] if ' ' in fam else fam
            if bare in EXEC_ONLY_FAMS:
                continue
            n_groups = len(csv_groups.get(fam, set()) | csv_groups.get(bare, set()))
            if n_groups == 0:
                continue
            got.append({
                'family': fam,
                'planned_status': x['status'][:30],
                'actual_groups': n_groups,
                'planned_qty': x['qty'],
            })
        return got

    violated = _collect('跳过')     # fatal
    undecided = _collect('待定')    # warn

    return {
        'ok': not missing and not count_mismatch and not violated,
        'skipped': False,
        'missing': missing,
        'count_mismatch': count_mismatch,
        'violated': violated,
        'undecided': undecided,
        'reason': '',
        'n_planned': len(must_do),
    }


if __name__ == '__main__':
    import sys
    sd = sys.argv[1] if len(sys.argv) > 1 else '.'
    r = check_plan_vs_csv(sd)
    import json
    print(json.dumps(r, ensure_ascii=False, indent=1))
