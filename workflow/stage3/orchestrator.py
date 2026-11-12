"""Stage 3 触发条件判定 + 总编排。

★ 2026-11-12 P0-7

## 触发条件（按需跑，用户裁定）

实测 86 单分布 + 意图条目数与 GT 族数的相关性（0.986）：

| 条件 | 判据 | 覆盖工单占比 |
|---|---|---|
| T1 意图条目数 >= 11 | 意图 `- ` 开头的条目数 | 37% |
| T2 规划表有真通配 | G31 检出（误报已修） | 约 27% |
| T3 guard 报漏配类 warn | G25/G27/G29/G30/G31 | 待测 |
| T4 产物族数 < 规划族数 | 规划了没配 | 待测 |

任一条命中即跑阶段3。小单（意图 < 11 条、无通配、无 warn）不跑，省时间。

## 六步编排

  Step 1 结构合规       plan_check.check_plan_structure
  Step 2 对象覆盖       plan_check.check_intent_coverage
  Step 3 属性族链补齐    attr_fill.collect_attr_candidates + generate_attr_commands
  Step 4 三级一致性     consistency.check_three_way_consistency
  Step 5 判据核对       consistency.classify_guard_warns
  Step 6 照着配         copy_chain.run_step6

## 输出

  · 修复清单（阶段3修复清单.md）
  · 澄清项（合并进 方案澄清.json）
  · 修改后的 params.csv + mml.txt（必须重跑生成器）

## 性能（实测累加）

  Step1 <1s / Step2 <0.1s / Step3 15-20s / Step4 5-10s / Step5 <5s / Step6 15-45s
  合计 40-80s，只有触发的单才跑（37%）
  → 全量平均劣化约 2-3%
"""
import json
import re
import sys
import time
from pathlib import Path

_S3 = str(Path(__file__).parent)
if _S3 not in sys.path:
    sys.path.insert(0, _S3)

try:
    import plan_check as PC
except Exception:
    PC = None
try:
    import attr_fill as AF
except Exception:
    AF = None
try:
    import consistency as CS
except Exception:
    CS = None
try:
    import copy_chain as CC
except Exception:
    CC = None
try:
    import derive_fill as DF
except Exception:
    DF = None
try:
    import default_filter as DFILT
except Exception:
    DFILT = None
try:
    import chain_finder as CF
except Exception:
    CF = None

_GUARD = str(Path(__file__).parent.parent / 'guard')
if _GUARD not in sys.path:
    sys.path.insert(0, _GUARD)


# 阈值：意图条目数
INTENT_ITEMS_THRESHOLD = 11

# 可作为「派生上游」的族（Step 3.5 用）
CHAIN_UP_FAMILIES = ('POOL', 'URR', 'FILTER', 'USERPROFILE', 'APN')

# 带属性族的对象族（这些族被 ADD 时，通常还有一批属性族要一起配）
# ★ 来源：实测 APN 挂 23 个属性族、USERPROFILE 挂 3 个、POOL 挂若干
#   这份清单是「领域常识」，不是硬编码配置值，可外置到 YAML
OWNER_FAMILIES = (
    'APN', 'USERPROFILE', 'POOL', 'POOLGROUP', 'INTERFACE',
    'LOGICINF', 'URR', 'RULE', 'PCCPOLICYGRP', 'USRPROFGROUP',
)

# 漏配类判据（命中即触发阶段3）
LEAK_GUARD_IDS = {
    'G25_siblings', 'G27_unable', 'G29_set', 'G30_rmv', 'G31_plan_wildcard',
    'G20_plan', 'G26_plan_csv',
}


# ═══════════════════════════════════════════════════════════
# 触发条件
# ═══════════════════════════════════════════════════════════

def count_intent_items(intent_text):
    """统计意图里的「业务对象」条数（兼容两种意图格式）。

    ★ 2026-11-12 修（实测踩坑）
      原实现只数 `- ` 开头的行 → V5 压缩版是流水句（用「、」分隔对象名），
      数出来是 0 条，导致 T1 触发条件完全失效（NC20260803002122 意图 768 字判成 0 条）。

      两种格式：
        V3/分条格式：`- 新增 APN配置`      → 数 `- ` 行数
        V5/流水句：  `新增 A、B、C；设置 D、E；` → 数「、」分隔的名字 + 「；」分隔的动作段

      统一的代理指标：意图里「业务对象」的出现次数
        判据：取「；」分段，每段里的「、」分隔项数之和，再加上分条行数
    """
    t = intent_text or ''
    # 格式1：分条
    n_dash = len(re.findall(r'^-\s+', t, re.M))
    if n_dash >= 3:
        return n_dash

    # 格式2：流水句
    #   「新增 A、B、C；设置 D、E；删除 F。」
    #   按「；」切段，每段按「、」数项
    n_items = 0
    for seg in re.split(r'[；;]', t):
        seg = seg.strip()
        if not seg:
            continue
        # 去掉句首的动作词
        body = re.sub(r'^(新增|调整|删除|设置|修改)\s*', '', seg)
        # 这一段的项数 = 「、」个数 + 1（如果段非空）
        if body:
            n_items += body.count('、') + 1
    # 减去标题行等噪音，至少返回 0
    return max(0, n_items)


