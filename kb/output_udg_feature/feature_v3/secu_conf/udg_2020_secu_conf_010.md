# 配置互访流量的重定向功能

* 操作场景
* 必备事项
* 操作步骤
* 任务示例

## 操作场景

重定向功能可以防止上行报文可能存在的报文攻击问题。通过重定向功能的设置保证了在同一UDG内部同一VPN的UE用户之间报文转发的安全。

* 适用于PGW-U、UPF。
* 本文中的重定向设备以Firewall为例。
* PGW-U/UPF内置NAT功能时，不支持UE互访。

UDG报文重定向示意图如图1和图2所示。

图2所示方案非华为数通标准方案，如需使用，请与数通工程师达成一致。

**图1** UDG报文重定向示意图（DC-GW上基于独立VPN实现重定向）

如图1，采用DC-GW上基于独立VPN实现重定向的方案时，组网要求如下：

* DCGW上接收UPF上行报文的接口（接口2）和向UPF发送下行报文的接口（接口5）分开，且两个接口绑定的VPN实例不同。
* DC-GW上接口2发布缺省路由给PGW-U/UPF，不接收PGW-U/UPF发布的UE路由。

  接口3绑定的VPN实例与接口2相同，接口3接收PE侧路由，但不能把UE路由发布给PE侧。
* DC-GW上接口5需要接收PGW-U/UPF发布的UE路由，不能向PGW-U/UPF发布缺省路由。

  接口4绑定的VPN实例与接口5相同，接口4发布UE路由给PE，但不接收PE侧路由。
* UDG上指定VPN的用户的所有上行报文均发送到重定向设备，由重定向设备安全过滤后基于目的IP转发报文。
* UDG上发送上行报文的接口（子接口1）和接收下行报文的接口（子接口6）分开，但两个子接口绑定的VPN实例相同。

  子接口1和子接口6的VLAN不复用，IP地址段不复用。UDG子接口1不对外发布UE路由（不需要引入wlr路由）。

**图2** UDG报文重定向示意图（DC-GW上基于ACL+重定向IP实现重定向）

如图2，采用DC-GW上基于ACL+重定向IP实现重定向方案时，组网要求如下：

* DC-GW上需完成ACL及重定向IP等策略路由的相关配置。
* UDG发送上行报文（重定向报文和普通N6/SGi报文）和接收用户下行报文的子接口复用（单子接口），VLAN复用，VPN复用，IP地址段复用。

## 必备事项

前提条件

如果运营商规划采用VPN组网方式，则操作员在执行本操作前应已创建了相应的VPN实例。

数据

**表1** 业务数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| 全局SGi重定向开关 | IPV4全局Gi重定向开关（V4GIREDIRSWITCH） | ENABLE | 本端规划 | **SET GIREDIRECTFUNC** |
|  | IPV6全局Gi重定向开关（V6GIREDIRSWITCH） | ENABLE | 本端规划 |  |
| 基于VPN的SGi接口重定向（IPv4） | 需绑定的VPN实例名（VPNINSTANCE） | ispvpn1 | 本端规划 | 此处是基于VPN实现UE互访，即：VPN和一个APN关联时，则是同一APN内的UE互访；VPN和多个APN关联时，则是同一APN内的UE互访+不同APN间的UE互访。  **ADD GIREDIRECTPARA**   * “IPv4重定向IP地址（IPV4ADDRESS）”是重定向设备的IPv4地址。 * “IPv6重定向IP地址（IPV6ADDRESS）”是重定向设备的IPv6地址。 |
|  | 重定向的目的地址类型（IPTYPE） | IPv4 | 全网规划 |  |
|  | IPv4重定向动作（V4REDIRIPTYPE） | IPADDRESS | 全网规划 |  |
|  | IPv4重定向IP地址（IPV4ADDRESS） | 10.1.1.1 | 全网规划 |  |
| 基于VPN的SGi接口重定向（IPv6） | 需绑定的VPN实例名（VPNINSTANCE） | ispvpn1 | 本端规划 |  |
|  | 重定向的目的地址类型（IPTYPE） | IPv6 | 全网规划 |  |
|  | IPv6重定向动作（V6REDIRIPTYPE） | IPADDRESS | 全网规划 |  |
|  | IPv6重定向IP地址（IPV6ADDRESS） | FC00::10:1:1:1 | 全网规划 |  |

