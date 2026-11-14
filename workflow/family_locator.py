"""按中文业务词定位 MML 命令族（确定性索引，不依赖向量库）。

★★ 2026-11-14 优化2（用户裁定「先做1和2」）

## 问题

实测 75 单全量：耗时是「固定成本」，与命令数几乎无关。
  GT 1-3 命令:     中位  256s（最长 2403s）
  GT 31-100 命令:  中位 1296s
  GT 101-300 命令: 中位  848s

极端案例 NC20260817001454：GT 只有 3 条命令，阶段1 跑了 2400s 超时。
→ agent 在几十万行的 EXP 里逐个族猜，把时间全耗在探索上。

## 为什么不用 kb_search_feature / kb_search_command(query=...)

两者都走向量检索（pymilvus + 本地 Milvus）。
实测容器内：
  kb_search_feature → Open local milvus failed（不可用）
  kb_search_command(query=) → 能跑但语义不准
    「会话通信计时器」命中的是 DSP MSSCOMMADAPTSERV（不相关）

## 本模块的做法：确定性索引

数据源：/opt/expgv/kb/output_*_mml/mml/MML/Document/*.md（13517 个）
每个文档第一行就是「中文命令名（动词 族名）」：
  # 增加GRE隧道（ADD GRETUNNEL）
  # 设置通用会话管理定时器参数（SET SMCOMMTIMER）
  # 基于APN配置地址分配规则（ADD APNIPALLOCRULE）

实测解析成功 7519 个文档 / 3192 个族。

## 匹配策略（三层，逐层放宽）

  L1 精确子串：意图关键词 ⊂ 文档中文名，或反之
  L2 去虚词后匹配：去掉「设置/配置/的/个/进行」等虚词再比
  L3 三元组相似度：字符 bigram/trigram 重合度 >= 阈值

实测（8 个真实意图词）：
  精确子串命中 2/8；去虚词后 6/8；再加相似度 8/8

## 输出

  [{'family': 'SMCOMMTIMER', 'cn': '设置通用会话管理定时器参数',
    'verbs': ['SET'], 'score': 0.85, 'how': 'L2'}, ...]
  按 score 降序。agent 拿这个列表去 exp_query 核对现网写法。
"""
import glob
import os
import re

# 动作词（中文命令名的前缀）
_VERB_WORDS = ('增加', '添加', '新增', '新建', '创建', '设置', '配置', '修改',
               '删除', '移除', '查询', '激活', '去激活', '锁定', '解锁',
               '复位', '重置', '启动', '停止', '清除', '同步', '加载', '重载')

_VERB_MAP = {
    '增加': 'ADD', '添加': 'ADD', '新增': 'ADD', '新建': 'ADD', '创建': 'ADD',
    '设置': 'SET', '配置': 'SET', '修改': 'MOD', '删除': 'RMV', '移除': 'RMV',
    '查询': 'DSP', '激活': 'ACT', '去激活': 'DEA', '锁定': 'LCK', '解锁': 'ULK',
    '复位': 'RTR', '重置': 'RST', '启动': 'STR', '停止': 'STP',
    '清除': 'CLR', '同步': 'SYN', '加载': 'LOD', '重载': 'RBL',
}

_FIRST_RE = re.compile(
    r'^(.+?)[（(]\s*(ADD|MOD|RMV|SET|ACT|DEA|RTR|RST|STR|STP|CLR|OPR|SYN|LOD|RBL|UPD|LCK|ULK)'
    r'\s+([A-Z][A-Z0-9_]+)\s*[）)]')

# 虚词/泛词：匹配前去掉，避免「设置XX的YY」和「XX YY」对不上
#   ★ 2026-11-14：「参数」不能算虚词（软参数比特位 → 软比特位 反而丢失关键语素）
_STOPWORDS = ('设置', '配置', '进行', '相关', '的', '了', '个', '项',
              '功能', '操作', '使能', '信息')

# 缓存
_INDEX = None


def _strip_stopwords(s):
    out = s
    for w in _STOPWORDS:
        out = out.replace(w, '')
    return out.strip()


def _bigrams(s):
    return {s[i:i + 2] for i in range(len(s) - 1)} if len(s) >= 2 else {s}


def _score(a, b):
    """中文短语的相似度。

    ★ 2026-11-14：纯 bigram Jaccard 对中文业务词太严
      「会话通信计时器」vs「设置通用会话管理定时器参数」：bigram 只有 0.13
      但人看就是同一个东西（都有 会话/定时器）。

    改为「双向 bigram 覆盖率」：
      cover(a→b) = a 的 bigram 有多少出现在 b 里
      cover(b→a) = b 的 bigram 有多少出现在 a 里
      score = max(cover(a→b), cover(b→a)) × 0.7 + 双侧平均 × 0.3
    这样「会话通信计时器」对上面那句：cover(a→b) ≈ 会话/通信/信计/计时/时器
    前两个能命中 → 0.4 左右，加上相似度加权可以过阈值。
    """
    A, B = _bigrams(a), _bigrams(b)
    if not A or not B:
        return 0.0
    inter = len(A & B)
    ca = inter / len(A)
    cb = inter / len(B)
    return 0.7 * max(ca, cb) + 0.3 * ((ca + cb) / 2)


