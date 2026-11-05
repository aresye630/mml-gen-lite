# 基于APN/DNN分配地址

* 操作场景
* 必备事项
* 操作步骤
* 任务示例

## 操作场景

运营商规划用户面网元（UPF/PGW-U）基于APN/DNN为UE分配IP地址时，可激活本特性。

适用于PGW-U、UPF。

## 必备事项

前提条件

* 请仔细阅读GWFD-020406 IPv6 Prefix Delegation。
* UDG本端已完成数据面逻辑接口（Sa/Sc/Pa）和N4/Sxa/Sxb逻辑接口的配置，配置过程可参考初始配置手册的配置业务接口数据。

数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **ADD VPNINST** | VPN实例（VPNINSTANCE） | vpn1 | 全网规划 | 此处绑定的VPN实例与业务APN绑定的VPN实例一致。 |
| **ADD APN** | APN名称（APN） | apn-test2 | 本端规划 | APN/DNN实例应该全网规划，UDG本端配置的APN/DNN实例应该与C面（SMF/SGW-C/PGW-C）配置的APN/DNN实例一致。 |
|  | 绑定VPN  （HASVPN） | ENABLE | 本端规划 | 如下三者绑定的VPN实例必须一致。   * 地址池绑定的VPN实例 * 用户激活使用的APN绑定的VPN实例 * 与PDN/DN连接的Gi/SGi/N6接口的外联口绑定的VPN实例 |
|  | VPN实例名（VPNINSTANCE） | vpn1 | 本端规划 | 可以使用**LST VPNINST**命令进行查询。 |
| **SET APNADDRESSATTR** | APN名称（APN） | apn-test2 | 已配置数据中获取 | 规划使能Routing Behind MS功能的APN实例，已通过**ADD APN**命令配置，可以使用查询APN配置（LST APN）命令进行查询。 |
|  | 支持IPV4（SUPPORTIPV4） | ENABLE | 本端规划 | 配置指定APN是否支持IPV4地址。 |
|  | 支持IPV6（SUPPORTIPV6） | ENABLE | 本端规划 | 配置指定APN是否支持IPV6地址。 |
| **ADD POOL** | 地址池名称（POOLNAME） | testpool1 | 本端规划 | - |
|  | 地址池类型（POOLTYPE） | LOCAL | 本端规划 | - |
|  | IP地址类型（IPVERSION） | IPV6 | 本端规划 | 本地地址池支持IPv4和IPv6类型，如果规划UE IPv4v6双栈地址，则需要配置两种类型的地址池。 |
|  | 绑定VPN（HASVPN） | ENABLE | 本端规划 | 如下三者绑定的VPN实例必须一致。   * 用户激活使用的APN绑定的VPN实例 * 地址池绑定的VPN实例 * 与PDN/DN连接的Gi/SGi/N6接口的外联口绑定的VPN实例 |
|  | VPN实例名（VPNINSTANCE） | vpn1 | 已配置数据中获取 | 可以使用**LST VPNINST**命令进行查询。 |
| **ADD SECTION** | 地址池名称（POOLNAME） | testpool1 | 本端规划 | 可以使用**LST POOL**命令进行查询。 |
|  | 地址段号（SECTIONNUM） | 1 | 本端规划 | - |
|  | IP地址类型（IPVERSION） | IPV6 | 本端规划 | - |
|  | IPv6前缀起始地址（V6PREFIXSTART） | fc00:0000:0000:fcee:0000:0000:0000:0000 | 全网规划 | 本地地址池支持IPv4和IPv6类型，如果规划UE IPv4v6双栈地址，则需要配置两种类型的地址池。 |
|  | IPv6前缀结束地址（V6PREFIXEND） | fc00:0000:0000:fcef:ffff:ffff:ffff:ffff | 全网规划 |  |
|  | IPv6前缀长度（V6PREFIXLENGTH） | 63 | 全网规划 | 前缀长度范围为49~64，当前缀长度小于64时，则表示该地址池采用IPv6 Prefix Delegation方式分配。 |
| **ADD POOLGROUP** | 地址池组名称（POOLGRPNAME） | poolgroup1 | 本端规划 | - |
|  | IPV4基于地址池优先级分配地址算法（IPV4ALLOCPRIALG） | ENABLE | 本端规划 | 若使用IPv4地址池优先级功能，则必须使能本参数。 |
|  | IPV6基于地址池优先级分配地址算法（IPV6ALLOCPRIALG） | ENABLE | 本端规划 | 若使用IPv6地址池优先级功能，则必须使能本参数。 |
| **ADD POOLBINDGROUP** | 地址池组名称（POOLGRPNAME） | poolgroup1 | 已配置数据中获取 | 可以使用**LST POOLGROUP**命令进行查询。 |
|  | 地址池名称（POOLNAME） | testpool1 | 本端规划 | 可以使用**LST POOL**命令进行查询。 |
|  | 优先级（PRIORITY） | 10 | 本端规划 | 地址池组下绑定多个地址池时，支持按地址池优先级分配地址。只有同类地址池之间才有优先级比较，不同类型的地址池间（IPv4和IPv6）没有优先级比较。 |
| **ADD CONFLICTIPV6** | 地址池名称（POOLNAME） | testpool1 | 已配置数据中获取 | 可以使用**LST POOL**命令进行查询。 |
|  | 冲突IPv6地址前缀（V6PREFIX） | fc00:0000:0000:fcee:0000:0000:0000:0001 | 全网规划 | 如果地址池中某一个IPv6地址+前缀长度已经使用，不可用于用户地址分配，则需要配置该冲突IPv6地址。 |
|  | IPv6前缀长度（V6PREFIXLENGTH） | 63 | 已配置数据中获取 | 该参数必须与地址池的前缀长度一致。 |
| **ADD POOLGRPMAP** | 映射规则名称（MAPPINGNAME） | mapping1 | 本端规划 | - |
|  | APN名称（APN） | apn-test2 | 已配置数据中获取 | 可以使用查询命令查询APN配置（LST APN）进行查询。 |
|  | 地址池组名称（POOLGROUPNAME） | poolgroup1 | 已配置数据中获取 | 可以使用**LST POOLGROUP**命令进行查询。 |
| **SET IPALLOCRULE** | 第一级规则开关（FIRSTRULESW） | ENABLE | 本端规划 | 第一规则优先级默认使能。 |
|  | 第一级规则（FIRSTRULE） | APN-1&LOCATION-0&SMF-0 | 本端规划 | - |
|  | 第二级规则开关（SECONDRULESW） | DISABLE | 本端规划 | 第二规则优先级默认不使能。 |
|  | 第三级规则开关（THIRDRULESW） | DISABLE | 本端规划 | 第三规则优先级默认不使能。 |
| **ADD OSPFV3** | OSPFv3进程号(PROCID) | 6 | 已配置数据中获取 | - |
|  | 路由器标识(ROUTERID) | 10.8.25.1 | 已配置数据中获取 | 须知：  Router ID必须全网唯一。 |
|  | VPN的名称(VRFNAME) | vpn1 | 全网规划 | 可以使用**LST VPNINST**命令进行查询。 |
|  | 使能BFD(BFDALLINTFFLG) | TRUE | 全网规划 | - |
|  | 去使能VPN路由环路检测(VPNINSCAPSIMFLG) | TRUE | 固定取值 | VNF支持VPN多实例时，需要取消环路检查（参数“VPNINSCAPSIMFLG”配置为“TRUE”），否则会导致OSPFv3路由引入失败。 |
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
2. 基于APN/DNN实例使能地址分配属性。
   1. 配置VPN实例。

      **ADD VPNINST**
   2. 配置APN/DNN实例。

      **ADD APN**
   3. 使能该APN的地址分配属性。

      **SET APNADDRESSATTR**
