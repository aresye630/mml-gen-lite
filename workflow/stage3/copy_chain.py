"""Step 6：照着配的三场景整合。

★ 2026-11-12 P0-6

## 三场景（实测 86 单分布）

| 场景 | 占比 | 特征 | 处理 |
|---|---|---|---|
| A 参照对象 + 业务段都有 | 17% | 意图说「按现网 X 配齐」+ 清单给了名字 | 提取参照链 → 校验 → 平移 |
| B 只有业务段 | 20% | 只说「新增 URR sos_sig_xxx」 | 自动找参照 → 校验 → 平移 |
| C 只有参照对象 | 5% | 说「按现网 X 配齐」但清单没给名字 | 输出澄清问业务段 |
| D 都不需要 | 58% | 新建对象，不涉及参照 | 走 Step 1-5 |

## 依赖的已完成模块

  biz_cluster.py   业务段识别 / 簇成员发现 / 名字平移 / 骨架校验
  auto_ref.py      自动选参照（四维评分）
  ref_validate.py  参照结构校验（参数覆盖 / 形态代表性）
  attr_fill.py     属性族链补齐

## 本模块做的整合

  1. 场景判定（从意图 + 数据清单）
  2. 场景 A/B 的完整流程
  3. 场景 C 的澄清输出
  4. 失败项统一进澄清（用户裁定：失败要列出来，补进澄清）
"""
import json
import re
import sys
from pathlib import Path

_S3 = str(Path(__file__).parent)
if _S3 not in sys.path:
    sys.path.insert(0, _S3)

try:
    import biz_cluster as BC
except Exception:
    BC = None
try:
    import auto_ref as AR
except Exception:
    AR = None
try:
    import ref_validate as RV
except Exception:
    RV = None


# ═══════════════════════════════════════════════════════════
# 场景判定
# ═══════════════════════════════════════════════════════════

# 「按现网 X 配齐」类措辞
RE_HAS_REF = re.compile(
    r'按现网|参照|照.{0,12}存量|按.{0,12}做法|按同类|按现网同类')

# 业务段候选
# ★ 2026-11-12 放宽：原要求至少 1 个下划线（{2,} 段），
#   但 up_sos / sos_sig 这类也要能识别
#   实测漏识别：数据清单只给「up_sos」时判不出业务段
RE_BIZ_LIKE = re.compile(r'\b([a-z][a-z0-9]{2,}(?:[_\-\.][a-z0-9]+)*)\b')

# 通用词（不是业务段）
GENERIC_BIZ_WORDS = {
    'see', 'the', 'and', 'for', 'with', 'from', 'into', 'data', 'list',
    'user', 'profile', 'pool', 'group', 'rule', 'policy', 'filter',
    'online', 'offline', 'default', 'enable', 'disable', 'true', 'false',
}


