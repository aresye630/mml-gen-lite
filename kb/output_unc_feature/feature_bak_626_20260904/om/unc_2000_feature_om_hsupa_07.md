# 激活HSUPA功能及其扩展包

- 操作场景
- 必备事项
- 操作流程
- 操作步骤
- 任务示例

## 操作场景

本操作指导介绍在运行网络中激活HSUPA功能及其扩展包的操作过程。

**说明** 

适用于SGSN、GGSN。

## 必备事项

前提条件

- 请仔细阅读HSUPA功能及其扩展包特性概述。
- 完成加载License。

- 需要对端网元MS、RNC、GGSN、HLR已经激活HSUPA功能及其扩展包功能。

数据

需要准备与对端网元协商和全网规划的数据

## 操作流程

激活HSUPA功能及其扩展包操作流程如图1 激活HSUPA功能及其扩展包操作流程所示。

**图1** 激活HSUPA功能及其扩展包操作流程

## 操作步骤

1. 进入“MML命令行-UNC”窗口。
2. 打开本功能集的License配置开关。

   **SET LICENSESWITCH**
3. 设置特定RNC的QoS支持版本。

   **MOD RNC**

   **说明** 

   - 在HSUPA功能及其扩展包1中，QoS版本为R99及以上版本。
   - 在HSDPA扩展包2中，参数“RNCVER”参数必须设置为R5及以上QoS版本。
   - 在HSUPA扩展包2–3中，参数“RNCVER”（RNC的协议版本）必须设置为“R7”，即RNC的协议版本为R7。
   - 在HSUPA扩展包2–3中，参数“R7QoS”（RNC是否支持R7 QoS）必须设置为“YES”，即RNC支持R7 QoS。
4. 设置特定GGSN的QoS版本为R99及以上版本。

   **ADD GGSNCHARACT**

   **说明** 

   - 不支持IPT地址类型为IPV6，因此参数“IPT”（IP地址类型）固定设置为“IPV4”。
   - 在HSUPA扩展包2–3中，设置GGSN支持的QoS版本为R7QoS，参数“QoSVER”（GGSN支持的QoS版本）固定选择“R7QoS”。
5. 设置特定SGSN的QoS版本为R99及以上版本。

   **ADD SGSNCHARACT**

   **说明** 

   - 不支持IPT地址类型为IPV6，因此参数“IPT”（IP地址类型）固定设置为“IPV4”。
   - 在HSUPA扩展包3–6中，设置SGSN支持的QoS版本为R7QoS，“QoSVER”（SGSN支持的QoS版本）固定选择“R7QoS”。
6. 设置SGSN支持的最大上行扩展比特率和保证上行扩展比特率为用户所购买License所支持的最大值
   1. **可选：**全部用户

      - HSUPA功能, 2M-4M:

        **MOD IMSISMCHAR**
      - HSUPA扩展包1, 4M-8M:

        **MOD IMSISMCHAR**
      - HSUPA扩展包2, 8M-12M:

        **MOD IMSISMCHAR**
      - HSUPA扩展包3, 12M-24M:

        **MOD IMSISMCHAR**

      **说明** 

      其中参数“MBRDNLK3G”、“GBRDNLK3G”、“MBRDNLKEX3G”和“GBRDNLKEX3G”为固定配置值，不建议修改。
   2. **可选：**部分用户

      - HSUPA功能, 2M-4M:

        **ADD IMSISMCHAR**
      - HSUPA扩展包1, 4M-8M:

        **ADD IMSISMCHAR**
      - HSUPA扩展包2, 8M-12M:

        **ADD IMSISMCHAR**
      - HSUPA扩展包3, 12M-24M:

        **ADD IMSISMCHAR**

      **说明** 

      其中参数“MBRDNLK3G”、“GBRDNLK3G”、“MBRDNLKEX3G”和“GBRDNLKEX3G”为固定配置值，不建议修改。

## 任务示例

任务描述

配置所有GGSN和SGSN的QoS版本为R7，设置特定RNC的QoS支持版本为R7，配置SGSN支持的最大上行扩展比特率和保证上行扩展比特率为最大值32(11.52Mbps)。

脚本

//打开License配置开关。

```
SET LICENSESWITCH: LICITEM="LKV2HSPAUL02", SWITCH=ENABLE;
```

//设置特定RNC支持的QoS版本和协议版本为R7。

```
MOD RNC: RNCX=1, RNCVER=R7, R7QOS=YES;
```

//设置GGSN的QoS支持版本为R7，GGSN的信令面IP地址为10.10.10.1，掩码为255.255.255.255。

```
ADD GGSNCHARACT: RANGE=SPECIAL_GGSN, IPT=IPV4, GGSNIPV4="10.10.10.1", MASKV4="255.255.255.255", QOSVER=R7QOS;
```

//设置SGSN的QoS支持版本为R7，SGSN的信令面IP地址为10.10.11.1，掩码为255.255.255.255。

```
ADD SGSNCHARACT: RANGE=SPECIAL_SGSN, IPT=IPV4, IPV4="10.10.11.1", MASKV4="255.255.255.255", QOSVER=R7QOS;
```

//设置SGSN支持的最大上行扩展比特率和保证上行扩展比特率为32(11.52Mbps)。

```
MOD IMSISMCHAR: SUBRANGE=ALL_USER, APNNI="00001", UEACCCAP=ALL_UE, NTYPE=NET_NEGO_QOS, QOS2G=NO, QOS3G=YES, MBRUPLK3G=254, GBRUPLK3G=254, MBRUPLKEX3G=32, GBRUPLKEX3G=32;
```