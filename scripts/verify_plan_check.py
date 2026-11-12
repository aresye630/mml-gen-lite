#!/usr/bin/env python3
"""P0-3 验证：Step1 结构合规 + Step2 意图对象提取与覆盖。

验证目标：
  V1 意图解析：三种格式（standard / copy / extra）都能解析
  V2 约束提取：行内括号 + 下一行括号都能挂到条目上
  V3 Step1 结构合规：状态非法/族列空/通配/散文族名 都能检出
  V4 Step2 对象覆盖：真实覆盖 vs 故意漏族 的差别能体现
  V5 误报控制：不会因为「用户模板清单」这行而误判「用户模板和规则的绑定关系」已覆盖
  V6 跨单一致性：多个工单都能跑通

判据原则（用户强调）：
  · 这是补全用途，判据必须能区分「真缺」和「格式差异」
  · 不能过宽（见词就判覆盖），也不能过严（同义词差异就判缺失）
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, '/Users/alesc/workspace/mml-gen-lite/workflow/stage3')
import plan_check as PC

GT = json.loads(Path('/tmp/gt_cleaned.json').read_text(encoding='utf-8'))
GT_MAP = {g['ticket']: g for g in GT}
INTENT_DIR = Path('/tmp/intent_v3')
PLAN_DIR = Path('/tmp/eval_versions_out/V3')

results = []


def check(name, cond, detail=''):
    results.append((name, bool(cond), detail))
    print(f'  {"✅" if cond else "❌"} {name}' + (f'  —— {detail}' if detail else ''))


def main():
    print('=' * 92)
    print('P0-3 验证：Step1 结构合规 + Step2 意图对象提取')
    print('=' * 92)

    # ══ V1 意图解析：三种格式 ══
    print('\n【V1】意图解析（三种格式）')
    TEXT = '''【APN 与移动性】
- 用户模板「up_sos」的配置：按现网同类用户模板「up_ims」的存量做法配齐
- 新增 APN配置
    （是否绑定 VPN为关闭，APN 名称为sos）
- 存量「up_ims」没有、需单独配置的：UPBINDUPG

【计费链】
- 新增 规则（策略类型为PCC，优先级为1000，过滤模式为FLOWFILTER）
- 删除 用户模板和规则的绑定关系（规则名称为r_sos_sig）'''
    p = PC.parse_intent(TEXT)
    kinds = {it['kind'] for it in p['items']}
    check('V1-1 三种格式都识别', kinds >= {'standard', 'copy', 'extra'},
          f'kinds={sorted(kinds)}')
    copies = [i for i in p['items'] if i['kind'] == 'copy']
    check('V1-2 copy 条目提取参照对象', copies and copies[0]['ref_instance'] == 'up_ims',
          f"ref={copies[0]['ref_instance'] if copies else None}")
    extras = [i for i in p['items'] if i['kind'] == 'extra']
    check('V1-3 extra 条目提取族名', extras and 'UPBINDUPG' in extras[0]['families'],
          f"families={extras[0]['families'] if extras else None}")

    # ══ V2 约束提取 ══
    print('\n【V2】约束提取（行内 + 下一行）')
    std = [i for i in p['items'] if i['kind'] == 'standard']
    # 行内约束
    rule_it = next((i for i in std if i['object'] and '规则' in i['object']), None)
    check('V2-1 行内约束提取',
          rule_it and rule_it['raw_params'].get('策略类型') == 'PCC',
          f"params={rule_it['raw_params'] if rule_it else None}")
    # 下一行约束
    apn_it = next((i for i in std if i['object'] and 'APN配置' in i['object']), None)
    # 键名归一化：'APN 名称' → 'APN'（RE_PARAM_VALUE 会把「XX名称为YY」剥成 XX）
    apn_params = apn_it['raw_params'] if apn_it else {}
    check('V2-2 下一行约束挂到条目',
          any(v == 'sos' for v in apn_params.values()),
          f"params={apn_params}")

    # ══ V3 Step1 结构合规 ══
    print('\n【V3】Step1 结构合规')
    BAD_PLAN = '''# 命令族规划

## 总览
| # | 数据清单表 | 业务对象 | 对象数量 | 现网已有 | 命令族 | 动作 | 判断依据 | 状态 |
|---|---|---|---|---|---|---|---|---|
| 1 | 表1 | 对象1 | 1 | 0 | ADD POOLGROUP | 新增 | 依据1 | 确认 |
| 2 | 表2 | 对象2 | 1 | 0 | SET APN* | 新增 | 依据2 | 已存在 |
| 3 | 表3 | 对象3 | 1 | 0 |  | 新增 |  | 确认 |

## 不确定项
APNCHARGECTRL 和 APNIDLETIME 这两个族要不要配不确定，NOID 也查不到。'''
    r1 = PC.check_plan_structure(BAD_PLAN)
    check('V3-1 检出状态非法', any(i['type'] == 'status_invalid' for i in r1['issues']),
          f"{[i['detail'][:30] for i in r1['issues'] if i['type'] == 'status_invalid']}")
    check('V3-2 检出族列为空', any(i['type'] == 'family_empty' for i in r1['issues']),
          f"{len([i for i in r1['issues'] if i['type'] == 'family_empty'])} 条")
    check('V3-3 检出通配', len(r1['wildcard_rows']) >= 1,
          f"{len(r1['wildcard_rows'])} 行")
    check('V3-4 散文族名救回', set(r1['prose_families']) >= {'APNCHARGECTRL', 'APNIDLETIME'},
          f"{r1['prose_families']}")
    check('V3-5 参数名不误判为族名（NOID 应排除）',
          'NOID' not in r1['prose_families'], f"{r1['prose_families']}")

    # ══ V4 Step2 对象覆盖 ══
    print('\n【V4】Step2 对象覆盖')
    # 意图 5 个对象：用户模板 up_sos / APN配置 / UPBINDUPG / 规则 / 绑定关系
    GOOD_PLAN = '''| # | 数据清单表 | 业务对象 | 对象数量 | 现网已有 | 命令族 | 动作 | 判断依据 | 状态 |
|---|---|---|---|---|---|---|---|---|
| 1 | 用户模板清单 | 用户模板 up_sos | 1 | 0 | ADD USERPROFILE | 新增 | 依据 | 确认 |
| 2 | APN配置 | APN配置 sos | 1 | 0 | ADD APN | 新增 | 依据 | 确认 |
| 3 | 补充项 | UPBINDUPG 绑定 | 1 | 0 | ADD UPBINDUPG | 新增 | 依据 | 确认 |
| 4 | 策略规则清单 | 策略规则 r_sos_sig | 1 | 0 | ADD RULE | 新增 | 依据 | 确认 |
| 5 | 绑定关系 | 用户模板和规则的绑定关系 | 1 | 0 | ADD RULEBINDING | 新增 | 依据 | 确认 |'''
    r2 = PC.check_intent_coverage(TEXT, GOOD_PLAN)
    check('V4-1 全覆盖时 coverage=1.0', r2['coverage_rate'] >= 0.99,
          f"{r2['coverage_rate']*100:.0f}%")

    # 反例：规划表只写了一条
    BAD_PLAN2 = '''| # | 数据清单表 | 业务对象 | 对象数量 | 现网已有 | 命令族 | 动作 | 判断依据 | 状态 |
|---|---|---|---|---|---|---|---|---|
| 1 | 用户模板清单 | 用户模板 up_sos | 1 | 0 | ADD USERPROFILE | 新增 | 依据 | 确认 |'''
    r3 = PC.check_intent_coverage(TEXT, BAD_PLAN2)
    check('V4-2 缺对象时能检出', len(r3['missing']) >= 2,
          f"缺 {len(r3['missing'])} 个: {[m['object'][:12] for m in r3['missing'][:3]]}")
    check('V4-3 覆盖率下降', r3['coverage_rate'] < 0.9,
          f"{r3['coverage_rate']*100:.0f}%")

    # ══ V5 误报控制：关键词必须同行 ══
    print('\n【V5】误报控制（关键词必须落在同一行）')
    PLAN_TRAP = '''| # | 数据清单表 | 业务对象 | 对象数量 | 现网已有 | 命令族 | 动作 | 判断依据 | 状态 |
|---|---|---|---|---|---|---|---|---|
| 1 | 用户模板清单 | 用户模板 up_sos | 1 | 0 | ADD USERPROFILE | 新增 | 依据 | 确认 |
| 2 | 规则清单 | 策略规则 r_sos_sig | 1 | 0 | ADD RULE | 新增 | 依据 | 确认 |'''
    INTENT_TRAP = '''【计费链】
- 删除 用户模板和规则的绑定关系（规则名称为r_sos_sig）'''
    r4 = PC.check_intent_coverage(INTENT_TRAP, PLAN_TRAP)
    # 「用户模板」在第1行，「规则」在第2行 → 没有一行同时含两个词 → 应判缺失
    check('V5-1 跨行的关键词不算覆盖',
          len(r4['missing']) == 1,
          f"missing={len(r4['missing'])} 个")

    # ══ V6 真实工单 ══
    print('\n【V6】真实工单')
    TK = 'NC20260810002261'
    ip = INTENT_DIR / f'{TK}_意图.md'
    pp = PLAN_DIR / TK / '命令族规划.md'
    if ip.exists() and pp.exists():
        itxt = ip.read_text(encoding='utf-8')
        ptxt = pp.read_text(encoding='utf-8')
        p2 = PC.parse_intent(itxt)
        check('V6-1 大单意图解析条目数 > 40', len(p2['items']) > 40,
              f"{len(p2['items'])} 条")
        r5 = PC.check_intent_coverage(itxt, ptxt)
        check('V6-2 大单对象覆盖 >= 90%', r5['coverage_rate'] >= 0.9,
              f"{r5['coverage_rate']*100:.0f}% ({len(r5['covered'])}/{r5['n_objects']})")
        r6 = PC.check_plan_structure(ptxt)
        check('V6-3 真实规划表结构合规', len(r6['issues']) == 0,
              f"{len(r6['issues'])} 个问题")

    # ══ 汇总 ══
    print('\n' + '=' * 92)
    ok = sum(1 for _, c, _ in results if c)
    print(f'结果: {ok}/{len(results)} 通过')
    fails = [(n, d) for n, c, d in results if not c]
    if fails:
        print('\n失败项：')
        for n, d in fails:
            print(f'  ❌ {n}  {d}')
    else:
        print('✅ 全部通过')
    print('=' * 92)
    return 0 if ok == len(results) else 1


if __name__ == '__main__':
    sys.exit(main())
