# 增加路由过滤策略（ADD FILTERPOLICY）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

该命令用于添加IPv4或IPv6路由过滤策略。

#### 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为65536。
- EXPORT和IMPORT都是必选参数，但不能相同。
- IMPORT为TRUE时，FILTERPROTOCOL只能为noprotocol。
- FILTERPROTOCOL为noprotocol、direct或static时，FILTERPROCESSID只能为0。
- FILTERPROTOCOL为ospf或ospfv3时，FILTERPROCESSID不能为0。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识            | 参数名称       | 参数说明                                                                                                                                                                                                                                                                                                                                       |
|:----------------|:-----------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| VRFNAME         | VPN实例名称    | 可选必选说明：可选参数 参数含义：该参数用于指定VPN实例名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～31。 默认值：_public_ 配置原则：使用LST L3VPNINST命令查看可用VPN。                                                                                                                                                                                                                             |
| AFTYPE          | 地址族类型      | 可选必选说明：必选参数 参数含义：该参数用于指定VRF的地址族类型。 数据来源：本端规划 取值范围：枚举类型。 ipv4uni：IPv4地址族。ipv4vpn：VPNv4地址族。ipv6uni：IPv6地址族。ipv6vpn：VPNv6地址族。 默认值：无                                                                                                                                                                                                           |
| EXPORT          | 出口方向       | 可选必选说明：条件必选参数 前提条件：该参数在“AFTYPE”配置为“ipv4uni”、“ipv4vpn”、“ipv6uni” 或 “ipv6vpn”时为必选参数。 参数含义：该参数用于指定该过滤策略是否应用在出口方向。 数据来源：本端规划 取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。 默认值：无 配置原则：EXPORT和IMPORT不能相同。                                                                                                                                                     |
| IMPORT          | 入口方向       | 可选必选说明：条件必选参数 前提条件：该参数在“AFTYPE”配置为“ipv4uni”、“ipv4vpn”、“ipv6uni” 或 “ipv6vpn”时为必选参数。 参数含义：该参数用于该过滤策略是否应用在入口方向。 数据来源：本端规划 取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。 默认值：无 配置原则：EXPORT和IMPORT不能相同。                                                                                                                                                       |
| FILTERPROTOCOL  | 路由协议       | 可选必选说明：条件必选参数 前提条件：该参数在“AFTYPE”配置为“ipv4uni”、“ipv4vpn”、“ipv6uni” 或 “ipv6vpn”时为必选参数。 参数含义：该参数用于指定发布路由信息的协议，对其进行过滤。 数据来源：本端规划 取值范围：枚举类型。 noprotocol：默认应用所有协议。direct：直连路由。ospf：OSPF路由。static：静态路由。ospfv3：OSPFv3路由。 默认值：无 配置原则：如果AFTYPE为VPNv4或VPNv6，或IMPORT为TRUE，该参数只能选择noprotocol。如果AFTYPE为IPv4uni，该参数不能选择ospfv3。如果AFTYPE为IPv6uni，该参数不能选择ospf。 |
| FILTERPROCESSID | 协议进程ID     | 可选必选说明：条件必选参数 前提条件：该参数在“AFTYPE”配置为“ipv4uni”、“ipv4vpn”、“ipv6uni” 或 “ipv6vpn”时为必选参数。 参数含义：该参数用于指定单播路由协议的进程号。 数据来源：本端规划 取值范围：整数类型，取值范围为0～4294967295。 默认值：无 配置原则：当单播路由协议为ospf或者ospfv3时，FILTERPROCESSID不能为0，当协议为noprotocol、direct、static，FILTERPROCESSID只能为0。                                                                                   |
| ACLNAMEORNUM    | ACL规则标识    | 可选必选说明：条件可选参数 前提条件：该参数在“AFTYPE”配置为“ipv4uni” 或 “ipv4vpn”时为可选参数。 参数含义：该参数用于指定IPv4访问控制列表ACL的名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～32。只支持ACL number取值范围为2000-2999的基本ACL策略。 默认值：无 配置原则：ACLNAMEORNUM和PREFLT4NAME命令行下发时，这两个参数选择其一。被引用的ACL策略中只会生效ACL number为2000-2999的基本ACL策略。                                                                         |
| PREFLT4NAME     | IPv4前缀过滤策略 | 可选必选说明：条件可选参数 前提条件：该参数在“AFTYPE”配置为“ipv4uni” 或 “ipv4vpn”时为可选参数。 参数含义：该参数用于指定IPv4前缀过滤策略名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～169。 默认值：无 配置原则：ACLNAMEORNUM和PREFLT4NAME命令行下发时，这两个参数选择其一。                                                                                                                                                           |
| ACL6NAMEORNUM   | ACL6规则标识   | 可选必选说明：条件可选参数 前提条件：该参数在“AFTYPE”配置为“ipv6uni” 或 “ipv6vpn”时为可选参数。 参数含义：该参数用于指定IPv6访问控制列表ACL的名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～32。只支持ACL number取值范围为2000-2999的基本ACL策略。 默认值：无 配置原则：ACL6NAMEORNUM和PREFLT6NAME两个参数必选其一。被引用的ACL策略中只会生效ACL number为2000-2999的基本ACL策略。                                                                                |
| PREFLT6NAME     | IPv6前缀过滤策略 | 可选必选说明：条件可选参数 前提条件：该参数在“AFTYPE”配置为“ipv6uni” 或 “ipv6vpn”时为可选参数。 参数含义：该参数用于指定IPv6前缀过滤策略名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～169。 默认值：无 配置原则：ACL6NAMEORNUM和PREFLT6NAME两个参数必选其一。                                                                                                                                                                  |

#### 使用实例

- 为VPN实例"vrf1"添加IPv4单播地址族的过滤策略，并指明方向及过滤策略等参数：

  ```
  ADD L3VPNINST: VRFNAME="vrf1";
  ADD VPNINSTAF:VRFNAME="vrf1", AFTYPE=ipv4uni;
  SET BGP:ASNUM="100", BGPENABLE=TRUE;
  ADD BGPVRF:VRFNAME="vrf1";
  ADD PREFIXFILTERNODE:NAME="asssd",NODESEQUENCE=1,MATCHMODE=permit,ADDRESS="10.1.1.1", MASKLENGTH=32;
  ADD FILTERPOLICY:VRFNAME="vrf1",AFTYPE=ipv4uni,EXPORT=FALSE,IMPORT=TRUE,FILTERPROTOCOL=noprotocol,FILTERPROCESSID=0,PREFLT4NAME="asssd";
  ```
- 为VPN实例"vrf1"添加IPv6单播地址族的过滤策略，并指明方向及过滤策略等参数：

  ```
  SET BGP:ASNUM="100",BGPENABLE=TRUE;
  ADD L3VPNINST: VRFNAME="vrf1";
  ADD VPNINSTAF:VRFNAME="vrf1", AFTYPE=ipv6uni;
  ADD BGPVRF:VRFNAME="vrf1",DEFAULTAFTYPE=ipv6uni;
  ADD IPV6PREFIXFILTERNODE:NAME="asssd",NODESEQUENCE=1,MATCHMODE=permit,ADDRESS="2001:db8:1:1:1:1:1:1", MASKLENGTH=32;
  ADD FILTERPOLICY:VRFNAME="vrf1",AFTYPE=ipv6uni,EXPORT=FALSE,IMPORT=TRUE,FILTERPROTOCOL=noprotocol,FILTERPROCESSID=0,PREFLT6NAME="asssd";
  ```