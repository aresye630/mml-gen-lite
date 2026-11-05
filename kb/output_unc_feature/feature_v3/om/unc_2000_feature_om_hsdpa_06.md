# 激活HSDPA功能及其扩展包

* 操作场景
* 必备事项
* 操作流程
* 操作步骤
* 任务示例

## 操作场景

本操作指导介绍在运行网络中激活HSDPA功能及其扩展包的操作过程。

HSDPA(High Speed Downlink Packet Access)功能, 2M-4M特性可以使终端用户可以享受新的应用业务和更快的下载速度。该特性可以使SGSN为UE提供的最大下行速率为4Mbit/s。

适用于SGSN、GGSN。

## 必备事项

前提条件

* 请仔细阅读HSDPA功能及其扩展包特性概述。
* 完成加载License。

* 需要对端网元UE、RNC、GGSN、HLR支持HSDPA功能及其扩展包。
* 终端 (手机或者数据卡)支持协议版本R5及R5以上。
* SGSN、GGSN以及在HLR中的开户信息均需支持到用户希望的最大速率。

数据

需要准备与对端网元协商和全网规划的数据

## 操作流程

激活HSDPA功能及其扩展包操作流程如图1 激活HSDPA功能及其扩展包操作流程所示。

**图1** 激活HSDPA功能及其扩展包操作流程

## 操作步骤

1. 进入“MML命令行-UNC”窗口。
2. 打开本功能集的License配置开关。

   **SET LICENSESWITCH**
3. **（可选）**不限定QoS为R5规定的最大下行速率。

   **SET COMPATIBILITY**

   本步骤仅需HSDPA扩展包3–6功能进行设置。
4. 设置特定RNC的QoS支持版本。

   * 在HSDPA扩展包2中:**MOD RNC**
   * 在HSDPA扩展包3–6中:**MOD RNC**
   * 在HSDPA扩展包3–6中:**MOD RNC**
5. 设置特定GGSN的QoS支持版本。

   **ADD GGSNCHARACT**

   * 不支持IPT地址类型为IPV6，因此参数“IPT”（IP地址类型）固定设置为“IPV4”。
   * 在HSDPA扩展包3–6中，设置GGSN支持的QoS版本为R7QoS，参数“QoSVER”（SGSN支持的QoS版本）固定选择“R7QoS”。
6. 设置特定SGSN的QoS支持版本。

   **ADD SGSNCHARACT**

   * 不支持IPT地址类型为IPV6，因此参数“IPT”（IP地址类型）固定设置为“IPV4”。
   * 在HSDPA扩展包3–6中，设置SGSN支持的QoS版本为R7QoS，“QoSVER”（SGSN支持的QoS版本）固定选择“R7QoS”。
7. 设置SGSN支持的下行速率和保证下行速率为用户所购买License所支持的最大值。
   1. **可选：**全部用户

      * HSDPA功能, 2M-4M:

        **MOD IMSISMCHAR**
      * HSDPA扩展包1, 4M-8M:

        **MOD IMSISMCHAR**
      * HSDPA扩展包2, 8M-16M:

        **MOD IMSISMCHAR**
      * HSDPA扩展包3, 16M-32M:

        **MOD IMSISMCHAR**
      * HSDPA扩展包4, 32M-48M:

        **MOD IMSISMCHAR**
      * HSDPA扩展包5, 48M-84M:

        **MOD IMSISMCHAR**
      * HSDPA扩展包6, 84M-168M:

        **MOD IMSISMCHAR**

      其中参数“MBRDNLK3G”、“GBRDNLK3G”、“MBRDNLKEX3G”和“GBRDNLKEX3G”为固定配置值，不建议修改。
   2. **可选：**部分用户

      * HSDPA功能, 2M-4M:

        **ADD IMSISMCHAR**
      * HSDPA扩展包1, 4M-8M:

        **ADD IMSISMCHAR**
      * HSDPA扩展包2, 8M-16M:

        **ADD IMSISMCHAR**
      * HSDPA扩展包3, 16M-32M:

        **ADD IMSISMCHAR**
      * HSDPA扩展包4, 32M-48M:

        **ADD IMSISMCHAR**
      * HSDPA扩展包5, 48M-84M:

        **ADD IMSISMCHAR**
      * HSDPA扩展包6, 84M-168M:

        **ADD IMSISMCHAR**

      其中参数“MBRDNLK3G”、“GBRDNLK3G”、“MBRDNLKEX3G”和“GBRDNLKEX3G”为固定配置值，不建议修改。

## 任务示例

任务描述

配置所有GGSN和SGSN的QoS版本为R99（默认值为R99QOS），设置特定RNC的QoS支持版本为R99，配置SGSN支持的下行速率为最大值为183(4Mbps)。

脚本

//打开License配置开关。

```
SET LICENSESWITCH: LICITEM="LKV2HD16M02", SWITCH=ENABLE;
```

//设置特定RNC的QoS支持版本为R99。

```
MOD RNC: RNCX=1, RNCVER=R99;
```

//设置GGSN的QoS支持版本为R5，GGSN的信令面IP地址为10.10.10.1，掩码为255.255.255.255。

```
ADD GGSNCHARACT: RANGE=SPECIAL_GGSN, IPT=IPV4, GGSNIPV4="10.10.10.1", MASKV4="255.255.255.255", QOSVER=R5QOS;
```

//设置SGSN的QoS支持版本为R5，SGSN的信令面IP地址为10.10.11.1，掩码为255.255.255.255。

```
ADD SGSNCHARACT: RANGE=SPECIAL_SGSN, IPT=IPV4, IPV4="10.10.11.1", MASKV4="255.255.255.255", QOSVER=R5QOS;
```

//设置SGSN支持的扩展下行速率和保证下行速率为最大值183(4Mbps)。

```
MOD IMSISMCHAR: SUBRANGE=ALL_USER, APNNI="000001", UEACCCAP=ALL_UE, QOS2G=NO, QOS3G=YES, MBRDNLKEX3G=183, GBRDNLKEX3G=183;
```

版权所有 © 华为技术有限公司
