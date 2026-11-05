# 激活基于VoNR的优先语音服务

* 操作场景
* 必备事项
* 操作步骤
* 任务示例

## 操作场景

本操作指导介绍在运行网络中激活基于VoNR的优先语音服务的操作过程。

适用于SMF。

## 必备事项

前提条件

* 请仔细阅读GWFD-025703 基于VoNR的优先语音服务特性概述。
* 已部署VoNR基础语音业务，详细请参考GWFD-025701 VoNR基础语音业务。
* AMF上已根据PPI配置不同的寻呼定时器、重发次数和重呼间隔时间，生成差异化的寻呼策略，为语音业务配置高优先级的寻呼策略。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **ADD CPAPN** | APN名称（APN） | ims | 本端规划 | 开启PPI（寻呼策略指示）功能。 |
|  | PPISWITCH（PPI 功能开关） | ENABLE | 本端规划 |  |

## 操作步骤

1. 进入“MML命令行-UEG”窗口。
2. **可选：**通过 **ADD CPAPN**命令开启PPI功能。
3. 通过 **ADD CPAPN**命令中继承**SET SMFFUNC**命令中的全局配置开启PPI功能。

## 任务示例

任务描述

按照网络规划，需要将使用APN为ims的业务，在SMF上使能该APN的PPI功能开关，后续AMF可以根据PPI识别语音业务，实现语音的优先寻呼。

脚本

//脚本一：直接通过ADD CPAPN命令开启PPI功能。

```
ADD CPAPN:APN="ims", PPISWITCH=ENABLE;
```

//脚本二：通过ADD CPAPN命令中继承SET SMFFUNC命令中的全局配置开启PPI功能。

```
SET SMFFUNC:PPISWITCH=ENABLE;
ADD CPAPN:APN="ims", PPISWITCH=INHERIT;
```

版权所有 © 华为技术有限公司
