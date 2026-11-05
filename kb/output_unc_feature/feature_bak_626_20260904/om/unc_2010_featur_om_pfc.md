# 激活PFC（仅用于Gb 模式）

- 操作场景
- 必备事项
- 操作步骤
- 任务示例

## 操作场景

本操作指导介绍在运行网络中激活PFC（仅用于Gb模式）特性的操作过程。

PFC（Packet Flow Context）是指通过为同一用户的多个QoS相近的PDP分配相同的PFI（Packet Flow Identifier），实现数据流的捆绑传送。

**说明** 

适用于SGSN。

## 必备事项

前提条件

- 请仔细阅读WSFD-105101 PFC特性概述。
- 完成加载License。

- 需要对端网元PCU和GGSN激活PFC（仅用于Gb 模式）特性。
- 信令实体NSE（Network Service Entity）已经配置完成，具体步骤请参见配置到PCU的数据。

数据

该操作无需准备数据。

## 操作步骤

1. 进入“MML命令行-UNC”窗口。
2. 打开本特性的License配置开关。

   **SET LICENSESWITCH**
3. 修改信令实体，打开PFC开关。

   **MOD NSE**

   **说明** 

   参数“PFC”（是否支持PFC）选择“YES”（是）。

## 任务示例

任务描述

修改NSE信令实体，打开NSE标识为10的信令实体的PFC（仅用于Gb模式）功能开关。

脚本

//设置PFC（仅用于Gb模式）为“ENABLE(打开)”。

```
SET LICENSESWITCH: LICITEM="LKV2PFC02", SWITCH=ENABLE;
```

//修改NSE配置，支持PFC（仅用于Gb模式）功能。

```
MOD NSE: NSEI=10, PFC=YES;
```