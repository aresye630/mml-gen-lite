#!/usr/bin/env python3
"""P0-7 验证：Stage3 触发条件 + 总编排。

验证目标：
  V1 触发条件四条都生效
  V2 不触发时不做无用工作（性能关键）
  V3 总编排六步都能跑（真实会话）
  V4 每步异常不影响后续步骤
  V5 修复清单 + 澄清项都能产出
  V6 报告渲染正确
  V7 性能：触发时 < 120s，不触发时 < 1s
"""
import json
import sys
import time
from pathlib import Path

sys.path.insert(0, '/Users/alesc/workspace/mml-gen-lite/workflow/stage3')
import orchestrator as OR

GT = json.loads(Path('/tmp/gt_cleaned.json').read_text(encoding='utf-8'))
GT_MAP = {g['ticket']: g for g in GT}

TK = 'NC20260810002261'
g = GT_MAP[TK]
adir_exp = Path(g['path']) / '备份附件'
EXPS = [str(p) for p in sorted(adir_exp.glob('*.txt'))]
ITXT = Path(f'/tmp/intent_v3/{TK}_意图.md').read_text(encoding='utf-8')
DTXT = Path(f'/tmp/intent_v3/{TK}_数据清单.md').read_text(encoding='utf-8')
SESSION = Path(f'/tmp/eval_versions_out/V3/{TK}')

results = []


def check(name, cond, detail=''):
    results.append((name, bool(cond), detail))
    print(f'  {"✅" if cond else "❌"} {name}' + (f'  —— {detail}' if detail else ''))


