#!/usr/bin/env python3
"""验证 _build_wildcard_expansion：程序替 agent 展开规划表通配。

要求（用户裁定）：
  「改阶段2，让它自己调 exp_attr_chain 补全，不依赖规划表粒度」
  —— 但「让它自己调」= 靠 prompt，不可靠。
  实际做法：程序先调好，把展开结果直接写进 prompt。

用例：
  W1 规划表有「SET APN*」→ 提示里出现 APN 的具体属性族清单（>=10 个）
  W2 规划表没有通配 → 提示为空（不干扰）
  W3 规划表有「等 N 个」写法 → 同样展开
  W4 跳过的行不展开
  W5 展开的族名必须真实存在于 EXP
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, '/Users/alesc/workspace/mml-gen-lite/workflow')
sys.path.insert(0, '/Users/alesc/workspace/mml-gen-lite/scripts')

GT = json.loads(Path('/tmp/gt_cleaned.json').read_text(encoding='utf-8'))
GT_MAP = {g['ticket']: g for g in GT}

TK = 'NC20260810002261'
g = GT_MAP[TK]
adir = Path(g['path']) / '备份附件'
EXPS = sorted(adir.glob('*.txt'))
UNC = next((p for p in EXPS if '_UNC_' in p.name), EXPS[0])

FILES_INFO = [
    {'name': UNC.name, 'is_exp': True, 'me_type': 'UNC',
     'parsed': str(UNC), 'path': str(UNC)},
]

results = []


def check(name, cond, detail=''):
    results.append((name, bool(cond), detail))
    print(f'  {"✅" if cond else "❌"} {name}' + (f'  —— {detail}' if detail else ''))


def build_plan(rows):
    out = ['# 命令族规划', '', '## 总览', '',
           '| # | 数据清单表 | 业务对象 | 对象数量 | 现网已有 | 命令族 | 动作 | 判断依据 | 状态 |',
           '|---|---|---|---|---|---|---|---|---|']
    for i, (fam, st) in enumerate(rows, 1):
        out.append(f'| {i} | 表{i} | 对象{i} | 1 | 0 | {fam} | 新增 | 依据 | {st} |')
    return '\n'.join(out)


def main():
    import agent_run
    import importlib
    importlib.reload(agent_run)

    print('=' * 88)
    print('_build_wildcard_expansion 验证（程序替 agent 展开通配）')
    print('=' * 88)
    print(f'  EXP: {UNC.name[:60]}')

    # ── W1：通配 SET APN* ──
    print('\n【W1】规划表有「SET APN*」')
    plan = build_plan([('ADD APN + SET APN*（UNC）', '确认')])
    hint = agent_run._build_wildcard_expansion(plan, FILES_INFO, None)
    print(f'  返回 {len(hint)} 字')
    print('  ---- 前 600 字 ----')
    for ln in hint.split('\n')[:14]:
        print(f'  {ln}')
    check('W1-1 提示非空', bool(hint))
    check('W1-2 出现「已替你把规划表里的通配展开」', '已替你把规划表里的通配展开' in hint)
    # 抽取族名
    import re
    fams = set(re.findall(r'\b(APN[A-Z0-9_]{2,})\b', hint))
    check('W1-3 展开出 >=10 个 APN 属性族', len(fams) >= 10,
          f'{len(fams)} 个: {sorted(fams)[:6]}')

    # W5：族名真实存在于 EXP
    text = UNC.read_text(encoding='utf-8', errors='replace') if UNC.suffix == '.txt' else ''
    if text:
        real = {f for f in fams if re.search(rf'\b(SET|ADD|MOD)\s+{re.escape(f)}\b', text)}
        check('W5 展开的族名真实存在于 EXP', len(real) == len(fams),
              f'{len(real)}/{len(fams)} 在 EXP 里有命令')

    # ── W2：无通配 ──
    print('\n【W2】规划表无通配')
    plan2 = build_plan([('ADD USERPROFILE（UNC）', '确认'),
                        ('MOD POOL（UDG）', '确认')])
    hint2 = agent_run._build_wildcard_expansion(plan2, FILES_INFO, None)
    check('W2-1 无通配时返回空（不干扰）', hint2 == '', f'{len(hint2)} 字')

    # ── W3：「等 N 个」写法 ──
    print('\n【W3】规划表有「等 23 个」概括')
    plan3 = build_plan([('SET APNADDRESSATTR / SET APNIMSATTR 等 23 个属性族', '确认')])
    hint3 = agent_run._build_wildcard_expansion(plan3, FILES_INFO, None)
    check('W3-1 「等 N 个」也能触发展开', bool(hint3), f'{len(hint3)} 字')

    # ── W4：跳过的行不展开 ──
    print('\n【W4】通配行状态=跳过')
    plan4 = build_plan([('SET APN*（UNC）', '跳过')])
    hint4 = agent_run._build_wildcard_expansion(plan4, FILES_INFO, None)
    check('W4-1 跳过的行不展开', hint4 == '', f'{len(hint4)} 字')

    # ── W6：真实规划表（本轮那个 11 行的）──
    print('\n【W6】真实规划表（11 行，含 SET APN*）')
    real_plan = Path('/tmp/eval_versions_out/V3/NC20260810002261/命令族规划.md')
    if real_plan.exists():
        hint6 = agent_run._build_wildcard_expansion(
            real_plan.read_text(encoding='utf-8'), FILES_INFO, None)
        fams6 = set(re.findall(r'\b(APN[A-Z0-9_]{2,})\b', hint6))
        check('W6-1 真实规划表能展开', bool(hint6), f'{len(hint6)} 字')
        check('W6-2 展开出 >=20 个族', len(fams6) >= 20, f'{len(fams6)} 个')
    else:
        print('  ⊘ 文件不存在')

    # ── 汇总 ──
    print('\n' + '=' * 88)
    ok = sum(1 for _, c, _ in results if c)
    print(f'结果: {ok}/{len(results)} 通过')
    fails = [(n, d) for n, c, d in results if not c]
    if fails:
        for n, d in fails:
            print(f'  ❌ {n}  {d}')
    else:
        print('✅ 全部通过')
    print('=' * 88)
    return 0 if ok == len(results) else 1


if __name__ == '__main__':
    sys.exit(main())
