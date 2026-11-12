#!/usr/bin/env python3
"""自动选参照（P0-2b）功能验证。

用户质疑："不能自己找么？"
→ 是的，必须自己找。实测 86 单里只有 17% 意图明确提了参照对象。

验证目标：
  1. 从意图行提取约束（参数名 + 值）
  2. 四维评分正确工作
  3. 自动选出的参照确实是最优（用 GT 做离线校验，不参与运行时）
  4. 反例：约束矛盾时能检出
  5. 无约束时退回形态代表性排序
  6. 性能可接受
"""
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, '/Users/alesc/workspace/mml-gen-lite/workflow/stage3')
import auto_ref as AR

GT = json.loads(Path('/tmp/gt_cleaned.json').read_text(encoding='utf-8'))
GT_MAP = {g['ticket']: g for g in GT}

TK = 'NC20260810002261'
g = GT_MAP[TK]
adir = Path(g['path']) / '备份附件'
UNC = next((p for p in adir.glob('*.txt') if '_UNC_' in p.name), None)
UDG = next((p for p in adir.glob('*.txt') if '_UDG_' in p.name), None)
EXPS = [str(UNC), str(UDG)]

results = []


def check(name, cond, detail=''):
    results.append((name, bool(cond), detail))
    print(f'  {"✅" if cond else "❌"} {name}' + (f'  —— {detail}' if detail else ''))


