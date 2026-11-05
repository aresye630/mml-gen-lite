"""summary.py — 代码生成每步的摘要（给下一步看）。

★ 用户裁决（2026-11-03）：摘要由代码按模板生成（A 方案），
  不靠 agent 自述 —— 稳定可控；配 loop 兜底。

★ 摘要的作用：下一步的 prompt 只带摘要（约 500~800 字），不带全量 json。
  若摘要不足，下一步通过 contract.pull_strategy 回要明细。
"""
from typing import Any


def _fmt_kv(d: dict, limit: int = 6) -> str:
    items = list(d.items())[:limit]
    s = '，'.join('%s=%s' % (k, v) for k, v in items)
    if len(d) > limit:
        s += ' …共%d项' % len(d)
    return s


def summary_01(out: dict) -> str:
    """意图分解 → 给检索看。"""
    subs = out.get('subtasks') or []
    if not subs:
        return '（意图分解无产出，检索将直接从意图原文提取关键词）'

    lines = ['本工单需完成 %d 个子任务：' % len(subs)]
    for s in subs[:10]:
        act = s.get('action', '?')
        tgt = s.get('target', '?')
        hint = s.get('families_hint') or []
        tail = '（可能是 %s）' % '/'.join(hint) if hint else ''
        unmapped = ' ⚠未能映射功能关键词' if s.get('unmapped') else ''
        lines.append('  %s. %s「%s」%s%s' % (s.get('id', '?'), act, tgt, tail, unmapped))
    if len(subs) > 10:
        lines.append('  …另有 %d 个' % (len(subs) - 10))
    if out.get('raw_intent_ref'):
        lines.append('完整意图：%s' % out['raw_intent_ref'])
    return '\n'.join(lines)


def summary_02(out: dict) -> str:
    """检索 → 给方案看。"""
    lines = []
    adopted = out.get('adopted_docs') or []
    retrieval = out.get('retrieval') or []

    n_excl = sum(len([c for c in r.get('candidates', []) if not c.get('adopted')])
                 for r in retrieval)
    lines.append('检索采用文档 %d 篇，排除 %d 篇。' % (len(adopted), n_excl))

    if out.get('no_basis'):
        lines.append('⚠ 无任何文档命中，方案将仅依据 EXP 形态推导。')

    # 采用的文档 + 命令链
    excerpts = out.get('doc_excerpts') or {}
    for doc in adopted[:5]:
        lines.append('· 采用：%s' % doc)
        ex = excerpts.get(doc) or {}
        chain = ex.get('command_chain') or []
        if chain:
            lines.append('  命令链：%s' % ' → '.join(chain))
        else:
            lines.append('  ⚠ 未抽出命令链（方案步骤将自行读取文档）')
        kp = ex.get('key_params') or {}
        if kp:
            lines.append('  关键参数：%s' % _fmt_kv(kp, 3))

    # 排除的文档（只列前 3，说明原因）
    excl = []
    for r in retrieval:
        for c in r.get('candidates', []):
            if not c.get('adopted') and c.get('reason'):
                excl.append('%s（%s）' % (c.get('doc', '?'), c['reason']))
    if excl:
        lines.append('· 排除：%s' % '；'.join(excl[:3]))

    # EXP 形态证据（这是方案步骤最需要的）
    ev = out.get('exp_evidence') or {}
    if ev:
        lines.append('EXP 现网形态证据：')
        for fam, info in list(ev.items())[:8]:
            if isinstance(info, dict):
                cnt = info.get('count', 0)
                naming = info.get('naming', '')
                lines.append('  %s 现网 %s 条%s' % (
                    fam, cnt, '，命名规律 %s' % naming if naming else ''))
            else:
                lines.append('  %s 现网 %s 条' % (fam, info))
        if len(ev) > 8:
            lines.append('  …另有 %d 个族' % (len(ev) - 8))
    return '\n'.join(lines)