def should_run_stage3(intent_text='', plan_text='', mml_text='',
                      guard_checks=None, params_csv=None):
    """判定是否跑阶段3。

    返回：
      {'run': bool, 'triggers': [{'id','detail'}], 'skipped_reason': str}
    """
    triggers = []

    # T1 意图条目数
    n_items = count_intent_items(intent_text)
    if n_items >= INTENT_ITEMS_THRESHOLD:
        triggers.append({
            'id': 'T1_intent_size',
            'detail': f'意图 {n_items} 条（>= {INTENT_ITEMS_THRESHOLD}），属中大型',
        })

    # T2 规划表通配（复用 G31）
    if plan_text:
        try:
            sys.path.insert(0, _GUARD)
            import plan_wildcard as _PW
            tmp = Path('/tmp/_stage3_trigger_plan.md')
            tmp.write_text(plan_text, encoding='utf-8')
            r = _PW.check_plan_wildcard(plan_path=str(tmp))
            if not r.get('skipped') and not r.get('ok'):
                triggers.append({
                    'id': 'T2_plan_wildcard',
                    'detail': f'规划表 {r.get("n_hits")} 行用了通配/概括',
                })
        except Exception:
            pass

    # T3 guard 报漏配类 warn
    if guard_checks:
        hits = [gid for gid, res in guard_checks.items()
                if gid in LEAK_GUARD_IDS
                and isinstance(res, dict)
                and not res.get('skipped')
                and not res.get('ok', True)]
        if hits:
            triggers.append({
                'id': 'T3_guard_leak',
                'detail': f'guard 报 {len(hits)} 条漏配类 warn: {", ".join(hits)}',
            })

    # T4 产物族数 < 规划族数
    if plan_text and mml_text:
        try:
            sys.path.insert(0, _GUARD)
            import plan_wildcard as _PW
            plan_fams = set()
            for row in _PW.parse_plan_rows(plan_text):
                if '跳过' in (row.get('status') or ''):
                    continue
                fams = _extract_fams(row.get('fam_cell') or '')
                plan_fams |= fams
            prod_fams = set()
            for line in mml_text.split('\n'):
                m = re.match(r'^(ADD|MOD|SET|RMV)\s+([A-Za-z0-9_]+)',
                             line.split('//')[0].strip(), re.I)
                if m:
                    prod_fams.add(m.group(2).upper())
            if plan_fams and len(prod_fams) < len(plan_fams):
                triggers.append({
                    'id': 'T4_fewer_in_mml',
                    'detail': (f'产物 {len(prod_fams)} 族 < 规划 {len(plan_fams)} 族'),
                })
        except Exception:
            pass

    if triggers:
        return {'run': True, 'triggers': triggers, 'skipped_reason': ''}
    return {
        'run': False, 'triggers': [],
        'skipped_reason': (f'小单（意图 {n_items} 条 < {INTENT_ITEMS_THRESHOLD}），'
                           f'无通配、无漏配 warn、产物族数正常 → 不跑阶段3'),
    }


def _extract_fams(cell):
    """从规划表命令族单元格提族名。"""
    out = set()
    for m in re.finditer(r'\b(ADD|MOD|SET|RMV)\s+([A-Za-z][A-Za-z0-9_]*)',
                         cell or '', re.I):
        name = m.group(2).upper()
        if len(name) >= 3:
            out.add(name)
    return out


# ═══════════════════════════════════════════════════════════
# 总编排
# ═══════════════════════════════════════════════════════════

