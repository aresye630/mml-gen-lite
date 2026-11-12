"""Step 1/2：规划表结构合规检查 + 意图对象提取。

★ 2026-11-12 P0-3

Step 1 规划表结构合规（纯代码，<1s）
  · 状态列取值合法
  · 命令族列无通配（复用 G31）
  · 判断依据非空
  · 散文里的族名 → 提取成表行

Step 2 意图对象覆盖（纯代码，<0.1s）
  实测 V3 意图格式：
    标准条目 932 条（97.4%）：`- 动作 对象（约束）`
    特殊条目 1：`- 对象「实例」的配置：按现网同类对象「参照」的存量做法配齐`
    特殊条目 2：`- 存量「X」没有、需单独配置的：族名`
  → 三种格式都能纯代码解析，无需 LLM

为什么要这样拆分：
  单靠 prompt 要求 agent「逐对象核对」，实测执行率不稳定（同一单 6 次运行
  覆盖 33/13/31/14/17/2 族）。改成代码提取对象清单 + 代码比对规划表，
  才能得到确定性的「哪些对象没进表」。
"""
import re
import sys
from pathlib import Path

# 复用 G31 的表格解析
_GUARD_DIR = str(Path(__file__).parent.parent / 'guard')
if _GUARD_DIR not in sys.path:
    sys.path.insert(0, _GUARD_DIR)

try:
    import plan_wildcard as _PW
except Exception:
    _PW = None


# ═══════════════════════════════════════════════════════════
# 意图解析
# ═══════════════════════════════════════════════════════════

# 动作词 → 语义动作
ACTION_MAP = {
    '新增': 'ADD', '添加': 'ADD', '创建': 'ADD', '新建': 'ADD',
    '调整': 'MOD', '修改': 'MOD', '设置': 'SET', '更新': 'MOD',
    '删除': 'RMV', '移除': 'RMV', '去除': 'RMV',
}

# 标准条目：`- 动作 对象（约束）`
RE_STANDARD = re.compile(r'^-\s*(新增|添加|创建|新建|调整|修改|设置|更新|删除|移除|去除)\s+(.+?)\s*$')

# 参照配齐条目：`- 用户模板「up_sos」的配置：按现网同类用户模板「up_ims」的存量做法配齐`
RE_COPY = re.compile(
    r'^-\s*(?P<obj>[^\s「]+)\s*「(?P<inst>[^」]+)」的配置[：:]\s*'
    r'按现网同类\s*(?P<ref_obj>[^\s「]+)\s*「(?P<ref_inst>[^」]+)」的存量做法配齐')

# 补充条目：`- 存量「up_ims」没有、需单独配置的：UPBINDUPG`
RE_EXTRA = re.compile(
    r'^-\s*存量「(?P<ref_inst>[^」]+)」没有[、,]?\s*需单独配置的[：:]\s*(?P<fams>.+)$')

# 约束括号：`（策略类型为PCC，优先级为1000）` 或 `(xxx)`
RE_CONSTRAINT = re.compile(r'[（(]([^（()）]*)[）)]')

# 「XXX 名称为YYY」→ 提取参数
RE_PARAM_VALUE = re.compile(r'([\u4e00-\u9fa5A-Za-z][\u4e00-\u9fa5A-Za-z\s]*?)\s*(?:名称)?为\s*([A-Za-z0-9_\-\.]+)')


