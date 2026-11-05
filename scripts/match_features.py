#!/usr/bin/env python3
"""特性匹配 T3：指纹库 × exp 索引 → 二分判定 + 归因 + 反向审计

治理前置后的匹配器：不做全量 991×N 两两对比。
- exp 侧建三类 O(1) 索引：命令类型 / 锚定参数值 (cmd,param)→values / 授权值
- 每特性按指纹查询（二分判定）：
    core L1/L3 类型命中 + L2 值锚定命中 → 已配置
    core 空且 license 非空（授权类特性）→ license 值锚定命中 → 已配置
    无 core 无 license（纯操作类）→ 需人工（无法命令判定）
    其余 → 未配置 + 归因（授权在/部分命中/缺项清单，信息不丢）
- 反向审计：exp 中未收录命令类型 → 候选新特性（前缀聚族）

用法:
  python3 match_features.py --feat-md <特性文档库> --fingerprint rules/features.yaml \
      --anchors rules/param_anchor.yaml --exp <exp.txt> -o <输出目录>
"""
import argparse
import json
import os
import re
import sys
import time
from collections import Counter, defaultdict, deque
from functools import lru_cache
from pathlib import Path

import yaml

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_feature_all as gfa  # noqa: E402

QUERY_PREFIXES = ('DSP', 'LST', 'SHOW', 'CHK', 'EXP')
# 授权/开关类命令（license 字段的 key 来源，值锚定 LICITEM 等）
LIC_CMD_PREFIXES = ('SET LICENSESWITCH', 'SET SOFTPARA')
# 版本对偶族：文档示例只演示一个版本时，局点用对偶版本 = 业务等价变体
# （接口族 F001~F005：文档示例 IPV4、局点全 IPv6 双栈/纯 v6，且无独立 IPv6 指纹）
# T0 值核对判 mismatch 前先查对偶；对偶值记 notes 注记，不降级。
DUAL_PAIRS = {'IPV4': {'IPV6'}, 'IPV6': {'IPV4'}, 'IPV4V6': set(),
              'IPV4UNI': {'IPV6UNI'}, 'IPV6UNI': {'IPV4UNI'},
              'IPV4UNI_IPV6UNI': set(), 'IPV6MULTI': set()}
MASK_RE = re.compile(r'^\*+$')
# 锚点出发的汇聚阈值：leaf_chain 默认 OBJ_THRESH=5 会把「锚点被大量 binding 引用」
# 这类真实多引用（如 USERPROFILE 挂 668 条 RULEBINDING）误折叠漏链；从锚点出发时
# 用较高阈值走全 core（含 URR/PROTBINDFLOWF）又不过度膨胀共享对象（FILTER 等）。
ANCHOR_OBJ_THRESH = 15

# ★ 性能修复（2026-10-28）：单次 build_leaf_instances 内的链节点预算。
#   实测 35MB EXP（24 万条命令）：单个慢特性会调 walk_chain 1500+ 次，
#   每次扩散到 62,497 个节点、耗时 3.5 秒 ⇒ 单特性 100 分钟。
#   根因：FLOWFILTERNAME 有 13,571 个唯一值、每个只被引用 2~5 次，
#   都低于 ANCHOR_OBJ_THRESH=15 ⇒ 折叠规则对「海量小值」无效，全部入队。
#   预算制：累计入链节点超限后停止后续 seed_item 的链遍历（已有 chain 保留）。
#   ⚠ 影响量化（17.5MB 工单实测）：耗时 1498s → 191s（7.9×），
#     435 个特性的 status **零变化**，全局 hit 326,588 → 326,584（-4 条，0.0012%），
#     差异集中在 4 个 https 公共实例各少 1 条 ADD RULE —— 可接受。
CHAIN_NODE_BUDGET = 5000
# 共享池判定阈值（用户拍板）：core 命令在实例链上的覆盖比例低于此值（少数实例），
# 且 exp 条数 >= 覆盖实例数 × SHARED_EXP_MULT（全局共享池而非逐实例专属链），
# 则该命令特性级存在即命中，不逐实例校验。
SHARED_COVER_RATIO = 0.2
SHARED_EXP_MULT = 10

# ═══ 公共对象判据（2026-10-18 裁决：按比例，不用绝对值）══════════════════
# 某命令被多少个特性的指纹 core 引用 ⇒ 跨特性引用数。超过阈值即视为"公共底座"：
# 它单独命中不足以证明"配了本特性"（只能证明 exp 里有这个底座）。
#
# 依据（实测）：UEG 1294 特性中 ADD VPNINSTAF 被 202 个特性引用（15.6%）、
# BGPPEER/BGPVRFAF 各 114（8.8%）、IMPORTROUTE 108（8.3%）。这些命令当锚点种子
# 是对的（实例建模基准），但当命中证据是错的。
#
# 阈值 = max(PUBLIC_RATIO × 本产品特性数, PUBLIC_MIN)
#   · 比例：UEG 1294→65 / UDG 435→22 / UNC 609→31（自动适应产品规模）
#   · 下限 20：防止小产品（如 100 个特性）把 5 个特性共享的命令误判成公共
PUBLIC_RATIO = 0.05
PUBLIC_MIN = 20
# 全局缓存（main() 建一次；judge_instances 查表 O(1)，不增加判定复杂度）
_GLOBAL_CORE_USE = {}      # cmd -> 跨特性引用数
_GLOBAL_FEAT_N = {}        # {'n': 特性总数}
# 实例成员归属倒排（方案 C：绑定即归属）
#   值 -> 该值出现的行里"其余名字值"集合（即它引用的下游对象）
#   例：FLTBINDFLOWF(FLOWFILTERNAME="any_f_f", FILTERNAME="any")
#         ⇒ refs["any_f_f"] ⊇ {"any"}，refs["any"] ⊇ {"any_f_f"}
#   用途：实例 K 收成员时，从 K 的直接成员出发，把"被它们引用的名字值"也纳入
_GLOBAL_VAL_REFS = {}
# 实例成员归属的最大引用跳数（2026-10-18 实测定的）
#   1 跳 = any_f_f → {any, cbnet_any}
#   2 跳 = + {u_p_cbn_cbnet}（rule 绑定的用户）
#   ≥3 跳会跨到别人实例（实测 15 行里混进 5 条别人实例的 SET URRGRPBINDING）
#   ⇒ 取 2。这是常量不是开关（不做成 CLI 参数，避免"多一个旋钮"）。
MAX_HOPS = 2
# Z1 分支阈值：实例"自己的直接成员行"（带锚点==key 的行）≤ 该值时，才允许追下游。
# 取 1 的依据（三产品实测）：
#   · F033/F034 这类"策略祖先"实例只有 1 行自己的证据（PCCPOLICYGRP 本身），
#     其余全在下游链上 ⇒ 必须追
#   · F881 这类实例有 3 行以上自己的证据 ⇒ 用 1 跳即可，不会串味
# 0 时 F033 修不好；≥2 时代价上升（UEG +21.7%）。1 是两全点。
DIRECT_MAX = 1
# BFS 追下游时的 owned 集合上限（防"超级 hub"爆炸，实测 UDG 事故）
#   UDG 13 个 hub 值（如 yksp_00_f_f 连 4891 个邻居）BFS 可达 49,745 个值 ≈ 整张图，
#   导致 15s → 76s。取 2000：正常链（F033 那条 48 个值）远低于此，
#   hub 爆炸会立刻触发并退回 1 跳。
OWNED_CAP = 2000
# 锚点参数别名（**自动推导**，不手写清单）
#   同一对象概念在 MML 里可能有多个参数名：
#     · F086 锚点 VRFNAME，但 ADD AUTOSCALINGSERVICE 用 VPNNAME
#     · F474 锚点 VPNINSTANCE，但 ADD VPNINSTAF 用 VRFNAME
#   手写映射只能覆盖见过的（实测漏了两个），所以改成**运行期按值域自动发现**：
#     实例 key 集合 ∩ 某参数名的值集合 ≠ ∅  ⇒ 该参数名与锚点同域 ⇒ 视为锚点别名。
#   这不是开关也不是硬编码，是从数据里长出来的（_discover_anchor_aliases）。
_ANCHOR_ALIASES = {}
# 只认这些"名字类"参数做归属判定（其余参数含小写也可能是描述文本，不放进来）
_NAME_LIKE_SUFFIX = ('NAME', 'INST', 'NM')
_NAME_LIKE_EXACT = ('VRFNAME', 'IFNAME', 'APN', 'DNN')
# 自定义值判定：含小写字母或点（对象名/IP），排除纯数字与全大写枚举
#   （与 leaf_chain.is_name_value 同口径 —— 那边是链遍历的判断，这里保持一致）
_NAMEV_RE = re.compile(r'[a-z.]')


def _is_name_param(p: str) -> bool:
    return p.endswith(_NAME_LIKE_SUFFIX) or p in _NAME_LIKE_EXACT


def _discover_anchor_aliases(anchor, keys):
    """从数据自动发现"与锚点同值域"的参数名（锚点别名）。

    判据（纯编码，零硬编码）：某名字类参数 param ≠ anchor，若它出现的值里有
    **至少 2 个**同时是实例 key 集合的元素 ⇒ 该参数与锚点指同一类对象 ⇒ 视为别名。

    为什么要自动发现（实测 2026-10-18 踩坑）：
      · F086 锚点 VRFNAME，成员命令 ADD AUTOSCALINGSERVICE 用的是 VPNNAME
      · F474 锚点 VPNINSTANCE，成员命令 ADD VPNINSTAF 用的是 VRFNAME
      手写映射表只覆盖见过的，两个都漏了 ⇒ 别人的行混进实例。
    为什么不认"所有名字类参数"：那会把 FILTERNAME 之类无关参数也当锚点，
    导致真正的跨实例串味被放过（实测：VPNNAME="CBN_SG" 溜进 CBN_GRE 实例）。

    ⚠ 复杂度：每个 (锚点) 只算一次并缓存到 _ANCHOR_ALIASES；
    扫描范围是 _GLOBAL_INST_BY_SEQ（O(N)），判定时查表 O(1)。
    """
    if not keys:
        return ()
    key_set = set(keys)
    hits = defaultdict(int)
    for _seq, (_cmd, params) in _GLOBAL_INST_BY_SEQ.items():
        for p, v in params.items():
            if p == anchor or not _is_name_param(p) or not v:
                continue
            if str(v) in key_set:
                hits[p] += 1
    # 至少 2 次命中才认（1 次可能是巧合撞名）
    return tuple(sorted(p for p, n in hits.items() if n >= 2))


