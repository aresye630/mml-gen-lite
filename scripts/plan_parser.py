#!/usr/bin/env python3
"""修正规划表族名解析器：兼容各种真实写法。

实测遇到过的写法（都来自真实 agent 输出）：
  ADD APN（UDG）                    ← 带网元后缀
  SET APN*（UNC）                   ← 带星号通配
  ADD USRPROFGROUP? / APNUSRPROFG（UNC）
                                    ← 带问号 + 多族斜杠分隔
  MOD POOL                          ← 标准
  ADD PCSCFGRPBNDAPN（UNC，候选）    ← 带候选标注
  新增 ADD APN                       ← 带中文动词前缀

旧正则要求「动词 + 族名 + 结尾」，上述全部漏掉 →
实测 NC20260810002261 明明规划了 25 个 APN 属性族，却被算成 0/53。
"""
import re
from pathlib import Path

# ── 新的族名解析（要同时改到所有统计脚本）──

VERB_RE = re.compile(r'\b(ADD|MOD|SET|RMV)\s+', re.I)
FAM_RE = re.compile(r'([A-Z][A-Z0-9_]{2,})')


def extract_fams_from_cell(cell):
    """从「命令族」单元格提取族名，兼容各种后缀。

    规则：
      1. 找单元格里所有 ADD/MOD/SET/RMV 之后的 token
      2. token 取前面连续的 [A-Z][A-Z0-9_]* 部分
      3. 去掉纯通配符（如 APN* → APN，SET APN* 表示所有 APN 开头的属性族）
    """
    out = set()
    if not cell:
        return out
    # 全大写化便于匹配，但保留原值用于判断
    for m in VERB_RE.finditer(cell):
        rest = cell[m.end():]
        # 取紧接着的 token
        tm = re.match(r'([A-Za-z][A-Za-z0-9_]*)', rest)
        if not tm:
            continue
        raw = tm.group(1)
        name = raw.upper()
        # 过滤：太短、纯数字、明显不是族名
        if len(name) < 3:
            continue
        # 「APN*」这种通配：标记为前缀匹配（返回带 * 的形态，调用方决定）
        if rest[len(raw):len(raw) + 1] == '*':
            out.add(name + '*')
        else:
            out.add(name)
    return out


def fam_matches(planned, gt_fam):
    """判断规划里的某个族（可能是前缀通配）是否命中 GT 族。"""
    if planned.endswith('*'):
        prefix = planned[:-1]
        return gt_fam.startswith(prefix)
    return planned == gt_fam


def expand_hits(planned_set, gt_set):
    """把规划集合（含通配）展开成命中的 GT 族。"""
    hits = set()
    for gt_fam in gt_set:
        for pl in planned_set:
            if fam_matches(pl, gt_fam):
                hits.add(gt_fam)
                break
    return hits


def parse_plan_table(text):
    """解析规划表，返回 {状态: set(族名或前缀*)}。

    同时返回全部（不分状态）的集合，供不同统计口径用。
    """
    by_status = {'确认': set(), '待定': set(), '跳过': set(), '其他': set()}
    lines = text.split('\n')
    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if not line.startswith('|'):
            i += 1
            continue
        header = [c.strip() for c in line.strip().strip('|').split('|')]
        if '命令族' not in header:
            i += 1
            continue
        fi = header.index('命令族')
        si = header.index('状态') if '状态' in header else None
        ncol = len(header)
        i += 1
        # 跳过分隔行
        if i < len(lines) and re.fullmatch(r'[|\s\-:]+', lines[i].strip()):
            i += 1
        while i < len(lines):
            row = lines[i].strip()
            if not row.startswith('|'):
                break
            cells = [c.strip() for c in row.strip().strip('|').split('|')]
            if len(cells) >= ncol:
                st_raw = cells[si] if (si is not None and si < ncol) else ''
                if '跳过' in st_raw:
                    st = '跳过'
                elif '待定' in st_raw or '待确认' in st_raw:
                    st = '待定'
                elif '确认' in st_raw or '人工调整' in st_raw:
                    st = '确认'
                else:
                    st = '其他'
                fams = extract_fams_from_cell(cells[fi])
                # 过滤掉明显是动作词/参数的假族名
                fams = {f for f in fams
                        if f not in ('ADD', 'MOD', 'SET', 'RMV')
                        and not f.isdigit()}
                by_status[st] |= fams
            i += 1
        continue
    return by_status


if __name__ == '__main__':
    # 自测：用真实规划表
    p = Path('/tmp/eval_versions_out/V3/NC20260810002261/命令族规划.md')
    if p.exists():
        bs = parse_plan_table(p.read_text(encoding='utf-8'))
        print('解析结果：')
        for k, v in bs.items():
            print(f'  {k}: {len(v)} 个')
        print(f'\n  确认的族样例: {sorted(bs["确认"])[:12]}')

        import json
        GT = json.loads(Path('/tmp/gt_cleaned.json').read_text(encoding='utf-8'))
        g = next(x for x in GT if x['ticket'] == 'NC20260810002261')
        gt = {f for _, _, f, _, _ in g['kept']}
        allf = bs['确认'] | bs['待定'] | bs['其他']
        hits = expand_hits(allf, gt)
        print(f'\n  命中 GT: {len(hits)}/{len(gt)}')
