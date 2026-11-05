# 激活基于eNodeB覆盖等级的寻呼

* 操作场景
* 必备事项
* 操作步骤
* 任务示例

## 操作场景

本操作指导介绍在运行网络中激活基于eNodeB覆盖等级的寻呼的操作过程。

随着物联网的广泛应用，智能终端也广泛部署在各种环境中，例如智能停车、智能抄表等大都部署在信号较弱或者没有信号的偏远郊区或者地下室，这就要求IoT基站深覆盖。目前IoT基站能够实现比LTE基站增强20dB寻呼终端，满足深覆盖需要。但并不是所有的终端都是位于覆盖较差的地方，若基站都是使用高覆盖等级进行寻呼，会导致容量下降，终端功耗增加。因此通过基于eNodeB覆盖等级(Coverage Enhancement Level)寻呼技术，将小区划分为不同的覆盖等级，根据小区信号进行等级寻呼，可节约空口资源，保证业务质量，节省终端电量。

适用于MME。

## 必备事项

前提条件

* 请仔细阅读GWFD-026110 基于eNodeB覆盖等级的寻呼特性概述。
* 部署WSFD-206001 精准寻呼特性

  若与WSFD-206001 精准寻呼特性一起部署，需要在MME上部署LTE精准寻呼特性，且**ADD S1PAGINGRULE**的参数“ACTGRP”配置包含“NEIGH\_ENODEB（邻接eNodeB）”，会基于eNodeB进行寻呼。单独部署时，会基于TA List进行寻呼。
* 完成加载License。

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

任务一：启用基于eNodeB覆盖等级的寻呼。

任务二：和精准寻呼一起部署，启动eNodeB覆盖等级的寻呼。

脚本

任务一：启用基于eNodeB覆盖等级的寻呼。

//配置eNodeB覆盖增强检查开关为打开。

```
SET M2MCTRL: CHK_ENB_CE_SW=ON;
```

//配置“Next Paging Area Scope 开关”为“YES”。

```
SET S1CMPT: NPAS=YES;
```

//打开本特性的License配置开关。

```
SET LICENSESWITCH: LICITEM="LKV2CELP01", SWITCH=ENABLE;
```

任务二：和精准寻呼一起部署，启动eNodeB覆盖等级的寻呼。

//配置eNodeB覆盖增强检查开关为打开。

```
SET M2MCTRL: CHK_ENB_CE_SW=ON;
```

//设置S1寻呼规则。

```
ADD S1PAGINGRULE: GRPTYPE=ALL_USER, SVRTYPE=S11_DOWNLINK, APNIND=SPEC_APN, MCC="123", MNC="03", APN="NBIOT.HUAWEI.COM", ACTGRP=LAST_ENODEB-1&NEIGH_ENODEB-1&LAST_TAI-1;
```

//设置MME重复发送Paging Request消息的最大次数。

```
SET NBEMM: N3413=3;
```

//设置精准寻呼定时器。

```
SET S1PAGINGCTRL: SUBT3413=5;
```

//打开本特性的License配置开关。

```
SET LICENSESWITCH: LICITEM="LKV2CELP01", SWITCH=ENABLE;
```

//打开MME支持LTE精准寻呼。

```
SET LICENSESWITCH: LICITEM="LKV2PRPG02", SWITCH=ENABLE;
```

版权所有 © 华为技术有限公司