3. 配置地址池绑定到地址池组。
   1. 配置LOCAL类型地址池。

      **ADD POOL**

      配置本地地址池的时候，选择参数“LOCAL”类型。
   2. 配置地址池里的地址段。

      **ADD SECTION**
   3. 配置地址池组。

      **ADD POOLGROUP**
   4. 配置地址池绑定到地址池组。

      **ADD POOLBINDGROUP**
   5. （可选）配置本地地址池中的冲突IPv6地址，标识为冲突状态的IPv6地址不会分配给用户。

      **ADD CONFLICTIPV6**
4. 配置APN实例与地址池组的映射关系。

   **ADD POOLGRPMAP**
5. 配置地址分配规则。

   地址分配规则支持两级控制：基于全局和基于APN。默认使用全局地址分配规则。如果配置了使用基于APN的地址分配规则，则使用APN的地址分配规则。

   1. 配置全局地址分配规则。

      **SET IPALLOCRULE**

      每级优先级规则中所选的条件之间为“与”的关系，表示从所选条件映射的地址范围内分配地址，此处设置的规则需要与地址池的映射条件一致。例如此处按照SMF+APN（APN-1&LOCATION-0&SMF-1）设置条件，则规划的地址池组需绑定SMF&APN。
   2. （可选）如果某一APN的地址分配规则不同于全局地址分配规则，则需执行配置基于APN的地址分配规则优先级。

      **SET APNIPALLOCRULE**