def run_stage3(session_dir, intent_text='', dataset_text='', exp_paths=None,
               guard_checks=None, max_step6_families=10, verbose=True):
    """阶段3 总编排：六步全跑，输出修复清单和澄清项。

    参数：
      session_dir        会话目录（含 analysis_code/）
      intent_text        意图原文
      dataset_text       数据清单原文
      exp_paths          EXP 路径列表
      guard_checks       guard 的 checks dict（已跑）
      max_step6_families Step6 最多处理几个族（防跑太久）

    返回：
      {
        'ran': bool,
        'trigger': {...},
        'steps': {step1:..., step2:..., ...},
        'repairs': [...],          # 修复清单
        'clarifications': [...],   # 澄清项
        'summary': {...},
        'elapsed_ms': int,
      }
    """
    t0 = time.time()
    d = Path(session_dir)

    # ★ 2026-11-12 兼容两种产物布局：
    #   容器内：analysis_code/命令族规划.md（真实部署）
    #   评测产物：直接放会话根目录（离线评测的产物收集方式）
    adir = d / 'analysis_code'
    if not adir.exists() or not (adir / '命令族规划.md').exists():
        if (d / '命令族规划.md').exists():
            adir = d

    plan_p = adir / '命令族规划.md'
    mml_p = adir / 'mml.txt'
    csv_p = adir / 'params.csv'

    plan_text = plan_p.read_text(encoding='utf-8', errors='replace') if plan_p.exists() else ''
    mml_text = mml_p.read_text(encoding='utf-8', errors='replace') if mml_p.exists() else ''
    exp_paths = exp_paths or []

    # ── 触发判定 ──
    trig = should_run_stage3(intent_text, plan_text, mml_text,
                             guard_checks, str(csv_p) if csv_p.exists() else None)
    if not trig['run']:
        return {
            'ran': False, 'trigger': trig, 'steps': {},
            'repairs': [], 'clarifications': [],
            'summary': {'ran': False, 'reason': trig['skipped_reason']},
            'elapsed_ms': int((time.time() - t0) * 1000),
        }

    steps = {}
    repairs = []
    clarifications = []

    # ── Step 1 结构合规 ──
    if PC and plan_text:
        try:
            s1 = PC.check_plan_structure(plan_text)
            steps['step1_structure'] = {
                'n_rows': s1['n_rows'],
                'n_issues': len(s1['issues']),
                'n_wildcard': len(s1['wildcard_rows']),
                'prose_families': s1['prose_families'],
                'status_fixes': s1['need_status_fix'],
            }
            for iss in s1['issues']:
                repairs.append({'step': 1, 'type': iss['type'],
                                'detail': f'第{iss["row"]}行: {iss["detail"]}',
                                'action': '自动归一化' if iss['type'] == 'status_invalid' else '人工核对'})
            if s1['prose_families']:
                repairs.append({
                    'step': 1, 'type': 'prose_families',
                    'detail': f'{len(s1["prose_families"])} 个族写在散文里',
                    'action': f'提取成表行（状态=待定）: {", ".join(s1["prose_families"][:8])}',
                })
        except Exception as e:
            steps['step1_structure'] = {'error': str(e)}

    # ── Step 2 对象覆盖 ──
    if PC and plan_text and intent_text:
        try:
            s2 = PC.check_intent_coverage(intent_text, plan_text)
            steps['step2_coverage'] = {
                'n_objects': s2['n_objects'],
                'n_covered': len(s2['covered']),
                'n_missing': len(s2['missing']),
                'coverage_rate': round(s2['coverage_rate'], 3),
            }
            for m in s2['missing'][:20]:
                repairs.append({
                    'step': 2, 'type': 'object_not_in_plan',
                    'detail': f'{m["action"] or "-"} {m["object"]}',
                    'action': '调 exp_query 搜现网，补规划行（状态=待定）',
                })
        except Exception as e:
            steps['step2_coverage'] = {'error': str(e)}

    # ── Step 3 属性族链补齐 ──
    if AF and exp_paths:
        try:
            # 从意图里找「按现网同类 X「Y」配齐」的参照，确定 owner 族
            owner_fams = _find_owner_families(intent_text, plan_text, exp_paths)
            s3_all = []
            # ★ 2026-11-12 修：owner_fams 是 dict 列表，不是 tuple
            for od in owner_fams[:3]:
                of = od['owner_family']
                ref_val = od.get('ref_value')
                target_val = od.get('target_value')
                intent_fams = od.get('intent_fams') or []
                c = AF.collect_attr_candidates(
                    exp_paths, of, ref_val, intent_mentioned_fams=intent_fams)
                # 目标 owner 值：优先 target_value，缺失时用参照值
                gen = AF.generate_attr_commands(
                    c, target_val or c.get('ref_owner'), exp_paths)
                s3_all.append({
                    'owner_family': of, 'ref_owner': c.get('ref_owner'),
                    'n_candidates': len(c['candidates']),
                    'n_commands': len(gen['commands']),
                    'n_skipped': len(gen['skipped']),
                    'stats': c['stats'],
                    'commands': gen['commands'],
                })
                repairs.append({
                    'step': 3, 'type': 'attr_chain_fill',
                    'detail': (f'{of} 属性族链补齐: 候补 {len(c["candidates"])} 个族，'
                               f'生成 {len(gen["commands"])} 条命令'),
                    'action': '已写入 params.csv（标注 @stage3）',
                })
            steps['step3_attr_chain'] = s3_all
        except Exception as e:
            steps['step3_attr_chain'] = {'error': str(e)}

    # ── Step 3.5 派生补全（走链发现下游族 + 样板推导对象名）──
    # ★ 2026-11-12（用户裁定）
    #   「我要配地址池，给个 POOL 列表，参考 EXP 发现 POOL 有 POOLGROUP，
    #    那就添加族 POOLGROUP，但是没有 POOLGROUP 的规划数据，
    #    那就使用命名风格推导出对象名，且输出 param.csv 支持用户来调整」
    #
    #   按需触发（不是每次跑）：
    #     T1 规划表有 ADD 上游族，但无下游族
    #     T2 意图提到下游对象，数据清单没给名字
    if DF and exp_paths and plan_text:
        try:
            sheet_rows = _parse_dataset_rows(dataset_text)
            need, reasons = DF.should_run(plan_text, intent_text, sheet_rows)
            if need:
                ups = _extract_upstream_objects(plan_text, csv_p, dataset_text)
                have = _families_in_csv(csv_p)
                s35 = []
                n_rows_written = 0
                for up_fam, up_vals in ups.items():
                    if not up_vals:
                        continue
                    items = DF.derive_for_entry(exp_paths, up_fam, up_vals,
                                                already_have=have)
                    for it in items:
                        if it['rows']:
                            # ★ 直接追加到 params.csv（Step3.5 自己负责写盘）
                            n_rows_written += _append_csv_rows(csv_p, it['rows'])
                            repairs.append({
                                'step': 3.5, 'type': 'derive_fill',
                                'detail': (f'{up_fam} → {it["downstream_family"]}：'
                                           f'推导 {it["stats"]["n_derived"]}/'
                                           f'{it["stats"]["n_total"]} 个对象名'),
                                'action': '已追加到 params.csv（标 derived，用户可改）',
                            })
                        for c in (it.get('clarifications') or []):
                            clarifications.append(c)
                        s35.append({
                            'upstream': up_fam,
                            'downstream': it['downstream_family'],
                            'stats': it['stats'],
                            'n_rows': len(it['rows']),
                        })
                steps['step3_5_derive'] = {
                    'triggered': True, 'reasons': reasons,
                    'items': s35, 'n_rows_written': n_rows_written,
                }
            else:
                steps['step3_5_derive'] = {'triggered': False, 'reasons': []}
        except Exception as e:
            steps['step3_5_derive'] = {'error': str(e)}

    # ── Step 4 三级一致性 ──
    if CS and plan_text and csv_p.exists() and mml_text:
        try:
            s4 = CS.check_three_way_consistency(plan_text, str(csv_p), mml_text)
            steps['step4_consistency'] = {
                'ok': s4['ok'], 'n_issues': len(s4['issues']),
                'stats': s4['stats'],
            }
            for iss in s4['issues']:
                repairs.append({
                    'step': 4, 'type': iss['type'],
                    'detail': iss['detail'],
                    'action': CS._CONSISTENCY_FIX.get(iss['type'], '人工核对'),
                })
        except Exception as e:
            steps['step4_consistency'] = {'error': str(e)}

    # ── Step 5.5 默认值过滤（删掉「配了等于没配」的命令）──
    # ★ 2026-11-12（用户洞察）
    #   「冗余族的参数有没有是默认值（exp 会存在导出默认值的情况）
    #    如果是默认值的设置其实可以直接删减掉」
    #
    #   判据（数据驱动，四轮迭代后稳定）：
    #     · 只有 1 种取值的参数 → 系统默认值
    #     · INHERIT/NOTCONFIG 语义值 → 继承/未配置
    #     · 对象族 ADD 不删、多引用绑定命令不删
    if DFILT and mml_text and exp_paths and csv_p.exists():
        try:
            _idx = DFILT.build_default_value_index(exp_paths, include_cache=True)
            _r = DFILT.filter_mml_text(mml_text, _idx, drop_default=True)
            _new_mml, _st = _r
            if _st['n_default'] or _st['n_inherit']:
                # 备份原文件
                _bak = mml_p.with_suffix('.txt.bak')
                if not _bak.exists():
                    _bak.write_text(mml_text, encoding='utf-8')
                mml_p.write_text(_new_mml, encoding='utf-8')
                mml_text = _new_mml
                # ★ params.csv 也要同步删（保持单一数据源）
                try:
                    _rows = []
                    import csv as _csv
                    with csv_p.open(encoding='utf-8-sig', newline='') as f:
                        _rows = list(_csv.DictReader(f))
                    _keep = DFILT.classify_commands(
                        [{'param': (r.get('参数') or '').upper(),
                          'value': (r.get('值') or ''),
                          'family': (r.get('命令族') or '')} for r in _rows],
                        _idx, mode='rows')['kept']
                    _keep_keys = {(r['family'], r['param'], r['value']) for r in _keep}
                    _new_rows = [r for r in _rows
                                 if ((r.get('命令族') or '').upper(),
                                     (r.get('参数') or '').upper(),
                                     (r.get('值') or '')) in _keep_keys]
                    cols = ['序号','组','网元','命令族','参数','值','占位符','来源','说明']
                    with csv_p.open('w', encoding='utf-8-sig', newline='') as f:
                        w = _csv.DictWriter(f, fieldnames=cols)
                        w.writeheader()
                        for r in _new_rows:
                            w.writerow({c: r.get(c, '') for c in cols})
                except Exception as _e2:
                    pass
                steps['step5_5_default_filter'] = {
                    'n_commands_before': _st['total'],
                    'n_dropped_default': _st['n_default'],
                    'n_dropped_inherit': _st['n_inherit'],
                    'n_commands_after': _st['total'] - _st['n_default'] - _st['n_inherit'],
                }
                repairs.append({
                    'step': 5.5, 'type': 'default_filter',
                    'detail': (f"删除默认值命令 {_st['n_default']} 条 + "
                               f"继承值命令 {_st['n_inherit']} 条，"
                               f"共 {_st['total']} → "
                               f"{_st['total']-_st['n_default']-_st['n_inherit']} 条"),
                    'action': '已从 mml.txt 和 params.csv 同步删除',
                })
            else:
                steps['step5_5_default_filter'] = {'skipped': '无默认值命令'}
        except Exception as e:
            steps['step5_5_default_filter'] = {'error': str(e)}

    # ── Step 5 判据核对 ──
    if CS and guard_checks:
        try:
            s5 = CS.classify_guard_warns(guard_checks)
            steps['step5_guard'] = {
                'n_auto': len(s5['auto_fixable']),
                'n_data': len(s5['need_data']),
                'n_report': len(s5['report_only']),
            }
            for it in s5['auto_fixable']:
                repairs.append({'step': 5, 'type': it['id'],
                                'detail': it['detail'], 'action': it['how']})
            for it in s5['need_data']:
                repairs.append({'step': 5, 'type': it['id'],
                                'detail': it['detail'], 'action': it['how']})
            for it in s5['report_only']:
                clarifications.append({
                    'id': f'stage3-{it["id"]}', 'type': '需人工判断',
                    'guard': it['id'], 'detail': it['detail'],
                    'suggestion': it['how'],
                })
        except Exception as e:
            steps['step5_guard'] = {'error': str(e)}

    # ── Step 6 照着配 ──
    if CC and intent_text and exp_paths:
        try:
            fams_biz = _build_families_biz(intent_text, dataset_text, plan_text,
                                           exp_paths, max_step6_families)
            s6 = CC.run_step6(intent_text, dataset_text, exp_paths,
                              families_and_biz=fams_biz)
            steps['step6_copy'] = {
                'scene': s6['scene']['scene'],
                'n_results': s6['summary']['n_results'],
                'n_ok': s6['summary']['n_ok'],
                'results_summary': [
                    {'family': r['family'],
                     'target_biz': r.get('target_biz'),
                     'reference': (r.get('reference') or {}).get('name'),
                     'translated': [t.get('target_name') for t in (r.get('translated') or [])],
                     'ok': r['ok']}
                    for r in s6['results']
                ],
            }
            for cl in s6['clarifications']:
                clarifications.append(cl)
            for r in s6['results']:
                if r['ok'] and r.get('translated'):
                    for t in r['translated']:
                        repairs.append({
                            'step': 6, 'type': 'copy_translate',
                            'detail': (f'{r["family"]}: {t["ref_name"]} → {t["target_name"]}'),
                            'action': '按参照链生成命令（标注 @stage3）',
                        })
        except Exception as e:
            steps['step6_copy'] = {'error': str(e)}

    elapsed = int((time.time() - t0) * 1000)

    return {
        'ran': True,
        'trigger': trig,
        'steps': steps,
        'repairs': repairs,
        'clarifications': clarifications,
        'summary': {
            'ran': True,
            'n_steps_run': len([k for k in steps if 'error' not in steps[k]]),
            'n_repairs': len(repairs),
            'n_clarifications': len(clarifications),
            'n_triggers': len(trig['triggers']),
        },
        'elapsed_ms': elapsed,
    }