def summary_03(out: dict) -> str:
    """方案 → 给组装看。"""
    lines = []
    phases = out.get('phases') or []
    fams = out.get('family_set') or []

    lines.append('方案 %d 个阶段，%d 个命令族：' % (len(phases), len(fams)))
    for p in phases:
        pf = p.get('families') or []
        lines.append('  %d. %s：%s' % (
            p.get('seq', '?'), p.get('name', '?'),
            ' → '.join(pf) if pf else '（未列族）'))
        if p.get('rationale'):
            lines.append('     依据：%s' % p['rationale'][:60])

    rej = out.get('rejected') or []
    if rej:
        lines.append('排除：%s' % '；'.join(
            '%s（%s）' % (r.get('family', '?'), r.get('reason', '')[:30])
            for r in rej[:3]))

    if out.get('need_retrieval'):
        lines.append('⚠ 方案声明需要补检索：%s' % out.get('need_retrieval_reason', ''))
    return '\n'.join(lines)


def summary_04(out: dict) -> str:
    """组装 → 给补充看。"""
    cmds = out.get('commands') or []
    from collections import Counter
    cnt = Counter(c.get('family', '?') for c in cmds)

    lines = ['已组装 %d 条命令，%d 个族：' % (len(cmds), len(cnt))]
    lines.append('  ' + '，'.join('%s×%d' % (k, v) for k, v in cnt.most_common(10)))
    if len(cnt) > 10:
        lines.append('  …另有 %d 族' % (len(cnt) - 10))

    # 待填参数（补充步骤不关心，但参数核查关心，这里给个预告）
    n_ph = sum(1 for c in cmds
               for p in (c.get('params') or {}).values()
               if isinstance(p, dict) and p.get('source') == 'placeholder')
    n_unknown = sum(1 for c in cmds
                    for p in (c.get('params') or {}).values()
                    if isinstance(p, dict) and p.get('source') == 'unknown')
    lines.append('待填参数 %d 个' % n_ph)
    if n_unknown:
        lines.append('⚠ 参数来源不明 %d 个（留待参数核查处理）' % n_unknown)
    return '\n'.join(lines)


def summary_05(out: dict) -> str:
    """补充 → 给参数核查看。"""
    before = out.get('before') or {}
    after = out.get('after') or {}
    lines = []

    lines.append('补充前 %s 条 / %s 族 → 补充后 %s 条 / %s 族' % (
        before.get('n_cmds', '?'), before.get('n_families', '?'),
        after.get('n_cmds', '?'), after.get('n_families', '?')))

    sup = out.get('supplemented') or []
    if sup:
        lines.append('补建 %d 族：' % len(sup))
        for s in sup[:5]:
            lines.append('  + %s（%s）' % (s.get('family', '?'),
                                           s.get('reason', '')[:40]))

    blocked = out.get('gate_blocked') or []
    if blocked:
        lines.append('拦截 %d 族：%s' % (
            len(blocked),
            '；'.join('%s（%s）' % (b.get('family', '?'), b.get('reason', '')[:30])
                     for b in blocked[:3])))

    exp_ex = out.get('exp_existing') or []
    if exp_ex:
        lines.append('EXP 已有 %d 族（建议注释而非重复下发）：%s' % (
            len(exp_ex),
            '，'.join('%s×%s' % (e.get('family', '?'), e.get('count_in_exp', '?'))
                     for e in exp_ex[:4])))

    if out.get('dangling_remaining'):
        lines.append('⚠ 仍有 %d 处引用未闭合' % out['dangling_remaining'])
    return '\n'.join(lines)


def summary_06a(out: dict) -> str:
    """参数核查 → 给回填看。"""
    return ('%s 个参数：%s 个已自动确定，%s 个需人工填。\nCSV：%s' % (
        out.get('params_total', '?'),
        out.get('auto_determined', '?'),
        out.get('need_manual', '?'),
        out.get('params_needed_csv', '?')))


SUMMARY_FN = {
    '01_intent': summary_01,
    '02_retrieval': summary_02,
    '03_plan': summary_03,
    '04_assemble': summary_04,
    '05_supplement': summary_05,
    '06a_param_check': summary_06a,
    '06b_param_fill': lambda out: '参数回填完成：%s 个参数已填。' % out.get('n_filled', '?'),
    '07_render': lambda out: '产物已生成：%s' % out.get('mml_txt', '?'),
}


def make_summary(step_name: str, output: dict) -> str:
    fn = SUMMARY_FN.get(step_name)
    if not fn:
        return '（无摘要模板）'
    try:
        return fn(output)
    except Exception as e:
        return '（摘要生成失败：%s）' % e