def detect_scene(intent_text, dataset_text=''):
    """判定属于哪个场景。

    返回：
      {
        'scene': 'A'|'B'|'C'|'D',
        'has_ref': bool,
        'biz_segments': [...],      # 从文本里采到的业务段候选
        'ref_hints': [...],         # 意图里提到的参照对象（「XX」里的）
        'reason': str,
      }
    """
    itxt = intent_text or ''
    dtxt = dataset_text or ''
    both = itxt + '\n' + dtxt

    has_ref = bool(RE_HAS_REF.search(itxt))

    # 参照对象候选：从「按现网同类XX「YY」」里提
    # ★ 2026-11-12 修：必须带「参照的对象类型」，否则会把
    #   「用户模板 up_ims」当成 RULE 的参照（实测踩坑）
    #   格式：'用户模板「up_sos」的配置：按现网同类用户模板「up_ims」的存量做法配齐'
    #   → {'obj_type': '用户模板', 'inst': 'up_sos', 'ref_inst': 'up_ims'}
    ref_hints = []
    for m in re.finditer(
            r'([^\s「]+)\s*「([^」]+)」的配置[：:]\s*'
            r'按现网同类\s*([^\s「]+)\s*「([^」]+)」', itxt):
        ref_hints.append({
            'obj_type': m.group(1),
            'ref_obj_type': m.group(3),
            'target_inst': m.group(2),
            'ref_inst': m.group(4),
        })
    # 兜底 1：宽松格式「按现网 XXX 的存量做法」
    #   实测：「按现网 cmnet 的存量做法配齐」→ 参照对象是 cmnet
    if not ref_hints:
        for m in re.finditer(r'按现网\s+([A-Za-z0-9_\-\.]+)\s*的', itxt):
            ref_hints.append({'obj_type': None, 'ref_obj_type': None,
                              'target_inst': None, 'ref_inst': m.group(1)})
    # 兜底 2：「参照「XXX」」
    if not ref_hints:
        for m in re.finditer(r'参照\s*[^\s「]*\s*「([^」]+)」', itxt):
            ref_hints.append({'obj_type': None, 'ref_obj_type': None,
                              'target_inst': None, 'ref_inst': m.group(1)})

    # ★ 2026-11-12 关键区分：目标业务段 vs 参照对象的业务段
    #   实测反例：意图「按现网 cmnet 的存量做法配齐」里 cmnet 是【参照对象】，
    #   不是【目标业务段】。旧实现把它当业务段 → 场景误判成 B。
    #
    #   规则：只从「数据清单」里取业务段（清单是目标侧数据），
    #        意图里的复合名只作为补充，且要排除掉参照提示里出现过的。

    # ★ 2026-11-12：只排除「参照实例」，不排除「目标实例」
    #   实测反例：「用户模板「up_sos」的配置：按现网同类用户模板「up_ims」」
    #   up_sos 是目标，up_ims 是参照。旧实现把两者都排除了 → 业务段识别失败
    ref_insts = set()
    target_insts = set()
    for h in ref_hints:
        if isinstance(h, dict):
            if h.get('ref_inst'):
                ref_insts.add(h['ref_inst'])
            if h.get('target_inst'):
                target_insts.add(h['target_inst'])
        elif isinstance(h, str):
            ref_insts.add(h)

    # 目标实例名集合（用于场景 A 判定：有参照 + 有目标实例即可）
    target_insts_for_scene = set()
    for h in ref_hints:
        if isinstance(h, dict) and h.get('target_inst'):
            target_insts_for_scene.add(h['target_inst'])

    def _is_target_biz(cand):
        """候选是否是「目标侧」业务段。"""
        head = cand.split('_')[0]
        if head in GENERIC_BIZ_WORDS or len(head) < 2:
            return False
        # 目标实例本身 → 算目标业务段
        if cand in target_insts:
            return True
        # 排除参照对象本身及其派生
        if cand in ref_insts:
            return False
        for ri in ref_insts:
            if not ri:
                continue
            if cand == ri or cand.startswith(ri + '_') or cand.startswith(ri + '.'):
                return False
        return True

    # 主线：数据清单
    biz_cands = set()
    for m in RE_BIZ_LIKE.finditer(dtxt):
        cand = m.group(1)
        if _is_target_biz(cand):
            biz_cands.add(cand)

    # 补充：意图里的复合名（但排除参照对象）
    for m in RE_BIZ_LIKE.finditer(itxt):
        cand = m.group(1)
        if _is_target_biz(cand):
            biz_cands.add(cand)

    # ★ 2026-11-12：场景 A 的判据放宽
    #   「有参照 + 有目标实例」就算 A（不一定需要复合名形态的业务段）
    #   实测：「用户模板「up_sos」的配置：按现网同类用户模板「up_ims」配齐」
    #        数据清单只给 up_sos（单段名）→ 旧逻辑判不出业务段 → 误判 C
    _tgt_insts = {h['target_inst'] for h in ref_hints
                  if isinstance(h, dict) and h.get('target_inst')}
    if has_ref and (biz_cands or _tgt_insts):
        n_biz = len(biz_cands) or len(_tgt_insts)
        scene, reason = 'A', f'有参照对象（{len(ref_hints)} 个）+ 目标业务（{n_biz} 个）'
    elif biz_cands:
        scene, reason = 'B', f'只有业务段（{len(biz_cands)} 个），需自动找参照'
    elif has_ref:
        scene, reason = 'C', '只有参照对象，业务段未知 → 需澄清'
    else:
        scene, reason = 'D', '不涉及参照（新建对象），走 Step 1-5'

    return {
        'scene': scene, 'has_ref': has_ref,
        'biz_segments': sorted(biz_cands)[:20],
        'ref_hints': ref_hints[:10],
        'reason': reason,
    }


