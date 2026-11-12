#!/usr/bin/env python3
"""参照对象结构校验（P0-2）功能验证。

核心能力：
  1. 参数覆盖检查：参照缺目标需要的参数 → 检出
  2. 形态代表性检查：参照所在形态占比过低 → 检出
  3. 换参照建议：给出参数齐全的候选（含所在网元）
  4. 多网元同名对象：按 target_params 选最匹配的版本
  5. 意图参数推断：从意图/清单文字推断目标需要哪些参数

判据设计要点（用户裁定）：
  · 阶段3 是补全用途，所以校验失败要给出「换哪个参照」而不是直接报错
  · 双网元同名对象配置不同，必须按 EXP 维度校验
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, '/Users/alesc/workspace/mml-gen-lite/workflow/stage3')
import ref_validate as RV

GT = json.loads(Path('/tmp/gt_cleaned.json').read_text(encoding='utf-8'))
GT_MAP = {g['ticket']: g for g in GT}

TK = 'NC20260810002261'
g = GT_MAP[TK]
adir = Path(g['path']) / '备份附件'
UNC = next((p for p in adir.glob('*.txt') if '_UNC_' in p.name), None)
UDG = next((p for p in adir.glob('*.txt') if '_UDG_' in p.name), None)

# sos 的 RULE 实际参数集（从 GT 提取）
TARGET_RULE = set()
for _, _, fam, params, raw in g['kept']:
    if fam == 'RULE' and 'sos_sig_f_f' in raw:
        TARGET_RULE = set(params.keys())
        break
if not TARGET_RULE:
    TARGET_RULE = {'RULENAME', 'POLICYTYPE', 'PRIORITY', 'POLICYNAME',
                   'FLOWFILTERNAME', 'FILTERINGMODE', 'RULESPECTYPE'}

results = []


def check(name, cond, detail=''):
    results.append((name, bool(cond), detail))
    print(f'  {"✅" if cond else "❌"} {name}' + (f'  —— {detail}' if detail else ''))


def main():
    print('=' * 92)
    print('参照对象结构校验（P0-2）功能验证')
    print('=' * 92)
    print(f'  目标参数集（sos RULE）: {sorted(TARGET_RULE)}')

    # ══ V1 参数覆盖检查 ══
    print('\n【V1】参数覆盖检查')
    r = RV.validate_reference_structure(
        [str(UNC), str(UDG)], 'RULE', 'r_ims_sig', target_params=TARGET_RULE)
    check('V1-1 无错误返回', not r.get('error'))
    # r_ims_sig 在 UNC 缺 FLOWFILTERNAME，在 UDG 有 → 应选 UDG 版本，通过
    check('V1-2 同名对象选最匹配版本（UDG 版参数齐全）',
          r['ok'], f"ok={r['ok']} 用的版本={r.get('ref_used_exp')}")
    check('V1-3 标出了所有版本',
          len(r.get('ref_versions') or []) == 2,
          f"{[(v['exp'][:20], v['n_params']) for v in (r.get('ref_versions') or [])]}")

    # 反例：用一个确定缺参数的参照
    r2 = RV.validate_reference_structure(
        str(UNC), 'RULE', 'r_ims_sig', target_params=TARGET_RULE)
    check('V1-4 只给 UNC 时检出缺参数',
          not r2['ok'] and 'FLOWFILTERNAME' in str(r2.get('missing')),
          f"missing={r2.get('missing')}")

    # ══ V2 换参照建议 ══
    print('\n【V2】换参照建议')
    # ★ 2026-11-12 修正用例语义：
    #   单 EXP 校验只能在该 EXP 内找候选（UNC 里确实没有全参数的 RULE）
    #   所以 V2 测的是「跨 EXP 时能否给出带 in_exp 的候选」
    r2b = RV.validate_reference_structure(
        [str(UNC), str(UDG)], 'RULE', 'r_ims_sig', target_params=TARGET_RULE)
    better = r2b.get('better_candidates') or []
    check('V2-1 跨 EXP 时给出换参照候选', len(better) >= 1,
          f'{len(better)} 个: {[(b["name"], b.get("in_exp")[:12]) for b in better[:2]]}')
    if better:
        c0 = better[0]
        check('V2-2 候选参数集覆盖目标', TARGET_RULE <= set(c0['params']),
              f'{c0["name"]} 参数 {len(c0["params"])} 个')
        check('V2-3 候选标出了所在 EXP', bool(c0.get('in_exp')),
              f"in_exp={c0.get('in_exp', '')[:40]}")

    # 单 EXP 时不该凭空跨库找
    r2c = RV.validate_reference_structure(
        str(UNC), 'RULE', 'r_ims_sig', target_params=TARGET_RULE)
    check('V2-4 单 EXP 校验不跨库找候选',
          all('UDG' not in (b.get('in_exp') or '')
              for b in (r2c.get('better_candidates') or [])),
          f'候选 EXP: {[b.get("in_exp", "")[:20] for b in (r2c.get("better_candidates") or [])]}')

    # ══ V3 形态代表性 ══
    print('\n【V3】形态代表性检查')
    # 构造一个极端稀有的参照：UNC 里带 FLOWFILTERNAME 的只有 3 个（0.4%）
    info_unc = RV.collect_family_param_sets(UNC, 'RULE')
    rare_name = None
    for nm, ps in info_unc['names'].items():
        if 'FLOWFILTERNAME' in ps and 'RULERANGE' in ps:
            rare_name = nm
            break
    if rare_name:
        r3 = RV.validate_reference_structure(
            str(UNC), 'RULE', rare_name, target_params=TARGET_RULE)
        check('V3-1 稀有形态能检出',
              any('特例' in i or '只有' in i for i in r3.get('issues') or []),
              f'issues={r3.get("issues")}')
        check('V3-2 稀有形态的占比 < 2%',
              r3['ref_shape_share'] < 0.02,
              f'{r3["ref_shape_share"]*100:.1f}%')
    else:
        print('  ⊘ 没找到稀有形态样本')

    # ══ V4 目标参数推断 ══
    print('\n【V4】从意图推断目标参数')
    CASES = [
        ('新增 规则（过滤模式为FLOWFILTER）；新增 流过滤器',
         {'FLOWFILTERNAME', 'FILTERINGMODE'}),
        ('新增 APN配置（APN 名称为sos）', {'APN'}),
        ('调整 地址池（地址池名称为pool_x）', {'POOLNAME'}),
    ]
    ok_n = 0
    for text, expect in CASES:
        got = RV.infer_target_params_from_intent(text)
        if expect <= got:
            ok_n += 1
        else:
            print(f'      "{text[:30]}": 期望含 {expect}，实际 {got}')
    check('V4-1 意图参数推断正确', ok_n == len(CASES), f'{ok_n}/{len(CASES)}')

    # 反例：不提任何参数
    r4 = RV.infer_target_params_from_intent('调整 PLMN')
    check('V4-2 无参数线索时返回空', len(r4) == 0, f'{r4}')

    # ══ V5 边界 ══
    print('\n【V5】边界')
    r5 = RV.validate_reference_structure(str(UNC), 'NOSUCHFAMILY', 'x')
    check('V5-1 不存在的族 → skipped', r5.get('skipped'), r5.get('reason', '')[:40])

    r6 = RV.validate_reference_structure(str(UNC), 'RULE', 'no_such_rule')
    check('V5-2 不存在的参照 → 报错不崩',
          not r6['ok'] and any('不在' in i for i in (r6.get('issues') or [])),
          str(r6.get('issues'))[:60])

    # ══ V6 真实场景：sos 该用哪个参照 ══
    print('\n【V6】真实场景：sos 的 RULE 该参照谁')
    r7 = RV.validate_reference_structure(
        [str(UNC), str(UDG)], 'RULE', 'r_ims_sig', target_params=TARGET_RULE)
    if r7['ok']:
        print(f'  → 用 r_ims_sig（{r7.get("ref_used_exp")} 版本）')
        check('V6-1 r_ims_sig 可用于参照', True,
              f'形态占比 {r7["ref_shape_share"]*100:.0f}%')
    else:
        print(f'  → 需换参照：{[b["name"] for b in (r7.get("better_candidates") or [])[:2]]}')
        check('V6-1 给出了替代方案',
              bool(r7.get('better_candidates')),
              f'缺 {r7.get("missing")}')

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
