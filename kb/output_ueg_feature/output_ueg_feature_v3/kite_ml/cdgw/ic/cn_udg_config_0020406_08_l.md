# 激活外部网元地址分配的IPv6 Prefix Delegation功能

* 操作场景
* 必备事项
* 操作步骤
* 任务示例

## 操作场景

运营商支持基于外部网元为UE分配地址时，激活本特性。

适用于PGW-U、UPF。

## 必备事项

前提条件

请仔细阅读GWFD-022906 IPv6 Prefix Delegation。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **ADD VPNINST** | VPN实例（VPNINSTANCE） | vpn1 | 全网规划 | - |
| **ADD POOLGROUP** | 地址池组名称（POOLGRPNAME） | poolgroup1 | 本端规划 | - |
| **ADD UPPOOL** | 地址池名称（POOLNAME） | testpool | 本端规划 | - |
|  | 地址池类型（POOLTYPE） | EXTERNAL | 本端规划 | - |
|  | 检查地址合法性（CHECKIPVALID） | ENABLE | 本端规划 | - |
|  | 绑定VPN（HASVPN） | ENABLE | 本端规划 | - |
|  | VPN实例名（VPNINSTANCE） | vpn1 | 已配置数据中获取 | 可以使用**LST VPNINST**命令进行查询。 |
| **ADD SECTION** | 地址池名称（POOLNAME） | testpool | 本端规划 | 可以使用**LST UPPOOL**命令进行查询。 |
|  | 地址段号（SECTIONNUM） | 1 | 本端规划 | - |
|  | IP地址类型（IPVERSION） | IPV6 | 本端规划 | - |
|  | IPv6前缀起始地址（V6PREFIXSTART） | fc00:0000:0000:fcee:0000:0000:0000:0000 | 全网规划 | 本地地址池支持IPv4和IPv6类型，如果规划UE IPv4v6双栈地址，则需要配置两种类型的地址池。 |
|  | IPv6前缀结束地址（V6PREFIXEND） | fc00:0000:0000:fcef:ffff:ffff:ffff:ffff | 全网规划 | - |
|  | IPv6前缀长度（V6PREFIXLENGTH） | 63 | 全网规划 | 前缀长度范围为49~64，当前缀长度小于64时，则表示该地址池采用IPv6 Prefix Delegation方式分配。 |
| **ADD POOLBINDGROUP** | 地址池组名称(POOLGROUPNAME) | poolgroup1 | 本端规划 | 可以使用**LST POOLBINDGROUP**命令进行查询。 |
|  | 地址池名称(POOLNAME) | testpool | 本端规划 | 可以使用**LST UPPOOL**命令进行查询。 |
| **ADD UPAPN** | APN名称(APN) | apn-test | 本端规划 | - |
|  | 绑定VPN(HASVPN) | ENABLE | 本端规划 | - |
|  | VPN实例名(VPNINSTANCE) | vpn1 | 本端规划 | 可以使用**LST VPNINST**命令进行查询。 |
| **ADD POOLGRPMAP** | 映射规则名称(MAPPINGNAME) | mapping1 | 本端规划 | - |
|  | APN名称(APN) | apn-test | 本端规划 | 可以使用**LST UPAPN**命令进行查询。 |
|  | 地址池组名称(POOLGROUPNAME) | poolgroup1 | 本端规划 | 可以使用**LST POOLBINDGROUP**命令进行查询。 |
| **ADD OSPFV3** | OSPFv3进程号(PROCID) | 6 | 已配置数据中获取 | - |
|  | 路由器标识(ROUTERID) | 10.8.25.1 | 已配置数据中获取 | 须知：  Router ID必须全网唯一。 |
|  | VPN的名称(VRFNAME) | vpn1 | 全网规划 | 可以使用**LST VPNINST**命令进行查询。 |
|  | 使能BFD(BFDALLINTFFLG) | TRUE | 全网规划 | - |
|  | 去使能VPN路由环路检测(VPNINSCAPSIMFLG) | TRUE | 固定取值 | 支持VPN多实例，需要取消环路检查（参数“VPNINSCAPSIMFLG”配置为“TRUE”），否则会导致OSPF路由引入失败。 |
|  | OSPFv3共网段虚拟系统使能标志(VIRTUALSYSFLAG) | TRUE | 全网规划 | 当OSPFv3路由配置共网段时，需要将参数“VIRTUALSYSFLAG（OSPFv3共网段虚拟系统使能标志）”配置为“TRUE”。 |
| **ADD OSPFV3AREA** | OSPFv3进程号（PROCID） | 6 | 本端规划 | - |
|  | OSPFv3区域标识（AREAID） | 0.0.0.5 | 与对端协商 | - |
| **ADD OSPFV3INTERFACE** | OSPFv3进程号(PROCID) | 6 | 本端规划 | - |
|  | OSPFv3区域号（AREAID） | 0.0.0.5 | 与对端协商 | - |
|  | 接口名称（IFNAME） | Eth-trunk1.1 | 全网规划 | - |
|  | 指定路由器优先级（DRPRI） | 0 | - | 广播或NBMA网络中，根据此接口优先级选举DR和BDR路由器，“优先级”设置为“0”表示不参与DR和BDR的选举。为避免VNF被选为DR或BDR，建议将VNF“优先级”配置为0，对端配置为非0。 |
|  | OSPFv3共网段虚拟系统使能标志(VIRTUALSYSFLAG) | TRUE | - | 当OSPFv3路由配置共网段时，需要将参数“VIRTUALSYSFLAG（OSPFv3共网段虚拟系统使能标志）”配置为“TRUE”。 |
| **ADD OSPFV3IMPORTROUTE** | OSPFv3进程号(PROCID) | 6 | 本端规划 | - |
|  | 拓扑标识(TOPOID) | 0 | 全网规划 | - |
|  | 协议号(PROTOCOL) | wlr | 本端规划 | - |