def _narrow_instance_members(instances, anchor):
    """按"引用链归属"收窄实例成员（2026-10-18 用户口径，方案 C）。

    核心判据：**本实例引用了它，它就是本实例的**（绑定即归属）。
    一条命令行属于实例 K，当且仅当：
      ① 它带锚点参数 anchor 且值 == K                       → 收（K 的直接成员）
      ② 它带锚点参数但值 ≠ K                                → 不收（别的实例）
      ③ 它不带锚点，但它的名字值**被 K 的成员命令引用过**     → 收（K 的下游对象）
         例：any_f_f 有 `FLTBINDFLOWF:FLOWFILTERNAME="any_f_f", FILTERNAME="any"`
             ⇒ "any" 被 any_f_f 引用 ⇒ `ADD FILTER:FILTERNAME="any"` 属于 any_f_f
         同一对象被多个实例引用时（any 同时被 any_f_f 与 stop_service_any_f_f 引用）
         **两边都算**——它确实同时是两个实例的成员，不是二选一。
      ④ 不带锚点、名字值**没有被 K 的成员引用过**            → 不收（与 K 无关）

    与前一版（"全局唯一才收"）的区别：前一版把 `any` 判成公共对象剔掉，
    导致 any_f_f 丢了 ADD FILTER ⇒ F881 九个实例全掉 partial。
    用户裁决（2026-10-18）：「any 应该算 any_f_f 的成员」⇒ 改成绑定即归属。

    为什么要这个：链遍历会经多对多桥（ADD RULEBINDING 一条挂 5 个业务用户）
    把别人的命令拉进来 —— 实测 F881 每个实例都装了全 exp 的 21 条 ADD FILTER。

    ⚠ 纯编码：只用"参数名后缀 + 值相等 + 命令名"，不引入模型。
    ⚠ 复杂度：每条命令行一次参数解析 + 一次集合查表；倒排索引 main() 建一次。
      整体仍是 O(总行数)。
    ⚠ 失效安全：拿不到倒排索引时**原样返回**，不静默清空实例。
    """
    if not instances or not anchor or not _GLOBAL_VAL_REFS:
        return instances
    out = []
    # ★ 性能修复（2026-10-28）：全集在循环内不变，原实现每实例重建一次 O(N)。
    #   改为循环外算一次；「除自己外」的语义在判断处用 `w == key` 表达，
    #   **不修改集合**（避免 discard/add 成对维护的隐患），内存不随实例数增长。
    _ALL_KEYS = {it.get('key') for it in instances if it.get('key')}
    for inst in instances:
        key = inst.get('key')
        cmds = inst.get('cmds') or {}
        # 本实例"引用过的名字值"：从**直接成员**（带锚点==key 的行）出发，
        # 沿"同一行内的其余名字值"走 **MAX_HOPS 跳**（默认 2）。
        #
        # ⚠⚠ 跳数是关键（实测 2026-10-18）：
        #   1 跳：any_f_f → {any, cbnet_any}                        ← 对
        #   2 跳：+ 从 cbnet_any → {u_p_cbn_cbnet}                  ← 对（rule 绑的用户）
        #   再往下：u_p_cbn_cbnet 的 RULEBINDING 还链到别的 rule，
        #          一路能走到 s13058_ag_gdsgjtysjiot（那是 gdsgjtysjiot 实例的）
        #          ⇒ 实测 15 行里混进 5 条别人实例的 SET URRGRPBINDING
        #   ⇒ 用 MAX_HOPS 封顶，且**只沿"本实例已确认成员"往下走**，
        #      不沿"别人的成员"继续扩散。
        owned_vals = set()
        frontier = set()
        n_direct = 0           # 本实例"自己的直接成员行"数（带锚点==key 的行）
        for seqs in cmds.values():
            for s in seqs:
                node = _GLOBAL_INST_BY_SEQ.get(s)
                params = (node[1] if node else None) or {}
                if params.get(anchor) != key:
                    continue
                n_direct += 1
                for p, v in params.items():
                    if v and p != anchor and _is_name_param(p) and _NAMEV_RE.search(str(v)):
                        frontier.add(str(v))
        # ── Z1 分支：实例自身证据密度决定"追不追下游"（2026-10-18）──────────
        # 判据（纯结构，**在判定之前**就算得出，不看 configured/weak）：
        #   · n_direct >  DIRECT_MAX ⇒ 实例自己有足够直接证据 ⇒ 只收直接引用（1 跳）
        #   · n_direct ≤  DIRECT_MAX ⇒ 实例几乎只有 1 行自己的证据，判据必然在下游
        #                              ⇒ 允许沿引用图追下游（BFS）
        # 实测依据：
        #   · F033 cbnet_01_pcc_p_g 只有 1 行带 PCCPOLICYGRPNM ⇒ 走 BFS ⇒
        #     RULE→FLOWFILTER→FLTBINDFLOWF→FILTER 整条链进来（修好 2 条误剔）
        #   · F881 any_f_f 有 3 行带 FLOWFILTERNAME ⇒ 走 1 跳 ⇒ 不会串入别人的 filter
        # 代价（三产品实测）：命令行 +18.0% / +9.7% / +5.1%
        # 合规性：n_direct 的分布与 core 条数无关（1 行组平均 core 9.3，2-3 行组 9.8），
        #         configured 率反而更低（3.0% vs 1.2%）⇒ 不是"按结果放宽证据"
        owned_vals |= frontier
        owned_direct = set(frontier)      # 只来自本实例直接成员行的名字值
        if n_direct <= DIRECT_MAX:
            # 追下游：沿引用图 BFS，遇到别的实例 key 立即停止该分支。
            #
            # ⚠⚠ 必须有 owned 上限（实测 UDG 性能事故，2026-10-18）：
            #   UDG 有 13 个"超级 hub"值（ADD FLTBINDFLOWF 的 FLOWFILTERNAME，
            #   如 yksp_00_f_f 一个值连接 4891 个其他名字值），从它们 BFS 能到达
            #   **49,745 个值**（≈ 整张图）。"遇到别的实例 key 就停"挡不住 hub，
            #   因为 hub 本身不是实例 key，它的邻居也不是。
            #   后果：UDG 耗时 15s → 76s（5 倍），且 owned 集合上万 ⇒ 逐行判断退化。
            #   ⇒ 加 OWNED_CAP：BFS 展开超过该值就整体放弃追下游（退回 1 跳）。
            #     放弃而不是截断，是因为截断会得到"随机的一半链"，比不追更不可解释。
            # ★ 全集用循环外算好的 _ALL_KEYS（原实现每实例重建 O(N)）；
            #   「除自己外」的语义在判断处用 `w != key` 表达，**不修改集合**，
            #   避免 discard/add 成对维护的隐患。
            other_keys = _ALL_KEYS
            fr2 = set(frontier)
            over_cap = False
            while fr2:
                nxt = set()
                for v in fr2:
                    for w in _GLOBAL_VAL_REFS.get(v, set()):
                        if w == key or w in other_keys or w in owned_vals:
                            continue
                        nxt.add(w)
                if not nxt:
                    break
                owned_vals |= nxt
                fr2 = nxt
                if len(owned_vals) > OWNED_CAP:
                    over_cap = True
                    break
            if over_cap:
                # 放弃追下游，退回"只认直接引用"，与 n_direct > DIRECT_MAX 的分支一致
                owned_vals = set(owned_direct)
        else:
            for _hop in range(MAX_HOPS - 1):
                nxt = set()
                for v in frontier:
                    nxt |= _GLOBAL_VAL_REFS.get(v, set())
                nxt -= owned_vals
                if not nxt:
                    break
                owned_vals |= nxt
                frontier = nxt
        kept = {}
        # 锚点别名：同一对象概念在 MML 里可能有多个参数名（实测：实例锚点是 VRFNAME，
        # 而 ADD AUTOSCALINGSERVICE 用的是 VPNNAME —— 同一个 VRF，参数名不同）。
        #   不认别名 ⇒ 1158/1159 收对了、1166（VPNNAME="CBN_SG"）混进 CBN_GRE 实例。
        #
        # ⚠⚠ 缓存两个要点（都用 None 判断，绝不能用 `not _alias`）：
        #   1) 只算一次 —— 实测 UDG F040 有 670 个实例，用 `if not _alias` 时
        #      670 次全部重扫 10 万条 exp 行 ⇒ 单特性 34s、整轮 10 分钟跑不完。
        #      别名可能是空 tuple（该锚点确无别名），必须把"空"也缓存住。
        #   2) 缓存键带 key 集合规模 —— 不同特性的实例 key 完全不同
        #      （CBN_Gn vs u_p_cmcc_cmwap），复用别的特性的别名等于用错判据。
        _keys = _ALL_KEYS
        _ck = (anchor, len(_keys))
        _alias = _ANCHOR_ALIASES.get(_ck)
        if _alias is None:
            _alias = _discover_anchor_aliases(anchor, _keys)
            _ANCHOR_ALIASES[_ck] = _alias
        _alias = _alias or ()
        for cmd, seqs in cmds.items():
            keep = []
            for s in seqs:
                node = _GLOBAL_INST_BY_SEQ.get(s)
                params = (node[1] if node else None) or {}
                # 先看锚点本身 + 别名，任一命中即按"带锚点"处理
                av = params.get(anchor)
                if av is None:
                    for _al in _alias:
                        if params.get(_al) is not None:
                            av = params.get(_al)
                            break
                a = av
                if a is not None:
                    if a == key:
                        keep.append(s)          # ① 直接成员
                    continue                    # ② 别的实例
                names = [str(v) for p, v in params.items()
                         if v and _is_name_param(p) and _NAMEV_RE.search(str(v))]
                if not names:
                    keep.append(s)              # 无名字参数 → 无法归属，保留
                    continue
                # ⚠ 用 owned_vals（BFS 可达全集），不是 owned_direct（只 1 跳）。
                #   2026-10-18 修正：早期用 owned_direct 是为了挡"两跳外扩混入"
                #   （SET URRGRPBINDING 被抓进 any_f_f），但那时**没有 other_keys 剪枝**。
                #   现在 BFS 遇到别的实例 key 就停 ⇒ 串味由剪枝挡住，不需要再限制跳数。
                #   实测：F033 的 ADD FILTER/FLOWFILTER/FLTBINDFLOWF 在 3~4 跳之外，
                #   用 owned_direct 会被全部误剔（11 条迁移受影响）。
                if any(v in owned_vals for v in names):
                    keep.append(s)              # ③ 本实例引用链上可达 ⇒ 归本实例
                # ④ 与本实例引用链无关 ⇒ 不收
            if keep:
                kept[cmd] = keep
        out.append({'key': key, 'cmds': kept})
    return out


def _clean_vals(vals):
    return {v for v in vals if v and not MASK_RE.match(str(v))}


def strict_value_check(feat, doc, exp_cmd_types, param_vals, core_cmds):
    """固定值契约核对（指纹 enum_vals × exp 值集合，upper 归一 + 对偶豁免）。

    返回 (value_mismatch, value_notes)：
      value_mismatch: T0（必备事项表 key_params 声明的参数）值方向不符 → 降黄
                      {cmd, param, expect, actual}
      value_notes:    T1（仅代码块示例值的参数）不符 + 版本对偶变体 → 注记不降级
    T0 分级依据（防 F218 REDUNDFUNC 类误伤）：必备事项表 = 文档作者对
    "配置本特性必须设置"的官方声明；代码块顺带示例值（如公共对象 ADD POOL
    的 REDUNDFUNC/IMSSW）只标注不降级。命令缺失不计（归 core_miss 层）。
    """
    enum = feat.get('enum_vals') or {}
    kp = (doc.get('key_params') or {})
    mismatch, notes = [], []
    for cmd, ps in enum.items():
        if cmd not in core_cmds or cmd not in exp_cmd_types:
            continue
        declared = set(kp.get(cmd, []))
        for p, ev in ps.items():
            exp_vals = {str(v).upper() for v in _clean_vals(param_vals.get((cmd, p), set()))}
            if not exp_vals:
                if p in declared:      # 必备参数在 exp 命令实例中缺失
                    mismatch.append({'cmd': cmd, 'param': p, 'expect': sorted(ev),
                                     'actual': []})
                continue
            if exp_vals & set(ev):
                continue               # 期望值命中（部分命中即通过，命令级值集合口径）
            # 全无交集 → 版本对偶豁免检查
            miss = exp_vals - set(ev)
            dual = all(any(d in DUAL_PAIRS.get(str(e).upper(), set()) for d in miss)
                       for e in ev)
            rec = {'cmd': cmd, 'param': p, 'expect': sorted(ev),
                   'actual': sorted(exp_vals)}
            if dual:
                rec['variant'] = 'dual'
                notes.append(rec)
            elif p in declared:
                mismatch.append(rec)
            else:
                notes.append(rec)
    return mismatch, notes


def _ver_family(cmd):
    """命令版本对偶族：去掉版本词后的同干命令互为同对象空间
    （FILTER↔FILTERIPV6、SRROUTE↔SRROUTE6、IFIPV4ADDRESS↔IFIPV6ADDRESS）。
    版本词 = 名中 IPV6/IPV4/V6/V4 或数字尾 6——局点双栈/纯 v6 时同一对象
    可能只建在版本对偶命令上（FLTBINDFLOWF 绑定 filter 的定义端可能是
    FILTERIPV6 而非 FILTER），定义端核对须并入族内全部 exp 命令的取值，
    否则把 IPv6 变体实现误判为悬空。
    """
    for w in ('IPV6', 'IPV4', 'V6', 'V4'):
        i = cmd.find(w)
        if i >= 0:
            base = cmd[:i] + cmd[i + len(w):]
            if base:
                return base
    if cmd.endswith('6') and len(cmd) > 3:
        return cmd[:-1]
    return cmd


def strict_link_check(feat, exp_cmd_types, param_vals, exp_cmd_types_full=None):
    """占位符关联核对（指纹 link_groups × exp 值集合，方向语义 + 版本对偶族）。

    组内值域最宽的位置 = 定义端（对象空间），其余位置 = 引用端。
    贯通 = 引用端 ∩ 定义端 ≠ ∅（弱链，存在合法引用）；不要求全覆盖。
    定义端值集合并入版本对偶族（同干命令如 FILTERIPV6/SRROUTE6 在 exp 的值），
    防双栈局点 IPv6 变体实现被误判悬空。
    返回 (groups_ok, groups_dangling, groups_break)：
      dangling: 通但部分引用值悬空（引用值无定义，逐值列出）→ 降黄
      break:    引用端 ∩ 定义端 = ∅（链完全没拼上）→ 降黄
    命令缺失的位置跳过（缺命令已在 core_miss 层表达）。
    """
    # 版本族预索引（一次）：base -> [exp 中的同族命令]
    fam = {}
    for c in exp_cmd_types:
        fam.setdefault(_ver_family(c), set()).add(c)
    dgl_out, brk_out, ok = [], [], 0
    for g in feat.get('link_groups') or []:
        sets = {}
        for cmd, p in g['occ']:
            if cmd not in exp_cmd_types:
                continue
            vs = _clean_vals(param_vals.get((cmd, p), set()))
            if vs:
                sets[(cmd, p)] = vs
        if len(sets) < 2:
            continue
        # 定义端 = occ 序首个有值位置（文档链方向：定义命令在前、引用在后）。
        # 若后续位置是前者的真超集（文档把绑定写前/大而全示例），按宽端覆盖。
        ordered = [tuple(k) for k in g['occ'] if tuple(k) in sets]
        if not ordered:
            continue
        def_end = ordered[0]
        for later in ordered[1:]:
            if sets[later] >= sets[def_end] and len(sets[later]) > len(sets[def_end]):
                def_end = later
        def_vals = set(sets[def_end])
        # 定义端并入版本对偶族取值（同参名：FILTER/FILTERIPV6 双空间）
        for fc in fam.get(_ver_family(def_end[0]), set()):
            if fc != def_end[0]:
                def_vals |= _clean_vals(param_vals.get((fc, def_end[1]), set()))
        dangling, broken = [], False
        for k, v in sets.items():
            if k == def_end:
                continue
            unsupported = v - def_vals
            if not (v & def_vals):
                broken = True
            if unsupported:
                dangling.append({'pos': f'{k[0]}.{k[1]}',
                                 'vals': sorted(unsupported)})
        rec = {'ex': g['ex'][0], 'def': f'{def_end[0]}.{def_end[1]}',
               'occ': [f'{c}.{p}' for c, p in g['occ']],
               'dangling': dangling}
        if broken:
            rec['break'] = True
            brk_out.append(rec)
        elif dangling:
            dgl_out.append(rec)
        else:
            ok += 1
    return ok, dgl_out, brk_out


def build_exp_index(cmds):
    """exp 命令列表 → 三类索引 + 实例证据表"""
    cmd_types = {c['cmd'] for c in cmds}
    param_vals = defaultdict(set)          # (cmd, param) -> set(values)
    inst = defaultdict(list)               # cmd -> [{'seq','params'}]
    for c in cmds:
        inst[c['cmd']].append({'seq': c['seq'], 'params': c['params']})
        for k, v in c['params'].items():
            if v:
                param_vals[(c['cmd'], k)].add(v)
    lic_cmd_types = {c for c in cmd_types
                     if c.startswith(LIC_CMD_PREFIXES)}
    return cmd_types, param_vals, lic_cmd_types, inst


def anchor_value_hit(doc, cmd, param_vals, anchors):
    """值锚定判定：anchors 中 (cmd, ps) 组 OR；组内 AND；组无文档示例值 → 不锚定。

    本实现为「多组 OR（任一组命中）」，与 gen_feature_all.cmd_matches 的
    「第一组优先（未命中即排除）」语义不同，属既有历史差异。
    """
    doc_anchor_vals = doc.get('anchor_vals', {})
    groups = [(c, ps) for (c, ps) in anchors if c == cmd]
    if not groups:
        return True
    any_anchored = False
    for c, ps in groups:
        vals_list = [doc_anchor_vals.get((c, p)) for p in ps]
        if not any(vals_list):
            continue   # 文档示例无这些参数值 → 本组不锚定
        any_anchored = True
        # 值比较大小写归一（IPv4/IPV4 等同值），与 gen_feature_all.cmd_matches 一致
        if all(v is None or ({str(x).upper() for x in param_vals.get((c, p), set())}
                             & {str(x).upper() for x in v})
               for p, v in zip(ps, vals_list)):
            return True
    # 有锚定组但全部未命中 → 排除；无任何锚定组 → 仅类型匹配
    return not any_anchored


# 参数族同义：IPv4/IPv6 双栈对偶参数（IPV4MASK1 ↔ IPV6PREFIXLEN1 等）。
# 归一 = 去 V4/V6 中缀 + 同义替换；判定时按族比较，避免 IPv4 示例文档
# 把 IPv6 组网局点误判为缺参。
FAM_SYN = {'MASK': 'PREFIXLEN'}


def _param_family(p):
    q = re.sub(r'V4|V6', '', p)
    for k, v in FAM_SYN.items():
        q = q.replace(k, v)
    return q


# 继承/关闭态值：参数以"跟随默认"形态规避显式取值（局点规划选择，非遗漏）。
# 检测模式：缺参 p 时同命令存在其开关变体参数（CARSHAPEUL→CARSHAPESWUL，
# 方向后缀 UL/DL 前插 SW）且 exp 取值 ⊂ 本集合。
INHERIT_STATES = {'INHERIT', 'DISABLE'}

_SW_DIR_RE = re.compile(r'^(.*?)([UD]L)$')


def _sw_variants(p):
    """参数 p 的开关变体参数名候选：CARSHAPEUL→CARSHAPESWUL；无方向后缀时
    直接 +SW（BUFFERMODE→BUFFERMODESW）。"""
    m = _SW_DIR_RE.match(p)
    if m:
        return [m.group(1) + 'SW' + m.group(2)]
    return [p + 'SW', re.sub(r'SW$', '', p) + 'SW']


# 预索引：cmd -> {param: set(values)}（性能：_evaded_params/key_param_missing 原每调用
# 全量扫 param_vals 590 命令×参数，11 亿次 str.upper 占 62% 耗时 → 改为按命令 O(1) 取）。
# 由 main() 在 build_exp_index 后构建（单进程单 run，模块级缓存即可，非局点特例）。
_PV_BY_CMD = {}
# 全局参数值倒排：param -> value -> [(cmd, seq)]（1 跳关联用：按"参数名=值"O(1)
# 定位到具体命令行，避免每实例内层全量扫 exp 大命令）。main() 建一次，特性间复用。
_GLOBAL_LINK_INDEX = defaultdict(lambda: defaultdict(list))
# 全局 seq 索引：seq -> (cmd, params)（walk_chain 逐 hop 取节点参数用）。main() 建一次，
# 特性间复用（原 build_leaf_instances / build_leaf_chains 各全量重建一遍，属纯重复）。
_GLOBAL_INST_BY_SEQ = {}


