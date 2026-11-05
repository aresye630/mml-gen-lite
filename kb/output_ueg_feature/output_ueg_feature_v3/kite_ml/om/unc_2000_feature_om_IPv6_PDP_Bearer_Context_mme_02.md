# 激活IPv6承载上下文特性（适用于PGW-C）

* 操作场景
* 必备事项
* 操作步骤
* 任务示例

## 操作场景

本操作指导介绍在运行网络中激活IPv6承载上下文的操作过程。

适用于PGW-C。

## 必备事项

前提条件

* 请仔细阅读GWFD-022901 IPv6承载上下文特性概述（MME、S/PGW-C）。
* 完成加载License。
* APN的IP地址分配属性指定为本地分配地址。

数据

该操作无需准备数据。

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **ADD CPSECTION** | IPv6前缀起始地址（V6PREFIXSTART） | fe80:1111:2222:3333:ff:ff:ff:ff | 全网规划 | IPv6地址前缀的地址段 |
|  | IPv6前缀结束地址（V6PREFIXEND） | fe80:1111:2222:4444:ff:ff:ff:ff | 全网规划 |  |
|  | IPv6前缀长度（V6PREFIXLENGTH） | 64 | 全网规划 |  |
| **ADD CPADDRPOOL** | 地址池名（POOLNAME） | testpool | 本端规划 | 本地地址池 |
| **ADD CPAPN** | APN实例名（APN） | apn-test | 从已配置数据中获取 | APN相关配置 |
| **SET CPAPNADDRESSATTR** | APN名称（APN） | apn-test | 从已配置数据中获取 |  |
|  | IPV6分配方式（IPV6ALLOCTYPE） | LOCAL | 本端规划 |  |
| ****ADD POOLBINDAPN**** | 地址池名（POOLNAME） | testpool | 从已配置数据中获取 |  |

## 操作步骤

1. 进入“MML命令行-UEG”窗口。
2. 打开IPv6承载上下文特性的License配置开关。

   **SET LICENSESWITCH**
3. 配置本地地址池分配IPv6地址。
   1. 创建本地地址池。

      **ADD CPADDRPOOL**

      **ADD CPADDRPOOL**时，“IPVERSION”请选择“IPV6”参数。
   2. 配置IPv6地址前缀的地址段。

      **ADD CPSECTION**
   3. 指定APN实例名称。

      **ADD CPAPN**
   4. 配置地址分配方式。

      **SET CPAPNADDRESSATTR**
   5. 为该APN绑定本地地址池。

      ****ADD POOLBINDAPN****

## 任务示例

任务描述

配置通过本地IPv6地址分配方式给MS/UE分配下行路由。

脚本

//打开本特性的License配置开关。

```
SET LICENSESWITCH: LICITEM="LKV2IPV6SM01", SWITCH=ENABLE;
```

//配置本地地址池分配IPv6地址。

```
ADD CPADDRPOOL:POOLNAME="testpool",IPVERSION=IPv6;
```

```
ADD CPSECTION:POOLNAME="testpool",SECTIONNUM=1,IPVERSION=IPV6,V6PREFIXSTART="fe80:1111:2222:3333:ff:ff:ff:ff",V6PREFIXEND="fe80:1111:2222:4444:ff:ff:ff:ff",V6PREFIXLENGTH=64;
```

```
ADD CPAPN:APN="apn-test";
```

```
SET CPAPNADDRESSATTR:APN="apn-test",IPV6ALLOCTYPE=Local;
```

```
ADD POOLBINDAPN:APN="apn-test",POOLNAME="testpool";
```

版权所有 © 华为技术有限公司
