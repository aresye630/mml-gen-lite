#!/usr/bin/env python3
"""从产物目录统计两阶段族覆盖（稳健版：按表头定位列）。

关键修正（2026-11-10）：
  原来硬编码 cells[1:][5] 取「命令族」列，但：
    1. 有的行 cells 数不是 11（判断依据里含特殊字符）
    2. 「配套关系」表结构完全不同（7 列），会被误解析
  现在改为：找到含「命令族」表头的表格，按表头名定位列索引。
"""
import json
import re
import subprocess
from pathlib import Path

GT = json.loads(Path('/tmp/gt_cleaned.json').read_text(encoding='utf-8'))
OUT = Path('/tmp/eval_2stage_v2_out')
GT_MAP = {g['ticket']: g for g in GT}


def split_row(line):
    """拆表格行。用 | 分隔，但保留被转义的 \\|。"""
    return [c.strip() for c in line.strip().strip('|').split('|')]


def parse_plan_fams(plan_text):
    """从规划表提取族。

    做法：遍历所有表格，找到含「命令族」表头的那张表，
         按表头名定位「命令族」和「状态」列索引。
    """
    out = set()
    if not plan_text:
        return out

    lines = plan_text.split('\n')
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line.startswith('|'):
            i += 1
            continue

        header = split_row(line)
        # 是不是表头？含「命令族」
        if '命令族' not in header:
            i += 1
            continue

        fam_idx = header.index('命令族')
        # ★ 2026-11-10：有的规划表没有「状态」列（只有 9 列）
        #   这种情况下 st_idx=-1 会取到最后一列「判断依据」，导致误判
        #   → 没有状态列时，视为全部「确认」
        st_idx = header.index('状态') if '状态' in header else None
        ncol = len(header)

        # 跳过分隔行
        i += 1
        if i < len(lines) and re.fullmatch(r'[\|\s\-:]+', lines[i].strip()):
            i += 1

        # 读数据行
        while i < len(lines):
            row = lines[i].strip()
            if not row.startswith('|'):
                break
            cells = split_row(row)
            if len(cells) < ncol:
                i += 1
                continue

            status = ''
            if st_idx is not None and st_idx < len(cells):
                status = cells[st_idx]
            if '跳过' in status:
                i += 1
                continue

            fam_cell = cells[fam_idx] if fam_idx < len(cells) else ''
            for part in re.split(r'[/,、]', fam_cell):
                t = part.strip().upper()
                # ★ 2026-11-10：命令族列有两种写法
                #   裸族名：TAIGROUP
                #   带动词：ADD TAIGROUP / SET IFIPV6ENABLE
                m2 = re.match(r'^(?:ADD|RMV|MOD|SET)\s+([A-Z][A-Z0-9_]{2,})$', t)
                if m2:
                    out.add(m2.group(1))
                elif re.fullmatch(r'[A-Z][A-Z0-9_]{2,}', t):
                    out.add(t)
            i += 1
        continue

    # 兜底：正文里明确写「ADD XXX」的
    for m in re.finditer(r'`(?:ADD|RMV|MOD|SET)\s+([A-Z][A-Z0-9_]{2,})', plan_text):
        out.add(m.group(1))

    return out


def parse_cmd_fams(text):
    c = set()
    for line in text.split('\n'):
        s = line.split('//')[0].strip()
        if s.startswith('/*') or s.startswith('#'):
            continue
        m = re.match(r'^(ADD|RMV|MOD|SET)\s+([A-Za-z0-9_]+)', s, re.I)
        if m:
            c.add(m.group(2).upper())
    return c


def read_container(sid, name, cont='mmlgen-clean'):
    r = subprocess.run(['docker', 'exec', cont, 'sh', '-c',
                        f'cat /data/sessions/{sid}/analysis_code/{name} 2>/dev/null'],
                       capture_output=True, text=True, timeout=120)
    return r.stdout or ''


def find_rerun_sessions():
    """找所有会话，返回 {ticket: sid}（取最新的）。"""
    out = {}
    r = subprocess.run(['docker', 'exec', 'mmlgen-clean', 'sh', '-c',
                        'ls -td /data/sessions/*/ 2>/dev/null | head -60'],
                       capture_output=True, text=True, timeout=120)
    for d in r.stdout.split():
        sid = d.rstrip('/').split('/')[-1]
        r2 = subprocess.run(['docker', 'exec', 'mmlgen-clean', 'sh', '-c',
                             f'cat {d}session.json 2>/dev/null'],
                            capture_output=True, text=True, timeout=60)
        try:
            nm = str(json.loads(r2.stdout).get('name') or '')
        except Exception:
            continue
        m = re.match(r'(NC\d+)', nm)
        if m and m.group(1) not in out:
            out[m.group(1)] = sid
    return out


