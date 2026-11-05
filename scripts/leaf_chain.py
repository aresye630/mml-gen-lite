"""从叶子出发的实例命令链遍历（方案B 汇聚粒度）。

核心语义（用户 2026-09-10 拍板）：
1. 实例 = 一条链条，从「第一个非全局命令」（叶子种子）的每个名字值出发；
   实例名 = 该名字值（如 FILTERNAME=12530_01_f_001）。
2. 沿唯一引用正向传播走到汇聚点终止：
   - 对象名引用（有定义方）：值 × 命令类型 fan-out > OBJ_THRESH → 该方向折叠；
   - 属性共享（无定义方，如 SVRIP）：值 × 命令类型 fan-out > OBJ_THRESH → 该方向折叠。
3. 方案B：汇聚判据粒度 = 值 × 命令类型，不是值整体。
   例：u_p_cmcc_cmnet 在 RULEBINDING 上 570 汇聚，但 USERPROFILE(1)/URRGRPBINDING(1)
   不汇聚 → 只折叠 RULEBINDING 方向，另外两个方向继续走。
4. 定义方 = 组内参数在 doc.anchor_vals 链序最早的命令（被引用对象）；
   引用方 = 引用它的命令。正向传播 = 定义方→引用方 / 引用方→定义方（唯一），绝不反向串台。

数据驱动：零硬编码命令名/参数名；关联组从 doc.anchor_vals 自动学习。
"""

import re
from collections import defaultdict, deque

import gen_feature_all as gfa


# ── 可配置阈值（数据驱动，非特例）──
OBJ_THRESH = 5      # 对象名引用汇聚阈值（用户拍板「同命令名 > 5 算汇聚」）

# ★ 性能修复（2026-10-28）：单次 walk_chain 内的节点访问上限。
#   实测 35MB EXP（24 万条命令）：ADD PROTBINDFLOWF 的 PROTOCOLNAME=dns 只有 2 条
#   （远低于 obj_thresh=15，不折叠），但沿 L7FILTERNAME(2) → FLOWFILTERNAME(13,571 个
#   唯一值，每个 2~5 条) → FILTER(44,292) → FLTBINDFLOWF(55,970) 连锁扩散到 62,497 节点，
#   单次耗时 3.5 秒。**折叠规则只看单层单值，对「每层都只是小值」的跨层累积无效。**
#   ⇒ 加节点访问上限，超限停止展开（已有 chain 保留，不丢已访问部分）。
#   ⚠ 影响量化：
#     · 单特性（激活RTSP头增强）：10.77s → 0.82s，status/实例/core_hit/core_miss 四项全一致
#     · 全量（17.5MB 工单 391 特性）：189.2s → 122.2s（1.5×），
#       判定差异 2/391（status 与实例数全不变，仅 core_hit 各多 1 条）
MAX_VISIT_PER_CALL = 500


def is_name_value(v):
    """自定义值：含小写字母或点（对象名/IP 等），排除纯数字/全大写枚举。"""
    return bool(re.search(r'[a-z.]', str(v)))


def fam(p):
    """参数族：去尾部数字（UPURRNAME1 → UPURRNAME）。"""
    return re.sub(r'\d+$', '', p)


