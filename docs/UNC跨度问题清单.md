# UNC 跨度问题清单

> 生成时间：2026-11-10
> 数据来源：87 工单 GT + 各工单上传的 EXP + 两阶段评估结果

## 一、问题概述

- 受影响工单：**26 / 87**
- 这些工单的 GT 里含有 UDG 文档库查不到的族（只在 UNC 文档库）
- 合计 UNC 独有族命令：**3158 条**
- 这些工单的 GT 族合计：549 个

## 二、根因

1. 工单材料只提供了 **UDG 侧**的 EXP 现网快照
2. GT 里的配置跨 UDG + UNC 两个网元（同一业务在两个网元各有命令族）
3. agent 在 UDG 的 EXP 里查不到 UNC 侧的族，无法配置

### 典型案例的工单原文佐证

**NC20260803000197** 的操作脚本步骤 1 明确写道：

```
网管进行操作前信息备份：登录网管进行主拓扑界面，
右键点击对应的 UNC/UDG 网元，选择"MML"，进入界面执行 EXP MML，导出脚本文件
```
→ 说明这个工单**本来就要求导出 UNC + UDG 两份 EXP**，但数据集只给了 UDG 那份。

### 已验证可解决

在工作区的 UNC EXP 里确实能查到这些族：

| 族 | 中文名 | 所在 UNC EXP |
|---|---|---|
| TAIRANGELIST | 查询NF TAI区域信息 | APP-NQGZhiSMF001BHW / APP-NQCDhiSMF001BHW |
| UPAREABINDN2TAI | 删除UPF服务区名称绑定的5G TAI范围 | ISGWC800 |

→ 补齐对应 UNC 网元的 EXP 即可自然解决。

## 三、工单明细

按 UNC 族命令数降序。**阶段1覆盖** 列格式为「规划命中族数 / GT族总数」。

