# 配置BGP over OSPF/静态路由+BFD（IPv4）

- 操作场景
- 必备事项
- 操作步骤
- 验证方法

## 操作场景

BGP（Border Gateway Protocol）边界网关协议是一种用于AS(Autonomous System)之间的动态路由协议，与OSPF、静态路由等内部网关协议（IGP）不同，其自身不能发现和计算路由，主要用于在自治系统AS间控制路由的传播和选择最佳路由。

当拓扑结构复杂且无法规划在同一自治区域内时，可以采用BGP over OSPF/静态路由+BFD实现VNF与对端设备的网络层互通。

**说明** 

- BGP协议自身没有自动部署功能，本文主要是在OSPF、静态路由等内部网关协议的自动部署基础上，通过BGP协议将其引入并传播。
- 采用DC-GW作网关时，采用BGP over静态路由+BFD；采用PE作网关时，采用BGP over静态路由+BFD（推荐）或BGP over OSPF+BFD。
- VNF所在硬件设备与DC-GW直连且采用双活网关时，支持BGP over 静态路由+BFD单臂echo，不支持OSPF动态路由协议。
- VNF所在硬件设备与DC-GW直连且采用M-LAG时，支持BGP over 静态路由+BFD单臂echo，不支持OSPF动态路由协议。

如图1所示为VNF与周边网元的BGP over OSPF/静态路由+BFD互通组网示意图。VNF与网关运行BGP over OSPF/静态路由+BFD路由协议而接入运营商网络（IP骨干网），网关可以使用DC-GW、EOR（End of Row）交换机或运营商的PE（Provider Edge）交换机。无论哪种方式，VNF的配置相同，没有差异。PE的路由配置请参考运营商的网络规划配置，DC-GW/EOR的配置请参考对应型号设备的产品文档。

**图1** BGP over OSPF/静态路由+BFD组网

## 必备事项

前提条件

- 请阅读并熟悉特性IPFD-014002 支持BGP特性概述。
- 已完成配置动态路由OSPF+BFD组网（IPv4）或配置静态路由+BFD组网（IPv4）。

- 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020/MAE客户端或登录OM Portal）。

- VNF与网络实体之间的网络环境已经构建完成。

数据

VNF使用BGP over OSPF/静态路由+BFD与对端设备建立可靠的IP连接。

本文以一组外联口子接口为例进行说明，一组外联口（对应一个逻辑接口）分别在每个CSLB各规划2个子接口负荷分担承载流量，后续扩容CSLB后自动在每个CSLB上扩展2个子接口承载流量。实际场景可根据网设规划进行适配。

**说明** 

**如下数据仅为举例，请注意修改成局点规划的数据。**

