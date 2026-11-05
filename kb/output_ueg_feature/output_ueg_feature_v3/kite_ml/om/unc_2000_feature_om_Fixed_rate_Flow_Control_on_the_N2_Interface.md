# 激活N2接口固定速率流控功能

* 操作场景
* 必备事项
* 操作步骤
* 任务示例

## 操作场景

本操作指导介绍在运行网络中激活N2接口固定速率流控功能的操作过程。

适用于AMF。

## 必备事项

前提条件

该操作无需具备特殊条件。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **SET N2FIXEDFCBYMSG** | 流控消息类型（MSGTYPE） | REGISTER | 全网规划 | 设置N2接口上指定消息类型固定速率流控信息。 |
|  | 固定速率流控开关（FCSWITCH） | On |  |  |
|  | 流控速率门限(个/秒)（THRESHOLD） | 4000 |  |  |
| **SET AMFSOFTPARAOFBIT** | 数据类型（DT） | Dw | 全网规划 | （可选）开启寻呼范围为TA级别的寻呼消息固定速率流控功能。 |
|  | Dword索引（DWORDNUM） | 14 |  |  |
|  | 软参记录值（VALUE） | VALUE\_0 |  |  |
|  | 比特位（POSITION） | 30 |  |  |
| **SET AMFSOFTPARA** | 数据类型（DT） | Dw | 全网规划 | （可选）设置寻呼范围为TA级别的寻呼消息固定速率流控阈值。  说明：  此处阈值为举例值，请根据网络具体情况进行阈值设置。 |
|  | Dword索引（DWORDNUM） | 28 |  |  |
|  | Dword值（DWORDVALUE） | 80000 |  |  |

## 操作步骤

1. 进入“MML命令行-UEG”窗口。
2. 设置N2接口指定消息类型固定流控速率。

   **SET N2FIXEDFCBYMSG**
3. **可选：**设置软参DWORD14 BIT30值为0，开启寻呼范围为TA级别的寻呼消息固定速率流控功能。

   **SET AMFSOFTPARAOFBIT**
4. **可选：**通过软参DWORD28设置寻呼范围为TA级别的寻呼消息固定速率流控阈值。

   **SET AMFSOFTPARA**

## 任务示例

任务描述

在重大节日或大型活动时，某些TA下集中大量用户，可以预期大量语音呼叫同时发生，因此系统开启N2接口Paging消息和Service Request消息的固定速率流控功能，设置打开固定速率流控开关，并设置固定流控速率。AMF的N2接口上发送的Paging消息按照设定的固定流控速率发送，接收的Service Request消息按照设定的固定流控速率接入，对于超过门限的Service Request消息，UEG丢弃，并上报N2固定速率流控起控告警。

脚本

//针对Paging和Registration Request开启固定速率流控，速率门限是单Pod 4000个/秒。执行如下命令：

```
SET N2FIXEDFCBYMSG:MSGTYPE=PAGING,FCSWITCH=On,THRESHOLD=4000;
SET N2FIXEDFCBYMSG:MSGTYPE=SERVICEREQUEST,FCSWITCH=On,THRESHOLD=4000;
```

//（可选）设置软参DWORD14 BIT30值为0，开启寻呼范围为TA级别的寻呼消息固定速率流控功能。

```
SET AMFSOFTPARAOFBIT: DT=Dw, DWORDNUM=14, VALUE=VALUE_0, POSITION=30;
```

//（可选）通过软参DWORD28设置寻呼范围为TA级别的寻呼消息固定速率流控阈值。

```
SET AMFSOFTPARA: DT=Dw, DWORDNUM=28, DWORDVALUE=80000;
```

版权所有 © 华为技术有限公司