# ═══════════════════════════════════════════════════════════
# 场景 A/B：参照配齐
# ═══════════════════════════════════════════════════════════

def _biz_from_single_name(name):
    """从单个对象名里剥出业务段。

    实测样例：
      r_ims_sig              → ims_sig   （剥前缀 r_）
      up_ims                 → ims       （剥前缀 up_）
      ims_sig_ch_p           → ims_sig   （剥后缀 _ch_p）
      ims_sig_pcc_p_g        → ims_sig   （剥后缀 _pcc_p_g）
      12530_01_cbb_offline   → 12530_01  （剥后缀 _cbb_offline）

    做法：已知前缀/后缀表，逐个尝试剥离；都不匹配则返回原名。
    """
    if not name:
        return None
    n = name

    # 已知前缀（按长度降序，优先剥长的）
    PREFIXES = ['up_group_', 'upg_', 'u_p_g_', 'u_p_', 'up_', 'r_', 'mk_', 'cg_']
    for pfx in PREFIXES:
        if n.lower().startswith(pfx):
            n = n[len(pfx):]
            break

    # 已知后缀
    SUFFIXES = ['_pcc_p_g', '_cbb_offline', '_cbb_online', '_ch_p',
                '_pcc_p', '_g', '_p', '_r']
    for sfx in SUFFIXES:
        if n.lower().endswith(sfx) and len(n) > len(sfx):
            n = n[:-len(sfx)]
            break

    return n if n and n != name else name


def infer_biz_segment_from_names(names):
    """从一组已知对象名里反推业务段（如 sos_sig_pcc_p_g → sos_sig）。"""
    if not BC or not names:
        return None
    seg, _cands = BC.extract_biz_segment(names)
    return seg