| 类别                | 参数名称                        | 取值样例            | 获取方法                                                                                                       | 说明                                                                                                        |
|:------------------|:----------------------------|:----------------|:-----------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------|
| ADD INTERFACE     | 接口名（IFNAME）                 | Loopback1       | 参见“5G Core LLD文档 > 路由设计 > BGP设计 > Local interface name（VNF）”。                                              | -                                                                                                         |
| ADD IPBINDVPN     | VPN实例名称（VRFNAME）            | VPN_Access      | 参见“5G Core LLD文档 > 路由设计 > BGP设计 > VRF名称（VNF）”。                                                             | 此处的VPN实例已经配置，与OSPF、静态路由等IGP协议的外联口绑定的VPN实例相同。                                                              |
| ADD IFIPV4ADDRESS | 接口IPv4地址（IFIPADDR）          | 10.90.7.160     | 参见“5G Core LLD文档 > 路由设计 > BGP设计 > Local interface address（VNF）”。                                           | 如果规划Loopback接口使用IPv4v6双栈地址，则分别执行ADD IFIPV4ADDRESS和ADD IFIPV6ADDRESS 对同一Loopback接口配置IPv4和IPv6地址。           |
| ADD IFIPV4ADDRESS | 接口IPv4地址掩码（SUBNETMASK）      | 255.255.255.255 | 固定取值                                                                                                       | 如果规划Loopback接口使用IPv4v6双栈地址，则分别执行ADD IFIPV4ADDRESS和ADD IFIPV6ADDRESS 对同一Loopback接口配置IPv4和IPv6地址。           |
| SET BGP           | 使能BGP（BGPENABLE）            | TRUE            | 固定取值                                                                                                       | -                                                                                                         |
| SET BGP           | BGP自治域号（ASNUM）              | 60001           | 参见“5G Core LLD文档 > 路由设计 > BGP设计 > AS号（VNF）”。                                                               | -                                                                                                         |
| ADD BGPVRF        | VPN实例名称（VRFNAME）            | VPN_Access      | 参见“5G Core LLD文档 > 路由设计 > BGP设计 > VRF名称（VNF）”。                                                             | BGP VPN实例需要与Loopback接口绑定的VPN实例名一致。                                                                        |
| ADD BGPVRF        | 默认地址族（DEFAULTAFTYPE）        | noaf            | 固定取值                                                                                                       | -                                                                                                         |
| ADD BGPVRF        | 路由器标识（ROUTERID）             | 10.90.7.160     | 参见“5G Core LLD文档 > 路由设计 > BGP设计 > Router ID（VNF）”。                                                         | 不同BGP VPN实例的ROUTERID不能重复。                                                                                 |
| ADD BGPVRFAF      | VPN实例名称（VRFNAME）            | VPN_Access      | 已配置数据中获取                                                                                                   | 使用ADD BGPVRF命令定义的VPN实例名称。                                                                                 |
| ADD BGPVRFAF      | 地址族类型（AFTYPE）               | ipv4uni         | 固定取值                                                                                                       | -                                                                                                         |
| ADD BGPVRFAF      | 最大等价路由数（MAXIMUMLOADBALANCE） | 2               | 参见“5G Core LLD文档 > 路由设计 > BGP设计 > LoadBalance是否使能（VNF）”。 “LoadBalance是否使能”为“Y”时，该参数取值与对接的负荷分担的BGP PEER数一致。 | 对接的负荷分担关系的BGP peer数。                                                                                      |
| ADD BGPPEER       | 地址类型（ADDRESSTYPE）           | ipv4            | -                                                                                                          | “PEERADDR”是网关上用于和VNF建立BGP邻居关系的IP地址。                                                                       |
| ADD BGPPEER       | IPv4对等体地址（PEERADDR）         | 10.9.7.135      | 参见“5G Core LLD文档 > 路由设计 > BGP设计 > Local interface address（L3GW）”。                                          | “PEERADDR”是网关上用于和VNF建立BGP邻居关系的IP地址。                                                                       |
| ADD BGPPEER       | 对等体AS号（REMOTEAS）            | 60002           | 参见“5G Core LLD文档 > 路由设计 > BGP设计 > AS号（L3GW）”。                                                              | “PEERADDR”是网关上用于和VNF建立BGP邻居关系的IP地址。                                                                       |
| ADD BGPPEER       | 本地接口地址（LOCALIFADDR）         | 10.90.7.160     | 参见“5G Core LLD文档 > 路由设计 > BGP设计 > Local interface address（VNF）”。                                           | “PEERADDR”是网关上用于和VNF建立BGP邻居关系的IP地址。                                                                       |
| ADD BGPPEER       | 本地接口名称（LOCALIFNAME）         | Loopback1       | 参见“5G Core LLD文档 > 路由设计 > BGP设计 > Local interface name（VNF）”。                                              | “PEERADDR”是网关上用于和VNF建立BGP邻居关系的IP地址。                                                                       |
| ADD BGPPEER       | EBGP最大跳数（EBGPMAXHOP）        | 10              | 本端规划                                                                                                       | 不小于到Peer之间的实际跳数，无法确认时，可设置为10。 如最大跳数设置过小，会导致BGP邻居建立失败。                                                     |
| ADD IMPORTROUTE   | 地址族类型（AFTYPE）               | ipv4uni         | -                                                                                                          | IPv4组网场景下，该参数选择ipv4uni。 该参数全局取值要一致。                                                                       |
| ADD IMPORTROUTE   | 路由协议（IMPORTPROTOCOL）        | wlr             | 参见“5G Core LLD文档 > 路由设计 > BGP设计 > Import Route类型（VNF）”。                                                    | -                                                                                                         |
| ADD IMPORTROUTE   | 使能MED（MEDENABLE）            | FALSE           | 本端规划                                                                                                       | 对于N6口，两个UPF上的UE地址段存在重叠且需要对外发布网段路由时（该场景下，两个UPF是主备容灾），该参数设置为“TRUE”；否则，该参数设置为“FALSE”。 对于其他接口，使用默认值“FALSE”即可。 |
| ADD IMPORTROUTE   | MED（MED）                    | 0               | 本端规划                                                                                                       | “MEDENABLE”设置为“TRUE”时，需要规划该参数。 主备UPF引入路由的MED值。主UPF设置的MED值必须小于备UPF设置的MED值。                                 |

U面下沉新建场景，采用高密度框式服务器+标卡+UPF分配IP地址+BGP over静态路由时，需要规划表2中的数据。仅N6/SGi接口需要规划，其他接口不需要规划。