def _evaded_params(cmd, kp):
    """继承态规避的 key_params 参数名清单：缺 p（族级不在 exp）但 exp 同命令存在
    其开关变体参数且取值全为继承/关闭态（如 CARSHAPEUL 未显式而 CARSHAPESWUL=INHERIT）
    → 形态偏（材料在、以继承默认方式规划），不算"缺关键参数"。
    命令级值集合口径：exp 该变体参数出现即视为该命令呈继承态。
    ⚠ p 本身已在 exp（族命中）不算规避——那是显式取值（DISABLE 由方向/值层处理），
    规避仅针对"参数真缺、以开关变体继承态代偿"的形态（2026-09-04 UDG 实证：
    SECONDRULESW=DISABLE 显式关闭被误判规避 → 600 实例/特性 ×5 误降黄）。"""
    return list(_evaded_params_cached(cmd, tuple(kp)))


@lru_cache(maxsize=None)
def _evaded_params_cached(cmd, kp_tuple):
    exp_vals = {p: {str(v).upper() for v in vs}
                for p, vs in _PV_BY_CMD.get(cmd, {}).items() if vs}
    if not exp_vals:
        return ()
    exp_fams = {_param_family(p) for p in exp_vals}
    evaded = []
    for p in kp_tuple:
        if _param_family(p) in exp_fams:
            continue                      # 参数本身已在 exp → 非缺参规避
        for cand in _sw_variants(p):
            vs = exp_vals.get(cand)
            if vs and vs <= INHERIT_STATES:
                evaded.append(p)
                break
    return tuple(evaded)


def key_param_missing(doc, cmd, enum=None):
    """必备事项关键参数校验：返回 exp 中缺失的参数名（族级，值不比较）。

    关键参数来自文档"必备事项/数据"表（如 ADD LOGICINF 的 NAME/IPVERSION/
    IPV4ADDRESS1/IPV4MASK1/VPNINSTANCE）——命令在但缺关键参数 = 配置不完整，
    不判命中。IPv4/IPv6 对偶参数按族归一（IPV4ADDRESS1≈IPV6ADDRESS1）。
    无关键参数表 → []（不校验）。

    两类豁免（2026-09-04 用户拍板口径）：
    A. 开放式数据参数不参与判定：key_params 中无枚举契约的参数（IP 地址/
       掩码/名称/编号等网络规划数据——局点规划值域开放，exp 命令能落库
       即必带值，缺参校验无判别力）由 enum_vals 契约缺席自动豁免；
    B. 继承态规避不算缺：同命令开关变体参数取继承/关闭态（见 _evaded_params）
       → 命令在、形态偏（调用方按 partial 黄处理，不按缺参红处理）。
    """
    kp = doc.get('key_params', {}).get(cmd, [])
    if not kp:
        return []
    cmd_enum = (enum or {}).get(cmd) or {}
    exp_fams = {_param_family(p) for p, vs in _PV_BY_CMD.get(cmd, {}).items() if vs}
    evaded = set(_evaded_params(cmd, kp))
    return [p for p in kp
            if p in cmd_enum                       # A：仅枚举契约内参数可判定
            and _param_family(p) not in exp_fams
            and p not in evaded]                   # B：继承态规避剔除


def _val_prefix(v):
    """锚点参数值的前缀归一：'Saif1/1/0'→'saif'；'S11-uif1/1/0'→'s11uif'
    （小写、取第一段、去尾数字段、去分隔符——接口命名规范值模式）"""
    s = str(v).strip().lower()
    first = s.split('/')[0]
    first = re.sub(r'\d+$', '', first)
    return re.sub(r'[^a-z0-9]', '', first)


def load_name_patterns(path):
    """值模式规则（rules/name_pattern.yaml）。缺文件 → []（不校验）。"""
    if not path or not os.path.exists(path):
        return []
    with open(path, encoding='utf-8') as f:
        data = yaml.safe_load(f) or {}
    return data.get('interface_name_patterns', []) or []


def apply_name_patterns(results, param_vals, patterns):
    """值模式归属校正：同命令集特性（如接口类全族 core 相同）按锚点参数值前缀归属。

    命令级已判 configured 的特性，若 exp 锚点值前缀与本特性命名模式无交集
    → 降级 not_configured（值模式不符，如局点只有 n4if/paif/scif 时 Sa 接口特性
    不判命中）。只降不升，避免误伤未配置特性。
    """
    for pat in patterns:
        fid = pat.get('fid')
        r = results.get(fid)
        if not r or r['status'] != 'configured':
            continue
        cmd, param = pat.get('cmd'), pat.get('param')
        exp_vals = {v for (c, p), vs in param_vals.items()
                    if c == cmd and p == param for v in vs}
        exp_pref = {_val_prefix(v) for v in exp_vals}
        expect = {str(p).lower() for p in pat.get('prefixes', [])}
        hit = bool(exp_pref & expect)
        d = r['detail']
        d['value_pattern'] = {
            'cmd': cmd, 'param': param,
            'expect': sorted(expect),
            'exp_prefixes': sorted(exp_pref),
            'matched': hit,
        }
        if not hit:
            r['status'] = 'not_configured'
            d['notes'] = ('值模式不符：exp 锚点前缀'
                          f'({",".join(sorted(exp_pref)) or "无"}) '
                          f'不匹配本特性命名({"/".join(sorted(expect))})'
                          + (('；' + d['notes']) if d.get('notes') else ''))
            # 命令级聚合同步降级
            d['core_hit'] = []
            d['core_miss'] = d.get('core_miss', []) + [pat.get('cmd', '')]


def extract_instance_anchors(doc, core_cmds, inst=None):
    """从文档示例提取实例锚点参数（数据驱动，不硬编码命令名）。

    实例锚点 = 把 exp 中同名参数值关联成"实例"的名称类参数（如 VRFNAME 把
    ADD L3VPNINST/ADD VPNINSTAF/ADD SRROUTE 串成同一 VRF 实例）。
    候选判定：
    - 参数名属名称类（NAME/NM/ID/KEY/INDEX 结尾，或 VRFNAME/VPNNAME/VPNINSTANCE/
      APNNAME/APN/DNNNAME 等特名）
    - 文档示例值非枚举（ENABLE/DISABLE/TRUE/FALSE/ON/OFF/YES/NO/0/1 等不算；
      文档示例多为单实例模板，值 ≥1 即算候选）
    排序（特性专属优先）：
    1) 组内命令在 exp 中的最少条数升序（条数少 = 特性专属信号，如 ADD IPFARM 1 条；
       公共对象 ADD FILTER 988 条排后）
    2) exp 中该参数值多样性降序（实例数信号，如 HOSTNAME 12 个域名）
    3) 跨命令共享度、文档示例值多样度降序
    返回 [(param, cmds, n_cmds, n_doc_vals, n_exp_vals)]。
    """
    NAME_RE = re.compile(r'(NAME|NM|ID|KEY|INDEX|GRPNAME|GROUPNAME|POOL|TNLNAME|IFNAME)$')
    ENUM_VALS = {'ENABLE', 'DISABLE', 'TRUE', 'FALSE', 'ON', 'OFF', 'YES', 'NO',
                 '0', '1', 'INHERIT', 'NONE', 'ALL'}
    doc_av = doc.get('anchor_vals', {})
    by_param = defaultdict(list)   # param -> [(cmd, values)]
    for (cmd, p), vals in doc_av.items():
        if cmd not in core_cmds:
            continue
        if not isinstance(vals, (set, list, tuple)) or not vals:
            continue
        by_param[p].append((cmd, set(vals)))
    cand = []
    for p, items in by_param.items():
        pu = p.upper()
        is_name = NAME_RE.search(pu) or pu in ('VRFNAME', 'VPNNAME', 'VPNINSTANCE',
                                               'APNNAME', 'APN', 'DNNNAME', 'DNN',
                                               'IPFARMNAME', 'HOSTNAME', 'SERVICENAME')
        if not is_name:
            continue
        all_vals = set()
        for _c, vs in items:
            all_vals |= vs
        ups = {str(x).upper() for x in all_vals}
        if ups <= ENUM_VALS or ups & ENUM_VALS == ups:
            continue   # 全枚举值 → 不是名称
        cmds = sorted({c for c, _ in items})
        # 特性专属度：组内命令在 exp 中的最少条数（公共对象条数巨大 → 排后）
        min_exp = min((len(inst.get(c, [])) for c in cmds), default=0) if inst else 0
        # exp 值多样性：该参数在 exp 中的去重值数（实例数信号）
        n_exp_vals = 0
        if inst:
            exp_vals = set()
            for c in cmds:
                for item in inst.get(c, []):
                    v = item['params'].get(p)
                    if v:
                        exp_vals.add(v)
            n_exp_vals = len(exp_vals)
        cand.append((p, cmds, len(cmds), len(ups), min_exp, n_exp_vals))
    cand.sort(key=lambda x: (x[4], -x[5], -x[2], -x[3]))
    return [(p, cmds, n, v, e) for p, cmds, n, v, _, e in cand[:3]]


def fold_or_groups(core_all, doc):
    """把 core 命令按场景变体 OR 组折叠 → [(label, members)]

    文档写 'ADD POOL(风筝S)/ADD UPPOOL(风筝M或L)' 表示风筝S 与风筝M/L 场景互斥，
    组内任一命令在 exp 命中即整组命中（label 取组内第一个命令名）。
    """
    units, used = [], set()
    for g in doc.get('cmd_or_groups', []):
        members = [c for c in g if c in core_all]
        if members:
            units.append((g[0], members))
            used.update(members)
    units.extend((c, [c]) for c in core_all if c not in used)
    return units


def learn_link_params(doc):
    """从文档示例学关联键参数（数据驱动，零硬编码）：anchor_vals 里存在"自定义值"
    的参数。自定义值 = 含小写字母或点号的值（对象名/IP 等自定义标识），自动排除
    纯数字（80/24/1008/优先级）与全大写枚举（ANY/PCC/ENABLE/OFFLINE/FREE/...）。
    这些参数的值用于 exp 跨命令关联（同名参数同值 1 跳），前端据此高亮共享值。
    例：F014 学得 USERPROFILENAME/RULENAME/FLOWFILTERNAME/FILTERNAME/SVRIP/
    URRNAME/URRGROUPNAME/PCCPOLICYGRPNM/POLICYNAME/PROTOCOLNAME/DFTURRGRPNAME
    /UPURRNAME1/DOWNURRNAME1 等。"""
    link_params = set()
    for (cmd, p), vs in doc.get('anchor_vals', {}).items():
        if not isinstance(vs, (set, list, tuple)) or not vs:
            continue
        for v in vs:
            if v and re.search(r'[a-z.]', str(v)):
                link_params.add(p)
                break
    return link_params


def build_instances(doc, core_cmds, inst, exp_cmd_types, ref_count=None):
    """按实例锚点把 exp 命令聚成实例 → (instances, global_cmds, shared_cmds, anchor_info)

    - 实例命令：core 中含主锚点参数的命令，按锚点值归入各实例
    - 全局型命令：core 中不含锚点参数的命令且 exp 条数 ≤ max(实例数,3) 或文档库引用数低
      （如 SET COLOCATEDLBO 全局开关、ADD POOL 特性专属地址池，属于所有实例的前置，须存在）
    - 公共型命令：exp 条数 ≫ 实例数 且 文档库引用数高（如 ADD FILTER 988 条/900+ 篇），
      跨特性共享对象，不参与实例判定（剔除）
    instances: [{key, cmds: {cmd: [seqs]}, hit, miss, status}]  key=锚点值
    anchor_info: [(param, cmds)] 用于 detail 展示
    """
    anchors = extract_instance_anchors(doc, core_cmds, inst)
    if not anchors or not inst:
        return None, [], [], [], set()
    main_param, main_cmds, _n, _v, _e = anchors[0]
    # 关联键参数（自定义值参数）；1 跳用全局倒排 _GLOBAL_LINK_INDEX
    link_params = learn_link_params(doc)
    link_index = _GLOBAL_LINK_INDEX   # param -> value -> [(cmd, seq)]
    # 通用实例命令全集：含主锚点参数的全部命令（含 prereq/关联命令，不只 core）。
    # 同一实例值被多个命令用同一锚点参数引用时完整收集（如 USERPROFILENAME 同时
    # 出现在 ADD USERPROFILE[prereq]/ADD RULEBINDING[prereq]/SET URRGRPBINDING[core]，
    # 只按 core 收会漏掉前两者 → 判定卡实例命令集不完整）。
    anchor_all_cmds = sorted({c for (c, p) in doc.get('anchor_vals', {})
                              if p == main_param})
    if not anchor_all_cmds:
        anchor_all_cmds = main_cmds   # 兜底：anchor_vals 缺失时退回 core 命令
    # 实例 key 全集：主锚点参数在 exp 中的值
    keys = set()
    for cmd in anchor_all_cmds:
        for item in inst.get(cmd, []):
            v = item['params'].get(main_param)
            if v:
                keys.add(v)
    if not keys:
        return None, [], [], [], link_params
    # 逐实例归组 + 1 跳关联扩展
    instances = []
    for k in sorted(keys):
        inst_cmds = {}
        link_vals = defaultdict(set)          # param -> set(exp 值)，1 跳用
        # 0 跳：含主锚点参数=k 的全部命令行（一个实例可有多条同命令行，
        # 如 u_p_cmcc_cmnet 绑定多个 RULENAME → 多条 ADD RULEBINDING），
        # 同时提取关联键值（避免二次遍历 inst）
        for cmd in anchor_all_cmds:
            for item in inst.get(cmd, []):
                v = item['params'].get(main_param)
                if v == k:
                    inst_cmds.setdefault(cmd, []).append(item['seq'])
                    for p, pv in item['params'].items():
                        if p in link_params and p != main_param and pv:
                            link_vals[p].add(pv)
        # 1 跳：从 0 跳命令的关联键值出发，同名参数同值找邻居命令
        #（如 ADD RULEBINDING.RULENAME=12530_01_r → ADD RULE.RULENAME=12530_01_r）
        #
        # ⚠⚠ 2026-10-18 修正（实测 F098/CBN_Gn）：旧实现只跳"已在 anchor_all_cmds 里"的，
        #   但**不检查邻居命令自己的主锚点值**。后果：ADD BGPPEER(VRFNAME="CBN_Internet")
        #   也会被拉进 CBN_Gn 实例 —— 实测该实例收进 142 行，只有 14 行属于它，
        #   另 128 行是 CBN_Internet/CBN_GRE/CBN_SG/CBN_N6_Local_2B 的（或没有 VRFNAME 的
        #   ADD INTERFACE）。这些"别人的命令"让每个实例都能给别人作证，是"命中偏多"的直接来源。
        #
        # 判据（用户 2026-10-18 确认的口径）：
        #   · 邻居命令**带**主锚点参数且值 ≠ 本实例 key ⇒ 属于别的实例，**不收**
        #   · 邻居命令**不带**主锚点参数 ⇒ 无法按锚点归属，仍收（如 ADD FILTER 这类
        #     通过规则名间接关联的对象；它们该不该算，属关联链建模问题，另行处理）
        for p, vals in link_vals.items():
            for v in vals:
                for cmd2, seq2 in link_index.get(p, {}).get(v, []):
                    if cmd2 in anchor_all_cmds:
                        continue   # 0 跳命令已在实例内（含主锚点），跳过避免重复
                    nv = _GLOBAL_INST_BY_SEQ.get(seq2)
                    if nv:
                        own = (nv[1] or {}).get(main_param)
                        if own and own != k:
                            continue   # ★ 邻居属于别的实例，不收
                    elif seq2 in inst_cmds.get(cmd2, []):
                        continue
                    inst_cmds.setdefault(cmd2, []).append(seq2)
        instances.append({'key': k, 'cmds': inst_cmds})
    n_inst = len(instances)
    # 全局型命令：core 中不含主锚点参数的命令（如 SET COLOCATEDLBO 全局开关、
    # ADD POOL 特性专属地址池），存在检查即可，属于所有实例的前置。
    # ⚠ 不做"exp 条数多即公共剔除"：core 是特性指纹认定的核心命令，
    #    exp 条数大不改变其核心地位（ADD POOL 36 条仍是 F001 核心）；
    #    公共对象误入 core 是治理层问题，判定层静默剔除会造成核心命令被忽略的误判。
    global_cmds = [cmd for cmd in core_cmds if cmd not in anchor_all_cmds]
    return instances, global_cmds, [], anchors, link_params


