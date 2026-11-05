# 激活路径管理（适用于SGW-C/PGW-C/SMF）

- 操作场景
- 必备事项
- 操作步骤
- 任务示例

## 操作场景

本操作指导介绍在运行网络中激活路径管理特性的操作过程。

路径管理是指本端向对端发送相关信令，通过检查对端是否响应的方法来判断路径是否正常，从而及时清除无效路径的一种机制。

**说明** 

适用于SGW-C/PGW-C/SMF。

## 必备事项

前提条件

请仔细阅读WSFD-010600 路径管理特性概述。

数据

| 类别              | 参数名称                   | 取值样例           | 获取方法   | 说明                                                 |
|:----------------|:-----------------------|:---------------|:-------|:---------------------------------------------------|
| SET PFCPPARA    | 心跳间隔(秒)（HBINTERVAL）    | 30             | 本端规划   | 配置PFCP路径管理参数。 说明： 增加UPF粒度PFCP参数后，优先使用UPF粒度的PFCP参数。 |
| SET PFCPPARA    | 心跳消息超时间隔(秒)（HBT1）      | 3              | 本端规划   | 配置PFCP路径管理参数。 说明： 增加UPF粒度PFCP参数后，优先使用UPF粒度的PFCP参数。 |
| SET PFCPPARA    | 心跳消息发送次数阈值（HBN1）       | 5              | 本端规划   | 配置PFCP路径管理参数。 说明： 增加UPF粒度PFCP参数后，优先使用UPF粒度的PFCP参数。 |
| SET PFCPPARA    | 去活用户开关（DEACTIVEFLAG）   | ENABLE         | 本端规划   | 配置PFCP路径管理参数。 说明： 增加UPF粒度PFCP参数后，优先使用UPF粒度的PFCP参数。 |
| SET PFCPPARA    | 去活间隔(秒)（DACTINTERVAL）  | 900            | 本端规划   | 配置PFCP路径管理参数。 说明： 增加UPF粒度PFCP参数后，优先使用UPF粒度的PFCP参数。 |
| ADD UPFPFCPPARA | UPF实例标识（UPFINSTANCEID） | UPF_Instance_1 | 全网规划   | 配置PFCP路径管理参数。 说明： 增加UPF粒度PFCP参数后，优先使用UPF粒度的PFCP参数。 |
| ADD UPFPFCPPARA | 心跳间隔(秒)（HBINTERVAL）    | 60             | 本端规划   | 配置PFCP路径管理参数。 说明： 增加UPF粒度PFCP参数后，优先使用UPF粒度的PFCP参数。 |
| ADD UPFPFCPPARA | 心跳消息发送次数阈值（HBN1）       | 5              | 本端规划   | 配置PFCP路径管理参数。 说明： 增加UPF粒度PFCP参数后，优先使用UPF粒度的PFCP参数。 |
| ADD UPFPFCPPARA | 去活用户开关（DEACTIVEFLAG）   | ENABLE         | 本端规划   | 配置PFCP路径管理参数。 说明： 增加UPF粒度PFCP参数后，优先使用UPF粒度的PFCP参数。 |
| ADD UPFPFCPPARA | 去活间隔(秒)（DACTINTERVAL）  | 900            | 本端规划   | 配置PFCP路径管理参数。 说明： 增加UPF粒度PFCP参数后，优先使用UPF粒度的PFCP参数。 |
| ADD UPFPFCPPARA | 心跳消息超时间隔(秒)（HBT1）      | 3              | 本端规划   | 配置PFCP路径管理参数。 说明： 增加UPF粒度PFCP参数后，优先使用UPF粒度的PFCP参数。 |

## 操作步骤

1. 进入“MML命令行-UEG”窗口。
2. 配置SMF到UPF的心跳探测并开启故障场景下去活该UPF上用户会话的功能。

   **SET PFCPPARA**
3. 配置UPF粒度的SMF到UPF的心跳探测并开启故障场景下去活该UPF上用户会话的功能。

   **ADD UPFPFCPPARA**

## 任务示例

任务描述

设置SGW-C/PGW-C/AMF/SMF的PFCP路径探测机制，配置全局和基于UPF粒度两种机制。两个UPF对应的实例标识分别为UPF\_Instance\_0、UPF\_Instance\_1，其中对UPF\_Instance\_0的故障探测机制继承SMF全局探测机制，对UPF\_Instance\_1则需要单独的故障探测机制。

- 全局探测机制：将心跳间隔设置为30s，心跳超时间隔设置为3s，发送次数阈值设为5次，去活用户开关设置为开，去活间隔设置为900s。
- 基于UPF粒度的探测机制：将心跳间隔设置为60s，将心跳超时间隔设置为5s，发送次数阈值设为3次，去活用户开关设置为开，去活间隔设置为100s，迁移间隔设置为60s。

脚本

//配置SMF到UPF的心跳探测并开启故障场景下去活该UPF上用户会话的功能。

```
SET PFCPPARA: HBINTERVAL=30, HBT1=3, HBN1=5, DACTINTERVAL=900;
ADD UPFPFCPPARA: NFINSTANCENAME="UPF_Instance_1", HBINTERVAL=60, HBT1=5, HBN1=3, DEACTIVEFLAG=ENABLE
, DACTINTERVAL=100, MIGINTERVAL=60, CHECKFLAG=ENABLE;
```