| 类别                     | 参数名称                          | 取值样例                | 获取方法     | 说明                                                                                                                                                                        |
|:-----------------------|:------------------------------|:--------------------|:---------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SET DATAPLANEGIINFMODE | 模式（MODE）                      | RU                  | 固定取值     | 开启下行入不转板功能后，地址池分段，并与ISU pod绑定。                                                                                                                                            |
| SET DATAPLANEGIINFMODE | 路由增强功能开关（ROUTEENHANCEDSW）     | ENABLE              | 本端规划     | 路由增强功能：通过VNF和DC-GW配合，减少DC-GW对承载网发布的用户下行路由的条数。 该参数值变更（DISABLE->ENABLE、ENABLE->DISABLE）前，需将用户下线。该参数值设置为ENABLE且ADD AUTOSCALINGBGPLF命令中的“发布的团体属性（UDADVCOM）”参数不为0时，路由增强功能才会生效。 |
| MOD BGPPEERAF          | VPN实例名称（VRFNAME）              | VPN_Access          | 已配置数据中获取 | 采用ADD BGPPEER命令配置的参数值，可通过LST BGPPEER命令获取。                                                                                                                                 |
| MOD BGPPEERAF          | 地址族类型（AFTYPE）                 | ipv4uni             | 已配置数据中获取 | 采用ADD BGPPEER命令配置的参数值，可通过LST BGPPEER命令获取。                                                                                                                                 |
| MOD BGPPEERAF          | IPv4对等体地址（REMOTEADDRESS）      | 10.9.7.135          | 已配置数据中获取 | 采用ADD BGPPEER命令配置的参数值，可通过LST BGPPEER命令获取。                                                                                                                                 |
| MOD BGPPEERAF          | 团体属性发布（ADVERTISECOMMUNITY）    | TRUE                | 本端规划     | 开启路由增强功能时，该参数需要设置为“TRUE”。其他场景下，该参数采用默认值即可。                                                                                                                                |
| ADD AUTOSCALINGBGPLF   | 策略名称（POLICYNAME）              | bgppolicy1          | 本端规划     | 不同BGPPEER时，该参数必须不同。同一BGPPEER时，该参数必须相同。BGP PEER上不需要配置该参数值。                                                                                                                 |
| ADD AUTOSCALINGBGPLF   | IP版本（IPVERSION）               | IPV4                | 全网规划     | 此处以IPv4为例。                                                                                                                                                                |
| ADD AUTOSCALINGBGPLF   | 服务名称（SERVICENAME）             | ServName_Access_100 | 已配置数据中获取 | 采用ADD AUTOSCALINGSERVICE命令定义的服务名称。                                                                                                                                        |
| ADD AUTOSCALINGBGPLF   | IP对等体地址（PEERIP）               | 10.9.7.135          | 从对端获取    | BGP PEER的IP地址。                                                                                                                                                            |
| ADD AUTOSCALINGBGPLF   | 对端团体属性（PEERCOMMUNITY）         | 1                   | 本端规划     | 不同BGPPEER时，该参数必须不同。同一BGPPEER时，该参数必须相同。BGP PEER上不需要配置该参数值。                                                                                                                 |
| ADD AUTOSCALINGBGPLF   | 使能发布团体属性开关（UDADVCOMENABLE）    | TRUE                | 本端规划     | VNF上部署路由增强功能后，DC-GW根据携带的团体属性值（此处配置的“发布的团体属性”值）进行路由过滤。建议先在DC-GW上配置，然后再在VNF上配置。                                                                                             |
| ADD AUTOSCALINGBGPLF   | 发布的团体属性（UDADVCOM）             | 200                 | 与对端协商    | VNF上部署路由增强功能后，DC-GW根据携带的团体属性值（此处配置的“发布的团体属性”值）进行路由过滤。建议先在DC-GW上配置，然后再在VNF上配置。                                                                                             |
| ADD AUTOSCALINGIPREACH | 服务名称（SERVICENAME）             | ServName_Access_100 | 已配置数据中获取 | 采用ADD AUTOSCALINGSERVICE命令定义的服务名称。                                                                                                                                        |
| ADD AUTOSCALINGIPREACH | IP版本（IPVERSION）               | IPV4                | 全网规划     | 此处以IPv4为例。                                                                                                                                                                |
| ADD AUTOSCALINGIPREACH | 目的地址（DESTADDR4）               | 10.9.7.135          | 从对端获取    | BGP PEER的IP地址。                                                                                                                                                            |
| ADD AUTOSCALINGIPREACH | BFD自动化配置模板名称（BFDTEMPLATENAME） | BFD_1               | 已配置数据中获取 | 本命令绑定的BFD模板，复用ADD AUTOSCALINGSRROUTE命令绑定BFD模板。 若ADD AUTOSCALINGSRROUTE命令没有绑定BFD模板，则需通过ADD AUTOSCALINGBFD命令新增BFD模板配置。                                                      |

中心云场景，若服务器+第三方底层平台场景下业务单板转发性能低（交换带宽不足），需要规划表3中的数据。N3/N9/S1-U/S5/S8/N6/SGi接口需要规划，其他接口不需要规划。

入不转板会增加组网复杂度，在交换带宽足够时，不建议开启入不转板功能。

