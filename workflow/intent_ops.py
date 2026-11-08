"""意图结构化解析：从意图文本提取「操作清单」。

用户裁定（2026-11-08）：
  · 代码优先解析，model 兜底
  · 目的：把【删除】/【新增】段落转成明确的操作清单，
    避免 agent 自己猜动词（实测 10 个有删除意图的工单里 8 个配成了新增）

输出：
  {
    operations: [{verb: 'RMV'|'ADD'|'MOD', targets: [名词...]}],
    source: 'code' | 'none',
    warnings: [...]
  }
"""
import re

# 段落标题 → 动词
SECTION_VERB = {
    '删除': 'RMV', '删掉': 'RMV', '去除': 'RMV', '移除': 'RMV', '下线': 'RMV',
    '新增': 'ADD', '增加': 'ADD', '新建': 'ADD', '添加': 'ADD',
    '修改': 'MOD', '调整': 'MOD', '变更': 'MOD', '更新': 'MOD',
}

# 段落标题的正则：【删除】【新增/修改】- 接口 等
SECTION_RE = re.compile(r'【([^】]+)】')


def _split_targets(text):
    """拆分目标名词列表。

    「对端NF的DNN信息、对端NF的SMF服务区域信息、UPF节点」
      → ['对端NF的DNN信息', '对端NF的SMF服务区域信息', 'UPF节点']
    """
    text = text.strip()
    if not text:
        return []
    # 去 bullet 和换行
    text = re.sub(r'^\s*[-•]\s*', '', text, flags=re.M)
    # 按顿号/分号/换行切
    parts = re.split(r'[、；;\n]+', text)
    out = []
    for p in parts:
        p = p.strip().strip('-•').strip()
        # 去掉「其他：」前缀
        p = re.sub(r'^其他[：:]\s*', '', p)
        # ★ 2026-11-08：过滤 markdown 标题、元信息行
        if p.startswith('#'):
            continue
        if re.match(r'^本工单涉及', p):
            continue
        if len(p) < 2 or len(p) > 60:
            continue
        # 过滤纯数值/键值对（如 RATE=100、TACRANGEINDEX=386）
        if re.match(r'^[A-Z_]+=\S+$', p):
            continue
        # 过滤纯 IP
        if re.match(r'^\d{1,3}(\.\d{1,3}){3}(/\d+)?$', p):
            continue
        # 过滤纯英文标识（无明显中文，且像对象名）
        if re.match(r'^[\x00-\x7F]+$', p) and len(p) < 40:
            continue
        out.append(p)
    return out