**表2** 外联口IP及路由数据（BGP over静态路由）

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| VPN实例 | VPN实例名称（VRFNAME） | ispvpn1 | 全网规划 | 与APN绑定的VPN实例相同。VRFRD取值此处以复用loopback接口IP为例。  **ADD L3VPNINST**  **ADD VPNINSTAF** |
|  | 地址族类型(AFTYPE) | * ipv4uni * ipv6uni | - |  |
|  | 路由标识（VRFRD） | 192.168.225.138:100 | 全网规划 |  |
| BGP本端IP | 接口名（IFNAME） | Loopback8 | 本端规划 | **ADD INTERFACE** |
|  | VPN实例名称（VRFNAME） | ispvpn1 | 已配置数据中获取 | **ADD IPBINDVPN** |
|  | IPv4地址（IFIPADDR） | 192.168.225.138 | 全网规划 | **ADD IFIPV4ADDRESS** |
|  | IPv4地址掩码（SUBNETMASK） | 255.255.255.255 | 固定取值 |  |
|  | IPv6地址（IPV6ADDRESS） | FC00::225:138 | 全网规划 | **ADD IFIPV6ADDRESS** |
|  | IPv6地址前缀（PREFIXLEN） | 128 | 固定取值 |  |
| BGP VPN实例 | VPN实例名称（VRFNAME） | ispvpn1 | 已配置数据中获取 | **ADD BGPVRF** |
|  | 默认地址族（DEFAULTAFTYPE） | noaf | 固定取值 |  |
|  | 路由器标识（ROUTERID） | 192.168.225.138 | 已配置数据中获取 |  |
| BGP VPN实例地址族 | VPN实例名称（VRFNAME） | ispvpn1 | 已配置数据中获取 | **ADD BGPVRFAF** |
|  | 地址族类型（AFTYPE） | * ipv4uni * ipv6uni | 本端规划 |  |
|  | 最大等价路由数（MAXIMUMLOADBALANCE） | 2 | 与对端协商 |  |
| BGP Peer | 地址类型（ADDRESSTYPE） | * ipv4 * ipv6 | 本端规划 | **ADD BGPPEER**   * “PEERADDR”是BGP Peer的IPv4地址。 * “PEERADDRV6”是BGP Peer的IPv6地址。   DC-GW上基于独立VPN实现重定向时，DC-GW上使用不同的VPN，分别用于接收UDG发送的上行报文及向UDG发送UE的下行报文。  即UDG上一个本端BGP地址，需要分别和DC-GW上两个VPN的loopback接口IP分别建立BGP邻居。UDG对接2个DC-GW，所以需要规划4个BGP Peer IP。 |
|  | IPv4对等体地址（PEERADDR） | * 192.168.78.1 * 192.168.78.2 * 192.168.79.1 * 192.168.79.2 | 全网规划 |  |
|  | IPv6对等体地址（PEERADDRV6） | * FC00:78:1 * FC00::78:2 * FC00::79:1 * FC00::79:2 | 全网规划 |  |
|  | 对等体AS号（REMOTEAS） | 60002 | 全网规划 | BGP Peer的AS号。 |
|  | 本地接口地址（LOCALIFADDR） | 192.168.225.138 | 已配置数据中获取 | BGP本端IP。上下行接口复用。 |
|  | 本地接口地址（LOCALIFADDR） | FC00::225:138 | 已配置数据中获取 |  |
|  | 本地接口名称（LOCALIFNAME） | Loopback8 | 已配置数据中获取 |  |
|  | EBGP最大跳数（EBGPMAXHOP） | 10 | 本端规划 | 不小于到Peer之间的实际跳数，无法确认时，可设置为10。  如最大跳数设置过小，会导致BGP邻居建立失败。 |
| 引入WLR路由 | VPN实例名称（VRFNAME） | ispvpn1 | 已配置数据中获取 | **ADD IMPORTROUTE** |
|  | 地址族类型（AFTYPE） | * ipv4uni * ipv6uni | - |  |
|  | 路由协议（IMPORTPROTOCOL） | wlr | 固定取值 |  |
|  | 使能MED（MEDENABLE） | FALSE | 固定取值 |  |
|  | MED（MED） | 0 | 固定取值 |  |
| 以太Trunk模板 | 以太Trunk模板ID（ETHTRUNKTMPID） | 6 | 本端规划 | **ADD AUTOSCALINGETHTRUNK** |
|  | 虚拟网卡ID列表（VNICLIST） | 6  7 | 本端规划 |  |
| 外联口IP、VLAN（IPv4） | 服务名称（SERVICENAME） | * ServName\_ispvpn1\_2008 * ServName\_ispvpn1\_2009 | 本端规划 | **ADD AUTOSCALINGSERVICE**  此处以下行接口（UDG用于接收重定向设备、PDN/DN Server发送的UE报文）所属VLAN是2008，上行接口（UDG用于发送上行报文到重定向设备、PDN/DN Server）所属VLAN是2009为例。  DC-GW上基于独立VPN实现重定向时，需要规划VLAN是2009的上行接口；DC-GW上基于ACL+重定向IP实现重定向时，仅规划VLAN是2008的接口即可。 |
|  | VPN实例名称（VPNNAME） | ispvpn1 | 已配置数据中获取 |  |
|  | 地址族（AFTYPE） | IPv4 | - |  |
|  | 以太Trunk模板ID（ETHTRUNKTMPID） | 6 | 已配置数据中获取 |  |
|  | VLAN ID（VLANID） | 2008  2009 | 全网规划 |  |
|  | 起始地址（BEGINADDR4） | * 192.168.88.2 * 192.168.89.2 | 全网规划 |  |
|  | 结束地址（ENDADDR4） | * 192.168.88.30 * 192.168.89.30 | 全网规划 |  |
|  | 地址池掩码长度（MASKLEN） | 27  27 | 全网规划 |  |
| 外联口IP、VLAN（IPv6） | 服务名称（SERVICENAME） | * ServName\_ispvpn1\_2008\_v6 * ServName\_ispvpn1\_2009\_v6 | 本端规划 |  |
|  | VPN实例名称（VPNNAME） | ispvpn1 | 已配置数据中获取 |  |
|  | 地址族（AFTYPE） | IPv6 | - |  |
|  | 以太Trunk模板ID（ETHTRUNKTMPID） | 6 | 已配置数据中获取 |  |
|  | VLAN ID（VLANID） | 2008  2009 | 全网规划 |  |
|  | 起始地址（BEGINADDR6） | * FC00::88C2 * FC00::89C2 | 全网规划 |  |
|  | 结束地址（ENDADDR6） | * FC00::88DE * FC00::89DE | 全网规划 |  |
|  | 地址池掩码长度（MASKLEN） | * 123 * 123 | 全网规划 |  |
| 单臂BFD（IPv4） | 模板名称（TEMPLATENAME） | * BFD\_2008 * BFD\_2009 | 本端规划 | **ADD AUTOSCALINGBFD**  此处以单臂BFD为例。双向BFD时，请使用**ADD AUTOSCALINGSRBFD**命令。 |
|  | BFD类型（BFDTYPE） | Static | 固定取值 |  |
|  | 服务名称（SERVICENAME） | * ServName\_ispvpn1\_2008 * ServName\_ispvpn1\_2009 | 已配置数据中获取 |  |
|  | IP版本（IPVERSION） | IPv4 | - |  |
|  | 目的地址（DESTADDR4） | * 192.168.88.1 * 192.168.89.1 | 全网规划 |  |
|  | 单臂Echo会话的收包间隔（ms）（MINECHORXINT） | 500 | 固定取值 |  |
|  | 检测倍数（DETECTMULTI） | 4 |  |  |
|  | 单臂Echo（ONEARMECHO） | TRUE |  |  |
| 单臂BFD（IPv6） | 模板名称（TEMPLATENAME） | * BFD\_2008\_v6 * BFD\_2009\_v6 | 本端规划 | **ADD AUTOSCALINGBFD**  此处以单臂BFD为例。双向BFD时，请使用**ADD AUTOSCALINGSRBFD**命令。 |
|  | BFD类型（BFDTYPE） | Static | 固定取值 |  |
|  | 服务名称（SERVICENAME） | * ServName\_ispvpn1\_2008\_v6 * ServName\_ispvpn1\_2009\_v6 | 已配置数据中获取 |  |
|  | IP版本（IPVERSION） | IPv6 | - |  |
|  | 目的地址（DESTADDR6） | * FC00::88C1 * FC00::89C1 | 全网规划 |  |
|  | 单臂Echo会话的收包间隔（ms）（MINECHORXINT） | 500 | 固定取值 |  |
|  | 检测倍数（DETECTMULTI） | 4 |  |  |
|  | 单臂Echo（ONEARMECHO） | TRUE |  |  |
| 到BGP Peer的静态路由（IPv4） | 服务名称（SERVICENAME） | * ServName\_ispvpn1\_2008 * ServName\_ispvpn1\_2008 * ServName\_ispvpn1\_2009 * ServName\_ispvpn1\_2009 | 已配置数据中获取 | **ADD AUTOSCALINGSRROUTE** |
|  | VPN实例名称 (VRFNAME) | ispvpn1 | 已配置数据中获取 | - |
|  | 路由前缀IPv4（PREFIX4） | * 192.168.78.1 * 192.168.78.2 * 192.168.79.1 * 192.168.79.2 | 全网规划 | BGP Peer的IP地址。 |
|  | 路由掩码长度（MASKLENGTH） | 32 | - |  |
|  | 路由下一跳IPv4（NEXTHOP4） | * 192.168.88.1 * 192.168.88.1 * 192.168.89.1 * 192.168.89.1 | 全网规划 | DC-GW的接口IP。 |
|  | 地址族（IPVERSION） | IPv4 | - | - |
|  | IPv4路由下一跳分配方式（NEXTHOPALLOCTYPE4） | CONFIG | 本端规划 | - |
|  | BFD使能标识 （BFDENABLE） | TRUE | 固定取值 | - |
|  | BFD模板名称（BFDTEMPLATENAME） | * BFD\_2008 * BFD\_2008 * BFD\_2009 * BFD\_2009 | 已配置数据中获取 | 使用**ADD AUTOSCALINGBFD**命令定义的BFD模板名称。 |
| 到BGP Peer的静态路由（IPv6） | 服务名称（SERVICENAME） | * ServName\_ispvpn1\_2008\_v6 * ServName\_ispvpn1\_2008\_v6 * ServName\_ispvpn1\_2009\_v6 * ServName\_ispvpn1\_2009\_v6 | 已配置数据中获取 | **ADD AUTOSCALINGSRROUTE** |
|  | VPN实例名称 (VRFNAME) | ispvpn1 | 已配置数据中获取 | - |
|  | 路由前缀IPv6（PREFIX6） | * FC00:78:1 * FC00::78:2 * FC00::79:1 * FC00::79:2 | 全网规划 | BGP Peer的IP地址。 |
|  | 路由掩码长度（MASKLENGTH） | 128 | - |  |
|  | 路由下一跳IPv6（NEXTHOP6） | * FC00::88C1 * FC00::88C1 * FC00::89C1 * FC00::89C1 | 全网规划 | DC-GW的接口IP。 |
|  | 地址族（IPVERSION） | IPv6 | - | - |
|  | IPv6路由下一跳分配方式（NEXTHOPALLOCTYPE6） | CONFIG | 本端规划 | - |
|  | BFD使能标识 （BFDENABLE） | TRUE | 固定取值 | - |
|  | BFD模板名称（BFDTEMPLATENAME） | * BFD\_2008\_v6 * BFD\_2008\_v6 * BFD\_2009\_v6 * BFD\_2009\_v6 | 已配置数据中获取 | 使用**ADD AUTOSCALINGBFD**命令定义的BFD模板名称。 |