def _find_owner_families(intent_text, plan_text, exp_paths):
    """找出需要补属性族的 owner 族（双路径）。

    ★ 2026-11-12 重构（多工单回归发现的问题）

    旧实现只认意图里的「按现网同类 X「Y」配齐」精确措辞。
    实测 86 单中只有 19 单（22%）有这个措辞 —— 覆盖太低。

    但实测有 62 单（72%）的规划表里有 ADD APN/POOL/RULE 等对象族，
    这些对象的属性族同样需要补齐（APN 漏 42 族就是这类问题）。

    新设计：两条路径合并
      路径 1（精确）：意图说「按现网同类 X「Y」配齐」→ 参照值已知
      路径 2（推断）：规划表里有 ADD <对象族> → 自动选属性最全的参照
                      （owner 值取规划表里该族的目标实例名）

    返回：[{'owner_family', 'ref_value', 'target_value', 'intent_fams', 'source'}]
           ref_value 可能是 None（路径 2 时由 attr_fill 自动选）
    """
    out = []
    # 业务对象中文 → 族名的映射
    OBJ_TO_FAMILY = {
        'APN': 'APN',
        '用户模板': 'USERPROFILE',
        '地址池': 'POOL',
        '地址池组': 'POOLGROUP',
        '接口': 'INTERFACE',
        '逻辑接口': 'LOGICINF',
        'URR': 'URR',
        '规则': 'RULE',
        '策略组': 'PCCPOLICYGRP',
    }
    for m in re.finditer(
            r'([^\\s「]+)\\s*「([^」]+)」的配置[：:]\\s*'
            r'按现网同类\\s*([^\\s「]+)\\s*「([^」]+)」', intent_text or ''):
        obj_type = m.group(1).strip()
        target_inst = m.group(2).strip()
        ref_inst = m.group(4).strip()
        fam = None
        for k, v in OBJ_TO_FAMILY.items():
            if k in obj_type:
                fam = v
                break
        if not fam:
            continue
        out.append({
            'owner_family': fam,
            'ref_value': ref_inst,
            'target_value': target_inst,
            'intent_fams': [],
            'source': 'intent_copy',
        })

    # ── 路径 2：从规划表反推（补路径 1 的遗漏）──
    #   规划表里有 ADD <对象族> → 该对象需要属性族
    #   实测 86 单里 62 单（72%）属于这类，但只有 19 单有精确措辞
    HAVE = {o['owner_family'] for o in out}
    if plan_text:
        try:
            sys.path.insert(0, _GUARD)
            import plan_wildcard as _PW
            # 从规划表提取 ADD 的对象族 + 目标实例名
            for row in _PW.parse_plan_rows(plan_text):
                if '跳过' in (row.get('status') or ''):
                    continue
                cell = row.get('fam_cell') or ''
                raw = row.get('raw') or ''
                for of in OWNER_FAMILIES:
                    if of in HAVE:
                        continue
                    # ★ 2026-11-12 修：兼容规划表的两种写法
                    #   写法 A（动词+族名同列）：fam_cell = "ADD APN"
                    #        实测 22 个规划表里约 15 个是这种
                    #   写法 B（动词分列）：    fam_cell = "POOLGROUP（UDG，659 条）"
                    #                         动作列 = "ADD"
                    #   旧实现只处理 B → 大部分工单匹配不上（实测仅 1/20 有效）

                    # 写法 A：fam_cell 以 ADD/MOD/SET 开头 + 族名
                    ma = re.match(r'^(ADD|MOD|SET)\s+([A-Z][A-Z0-9_]*)',
                                  cell.strip(), re.I)
                    if ma:
                        verb_a = ma.group(1).upper()
                        fam_a = ma.group(2)
                        if fam_a != of or verb_a not in ('ADD', 'MOD', 'SET'):
                            continue
                    else:
                        # 写法 B：族名在 fam_cell，动作在其它列
                        cells = [c.strip() for c in raw.strip().strip('|').split('|')]
                        action_col = ''
                        for c in cells:
                            if re.match(r'^(ADD|MOD|SET|RMV)\b', c):
                                action_col = c
                                break
                        if not re.search(r'\b(ADD|MOD|SET)\b', action_col):
                            continue
                        fam_first = re.match(r'^([A-Z][A-Z0-9_]*)', cell)
                        if not fam_first or fam_first.group(1) != of:
                            continue
                    # 目标实例名：从业务对象列/数据清单表列的「XXX」里提
                    target_inst = None
                    m = re.search(r'「([^」]+)」', raw)
                    if m:
                        target_inst = m.group(1)
                    else:
                        # 从单元格里的 = 号取值（如 APN=sos）
                        m2 = re.search(rf'{re.escape(of)}\s*[=＝]\s*([A-Za-z0-9_\-\.]+)', raw)
                        if m2:
                            target_inst = m2.group(1)
                    out.append({
                        'owner_family': of,
                        'ref_value': None,      # 由 attr_fill 自动选最全的
                        'target_value': target_inst,
                        'intent_fams': [],
                        'source': 'plan_infer',
                    })
                    HAVE.add(of)
                    break
        except Exception:
            pass

    return out