def main():
    print('=' * 92)
    print('P0-7 验证：Stage3 触发条件 + 总编排')
    print('=' * 92)

    # ══ V1 触发条件 ══
    print('\n【V1】触发条件四条')

    # T1 意图条目数
    r1 = OR.should_run_stage3('\n'.join(f'- 新增 对象{i}' for i in range(15)))
    check('V1-1 T1 意图 >= 11 条触发', r1['run'] and
          any(t['id'] == 'T1_intent_size' for t in r1['triggers']),
          f"{[t['id'] for t in r1['triggers']]}")

    r1b = OR.should_run_stage3('\n'.join(f'- 新增 对象{i}' for i in range(5)))
    check('V1-2 T1 意图 < 11 条不触发', not r1b['run'], r1b['skipped_reason'][:40])

    # T2 规划表通配
    PLAN_WILD = ('| # | 数据清单表 | 业务对象 | 对象数量 | 现网已有 | 命令族 | 动作 | 判断依据 | 状态 |\n'
                 '|---|---|---|---|---|---|---|---|---|\n'
                 '| 1 | t | o | 1 | 0 | SET APN* | 新增 | x | 确认 |')
    r2 = OR.should_run_stage3('- 新增 x', PLAN_WILD)
    check('V1-3 T2 通配触发', r2['run'] and
          any(t['id'] == 'T2_plan_wildcard' for t in r2['triggers']),
          f"{[t['id'] for t in r2['triggers']]}")

    # T3 guard warn
    r3 = OR.should_run_stage3('- 新增 x', '', '',
                              {'G29_set': {'ok': False, 'missing': [{'family': 'X'}]}})
    check('V1-4 T3 guard 漏配 warn 触发', r3['run'] and
          any(t['id'] == 'T3_guard_leak' for t in r3['triggers']),
          f"{[t['id'] for t in r3['triggers']]}")

    # T3 反例：非漏配类 warn 不触发
    r3b = OR.should_run_stage3('- 新增 x', '', '',
                               {'G22_placeholder': {'ok': False, 'warnings': ['x']}})
    check('V1-5 T3 非漏配类 warn 不触发', not r3b['run'], r3b['skipped_reason'][:40])

    # T4 产物族少
    PLAN_OK = ('| # | 数据清单表 | 业务对象 | 对象数量 | 现网已有 | 命令族 | 动作 | 判断依据 | 状态 |\n'
               '|---|---|---|---|---|---|---|---|---|\n'
               '| 1 | t | o | 1 | 0 | ADD POOL | 新增 | x | 确认 |\n'
               '| 2 | t | o | 1 | 0 | ADD URR | 新增 | x | 确认 |')
    MML_FEW = 'ADD POOL: POOLNAME="p1";'
    r4 = OR.should_run_stage3('- 新增 x', PLAN_OK, MML_FEW)
    check('V1-6 T4 产物族少触发', r4['run'] and
          any(t['id'] == 'T4_fewer_in_mml' for t in r4['triggers']),
          f"{[t['id'] for t in r4['triggers']]}")

    # ══ V2 不触发时不做无用工作 ══
    print('\n【V2】不触发时的开销')
    # ★ 2026-11-12 修正用例：必须用「空会话」测不触发，
    #   否则真实会话里的规划表会触发 T2/T4（那样测的就不是不触发路径）
    import tempfile, shutil
    empty_dir = Path(tempfile.mkdtemp(prefix='stage3_empty_'))
    try:
        t0 = time.time()
        r_no = OR.run_stage3(str(empty_dir), intent_text='- 设置 业务刷新：ALL')
        elapsed_no = time.time() - t0
        check('V2-1 不触发时 ran=False', r_no['ran'] is False,
              r_no['summary'].get('reason', '')[:40])
        check('V2-2 不触发时 steps 为空', not r_no['steps'], f'{len(r_no["steps"])} 步')
        check('V2-3 不触发时耗时 < 100ms', elapsed_no < 0.1, f'{elapsed_no*1000:.1f}ms')
    finally:
        shutil.rmtree(empty_dir, ignore_errors=True)

    # ══ V3 总编排六步（真实会话）══
    print('\n【V3】总编排（真实会话 NC20260810002261）')
    if not SESSION.exists():
        print(f'  ⊘ 会话目录不存在: {SESSION}')
    else:
        t0 = time.time()
        r = OR.run_stage3(
            str(SESSION), intent_text=ITXT, dataset_text=DTXT,
            exp_paths=EXPS,
            guard_checks={'G30_rmv': {'ok': False, 'reversed': [{'family': 'X', 'n_add': 1}]},
                          'G22_placeholder': {'ok': False, 'warnings': ['x']}},
            max_step6_families=3,
        )
        elapsed = time.time() - t0

        check('V3-1 触发了', r['ran'] is True,
              f"triggers={[t['id'] for t in r['trigger']['triggers']]}")
        st = r['steps']
        check('V3-2 Step1 结构合规有结果', 'step1_structure' in st and
              'error' not in st.get('step1_structure', {}),
              f"{st.get('step1_structure', {})}")
        check('V3-3 Step2 对象覆盖有结果', 'step2_coverage' in st and
              'error' not in st.get('step2_coverage', {}),
              str(st.get('step2_coverage', {}))[:70])
        check('V3-4 Step3 属性族链有结果', 'step3_attr_chain' in st,
              f"{len(st.get('step3_attr_chain') or [])} 个 owner 族")
        check('V3-5 Step4 一致性能跑', 'step4_consistency' in st,
              str(st.get('step4_consistency', {}))[:70])
        check('V3-6 Step5 判据分类能跑', 'step5_guard' in st,
              str(st.get('step5_guard', {}))[:70])
        check('V3-7 Step6 照着配有结果', 'step6_copy' in st,
              str(st.get('step6_copy', {}))[:70])

        check('V3-8 产出修复清单', len(r['repairs']) >= 1, f'{len(r["repairs"])} 条')
        check('V3-9 产出澄清项', len(r['clarifications']) >= 1, f'{len(r["clarifications"])} 条')

        # ══ V7 性能 ══
        print('\n【V7】性能')
        check('V7-1 触发时耗时 < 120s', elapsed < 120, f'{elapsed:.1f}s')
        print(f'  （实测 {elapsed:.2f}s，编排本身不含 agent 调用）')

        # ══ V6 报告渲染 ══
        print('\n【V6】报告渲染')
        report = OR.render_repair_report(r, TK)
        check('V6-1 报告非空', len(report) > 200, f'{len(report)} 字')
        check('V6-2 含触发原因', '## 触发原因' in report)
        check('V6-3 含各步结果', '## 各步结果' in report)
        check('V6-4 含补配清单', '## 补配清单' in report or len(r['repairs']) == 0)
        check('V6-5 含汇总', '## 汇总' in report)
        (SESSION / '阶段3修复清单.md').write_text(report, encoding='utf-8')
        print(f'  报告已写: {SESSION}/阶段3修复清单.md')

        # 不触发时的报告（用 r_no，它是空会话的结果）
        rep_no = OR.render_repair_report(r_no, TK)
        check('V6-6 不触发时报告说明原因', '未运行' in rep_no and '原因' in rep_no,
              rep_no.split('\n')[4][:50] if len(rep_no.split('\n')) > 4 else '')

    # ══ V4 每步异常不影响后续 ══
    print('\n【V4】单步异常隔离')
    r_err = OR.run_stage3(
        '/tmp/nonexistent_session_dir_xyz',
        intent_text='\n'.join(f'- 新增 对象{i}' for i in range(15)),
        dataset_text='', exp_paths=[], guard_checks={})
    check('V4-1 缺文件不崩', isinstance(r_err, dict), f'ran={r_err.get("ran")}')
    check('V4-2 仍产出 summary', 'summary' in r_err, str(r_err.get('summary'))[:60])

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
