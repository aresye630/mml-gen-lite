# 基于SMF分配地址

- 操作场景
- 必备事项
- 操作步骤
- 任务示例

## 操作场景

运营商规划用户面网元（UPF/PGW-U）基于SMF为UE分配IP地址时，可激活本特性。

**说明** 

适用于PGW-U、UPF。

## 必备事项

前提条件

- 请仔细阅读GWFD-022906 IPv6 Prefix Delegation。
- UEG本端已完成数据面逻辑接口（Sa/Sc/Pa）和N4/Sxa/Sxb逻辑接口的配置，配置过程可参考初始配置手册的配置业务数据。

数据

| 类别                              | 参数名称                                | 取值样例                                    | 获取方法     | 说明                                                                                                          |
|:--------------------------------|:------------------------------------|:----------------------------------------|:---------|:------------------------------------------------------------------------------------------------------------|
| ADD VPNINST                     | VPN实例（VPNINSTANCE）                  | vpn1                                    | 全网规划     | 此处绑定的VPN实例与业务APN绑定的VPN实例一致。                                                                                 |
| ADD APN(风筝S)/ADD UPAPN(风筝M或L)   | APN名称（APN）                          | apn-test2                               | 本端规划     | APN/DNN实例应该全网规划，UEG本端配置的APN/DNN实例应该与C面（SMF/SGW-C/PGW-C）配置的APN/DNN实例一致。                                      |
| ADD APN(风筝S)/ADD UPAPN(风筝M或L)   | 绑定VPN （HASVPN）                      | ENABLE                                  | 本端规划     | 如下三者绑定的VPN实例必须一致。 地址池绑定的VPN实例用户激活使用的APN绑定的VPN实例与PDN/DN连接的Gi/SGi/N6接口的外联口绑定的VPN实例                            |
| ADD APN(风筝S)/ADD UPAPN(风筝M或L)   | VPN实例名（VPNINSTANCE）                 | vpn1                                    | 本端规划     | 可以使用LST VPNINST命令进行查询。                                                                                      |
| SET APNADDRESSATTR              | APN名称（APN）                          | apn-test2                               | 已配置数据中获取 | 规划使能Routing Behind MS功能的APN实例，已通过ADD APN(风筝S)/ADD UPAPN(风筝M或L)命令配置，可以使用LST APN(风筝S)/LST UPAPN(风筝M或L)命令进行查询。 |
| SET APNADDRESSATTR              | 支持IPV4（SUPPORTIPV4）                 | ENABLE                                  | 本端规划     | 配置指定APN是否支持IPV4地址。                                                                                          |
| SET APNADDRESSATTR              | 支持IPV6（SUPPORTIPV6）                 | ENABLE                                  | 本端规划     | 配置指定APN是否支持IPV6地址。                                                                                          |
| ADD POOL(风筝S)/ADD UPPOOL(风筝M或L) | 地址池名称（POOLNAME）                     | testpool3                               | 本端规划     | -                                                                                                           |
| ADD POOL(风筝S)/ADD UPPOOL(风筝M或L) | 地址池类型（POOLTYPE）                     | LOCAL                                   | 本端规划     | -                                                                                                           |
| ADD POOL(风筝S)/ADD UPPOOL(风筝M或L) | IP地址类型（IPVERSION）                   | IPV6                                    | 本端规划     | 本地地址池支持IPv4和IPv6类型，如果规划UE IPv4v6双栈地址，则需要配置两种类型的地址池。                                                         |
| ADD POOL(风筝S)/ADD UPPOOL(风筝M或L) | 绑定VPN（HASVPN）                       | ENABLE                                  | 本端规划     | 如下三者绑定的VPN实例必须一致。 用户激活使用的APN绑定的VPN实例地址池绑定的VPN实例与PDN/DN连接的Gi/SGi/N6接口的外联口绑定的VPN实例                            |
| ADD POOL(风筝S)/ADD UPPOOL(风筝M或L) | VPN实例名（VPNINSTANCE）                 | vpn1                                    | 已配置数据中获取 | 可以使用LST VPNINST命令进行查询。                                                                                      |
| ADD SECTION                     | 地址池名称（POOLNAME）                     | testpool3                               | 本端规划     | 可以使用LST POOL(风筝S)/LST UPPOOL(风筝M或L)命令进行查询。                                                                  |
| ADD SECTION                     | 地址段号（SECTIONNUM）                    | 1                                       | 本端规划     | -                                                                                                           |
| ADD SECTION                     | IP地址类型（IPVERSION）                   | IPV6                                    | 本端规划     | -                                                                                                           |
| ADD SECTION                     | IPv6前缀起始地址（V6PREFIXSTART）           | fc00:0000:0000:fcee:0000:0000:0000:0000 | 全网规划     | 本地地址池支持IPv4和IPv6类型，如果规划UE IPv4v6双栈地址，则需要配置两种类型的地址池。                                                         |
| ADD SECTION                     | IPv6前缀结束地址（V6PREFIXEND）             | fc00:0000:0000:fcef:ffff:ffff:ffff:ffff | 全网规划     | 本地地址池支持IPv4和IPv6类型，如果规划UE IPv4v6双栈地址，则需要配置两种类型的地址池。                                                         |
| ADD SECTION                     | IPv6前缀长度（V6PREFIXLENGTH）            | 63                                      | 全网规划     | 前缀长度范围为49~64，当前缀长度小于64时，则表示该地址池采用IPv6 Prefix Delegation方式分配。                                                |
| ADD POOLGROUP                   | 地址池组名称（POOLGRPNAME）                 | poolgroup3                              | 本端规划     | -                                                                                                           |
| ADD POOLGROUP                   | IPV4基于地址池优先级分配地址算法（IPV4ALLOCPRIALG） | ENABLE                                  | 本端规划     | 若使用IPv4地址池优先级功能，则必须使能本参数。                                                                                   |
| ADD POOLGROUP                   | IPV6基于地址池优先级分配地址算法（IPV6ALLOCPRIALG） | ENABLE                                  | 本端规划     | 若使用IPv6地址池优先级功能，则必须使能本参数。                                                                                   |
| ADD POOLBINDGROUP               | 地址池组名称（POOLGRPNAME）                 | poolgroup3                              | 已配置数据中获取 | 可以使用LST POOLGROUP命令进行查询。                                                                                    |
| ADD POOLBINDGROUP               | 地址池名称（POOLNAME）                     | testpool3                               | 本端规划     | 可以使用LST POOL(风筝S)/LST UPPOOL(风筝M或L)命令进行查询。                                                                  |
| ADD POOLBINDGROUP               | 优先级（PRIORITY）                       | 10                                      | 本端规划     | 地址池组下绑定多个地址池时，支持按地址池优先级分配地址。只有同类地址池之间才有优先级比较，不同类型的地址池间（IPv4和IPv6）没有优先级比较。                                   |
| ADD CPNODEID                    | SMF 名称（CPNAME）                      | smfnode1                                | 本端规划     | -                                                                                                           |
| ADD CPNODEID                    | IPv4地址类型的Node Id（IPV4NODEID）        | 10.0.0.1                                | 对端获取     | 不同SMF实例的SMF NodeID不可以相同。该参数要与对端SMF上的配置取值一致。                                                                 |
| ADD CPNODEID                    | IPv6地址类型的Node Id（IPV6NODEID）        | FC00:1111:1001:0001:0100:1100:0000:0001 | 对端获取     | 不同SMF实例的SMF NodeID不可以相同。该参数要与对端SMF上的配置取值一致。                                                                 |
| ADD CPNODEID                    | FQDN类型的Node Id（FQDNNODEID）          | consumer.huawei.com                     | 对端获取     | 不同SMF实例的SMF NodeID不可以相同。该参数要与对端SMF上的配置取值一致。                                                                 |
| ADD CONFLICTIPV6                | 地址池名称（POOLNAME）                     | testpool3                               | 已配置数据中获取 | 可以使用LST POOL(风筝S)/LST UPPOOL(风筝M或L)命令进行查询。                                                                  |
| ADD CONFLICTIPV6                | 冲突IPv6地址前缀（V6PREFIX）                | fc00:0000:0000:fcee:0000:0000:0000:0001 | 全网规划     | 如果地址池中某一个IPv6地址+前缀长度已经使用，不可用于用户地址分配，则需要配置该冲突IPv6地址。                                                         |
| ADD CONFLICTIPV6                | IPv6前缀长度（V6PREFIXLENGTH）            | 63                                      | 已配置数据中获取 | 该参数必须与地址池的前缀长度一致。                                                                                           |
| ADD POOLGRPMAP                  | 映射规则名称（MAPPINGNAME）                 | mapping3                                | 本端规划     | -                                                                                                           |
| ADD POOLGRPMAP                  | SMF名称（SMF）                          | smfnode1                                | 已配置数据中获取 | 可以使用查询命令LST CPNODEID进行查询。                                                                                   |
| ADD POOLGRPMAP                  | 地址池组名称（POOLGROUPNAME）               | poolgroup3                              | 已配置数据中获取 | 可以使用LST POOLGROUP命令进行查询。                                                                                    |
| SET IPALLOCRULE                 | 第一级规则开关（FIRSTRULESW）                | ENABLE                                  | 本端规划     | 第一规则优先级默认使能。                                                                                                |
| SET IPALLOCRULE                 | 第一级规则（FIRSTRULE）                    | APN-0&LOCATION-0&SMF-1                  | 本端规划     | -                                                                                                           |
| SET IPALLOCRULE                 | 第二级规则开关（SECONDRULESW）               | DISABLE                                 | 本端规划     | 第二规则优先级默认不使能。                                                                                               |
| SET IPALLOCRULE                 | 第三级规则开关（THIRDRULESW）                | DISABLE                                 | 本端规划     | 第三规则优先级默认不使能。                                                                                               |
| SET IPALLOCBYSMFGLBSW           | 开关（SWITCH）                          | ENABLE                                  | 本端规划     | -                                                                                                           |
| ADD OSPFV3                      | OSPFv3进程号(PROCID)                   | 6                                       | 已配置数据中获取 | -                                                                                                           |
| ADD OSPFV3                      | 路由器标识(ROUTERID)                     | 10.8.25.1                               | 已配置数据中获取 | 须知： Router ID必须全网唯一。                                                                                        |
| ADD OSPFV3                      | VPN的名称(VRFNAME)                     | vpn1                                    | 全网规划     | 可以使用LST VPNINST命令进行查询。                                                                                      |
| ADD OSPFV3                      | 使能BFD(BFDALLINTFFLG)                | TRUE                                    | 全网规划     | -                                                                                                           |
| ADD OSPFV3                      | 去使能VPN路由环路检测(VPNINSCAPSIMFLG)       | TRUE                                    | 固定取值     | VNF支持VPN多实例时，需要取消环路检查（参数“VPNINSCAPSIMFLG”配置为“TRUE”），否则会导致OSPFv3路由引入失败。                                      |
| ADD OSPFV3                      | OSPFv3共网段虚拟系统使能标志(VIRTUALSYSFLAG)   | TRUE                                    | 全网规划     | 当OSPFv3路由配置共网段时，需要将参数“VIRTUALSYSFLAG（OSPFv3共网段虚拟系统使能标志）”配置为“TRUE”。                                          |
| ADD OSPFV3AREA                  | OSPFv3进程号（PROCID）                   | 6                                       | 本端规划     | -                                                                                                           |
| ADD OSPFV3AREA                  | OSPFv3区域标识（AREAID）                  | 0.0.0.5                                 | 与对端协商    | -                                                                                                           |
| ADD OSPFV3INTERFACE             | OSPFv3进程号(PROCID)                   | 6                                       | 本端规划     | -                                                                                                           |
| ADD OSPFV3INTERFACE             | OSPFv3区域号（AREAID）                   | 0.0.0.5                                 | 与对端协商    | -                                                                                                           |
| ADD OSPFV3INTERFACE             | 接口名称（IFNAME）                        | Eth-trunk1.1                            | 全网规划     | 根据手机下行路由的外联口规划。                                                                                             |
| ADD OSPFV3INTERFACE             | 指定路由器优先级（DRPRI）                     | 0                                       | -        | 广播或NBMA网络中，根据此接口优先级选举DR和BDR路由器，“优先级”设置为“0”表示不参与DR和BDR的选举。为避免VNF被选为DR或BDR，建议将VNF“优先级”配置为0，对端配置为非0。           |
| ADD OSPFV3INTERFACE             | OSPFv3共网段虚拟系统使能标志(VIRTUALSYSFLAG)   | TRUE                                    | -        | 当OSPFv3路由配置共网段时，需要将参数“VIRTUALSYSFLAG（OSPFv3共网段虚拟系统使能标志）”配置为“TRUE”。                                          |
| ADD OSPFV3IMPORTROUTE           | OSPFv3进程号(PROCID)                   | 6                                       | 本端规划     | -                                                                                                           |
| ADD OSPFV3IMPORTROUTE           | 拓扑标识(TOPOID)                        | 0                                       | 全网规划     | -                                                                                                           |
| ADD OSPFV3IMPORTROUTE           | 协议号(PROTOCOL)                       | wlr                                     | 本端规划     | -                                                                                                           |

