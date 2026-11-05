# 激活终端省电PSM模式

* 操作场景
* 必备事项
* 操作步骤
* 任务示例

## 操作场景

本操作指导介绍在运行网络中激活终端省电PSM模式的操作过程。

随着物联网的发展，M2M广泛应用于智能抄表等领域。这些领域的M2M终端被置于某些固定位置，采用各种电池供电，这种情况对电池寿命要求较高。本特性可以在这类M2M终端无上行数传时，指示终端进入PSM（Power Saving Mode）。终端进入PSM后不再接收下行消息，达到省电的目的，从而提高电池的使用寿命。

适用于MME。

## 必备事项

前提条件

* 请仔细阅读GWFD-026103 终端省电PSM模式特性概述。
* 完成加载License。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **ADD M2MPLCY** | 用户范围（SUBRANGE） | IMSI\_PREFIX | 全网规划 | 为号段1用户增加M2M终端省电策略。 |
|  | IMSI前缀（IMSIPRE） | 123034801 |  |  |
|  | APNNI（APNNI） | HUAWEI1.com |  |  |
|  | PSM开关(PSMSW) | ON |  |  |
|  | Active Timer来源(ACTIVETIMERSRC) | USE\_MAXRSPTM\_OR\_UEREQ |  |  |
|  | 延迟发送(DELAYSEND) | NO（否） |  |  |
|  | 用户范围（SUBRANGE） | IMSI\_PREFIX |  | 为号段2用户增加M2M终端省电策略。 |
|  | IMSI前缀（IMSIPRE） | 123034802 |  |  |
|  | APNNI（APNNI） | HUAWEI1.com |  |  |
|  | PSM开关(PSMSW) | ON |  |  |
|  | Active Timer来源(ACTIVETIMERSRC) | USE\_MAXRSPTM |  |  |
|  | Active Timer定时器时长（秒）（ACTIVETIMER） | 180 |  |  |
|  | 延迟发送(DELAYSEND) | NO（否） |  |  |

## 操作步骤

1. 进入“MML命令行-UEG”窗口。
2. 配置M2M终端省电策略。

   **ADD M2MPLCY**

   对于处于PSM态的终端，当有下行短消息时，MME会通知上游网元终端不可达。当终端进入连接态后，HSS给短消息中心发送Alert Service Request消息触发短消息重发流程，此时由于短消息中心向EPC核心网下发的短消息存在延时，可能出现短消息下发至终端时，终端又再一次进入PSM态，导致短消息一直发送失败。因此若存在下行短消息的场景，参数“ACTIVETIMER”时长的设置需要和短消息中心协商。
3. 打开本功能的License配置开关。

   **SET LICENSESWITCH**

## 任务示例

任务描述

任务1：假设某行业用户APNNI为"HUAWEI1.com"，运营商为其分配了IMSI前缀为"123034801"的号段，Active Timer来源优先考虑从签约数据（来自HSS的Maximum Response Time或Active-Time）中获取，如果未签约则使用UE请求消息中的T3324信元为其赋值。

任务2：假设某行业用户APNNI为"HUAWEI1.com"，运营商为其分配了IMSI前缀为"123034802"的号段，Active Timer来源优先考虑从签约数据（仅考虑来自HSS的Maximum Response Time，不考虑Active-Time）中获取，如果未签约则使用系统配置的“Active Timer定时器时长(秒)”为其赋值。

脚本

任务1：

//配置M2M终端省电策略。

```
ADD M2MPLCY: SUBRANGE=IMSI_PREFIX, IMSIPRE="123034801", APNNI="HUAWEI1.com",PSMSW=ON,ACTIVETIMERSRC=USE_MAXRSPTM_OR_UEREQ, DELAYSEND=NO;
```

//将软参DWORD\_EX18 BIT8置为1。

```
SET SOFTPARAOFBIT: DT=DWORD_EX, PARANUM=18, VALUE=VALUE_1, POSITION=8;
```

//打开本功能的License配置开关。

```
SET LICENSESWITCH: LICITEM="LKV2M2MS01", SWITCH=ENABLE;
```

任务2：

//配置M2M终端省电策略。

```
ADD M2MPLCY: SUBRANGE=IMSI_PREFIX, IMSIPRE="123034802", APNNI="HUAWEI1.com",PSMSW=ON,ACTIVETIMERSRC=USE_MAXRSPTM, ACTIVETIMER=180, DELAYSEND=NO;
```

//将软参DWORD\_EX18 BIT8置为0。

```
SET SOFTPARAOFBIT: DT=DWORD_EX, PARANUM=18, VALUE=VALUE_0, POSITION=8;
```

//打开本功能的License配置开关。

```
SET LICENSESWITCH: LICITEM="LKV2M2MS01", SWITCH=ENABLE;
```

版权所有 © 华为技术有限公司