| # | 工单 | GT条数 | GT族数 | UNC族数 | UNC命令数 | 阶段1覆盖 | EXP覆盖 | 主要缺失的 UNC 族 |
|---|---|---|---|---|---|---|---|---|
| 1 | NC20260811002706 | 1164 | 57 | 30 | 728 | 25/57 | 46% | CONNECTPLMN(674)、PNFDNN(12)、HPLMN(7)、USRPROFGROUP(3)、UPBINDUPG(3) 等 30 个 |
| 2 | NC20260828000360 | 1035 | 49 | 27 | 724 | 19/49 | 43% | CONNECTPLMN(677)、PNFDNN(10)、HPLMN(7)、NGCONNECTPLMN(2)、PCSCFGROUP(2) 等 27 个 |
| 3 | NC20260823000103 | 765 | 54 | 27 | 390 | 25/54 | 48% | CONNECTPLMN(339)、NGCONNECTPLMN(12)、HPLMN(7)、PCSCFIP(4)、PNFDNN(4) 等 27 个 |
| 4 | NC20260810002261 | 436 | 53 | 27 | 385 | 17/53 | 47% | CONNECTPLMN(343)、HPLMN(7)、PCSCFIP(4)、PNFDNN(4)、NGCONNECTPLMN(3) 等 27 个 |
| 5 | NC20260820000552 | 341 | 16 | 15 | 340 | 1/16 | 6% | BSFIPRANGEBIND(249)、TAIRANGELIST(40)、UPBINDS11(20)、PEERNFIPLIST(7)、PNFDNN(5) 等 15 个 |
| 6 | NC20260806001438 | 321 | 55 | 28 | 198 | 18/55 | 47% | PNFDNN(36)、CONNECTPLMN(35)、VIRTUALAPNRULE(29)、APNDEACTQFPLCY(20)、APNPCCFUNC(10) 等 28 个 |
| 7 | NC20260806001780 | 412 | 41 | 16 | 63 | 25/41 | 61% | PNFDNN(28)、PCSCFIP(13)、PCSCFGRPBNDAPN(4)、PCSCFGROUP(3)、APNDEACTQFPLCY(2) 等 16 个 |
| 8 | NC20260907000688 | 209 | 12 | 3 | 40 | 4/12 | 75% | UPIPDOMAIN(36)、UPFBINDSELRULE(2)、UPCMPT(2) |
| 9 | NC20260907001683 | 50 | 5 | 2 | 40 | 0/5 | 60% | UNCIPRESOUCE(38)、PNFDNN(2) |
| 10 | NC20260828000409 | 148 | 22 | 5 | 35 | 9/22 | 77% | PNFDNN(21)、APNRDSSVRGRP(4)、APNUSRPROFG(4)、NSDNN(4)、PNFNS(2) |
| 11 | NC20260915001368 | 45 | 7 | 4 | 35 | 3/7 | 43% | MMEIPTOMMEPOOL(16)、SGWIPTOSGWPOOL(16)、NGALMRPTMODE(2)、NGCBSFUNC(1) |
| 12 | NC20260811002152 | 166 | 12 | 7 | 33 | 4/12 | 42% | PCSCFGRPBNDAPN(9)、PCSCFGROUP(8)、PCSCFIP(8)、UPNODE(2)、PNFSUPI(2) 等 7 个 |
| 13 | NC20260808000433 | 25 | 6 | 5 | 24 | 1/6 | 17% | PNFSMFSERAREA(8)、UPNODE(4)、PNFPROFILE(4)、PNFNS(4)、UPBINDS11(4) |
| 14 | NC20260828001156 | 360 | 12 | 3 | 20 | 9/12 | 75% | PNFSMFSERAREA(12)、PNFDNN(4)、IMSIBINDUP(4) |
| 15 | NC20260820001773 | 67 | 41 | 14 | 20 | 26/41 | 66% | UPIPDOMAIN(4)、PNFDNN(2)、APNUPFINFO(2)、SRVNODERAT(2)、APNIDLETIME(1) 等 14 个 |
| 16 | NC20260911000610 | 323 | 11 | 6 | 19 | 1/11 | 9% | PNFNS(7)、PNFDNN(7)、NFNS(2)、PLMNNS(1)、LOCALNSDNN(1) 等 6 个 |
| 17 | NC20260805002150 | 30 | 24 | 10 | 12 | 12/24 | 33% | PNFDNN(2)、UPNODE(2)、NSDNN(1)、APNUPSELPLY(1)、APNUSRPROFG(1) 等 10 个 |
| 18 | NC20260825001638 | 227 | 17 | 2 | 12 | 15/17 | 53% | UPFBINDSELRULE(6)、UPCMPT(6) |
| 19 | NC20260803000197 | 15 | 6 | 2 | 11 | 4/6 | 67% | TAIRANGELIST(8)、UPAREABINDN2TAI(3) |
| 20 | NC20260803002122 | 52 | 22 | 7 | 10 | 14/22 | 68% | PNFDNN(4)、NSDNN(1)、APNPCCFUNC(1)、APNUSRPROFG(1)、APNIDLETIME(1) 等 7 个 |
| 21 | NC20260907000242 | 30 | 16 | 4 | 6 | 13/16 | 75% | PCSCFIP(2)、PCSCFIMSISDNSEG(2)、PCSCFGROUP(1)、PCSCFGRPBNDAPN(1) |
| 22 | NC20260812000714 | 9 | 3 | 1 | 5 | 1/3 | 67% | PNFDNN(5) |
| 23 | NC20260817001781 | 2 | 1 | 1 | 2 | 0/1 | 0% | PNFDNN(2) |
| 24 | NC20260817001454 | 3 | 2 | 1 | 2 | 1/2 | 50% | UPNODE(2) |
| 25 | NC20260901002241 | 4 | 3 | 1 | 2 | 0/3 | 67% | UPNODE(2) |
| 26 | NC20260911001671 | 2 | 2 | 2 | 2 | 0/2 | 0% | SMCOMMTIMER(1)、AMFSOFTPARAOFBIT(1) |

## 四、TOP 10 工单的族级明细

### NC20260811002706（GT 1164 条 / 57 族，其中 UNC 族 30 个）