def build_leaf_chains(doc, inst, param_vals, leaf_ctx=None, max_per_leaf=3):
    """用 leaf_chain 从叶子出发生成配置链（方案B：值×命令类型汇聚 + 链终点叶子）。

    定位：展示层能力，不改判定（零漂移）。产出挂在 detail['leaf_chains'] 供前端
    「去全部聚合 + 汇聚折叠」展示。与 build_instances 的锚点聚合（判定用）正交。

    leaf_ctx：build_leaf_instances 已算好的 groups/param_group/cmd_class/leaf_cmds/
    endpoint_leaf（同一 doc，复用省一次 learn_link_groups；None 则自算，向后兼容）。

    返回 {'leaf_cmds': [...], 'endpoint_leaf': ..., 'chains': {cmd: [代表性链...]}}
    或 None（无叶子/算法异常）。
    """
    try:
        import leaf_chain as lc
    except ImportError:
        return None
    if leaf_ctx is not None:
        groups = leaf_ctx['groups']
        param_group = leaf_ctx['param_group']
        cmd_class = leaf_ctx['cmd_class']
        leaf_cmds = leaf_ctx['leaf_cmds']
        endpoint_leaf = leaf_ctx['endpoint_leaf']
        if not leaf_cmds:
            return None
    else:
        all_params = sorted({p for (cmd, p) in param_vals})
        try:
            groups, cmd_order, cmd_rank = lc.learn_link_groups(doc, all_params)
            cmd_class, leaf_cmds = lc.classify_commands(doc, groups, cmd_order)
        except Exception:
            return None
        endpoint_leaf = leaf_cmds[-1] if leaf_cmds else None
        if not leaf_cmds:
            return None
        param_group = {}
        for gi, g in enumerate(groups):
            for p in g['params']:
                param_group[p] = gi
    inst_by_seq = _GLOBAL_INST_BY_SEQ
    GRAPH = _GLOBAL_LINK_INDEX
    doc_cmd_types = doc.get('all_cmd_types', [])
    chains = {}
    for lc_cmd in leaf_cmds:
        items_lc = inst.get(lc_cmd, [])
        if not items_lc:
            continue
        name_params = []
        for (c, p), vals in doc.get('anchor_vals', {}).items():
            if c == lc_cmd:
                for v in vals:
                    if v and lc.is_name_value(v):
                        name_params.append(p)
                        break
        nm = name_params[0] if name_params else ''
        rep = []
        for it in items_lc[:max_per_leaf]:
            chain, hotspots = lc.walk_chain(lc_cmd, it['seq'], it['params'], groups,
                                            param_group, cmd_class, GRAPH, inst_by_seq,
                                            doc_cmd_types, endpoint_leaf=endpoint_leaf)
            rep.append({'seq': it['seq'], 'name': it['params'].get(nm, ''),
                        'chain': {c: sorted(ss) for c, ss in chain.items()},
                        'hotspots': [(v, c, n) for v, c, n in hotspots]})
        chains[lc_cmd] = rep
    return {'leaf_cmds': leaf_cmds, 'endpoint_leaf': endpoint_leaf, 'chains': chains}


def build_leaf_instances(doc, core_cmds, inst, param_vals):
    """锚点实例建模（叶子链修正版）：实例标识 = 特性专属锚点（extract_instance_anchors
    首选，如 USERPROFILENAME），实例 cmds = 从锚点的 definer 命令出发、用 leaf_chain
    walk_chain 走出的完整链（含叶子命令 FILTER/URR 等）。

    定位：替代 build_instances 的「锚点 + 1 跳关联」——1 跳够不到多跳链上的叶子
    命令（FILTER/URR/FLTBINDFLOWF 被误归「全局型命令存在即命中」）。walk_chain 沿
    definer 组对象名引用正向传播走完整链，汇聚折叠防共享对象串台。

    阈值说明：leaf_chain 默认 OBJ_THRESH=5（拍板「>5 算汇聚」）会把「锚点被大量
    binding 引用」这类真实多引用（如 USERPROFILE 挂 668 条 RULEBINDING）误折叠、
    漏链。从锚点出发时用较高阈值 ANCHOR_OBJ_THRESH 走全 core 又不过度膨胀。

    返回 (instances, leaf_info)：
    - instances: [{key, cmds}]（key=锚点值，cmds=完整链 {cmd: [seqs]}）
    - leaf_info: {seed_name_param, seed_cmd, anchor_cmds, cmd_class}
    或 (None, None)（无锚点/算法异常，调用方回退 build_instances）。
    """
    anchors = extract_instance_anchors(doc, core_cmds, inst)
    if not anchors or not inst:
        return None, None
    try:
        import leaf_chain as lc
    except ImportError:
        return None, None
    all_params = sorted({p for (cmd, p) in param_vals})
    try:
        groups, cmd_order, cmd_rank = lc.learn_link_groups(doc, all_params)
        cmd_class, leaf_cmds = lc.classify_commands(doc, groups, cmd_order)
    except Exception:
        return None, None
    # 对象名参数 → definer（属性共享参数 definer=None 不是实例锚点，排除）
    definer_by_param = {}
    for g in groups:
        if g['definer']:
            for p in g['params']:
                definer_by_param[p] = g['definer']
    # 选第一个「对象名（definer 非 None）」锚点：extract_instance_anchors 按 exp
    # 条数升序会优先选中属性共享参数（如 PROTOCOLNAME 协议名，definer=None），
    # 但属性共享参数不是实例锚点——从它出发 walk_chain 走不到特性专属对象
    # （ADD HEADEN 等）。跳过属性共享，改用特性专属对象锚点（如 HEADENNAME）。
    main_param = None
    seed_cmd = None
    for p, _cmds, _n, _v, _e in anchors:
        if p in definer_by_param:
            main_param = p
            seed_cmd = definer_by_param[p]
            break
    if not main_param or not seed_cmd:
        return None, None
    param_group = {}
    for gi, g in enumerate(groups):
        for p in g['params']:
            param_group[p] = gi
    endpoint_leaf = leaf_cmds[-1] if leaf_cmds else None
    # 命令实例索引 + 图谱
    inst_by_seq = _GLOBAL_INST_BY_SEQ
    GRAPH = _GLOBAL_LINK_INDEX
    doc_cmd_types = doc.get('all_cmd_types', [])
    # 实例 key 全集 = 所有含 main_param 的命令（anchor_all_cmds）里 main_param 值并集，
    # 不能只从 seed_cmd 收集——definer 判定可能把「引用方」误当定义方（如 F266
    # USERPROFILENAME 被学成 ADD RULEBINDING 定义，漏掉无 binding 的 profile）。
    anchor_all_cmds = sorted({c for (c, p) in doc.get('anchor_vals', {})
                              if p == main_param})
    if not anchor_all_cmds:
        anchor_all_cmds = [seed_cmd]
    keys = set()
    for cmd in anchor_all_cmds:
        for it in inst.get(cmd, []):
            v = it['params'].get(main_param)
            if v:
                keys.add(v)
    instances = []
    # ★ 性能修复（2026-10-28）：原实现对每个 key 全量重扫 inst[cmd]，O(N×M)。
    #   实测 5.4MB 切片：ADD FILTER 23,227 条、keys 2,846 个 ⇒ 单特性 ~6600 万次比较。
    #   改为「按 main_param 值建一次索引」。⚠ 只用局部变量，不跨调用缓存
    #   （原版内存基线仅 194MB，绝不能引入随实例数增长的常驻结构）。
    _seed_idx = {}
    for _it in inst.get(seed_cmd, []):
        _v = _it['params'].get(main_param)
        if _v:
            _seed_idx.setdefault(_v, []).append(_it)
    _anchor_idx = {}
    for _cmd in anchor_all_cmds:
        _d = {}
        for _it in inst.get(_cmd, []):
            _v = _it['params'].get(main_param)
            if _v:
                _d.setdefault(_v, []).append(_it)
        _anchor_idx[_cmd] = _d

    for key in sorted(keys):
        # 该 key 的 seed 实例：优先 seed_cmd，否则退回 anchor_all_cmds 首个含该 key 命令
        seed_items = _seed_idx.get(key, [])
        walk_cmd = seed_cmd
        if not seed_items:
            for cmd in anchor_all_cmds:
                its = _anchor_idx[cmd].get(key, [])
                if its:
                    seed_items = its
                    walk_cmd = cmd
                    break
        if not seed_items:
            continue
        chain = defaultdict(set)
        _CHAIN_NODES = 0                      # 本实例已入链的节点数（预算计数）
        for it in seed_items:
            if _CHAIN_NODES >= CHAIN_NODE_BUDGET:
                break                          # 预算用尽，后续 seed 不再走链
            c, _hotspots = lc.walk_chain(walk_cmd, it['seq'], it['params'], groups,
                                         param_group, cmd_class, GRAPH, inst_by_seq,
                                         doc_cmd_types, endpoint_leaf=endpoint_leaf,
                                         obj_thresh=ANCHOR_OBJ_THRESH)
            for cmd, ss in c.items():
                _prev = len(chain[cmd])
                chain[cmd] |= set(ss)
                _CHAIN_NODES += len(chain[cmd]) - _prev
        # ⚠⚠ 2026-10-18 修正（实测 F098/CBN_Gn）：walk_chain 沿 definer 组对象名引用
        #   正向传播，会经"同名参数同值"把**属于别的实例**的命令也带进来 ——
        #   实测该实例收进 142 行，只有 14 行真属于它，另 128 行是
        #   CBN_Internet/CBN_GRE/CBN_SG/CBN_N6_Local_2B 的。
        #   判据（用户确认口径）：链上命令**带**主锚点参数且值 ≠ 本实例 key ⇒ 属于
        #   别的实例，剔除；**不带**主锚点参数的（ADD INTERFACE / ADD FILTER 等）
        #   无法按锚点归属，保留（其归属属关联链建模问题）。
        if main_param:
            for cmd in list(chain.keys()):
                keep = [s for s in chain[cmd]
                        if (inst_by_seq.get(s) or (None, {}))[1].get(main_param) in (None, key)]
                if keep:
                    chain[cmd] = set(keep)
                else:
                    del chain[cmd]
        instances.append({'key': key,
                          'cmds': {c: sorted(ss) for c, ss in chain.items()}})
    # 值级链可达：core 命令若在任一实例的 walk_chain 链上出现 = 链上命令（逐实例
    # 校验）；不在任何实例链上 = 并列/共享命令（特性级存在即命中，如 ADD HEADEN 不
    # 引用 PROTOCOLNAME、ADD FILTERIPV6 跨 profile 共享、ADD POOL 地址池并列块）。
    # 用值级 walk_chain 结果（instances[].cmds）而非命令类型级 BFS——命令类型级会
    # 把「理论经中间命令可达」的并列对象误判为链上命令。
    #
    # 共享池信号（用户拍板）：覆盖少数实例（< 20%）且 exp 条数远大于覆盖实例数
    # （≥ 10 倍）的命令 = 全局共享池（如 ADD L7FILTER 3705 条只覆盖 3/31 profile），
    # 特性级存在即命中，不逐实例校验；区别于「专属链上命令部分缺失」（如 F014 URR
    # 覆盖 20/31）。是否真缺由 judge_instances 的 exp_cmd_types 存在性把关。
    covered = defaultdict(int)
    for it in instances:
        for c in it['cmds']:
            covered[c] += 1
    n_inst = len(instances)
    parallel_cmds = []
    for c in core_cmds:
        cov = covered.get(c, 0)
        if cov == 0:
            parallel_cmds.append(c)   # 不在任何实例链上
        elif (cov < n_inst * SHARED_COVER_RATIO
              and len(inst.get(c, [])) >= cov * SHARED_EXP_MULT):
            parallel_cmds.append(c)   # 共享池：少数实例 + exp 条数大
    return instances, {'seed_name_param': main_param, 'seed_cmd': seed_cmd,
                       'anchor_cmds': sorted({c for (c, p) in doc.get('anchor_vals', {})
                                              if p == main_param}),
                       'cmd_class': cmd_class, 'parallel_cmds': parallel_cmds,
                       'groups': groups, 'param_group': param_group,
                       'leaf_cmds': leaf_cmds, 'endpoint_leaf': endpoint_leaf}