def parse_intent_ops(intent_text):
    """从意图文本解析操作清单（纯代码，无 model）。"""
    if not intent_text:
        return {'operations': [], 'source': 'none', 'warnings': []}

    warnings = []

    # ★ 2026-11-08 修 bug：调用方常把「意图 + 业务数据」拼在一起传入，
    #   业务数据里的 markdown 标题和小标题会被当成目标名词解析。
    #   这里先截掉业务数据部分（以「# <工单号> 业务数据」或「## 变更规模」开头）。
    raw = intent_text
    for marker in ('# NC', '## 变更规模', '## 业务标识', '## 域名', '## IP 地址'):
        idx = raw.find(marker)
        if idx > 0 and re.match(r'^# NC\d+ 业务数据', raw[idx:idx + 40]):
            raw = raw[:idx]
            break
    # 兜底：如果出现「## 变更规模」且前面没截，就截到那里
    if '## 变更规模' in raw:
        raw = raw.split('## 变更规模')[0]

    intent_text = raw

    ops_by_verb = {}

    # 找「需要做的变更」段落之后的内容
    m = re.search(r'需要做的变更[：:]\s*(.*)$', intent_text, re.S)
    body = m.group(1) if m else intent_text

    # 切分段落：【删除】...、【新增/修改】...
    # 用 SECTION_RE 定位每个段落标题及其后的内容
    marks = list(SECTION_RE.finditer(body))
    if not marks:
        # 没有【】标记，看有没有「本次变更：...删除 X，新增 Y」这种句式
        m2 = re.search(r'本次变更[：:](.{0,300})', intent_text, re.S)
        if m2:
            seg = m2.group(1)
            for kw, verb in SECTION_VERB.items():
                for mm in re.finditer(kw + r'\s*([^，。；]+)', seg):
                    targets = _split_targets(mm.group(1))
                    if targets:
                        ops_by_verb.setdefault(verb, []).extend(targets)
            if ops_by_verb:
                warnings.append('用「本次变更」句式解析，未经【】段落确认')
        else:
            return {'operations': [], 'source': 'none', 'warnings': ['意图里没有结构化变更描述']}

    # 有【】段落
    for i, mk in enumerate(marks):
        header = mk.group(1)
        start = mk.end()
        end = marks[i + 1].start() if i + 1 < len(marks) else len(body)
        content = body[start:end]

        # 判动词：header 里可能含多个词（如「新增/修改」）
        verbs = set()
        for kw, v in SECTION_VERB.items():
            if kw in header:
                verbs.add(v)
        if not verbs:
            continue

        targets = _split_targets(content)
        if not targets:
            continue

        # ★ 2026-11-08：同时含 ADD 和 MOD 时，合并成 ADD_OR_MOD
        #   原实现会拆成两条（ADD 一份、MOD 一份），清单重复且矛盾。
        #   实际语义：这些对象该新增还是修改，取决于现网有没有，让 agent 判断。
        if verbs == {'ADD', 'MOD'}:
            ops_by_verb.setdefault('ADD_OR_MOD', []).extend(targets)
        else:
            for v in verbs:
                ops_by_verb.setdefault(v, []).extend(targets)

    # 去重保序
    operations = []
    for verb in ('RMV', 'MOD', 'ADD', 'ADD_OR_MOD'):
        if verb not in ops_by_verb:
            continue
        seen = set()
        uniq = []
        for t in ops_by_verb[verb]:
            if t not in seen:
                seen.add(t)
                uniq.append(t)
        operations.append({'verb': verb, 'targets': uniq})

    return {
        'operations': operations,
        'source': 'code' if operations else 'none',
        'warnings': warnings,
    }


def format_ops_text(parsed):
    """把解析结果格式化成给 agent 看的文本（附在意图后面）。"""
    ops = parsed.get('operations') or []
    if not ops:
        return ''

    verb_cn = {'RMV': '删除', 'MOD': '修改', 'ADD': '新增',
               'ADD_OR_MOD': '新增或修改（看现网有没有）'}
    lines = ['', '【操作清单（代码从意图解析，请严格按此动词配置）】']
    for op in ops:
        v = op['verb']
        ts = '、'.join(op['targets'][:20])
        lines.append(f"  {v}（{verb_cn.get(v, v)}）: {ts}")
    lines.append('  ★ 上面这些是【业务描述】，不是 MML 命令族名。')
    lines.append('    你需要结合 EXP 现网已有对象和知识库，自己判断它们对应哪个命令族。')
    lines.append('    动词（RMV/ADD/MOD）照上面用，族名由你判断。')
    lines.append('    不要为了「精确匹配某个族名」反复检索——查 2-3 次仍找不到，')
    lines.append('    就把该项写进方案澄清，说明「业务名词 X 找不到对应命令族」，不要卡住。')
    lines.append('  ⚠ 动词必须照上面用：删除用 RMV，修改用 MOD，新增用 ADD。')
    if any(o['verb'] == 'ADD_OR_MOD' for o in ops):
        lines.append('  ⚠ 标「新增或修改」的项：先查现网有没有该对象，'
                     '有则 MOD，无则 ADD。')
    lines.append('  ⚠ 如果某项在现网不存在而无法配置，请调 clarify 说明，不要自行省略。')
    return '\n'.join(lines)
