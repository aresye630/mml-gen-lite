# 设置报文上送优先级（SET SECPOLICYPRIO）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 参考信息

#### 命令功能

该命令用来配置报文上送优先级。

当上送CPU的报文队列满时，为保护CPU，可以设置报文上送CPU的优先级，优先上送高优先级的报文。

缺省情况下，上送报文的优先级各不相同，可以使用DSP SECCARINFO命令查看。

#### 注意事项

- 该命令执行后立即生效。
- 该命令的设定值可通过LST SECPOLICYPRIO命令进行查询。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识            | 参数名称       | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|:----------------|:-----------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SECPOLICYID     | 安全策略号      | 可选必选说明：必选参数 参数含义：安全策略号。 数据来源：本端规划 取值范围：整数类型，取值范围为1～30。 默认值：无 配置原则：需要先添加安全策略。                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| SECPOLICYTYPE   | 安全策略类型     | 可选必选说明：必选参数 参数含义：安全策略类型。 数据来源：本端规划 取值范围：枚举类型。 Tcpip：TCP/IP。WhiteList：白名单。BlackList：黑名单。Index：索引。UserFlow：用户自定义流。Protocol：协议。WhiteListV6：IPv6白名单。 默认值：无                                                                                                                                                                                                                                                                                                                                                                        |
| SECPOLICYTYPEID | 安全策略类型号    | 可选必选说明：条件必选参数 前提条件：该参数在“SECPOLICYTYPE”配置为“UserFlow” 或 “Index”时为必选参数。 参数含义：安全策略类型号。 数据来源：本端规划 取值范围：整数类型，取值范围为0～4294967295。 默认值：无 配置原则：如果SECPOLICYTYPE选择Index，需要根据DSP SECCARINFO查看安全CAR系统ID并在[35，1658]区间，[125，158]区间除外。如果SECPOLICYTYPE选择UserFlow，本参数在[1，32]之间。                                                                                                                                                                                                                                                                  |
| SECPRIORITY     | 安全优先级      | 可选必选说明：条件必选参数 前提条件：该参数在“SECPOLICYTYPE”配置为“Protocol”、“Tcpip”、“UserFlow”、“WhiteList”、“BlackList”、“WhiteListV6” 或 “Index”时为必选参数。 参数含义：安全优先级。 数据来源：本端规划 取值范围：枚举类型。 low：低。middle：中。high：高。 默认值：无                                                                                                                                                                                                                                                                                                                                   |
| SUBPROTOTYPE    | 安全协议类型     | 可选必选说明：条件必选参数 前提条件：该参数在“SECPOLICYTYPE”配置为“Protocol”时为必选参数。 参数含义：协议类型。 数据来源：本端规划 取值范围：枚举类型。 bfd：BFD协议。bgp：BGP协议。icmp：ICMP协议。ldp：LDP协议。ospf：OSPF协议。arp：ARP协议。arp-miss：ARP-MISS消息。gre：GRE协议。ssh_server：SSH服务器。ssh_client：SSH客户端。dhcp：DHCP协议。dhcpv6：DHCPv6协议。pim：PIM协议。igmp：IGMP协议。ipv4-reserved-mc：IPv4默认保留组播报文。ipv6-too-big：IPv6超大报文。ipv4-mc-fib-miss：IPv4组播转发表项MISS协议。bgpv6：BGPv6报文。icmpv6：ICMPv6协议。ospfv3：OSPFv3报文。na：NA报文。ns：NS报文。ra：RA报文。rs：RS报文。mld：MLD报文。ipv6-nd-miss：IPv6 ND-MISS消息。ipv6-ndh-miss：IPv6 NDH-MISS消息。 默认值：无 |
| SUBTCPIPTYPE    | 安全TCP/IP类型 | 可选必选说明：条件必选参数 前提条件：该参数在“SECPOLICYTYPE”配置为“Tcpip”时为必选参数。 参数含义：TCP/IP防攻击类型。 数据来源：本端规划 取值范围：枚举类型。 TCPSYN：TCPSYN报文。FRAGMENT：分片报文。 默认值：无                                                                                                                                                                                                                                                                                                                                                                                           |

#### 使用实例

配置报文上送优先级：

```
SET SECPOLICYPRIO: SECPOLICYID=1, SECPOLICYTYPE=Tcpip, SECPRIORITY=low, SUBTCPIPTYPE=TCPSYN;
```

#### 参考信息

需要先添加安全策略。