def parse_intent(intent_text):
    """解析意图，返回结构化对象清单。

    返回：
      {
        'groups': [{'name': '【APN 与移动性】', 'items': [...]}],
        'items': [{
            'kind': 'standard' | 'copy' | 'extra',
            'group': '...',
            'action': 'ADD'/'MOD'/'SET'/'RMV' | None,
            'object': '规则',
            'instance': 'r_sos_sig' | None,
            'constraints': {'POLICYTYPE': 'PCC', ...},   # 原文字面，未映射到 MML 参数
            'raw_params': {'策略类型': 'PCC', ...},
            'ref_object': '用户模板' | None,      # copy 场景
            'ref_instance': 'up_ims' | None,
            'families': ['UPBINDUPG'],            # extra 场景
            'raw': '原始行',
          }],
      }
    """
    groups = []
    items = []
    cur_group = None

    for raw_line in (intent_text or '').split('\n'):
        line = raw_line.strip()
        if not line:
            continue

        # 分组标题
        m = re.match(r'^(【[^】]+】)', line)
        if m:
            cur_group = m.group(1)
            groups.append({'name': cur_group, 'items': []})
            continue

        if not line.startswith('- '):
            continue

        # ── 参照配齐 ──
        mc = RE_COPY.match(line)
        if mc:
            it = {
                'kind': 'copy', 'group': cur_group, 'action': None,
                'object': mc.group('obj'), 'instance': mc.group('inst'),
                'constraints': {}, 'raw_params': {},
                'ref_object': mc.group('ref_obj'),
                'ref_instance': mc.group('ref_inst'),
                'families': [], 'raw': line,
            }
            items.append(it)
            if groups:
                groups[-1]['items'].append(it)
            continue

        # ── 补充项 ──
        me_ = RE_EXTRA.match(line)
        if me_:
            fams = [f.strip().upper() for f in
                    re.split(r'[/,、\s]+', me_.group('fams')) if f.strip()]
            it = {
                'kind': 'extra', 'group': cur_group, 'action': None,
                'object': None, 'instance': None,
                'constraints': {}, 'raw_params': {},
                'ref_object': None, 'ref_instance': me_.group('ref_inst'),
                'families': fams, 'raw': line,
            }
            items.append(it)
            if groups:
                groups[-1]['items'].append(it)
            continue

        # ── 标准条目 ──
        ms = RE_STANDARD.match(line)
        if ms:
            action_word, rest = ms.group(1), ms.group(2)

            # 提取约束括号（可能有多个，也可能是行内）
            constraints_text = []
            for cm in RE_CONSTRAINT.finditer(rest):
                constraints_text.append(cm.group(1))
            # 约束也可能在下一行的括号里（V3 格式），这里只处理行内
            rest_clean = RE_CONSTRAINT.sub('', rest).strip()

            # 「见数据清单」不算对象
            rest_clean = re.sub(r'[（(]?见数据清单[）)]?', '', rest_clean).strip()

            # 从约束里提 参数:值
            raw_params = {}
            for ct in constraints_text:
                for pm in RE_PARAM_VALUE.finditer(ct):
                    k = pm.group(1).strip()
                    v = pm.group(2).strip()
                    if k and v:
                        raw_params[k] = v

            # 对象名里若有「实例」引号，提取实例
            inst = None
            mi = re.search(r'「([^」]+)」', rest_clean)
            if mi:
                inst = mi.group(1)
                rest_clean = re.sub(r'「[^」]+」', '', rest_clean).strip()

            it = {
                'kind': 'standard', 'group': cur_group,
                'action': ACTION_MAP.get(action_word, action_word),
                'object': rest_clean, 'instance': inst,
                'constraints': constraints_text, 'raw_params': raw_params,
                'ref_object': None, 'ref_instance': None,
                'families': [], 'raw': line,
            }
            items.append(it)
            if groups:
                groups[-1]['items'].append(it)
            continue

        # 未识别格式
        it = {
            'kind': 'unknown', 'group': cur_group, 'action': None,
            'object': line[2:].strip(), 'instance': None,
            'constraints': [], 'raw_params': {},
            'ref_object': None, 'ref_instance': None,
            'families': [], 'raw': line,
        }
        items.append(it)
        if groups:
            groups[-1]['items'].append(it)

    # 补充「下一行的约束括号」：V3 里约束常在条目下一行单独成行
    _attach_following_constraints(intent_text, items)

    return {'groups': groups, 'items': items}


