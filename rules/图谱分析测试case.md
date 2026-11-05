# EXP 图谱分析测试 case（tzq / he_service 服务链）

## 一、定位区分（为什么把 tzq 死环支从「特性匹配」挪到「图谱分析」）

| 维度 | 特性匹配（黄金规则 56 条） | EXP 分析（图谱走链） |
|---|---|---|
| 要回答 | 特性文档 F014 的配置模式是否在现网落地 | 现网某条业务链是否完整闭环 |
| 证据充分性 | 已由 94872/94873/94900/94901/94904/95159/95160 这些 RULE 证明（POLICYTYPE/POLICYNAME/FLOWFILTERNAME/FILTERINGMODE 模式一致），**不依赖 95452** | tzq 死环支 6 MISSING 是 he_service 服务的一条完整业务链 |
| 走链机制 | 特性文档 examples 锚定种子 + 关联组展开 | 引用关系图（name 参数值 = 对象名字参数值）双向走通连通分量 |

结论：95452 只是 he_service 服务下「url 分支」的一条 RULE，它和已命中的 95429(tzq_r_ip)、95430~95451(tzq_r_l3l7_*) 是同构的——都 POLICYNAME=he_service。特性匹配的证据已足，tzq 的「完整链」用图谱解决。

## 二、case 格式

同黄金规则：`命令类型 → 期望 seq 列表`，但语义是「从入口锚点沿引用关系图走通的连通分量成员」。
每个 case 附：入口锚点 + 现网实例值依据 + 判别点。

## 三、数据背景（现网实例值，EXP = XAUPF017BHW）

he_service 服务（跨网元：PCCPOLICYGRP 定义方在 SMF 侧，UPF 侧定义方是 ADD HEADEN）：

```
ADD HEADEN  HEADERENNAME=he_service    → 94122(MSISDN1) / 94123(MSIP1) / 94124(RAT1)
ADD RULE    POLICYNAME=he_service      → 24 条（url 1 + ip 1 + l3l7 22）
   url  分支: 95452 tzq_r_url           FLOWFILTERNAME=tzq_f_f_url
   ip   分支: 95429 tzq_r_ip            FLOWFILTERNAME=tzq_f_f_ip
   l3l7 分支: 95430~95451 tzq_r_l3l7_*  FLOWFILTERNAME=tzq_f_f_l3l7_*
ADD RULEBINDING  RULENAME=tzq_r_*      → 96108(ip) / 96109~96130(l3l7) / 96131(url)
```

负例（https 变体，同构但值不同，不应混入）：
```
ADD TLSHEADEN  HEADERENNAME=he_service_https → 94126/94127/94128/94129
ADD RULE       https_tzq_r_url (95039)         FLOWFILTERNAME=https_tzq_f_f_url
```

---

## Case 1 —— FILTER 消费链（对象→绑定 1:1 干净链）

入口：ADD FILTER(tzq_f_0393) @24198
图谱机制：定义方参数值 FILTERNAME=tzq_f_0393 → 引用方 FLTBINDFLOWF.FILTERNAME

期望（黄金规则格式）：

    ADD FILTER        期望[24198]
    ADD FLTBINDFLOWF  期望[84068]

现网实例值依据：
- ADD FILTER@24198: FILTERNAME=tzq_f_0393
- ADD FLTBINDFLOWF@84068: FLOWFILTERNAME=tzq_f_f_ip, FILTERNAME=tzq_f_0393

判别点：tzq_f_0393 全 EXP 仅 2 条引用（定义方 ADD FILTER 24198 + 消费方 FLTBINDFLOWF 84068），干净 1:1，图谱应精确走通，不越界。

---

## Case 2 —— FLOWFILTER 消费链（汇聚 vs 非汇聚判别）

入口：ADD FLOWFILTER(tzq_f_f_url) @49908
图谱机制：FLOWFILTERNAME=tzq_f_f_url → 消费方 PROTBINDFLOWF / RULE

期望（黄金规则格式）：

    ADD FLOWFILTER      期望[49908]
    ADD PROTBINDFLOWF   期望[94071]
    ADD RULE            期望[95452]

现网实例值依据：
- ADD FLOWFILTER@49908: FLOWFILTERNAME=tzq_f_f_url
- ADD PROTBINDFLOWF@94071: FLOWFILTERNAME=tzq_f_f_url, PROTOCOLNAME=http, L7FILTERNAME=tzq_l7_f
- ADD RULE@95452: RULENAME=tzq_r_url, FLOWFILTERNAME=tzq_f_f_url, POLICYNAME=he_service

判别点（难度梯度）：tzq_f_f_url 全 EXP 仅 3 条引用（定义方 + PROTBINDFLOWF + RULE），非汇聚，干净链；对比 tzq_f_f_ip 有 693 条引用（定义方 + 691 条 FLTBINDFLOWF + 1 条 RULE），是汇聚链。图谱应能区分「非汇聚精确走通」与「汇聚按规则展开/拦截」。

