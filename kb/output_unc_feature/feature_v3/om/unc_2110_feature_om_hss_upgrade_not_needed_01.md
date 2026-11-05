# 激活HSS免升级

* 操作场景
* 必备事项
* 操作步骤
* 任务示例

## 操作场景

本操作指导介绍在运行网络中激活HSS免升级的操作过程。

在HSS未升级不支持NB-IoT终端接入、无法进行Non-IP数据传输的情况下，通过配置使MME发送给HSS可以识别的消息和信元，建立Non-IP的PDN上下文，保证NB-IoT终端成功接入网络，采用Non-IP Data Over NAS进行数据传输。

适用于MME。

## 必备事项

前提条件

* 请仔细阅读WSFD-215301 HSS免升级特性概述。
* 已完成加载License。

数据

| 类别 | 参数 | 取值样例 | 获取方法 | 相关命令 |
| --- | --- | --- | --- | --- |
| **SET DMCMPT** | 是否支持NB-IoT RAT（NBIOTRAT） | NOT\_SUPPORT | 全网规划 | S6a接口兼容性策略 |
| **ADD NONIPSUBCTRL** | 用户范围（SUBRANGE） | IMSI\_PREFIX | 全网规划 | 增加Non-IP APNNI配置 |
|  | IMSI前缀（IMSIPRE） | 12303 |  |  |
|  | 支持Non-IP的APNNI（SUPAPNNI） | ALL\_APNNI |  |  |

## 操作步骤

1. 进入“MML命令行-UNC”窗口。
2. 配置S6a接口兼容性策略。

   **SET DMCMPT**
3. **可选：**当HSS中未给用户签约Non-IP签约数据且需要使用Non-IP业务时，需要增加Non-IP APNNI配置。

   **ADD NONIPSUBCTRL**

   当“SUPAPNNI”选为“SPECIAL\_APNNI”时，需要先通过**ADD APNNIGROUP**和**ADD APNNI**来绑定APNNI组。
4. 打开本功能的License配置开关。

   **SET LICENSESWITCH**

## 任务示例

任务描述

对接HSS为HSS不能识别NB-IoT RAT且不支持Non-IP签约数据下发，启用HSS免升级。

脚本

//配置S6a接口兼容性策略“是否支持NB-IoT RAT”为“NOT\_SUPPORT”。

```
SET DMCMPT: NBIOTRAT=NOT_SUPPORT;
```

//增加Non-IP APNNI配置。

```
ADD NONIPSUBCTRL: SUBRANGE=IMSI_PREFIX, IMSIPRE="12303", SUPAPNNI=ALL_APNNI;
```

//打开本功能的License配置开关。

```
SET LICENSESWITCH: LICITEM="LKV2HUNN01", SWITCH=ENABLE;
```

版权所有 © 华为技术有限公司