def learn_link_groups(doc, all_params):
    """从 doc.anchor_vals 学关联组（跨名引用组 + 数字变体扩展 + 定义方识别）。

    返回 groups = [{'params': frozenset, 'definer': cmd|None, 'def_param': p|None}]
    - params：组内参数（值共享并查集 + 数字变体扩展）
    - definer：组内参数在 doc 链序最早出现的命令（被引用对象定义方）；仅跨命令引用（≥2 命令）才有
    - def_param：定义方命令上属于本组的参数名
    """
    cmd_order = []
    for s in doc.get('scripts', []):
        for ln in s.split('\n'):
            pr = gfa.parse_mml_cmd(ln)
            if pr and pr[0] not in cmd_order:
                cmd_order.append(pr[0])
    cmd_rank = {c: i for i, c in enumerate(cmd_order)}

    av = doc.get('anchor_vals', {})
    val_to_params = defaultdict(set)
    for (cmd, p), vals in av.items():
        for v in vals:
            if v and is_name_value(v):
                val_to_params[v].add(p)
    # 并查集：共享同一值的参数归组
    parent = {}
    def find(x):
        parent.setdefault(x, x)
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    def union(a, b):
        ra, rb = find(a), find(b)
        if ra != rb:
            parent[rb] = ra
    all_link = set()
    for (cmd, p), vals in av.items():
        for v in vals:
            if v and is_name_value(v):
                all_link.add(p)
    for v, ps in val_to_params.items():
        ps = sorted(ps)
        for i in range(1, len(ps)):
            union(ps[0], ps[i])
    groups0 = defaultdict(set)
    for p in sorted(all_link):
        groups0[find(p)].add(p)
    # 参数在哪些命令出现
    param_cmds = defaultdict(set)
    for (cmd, p), vals in av.items():
        for v in vals:
            if v and is_name_value(v):
                param_cmds[p].add(cmd)
    groups = []
    for root, members in groups0.items():
        fams = {fam(m) for m in members}
        s = set(members)
        for f in sorted(fams):
            for ep in all_params:
                if fam(ep) == f:
                    s.add(ep)
        cmds_seen = set()
        for p in sorted(s):
            cmds_seen |= param_cmds.get(p, set())
        definer = None
        if len(cmds_seen) >= 2:
            definer = min(sorted(cmds_seen), key=lambda c: cmd_rank.get(c, 999))
        def_param = None
        for p in sorted(s):
            if definer in param_cmds.get(p, set()):
                def_param = p
                break
        groups.append({'params': frozenset(s), 'params_sorted': tuple(sorted(s)),
                       'definer': definer, 'def_param': def_param})
    return groups, cmd_order, cmd_rank


def classify_commands(doc, groups, cmd_order):
    """命令三分类 + 叶子种子。

    - global：无名字参数（如 SET LICENSESWITCH）
    - object：含定义方参数（被引用对象，如 ADD FILTER/ADD FLOWFILTER）
    - binding：有名字参数但非定义方（引用方，如 ADD FLTBINDFLOWF/ADD RULEBINDING）
    叶子种子 = object 类 + 入度 0（不被其它命令引用 → 链的起点）。
    """
    av = doc.get('anchor_vals', {})
    cmd_name_params = defaultdict(set)
    for (cmd, p), vals in av.items():
        for v in vals:
            if v and is_name_value(v):
                cmd_name_params[cmd].add(p)
    param_definer = {}
    for g in groups:
        if g['definer']:
            for p in g['params']:
                param_definer[p] = g['definer']
    cmd_class = {}
    for c in cmd_order:
        nps = cmd_name_params.get(c, set())
        if not nps:
            cmd_class[c] = 'global'
        elif any(param_definer.get(p) == c for p in nps):
            cmd_class[c] = 'object'
        else:
            cmd_class[c] = 'binding'
    # 入度：object 命令被其它命令（引用方）引用次数
    param_cmds = defaultdict(set)
    for (cmd, p), vals in av.items():
        for v in vals:
            if v and is_name_value(v):
                param_cmds[p].add(cmd)
    indegree = defaultdict(int)
    for g in groups:
        if not g['definer']:
            continue
        for p in g['params']:
            for c in param_cmds.get(p, set()):
                if c != g['definer']:
                    indegree[c] += 1
    leaf_cmds = [c for c in cmd_order if cmd_class[c] == 'object' and indegree[c] == 0]
    return cmd_class, leaf_cmds