def judge_instances(feat, doc, exp_cmd_types, param_vals, anchors, inst, ref_count=None):
    """实例级判定：按锚点值分组 → 逐实例判定 → (status, detail)

    实例已配置 = 该实例的全部实例命令命中（无类型缺失/值方向不符/L2 锚定不符）
    + 全部全局型命令存在。特性状态 = 任一实例已配置 → configured（实例清单全列出）；
    全未配置 → not_configured（实例缺失清单）。公共型命令剔除不计入。
    场景变体命令（如 ADD POOL(风筝S)/ADD UPPOOL(风筝M或L)）按 OR 组折叠，组内任一命中即整组命中。
    """
    core = feat.get('core', {})
    core_all = core.get('L1', []) + core.get('L2', []) + core.get('L3', [])
    # 方案2：锚点实例建模（特性专属锚点 + 沿对象名引用多跳 BFS 走完整链），
    # 逐实例真实还原链（含叶子命令 FILTER/URR 等）；无锚点/算法异常回退 build_instances。
    leaf_insts, leaf_info = build_leaf_instances(doc, core_all, inst, param_vals)
    if leaf_insts:
        instances = leaf_insts
        main_param = leaf_info['seed_name_param']
        # ⚠⚠ 2026-10-18 新增（实例成员归属收窄）：链遍历会把"别人的命令"拉进本实例。
        #   实测 F881「部署UPF」9 个实例**每个都装了全 exp 的 21 条 ADD FILTER**：
        #     any_f_f 自己的只有 1 条（FILTERNAME="any"，公共对象）
        #     gdsgjtysjiot_00_f_f 自己的有 9 条（_f_001..009）
        #   根因：ADD RULEBINDING 是多对多桥（一条挂 5 个业务用户），
        #   链遍历顺着 RULENAME 反向展开，把 5 家的 filter 树全收进来；
        #   而汇聚阈值 OBJ_THRESH=5 按"单值×单命令类型次数"判，邻居 rule 只出现 1 次
        #   ⇒ 不算汇聚 ⇒ 全部展开。
        #   ⇒ 判据（用户 2026-10-18 确认）：一条命令属于实例 K，当且仅当
        #     ① 带锚点参数且值==K，或
        #     ② 不带锚点参数、但它的名字值**只被 K 使用**（K 的专属下游对象）
        #   共享名字值（如 any）⇒ 不收；带锚点但值≠K ⇒ 不收（上一轮已做）。
        #   ⚠ 性能：倒排索引在 main() 建一次，这里查表 O(1)，不引入模型。
        instances = _narrow_instance_members(instances, main_param)
        # 全局型命令 = core 中无名字参数的 global 类命令（如 SET 全局开关）+
        # 结构上不关联锚点的并列命令（如 ADD HEADEN 不引用 PROTOCOLNAME，特性级
        # 存在即命中）；链上命令（沿 definer 组可达）才逐实例校验。
        global_cmds = [c for c in core_all
                       if leaf_info['cmd_class'].get(c) == 'global']
        global_cmds += leaf_info.get('parallel_cmds', [])
        shared = []
        anchor_info = [(leaf_info['seed_name_param'], [leaf_info['seed_cmd']])]
        link_params = set()
    else:
        instances, global_cmds, shared, anchor_info, link_params = build_instances(
            doc, core_all, inst, exp_cmd_types, ref_count)
        if not instances:
            return None
        main_param = anchor_info[0][0]
    units = fold_or_groups(core_all, doc)
    # 关键参数方向 veto（特性级）：核心实例命令之外的必备事项关键参数
    # 激活方向全 exp 反向 → 业务未激活（与 judge_feature 同语义）
    kp_flips = _keyparam_dir_flips(doc, units, param_vals)

    enum_vals = feat.get('enum_vals') or {}

    # ── 公共对象判据（2026-10-18，裁决：每产品 5% 比例，不用绝对值）──────────
    # 跨特性引用数 = 有多少个特性的 core 引用了该命令。用来识别"公共底座"：
    # 它出现在指纹里是合理的（当锚点种子），但单独命中不足以证明"配了本特性"。
    # ⚠ 性能：整个 match 只算一次（main() 缓存到 _GLOBAL_CORE_USE），
    #   这里查表 O(1)，**不改判定复杂度**，也不引入任何模型。
    _core_use = _GLOBAL_CORE_USE
    # 比例阈值：5% × 本产品特性数；下限 20 防止小产品把真核心误判成公共
    _public_thr = max(int(round(len(_GLOBAL_FEAT_N) * PUBLIC_RATIO)), PUBLIC_MIN)

    def _cmd_ok(cmd):
        """命令级值校验：L2 值锚定 + 开关方向 + 必备事项关键参数。
        返回 (ok, reason, evaded)：evaded = 继承态规避的 key_params 参数名
        （材料在、以继承默认方式规划——命令判"形态命中"但实例按 partial 记，
        由调用方据此降级，不按 configured 记）。"""
        if cmd not in exp_cmd_types:
            return False, '类型缺失', []
        if cmd in core.get('L2', []):
            if not anchor_value_hit(doc, cmd, param_vals, anchors):
                return False, '值锚定不符', []
        dm = _dir_mismatch_cmd(doc, cmd, param_vals)
        if dm:
            return False, f'方向不符({dm})', []
        kpm = key_param_missing(doc, cmd, enum_vals)
        if kpm:
            return False, f'缺关键参数({"、".join(kpm)})', []
        ev = _evaded_params(cmd, doc.get('key_params', {}).get(cmd, []) or [])
        return True, '', ev

    rows = []
    any_ok = False
    for it in instances:
        hit, miss = [], []
        miss_reason = {}
        evaded_cmds = {}
        for label, members in units:
            ok = False
            reason = ''
            for cmd in members:
                if cmd in it['cmds'] or (cmd in global_cmds and cmd in exp_cmd_types):
                    o, rr, ev = _cmd_ok(cmd)
                    if o:
                        ok = True
                        if ev:
                            evaded_cmds[cmd] = ev   # 形态命中但继承态规避
                        break
                    reason = rr
            (hit if ok else miss).append(label)
            if not ok and reason:
                miss_reason[label] = reason
        status = 'configured' if not miss else ('partial' if hit else 'none')
        if status == 'configured' and evaded_cmds:
            # 材料在但关键参数以继承态规避（如 CARSHAPESUL=INHERIT 未显式
            # 选择速率档）→ 形态偏：黄级 partial，不记 configured
            status = 'partial'
        # ⚠⚠ 2026-10-18 新增（裁决 1b）：**命中证据全是公共对象 ⇒ 不判 configured**
        #   背景（实测）：UEG case11 的 405 条命中里 348 条（77.5%）的命中最强证据是
        #   "被几十上百个特性共用"的命令（ADD VPNINSTAF 被 202 个特性 core 引用、
        #   ADD BGPPEER 114、ADD IMPORTROUTE 108）。这类命令只能证明"exp 有 VPN 实例"，
        #   不能证明"配了本特性"。典型：F098 指纹 core 只有 [ADD BGPPEER, ADD BGPVRFAF,
        #   ADD IMPORTROUTE] 三条底座，它真正的特征命令（ADD BGPPEERBFD/MOD BGPVRF）
        #   从未进 core ⇒ 13 个 VRF 实例全判 configured，但证据是空的。
        #
        #   为什么不改指纹库（曾试过，已否决）：把 VPNINSTAF 移出 core 会让
        #   extract_instance_anchors 退而挑 VRFNAME 之外的参数（F103 改用 IFNAME →
        #   115 个"物理接口"伪实例，从 13 个暴涨），判据不是变干净而是换成错基准。
        #   ⇒ 公共命令必须留在 core 里当**锚点种子**（实例建模基准），
        #     但**不能单独充当命中证据**。
        #
        #   判据（零额外开销：只用核心命令的跨特性引用数，不引入模型/不改复杂度）：
        #     该实例的 hit 集全部落在"被 > 阈值 的特性引用"的命令上 ⇒ 降 partial。
        #   阈值 = max(比例阈值, 绝对下限)，比例来自裁决（每产品 5%）：
        #     取 max(5% × 本产品特性数, 20) —— 下限 20 防止小产品把真核心误判成公共。
        if status == 'configured' and hit and all(
                _core_use.get(c, 0) > _public_thr for c in hit):
            status = 'partial'
            public_only_inst = True
            miss_reason['__public_only__'] = (
                f'命中证据全部是公共对象（被 >{_public_thr} 个特性引用），'
                f'不足以证明该实例已配置')
        if status == 'configured':
            any_ok = True
        rows.append({'key': it['key'], 'cmds': it['cmds'], 'hit': hit,
                     'miss': miss, 'miss_reason': miss_reason,
                     'evaded': evaded_cmds or None, 'status': status})
    # 命令级聚合（兼容统计/报告/前端：core_hit/core_miss 语义）。
    # ⚠ 实例级判定下必须互斥：core_hit = 所有实例都命中的命令（命中并集 − 缺失并集），
    # core_miss = 至少一个实例缺失的命令（缺失并集）。旧并集口径会让「部分实例命中」的
    # 命令同时进 hit 和 miss（F014 的 ADD FILTER 等 5 个），前端「命中/缺失」两区块重复
    # 出现同一命令，与实例表逐实例缺失对不上（用户 2026-09-11 反馈，方案1 裁定）。
    _hit_all = {c for r in rows for c in r['hit']}
    _miss_all = {c for r in rows for c in r['miss']}
    detail = {
        'mode': 'instances',
        'instance_anchor': main_param,
        'link_params': sorted(link_params),
        'instance_count': len(rows),
        'instances': rows,
        'shared_cmds': shared,
        'core_hit': sorted(_hit_all - _miss_all),
        'core_miss': sorted(_miss_all),
        'core_hit_anchors': [], 'core_miss_anchors': [],
        'dir_mismatch': kp_flips, 'lic_hit': [], 'lic_miss': [],
        'param_incomplete': {},   # 实例级缺失见 instances[].miss_reason
        'lic_on': False, 'lic_item_on': False,
        'evidence': {},
        'notes': '',
        # 配置链（方案B 链遍历，展示层；不改判定，零漂移）
        'leaf_chains': build_leaf_chains(doc, inst, param_vals, leaf_info),
    }
    # 许可值锚定（功能标识参数须值锚定，禁止只看命令类型——SET LICENSESWITCH
    # 的 LICITEM 授权项：值 ∈ 文档示例期望 且 开关 ENABLE 同行才计开通；实例级
    # 判定分支与命令级 742 行同语义，但升格为行级（LICITEM 与 SWITCH 同现））
    lic = feat.get('license') or {}
    lic_cmds = list(lic) if isinstance(lic, dict) else (list(lic) if lic else [])
    lic_hit, lic_miss = [], []
    lic_item_on = False
    if lic_cmds:
        da = doc.get('anchor_vals') or {}
        for cmd in lic_cmds:
            ps = list(lic.get(cmd, []) or []) if isinstance(lic, dict) else ['LICITEM']
            if not ps:
                ps = ['LICITEM']
            expect_vals = set()
            for p in ps:
                expect_vals |= {str(x).upper() for x in (da.get((cmd, p)) or set())}
            rows_ = list((inst or {}).get(cmd) or [])
            hit_row = None
            for row in rows_:
                rp = row.get('params') or {}
                val_ok = (not expect_vals
                          or bool({str(rp.get(p, '')).upper() for p in ps} & expect_vals))
                sw = str(rp.get('SWITCH', '')).upper()
                if val_ok and (not sw or sw in ('ENABLE', 'ON')):
                    hit_row = row
                    break
            if not expect_vals:
                # 文档示例未提供授权项值（值锚定契约缺席）→ 仅类型存在性核对，
                # 命中与否不降级（豁免口径同 enum_vals 契约缺席）
                if not rows_:
                    lic_miss.append({'cmd': cmd, 'expect': [], 'actual': [],
                                     'note': 'exp 无该命令；文档亦未提供授权项值'})
            elif hit_row is not None:
                hp = hit_row.get('params') or {}
                lic_hit.append({'cmd': cmd,
                                'params': {p: hp.get(p) for p in ps if hp.get(p)},
                                'switch': hp.get('SWITCH', ''),
                                'seq': hit_row.get('seq')})
                lic_item_on = True
            else:
                lic_miss.append({'cmd': cmd, 'expect': sorted(expect_vals),
                                 'actual': sorted({str(x).upper() for x in
                                                   param_vals.get((cmd, ps[0]), set())})})
    if lic_miss:
        detail['lic_miss'] = lic_miss
        miss_s = '、'.join(f"{m['cmd']}(期望 {'/'.join(m['expect']) or '—'})"
                           for m in lic_miss if m.get('expect'))
        if miss_s:
            detail['notes'] = (('；' if detail.get('notes') else '')
                               + f'授权未开（LICITEM 值锚定不中或开关未 ENABLE）：{miss_s}')
    elif lic_hit:
        detail['lic_hit'] = lic_hit
        detail['lic_on'] = True
        detail['lic_item_on'] = True
        hit_s = '、'.join(f"{h['cmd']}({h['params'].get('LICITEM', h['switch'] or '')}"
                          f"{' ENABLE' if str(h.get('switch', '')).upper() == 'ENABLE' else ''}"
                          f" L{h['seq']})" for h in lic_hit)
        if hit_s:
            detail['notes'] = (('；' if detail.get('notes') else '')
                               + f'授权项值锚定命中：{hit_s}')
    if any_ok and not kp_flips:
        if lic_miss:
            # 实例材料齐但授权项未开通 → 不能绿（功能标识参数值锚定 veto）
            detail['mode'] = 'instances_lic_missing'
            return 'weak', detail
        return 'configured', detail
    if kp_flips:
        dm_s = '、'.join(f"{d['cmd']} {p}期望{sorted(dv)}实际{sorted(ev)}"
                         for d in kp_flips for p, dv, ev in d['params'])
        detail['mode'] = 'dir_flip'
        detail['notes'] = f'关键参数方向不符：{dm_s}'
        return 'not_configured', detail
    detail['notes'] = f'实例级判定：{len(rows)} 个实例均未完整配置'
    return 'not_configured', detail


def _dir_mismatch_cmd(doc, cmd, param_vals, declared_only=False):
    """开关类参数方向校验（模块级，judge_feature/judge_instances 共用）：
    返回 [(param, doc_vals, exp_vals)]，空列表 = 方向一致。

    仅校验"文档期望开启、局点关闭"的激活方向（特性未激活却判已配置的核心误判）：
    - 文档示例值必须含开启类（ENABLE/TRUE/ON/YES/PF_ACT_ENABLE）
    - exp 值（掩码 *** 跳过）与文档示例值交集为空 → 方向不符
    文档示例为 DISABLE/关闭时**不校验**：示例值只是示例场景（如 IMSSW 示例
    DISABLE 而局点 ENABLE 属"多开"，不影响特性已配置的事实），不做降级。

    参与校验的参数范围（2026-09-04 分层修订，防"部署示例大杂烩文档"误伤）：
    - declared_only=True（必备事项表声明参数专用路径）：仅 doc.key_params[cmd]
      声明的参数——必备事项表是文档作者对"配置本特性必须设置"的官方声明，
      翻转 = 未按必备配置，特性不成立。族级匹配（IPv4/IPv6 对偶）。
    - declared_only=False（core 命令路径，默认）：key_params 声明参数 **或**
      参数名带开关词（SW/SWITCH/ENABLE/ACTIVE/FLAG）——后者保留 8-28 原机制
      （无必备事项表文档的激活开关仍可检出，如 ULCLSWITCH）。
    - 代码块示例里非声明的普通参数（如部署示例顺带的 ADD POOL REDUNDFUNC=
      ENABLE，其激活语义属于另一特性）**不做方向降级**：示例值只是示例场景。
    """
    ON_VALS = {'ENABLE', 'TRUE', 'ON', 'YES', 'PF_ACT_ENABLE', 'ENABLED'}
    kp_fams = {_param_family(x)
               for x in (doc.get('key_params') or {}).get(cmd, [])}
    out = []
    for (c, p), vals in doc.get('anchor_vals', {}).items():
        if c != cmd:
            continue
        pu = p.upper()
        pf = _param_family(p)
        if declared_only:
            if pf not in kp_fams:
                continue
        else:
            if not (pf in kp_fams
                    or any(s in pu for s in ('SW', 'SWITCH', 'ENABLE', 'ACTIVE', 'FLAG'))):
                continue
        ups = {str(x).upper() for x in vals} if vals else set()
        if len(ups) > 3:
            continue   # 示例值过多（枚举含变量）不自动锚定，防实例名/数值误伤
        if not (ups & ON_VALS):
            continue   # 文档示例非开启类 → 不校验（多开不是缺失）
        exp_vals = {str(x).upper() for x in param_vals.get((cmd, p), set())}
        exp_vals = {x for x in exp_vals if not re.fullmatch(r'\*+', x)}   # exp 脱敏掩码跳过
        if exp_vals and not (exp_vals & ups):
            out.append((p, sorted(ups), sorted(exp_vals)))
    return out


def _keyparam_dir_flips(doc, units, param_vals):
    """必备事项关键参数方向 veto：core 命令之外命令上**表声明**开关的翻转。

    关键参数表（必备事项/数据）是文档作者对"特性生效必备参数"的声明——
    命令可能是配套公共命令（F049 ADD USERPROFILE 的 DDOSCHECK 就是 prereq），
    但其激活方向全 exp 反向（期望 ENABLE、exp 全 DISABLE）= 业务未激活，
    特性不得判已配置。core 命令的翻转已在命令级循环/_cmd_ok 降级处理，
    这里只补 prereq/other 命令，且**只认表声明参数**（declared_only=True，
    名字带开关词的非声明参数不 veto——prereq 命令被多特性共享，其开关可能
    属于别家特性，如 ADD USERPROFILE 的 ALIASMARKFLAG）。
    返回 [{cmd, params, src:'key_param'}]。
    """
    kp = doc.get('key_params') or {}
    core_cmds = {m for u in units for m in u[1]}
    flips = []
    for cmd in sorted(set(kp) - core_cmds):
        dm = _dir_mismatch_cmd(doc, cmd, param_vals, declared_only=True)
        if dm:
            flips.append({'cmd': cmd, 'params': dm, 'src': 'key_param'})
    return flips