6. 配置手机下行路由。
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

UE接入核心网，UDG采用本地地址池为UE动态分配IPv4地址。其中第一优先级按照从APN/DNN映射的地址范围内分配地址，如果第一优先级的规则匹配不上，则分配地址失败。如图1所示。其中IPv6地址fc00:0000:0000:fcee:0000:0000:0000:0001/63已使用，不可以用于用户面地址分配。

**图1** 基于APN分配示意图

脚本

//打开本特性的License配置开关。

```
SET LICENSESWITCH:LICITEM="LKV3G5P6PD01",SWITCH=ENABLE;
```

//基于APN使能地址分配属性。

```
ADD VPNINST:VPNINSTANCE="vpn1";
ADD APN:APN="apn-test2",HASVPN=ENABLE,VPNINSTANCE="vpn1";
SET APNADDRESSATTR:APN="apn-test2",SUPPORTIPV4=ENABLE,SUPPORTIPV6=ENABLE;
```

//配置地址池绑定到地址池组。

```
ADD POOL:POOLNAME="testpool",POOLTYPE=LOCAL,IPVERSION=IPV6, HASVPN=ENABLE,VPNINSTANCE="vpn1";
```

```
ADD SECTION:POOLNAME="testpool",SECTIONNUM=1,IPVERSION=IPV6,V6PREFIXSTART="fc00:0000:0000:fcee:0000:0000:0000:0000",V6PREFIXEND="fc00:0000:0000:fcef:ffff:ffff:ffff:ffff", V6PREFIXLENGTH=63;
```

```
ADD POOLGROUP: POOLGRPNAME="poolgroup1", IPV4ALLOCPRIALG=ENABLE, IPV6ALLOCPRIALG=ENABLE;
```

```
ADD POOLBINDGROUP: POOLGROUPNAME="poolgroup1", POOLNAME="testpool", PRIORITY=10;
ADD CONFLICTIPV6:POOLNAME="testpool",V6PREFIX="fc00:0000:0000:fcee:0000:0000:0000:0001", V6PREFIXLENGTH=63;
```

//配置APN与地址池组的映射关系。

```
ADD POOLGRPMAP: MAPPINGNAME="mapping1", APN="apn-test2", POOLGROUPNAME="poolgroup1";
```

//配置地址分配规则。

```
SET IPALLOCRULE: FIRSTRULESW=ENABLE, FIRSTRULE=APN-1&LOCATION-0&SMF-0, SECONDRULESW=DISABLE, THIRDRULESW=DISABLE;
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
