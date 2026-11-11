#!/usr/bin/env python3
"""V5：V3 的准确率 + V4 的简洁度。

设计依据（2026-11-11 实测 20 单 × 3 版）：
  V3 参照存量：阶段2 达标 90%，448 字   ← 参照是关键，不能丢
  V4 极致压缩：阶段2 达标 75%，202 字   ← 压缩丢掉了参照
  V2 逐条列  ：阶段2 达标 70%，465 字

V5 的做法：
  1. 保留 V3 的「参照存量」总述条目不压缩（这是准确率来源）
  2. 结构类条目（新增/删除/调整）按动作合并成流水句
  3. 保留固定值/规律约束（V4 首版坑：丢了约束，3 单从 100% 掉到 0%）
  4. 去掉分组标题，但条目顺序按「参照 → 结构变更」排

目标：字数接近 V4（200 左右），达标率接近或超过 V3（90%）。
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
OUT = Path('/tmp/intent_v5')


def read(p):
    return p.read_text(encoding='utf-8', errors='replace') if p.exists() else ''


def parse_v3(text):
    """解析 V3 → {refs: [参照总述], items: [{action, obj, cons}]}"""
    refs, items = [], []
    lines = text.split('\n')
    i = 0
    while i < len(lines):
        s = lines[i].strip()
        if not s.startswith('- '):
            i += 1
            continue
        body = s[2:].strip()
        cons = []
        j = i + 1
        while j < len(lines) and lines[j].strip().startswith('（'):
            cons.append(lines[j].strip().strip('（）()'))
            j += 1

        # 参照总述：「APN「sos」的配置：按现网同类APN「ims」的存量做法配齐」
        if '存量做法配齐' in body:
            refs.append({'raw': body, 'cons': cons})
            i = j
            continue
        # 存量补列：「存量「ims」没有、需单独配置的：XXX」
        if body.startswith('存量「'):
            refs.append({'raw': body, 'cons': [], 'extra': True})
            i = j
            continue

        m = re.match(r'^(新增|调整|删除|设置)\s+(.+?)(（见数据清单）)?$', body)
        if m:
            obj = m.group(2).strip()
            # 去掉「见数据清单」这种无信息标注（V5 统一在开头说一次）
            items.append({
                'action': m.group(1), 'obj': obj,
                'cons': [c for c in cons if '见数据清单' not in c],
            })
        i = j
    return refs, items


def build_v5(tk):
    v3 = read(V3 / f'{tk}_意图.md')
    if not v3:
        return None
    g = GT_MAP.get(tk)
    if not g or not g['kept']:
        return None

    refs, items = parse_v3(v3)
    if not items and not refs:
        return None

    # ── 1. 参照总述：原样保留（准确率来源）──
    ref_lines = []
    for r in refs:
        if r.get('extra'):
            ref_lines.append(r['raw'])
        else:
            ref_lines.append(r['raw'].rstrip('。'))

    # ── 2. 结构条目：按动作归并成流水句 ──
    acts = OrderedDict()
    for it in items:
        acts.setdefault(it['action'], []).append(it)

    body_parts = []
    for act, its in acts.items():
        # ★ 2026-11-11：约束必须跟对象配对，不能全部堆到一个括号里。
        #   首版实测：25 个对象共用一长串约束，agent 分不清哪个约束属于哪个对象。
        #   做法：按「约束签名」把对象分组，同约束的对象写在一起。
        groups = OrderedDict()      # {约束元组: [对象名]}
        for it in its:
            key = tuple(it['cons'])
            groups.setdefault(key, [])
            if it['obj'] not in groups[key]:
                groups[key].append(it['obj'])

        segs = []
        for cons, objs in groups.items():
            seg = '、'.join(objs)
            if cons:
                seg += f'（{"；".join(cons)}）'
            segs.append(seg)
        body_parts.append(f'{act} ' + '；'.join(segs))

    # ── 3. 组装 ──
    blocks = []
    if ref_lines:
        blocks.append('\n'.join(ref_lines))
    if body_parts:
        blocks.append('；'.join(body_parts))

    body = '。\n'.join(b for b in blocks if b)
    body = re.sub(r'。{2,}', '。', body).rstrip('。') + '。'

    text = f"""# {tk} — 意图

{body}

（各项的具体对象与取值见数据清单。）
"""
    return {
        'tk': tk, 'text': text,
        'n_refs': len(refs), 'n_items': len(items),
        'n_acts': len(acts),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--ticket', default='')
    args = ap.parse_args()

    OUT.mkdir(exist_ok=True)
    n = 0
    for g in GT:
        tk = g['ticket']
        if args.ticket and tk != args.ticket:
            continue
        if not (V3 / f'{tk}_意图.md').exists():
            continue
        r = build_v5(tk)
        if not r:
            continue
        (OUT / f'{tk}_意图.md').write_text(r['text'], encoding='utf-8')
        # 数据清单沿用 V3
        for src_dir in (V3, V2):
            ds = src_dir / f'{tk}_数据清单.md'
            if ds.exists():
                (OUT / f'{tk}_数据清单.md').write_text(
                    ds.read_text(encoding='utf-8'), encoding='utf-8')
                break
        n += 1

    print(f'✅ 生成 {n} 个工单 → {OUT}')


if __name__ == '__main__':
    main()
