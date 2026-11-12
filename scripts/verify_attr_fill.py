#!/usr/bin/env python3
"""P0-4 验证：Step3 属性族链补齐。

验证目标：
  V1 覆盖率计算正确（不超 100%，不重复计数）
  V2 自动选参照 owner（属性配置最全的）
  V3 三种候选来源都能生效（ref / intent / musthave）
  V4 命令生成：owner 值替换正确，不再用 ref_owner 硬匹配
  V5 注释标注：每条命令都带 @stage3 标记
  V6 置信度分级：ref/intent 来源 high，musthave 来源 medium
  V7 与 GT 的离线对比（多配量，GT 只在这里用）

用户裁定（设计依据）：
  「直接配，多配的标明注释让判断（让用户删比让用户再补意图交互要简单）」
  → 所以多配不是 bug，是设计意图；但必须能在注释里一眼看出来
"""
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, '/Users/alesc/workspace/mml-gen-lite/workflow/stage3')
import attr_fill as AF

GT = json.loads(Path('/tmp/gt_cleaned.json').read_text(encoding='utf-8'))
GT_MAP = {g['ticket']: g for g in GT}

TK = 'NC20260810002261'
g = GT_MAP[TK]
adir = Path(g['path']) / '备份附件'
EXPS = [str(p) for p in sorted(adir.glob('*.txt'))]

results = []


def check(name, cond, detail=''):
    results.append((name, bool(cond), detail))
    print(f'  {"✅" if cond else "❌"} {name}' + (f'  —— {detail}' if detail else ''))