def walk_chain(seed_cmd, seed_seq, seed_params, groups, param_group, cmd_class,
               GRAPH, inst_by_seq, doc_cmd_types,
               obj_thresh=OBJ_THRESH, endpoint_leaf=None):
    """从单个叶子种子实例出发，正向传播走链。

    返回 (chain, hotspots)：
    - chain: {cmd: set(seq)}
    - hotspots: [(value, cmd, cnt)] 汇聚点（被折叠的方向）

    方案B 核心：汇聚判据 = 值 × 命令类型，对称应用于三个方向：
    1. 属性共享（definer=None）：无向，值×命令类型 fan-out > 阈值折叠
    2. 定义方 → 引用方：值×命令类型 fan-out > 阈值折叠
    3. 引用方 → 定义方：值在任何命令类型上汇聚（> 阈值）→ 不追 definer，
       除非 definer 是链终点叶子（endpoint_leaf，链序最晚的叶子对象命令，
       如 ADD USERPROFILE）。方案 B：链终点对象被大量 bind 引用（汇聚）仍进链，
       中间叶子（如 FLOWFILTER）汇聚则不追，阻断共享 flowfilter/默认组串台。
    """
    chain = defaultdict(set)
    hotspots = []
    queue = deque([(seed_cmd, seed_seq, seed_params)])
    visited = set()

    def _fanout_by_cmd(v, g):
        """值 v 在组 g 内所有参数（跨名合并）上按命令类型分组的 fan-out。

        ★ M3：组参数顺序在建组时已算好（g['params_sorted']），不再每次排序。
          实测 _fanout_by_cmd 占 ~23%（采样），其中 sorted 是大头；
          而它只依赖组、与 v 及循环状态无关 ⇒ 移到建组处一次完成。
        """
        by_cmd = defaultdict(set)
        for gp in g['params_sorted']:
            for ncmd, nseq in GRAPH[gp].get(v, []):
                if ncmd not in doc_cmd_types:
                    continue
                by_cmd[ncmd].add(nseq)
        return by_cmd

    while queue:
        # ★ 2026-10-28：节点访问上限（防跨层连锁扩散，见 MAX_VISIT_PER_CALL 注释）
        if len(visited) >= MAX_VISIT_PER_CALL:
            break
        cmd, seq, params = queue.popleft()
        if (cmd, seq) in visited:
            continue
        visited.add((cmd, seq))
        chain[cmd].add(seq)
        for p, v in params.items():
            if not is_name_value(v):
                continue
            gi = param_group.get(p)
            if gi is None:
                continue
            g = groups[gi]
            definer = g['definer']
            def_param = g['def_param']
            if definer is None:
                # 属性共享（如 SVRIP）：无方向，值×命令类型判汇聚
                by_cmd = _fanout_by_cmd(v, g)
                for ncmd in sorted(by_cmd):
                    nseqs = by_cmd[ncmd]
                    if len(nseqs) > obj_thresh:
                        hotspots.append((v, ncmd, len(nseqs)))
                        continue
                    for nseq in sorted(nseqs):
                        if (ncmd, nseq) != (cmd, seq):
                            queue.append((ncmd, nseq, inst_by_seq[nseq][1]))
            elif cmd == definer:
                # 定义方 → 引用方（方案B：值×命令类型判汇聚）
                ref = defaultdict(set)
                for gp in g['params_sorted']:   # ★ M3：预排序字段（同 _fanout_by_cmd）
                    for ncmd, nseq in GRAPH[gp].get(v, []):
                        if ncmd == definer:
                            continue
                        if ncmd not in doc_cmd_types:
                            continue
                        ref[ncmd].add(nseq)
                for ncmd in sorted(ref):
                    nseqs = ref[ncmd]
                    if len(nseqs) > obj_thresh:
                        hotspots.append((v, ncmd, len(nseqs)))
                        continue
                    for nseq in sorted(nseqs):
                        queue.append((ncmd, nseq, inst_by_seq[nseq][1]))
            else:
                # 引用方 → 定义方（方案B：值汇聚则不追 definer，除非 definer 是链终点叶子）
                if not def_param:
                    continue
                by_cmd = _fanout_by_cmd(v, g)
                is_hotspot = any(len(nseqs) > obj_thresh for nseqs in by_cmd.values())
                if is_hotspot and definer != endpoint_leaf:
                    # 值在某个命令类型上汇聚，且 definer 不是链终点叶子 → 不追，
                    # 阻断公共默认组/共享 flowfilter 串台
                    hotspots.append((v, cmd, max(len(n) for n in by_cmd.values())))
                    continue
                for ncmd, nseq in GRAPH[def_param].get(v, []):
                    if ncmd == definer and ncmd in doc_cmd_types:
                        queue.append((ncmd, nseq, inst_by_seq[nseq][1]))
    return chain, hotspots