| 命令族 | 中文名 | GT条数 |
|---|---|---|
| CONNECTPLMN | 修改互联PLMN | 674 |
| PNFDNN | 删除对端NF的DNN信息 | 12 |
| HPLMN | 查询本地PLMN | 7 |
| USRPROFGROUP | 删除用户模板组 | 3 |
| UPBINDUPG | 增加用户模板组和用户模板的绑定关系 | 3 |
| NGCONNECTPLMN | 删除5G Connect PLMN | 2 |
| PCSCFGROUP | 增加P-CSCF组配置 | 2 |
| PCSCFIP | 增加P-CSCF地址配置 | 2 |
| APNDEACTQFPLCY | 删除基于APN去活用户面专有QoS Flow策略 | 2 |
| MMFUNC | 查询移动性管理扩展功能 | 1 |
| EMGCFG | 修改运营商紧急呼叫功能配置 | 1 |
| PGWRESEL | 删除本地P-GW重选策略 | 1 |
| SRVCCLMTPLCY | 查询SRVCC流程限制策略 | 1 |
| NGEMGSRVFUNC | 查询5G紧急服务功能 | 1 |
| NGEMGCFG | 增加运营商紧急呼叫功能配置 | 1 |
| AMFSOFTPARAOFBIT | 设置AMF软件参数比特位 | 1 |
| NGNILRPARA | 删除NI-LR功能参数 | 1 |
| NGMMFUNC | 设置5G移动性管理功能 | 1 |
| NSDNN | 删除网络切片支持的DNN | 1 |
| APNPCCFUNC | 查询APN PCC功能 | 1 |
| PCSCFGRPBNDAPN | 删除APN和P-CSCF组关联关系 | 1 |
| SMFEMGCFG | 查询运营商紧急呼叫会话功能配置 | 1 |
| APNIDLETIME | 查询APN空闲上下文定时器配置 | 1 |
| APNCHARGECTRL | 设置APN的计费配置 | 1 |
| DBPARAS | 设置DB参数 | 1 |
| SMFPDUREACT | 修改跨区域PDU会话重建策略 | 1 |
| USERPROFILELOCK | 设置用户模板的锁定 | 1 |
| CTXSTARTRATING | 设置给OCS/CHF发送的消息初始携带的计费属性 | 1 |
| USRPROFCHARGE | 查询User Profile的计费配置 | 1 |
| APNUSRPROFG | 查询APN用户模板组绑定关系 | 1 |

### NC20260828000360（GT 1035 条 / 49 族，其中 UNC 族 27 个）

| 命令族 | 中文名 | GT条数 |
|---|---|---|
| CONNECTPLMN | 修改互联PLMN | 677 |
| PNFDNN | 删除对端NF的DNN信息 | 10 |
| HPLMN | 查询本地PLMN | 7 |
| NGCONNECTPLMN | 删除5G Connect PLMN | 2 |
| PCSCFGROUP | 增加P-CSCF组配置 | 2 |
| PCSCFIP | 增加P-CSCF地址配置 | 2 |
| APNDEACTQFPLCY | 删除基于APN去活用户面专有QoS Flow策略 | 2 |
| UPBINDUPG | 增加用户模板组和用户模板的绑定关系 | 2 |
| USRPROFGROUP | 删除用户模板组 | 2 |
| MMFUNC | 查询移动性管理扩展功能 | 1 |
| EMGCFG | 修改运营商紧急呼叫功能配置 | 1 |
| PGWRESEL | 删除本地P-GW重选策略 | 1 |
| SRVCCLMTPLCY | 查询SRVCC流程限制策略 | 1 |
| NGEMGSRVFUNC | 查询5G紧急服务功能 | 1 |
| NGEMGCFG | 增加运营商紧急呼叫功能配置 | 1 |
| AMFSOFTPARAOFBIT | 设置AMF软件参数比特位 | 1 |
| NGNILRPARA | 删除NI-LR功能参数 | 1 |
| NGMMFUNC | 设置5G移动性管理功能 | 1 |
| NSDNN | 删除网络切片支持的DNN | 1 |
| APNPCCFUNC | 查询APN PCC功能 | 1 |
| PCSCFGRPBNDAPN | 删除APN和P-CSCF组关联关系 | 1 |
| SMFEMGCFG | 查询运营商紧急呼叫会话功能配置 | 1 |
| APNIDLETIME | 查询APN空闲上下文定时器配置 | 1 |
| APNCHARGECTRL | 设置APN的计费配置 | 1 |
| DBPARAS | 设置DB参数 | 1 |
| SMFPDUREACT | 修改跨区域PDU会话重建策略 | 1 |
| APNUSRPROFG | 查询APN用户模板组绑定关系 | 1 |

### NC20260823000103（GT 765 条 / 54 族，其中 UNC 族 27 个）

