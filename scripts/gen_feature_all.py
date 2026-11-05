#!/usr/bin/env python3
"""以特性文档为基准全量生成特性配置对照 MD。

遍历特性文档库全部 md：
  §1 特性完整内容（操作场景/必备事项/操作步骤/任务示例，官方原文完整呈现）
  §2 官方示例命令（特性文档自带的所有 MML 命令，完整不截断）
  §3 exp 对应实例（文档命令类型 ∩ exp → 匹配命令带 EXP 行号；无匹配则标注）

用法:
  python3 gen_feature_all.py --feat-dir <特性文档目录> --exp <exp.txt> -o <输出目录>
"""
import argparse
import json
from pathlib import Path
import yaml
import hashlib
import os
import re
import sys
from collections import Counter, defaultdict

# ═══ 特性文档解析 ══════════════════════════════════════════

MML_CMD_RE = re.compile(r'^\s*(?://[^\n]*\n\s*)?('
                        r'(?:[A-Z]+ [A-Z0-9]+(?:\([^)]*\))?)'
                        r'(?:\s*/\s*(?:[A-Z]+ [A-Z0-9]+(?:\([^)]*\))?))*):', re.M)
MML_LINE_RE = re.compile(r'^\s*(?://[^\n]*\n\s*)?('
                         r'(?:[A-Z]+ [A-Z0-9]+(?:\([^)]*\))?)'
                         r'(?:\s*/\s*(?:[A-Z]+ [A-Z0-9]+(?:\([^)]*\))?))*):(.*?);?\s*$')
PARAM_RE = re.compile(r'([A-Z0-9_]+)=(?:([^,;"]+)|"([^"]*)")')
# MML 动词白名单：必备事项表格解析用，防止 "VLAN ID" 等名词短语被误当命令类型
MML_VERBS = frozenset(
    'ADD MOD SET DEL RMV DSP LST SHOW CHK EXP OPR LOD LCK UNL RST ACT DEA '
    'CLS ENQ ED MOV CPY RCL CLR TST INS UPD'.split())


# 场景标注命令拆分：'ADD POOL(风筝S)/ADD UPPOOL(风筝M或L)' → {'ADD POOL', 'ADD UPPOOL'}
CMD_SPAN_RE = re.compile(r'([A-Z]+) ([A-Z0-9]+)(?:\([^)]*\))?')


def cmd_spans_to_names(span: str) -> set:
    """'ADD POOL(风筝S)/ADD UPPOOL(风筝M或L)' → {'ADD POOL', 'ADD UPPOOL'}（剥离场景标注，动词白名单过滤）"""
    out = set()
    for v, t in CMD_SPAN_RE.findall(span):
        if v in MML_VERBS:
            out.add(f'{v} {t}')
    return out


def parse_mml_cmd(line):
    """解析单条 MML → (cmd, params) 或 None"""
    m = MML_LINE_RE.match(line)
    if not m:
        return None
    names = CMD_SPAN_RE.findall(m.group(1))
    cmd = f'{names[0][0]} {names[0][1]}' if names else m.group(1).strip()
    params = {}
    for pm in PARAM_RE.finditer(m.group(2)):
        params[pm.group(1)] = (pm.group(2) or pm.group(3) or '').strip()
    return cmd, params


def baseline_for(doc, cmd, max_lines=2):
    """文档代码块中该命令的原始示例行（含场景括号原样），去重取前 max_lines 条"""
    out = []
    for s in doc.get('scripts', []):
        for ln in s.split('\n'):
            for span in MML_CMD_RE.findall(ln):
                if cmd in cmd_spans_to_names(span):
                    t = ln.strip()
                    if t and t not in out:
                        out.append(t)
                    break
            if len(out) >= max_lines:
                return out
    return out


def load_param_anchors(path):
    """加载值锚定参数 → {(cmd, (p1, p2, ...))}（组内 AND，同命令多行 OR）"""
    if not path or not os.path.exists(path):
        return set()
    anchors = set()
    with open(path, encoding='utf-8') as f:
        for ln in f:
            ln = ln.strip()
            if not ln or ln.startswith('#'):
                continue
            m = re.match(r'^([A-Z]+ [A-Z0-9]+)\s*:\s*\[(.*?)\]$', ln)
            if m:
                ps = tuple(p.strip() for p in m.group(2).split(',') if p.strip())
                if ps:
                    anchors.add((m.group(1), ps))
    return anchors


