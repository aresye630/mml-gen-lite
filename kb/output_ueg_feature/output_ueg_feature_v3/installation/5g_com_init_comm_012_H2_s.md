# 配置BGP over 静态路由+BFD（IPv6）

## 操作场景

BGP（Border Gateway Protocol）边界网关协议是一种用于AS(Autonomous System)之间的动态路由协议，与静态路由等内部网关协议（IGP）不同，其自身不能发现和计算路由，主要用于在自治系统AS间控制路由的传播和选择最佳路由。同时，利用BFD检测机制，提高链路可靠性。

当拓扑结构复杂且无法规划在同一自治区域内时，可以采用BGP over 静态路由+BFD实现VNF与对端设备的网络层互通。

如图1所示为UEG与周边网元的BGP over 静态路由+BFD互通组网示意图。UEG与三层路由设备运行BGP over 静态路由+BFD路由协议而接入IP网络（运营商IP骨干网/企业网络），网关可以使用运营商的承载网路由设备，也可以使用DC-GW。DC-GW的配置请参考对应型号设备的产品文档。

**图1** BGP over静态路由+BFD组网

* UEG直连PE时，组bonding的2个端口连接到同一PE设备。
* UEG直连DCGW时，组bonding的2个端口连接到不同DCGW设备。

## 必备事项

前提条件

* 请阅读并熟悉特性IPFD-020502 支持BGP特性概述。

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录MAE客户端或登录OM Portal）。

* UEG与网络实体之间的网络环境已经构建完成。

数据

**如下数据仅为举例，请注意修改成局点规划的数据。**