| 类别                     | 参数名称                          | 取值样例                | 获取方法     | 说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|:-----------------------|:------------------------------|:--------------------|:---------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SET DATAPLANEINFMODE   | 模式（MODE）                      | Instance            | 固定取值     | 开启入不转板时，必须使用样例值。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| SET DATAPLANEINFMODE   | 路由增强功能开关（ROUTEENHANCEDSW）     | ENABLE              | 本端规划     | 路由增强功能：通过VNF和DC-GW配合，减少DC-GW对承载网发布的用户下行路由的条数。 该参数值变更（DISABLE->ENABLE、ENABLE->DISABLE）前，需将用户下线。该参数值设置为ENABLE且ADD AUTOSCALINGBGPLF命令中的“发布的团体属性（UDADVCOM）”参数不为0时，路由增强功能才会生效。                                                                                                                                                                                                                                                                                                                                   |
| MOD AUTOSCALINGSERVICE | 服务名称（SERVICENAME）             | ServName_Access_100 | 已配置数据中获取 | 采用ADD AUTOSCALINGSERVICE命令定义的服务名称。                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| MOD AUTOSCALINGSERVICE | 备用路由组标识（ISBACKUP）             | TRUE                | 与对端协商    | “ISBACKUP”设置为“TRUE”时，表示在保护组上生效；“ISBACKUP”设置为“FALSE”时，表示在非保护组上生效。 DC-GW只与保护组内ISU之间建立BFD会话，备路由也只到保护组内ISU的ECMP路由。请根据DC-GW能力规划保护组中ISU POD最大个数，建议将所有ISU都规划到保护组中。 执行OPR DSPPRTGRPSPEC命令可查询保护组中ISU POD的最大个数。 当“保护组规格值”取值是“65535”时，“环境变量保护组规格值”参数值就是保护组中ISU POD的最大个数。 当“保护组规格值”取值不是“65535”时，“保护组规格值”参数值就是保护组中ISU POD的最大个数。 执行DSP POD命令可查询系统中的ISU POD的个数。 当系统中的所有ISU POD都在保护组中时，仅需要规划“ISBACKUP”值为“TRUE”的接口自动化配置模板。 当系统中的ISU POD个数大于保护组中ISU POD的个数时，需要同时规划“ISBACKUP”值为“TRUE”的接口自动化配置模板和“ISBACKUP”值为“FALSE”的接口自动化配置模板。 |
| MOD BGPPEERAF          | VPN实例名称（VRFNAME）              | VPN_Access          | 已配置数据中获取 | 采用ADD BGPPEER命令配置的参数值，可通过LST BGPPEER命令获取。                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| MOD BGPPEERAF          | 地址族类型（AFTYPE）                 | ipv4uni             | 已配置数据中获取 | 采用ADD BGPPEER命令配置的参数值，可通过LST BGPPEER命令获取。                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| MOD BGPPEERAF          | IPv4对等体地址（REMOTEADDRESS）      | 10.9.7.135          | 已配置数据中获取 | 采用ADD BGPPEER命令配置的参数值，可通过LST BGPPEER命令获取。                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| MOD BGPPEERAF          | 团体属性发布（ADVERTISECOMMUNITY）    | TRUE                | 本端规划     | 开启路由增强功能时，该参数需要设置为“TRUE”。其他场景下，该参数采用默认值即可。                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ADD AUTOSCALINGBGPLF   | 策略名称（POLICYNAME）              | bgppolicy1          | 本端规划     | 不同BGPPEER时，该参数必须不同。同一BGPPEER时，该参数必须相同。BGP PEER上不需要配置该参数值。                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ADD AUTOSCALINGBGPLF   | IP版本（IPVERSION）               | IPV4                | 全网规划     | 此处以IPv4为例。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ADD AUTOSCALINGBGPLF   | 服务名称（SERVICENAME）             | ServName_Access_100 | 已配置数据中获取 | 采用ADD AUTOSCALINGSERVICE命令定义的服务名称。                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ADD AUTOSCALINGBGPLF   | IP对等体地址（PEERIP）               | 10.9.7.135          | 从对端获取    | BGP PEER的IP地址。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ADD AUTOSCALINGBGPLF   | 对端团体属性（PEERCOMMUNITY）         | 1                   | 本端规划     | 不同BGPPEER时，该参数必须不同。同一BGPPEER时，该参数必须相同。BGP PEER上不需要配置该参数值。                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ADD AUTOSCALINGBGPLF   | 使能发布团体属性开关（UDADVCOMENABLE）    | TRUE                | 本端规划     | VNF上部署路由增强功能后，DC-GW根据携带的团体属性值（此处配置的“发布的团体属性”值）进行路由过滤。建议先在DC-GW上配置，然后再在VNF上配置。                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ADD AUTOSCALINGBGPLF   | 发布的团体属性（UDADVCOM）             | 200                 | 与对端协商    | VNF上部署路由增强功能后，DC-GW根据携带的团体属性值（此处配置的“发布的团体属性”值）进行路由过滤。建议先在DC-GW上配置，然后再在VNF上配置。                                                                                                                                                                                                                                                                                                                                                                                                                               |
| ADD AUTOSCALINGIPREACH | 服务名称（SERVICENAME）             | ServName_Access_100 | 已配置数据中获取 | 采用ADD AUTOSCALINGSERVICE命令定义的服务名称。                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ADD AUTOSCALINGIPREACH | IP版本（IPVERSION）               | IPV4                | 全网规划     | 此处以IPv4为例。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| ADD AUTOSCALINGIPREACH | 目的地址（DESTADDR4）               | 10.9.7.135          | 从对端获取    | BGP PEER的IP地址。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ADD AUTOSCALINGIPREACH | BFD自动化配置模板名称（BFDTEMPLATENAME） | BFD_1               | 已配置数据中获取 | 本命令绑定的BFD模板，复用ADD AUTOSCALINGSRROUTE命令绑定BFD模板。 若ADD AUTOSCALINGSRROUTE命令没有绑定BFD模板，则需通过ADD AUTOSCALINGBFD命令新增BFD模板配置。                                                                                                                                                                                                                                                                                                                                                                                        |