| 命令族 | 中文名 | GT条数 |
|---|---|---|
| CONNECTPLMN | 修改互联PLMN | 339 |
| NGCONNECTPLMN | 删除5G Connect PLMN | 12 |
| HPLMN | 查询本地PLMN | 7 |
| PCSCFIP | 增加P-CSCF地址配置 | 4 |
| PNFDNN | 删除对端NF的DNN信息 | 4 |
| PCSCFGROUP | 增加P-CSCF组配置 | 2 |
| APNDEACTQFPLCY | 删除基于APN去活用户面专有QoS Flow策略 | 2 |
| MMFUNC | 查询移动性管理扩展功能 | 1 |
| EMGCFG | 修改运营商紧急呼叫功能配置 | 1 |
| PGWRESEL | 删除本地P-GW重选策略 | 1 |
| SRVCCLMTPLCY | 查询SRVCC流程限制策略 | 1 |
| NGEMGSRVFUNC | 查询5G紧急服务功能 | 1 |
| NGEMGCFG | 增加运营商紧急呼叫功能配置 | 1 |
| AMFSOFTPARAOFBIT | 设置AMF软件参数比特位 | 1 |
| NGNILRPARA | 删除NI-LR功能参数 | 1 |
| NGMMFUNC | 设置5G移动性管理功能 | 1 |
| NSDNN | 删除网络切片支持的DNN | 1 |
| APNPCCFUNC | 查询APN PCC功能 | 1 |
| PCSCFGRPBNDAPN | 删除APN和P-CSCF组关联关系 | 1 |
| SMFEMGCFG | 查询运营商紧急呼叫会话功能配置 | 1 |
| APNIDLETIME | 查询APN空闲上下文定时器配置 | 1 |
| APNCHARGECTRL | 设置APN的计费配置 | 1 |
| DBPARAS | 设置DB参数 | 1 |
| SMFPDUREACT | 修改跨区域PDU会话重建策略 | 1 |
| USRPROFGROUP | 删除用户模板组 | 1 |
| UPBINDUPG | 增加用户模板组和用户模板的绑定关系 | 1 |
| APNUSRPROFG | 查询APN用户模板组绑定关系 | 1 |

### NC20260810002261（GT 436 条 / 53 族，其中 UNC 族 27 个）

| 命令族 | 中文名 | GT条数 |
|---|---|---|
| CONNECTPLMN | 修改互联PLMN | 343 |
| HPLMN | 查询本地PLMN | 7 |
| PCSCFIP | 增加P-CSCF地址配置 | 4 |
| PNFDNN | 删除对端NF的DNN信息 | 4 |
| NGCONNECTPLMN | 删除5G Connect PLMN | 3 |
| PCSCFGROUP | 增加P-CSCF组配置 | 2 |
| APNDEACTQFPLCY | 删除基于APN去活用户面专有QoS Flow策略 | 2 |
| MMFUNC | 查询移动性管理扩展功能 | 1 |
| EMGCFG | 修改运营商紧急呼叫功能配置 | 1 |
| PGWRESEL | 删除本地P-GW重选策略 | 1 |
| SRVCCLMTPLCY | 查询SRVCC流程限制策略 | 1 |
| NGEMGSRVFUNC | 查询5G紧急服务功能 | 1 |
| NGEMGCFG | 增加运营商紧急呼叫功能配置 | 1 |
| AMFSOFTPARAOFBIT | 设置AMF软件参数比特位 | 1 |
| NGNILRPARA | 删除NI-LR功能参数 | 1 |
| NGMMFUNC | 设置5G移动性管理功能 | 1 |
| NSDNN | 删除网络切片支持的DNN | 1 |
| APNPCCFUNC | 查询APN PCC功能 | 1 |
| PCSCFGRPBNDAPN | 删除APN和P-CSCF组关联关系 | 1 |
| SMFEMGCFG | 查询运营商紧急呼叫会话功能配置 | 1 |
| APNIDLETIME | 查询APN空闲上下文定时器配置 | 1 |
| APNCHARGECTRL | 设置APN的计费配置 | 1 |
| DBPARAS | 设置DB参数 | 1 |
| SMFPDUREACT | 修改跨区域PDU会话重建策略 | 1 |
| USRPROFGROUP | 删除用户模板组 | 1 |
| UPBINDUPG | 增加用户模板组和用户模板的绑定关系 | 1 |
| APNUSRPROFG | 查询APN用户模板组绑定关系 | 1 |

### NC20260820000552（GT 341 条 / 16 族，其中 UNC 族 15 个）