**表1** 静态路由数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| **ADD L3VPNINST** | VPN实例名称（VRFNAME） | VPN\_Access | 本端规划 | VPN实例全网统一规划，一条通信路径上所有节点绑定的VPN实例要一致，才能正常通信。 |
| **ADD VPNINSTAF** | 地址族类型（AFTYPE） | ipv6uni | - | IPv6组网场景下，该参数选择ipv6uni。 |
| **MOD INTERFACE** | 接口名称（IFNAME） | Ethernet64/0/4  Ethernet64/0/5 | 本端规划 | （UEG-S）请参考外联口介绍(机架服务器-ARM)/外联口介绍(刀片式服务器2U)进行规划。 |
| **ADD INTERFACE** | 子接口名字（IFNAME） | Ethernet64/0/4.1  Ethernet64/0/5.1 | 本端规划 | 非SR-IOV bonding组网需要规划。   （UEG-S）直连PE时，N6外联口采用非SR-IOV bonding组网，详细请参见外联口介绍(机架服务器-ARM)/外联口介绍(刀片式服务器2U)。 |
| **ADD INTERFACE** | 接口名称（IFNAME） | Eth-trunk1 | 本端规划 | SR-IOV bonding组网需要规划。   （UEG-S）N3/N4/N9外联口采用SR-IOV bonding组网，详细请参见外联口介绍(机架服务器-ARM)/外联口介绍(刀片式服务器2U)。 |
|  | 接口名称（IFNAME） | Eth-trunk1.1 | 本端规划 |  |
| **MOD TRUNKIF** | 接口名称（IFNAME） | Eth-trunk1 | 已规划数据中获取 | SR-IOV bonding组网下需要规划。  需保证只有MAC地址一样的VNIC加到同一个Eth-trunk接口中。 |
|  | 工作模式（WORKMODE） | Manual | 固定值 |  |
| **ADD TRUNKMEMBER** | Trunk接口名（TRUNKIFNAME） | Eth-trunk1 | 已规划数据中获取 |  |
|  | 成员接口名（MEMBERIFNAME） | Ethernet64/0/4  Ethernet64/0/5 | 本端规划 |  |
| **ADD IPBINDVPN** | VPN名字(VRFNAME) | VPN\_Access | 已配置数据中获取 | - |
| **ADD ETHSUBIF** | VLAN类型子接口的VLAN ID（VLANTYPEVID） | 100  200 | 全网规划 | 此处以双平面为例，SR-IOV bonding单平面组网时，只需规划一条数据（例如只规划VLAN 100）。 |
| **SET IFIPV6ENABLE** | IPv6使能标志（ENABLEFLAG） | TRUE | 固定取值 | - |
| **ADD IFIPV6ADDRESS** | IPv6地址(IPV6ADDRESS) | FC00::10C2  FC00::10E2 | 全网规划 | 如果规划外联口使用IPv4v6双栈地址，则分别执行**ADD IFIPV4ADDRESS**和**ADD IFIPV6ADDRESS**  对同一外联口配置IPv4和IPv6地址。 |
|  | IPv6地址前缀(PREFIXLEN) | 123 | 全网规划 |  |
| **SET BFD** | 激活BFD（BFDENABLE） | TRUE | 全网规划 | 参数“DELAYUPTIMER”（会话延迟UP时间）和“TOSEXP”（动态会话报文优先级）可以不用配置，使用默认值即可。 |
| **ADD BFDSESSION** | 会话名称（SESSNAME） | BfdName21  BfdName23 | 本端规划 | - |
|  | IP协议版本号（ADDRTYPE） | IPv6 | 固定取值 |  |
|  | 本地标识符（LOCALDISCR） | 121  123 | 本端规划 | VNF上BFD会话的本地标识符，需要和对接网关上的标识符对应，即本端的本地标识符与对端网关侧的远端标识符相同。 |
|  | 远端标识符（REMOTEDISCR） | 221  223 | 与对端协商 | VNF上BFD会话的远端标识符，需要和对接网关上的标识符对应，即本端的远端标识符与对端网关侧的本端标识符相同。 |
|  | IPv6目的地址（DESTADDR6） | FC00::10C1  FC00::10E1 | 与对端协商 | 参数“DESTADDR6”是网关的接口IP，此处用于检测目的IP能否正常接收报文。 |
|  | 链路类型（LINKTYPE） | IP | 固定取值 |  |
|  | IPv6会话创建方式（CREATETYPE6） | SESS\_STATIC | 固定取值 |  |
|  | 出接口名称（IFNAME） | Ethernet64/0/4.1  Ethernet64/0/5.1  Eth-trunk1.1 | 已配置数据中获取 | 非SR-IOV bonding组网需要规划Ethernet接口，SR-IOV bonding组网需要规划Eth-trunk接口。 |
|  | VPN实例名称（VRFNAME） | VPN\_Access | 已配置数据中获取 | 直连DCGW时，DCGW之间是M-LAG组网，该场景下，“ONEARMECHO6”需要设置为“TRUE”。  直连PE设备时，PE不支持BFD探测时，“ONEARMECHO6”需要设置为“TRUE”。 |
|  | IPv6单臂Echo（ONEARMECHO6） | FALSE | 全网规划 |  |
| **ADD SRROUTE6** | VPN实例名称 （VRFNAME） | VPN\_Access | 已配置数据中获取 | SR-IOV bonding组网时，1个路由下一跳IP地址。  双平面组网时，2个路由下一跳IP地址在不同网段。  参数“PREFIX”是目的IP，此处是BGP对等体地址。  参数“NEXTHOP”是网关的接口IP。 |
|  | 路由前缀（PREFIX） | FC00:2013::2  FC00:2013::3 | 与对端协商 |  |
|  | 路由掩码长度（MASKLENGTH） | 128 | 与对端协商 |  |
|  | 路由下一跳（NEXTHOP） | FC00::10C1  FC00::10E1 | 已规划数据中获取 |  |
|  | 静态BFD会话名（SESSIONNAME） | BfdName21  BfdName23 | 已配置数据中获取 |  |

