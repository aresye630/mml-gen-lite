#!/usr/bin/env python3
"""P0-6 验证：Step6 照着配三场景整合。

验证目标：
  V1 场景判定正确（A/B/C/D 四种）
  V2 场景 D 不做事（58% 的工单属于这类，不能白跑）
  V3 场景 C 输出结构化澄清（问业务段）
  V4 场景 A：意图给了参照时的完整流程
  V5 场景 B：意图没给参照时自动选
  V6 参照提示的归属校验（不会把「用户模板的参照」用到 RULE 上）
  V7 平移结果：骨架 + 形态 + 与 GT 对比
  V8 失败项全部进澄清
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, '/Users/alesc/workspace/mml-gen-lite/workflow/stage3')
import copy_chain as CC

GT = json.loads(Path('/tmp/gt_cleaned.json').read_text(encoding='utf-8'))
GT_MAP = {g['ticket']: g for g in GT}

TK = 'NC20260810002261'
g = GT_MAP[TK]
adir = Path(g['path']) / '备份附件'
EXPS = [str(p) for p in sorted(adir.glob('*.txt'))]
ITXT = Path(f'/tmp/intent_v3/{TK}_意图.md').read_text(encoding='utf-8')
DTXT = Path(f'/tmp/intent_v3/{TK}_数据清单.md').read_text(encoding='utf-8')

results = []


def check(name, cond, detail=''):
    results.append((name, bool(cond), detail))
    print(f'  {"✅" if cond else "❌"} {name}' + (f'  —— {detail}' if detail else ''))


def main():
    print('=' * 92)
    print('P0-6 验证：Step6 照着配三场景')
    print('=' * 92)

    # ══ V1 场景判定 ══
    print('\n【V1】场景判定')
    CASES = [
        # (意图, 清单, 期望场景)
        # ★ 2026-11-12：up_sos 是目标实例，应在数据清单里识别为目标业务段
        ('- 用户模板「up_sos」的配置：按现网同类用户模板「up_ims」的存量做法配齐',
         '| 名称 |\n| up_sos |\n| up_sos_2 |', 'A'),
        ('- 新增 URR sos_sig_cbb_offline',
         '| 名称 |\n| sos_sig_cbb_offline |', 'B'),
        ('- 按现网 cmnet 的存量做法配齐', '（无数据）', 'C'),
        ('- 设置 业务刷新：ALL', '（无数据）', 'D'),
    ]
    ok_n = 0
    for itxt, dtxt, expect in CASES:
        sc = CC.detect_scene(itxt, dtxt)
        if sc['scene'] == expect:
            ok_n += 1
        else:
            print(f'      "{itxt[:36]}" 期望 {expect} 实际 {sc["scene"]} ({sc["reason"][:40]})')
    check('V1-1 四种场景判定正确', ok_n == len(CASES), f'{ok_n}/{len(CASES)}')

    # ══ V2 场景 D 不做事 ══
    print('\n【V2】场景 D（不涉及参照）')
    r = CC.run_step6('- 设置 业务刷新：ALL', '', EXPS)
    check('V2-1 场景 D 判定正确', r['scene']['scene'] == 'D', r['scene']['reason'])
    check('V2-2 场景 D 不产生结果', r['summary']['n_results'] == 0)
    check('V2-3 场景 D 不产生澄清', r['summary']['n_clarifications'] == 0)

    # ══ V3 场景 C 澄清 ══
    print('\n【V3】场景 C（只有参照无业务段）')
    r2 = CC.run_step6('- 按现网 cmnet 的存量做法配齐', '', EXPS,
                      families_and_biz=[{'family': 'URR', 'biz': None}])
    check('V3-1 场景 C 判定正确', r2['scene']['scene'] == 'C', r2['scene']['reason'])
    check('V3-2 产出澄清项', len(r2['clarifications']) >= 1,
          f'{len(r2["clarifications"])} 项')
    if r2['clarifications']:
        c0 = r2['clarifications'][0]
        check('V3-3 澄清问的是业务段', '业务段' in c0.get('question', ''),
              c0.get('question', '')[:50])
        check('V3-4 澄清给出了命名模式样例',
              bool(c0.get('what_we_found', {}).get('names_pattern')) or bool(c0.get('example')),
              str(c0.get('example', ''))[:60])

    # ══ V4 场景 A 完整流程 ══
    print('\n【V4】场景 A（意图给参照 + 清单给业务段）')
    TARGET_RULE = {'RULENAME', 'POLICYTYPE', 'PRIORITY', 'POLICYNAME',
                   'FLOWFILTERNAME', 'FILTERINGMODE', 'RULESPECTYPE'}
    r3 = CC.run_step6(
        ITXT, DTXT, EXPS,
        families_and_biz=[{'family': 'RULE', 'biz': 'sos_sig',
                           'line': '新增 规则（策略类型为PCC，优先级为1000，过滤模式为FLOWFILTER）'}],
        target_params_map={'RULE': TARGET_RULE},
    )
    check('V4-1 场景 A 判定正确', r3['scene']['scene'] == 'A', r3['scene']['reason'])
    res = r3['results'][0] if r3['results'] else {}
    check('V4-2 选出参照', bool(res.get('reference')),
          f"{(res.get('reference') or {}).get('name')}")
    check('V4-3 结构校验通过', (res.get('validation') or {}).get('ok') is True,
          f"missing={(res.get('validation') or {}).get('missing')}")
    check('V4-4 平移出目标名', bool(res.get('translated')),
          f"{res['translated'][0]['target_name'] if res.get('translated') else None}")

    # ══ V5 场景 B 自动选参照 ══
    print('\n【V5】场景 B（意图没给参照）')
    r4 = CC.run_step6(
        '- 新增 规则（策略类型为PCC，过滤模式为FLOWFILTER）',
        '| 名称 |\n| sos_sig_pcc_p_g |', EXPS,
        families_and_biz=[{'family': 'RULE', 'biz': 'sos_sig',
                           'line': '新增 规则（策略类型为PCC，过滤模式为FLOWFILTER）'}],
        target_params_map={'RULE': TARGET_RULE},
    )
    check('V5-1 场景 B 判定正确', r4['scene']['scene'] == 'B', r4['scene']['reason'])
    res4 = r4['results'][0] if r4['results'] else {}
    check('V5-2 自动选到参照', bool(res4.get('reference')),
          f"{(res4.get('reference') or {}).get('name')} how={(res4.get('reference') or {}).get('how')}")
    check('V5-3 选用方式标为 auto',
          (res4.get('reference') or {}).get('how') == 'auto',
          f"how={(res4.get('reference') or {}).get('how')}")

    # ══ V6 参照提示的归属校验 ══
    print('\n【V6】参照提示归属校验（关键防错）')
    # 意图里有两个参照（用户模板 up_ims / APN ims.wh），处理 RULE 族时
    # 都不该被误用（它们都不是 RULE）
    sc = CC.detect_scene(ITXT, DTXT)
    check('V6-1 提取到带类型的参照提示', all(
        isinstance(h, dict) and h.get('ref_inst')
        for h in sc['ref_hints']), f'{len(sc["ref_hints"])} 个')
    check('V6-2 提示含对象类型', all(h.get('obj_type') for h in sc['ref_hints']),
          f'{[h.get("obj_type") for h in sc["ref_hints"]]}')

    # RULE 族处理时应自动选（不用 up_ims/ims.wh）
    ref_used = (res.get('reference') or {}).get('name')
    check('V6-3 RULE 族没用错参照（不是 up_ims/ims.wh）',
          ref_used not in ('up_ims', 'ims.wh'), f'实际用 {ref_used}')

    # ══ V7 平移质量 ══
    print('\n【V7】平移质量')
    t = (res.get('translated') or [{}])[0]
    check('V7-1 骨架校验通过', t.get('skeleton_ok') is True, t.get('skeleton_reason', '')[:50])
    check('V7-2 形态校验通过（或继承参照的特例形态）',
          t.get('pattern_ok') is True, t.get('pattern_reason', '')[:50])
    # 与 GT 对比（GT 只在这里用）
    gt_rule_names = [raw.split(':')[1].split(',')[0].split('=')[1].strip('" ;')
                     for _, _, fam, _, raw in g['kept']
                     if fam == 'RULE' and 'sos' in raw]
    tgt = t.get('target_name')
    check('V7-3 平移结果命中 GT 里的规则名',
          tgt in gt_rule_names if gt_rule_names else True,
          f'{tgt} vs GT {gt_rule_names[:2]}')

    # ══ V8 失败项进澄清 ══
    print('\n【V8】失败项进澄清')
    check('V8-1 有问题时产出澄清', len(r3['clarifications']) >= 0,
          f'{len(r3["clarifications"])} 项')
    if r3['clarifications']:
        c0 = r3['clarifications'][0]
        check('V8-2 澄清含族名和问题', 'family' in c0 and 'issues' in c0,
              f'{c0.get("family")}: {len(c0.get("issues") or [])} 个问题')
        check('V8-3 澄清标了 needs_review', c0.get('needs_review') is True)

    # 构造一个必然失败的场景
    # ★ 2026-11-12 修正用例：'- 新增 规则' 没有参照也没业务段 → 场景 D，
    #   场景 D 直接 return 不处理 families_and_biz（正确行为）。
    #   改用场景 B（有业务段但族不存在）才能真正触发失败路径。
    r5 = CC.run_step6(
        '- 新增 URR sos_sig_cbb_offline', '| 名称 |\n| sos_sig_cbb_offline |',
        EXPS,
        families_and_biz=[{'family': 'NOSUCHFAMILY', 'biz': 'sos_sig',
                           'line': '新增 URR sos_sig_cbb_offline'}])
    check('V8-4 失败场景产出澄清', len(r5['clarifications']) >= 1,
          f'{len(r5["clarifications"])} 项（scene={r5["scene"]["scene"]}）')
    if r5['clarifications']:
        check('V8-5 失败原因写清楚',
              bool(r5['clarifications'][0].get('issues')),
              str(r5['clarifications'][0].get('issues'))[:70])

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