| 命令族 | 中文名 | GT条数 |
|---|---|---|
| BSFIPRANGEBIND | 查询BSF实例与IPRANGE之间的绑定关系 | 249 |
| TAIRANGELIST | 查询NF TAI区域信息 | 40 |
| UPBINDS11 | 修改SGW-U与SGW-C侧S11接口的绑定关系 | 20 |
| PEERNFIPLIST | 增加对端局向连接列表 | 7 |
| PNFDNN | 删除对端NF的DNN信息 | 5 |
| LOCBINDAREA | 查询UPF位置信息与该UPF优先支持的服务区的绑定关系 | 3 |
| PNFSMFSERAREA | 修改对端NF的SMF服务区域信息 | 3 |
| UPNODE | 修改UPF节点 | 2 |
| UPAREABINDN2TAI | 删除UPF服务区名称绑定的5G TAI范围 | 2 |
| UPAREA | 删除UPF服务区 | 2 |
| TACRANGE | 查询NF TAC区域信息 | 2 |
| PNFNS | 修改对端NF的切片信息 | 2 |
| PNFPROFILE | 删除对端NF实例概述信息 | 1 |
| UPIPDOMAIN | 增加当前UPF绑定的IP域 | 1 |
| PNFTAIRANGE | 查询对端NF的TAI范围 | 1 |

### NC20260806001438（GT 321 条 / 55 族，其中 UNC 族 28 个）

| 命令族 | 中文名 | GT条数 |
|---|---|---|
| PNFDNN | 删除对端NF的DNN信息 | 36 |
| CONNECTPLMN | 修改互联PLMN | 35 |
| VIRTUALAPNRULE | 查询虚拟APN映射策略配置 | 29 |
| APNDEACTQFPLCY | 删除基于APN去活用户面专有QoS Flow策略 | 20 |
| APNPCCFUNC | 查询APN PCC功能 | 10 |
| PCSCFGRPBNDAPN | 删除APN和P-CSCF组关联关系 | 10 |
| APNIDLETIME | 查询APN空闲上下文定时器配置 | 10 |
| APNCHARGECTRL | 设置APN的计费配置 | 10 |
| APNUSRPROFG | 查询APN用户模板组绑定关系 | 10 |
| HPLMN | 查询本地PLMN | 7 |
| NGCONNECTPLMN | 删除5G Connect PLMN | 2 |
| PCSCFGROUP | 增加P-CSCF组配置 | 2 |
| PCSCFIP | 增加P-CSCF地址配置 | 2 |
| MMFUNC | 查询移动性管理扩展功能 | 1 |
| EMGCFG | 修改运营商紧急呼叫功能配置 | 1 |
| PGWRESEL | 删除本地P-GW重选策略 | 1 |
| SRVCCLMTPLCY | 查询SRVCC流程限制策略 | 1 |
| NGEMGSRVFUNC | 查询5G紧急服务功能 | 1 |
| NGEMGCFG | 增加运营商紧急呼叫功能配置 | 1 |
| AMFSOFTPARAOFBIT | 设置AMF软件参数比特位 | 1 |
| NGNILRPARA | 删除NI-LR功能参数 | 1 |
| NGMMFUNC | 设置5G移动性管理功能 | 1 |
| NSDNN | 删除网络切片支持的DNN | 1 |
| SMFEMGCFG | 查询运营商紧急呼叫会话功能配置 | 1 |
| DBPARAS | 设置DB参数 | 1 |
| SMFPDUREACT | 修改跨区域PDU会话重建策略 | 1 |
| USRPROFGROUP | 删除用户模板组 | 1 |
| UPBINDUPG | 增加用户模板组和用户模板的绑定关系 | 1 |

### NC20260806001780（GT 412 条 / 41 族，其中 UNC 族 16 个）

| 命令族 | 中文名 | GT条数 |
|---|---|---|
| PNFDNN | 删除对端NF的DNN信息 | 28 |
| PCSCFIP | 增加P-CSCF地址配置 | 13 |
| PCSCFGRPBNDAPN | 删除APN和P-CSCF组关联关系 | 4 |
| PCSCFGROUP | 增加P-CSCF组配置 | 3 |
| APNDEACTQFPLCY | 删除基于APN去活用户面专有QoS Flow策略 | 2 |
| APNUSRPROFG | 查询APN用户模板组绑定关系 | 2 |
| PCSCFIMSISDNSEG | 修改IMSI和MSISDN号段 | 2 |
| NSDNN | 删除网络切片支持的DNN | 1 |
| APNPCCFUNC | 查询APN PCC功能 | 1 |
| SMFEMGCFG | 查询运营商紧急呼叫会话功能配置 | 1 |
| APNIDLETIME | 查询APN空闲上下文定时器配置 | 1 |
| APNCHARGECTRL | 设置APN的计费配置 | 1 |
| DBPARAS | 设置DB参数 | 1 |
| SMFPDUREACT | 修改跨区域PDU会话重建策略 | 1 |
| USRPROFGROUP | 删除用户模板组 | 1 |
| UPBINDUPG | 增加用户模板组和用户模板的绑定关系 | 1 |