**表2** BGP数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| ****ADD INTERFACE**** | 接口名（IFNAME） | Loopback1 | 本端规划 | - |
| ****ADD IPBINDVPN**** | VPN实例名称（VRFNAME） | VPN\_Access | 已配置数据中获取 | 此处的VPN实例已经配置，与静态路由等IGP协议的外联口绑定的VPN实例相同。 |
| **SET IFIPV6ENABLE** | IPv6使能标志（ENABLEFLAG） | TRUE | 固定取值 | - |
| **ADD IFIPV6ADDRESS** | IPv6地址(IPV6ADDRESS) | FC00:2013::1 | 全网规划 | 如果规划Loopback接口使用IPv4v6双栈地址，则分别执行**ADD IFIPV4ADDRESS**和**ADD IFIPV6ADDRESS**  对同一Loopback接口配置IPv4和IPv6地址。 |
|  | IPv6地址前缀(PREFIXLEN) | 128 | - |  |
| **SET BGP** | 使能BGP（BGPENABLE） | TRUE | 固定取值 | - |
|  | BGP自治域号（ASNUM） | 60001 | 全网规划 |  |
| ****ADD BGPVRF**** | VPN实例名称（VRFNAME） | VPN\_Access | 已配置数据中获取 | BGP VPN实例需要与Loopback接口绑定的VPN实例名一致。 |
|  | 默认地址族（DEFAULTAFTYPE） | noaf | 固定取值 | - |
|  | 路由器标识（ROUTERID） | 10.90.7.160 | 全网规划 | 不同BGP VPN实例的ROUTERID不能重复。 |
| **ADD BGPVRFAF** | VPN实例名称（VRFNAME） | VPN\_Access | 已配置数据中获取 | 使用**ADD BGPVRF**命令定义的VPN实例名称。 |
|  | 地址族类型（AFTYPE） | ipv6uni | 固定取值 | - |
|  | 最大等价路由数（MAXIMUMLOADBALANCE） | 2 | 本端规划 | 对接的负荷分担关系的BGP peer数。 |
| ****ADD BGPPEER**** | 地址类型（ADDRESSTYPE） | ipv6 | - | “PEERADDRV6”是网关上用于和VNF建立BGP邻居关系的IP地址。 |
|  | IPv6对等体地址（PEERADDRV6） | FC00:2013::2  FC00:2013::3 | 与对端协商 |  |
|  | 对等体AS号（REMOTEAS） | 60002 | 与对端协商 |  |
|  | 本地接口地址（LOCALIFADDR） | FC00:2013::1 | 已配置数据中获取 |  |
|  | 本地接口名称（LOCALIFNAME） | Loopback1 | 已配置数据中获取 |  |
|  | EBGP最大跳数（EBGP最大跳数） | 10 | 本端规划 | 不小于到Peer之间的实际跳数，无法确认时，可设置为10。  如最大跳数设置过小，会导致BGP邻居建立失败。 |
| ****ADD IMPORTROUTE**** | 地址族类型（AFTYPE） | ipv6uni | - | IPv6组网场景下，该参数选择ipv6uni。  该参数全局取值要一致。 |
|  | 路由协议（IMPORTPROTOCOL） | wlr | 固定取值 | - |
|  | 使能MED（MEDENABLE） | FALSE | 本端规划 | 对于N6口，两个UPF上的UE地址段存在重叠且需要对外发布网段路由时（该场景下，两个UPF是主备容灾），该参数设置为“TRUE”；否则，该参数设置为“FALSE”。  对于其他接口，使用默认值“FALSE”即可。 |
|  | MED（MED） | 0 | 本端规划 | “MEDENABLE”设置为“TRUE”时，需要规划该参数。  主备UPF引入路由的MED值。主UPF设置的MED值必须小于备UPF设置的MED值。 |

## 操作步骤