def parse_feature_md(text, doc_path):
    """解析特性文档 MD → dict（完整内容，不截断）；兼容 UTF-8 BOM"""
    text = text.lstrip('\ufeff')
    lines = text.split('\n')
    title = ''
    for ln in lines:
        if ln.startswith('# '):
            title = ln[2:].strip()
            break
    if not title:
        return None
    # doc_source：文档树路径（用于同名文档的标题补充，见 doc_name_suffix）
    doc_source = []
    mds = re.search(r'^doc_source:\s*\[(.*?)\]', text, re.M | re.S)
    if mds:
        doc_source = [x.strip().strip('"\'') for x in mds.group(1).split(',')]
        doc_source = [x for x in doc_source if x]
    # 分节（保留原文行）
    sections = {}
    cur = None
    for ln in lines:
        if ln.startswith('## '):
            cur = ln[3:].strip()
            sections[cur] = []
        elif cur is not None:
            sections[cur].append(ln)
    # 代码块（任务示例 + 操作步骤 + 全部章节）
    scripts = []
    for sec in ('任务示例', '操作步骤'):
        in_code = False
        buf = []
        for ln in sections.get(sec, []):
            if ln.strip().startswith('```'):
                if in_code:
                    scripts.append('\n'.join(buf))
                    buf = []
                    in_code = False
                else:
                    in_code = True
            elif in_code:
                buf.append(ln)
        if in_code and buf:
            scripts.append('\n'.join(buf))
    # 命令类型全集（脚本 + 步骤 **CMD** 引用）
    all_cmd_types = set()
    or_spans = []   # 含 '/' 的场景变体 span（如 ADD POOL(风筝S)/ADD UPPOOL(风筝M或L)）
    for s in scripts:
        for span in MML_CMD_RE.findall(s):
            all_cmd_types |= cmd_spans_to_names(span)
            if '/' in span:
                or_spans.append(span)
    cmd_chain = []
    for ln in sections.get('操作步骤', []):
        m = re.search(r'\*\*([A-Z]+ [A-Z0-9]+(?:\([^)]*\))?(?:\s*/\s*[A-Z]+ [A-Z0-9]+(?:\([^)]*\))?)*)\*\*', ln)
        if m:
            cmd_chain.extend(sorted(cmd_spans_to_names(m.group(1))))
            if '/' in m.group(1):
                or_spans.append(m.group(1))
    all_cmd_types.update(cmd_chain)
    # 数据表命令（必备事项）
    for ln in sections.get('必备事项', []):
        # 命令格可能带 **加粗**（新版 preprocess 文档形态）→ 先剥离星号再匹配
        m = re.match(r'\|?\s*\*?\*?([A-Z]+ [A-Z0-9]+(?:\s*\([^)]*\))?(?:\s*/\s*[A-Z]+ [A-Z0-9]+(?:\s*\([^)]*\))?)*)\*?\*?\s*\|', ln)
        if m:
            all_cmd_types |= cmd_spans_to_names(m.group(1))
            if '/' in m.group(1):
                or_spans.append(m.group(1))
    # 关键参数表（必备事项"数据"表：参数名称列括号内的参数名 → 判定须命中）
    # 表行格式：| **ADD LOGICINF** | 逻辑接口名称（NAME） | 取值样例 | ... |
    key_params = defaultdict(list)
    last_cmds = []                      # 续行继承：新版文档合并单元格后仅首行带命令列（OR 组挂全部）
    for ln in sections.get('必备事项', []):
        cells = [c.strip() for c in ln.split('|')]
        if len(cells) < 4:
            continue
        cm = re.match(r'^\*?\*?([A-Z]+ [A-Z0-9]+(?:\s*\([^)]*\))?(?:\s*/\s*[A-Z]+ [A-Z0-9]+(?:\s*\([^)]*\))?)*)\*?\*?$', cells[1].strip('*'))
        if cm:
            last_cmds = cmd_spans_to_names(cm.group(1))
        pm = re.search(r'（([A-Z0-9_]+)）', cells[2])
        if not pm or not last_cmds:
            continue
        pname = pm.group(1)
        for c in last_cmds:
            if pname not in key_params[c]:
                key_params[c].append(pname)
    # 场景变体 OR 组：'ADD POOL(风筝S)/ADD UPPOOL(风筝M或L)' → ['ADD POOL', 'ADD UPPOOL']
    # （风筝S 与风筝M/L 场景互斥，判定时组内任一命令命中即整组命中）
    cmd_or_groups = []
    for span in or_spans:
        names = sorted(cmd_spans_to_names(span))
        if len(names) > 1 and names not in cmd_or_groups:
            cmd_or_groups.append(names)
    # 示例命令参数值（用于值锚定匹配：LICITEM 等功能标识参数）
    anchor_vals = {}
    script_counter = Counter()
    for s in scripts:
        for ln in s.split('\n'):
            pr = parse_mml_cmd(ln)
            if pr:
                cmd, params = pr
                script_counter[cmd] += 1
                for k, v in params.items():
                    anchor_vals.setdefault((cmd, k), set()).add(v)
    # 关键命令：操作步骤命令链优先；无链时用示例脚本出现最多的命令
    key_cmds = list(dict.fromkeys(cmd_chain)) or [c for c, _ in script_counter.most_common(3)]
    return {
        'title': title,
        'sections': sections,
        'scripts': scripts,
        'cmd_chain': cmd_chain,
        'cmd_or_groups': cmd_or_groups,
        'all_cmd_types': all_cmd_types,
        'anchor_vals': anchor_vals,
        'key_params': dict(key_params),
        'key_cmds': key_cmds,
        'doc_path': doc_path,
        'doc_source': doc_source,
    }


def _norm_for_dedup(text):
    """内容去重用的归一化键：去开头目录块 + 压缩空白。

    为什么不用原始字节：知识库同一文档存在多种导出格式 —— 实测
    `cn_22_14_000018.md` 两份，一份开头带 `* 操作场景 / * 对系统的影响 /
    * 必备事项 / * 操作步骤` 目录块，正文完全相同（379 vs 410 字节）。
    字节比较会漏掉这类真冗余。

    归一化规则（保守，只抹格式不抹内容）：
      1. 删除正文开头的「目录块」：连续的 `* 一行短词` 且不含句号的条目
      2. 删除所有空白字符（空格/换行/制表）
    残留差异（真正的正文不同）不会被抹掉 —— 判据仍有判别力。
    """
    import re as _re
    lines = text.split('\n')
    # 1. 跳过开头的标题行（# 开头）与其后的空行
    i = 0
    while i < len(lines) and not lines[i].strip():
        i += 1                       # 前导空行
    if i < len(lines) and lines[i].lstrip().startswith('#'):
        i += 1                       # 标题行
    while i < len(lines) and not lines[i].strip():
        i += 1                       # 标题后的空行
    # 2. 目录块：连续以 '* ' 开头、长度 < 20、不含句号/冒号的行
    #    （正文条目通常较长且含标点；目录条目是短词）
    while i < len(lines):
        ln = lines[i].strip()
        if ln.startswith('* ') and len(ln) < 20 and '。' not in ln and '：' not in ln:
            i += 1
        else:
            break
    body = '\n'.join(lines[i:])
    return _re.sub(r'\s+', '', body)


def load_feature_docs(feat_dir):
    """扫描特性文档 → docs 列表（F 编号顺序基准）

    ⚠ 顺序稳定性：F 编号 = 本文档顺序（F001=第 1 篇）。os.walk 必须对 dirs
    排序，否则依赖文件系统 listdir 顺序（macOS APFS 与 Linux ext4 不同），
    跨环境重跑会静默漂移、指纹与文档错位。

    ★ 内容去重（2026-09-19 用户裁决）：
      知识库把同一篇文档收录在多个「知识模块」路径下（UEG 实测 2343 篇
      只有 1294 种内容，冗余 44.7%；如 .../kite_l_bm_Security_Cnf/... 与
      .../bas_oper_l_bm/... 下同一篇证书文档各一份）。
      语义上这表示「多个场景功能复用同一特性方案」，不是独立特性
      ⇒ 按内容 sha256 去重，只保留首次出现的一份。
      ⚠ 只在**同名**之间去重：不同标题的同内容文档保留（标题本身是信息，
        且指纹/F编号按标题对齐，跨标题合并会打乱编号基准）。
      被丢的路径记入 rec['_dup_paths'] 供审计（不静默丢弃）。
    """
    docs = []
    _seen = {}          # (title, sha256) → 首次出现的 doc
    n_dup = 0
    for root, dirs, files in os.walk(feat_dir):
        dirs.sort()   # 目录顺序稳定：跨环境一致
        for fn in sorted(files):
            if not fn.endswith('.md'):
                continue
            path = os.path.join(root, fn)
            try:
                with open(path, encoding='utf-8') as f:
                    text = f.read()
            except Exception:
                continue
            rec = parse_feature_md(text, os.path.relpath(path, feat_dir))
            if rec:
                rec['_raw'] = text     # 原文：供同名文档的语义后缀提取用
                # 同名 + 同内容 → 去重（保留首份，记录冗余路径）
                # ⚠ 判据用「归一化后」而非原始字节：实测同一文档有两种导出
                #   格式 —— 一种开头多一段目录（`* 操作场景 / * 对系统的
                #   影响 / ...`），正文完全相同。字节比较会漏掉这类。
                #   归一化：去掉开头目录块 + 压缩所有空白。
                _key = (rec.get('title', ''), _norm_for_dedup(text))
                if _key in _seen:
                    _seen[_key].setdefault('_dup_paths', []).append(rec.get('doc_path', path))
                    n_dup += 1
                    continue
                _seen[_key] = rec
                docs.append(rec)
    if n_dup:
        docs[0].setdefault('_stats', {})['dedup_dropped'] = n_dup
    return docs