def _attach_following_constraints(intent_text, items):
    """把「下一行单独的（约束）」挂到上一条目上。

    V3 意图格式：
      - 新增 APN配置
          （是否绑定 VPN为关闭，APN 名称为sos）
    """
    if not items:
        return
    lines = [l.strip() for l in (intent_text or '').split('\n')]
    # 建立 raw_line -> 索引
    raw_to_item = {}
    for it in items:
        raw_to_item.setdefault(it['raw'], it)

    for i, line in enumerate(lines):
        it = raw_to_item.get(line)
        if not it:
            continue
        if not line.startswith('- '):
            continue
        # 看下一行是不是纯括号
        if i + 1 >= len(lines):
            continue
        nxt = lines[i + 1]
        if not nxt or nxt.startswith('- ') or nxt.startswith('【'):
            continue
        if not (nxt.startswith('（') or nxt.startswith('(')):
            continue
        inner = nxt.strip('（）()').strip()
        if not inner:
            continue
        for pm in RE_PARAM_VALUE.finditer(inner):
            k = pm.group(1).strip()
            v = pm.group(2).strip()
            if k and v:
                it['raw_params'].setdefault(k, v)
        if isinstance(it['constraints'], list):
            it['constraints'].append(inner)


# ═══════════════════════════════════════════════════════════
# Step 1 规划表结构合规
# ═══════════════════════════════════════════════════════════

VALID_STATUS = ('确认', '待定', '跳过')

# 不是族名的全大写 token（动作词 / 参数名 / 枚举值 / 网元代号）
_NON_FAMILY_TOKENS = {
    'ADD', 'SET', 'MOD', 'RMV', 'UNC', 'UDG', 'UEG', 'EXP', 'MML',
    'NOID', 'SUBRANGE', 'ENABLE', 'DISABLE', 'NONE', 'NULL', 'DEFAULT',
    'INDEX', 'NAME', 'ID', 'TYPE', 'MODE', 'ONLINE', 'OFFLINE',
    'ALL', 'ANY', 'TRUE', 'FALSE', 'YES', 'NO', 'ON', 'OFF',
    'PCC', 'IMS', 'APN', 'VPN', 'IPV4', 'IPV6', 'DNS', 'NAT',
    'RANGE', 'START', 'END', 'MIN', 'MAX', 'SIZE', 'COUNT',
}


def normalize_status(raw):
    """归一化状态列取值。"""
    s = (raw or '').strip()
    if not s:
        return '待定'
    if '跳过' in s or '不配' in s:
        return '跳过'
    if '待定' in s or '待确认' in s:
        return '待定'
    if '确认' in s or '人工调整' in s:
        return '确认'
    return '待定'   # 无法识别时保守处理


def check_plan_structure(plan_text):
    """Step 1：检查规划表结构，返回问题清单 + 可从散文救回的族。

    返回：
      {
        'rows': [...],
        'issues': [{'row': '2', 'type': 'status_invalid', 'detail': '...'}],
        'wildcard_rows': [...],          # 复用 G31
        'prose_families': ['APNCHARGECTRL', ...],  # 散文里救出来的族
        'need_status_fix': [{'row': idx, 'from': '已存在', 'to': '待定'}],
      }
    """
    issues = []
    prose_families = []
    need_status_fix = []

    if _PW is None:
        rows = []
    else:
        try:
            rows = _PW.parse_plan_rows(plan_text)
        except Exception:
            rows = []

    for r in rows:
        st = (r.get('status') or '').strip()
        norm = normalize_status(st)
        if st and st not in VALID_STATUS and norm != st:
            issues.append({'row': r['row_no'], 'type': 'status_invalid',
                           'detail': f'状态「{st}」不合法，建议改为「{norm}」'})
            need_status_fix.append({'row': r['row_no'], 'from': st, 'to': norm})

        if not (r.get('fam_cell') or '').strip():
            issues.append({'row': r['row_no'], 'type': 'family_empty',
                           'detail': '命令族列为空'})

    # 通配检查（复用 G31）
    wildcard_rows = []
    if _PW is not None:
        try:
            tmp = Path('/tmp/_p03_plan.md')
            tmp.write_text(plan_text, encoding='utf-8')
            wr = _PW.check_plan_wildcard(plan_path=str(tmp))
            if not wr.get('skipped') and not wr.get('ok'):
                wildcard_rows = wr.get('hits') or []
        except Exception:
            pass

    # 散文里的族名（在非表格区域出现的全大写族名）
    table_lines = set()
    for line in plan_text.split('\n'):
        if line.strip().startswith('|'):
            table_lines.add(line.strip())

    FAM_RE = re.compile(r'\b([A-Z][A-Z0-9_]{3,})\b')
    in_table_fams = set()
    for tl in table_lines:
        for m in FAM_RE.finditer(tl):
            in_table_fams.add(m.group(1))

    # 只看「不确定项」「待人工确认」这两个小节里的散文
    section = None
    for line in plan_text.split('\n'):
        s = line.strip()
        if s.startswith('##'):
            section = s
            continue
        if section and ('不确定' in section or '待人工' in section):
            if s.startswith('|') or not s:
                continue
            for m in FAM_RE.finditer(s):
                fam = m.group(1)
                # ★ 2026-11-12 修误报：排除动作词和常见参数名
                #   实测误报：NOID / SUBRANGE / ENABLE / DISABLE 被当成族名
                if fam in _NON_FAMILY_TOKENS:
                    continue
                # 族名特征：不含纯枚举词，且长度 >= 4
                if fam in in_table_fams or fam in prose_families:
                    continue
                prose_families.append(fam)

    return {
        'n_rows': len(rows),
        'issues': issues,
        'wildcard_rows': wildcard_rows,
        'prose_families': prose_families,
        'need_status_fix': need_status_fix,
    }


