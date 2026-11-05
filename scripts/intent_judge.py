#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""意图定位判据（★ 唯一真相源）。

被两方消费：
  1. materials/scripts/intent_precheck.py（运行期：生成前跑，渲染任务书片段）
  2. tools/intent_locate.py（构建期：判别力/泛化验证）

═══ 为什么要有这个模块 ═══
  A 方案落地时，我先在 tools/ 写了判据，又在 scripts/ 写了运行期版本
  → 两份同名函数（norm/lcs_len/classify/best_signal/locate）各写一遍，
    且**逻辑真的分叉了**（如 L>=4 单独成 weak 的分支只在其中一份）
  → 违反「一条主路径、一个真相源，不留并行实现」（用户架构口径）
  → 抽出本模块：判据只有这一份，渲染层/验证层各自 import

═══ 判据本身（LCS + 稀有度双门限）═══
  排除了三个候选（实测都有反例，见下）：
    ✗ 绝对分数（COSINE top1）：真组 0.65-1.00 vs 假组 0.59-0.69 → 完全重叠
      反例：VRF(0.6927) 分比 ULCL(0.6547) 高，但 VRF 是错的
    ✗ 分差 top1-top2：真组 0.0001-0.0948 vs 假组 0.0112-0.0120 → 重叠
      反例：ULCL 分差 0.0001（几乎平局）却是对的
    ✗ 字面重合度 2-gram：真组 0.074-1.0 vs 假组 0.0-0.222 → 重叠
  采用：LCS（最长**连续**公共子串）+ 稀有度 R 双门限
    · 纯字符串比对、不调模型 ⇒ 天然确定、毫秒级、可复现

★ 设计纪律（写死在这里，避免各处解释不一致）：
  · 判据是**加速器不是闸门** —— strong 档也允许 agent 推翻
  · weak/none 档**不能据此拒绝** —— 交 agent 语义判断（避免误杀）
  · 任何异常都降级为「无定位」（等同现状行为），绝不阻塞生成
"""
import re

# 停用词：出现在特性名里但不构成「定位信号」的词
# ★ 必须跳过 —— 否则「配置XXX」永远命中的是「配置」（实测：若不跳，
#   '配置手机上网' 会得到 weak 档，属假阳性）
STOP_GRAM = {
    '配置', '激活', '支持', '功能', '数据', '业务', '模式', '查询',
    '管理', '设置', '修改', '删除', '调整', '基于', '进行', '用户',
    '接口', '地址', '网络', '状态', '信息', '参数', '设备', '服务',
}

# 双门限（实测标定，改任一个都会破坏判别力 —— 见 tools/intent_locate.py 的反例守卫）
TH_STRONG_L = 6      # L ≥ 6 → strong
TH_MID_L = 4         # L ≥ 4 且 R ≤ TH_MID_R → strong
TH_MID_R = 20
TH_SHORT_L = 2       # L = 2,3 且 R ≤ TH_SHORT_R → weak
TH_SHORT_R = 3

# Milvus 默认路径（运行期由调用方按需覆盖）
MILVUS_URI = '/opt/expgv/milvus-seed/milvus_mml.db'


def norm(s):
    """归一化：去引号/括号/标点/空白（特性名和意图都要过这一步）"""
    return re.sub(r'[“”"\'（）()【】\[\]，,。;；:：\s]', '', s or '')


def lcs_len(a, b):
    """最长**连续**公共子串长度 + 子串本身 → (len, sub)"""
    a, b = norm(a), norm(b)
    if not a or not b:
        return 0, ''
    best, bl = 0, ''
    for i in range(len(a)):
        for j in range(len(b)):
            k = 0
            while i + k < len(a) and j + k < len(b) and a[i + k] == b[j + k]:
                k += 1
            if k > best:
                best, bl = k, a[i:i + k]
    return best, bl


def classify(L, R):
    """判据核心：L 与 R 双门限。

    ★ 为什么双门限而不是单一阈值：
      · "配置ULCL分流" → L=6 少字但极长，R=1  → 无需看 R
      · "ULCL"         → L=4 短，但 R=1 极独特 → 靠 R 救回
      · "配置"         → L=2 且 R=194 泛滥     → 必须拒绝
    单一阈值无法同时容纳前两者、拒绝第三者（实测出来的结构）。
    """
    if L == 0:
        return 'out_of_scope'
    if L >= TH_STRONG_L:
        return 'strong'
    if L >= TH_MID_L and R <= TH_MID_R:
        return 'strong'
    if L >= TH_MID_L:
        return 'weak'
    if L >= TH_SHORT_L and R <= TH_SHORT_R:
        return 'weak'
    return 'none'


def best_signal(intent, titles):
    """在特性名集合里找最强定位信号。

    返回 (L, 子串, 稀有度R, 命中特性名)
    """
    best = (0, '', 10 ** 9, '')
    for t in titles:
        n, sub = lcs_len(intent, t)
        if n < 2:
            continue
        if sub in STOP_GRAM:
            continue
        rare = sum(1 for x in titles if sub in norm(x))
        # 评优：先比 L（大者优），同 L 比 R（小者优）
        if (n, -rare) > (best[0], -best[2]):
            best = (n, sub, rare, t)
    return best


def locate(intent, titles):
    """主入口：意图 → 定位结果 dict"""
    if not titles:
        return {'verdict': 'no_titles', 'L': 0, 'sub': '', 'R': -1, 'match': '',
                'note': '特性名集合为空'}
    L, sub, R, match = best_signal(intent, titles)
    v = classify(L, R)
    note = {
        'strong': '定位明确，可直接按此特性生成（无需检索探索）',
        'weak': '有弱信号，但不足以定位 —— 交给 agent 做语义判断',
        'none': '无定位信号 —— 交给 agent 判断（可能需引导或换说法）',
        'out_of_scope': '意图与任何特性名均无 ≥2 字连续重叠 —— 可能超出范围或需换说法',
    }.get(v, '')
    return {'verdict': v, 'L': L, 'sub': sub, 'R': R, 'match': match, 'note': note}


def load_titles(product, uri=None):
    """从 Milvus mml_feature 取特性名集合（权威源，600 条/UEG）"""
    import pymilvus
    c = pymilvus.MilvusClient(uri=uri or MILVUS_URI)
    c.load_collection('mml_feature')
    flt = f'product == "{product}"' if product else ''
    out, seen = [], set()
    for x in c.query('mml_feature', filter=flt,
                     output_fields=['feature_name'], limit=2000):
        n = x.get('feature_name', '')
        if n and n not in seen:
            seen.add(n)
            out.append(n)
    return out
