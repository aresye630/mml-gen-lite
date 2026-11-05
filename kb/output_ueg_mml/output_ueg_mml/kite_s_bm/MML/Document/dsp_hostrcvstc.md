# 查询接收方向协议报文统计计数（DSP HOSTRCVSTC）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于查询接收方向协议报文统计计数。

当查询类型为IF\_STC时，只显示统计计数非零的前十的接口统计信息，当不指定PROTTYPE查询时，查询结果不受开关控制。

当查询类型为PROT\_STC，不指定IFNAME参数时，查询所有接口的统计信息；当指定IFNAME参数时，可以查询指定接口的统计信息。

查询之前需先配置全局或者接口协议报文统计配置；当删除全局或者接口协议报文统计配置时对应的统计计数将被清零。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识      | 参数名称   | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|:----------|:-------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| QUERYTYPE | 查询类型   | 可选必选说明：必选参数 参数含义：该参数用于表示查询类型。 数据来源：本端规划 取值范围：枚举类型。 IF_STC：接口上指定协议类型的报文统计信息。PROT_STC：接口上各协议类型的报文统计信息。 默认值：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| IFNAME    | 接口名称   | 可选必选说明：条件可选参数 前提条件：该参数在“QUERYTYPE”配置为“PROT_STC”时为可选参数。 参数含义：该参数用于表示接口名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。接口名称由接口类型+接口编号组成。 默认值：无 配置原则：请使用LST INTERFACE命令查看可用接口。                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| PROTTYPE  | 协议类型   | 可选必选说明：条件可选参数 前提条件：该参数在“QUERYTYPE”配置为“IF_STC”时为可选参数。 参数含义：该参数用于表示协议类型。 数据来源：本端规划 取值范围：枚举类型。 ARP：ARP协议类型。STP：STP协议类型。LACP：LACP协议类型。LLDP：LLDP协议类型。ISIS：ISIS协议类型。LINK_OTHER：其它链路层协议类型。ICMP：ICMP协议类型。OSPF：OSPF协议类型。PIM：PIM协议类型。IGMP：IGMP协议类型。VRRP：VRRP协议类型。RAWIP_OTHER：其它RawIP协议类型。SNMP：SNMP协议类型。DHCP：DHCP协议类型。UDP_OTHER：其它UDP协议类型。BGP：BGP协议类型。LDP：LDP协议类型。TCP_OTHER：其它TCP协议类型。ICMPV6：ICMPv6协议类型。OSPFV3：OSPFv3协议类型。PIMV6：PIMv6协议类型。MLD：MLD协议类型。VRRPV6：VRRPv6协议类型。RAWIPV6_OTHER：其它RawIPv6协议类型。SNMPV6：SNMPv6协议类型。DHCPV6：DHCPv6协议类型。IPV6UDP_OTHER：其它IPv6 UDP协议类型。BGP4PLUS：BGP4PLUS协议类型。LDPV6：LDPv6协议类型。IPV6TCP_OTHER：其它IPv6 TCP协议类型。 默认值：无 |

#### 使用实例

- 查询接收方向接口上指定协议类型的协议报文统计计数：

  ```
  DSP HOSTRCVSTC: QUERYTYPE=IF_STC, PROTTYPE=ARP;
  ```

  ```
  RETCODE = 0  操作成功。

  结果如下
  --------
      接口名称  =  GigabitEthernet0/0/1
  接收报文总数  =  1416
  (结果个数 = 1)
  ---    END
  ```
- 查询接收方向协议报文统计计数：

  ```
  DSP HOSTRCVSTC: QUERYTYPE=PROT_STC;
  ```

  ```
  RETCODE = 0  操作成功。

  结果如下
  --------
  协议层次    协议类型            上送报文总数    接收方向丢弃报文总数

  LINK        ARP                 8100            0
  LINK        STP                 0               0
  LINK        LACP                0               0
  LINK        LLDP                0               0
  LINK        ISIS                0               0
  LINK        其它链路层协议      89              111
  RawIP       ICMP                0               0
  RawIP       OSPF                0               0
  RawIP       PIM                 0               0
  RawIP       IGMP                0               4
  RawIP       VRRP                0               0
  RawIP       其它RawIP协议       0               0
  IPv4 UDP    SNMP                0               0
  IPv4 UDP    DHCP                52              0
  IPv4 UDP    其它UDP协议         989             0
  IPv4 TCP    BGP                 0               0
  IPv4 TCP    LDP                 0               0
  IPv4 TCP    其它TCP协议         56              0
  RawIPv6     ICMPv6              0               0
  RawIPv6     OSPFv3              0               0
  RawIPv6     PIMv6               0               0
  RawIPv6     MLD                 0               15
  RawIPv6     VRRPv6              0               0
  RawIPv6     其它RawIPv6协议     0               0
  IPv6 UDP    SNMPv6              0               0
  IPv6 UDP    DHCPv6              0               0
  IPv6 UDP    其它IPv6 UDP协议    0               0
  IPv6 TCP    BGP4PLUS            0               0
  IPv6 TCP    LDPv6               0               0
  IPv6 TCP    其它IPv6 TCP协议    0               0
  (结果个数 = 30)
  ---    END
  ```
- 查询接收方向指定接口上的协议报文统计计数：

  ```
  DSP HOSTRCVSTC: QUERYTYPE=PROT_STC, IFNAME="GigabitEthernet0/0/1";
  ```

  ```
  RETCODE = 0  操作成功。

  结果如下
  --------
  协议层次    协议类型            上送报文总数    接收方向丢弃报文总数

  LINK        ARP                 3471            0
  LINK        STP                 0               0
  LINK        LACP                0               0
  LINK        LLDP                0               0
  LINK        ISIS                0               0
  LINK        其它链路层协议      0               53
  RawIP       ICMP                0               0
  RawIP       OSPF                0               0
  RawIP       PIM                 0               0
  RawIP       IGMP                0               0
  RawIP       VRRP                0               0
  RawIP       其它RawIP协议       0               0
  IPv4 UDP    SNMP                0               0
  IPv4 UDP    DHCP                0               0
  IPv4 UDP    其它UDP协议         0               0
  IPv4 TCP    BGP                 0               0
  IPv4 TCP    LDP                 0               0
  IPv4 TCP    其它TCP协议         0               0
  RawIPv6     ICMPv6              0               0
  RawIPv6     OSPFv3              0               0
  RawIPv6     PIMv6               0               0
  RawIPv6     MLD                 0               5
  RawIPv6     VRRPv6              0               0
  RawIPv6     其它RawIPv6协议     0               0
  IPv6 UDP    SNMPv6              0               0
  IPv6 UDP    DHCPv6              0               0
  IPv6 UDP    其它IPv6 UDP协议    0               0
  IPv6 TCP    BGP4PLUS            0               0
  IPv6 TCP    LDPv6               0               0
  IPv6 TCP    其它IPv6 TCP协议    0               0
  (结果个数 = 30)
  ---    END
  ```

#### 输出结果说明

| 输出项名称      | 输出项解释           |
|:-----------|:----------------|
| 接口名称       | 用于表示接口名称。       |
| 接收报文总数     | 用于表示接收报文总数。     |
| 协议层次       | 用于表示协议层次。       |
| 协议类型       | 用于表示协议类型。       |
| 上送报文总数     | 用于表示上送报文总数。     |
| 接收方向丢弃报文总数 | 用于表示接收方向丢弃报文总数。 |