# ═══ exp 解析 ══════════════════════════════════════════════

def parse_exp(path):
    """exp → [(seq, cmd, params)]，带原文行号；自动检测编码（utf-8 → gbk → 替换）"""
    text = None
    for enc in ('utf-8', 'gbk'):
        try:
            text = open(path, encoding=enc).read()
            break
        except (UnicodeDecodeError, UnicodeError):
            continue
    if text is None:
        text = open(path, encoding='utf-8', errors='replace').read()
    cmds = []
    for seq, ln in enumerate(text.split('\n'), 1):
        ln = ln.strip()
        if not ln or ln.startswith(';') or ln.startswith('//'):
            continue
        m = re.match(r'^([A-Z]+ [A-Z0-9]+):(.*?);?\s*$', ln)
        if m:
            cmd = m.group(1)
            params = {}
            for pm in re.finditer(r'([A-Z0-9_]+)=(?:([^,;"]+)|"([^"]*)")', m.group(2)):
                params[pm.group(1)] = (pm.group(2) or pm.group(3) or '').strip()
            cmds.append({'seq': seq, 'cmd': cmd, 'params': params, 'raw': ln})
    return cmds


# ═══ MD 渲染 ═══════════════════════════════════════════════

def render_sec(lines, title):
    if lines:
        return '\n'.join(lines).strip()
    return ''


def build_anchor_index(anchors):
    """anchors → {cmd: [(cmd, ps), ...]} 预建索引。

    ★ M3 优化（2026-09-18）：原实现每次调用都
        sorted((cmd, ps) for (cmd, ps) in anchors if cmd == c['cmd'])
      而它处在「515 篇文档 × 101232 条命令」的双层循环里 ⇒ 约 5200 万次
      全量遍历 + 排序（实测 sorted 独占 13.7s / cmd_matches 28.1s）。
      索引结果只依赖 cmd，与具体命令实例/文档无关 ⇒ 可提前算好。

    **结果与旧实现逐字节相同**：
      · 保持 sorted（组序影响 early return，必须确定性）
      · 同 cmd 的多组，顺序与 sorted 全量后过滤一致
    """
    idx = {}
    for cmd, ps in sorted(anchors):
        idx.setdefault(cmd, []).append((cmd, ps))
    return idx


# 外部调用者（feature_relations 等）反复传**同一个 set 对象**；
# 按其 id 缓存索引 ⇒ 只算一次。⚠ set 不可哈希，不能用 lru_cache。
_idx_cache = {}


def _index_from_set(anchors):
    """set → 索引（按对象 id 缓存；同一 set 对象只算一次）"""
    key = id(anchors)
    hit = _idx_cache.get(key)
    if hit is not None and hit[0] is anchors:
        return hit[1]           # 复核对象身份，防 id 复用
    idx = build_anchor_index(anchors)
    _idx_cache[key] = (anchors, idx)
    return idx


def _groups_for(cmd, anchors_or_idx):
    """取该 cmd 的锚定组（接受 set 或索引）。

    ★ 为什么统一在这里适配：cmd_matches 有 3 处外部调用者
      （feature_relations / analyze_weak_semantics），它们传的是 set。
      在签名上强求索引会逼所有调用者改 —— 而适配放这里只需一处，
      且不产生「两条实现路径」（都归结为同一次查表）。
    """
    if isinstance(anchors_or_idx, dict):
        return anchors_or_idx.get(cmd) or []
    return _index_from_set(anchors_or_idx).get(cmd) or []


def cmd_matches(c, doc, anchors):
    """exp 命令是否匹配特性文档：命令类型 ∈ 文档类型，且值锚定参数命中

    锚定组语义：组内多参数 AND；组无文档示例值 → 不锚定。
    同命令多组时按组序取第一个「有示例值」的组判定：命中即匹配、未命中即排除
    （不再看后续组）——即「第一组优先」，非多组 OR。与 match_features.anchor_value_hit
    的「任一组命中（多组 OR）」语义不同，属既有历史差异，勿按此处推断 OR。
    """
    if c['cmd'] not in doc['all_cmd_types']:
        return False
    doc_anchor_vals = doc.get('anchor_vals', {})
    # ★ 统一入口：接受 anchors(set) 或预建索引(dict)，内部归一为查表。
    #   - 热路径（gen_feature_all 双层循环）：调用方传索引 → O(1)
    #   - 外部调用者（feature_relations / analyze_weak_semantics）：仍传 set，
    #     此处用 lru_cache 按 id 缓存其索引 → 同样 O(1)，且调用点无需改动。
    groups = _groups_for(c['cmd'], anchors)
    if not groups:
        return True
    for cmd, ps in groups:
        vals_list = [doc_anchor_vals.get((cmd, p)) for p in ps]
        if not any(vals_list):
            continue   # 文档示例无这些参数值 → 本组不锚定
        # 组内 AND：有文档示例值的参数必须命中，无示例值的参数跳过
        # （值比较大小写归一：IPv4/IPV4、Local/LOCAL、ipv4uni/IPV4UNI 视为同值）
        if all(v is None or str(c['params'].get(p)).upper() in {str(x).upper() for x in v}
               for p, v in zip(ps, vals_list)):
            return True
        return False   # 本组有锚定值但未命中 → 排除
    return True   # 所有组都无锚定值 → 仅类型匹配


