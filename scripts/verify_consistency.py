#!/usr/bin/env python3
"""P0-5 验证：Step4 三级一致性 + Step5 判据核对。

验证目标：
  V1 三级一致性的 4 类问题都能检出
     · plan_missing_in_csv    规划有 csv 无
     · csv_missing_in_mml     csv 有 mml 无
     · mml_extra_not_in_csv   mml 有 csv 无（绕过单一数据源）
     · skipped_but_generated  标跳过但产物有
  V2 判据分类正确（auto / data / report 三类）
  V3 修复计划合成正确
  V4 自动修复只做确定性的事：
     · F3 删跳过族的行 ✅ 做
     · mml 多余的族    ❌ 不自动删（可能是有意的）
  V5 真实工单的三级一致性
  V6 边界：空文件 / 不存在的文件 不崩
"""
import json
import sys
from pathlib import Path

sys.path.insert(0, '/Users/alesc/workspace/mml-gen-lite/workflow/stage3')
import consistency as CS

GT = json.loads(Path('/tmp/gt_cleaned.json').read_text(encoding='utf-8'))
GT_MAP = {g['ticket']: g for g in GT}

results = []


def check(name, cond, detail=''):
    results.append((name, bool(cond), detail))
    print(f'  {"✅" if cond else "❌"} {name}' + (f'  —— {detail}' if detail else ''))


HEADER = ('| # | 数据清单表 | 业务对象 | 对象数量 | 现网已有 | 命令族 | '
          '动作 | 判断依据 | 状态 |\n|---|---|---|---|---|---|---|---|---|\n')


def make_plan(rows):
    body = ''
    for i, (fam, st) in enumerate(rows, 1):
        body += f'| {i} | 表{i} | 对象{i} | 1 | 0 | {fam} | 新增 | 依据 | {st} |\n'
    return '# 命令族规划\n\n## 总览\n' + HEADER + body


def make_csv(rows):
    out = '序号,组,网元,命令族,参数,值,占位符,来源,说明\n'
    for i, (grp, fam, pname, pval) in enumerate(rows, 1):
        out += f'{i},{grp},UNC,{fam},{pname},{pval},,test,\n'
    return out


