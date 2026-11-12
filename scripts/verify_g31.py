#!/usr/bin/env python3
"""G31（规划表通配检测）判别力验证。

要求：
  真正例：通配/概括的写法必须检出
  真负例：正常写法必须放过（一行多个具体族是允许的）

用真实规划表 + 构造用例双重验证。
"""
import sys
from pathlib import Path

sys.path.insert(0, '/Users/alesc/workspace/mml-gen-lite/workflow/guard')
import plan_wildcard as G


CASES = [
    # ── 应检出（正例）──
    ('正例1 通配星号', 'ADD APN + SET APN*（UNC）', True),
    ('正例2 数量概括', 'SET APNxxx 属性族 25 个', True),
    ('正例3 等N', 'SET APN 属性族等 25 个', True),
    ('正例4 省略号', 'ADD RULE, URRGROUP, ...', True),
    ('正例5 xxx占位', 'SET APNxxx（UNC）', True),
    ('正例6 N条', 'ADD FILTER 共 12 条', True),

    # ── 应放过（负例）──
    ('负例1 单族', 'ADD USERPROFILE（UNC）', False),
    ('负例2 多族具体', 'ADD APN / SET APNCHARGECTRL / SET APNIDLETIME', False),
    ('负例3 带网元后缀', 'MOD POOL（UDG）', False),
    ('负例4 带候选标注', 'ADD PCSCFGRPBNDAPN（UNC，候选）', False),
    ('负例5 单族+动作', 'RMV FILTERIPV6', False),
    ('负例6 两个族逗号分隔', 'ADD URR, URRGROUP', False),

    # ── 边界 ──
    ('边界1 空', '', False),
    ('边界2 只有动作', 'ADD', False),
]


def build_plan(rows):
    """把 [(fam_cell, status)] 拼成规划表。"""
    out = ['# 命令族规划', '', '## 总览', '',
           '| # | 数据清单表 | 业务对象 | 对象数量 | 现网已有 | 命令族 | 动作 | 判断依据 | 状态 |',
           '|---|---|---|---|---|---|---|---|---|']
    for i, (fam, st) in enumerate(rows, 1):
        out.append(f'| {i} | 表{i} | 对象{i} | 1 | 0 | {fam} | 新增 | 依据 | {st} |')
    return '\n'.join(out)


def main():
    results = []
    tmp = Path('/tmp/g31_test')
    tmp.mkdir(exist_ok=True)

    print('=' * 84)
    print('G31 判别力验证')
    print('=' * 84)

    # ── 逐用例 ──
    print('\n【单元用例】')
    for name, cell, expect_hit in CASES:
        plan = build_plan([(cell, '确认')])
        pf = tmp / 'plan.md'
        pf.write_text(plan, encoding='utf-8')
        r = G.check_plan_wildcard(plan_path=str(pf))
        hit = not r['ok'] and not r.get('skipped')
        ok = (hit == expect_hit)
        results.append((name, ok))
        mark = '✅' if ok else '❌'
        detail = ''
        if hit:
            detail = r['hits'][0]['reasons'][0] if r['hits'] else ''
        print(f'  {mark} {name:<22} 期望{"检出" if expect_hit else "放过"} '
              f'实际{"检出" if hit else "放过"}  {detail}')

    # ── 真实规划表 ──
    print('\n【真实规划表】')
    real_cases = [
        ('本轮加硬要求后（含 SET APN*）',
         '/tmp/eval_versions_out/V3/NC20260810002261/命令族规划.md', True),
        ('历史最好（逐族列 63 行）',
         '/tmp/plan_20261111_222758_756b.md', None),
    ]
    for name, path, expect in real_cases:
        p = Path(path)
        if not p.exists():
            print(f'  ⊘ {name}: 文件不存在')
            continue
        r = G.check_plan_wildcard(plan_path=str(p))
        if r.get('skipped'):
            print(f'  ⊘ {name}: {r.get("reason")}')
            continue
        hit = not r['ok']
        mark = '✅' if (expect is None or hit == expect) else '❌'
        results.append((name, expect is None or hit == expect))
        print(f'  {mark} {name}: {r["n_rows"]} 行, 检出 {r["n_hits"]} 行通配')
        for h in (r.get('hits') or [])[:3]:
            print(f'      第 {h["row"]} 行: {h["fam_cell"][:60]}  [{", ".join(h["reasons"])}]')

    # ── 跳过逻辑 ──
    print('\n【跳过逻辑】')
    plan = build_plan([('SET APN*（UNC）', '跳过'), ('MOD POOL', '确认')])
    pf = tmp / 'plan2.md'
    pf.write_text(plan, encoding='utf-8')
    r = G.check_plan_wildcard(plan_path=str(pf))
    ok = r['ok']     # 跳过的行不检查
    results.append(('跳过的行不报', ok))
    print(f'  {"✅" if ok else "❌"} 状态=跳过的行即使有通配也不报')

    # ── 汇总 ──
    print('\n' + '=' * 84)
    ok_n = sum(1 for _, c in results if c)
    print(f'结果: {ok_n}/{len(results)} 通过')
    fails = [n for n, c in results if not c]
    if fails:
        print(f'失败: {fails}')
    else:
        print('✅ 全部通过')
    print('=' * 84)
    return 0 if ok_n == len(results) else 1


if __name__ == '__main__':
    sys.exit(main())