### NC20260907000688（GT 209 条 / 12 族，其中 UNC 族 3 个）

| 命令族 | 中文名 | GT条数 |
|---|---|---|
| UPIPDOMAIN | 增加当前UPF绑定的IP域 | 36 |
| UPFBINDSELRULE | 修改UPF和规则的绑定关系 | 2 |
| UPCMPT | 删除UP节点协议兼容性配置 | 2 |

### NC20260907001683（GT 50 条 / 5 族，其中 UNC 族 2 个）

| 命令族 | 中文名 | GT条数 |
|---|---|---|
| UNCIPRESOUCE | 查询UNC接口IP地址 | 38 |
| PNFDNN | 删除对端NF的DNN信息 | 2 |

### NC20260828000409（GT 148 条 / 22 族，其中 UNC 族 5 个）

| 命令族 | 中文名 | GT条数 |
|---|---|---|
| PNFDNN | 删除对端NF的DNN信息 | 21 |
| APNRDSSVRGRP | 修改APN Radius服务器组 | 4 |
| APNUSRPROFG | 查询APN用户模板组绑定关系 | 4 |
| NSDNN | 删除网络切片支持的DNN | 4 |
| PNFNS | 修改对端NF的切片信息 | 2 |

## 五、UNC 独有族汇总

共 69 个 UNC 独有族。按命令数排序：

