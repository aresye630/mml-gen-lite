# 特性治理统计报告（自动提取 + 通用规则治理）

- 产品：UDG
- 特性总数：515 篇
- 治理状态：governed 515
- 置信度：high 281 / mid 159 / low 75
- 域分布（标题关键词猜测）：
  - 其他: 152
  - 部署: 88
  - 计费: 76
  - 路由: 51
  - 接口: 40
  - 地址分配: 30
  - 安全: 25
  - 带宽控制: 21
  - 跟踪: 11
  - 分流: 8
  - 容灾: 5
  - 隧道: 4
  - 语音: 2
  - NAT: 2

- 含 license 授权开关的特性：105 篇（SET LICENSESWITCH/SOFTPARA 值锚定）

- **无 core 命令特性：75 篇**（纯公共/查询组合，需人工补指纹）
  - F012 激活计费信息实时提醒
  - F033 激活Direct Tunnel功能
  - F039 激活EPS Fallback
  - F052 激活SRVCC
  - F100 备份网元数据（U2020/MAE）
  - F101 自动备份
  - F102 手动备份
  - F149 查看应用性能统计结果
  - F168 激活7层流量统计
  - F171 配置会话级累计流量策略控制
  - F183 配置UDG与安全扫描系统对接
  - F184 激活目的地址的NAT44转换
  - F192 证书与证书集管理
  - F194 激活VoNR基础语音业务
  - F195 GRP接口跟踪
  - F205 UDG 染色跟踪
  - F206 激活源地址的NAT64转换
  - F208 管理用户帐号
  - F209 检查漫游用户数
  - F215 UDG Tm3接口跟踪
  - F216 检查用户漫游状态
  - F233 UDG GCF接口跟踪
  - F234 激活网络加速卡流量加速单元
  - F247 HTTP接口跟踪
  - F253 配置NAT基本功能License开关
  - F303 安装后检查
  - F377 安装后检查
  - F378 UDG SWu接口跟踪
  - F387 UDG SWm接口跟踪
  - F393 卸载RELAY服务
  - F397 安装RELAY服务
  - F406 CDN随机跟踪
  - F412 配置专网UPF
  - F415 模块级KPI异常检测与恢复人工执行解除隔离操作
  - F419 安装CoreMind服务
  - F445 证书应用场景关联
  - F446 证书吊销列表管理
  - F447 检查补丁状态
  - F448 核对软件版本
  - F449 核查系统数据
  - …… 其余 35 篇

## 域级自动收回（本域高频引用 + 跨域低引用 → prereq 收回 core.L3）

### 地址分配（14 条）
| 命令类型 | 域内特性引用数 | 域内引用率 |
|---|---|---|
| ADD L3VPNINST | 13 | 43% |
| ADD VPNINST | 24 | 80% |
| ADD APN | 22 | 73% |
| ADD POOLGRPMAP | 23 | 77% |
| ADD POOL | 21 | 70% |
| ADD OSPF | 18 | 60% |
| ADD OSPFAREA | 18 | 60% |
| ADD POOLBINDGROUP | 16 | 53% |
| ADD POOLGROUP | 16 | 53% |
| SET IPALLOCRULE | 18 | 60% |
| ADD OSPFNETWORK | 18 | 60% |
| SET APNADDRESSATTR | 20 | 67% |
| SET APNIPALLOCRULE | 14 | 47% |
| ADD CONFLICTIP | 10 | 33% |

### 容灾（14 条）
| 命令类型 | 域内特性引用数 | 域内引用率 |
|---|---|---|
| ADD L3VPNINST | 2 | 40% |
| ADD INTERFACE | 2 | 40% |
| ADD IPBINDVPN | 2 | 40% |
| MOD INTERFACE | 2 | 40% |
| ADD IKEPROPOSAL | 2 | 40% |
| ADD INTERFACEIPSEC | 2 | 40% |
| ADD IPBINDVPNIPSEC | 2 | 40% |
| ADD IPSECINTFCFGIPSEC | 2 | 40% |
| ADD L3VPNINSTIPSEC | 2 | 40% |
| ADD ATTACHIKEPEER | 2 | 40% |
| ADD IPSECINTFCFG | 2 | 40% |
| ADD PROPATTACHIPSECPROPOSAL | 2 | 40% |
| SET IKEGLOBALCONFIG | 2 | 40% |
| SET IPFARMGLOBAL | 2 | 40% |

### 路由（8 条）
| 命令类型 | 域内特性引用数 | 域内引用率 |
|---|---|---|
| ADD L3VPNINST | 39 | 76% |
| ADD INTERFACE | 32 | 63% |
| ADD IPBINDVPN | 28 | 55% |
| ADD IFIPV4ADDRESS | 25 | 49% |
| SET BFD | 33 | 65% |
| ADD BGPVRF | 21 | 41% |
| SET BGP | 21 | 41% |
| ADD AUTOSCALINGETHTRUNK | 18 | 35% |

### 带宽控制（6 条）
| 命令类型 | 域内特性引用数 | 域内引用率 |
|---|---|---|
| ADD APN | 7 | 33% |
| ADD BWMCONTROLLER | 10 | 48% |
| ADD BWMRULE | 9 | 43% |
| ADD BWMUSERGROUP | 9 | 43% |
| ADD APNBINDBWMUSRG | 8 | 38% |
| ADD BWMSERVICE | 8 | 38% |

### 计费（2 条）
| 命令类型 | 域内特性引用数 | 域内引用率 |
|---|---|---|
| SET APNCHARGECTRL | 26 | 34% |
| SET USRPROFCHARGE | 24 | 32% |


## L3 误归公共候选（频次 >40 但语义域内的业务命令，治理时收回 L3）

| 命令类型 | 被引用篇数 |
|---|---|
| SET LICENSESWITCH | 107 |
| ADD L3VPNINST | 72 |
| ADD VPNINSTAF | 72 |
| ADD RULE | 64 |
| ADD VPNINST | 63 |
| ADD APN | 59 |
| ADD INTERFACE | 51 |
| ADD RULEBINDING | 49 |
| ADD PCCPOLICYGRP | 48 |
| ADD IPBINDVPN | 46 |
| SET REFRESHSRV | 45 |
| ADD URR | 45 |
| ADD FLOWFILTER | 44 |
| ADD USERPROFILE | 43 |
| ADD URRGROUP | 43 |
| ADD IFIPV4ADDRESS | 40 |

> 治理动作：domain 修正 + L3 收回 + key_cmds 裁减 + status→approved
> 确认一批 → meta.version+1