def run_scene_a_or_b(scene_info, exp_paths, family, target_biz,
                     intent_line='', target_params=None):
    """场景 A/B 的主流程：选参照 → 校验 → 平移。

    参数：
      scene_info     detect_scene 的返回
      exp_paths      EXP 路径列表
      family         目标族（如 'RULE'）
      target_biz     目标业务段（如 'sos' / 'sos_sig'）
      intent_line    意图里对应的那一行（用于提取约束）
      target_params  目标需要的参数集（来自意图推断或 GT 离线校验）

    返回：
      {
        'ok': bool,
        'reference': {'name':..., 'exp':..., 'score':..., 'how': 'auto'|'hint'},
        'validation': {...},
        'translated': [{'ref_name':..., 'target_name':..., 'skeleton_ok':...}],
        'issues': [...],
      }
    """
    out = {'ok': False, 'reference': None, 'validation': None,
           'translated': [], 'issues': []}

    if not AR:
        out['issues'].append('auto_ref 模块不可用')
        return out

    # ── Step 1 选参照 ──
    # 优先用意图里明示的参照对象（但必须是本族的）
    # ★ 2026-11-12 修：旧做法直接取 ref_hints[0]，
    #   实测把「用户模板的参照 up_ims」用到了 RULE 族上 → 找不到
    #   正确做法：先用参数覆盖校验确认该参照属于本族，不属于才自动选
    hint_ref = None
    for h in (scene_info.get('ref_hints') or []):
        cand = h.get('ref_inst') if isinstance(h, dict) else h
        if not cand:
            continue
        # 校验：这个参照在 EXP 的本族里存在吗
        if RV:
            v = RV.validate_reference_structure(
                exp_paths, family, cand, target_params=target_params)
            if not v.get('skipped') and v.get('issues') is not None:
                # 不在本族里 → 跳过这个提示
                if any('不在' in str(i) for i in (v.get('issues') or [])):
                    continue
            hint_ref = cand
            break
        else:
            hint_ref = cand
            break

    if hint_ref:
        # 验证这个参照存在且合适
        if RV:
            v = RV.validate_reference_structure(
                exp_paths, family, hint_ref, target_params=target_params)
            if v.get('skipped'):
                out['issues'].append(f'意图给的参照 {hint_ref} 在 EXP 里找不到')
                hint_ref = None
            elif not v.get('ok'):
                out['issues'].append(
                    f'意图给的参照 {hint_ref} 结构不符: {v.get("issues")}')
                # 尝试用 better_candidates 换
                better = v.get('better_candidates') or []
                if better:
                    hint_ref = better[0]['name']
                    out['issues'].append(f'改用更好的参照: {hint_ref}')
                else:
                    hint_ref = None

    if hint_ref:
        out['reference'] = {'name': hint_ref, 'how': 'intent_hint'}
    else:
        # 自动选
        r = AR.auto_select_reference(exp_paths, family, intent_line or '',
                                     target_biz=target_biz)
        if not r.get('best'):
            out['issues'].append(f'无法自动选参照: {r.get("reason")}')
            return out
        out['reference'] = {
            'name': r['best']['name'],
            'exp': r['best']['exp'],
            'score': r['best']['score'],
            'how': 'auto',
            'candidates': [c['name'] for c in r['candidates'][:3]],
        }

    # ── Step 2 结构校验 ──
    if RV and target_params:
        v = RV.validate_reference_structure(
            exp_paths, family, out['reference']['name'],
            target_params=target_params)
        out['validation'] = {
            'ok': v.get('ok'), 'issues': v.get('issues'),
            'missing': v.get('missing'),
            'shape_share': v.get('ref_shape_share'),
        }
        if not v.get('ok'):
            out['issues'].extend(v.get('issues') or [])

    # ── Step 3 名字平移 ──
    if BC and target_biz:
        # 从参照对象的实例名反推参照业务段
        ref_name = out['reference']['name']
        # ★ 2026-11-12：单名字无法用「多名字取公共段」的方法，
        #   改用「剥掉通用前后缀」的方式（r_ims_sig → ims_sig）
        ref_biz = _biz_from_single_name(ref_name)
        if ref_biz:
            tgt_name = BC.translate_name(ref_name, ref_biz, target_biz)
            sk = BC.check_skeleton_preserved(ref_name, tgt_name, ref_biz, target_biz)
            # ★ 2026-11-12 修误报：先看参照名本身在现网是否是「主流形态」
            #   实测 RULE：r_ims_sig 的 r_ 前缀只占 0.3%，但它是现网真实存在的对象
            #   平移后 r_sos_sig 继承同样结构 → 不应判「不符形态」
            #   判据：只要参照名本身合法（在现网存在），平移结果就继承合法性
            ref_pat = BC.check_name_against_pattern(
                family, ref_name, exp_paths[0] if exp_paths else '')
            pat = BC.check_name_against_pattern(
                family, tgt_name, exp_paths[0] if exp_paths else '')

            # 参照名是特例形态（占比低）→ 平移结果也标特例，但不报错
            pattern_ok = pat.get('ok') or (not ref_pat.get('ok'))
            pattern_note = ''
            if not pat.get('ok') and not ref_pat.get('ok'):
                pattern_note = (f'参照名本身即特例形态（{ref_pat.get("reason", "")[:60]}），'
                                f'平移结果继承该形态，建议核对')

            out['translated'].append({
                'ref_name': ref_name, 'target_name': tgt_name,
                'ref_biz': ref_biz, 'target_biz': target_biz,
                'skeleton_ok': sk.get('ok'),
                'skeleton_reason': sk.get('reason'),
                'pattern_ok': pattern_ok,
                'pattern_reason': pat.get('reason'),
                'pattern_note': pattern_note,
                'ref_pattern_ok': ref_pat.get('ok'),
            })
            if not pattern_ok:
                out['issues'].append(f'平移后的名字不符现网形态: {pat.get("reason")}')
            elif pattern_note:
                out['issues'].append(f'提示：{pattern_note}')
        else:
            out['issues'].append(f'无法从 {ref_name} 反推参照业务段')
    else:
        out['issues'].append('缺少业务段，无法平移名字')

    out['ok'] = bool(out['reference'] and out['translated'])
    return out