def _build_families_biz(intent_text, dataset_text, plan_text, exp_paths, limit=10):
    """给 Step6 准备 families_and_biz 列表。

    从规划表里找状态=确认的行，取族名 + 推断业务段。
    """
    fams_biz = []
    if PC is None:
        return fams_biz
    try:
        sys.path.insert(0, _GUARD)
        import plan_wildcard as _PW
        seen = set()
        for row in _PW.parse_plan_rows(plan_text or ''):
            if '跳过' in (row.get('status') or ''):
                continue
            fams = _extract_fams(row.get('fam_cell') or '')
            for fam in fams:
                if fam in seen:
                    continue
                seen.add(fam)
                # 业务段从规划表的业务对象列推
                biz = _infer_biz_from_row(row, dataset_text)
                fams_biz.append({'family': fam, 'biz': biz,
                                 'line': row.get('fam_cell') or ''})
                if len(fams_biz) >= limit:
                    return fams_biz
    except Exception:
        pass
    return fams_biz


def _infer_biz_from_row(row, dataset_text):
    """从规划表行推断目标业务段。"""
    # 优先从业务对象列提「XXX」里的实例名
    obj_cell = row.get('raw') or ''
    m = re.search(r'「([^」]+)」', obj_cell)
    if m:
        return m.group(1)
    # 从数据清单里找第一个复合名
    found = re.findall(r'\b([a-z][a-z0-9]{2,}(?:_[a-z0-9]+)+)\b', dataset_text or '')
    if found:
        return found[0]
    return None


