# 特性治理统计报告（自动提取 + 通用规则治理）

- 产品：UNC
- 特性总数：715 篇
- 治理状态：governed 715
- 置信度：high 409 / mid 224 / low 82
- 域分布（标题关键词猜测）：
  - 其他: 244
  - 部署: 161
  - 计费: 97
  - 接口: 52
  - 安全: 37
  - 路由: 31
  - 分流: 24
  - 容灾: 24
  - 地址分配: 15
  - 带宽控制: 13
  - 跟踪: 12
  - 切片: 5

- 含 license 授权开关的特性：161 篇（SET LICENSESWITCH/SOFTPARA 值锚定）

- **无 core 命令特性：82 篇**（纯公共/查询组合，需人工补指纹）
  - F009 备份网元数据（U2020/MAE）
  - F010 自动备份
  - F011 手动备份
  - F016 激活AMF Pool特性
  - F017 激活AMF Pool 用户迁移特性
  - F079 配置到MME的数据
  - F080 配置到SGW的数据
  - F107 查看应用性能统计结果
  - F110 激活Flash CSFB with RIM
  - F122 部署基于动态规则的分流策略控制
  - F137 配置会话级累计流量策略控制
  - F147 激活支持用户发起的二次激活
  - F153 USM GTPU接口跟踪
  - F175 配置UNC与安全扫描系统对接
  - F177 检查NSSF系统状态
  - F179 检查NSSF链路状态
  - F183 HTTP接口跟踪
  - F190 激活基于PCF的VoNR业务快速恢复
  - F200 证书与证书集管理
  - F215 DHCP接口跟踪
  - F221 检查漫游用户数
  - F224 激活WSFD-102601 LTE一键通基础功能（适用于PGW-C/SGW-C）
  - F226 检查用户漫游状态
  - F228 TM接口跟踪
  - F229 SGsR接口跟踪
  - F230 Rcap接口跟踪
  - F254 5G广播会话跟踪
  - F322 证书应用场景关联
  - F324 证书与证书集管理
  - F331 证书吊销列表管理
  - F370 安装后检查
  - F443 安装后检查
  - F444 安装后检查
  - F450 开启特性License开关
  - F459 媒体中继UPF选择结果验证
  - F476 配置专网UPF
  - F478 模块级KPI异常检测与恢复人工执行解除隔离操作
  - F501 用户跟踪
  - F502 配置用户跟踪净荷长度
  - F503 激活5G超高带宽基本功能及其高速承载接入
  - …… 其余 42 篇

## 域级自动收回（本域高频引用 + 跨域低引用 → prereq 收回 core.L3）

### 地址分配（17 条）
| 命令类型 | 域内特性引用数 | 域内引用率 |
|---|---|---|
| ADD L3VPNINST | 8 | 53% |
| ADD APN | 10 | 67% |
| ADD VPNINST | 12 | 80% |
| ADD OSPF | 10 | 67% |
| ADD OSPFAREA | 10 | 67% |
| ADD OSPFNETWORK | 10 | 67% |
| ADD UPNODE | 5 | 33% |
| ADD POOL | 9 | 60% |
| SET APNADDRESSATTR | 9 | 60% |
| ADD POOLGRPMAP | 11 | 73% |
| ADD ADDRPOOL | 7 | 47% |
| ADD ADDRPOOLGRP | 7 | 47% |
| ADD ADDRUPGROUP | 7 | 47% |
| ADD POOLBINDGRP | 7 | 47% |
| ADD UPFBINDGRP | 7 | 47% |
| SET IPALLOCRULE | 8 | 53% |
| ADD CONFLICTIP | 6 | 40% |

### 路由（5 条）
| 命令类型 | 域内特性引用数 | 域内引用率 |
|---|---|---|
| ADD L3VPNINST | 17 | 55% |
| ADD INTERFACE | 13 | 42% |
| ADD IPBINDVPN | 13 | 42% |
| ADD IFIPV4ADDRESS | 10 | 32% |
| SET BFD | 11 | 35% |

### 分流（4 条）
| 命令类型 | 域内特性引用数 | 域内引用率 |
|---|---|---|
| ADD USERPROFILE | 8 | 33% |
| ADD FLOWFILTER | 10 | 42% |
| SET SMFFUNC | 9 | 38% |
| ADD ULCLPROP | 8 | 33% |

### 计费（2 条）
| 命令类型 | 域内特性引用数 | 域内引用率 |
|---|---|---|
| SET APNCHARGECTRL | 38 | 39% |
| SET USRPROFCHARGE | 35 | 36% |

### 切片（1 条）
| 命令类型 | 域内特性引用数 | 域内引用率 |
|---|---|---|
| SET NGMMFUNC | 2 | 40% |


## L3 误归公共候选（频次 >40 但语义域内的业务命令，治理时收回 L3）

| 命令类型 | 被引用篇数 |
|---|---|
| SET LICENSESWITCH | 169 |
| ADD L3VPNINST | 65 |
| ADD VPNINSTAF | 65 |
| ADD APN | 53 |
| ADD RULE | 48 |
| ADD USERPROFILE | 44 |
| ADD LOGICIP | 42 |
| SET APNCHARGECTRL | 42 |
| ADD SERVICEIP | 40 |

> 治理动作：domain 修正 + L3 收回 + key_cmds 裁减 + status→approved
> 确认一批 → meta.version+1