COVERAGE_THRESHOLD = 0.5   # 命令类型覆盖度 ≥50% 且关键配置命令命中 → 判定已配置
QUERY_PREFIXES = ('DSP', 'LST', 'SHOW', 'CHK', 'EXP')   # 查询类命令缺失不致命


def assess_match(matched, doc):
    """匹配程度评估 → (level, coverage, key_hits, key_miss, key_miss_cfg)"""
    match_types = {c['cmd'] for c in matched}
    total = len(doc['all_cmd_types'])
    coverage = len(match_types) / total if total else 0.0
    key_cmds = doc.get('key_cmds', [])
    key_hits = [c for c in key_cmds if c in match_types]
    key_miss = [c for c in key_cmds if c not in match_types]
    key_miss_cfg = [c for c in key_miss if not c.startswith(QUERY_PREFIXES)]
    if matched and coverage >= COVERAGE_THRESHOLD and key_hits and not key_miss_cfg:
        level = '强匹配'
    elif matched:
        level = '弱匹配'
    else:
        level = '未配置'
    return level, coverage, key_hits, key_miss, key_miss_cfg


def _shortest_suffix(paths, title):
    """给一组文档路径找「能让各篇互不相同的最短路径后缀」。

    用于同名文档的标题补充（用户 2026-09-19 裁决）：
      同标题但内容不同的文档（如「部署UPF」10 篇分属不同计费方案）
      必须保留，并从 doc_source 路径取父级作为后缀，让文件名可区分。
    """
    trimmed = []
    for pth in paths:
        q = list(pth)
        while q and q[-1] == title:
            q.pop()
        trimmed.append(q)
    maxlen = max((len(q) for q in trimmed), default=0)
    for k in range(1, maxlen + 1):
        cands = [tuple(q[-k:]) if k <= len(q) else tuple(q) for q in trimmed]
        if len(set(cands)) == len(cands):
            return cands
    return [tuple(q) for q in trimmed]


def _parse_nav(nav_dir):
    """解析 NAV 目录树（缩进式 markdown）→ 标题 → [父级路径]。

    NAV 文件（如 output_udg_nav/NAV_UDG_特性部署.md）形如：
        - 业务专题
          - 5G Core FUP解决方案
            ...
              - 部署UPF        ← 叶子 = 文档标题
    同名标题在树里出现多次（如「部署UPF」10 次，分属不同方案），
    其父级路径天然可区分 —— 这是同名文档命名补充的**权威来源**
    （用户 2026-09-19：路径父标题差异可作为命名补充）。
    """
    import re as _re
    from collections import defaultdict
    raw = defaultdict(list)
    nd = Path(nav_dir)
    if not nd.is_dir():
        return raw

    # ⚠ 两处产品差异（实测，不改会静默出错）：
    #   1. 用 rglob 不用 glob —— UEG 的 NAV 在子目录
    #      （output_ueg_nav/output_ueg_nav_v2/*.md，9578 篇）；
    #      用 glob 会静默解析出 0 条（不报错，产物只是没后缀）。
    #   2. 路径要去重 —— UEG 每个文件是独立小树，同一路径被多个文件
    #      重复收录（实测某路径出现 24 次），不去重会让
    #      「路径数 ≥ 篇数」的判断失效。
    for nf in sorted(nd.rglob('*.md')):
        stack = []
        for ln in nf.read_text(encoding='utf-8',
                               errors='replace').splitlines():
            m = _re.match(r'^(\s*)-\s+(.+?)\s*$', ln)
            if not m:
                continue
            level = len(m.group(1)) // 2
            name = m.group(2).strip()
            while stack and stack[-1][0] >= level:
                stack.pop()
            raw[name].append([x[1] for x in stack])
            stack.append((level, name))
    # 去重（保持出现顺序）
    out = {k: [list(x) for x in dict.fromkeys(tuple(p) for p in v)]
           for k, v in raw.items()}
    return out


def _pick_nav_suffix(paths, title, used):
    """从 NAV 父级路径里挑「能和已用后缀区分开」的最短后缀。

    used: 本组已分配的后缀集合（避免新后缀撞车）。
    """
    cands = []
    for pth in paths:
        for k in range(1, len(pth) + 1):
            cands.append((k, ' / '.join(pth[-k:])))
    # 优先最短，其次不与已用重复
    cands.sort(key=lambda x: (x[0], x[1]))
    for k, txt in cands:
        if txt and txt not in used:
            return txt
    return ''


def _own_candidates(text, doc_path=''):
    """从文档自身提取「候选区分特征」，按可信度降序返回列表。

    为什么改成列表（2026-09-19 实测）：单返回值会「过早锁定」——
    同级文档 ID 相同（同一特性的不同方案版本）时，返回 ID 等于没区分，
    但函数已经用了最高优先级的信息，无法降级到下一级。
    ⇒ 返回候选序列，由调用方在同名组内逐级尝试，冲突才降级。

    候选层级（可信度降序）:
      1. 正文「前提条件」里的场景/方案描述（如「风筝S场景」「风筝M/L场景」）
         —— 文档自述适用场景，最准
      2. 正文「前提条件」引用的特性 ID + 名称（如 GWFD-010173融合计费）
         —— 能区分不同特性；同特性不同方案时会同值
      3. 文件名后缀 _l/_s/_m（风筝L / 风筝S / 风筝M 方案标识）
         —— 上游命名约定，用于第 2 级同值时的最后区分
    """
    out = []
    m0 = re.search(r'前提条件\s*\n+(.*?)(?:\n\s*\n|\Z)', text, re.S)
    seg = m0.group(1) if m0 else ''

    # ── 1. 场景/方案描述 ──
    if seg:
        sc = re.findall(r'([\u4e00-\u9fffA-Za-z0-9/、]{1,12}?)场景', seg)
        sc = [x for x in sc if x and x not in ('该', '以下', '此', '本', '适用', '典型')]
        seen, uniq = set(), []
        for x in sc:
            if x not in seen:
                seen.add(x)
                uniq.append(x)
        if uniq:
            out.append('、'.join(uniq)[:60] + '场景')

    # ── 2. 特性 ID ──
    if seg:
        ids = re.findall(r'(GWFD-\d+)\s*([\u4e00-\u9fffA-Za-z0-9]*)', seg)
        if ids:
            out.append('、'.join((a + b).strip() for a, b in ids)[:60])

    # ── 3. 文件名方案后缀 ──
    if doc_path:
        m1 = re.search(r'_(l|s|m)\.md$', doc_path)
        if m1:
            out.append({'l': '风筝L方案', 's': '风筝S方案', 'm': '风筝M方案'}[m1.group(1)])

    # 去重保序
    seen2, res = set(), []
    for x in out:
        if x and x not in seen2:
            seen2.add(x)
            res.append(x)
    return res