## 操作步骤

1. 打开本特性的License配置开关。

   **SET LICENSESWITCH**
2. 基于APN/DNN实例使能地址分配属性。
   1. 配置VPN实例。

      **ADD VPNINST**
   2. 配置APN/DNN实例。

      **ADD APN****(风筝S)/ADD UPAPN(风筝M或L)**
   3. 使能该APN的地址分配属性。

      **SET APNADDRESSATTR**
3. 配置地址池绑定到地址池组。
   1. 配置LOCAL类型地址池。

      **ADD POOL****(风筝S)/ADD UPPOOL(风筝M或L)**

      **说明** 

      配置本地地址池的时候，选择参数“LOCAL”类型。
   2. 配置地址池里的地址段。

      **ADD SECTION**
   3. 配置地址池组。

      **ADD POOLGROUP**
   4. 配置地址池绑定到地址池组。

      **ADD POOLBINDGROUP**
   5. （可选）配置本地地址池中的冲突IPv6地址，标识为冲突状态的IPv6地址不会分配给用户。

      **ADD CONFLICTIPV6**
4. 配置SMF与地址池组的映射关系。
   1. 配置SMF实例信息。

      **ADD CPNODEID**
   2. 配置SMF实例与地址池组的映射关系。

      **ADD POOLGRPMAP**