def judge_feature(feat, doc, exp_cmd_types, param_vals, anchors, inst=None, ref_count=None):
    """一条指纹 × exp → (status, detail)

    status: configured / not_configured / manual
    detail: {mode, lic_on, lic_item_on, core_hit, core_miss, lic_hit, evidence, notes}
    evidence: groundtruth 实例证据 {cmd: {'seqs': [...], 'first': {param: value}}}（inst 提供时）

    值方向校验（DIRECTION_MISMATCH）：core L1/L3 命令即使类型命中，若文档示例中该命令
    存在开关/使能类参数（参数名含 SW/SWITCH/ENABLE/ACTIVE/FLAG，示例值集合 ≤3 个），
    而 exp 中该参数全部值（掩码 *** 除外）与文档示例值交集为空 → 方向不符（如文档期望
    ULCLSWITCH=ENABLE 而 exp 为 DISABLE），命令从 core_hit 降入 core_miss。
    """
    core = feat.get('core', {})
    core_all = core.get('L1', []) + core.get('L2', []) + core.get('L3', [])
    lic = feat.get('license') or {}
    lic_cmds = list(lic) if isinstance(lic, dict) else lic

    def _evidence(cmd):
        if not inst or cmd not in inst:
            return None
        items = inst[cmd]
        return {'seqs': [x['seq'] for x in items],
                'first': items[0]['params']}

    # 严格核对（绿卡标准：固定值契约 T0 方向 + 占位符关联贯通）
    vm, vn = strict_value_check(feat, doc, exp_cmd_types, param_vals, core_all)
    _lk_ok, lk_dgl, lk_brk = strict_link_check(feat, exp_cmd_types, param_vals)
    lk_bad = lk_dgl + lk_brk
    strict_bad = bool(vm) or bool(lk_bad)

    def _fill_strict(detail):
        detail['value_mismatch'] = vm          # T0 固定值方向不符（降黄依据）
        if vn:
            detail['value_notes'] = vn         # T1 代码块顺带值/对偶变体（注记）
        detail['link_mismatch'] = lk_bad       # 占位符关联悬空/断（降黄依据）
        if strict_bad:
            parts = []
            for m in vm:
                parts.append(f"{m['cmd']} {m['param']}期望"
                             f"{'/'.join(m['expect'])}实际{'/'.join(m['actual']) or '无'}")
            for g in lk_brk:
                parts.append(f"关联[{g['ex']}]断(定义{g['def']})")
            for g in lk_dgl:
                dl = '、'.join(f"{d['pos']}悬空{d['vals']}" for d in g['dangling'])
                parts.append(f"关联[{g['ex']}]悬空({dl})")
            if parts:
                detail['notes'] = (('；' if detail.get('notes') else '')
                                   + '严格核对：' + '；'.join(parts[:6])
                                   + ('…' if len(parts) > 6 else ''))

    # 实例级判定优先（有实例锚点的特性按实例输出，命令级判定降为参考）
    inst_result = judge_instances(feat, doc, exp_cmd_types, param_vals, anchors, inst, ref_count)
    if inst_result:
        status, idetail = inst_result
        # 补充命令级参考信息（供对照）
        idetail['cmd_level'] = None
        _fill_strict(idetail)
        if status == 'configured' and strict_bad:
            status = 'weak'                    # 实例配齐但固定值/关联有偏差 → 黄
        elif (status == 'not_configured'
              and idetail.get('mode') == 'instances'):
            # 实例级红卡细分：存在部分命中实例（材料在、没拼齐）→ 黄
            rows = idetail.get('instances') or []
            n_part = sum(1 for it in rows if it['hit'])
            if n_part and not idetail.get('dir_mismatch'):
                status = 'weak'
                idetail['mode'] = 'instances_partial'
                idetail['notes'] = (('；' if idetail.get('notes') else '')
                                    + f'{n_part}/{len(rows)} 实例部分配置（材料在，'
                                    f'链/值未全部拼齐，见实例明细）')
        return status, idetail

    core_hit, core_miss = [], []
    dir_mismatch = []   # {cmd, param, doc_vals, exp_vals}
    param_incomplete = {}   # cmd -> [缺失关键参数]
    units = fold_or_groups(core_all, doc)
    for label, members in units:
        is_l2 = any(m in core.get('L2', []) for m in members)
        hit_any = False
        for cmd in members:
            if cmd not in exp_cmd_types:
                continue
            if is_l2 and not anchor_value_hit(doc, cmd, param_vals, anchors):
                continue
            dm = _dir_mismatch_cmd(doc, cmd, param_vals)
            if dm:
                dir_mismatch.append({'cmd': cmd, 'params': dm})
                continue
            kpm = key_param_missing(doc, cmd, feat.get('enum_vals') or {})
            if kpm:
                param_incomplete[cmd] = kpm
                continue
            hit_any = True
        (core_hit if hit_any else core_miss).append(label)

    # 关键参数方向 veto：必备事项表声明但不在 core 的命令（prereq/other），
    # 激活方向全 exp 反向 → 业务未激活（F049：ADD USERPROFILE DDOSCHECK 期望
    # ENABLE 而 exp 全 DISABLE，SET DDOS 阈值在 ≠ 防DDoS已激活）
    kp_flips = _keyparam_dir_flips(doc, units, param_vals)
    dir_mismatch += kp_flips

    lic_hit, lic_miss = [], []
    for cmd in lic_cmds:
        ok = cmd in exp_cmd_types and anchor_value_hit(doc, cmd, param_vals, anchors)
        # 行级升格（与实例级分支同口径）：授权值须落在 SWITCH=ENABLE 行，
        # 仅值存在于 DISABLE 行不算授权开通；文档未给授权项值则不升格（契约缺席豁免）
        if ok and inst and cmd in inst:
            da = doc.get('anchor_vals') or {}
            lic_ps = (lic.get(cmd, ['LICITEM']) if isinstance(lic, dict)
                      else ['LICITEM'])
            expv = set()
            for p in lic_ps:
                expv |= {str(x).upper() for x in (da.get((cmd, p)) or set())}
            if expv:
                ok = any(
                    {str(r.get('params', {}).get(p, '')).upper() for p in lic_ps} & expv
                    and str(r.get('params', {}).get('SWITCH', '')).upper()
                    in ('', 'ENABLE', 'ON')
                    for r in inst.get(cmd, []))
        (lic_hit if ok else lic_miss).append(cmd)

    # 核心命令携带锚定参数：命中=现网实例值（evidence 首条），缺失=文档示例期望值
    anchor_groups = defaultdict(list)
    for c, ps in anchors:
        anchor_groups[c].extend(ps)
    core_hit_anchors, core_miss_anchors = [], []
    for cmd in core_hit:
        ps = list(dict.fromkeys(anchor_groups.get(cmd, [])))
        if not ps or not inst or cmd not in inst:
            continue
        first = inst[cmd][0]['params']
        vals = {p: first.get(p) for p in ps if first.get(p)}
        if vals:
            core_hit_anchors.append({'cmd': cmd, 'params': vals})
    for cmd in core_miss:
        ps = list(dict.fromkeys(anchor_groups.get(cmd, [])))
        if not ps:
            continue
        vals = {}
        for p in ps:
            dv = doc.get('anchor_vals', {}).get((cmd, p))
            if dv:
                vals[p] = sorted(dv)
        if vals:
            core_miss_anchors.append({'cmd': cmd, 'params': vals})

    ev_cmds = core_hit or lic_hit
    evidence = {cmd: _evidence(cmd) for cmd in ev_cmds if _evidence(cmd)}

    detail = {
        'mode': 'core_all_hit',
        'core_hit': core_hit, 'core_miss': core_miss,
        'core_hit_anchors': core_hit_anchors,
        'core_miss_anchors': core_miss_anchors,
        'dir_mismatch': dir_mismatch,   # 值方向不符（命令在但开关方向与文档示例相反）
        'param_incomplete': param_incomplete,   # 缺关键参数（必备事项表参数未命中）
        'lic_hit': lic_hit, 'lic_miss': lic_miss,
        'lic_on': bool(lic_hit),          # 授权开关类型命中
        'lic_item_on': bool(lic_hit),     # 授权值锚定命中（含 LICITEM 值）
        'evidence': evidence,
        'notes': '',
    }
    if core_all:
        _fill_strict(detail)
        if not core_miss and not kp_flips:
            # 命令全命中 + 无方向 veto：严格核对通过 = 绿；T0 值偏/链悬空 = 黄
            if strict_bad:
                detail['mode'] = 'strict_dev'
                return 'weak', detail
            return 'configured', detail
        if not core_miss and kp_flips:
            detail['mode'] = 'dir_flip'
        elif core_hit:
            # 域内部分命中（命令少）→ 黄：材料不齐，已命中部分严格核对
            detail['mode'] = 'core_partial'
            detail['notes'] = (('；' if detail.get('notes') else '')
                               + f'核心命令缺 {len(core_miss)} 组'
                               f'（{"、".join(core_miss[:5])}）'
                               + ('…' if len(core_miss) > 5 else ''))
            detail['notes'] += ('；授权在、业务核心未建' if lic_hit else '')
            return 'weak', detail
        else:
            detail['mode'] = 'core_missing'
        core_dm = [d for d in dir_mismatch if d.get('src') != 'key_param']
        if core_dm:
            dm_s = '、'.join(f"{d['cmd']} {p}期望{sorted(dv)}实际{sorted(ev)}"
                             for d in core_dm
                             for p, dv, ev in d['params'])
            detail['notes'] = f'值方向不符：{dm_s}'
        if kp_flips:
            dm_s = '、'.join(f"{d['cmd']} {p}期望{sorted(dv)}实际{sorted(ev)}"
                             for d in kp_flips
                             for p, dv, ev in d['params'])
            detail['notes'] += ('；' if detail['notes'] else '') + f'关键参数方向不符：{dm_s}'
        if lic_hit:
            detail['notes'] += ('；' if detail['notes'] else '') + '授权在、业务核心未建'
        return 'not_configured', detail
    if lic_cmds:
        if lic_hit:
            return 'configured', {'mode': 'license_only', **detail,
                                  'notes': '授权类特性：LICITEM 授权开通'}
        detail['mode'] = 'license_missing'
        detail['notes'] = '授权未开（LICITEM 值锚定未命中）'
        return 'not_configured', detail
    # 无 core 无 license：纯操作类（改密码/加载证书等），无法命令判定
    detail['mode'] = 'no_core_no_lic'
    detail['notes'] = '纯操作/运维类，无业务核心命令，需人工确认'
    return 'manual', detail


def audit_uncovered(exp_cmd_types, docs):
    """反向审计：exp 中未收录命令 → 候选新特性（前缀聚族）。

    SET 类多为网元参数级命令（SET ALARMSWITCH 等），按二级前缀聚类提示；
    ADD/MOD/LCK/LOD 等结构命令是真正的候选特性信号。
    """
    covered = set()
    for d in docs:
        covered.update(d['all_cmd_types'])
    uncovered = sorted(exp_cmd_types - covered)
    cfg = [c for c in uncovered if not c.startswith(QUERY_PREFIXES)]
    fam = Counter()
    for c in cfg:
        if ' ' in c:
            verb, noun = c.split(' ', 1)
            key = f'{verb} {noun[:6]}*' if verb == 'SET' else verb
        else:
            key = c
        fam[key] += 1
    return uncovered, cfg, fam


def detect_product(exp_path, products):
    """从 exp 文件名/路径关键字探测产品（products.yaml detect 列表，顺序即优先级）"""
    p = exp_path.upper()
    for name, pr in products.items():
        for kw in pr.get('detect', []):
            if kw.upper() in p:
                return name
    return ''