**表3** 外联口IP及路由数据（OSPF动态路由）

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| VPN实例 | VPN实例名称（VRFNAME） | ispvpn1 | 全网规划 | 与APN绑定的VPN实例相同。VRFRD取值此处以复用loopback接口IP为例。  **ADD L3VPNINST**  **ADD VPNINSTAF** |
|  | 地址族名称(AFTYPE) | * ipv4uni * ipv6uni | - |  |
|  | 路由标识（VRFRD） | 192.168.225.138:100 | 全网规划 |  |
| OSPF Loopback接口IP  （仅IPv4需要） | 接口名（IFNAME） | Loopback8 | 本端规划 | **ADD INTERFACE**  **ADD OSPFINTERFACE** |
|  | VPN实例名称（VRFNAME） | ispvpn1 | 已配置数据中获取 | **ADD IPBINDVPN** |
|  | 接口IPv4地址（IFIPADDR） | 192.168.225.138 | 全网规划 | **ADD IFIPV4ADDRESS** |
|  | 接口IPv4地址掩码（SUBNETMASK） | 255.255.255.255 | 固定取值 |  |
| 以太Trunk模板 | 以太Trunk模板ID（ETHTRUNKTMPID） | 6 | 本端规划 | **ADD AUTOSCALINGETHTRUNK** |
|  | 虚拟网卡ID列表（VNICLIST） | 6  7 | 本端规划 |  |
| 外联口IP、VLAN（IPv4） | 服务名称（SERVICENAME） | * ServName\_ispvpn1\_2008 * ServName\_ispvpn1\_2009 | 本端规划 | **ADD AUTOSCALINGSERVICE**  此处以下行接口（UDG用于接收重定向设备、PDN/DN Server发送的UE报文）所属VLAN是2008，上行接口（UDG用于发送上行报文到重定向设备、PDN/DN Server）所属VLAN是2009为例。  DC-GW上基于独立VPN实现重定向时，需要规划VLAN是2009的上行接口；DC-GW上基于ACL+重定向IP实现重定向时，仅规划VLAN是2008的接口即可。 |
|  | VPN实例名称（VPNNAME） | ispvpn1 | 已配置数据中获取 |  |
|  | 地址族（AFTYPE） | IPv4 | - |  |
|  | 以太Trunk模板ID（ETHTRUNKTMPID） | 6 | 已配置数据中获取 |  |
|  | VLAN ID（VLANID） | * 2008 * 2009 | 全网规划 |  |
|  | 起始地址（BEGINADDR4） | * 192.168.88.2 * 192.168.89.2 | 全网规划 |  |
|  | 结束地址（ENDADDR4） | * 192.168.88.30 * 192.168.89.30 | 全网规划 |  |
|  | 地址池掩码长度（MASKLEN） | * 27 * 27 | 全网规划 |  |
| 外联口IP、VLAN（IPv6） | 服务名称（SERVICENAME） | * ServName\_ispvpn1\_2008\_v6 * ServName\_ispvpn1\_2009\_v6 | 本端规划 |  |
|  | VPN实例名称（VPNNAME） | ispvpn1 | 已配置数据中获取 |  |
|  | 地址族（AFTYPE） | IPv6 | - |  |
|  | 以太Trunk模板ID（ETHTRUNKTMPID） | 6 | 已配置数据中获取 |  |
|  | VLAN ID（VLANID） | * 2008 * 2009 | 全网规划 |  |
|  | 起始地址（BEGINADDR6） | * FC00::88C2 * FC00::89C2 | 全网规划 |  |
|  | 结束地址（ENDADDR6） | * FC00::88DE * FC00::89DE | 全网规划 |  |
|  | 地址池掩码长度（MASKLEN） | * 123 * 123 | 全网规划 |  |
| OSPF进程号及Area ID | 使能OSPF（OSPFENABLE） | TRUE | 固定取值 | **ADD AUTOSCALINGSERVICE** |
|  | OSPF进程ID（OSPFPROCID） | * 8 * 9 | 本端规划 | **ADD AUTOSCALINGSERVICE**   * IPv4 MML： **ADD OSPF**  **ADD OSPFAREA** * IPv6 MML： **ADD OSPFV3**  **ADD OSPFV3AREA**   存在多个进程时，进程号不能重复。  此处以OSPF进程8为接收下行报文的进程，OSPF进程9为发送上行报文的 |
|  | 区域号（AREAID） | 0.0.0.5 | 全网规划 | 需要和对接的DC-GW接口的OSPF区域ID相同。 |
|  | 区域类型（AREATYPE） | NSSA | 全网规划 | 两个接口若要建立邻居关系，则Area Type必须相同。 |
|  | 使能入方向的流量策略（TPINENABLE） | FALSE | - | - |
|  | 使能出方向的流量策略（TPOUTENABLE） | FALSE | - | - |
| 引入WLR路由 | OSPF进程ID（PROCID） | 8 | 已规划数据中获取 | 仅和接收下行报文相关的OSPF进程发布wlr路由。   * IPv4 MML：**ADD OSPFIMPORTROUTE** * IPv6 MML：**ADD OSPFV3IMPORTROUTE** |
|  | 拓扑标识（TOPOID） | 0 | 固定取值 |  |
|  | 协议分类 （PROTOCOL） | wlr | 固定取值 |  |

PGW-U/UPF上行接口不发布任何路由，下行接口不接收任何路由。对应的路由策略如表4所示。

**表4** 路由策略数据