5. 配置地址分配规则。

   **说明** 

   地址分配规则支持两级控制：基于全局和基于APN。默认使用全局地址分配规则。如果配置了使用基于APN的地址分配规则，则使用APN的地址分配规则。

   1. 配置全局地址分配规则。

      **SET IPALLOCRULE**

      **说明** 

      每级优先级规则中所选的条件之间为“与”的关系，表示从所选条件映射的地址范围内分配地址，此处设置的规则需要与地址池的映射条件一致。例如此处按照SMF+APN（APN-1&LOCATION-0&SMF-1）设置条件，则规划的地址池组需绑定SMF&APN。
   2. （可选）如果某一APN的地址分配规则不同于全局地址分配规则，则需执行配置基于APN的地址分配规则优先级。

      **SET APNIPALLOCRULE**
6. 配置基于SMF分配地址的开关。

   **说明** 

   基于SMF分配地址的开关支持两级控制：基于全局和指定SMF。

   1. 配置基于SMF分配地址的全局开关。

      **SET IPALLOCBYSMFGLBSW**
   2. （可选）如果某一指定SMF的地址分配开关不同于全局SMF地址分配开关的使能状态，则需执行配置基于指定SMF分配地址的开关。

      **SET IPALLOCBYSMFSW**
7. 配置手机下行路由。
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