1. 配置外联口的VPN实例。

   ```
   ADD L3VPNINST:VRFNAME="VPN_Access";
   ADD VPNINSTAF:VRFNAME="VPN_Access",AFTYPE=ipv6uni;
   ```

   一条通信路径上所有节点绑定的VPN实例要一致，才能正常通信，例如VNF逻辑接口、VNF外联口、网关上的VPN，否则从逻辑接口发出去的报文会查询路由失败。
2. 非SR-IOV bonding组网时，配置外联口IP地址。SR-IOV bonding组网时，请跳转到3。

   1. 查看接口状态及信息。

      ```
      LST INTERFACE:;
      ```
   2. 配置主接口的管理状态为up。

      ```
      MOD INTERFACE:IFNAME="Ethernet64/0/4",IFADMINSTATUS=up;
      MOD INTERFACE:IFNAME="Ethernet64/0/5",IFADMINSTATUS=up;
      ```
   3. 配置以太网子接口。

      ```
      ADD INTERFACE:IFNAME="Ethernet64/0/4.1";
      ADD INTERFACE:IFNAME="Ethernet64/0/5.1";
      ```
   4. 增加接口绑定VPN。

      ```
      ADD IPBINDVPN:IFNAME="Ethernet64/0/4.1",VRFNAME="VPN_Access";
      ADD IPBINDVPN:IFNAME="Ethernet64/0/5.1",VRFNAME="VPN_Access";
      ```
   5. 在以太网子接口上关联VLAN ID。

      ```
      ADD ETHSUBIF:IFNAME="Ethernet64/0/4.1",VLANTYPEVID=100;
      ADD ETHSUBIF:IFNAME="Ethernet64/0/5.1",VLANTYPEVID=200;
      ```

      子接口配置了VLAN，则需要在交换机、对接网关上调整VLAN的配置。
   6. 配置IPv6使能。

      ```
      SET IFIPV6ENABLE: IFNAME="Ethernet64/0/4.1", ENABLEFLAG=TRUE;
      SET IFIPV6ENABLE: IFNAME="Ethernet64/0/5.1", ENABLEFLAG=TRUE;
      ```
   7. 配置外联口的IP地址。

      ```
      ADD IFIPV6ADDRESS:IFNAME="Ethernet64/0/4.1",IPV6ADDRESS="FC00::10C2",PREFIXLEN=123;
      ADD IFIPV6ADDRESS:IFNAME="Ethernet64/0/5.1",IPV6ADDRESS="FC00::10E2",PREFIXLEN=123;
      ```

      如果规划外联口使用IPv4v6双栈地址，则分别执行**ADD IFIPV4ADDRESS**和**ADD IFIPV6ADDRESS**对同一外联口配置IPv4和IPv6地址。
3. SR-IOV bonding组网时，配置外联口IP地址。

   1. 查看接口状态及信息。

      ```
      LST INTERFACE:;
      ```
   2. 配置主接口的管理状态为up。

      ```
      MOD INTERFACE:IFNAME="Ethernet64/0/4",IFADMINSTATUS=up;
      MOD INTERFACE:IFNAME="Ethernet64/0/5",IFADMINSTATUS=up;
      ```
   3. 配置以太Trunk接口。

      ```
      ADD INTERFACE:IFNAME="Eth-trunk1";
      ```
   4. 配置Eth-trunk接口的工作模式并添加成员端口。

      ```
      MOD TRUNKIF:IFNAME="Eth-Trunk1",WORKMODE=Manual;
      ADD TRUNKMEMBER:TRUNKIFNAME="Eth-trunk1",MEMBERIFNAME="Ethernet64/0/4";
      ADD TRUNKMEMBER:TRUNKIFNAME="Eth-trunk1",MEMBERIFNAME="Ethernet64/0/5";
      ```
   5. 配置以太Trunk子接口。

      ```
      ADD INTERFACE:IFNAME="Eth-trunk1.1";
      ```
   6. 增加接口绑定VPN。

      ```
      ADD IPBINDVPN:IFNAME="Eth-trunk1.1",VRFNAME="VPN_Access";
      ```
   7. 在以太网子接口上关联VLAN ID。

      ```
      ADD ETHSUBIF:IFNAME="Eth-trunk1.1",VLANTYPEVID=100;
      ```

      子接口配置了VLAN，则需要在交换机、对接网关上调整VLAN的配置。
   8. 配置IPv6使能。

      ```
      SET IFIPV6ENABLE: IFNAME="Eth-trunk1.1", ENABLEFLAG=TRUE;
      ```
   9. 配置外联口的IP地址。

      ```
      ADD IFIPV6ADDRESS:IFNAME="Eth-trunk1.1",IPV6ADDRESS="FC00::10C2",PREFIXLEN=123;
      ```

      如果规划外联口使用IPv4v6双栈地址，则分别执行**ADD IFIPV4ADDRESS**和**ADD IFIPV6ADDRESS**对同一外联口配置IPv4和IPv6地址。