| 类别 | 参数名称 | 取值样例 | 获取方法 | 说明 |
| --- | --- | --- | --- | --- |
| 路由策略节点 | 路由策略名字（POLICYNAME） | routepolicy\_deny | 本端规划 | **ADD ROUTEPOLICY** |
|  | 路由策略节点号（NODESEQUENCE） | 50 | 本端规划 | **ADD ROUTEPOLICYNODE** |
|  | 匹配模式（MATCHMODE） | deny | 固定取值 | 配置的路由策略节点，用于拒绝接收任何路由。 |
| IP前缀列表（IPv4） | IP前缀列表名字（NAME） | ip-prefix\_test | 本端规划 | **ADD PREFIXFILTERNODE** |
|  | IP前缀列表节点号（NODESEQUENCE） | 50 | 已配置数据中获取 |  |
|  | IP前缀列表匹配模式（MATCHMODE） | deny | 固定取值 |  |
|  | IP地址（ADDRESS） | 0.0.0.0 | 固定取值 |  |
|  | 掩码长度（MASKLENGTH） | 0 | 固定取值 |  |
|  | 大于或等于（GREATEREQUAL） | 0 | 固定取值 |  |
|  | 小于或等于（LESSEQUAL） | 32 | 固定取值 |  |
| IP前缀列表（IPv6） | IPv6前缀列表名字（NAME） | ip-prefix\_test\_v6 | 本端规划 | **ADD IPV6PREFIXFILTERNODE** |
|  | IPv6前缀列表节点号（NODESEQUENCE） | 50 | 已配置数据中获取 |  |
|  | IPv6前缀列表匹配模式（MATCHMODE） | deny | 固定取值 |  |
|  | IPv6地址（ADDRESS） | 0:0:0:0:0:0:0:0 | 固定取值 |  |
|  | 掩码长度（MASKLENGTH） | 0 | 固定取值 |  |
|  | 掩码长度匹配范围下限（GREATEREQUAL） | 0 | 固定取值 |  |
|  | 掩码长度匹配范围上限（LESSEQUAL） | 128 | 固定取值 |  |
| 路由策略节点和IP前缀列表绑定（IPv4） | 路由策略名字（POLICYNAME） | routepolicy\_deny | 已配置数据中获取 | **ADD MATCHDESTPREFIXFILTER** |
|  | 路由策略节点号（NODESEQUENCE） | 50 | 已配置数据中获取 |  |
|  | IP前缀列表名字（PREFIXNAME） | ip-prefix\_test | 已配置数据中获取 |  |
| 路由策略节点和IP前缀列表绑定（IPv6） | 路由策略名字（POLICYNAME） | routepolicy\_deny | 已配置数据中获取 | **ADD MATCHDESTPREFIX6FILTER** |
|  | 路由策略节点号（NODESEQUENCE） | 50 | 已配置数据中获取 |  |
|  | IPv6前缀列表名字（IPV6PREFIXNAME） | ip-prefix\_test\_v6 | 已配置数据中获取 |  |
| BGP对等体地址族应用路由策略（下行接口对应的BGP Peer）  （BGP over静态路由适用） | VPN实例名称（VRFNAME） | ispvpn1 | 已配置数据中获取 | **ADD BGPPEERAF**   * 不接收BGP Peer 192.168.78.1和192.168.78.2发布的任何路由。 * 不接收BGP Peer FC00::78:1和FC00::78:2发布的任何路由。 |
|  | 地址族类型（AFTYPE） | * ipv4uni * ipv6uni | 本端规划 |  |
|  | IPv4对等体地址（REMOTEADDRESS） | * 192.168.78.1 * 192.168.78.2 | 已配置数据中获取 |  |
|  | IPv6对等体地址（REMOTEADDRESSV6） | * FC00::78:1 * FC00::78:2 | 已配置数据中获取 |  |
|  | 引入路由策略（IMPORTRTPOLICYNAME） | routepolicy\_deny | 已配置数据中获取 |  |
| BGP对等体地址族应用路由策略（上行接口对应的BGP Peer）  （BGP over静态路由适用） | VPN实例名称（VRFNAME） | ispvpn1 | 已配置数据中获取 | **ADD BGPPEERAF**   * 不向BGP Peer 192.168.79.1和192.168.79.2发布任何路由。 * 不向BGP Peer FC00::79:1和FC00::79:2发布任何路由。 |
|  | 地址族类型（AFTYPE） | * ipv4uni * ipv6uni | 本端规划 |  |
|  | IPv4对等体地址（REMOTEADDRESS） | * 192.168.79.1 * 192.168.79.2 | 已配置数据中获取 |  |
|  | IPv6对等体地址（REMOTEADDRESSV6） | * FC00::79:1 * FC00::79:2 | 已配置数据中获取 |  |
|  | 发布路由策略（EXPORTRTPOLICYNAME） | routepolicy\_deny | 已配置数据中获取 |  |
| OSPF过滤策略  下行接口进程上，不引入任何路由；上行接口进程上，不发布任何路由。 | 进程号（PROCID） | * 8 * 9 | 已配置数据中获取 | * IPv4 MML：**ADD OSPFFILTERPOLICY** * IPv6 MML：**ADD OSPFV3FILTERPOLICY**   import表示对接收到的路由进行过滤。  export表示对通过OSPF引入的路由信息向外发布时进行过滤。  “FILTERTYPE”设置为“export”时，可指定对外不发布路由的协议类型，此处以对外不发布wlr路由为例（PROTOCOL设置为wlr）。 |
|  | 过滤方向（FILTERTYPE） | * import * export | 本端规划 |  |
|  | 过滤规则类型（TYPE） | ip\_prefix | 本端规划 |  |
|  | IP前缀列表名称（IPPREFIX） | * ip-prefix\_test * ip-prefix\_test\_v6 | 已配置数据中获取 |  |
|  | 协议分类（PROTOCOL） | wlr | 本端规划 |  |

## 操作步骤

1. 以下命令在“MML命令行 - UDG”窗口上执行。设置全局的SGi重定向开关。

   **SET GIREDIRECTFUNC**:V4GIREDIRSWITCH=ENABLE,V6GIREDIRSWITCH=ENABLE;

   当全局的SGi接口重定向开关为不使能时，整个UDG的所有VPN的SGi接口重定向功能都会被关闭。使能全局的SGi接口重定向后，还要根据各个VPN的重定向配置来决定是否进行SGi接口的重定向。
2. 设置基于某个VPN的SGi重定向开关及重定向报文的目的地址。

   **ADD GIREDIRECTPARA**:VPNINSTANCE="需绑定的VPN实例名",IPTYPE=IPv4,V4REDIRIPTYPE=IPADDRESS,IPV4ADDRESS="IPV4地址";
3. 设置默认VPN（\_public\_）用户的SGi重定向开关及重定向报文的目的地址。

   **ADD GIREDIRECTPARA**:VPNINSTANCE="\_public\_",IPTYPE=IPv4,V4REDIRIPTYPE=IPADDRESS,IPV4ADDRESS="IPV4地址";
4. 设置IPv6 Gi redirect。

   **ADD GIREDIRECTPARA**:VPNINSTANCE="VPN Instance to Bind",IPTYPE=IPv6,V6REDIRIPTYPE=IPADDRESS,IPV6ADDRESS="IPV6地址";
5. 配置外联口IP及路由。

   详细操作步骤请参见《UDG 初始配置与调测》。

## 任务示例

任务描述

