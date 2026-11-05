# 激活基于信令面的数据传输（SGW-C）

- 操作场景
- 必备事项
- 操作步骤
- 任务示例

## 操作场景

本操作指导介绍在运行网络中激活基于信令面的数据传输特性的操作过程。

**说明** 

适用于SGW-C

## 必备事项

前提条件

- 请仔细阅读GWFD-026105 基于信令面的数据传输特性概述（SGW-C）。
- 完成加载License。

数据

| 类别               | 参数名称            | 取值样例         | 获取方法   | 说明                                       |
|:-----------------|:----------------|:-------------|:-------|:-----------------------------------------|
| ADD CDRFIELDTEMP | TEMPLATENAME    | cdrfieldtemp | 本端规划   | 指定话单字段模板的名称。                             |
| ADD CDRFIELDTEMP | CPEPSOINDICATOR | ENABLE       | 本端规划   | 置话单中是否携带cp-eps-optimisation-indicator字段。 |
| ADD CDRFIELDTEMP | UNIPDUCPONLY    | ENABLE       | 本端规划   | 配置话单中是否携带uni-pdu-cp-only-flag字段。         |

## 操作步骤

1. 进入“MML命令行-UEG”窗口。
2. 打开本特性的License配置开关。

   **SET LICENSESWITCH**
3. **可选：**配置话单中是否携带CP CIoT EPS Optimisation Indicator、UNI PDU CP Only Flag字段。

   **ADD CDRFIELDTEMP**

## 任务示例

任务描述

在UEG上配置基于信令面的数据传输功能。

脚本

//打开本特性的License配置开关。

```
SET LICENSESWITCH:LICITEM="LKV3WPSDTO11",SWITCH=ENABLE;
```

//可选：配置话单中携带CP CIoT EPS Optimisation Indicator、UNI PDU CP Only Flag字段。

```
ADD CDRFIELDTEMP:TEMPLATENAME="cdrfieldtemp",CPEPSOINDICATOR=ENABLE,UNIPDUCPONLY=ENABLE;
```