def main():
    print('=' * 92)
    print('自动选参照（P0-2b）功能验证')
    print('=' * 92)

    # ══ V1 约束提取 ══
    print('\n【V1】从意图行提取约束')
    CASES = [
        ('新增 规则（策略类型为PCC，优先级为1000，过滤模式为FLOWFILTER）',
         {'POLICYTYPE': 'PCC', 'PRIORITY': '1000', 'FILTERINGMODE': 'FLOWFILTER'}),
        ('新增 APN配置（是否绑定 VPN为关闭，APN 名称为sos）',
         {'APN': 'sos'}),
        ('新增 流过滤器', {}),
    ]
    ok_n = 0
    for line, expect in CASES:
        got = AR.extract_constraints(line)
        # 只检查期望的项都在
        if all(got.get(k) == v for k, v in expect.items()):
            ok_n += 1
        else:
            print(f'      "{line[:32]}" 期望 {expect} 实际 {got}')
    check('V1-1 约束提取正确', ok_n == len(CASES), f'{ok_n}/{len(CASES)}')

    # ══ V2 四维评分 ══
    print('\n【V2】四维评分')
    # 完美匹配的候选
    sc = AR.score_candidate(
        'RULE',
        {'POLICYTYPE': 'PCC', 'FILTERINGMODE': 'FLOWFILTER'},
        'sos_sig',
        {'RULENAME': 'r_ims_sig', 'POLICYTYPE': 'PCC',
         'FILTERINGMODE': 'FLOWFILTER', 'PRIORITY': '1000'},
        'r_ims_sig', 0.9)
    check('V2-1 完美匹配得满分', sc['score'] >= 0.95, f"score={sc['score']}")

    # 缺参数
    sc2 = AR.score_candidate(
        'RULE',
        {'POLICYTYPE': 'PCC', 'FILTERINGMODE': 'FLOWFILTER'},
        'sos_sig',
        {'RULENAME': 'x', 'POLICYTYPE': 'PCC'},   # 缺 FILTERINGMODE
        'x', 0.9)
    check('V2-2 缺参数扣 D1', sc2['d1'] < 1.0, f"d1={sc2['d1']}")
    check('V2-3 缺参数有说明', any('缺' in r for r in sc2['reasons']),
          str(sc2['reasons'][:1]))

    # 约束值不符
    sc3 = AR.score_candidate(
        'RULE',
        {'POLICYTYPE': 'PCC', 'FILTERINGMODE': 'FLOWFILTER'},
        'sos_sig',
        {'RULENAME': 'x', 'POLICYTYPE': 'ULCL', 'FILTERINGMODE': 'FLOWFILTER'},
        'x', 0.9)
    check('V2-4 约束值不符扣 D2', sc3['d2'] < 1.0, f"d2={sc3['d2']}")

    # 稀有形态扣 D3
    sc4 = AR.score_candidate(
        'RULE', {}, 'sos_sig',
        {'RULENAME': 'x', 'POLICYTYPE': 'PCC'}, 'x', 0.004)
    check('V2-5 稀有形态扣 D3', sc4['d3'] < 0.1, f"d3={sc4['d3']}")
    check('V2-6 稀有形态有警示', any('特例' in r for r in sc4['reasons']),
          str(sc4['reasons']))

    # ══ V3 自动选择 ══
    print('\n【V3】自动选择（真实场景）')
    LINE = '新增 规则（策略类型为PCC，优先级为1000，过滤模式为FLOWFILTER）'
    t0 = time.time()
    r = AR.auto_select_reference(EXPS, 'RULE', LINE, target_biz='sos_sig')
    elapsed = time.time() - t0

    check('V3-1 选出参照', r['best'] is not None,
          f"best={r['best']['name'] if r['best'] else None}")
    check('V3-2 得分 >= 0.9', r['best'] and r['best']['score'] >= 0.9,
          f"score={r['best']['score'] if r['best'] else 0}")
    check('V3-3 给出候选列表', len(r['candidates']) >= 3,
          f"{len(r['candidates'])} 个")

    # ══ V4 用 GT 做离线校验（运行时不用 GT）══
    print('\n【V4】离线校验：自动选的参照是否对（GT 只在这里用）')
    # 目标真实参数集
    target_params = {}
    for _, v, fam, params, raw in g['kept']:
        if fam == 'RULE' and 'sos_sig_f_f' in raw:
            target_params = params
            break
    check('V4-0 GT 目标参数集非空', bool(target_params),
          f'{len(target_params)} 个参数')

    if r['best']:
        best_name = r['best']['name']
        best_exp = r['best']['exp']
        # 找到这个候选的完整参数
        info = AR.collect_family_instances(EXPS, 'RULE')
        cand_params = None
        for inst in info['instances']:
            if inst['name'] == best_name and Path(inst['exp']).name == best_exp:
                cand_params = inst['params']
                break
        if cand_params:
            missing = set(target_params) - set(cand_params)
            check('V4-1 参照参数集覆盖 GT 需求', not missing,
                  f'缺 {sorted(missing)}' if missing else '全覆盖')

            # 枚举型参数值是否一致
            ENUM_PARAMS = {'POLICYTYPE', 'FILTERINGMODE', 'RULESPECTYPE'}
            mismatched = []
            for pn in ENUM_PARAMS:
                if pn in target_params and pn in cand_params:
                    if str(target_params[pn]).upper() != str(cand_params[pn]).upper():
                        mismatched.append((pn, target_params[pn], cand_params[pn]))
            check('V4-2 关键枚举值一致', not mismatched,
                  f'不一致: {mismatched}' if mismatched else '全一致')

    # ══ V5 无约束时的退化 ══
    print('\n【V5】无约束时退回形态代表性')
    r2 = AR.auto_select_reference(EXPS, 'RULE', '新增 规则')
    check('V5-1 无约束也能选出参照', r2['best'] is not None,
          f"best={r2['best']['name'] if r2['best'] else None}")
    if r2['best']:
        # ★ 2026-11-12 修正断言：双网元时同名族形态天然各占一半
        #   实测 UNC RULE 687/1415 = 48.6%，UDG RULE 667/1415 = 47.1%
        #   最大形态不可能到 50% → 改为「必须是占比最高的」
        top_share = max(c['shape_share'] for c in r2['candidates'])
        check('V5-2 选中的是占比最高的形态',
              abs(r2['best']['shape_share'] - top_share) < 0.01,
              f"best={r2['best']['shape_share']} top={top_share}")

    # ══ V6 边界 ══
    print('\n【V6】边界')
    r3 = AR.auto_select_reference(EXPS, 'NOSUCHFAMILY', '任意')
    check('V6-1 不存在的族 → best 为空', r3['best'] is None,
          r3['reason'][:50])

    # ══ V7 性能 ══
    print('\n【V7】性能')
    check('V7-1 自动选参照耗时 < 5s', elapsed < 5.0, f'{elapsed*1000:.0f}ms')

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