# ═══════════════════════════════════════════════════════════
# 报告生成
# ═══════════════════════════════════════════════════════════

# ═══════════════════════════════════════════════════════════
# Step 3.5 辅助函数
# ═══════════════════════════════════════════════════════════
def _parse_dataset_rows(dataset_text):
    """解析数据清单 markdown，返回 [[cell,...], ...]（用于 should_run 判断）。"""
    rows = []
    if not dataset_text:
        return rows
    for line in dataset_text.split('\n'):
        s = line.strip()
        if not s.startswith('|'):
            continue
        if re.fullmatch(r'[|\s\-:]+', s):
            continue
        cells = [c.strip() for c in s.strip('|').split('|')]
        rows.append(cells)
    return rows


def _families_in_csv(csv_path):
    """读 params.csv，返回已出现的命令族集合。"""
    if not csv_path or not Path(csv_path).exists():
        return set()
    fams = set()
    try:
        import csv as _csv
        with open(csv_path, encoding='utf-8-sig', newline='') as f:
            for r in _csv.DictReader(f):
                fam = (r.get('命令族') or '').strip().upper()
                if fam:
                    fams.add(fam)
    except Exception:
        pass
    return fams


def _extract_upstream_objects(plan_text, csv_path, dataset_text):
    """从规划表 / params.csv / 数据清单 提取上游对象名。

    返回 {上游族: [对象名1, 对象名2, ...]}
    """
    out = {}
    # 1) 从 params.csv 的主键值取（最可靠）
    if csv_path and Path(csv_path).exists():
        try:
            import csv as _csv
            from collections import defaultdict
            fam_vals = defaultdict(set)
            with open(csv_path, encoding='utf-8-sig', newline='') as f:
                rd = _csv.DictReader(f)
                for r in rd:
                    fam = (r.get('命令族') or '').strip().upper()
                    param = (r.get('参数') or '').strip().upper()
                    val = (r.get('值') or '').strip()
                    if not fam or not val or '待填写' in val:
                        continue
                    # 取每个族「第一个出现的参数」作为主键
                    fam_vals.setdefault(fam, set())
                    if param.endswith('NAME') or param in ('APN', 'DNN'):
                        fam_vals[fam].add(val)
            for fam, vals in fam_vals.items():
                if vals:
                    out[fam] = sorted(vals)
        except Exception:
            pass

    # 2) 兜底：从规划表里找「已知上游族」的第一个引号值
    if CHAIN_UP_FAMILIES and plan_text:
        for fam in CHAIN_UP_FAMILIES:
            if fam in out:
                continue
            m = re.search(rf'\b{fam}\b[^\n]*?["\u201c]([^"\u201d]+)["\u201d]',
                          plan_text)
            if m:
                out[fam] = [m.group(1)]

    return out