4. 全局激活BFD。

   ```
   SET BFD: BFDENABLE=TRUE;
   ```

   参数“DELAYUPTIMER”（会话延迟UP时间）和“TOSEXP”（动态会话报文优先级）可以不用配置，使用默认值即可。
5. 新建BFD会话。

   必须全局使能BFD功能后该命令才可生效。

   * 非SR-IOV bonding组网场景下：

     ```
     ADD BFDSESSION: SESSNAME="BfdName21",ADDRTYPE=IPv6,CREATETYPE6=SESS_STATIC,ONEARMECHO6=FALSE,LINKTYPE=IP,VRFNAME="VPN_Access",LOCALDISCR=121,REMOTEDISCR=221,IFNAME="Ethernet64/0/4.1",DESTADDR6="FC00::10C1";
     ADD BFDSESSION: SESSNAME="BfdName23",ADDRTYPE=IPv6,CREATETYPE6=SESS_STATIC,ONEARMECHO6=FALSE,LINKTYPE=IP,VRFNAME="VPN_Access",LOCALDISCR=123,REMOTEDISCR=223,IFNAME="Ethernet64/0/5.1",DESTADDR6="FC00::10E1";
     ```
   * SR-IOV bonding组网场景下：

     ```
     ADD BFDSESSION: SESSNAME="BfdName21",ADDRTYPE=IPv6,CREATETYPE6=SESS_STATIC,ONEARMECHO6=TRUE,LINKTYPE=IP,VRFNAME="VPN_Access",LOCALDISCR=121,IFNAME="Eth-trunk1.1",DESTADDR6="FC00::10C1";
     ```
