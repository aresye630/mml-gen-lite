"""G29：SET 属性族漏配检测。

用户要求（2026-11-10）：「G29直接加」

背景实测（27 个阶段1 低覆盖工单）：
  「EXP 有但 agent 漏了」的 40 个族里，15 个是纯 SET 属性命令：
    ALMINFO 8 / APNSGLPASS 6 / LICENSESWITCH 5 / REFRESHSRV 3
    APNIPALLOCRULE 2 / URRGRPBINDING 2 / DEACTIVERATE 2 ...
  agent 的系统性偏好是「建新对象」（ADD），不愿「给已有对象设属性」（SET）。

判据设计：
  1. 读规划表，找状态=「确认」且命令族是 SET xxx 行
  2. 检查产物 mml 里有没有对应的 SET 命令
  3. 没有 → warn（列出该配的 SET 族）

  注意：这里查的是「规划了却没配」，与 G26（规划 vs params.csv）互补，
       G26 看 csv 层面，G29 看 mml 层面。
"""
import re
from pathlib import Path

# 不需要配置的 SET 族（一次性操作，不产生持久配置）
# ★ 2026-11-10 修正：原来误把 LICENSESWITCH 放进来，导致它永远不被检查。
#   LICENSESWITCH 是持久配置（License 开关），必须检查。
EXEC_ONLY_FAMS = {
    'REFRESHSRV',      # 业务刷新：操作类，执行后不保留状态
    'NFUPDATE',        # 网元更新：操作类
    'ACTNF',           # 激活网元：操作类
    'DEACTNF',         # 去激活网元
}


def parse_plan_set_rows(plan_text):
    """从规划表提取「命令族 = SET xxx」的行。"""
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

        fam_idx = header.index('命令族')
        st_idx = header.index('状态') if '状态' in header else None
        biz_idx = header.index('业务对象') if '业务对象' in header else None
        ncol = len(header)

        i += 1
        if i < len(lines) and re.fullmatch(r'[|\s\-:]+', lines[i].strip()):
            i += 1

        while i < len(lines):
            row = lines[i].strip()
            if not row.startswith('|'):
                break
            cells = [c.strip() for c in row.strip().strip('|').split('|')]
            if len(cells) < ncol:
                i += 1
                continue

            status = cells[st_idx] if (st_idx is not None and st_idx < len(cells)) else ''
            if '跳过' in status or '待定' in status:
                i += 1
                continue

            fam_cell = cells[fam_idx] if fam_idx < len(cells) else ''
            biz = cells[biz_idx] if (biz_idx is not None and biz_idx < len(cells)) else ''

            for part in re.split(r'[/,、]', fam_cell):
                t = part.strip().upper()
                m = re.match(r'^SET\s+([A-Z][A-Z0-9_]{2,})$', t)
                if m:
                    fam = m.group(1)
                    if fam in EXEC_ONLY_FAMS:
                        continue
                    out.append({'family': fam, 'biz': biz[:50], 'status': status})
            i += 1
        continue
    return out


def check_set_missing(sess_dir):
    """G29：规划表里标「确认」的 SET 族，产物里有没有配。

    Returns {
      ok: bool,
      skipped: bool,
      n_planned: int,
      missing: [{family, biz}],
    }
    """
    adir = Path(sess_dir) / 'analysis_code'
    plan_p = adir / '命令族规划.md'
    mml_p = adir / 'mml.txt'

    if not plan_p.exists():
        return {'ok': True, 'skipped': True, 'reason': '无规划表',
                'n_planned': 0, 'missing': []}
    if not mml_p.exists():
        return {'ok': True, 'skipped': True, 'reason': '无 mml.txt',
                'n_planned': 0, 'missing': []}

    planned = parse_plan_set_rows(plan_p.read_text(encoding='utf-8', errors='replace'))
    if not planned:
        return {'ok': True, 'skipped': True, 'reason': '规划表无 SET 族',
                'n_planned': 0, 'missing': []}

    mml_text = mml_p.read_text(encoding='utf-8', errors='replace')

    # 产物里出现的 SET 族
    prod_sets = set()
    for line in mml_text.split('\n'):
        s = line.split('//')[0].strip()
        if s.startswith(('/*', '#', '*')):
            continue
        m = re.match(r'^SET\s+([A-Za-z0-9_]+)', s, re.I)
        if m:
            prod_sets.add(m.group(1).upper())

    missing = [p for p in planned if p['family'] not in prod_sets]

    return {
        'ok': not missing,
        'skipped': False,
        'n_planned': len(planned),
        'n_prod_sets': len(prod_sets),
        'missing': missing[:10],
    }


if __name__ == '__main__':
    import json
    import sys
    sd = sys.argv[1] if len(sys.argv) > 1 else '.'
    print(json.dumps(check_set_missing(sd), ensure_ascii=False, indent=1))
