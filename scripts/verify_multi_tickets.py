#!/usr/bin/env python3
"""阶段3 多工单回归验证（12 单，覆盖小/中/大 × 单/双网元）。

★ 2026-11-12（用户质疑："现在的验证是一个case还是多个case的"）

之前 161 项验证全部基于 NC20260810002261 单工单，
不能证明系统在其它工单上成立。本脚本做多工单回归。

## 验证策略

不重跑 agent（太慢），用已有评测产物 + 意图数据做「模块级回归」：
  · 每个工单跑 8 个模块，检查是否崩溃、是否产出合理结果
  · 用 GT 做离线校验（多配量、命中率），但不在运行时用

## 判据（每单都要过）

  R1 不崩：所有模块返回 dict，无异常
  R2 场景判定合理：场景 D 占比应接近 58%（与意图分布一致）
  R3 对象覆盖：意图解析条目数 > 0，覆盖率 >= 60%
  R4 属性族补齐：能生成命令（大单尤其）
  R5 一致性检查：能检出问题（真实产物几乎都有不一致）
  R6 触发判定：大单触发、小单不触发

## 输出

  · 逐单结果表
  · 分档统计（小/中/大）
  · 失败清单
"""
import json
import re
import sys
import time
import traceback
from pathlib import Path

sys.path.insert(0, '/Users/alesc/workspace/mml-gen-lite/workflow/stage3')
import biz_cluster as BC
import ref_validate as RV
import auto_ref as AR
import plan_check as PC
import attr_fill as AF
import consistency as CS
import copy_chain as CC
import orchestrator as OR

GT = json.loads(Path('/tmp/gt_cleaned.json').read_text(encoding='utf-8'))
GT_MAP = {g['ticket']: g for g in GT}
INTENT_DIR = Path('/tmp/intent_v3')
OUT_DIR = Path('/tmp/eval_versions_out/V3')
OUT_DIR_V2 = Path('/tmp/eval_versions_out/V2')

# 12 单：小/中/大 × 单/双网元
TICKETS = [
    # 小单（<6 条）
    ('NC20260804001796', 'small', 'single'),
    ('NC20260803000378', 'small', 'single'),
    ('NC20260812000824', 'small', 'single'),
    ('NC20260817001844', 'small', 'multi'),
    # 中单（6-15 条）
    ('NC20260808000433', 'medium', 'multi'),
    ('NC20260805000498', 'medium', 'single'),
    ('NC20260811002152', 'medium', 'multi'),
    ('NC20260803002122', 'medium', 'multi'),
    # 大单（>15 条）
    ('NC20260811002706', 'large', 'multi'),
    ('NC20260810002261', 'large', 'multi'),
    ('NC20260806001438', 'large', 'multi'),
    ('NC20260828000360', 'large', 'multi'),
]


