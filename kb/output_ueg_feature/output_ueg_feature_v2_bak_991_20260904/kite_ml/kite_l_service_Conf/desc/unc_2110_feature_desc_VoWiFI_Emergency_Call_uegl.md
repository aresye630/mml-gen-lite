# 激活VoWIFI紧急呼叫

- 操作场景
- 必备事项
- 操作步骤
- 任务示例

## 操作场景

在UEG上激活VoWiFi紧急呼叫功能，将紧急呼叫的用户接入WIFI网络。

目前UEG支持VoWiFi紧急呼叫功能，可以通过**ADD APN**的“EMERGENCYSWITCH”和“S6BEMERGCYSERVICE”参数分别配置开关和AAR消息是否携带Emergency Service标识。在Wi-Fi覆盖范围内且UE支持的情况下，针对VoWiFi紧急呼叫业务的处理方式是：在3GPP网络覆盖下，UE发起紧急呼叫时优先回落CS域进行处理。

**说明** 

适用于PGW-C。

## 必备事项

前提条件

- 请仔细阅读GWFD-025403 VoLTE紧急呼叫。
- 完成激活VoLTE紧急呼叫（适用于SGW-C/PGW-C）。
- 完成加载License。

数据

| 类别      | 参数名称                                        | 取值样例   | 获取方法     | 说明                              |
|:--------|:--------------------------------------------|:-------|:---------|:--------------------------------|
| ADD APN | APN名称（APN）                                  | sos    | 已配置数据中获取 | 规划使能紧急呼叫功能的APN实例。               |
| ADD APN | 支持紧急呼叫（EMERGENCYSWITCH）                     | ENABLE | 已配置数据中获取 | 是否使能VoWiFi紧急呼叫功能，默认值为“DISABLE”。 |
| ADD APN | S6b Emergency Service 标识（S6BEMERGCYSERVICE） | ENABLE | 本端规划     | 该参数仅在EMERGENCYSWITCH开启才能生效      |

## 操作步骤

1. 配置S/PGW-C数据

   使能VoWiFi紧急呼叫功能。

   在“MML命令行-UEG”窗口上执行命令

   **ADD APN**

   **说明** 

   若此APN上已有用户，则已接入的用户仍然按照普通APN处理，新接入的用户按照紧急呼叫用户处理。
2. 配置MME数据

   请参考激活LTE和WiFi网络之间的紧急呼叫切换

## 任务示例

任务描述

使能APN为“sos”的VoWiFi紧急呼叫功能。

脚本

使能VoWiFi紧急呼叫功能

在“MML命令行-UEG”窗口上执行命令

```
ADD CPAPN:APN="sos",EMERGENCYSWITCH=ENABLE,S6BEMERGCYSERVICE=ENABLE;
```