6. 配置静态路由并绑定BFD会话。
   * 非SR-IOV bonding组网场景下：

     ```
     ADD SRROUTE6: VRFNAME="VPN_Access", AFTYPE=ipv6unicast, PREFIX="FC00:2013::2", MASKLENGTH=128, DESTVRFNAME="VPN_Access", NEXTHOP="FC00::10C1", IFNAME="Ethernet64/0/4.1", SESSIONNAME="BfdName21";
     ADD SRROUTE6: VRFNAME="VPN_Access", AFTYPE=ipv6unicast, PREFIX="FC00:2013::3", MASKLENGTH=128, DESTVRFNAME="VPN_Access", NEXTHOP="FC00::10E1", IFNAME="Ethernet64/0/5.1", SESSIONNAME="BfdName23";
     ```
   * SR-IOV bonding组网场景下：

     ```
     ADD SRROUTE6: VRFNAME="VPN_Access", AFTYPE=ipv6unicast, PREFIX="FC00:2013::2", MASKLENGTH=128, DESTVRFNAME="VPN_Access", NEXTHOP="FC00::10C1", IFNAME="Eth-trunk1.1", SESSIONNAME="BfdName21";
     ADD SRROUTE6: VRFNAME="VPN_Access", AFTYPE=ipv6unicast, PREFIX="FC00:2013::3", MASKLENGTH=128, DESTVRFNAME="VPN_Access", NEXTHOP="FC00::10C1", IFNAME="Eth-trunk1.1", SESSIONNAME="BfdName21";
     ```

   * BFD会话绑定的是路由，不是BGPPEER。如存在**ADD BGPPEERBFD**配置，请删除。静态路由绑定静态BFD会话时，通过**ADD SRROUTE6**的“静态BFD会话名”来指定静态路由所联动的静态BFD的会话名。
   * 静态路由用于实现VNF 的Loopback接口地址与BGP PEER IP（DC-GW）之间的互通。
   * 本步骤配置的是静态路由时，需要配置如下两类路由：
     + IP路由1：目的IP是BGP对等体地址，下一跳是网关的接口IP地址，且该路由需要绑定BFD会话。
     + IP路由2：目的IP是0:0:0:0:0:0:0:0，掩码长度是0。其他参数取值与“IP路由1”中的参数值相同。对端网元不发布默认BGP路由时需要配置。
   * 在网关侧配置到VNF的回程路由，目的地址为VNF上各逻辑接口的IP地址，下一跳为VNF上配置的各逻辑接口对应的外联口的IP地址。

     需要说明的是，配置VNF与DN/PDN通信的回程路由时，目的地址为UE的网段地址，下一跳为VNF上外联口的IP地址。
7. 配置Loopback接口地址。
   1. 配置Loopback接口。

      ```
      ADD INTERFACE:IFNAME="Loopback1";
      ```
   2. 配置接口绑定VPN。

      ```
      ADD IPBINDVPN:IFNAME="Loopback1",VRFNAME="VPN_Access";
      ```
   3. 配置IPv6使能。

      ```
      SET IFIPV6ENABLE: IFNAME="Loopback1", ENABLEFLAG=TRUE;
      ```
   4. 配置接口IP地址。

      ```
      ADD IFIPV6ADDRESS:IFNAME="Loopback1",IPV6ADDRESS="FC00:2013::1",PREFIXLEN=128;
      ```
8. 全局激活BGP。

   ```
   SET BGP: BGPENABLE=TRUE, ASNUM="60001";
   ```
