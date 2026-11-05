# 增加BGP对等体组BFD检测（ADD BGPPEERGROUPBFD）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

该命令为对等体组添加BFD检测。

#### 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为65535。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识        | 参数名称         | 参数说明                                                                                                                                                                         |
|:------------|:-------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| VRFNAME     | VPN实例名称      | 可选必选说明：可选参数 参数含义：该参数用于指定用户的BGP VPN实例。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～31。 默认值：_public_ 配置原则：使用LST L3VPNINST命令查看可用VPN。                                                          |
| GROUPNAME   | 组名           | 可选必选说明：必选参数 参数含义：该参数用于指定用户所配置的对等体组。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～47。 默认值：无 配置原则：使用LST BGPPEERGROUP命令查看可用对等体组名。                                                              |
| AFTYPE      | 组地址族类型       | 可选必选说明：必选参数 参数含义：该参数用于指定BGP VPN实例下的地址族。 数据来源：本端规划 取值范围：枚举类型。 public：公网地址族。ipv4uni：IPv4地址族。ipv6uni：IPv6地址族。noaf：不指定地址族。 默认值：无 配置原则：公网group配置public，私网则配置noaf、ipv4uni、ipv6uni。 |
| MULTIPLIER  | 检测时间倍数       | 可选必选说明：可选参数 参数含义：该参数用于指定BFD会话的检测时间倍数。 数据来源：本端规划 取值范围：整数类型，取值范围为3～50。 默认值：3                                                                                                   |
| ISBFDENABLE | BFD是否使能      | 可选必选说明：可选参数 参数含义：该参数用于指定是否使能BFD检测。 数据来源：本端规划 取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。 默认值：FALSE 配置原则：ISBFDENABLE为TRUE时才可配置ISSINGLEHOP为TRUE；ISBFDENABLE为FALSE时，会同时改变ISSINGLEHOP为FALSE。 |
| RXINTERVAL  | 最小接收间隔时间（ms） | 可选必选说明：可选参数 参数含义：该参数用于指定该BFD的最小接收时间间隔。 数据来源：本端规划 取值范围：整数类型，取值范围为30～1000，单位是毫秒。 默认值：无 配置原则：如果不输入该参数，则实际生效值为200ms。                                                             |
| TXINTERVAL  | 最小发送间隔时间（ms） | 可选必选说明：可选参数 参数含义：该参数用于指定该BFD的最小发送时间间隔。 数据来源：本端规划 取值范围：整数类型，取值范围为30～1000，单位是毫秒。 默认值：无 配置原则：如果不输入该参数，则实际生效值为200ms。                                                             |
| ISSINGLEHOP | 使能单跳模式       | 可选必选说明：可选参数 参数含义：该参数用于指定是否设置BFD为单跳模式。 数据来源：本端规划 取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。 默认值：FALSE 配置原则： ISBFDENABLE为TRUE时ISSINGLEHOP才可配置为TRUE。此参数不支持EBGP邻居。                          |

#### 使用实例

为对等体组添加BFD检测：

```
SET BGP:ASNUM="100",BGPENABLE=TRUE;
ADD L3VPNINST:VRFNAME="vrf1";
ADD VPNINSTAF:VRFNAME="vrf1",AFTYPE=ipv4uni;
ADD BGPVRF:VRFNAME="vrf1";
ADD BGPPEERGROUP:VRFNAME="vrf1",GROUPNAME="asdf",AFTYPE=ipv4uni;
ADD BGPPEERGROUPBFD:VRFNAME="vrf1",AFTYPE=ipv4uni,GROUPNAME="asdf",ISBFDENABLE=TRUE;
```