## 操作步骤

1. 打开本特性的License配置开关。

   **SET LICENSESWITCH**
2. **可选：**配置白名单检测功能。
   1. 配置VPN实例。

      **ADD VPNINST**
   2. 配置地址池组。

      **ADD POOLGROUP**
   3. 配置EXTERNAL类型地址池。

      **ADD UPPOOL**

      如果需要开启静态地址的白名单检测功能，需将**ADD UPPOOL**的“CHECKIPVALID”设置为“ENABLE”。
   4. 配置地址池里的IPv4地址段。

      **ADD SECTION**
   5. 将地址池绑定地址池组。

      **ADD POOLBINDGROUP**
   6. 配置APN名称。

      **ADD UPAPN**
   7. 配置地址池组与APN的映射关系。

      **ADD POOLGRPMAP**
3. 配置手机下行路由。
   1. 创建OSPFv3进程。

      **ADD OSPFV3**
   2. 增加OSPFv3区域。

      **ADD OSPFV3AREA**
   3. 配置运行OSPFv3协议的接口。

      **ADD OSPFV3INTERFACE**
   4. 设置OSPFv3引入路由类型。

      **ADD OSPFV3IMPORTROUTE**

## 任务示例

任务描述

UE接入核心网，UEG采用外部地址分配方式为UE分配IP地址。

脚本

//配置外部地址分配时的白名单检测功能。

```
ADD VPNINST:VPNINSTANCE="vpn1";
```

```
ADD POOLGROUP: POOLGRPNAME="poolgroup1";
```

```
ADD UPPOOL:POOLNAME="testpool",POOLTYPE=EXTERNAL,IPVERSION=IPV6,CHECKIPVALID=ENABLE,HASVPN=ENABLE,VPNINSTANCE="vpn1";
ADD SECTION:POOLNAME="testpool",SECTIONNUM=1,IPVERSION=IPV6,V6PREFIXSTART="fc00:0000:0000:fcee:0000:0000:0000:0000",V6PREFIXEND="fc00:0000:0000:fcef:ffff:ffff:ffff:ffff", V6PREFIXLENGTH=63;
```

```
ADD POOLBINDGROUP:POOLGROUPNAME="poolgroup1", POOLNAME="testpool";
```

```
ADD UPAPN:APN="apn-test",HASVPN=ENABLE,VPNINSTANCE="vpn1";
```

```
ADD POOLGRPMAP: MAPPINGNAME="mapping1", APN="apn-test", POOLGROUPNAME="poolgroup1";
```

//配置手机下行路由。

```
ADD OSPFV3:PROCID=6,VRFNAME="vpn1",ROUTERID="10.8.25.1",BFDALLINTFFLG=TRUE,VPNINSCAPSIMFLG=TRUE,VIRTUALSYSFLAG=TRUE;
```

```
ADD OSPFV3AREA:PROCID=6,AREAID="0.0.0.5";
```

```
ADD OSPFV3INTERFACE:PROCID=6,AREAID="0.0.0.5",IFNAME="Eth-trunk1.1",DRPRI=0,VIRTUALSYSFLAG=TRUE, CFGROUTERIDFLAG=FALSE;
```

```
ADD OSPFV3IMPORTROUTE:PROCID=6,TOPOID=0,PROTOCOL=wlr;
```

版权所有 © 华为技术有限公司