#!/usr/bin/env python3
"""explain.py — 把 guard 的检查结果翻译成人和 agent 都看得懂的话。

★ 2026-11-06 用户要求：
  「现在直接一个守门 Fail 没人知道啥意思」
  → 每个 fatal 要说清楚：是什么问题、为什么错、怎么改、影响什么

设计：
  · explain_fatal(item) → {title, detail, how_to_fix, severity, family}
  · explain_guard(guard_result) → {summary, items[], can_auto_fix}
"""
import re


def _t(s):
    return str(s or '')


def explain_fatal(item):
    """把单条 fatal 转成结构化说明。"""
    raw = item if isinstance(item, str) else _t(
        item.get('message') or item.get('msg') or item)
    code = ''
    if isinstance(item, dict):
        code = _t(item.get('code'))

    # ── G21 csv↔mml 一致性 ──
    if raw.startswith('G21') or 'csv 生成' in raw:
        m = re.search(r'（(\d+) 条）', raw)
        n = m.group(1) if m else '?'
        return {
            'code': 'G21',
            'severity': 'fatal',
            'title': f'参数表和配置命令对不上（{n} 条）',
            'detail': ('params.csv 里列出的参数，在 mml.txt 里没有全部体现。'
                       '这说明两者有一处写错了：要么 csv 少写了、要么 mml 抄错了。'),
            'why_bad': ('csv 是唯一数据源，用户改完 csv 重新生成 mml 时结果会变，'
                        '现在两者不一致就说明其中一份是错的。'),
            'how_to_fix': ('以 params.csv 为准，逐条核对 mml.txt 对应命令的参数。'
                           '特别注意：值里出现 *** 的，说明是从 EXP 的脱敏字段照抄的，'
                           '要改成同族其他实例的多数值（如 TOKENFUNCFLAG 现网 101 条全是 DISABLE）。'),
            'family': 'G21',
        }

    # ── G19 来源标注 ──
    if raw.startswith('G19'):
        m = re.search(r'第 (\d+) 行', raw)
        line = m.group(1) if m else '?'

        # 脱敏残留（优先判断，因为它也带 G19 前缀）
        if '脱敏残留' in raw:
            pm = re.search(r'([A-Z][A-Z0-9_]+)\.([A-Z][A-Z0-9_]+)=\*+', raw)
            param = f'{pm.group(1)}.{pm.group(2)}' if pm else '某个参数'
            return {
                'code': 'G19-SANITIZE', 'severity': 'fatal',
                'title': f'第 {line} 行照抄了 EXP 里的脱敏值 ***',
                'detail': (f'{param} 的值是 ***，这是现网快照里的脱敏占位符，不是真实配置值。'),
                'why_bad': ('直接把 *** 下发到网元会导致命令语法错误或参数非法，'
                            '整条配置执行失败。'),
                'how_to_fix': ('不要照抄 ***。正确做法：用 exp_query 查同族其他实例，'
                               '取出现最多的一致值；或查特性文档取默认值。'
                               '例如 TOKENFUNCFLAG 现网 101 条全是 DISABLE，就按 DISABLE 写。'),
                'family': 'G19',
            }
        if '编造值' in raw:
            return {
                'code': 'G19', 'severity': 'fatal',
                'title': f'第 {line} 行的值没有依据',
                'detail': '这个参数填了具体值，但没写 @src 说明依据是什么。',
                'why_bad': '看不出这个值是查现网来的、文档来的，还是模型编的。',
                'how_to_fix': '要么补上 // @src=exp:L行号 或 @src=doc:章节，要么改成【待填写】。',
                'family': 'G19',
            }
        if '虚假依据' in raw:
            return {
                'code': 'G19', 'severity': 'fatal',
                'title': f'第 {line} 行标的依据是假的',
                'detail': '写了 @src=exp:L行号，但那一行不是同族命令、或行号越界。',
                'why_bad': '声称"参照现网"，实际现网里没有，等于编造。',
                'how_to_fix': '用 exp_query 重新确认行号；或者改成 @src=infer 并说明推导规则。',
                'family': 'G19',
            }
        return {'code': 'G19', 'severity': 'fatal', 'title': '来源标注有问题',
                'detail': raw, 'why_bad': '', 'how_to_fix': '检查 @src 写法', 'family': 'G19'}

    # ── C2 引用悬空 ──
    if raw.startswith('C2'):
        return {
            'code': 'C2', 'severity': 'fatal',
            'title': '引用了不存在的对象',
            'detail': '某个命令引用的对象（HOST/FILTER/URR 等）在产物和现网里都找不到定义。',
            'why_bad': 'MML 执行时会报"对象不存在"，整条命令失败。',
            'how_to_fix': '要么在前面补上该对象的 ADD 命令，要么改成现网已有的对象名。',
            'family': 'C2',
        }

    # ── G11 主键重复 ──
    if raw.startswith('G11'):
        return {
            'code': 'G11', 'severity': 'fatal',
            'title': '同一个对象定义了两次',
            'detail': '同一网元内，某个对象的主键（如 HOSTNAME）出现了两条 ADD。',
            'why_bad': '第二条会被网元拒绝，或者覆盖第一条。',
            'how_to_fix': '合并成一条，或删掉重复的那条。',
            'family': 'G11',
        }

    # ── G18 族缺失 ──
    if raw.startswith('G18'):
        return {
            'code': 'G18', 'severity': 'fatal',
            'title': '意图要求配置的命令族缺失',
            'detail': raw,
            'why_bad': '用户明确提到的功能没配上，配置不完整。',
            'how_to_fix': '补上缺失的命令族；如果是删除意图，则确认真的删掉了。',
            'family': 'G18',
        }

    # ── G22 占位符 ──
    if raw.startswith('G22'):
        return {
            'code': 'G22', 'severity': 'fatal',
            'title': '占位符列和值不一致',
            'detail': raw,
            'why_bad': '改一处无法自动关联，用户会漏改。',
            'how_to_fix': '「占位符」列填的名字要和「值」列里的【XXX】一致。',
            'family': 'G22',
        }

    # ── 缺产物 ──
    if 'MISSING_ARTIFACT' in code or '缺少产物' in raw:
        return {
            'code': 'MISSING_ARTIFACT', 'severity': 'fatal',
            'title': '产物没写全',
            'detail': raw,
            'why_bad': '缺文件无法交付。',
            'how_to_fix': '用 artifact_write 补写缺失的文件（大文件分块写）。',
            'family': 'ARTIFACT',
        }

    # 兜底
    return {
        'code': code or 'UNKNOWN', 'severity': 'fatal',
        'title': raw[:60], 'detail': raw,
        'why_bad': '', 'how_to_fix': '按提示修正',
        'family': code or 'UNKNOWN',
    }


