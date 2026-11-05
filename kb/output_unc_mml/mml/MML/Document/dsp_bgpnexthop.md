# 查询BGP下一跳信息（DSP BGPNEXTHOP）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用来查看BGP指定地址族中的下一跳迭代信息。

#### 注意事项

该命令执行后立即生效。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识    | 参数名称     | 参数说明                                                                                                    |
|:--------|:---------|:--------------------------------------------------------------------------------------------------------|
| AFTYPE  | BGP地址族类型 | 可选必选说明：必选参数 参数含义：BGP地址族类型。 数据来源：本端规划 取值范围：枚举类型。 ipv4uni：IPv4地址族。ipv6uni：IPv6地址族。 默认值：无                  |
| VRFNAME | VPN实例名称  | 可选必选说明：可选参数 参数含义：VPN实例名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～31。 默认值：_public_ 配置原则：使用LST L3VPNINST命令查看可用VPN。 |

#### 使用实例

查询BGP下一跳信息：

```
DSP BGPNEXTHOP:AFTYPE=ipv4uni;
```

```
RETCODE = 0  操作成功。

结果如下
------------------------
BGP下一跳信息 =

Import Base Count: 1

Original Nexthop     : 10.2.2.2
Original Type        : 4
UserData : 00000000000000000000
Tunnel Policy Name : nil
Relay Type : Route Relay
IID : 771751943
Route Relay Info
Relay Ip Last Change Time : 2016-07-01 10:43:58
Relay Status : Route Reachable
Relay IID : 771751943
Relay Cost : 0
Relay Number : 1
Relay Depth : 0
Restrain Count : 0
Restrain Time Left : 0s
First Relay Info
Relay Nexthop : 10.2.2.2
Relay Label   : NULL
Relay Out Interface : NULL0
Relay RouteSource : 0.0.0.0
IpRelay Flap Count : 0
TnlRelay Flap Count : 0

(结果个数 = 1)
---    END
```

#### 输出结果说明

| 输出项名称    | 输出项解释         |
|:---------|:--------------|
| BGP下一跳信息 | 用于指定BGP下一跳信息。 |