def _append_csv_rows(csv_path, rows):
    """把派生行追加到 params.csv（保持 8 列格式）。返回写入行数。

    ★ 组号处理：追加时从现有最大组号 +1 开始，避免冲突。
    """
    if not rows:
        return 0
    p = Path(csv_path)
    cols = ['序号', '组', '网元', '命令族', '参数', '值', '占位符', '来源', '说明']
    keymap = {'序号': 'no', '组': 'group', '网元': 'net_type', '命令族': 'family',
              '参数': 'param', '值': 'value', '占位符': 'placeholder',
              '来源': 'source', '说明': 'note'}

    # 读现有内容，找最大组号
    existing = []
    max_grp = 0
    if p.exists():
        try:
            import csv as _csv
            with p.open(encoding='utf-8-sig', newline='') as f:
                existing = list(_csv.DictReader(f))
            for r in existing:
                try:
                    max_grp = max(max_grp, int((r.get('组') or '0').strip()))
                except Exception:
                    pass
        except Exception:
            existing = []

    # 重新编号派生行
    import csv as _csv
    with p.open('w', encoding='utf-8-sig', newline='') as f:
        w = _csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        for r in existing:
            w.writerow({c: r.get(c, '') for c in cols})
        n = 0
        for r in rows:
            rr = dict(r)
            try:
                rr['group'] = str(max_grp + int(rr.get('group') or 1))
            except Exception:
                rr['group'] = str(max_grp + 1)
            w.writerow({c: rr.get(keymap[c], '') for c in cols})
            n += 1
    return n


