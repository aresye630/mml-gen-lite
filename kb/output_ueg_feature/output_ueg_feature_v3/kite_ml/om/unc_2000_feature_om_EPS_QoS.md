# 激活QoS与流量管理（适用于MME）

* 操作场景
* 必备事项
* 操作步骤
* 任务示例

## 操作场景

本操作指导介绍在运行网络中控制EPS QoS各项功能的启动和调整的操作过程。

在E-UTRAN网络和GERAN/UTRAN网络互操作过程中，UEG支持EPS（Evolved Packet System） QoS参数和Pre-Rel-8 QoS参数之间的映射，实现网络间的切换和重选。UEG支持承载级别、APN级别、终端级别的EPS QoS控制。

QoS与流量管理指UEG支持3GPP QoS，按照QoS等级对用户报文进行分类，还可以提供DiffServ，从而支持流量监管、拥塞管理、拥塞避免等多种QoS实现技术。

## 必备事项

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **SET R8QOSMAP** | QoS级别标识（QCI） | 1 | 全网规划 | 配置EPS QoS参数到Pre-Rel-8 QoS参数映射。 |
|  | 流量等级（TC） | CC |  |  |
|  | 最大SDU长度（MAXSDU） | 150 |  |  |
|  | 发送次序（DO） | ORDER |  |  |
|  | 发送错误SDU（DESDU） | NOT\_DETECT |  |  |
|  | 保留BER（RBER） | E\_RESIDUAL\_BIT\_ERR\_RATIO\_1 |  |  |
|  | SDU误码率（SDUER） | SDUER4 |  |  |
|  | 发送控制优先级（THPRI） | THPRI1 |  |  |
|  | 传递时延（TD） | 10 |  |  |
| **SET COMPATIBILITY** | H值（HARP） | 5 | 本端规划 | 配置QoS兼容性。 |
|  | M值（MARP） | 10 |  |  |
|  | 发送EPS QoS Extended-2（EPSQOSEXT2） | NO | 全网规划 |  |

## 操作步骤

1. 进入“MML命令行-UEG”窗口。
2. 增加EPS QoS参数到Pre-Rel-8 QoS参数映射规则。

   **SET R8QOSMAP**
3. 设置QoS兼容性（EPS ARP、Pre-Rel-8 ARP转换参数和EPS QoS Extended-2信元控制参数等）。

   **SET COMPATIBILITY**

## 任务示例

任务描述

增加一条QCI为1的EPS QoS参数到Pre-Rel-8 QoS参数的映射规则，当EPS QoS参数中的QCI为1时，映射到Pre-Rel-8 QoS参数的流量等级为Conversational class，最大SDU长度为150字节，发送次序存在，不检查发送错误SDU，保留BER为5×10-2，SDU误码率为1×10-4，QoS传递时延为10ms。同时设置EPS ARP和Pre-Rel-8 ARP转换参数H值为5，M值为10，EPS QoS Extended-2信元控制参数设置为关闭状态。

脚本

//增加EPS QoS参数到Pre-Rel-8 QoS参数的映射规则。

```
SET R8QOSMAP: QCI=1, TC=CC, MAXSDU=150, DO=ORDER, DESDU=NOT_DETECT, RBER=E_RESIDUAL_BIT_ERR_RATIO_1, SDUER=SDUER4, TD=10;
```

//设置QoS兼容性（EPS ARP、Pre-Rel-8 ARP转换参数和EPS QoS Extended-2信元控制参数等）。

```
SET COMPATIBILITY: HARP=5, MARP=10, EPSQOSEXT2=NO;
```

版权所有 © 华为技术有限公司