文档

获取网设LLD文档。

## 操作步骤

1. 配置OSPF+BFD、静态路由+BFD。

   由于BGP协议自身不能发现路由，所以需要引入其他协议的路由（如OSPF或者静态路由等）注入到BGP路由表中，从而将这些路由在AS之内和AS之间传播。

   - 配置动态路由OSPF+BFD组网（IPv4）
   - 配置静态路由+BFD组网（IPv4）

   **说明** 

   - BFD会话绑定的是路由，不是BGPPEER。如存在**ADD BGPPEERBFD**配置，请删除。
   - 静态路由用于实现VNF 的Loopback接口地址与BGP PEER IP（DC-GW）之间的互通。配置静态路由时，需满足如下配置点：
     - 外联口的IP地址，是通过将“IPALLOCTYPE4”设置为“USER-CONFIG”的方式在VNF上配置。
     - VNF所在硬件设备与DC-GW直连且采用双活网关时，支持BGP over 静态路由+BFD单臂echo，不支持OSPF动态路由协议。
     - VNF所在硬件设备与DC-GW直连且采用M-LAG时，支持BGP over 静态路由+BFD单臂echo，不支持OSPF动态路由协议。
   - 本步骤配置的是静态路由时，需要配置如下两类路由：
     - IP路由1：目的IP是BGP对等体地址，下一跳是网关的接口IP地址，且该路由需要绑定BFD会话。
     - IP路由2：目的IP是0.0.0.0，掩码长度是0，其他参数取值与“IP路由1”中的参数值相同。对端不发布默认路由时需要配置。
2. 配置Loopback接口地址。
   1. 配置Loopback接口。

      ```
      ADD INTERFACE:IFNAME="Loopback1";
      ```
   2. 配置接口绑定VPN。

      ```
      ADD IPBINDVPN:IFNAME="Loopback1",VRFNAME="VPN_Access";
      ```
   3. 配置接口IP地址。

      ```
      ADD IFIPV4ADDRESS:IFNAME="Loopback1",IFIPADDR="10.90.7.160",SUBNETMASK="255.255.255.255";
      ```
3. 全局激活BGP。

   ```
   SET BGP: BGPENABLE=TRUE, ASNUM="60001";
   ```
4. 配置BGP。
   1. 增加BGP VPN实例。

      ```
      ADD BGPVRF: VRFNAME="VPN_Access", DEFAULTAFTYPE=noaf, ROUTERID="10.90.7.160";
      ```

      **说明** 

      - 此处配置的“ROUTERID”是BGP VPN实例级别的ROUTERID。

        IPv4v6双栈时，IPv4 BGP VPN实例地址族和IPv6 BGP VPN实例地址族共用此处配置的“ROUTERID”值。
      - 已配置IPv4v6双栈的BGP VPN实例地址族，若需删除IPv4的BGP VPN实例地址族配置，则：

        1、删除IPv4的配置前需查询并记录“ROUTERID”值。

        2、删除IPv4的配置后需查询“ROUTERID”值是否存在，若不存在则需通过**MOD BGPVRF**命令将“ROUTERID”参数设置为删除IPv4的配置前记录的“ROUTERID”值。否则IPv6 BGP重新协商时会因无“ROUTERID”值可用而导致协商失败。
   2. 增加BGP VPN实例地址族。UDG对接2个负荷分担的BGP PEER时，“MAXIMUMLOADBALANCE”设置为“2”。

      ```
      ADD BGPVRFAF: VRFNAME="VPN_Access", AFTYPE=ipv4uni, MAXIMUMLOADBALANCE=2;
      ```
   3. 增加BGP对等体。

      ```
      ADD BGPPEER: VRFNAME="VPN_Access", ADDRESSTYPE=ipv4, PEERADDR="10.9.7.135", REMOTEAS="60002", LOCALIFADDR="10.90.7.160", LOCALIFNAME="Loopback1", EBGPMAXHOP=10;
      ```
   4. 增加BGP引入路由。

      ```
      ADD IMPORTROUTE: VRFNAME="VPN_Access", AFTYPE=ipv4uni, IMPORTPROTOCOL=wlr, MEDENABLE=FALSE;
      ```

      **说明** 

      - 由于BGP协议自身不能发现路由，所以需要引入其他协议的路由（如OSPF、静态路由或WLR等）注入到BGP路由表中，从而将这些路由在AS之内和AS之间传播。
      - 对于N6口，两个UPF上的UE地址段存在重叠且需要对外发布网段路由时，需要将“MEDENABLE”设置为“TRUE”，并设置备UPF的“MED”值大于主UPF的“MED”值。