对同一UDG内部的UE之间报文进行重定向，APN绑定的VPN实例以ispvpn1为例。

重定向方案以DC-GW上基于独立VPN实现重定向为例。6和7选择一种路由方案即可。

* 采用BGP over静态路由时，需配置6，BFD以单臂BFD为例。
* 采用OSPF动态路由时，需配置7。

脚本

1. 配置全局的Gi接口重定向功能。

   ```
   SET GIREDIRECTFUNC:V4GIREDIRSWITCH=ENABLE,V6GIREDIRSWITCH=ENABLE;
   ```
2. 配置VPN实例。

   ```
   //IPv4, IPv6, or IPv4v6:
   ADD L3VPNINST:VRFNAME="ispvpn1";
   ADD VPNINST: VPNINSTANCE="ispvpn1";

   //IPv4:
   ADD VPNINSTAF:VRFNAME="ispvpn1", AFTYPE=ipv4uni, VRFRD="192.168.225.138:100";

   //IPv6:
   ADD VPNINSTAF:VRFNAME="ispvpn1", AFTYPE=ipv6uni, VRFRD="192.168.225.138:100";
   ```
3. 配置基于VPN的Gi接口重定向。

   //IPv4：

   ```
   ADD GIREDIRECTPARA:VPNINSTANCE="ispvpn1",IPTYPE=IPv4,V4REDIRIPTYPE=IPADDRESS,IPV4ADDRESS="10.1.1.1";
   ```

   //IPv6：

   ```
   ADD GIREDIRECTPARA:VPNINSTANCE="ispvpn1",IPTYPE=IPv6,V6REDIRIPTYPE=IPADDRESS,IPV6ADDRESS="FC00::10:1:1:1";
   ```
4. 配置默认VPN用户的Gi接口重定向。

   //IPv4：

   ```
   ADD GIREDIRECTPARA:VPNINSTANCE="_public_",IPTYPE=IPv4,V4REDIRIPTYPE=IPADDRESS,IPV4ADDRESS="10.1.1.1";
   ```

   //IPv6：

   ```
   ADD GIREDIRECTPARA:VPNINSTANCE="_public_",IPTYPE=IPv6,V6REDIRIPTYPE=IPADDRESS,IPV6ADDRESS="FC00::10:1:1:1";
   ```
5. 关闭自动配置开关。
   1. 查询自动配置开关。

      ```
      LST AUTOCONFIG:;
      ```

      * 如果“自动配置开关”值为“是”，需要执行5.b和5.c关闭自动配置开关。
      * 如果“自动配置开关”值为“否”，说明已关闭自动配置开关，请跳转到6或7。
   2. 查询自动部署维护助手“autoscaling\_autoconfig.py”的状态，确保状态为“准备好状态（Ready）”或者查询无该脚本，以保证当前设备不在自动部署过程中。因为若系统当前有正在进行的自动部署，而自动部署生效有时延，此时若关闭自动配置开关，会影响系统配置效果。

      ```
      DSP OPSASSISTSTATE:;
      ```
   3. 关闭自动配置开关。自动化配置命令只有在自动配置开关为关闭的状态下才可执行，因此需要提前关闭。

      ```
      SET AUTOCONFIG:SWITCHFLAG=FALSE;
      ```
