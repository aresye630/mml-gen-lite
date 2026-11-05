# 激活eMTC基于eNodeB覆盖等级的寻呼

* 操作场景
* 必备事项
* 操作步骤
* 任务示例

## 操作场景

本操作指导介绍在运行网络中激活eMTC基于eNodeB覆盖等级的寻呼的操作过程。

基于eNodeB覆盖等级的寻呼，指MME根据eNodeB上报的推荐寻呼的eNodeB进行寻呼优化，并在寻呼消息中将eNodeB上报的推荐寻呼的小区和小区覆盖等级通过寻呼辅助信息传给eNodeB，用以支持eNodeB覆盖等级的寻呼。

适用于MME。

## 必备事项

前提条件

* 请仔细阅读GWFD-026303 eMTC基于eNodeB覆盖等级的寻呼特性概述。
* 已完成加载License。

数据

该操作无需准备数据。

## 操作步骤

1. 进入“MML命令行-UEG”窗口。
2. **可选：**配置“eNodeB覆盖增强检查开关”为“打开”。

   **SET M2MCTRL**

   当“eNodeB覆盖增强检查开关”为“打开”时，MME只向支持覆盖增强寻呼的eNodeB下发携带寻呼辅助信息（Assistance Data for Paging）信元的寻呼请求。关于此参数的详细说明请参考**SET M2MCTRL**。
3. **可选：**配置“Next Paging Area Scope开关”为“YES”。

   **SET S1CMPT**
4. 打开本功能的License配置开关。

   **SET LICENSESWITCH**

## 任务示例

任务描述

启用eMTC基于eNodeB覆盖等级的寻呼。

脚本

//配置eNodeB覆盖增强检查开关为打开。

```
SET M2MCTRL: CHK_ENB_CE_SW=ON;
```

//配置“Next Paging Area Scope开关”为“YES”。

```
SET S1CMPT: NPAS=YES;
```

//打开本特性的License配置开关。

```
SET LICENSESWITCH: LICITEM="LKV2CELP02", SWITCH=ENABLE;
```

版权所有 © 华为技术有限公司