5. U面下沉新建场景，采用高密度框式服务器+标卡+UPF分配IP地址+BGP over静态路由时，配置下行入不转板功能。其他场景不需要配置。

   **注意** 

   - 仅N6/SGi接口需要配置，其他接口不需要配置。
   - 步骤 5.c和步骤 5.d须在自动化配置开关关闭状态下执行，否则执行失败。相关操作请参见配置静态路由+BFD组网（IPv4）中的步骤 3。
   - 步骤 5.c和步骤 5.d配置完成后，须开启自动化配置开关（“SWITCHFLAG”设置为“TRUE”），否则配置不生效。相关操作请参见配置静态路由+BFD组网（IPv4）中的步骤 9。
   - 开启下行入不转板的命令是**SET DATAPLANEGIINFMODE**，不是**SET DATAPLANEINFMODE**。

     若误使用**SET DATAPLANEINFMODE**，则会上报ALM-81210 ISU或APU不可用告警。

   1. 开启下行入不转板开关。此处以开启路由增强功能为例。

      ```
      SET DATAPLANEGIINFMODE: MODE=RU, ROUTEENHANCEDSW=ENABLE;
      ```
   2. 开启路由增强功能时，修改BGP对等体地址族。

      开启路由增强功能时，必须将“ADVERTISECOMMUNITY”设置为“TRUE”。其他参数值此处仅为举例，请通过**LST BGPPEER**获取。

      ```
      MOD BGPPEERAF: VRFNAME="VPN_Access", AFTYPE=ipv4uni, REMOTEADDRESS="10.9.7.135", ADVERTISECOMMUNITY=TRUE;
      ```
   3. 增加入不转板策略自动化配置模板。

      ```
      ADD AUTOSCALINGBGPLF: POLICYNAME="bgppolicy1", IPVERSION=IPv4, SERVICENAME="ServName_Access_100", PEERIP="10.9.7.135", PEERCOMMUNITY=1, UDADVCOMENABLE=TRUE, UDADVCOM="200";
      ```
   4. 增加IP可达性检测自动化配置模板。

      ```
      ADD AUTOSCALINGIPREACH: SERVICENAME="ServName_Access_100", IPVERSION=IPv4, DESTADDR4="10.9.7.135", BFDTEMPLATENAME="BFD_1";
      ```
6. 中心云新建场景，第三方底层平台场景下业务单板转发性能低+采用ISU POD+标卡+UPF分配IP地址+BGP over静态路由时，配置入不转板功能。其他场景不需要配置。

   **注意** 

   - 仅如下逻辑接口对应的外联口需要配置，其他接口不需要配置。
     - s1-uif（S1-U）、n3if（N3）、saif（S1-U和N3）。
     - s5-sif（S5/S8-S）、n9cif（N9c）、scif（S5/S8-S和N9c）。
     - paif（N9a/S5-P/S8-P/S2b/Gn-U/Gp-U）。
   - 步骤 6.b~步骤 6.e须在自动化配置开关关闭状态下执行，否则执行失败。相关操作请参见配置静态路由+BFD组网（IPv4）中的步骤 3。
   - 步骤 6.b~步骤 6.e配置完成后，须开启自动化配置开关（“SWITCHFLAG”设置为“TRUE”），否则配置不生效。相关操作请参见配置静态路由+BFD组网（IPv4）中的步骤 9。
   - 开启入不转板的命令是**SET DATAPLANEINFMODE**，不是**SET DATAPLANEGIINFMODE**。

     如误使用**SET DATAPLANEGIINFMODE**，则下行业务入不转板，上行业务入转板。

   1. 开启入不转板开关。此处以开启路由增强功能为例。

      ```
      SET DATAPLANEINFMODE: MODE=Instance, ROUTEENHANCEDSW=ENABLE;
      ```
   2. 将接口模板设置为在保护组上生效。

      //“ISBACKUP”设置为“TRUE”时，表示在保护组上生效；“ISBACKUP”设置为“FALSE”时，表示在非保护组上生效。

      ```
      MOD AUTOSCALINGSERVICE: SERVICENAME="ServName_Access_100", ISBACKUP=TRUE;
      ```
   3. 开启路由增强功能时，修改BGP对等体地址族。

      开启路由增强功能时，必须将“ADVERTISECOMMUNITY”设置为“TRUE”。其他参数值此处仅为举例，请通过**LST BGPPEER**获取。

      ```
      MOD BGPPEERAF: VRFNAME="VPN_Access", AFTYPE=ipv4uni, REMOTEADDRESS="10.9.7.135", ADVERTISECOMMUNITY=TRUE;
      ```
   4. 增加入不转板策略自动化配置模板。

      ```
      ADD AUTOSCALINGBGPLF: POLICYNAME="bgppolicy1", IPVERSION=IPv4, SERVICENAME="ServName_Access_100", PEERIP="10.9.7.135", PEERCOMMUNITY=1, UDADVCOMENABLE=TRUE, UDADVCOM="200";
      ```
   5. 增加IP可达性检测自动化配置模板。

      ```
      ADD AUTOSCALINGIPREACH: SERVICENAME="ServName_Access_100", IPVERSION=IPv4, DESTADDR4="10.9.7.135", BFDTEMPLATENAME="BFD_1";
      ```

## 验证方法