def build_index(kb_root=None):
    """建「族名 → 中文名/动词」索引。

    返回 {fam: {'cn': set(中文名), 'verbs': set(动词), 'doc': 首个文档路径}}
    """
    root = kb_root or os.environ.get('KB_ROOT', '/opt/expgv/kb')
    idx = {}
    seen_docs = set()
    for f in glob.glob(f'{root}/output_*_mml/mml/MML/Document/*.md'):
        base = os.path.basename(f)
        if base in seen_docs:
            continue
        try:
            with open(f, encoding='utf-8', errors='replace') as fh:
                first = fh.readline().strip().lstrip('\ufeff').lstrip('#').strip()
        except Exception:
            continue
        m = _FIRST_RE.match(first)
        if not m:
            continue
        seen_docs.add(base)
        cn, verb, fam = m.group(1).strip(), m.group(2).upper(), m.group(3).upper()
        e = idx.setdefault(fam, {'cn': set(), 'verbs': set(), 'doc': f})
        e['cn'].add(cn)
        e['verbs'].add(verb)
    return idx


def get_index(kb_root=None):
    global _INDEX
    if _INDEX is None:
        _INDEX = build_index(kb_root)
    return _INDEX


def find_families(query, top_k=10, min_score=0.30, kb_root=None):
    """按中文业务词找候选族。

    三层：精确子串 → 去虚词 → bigram 相似度。
    """
    q = str(query or '').strip()
    if not q:
        return []
    idx = get_index(kb_root)
    qs = _strip_stopwords(q)
    hits = []

    for fam, e in idx.items():
        best = 0.0
        how = ''
        best_cn = ''
        for cn in e['cn']:
            # L1 精确子串
            if q in cn or cn in q or (qs and (qs in cn or cn in qs)):
                s, h = 0.95, 'L1'
            else:
                # L2 去虚词
                cs = _strip_stopwords(cn)
                if qs and cs and (qs in cs or cs in qs):
                    s, h = 0.85, 'L2'
                else:
                    # L3 bigram 相似度（双向取大）
                    s = max(_score(qs, cs), _score(q, cn)) if qs else 0.0
                    h = 'L3'
            if s > best:
                best, how, best_cn = s, h, cn

        if best >= min_score:
            hits.append({
                'family': fam,
                'cn': best_cn,
                'verbs': sorted(e['verbs']),
                'score': round(best, 3),
                'how': how,
            })

    hits.sort(key=lambda x: (-x['score'], x['family']))
    return hits[:top_k]


def explain(name):
    """查某族的中文名和动词（供 prompt 说明用）。"""
    idx = get_index()
    e = idx.get(str(name or '').upper())
    if not e:
        return None
    return {'family': name.upper(), 'cn': sorted(e['cn']),
            'verbs': sorted(e['verbs']), 'doc': e['doc']}


if __name__ == '__main__':
    import json
    import sys
    for q in sys.argv[1:]:
        print(f'\n=== {q} ===')
        for h in find_families(q):
            print(f"  {h['family']:<24} {h['score']:.2f} {h['how']}  "
                  f"{h['cn']}  {h['verbs']}")

def annotate_families(families, kb_root=None):
    """给族名列表补上中文名和动词（供 exp_stats 输出「族名 + 中文名」清单）。

    ★ 2026-11-14：这是优化2 的最终方案。
      实测结论：
        · 「业务词 → 族名」用向量检索不可靠（kb_search_command 1/3、
          kb_search_feature→特性→命令 1/3、字符串匹配 5/10）
        · 但「族名 → 中文名」是 100% 可靠的（MML 文档第一行就是
          「# 设置通用会话管理定时器参数（SET SMCOMMTIMER）」）

      所以不要猜，直接给 agent 一份【全族名 + 中文名】清单，
      让它自己用中文名对上意图的业务词。一次 exp_stats 就能拿到，
      比逐个族试快几十倍。

    参数：
      families  族名列表（如 exp_stats 返回的 object_families）
    返回：
      [{'family':..., 'cn': '设置...', 'verbs': ['SET'], 'matched': None}]
    """
    idx = get_index(kb_root)
    out = []
    for f in families:
        name = str(f.get('family') if isinstance(f, dict) else f).upper()
        e = idx.get(name)
        out.append({
            'family': name,
            'cn': sorted(e['cn'])[:2] if e else [],
            'verbs': sorted(e['verbs']) if e else [],
        })
    return out