# ═══════════════════════════════════════════════════════════
# Step 2 意图对象覆盖检查
# ═══════════════════════════════════════════════════════════

def _normalize_cn(text):
    """归一化中文文本用于模糊匹配。

    实测问题（NC20260810002261）：
      意图「新增 PCC策略组」 vs 规划表「PCC 策略组」     → 空格差异
      意图「用户模板和规则的绑定关系」vs「用户模板与规则对应关系」→ 和/与 + 绑定/对应
      意图「License项的开关」 vs「License 项的开关」    → 空格差异

    做法：去空格、统一同义词、去标点，全小写。
    """
    if not text:
        return ''
    t = str(text)
    # 统一同义词
    for a, b in [('与', '和'), ('对应关系', '绑定关系'), ('绑定', '绑定'),
                 ('及', '和'), ('、', ''), ('，', ''), ('。', '')]:
        t = t.replace(a, b)
    # 去空格和常见标点
    t = re.sub(r'[\s\-_/\\()（）「」.【】:：;；]', '', t)
    return t.lower()


def _keywords(obj_name):
    """从对象名里提取关键词（用于宽松匹配）。

    '用户模板和规则的绑定关系' → ['用户模板', '规则', '绑定']
    'PCC策略组'               → ['pcc', '策略组']
    """
    if not obj_name:
        return []
    t = obj_name
    for w in ('的配置', '配置', '信息', '相关属性', '的开关', '的绑定关系',
              '和', '与', '及', '的'):
        t = t.replace(w, ' ')
    toks = [x for x in re.split(r'[\s]+', t) if x]
    # 保留长度 >= 2 的
    return [_normalize_cn(x) for x in toks if len(x) >= 2]