# ═══════════════════════════════════════════════════════════
# 场景 C：只输出澄清
# ═══════════════════════════════════════════════════════════

def build_scene_c_clarification(scene_info, family, exp_paths):
    """场景 C：只有参照对象没有业务段 → 输出澄清项。

    按用户裁定：「失败要列出来，补进澄清里」
    """
    ref_name = scene_info['ref_hints'][0] if scene_info.get('ref_hints') else None

    chain_families = []
    names_pattern = ''
    first_exp = (exp_paths[0] if exp_paths else '')
    if BC and ref_name and first_exp and Path(first_exp).exists():
        try:
            biz, _ = BC.extract_biz_segment([ref_name])
            if biz:
                cluster = BC.find_cluster_members(first_exp, biz)
                chain_families = sorted(cluster.keys())[:10]
                # 归纳命名模式
                pats = []
                for fam, d in list(cluster.items())[:5]:
                    for nm in (d.get('names') or [])[:1]:
                        if biz in nm:
                            pats.append(nm.replace(biz, '<业务段>'))
                names_pattern = ' / '.join(pats[:3])
        except Exception:
            pass

    return {
        'id': f'stage3-sceneC-{family}',
        'type': '参照配齐失败',
        'scene': 'C 只有参照无业务段',
        'reference_object': ref_name,
        'family': family,
        'missing_info': '目标业务段名称',
        'what_we_found': {
            'cluster_families': chain_families,
            'names_pattern': names_pattern,
        },
        'question': (f'本次要新建的业务段叫什么？'
                     f'（参照 {ref_name} 的命名结构，填业务段即可自动生成全部名字）'),
        'example': (f'若填 <业务段>，将生成 {names_pattern}' if names_pattern
                    else '若填 <业务段>，将按参照对象的命名结构生成'),
    }


# ═══════════════════════════════════════════════════════════
# 统一入口
# ═══════════════════════════════════════════════════════════

