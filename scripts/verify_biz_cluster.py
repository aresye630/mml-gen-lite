#!/usr/bin/env python3
"""业务段簇分析（P0-1）功能验证。

验证目标：
  1. 业务段识别：从参照对象名列表里提取出正确的业务段
  2. 簇成员发现：用业务段找到完整簇（按 token 边界，无误报）
  3. 名字平移：只替换业务段，骨架不变
  4. 骨架校验：平移正确时通过，破坏骨架时检出
  5. 命名形态校验：抓出「骨架对但形态不符」的情况（UPBINDUPG）
  6. 真实还原：ims_sig 链 → sos 链，与 GT 逐条对比

判据设计原则（用户裁定）：
  · 平移后名字 = 参照名只换业务段 → 骨架校验必须通过
  · 骨架通过后，再看该族现网主流形态是否接受这个前缀/后缀
  · 两层都过 → ok
    骨架过但形态不符 → 标「待确认」（不阻断）
    骨架被破坏 → 报错
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, '/Users/alesc/workspace/mml-gen-lite/workflow/stage3')
import biz_cluster as B

GT = json.loads(Path('/tmp/gt_cleaned.json').read_text(encoding='utf-8'))
GT_MAP = {g['ticket']: g for g in GT}

TK = 'NC20260810002261'
g = GT_MAP[TK]
adir = Path(g['path']) / '备份附件'
UNC = next((p for p in adir.glob('*.txt') if '_UNC_' in p.name), None)

results = []


def check(name, cond, detail=''):
    results.append((name, bool(cond), detail))
    print(f'  {"✅" if cond else "❌"} {name}' + (f'  —— {detail}' if detail else ''))


def main():
    print('=' * 90)
    print('业务段簇分析（P0-1）功能验证')
    print('=' * 90)
    print(f'  EXP: {UNC.name[:70]}')

    # ══ V1 业务段识别 ══
    print('\n【V1】业务段识别')
    SEED = ['ims_sig_cbb_offline', 'ims_sig_cbb_online', 'ims_sig_ch_p',
            'ims_sig_pcc_p_g', 'r_ims_sig', 'up_ims', 'upg_ims']
    biz, cands = B.extract_biz_segment(SEED)
    check('V1-1 识别出业务段', biz is not None, f'biz={biz!r}')
    check('V1-2 业务段是 ims', biz == 'ims', f'实际 {biz!r}')

    # 反例：没有共同业务段的名字
    biz2, _ = B.extract_biz_segment(['abc_001', 'xyz_002', 'qqq_003'])
    check('V1-3 无共同业务段时返回 None', biz2 is None, f'biz={biz2!r}')

    # 通用词不应被识别为业务段
    biz3, _ = B.extract_biz_segment(['a_online', 'b_online', 'c_online'])
    check('V1-4 通用词 online 不当业务段',
          biz3 != 'online', f'biz={biz3!r}')

    # ══ V2 簇成员发现 ══
    print('\n【V2】簇成员发现')
    cluster = B.find_cluster_members(str(UNC), biz)
    check('V2-1 找到多个族', len(cluster) >= 5, f'{len(cluster)} 个族')

    # 应包含的核心族
    core = ['URR', 'URRGROUP', 'PCCPOLICYGRP', 'RULE', 'USERPROFILE',
            'RULEBINDING', 'UPBINDUPG']
    missing_core = [f for f in core if f not in cluster]
    check('V2-2 包含计费链核心族', not missing_core,
          f'缺: {missing_core}' if missing_core else '7 个核心族都有')

    # 不应包含误报族（IMSI 相关）
    false_pos = ['GBIMEICFG', 'IUIMEICFG', 'S1IMEICFG', 'IMSISMCHAR']
    caught = [f for f in false_pos if f in cluster]
    check('V2-3 无误报（IMSI 类不该被当成 ims）', not caught,
          f'误报: {caught}' if caught else 'IMSI_PREFIX 相关族已排除')

    # ══ V3 名字平移 ══
    print('\n【V3】名字平移（业务段替换）')
    CASES = [
        ('ims_sig_cbb_offline', 'sos_sig_cbb_offline'),
        ('ims_sig_ch_p',        'sos_sig_ch_p'),
        ('r_ims_sig',           'r_sos_sig'),
        ('up_ims',              'up_sos'),
        ('ims.wh',              'sos.wh'),
    ]
    ok_n = 0
    for ref, expect in CASES:
        got = B.translate_name(ref, 'ims', 'sos')
        if got == expect:
            ok_n += 1
        else:
            print(f'      {ref}: 期望 {expect} 实际 {got}')
    check('V3-1 平移结果正确', ok_n == len(CASES), f'{ok_n}/{len(CASES)}')

    # 子串不误伤
    check('V3-2 不误伤子串（imsims 里的 ims 不该被替换）',
          B.translate_name('imsims_x', 'ims', 'sos') == 'imsims_x',
          f"实际 {B.translate_name('imsims_x', 'ims', 'sos')}")

    # 大小写保持
    check('V3-3 保持大小写',
          B.translate_name('IMS_SIG', 'ims', 'sos') == 'SOS_SIG',
          f"实际 {B.translate_name('IMS_SIG', 'ims', 'sos')}")

    # ══ V4 骨架校验 ══
    print('\n【V4】骨架校验')
    r = B.check_skeleton_preserved('r_ims_sig', 'r_sos_sig', 'ims', 'sos')
    check('V4-1 正确平移时骨架保持', r['ok'], r['reason'][:50])

    r = B.check_skeleton_preserved('r_ims_sig', 'r_sos_xx', 'ims', 'sos')
    check('V4-2 骨架被破坏时检出', not r['ok'], r['reason'][:60])

    # ══ V5 命名形态校验（抓 UPBINDUPG）══
    print('\n【V5】命名形态校验')
    # 应通过：后缀明确的族
    for fam, name in [('URRGROUP', 'sos_sig_ch_p'),
                      ('PCCPOLICYGRP', 'sos_sig_pcc_p_g')]:
        r = B.check_name_against_pattern(fam, name, str(UNC))
        check(f'V5 {fam} {name} 通过', r['ok'], r['reason'][:55])

    # 应给出警告：UPBINDUPG 的 upg_ 前缀只占 6.2%，主流是 up_group_
    r = B.check_name_against_pattern('UPBINDUPG', 'upg_sos', str(UNC))
    check('V5 UPBINDUPG upg_sos 被标形态不符', not r['ok'],
          r['reason'][:70])

    # 建议值应包含 up_group_
    if not r['ok']:
        check('V5-2 建议值指向 up_group_',
              'up_group_' in (r.get('suggested') or ''),
              f"suggested={r.get('suggested')}")

    # ══ V6 真实还原对比 GT ══
    print('\n【V6】真实还原：ims_sig 链 → sos 链，与 GT 对比')
    REF_CHAIN = {
        'URR':        ['ims_sig_cbb_offline', 'ims_sig_cbb_online'],
        'URRGROUP':   ['ims_sig_ch_p'],
        'PCCPOLICYGRP': ['ims_sig_pcc_p_g'],
        'RULE':       ['r_ims_sig'],
        'USERPROFILE': ['up_ims'],
        'UPBINDUPG':  ['upg_ims'],
    }
    gt_all = {f for _, _, f, _, _ in g['kept']}
    gt_names = set()
    for _, _, fam, params, raw in g['kept']:
        if fam in REF_CHAIN and 'sos' in raw:
            gt_names.add(raw.split(':')[1].strip().split(',')[0].split('=')[1].strip('" ;'))

    ok_cnt = 0
    total_cnt = 0
    for fam, refs in REF_CHAIN.items():
        for ref in refs:
            total_cnt += 1
            new = B.translate_name(ref, 'ims', 'sos')
            # 检查生成的族在 GT 里有
            fam_in_gt = fam in gt_all
            # 检查名字是否在 GT 里出现
            in_gt = any(new in raw for _, _, f, _, raw in g['kept'] if f == fam)
            if fam_in_gt and in_gt:
                ok_cnt += 1
                print(f'      ✅ {fam:<16} {new}')
            else:
                print(f'      ⚠ {fam:<16} {new}  (GT 族={fam_in_gt}, 名字命中={in_gt})')

    check('V6-1 还原的族名在 GT 里命中率 >= 5/7',
          ok_cnt >= 5, f'{ok_cnt}/{total_cnt}')

    # ══ 汇总 ══
    print('\n' + '=' * 90)
    ok = sum(1 for _, c, _ in results if c)
    print(f'结果: {ok}/{len(results)} 通过')
    fails = [(n, d) for n, c, d in results if not c]
    if fails:
        print('\n失败项：')
        for n, d in fails:
            print(f'  ❌ {n}  {d}')
    else:
        print('✅ 全部通过')
    print('=' * 90)
    return 0 if ok == len(results) else 1


if __name__ == '__main__':
    sys.exit(main())