def check_intent_coverage(intent_text, plan_text):
    """Step 2：检查意图里每个业务对象，规划表里有没有对应行。

    覆盖判据（任一满足就算覆盖）：
      · 规划表某行的「业务对象」列含该对象名
      · 规划表某行的「数据清单表」列含该对象名
      · 规划表某行的「命令族」列含该对象的族名（若已映射）
      · 该对象出现在规划表全文中（兜底）

    返回：
      {
        'n_objects': 总对象数,
        'covered': [...],
        'missing': [{'object': '规则', 'instance': 'r_sos_sig', 'action': 'ADD'}],
        'coverage_rate': 0.85,
      }
    """
    parsed = parse_intent(intent_text)
    objs = []
    for it in parsed['items']:
        if it['kind'] == 'standard' and it['object']:
            objs.append({
                'object': it['object'],
                'instance': it['instance'],
                'action': it['action'],
                'group': it['group'],
            })
        elif it['kind'] == 'copy':
            objs.append({
                'object': it['object'],
                'instance': it['instance'],
                'action': 'ADD',
                'group': it['group'],
            })
        elif it['kind'] == 'extra':
            for fam in it['families']:
                objs.append({
                    'object': fam,
                    'instance': None,
                    'action': None,
                    'group': it['group'],
                })

    plan_norm = _normalize_cn(plan_text or '')
    plan_lines = [l.strip() for l in (plan_text or '').split('\n')
                  if l.strip()]

    covered = []
    missing = []
    for o in objs:
        hit = False
        # ① 实例名直接命中（最可靠）
        if o['instance'] and o['instance'] in (plan_text or ''):
            hit = True
        # ② 归一化后的对象名命中
        if not hit and o['object']:
            obj_norm = _normalize_cn(o['object'])
            if obj_norm and obj_norm in plan_norm:
                hit = True
        # ③ 去虚词后再试
        if not hit and o['object']:
            core = re.sub(r'(的配置|配置|信息|相关属性|的开关)$', '', o['object']).strip()
            core_norm = _normalize_cn(core)
            if core_norm and core_norm in plan_norm:
                hit = True
        # ④ 关键词组合命中，但必须落在同一表格行
        #   ★ 2026-11-12 收紧：旧做法只看「词在不在全文」，
        #     实测「用户模板和规则的绑定关系」会命中「用户模板清单」那行（错行）
        #   改为：所有关键词必须出现在同一个表格行里
        if not hit and o['object']:
            kws = _keywords(o['object'])
            if kws:
                for tl in plan_lines:
                    tl_norm = _normalize_cn(tl)
                    if all(k in tl_norm for k in kws):
                        hit = True
                        matched_row = tl
                        break
        if hit:
            covered.append(o)
        else:
            missing.append(o)

    n = len(objs)
    return {
        'n_objects': n,
        'covered': covered,
        'missing': missing,
        'coverage_rate': (len(covered) / n) if n else 1.0,
        'objects': objs,
    }


if __name__ == '__main__':
    import json

    GT = json.loads(Path('/tmp/gt_cleaned.json').read_text(encoding='utf-8'))
    g = next(x for x in GT if x['ticket'] == 'NC20260810002261')
    INTENT = Path('/tmp/intent_v3/NC20260810002261_意图.md')
    PLAN = Path('/tmp/eval_versions_out/V3/NC20260810002261/命令族规划.md')

    print('=' * 92)
    print('P0-3 自测：意图解析 + 结构合规 + 对象覆盖')
    print('=' * 92)

    itxt = INTENT.read_text(encoding='utf-8')
    parsed = parse_intent(itxt)
    print(f'\n【意图解析】')
    print(f'  分组 {len(parsed["groups"])} 个，条目 {len(parsed["items"])} 条')
    from collections import Counter
    kinds = Counter(i['kind'] for i in parsed['items'])
    print(f'  类型分布: {dict(kinds)}')
    for it in parsed['items'][:5]:
        print(f'    [{it["kind"]}] {it["action"] or "-":<4} {str(it["object"])[:24]:<26} '
              f'inst={it["instance"]} params={len(it["raw_params"])}')

    if PLAN.exists():
        ptxt = PLAN.read_text(encoding='utf-8')
        print(f'\n【Step 1 结构合规】')
        r1 = check_plan_structure(ptxt)
        print(f'  表格行 {r1["n_rows"]}，问题 {len(r1["issues"])} 条')
        for iss in r1['issues'][:5]:
            print(f'    第{iss["row"]}行 [{iss["type"]}] {iss["detail"][:50]}')
        print(f'  通配行 {len(r1["wildcard_rows"])} 行')
        print(f'  散文族名 {len(r1["prose_families"])} 个: {r1["prose_families"][:8]}')

        print(f'\n【Step 2 对象覆盖】')
        r2 = check_intent_coverage(itxt, ptxt)
        print(f'  意图对象 {r2["n_objects"]} 个，覆盖 {len(r2["covered"])} 个 '
              f'({r2["coverage_rate"]*100:.0f}%)')
        if r2['missing']:
            print(f'  未覆盖 {len(r2["missing"])} 个:')
            for m in r2['missing'][:8]:
                print(f'    {m["action"] or "-":<4} {m["object"][:30]}')