9. 配置BGP。
   1. 增加BGP VPN实例。

      ```
      ADD BGPVRF: VRFNAME="VPN_Access", DEFAULTAFTYPE=noaf, ROUTERID="10.90.7.160";
      ```

      * 此处配置的“ROUTERID”是BGP VPN实例级别的ROUTERID。

        IPv4v6双栈时，IPv4 BGP VPN实例地址族和IPv6 BGP VPN实例地址族共用此处配置的“ROUTERID”值。
      * 已配置IPv4v6双栈的BGP VPN实例地址族，若需删除IPv4的BGP VPN实例地址族配置，则：

        1、删除IPv4的配置前需查询并记录“ROUTERID”值。

        2、删除IPv4的配置后需查询“ROUTERID”值是否存在，若不存在则需通过**MOD BGPVRF**命令将“ROUTERID”参数设置为删除IPv4的配置前记录的“ROUTERID”值。否则IPv6 BGP重新协商时会因无“ROUTERID”值可用而导致协商失败。
   2. 增加BGP VPN地址族。

      ```
      ADD BGPVRFAF: VRFNAME="VPN_Access", AFTYPE=ipv6uni, MAXIMUMLOADBALANCE=2;
      ```

      * SR-IOV bonding场景（直连DCGW）或SR-IOV双平面场景（直连PE）场景，UEG对接2个负荷分担的路由设备，“MAXIMUMLOADBALANCE”设置为“2”。
      * SR-IOV bonding场景（直连PE），UEG对接1个路由设备，“MAXIMUMLOADBALANCE”设置为“1”。
   3. 增加BGP对等体。

      * SR-IOV bonding场景（直连DCGW）或SR-IOV双平面场景（直连PE）场景：

        ```
        ADD BGPPEER: VRFNAME="VPN_Access", ADDRESSTYPE=ipv6, PEERADDRV6="FC00:2013::2", REMOTEAS="60002", LOCALIFADDR="FC00:2013::1", LOCALIFNAME="Loopback1", EBGPMAXHOP=10;
        ADD BGPPEER: VRFNAME="VPN_Access", ADDRESSTYPE=ipv6, PEERADDRV6="FC00:2013::3", REMOTEAS="60002", LOCALIFADDR="FC00:2013::1", LOCALIFNAME="Loopback1", EBGPMAXHOP=10;
        ```

      * SR-IOV bonding场景（直连PE）：

        ```
        ADD BGPPEER: VRFNAME="VPN_Access", ADDRESSTYPE=ipv6, PEERADDRV6="FC00:2013::2", REMOTEAS="60002", LOCALIFADDR="FC00:2013::1", LOCALIFNAME="Loopback1", EBGPMAXHOP=10;
        ```
   4. 增加BGP引入路由。

      ```
      ADD IMPORTROUTE: VRFNAME="VPN_Access", AFTYPE=ipv6uni, IMPORTPROTOCOL=wlr, MEDENABLE=FALSE;
      ```

      * 由于BGP协议自身不能发现路由，所以需要引入其他协议的路由（如静态路由或WLR等）注入到BGP路由表中，从而将这些路由在AS之内和AS之间传播。
      * 对于N6口，两个UPF上的UE地址段存在重叠且需要对外发布网段路由时，需要将“MEDENABLE”设置为“TRUE”，并设置备UPF的“MED”值大于主UPF的“MED”值。

## 验证方法

1. 查看各网元间的路由连接是否正常。

   执行**PING**命令，查看VNF与对端网元间的路由连接是否正常。

   如果使用了VPN组网，还需使用“VPN实例名称（VPNNAME）”指定VPN实例，这样才能验证VPN实例路由是否正常。

   * 如果收到对端网元的响应且响应报文中有成功收发包的个数，表明连接正常，请执行2。
   * 如果连续出现timeout，表明链路不通，请检查本端或承载网是否存在物理接口故障或者路由配置错误，请执行3。
2. 执行**PING**命令，在DC-GW上检查DC-GW接口IP与VNF外联口IP之间是否路由可达。

   需要在DC-GW上分别PING VNF上的负荷分担关系的每个外联口的IP，且能PING通。

   * 是，请执行4。
   * 否，请联系华为技术支持工程师处理（例如检查DC-GW上是否存在到VNF BGP IP的路由，下一跳分别是VNF的负荷分担关系的每个外联口的IP），然后重新执行2。
3. 执行**LST INTERFACE**命令，查看接口状态及信息是否与规划数据一致。

   * 如果一致，请执行4。
   * 如果不一致，请参考“操作步骤”修改配置后，重新执行1。
4. 执行**LST BGPPEER**命令，查看BGP对等体配置是否与规划数据一致。
   * 如果一致，请执行5。
   * 如果不一致，请参考“操作步骤”修改配置后，重新执行1。
5. 执行**DSP BGPPEERINFO**命令，检查BGP对等体条数是否正确及BGP对等体状态是否为Established。

   本步骤的显示结果中的BGP对等体的条数与LST BGPPEER中查询的对等体的条数相等，且“对等体状态”为“Established”。

   * 是，调测结束。
   * 否，请执行6。
6. 收集信息并寻求技术支持。

   1. 执行**EXP MML**命令将当前配置数据导出为MML脚本文件并保存。
   2. 收集并保存上述所有查询信息。
   3. 查看并收集对端设备配置及接口状态信息。
   4. 收集归纳所有信息并联系华为技术支持解决。

版权所有 © 华为技术有限公司