def _run_single(args):
    """单 exp（或单网元切分后的一片）分析主流程 —— 原 main() 体，逻辑未改。

    与改造前的唯一差别：
      · `args.exp` 可以是"多 exp 输入"里的某一个
      · 新增 `args._cmds` / `args._exp_label` / `args._me_info`：
        cmdse 已在外部解析过（多 exp 场景下避免重复读文件），
        label 用于报告标题与输出目录名，me_info 是 exp_me.scan_me 的结果
      · 结束时返回本次的统计（供多 exp 汇总）
    """
    import yaml
    here = os.path.dirname(os.path.abspath(__file__))
    products = (yaml.safe_load(open(os.path.join(here, '..', 'rules', 'products.yaml'),
                                    encoding='utf-8')) or {}).get('products', {})

    # 产品解析：显式 > 自动探测 > 无（直接给路径）
    product_name = args.product
    if not product_name:
        product_name = detect_product(args.exp, products)
        if product_name:
            print(f'自动探测产品：{product_name}')
    if product_name and product_name not in products:
        raise SystemExit(f'产品未注册：{product_name}（见 rules/products.yaml）')
    pr = products.get(product_name, {}) if product_name else {}
    if not args.feat_dir:
        args.feat_dir = os.path.expanduser(pr.get('feat_dir', ''))
    if not args.fingerprint:
        args.fingerprint = pr.get('fingerprint', 'rules/features.yaml')
    if not args.anchors:
        args.anchors = 'rules/param_anchor.yaml'
    if not args.patterns:
        args.patterns = 'rules/name_pattern.yaml'
    if not args.out:
        import re as _re
        # 多 exp 场景下 args.out 由调用方给定（match_multi/<产品>/<exp>/<MEID>）
        base = _re.sub(r'[^A-Za-z0-9_.-]', '_',
                       os.path.basename(getattr(args, '_exp_label', '') or args.exp))[:40]
        args.out = f"match_{product_name or 'x'}_{base}"
    if not args.feat_dir or not os.path.isdir(args.feat_dir):
        raise SystemExit(f'特性文档库不存在：{args.feat_dir}（--product 或 --feat-md）')

    t0 = time.time()
    docs = gfa.load_feature_docs(args.feat_dir)
    anchors = gfa.load_param_anchors(args.anchors)
    fp = yaml.safe_load(open(args.fingerprint, encoding='utf-8'))
    feats = fp['features']
    if len(docs) != len(feats):
        print(f'⚠️ 文档 {len(docs)} 篇 vs 指纹 {len(feats)} 条不一致')
    # 对齐：doc_path 主键（title 重复 203 组不能作主键）；旧指纹无 doc_path → 回退位置
    path2doc = {d['doc_path']: d for d in docs}
    doc_by_fid = {}
    pos_fallback = 0
    for fid, f in feats.items():
        p = f.get('doc_path')
        if p and p in path2doc:
            doc_by_fid[fid] = path2doc[p]
        else:
            pos_fallback += 1
    if pos_fallback:
        print(f'⚠️ {pos_fallback} 条指纹无 doc_path，回退位置对齐'
              f'（建议重跑 govern_features --init 重建指纹库）')
    mismatch = sum(1 for fid, f in feats.items()
                   if fid in doc_by_fid and doc_by_fid[fid]['title'] != f.get('title'))
    if mismatch:
        print(f'⚠️ {mismatch} 处 doc_path 对应文档 title 与指纹不一致（doc_path 漂移）')

    # ⚠ 多 exp / 多网元场景：调用方已把 exp 解析并按网元切好，这里直接用
    #   args._cmds，避免同一份 exp 被重复读+解析（UDG 有 10 万行，重复读很贵）。
    cmds = getattr(args, '_cmds', None)
    if cmds is None:
        cmds = gfa.parse_exp(args.exp)
    exp_cmd_types, param_vals, lic_cmd_types, inst = build_exp_index(cmds)
    global _PV_BY_CMD, _GLOBAL_LINK_INDEX, _GLOBAL_INST_BY_SEQ
    _PV_BY_CMD = {}
    for (cmd, p), vs in param_vals.items():
        _PV_BY_CMD.setdefault(cmd, {})[p] = vs
    _GLOBAL_LINK_INDEX = defaultdict(lambda: defaultdict(list))
    _GLOBAL_INST_BY_SEQ = {}
    for cmd, items in inst.items():
        for item in items:
            _GLOBAL_INST_BY_SEQ[item['seq']] = (cmd, item['params'])
            for p, v in item['params'].items():
                if v:
                    _GLOBAL_LINK_INDEX[p][v].append((cmd, item['seq']))
    print(f'exp: {len(cmds)} 条命令 / {len(exp_cmd_types)} 种类型 '
          f'（授权类 {len(lic_cmd_types)}）')

    # ── 公共对象查表（2026-10-18，裁决：比例 5%）──────────────────────────
    # 算一次：cmd -> 有多少个特性的 core 引用它。O(特征数 × core 数)，
    # 与"每条特性各算一遍"相比只省不费，**不改变判定复杂度**（原来每条特性已 O(core)）。
    global _GLOBAL_CORE_USE, _GLOBAL_FEAT_N
    _use = Counter()
    for _f in feats.values():
        _c = _f.get('core') or {}
        if not isinstance(_c, dict):
            continue
        for _lvl in ('L1', 'L2', 'L3'):
            for _cmd in (_c.get(_lvl) or []):
                _use[_cmd] += 1
    _GLOBAL_CORE_USE = dict(_use)
    _GLOBAL_FEAT_N = {'n': len(feats)}
    _thr = max(int(round(len(feats) * PUBLIC_RATIO)), PUBLIC_MIN)
    _public_thr_main = _thr          # 供报告段引用（判据阈值，与判定一致）
    _npub = sum(1 for v in _use.values() if v > _thr)

    # ── 实例成员归属倒排（2026-10-18 方案 C：绑定即归属，**单向**）──────────
    # 方向：引用方 → 被引用方（只沿这个方向走，绝不反向）。
    #
    # ⚠⚠ 为什么要单向（实测踩坑）：第一版建的是**双向**（同一行内任意两个名字值互指），
    #   于是 any ↔ any_f_f 互为引用，无论限几跳都会绕回来，把整张图连成一片 ⇒
    #   限跳数完全无效（实测 15 行的实例里有 5 行是别人实例的）。
    #
    # 方向怎么判（纯编码，不靠语义模型）：
    #   · 带锚点参数的行（如 FLTBINDFLOWF: FLOWFILTERNAME=x, FILTERNAME=y）
    #       ⇒ 锚点值是"上位"，其余名字值是"下位"  ⇒ x → y
    # 值 -> 该值出现的行里"其余名字值"。用途：实例收成员时，从直接成员出发，
    # 把"被它们引用过的名字值"也纳入（any_f_f 通过 FLTBINDFLOWF 引用 any ⇒ any 属于它）。
    #
    # ⚠⚠ 方向问题（2026-10-18 实测修正）：
    #   1) 最初做成**双向**（互指）⇒ 限几跳都绕回，整图连成一片，F881 混进别人命令。
    #   2) 改成**单向**（行内第一个名字值 = 上位 ⇒ 只存 top→others）。
    #      但实测 1727 行
    #        ADD RULE:RULENAME="cbnet_any", FLOWFILTERNAME="any_f_f", POLICYNAME="cbnet_01_pcc_p_g"
    #      第一个是 RULENAME，于是边建成 cbnet_any → {any_f_f, cbnet_01_pcc_p_g}，
    #      而真实语义是 **policy 引用 rule**（cbnet_01_pcc_p_g → cbnet_any）⇒ 方向反了，
    #      F033 从锚点出发走不到自己的下游 ⇒ 收窄把 ADD FILTER/FLOWFILTER 全剔掉（误伤 11 条）。
    #   ⇒ 现在改回**双向**，但**防串味不靠方向、靠"遇到别的实例 key 立即停"**（见
    #      _narrow_instance_members 的 BFS 分支：other_keys 剪枝）。
    #      双向 + other_keys 剪枝 = 能从锚点走到自己链上任意深度，但一步也走不出本实例。
    global _GLOBAL_VAL_REFS
    _refs = defaultdict(set)
    for _seq, (_cmd, _params) in _GLOBAL_INST_BY_SEQ.items():
        _names = [(p, str(v)) for p, v in _params.items()
                  if v and _is_name_param(p) and _NAMEV_RE.search(str(v))]
        if len(_names) < 2:
            continue
        for _p, _v in _names:
            _refs[_v] |= {ov for op, ov in _names if ov != _v}
    _GLOBAL_VAL_REFS = dict(_refs)
    print(f'实例归属索引：{len(_GLOBAL_VAL_REFS)} 个名字值建了引用关系（双向 + 实例 key 剪枝）')
    print(f'公共对象判据：阈值 {_thr}（{len(feats)}×{PUBLIC_RATIO:.0%}，'
          f'下限 {PUBLIC_MIN}）→ {_npub} 种命令视为公共底座')
    # 文档库引用数：跨特性共享对象判据（公共型剔除用，如 ADD FILTER 900+ 篇引用）
    from collections import Counter as _Counter
    ref_count = _Counter(c for doc in docs for c in doc['all_cmd_types'])

    results = {}
    for i, (fid, f) in enumerate(feats.items()):
        doc = doc_by_fid.get(fid) or (docs[i] if i < len(docs) else None)
        if doc is None:
            # ⚠ 必须带 domain：统计段 dom_stat[r['domain']] 直接取键，
            #   缺了会 KeyError（UEG 有 249 条指纹无 doc_path，必走这里）
            results[fid] = {'status': 'manual', 'detail': {'notes': '文档缺失'},
                            'title': f.get('title', ''), 'domain': f.get('domain', '')}
            continue
        status, detail = judge_feature(f, doc, exp_cmd_types, param_vals, anchors, inst, ref_count)
        results[fid] = {'status': status, 'detail': detail,
                        'title': f.get('title', ''), 'domain': f.get('domain', '')}

    # ── 值模式归属校正（同命令集特性按锚点参数值前缀归属，如接口类全族）──
    patterns = load_name_patterns(args.patterns)
    if patterns:
        apply_name_patterns(results, param_vals, patterns)
        vp = sum(1 for r in results.values() if 'value_pattern' in r['detail'])
        vp_down = sum(1 for r in results.values()
                      if r['detail'].get('value_pattern', {}).get('matched') is False)
        print(f'值模式归属：{len(patterns)} 条规则生效，{vp} 条特性参与，'
              f'{vp_down} 条值模式不符降级')

    # ── 统计 ──
    # ⚠ 2026-10-18：命中证据强度标注 + 同标题族折叠（只标注/只折叠展示，**不改 status**）。
    #   依据：实测 UEG 449 条命中里 348 条的最强证据是"被几十上百特性共用"的公共命令；
    #   同标题多指纹 93 组 / 307 条，展示层折叠后 449 → 235 个特性。
    #   判定层不做公共对象剔除（那是治理层问题，静默剔除会掩盖真缺陷）。
    try:
        import evidence_strength as _es
        _es.annotate(results, feats)
        _families, _fam_stats = _es.fold_by_title(results)
    except Exception as _e:      # 标注失败不影响判定结果（附加维度，非主流程）
        _es, _families, _fam_stats = None, [], {}
        print(f'⚠ 证据强度标注失败（不影响判定）：{_e}')

    cnt = Counter(r['status'] for r in results.values())
    dom_stat = defaultdict(Counter)
    for fid, r in results.items():
        dom_stat[r.get('domain', '')][r['status']] += 1   # 防御：任一分支漏 domain 也不崩
    # 红卡（not_configured）归因细分 + 黄卡（weak）成因细分
    not_cfg = [r for r in results.values() if r['status'] == 'not_configured']
    attr = Counter()
    for r in not_cfg:
        d = r['detail']
        core_all = d['core_hit'] + d['core_miss']
        if d['lic_on']:
            attr['授权在、业务核心未建'] += 1
        elif not core_all:
            attr['纯公共/查询组合无核心'] += 1
        elif not d['core_hit']:
            attr['业务核心整族缺失'] += 1
        else:
            attr['域内部分存在'] += 1
    weak_cfg = [r for r in results.values() if r['status'] == 'weak']
    wattr = Counter()
    for r in weak_cfg:
        d = r['detail']
        vm = d.get('value_mismatch') or []
        lm = d.get('link_mismatch') or []
        if d.get('mode') == 'strict_dev':
            wattr['固定值/关联有偏差（命令齐）'] += 1
        elif d.get('core_hit'):
            if vm or lm:
                wattr['命令少+值/链偏差'] += 1
            else:
                wattr['命令少（域内部分命中）'] += 1
        elif vm or lm:
            wattr['命令在但值/链偏差'] += 1
        else:
            wattr['其他'] += 1
    # 缺失命令聚族（缺项清单的跨特性信号：红+黄卡）
    miss_cluster = Counter()
    for r in not_cfg + weak_cfg:
        for c in r['detail']['core_miss']:
            miss_cluster[c] += 1
    # 反向审计
    uncovered, unc_cfg, unc_fam = audit_uncovered(exp_cmd_types, docs)

    # ── 报告 ──
    meta = fp.get('meta', {})
    rep = [
        '# 特性匹配报告（治理指纹 × exp 索引）', '',
        f'- exp：`{args.exp}`',
        f'- 指纹库：`{args.fingerprint}`（version {meta.get("version", "?")}，'
        f'approved {meta.get("stats", {}).get("approved", "?")}/pending {meta.get("stats", {}).get("pending", "?")}）',
        f'- exp 命令：{len(cmds)} 条 / {len(exp_cmd_types)} 种类型',
        f'- 耗时：{time.time() - t0:.1f}s', '',
        '## 总览', '',
        '> 分层语义（2026-09-04 严格匹配）：**绿 = 严格匹配全通过**（core 命令齐全 + '
        '必备固定值 T0 方向命中 + 占位符关联贯通）；**黄 = 严格逻辑下的部分命中**：'
        '命令少（材料不齐）或相似度高但值/关联有偏差——偏差明细逐条列出；'
        '**红 = 无相似**（业务核心整族缺失/方向反向/纯公共）；人工 = 无 core 无 license 的纯操作类。',
        '',
        f'- ✅ 已配置（绿，严格全过）：{cnt["configured"]} 篇',
        f'- 🟡 弱匹配（黄，命令少/值偏/链偏）：{cnt["weak"]} 篇',
        f'- ❌ 未配置（红，无相似）：{cnt["not_configured"]} 篇',
        f'- ⚠️ 需人工：{cnt["manual"]} 篇（无 core 无 license 的纯操作类）', '',
    ]
    # ── 命中证据强度 + 同标题族折叠（2026-10-18 新增）──
    if _fam_stats:
        _et = Counter()
        for _r in results.values():
            if _r['status'] in ('configured', 'weak'):
                _t = ((_r.get('detail') or {}).get('evidence_strength') or {}).get('tier')
                _et[_t or 'unknown'] += 1
        rep += [
            '### 命中证据强度（★ 2026-10-18 新增：只标注，不改判定）', '',
            '> 判据：该命中里**最有区分性**的 core 命令，被多少个特性的指纹同时引用。',
            '> 一条被 200 个特性共用的命令（如 ADD VPNINSTAF）命中，只能证明"这个 exp 有 VPN',
            '> 实例"，不能证明"本特性已配置"。⚠ 这是**复核线索**，不是自动降级。', '',
            f'- 命中条目 **{_fam_stats["hit_results"]}** 条，按标题折叠后 = '
            f'**{_fam_stats["hit_families"]} 个特性**（同标题多指纹 '
            f'{_fam_stats["n_dup_families"]} 组，共折叠 {_fam_stats["n_folded"]} 条）',
            f'- 其中 **{_fam_stats["unbacked"]} 条**命中的证据**全是公共对象**，需重点复核', '',
            '| 证据档 | 命中条目数 |', '|---|---|',
        ]
        for _k in ('strong', 'medium', 'weak', 'public', 'none', 'unknown'):
            if _et.get(_k):
                rep.append(f'| {_es.TIER_CN.get(_k, _k)} | {_et[_k]} |')
        rep += ['', '**证据全是公共对象的命中（优先复核）**：', '',
                '| F | 特性 | 状态 | 命中的公共命令(被N特性共用) |', '|---|---|---|---|']
        _nb = [(fid, r) for fid, r in results.items()
               if ((r.get('detail') or {}).get('evidence_strength') or {}).get('unbacked')]
        for fid, r in _nb[:20]:
            _h = r['detail']['evidence_strength']['hit_cmds']
            _desc = '、'.join(f'{x["cmd"]}({x["use"]})' for x in _h[:3])
            rep.append(f'| {fid} | {r["title"][:26]} | {r["status"]} | {_desc} |')
        if len(_nb) > 20:
            rep.append(f'| … | 其余 {len(_nb) - 20} 条 | | |')
        rep += ['', '']
        # 同标题族折叠总表
        rep += ['### 特性族折叠（同标题多指纹合并显示）', '',
                f'- 指纹 {_fam_stats["n_results"]} 条 → 特性族 {_fam_stats["n_families"]} 个', '']
    rep += [
        '### 红卡归因细分', '',
    ]
    for k, n in attr.most_common():
        rep.append(f'- {k}: {n}')
    rep += ['', '### 黄卡成因细分', '']
    for k, n in wattr.most_common():
        rep.append(f'- {k}: {n}')
    rep += ['', '## 按业务域分布', '', '| 域 | 已配置 | 弱匹配 | 未配置 | 需人工 |', '|---|---|---|---|---|']
    for d in sorted(dom_stat, key=lambda x: -sum(dom_stat[x].values())):
        s = dom_stat[d]
        rep.append(f'| {d} | {s["configured"]} | {s["weak"]} | {s["not_configured"]} | {s["manual"]} |')
    inst_n = sum(1 for r in results.values() if r['detail'].get('mode') == 'instances')
    rep += ['', f'## 实例级判定（{inst_n} 篇按实例锚点分组判定）', '',
            '> 特性核心命令含名称类锚点参数（如 VRFNAME/HOSTNAME/IPFARMNAME）时，exp 中',
            '> 按锚点值聚成实例逐份判定，输出实例数而非单一命令命中数；公共对象命令',
            '> （如 ADD FILTER 数百条）剔除为 shared 不参与实例判定。', '',
            '| F | 特性 | 锚点参数 | 实例数 | 已配置实例 | 状态 |', '|---|---|---|---|---|---|']
    for fid, r in results.items():
        d = r['detail']
        if d.get('mode') != 'instances':
            continue
        rows = d.get('instances', [])
        n_ok = sum(1 for it in rows if it['status'] == 'configured')
        rep.append(f'| {fid} | {r["title"][:30]} | {d.get("instance_anchor", "")} | '
                   f'{d.get("instance_count", 0)} | {n_ok} | {r["status"]} |')
    rep += ['']
    rep += ['', '## 缺失核心命令聚族（未配置特性的缺项信号）', '',
            '| 命令类型 | 缺失篇数 |', '|---|---|']
    for c, n in miss_cluster.most_common(25):
        rep.append(f'| {c} | {n} |')
    rep += ['', '## 反向审计：exp 未收录命令（候选新特性）', '',
            f'- exp 命令类型 {len(exp_cmd_types)} 种，文档库覆盖 {len(exp_cmd_types) - len(uncovered)} 种，'
            f'未收录 {len(uncovered)} 种（其中非查询 {len(unc_cfg)} 种）', '',
            '| 命令族（前缀） | 未收录条数 |', '|---|---|']
    for c, n in unc_fam.most_common(20):
        rep.append(f'| {c} | {n} |')
    non_set = [c for c in unc_cfg if not c.startswith('SET ')]
    rep += ['', f'> SET 族 {len(unc_cfg) - len(non_set)} 条为网元参数级命令'
            '（SET ALARMSWITCH 等），不构成独立特性；以下为结构命令候选：', '',
            '### 候选新特性命令（非 SET）', '']
    for c in non_set[:40]:
        rep.append(f'- {c}')
    if len(non_set) > 40:
        rep.append(f'- …… 其余 {len(non_set) - 40} 条')
    rep += ['', '## 已配置样例（绿：严格全过 + exp 实例证据行号）', '']
    shown = 0
    for fid, r in results.items():
        if r['status'] == 'configured' and r['detail'].get('core_hit'):
            ev = r['detail'].get('evidence', {})
            lines = []
            for cmd, e in list(ev.items())[:4]:
                seqs = e['seqs']
                span = f'{seqs[0]}–{seqs[-1]}' if len(seqs) > 1 else str(seqs[0])
                lines.append(f'{cmd}@{span}')
            rep.append(f'- {fid} {r["title"][:36]}：{"、".join(lines)}')
            shown += 1
            if shown >= 10:
                break
    if not shown:
        rep.append('（无）')
    rep += ['', '> groundtruth 说明：evidence 来自 exp 原文按特性指纹提取的现网实例（行号可回溯）；',
            '> 判定是分析层（指纹×exp 索引），实例证据才是事实层，二者分离可校验。']
    rep += ['', '## 弱匹配样例（黄：命令少/值偏/链偏，含偏差明细）', '']
    shown = 0
    for fid, r in results.items():
        if r['status'] == 'weak':
            d = r['detail']
            vm = d.get('value_mismatch') or []
            lm = d.get('link_mismatch') or []
            mm_s = '、'.join(f"{m['cmd']}.{m['param']}期望{'/'.join(m['expect'])}"
                             f"实际{'/'.join(m['actual']) or '无'}" for m in vm[:2])
            lm_s = '、'.join(f"[{g['ex']}]" + (f"断" if g.get('break') else f"悬空")
                             for g in lm[:2])
            cause = []
            if d.get('core_miss'):
                cause.append(f"缺{len(d['core_miss'])}组")
            if vm:
                cause.append(f"值偏({mm_s})")
            if lm:
                cause.append(f"链({lm_s})")
            note = f'，{d["notes"][:160]}' if d.get('notes') else ''
            rep.append(f'- {fid} {r["title"][:34]}：{"；".join(cause)}{note}')
            shown += 1
            if shown >= 15:
                break
    if not shown:
        rep.append('（无）')
    rep += ['', '> 说明：黄卡与绿卡同一套严格匹配逻辑（命令类型 → 必备固定值 T0 → 占位符关联），'
            '仅因材料不齐或值/关联偏差未达绿；偏差明细即相似度最高的部分与文档契约的差距。']
    rep += ['', '## 未配置样例（红：无相似，含归因）', '']
    shown = 0
    for fid, r in results.items():
        if r['status'] == 'not_configured':
            d = r['detail']
            note = f'，{d["notes"]}' if d['notes'] else ''
            rep.append(f'- {fid} {r["title"][:36]}：缺 {len(d["core_miss"])} 条'
                       f'{"，授权在" if d["lic_on"] else ""}{note}')
            shown += 1
            if shown >= 15:
                break
    rep += ['', '> 归因说明：授权在 = LICENSESWITCH/SOFTPARA 授权开关命中（只证明授权开通，不证明业务已建）；',
            '> 缺项清单 = core_miss（业务核心命令整族或部分缺失）。']

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    rep_path = out / '匹配报告.md'
    rep_path.write_text('\n'.join(rep), encoding='utf-8')
    json_path = out / 'match_result.json'
    # 网元信息（2026-10-19 新增）：从 exp 头部与 MOD ME 行读出，写进 meta 与报告
    _me = getattr(args, '_me_info', None) or {}
    _me_block = {}
    if _me:
        _me_block = {
            'me_type': _me.get('file_me_type', ''),
            'version': _me.get('file_version', ''),
            'patch_version': _me.get('file_patch', ''),
            'meid': getattr(args, '_meid', ''),
            'meln': getattr(args, '_meln', ''),
            'mename': getattr(args, '_mename', ''),
            'meiid': getattr(args, '_meiid', ''),
            'is_multi': bool(_me.get('has_multi')),
        }
    # ⚠ 2026-10-18：results 里新增 detail.evidence_strength（命中证据强度），
    #   并在顶层加 families（同标题折叠后的特性族）+ stats。判定 status 未改动。
    json_path.write_text(json.dumps(
        {'meta': {'exp': args.exp, 'fingerprint': str(args.fingerprint),
                  'updated_at': time.strftime('%Y-%m-%d %H:%M:%S'),
                  'exp_cmds': len(cmds), 'exp_cmd_types': len(exp_cmd_types),
                  'total': len(results), **cnt,
                  # 折叠口径：hit_families 才是"配了哪些特性"的条数
                  **_fam_stats,
                  **({'me': _me_block} if _me_block else {})},
         'families': _families,
         'results': results}, ensure_ascii=False, indent=1), encoding='utf-8')
    print(f'✅ 匹配报告 → {rep_path}')
    print(f'✅ 结果 JSON → {json_path}')
    print(f'状态: 绿已配置 {cnt["configured"]} / 黄弱匹配 {cnt["weak"]} / '
          f'红未配置 {cnt["not_configured"]} / 需人工 {cnt["manual"]}')
    if _fam_stats:
        print(f'证据强度: 命中 {_fam_stats["hit_results"]} 条 → 折叠后 '
              f'{_fam_stats["hit_families"]} 个特性；'
              f'其中 {_fam_stats["unbacked"]} 条证据全是公共对象（详见报告）')
    print(f'反向审计: 未收录 {len(uncovered)} 种（非查询 {len(unc_cfg)}）')
    # 返回统计（多 exp 汇总用）
    return {'exp': args.exp, 'label': getattr(args, '_exp_label', ''),
            'meid': getattr(args, '_meid', ''), 'meln': getattr(args, '_meln', ''),
            'mename': getattr(args, '_mename', ''),
            'out': str(out), 'exp_cmds': len(cmds),
            'cmd_types': len(exp_cmd_types), 'total': len(results),
            'configured': cnt['configured'], 'weak': cnt['weak'],
            'not_configured': cnt['not_configured'], 'manual': cnt['manual'],
            'hit_results': _fam_stats.get('hit_results', 0) if _fam_stats else 0,
            'hit_families': _fam_stats.get('hit_families', 0) if _fam_stats else 0,
            'unbacked': _fam_stats.get('unbacked', 0) if _fam_stats else 0,
            'me': _me_block}


