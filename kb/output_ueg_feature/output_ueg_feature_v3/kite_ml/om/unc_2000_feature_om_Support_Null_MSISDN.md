# 激活支持Null-MSISDN（适用于MME）

* 操作场景
* 必备事项
* 操作步骤
* 任务示例

## 操作场景

本操作指导介绍在运行网络中激活支持Null-MSISDN特性的操作过程。

支持Null-MSISDN特性是指UEG支持不携带MSISDN（Mobile Station International ISDN Number）的用户进行基本的移动性管理和会话管理业务，如附着、TAU/RAU、激活等。

适用于MME。

## 必备事项

前提条件

* 请仔细阅读GWFD-020913 支持Null-MSISDN特性概述。
* 已完成加载License，对应的License项为“82207024 LKV2NOISDN02 支持Null-MSISDN”。
* 移动网络中的相关网元（如P-GW、HSS等）打开Null MSISDN业务功能。

数据

该操作无需准备数据。

## 操作步骤

1. 打开本特性的License配置开关。

   进入“MML命令行-UEG”窗口。

   **SET LICENSESWITCH**

## 任务示例

任务描述

启用支持Null-MSISDN业务。

脚本

//打开License配置开关。

```
SET LICENSESWITCH: LICITEM="LKV2NOISDN02", SWITCH=ENABLE;
```

版权所有 © 华为技术有限公司