6. 采用BGP over静态路由时，配置外联口IP及路由。此处以APN绑定的VPN实例是ispvpn1为例。

   上下行的配置区别是：PGW-U/UPF上下行使用的子接口不同，VLAN不同，外联口IP地址不同，BGP Peer IP不同，VPN相同，BGP本端IP相同，且上行不需要引入wlr路由。如图3所示。

   如下PGW-U/UPF脚本以对接2个DC-GW（M-LAG组网）为例，为方便绘图，图形中仅呈现一个DC-GW图标。

   **图3** 外联口IP&路由（BGP over静态路由）

   1. 配置下行报文使用的外联口IP及路由。UDG用于接收重定向设备、PDN/DN Server发送的UE报文。IPv4组网时，不接收BGP Peer 192.168.78.1和192.168.78.2发布的任何路由。IPv6组网时，不接收BGP Peer FC00::78:1和FC00::78:2发布的任何路由。

      ```
      //IPv4, IPv6, or IPv4v6:
      ADD INTERFACE:IFNAME="LoopBack8";
      ADD IPBINDVPN:IFNAME="LoopBack8",VRFNAME="ispvpn1";

      //IPv4:
      ADD IFIPV4ADDRESS:IFNAME="LoopBack8",IFIPADDR="192.168.225.138",SUBNETMASK="255.255.255.255",ADDRTYPE=main;

      //IPv6:
      SET IFIPV6ENABLE: IFNAME="Loopback8", ENABLEFLAG=TRUE;
      ADD IFIPV6ADDRESS:IFNAME="Loopback8",IPV6ADDRESS="FC00::225:138",PREFIXLEN=128;

      //Global:
      SET BFD: BFDENABLE=TRUE;
      SET BGP: BGPENABLE=TRUE, ASNUM="60001";

      //IPv4, IPv6, or IPv4v6:
      ADD BGPVRF: VRFNAME="ispvpn1", DEFAULTAFTYPE=noaf, ROUTERID="192.168.225.138";

      //IPv4:
      ADD BGPVRFAF: VRFNAME="ispvpn1", AFTYPE=ipv4uni, MAXIMUMLOADBALANCE=2;
      ADD BGPPEER: VRFNAME="ispvpn1", ADDRESSTYPE=ipv4, PEERADDR="192.168.78.1", REMOTEAS="60002", LOCALIFADDR="192.168.225.138", LOCALIFNAME="Loopback8", EBGPMAXHOP=10;
      ADD BGPPEER: VRFNAME="ispvpn1", ADDRESSTYPE=ipv4, PEERADDR="192.168.78.2", REMOTEAS="60002", LOCALIFADDR="192.168.225.138", LOCALIFNAME="Loopback8", EBGPMAXHOP=10;

      //IPv6:
      ADD BGPVRFAF: VRFNAME="ispvpn1", AFTYPE=ipv6uni, MAXIMUMLOADBALANCE=2;
      ADD BGPPEER: VRFNAME="ispvpn1", ADDRESSTYPE=ipv6, PEERADDRV6="FC00::78:1", REMOTEAS="60002", LOCALIFADDR="FC00::225:138", LOCALIFNAME="Loopback8", EBGPMAXHOP=10;
      ADD BGPPEER: VRFNAME="ispvpn1", ADDRESSTYPE=ipv6, PEERADDRV6="FC00::78:2", REMOTEAS="60002", LOCALIFADDR="FC00::225:138", LOCALIFNAME="Loopback8", EBGPMAXHOP=10;

      //IPv4:
      ADD IMPORTROUTE: VRFNAME="ispvpn1", AFTYPE=ipv4uni, IMPORTPROTOCOL=wlr, MEDENABLE=FALSE;

      //IPv6:
      ADD IMPORTROUTE: VRFNAME="ispvpn1", AFTYPE=ipv6uni, IMPORTPROTOCOL=wlr, MEDENABLE=FALSE;


      //IPv4, IPv6, or IPv4v6:
      ADD ROUTEPOLICY: POLICYNAME="routepolicy_deny";
      ADD ROUTEPOLICYNODE: POLICYNAME="routepolicy_deny", NODESEQUENCE=50, MATCHMODE=deny;

      //IPv4:
      ADD PREFIXFILTERNODE: NAME="ip-prefix_test", NODESEQUENCE=50, MATCHMODE=deny, ADDRESS="0.0.0.0", MASKLENGTH=0, GREATEREQUAL=0, LESSEQUAL=32, MATCHNETWORK=FALSE;
      ADD MATCHDESTPREFIXFILTER: POLICYNAME="routepolicy_deny", NODESEQUENCE=50, PREFIXNAME="ip-prefix_test";
      MOD BGPPEERAF: VRFNAME="ispvpn1", AFTYPE=ipv4uni, REMOTEADDRESS="192.168.78.1",IMPORTRTPOLICYNAME="routepolicy_deny";
      MOD BGPPEERAF: VRFNAME="ispvpn1", AFTYPE=ipv4uni, REMOTEADDRESS="192.168.78.2",IMPORTRTPOLICYNAME="routepolicy_deny";

      //IPv6:
      ADD IPV6PREFIXFILTERNODE: NAME="ip-prefix_test_v6", NODESEQUENCE=50, MATCHMODE=deny, ADDRESS="0:0:0:0:0:0:0:0", MASKLENGTH=0, MATCHNETWORK=FALSE, GREATEREQUAL=0, LESSEQUAL=128;
      ADD MATCHDESTPREFIX6FILTER: POLICYNAME="routepolicy_deny", NODESEQUENCE=50, IPV6PREFIXNAME="ip-prefix_test_v6";
      MOD BGPPEERAF: VRFNAME="ispvpn1", AFTYPE=ipv6uni, ADDRESSTYPE=ipv6, REMOTEADDRESSV6="FC00::78:1",IMPORTRTPOLICYNAME="routepolicy_deny";
      MOD BGPPEERAF: VRFNAME="ispvpn1", AFTYPE=ipv6uni, ADDRESSTYPE=ipv6, REMOTEADDRESSV6="FC00::78:2",IMPORTRTPOLICYNAME="routepolicy_deny";


      //IPv4, IPv6, or IPv4v6:
      ADD AUTOSCALINGETHTRUNK: ETHTRUNKTMPID=6, VNICLIST="6 7";

      //IPv4:
      ADD AUTOSCALINGSERVICE: SERVICENAME="ServName_ispvpn1_2008", VPNNAME="ispvpn1", AFTYPE=IPv4, IPALLOCTYPE4=USER_CONFIG, AUTOCFGIFTYPE=ETHTRUNK, ETHTRUNKTMPID=6, VLANID=2008, BEGINADDR4="192.168.88.2", ENDADDR4="192.168.88.30", MASKLEN=27; 
      ADD AUTOSCALINGBFD: TEMPLATENAME="BFD_2008", BFDTYPE=Static, SERVICENAME="ServName_ispvpn1_2008", IPVERSION=IPv4, DESTADDR4="192.168.88.1", MINECHORXINT=500, DETECTMULTI=4, ONEARMECHO=TRUE;
      ADD AUTOSCALINGSRROUTE: SERVICENAME="ServName_ispvpn1_2008", VRFNAME="ispvpn1", IPVERSION=IPv4, PREFIX4="192.168.78.1", MASKLENGTH=32, NEXTHOPALLOCTYPE4=CONFIG, NEXTHOP4="192.168.88.1", BFDENABLE=TRUE, DESCRIPTION="ispvpn1", BFDTEMPLATENAME="BFD_2008"; 
      ADD AUTOSCALINGSRROUTE: SERVICENAME="ServName_ispvpn1_2008", VRFNAME="ispvpn1", IPVERSION=IPv4, PREFIX4="192.168.78.2", MASKLENGTH=32, NEXTHOPALLOCTYPE4=CONFIG, NEXTHOP4="192.168.88.1", BFDENABLE=TRUE, DESCRIPTION="ispvpn1", BFDTEMPLATENAME="BFD_2008";

      //IPv6:
      ADD AUTOSCALINGSERVICE: SERVICENAME="ServName_ispvpn1_2008_v6", VPNNAME="ispvpn1", AFTYPE=IPv6, IPALLOCTYPE6=USER_CONFIG, AUTOCFGIFTYPE=ETHTRUNK, ETHTRUNKTMPID=6, VLANID=2008, BEGINADDR6="FC00::88C2", ENDADDR6="FC00::88DE", MASKLEN=123; 
      ADD AUTOSCALINGBFD: TEMPLATENAME="BFD_2008_v6", BFDTYPE=Static, SERVICENAME="ServName_ispvpn1_2008_v6", IPVERSION=IPv6, DESTADDR6="FC00::88C1", MINECHORXINT=500, DETECTMULTI=4, ONEARMECHO=TRUE;
      ADD AUTOSCALINGSRROUTE: SERVICENAME="ServName_ispvpn1_2008_v6", VRFNAME="ispvpn1", IPVERSION=IPv6, PREFIX6="FC00::78:1", MASKLENGTH=128, NEXTHOPALLOCTYPE6=CONFIG, NEXTHOP6="FC00::88C1", BFDENABLE=TRUE, DESCRIPTION="ispvpn1", BFDTEMPLATENAME="BFD_2008_v6"; 
      ADD AUTOSCALINGSRROUTE: SERVICENAME="ServName_ispvpn1_2008_v6", VRFNAME="ispvpn1", IPVERSION=IPv6, PREFIX6="FC00::78:2", MASKLENGTH=128, NEXTHOPALLOCTYPE6=CONFIG, NEXTHOP6="FC00::88C1", BFDENABLE=TRUE, DESCRIPTION="ispvpn1", BFDTEMPLATENAME="BFD_2008_v6";
      ```
   2. 配置上行报文使用的外联口IP及路由。UDG用于发送上行报文到重定向设备、PDN/DN Server。IPv4组网时，不向BGP Peer 192.168.79.1和192.168.79.2发布任何路由。IPv6组网时，不向BGP Peer FC00::79:1和FC00::79:2发布任何路由。

      ```
      //IPv4:
      ADD BGPPEER: VRFNAME="ispvpn1", ADDRESSTYPE=ipv4, PEERADDR="192.168.79.1", REMOTEAS="60002", LOCALIFADDR="192.168.225.138", LOCALIFNAME="Loopback8", EBGPMAXHOP=10;
      ADD BGPPEER: VRFNAME="ispvpn1", ADDRESSTYPE=ipv4, PEERADDR="192.168.79.2", REMOTEAS="60002", LOCALIFADDR="192.168.225.138", LOCALIFNAME="Loopback8", EBGPMAXHOP=10;

      //IPv4:
      MOD BGPPEERAF: VRFNAME="ispvpn1", AFTYPE=ipv4uni, REMOTEADDRESS="192.168.79.1",EXPORTRTPOLICYNAME="routepolicy_deny";
      MOD BGPPEERAF: VRFNAME="ispvpn1", AFTYPE=ipv4uni, REMOTEADDRESS="192.168.79.2",EXPORTRTPOLICYNAME="routepolicy_deny";

      //IPv4:
      ADD AUTOSCALINGSERVICE: SERVICENAME="ServName_ispvpn1_2009", VPNNAME="ispvpn1", AFTYPE=IPv4, IPALLOCTYPE4=USER_CONFIG, AUTOCFGIFTYPE=ETHTRUNK, ETHTRUNKTMPID=6, VLANID=2009, BEGINADDR4="192.168.89.2", ENDADDR4="192.168.89.30", MASKLEN=27; 
      ADD AUTOSCALINGBFD: TEMPLATENAME="BFD_2009", BFDTYPE=Static, SERVICENAME="ServName_ispvpn1_2009", IPVERSION=IPv4, DESTADDR4="192.168.89.1", MINECHORXINT=500, DETECTMULTI=4, ONEARMECHO=TRUE;
      ADD AUTOSCALINGSRROUTE: SERVICENAME="ServName_ispvpn1_2009", VRFNAME="ispvpn1", IPVERSION=IPv4, PREFIX4="192.168.79.1", MASKLENGTH=32, NEXTHOPALLOCTYPE4=CONFIG, NEXTHOP4="192.168.89.1", BFDENABLE=TRUE, DESCRIPTION="ispvpn1", BFDTEMPLATENAME="BFD_2009"; 
      ADD AUTOSCALINGSRROUTE: SERVICENAME="ServName_ispvpn1_2009", VRFNAME="ispvpn1", IPVERSION=IPv4, PREFIX4="192.168.79.2", MASKLENGTH=32, NEXTHOPALLOCTYPE4=CONFIG, NEXTHOP4="192.168.89.1", BFDENABLE=TRUE, DESCRIPTION="ispvpn1", BFDTEMPLATENAME="BFD_2009";

      //IPv6:
      ADD BGPPEER: VRFNAME="ispvpn1", ADDRESSTYPE=ipv6, PEERADDRV6="FC00::79:1", REMOTEAS="60002", LOCALIFADDR="FC00::225:138", LOCALIFNAME="Loopback8", EBGPMAXHOP=10;
      ADD BGPPEER: VRFNAME="ispvpn1", ADDRESSTYPE=ipv6, PEERADDRV6="FC00::79:2", REMOTEAS="60002", LOCALIFADDR="FC00::225:138", LOCALIFNAME="Loopback8", EBGPMAXHOP=10;

      //IPv6:
      MOD BGPPEERAF: VRFNAME="ispvpn1", AFTYPE=ipv6uni, ADDRESSTYPE=ipv6, REMOTEADDRESSV6="FC00::79:1",EXPORTRTPOLICYNAME="routepolicy_deny";
      MOD BGPPEERAF: VRFNAME="ispvpn1", AFTYPE=ipv6uni, ADDRESSTYPE=ipv6, REMOTEADDRESSV6="FC00::79:2",EXPORTRTPOLICYNAME="routepolicy_deny";

      //IPv6
      ADD AUTOSCALINGSERVICE: SERVICENAME="ServName_ispvpn1_2009_v6", VPNNAME="ispvpn1", AFTYPE=IPv6, IPALLOCTYPE6=USER_CONFIG, AUTOCFGIFTYPE=ETHTRUNK, ETHTRUNKTMPID=6, VLANID=2009, BEGINADDR6="FC00::89C2", ENDADDR6="FC00::89DE", MASKLEN=123; 
      ADD AUTOSCALINGBFD: TEMPLATENAME="BFD_2009_v6", BFDTYPE=Static, SERVICENAME="ServName_ispvpn1_2009_v6", IPVERSION=IPv6, DESTADDR6="FC00::89C1", MINECHORXINT=500, DETECTMULTI=4, ONEARMECHO=TRUE;
      ADD AUTOSCALINGSRROUTE: SERVICENAME="ServName_ispvpn1_2009_v6", VRFNAME="ispvpn1", IPVERSION=IPv6, PREFIX6="FC00::79:1", MASKLENGTH=128, NEXTHOPALLOCTYPE6=CONFIG, NEXTHOP6="FC00::89C1", BFDENABLE=TRUE, DESCRIPTION="ispvpn1", BFDTEMPLATENAME="BFD_2009_v6"; 
      ADD AUTOSCALINGSRROUTE: SERVICENAME="ServName_ispvpn1_2009_v6", VRFNAME="ispvpn1", IPVERSION=IPv6, PREFIX6="FC00::79:2", MASKLENGTH=128, NEXTHOPALLOCTYPE6=CONFIG, NEXTHOP6="FC00::89C1", BFDENABLE=TRUE, DESCRIPTION="ispvpn1", BFDTEMPLATENAME="BFD_2009_v6";
      ```
