# 激活eMTC终端省电PSM模式

* 操作场景
* 对系统的影响
* 必备事项
* 操作步骤
* 任务示例

## 操作场景

本操作指导介绍在运行网络中激活eMTC终端省电PSM模式的操作过程。

随着物联网的发展，eMTC（enhanced Machine-Type Communications）广泛应用于智能抄表等领域。这些领域的eMTC终端被置于某些固定位置，采用各种电池供电，这种情况对电池寿命要求较高。本特性可以在这类eMTC终端无上行数传时，指示终端进入PSM（Power Saving Mode）。终端进入PSM后MME将拒绝周边网元对终端的寻呼请求，达到省电的目的，从而提高电池的使用寿命。

适用于MME。

## 对系统的影响

该操作对系统正常运行无影响。

## 必备事项

前提条件

* 请仔细阅读GWFD-026301 eMTC终端省电PSM模式特性概述。
* 已完成加载License。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **ADD M2MPLCY** | 用户范围（SUBRANGE） | IMSI\_PREFIX | 全网规划 | 增加eMTC终端省电策略 |
|  | IMSI前缀（IMSIPRE） | 123033601 |  |  |
|  | APNNI（APNNI） | HUAWEI1.com |  |  |
|  | PSM开关(PSMSW) | ON |  |  |
|  | Active Timer来源(ACTIVETIMERSRC) | USE\_CONFIG |  |  |
|  | Active Timer定时器时长（秒）（ACTIVETIMER） | 180 |  |  |
|  | 延迟发送（DELAYSEND） | NO |  |  |

## 操作步骤

1. 进入“MML命令行-UEG”窗口。
2. 配置eMTC终端省电策略。
   1. 查询某指定用户范围的省电策略配置。

      **LST M2MPLCY**

      对于处于PSM态的终端，当有下行短消息时，MME会通知上游网元终端不可达。当终端进入连接态后，HSS给短消息中心发送Alert Service Request消息触发短消息重发流程，此时由于短消息中心向EPC核心网下发的短消息存在延时，可能出现短消息下发至终端时，终端又再一次进入PSM态，导致短消息一直发送失败。因此若存在下行短消息的场景，参数“ACTIVETIMER”时长的设置需要和短消息中心协商。
   2. **可选：**如果步骤a未查询到该指定用户范围的相关配置，则执行此步骤，为该用户范围新配置省电策略。

      **ADD M2MPLCY**

      Active Timer定时器时长必须小于Periodic TAU Timer (T3412/T3412 extended)转化为秒之后的时长。
   3. **可选：**如果步骤a查询到系统已存在该指定用户范围的相关配置，则执行此步骤，修改其原有省电策略。

      **MOD M2MPLCY**
3. 打开本功能的License配置开关。

   **SET LICENSESWITCH**

## 任务示例

任务描述

假设某行业用户APNNI为“HUAWEI1.com”，运营商为其分配了IMSI前缀为“123033601”的号段，配置本特性。

脚本

//配置eMTC终端省电策略。

```
ADD M2MPLCY: SUBRANGE=IMSI_PREFIX, IMSIPRE="123033601", APNNI="HUAWEI1.com", PSMSW=ON,ACTIVETIMERSRC=USE_CONFIG, ACTIVETIMER=180, DELAYSEND=NO;
```

//打开本功能的License配置开关。

```
SET LICENSESWITCH: LICITEM="LKV2M2MS02", SWITCH=ENABLE;
```

版权所有 © 华为技术有限公司