| 命令族 | 中文名 | 涉及工单数 | 总命令数 |
|---|---|---|---|
| CONNECTPLMN | 修改互联PLMN | 5 | 2068 |
| BSFIPRANGEBIND | 查询BSF实例与IPRANGE之间的绑定关系 | 1 | 249 |
| PNFDNN | 删除对端NF的DNN信息 | 16 | 148 |
| TAIRANGELIST | 查询NF TAI区域信息 | 2 | 48 |
| UPIPDOMAIN | 增加当前UPF绑定的IP域 | 3 | 41 |
| UNCIPRESOUCE | 查询UNC接口IP地址 | 1 | 38 |
| PCSCFIP | 增加P-CSCF地址配置 | 8 | 37 |
| HPLMN | 查询本地PLMN | 5 | 35 |
| APNDEACTQFPLCY | 删除基于APN去活用户面专有QoS Flow策略 | 6 | 30 |
| VIRTUALAPNRULE | 查询虚拟APN映射策略配置 | 1 | 29 |
| PCSCFGRPBNDAPN | 删除APN和P-CSCF组关联关系 | 8 | 28 |
| UPBINDS11 | 修改SGW-U与SGW-C侧S11接口的绑定关系 | 2 | 24 |
| APNUSRPROFG | 查询APN用户模板组绑定关系 | 10 | 23 |
| PNFSMFSERAREA | 修改对端NF的SMF服务区域信息 | 3 | 23 |
| PCSCFGROUP | 增加P-CSCF组配置 | 8 | 22 |
| NGCONNECTPLMN | 删除5G Connect PLMN | 5 | 21 |
| APNPCCFUNC | 查询APN PCC功能 | 9 | 18 |
| APNIDLETIME | 查询APN空闲上下文定时器配置 | 8 | 17 |
| APNCHARGECTRL | 设置APN的计费配置 | 8 | 17 |
| MMEIPTOMMEPOOL | 修改MME IP | 1 | 16 |
| SGWIPTOSGWPOOL | 删除SGW IP | 1 | 16 |
| PNFNS | 修改对端NF的切片信息 | 4 | 15 |
| NSDNN | 删除网络切片支持的DNN | 11 | 14 |
| UPNODE | 修改UPF节点 | 6 | 14 |
| USRPROFGROUP | 删除用户模板组 | 7 | 10 |
| UPBINDUPG | 增加用户模板组和用户模板的绑定关系 | 7 | 10 |
| UPFBINDSELRULE | 修改UPF和规则的绑定关系 | 2 | 8 |
| UPCMPT | 删除UP节点协议兼容性配置 | 2 | 8 |
| PEERNFIPLIST | 增加对端局向连接列表 | 1 | 7 |
| AMFSOFTPARAOFBIT | 设置AMF软件参数比特位 | 6 | 6 |
| SMFEMGCFG | 查询运营商紧急呼叫会话功能配置 | 6 | 6 |
| DBPARAS | 设置DB参数 | 6 | 6 |
| SMFPDUREACT | 修改跨区域PDU会话重建策略 | 6 | 6 |
| PCSCFIMSISDNSEG | 修改IMSI和MSISDN号段 | 3 | 6 |
| IMSIBINDUP | 查询用户和UPF的绑定关系 | 2 | 6 |
| MMFUNC | 查询移动性管理扩展功能 | 5 | 5 |
| EMGCFG | 修改运营商紧急呼叫功能配置 | 5 | 5 |
| PGWRESEL | 删除本地P-GW重选策略 | 5 | 5 |
| SRVCCLMTPLCY | 查询SRVCC流程限制策略 | 5 | 5 |
| NGEMGSRVFUNC | 查询5G紧急服务功能 | 5 | 5 |
| NGEMGCFG | 增加运营商紧急呼叫功能配置 | 5 | 5 |
| NGNILRPARA | 删除NI-LR功能参数 | 5 | 5 |
| NGMMFUNC | 设置5G移动性管理功能 | 5 | 5 |
| UPAREABINDN2TAI | 删除UPF服务区名称绑定的5G TAI范围 | 2 | 5 |
| PNFPROFILE | 删除对端NF实例概述信息 | 2 | 5 |
| APNRDSSVRGRP | 修改APN Radius服务器组 | 1 | 4 |
| LOCBINDAREA | 查询UPF位置信息与该UPF优先支持的服务区的绑定关系 | 1 | 3 |
| CTXSTARTRATING | 设置给OCS/CHF发送的消息初始携带的计费属性 | 2 | 2 |
| UPAREA | 删除UPF服务区 | 1 | 2 |
| TACRANGE | 查询NF TAC区域信息 | 1 | 2 |
| NGALMRPTMODE | 设置5G告警上报模式 | 1 | 2 |
| PNFSUPI | 查询对端NF的SUPI信息 | 1 | 2 |
| APNUPFINFO | 查询指定APN的UPF节点信息 | 1 | 2 |
| SRVNODERAT | 修改SGSN/SGW IP与RAT类型间的映射关系 | 1 | 2 |
| NFNS | 查询NF支持的网络切片 | 1 | 2 |
| APNUPSELPLY | 查询APN粒度的UP选择策略 | 2 | 2 |
| USERPROFILELOCK | 设置用户模板的锁定 | 1 | 1 |
| USRPROFCHARGE | 查询User Profile的计费配置 | 1 | 1 |
| PNFTAIRANGE | 查询对端NF的TAI范围 | 1 | 1 |
| NGCBSFUNC | 设置小区广播功能 | 1 | 1 |
| APNINTELSHUNT | 查询APN智能分流关键词 | 1 | 1 |
| SRVNODERATPRI | 查询获取RAT Type的优先级 | 1 | 1 |
| PLMNNS | 增加网络切片 | 1 | 1 |
| LOCALNSDNN | 增加网络切片或DNN纠正配置 | 1 | 1 |
| SMFFUNC | 查询SMF扩展功能 | 1 | 1 |
| PFCPPVTEXT | 设置PFCP私有信元携带配置 | 1 | 1 |
| GRPNGLANFUNC | 查询指定群组的5G LAN会话扩展参数 | 1 | 1 |
| BACKOFFTIME | 查询Back-off Time信息 | 1 | 1 |
| SMCOMMTIMER | 查询通用会话管理定时器参数 | 1 | 1 |

## 六、处理建议

| 措施 | 说明 | 预估效果 |
|---|---|---|
| **补齐 UNC 侧 EXP** | 按工单材料列出的网元清单，补充导出 UNC 的 EXP | 阶段1 覆盖 +15pp 左右 |
| 评估分层 | 对无 UNC EXP 的工单，UNC 族单独列出不参与评分 | 已有 EXP覆盖 列标注 |
| agent 提示 | 已在 prompt 加「本网元无法配置的项」要求 + G27 判据 | 已上线 |

**优先级：补齐 EXP 是数据层面的工作，代码侧已尽力。**