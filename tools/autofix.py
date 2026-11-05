# -*- coding: utf-8 -*-
"""autofix.py — 生成产物的自动修复（交付前闭环的第 2 步）。

设计原则：
  · 只做**确定性**修复，能从 schema/意图机械推出的才修
  · 需业务判断的（如引用悬空）不修，只报告
  · 每项修复都记录 before/after 计数，供交付报告引用

可自动修的：
  V1 装配丢失  → 从 schema 重新装配，与现有 mml 取并集
  V3 重复 ADD/SET/MOD → 删除与 EXP 完全相同的命令（SET REFRESHSRV 例外）
  V4 批量不足  → 从意图操作脚本补齐实例

不可自动修的：
  V2 引用悬空  → 该补建父对象？删子对象？改引用？处置相反，需人判断
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, '/opt/expgv/tools')
sys.path.insert(0, '/opt/expgv/backend')

import gen_selfcheck as gs
import fix_exp_template as _fxt


def lines_of(mml_text):
    """保留原始行（含注释/空行），用于回写时保持顺序"""
    return (mml_text or '').split('\n')


def cmd_line_indices(mml_text):
    """返回 [(行号, verb, cmd, params)] —— 只针对可解析的命令行"""
    out = []
    for i, line in enumerate(lines_of(mml_text)):
        s = line.strip()
        if not s or s.startswith('//') or s.startswith('#'):
            continue
        m = gs._CMD_RE.match(s)
        if not m:
            continue
        verb, cmd, body = m.group(1), m.group(2), m.group(3)
        params = {}
        for pm in re.finditer(r'([A-Za-z0-9_]+)\s*=\s*(?:"([^"]*)"|([^,;]+))', body):
            k = pm.group(1).upper()
            v = (pm.group(2) if pm.group(2) is not None else pm.group(3)).strip()
            params[k] = v
        out.append((i, verb, cmd, params))
    return out


def _orig_case(val, intent_text):
    """从意图原文里找该值的原始写法（extract_instances 返回的是大写）。"""
    import re as _re
    up = str(val)
    m = _re.search(_re.escape(up), (intent_text or ''), _re.IGNORECASE)
    if m:
        return m.group(0)
    return up


def main_key_param(params):
    """取该命令的"对象标识参数名"（只返回键名，不含值）。

    ⚠ 不能用 gs._first_ref_param：它返回 'IFNAME=loopback1060' 这种展示串，
      拿来当 dict key 会拼出 IFNAME=loopback1060="LOOPBACK1061" 的畸形命令。
    """
    import re as _re
    for k in params:
        if _re.search(r'(NAME|ID|INDEX|ADDR|DNN|APN)$', k.upper()):
            return k
    return next(iter(params), '')


# ─────────────────────────── V3 去重 ───────────────────────────

def fix_duplicates(mml_text, exp_text, plan_fams=None, v8_fams=None):
    """删除与 EXP 完全相同的命令（唯一豁免 SET REFRESHSRV）。

    ★ 2026-10-30（V3-M2 冲突修复）：
      原实现「与 EXP 同签名就删」会与 V8「从 EXP 补全」打架 ——
      V8 刚补进来的命令，V3 下一轮就删掉，闭环永远收敛不了。

      新口径：只有在 —— 方案**没要求**该族、且 V8 **没补过**该族 —— 时才删。
        · 方案要求该族 → 这是"方案本来就要的"，EXP 里有不代表不该做
        · V8 补过该族   → 是补全动作的产物，不能自我抵消

    返回 (new_mml, removed_list)
    """
    exp_sigs = {gs._cmd_sig(*c) for c in gs.parse_mml(exp_text)}
    if not exp_sigs:
        return mml_text, []

    plan_fams = {f.upper() for f in (plan_fams or set())}
    v8_fams = {f.upper() for f in (v8_fams or set())}

    lines = lines_of(mml_text)
    drop = set()
    removed = []
    seen = set()
    for idx, verb, cmd, params in cmd_line_indices(mml_text):
        sig = gs._cmd_sig(verb, cmd, params)
        if sig not in exp_sigs:
            continue
        if str(cmd).upper() in gs.DUPLICATE_EXEMPT_CMDS:
            continue                     # SET REFRESHSRV 例外
        fam = f'{verb} {cmd}'.upper()
        if fam in plan_fams or fam in v8_fams:
            continue                     # 方案要求 / V8 补的 → 不删
        if sig in seen:
            continue                     # 同一重复只删第一处，保留判断可追溯
        seen.add(sig)
        drop.add(idx)
        removed.append(f'{verb} {cmd}')

    if not drop:
        return mml_text, []
    new_lines = [l for i, l in enumerate(lines) if i not in drop]
    return '\n'.join(new_lines), removed


# ─────────────────────────── V1 装配补齐 ───────────────────────────

def fix_assembly(plan_text, mml_text, schema=None, exp_text=''):
    """方案 md 里有、mml 里没有的命令族 → 从 schema 补齐。

    ⚠ 只在能拿到 schema 时才可能精确补齐；否则退化为「报告不可修」。

    ★ 2026-10-30 修（死循环根因）：补齐时必须**跳过 EXP 里已有的命令**。
      否则 V1 补回来 → V3 删掉 → 下一轮 V1 又补回来，C1 与 C3 互相打架。
      实测 02152：SET DEACTIVERATE / SET IPFARMGLOBAL 在 R1 删、R2 补、R2 又删。

    返回 (new_mml, added_list, note)
    """
    chk = gs.check_assembly(plan_text, mml_text, exp_text)
    missing = chk.get('missing_in_mml') or []
    if not missing:
        return mml_text, [], ''

    if not schema or not (schema.get('steps')):
        return mml_text, [], f'装配丢失 {len(missing)} 族，但无 schema 可补'

    try:
        import gen_assemble as ga
        rebuilt = ga.schema_to_mml(schema)
    except Exception as e:
        return mml_text, [], f'装配丢失 {len(missing)} 族，重新装配失败:{type(e).__name__}'

    # 并集：现有 mml 的行 + 新装配里缺失族对应的行
    have = {f'{c[0]} {c[1]}' for c in gs.parse_mml(mml_text)}
    # EXP 已有命令的签名（补齐时跳过，避免 V1↔V3 死循环）
    exp_sigs = {gs._cmd_sig(*c) for c in gs.parse_mml(exp_text)} if exp_text else set()
    add_lines = []
    skipped_dup = 0
    for line in lines_of(rebuilt):
        s = line.strip()
        if not s or s.startswith('//'):
            continue
        m = gs._CMD_RE.match(s)
        if not m:
            continue
        fam = f'{m.group(1)} {m.group(2)}'
        if fam not in missing or fam in have:
            continue
        # 跳过 EXP 里已有的（让 V3 去重逻辑保持收敛）
        if exp_sigs:
            _p = dict()
            for pm in re.finditer(r'([A-Za-z0-9_]+)\s*=\s*(?:"([^"]*)"|([^,;]+))',
                                  m.group(3)):
                _k = pm.group(1).upper()
                _v = (pm.group(2) if pm.group(2) is not None else pm.group(3)).strip()
                _p[_k] = _v
            if gs._cmd_sig(m.group(1), m.group(2), _p) in exp_sigs:
                skipped_dup += 1
                continue
        add_lines.append(s)
    if not add_lines:
        return mml_text, [], f'装配丢失 {len(missing)} 族，schema 里也没有对应命令'

    new = mml_text.rstrip() + '\n\n// ── 交付前自检补齐（V1 装配丢失）──\n' + '\n'.join(add_lines) + '\n'
    _n = f'从 schema 补齐 {len(add_lines)} 条命令'
    if skipped_dup:
        _n += f'（跳过 EXP 已有的 {skipped_dup} 条）'
    return new, add_lines, _n


# ─────────────────────────── V4 批量补齐 ───────────────────────────

def fix_batch(intent_text, mml_text):
    """意图操作脚本里有多实例，产物只做了一个 → 补齐。

    复用 agent_projection.backfill_batch_from_intent 的思路：
    提取实例集合，对 mml 里缺少的实例生成命令。

    返回 (new_mml, added_list, note)
    """
    chk = gs.check_batch_coverage(intent_text, mml_text)
    under = chk.get('under_covered') or []
    if not under:
        return mml_text, [], ''

    # 需要按命令族取模板：从 mml 里找该族的第一条命令，替换主键值
    by_fam = {}
    for idx, verb, cmd, params in cmd_line_indices(mml_text):
        by_fam.setdefault(f'{verb} {cmd}', (verb, cmd, params))

    add_lines = []
    for u in under:
        # check_batch_coverage 返回 {family, need, got, missing[], missing_n, ratio}
        fam = u.get('family') or u.get('cmd') or ''
        if fam not in by_fam:
            continue
        verb, cmd, tpl_params = by_fam[fam]
        keyp = main_key_param(tpl_params)
        miss_vals = u.get('missing') or []
        if not keyp or not miss_vals:
            continue
        # 已有实例（避免每轮重复补同一条）
        have_vals = set()
        for x in cmd_line_indices(mml_text):
            if f'{x[1]} {x[2]}' == fam and keyp in x[3]:
                have_vals.add(str(x[3][keyp]).upper())
        for val in miss_vals:
            if str(val).upper() in have_vals:
                continue
            params = dict(tpl_params)
            # 保留意图里的原始大小写（extract_instances 会转大写，这里回填原值）
            params[keyp] = _orig_case(val, intent_text)
            parts = []
            for k, v in params.items():
                sv = str(v)
                parts.append(f'{k}="{sv}"' if any(c.isalpha() for c in sv) else f'{k}={sv}')
            add_lines.append(f'{verb} {cmd}:' + ','.join(parts) + ';')

    if not add_lines:
        # ★ 说清为什么补不了（原始报告只有「无法构造」四个字，看不出卡在哪）
        _why = []
        for u in under:
            fam = u.get('family') or ''
            if fam not in by_fam:
                _why.append(f'{fam} 在 mml 里没有模板命令')
            elif not (u.get('missing') or []):
                _why.append(f'{fam} 未提供缺失实例清单')
            else:
                _why.append(f'{fam} 缺主键参数')
        return mml_text, [], (f'批量不足 {len(under)} 族但补不了：' + '；'.join(_why[:3]))

    new = mml_text.rstrip() + '\n\n// ── 交付前自检补齐（V4 批量不足）──\n' + '\n'.join(add_lines) + '\n'
    return new, add_lines, f'补齐 {len(add_lines)} 条实例命令'


# ─────────────────────────── 闭环主函数 ───────────────────────────

def _build_pending_md(suggestions, exp_filename=''):
    """生成写进方案 md 的「待确认」段落（空则返回空串）"""
    if not suggestions:
        return ''
    try:
        import suggest_creation as _sc3
        return _sc3.build_pending_confirm(suggestions, exp_filename or '')
    except Exception:
        return ''


def autofix(plan_text, mml_text, exp_text, intent_text, schema=None,
            max_rounds=3, exp_filename=''):
    """交付前自检闭环：校验 → 修复 → 复验，最多 max_rounds 轮。

    返回 {
      'mml': 修复后的文本,
      'rounds': [...每轮的 before/after 指标...],
      'fixed': {V1: n, V3: n, V4: n},
      'unfixable': [{check, detail, why}],
      'final': 最终自检结果,
      'ok': bool,
    }
    """
    cur = mml_text
    rounds = []
    fixed = {'V1': 0, 'V3': 0, 'V4': 0, 'V8': 0}
    notes = []

    # V3 去重的豁免集合（方案明确要求的族）
    _plan_fams = {f'{v} {c}'.upper() for v, c, p in
                  gs.parse_mml(gs._exclude_non_target(plan_text))}

    # ★ 2026-10-31 修（补建族被当重复删掉）：
    #   _plan_fams 原来只取**方案 md** 里的族。但装配阶段有两类命令不在方案 md 里：
    #     ① 方案 B 从意图补建的族（方案没写但意图要求）
    #     ② G9 从 EXP 同族补全的命令
    #   ⇒ G3 把它们当"EXP 已有 = 重复"删掉。
    #   实测 NC20260911000610：
    #     意图要求 SET LICENSESWITCH:LICITEM="LKV3G5DFIS01",SWITCH=ENABLE
    #     装配时补建成功（schema 里有 step10，origin=intent）
    #     但 autofix round0 的 C3 判定为重复 → round1 删掉 → 产物 0 条
    #     ⇒ GT 族覆盖从 100% 掉到 50%
    #   修法：把**当前产物里已有的族**也纳入豁免集合。
    #   （产物是补建后的结果，意图要求什么它就有什么；
    #     真·多余的族由 C1 装配一致性 / C4 批量覆盖负责，不靠 C3 删。）
    #   精确做法：只纳入**意图操作脚本里明确要求的族**（不纳产物全部族，
    #   否则 G3 等于失效）。意图是事中可得输入，不是事后视角。
    _plan_fams_from_intent = True
    try:
        if intent_text:
            _ops = gs._intent_ops_section(intent_text)                 if hasattr(gs, '_intent_ops_section') else intent_text
            _plan_fams |= {f'{v} {c}'.upper() for v, c, p in gs.parse_mml(_ops)}
    except Exception:
        pass

    def snap(t, plan_fams=None):
        c1 = gs.check_assembly(plan_text, t, exp_text)
        c2 = gs.check_references(t, exp_text)
        c3 = gs.check_duplicate(t, exp_text, plan_fams=plan_fams)
        c4 = gs.check_batch_coverage(intent_text, t)
        return {
            'C1': len(c1.get('missing_in_mml') or []),
            'C2': len(c2.get('dangling') or []),
            'C3': len(c3.get('duplicates') or []),
            'C4': len(c4.get('under_covered') or []),
            'n_cmds': len(gs.parse_mml(t)),
            '_raw': {'C1': c1, 'C2': c2, 'C3': c3, 'C4': c4},
        }

    before = snap(cur, _plan_fams)
    rounds.append({'round': 0, 'phase': 'before', 'm': before})

    _v8_fams = set()

    for rnd in range(1, max_rounds + 1):
        changed = False

        # ① V1 装配补齐
        #   ★ 2026-10-30 调整顺序：原来 V3 在最先，但 V1/V4 补齐时会把 EXP 里
        #     已有的命令重新加回来 ⇒ 下一轮 V3 又删一次，最终仍残留重复。
        #     实测 02152：R1 删 SET DEACTIVERATE、R2 又删一次，最终 C3=1。
        #     改为「先补齐、后去重」，去重永远在末尾执行，保证终态干净。
        cur2, added, note = fix_assembly(plan_text, cur, schema, exp_text)
        if added:
            fixed['V1'] += len(added)
            notes.append(f'R{rnd} V1 {note}')
            cur = cur2
            changed = True
        elif note:
            notes.append(f'R{rnd} V1 {note}（无法自动修）')

        # ①' V8 EXP 同族模板补全（V3-M2，2026-10-30）
        #   用户拍板 1B：先全部允许照抄，发现问题再禁。
        #   ★ 放在 V1 之后：V1 用 schema 精确补，V8 用 EXP 模板兜底补
        cur8, added8, note8 = _fxt.fix_exp_template(plan_text, cur, exp_text, intent_text)
        if added8:
            fixed['V8'] += len(added8)
            notes.append(f'R{rnd} V8 {note8}')
            for _ln in added8:
                _m = gs._CMD_RE.match(str(_ln).strip())
                if _m:
                    _v8_fams.add(f'{_m.group(1)} {_m.group(2)}'.upper())
            cur = cur8
            changed = True

        # ② V4 批量补齐
        cur3, added4, note4 = fix_batch(intent_text, cur)
        if added4:
            fixed['V4'] += len(added4)
            notes.append(f'R{rnd} V4 {note4}')
            cur = cur3
            changed = True
        elif note4:
            notes.append(f'R{rnd} V4 {note4}')

        # ③ V3 去重（放在最后：补齐可能带回 EXP 已有命令，此步保证终态干净）
        cur, rm = fix_duplicates(cur, exp_text, plan_fams=_plan_fams, v8_fams=_v8_fams)
        if rm:
            fixed['V3'] += len(rm)
            notes.append(f'R{rnd} 删除重复下发 {len(rm)} 条：{", ".join(rm[:6])}')
            changed = True

        after = snap(cur, _plan_fams)
        rounds.append({'round': rnd, 'phase': 'after', 'm': after})

        if not changed:
            break
        # 全绿就停
        if (after['C1'] + after['C3'] + after['C4']) == 0:
            break

    final = snap(cur, _plan_fams)
    unfixable = []
    suggestions = []
    if final['C2'] > 0:
        # ★ 2026-10-30：引用悬空 → 生成**注释掉的**补建建议 + 问询（不自动执行）
        #   用户裁决：只做①（提醒 + EXP 对齐），不猜补建/删子/改引用
        try:
            import suggest_creation as _sc2
            _dang = final['_raw']['C2'].get('dangling') or []
            # EXP 佐证（用于 ④ 判断）
            _exp_info = {}
            if exp_filename:
                try:
                    import check_v0_v5 as _v
                    _nf = _v.check_exp_nf(exp_filename, intent_text)
                    _align = _v.check_exp_content_alignment(intent_text, exp_text)
                    _exp_info = {'exp_nf': _nf.get('exp_nf', ''),
                                 'warn_exp_nf': _align.get('warn', False),
                                 'detail': _align.get('detail', '') or _nf.get('detail', '')}
                except Exception:
                    pass
            for _d in _dang[:20]:
                sg = _sc2.build_suggestion(_d, _exp_info)
                suggestions.append(sg)
            if suggestions:
                _blk = _sc2.build_block(suggestions, exp_filename or '')
                if _blk.strip() and '⚠ 交付前自检（V2' not in cur:
                    cur = cur.rstrip() + '\n' + _blk
            unfixable.append({
                'check': 'V2 引用悬空',
                'n': final['C2'],
                'detail': _dang[:5],
                'why': '已生成注释掉的补建建议 + 问询。'
                       '按概率：④ EXP 拿错网元最可能，① 规划占位次之；'
                       '② 该删不该删基本不存在；③ 人为写错不管。需人工确认后再改。',
            })
        except Exception as _e:
            unfixable.append({
                'check': 'V2 引用悬空',
                'n': final['C2'],
                'detail': (final['_raw']['C2'].get('dangling') or [])[:5],
                'why': f'生成建议失败({type(_e).__name__}) ⇒ 交人工',
            })
    if final['C1'] > 0:
        unfixable.append({
            'check': 'V1 装配丢失',
            'n': final['C1'],
            'detail': (final['_raw']['C1'].get('missing_in_mml') or [])[:8],
            'why': '缺少对应 schema step，无法机械补齐 ⇒ 需重新规划这几族',
        })
    if final['C4'] > 0:
        unfixable.append({
            'check': 'V4 批量不足',
            'n': final['C4'],
            'detail': (final['_raw']['C4'].get('under_covered') or [])[:5],
            'why': '意图里没有完整实例清单，或产物缺少该族的模板命令',
        })

    return {
        'mml': cur,
        'rounds': rounds,
        'fixed': fixed,
        'notes': notes,
        'unfixable': unfixable,
        'suggestions': suggestions,
        'pending_md': _build_pending_md(suggestions, exp_filename),
        'final': {k: v for k, v in final.items() if k != '_raw'},
        'ok': (final['C1'] + final['C2'] + final['C3'] + final['C4']) == 0,
    }


if __name__ == '__main__':
    # 冒烟：读入一个会话的产物跑一遍
    sid = sys.argv[1] if len(sys.argv) > 1 else ''
    base = Path(f'/data/sessions/{sid}/gen_v1/g1') if sid else None
    if not base or not base.exists():
        print('用法: autofix.py <session_id>')
        sys.exit(1)
    plan = next((p.read_text(errors='replace') for p in base.glob('配置分析*.md')), '')
    mml = (base / 'mml.txt').read_text(errors='replace') if (base / 'mml.txt').exists() else ''
    schema = None
    if (base / 'schema.json').exists():
        import json
        schema = json.loads((base / 'schema.json').read_text())
    print('（冒烟需 exp/intent，此处仅验证可导入）')
    print(f'plan {len(plan)} mml {len(mml)} schema {bool(schema)}')