def main():
    print('=' * 92)
    print('P0-5 验证：Step4 三级一致性 + Step5 判据核对')
    print('=' * 92)

    tmp = Path('/tmp/p05_verify')
    tmp.mkdir(exist_ok=True)

    # ══ V1 四类一致性问题 ══
    print('\n【V1】三级一致性的四类问题')

    # C1 规划有 csv 无
    plan = make_plan([('ADD POOLGROUP', '确认'), ('ADD USERPROFILE', '确认')])
    csv_text = make_csv([('g1', 'POOLGROUP', 'POOLGROUPNAME', 'p1')])   # 缺 USERPROFILE
    mml = 'ADD POOLGROUP: POOLGROUPNAME="p1";'
    (tmp / 'c1.csv').write_text(csv_text, encoding='utf-8')
    r = CS.check_three_way_consistency(plan, str(tmp / 'c1.csv'), mml)
    c1 = [i for i in r['issues'] if i['type'] == 'plan_missing_in_csv']
    check('V1-1 检出「规划有 csv 无」', len(c1) == 1,
          f'{c1[0]["families"] if c1 else "未检出"}')

    # C2 csv 有 mml 无
    plan2 = make_plan([('ADD POOLGROUP', '确认'), ('ADD USERPROFILE', '确认')])
    csv2 = make_csv([('g1', 'POOLGROUP', 'POOLGROUPNAME', 'p1'),
                     ('g2', 'USERPROFILE', 'USERPROFILENAME', 'u1')])
    mml2 = 'ADD POOLGROUP: POOLGROUPNAME="p1";'    # 缺 USERPROFILE
    (tmp / 'c2.csv').write_text(csv2, encoding='utf-8')
    r2 = CS.check_three_way_consistency(plan2, str(tmp / 'c2.csv'), mml2)
    c2 = [i for i in r2['issues'] if i['type'] == 'csv_missing_in_mml']
    check('V1-2 检出「csv 有 mml 无」', len(c2) == 1,
          f'{c2[0]["families"] if c2 else "未检出"}')

    # C3 mml 有 csv 无（绕过单一数据源）
    plan3 = make_plan([('ADD POOLGROUP', '确认')])
    csv3 = make_csv([('g1', 'POOLGROUP', 'POOLGROUPNAME', 'p1')])
    mml3 = 'ADD POOLGROUP: POOLGROUPNAME="p1";\nADD FILTER: FILTERNAME="f1";'
    (tmp / 'c3.csv').write_text(csv3, encoding='utf-8')
    r3 = CS.check_three_way_consistency(plan3, str(tmp / 'c3.csv'), mml3)
    c3 = [i for i in r3['issues'] if i['type'] == 'mml_extra_not_in_csv']
    check('V1-3 检出「mml 有 csv 无」（绕过单一数据源）', len(c3) == 1,
          f'{c3[0]["families"] if c3 else "未检出"}')

    # C4 标跳过但产物有
    plan4 = make_plan([('ADD POOLGROUP', '确认'), ('RMV FILTER', '跳过')])
    csv4 = make_csv([('g1', 'POOLGROUP', 'POOLGROUPNAME', 'p1'),
                     ('g2', 'FILTER', 'FILTERNAME', 'f1')])
    mml4 = 'ADD POOLGROUP: POOLGROUPNAME="p1";\nRMV FILTER: FILTERNAME="f1";'
    (tmp / 'c4.csv').write_text(csv4, encoding='utf-8')
    r4 = CS.check_three_way_consistency(plan4, str(tmp / 'c4.csv'), mml4)
    c4 = [i for i in r4['issues'] if i['type'] == 'skipped_but_generated']
    check('V1-4 检出「标跳过但产物有」', len(c4) == 1,
          f'{c4[0]["families"] if c4 else "未检出"}')

    # 全一致时 ok=True
    plan5 = make_plan([('ADD POOLGROUP', '确认')])
    csv5 = make_csv([('g1', 'POOLGROUP', 'POOLGROUPNAME', 'p1')])
    mml5 = 'ADD POOLGROUP: POOLGROUPNAME="p1";'
    (tmp / 'c5.csv').write_text(csv5, encoding='utf-8')
    r5 = CS.check_three_way_consistency(plan5, str(tmp / 'c5.csv'), mml5)
    check('V1-5 全一致时 ok=True', r5['ok'], f'issues={len(r5["issues"])}')

    # ══ V2 判据分类 ══
    print('\n【V2】判据分类（auto / data / report）')
    GUARD = {
        'G30_rmv': {'ok': False, 'reversed': [{'family': 'POOL', 'n_add': 2}]},
        'G31_plan_wildcard': {'ok': False, 'hits': [{'row': '2', 'fam_cell': 'SET APN*'}]},
        'G22_placeholder': {'ok': False, 'warnings': ['3 个占位符']},
        'G18_coverage': {'ok': False, 'missing': ['PRIORITY']},
        'G27_unable': {'ok': False, 'issues': ['需要 UNC 数据']},
        'G17_scale': {'ok': False, 'problems': ['数量不符']},
        'G11_unique': {'ok': True},
        'G12_param_fmt': {'skipped': True},
    }
    cls = CS.classify_guard_warns(GUARD)
    auto_ids = {x['id'] for x in cls['auto_fixable']}
    data_ids = {x['id'] for x in cls['need_data']}
    report_ids = {x['id'] for x in cls['report_only']}

    check('V2-1 auto 类正确', auto_ids == {'G30_rmv', 'G31_plan_wildcard'},
          f'{sorted(auto_ids)}')
    check('V2-2 data 类正确', data_ids == {'G22_placeholder', 'G18_coverage'},
          f'{sorted(data_ids)}')
    check('V2-3 report 类正确', report_ids == {'G27_unable', 'G17_scale'},
          f'{sorted(report_ids)}')
    check('V2-4 ok 的判据被跳过', 'G11_unique' not in (auto_ids | data_ids | report_ids))
    check('V2-5 skipped 的判据被跳过', 'G12_param_fmt' not in (auto_ids | data_ids | report_ids))
    check('V2-6 all_ok 标记正确', cls['all_ok'] is False)

    # ══ V3 修复计划 ══
    print('\n【V3】修复计划合成')
    fp = CS.build_fix_plan(r4, cls)
    check('V3-1 must_fix 含一致性问题', fp['summary']['n_must'] >= 1,
          f'{fp["summary"]["n_must"]} 项')
    check('V3-2 should_fix 含 auto+data', fp['summary']['n_should'] == 4,
          f'{fp["summary"]["n_should"]} 项')
    check('V3-3 report 含只报项', fp['summary']['n_report'] == 2,
          f'{fp["summary"]["n_report"]} 项')
    check('V3-4 每项都有 action', all(m.get('action') for m in fp['must_fix']),
          f'{len(fp["must_fix"])} 项')

    # ══ V4 自动修复只做确定性的事 ══
    print('\n【V4】自动修复的边界')
    plan6 = make_plan([('ADD POOLGROUP', '确认'), ('RMV FILTER', '跳过')])
    csv6 = make_csv([('g1', 'POOLGROUP', 'POOLGROUPNAME', 'p1'),
                     ('g2', 'FILTER', 'FILTERNAME', 'f1')])
    (tmp / 'c6.csv').write_text(csv6, encoding='utf-8')
    af = CS.apply_auto_fixes(str(tmp / 'c6.csv'), plan6, str(tmp / 'c6.csv'))
    fix_ids = {f['id'] for f in af['fixes']}
    check('V4-1 F3 删除跳过族', 'F3' in fix_ids, f'{[f["detail"] for f in af["fixes"]]}')
    check('V4-2 F1 重跑生成器', 'F1' in fix_ids, f'{len(af["new_text"])} 字')

    # 修复后的 csv 里不该有 FILTER
    rows_after = CS.read_params_csv(str(tmp / 'c6.csv'))
    fams_after = {r['family'] for r in rows_after}
    check('V4-3 修复后 FILTER 已删', 'FILTER' not in fams_after, f'{sorted(fams_after)}')
    check('V4-4 POOLGROUP 保留', 'POOLGROUP' in fams_after)

    # 另一条：mml 多余的族不应被自动删
    plan7 = make_plan([('ADD POOLGROUP', '确认')])
    csv7 = make_csv([('g1', 'POOLGROUP', 'POOLGROUPNAME', 'p1')])
    (tmp / 'c7.csv').write_text(csv7, encoding='utf-8')
    af7 = CS.apply_auto_fixes(str(tmp / 'c7.csv'), plan7, str(tmp / 'c7.csv'))
    rows7 = CS.read_params_csv(str(tmp / 'c7.csv'))
    check('V4-5 不自动删「规划表没有的族」', len(rows7) == 1,
          f'保留 {len(rows7)} 行（不应清空）')

    # ══ V5 真实工单 ══
    print('\n【V5】真实工单三级一致性')
    TK = 'NC20260810002261'
    d = Path(f'/tmp/eval_versions_out/V3/{TK}')
    plan_p = d / '命令族规划.md'
    mml_p = d / 'mml.txt'
    csv_p = d / 'params.csv'
    if plan_p.exists() and mml_p.exists():
        ptxt = plan_p.read_text(encoding='utf-8')
        mtxt = mml_p.read_text(encoding='utf-8')
        if csv_p.exists():
            r6 = CS.check_three_way_consistency(ptxt, str(csv_p), mtxt)
            print(f'  统计: {r6["stats"]}')
            check('V5-1 真实工单能检查（不崩）', True,
                  f'{len(r6["issues"])} 个问题')
            for iss in r6['issues']:
                print(f'    [{iss["level"]}] {iss["detail"]}')
        else:
            print(f'  ⊘ params.csv 不存在，跳过')
    else:
        print(f'  ⊘ 产物不存在，跳过')

    # ══ V6 边界 ══
    print('\n【V6】边界')
    r7 = CS.check_three_way_consistency('', '/nonexistent.csv', '')
    check('V6-1 空输入不崩', isinstance(r7, dict), f'ok={r7["ok"]}')

    af8 = CS.apply_auto_fixes('/nonexistent.csv', '', '/tmp/x.csv')
    check('V6-2 不存在的 csv 不崩', isinstance(af8, dict),
          f'skipped={len(af8.get("skipped") or [])}')

    # ══ 汇总 ══
    print('\n' + '=' * 92)
    ok = sum(1 for _, c, _ in results if c)
    print(f'结果: {ok}/{len(results)} 通过')
    fails = [(n, dd) for n, c, dd in results if not c]
    if fails:
        print('\n失败项：')
        for n, dd in fails:
            print(f'  ❌ {n}  {dd}')
    else:
        print('✅ 全部通过')
    print('=' * 92)
    return 0 if ok == len(results) else 1


if __name__ == '__main__':
    sys.exit(main())