def _own_feature(text, doc_path=''):
    """兼容旧调用：返回最高可信度的单个候选（无候选则空串）。"""
    c = _own_candidates(text, doc_path)
    return c[0] if c else ''



# ═══ 路径后缀（同名文档的最后一级区分手段）════════════════════
#  用户裁决（2026-09-19 方案2）：NAV/正文特征都区分不了时，用「路径的
#  可区分段」作后缀，不要用无意义的序号。
#  规则：① 语义目录段（BM/VM/kite/bas_oper_l_bm）→ ② 语义文件名
#        → ③ 完整路径（含 ID）→ ④ 序号兜底
#  ⚠ 剥掉各篇公共的「连续尾段」——真正差异常在首段（如 BM/VM/kite）。

import re as _re2

_RE_ID_SEG = _re2.compile(r'^(zh-cn|DOCNAV|cn_|udg_)?[a-z0-9_\-]*\d{4,}[a-z0-9_\-]*$', _re2.I)
_RE_NUMSEG = _re2.compile(r'^\d+$')


def _seg_meaningful(seg):
    """路径段是否有语义（非纯 ID、非纯数字）。"""
    return not _RE_ID_SEG.match(seg) and not _RE_NUMSEG.match(seg)


def _path_semantic_segs(path):
    """目录段中有语义的部分（不含文件名）。"""
    body = path.split('/')[:-1]
    return [x for x in body if _seg_meaningful(x)]


def _path_fname_segs(path):
    """文件名去扩展名（本身不是纯 ID 时才有意义）。"""
    fn = path.split('/')[-1]
    stem = fn[:-3] if fn.endswith('.md') else fn
    return [stem] if _seg_meaningful(stem) else []


def _strip_common_tail(segs_list):
    """剥掉各篇公共的连续尾段，返回差异核心。"""
    if not segs_list:
        return segs_list
    common, maxlen = 0, min((len(x) for x in segs_list), default=0)
    for d in range(1, maxlen + 1):
        if len({tuple(x[-d:]) for x in segs_list}) == 1:
            common = d
        else:
            break
    return [x[:len(x) - common] if common else x for x in segs_list]


def path_suffixes(doc_paths):
    """给同名组的多条路径，返回各自「最短可区分段」（无法区分返回 ''）。"""
    from collections import Counter as _C
    n = len(doc_paths)
    if n < 2:
        return [''] * n
    out = [''] * n

    def _fill(source, maxd):
        for d in range(1, maxd + 1):
            if all(out[i] for i in range(n)):
                return
            keys = ['__DONE__%d' % i if out[i] else
                    ('/'.join(source[i][-d:]) if source[i] else '')
                    for i in range(n)]
            c = _C(k for k, o in zip(keys, out) if not o)
            for i in range(n):
                if not out[i] and keys[i] and c[keys[i]] == 1:
                    out[i] = keys[i]

    _fill(_strip_common_tail([_path_semantic_segs(p) for p in doc_paths]), 5)
    _fill(_strip_common_tail([_path_fname_segs(p) for p in doc_paths]), 2)
    _fill([p.split('/') for p in doc_paths], 8)
    return out


_KB_CACHE = {}