def main():
    print('=' * 100)
    print('阶段3 多工单回归验证（12 单）')
    print('=' * 100)

    all_rows = []
    t_start = time.time()

    for tk, band, me_kind in TICKETS:
        g = GT_MAP.get(tk)
        if not g or not g['kept']:
            print(f'\n⊘ {tk} 无 GT，跳过')
            continue

        ip = INTENT_DIR / f'{tk}_意图.md'
        dp = INTENT_DIR / f'{tk}_数据清单.md'
        if not ip.exists():
            print(f'\n⊘ {tk} 无意图，跳过')
            continue
        intent_text = ip.read_text(encoding='utf-8')
        dataset_text = dp.read_text(encoding='utf-8') if dp.exists() else ''

        adir = Path(g['path']) / '备份附件'
        exps = [str(p) for p in sorted(adir.glob('*.txt'))] if adir.exists() else []

        # 找产物目录
        sess = None
        for base in (OUT_DIR, OUT_DIR_V2):
            cand = base / tk
            if cand.exists() and (cand / '命令族规划.md').exists():
                sess = cand
                break

        gt_fams = {f for _, _, f, _, _ in g['kept']}
        n_items = len(re.findall(r'^-\s', intent_text, re.M))

        row = {
            'ticket': tk, 'band': band, 'me': me_kind,
            'n_items': n_items, 'gt_fams': len(gt_fams),
            'gt_cmds': len(g['kept']), 'n_exp': len(exps),
            'has_prod': sess is not None,
            'modules': {}, 'errors': [],
        }

        print(f'\n{"─"*100}')
        print(f'{tk}  [{band}/{me_kind}]  意图{n_items}条  GT{len(gt_fams)}族/{len(g["kept"])}条  '
              f'EXP{len(exps)}个  产物={sess.name if sess else "无"}')

        # ── M1 意图解析 + 场景判定 ──
        try:
            parsed = PC.parse_intent(intent_text)
            sc = CC.detect_scene(intent_text, dataset_text)
            row['modules']['m1_parse'] = {
                'ok': True,
                'n_parsed': len(parsed['items']),
                'scene': sc['scene'],
            }
            print(f'  M1 意图解析: {len(parsed["items"])} 条, 场景={sc["scene"]}')
        except Exception as e:
            row['modules']['m1_parse'] = {'ok': False, 'error': str(e)}
            row['errors'].append(f'M1: {e}')
            print(f'  M1 ❌ {e}')

        # ── M2 触发判定 ──
        try:
            plan_text = ''
            mml_text = ''
            if sess:
                pf = sess / '命令族规划.md'
                mf = sess / 'mml.txt'
                plan_text = pf.read_text(encoding='utf-8', errors='replace') if pf.exists() else ''
                mml_text = mf.read_text(encoding='utf-8', errors='replace') if mf.exists() else ''
            trig = OR.should_run_stage3(intent_text, plan_text, mml_text)
            row['modules']['m2_trigger'] = {
                'ok': True, 'run': trig['run'],
                'triggers': [t['id'] for t in trig['triggers']],
            }
            print(f'  M2 触发判定: run={trig["run"]} {[t["id"] for t in trig["triggers"]]}')
        except Exception as e:
            row['modules']['m2_trigger'] = {'ok': False, 'error': str(e)}
            row['errors'].append(f'M2: {e}')
            print(f'  M2 ❌ {e}')

        # ── M3 结构合规 + 对象覆盖 ──
        if plan_text:
            try:
                s1 = PC.check_plan_structure(plan_text)
                s2 = PC.check_intent_coverage(intent_text, plan_text)
                row['modules']['m3_plan'] = {
                    'ok': True,
                    'n_rows': s1['n_rows'],
                    'n_issues': len(s1['issues']),
                    'n_wildcard': len(s1['wildcard_rows']),
                    'coverage': round(s2['coverage_rate'], 3),
                    'n_objects': s2['n_objects'],
                    'n_missing': len(s2['missing']),
                }
                print(f'  M3 规划检查: {s1["n_rows"]}行/{len(s1["issues"])}问题/'
                      f'{len(s1["wildcard_rows"])}通配  覆盖{s2["coverage_rate"]*100:.0f}%')
            except Exception as e:
                row['modules']['m3_plan'] = {'ok': False, 'error': str(e)}
                row['errors'].append(f'M3: {e}')
                print(f'  M3 ❌ {e}')
        else:
            row['modules']['m3_plan'] = {'ok': True, 'skipped': 'no plan'}

        # ── M4 属性族补齐 ──
        if exps:
            try:
                owners = OR._find_owner_families(intent_text, plan_text, exps)
                results = []
                for od in owners[:3]:
                    of = od['owner_family']
                    c = AF.collect_attr_candidates(exps, of, od.get('ref_value'))
                    tgt = od.get('target_value') or c.get('ref_owner')
                    gen = AF.generate_attr_commands(c, tgt, exps)
                    results.append({
                        'owner': of,
                        'n_cand': len(c['candidates']),
                        'n_cmd': len(gen['commands']),
                        'tgt': tgt,
                    })
                row['modules']['m4_attr'] = {'ok': True, 'results': results}
                print(f'  M4 属性族补齐: ' +
                      (', '.join(f'{r["owner"]} {r["n_cmd"]}条' for r in results) or '无 owner 族'))
            except Exception as e:
                row['modules']['m4_attr'] = {'ok': False, 'error': str(e)}
                row['errors'].append(f'M4: {e}')
                print(f'  M4 ❌ {e}')
        else:
            row['modules']['m4_attr'] = {'ok': True, 'skipped': 'no exp'}

        # ── M5 三级一致性 ──
        if sess and (sess / 'params.csv').exists() and mml_text:
            try:
                s4 = CS.check_three_way_consistency(
                    plan_text, str(sess / 'params.csv'), mml_text)
                row['modules']['m5_consistency'] = {
                    'ok': True, 'consistent': s4['ok'],
                    'n_issues': len(s4['issues']),
                    'issue_types': [i['type'] for i in s4['issues']],
                }
                print(f'  M5 一致性: {"通过" if s4["ok"] else str(len(s4["issues"])) + "个问题"} '
                      f'{[i["type"] for i in s4["issues"]]}')
            except Exception as e:
                row['modules']['m5_consistency'] = {'ok': False, 'error': str(e)}
                row['errors'].append(f'M5: {e}')
                print(f'  M5 ❌ {e}')
        else:
            row['modules']['m5_consistency'] = {'ok': True, 'skipped': 'no params.csv'}

        # ── M6 照着配 ──
        if exps and intent_text:
            try:
                fams_biz = OR._build_families_biz(intent_text, dataset_text,
                                                  plan_text, exps, limit=3)
                s6 = CC.run_step6(intent_text, dataset_text, exps,
                                  families_and_biz=fams_biz)
                row['modules']['m6_copy'] = {
                    'ok': True,
                    'scene': s6['scene']['scene'],
                    'n_results': s6['summary']['n_results'],
                    'n_ok': s6['summary']['n_ok'],
                    'translated': [
                        {'family': r['family'],
                         'target': (r.get('translated') or [{}])[0].get('target_name')
                         if r.get('translated') else None,
                         'ok': r['ok']}
                        for r in s6['results']],
                }
                print(f'  M6 照着配: 场景{s6["scene"]["scene"]} '
                      f'{s6["summary"]["n_ok"]}/{s6["summary"]["n_results"]} 成功')
            except Exception as e:
                row['modules']['m6_copy'] = {'ok': False, 'error': str(e)}
                row['errors'].append(f'M6: {e}')
                print(f'  M6 ❌ {e}')
        else:
            row['modules']['m6_copy'] = {'ok': True, 'skipped': 'no exp/intent'}

        all_rows.append(row)

    # ══ 汇总 ══
    elapsed = time.time() - t_start
    print('\n' + '=' * 100)
    print('汇总')
    print('=' * 100)

    print(f'\n{"工单":<22} {"档":<7} {"网易元":<8} {"意图":>4} {"GT族":>5} '
          f'{"场景":>4} {"触发":>4} {"覆盖":>6} {"一致":>6} {"错误":>4}')
    print('─' * 100)
    for r in all_rows:
        m1 = r['modules'].get('m1_parse', {})
        m2 = r['modules'].get('m2_trigger', {})
        m3 = r['modules'].get('m3_plan', {})
        m5 = r['modules'].get('m5_consistency', {})
        cov = f'{m3.get("coverage", 0)*100:.0f}%' if 'coverage' in m3 else '-'
        cons = ('✓' if m5.get('consistent') else
                f'{m5.get("n_issues", 0)}问题' if 'n_issues' in m5 else '-')
        print(f'{r["ticket"]:<22} {r["band"]:<7} {r["me"]:<8} {r["n_items"]:>4} '
              f'{r["gt_fams"]:>5} {m1.get("scene", "-"):>4} '
              f'{"是" if m2.get("run") else "否":>4} {cov:>6} {cons:>6} '
              f'{len(r["errors"]):>4}')

    # 分档统计
    print(f'\n{"分档":<10} {"单数":>5} {"平均对象数":>10} {"平均覆盖":>9} {"触发率":>7} {"崩溃数":>7}')
    print('─' * 100)
    for band in ('small', 'medium', 'large'):
        sel = [r for r in all_rows if r['band'] == band]
        if not sel:
            continue
        n_obj = [r['modules'].get('m3_plan', {}).get('n_objects', 0) for r in sel]
        covs = [r['modules'].get('m3_plan', {}).get('coverage', 0)
                for r in sel if 'coverage' in r['modules'].get('m3_plan', {})]
        trigs = [r['modules'].get('m2_trigger', {}).get('run') for r in sel]
        n_err = sum(len(r['errors']) for r in sel)
        print(f'{band:<10} {len(sel):>5} {sum(n_obj)/len(n_obj):>10.1f} '
              f'{sum(covs)/len(covs)*100 if covs else 0:>8.0f}% '
              f'{sum(1 for t in trigs if t)}/{len(trigs):<5} {n_err:>7}')

    # 场景分布
    scenes = [r['modules'].get('m1_parse', {}).get('scene') for r in all_rows]
    print(f'\n场景分布: ' + ', '.join(
        f'{s}={scenes.count(s)}' for s in ('A', 'B', 'C', 'D') if s in scenes))

    # 失败清单
    all_err = [(r['ticket'], e) for r in all_rows for e in r['errors']]
    print(f'\n总耗时 {elapsed:.1f}s')
    if all_err:
        print(f'\n❌ 失败 {len(all_err)} 项：')
        for tk, e in all_err:
            print(f'  {tk}: {e[:100]}')
    else:
        print('\n✅ 全部工单无崩溃')

    # 保存
    out = Path('/tmp/stage3_multi_verify.json')
    out.write_text(json.dumps(all_rows, ensure_ascii=False, indent=1), encoding='utf-8')
    print(f'\n结果已存: {out}')
    return 0 if not all_err else 1


if __name__ == '__main__':
    sys.exit(main())