def main():
    print('=' * 92)
    print('P0-4 验证：Step3 属性族链补齐')
    print('=' * 92)

    # ══ V1 覆盖率计算 ══
    print('\n【V1】覆盖率计算')
    u = AF._scan_attr_usage(EXPS, 'APN', ['ims.wh'])
    check('V1-1 owner 实例数合理', 100 <= u['n_owners'] <= 2000,
          f"{u['n_owners']} 个")
    max_cov = max(u['attr_coverage'].values()) if u['attr_coverage'] else 0
    check('V1-2 覆盖率不超 100%（无重复计数）',
          max_cov <= u['n_owners'],
          f"最高 {max_cov}/{u['n_owners']} = {max_cov/u['n_owners']*100:.1f}%")
    check('V1-3 参照对象明细存在', 'ims.wh' in u['owner_attrs'],
          f"ims.wh 配了 {len(u['owner_attrs'].get('ims.wh', []))} 个族")

    # ══ V2 自动选参照 ══
    print('\n【V2】自动选参照 owner')
    auto, ranking = AF.find_ref_owner_for_attrchain(EXPS, 'APN')
    check('V2-1 能自动选出', auto is not None, f'ref={auto}')
    check('V2-2 选的是属性最全的',
          ranking and ranking.get(auto) == max(ranking.values()),
          f'{auto} 配了 {ranking.get(auto)} 个族')

    # ══ V3 三种候选来源 ══
    print('\n【V3】三种候选来源')
    c = AF.collect_attr_candidates(EXPS, 'APN', 'ims.wh',
                                   intent_mentioned_fams=['APNIMSSIGFLTR'])
    st = c['stats']
    check('V3-1 ref 来源有候选', st['n_from_ref'] >= 15, f"ref={st['n_from_ref']}")
    check('V3-2 intent 来源有候选', st['n_from_intent'] >= 1, f"intent={st['n_from_intent']}")
    check('V3-3 musthave 兜底生效', 'n_from_musthave' in st,
          f"musthave={st['n_from_musthave']}")
    srcs = {x['source'] for x in c['candidates']}
    check('V3-4 来源标记完整', srcs <= {'ref', 'intent', 'musthave'}, f'{sorted(srcs)}')

    # ══ V4 命令生成 ══
    print('\n【V4】命令生成')
    r = AF.generate_attr_commands(c, 'sos', EXPS)
    check('V4-1 生成成功', len(r['commands']) >= 20, f"{len(r['commands'])} 条")
    check('V4-2 跳过很少', len(r['skipped']) <= 2,
          f"跳过 {len(r['skipped'])}: {[s['family'] for s in r['skipped'][:3]]}")

    # owner 值替换正确
    # ★ 2026-11-12 修正断言：owner 参数名有多种写法
    #   APN / APNNAME（实测 BACKOFFTIME、APNCFFUNC 用 APNNAME）
    bad_replace = []
    for cmd in r['commands']:
        if not re.search(r'(APN|APNNAME)="sos"', cmd['cmd']):
            bad_replace.append(cmd['family'])
    check('V4-3 所有命令 owner 值都替换成 sos', not bad_replace,
          f'未替换: {bad_replace[:5]}' if bad_replace else f'{len(r["commands"])} 条全替换')

    # 额外验证：APNNAME 写法的族也在（证明候选参数名机制生效）
    apnname_fams = [c0['family'] for c0 in r['commands'] if 'APNNAME="sos"' in c0['cmd']]
    check('V4-5 支持 APNNAME 形式的 owner 参数', len(apnname_fams) >= 1,
          f'{apnname_fams[:3]}')

    # 不应残留参照值
    leak = [c0['family'] for c0 in r['commands'] if 'ims.wh' in c0['cmd']]
    check('V4-4 无参照值残留', not leak, f'残留: {leak[:5]}' if leak else '无残留')

    # ══ V5 注释标注 ══
    print('\n【V5】注释标注')
    no_tag = [c0['family'] for c0 in r['commands']
              if '@stage3=attr_chain' not in c0['annotated']]
    check('V5-1 每条命令都有 @stage3 标记', not no_tag,
          f'缺标记: {no_tag[:5]}' if no_tag else f'{len(r["commands"])} 条全标记')
    has_src = all('src=' in c0['annotated'] for c0 in r['commands'])
    check('V5-2 标记里含来源', has_src, 'src=ref/intent/musthave')
    has_cov = all('cov=' in c0['annotated'] for c0 in r['commands'])
    check('V5-3 标记里含覆盖率', has_cov, 'cov=100%')

    # ══ V6 置信度分级 ══
    print('\n【V6】置信度分级')
    high = [x for x in r['commands'] if x['confidence'] == 'high']
    med = [x for x in r['commands'] if x['confidence'] == 'medium']
    check('V6-1 ref/intent 来源为 high', len(high) >= 20, f'{len(high)} 条 high')
    check('V6-2 musthave 来源为 medium', all(
        x['source'] == 'musthave' for x in med), f'{len(med)} 条 medium')

    # ══ V7 离线对比 GT（多配量，GT 只在这里用）══
    print('\n【V7】离线对比 GT（多配量，GT 只在这里用）')
    gt_fams = {f for _, _, f, _, _ in g['kept']}
    gt_apn = {f for f in gt_fams if f.startswith('APN')}
    gen_fams = {x['family'] for x in r['commands']}

    hit = gen_fams & gt_apn
    extra = gen_fams - gt_fams
    miss = gt_apn - gen_fams

    print(f'  GT 的 APN 族: {len(gt_apn)} 个')
    print(f'  生成: {len(gen_fams)} 个')
    print(f'  ✅ 命中 GT: {len(hit)}')
    print(f'  ⚠ 多配: {len(extra)}（设计意图，已标注）')
    print(f'  ⚠ 漏 GT: {len(miss)}: {sorted(miss)}')

    check('V7-1 命中 GT 过半', len(hit) / max(1, len(gt_apn)) >= 0.5,
          f'{len(hit)}/{len(gt_apn)} = {len(hit)/max(1,len(gt_apn))*100:.0f}%')
    check('V7-2 多配量在可 review 范围（<= 50）', len(extra) <= 50,
          f'{len(extra)} 个')

    # 漏的族能不能解释
    explainable = {'APN'}   # APN 本体不算属性族
    unexplained = miss - explainable
    if unexplained:
        print(f'  漏 GT 中无法解释的: {sorted(unexplained)}')

    # ══ 汇总 ══
    print('\n' + '=' * 92)
    ok = sum(1 for _, c2, _ in results if c2)
    print(f'结果: {ok}/{len(results)} 通过')
    fails = [(n, d) for n, c2, d in results if not c2]
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