---

## Case 3 —— 服务聚合（跨参数同值 HEADERENNAME=POLICYNAME，1:N）

入口：ADD HEADEN(he_service) @94122
图谱机制：HEADERENNAME=he_service = POLICYNAME=he_service，跨参数同值聚合 RULE

期望（黄金规则格式）：

    ADD HEADEN       期望[94122, 94123, 94124]
    ADD RULE         期望[95429, 95430..95452]   # 24 条，seq 连续 95429~95452

现网实例值依据：
- ADD HEADEN@94122: HEADERENNAME=he_service, DATATYPE=MSISDN1
- ADD HEADEN@94123: HEADERENNAME=he_service, DATATYPE=MSIP1
- ADD HEADEN@94124: HEADERENNAME=he_service, DATATYPE=RAT1
- ADD RULE ×24: POLICYNAME=he_service（95452 url / 95429 ip / 95430~95451 l3l7）

判别点：he_service 的 PCCPOLICYGRP 定义方在 SMF 侧（UPF EXP 无实例），是跨网元对象；UPF 侧通过 HEADEN 定义 + POLICYNAME 引用聚合 24 条 RULE。图谱需跨参数同值连接（HEADERENNAME 值 = POLICYNAME 值），不能只靠同一关联组。

---

## Case 4 —— url 分支完整闭环（黄金规则 6 MISSING 的图谱版）

入口：ADD HEADEN(he_service) @94122（或 ADD FILTER(tzq_f_0393) @24198）
图谱机制：服务→规则→绑定→流过滤→过滤对象 的完整连通

期望（黄金规则格式）：

    ADD HEADEN         期望[94122, 94123, 94124]
    ADD RULE           期望[95452]
    ADD RULEBINDING    期望[96131]
    ADD FLOWFILTER     期望[49908]
    ADD PROTBINDFLOWF  期望[94071]
    ADD L7FILTER       期望[48711]

现网实例值依据（url 分支闭环）：
- ADD RULE@95452: RULENAME=tzq_r_url, FLOWFILTERNAME=tzq_f_f_url, POLICYNAME=he_service, POLICYTYPE=HEADEN
- ADD RULEBINDING@96131: USERPROFILENAME=u_p_cmcc_cmnet, RULENAME=tzq_r_url, POLICYTYPE=HEADEN
- ADD FLOWFILTER@49908: FLOWFILTERNAME=tzq_f_f_url
- ADD PROTBINDFLOWF@94071: FLOWFILTERNAME=tzq_f_f_url, L7FILTERNAME=tzq_l7_f
- ADD L7FILTER@48711: L7FILTERNAME=tzq_l7_f, SUBL7FLTNAME=tzq_sl7_f_0464

判别点：这是黄金规则 6 MISSING 本体。图谱应从 he_service 走到 tzq_r_url → tzq_f_f_url → tzq_l7_f 完整闭环，且不混入 https 变体。注意 tzq_l7_f 有 638 条子过滤器（L7FILTERNAME=tzq_l7_f，SUBL7FLTNAME 各异），完整图谱走通全部；特性匹配只收 0464 一条——这正是「完整链交给图谱」的边界。

---

## Case 5 —— https 变体隔离（负例判别）

入口：ADD HEADEN(he_service) @94122
图谱机制：不应跨值连接到 he_service_https

期望（黄金规则格式）：

    ADD HEADEN         期望[94122, 94123, 94124]
    # 以下不得出现（负例）：
    # ADD TLSHEADEN     94126/94127/94128/94129  (HEADERENNAME=he_service_https)
    # ADD RULE          95039                    (https_tzq_r_url)
    # ADD RULEBINDING   95792                    (RULENAME=https_tzq_r_url)
    # ADD FLOWFILTER    49548                    (https_tzq_f_f_url)

现网实例值依据（负例依据）：
- ADD TLSHEADEN@94126: HEADERENNAME=he_service_https, TLSTYPEVAL=17516
- ADD RULE@95039: RULENAME=https_tzq_r_url, POLICYNAME=he_service_https, FLOWFILTERNAME=https_tzq_f_f_url

判别点：he_service 与 he_service_https 是不同值，图谱按「值」精确连接，不应跨值串链。这是判别图谱是否「值锚定」而非「前缀模糊匹配」的关键负例。

---

## 附：五个 case 的机制覆盖矩阵

| Case | 图谱机制 | 难度 | 判别力 |
|---|---|---|---|
| 1 | 定义方值→引用方（同参数） | 简单 | 1:1 干净链，不越界 |
| 2 | 定义方值→引用方（汇聚判别） | 中 | 非汇聚精确 vs 汇聚展开 |
| 3 | 跨参数同值（HEADERENNAME=POLICYNAME） | 中 | 跨网元 1:N 聚合 |
| 4 | 完整连通分量（服务闭环） | 难 | 6 MISSING 本体闭环 |
| 5 | 值锚定负例（不跨值串链） | 难 | 排除 https 变体误收 |
