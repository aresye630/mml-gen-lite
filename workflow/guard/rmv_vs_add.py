"""G30：意图要删除的对象，产物里用了 ADD 或漏删。

用户要求（2026-11-10）：「实现G30」

背景实测（长期高频问题）：
  prompt 明确写了「删除对象用 RMV，不要用 ADD」，
  但实测 10 单里 8 单把 RMV 配成了 ADD。
  （记录在 MEMORY：★prompt不可靠:10单8单把RMV配成ADD）

为什么可以用规则做（不需要 LLM）：
  意图已经由 intent_ops.py 解析成结构化「操作清单」
  （动词 + 目标对象），所以可以做确定性比对。

判据逻辑：
  1. 从意图解析出「要删除的对象」（动词=RMV 的条目）
  2. 从产物 mml 提取每个族的 ADD/RMV 对象名
  3. 检查：
     A. 意图要删的对象，产物里却 ADD 了同名对象 → warn（方向反了）
     B. 意图要删的族，产物里一条 RMV 都没有 → warn（漏删）
  4. 输入缺意图/产物 → skipped
"""
import re
from pathlib import Path

# 意图里表示「删除」的词
RMV_WORDS = ('删除', '移除', '去除', '清除', '去掉')

# 对象名 → 可能的族（用于反查，只做提示）
# 这是纯业务名到族的映射，不含命令模板
BIZ_TO_FAM_HINT = {
    '过滤器': 'FILTER',
    '流过滤器': 'FLOWFILTER',
    '七层过滤器': 'L7FILTER',
    '域名': 'HOST',
    'Host': 'HOST',
    '规则': 'RULE',
    '用户模板': 'USERPROFILE',
    '模板': 'USERPROFILE',
    '计费规则': 'URR',
    'URR': 'URR',
    'PCC策略组': 'PCCPOLICYGRP',
    '策略组': 'PCCPOLICYGRP',
    '地址池': 'POOL',
    '池': 'POOL',
    '隧道': 'GRE TUNNEL',
    '路由': 'SRROUTE',
    '接口': 'INTERFACE',
    'NTP': 'NTPSVR',
    '服务器': 'NTPSVR',
}


def parse_intent_rmv(intent_text):
    """从意图里解析「要删除的对象」。

    Returns [{biz, fam_hint}]
    """
    out = []
    if not intent_text:
        return out

    # 找「删除 xxx」形式的行
    for line in intent_text.split('\n'):
        s = line.strip().lstrip('-*·').strip()
        if not s:
            continue
        # 判断是不是删除类
        is_rmv = any(w in s for w in RMV_WORDS)
        if not is_rmv:
            continue

        # 提取对象名：去掉「删除」动词和数量描述
        obj = s
        for w in RMV_WORDS:
            obj = obj.replace(w, '', 1)
        obj = re.sub(r'约?\s*\d+\s*个?', '', obj)
        obj = re.sub(r'[，,（(].*$', '', obj)
        obj = obj.strip().strip('，,。:：')
        if not obj or len(obj) < 2:
            continue

        # 匹配可能的族
        hint = None
        for k, v in BIZ_TO_FAM_HINT.items():
            if k in obj:
                hint = v
                break

        out.append({'biz': obj[:40], 'fam_hint': hint})
    return out


def parse_prod_keys(mml_text):
    """产物里每个族的 ADD / RMV 对象名集合。

    Returns {family: {'ADD': set(), 'RMV': set()}}
    """
    out = {}
    for line in mml_text.split('\n'):
        s = line.split('//')[0].strip()
        if not s or s.startswith(('/*', '#', '*')):
            continue
        m = re.match(r'^(ADD|RMV|MOD|SET)\s+([A-Za-z0-9_]+)\s*[:：]\s*(.*)$',
                     s.rstrip(';'), re.I | re.S)
        if not m:
            continue
        verb = m.group(1).upper()
        fam = m.group(2).upper()
        rest = m.group(3)
        # 取第一个参数值作对象名
        pm = re.search(r'=\s*"([^"]*)"', rest)
        if not pm:
            pm = re.search(r'=\s*([^,;\s]+)', rest)
        key = pm.group(1) if pm else None
        d = out.setdefault(fam, {'ADD': set(), 'RMV': set()})
        if key:
            d[verb].add(key)
    return out


def check_rmv_vs_add(sess_dir=None, intent_text='', mml_text=''):
    """G30：意图要删的对象，产物里用了 ADD 或漏删。

    Returns {
      ok: bool,
      skipped: bool,
      n_intent_rmv: int,      # 意图里删除类条目数
      reversed: [{biz, family, keys}],   # 方向反了（要删却 ADD）
      missed: [{biz, family}],           # 漏删（一条 RMV 都没有）
    }
    """
    if sess_dir:
        base = Path(sess_dir) / 'analysis_code'
        if not intent_text:
            for cand in (base / '.intent.md', base / '意图.md'):
                if cand.exists():
                    intent_text = cand.read_text(encoding='utf-8', errors='replace')
                    break
        if not mml_text:
            p = base / 'mml.txt'
            if p.exists():
                mml_text = p.read_text(encoding='utf-8', errors='replace')

    if not intent_text or not mml_text:
        return {'ok': True, 'skipped': True, 'reason': '缺意图或 mml',
                'n_intent_rmv': 0, 'reversed': [], 'missed': []}

    rmv_items = parse_intent_rmv(intent_text)
    if not rmv_items:
        return {'ok': True, 'skipped': True, 'reason': '意图里没有删除类条目',
                'n_intent_rmv': 0, 'reversed': [], 'missed': []}

    prod = parse_prod_keys(mml_text)

    reversed_list = []
    missed_list = []

    for it in rmv_items:
        hint = it['fam_hint']
        if not hint:
            continue
        fam = hint.replace(' ', '_')

        d = prod.get(fam)
        if d is None:
            # 产物里完全没有这个族 → 漏删
            missed_list.append({'biz': it['biz'], 'family': fam, 'why': '产物无此族'})
            continue

        if not d['RMV'] and d['ADD']:
            # 有 ADD 无 RMV → 方向反了
            reversed_list.append({
                'biz': it['biz'], 'family': fam,
                'keys': sorted(d['ADD'])[:5],
                'n': len(d['ADD']),
            })
        elif not d['RMV'] and not d['ADD']:
            missed_list.append({'biz': it['biz'], 'family': fam, 'why': '族存在但无命令'})

    return {
        'ok': not reversed_list and not missed_list,
        'skipped': False,
        'n_intent_rmv': len([x for x in rmv_items if x['fam_hint']]),
        'reversed': reversed_list[:8],
        'missed': missed_list[:8],
    }


if __name__ == '__main__':
    import json
    import sys
    sd = sys.argv[1] if len(sys.argv) > 1 else '.'
    print(json.dumps(check_rmv_vs_add(sess_dir=sd), ensure_ascii=False, indent=1))