1. 执行**LST INTERFACE**/**LST IFIPV4ADDRESS**/**LST IFIPV6ADDRESS**/**LST IPBINDVPN**命令，查看接口状态及信息是否与规划数据一致。

   - 如果一致，请执行2。
   - 如果不一致，请参考“操作步骤”修改配置后，执行2。
2. 执行**PING**命令，查看VNF与BGP PEER间的路由连接是否正常。

   ```
   PING:IPVERSION=IPv4,VPNNAME="VPN_Access",DESTIPV4ADDRESS="BGP PEER IPv4地址";
   ```

   ```
   PING:IPVERSION=IPv6,VPNNAME="VPN_Access",DESTIPV6ADDRESS="BGP PEER IPv6地址";
   ```

   **说明** 

   - 如果使用了VPN组网，还需使用“VPN实例名称（VPNNAME）”指定VPN实例，这样才能验证VPN实例路由是否正常。
   - 需要在VNF上分别PING BGP PEER IP，出接口是VNF上负荷分担关系的每个子接口，且能PING通。

   - 丢包率为0%，请执行3。
   - 如果连续出现timeout，请参考验证方法，调测到BGP PEER的静态路由数据。
3. 执行**PING**命令，在DC-GW上检查DC-GW与VNF Loopback接口IP之间是否路由可达。
   - 是，请执行4。
   - 否，请联系华为技术支持工程师处理（例如检查DC-GW上是否存在到VNF BGP IP的路由，下一跳分别是VNF的负荷分担关系的每个外联口的IP），然后执行4。
4. 执行**LST BGPPEER**命令，查看BGP对等体配置是否与规划数据一致。
   - 如果一致，请执行5。
   - 如果不一致，请参考“操作步骤”修改配置后，重新执行2。
5. 执行**DSP BGPPEERINFO**命令，检查BGP对等体条数是否正确及BGP对等体状态是否为Established。

   本步骤的显示结果中的BGP对等体的条数与LST BGPPEER中查询的对等体的条数相等，且“对等体状态”为“Established”。

   - 是且未开启入不转板功能，调测结束。
   - 是且开启了入不转板功能，请执行6。
   - 否，请执行8。
6. 开启入不转板功能时，查看BGP入不转板自动部署模板配置是否与规划数据一致。
   - 一致，请执行7。
   - 不一致，请参考如下子步骤修改BGP入不转板自动部署模板。

   **说明** 

   BGP入不转板自动部署模板的“策略名称”参数取值以“bgppolicy1”为例，实际请执行**LST AUTOSCALINGBGPLF**命令获取。

   1. 关闭自动化配置开关。

      ```
      SET AUTOCONFIG: SWITCHFLAG=FALSE;
      ```
   2. 删除指定的路由策略节点。
      1. 查询并记录路由策略节点信息。

         ```
         LST ROUTEPOLICYNODE: POLICYNAME="bgppolicy1";
         ```

         ```
         %%LST ROUTEPOLICYNODE: POLICYNAME="bgppolicy1";%%
         RETCODE = 0  Operation succeeded

         The result is as follows:
         -------------------------
         Route-Policy Name  Route-Policy Node ID  Matching Mode  Route-Policy Node Description  

         bgppolicy1         64                    Permit         NULL                           
         bgppolicy1         65                    Permit         NULL                           
         bgppolicy1         6405                  Permit         NULL                           
         bgppolicy1         6410                  Permit         NULL                           
         bgppolicy1         6505                  Permit         NULL                           
         bgppolicy1         6510                  Permit         NULL                           
         bgppolicy1         65535                 Permit         NULL                           
         (Number of results = 7)

         ---    END
         ```
      2. 删除指定的路由策略节点。“路由策略节点号”是“65535”的无法删除，请忽略。

         ```
         RMV ROUTEPOLICYNODE: POLICYNAME="bgppolicy1", NODESEQUENCE=64;
         RMV ROUTEPOLICYNODE: POLICYNAME="bgppolicy1", NODESEQUENCE=65;
         RMV ROUTEPOLICYNODE: POLICYNAME="bgppolicy1", NODESEQUENCE=6405;
         RMV ROUTEPOLICYNODE: POLICYNAME="bgppolicy1", NODESEQUENCE=6410;
         RMV ROUTEPOLICYNODE: POLICYNAME="bgppolicy1", NODESEQUENCE=6505;
         RMV ROUTEPOLICYNODE: POLICYNAME="bgppolicy1", NODESEQUENCE=6510;
         ```
   3. 删除指定的团体属性过滤器。
      1. 查询并记录团体属性过滤器。

         ```
         LST COMMUNITYFILTER:;
         ```

         ```
         %%LST COMMUNITYFILTER:;%%
         RETCODE = 0  Operation succeeded

         The result is as follows:
         -------------------------
                   Community Filter Type  =  Basic
         Community Filter Name or Number  =  comm-filter-bgppolicy1
         (Number of results = 1)

         ---    END
         ```
      2. 删除指定的团体属性过滤器。

         ```
         RMV COMMUNITYFILTER: CMNTYNAMEORNUM="comm-filter-bgppolicy1";
         ```
   4. 删除指定的应用团体属性。
      1. 查询应用团体属性。

         ```
         LST APPLYCOMMUNITY:;
         ```

         ```
         %%LST APPLYCOMMUNITY:;%%
         RETCODE = 0  Operation succeeded

         The result is as follows:
         -------------------------
            Route-Policy Name  =  bgppolicy1
         Route-Policy Node ID  =  65535
               Operation Type  =  Delete
         (Number of results = 1)

         ---    END
         ```
      2. 删除指定的应用团体属性。

         ```
         RMV APPLYCOMMUNITY: POLICYNAME="bgppolicy1", NODESEQUENCE=65535;
         ```
   5. 修改BGP对等体地址族，删除“EXPORTRTPOLICYNAME”参数值。
      1. 查询并记录BGP对等体地址族。此处显示信息以IPv4为例。

         ```
         LST BGPPEERAF:;
         ```

         ```
         %%LST BGPPEERAF:;%%
         RETCODE = 0  Operation succeeded

         The result is as follows:
         -------------------------
                                         VPN Name  =  VPN_Access
                          VRF Address Family Type  =  IPv4uni
                                       IP Version  =  IPv4
                                IPv4 Peer Address  =  10.9.7.135
                                IPv6 Peer Address  =  ::
                                                  ...
                         Export Route Policy Name  =  bgppolicy1
                                                  ...
         (Number of results = 1)

         ---    END
         ```
      2. 修改BGP对等体地址族，删除“EXPORTRTPOLICYNAME”参数值。

         ```
         MOD BGPPEERAF: VRFNAME="VPN_Access", AFTYPE=ipv4uni, REMOTEADDRESS="10.9.7.135", EXPORTRTPOLICYNAME=" ";
         ```

         ```
         MOD BGPPEERAF: VRFNAME="VPN_Access", AFTYPE=ipv6uni, ADDRESSTYPE=ipv6, REMOTEADDRESSV6="FC00:2013::2", EXPORTRTPOLICYNAME=" ";
         ```
   6. 删除指定的路由策略。
      1. 查询并记录路由策略。

         ```
         LST ROUTEPOLICY:;
         ```

         ```
         %%LST ROUTEPOLICY:;%%
         RETCODE = 0  Operation succeeded

         The result is as follows:
         -------------------------
         Route-Policy Name  =  bgppolicy1
         (Number of results = 1)

         ---    END
         ```
      2. 删除指定的路由策略。

         ```
         RMV ROUTEPOLICY: POLICYNAME="bgppolicy1";
         ```
   7. 删除指定的BGP入不转板自动化配置模板
      1. 查询并记录BGP入不转板自动部署模板。此处显示信息以IPv4为例。

         ```
         LST AUTOSCALINGBGPLF:;
         ```

         ```
         %%LST AUTOSCALINGBGPLF:;%%
         RETCODE = 0  Operation succeeded

         The result is as follows
         ------------------------
                        Policy Name  =  bgppolicy1
                         IP Version  =  IPv4 Address Family
                       Service Name  =  ServName_Access_100
                    IP Peer Address  =  10.9.7.135
                     Peer Community  =  1
         Enable Advertise Community  =  TRUE
               Advertised Community  =  200
         (Number of results = 1)

         ---    END
         ```
      2. 删除指定的BGP入不转板自动化配置模板。

         ```
         RMV AUTOSCALINGBGPLF: POLICYNAME="bgppolicy1", SERVICENAME="ServName_Access_100";
         ```
   8. 重新配置外联口自动化配置模板。此处以“UDADVCOM”值修改为“100”为例。

      ```
      ADD AUTOSCALINGBGPLF: POLICYNAME="bgppolicy1", IPVERSION=IPv4, SERVICENAME="ServName_Access_100", PEERIP="10.9.7.135", PEERCOMMUNITY=1, UDADVCOMENABLE=TRUE, UDADVCOM="100";
      ```

      ```
      ADD AUTOSCALINGBGPLF: POLICYNAME="bgppolicy1", IPVERSION=IPv6, SERVICENAME="ServName_Access_100", PEERIPV6="fc00:0:0:0:10:9:7:135", PEERCOMMUNITY=1, UDADVCOMENABLE=TRUE, UDADVCOM="100";
      ```
   9. 打开自动化配置开关。

      ```
      SET AUTOCONFIG: SWITCHFLAG=TRUE;
      ```
7. 开启入不转板功能时，执行**DSP WLRTABLE**检查显示结果中“路由类型”为“WLR\_UD”时，“团体属性”值是否不为“NULL”。

   执行脚本如下，其中“VRFNAME”采用APN绑定的VPN实例名称。

   ```
   DSP WLRTABLE: AFTYPE=ipv4unicast, VRFNAME="VRF_Internet";
   ```

   ```
   DSP WLRTABLE: AFTYPE=ipv6unicast, VRFNAME="VRF_Internet";
   ```

   - 是，调测结束。
   - 否，请执行8。
8. 收集信息并寻求技术支持。

   1. 执行**EXP MML**命令将当前配置数据导出为MML脚本文件并保存。
   2. 收集并保存上述所有查询信息。
   3. 查看并收集对端设备配置及接口状态信息。
   4. 收集归纳所有信息并联系华为技术支持解决。