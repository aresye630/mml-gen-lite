"""G27：跨网元无法配置项的提示检测。

用户要求（2026-11-10）：
  「对于未修改的：2、agent 能不能提示出来」
  即：意图里点名要做、但对应命令族在本网元 EXP 里不存在时，
      agent 必须主动说明，而不是默默跳过。

背景实测：
  87 工单里 26 个跨 UDG+UNC，但只提供了 UDG 侧 EXP。
  UNC 侧的族（EMGCFG / USRPROFGROUP / DBPARAS / PNFDNN 等）在本网元查不到，
  agent 配不出来，用户也不知道为什么少了这些族。

判据：
  1. 从意图里提取「点名的业务项」（【】段落里的条目）
  2. 从规划表提取「标为跳过/无命令族」的行
  3. 如果规划里有跳过的项，但 配置分析.md 里没有「本网元无法配置」的说明 → warn
  4. 不判 fatal（说明性内容，不影响配置可用性）
"""
import re
from pathlib import Path

# 配置分析里表示「配不了」的表述
UNABLE_MARKERS = [
    '本网元无法配置',
    '本网元不存在',
    '本网元配不了',
    '不在本网元',
    '非本网元',
    '属 BSF 网元',
    '属 UNC 网元',
    '属 SMF 网元',
    '需在',
    '无法在本网元',
    '本 EXP 中不存在',
    '族不存在',
    '查 0 条',
]


def parse_plan_skipped(plan_text):
    """从规划表提取标为「跳过」或「无命令族」的项。"""
    out = []
    for line in plan_text.split('\n'):
        line = line.strip()
        if not line.startswith('|'):
            continue
        cells = [c.strip() for c in line.split('|')]
        if len(cells) < 10:
            continue
        body = cells[1:-1]
        if len(body) < 9:
            continue
        # 跳过表头/分隔行
        if body[0] in ('#', '---') or not body[0].isdigit():
            continue

        biz = body[2]        # 业务对象
        fam = body[5]        # 命令族
        status = body[8]     # 状态

        is_skipped = ('跳过' in status) or ('无' in fam and len(fam) < 30)
        if is_skipped:
            out.append({
                'biz': biz[:60],
                'family': fam[:40],
                'status': status[:30],
            })
    return out


def check_unable_notice(sess_dir):
    """检查「配不了的项」是否在配置分析里说明了。

    Returns:
      {
        'ok': bool,
        'skipped': bool,
        'n_plan_skipped': int,      # 规划里标跳过的项数
        'n_explained': int,         # 配置分析里解释了几项
        'unexplained': [...],       # 没解释的项
      }
    """
    adir = Path(sess_dir) / 'analysis_code'
    plan_p = adir / '命令族规划.md'
    ca_p = adir / '配置分析.md'

    if not plan_p.exists():
        return {'ok': True, 'skipped': True, 'reason': '无规划表',
                'n_plan_skipped': 0, 'n_explained': 0, 'unexplained': []}

    plan_text = plan_p.read_text(encoding='utf-8', errors='replace')
    skipped_items = parse_plan_skipped(plan_text)

    if not skipped_items:
        return {'ok': True, 'skipped': True, 'reason': '规划里没有跳过的项',
                'n_plan_skipped': 0, 'n_explained': 0, 'unexplained': []}

    ca_text = ca_p.read_text(encoding='utf-8', errors='replace') if ca_p.exists() else ''

    # 有没有「本网元无法配置」这类章节或表述
    has_notice = any(m in ca_text for m in UNABLE_MARKERS)

    # 逐项检查：该项的业务关键词有没有在配置分析里出现
    unexplained = []
    explained = 0
    for it in skipped_items:
        biz = it['biz']
        # 提取业务关键词（去掉标点，取前 8 个字）
        kw = re.sub(r'[（）()\[\]【】\s]', '', biz)[:8]
        if kw and kw in ca_text:
            explained += 1
        elif has_notice:
            # 有总体说明就算解释过（避免过度苛责）
            explained += 1
        else:
            unexplained.append(it)

    return {
        'ok': not unexplained,
        'skipped': False,
        'n_plan_skipped': len(skipped_items),
        'n_explained': explained,
        'unexplained': unexplained[:5],
        'has_notice_section': has_notice,
    }


if __name__ == '__main__':
    import json
    import sys
    sd = sys.argv[1] if len(sys.argv) > 1 else '.'
    print(json.dumps(check_unable_notice(sd), ensure_ascii=False, indent=1))