def main():
    rerun = find_rerun_sessions()
    print(f"找到 {len(rerun)} 个会话\n")

    rows = []
    for tk, g in GT_MAP.items():
        if not g['kept']:
            continue
        gt = {f for _, v, f, p, _ in g['kept']}

        d = OUT / tk
        plan_text = (d / '命令族规划.md').read_text(encoding='utf-8') if (d / '命令族规划.md').exists() else ''
        mml_text = (d / 'mml.txt').read_text(encoding='utf-8') if (d / 'mml.txt').exists() else ''

        # 有容器会话的优先用容器里的（更新）
        if tk in rerun:
            sid = rerun[tk]
            p2 = read_container(sid, '命令族规划.md')
            m2 = read_container(sid, 'mml.txt')
            if p2:
                plan_text = p2
            if m2:
                mml_text = m2

        if not plan_text and not mml_text:
            continue

        plan = parse_plan_fams(plan_text)
        prod = parse_cmd_fams(mml_text)

        rows.append({
            'tk': tk,
            'gt': len(gt),
            'plan_n': len(plan),
            'prod_n': len(prod),
            's1': len(gt & plan),
            's2': len(gt & prod),
            's1_miss': sorted(gt - plan),
            's2_miss': sorted(gt - prod),
            'gt_cmds': len(g['kept']),
            'prod_cmds': len([l for l in mml_text.split('\n')
                              if l.strip() and not l.strip().startswith(('/*', '//', '#'))]),
            'level': 'complex' if len(g['kept']) > 200 else ('medium' if len(g['kept']) >= 50 else 'simple'),
        })

    tot = {'gt': 0, 's1': 0, 's2': 0, 'gc': 0, 'pc': 0}
    by_level = {}
    for r in rows:
        tot['gt'] += r['gt']; tot['s1'] += r['s1']; tot['s2'] += r['s2']
        tot['gc'] += r['gt_cmds']; tot['pc'] += r['prod_cmds']
        d = by_level.setdefault(r['level'], {'n': 0, 'gt': 0, 's1': 0, 's2': 0, 'gc': 0, 'pc': 0})
        d['n'] += 1; d['gt'] += r['gt']; d['s1'] += r['s1']; d['s2'] += r['s2']
        d['gc'] += r['gt_cmds']; d['pc'] += r['prod_cmds']

    print('=' * 82)
    print('两阶段族覆盖统计')
    print('=' * 82)
    print(f"工单数         {len(rows)}")
    print(f"GT 族总数      {tot['gt']}")
    print(f"阶段1 规划覆盖  {tot['s1']}/{tot['gt']} = {tot['s1']/max(1,tot['gt'])*100:.1f}%")
    print(f"阶段2 产物覆盖  {tot['s2']}/{tot['gt']} = {tot['s2']/max(1,tot['gt'])*100:.1f}%")
    print(f"阶段损耗        {tot['s1']-tot['s2']} 个族（规划了但没配出来）")
    print(f"命令数          {tot['pc']}/{tot['gc']} = {tot['pc']/max(1,tot['gc'])*100:.0f}%")

    print(f"\n{'分档':<14} {'工单':>4} {'GT族':>5} {'阶段1覆盖':>10} {'阶段2覆盖':>10} {'阶段损耗':>8} {'命令数':>7}")
    print('-' * 72)
    for lv in ['simple', 'medium', 'complex']:
        d = by_level.get(lv)
        if not d:
            continue
        label = {'simple': '简单 <50', 'medium': '中等 50-200', 'complex': '复杂 >200'}[lv]
        print(f"{label:<14} {d['n']:>4} {d['gt']:>5} "
              f"{d['s1']/max(1,d['gt'])*100:>9.1f}% {d['s2']/max(1,d['gt'])*100:>9.1f}% "
              f"{d['s1']-d['s2']:>8} {d['pc']/max(1,d['gc'])*100:>6.0f}%")

    print(f"\n=== 阶段1 就漏了族（规划覆盖 < 80%）===")
    low = sorted([r for r in rows if r['s1']/max(1,r['gt']) < 0.8], key=lambda x: x['s1']/max(1,x['gt']))
    for r in low[:12]:
        rate = r['s1'] / max(1, r['gt']) * 100
        print(f"  {r['tk']:<22} {rate:>5.0f}%  GT{r['gt']:>3} 规划{r['s1']:>3}  "
              f"漏 {len(r['s1_miss'])}: {r['s1_miss'][:3]}")

    print(f"\n=== 阶段2 损耗大（规划有但产物没）===")
    loss = sorted([r for r in rows if r['s1'] > r['s2']], key=lambda x: -(x['s1'] - x['s2']))
    for r in loss[:10]:
        print(f"  {r['tk']:<22} 规划{r['s1']:>3} 产物{r['s2']:>3} 丢{r['s1']-r['s2']:>2}  "
              f"{r['s2_miss'][:3]}")

    Path('/tmp/twostage_stat.json').write_text(
        json.dumps({'tot': tot, 'by_level': by_level, 'rows': rows}, ensure_ascii=False, indent=1),
        encoding='utf-8')
    print(f"\n已存 /tmp/twostage_stat.json")


if __name__ == '__main__':
    main()
