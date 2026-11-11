#!/usr/bin/env python3
"""V4：极致压缩版 —— 按业务链路的一句话流式描述，像人写的备忘录。

用户裁定（2026-11-11）：
  「按业务链路一句话流式描述（不分段、不分行，像人写的备忘录）」

四种意图版本并存：
  V1 原始工单意图（客户写的）      /Users/alesc/workspace/gt-rewrite-samples/86个意图_v5
  V2 GT 反推（逐条列）             /tmp/intent_dataset
  V3 参照 EXP 改写                 /tmp/intent_v3
  V4 极致压缩（本文档）             /tmp/intent_v4

V4 生成规则：
  1. 以 V3 为基础（V3 已有「参照存量」的总述和结构类条目）
  2. 丢掉分组标题，所有条目按「锚点对象」聚成一两条流水句
  3. 同锚点的操作连成一串：「新建 sos 的 APN，属性照 ims 配齐，
     另建 DNN信息、IMS分类器、切片DNN、P-CSCF组关联」
  4. 「（见数据清单）」只提一次，不逐条重复
"""
import argparse
import json
import re
from collections import Counter, OrderedDict, defaultdict
from pathlib import Path

GT = json.loads(Path('/tmp/gt_cleaned.json').read_text(encoding='utf-8'))
GT_MAP = {g['ticket']: g for g in GT}

V2 = Path('/tmp/intent_dataset')
V3 = Path('/tmp/intent_v3')
OUT = Path('/tmp/intent_v4')

# 锚点参数 → 中文
ANCHOR_CN = {
    'APN': 'APN', 'USERPROFILENAME': '用户模板', 'VPNINSTANCE': 'VPN 实例',
    'POOLNAME': '地址池', 'POOLGROUPNAME': '地址池组', 'VRFNAME': 'VPN',
    'FILTERNAME': '过滤器', 'HOSTNAME': '域名对象',
}

# 业务链路分组（按族名前缀 → 链路）
CHAIN_RULES = [
    ('计费链', ('URR', 'PCC', 'RULE', 'USERPROFILE', 'UPBIND', 'CTXSTART', 'APNUSRPROFG')),
    ('流量识别', ('FILTER', 'FLOWFILTER', 'L7FILTER', 'PROTBIND', 'HOST',
                  'APNSGLPASS', 'APNIMSSIGFLTR', 'APNDEACTQFPLCY')),
    ('地址资源', ('POOL', 'SECTION', 'TAC', 'TAI', 'UPAREA', 'LOC', 'DNAI',
                  'IPALLOC', 'PNFDNN', 'PNFNS', 'PNFTAIRANGE', 'BSFIPRANGE')),
    ('承载路由', ('GRETUNNEL', 'INTERFACE', 'IFIPV4', 'IFIPV6', 'IPBINDVPN',
                  'SRROUTE', 'VPNINST', 'L3VPN', 'BGP', 'OSPF', 'CPASSOCIATION')),
    ('紧急呼叫', ('EMGCFG', 'NGEMGCFG', 'SRVCC', 'NILR')),
    ('许可与软参', ('LICENSE', 'SOFTPARA', 'DBPARAS', 'ALM', 'REFRESH')),
]


def chain_of(fam):
    for name, prefixes in CHAIN_RULES:
        for p in prefixes:
            if fam.startswith(p):
                return name
    return '其他'


def read(p):
    return p.read_text(encoding='utf-8', errors='replace') if p.exists() else ''


def parse_v3(text):
    """解析 V3 意图为 [{group, action, obj, cons, is_summary, is_extra}]"""
    items = []
    cur_group = None
    lines = text.split('\n')
    i = 0
    while i < len(lines):
        s = lines[i].strip()
        if s.startswith('【') and s.endswith('】'):
            cur_group = s[1:-1]
            i += 1
            continue
        if s.startswith('- '):
            body = s[2:].strip()
            cons = []
            j = i + 1
            while j < len(lines) and lines[j].strip().startswith('（'):
                cons.append(lines[j].strip().strip('（）()'))
                j += 1
            is_summary = '存量做法配齐' in body
            is_extra = body.startswith('存量「')
            m = re.match(r'^(新增|调整|删除|设置)\s+(.+?)(（见数据清单）)?$', body)
            if m:
                items.append({
                    'group': cur_group, 'action': m.group(1),
                    'obj': m.group(2).strip(), 'cons': cons,
                    'is_summary': is_summary, 'is_extra': is_extra,
                    'raw': body,
                })
            elif is_summary or is_extra:
                items.append({
                    'group': cur_group, 'action': '', 'obj': body,
                    'cons': [], 'is_summary': is_summary,
                    'is_extra': is_extra, 'raw': body,
                })
            i = j
            continue
        i += 1
    return items


def anchor_in(item, anchors):
    """条目是否属于某个锚点。"""
    txt = ' '.join(item['cons']) + ' ' + item['obj']
    for a in anchors:
        if re.search(rf'(?<![A-Za-z0-9_.\-]){re.escape(a)}(?![A-Za-z0-9_.\-])', txt):
            return a
    return None


