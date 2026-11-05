# 激活IPv6前缀代理

* 操作场景
* 必备事项
* 操作步骤
* 任务示例

## 操作场景

当网络中部署IPv6 Prefix Delegation功能，并通过UEG本地地址池方式或者Radius服务器分配IPv6代理前缀时，需要配置本地/Radius分配IPv6代理前缀。

适用于SGW-C、PGW-C、SMF。

## 必备事项

前提条件

* 请仔细阅读GWFD-022906 IPv6 Prefix Delegation特性概述。
* 完成激活RADIUS功能。
* 完成加载License。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **ADD CPVPNINST** | VPN实例名（VPNINSTACE） | vpn1 | 全网规划 | 配置VPN实例。 |
| ****ADD L3VPNINST**** | VPN实例名称（VRFNAME） | vpn1 | 本端规划 | 配置L3VPN实例。 |
| ****ADD VPNINSTAF**** | VPN实例名称（VRFNAME） | vpn1 | 已配置数据中获取 | 已通过****ADD L3VPNINST****命令配置，可以使用****LST L3VPNINST****命令进行查询。 |
|  | 地址族类型（AFTYPE） | ipv6uni | 本端规划 | - |
| ****MOD VPNINSTAF**** | VPN实例名称（VRFNAME） | vpn1 | 已配置数据中获取 | 已通过****ADD L3VPNINST****命令配置，可以使用****LST L3VPNINST****命令进行查询。 |
|  | 地址族类型（AFTYPE） | ipv6uni | 已配置数据中获取 | - |
|  | 路由标识（VRFRD） | 65512:2 | 本端规划 |  |
| **ADD CPADDRPOOL** | 地址池名（POOLNAME） | pool01 | 本端规划 | 配置地址池。 |
|  | IP地址类型（IPVERSION） | IPv6 | 本端规划 |  |
|  | POOLTYPE（地址池类型） | Local | 本端规划 |  |
|  | CHECKIPVALID（检查地址合法性） | Enable | 本端规划 |  |
| **SET CPAPNADDRESSATTR** | APN名称（APN） | huawei.com | 已配置数据中获取 | 规划使能IPv6 Prefix Delegation功能的APN实例，已通过 **ADD CPAPN**命令配置，可以使用 **LST CPAPN**命令进行查询。 |
|  | IPV6分配方式（IPV6ALLOCTYPE） | LOCAL | 本端规划 | 配置APN下的IPv6地址分配属性。  IPv6 Prefix Delegation功能支持通过本地地址池方式或者Radius服务器分配IPv6代理前缀。 |

## 操作步骤

1. 进入“MML命令行-UEG”窗口。
2. 打开本特性的License开关。

   **SET LICENSESWITCH**
3. 配置IPv6 VPN。

   1. 创建VPN实例。

      **ADD CPVPNINST**
   2. 使能IPv6地址族。

      ****ADD L3VPNINST****

      ****ADD VPNINSTAF****
   3. 配置路由标识符。

      ****MOD VPNINSTAF****
4. 配置分配IPv6代理前缀。

   1. 配置IPv6地址前缀名和IPv6前缀关联的VPN实例。

      **ADD CPADDRPOOL**

   * 如果APN使能了L2TP功能，则无需开启IPv6 Prefix Delegation功能。
   * 在功能开启前，需要在AAA Server上配置好分配给终端设备使用的IP地址段。
5. 配置APN下的地址分配属性。根据规划配置为本地或Radius分配IPv6代理前缀。

   1. 指定APN名称。

      **ADD CPAPN**
   2. 配置地址分配属性。为本地或Radius分配IPv6代理前缀。

      **SET CPAPNADDRESSATTR**
   3. 配置APN所属的IPv6 APN。

      **MOD CPAPN**

## 任务示例

任务描述

使能APN“huawei.com”的IPv6 Prefix Delegation功能，配置本地地址池地分配IPv6代理前缀，绑定的VPN实例为“vpn1”。

脚本

//打开本特性的License配置开关。

```
SET LICENSESWITCH:LICITEM="LKV3W9V6PD11",SWITCH=ENABLE;
```

//创建IPv6 VPN实例。

```
ADD CPVPNINST: VPNINSTANCE="vpn1";
ADD L3VPNINST: VRFNAME="vpn1";
ADD VPNINSTAF: VRFNAME="vpn1", AFTYPE=ipv6uni;
MOD VPNINSTAF: VRFNAME="vpn1", AFTYPE=ipv6uni, VRFRD="65512:2";
```

//配置本地地址池分配IPv6代理前缀。

```
ADD CPADDRPOOL: POOLNAME="pool01", POOLTYPE=Local, IPVERSION=IPv6, HASVPN=Enable, VPNINSTANCE="vpn1";
```

//配置APN下的IP地址分配属性。

```
ADD CPAPN: APN="huawei.com";
SET CPAPNADDRESSATTR: APN="huawei.com", IPV6ALLOCTYPE=LOCAL;
MOD CPAPN: APN="huawei.com", HASVPNIPV6=ENABLE, VPNINSTANCEIPV6="vpn1";
```

版权所有 © 华为技术有限公司