UE接入核心网，UEG采用本地地址池为UE动态分配IPv4地址。其中第一优先级按照从SMF映射的地址范围内分配地址，如果第一优先级的规则匹配不上，则分配地址失败。如图1所示。其中IPv6地址fc00:0000:0000:fcee:0000:0000:0000:0001/63已使用，不可以用于用户面地址分配。

**图1** 基于SMF分配示意图

脚本

//打开本特性的License配置开关。

```
SET LICENSESWITCH:LICITEM="LKV3G5P6PD01",SWITCH=ENABLE;
```

//基于APN使能地址分配属性。

```
ADD VPNINST:VPNINSTANCE="vpn1";
ADD APN(风筝S)/ADD UPAPN(风筝M或L):APN="apn-test2",HASVPN=ENABLE,VPNINSTANCE="vpn1";
SET APNADDRESSATTR:APN="apn-test2",SUPPORTIPV4=ENABLE,SUPPORTIPV6=ENABLE;
```

//配置地址池绑定到地址池组。

```
ADD POOL(风筝S)/ADD UPPOOL(风筝M或L):POOLNAME="testpool3",POOLTYPE=LOCAL,IPVERSION=IPV6, HASVPN=ENABLE,VPNINSTANCE="vpn1";
```

```
ADD SECTION:POOLNAME="testpool3",SECTIONNUM=1,IPVERSION=IPV6,V6PREFIXSTART="fc00:0000:0000:fcee:0000:0000:0000:0000",V6PREFIXEND="fc00:0000:0000:fcef:ffff:ffff:ffff:ffff", V6PREFIXLENGTH=63;
```

```
ADD POOLGROUP: POOLGRPNAME="poolgroup3", IPV4ALLOCPRIALG=ENABLE, IPV6ALLOCPRIALG=ENABLE;
```

```
ADD POOLBINDGROUP: POOLGROUPNAME="poolgroup3", POOLNAME="testpool3", PRIORITY=10;
ADD CONFLICTIPV6:POOLNAME="testpool3",V6PREFIX="fc00:0000:0000:fcee:0000:0000:0000:0001", V6PREFIXLENGTH=63;
```

//配置SMF实例与地址池组的映射关系。

```
ADD CPNODEID: CPNAME="smfnode1", IPV4NODEID="10.0.0.1", IPV6NODEID="FC00:1111:1001:0001:0100:1100:0000:0001", FQDNNODEID="consumer.huawei.com";
ADD POOLGRPMAP: MAPPINGNAME="mapping3", SMF="smfnode1", POOLGROUPNAME="poolgroup3";
```

//配置地址分配规则。

```
SET IPALLOCRULE: FIRSTRULESW=ENABLE, FIRSTRULE=APN-0&LOCATION-0&SMF-1, SECONDRULESW=DISABLE, THIRDRULESW=DISABLE;
```

//配置基于SMF分配地址的开关。

**说明** 

基于SMF分配地址的开关支持两级控制：基于全局和指定SMF。此处配置的是基于全局的开关，如果某一指定SMF的地址分配开关不同于全局SMF地址分配开关的使能状态，则需配置基于指定SMF分配地址的开关。

```
SET IPALLOCBYSMFGLBSW: SWITCH=ENABLE;
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