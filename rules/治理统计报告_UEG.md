# 特性治理统计报告（自动提取 + 通用规则治理）

- 产品：UEG
- 特性总数：2343 篇
- 治理状态：governed 2343
- 置信度：high 950 / mid 701 / low 692
- 域分布（标题关键词猜测）：
  - 其他: 807
  - 部署: 291
  - 接口: 246
  - 安全: 244
  - 路由: 209
  - 语音: 120
  - 带宽控制: 80
  - 跟踪: 71
  - 计费: 68
  - 容灾: 54
  - 地址分配: 50
  - 隧道: 40
  - NAT: 27
  - 分流: 19
  - 切片: 15
  - 负载均衡: 2

- 含 license 授权开关的特性：355 篇（SET LICENSESWITCH/SOFTPARA 值锚定）

- **无 core 命令特性：692 篇**（纯公共/查询组合，需人工补指纹）
  - F001 更新物理数据库帐户密码
  - F002 配置HTTPS安全协议（SOAP）
  - F003 配置HTTPS安全协议（WebLMT）
  - F004 配置PGW的接入权限
  - F005 配置PGW Web LMT的安全策略
  - F006 配置TLS安全协议（MML）
  - F008 配置PGW HTTPS数字证书
  - F009 配置MML的SSH接入
  - F010 配置业务发放系统的安全接入策略
  - F011 配置LAS TLS数字证书
  - F012 增加用户
  - F013 修改PGW Web LMT操作员密码
  - F014 删除用户
  - F015 增加命令组
  - F016 删除命令组
  - F017 修改用户操作权限
  - F018 修改用户操作时段
  - F019 修改用户重复登录权限
  - F020 修改用户状态
  - F021 手动解锁用户
  - F022 切换PGW Web LMT访问方式
  - F030 激活EPS Fallback
  - F045 配置Sa/N3/S1-U接口数据
  - F046 配置Sa/N3/S1-U接口数据
  - F047 配置Sa/N3/S1-U接口数据
  - F048 配置Sa/N3/S1-U接口数据
  - F049 配置Sa/N3/S1-U接口数据
  - F050 配置Sa/N3/S1-U接口数据
  - F051 配置Sc/N9c/S5-S/S8-S接口数据
  - F052 配置Sc/N9c/S5-S/S8-S接口数据
  - F053 配置Sc/N9c/S5-S/S8-S接口数据
  - F054 配置Pa(N9a/S5-P/S8-P/S2b)接口数据
  - F055 配置Pa(N9a/S5-P/S8-P/S2b)接口数据
  - F056 配置Pa(N9a/S5-P/S8-P/S2b)接口数据
  - F057 配置Pa(N9a/S5-P/S8-P/S2b)接口数据
  - F058 配置Pa(N9a/S5-P/S8-P/S2b)接口数据
  - F059 配置Pa(N9a/S5-P/S8-P/S2b)接口数据
  - F060 配置N4(N4/Sxa/Sxb)接口数据
  - F061 配置N4(N4/Sxa/Sxb)接口数据
  - F062 配置N4(N4/Sxa/Sxb)接口数据
  - …… 其余 652 篇

## 域级自动收回（本域高频引用 + 跨域低引用 → prereq 收回 core.L3）

### 隧道（10 条）
| 命令类型 | 域内特性引用数 | 域内引用率 |
|---|---|---|
| ADD FLTBINDFLOWF | 13 | 32% |
| ADD GRETUNNEL | 27 | 68% |
| ADD VTEP | 13 | 32% |
| ADD VTEPBINDGRP | 13 | 32% |
| ADD NETWORKROUTE | 27 | 68% |
| ADD VXLANGRP | 13 | 32% |
| ADD VXLANBINDAPN | 13 | 32% |
| MOD GRETUNNEL | 20 | 50% |
| SET APNTRAFDFUNC | 13 | 32% |
| ADD VXLANBINDRULE | 13 | 32% |

