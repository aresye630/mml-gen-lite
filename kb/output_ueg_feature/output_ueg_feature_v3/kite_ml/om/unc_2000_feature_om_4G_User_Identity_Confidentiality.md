# 激活用户身份保密性功能（适用于4G）

* 操作场景
* 必备事项
* 操作步骤
* 任务示例

## 操作场景

本操作指导介绍在运行网络中激活用户身份保密特性的操作过程。

用户身份保密性功能是通过GUTI的分配来实现。分配GUTI（Globally Unique Temporary UE Identity）的目的是为入网的用户提供一个临时标识，同时这个标识不会展现用户的永久性标识。

适用于MME

## 必备事项

前提条件

* 请仔细阅读GWFD-021504 用户身份保密性功能特性概述（适用于4G）。
* EPS网络中各网元系统及操作维护台运行正常。
* UE成功在UEG上附着。

数据

| 类别 | 参数 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **SET EMM** | GUTI重分配定时器（GUTITMR） | 1 | 全网规划 | 重分配GUTI的相关参数 |
|  | Attach或TAU中重分配GUTI（GUTIREALLOC） | YES | 全网规划 |  |
|  | GUTI重分配最大间隔(h)（GUTIREALLOCTMR） | 1 | 全网规划 |  |
| **SET CPSYS** | TMSI资源分配方式（TMSIALLOC） | ENHAN | 本端规划 | TMSI资源分配方式 |

## 操作步骤

1. 配置GUTI重分配策略。

   进入“MML命令行-UEG”窗口。

   **SET EMM**
2. 配置GUTI分配方式。

   系统默认采用增强TMSI分配方式，只有当增强算法存在无法解决的问题时，才使用非增强算法。为确保GUTI分配方式在各业务VM上的一致性，当执行此步骤修改GUTI分配方式后，需立即整系统重启。

   进入“MML命令行-UEG”窗口。

   ****SET CPSYS****

## 任务示例

任务描述

配置在Attach或TAU流程中使用增强TMSI算法重分配GUTI，重分配定时器时长和最大间隔均为1小时。

脚本

//配置GUTI重分配策略。

```
SET EMM:GUTITMR=1,GUTIREALLOC=YES,GUTIREALLOCTMR=1;
```

//配置GUTI分配方式。

```
SET CPSYS: TMSIALLOC=ENHAN;
```

版权所有 © 华为技术有限公司
