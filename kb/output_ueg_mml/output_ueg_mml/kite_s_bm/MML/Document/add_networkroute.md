# 增加引入路由指定前缀和掩码长度（ADD NETWORKROUTE）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

该命令用于通过Network方式引入BGP外部路由信息。

BGP协议自身不能发现路由，所以需要引入其他协议的路由（如IGP或者静态路由等）注入到BGP路由表中，从而将这些路由在AS之内和AS之间传播。

BGP引入路由时支持Import和Network两种方式：

Import方式是按协议类型，将OSPF路由、静态路由和直连路由等某一协议的路由注入到BGP路由表中。

Network方式比Import方式更精确，将指定前缀和掩码的一条路由注入到BGP路由表中。

#### 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为65536。
- 需要确保指定的BGP VPN实例在设备上已创建。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识             | 参数名称       | 参数说明                                                                                                                                                                                              |
|:-----------------|:-----------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| VRFNAME          | VPN实例名称    | 可选必选说明：可选参数 参数含义：该参数用于指定用户增加引入network路由的BGP VPN实例名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～31。 默认值：_public_ 配置原则：使用LST L3VPNINST命令查看可用VPN。                                                                |
| AFTYPE           | 地址族类型      | 可选必选说明：必选参数 参数含义：该参数用于指定BGP VPN实例下的地址族。 数据来源：本端规划 取值范围：枚举类型。 ipv4uni：IPv4地址族。ipv6uni：IPv6地址族。 默认值：无                                                                                               |
| NETWORKADDRESS   | IPv4路由前缀地址 | 可选必选说明：条件必选参数 前提条件：该参数在“AFTYPE”配置为“ipv4uni”时为必选参数。 参数含义：该参数用于指定引入IPv4路由的前缀信息。 数据来源：全网规划 取值范围：IPv4地址类型。 默认值：无 配置原则：配置该参数时，需要同时配置MASKLEN指定路由的掩码长度。                                                  |
| MASKLEN          | IPv4掩码长度   | 可选必选说明：条件必选参数 前提条件：该参数在“AFTYPE”配置为“ipv4uni”时为必选参数。 参数含义：该参数用于指定引入外部IPv4路由的掩码长度。 数据来源：本端规划 取值范围：整数类型，取值范围为0～32。 默认值：无 配置原则：配置NETWORKADDRESS参数时，需要配置本参数指定引入路由的掩码长度。                                 |
| NETWORKADDRESSV6 | IPv6路由前缀地址 | 可选必选说明：条件必选参数 前提条件：该参数在“AFTYPE”配置为“ipv6uni”时为必选参数。 参数含义：该参数用于指定引入IPv6路由的前缀信息。 数据来源：全网规划 取值范围：IPv6地址类型。 默认值：无 配置原则：配置该参数时，需要同时配置MASKLENV6指定路由的前缀长度。                                                |
| MASKLENV6        | IPv6掩码长度   | 可选必选说明：条件必选参数 前提条件：该参数在“AFTYPE”配置为“ipv6uni”时为必选参数。 参数含义：该参数用于指定引入外部IPv6路由的前缀长度。 数据来源：本端规划 取值范围：整数类型，取值范围为0～128。 默认值：无 配置原则：配置NETWORKADDRESSV6参数时，需要配置本参数指定引入路由的前缀长度。                              |
| NETWORKPOLICY    | 策略名称       | 可选必选说明：条件可选参数 前提条件：该参数在“AFTYPE”配置为“ipv4uni” 或 “ipv6uni”时为可选参数。 参数含义：用户设定引入其他协议路由时的策略名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～200。 默认值：无 配置原则：在此之前应使用ADD ROUTEPOLICY命令配置对应策略。使用LST ROUTEPOLICY命令查看可用路由策略。 |

#### 使用实例

- 在名称为“vrf1”的BGP VPN实例下引入为192.168.2.0/24的外部路由：

  ```
  SET BGP:ASNUM="100",BGPENABLE=TRUE;
  ADD L3VPNINST:VRFNAME="vrf1";
  ADD VPNINSTAF:VRFNAME="vrf1",AFTYPE=ipv4uni;
  ADD BGPVRF:VRFNAME="vrf1";
  ADD NETWORKROUTE:VRFNAME="vrf1",AFTYPE=ipv4uni,NETWORKADDRESS="192.168.2.0",MASKLEN=24;
  ```
- 在名称为“vrf1”的BGP VPN实例下引入为2001:db8:1:1:1:1:1:1/32的外部路由：

  ```
  SET BGP:ASNUM="100",BGPENABLE=TRUE;
  ADD L3VPNINST:VRFNAME="vrf1";
  ADD VPNINSTAF:VRFNAME="vrf1",AFTYPE=ipv6uni;
  ADD BGPVRF:VRFNAME="vrf1",DEFAULTAFTYPE=ipv6uni;
  ADD NETWORKROUTE:VRFNAME="vrf1",AFTYPE=ipv6uni,NETWORKADDRESSV6="2001:db8:1:1:1:1:1:1",MASKLENV6=32;
  ```