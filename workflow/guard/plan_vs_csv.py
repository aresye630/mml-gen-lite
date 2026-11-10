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

    表格结构：
      | # | 数据清单表 | 业务对象 | 对象数量 | 现网已有 | 命令族 | 动作 | 判断依据 | 状态 |
      索引:  0    1          2         3         4       5      6       7        8
    """
    out = []
    for line in plan_text.split('\n'):
        line = line.strip()
        if not line.startswith('|'):
            continue
        cells = [c.strip() for c in line.split('|')]
        # cells[0] 和最后一个是空（前后各一个 |）
        if len(cells) < 10:
            continue
        # 跳过分隔行 |---|---|
        if all(re.fullmatch(r':?-+:?', c) for c in cells[1:-1] if c):
            continue

        body = cells[1:-1]
        if len(body) < 9:
            continue

        # 表头：| # | 数据清单表 | 业务对象 | 对象数量 | 现网已有 | 命令族 | 动作 | 判断依据 | 状态 |
        # body:  0    1          2         3         4       5      6       7        8
        fam_cell = body[5]      # 命令族
        status_cell = body[8]   # 状态
        qty_cell = body[3]      # 对象数量

        # ★ 规划表的「命令族」列是裸族名（N2TACID），动词在「动作」列（RMV）
        #   也可能一格里写多个族（EPRPDYN / EPRPDYNIP）
        action_cell = body[6] if len(body) > 6 else ''
        verb = ''
        for v in ('ADD', 'MOD', 'RMV', 'SET'):
            if v in action_cell.upper():
                verb = v
                break

        # 提取族名（支持裸族名 + 多个族用 / 分隔）
        fams_in_cell = []
        m = FAM_RE.search(fam_cell)
        if m:
            fams_in_cell.append(f'{m.group(1)} {m.group(2)}')
        else:
            # 裸族名：全大写+下划线，长度>=3，用 / 或 , 分隔
            for part in re.split(r'[/,、]', fam_cell):
                t = part.strip().upper()
                if re.fullmatch(r'[A-Z][A-Z0-9_]{2,}', t):
                    fams_in_cell.append(f'{verb} {t}' if verb else t)

        if not fams_in_cell:
            # 命令族列明确写「无」→ agent 已说明理由，跳过
            continue

        # 状态：确认 / 待定 / 跳过 / ★人工调整
        st = status_cell.strip()
        # 数量
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

    return {
        'ok': not missing and not count_mismatch,
        'skipped': False,
        'missing': missing,
        'count_mismatch': count_mismatch,
        'reason': '',
        'n_planned': len(must_do),
    }


if __name__ == '__main__':
    import sys
    sd = sys.argv[1] if len(sys.argv) > 1 else '.'
    r = check_plan_vs_csv(sd)
    import json
    print(json.dumps(r, ensure_ascii=False, indent=1))
