# 增加BGP对等体BFD检测（ADD BGPPEERBFD）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

该命令用于增加IPv4或IPv6对等体BFD的相关参数。

#### 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为65535。
- 至少输入一个参数。
- 对于设备建立了Overlay BGP邻居，并且使能了BFD for BGP（Underlay通过OSPF路由、静态路由等负载分担）的场景。BFD检测状态机随机选择到一个RU，此RU故障后会造成BFD会话Down，即使其他RU不存在故障，也会触发BGP会话Down。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识        | 参数名称          | 参数说明                                                                                                                                                                                                                                                                                                       |
|:------------|:--------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| VRFNAME     | VPN实例名称       | 可选必选说明：可选参数 参数含义：该参数用于指定VPN实例名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～31。 默认值：_public_ 配置原则：使用LST L3VPNINST命令查看可用VPN。                                                                                                                                                                                             |
| ADDRESSTYPE | 地址类型          | 可选必选说明：可选参数 参数含义：该参数用于指定对等体的地址类型。 数据来源：本端规划 取值范围：枚举类型。 ipv4：IPv4。ipv6：IPv6。 默认值：ipv4                                                                                                                                                                                                                       |
| PEERADDR    | IPv4对等体地址     | 可选必选说明：条件必选参数 前提条件：该参数在“ADDRESSTYPE”配置为“ipv4”时为必选参数。 参数含义：该参数用于指定连接对等体的IPv4接口地址。 数据来源：对端协商 取值范围：IPv4地址类型。 默认值：无 配置原则：使用LST BGPPEER命令查看可用对等体。                                                                                                                                                               |
| PEERADDRV6  | IPv6对等体地址     | 可选必选说明：条件必选参数 前提条件：该参数在“ADDRESSTYPE”配置为“ipv6”时为必选参数。 参数含义：该参数用于指定连接对等体的IPv6接口地址。 数据来源：对端协商 取值范围：IPv6地址类型。 默认值：无 配置原则：使用LST BGPPEER命令查看可用对等体。                                                                                                                                                               |
| ISBFDBLOCK  | 使能BFD Block功能 | 可选必选说明：条件可选参数 前提条件：该参数在“ADDRESSTYPE”配置为“ipv4” 或 “ipv6”时为可选参数。 参数含义：该参数用于指定是否阻止对等体从对等体组中继承BFD功能。 数据来源：本端规划 取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。 默认值：FALSE 配置原则：ISBFDBLOCK和ISBFDENABLE互斥，不能同时配置。                                                                                                                  |
| MULTIPLIER  | 检测时间倍数        | 可选必选说明：条件可选参数 前提条件：该参数在“ADDRESSTYPE”配置为“ipv4” 或 “ipv6”时为可选参数。 参数含义：该参数用于指定BFD会话的检测时间倍数。 数据来源：本端规划 取值范围：整数类型，取值范围为3～50。 默认值：3                                                                                                                                                                               |
| ISBFDENABLE | 使能BFD         | 可选必选说明：条件可选参数 前提条件：该参数在“ADDRESSTYPE”配置为“ipv4” 或 “ipv6”时为可选参数。 参数含义：该参数用于指定是否使能BFD检测。 数据来源：本端规划 取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。 默认值：FALSE                                                                                                                                                                   |
| RXINTERVAL  | 最小接收间隔时间（ms）  | 可选必选说明：条件可选参数 前提条件：该参数在“ADDRESSTYPE”配置为“ipv4” 或 “ipv6”时为可选参数。 参数含义：该参数用于指定该BFD的期望接收时间间隔。 数据来源：本端规划 取值范围：整数类型，取值范围为30～1000，单位是毫秒。 默认值：无 配置原则：如果不输入该参数，则实际生效值为200ms。                                                                                                                                         |
| TXINTERVAL  | 最小发送间隔时间（ms）  | 可选必选说明：条件可选参数 前提条件：该参数在“ADDRESSTYPE”配置为“ipv4” 或 “ipv6”时为可选参数。 参数含义：该参数用于指定该BFD的期望发送时间间隔。 数据来源：本端规划 取值范围：整数类型，取值范围为30～1000，单位是毫秒。 默认值：无 配置原则：如果不输入该参数，则实际生效值为200ms。                                                                                                                                         |
| ISSINGLEHOP | 使能单跳模式        | 可选必选说明：条件可选参数 前提条件：该参数在“ADDRESSTYPE”配置为“ipv4” 或 “ipv6”时为可选参数。 参数含义：single-hop-prefer参数用来在IBGP对等体之间创建BFD会话时优先使用单跳检测，用于对等体之间的IP连通性检测，即对于IBGP的指定接口上只存在一个BFD会话。此参数用于和其他厂商设备连接时，保证本端和对端采用相同的检测方式。 数据来源：本端规划 取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。 默认值：FALSE 配置原则： ISBFDENABLE为TRUE时ISSINGLEHOP才可配置为TRUE。此参数不支持EBGP邻居。 |

#### 使用实例

- 在名称为“vrf1”的BGP VPN实例下为10.2.2.2对等体添加BFD检测：

  ```
  SET BGP:ASNUM="100",BGPENABLE=TRUE;
  ADD L3VPNINST:VRFNAME="vrf1";
  ADD VPNINSTAF:VRFNAME="vrf1", AFTYPE=ipv4uni;
  ADD BGPVRF:VRFNAME="vrf1";
  ADD BGPPEER:VRFNAME="vrf1",PEERADDR="10.2.2.2",REMOTEAS="100";
  ADD BGPPEERBFD:VRFNAME="vrf1",PEERADDR="10.2.2.2",ISBFDENABLE=TRUE;
  ```
- 在名称为“vrf1”的BGP VPN实例下为2001:db8:1:1:1:1:1:1对等体添加BFD检测：

  ```
  SET BGP:ASNUM="100",BGPENABLE=TRUE;
  ADD L3VPNINST:VRFNAME="vrf1";
  ADD VPNINSTAF:VRFNAME="vrf1", AFTYPE=ipv6uni;
  ADD BGPVRF:VRFNAME="vrf1",DEFAULTAFTYPE=ipv6uni;
  ADD BGPPEER:VRFNAME="vrf1",ADDRESSTYPE=ipv6,PEERADDRV6="2001:db8:1:1:1:1:1:1",REMOTEAS="100";
  ADD BGPPEERBFD:VRFNAME="vrf1",ADDRESSTYPE=ipv6,PEERADDRV6="2001:db8:1:1:1:1:1:1",ISBFDENABLE=TRUE;
  ```