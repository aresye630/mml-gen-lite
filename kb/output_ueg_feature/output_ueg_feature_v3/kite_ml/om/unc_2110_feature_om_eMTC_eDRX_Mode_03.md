# 激活eMTC eDRX模式（适用于SGW-C）

* 操作场景
* 必备事项
* 操作步骤
* 任务示例

## 操作场景

本操作指导介绍在运行网络中激活eMTC eDRX模式特性的操作过程。

适用于SGW-C

## 必备事项

前提条件

* 请仔细阅读GWFD-026302 eMTC eDRX模式特性概述（适用于SGW-C）。
* 已完成加载License。

数据

该操作无需准备数据。

## 操作步骤

1. 进入“MML命令行-UEG”窗口。
2. 打开本特性的License配置开关。

   **SET LICENSESWITCH**

## 任务示例

任务描述

在UEG上配置eMTC eDRX模式功能。

脚本

//打开本特性的License配置开关。

```
SET LICENSESWITCH:LICITEM="LKV3WMTDRX11",SWITCH=ENABLE;
```

版权所有 © 华为技术有限公司