def build_v4(tk):
    v3 = read(V3 / f'{tk}_意图.md')
    if not v3:
        return None
    g = GT_MAP.get(tk)
    if not g or not g['kept']:
        return None

    items = parse_v3(v3)
    if not items:
        return None

    # 收集所有锚点（从 cons 里「名称为 X」提取 + GT 参数）
    anchors = set()
    for it in items:
        for c in it['cons']:
            m = re.search(r'名称为\s*([A-Za-z0-9_.\-]+)', c)
            if m:
                anchors.add(m.group(1))

    # 参照总述单独提出来
    refs = [it for it in items if it['is_summary']]
    extras = [it for it in items if it['is_extra']]
    normal = [it for it in items if not it['is_summary'] and not it['is_extra']]

    # 把 normal 按「归属锚点」分组，无锚点的按业务链分组
    by_anchor = defaultdict(list)
    by_chain = defaultdict(list)
    for it in normal:
        a = anchor_in(it, anchors)
        if a:
            by_anchor[a].append(it)
        else:
            # 用族名反推链路，再归类
            chain = '其他'
            for _, v, fam, _, _ in g['kept']:
                if any(kw in it['obj'] for kw in ('地址池', 'DNN', '隧道', '规则',
                                                   '过滤器', 'URR', '接口', '紧急',
                                                   '切片', '路由', 'VPN')):
                    pass
            by_chain[chain].append(it)

    # ── 生成流水句 ──
    sentences = []

    # 1. 锚点相关的：一个锚点一句话
    for a, its in sorted(by_anchor.items(), key=lambda x: -len(x[1])):
        # 找该锚点的参照总述
        # 精确匹配：「APN「sos」的配置」这种，锚点名要完整出现且前面对应的对象类型一致
        ref = None
        for r in refs:
            m0 = re.search(r'「([^」]+)」', r['obj'])
            if m0 and m0.group(1) == a:
                ref = r
                break
        parts = []
        if ref:
            m = re.search(r'按现网同类(.+?)「(.+?)」的存量做法配齐', ref['obj'])
            if m:
                parts.append(f'属性按现网同类{m.group(1)}「{m.group(2)}」配齐')

        # 该锚点的结构性操作，按动作归并
        acts = OrderedDict()
        for it in its:
            acts.setdefault(it['action'], []).append(it)
        for act, its2 in acts.items():
            seen = []
            for it2 in its2:
                if it2['obj'] not in seen:
                    seen.append(it2['obj'])
            # ★ 2026-11-11：关键约束不能丢
            #   实测 V4 首版把「数据面探测开关为开启,逻辑接口类型为N3-1&...」
            #   「地址释放时长为60,池类型为本地池」这类固定值约束全丢了，
            #   导致 NC20260904002179/NC20260914002657 从 100% 掉到 0%。
            _cons = []
            for it2 in its2:
                for c in it2['cons']:
                    if c not in _cons and '见数据清单' not in c:
                        _cons.append(c)
            _tail = f'（{("；".join(_cons))}）' if _cons else ''
            parts.append(f'{act} ' + '、'.join(seen) + _tail)

        if parts:
            # 单条超过 60 字就拆成两句，读起来更顺
            _joined = '；'.join(parts)
            if len(_joined) > 60:
                sentences.append(f'「{a}」：{parts[0]}。')
                if len(parts) > 1:
                    sentences.append('另外' + '；'.join(parts[1:]) + '。')
            else:
                sentences.append(f'「{a}」：' + _joined + '。')

    # 2. 无锚点的：每个动作一句（避免一长串）
    for chain, its in by_chain.items():
        acts = OrderedDict()
        for it in its:
            acts.setdefault(it['action'], []).append(it)
        for act, its2 in acts.items():
            seen = []
            _cons = []
            for it2 in its2:
                if it2['obj'] not in seen:
                    seen.append(it2['obj'])
                for c in it2['cons']:
                    if c not in _cons and '见数据清单' not in c:
                        _cons.append(c)
            if seen:
                _tail = f'（{("；".join(_cons))}）' if _cons else ''
                sentences.append(f'{act} ' + '、'.join(seen) + _tail + '。')

    # ── 组装成备忘录 ──
    body = ''.join(sentences)
    # 清理重复标点（。。、；。、，。 等）
    body = re.sub(r'[，。；]{2,}', '。', body)
    body = body.rstrip('，。；') + '。'

    text = f"""# {tk} — 意图

{body}

（各项的具体对象与取值见数据清单。）
"""
    return {'tk': tk, 'text': text, 'n_items': len(items), 'n_sent': len(sentences)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--ticket', default='')
    args = ap.parse_args()

    OUT.mkdir(exist_ok=True)
    n_total = n_ok = 0
    for g in GT:
        tk = g['ticket']
        if args.ticket and tk != args.ticket:
            continue
        if not (V3 / f'{tk}_意图.md').exists():
            continue
        r = build_v4(tk)
        if not r:
            continue
        (OUT / f'{tk}_意图.md').write_text(r['text'], encoding='utf-8')
        src_ds = V3 / f'{tk}_数据清单.md'
        if not src_ds.exists():
            src_ds = V2 / f'{tk}_数据清单.md'
        if src_ds.exists():
            (OUT / f'{tk}_数据清单.md').write_text(
                src_ds.read_text(encoding='utf-8'), encoding='utf-8')
        n_total += 1
        n_ok += 1

    print(f'✅ 生成 {n_ok}/{n_total} 个工单 → {OUT}')


if __name__ == '__main__':
    main()