def explain_guard(guard_result):
    """整体解释一次 guard 结果。"""
    fatal = guard_result.get('fatal') or []
    warnings = guard_result.get('warnings') or []
    verdict = guard_result.get('verdict') or 'unknown'

    items = [explain_fatal(f) for f in fatal[:12]]

    if verdict == 'pass':
        summary = '自检通过，配置可以直接下发。'
    elif verdict == 'warn':
        summary = f'配置已生成，有 {len(warnings)} 条提示，不影响下发。'
    elif not fatal:
        summary = '配置已生成，但自检未完成。'
    else:
        # 按类型归类
        fams = {}
        for it in items:
            fams.setdefault(it['family'], 0)
            fams[it['family']] += 1
        parts = []
        for fam, n in sorted(fams.items(), key=lambda x: -x[1]):
            title = next((i['title'] for i in items if i['family'] == fam), fam)
            parts.append(f'{title}' + (f'（{n} 处）' if n > 1 else ''))
        summary = f'配置已生成，但有 {len(fatal)} 个问题需要修复：' + '；'.join(parts[:3])

    return {
        'verdict': verdict,
        'summary': summary,
        'n_fatal': len(fatal),
        'n_warn': len(warnings),
        'items': items,
        # 有产物 = 不是空手而归，只是需要修
        'has_artifacts': guard_result.get('has_artifacts', True),
        'can_auto_fix': all(it['family'] in ('G19', 'G21', 'G22', 'C2', 'G11')
                            for it in items) if items else True,
    }


def to_agent_instruction(guard_result):
    """给 agent 的修正指令（比原来的更具体）。"""
    ex = explain_guard(guard_result)
    lines = ['【上一轮产物未通过自检，需要你修正】', '']
    lines.append(f'结论：{ex["summary"]}')
    lines.append('')
    lines.append('具体问题：')
    for i, it in enumerate(ex['items'], 1):
        lines.append(f'{i}. 【{it["code"]}】{it["title"]}')
        if it['detail']:
            lines.append(f'   现象：{it["detail"]}')
        if it.get('why_bad'):
            lines.append(f'   为什么不对：{it["why_bad"]}')
        if it.get('how_to_fix'):
            lines.append(f'   怎么改：{it["how_to_fix"]}')
        lines.append('')
    lines.append('【修改原则】')
    lines.append('  · 保留上一轮所有正确的命令，只改有问题的地方')
    lines.append('  · 不要为了消除告警就删掉整族命令')
    lines.append('  · 改完用 artifact_write 覆盖写对应文件（大文件分块写）')
    lines.append('  · 改完再调 guard_check 确认')
    return '\n'.join(lines)


if __name__ == '__main__':
    import json
    import sys
    data = json.loads(sys.stdin.read()) if not sys.argv[1:] else json.load(open(sys.argv[1]))
    print(json.dumps(explain_guard(data), ensure_ascii=False, indent=1))
