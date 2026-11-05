# 激活AMF Pool特性

* 操作场景
* 必备事项
* 操作步骤
* 任务示例

## 操作场景

本操作指导介绍在运行网络中激活AMF Pool特性的操作过程。

AMF Pool是指多个AMF同时为相同的无线区域服务，Pool内的AMF与相应区域内所有gNodeB连接。Pool内AMF之间实现资源共享、业务负荷分担。gNodeB探测AMF的设备状态（是否可用）并获取AMF的负荷权重，根据设备状态及负荷权重来及时调整Pool的负荷均衡策略。

适用于AMF。

## 必备事项

前提条件

* 请仔细阅读GWFD-024201 AMF Pool特性概述。
* 在“初始配置 > 配置AMF”的时候，完成AMF全局标识配置，且Pool内所有AMF的“PLMNIDX”、“AMFREGIONID”和“AMFSETID”取值相同。
* 完成加载License。

数据

该操作无需准备数据。

## 操作步骤

1. 进入“MML命令行-UEG”窗口。
2. 打开本特性的License配置开关。

   SET LICENSESWITCH

## 任务示例

任务描述

AMF Pool中由AMF 1、AMF 2和AMF 3组成。需要分别在3个AMF上激活AMF Pool特性。

脚本

//AMF 1上的脚本：

//打开本特性的License配置开关。

```
SET LICENSESWITCH: LICITEM="LKV2AMFPL01", SWITCH=ENABLE;
```

//AMF 2上的脚本：

//打开本特性的License配置开关。

```
SET LICENSESWITCH: LICITEM="LKV2AMFPL01", SWITCH=ENABLE;
```

//AMF 3上的脚本：

//打开本特性的License配置开关。

```
SET LICENSESWITCH: LICITEM="LKV2AMFPL01", SWITCH=ENABLE;
```

版权所有 © 华为技术有限公司