### 地址分配（9 条）
| 命令类型 | 域内特性引用数 | 域内引用率 |
|---|---|---|
| ADD POOLBINDGROUP | 27 | 54% |
| ADD POOLGROUP | 27 | 54% |
| ADD OSPF | 26 | 52% |
| ADD OSPFAREA | 26 | 52% |
| SET APNADDRESSATTR | 31 | 62% |
| ADD POOL | 21 | 42% |
| ADD OSPFNETWORK | 26 | 52% |
| SET IPALLOCRULE | 28 | 56% |
| SET APNIPALLOCRULE | 23 | 46% |

### 带宽控制（5 条）
| 命令类型 | 域内特性引用数 | 域内引用率 |
|---|---|---|
| ADD BWMCONTROLLER | 52 | 65% |
| ADD BWMUSERGROUP | 52 | 65% |
| ADD BWMRULE | 52 | 65% |
| ADD BWMSERVICE | 52 | 65% |
| ADD APNBINDBWMUSRG | 50 | 62% |

### 分流（5 条）
| 命令类型 | 域内特性引用数 | 域内引用率 |
|---|---|---|
| ADD FLTBINDFLOWF | 6 | 32% |
| ADD L7FILTER | 6 | 32% |
| SET COLOCATEDLBO | 6 | 32% |
| ADD FLOWFILTERGRP | 6 | 32% |
| ADD HOST | 6 | 32% |

### 切片（4 条）
| 命令类型 | 域内特性引用数 | 域内引用率 |
|---|---|---|
| ADD NFNS | 8 | 53% |
| ADD PLMNNS | 8 | 53% |
| ADD SNSSAI | 5 | 33% |
| ADD SNSSAIUPINTF | 5 | 33% |

### 计费（3 条）
| 命令类型 | 域内特性引用数 | 域内引用率 |
|---|---|---|
| ADD FLTBINDFLOWF | 26 | 38% |
| SET REFRESHSRV | 30 | 44% |
| ADD PCCPOLICYGRP | 31 | 46% |

### 语音（3 条）
| 命令类型 | 域内特性引用数 | 域内引用率 |
|---|---|---|
| ADD UPNODE | 54 | 45% |
| ADD PNFUPFINFO | 54 | 45% |
| ADD UPAREABINDS1TAI | 42 | 35% |

### NAT（2 条）
| 命令类型 | 域内特性引用数 | 域内引用率 |
|---|---|---|
| SET FWSOFTPARA | 17 | 63% |
| OPR ONECLICKDEPLOY | 9 | 33% |

### 容灾（2 条）
| 命令类型 | 域内特性引用数 | 域内引用率 |
|---|---|---|
| SET DRKEYNF | 21 | 39% |
| SET DRCOUPLINGRESET | 17 | 31% |


## L3 误归公共候选（频次 >40 但语义域内的业务命令，治理时收回 L3）

| 命令类型 | 被引用篇数 |
|---|---|
| SET LICENSESWITCH | 363 |
| ADD INTERFACE | 358 |
| ADD IPBINDVPN | 354 |
| ADD L3VPNINST | 332 |
| ADD VPNINSTAF | 331 |
| ADD IFIPV4ADDRESS | 327 |
| ADD VPNINST | 318 |
| SET IFIPV6ENABLE | 249 |
| ADD IFIPV6ADDRESS | 243 |
| MOD INTERFACE | 220 |
| SET BFD | 210 |
| ADD IMPORTROUTE | 202 |
| ADD BGPVRF | 199 |
| ADD LOGICINF | 195 |
| ADD BGPVRFAF | 193 |
| ADD BGPPEER | 193 |
| ADD SRROUTE | 172 |
| ADD ETHSUBIF | 159 |
| ADD APN | 155 |
| SET BGP | 141 |
| ADD PNFDNN | 130 |
| ADD SRROUTE6 | 120 |
| ADD BFDSESSION | 119 |
| ADD FLOWFILTER | 116 |
| SET AUTOCONFIG | 116 |
| ADD UPAREABINDN2TAI | 115 |
| ADD PNFSMFSERAREA | 114 |
| ADD UPAREA | 114 |
| ADD RULE | 113 |
| ADD AUTOSCALINGSERVICE | 112 |

> 治理动作：domain 修正 + L3 收回 + key_cmds 裁减 + status→approved
> 确认一批 → meta.version+1