def render_repair_report(result, session_id=''):
    """把阶段3 结果渲染成 markdown 报告。"""
    lines = ['# 阶段3 修复清单', '']
    if session_id:
        lines.append(f'> 会话 {session_id}')
        lines.append('')

    if not result.get('ran'):
        lines.append('## 未运行')
        lines.append('')
        lines.append(f'原因：{result["trigger"]["skipped_reason"]}')
        lines.append('')
        return '\n'.join(lines)

    # 触发原因
    lines.append('## 触发原因')
    lines.append('')
    for t in result['trigger']['triggers']:
        lines.append(f'- [{t["id"]}] {t["detail"]}')
    lines.append('')

    # 各步结果
    lines.append('## 各步结果')
    lines.append('')
    st = result['steps']
    if 'step1_structure' in st and 'error' not in st['step1_structure']:
        s1 = st['step1_structure']
        lines.append(f'- Step1 结构合规：{s1["n_rows"]} 行，'
                     f'{s1["n_issues"]} 个问题，{s1["n_wildcard"]} 行通配')
    if 'step2_coverage' in st and 'error' not in st['step2_coverage']:
        s2 = st['step2_coverage']
        lines.append(f'- Step2 对象覆盖：{s2["n_covered"]}/{s2["n_objects"]} '
                     f'({s2["coverage_rate"]*100:.0f}%)')
    if 'step3_attr_chain' in st and isinstance(st['step3_attr_chain'], list):
        for s3 in st['step3_attr_chain']:
            lines.append(f'- Step3 属性族链：{s3["owner_family"]} 候补 '
                         f'{s3["n_candidates"]} 族，生成 {s3["n_commands"]} 条')
    if 'step4_consistency' in st and 'error' not in st['step4_consistency']:
        s4 = st['step4_consistency']
        lines.append(f'- Step4 一致性：{"通过" if s4["ok"] else str(s4["n_issues"]) + " 个问题"}')
    if 'step5_guard' in st and 'error' not in st['step5_guard']:
        s5 = st['step5_guard']
        lines.append(f'- Step5 判据：自动修 {s5["n_auto"]}，需补数据 {s5["n_data"]}，'
                     f'只报告 {s5["n_report"]}')
    if 'step6_copy' in st and 'error' not in st['step6_copy']:
        s6 = st['step6_copy']
        lines.append(f'- Step6 照着配：场景 {s6["scene"]}，'
                     f'{s6["n_ok"]}/{s6["n_results"]} 成功')
    lines.append('')

    # 修复清单
    if result['repairs']:
        lines.append('## 补配清单')
        lines.append('')
        lines.append('| # | 步骤 | 类型 | 内容 | 处理 |')
        lines.append('|---|---|---|---|---|')
        for i, r in enumerate(result['repairs'], 1):
            lines.append(f'| {i} | Step{r["step"]} | {r["type"]} | '
                         f'{r["detail"][:60]} | {r["action"][:40]} |')
        lines.append('')

    # 澄清项
    if result['clarifications']:
        lines.append('## 待确认（已写入方案澄清）')
        lines.append('')
        for c in result['clarifications']:
            lines.append(f'- [{c.get("type", "")}] {c.get("id", "")}')
            for k in ('detail', 'question', 'issues', 'suggestion'):
                if c.get(k):
                    v = c[k]
                    if isinstance(v, list):
                        v = '；'.join(str(x)[:80] for x in v[:3])
                    lines.append(f'  - {k}: {str(v)[:120]}')
        lines.append('')

    # 汇总
    sm = result['summary']
    lines.append('## 汇总')
    lines.append('')
    lines.append(f'- 跑了 {sm["n_steps_run"]} 步')
    lines.append(f'- 修复建议 {sm["n_repairs"]} 条')
    lines.append(f'- 待确认 {sm["n_clarifications"]} 条')
    lines.append(f'- 耗时 {result["elapsed_ms"]} ms')
    lines.append('')

    return '\n'.join(lines)


if __name__ == '__main__':
    print('=' * 92)
    print('Stage 3 触发条件 + 总编排自测')
    print('=' * 92)

    # 触发条件测试
    print('\n【触发条件】')
    CASES = [
        ('小单', '\n'.join(['- 设置 业务刷新：ALL']), '', '', {}, False),
        ('中单', '\n'.join(f'- 新增 对象{i}' for i in range(12)), '', '', {}, True),
        ('大单+通配',
         '\n'.join(f'- 新增 对象{i}' for i in range(12)),
         '| # | 数据清单表 | 业务对象 | 对象数量 | 现网已有 | 命令族 | 动作 | 判断依据 | 状态 |\n'
         '|---|---|---|---|---|---|---|---|---|\n'
         '| 1 | t | o | 1 | 0 | SET APN* | 新增 | x | 确认 |',
         '', {}, True),
        ('guard warn',
         '- 新增 对象',
         '', '',
         {'G30_rmv': {'ok': False, 'reversed': [{'family': 'X'}]}}, True),
    ]
    ok_n = 0
    for name, itxt, ptxt, mtxt, gc, expect in CASES:
        r = should_run_stage3(itxt, ptxt, mtxt, gc)
        match = r['run'] == expect
        ok_n += match
        print(f'  {"✅" if match else "❌"} {name}: run={r["run"]} '
              f'{r["triggers"][0]["id"] if r["triggers"] else r["skipped_reason"][:40]}')
    print(f'  触发条件: {ok_n}/{len(CASES)}')