7. 采用OSPF动态路由时，配置外联口IP及路由。此处以APN绑定的VPN实例是ispvpn1为例，如其他APN还绑定其他VPN（如\_public\_），请参考本步骤进行配置。

   上下行的配置区别是：上下行使用的子接口不同，VLAN不同，外联口IP地址不同，OSPF进程ID不同，VPN相同，OSPF Area ID相同，OSPF的loopback 接口IP相同，且上行不需要引入wlr路由。如图4所示。

   **图4** 外联口IP&路由（OSPF动态路由）

   1. 配置下行报文使用的外联口IP及路由。UDG用于接收重定向设备、PDN/DN Server发送的UE报文。该OSPF进程不接收任何路由。

      ```
      //Global:
      SET BFD: BFDENABLE=TRUE;

      //IPv4:
      ADD OSPF: PROCID=8, VRFNAME="ispvpn1", SCHEMAROUID="192.168.225.138", BFDALLINTFFLG=TRUE, BFDRXCFGFLAG=TRUE, BFDMINRXINTV=500, BFDTXCFGFLAG=TRUE, BFDMINTXINTV=500, SCHEMABFDDETMUL=4, LSAARRINTVFLAG=FALSE, LSAARRMAXINTV=1000, LSAARRSTARINTV=500, LSAARRHLDINTV=500, VPNINSCAPSIMFLG=TRUE, VIRTUALSYSFLAG=TRUE;
      ADD OSPFAREA: PROCID=8, AREAID="0.0.0.5", AREATYPE=NSSA, MAXCOSTFLAG=FALSE;
      ADD OSPFIMPORTROUTE:PROCID=8,TOPOID=0,PROTOCOL=wlr,IMPTCOSTCFG=FALSE,IMPTTAGCFG=FALSE,IMPTTYPECFG=FALSE;

      //IPv6:
      ADD OSPFV3: PROCID=8, ROUTERID="192.168.225.138", VRFNAME="ispvpn1", BFDALLINTFFLG=TRUE, BFDRXCFGFLAG=TRUE, BFDMINRXINTV=500, BFDTXCFGFLAG=TRUE, BFDMINTXINTV=500, DETECTMULINTV=4, VPNINSCAPSIMFLG=TRUE, VIRTUALSYSFLAG=TRUE;
      ADD OSPFV3AREA: PROCID=8, AREAID="0.0.0.5", AREATYPE=NSSA, NSSADEFAULTROUTEADVERTISE=FALSE;
      ADD OSPFV3IMPORTROUTE: PROCID=8,TOPOID=0,PROTOCOL=wlr,IMPTCOSTCFG=FALSE,IMPTTAGCFG=FALSE,IMPTTYPECFG=FALSE;


      //IPv4, IPv6, or IPv4v6:
      ADD ROUTEPOLICY: POLICYNAME="routepolicy_deny";
      ADD ROUTEPOLICYNODE: POLICYNAME="routepolicy_deny", NODESEQUENCE=50, MATCHMODE=deny;

      //IPv4:
      ADD PREFIXFILTERNODE: NAME="ip-prefix_test", NODESEQUENCE=50, MATCHMODE=deny, ADDRESS="0.0.0.0", MASKLENGTH=0, GREATEREQUAL=0, LESSEQUAL=32, MATCHNETWORK=FALSE;
      ADD MATCHDESTPREFIXFILTER: POLICYNAME="routepolicy_deny", NODESEQUENCE=50, PREFIXNAME="ip-prefix_test";
      ADD OSPFFILTERPOLICY: PROCID=8, FILTERTYPE=import, TYPE=ip_prefix, IPPREFIX="ip-prefix_test";

      //IPv4:
      ADD INTERFACE:IFNAME="LoopBack8";
      ADD IPBINDVPN:IFNAME="LoopBack8",VRFNAME="ispvpn1";
      ADD IFIPV4ADDRESS:IFNAME="LoopBack8",IFIPADDR="192.168.225.138",SUBNETMASK="255.255.255.255",ADDRTYPE=main;
      ADD OSPFINTERFACE: PROCID=8, AREAID="0.0.0.5", IFNAME="LoopBack8";

      //IPv6:
      ADD IPV6PREFIXFILTERNODE: NAME="ip-prefix_test_v6", NODESEQUENCE=50, MATCHMODE=deny, ADDRESS="0:0:0:0:0:0:0:0", MASKLENGTH=0, MATCHNETWORK=FALSE, GREATEREQUAL=0, LESSEQUAL=128;
      ADD MATCHDESTPREFIX6FILTER: POLICYNAME="routepolicy_deny", NODESEQUENCE=50, IPV6PREFIXNAME="ip-prefix_test_v6";
      ADD OSPFV3FILTERPOLICY: PROCID=8, FILTERTYPE=import, TYPE=ip_prefix, IPPREFIX="ip-prefix_test_v6";


      //IPv4, IPv6, or IPv4v6:
      ADD AUTOSCALINGETHTRUNK: ETHTRUNKTMPID=6, VNICLIST="6 7";

      //IPv4:
      ADD AUTOSCALINGSERVICE: SERVICENAME="ServName_ispvpn1_2008", VPNNAME="ispvpn1", AFTYPE=IPv4, IPALLOCTYPE4=USER_CONFIG, AUTOCFGIFTYPE=ETHTRUNK, ETHTRUNKTMPID=6, VLANID=2008, BEGINADDR4="192.168.88.2", ENDADDR4="192.168.88.30", MASKLEN=27, OSPFENABLE=TRUE, OSPFPROCID=8, OSPFAREAID="0.0.0.5", TPINENABLE=FALSE, TPOUTENABLE=FALSE; 

      //IPv6:
      ADD AUTOSCALINGSERVICE: SERVICENAME="ServName_ispvpn1_2008_v6", VPNNAME="ispvpn1", AFTYPE=IPv6, IPALLOCTYPE6=USER_CONFIG, AUTOCFGIFTYPE=ETHTRUNK, ETHTRUNKTMPID=6, VLANID=2008, BEGINADDR6="FC00::88C2", ENDADDR6="FC00::88DE", MASKLEN=123, OSPFENABLE=TRUE, OSPFPROCID=8, OSPFAREAID="0.0.0.5", TPINENABLE=FALSE, TPOUTENABLE=FALSE;
      ```
   2. 配置上行报文使用的外联口IP及路由。UDG用于发送上行报文到重定向设备、PDN/DN Server。该OSPF进程不发布wlr路由。

      ```
      //IPv4:
      ADD OSPF: PROCID=9, VRFNAME="ispvpn1", SCHEMAROUID="192.168.225.138", BFDALLINTFFLG=TRUE, BFDRXCFGFLAG=TRUE, BFDMINRXINTV=500, BFDTXCFGFLAG=TRUE, BFDMINTXINTV=500, SCHEMABFDDETMUL=4, LSAARRINTVFLAG=FALSE, LSAARRMAXINTV=1000, LSAARRSTARINTV=500, LSAARRHLDINTV=500, VPNINSCAPSIMFLG=TRUE, VIRTUALSYSFLAG=TRUE;
      ADD OSPFAREA: PROCID=9, AREAID="0.0.0.5", AREATYPE=NSSA, MAXCOSTFLAG=FALSE;

      //IPv4
      ADD OSPFFILTERPOLICY: PROCID=9, FILTERTYPE=export, TYPE=ip_prefix, IPPREFIX="ip-prefix_test", PROTOCOL=wlr;

      //IPv4:
      ADD AUTOSCALINGSERVICE: SERVICENAME="ServName_ispvpn1_2009", VPNNAME="ispvpn1", AFTYPE=IPv4, IPALLOCTYPE4=USER_CONFIG, AUTOCFGIFTYPE=ETHTRUNK, ETHTRUNKTMPID=6, VLANID=2009, BEGINADDR4="192.168.89.2", ENDADDR4="192.168.89.30", MASKLEN=27, OSPFENABLE=TRUE, OSPFPROCID=9, OSPFAREAID="0.0.0.5", TPINENABLE=FALSE, TPOUTENABLE=FALSE; 

      //IPv6:
      ADD OSPFV3: PROCID=9, ROUTERID="192.168.225.138", VRFNAME="ispvpn1", BFDALLINTFFLG=TRUE, BFDRXCFGFLAG=TRUE, BFDMINRXINTV=500, BFDTXCFGFLAG=TRUE, BFDMINTXINTV=500, DETECTMULINTV=4, VPNINSCAPSIMFLG=TRUE, VIRTUALSYSFLAG=TRUE;
      ADD OSPFV3AREA: PROCID=9, AREAID="0.0.0.5", AREATYPE=NSSA, NSSADEFAULTROUTEADVERTISE=FALSE;

      //IPv6:
      ADD OSPFV3FILTERPOLICY: PROCID=9, FILTERTYPE=export, TYPE=ip_prefix, IPPREFIX="ip-prefix_test_v6", PROTOCOL=wlr;

      //IPv6:
      ADD AUTOSCALINGSERVICE: SERVICENAME="ServName_ispvpn1_2009_v6", VPNNAME="ispvpn1", AFTYPE=IPv6, IPALLOCTYPE6=USER_CONFIG, AUTOCFGIFTYPE=ETHTRUNK, ETHTRUNKTMPID=6, VLANID=2009, BEGINADDR6="FC00::89C2", ENDADDR6="FC00::89DE", MASKLEN=123, OSPFENABLE=TRUE, OSPFPROCID=9, OSPFAREAID="0.0.0.5", TPINENABLE=FALSE, TPOUTENABLE=FALSE;
      ```
8. 打开自动部署开关。

   ```
   SET AUTOCONFIG: SWITCHFLAG=TRUE;
   ```

   从自动部署开关打开到自动部署功能生效有时延，因此执行其他操作前（例如手动部署路由互通、关闭自动部署开关），务必先执行**DSP OPSASSISTSTATE**命令查询自动部署维护助手“autoscaling\_autoconfig.py”的状态为“准备好状态（Ready）”，否则结果不可预期。

版权所有 © 华为技术有限公司
