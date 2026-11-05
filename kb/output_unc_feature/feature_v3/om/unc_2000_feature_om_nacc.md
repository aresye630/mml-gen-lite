# 激活NACC

* 操作场景
* 必备事项
* 操作步骤

## 操作场景

本操作指导介绍在运行网络中激活NACC特性的操作过程。

NACC（Network Assisted Cell Change）特性是指UE需要在执行小区改变前，如果目标小区属于不同的接入设备，且接入设备间无法传递接入参数信息时，则需要核心网设备UNC辅助完成接入参数信息在两个接入设备之间的传递。

适用于SGSN、MME。

## 必备事项

前提条件

* 请仔细阅读MOD NSE
* 完成加载License。

数据

该操作无需准备数据。

## 操作步骤

1. 进入“MML命令行-UNC”窗口。
2. 打开本特性的License配置开关。

   **SET LICENSESWITCH**
3. 在GERAN网络下需打开RIM功能。

   如果NSE为静态配置，通过**MOD NSE**修改“是否支持RIM”参数打开RIM功能。

   如果NSE为动态配置，找到其对应的NSE属性模板，通过**MOD GBNSECFGPARA**修改“是否支持RIM”参数打开RIM功能。

   * 执行**MOD NSE**或**MOD GBNSECFGPARA**命令修改相关参数时，SGSN会复位相关SIGBVC信令实体；但是如果相关参数的对应功能在BSC侧是关闭的，在SGSN侧是开启的，这种情况下在SGSN侧关闭这些功能，SGSN不会复位SIGBVC信令实体。
   * 如果修改NSE的任意一个或多个参数取值，会导致SGSN主动发起针对该NSE的BVC-RESET流程，导致该NSE下的小区重新上报，引起业务短暂中断。但是如果相关参数的对应功能在BSC侧是关闭的，在SGSN侧是开启的，这种情况下在SGSN侧关闭这些功能，SGSN不会复位SIGBVC信令实体。

版权所有 © 华为技术有限公司