def _norm_body(raw, sample=1800):
    """归一正文并采样：去 frontmatter、去空白，取「首/中/尾」三段定长样本。

    ⚠ 性能（2026-09-19 实测）：原本对 2 万字符做 difflib 全文相似度，
    588 次 ratio() 耗 62s（find_longest_match O(n²)）。
    改为等量采样后计算量降约一个量级，配对结论不变（对比 10 组样本一致）。
    """
    import re as _re
    body = _re.sub(r'^---\n.*?\n---\n', '', raw, flags=_re.S)
    body = _re.sub(r'[ \t\r\n]+', '', body)
    n = len(body)
    if n <= sample * 3:
        return body
    return (body[:sample] + body[n // 2 - sample // 2: n // 2 + sample // 2]
            + body[-sample:])


def _load_kb_index(kb_dir):
    """读 kb111 索引（进程内缓存）：name → [(filename, doc_source 路径, 采样正文)]"""
    import re as _re
    if kb_dir in _KB_CACHE:
        return _KB_CACHE[kb_dir]
    kb = Path(kb_dir)
    idx = {}
    if kb.is_dir():
        for p in sorted(kb.glob('*.md')):
            raw = p.read_text(encoding='utf-8', errors='replace')
            m = _re.search(r'^name:\s*(.+?)\s*$', raw, _re.M)
            if not m:
                continue
            ds = _re.search(r'^doc_source:\s*\[(.*?)\]', raw, _re.M | _re.S)
            pth = ([x.strip().strip('"\'') for x in ds.group(1).split(',')]
                   if ds else [])
            idx.setdefault(m.group(1).strip(), []).append(
                (p.name, [x for x in pth if x], _norm_body(raw)))
    _KB_CACHE[kb_dir] = idx
    return idx


def _match_kb_suffix(docs, kb_dir):
    """把无自身特征的文档配对到 kb111 文档，取 doc_source 父级做后缀。

    配对判据：采样正文相似度（difflib）+ 一对一最优分配（贪心取全局最高）。
    返回 doc_path → 后缀。配不上的不出现在返回值里。
    """
    import difflib
    kb_by_name = _load_kb_index(kb_dir)
    if not kb_by_name:
        return {}
    # 待配对的文档：按标题分组
    from collections import defaultdict
    todo = defaultdict(list)
    for d in docs:
        todo[d['title']].append(d)

    out = {}
    for title, group in todo.items():
        cands = kb_by_name.get(title)
        if not cands:
            continue
        bodies = [_norm_body(d.get('_raw') or '') for d in group]
        M = []
        for body in bodies:
            M.append([difflib.SequenceMatcher(None, body, c[2]).ratio()
                      for c in cands])
        flat = sorted(((M[i][j], i, j) for i in range(len(group))
                       for j in range(len(cands))), reverse=True)
        used_d, used_c = set(), set()
        for r, i, j in flat:
            if i in used_d or j in used_c:
                continue
            used_d.add(i)
            used_c.add(j)
            name, pth, _ = cands[j]
            suf = _shortest_suffix([pth], title)
            txt = ' / '.join(suf[0]) if suf and suf[0] else ''
            if txt:
                out[group[i]['doc_path']] = txt
    return out


def compute_name_suffixes(docs, nav_dir=None):
    """为同名文档计算标题后缀：doc_path → 后缀字符串（'' = 无需后缀）。

    三步走（用户 2026-09-19 裁决：路径父标题差异可作为命名补充）：
      1. NAV 目录树 —— 同名标题在树里的父级路径（权威来源）
      2. 文档自身特征 —— 「前提条件」引用的特性 ID（如 GWFD-010173）
      3. 仍无法区分 —— 加序号，保证文件名不冲突

    ⛔ 不做「与 kb111 全文相似度配对」—— 实测判据不成立：同名文档在
       参数值层面完全相同（5 篇「部署UPF」参数值对都是 89 个），
       相似度 0.13 处于噪声区，两版实现给出不同配对结论。
    """
    from collections import defaultdict
    nav = _parse_nav(nav_dir) if nav_dir else {}
    by_title = defaultdict(list)
    for d in docs:
        by_title[d['title']].append(d)
    out = {}
    for title, items in by_title.items():
        if len(items) <= 1:
            out[items[0]['doc_path']] = ''
            continue
        sufs = [''] * len(items)
        used = set()
        # 第一步：NAV 目录树（同名标题 → 多条父级路径）
        navpaths = nav.get(title) or []
        if len(navpaths) >= len(items):
            for k in range(len(items)):
                sfx = _pick_nav_suffix(navpaths, title, used)
                if sfx:
                    sufs[k] = sfx
                    used.add(sfx)
        # 第二步：文档自身特征 —— 逐级降级（候选按可信度降序，
        # 同组内冲突则试下一级，见 _own_candidates 文档）
        cands = [_own_candidates(it.get('_raw') or '', it.get('doc_path') or '')
                 for it in items]
        maxlv = max((len(c) for c in cands), default=0)
        for lv in range(maxlv):
            for k, cs in enumerate(cands):
                if sufs[k] or lv >= len(cs):
                    continue
                sfx = cs[lv]
                if sfx and sfx not in used:
                    sufs[k] = sfx
                    used.add(sfx)
        # 第三步：路径可区分段（用户裁决 2026-09-19 方案2）
        #   NAV 与正文特征都区分不了时，用路径段而不是无意义序号。
        remain = [k for k, sfx in enumerate(sufs) if not sfx]
        if remain:
            psufs = path_suffixes([items[k].get('doc_path', '') for k in remain])
            for k, ps in zip(remain, psufs):
                if ps and ps not in used:
                    sufs[k] = ps
                    used.add(ps)
        # 第四步：仍冲突的加序号（保证不重名）
        seen = defaultdict(list)
        for k, sfx in enumerate(sufs):
            seen[sfx].append(k)
        for key, ks in seen.items():
            if len(ks) > 1:
                for n, k in enumerate(ks, 1):
                    sufs[k] = (f'{sufs[k]}·{n}' if sufs[k]
                               else f'同名文档{n}')
        for it, sfx in zip(items, sufs):
            out[it['doc_path']] = sfx
    return out
def make_fname(doc, level, prefix='F', suffix=''):
    """文件名：序号_[后缀#]标题；弱匹配/未配置加标识。

    suffix: 同名文档的父级限定词（见 compute_name_suffixes），
            写在标题前，形如 `F212_部署UPF（GWFD-010173 融合计费）.md`。
    """
    title = re.sub(r'[\\/:*?"<>|#]', '', doc['title']).strip() or 'untitled'
    tag = {'强匹配': '', '弱匹配': '弱匹配_', '未配置': '未配置_'}[level]
    sfx = re.sub(r'[\\/:*?"<>|#]', '', suffix).strip()
    mid = f'（{sfx[:40]}）' if sfx else ''
    return f"{prefix}{doc['_idx']:03d}_{tag}{title}{mid}.md"


def _render_chain_section(fp_feat, exp_idx):
    """§3 链装配渲染 —— 复用 chain_by_linkgroups 的渲染结果，只取「现网实例 + 结论」两段。

    为什么只取两段：本函数嵌在 gen_feature_all 的产物里，
    §1 已由 gen_feature_all 出（官方文档原文），
    chain_by_linkgroups 的「一、特性骨架」与 §1 信息重叠，故剥掉。
    """
    import chain_by_linkgroups as CB
    fid = fp_feat.get('_fid') or 'F???'
    # sections='instances'：只渲染「现网实例 + 结论」，标题降为 '###'/'####'
    # —— gen_feature_all 的 §1 已出官方文档原文与骨架，避免重复。
    md = CB.render_feature(fid, fp_feat, [], exp_idx,
                           sections='instances', heading_level=3)
    return md.rstrip() + '\n'


def gen_feature_md(doc, exp_cmds, exp_cmd_types, anchors, anchor_idx,
                   has_exp=True, fp_feat=None, exp_idx=None):
    """一篇特性文档 → MD 文本（has_exp=False：无 exp 模式，§3 标注标准方案）。

    fp_feat: 该文档对应的特性指纹 dict（features_*.yaml 的 features[fid]）。
             有指纹时 §3 走「链装配」渲染（link_groups 按值聚合 + enum 严格口径），
             无指纹时退回旧的「行号区间平铺」渲染（兼容）。
    exp_idx: EXP 命令按类型索引（{cmd: [实例,...]}），有指纹时必需。
    """
    L = []
    L.append(f"# {doc['title']}")
    L.append("")
    L.append(f"> 来源：`{doc['doc_path']}`")
    L.append("")

    # 值锚定说明（该文档示例中出现的锚定参数值）
    doc_anchor_vals = doc.get('anchor_vals', {})
    anchor_note = []
    for (cmd, ps) in sorted(anchors):
        if cmd not in doc['all_cmd_types']:
            continue
        parts = []
        for p in ps:
            vals = doc_anchor_vals.get((cmd, p))
            if vals:
                parts.append(f"{p} ∈ {{{'、'.join(sorted(vals))}}}")
        if parts:
            anchor_note.append(f"{cmd} 仅匹配 {' 且 '.join(parts)}")

    # ── §1 特性完整内容 ──────────────────────────────────
    L.append("## 1. 特性完整内容（官方文档原文）")
    L.append("")
    for sec in ('操作场景', '必备事项', '操作步骤'):
        body = doc['sections'].get(sec)
        if body:
            L.append(f"### {sec}")
            L.append("")
            L.append('\n'.join(body).strip())
            L.append("")

    # ── §2 官方示例命令（完整）───────────────────────────
    L.append("## 2. 官方示例命令（特性文档原始配置示例，完整）")
    L.append("")
    if doc['scripts']:
        for s in doc['scripts']:
            L.append("```mml")
            L.append(s.strip())
            L.append("```")
            L.append("")
        types = sorted(doc['all_cmd_types'])
        L.append(f"**本特性覆盖命令类型（{len(types)}）**：{'、'.join(types)}")
        L.append("")
    else:
        L.append("> 特性文档无 MML 示例命令块（仅文字说明）。")
        L.append("")
        if doc['cmd_chain']:
            L.append(f"**操作步骤命令链**：{' → '.join(doc['cmd_chain'])}")
            L.append("")

    # ═══ §3 现网实例 ═══
    # 有特性指纹 → 链装配渲染（link_groups 按值聚合成链 + enum 严格口径三态）
    # 无指纹       → 退回旧的「EXP 行号区间平铺」（兼容未覆盖的文档）
    if fp_feat is not None and exp_idx is not None:
        L.append("## 3. 现网实例（链装配）")
        L.append("")
        L.append(_render_chain_section(fp_feat, exp_idx))
        return '\n'.join(L)

    # ── 旧渲染（无指纹时的兜底）──
    L.append("## 3. exp 对应实例")
    L.append("")
    if not has_exp:
        L.append("> 无 exp 参考：基于特性文档生成标准方案，参数值用官方示例值并标注待确认"
                 "（命名/编号规律按文档示例归纳，落地前需专家确认）。")
        L.append("")
        if anchor_note:
            L.append(f"> 值锚定说明：{'；'.join(anchor_note)}")
            L.append("")
        return '\n'.join(L)
    matched = [c for c in exp_cmds if cmd_matches(c, doc, anchor_idx)]
    if not matched:
        L.append(f"> 本局点 exp（FSUPFm102BHW）未配置此特性："
                 f"{'文档命令类型与 exp 无交集' if not (doc['all_cmd_types'] & exp_cmd_types)
                  else '文档命令在 exp 中存在类型但值锚定参数未命中（授权项/标识未启用）'}。")
        L.append("")
        if anchor_note:
            L.append(f"> 值锚定说明：{'；'.join(anchor_note)}")
            L.append("")
        return '\n'.join(L)
    match_types = sorted({c['cmd'] for c in matched})
    level, coverage, key_hits, key_miss, key_miss_cfg = assess_match(matched, doc)
    L.append(f"> exp 匹配：{len(match_types)}/{len(doc['all_cmd_types'])} 种命令类型"
             f"（{coverage * 100:.0f}%），{len(matched)} 条命令"
             f"（EXP 行号 {matched[0]['seq']}–{matched[-1]['seq']}）")
    L.append("")
    if anchor_note:
        L.append(f"> 值锚定：{'；'.join(anchor_note)}")
        L.append("")
    key_txt = f"关键命令命中 {len(key_hits)}/{len(doc.get('key_cmds', []))}"
    if key_hits:
        key_txt += f"（{'、'.join(key_hits)}）"
    if key_miss_cfg:
        key_txt += f"，缺关键配置命令：{'、'.join(key_miss_cfg)}"
    elif key_miss:
        key_txt += f"，缺查询类：{'、'.join(key_miss)}"
    L.append(f"> {key_txt}")
    L.append("")
    if level == '强匹配':
        verdict = f"匹配程度：**强匹配**（覆盖度 {coverage * 100:.0f}% ≥ 50% 且关键配置命令命中）→ 判定已配置"
    else:
        reason = []
        if coverage < COVERAGE_THRESHOLD:
            reason.append(f"覆盖度 {coverage * 100:.0f}% < 50%")
        if not key_hits:
            reason.append("关键命令未命中")
        if key_miss_cfg:
            reason.append(f"关键配置命令缺失：{'、'.join(key_miss_cfg)}")
        verdict = (f"匹配程度：**弱匹配**（{'、'.join(reason)}）"
                   f"→ 仅 exp 中存在部分命令，未达『已配置』标准")
    L.append(f"> {verdict}")
    L.append("")

    # ── 段落聚类：相邻匹配命令行号间隔 ≤ GAP → 同一段落 ──
    GAP = 30
    paras = []
    cur = []
    prev = None
    for c in matched:
        if prev is None or c['seq'] - prev <= GAP:
            cur.append(c)
        else:
            paras.append(cur)
            cur = [c]
        prev = c['seq']
    if cur:
        paras.append(cur)

    # 官方示例块命令类型（用于段落 ↔ 示例块对应标注）
    script_blocks = []
    for s in doc['scripts']:
        blk = []
        for ln in s.split('\n'):
            pr = parse_mml_cmd(ln)
            if pr:
                blk.append(pr[0])
        script_blocks.append(blk)

    for pi, para in enumerate(paras, 1):
        cts = [c['cmd'] for c in para]
        cnt = Counter(cts)
        top = '、'.join(f"{k}×{v}" for k, v in cnt.most_common(4))
        more = f" 等 {len(cnt)} 种" if len(cnt) > 4 else ''
        L.append(f"### 3.{pi} EXP 行 {para[0]['seq']}–{para[-1]['seq']}（{len(para)} 条：{top}{more}）")
        L.append("")
        # 对应官方示例块标注：段落命令类型 ∩ 示例块命令类型
        para_types = set(cts)
        blk_hits = []
        for bi, blk in enumerate(script_blocks, 1):
            inter = para_types & set(blk)
            if inter:
                blk_hits.append(f"示例块 #{bi}（{'、'.join(sorted(inter))}）")
        if blk_hits:
            L.append(f"> 对应：{'；'.join(blk_hits[:3])}")
            L.append("")
        L.append("```text")
        for c in para:
            L.append(f"{c['seq']:>5}  {c['raw']}")
        L.append("```")
        L.append("")
    return '\n'.join(L)


# ═══ main ══════════════════════════════════════════════════

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--feat-dir', required=True, help='特性文档目录')
    ap.add_argument('--exp', required=False, default=None,
                    help='exp 原文（可选；缺省=无 exp 模式，生成标准方案，§3 标注无 exp 参考）')
    ap.add_argument('-o', '--output', required=True, help='输出目录')
    ap.add_argument('--name-prefix', default='F', help='文件名序号前缀')
    ap.add_argument('--fingerprint', default=None,
                    help='特性指纹 YAML（features_*.yaml）；给了则 §3 走链装配渲染')
    ap.add_argument('--nav-dir', default=None,
                    help='NAV 目录树目录（如 output_udg_nav）：'
                         '同名文档按父级路径补后缀；不给则只靠自身特征+序号')
    ap.add_argument('--anchors', default=None,
                    help='值锚定参数规则 YAML（默认 rules/param_anchor.yaml）')
    args = ap.parse_args()

    if args.anchors is None:
        args.anchors = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                    '..', 'rules', 'param_anchor.yaml')
    anchors = load_param_anchors(args.anchors)
    # ★ M3：一次性预建索引（旧实现在双层循环里每次重算+排序，5200 万次）
    anchor_idx = build_anchor_index(anchors)
    print(f"值锚定参数: {sorted(anchors) if anchors else '无'}")

    docs = load_feature_docs(args.feat_dir)
    has_exp = bool(args.exp)
    exp_cmds = parse_exp(args.exp) if has_exp else []
    exp_cmd_types = {c['cmd'] for c in exp_cmds}

    # ★ 特性指纹（链装配渲染的数据源）：doc_path → 指纹 dict
    fp_by_doc = {}
    exp_idx = None
    if args.fingerprint:
        import chain_by_linkgroups as CB
        if not os.path.exists(args.fingerprint):
            sys.exit(f'找不到指纹文件: {args.fingerprint}')
        with open(args.fingerprint, encoding='utf-8') as f:
            _fpd = yaml.safe_load(f)
        fp_by_title = {}
        for _fid, _fv in (_fpd.get('features') or {}).items():
            _fv['_fid'] = _fid                # 渲染时取用
            _dp = _fv.get('doc_path')
            if _dp:
                fp_by_doc[_dp] = _fv
            _tt = (_fv.get('title') or '').strip()
            if _tt:
                fp_by_title.setdefault(_tt, _fv)
        exp_idx = CB.index_exp(exp_cmds)
        print(f"特性指纹: {len(fp_by_doc)} 个 doc_path（来自 {args.fingerprint}）")
    print(f"特性文档: {len(docs)} 篇 | exp: {len(exp_cmds)} 条命令 / {len(exp_cmd_types)} 种类型"
          if has_exp else f"特性文档: {len(docs)} 篇 | 无 exp（标准方案模式）")

    # 同名文档的标题补充（doc_path → 后缀）；无指纹时也用，保证文件名可区分
    name_suffix = compute_name_suffixes(docs, nav_dir=args.nav_dir)
    if any(name_suffix.values()):
        n_sfx = sum(1 for v in name_suffix.values() if v)
        print(f"同名文档标题补充: {n_sfx} 篇（从 doc_source 取父级限定词）")

    os.makedirs(args.output, exist_ok=True)
    # 清空旧产物（仅本目录 *.md）
    for fn in os.listdir(args.output):
        if fn.endswith('.md'):
            os.remove(os.path.join(args.output, fn))

    strong_docs, weak_docs, unmatched_docs = [], [], []
    docmap = {}   # doc_path → 文件名（doc_card_side/装配取档反查键，见方案_判定卡doc侧错位修复）
    for i, doc in enumerate(docs, 1):
        doc['_idx'] = i
        matched = [c for c in exp_cmds if cmd_matches(c, doc, anchor_idx)]
        level = assess_match(matched, doc)[0]
        if level == '强匹配':
            strong_docs.append(doc)
        elif level == '弱匹配':
            weak_docs.append(doc)
        else:
            unmatched_docs.append(doc)
        # 指纹匹配：先按 doc_path 精确，再按标题兜底
        # （同标题多文档 = 同一特性在不同方案下的文档，共用同一套链装配）
        _fp = fp_by_doc.get(doc['doc_path']) or fp_by_title.get(doc['title'])
        md = gen_feature_md(doc, exp_cmds, exp_cmd_types, anchors, anchor_idx,
                            has_exp, fp_feat=_fp, exp_idx=exp_idx)
        fname = make_fname(doc, level, args.name_prefix,
                           suffix=name_suffix.get(doc['doc_path'], ''))
        docmap[doc['doc_path']] = fname
        with open(os.path.join(args.output, fname), 'w', encoding='utf-8') as f:
            f.write(md)
    # _docmap.json：doc_path 主键 → 文件名（与 README 同生命周期）。
    # ⚠ gt 文件名为遍历序，与指纹 F-ID（去重 doc_path 字典序）是两套编号——
    #   消费方一律经此反查取档，禁止 fid 前缀 glob（Pitfall 见方案文档 §1）。
    with open(os.path.join(args.output, '_docmap.json'), 'w', encoding='utf-8') as f:
        json.dump(docmap, f, ensure_ascii=False, indent=1)

    # README 索引
    readme = [f"# 特性配置 groundtruth（以特性文档为基准）", "",
              f"- 特性文档库：{args.feat_dir}",
              (f"- exp：{args.exp}（{len(exp_cmds)} 条命令）" if has_exp
               else "- exp：无（标准方案模式，参数值用官方示例值并标注待确认）"),
              f"- 特性文档总数：{len(docs)} 篇",
              f"- **强匹配**（覆盖度 ≥50% 且关键命令命中，判定已配置）：{len(strong_docs)} 篇",
              f"- **弱匹配**（有对应命令但未达标准）：{len(weak_docs)} 篇（文件名带『弱匹配_』）",
              f"- **未配置**（无对应命令/值锚定未命中）：{len(unmatched_docs)} 篇（文件名带『未配置_』）",
              "",
              "## 强匹配（判定已配置）", "",
              "| 文件 | 特性 | 命令类型覆盖 |",
              "|---|---|---|"]
    for doc in strong_docs:
        fname = make_fname(doc, '强匹配', args.name_prefix,
                           suffix=name_suffix.get(doc['doc_path'], ''))
        inter = len({c['cmd'] for c in exp_cmds if cmd_matches(c, doc, anchor_idx)})
        readme.append(f"| {fname} | {doc['title']} | {inter}/{len(doc['all_cmd_types'])} |")
    readme += ["", "## 弱匹配（未达已配置标准）", ""]
    for doc in weak_docs[:60]:
        readme.append(f"- {make_fname(doc, '弱匹配', args.name_prefix, suffix=name_suffix.get(doc['doc_path'], ''))}")
    if len(weak_docs) > 60:
        readme.append(f"- …… 其余 {len(weak_docs) - 60} 篇略")
    readme += ["", "## 未配置（本局点未配置）", ""]
    for doc in unmatched_docs[:60]:
        readme.append(f"- {make_fname(doc, '未配置', args.name_prefix, suffix=name_suffix.get(doc['doc_path'], ''))}")
    if len(unmatched_docs) > 60:
        readme.append(f"- …… 其余 {len(unmatched_docs) - 60} 篇略")
    with open(os.path.join(args.output, 'README.md'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(readme))
    print(f"✅ 已生成 {len(docs)} 篇 MD + README → {args.output}")


if __name__ == '__main__':
    main()
