# 激活eNodeB SON信息传送功能

* 操作场景
* 必备事项
* 操作步骤

## 操作场景

本操作指导介绍在运行网络中激活eNodeB SON信息传送功能特性的操作过程。

适用于MME。

本场景应用于eNodeB全部支持SON流程自动发现X2地址的组网。

如图1所示，eNodeB2和eNodeB3连接于同一个MME即MME2；eNodeB1连接于独立的MME1。eNodeB1与eNodeB2，eNodeB2与eNodeB3之间互为相邻，之间通过X2接口传递切换和eNodeB状态信息。

**图1** SON组网图

## 必备事项

前提条件

* 请仔细阅读GWFD-023104 eNodeB SON信息传送功能特性概述。
* 完成加载License。
* MME、eNodeB网元上首先完成基本业务的数据配置。S1–MME、S10接口的数据配置，按网络规划配置数据进行，具体请参见配置到eNodeB的数据、配置到MME的数据，本文不再赘述。

数据

该操作无需准备数据。

## 操作步骤

1. 打开本特性的License配置开关。

   进入“MML命令行-UEG”窗口。

   **SET LICENSESWITCH**

版权所有 © 华为技术有限公司