def run_step6(intent_text, dataset_text, exp_paths,
              families_and_biz=None, target_params_map=None):
    """Step 6 统一入口。

    参数：
      intent_text        意图全文
      dataset_text       数据清单全文
      exp_paths          EXP 路径列表
      families_and_biz   [{'family': 'RULE', 'biz': 'sos_sig', 'line': '...'}]
                         若为 None 则只用 scene 判定
      target_params_map  {'RULE': {'POLICYTYPE', 'FILTERINGMODE', ...}}

    返回：
      {
        'scene': {...},
        'results': [每个族的处理结果],
        'clarifications': [...],   # 需用户回答的
        'summary': {...},
      }
    """
    scene = detect_scene(intent_text, dataset_text)
    results = []
    clarifications = []

    if scene['scene'] == 'D':
        return {'scene': scene, 'results': [], 'clarifications': [],
                'summary': {'scene': 'D', 'n_results': 0, 'n_ok': 0,
                            'n_failed': 0, 'n_clarifications': 0,
                            'reason': '不涉及参照，走 Step 1-5'}}

    # 场景 C：直接输出澄清
    if scene['scene'] == 'C':
        fams = [f['family'] for f in (families_and_biz or [])] or ['(未知族)']
        for fam in fams:
            clarifications.append(
                build_scene_c_clarification(scene, fam, exp_paths))
        return {'scene': scene, 'results': [], 'clarifications': clarifications,
                'summary': {'scene': 'C', 'n_results': 0,
                            'n_clarifications': len(clarifications)}}

    # 场景 A/B：逐族跑流程
    for item in (families_and_biz or []):
        fam = item['family']
        biz = item['biz']
        line = item.get('line') or intent_text
        tps = (target_params_map or {}).get(fam)
        r = run_scene_a_or_b(scene, exp_paths, fam, biz,
                             intent_line=line, target_params=tps)
        r['family'] = fam
        r['target_biz'] = biz
        results.append(r)
        # 失败项进澄清
        if not r['ok'] or r.get('issues'):
            clarifications.append({
                'id': f'stage3-{fam}',
                'type': '参照配齐有异常',
                'family': fam,
                'target_biz': biz,
                'reference': (r.get('reference') or {}).get('name'),
                'issues': r.get('issues') or [],
                'needs_review': True,
            })

    # 若无 families_and_biz，用场景的 biz_segments 自动推
    if not (families_and_biz or []):
        clarifications.append({
            'id': 'stage3-no-family',
            'type': '需要明确族',
            'scene': scene['scene'],
            'biz_segments': scene['biz_segments'],
            'question': '检测到涉及参照配齐，但未明确是哪个命令族，请确认要处理哪些族',
        })

    return {
        'scene': scene,
        'results': results,
        'clarifications': clarifications,
        'summary': {
            'scene': scene['scene'],
            'n_results': len(results),
            'n_ok': sum(1 for r in results if r['ok']),
            'n_failed': sum(1 for r in results if not r['ok']),
            'n_clarifications': len(clarifications),
        },
    }


if __name__ == '__main__':
    import json as _json

    GT = _json.loads(Path('/tmp/gt_cleaned.json').read_text(encoding='utf-8'))
    g = next(x for x in GT if x['ticket'] == 'NC20260810002261')
    adir = Path(g['path']) / '备份附件'
    EXPS = [str(p) for p in sorted(adir.glob('*.txt'))]
    ITXT = Path('/tmp/intent_v3/NC20260810002261_意图.md').read_text(encoding='utf-8')
    DTXT = Path('/tmp/intent_v3/NC20260810002261_数据清单.md').read_text(encoding='utf-8')

    print('=' * 92)
    print('Step 6 自测：三场景判定 + 参照配齐')
    print('=' * 92)

    sc = detect_scene(ITXT, DTXT)
    print(f'\n【场景判定】')
    print(f'  scene={sc["scene"]}  {sc["reason"]}')
    print(f'  参照提示: {sc["ref_hints"]}')
    print(f'  业务段候选: {sc["biz_segments"][:8]}')

    print(f'\n【场景 A/B 流程：RULE 族】')
    r = run_step6(
        ITXT, DTXT, EXPS,
        families_and_biz=[{
            'family': 'RULE',
            'biz': 'sos_sig',
            'line': '新增 规则（策略类型为PCC，优先级为1000，过滤模式为FLOWFILTER）',
        }],
        target_params_map={'RULE': {'RULENAME', 'POLICYTYPE', 'PRIORITY',
                                    'POLICYNAME', 'FLOWFILTERNAME',
                                    'FILTERINGMODE', 'RULESPECTYPE'}},
    )
    print(f'  汇总: {r["summary"]}')
    for res in r['results']:
        print(f'  族 {res["family"]}: ok={res["ok"]}')
        if res.get('reference'):
            print(f'    参照: {res["reference"]}')
        if res.get('validation'):
            print(f'    校验: ok={res["validation"]["ok"]} '
                  f'missing={res["validation"]["missing"]}')
        for t in res.get('translated') or []:
            print(f'    平移: {t["ref_name"]} → {t["target_name"]}')
            print(f'          骨架={t["skeleton_ok"]} 形态={t["pattern_ok"]}')
        for iss in res.get('issues') or []:
            print(f'    问题: {iss[:80]}')