def _write_me_report(me_info, path):
    """把 exp 解析出的网元信息写成 markdown（多 exp 时每个 exp 一份）"""
    els = me_info.get('elements') or {}
    L = ['# exp 网元信息', '']
    L.append(f"- 文件：`{me_info.get('source', '')}`")
    L.append(f"- 网元类型：**{me_info.get('file_me_type') or '未声明'}**")
    L.append(f"- 版本：{me_info.get('file_version') or '未声明'}"
             f"（patch {me_info.get('file_patch') or '-'}）")
    L.append(f"- 网元数：**{len(els)}**"
             f"{'（多网元，已按 MEID 切分）' if me_info.get('has_multi') else '（单网元）'}")
    L.append('')
    if els:
        L += ['| MEID | 网元名 (MELN) | MENAME | 版本 (MEIID) | 业务命令数 | 定义行号 |',
              '|---|---|---|---|---|---|']
        for meid, e in els.items():
            meln = e.get('meln', '')
            if not meln or meln.lower() == 'null':
                meln = f'（MELN=null，用 MENAME）'
            L.append(f"| {meid} | {meln} | {e.get('mename') or '-'} | "
                     f"{e.get('meiid') or '-'} | {e.get('cmd_count')} | {e.get('declared_at')} |")
    else:
        L.append('> 未在 exp 中识别到 `MOD ME` 定义行。')
    path.write_text('\n'.join(L) + '\n', encoding='utf-8')
    return path


def main():
    """入口：支持单 exp（旧用法不变）与多 exp / 多网元。

    输入形态（用户 2026-10-19 裁决：两种都要）：
      1. 多文件：`--exp a.txt b.txt` 或 `--exp <目录>`（递归取 *.txt）
      2. 单文件多段：自动识别 `MOD ME` + `USE ME` 切分，每个 MEID 分别分析

    输出（--out 缺省 match_multi）：
      <out>/<产品>/<exp名>/<MEID>/匹配报告.md   —— 每个网元一份
      <out>/<产品>/<exp名>/网元信息.md          —— 该 exp 的网元清单
      <out>/汇总.md                             —— 跨 exp/网元汇总
      <out>/summary.json                        —— 同上，机读
    """
    ap = argparse.ArgumentParser(
        description='特性匹配（支持单 exp / 多 exp / 单文件多网元）')
    ap.add_argument('--product', default='', help='产品名（显式指定，覆盖自动探测）')
    ap.add_argument('--feat-md', default='', dest='feat_dir',
                    help='特性文档库根目录（缺省按产品）')
    ap.add_argument('--fingerprint', default='', help='指纹库路径（缺省按产品）')
    ap.add_argument('--anchors', default='',
                    help='param_anchor.yaml（缺省 rules/param_anchor.yaml）')
    ap.add_argument('--patterns', default='',
                    help='name_pattern.yaml 值模式规则（缺省 rules/name_pattern.yaml）')
    ap.add_argument('--exp', required=True, nargs='+',
                    help='exp 路径，可给多个文件或一个目录（递归取 *.txt）')
    ap.add_argument('-o', '--out', default='',
                    help='输出目录（单 exp 缺省 match_<产品>_<exp名>；多 exp 缺省 match_multi）')
    ap.add_argument('--no-split-me', action='store_true',
                    help='不按 MEID 切分（整个文件当一个网元，兼容旧行为）')
    args = ap.parse_args()

    import exp_me
    files = exp_me.expand_inputs(args.exp)
    if not files:
        raise SystemExit(f'没有找到 exp 文件：{args.exp}')

    # 输出根目录
    single = len(files) == 1
    user_out = bool(args.out)          # 用户是否显式给了 -o
    root = Path(args.out) if user_out else None
    if root is None and not single:
        root = Path('match_multi')

    print(f'共 {len(files)} 个 exp 文件'
          f'{"（单文件" + ("，显式 -o ⇒ 用多网元布局" if user_out else "，保持旧输出布局") + "）" if single else ""}')
    all_stats = []
    for fi, fpath in enumerate(files, 1):
        text = exp_me.read_exp_text(fpath)
        info = exp_me.scan_me(text, fpath)
        info['source'] = fpath
        print(f'\n[{fi}/{len(files)}] {os.path.basename(fpath)}')
        print(f'  网元：{exp_me.describe(info)}')
        entries = gfa.parse_exp(fpath)
        groups = (exp_me.split_by_me(entries, info)
                  if (info['has_multi'] and not args.no_split_me)
                  else {next(iter(info['elements'])): entries})
        # 旧布局条件：**任一**成立即走会话/指定目录直写（不套 <exp>/ME<id>/）：
        #   · 单文件 + 单网元 + 用户没给 -o（历史默认行为）
        #   · 显式 --no-split-me（调用方已切好片，产物就该直接落 -o 目录）
        # ⚠ 实测 bug（2026-10-19）：早期只判第一种，后端逐网元调用时传了 -o
        #   且带 --no-split-me，仍被套了一层 `_unit_xxx/ME0/`，导致后端判"没产出"。
        old_layout = (single and (not info['has_multi']) and (not user_out)) \
            or bool(args.no_split_me)
        exp_dir = None
        if not old_layout:
            root = root or Path('match_multi')      # 单文件但多网元时 root 可能为 None
            exp_dir = root / (os.path.splitext(os.path.basename(fpath))[0])
            exp_dir.mkdir(parents=True, exist_ok=True)
            _write_me_report(info, exp_dir / '网元信息.md')

        for meid, ents in groups.items():
            e = info['elements'].get(meid, {})
            sub = argparse.Namespace(**vars(args))
            sub._cmds = ents
            sub._me_info = info
            sub._meid = meid
            sub._meln = e.get('meln', '')
            sub._mename = e.get('mename', '')
            sub._meiid = e.get('meiid', '')
            sub._exp_label = (os.path.splitext(os.path.basename(fpath))[0]
                              if len(groups) == 1 else
                              f'{os.path.splitext(os.path.basename(fpath))[0]}__ME{meid}')
            sub.exp = fpath
            if old_layout:
                # 旧布局：直接用用户给的 -o（没给则交给 _run_single 自动命名）。
                # ⚠ 早期写成 sub.out = ''，把用户显式给的 -o 也清掉了 ——
                #   实测（2026-10-19）产物跑到当前目录 match_UEG_a/，-o 目录空。
                sub.out = str(root) if (user_out and root) else ''
            else:
                sub.out = str(exp_dir / f'ME{meid}')
            tag = f'MEID={meid}'
            if e.get('meln') or e.get('mename'):
                tag += f' {e.get("meln") or e.get("mename")}'
            print(f'  ── {tag}：{len(ents)} 条命令')
            st = _run_single(sub)
            all_stats.append(st)

    # 多 exp / 多网元：写汇总
    if not (single and len(all_stats) == 1):
        root = root or Path('match_multi')
        root.mkdir(parents=True, exist_ok=True)
        L = ['# 多 exp 分析汇总', '',
             f'- exp 文件：**{len(files)}** 个',
             f'- 网元（分析单元）：**{len(all_stats)}** 个',
             f'- 生成时间：{time.strftime("%Y-%m-%d %H:%M:%S")}', '',
             '| # | exp | MEID | 网元名 | 类型/版本 | 命令数 | 绿 | 黄 | 红 | 人工 | 输出 |',
             '|---|---|---|---|---|---|---|---|---|---|---|']
        for i, s in enumerate(all_stats, 1):
            me = s.get('me') or {}
            nm = s.get('meln') or s.get('mename') or '-'
            if not nm or str(nm).lower() == 'null':
                nm = s.get('mename') or '-'
            tv = f'{me.get("me_type") or "-"} {me.get("version") or ""}'.strip()
            L.append(f'| {i} | {os.path.basename(s["exp"])} | {s["meid"]} | {nm} | {tv} | '
                     f'{s["exp_cmds"]} | {s["configured"]} | {s["weak"]} | '
                     f'{s["not_configured"]} | {s["manual"]} | `{s["out"]}` |')
        (root / '汇总.md').write_text('\n'.join(L) + '\n', encoding='utf-8')
        (root / 'summary.json').write_text(
            json.dumps({'generated_at': time.strftime('%Y-%m-%d %H:%M:%S'),
                        'files': len(files), 'units': len(all_stats),
                        'units_detail': all_stats}, ensure_ascii=False, indent=1),
            encoding='utf-8')
        print(f'\n✅ 汇总 → {root / "汇总.md"}')
        print(f'✅ 汇总 JSON → {root / "summary.json"}')
        tot = {k: sum(s[k] for s in all_stats)
               for k in ('configured', 'weak', 'not_configured', 'manual')}
        print(f'合计 {len(all_stats)} 个网元：绿 {tot["configured"]} / 黄 {tot["weak"]} / '
              f'红 {tot["not_configured"]} / 人工 {tot["manual"]}')


if __name__ == '__main__':
    main()