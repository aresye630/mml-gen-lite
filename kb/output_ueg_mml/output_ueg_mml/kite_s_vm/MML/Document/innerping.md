# INNER IP Ping（INNERPING）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

PING是最常见的用于检测网络设备可访问性的调试工具，它使用ICMP报文来检测远程设备是否可用、远程主机通信的来回旅程的延迟以及包的丢失情况。

#### 注意事项

- 该命令执行后立即生效。

当前存在三类PING调测命令：

**PING**

、

**INNERPING**

、

**NGPING**

，差异如下。

- **PING**：该命令用于排查本网元**外联口IP**与对端设备之间是否可以PING通。

**INNERPING、NGPING**

：该命令用于排查本网元

**业务IP**

与对端设备之间是否可以PING通。INNERPING适用场景如下表所示，其他场景均使用NGPING。

| NF形态     | 接口                 | 业务IP配置方式         | “服务实例”参数取值    |
|:---------|:-------------------|:-----------------|:--------------|
| SGSN/MME | Ga、Gn-U、S11-U      | ADD SERVICEIP    | USN_VNFC_999  |
| SGSN/MME | Gb                 | ADD SERVICEIP    | GB_VNFC_999   |
| SGSN/MME | Sdup               | ADD SERVICEIPMCR | MCR_VNFC_999  |
| SGSN/MME | 其他：如Gn、Sv、S10、S11等 | ADD SERVICEIP    | LINK_VNFC_999 |
| AMF      | N2                 | ADD SERVICEIP    | LINK_VNFC_999 |
| AMF      | DNS接口              | ADD SERVICEIP    | LINK_VNFC_999 |
| SMSF     | MAP接口              | ADD SERVICEIP    | LINK_VNFC_999 |
| CHF      | Ga（内部）Server       | ADD IPRESOURCE   | CG_VNFC_999   |
| CHF      | BI                 | ADD IPRESOURCE   | CG_VNFC_999   |
| NRF      | DCI接口（NRF双活容灾接口）   | ADD DRCOMM       | -             |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识              | 参数名称        | 参数说明                                                                                                                                                         |
|:------------------|:------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IPVERSION         | IP协议版本号     | 可选必选说明：必选参数 参数含义：该参数用于指定发送ECHO-REQUEST报文的IP协议版本。 数据来源：本端规划 取值范围：枚举类型。 IPv4：IPv4协议族。IPv6：IPv6协议族。 默认值：无                                                       |
| VPNNAME           | VPN实例名称     | 可选必选说明：可选参数 参数含义：该参数用于指定VPN实例名。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～31。 默认值：无                                                                                      |
| SOURCEIPV4ADDRESS | 源IPv4地址     | 可选必选说明：条件必选参数 前提条件：该参数在“IPVERSION”配置为“IPv4”时为条件必选参数。 参数含义：该参数用于指定发送ECHO-REQUEST报文的源IPv4地址。 数据来源：本端规划 取值范围：IPv4地址类型。 默认值：无                                    |
| SOURCEIPV6ADDRESS | 源IPv6地址     | 可选必选说明：条件必选参数 前提条件：该参数在“IPVERSION”配置为“IPv6”时为条件必选参数。 参数含义：该参数用于指定发送ECHO-REQUEST报文的源IPv6地址。 数据来源：本端规划 取值范围：IPv6地址类型。 默认值：无                                    |
| DESTIPV4ADDRESS   | 目的IPv4地址    | 可选必选说明：条件必选参数 前提条件：该参数在“IPVERSION”配置为“IPv4”时为条件必选参数。 参数含义：该参数用于指定目的主机IPv4地址。 数据来源：本端规划 取值范围：IPv4地址类型。 默认值：无                                                  |
| DESTIPV6ADDRESS   | 目的IPv6地址    | 可选必选说明：条件必选参数 前提条件：该参数在“IPVERSION”配置为“IPv6”时为条件必选参数。 参数含义：该参数用于指定目的主机IPv6地址。 数据来源：本端规划 取值范围：IPv6地址类型。 默认值：无                                                  |
| PACKETCOUNT       | 发包数         | 可选必选说明：可选参数 参数含义：该参数用于指定发送ECHO-REQUEST报文次数。 数据来源：本端规划 取值范围：整数类型，取值范围为1～4294967295，单位是包数。 默认值：5                                                               |
| PACKETSIZE        | 报文字节数       | 可选必选说明：可选参数 参数含义：该参数用于指定ECHO-REQUEST报文长度（不包括IP和ICMP报文头）。 数据来源：本端规划 取值范围：整数类型，取值范围为20～9600，单位是字节。 默认值：56                                                      |
| INTERVAL          | 报文间隔（ms）    | 可选必选说明：可选参数 参数含义：该参数用于指定发送下一个ECHO-REQUEST报文的等待时间。 数据来源：本端规划 取值范围：整数类型，取值范围为100～10000，单位是毫秒。 默认值：500                                                          |
| TIMEOUT           | 超时时间（ms）    | 可选必选说明：可选参数 参数含义：该参数用于指定发送完ECHO-REQUEST报文后，等待ECHO-REPLY报文的超时时间。 数据来源：本端规划 取值范围：整数类型，取值范围为1～20000，单位是毫秒。 默认值：2000                                             |
| TTL               | TTL值        | 可选必选说明：条件可选参数 前提条件：该参数在“IPVERSION”配置为“IPv4”时为条件可选参数。 参数含义：该参数用于指定TTL的值。 数据来源：本端规划 取值范围：整数类型，取值范围为1～255。 默认值：255                                              |
| TOSORDSCP         | 基于TOS或者DSCP | 可选必选说明：条件可选参数 前提条件：该参数在“IPVERSION”配置为“IPv4”时为条件可选参数。 参数含义：该参数用于指定发送ECHO-REQUEST报文是基于TOS还是DSCP。 数据来源：本端规划 取值范围：枚举类型。 TOS：TOS服务类型。DSCP：DSCP服务类型。 默认值：无         |
| DSCP              | DSCP值       | 可选必选说明：条件可选参数 前提条件：该参数在“TOSORDSCP”配置为“DSCP”时为条件可选参数。 参数含义：该参数用于指定发送ECHO-REQUEST报文的DSCP值。 数据来源：本端规划 取值范围：整数类型，取值范围为0～63。 默认值：0                                |
| TOS               | TOS值        | 可选必选说明：条件可选参数 前提条件：该参数在“TOSORDSCP”配置为“TOS”时为条件可选参数。 参数含义：该参数用于指定发送ECHO-REQUEST报文的TOS值。 数据来源：本端规划 取值范围：整数类型，取值范围为0～255。 默认值：0                                 |
| VERBOSE           | 详细回显        | 可选必选说明：条件可选参数 前提条件：该参数在“IPVERSION”配置为“IPv4”时为可选参数。 参数含义：该参数用于显示PING详细回显信息。 数据来源：本端规划 取值范围：枚举类型。 ENABLE：使能。DISABLE：去使能。 默认值：DISABLE 配置原则：如果不输入该参数，则表示不显示详细信息。 |
| SERVICEINSTANCE   | 服务实例        | 可选必选说明：必选参数 参数含义：该参数表示大颗粒服务实例名称。 数据来源：本端规划 取值范围：字符串类型，通过LST VNFC命令获取。 默认值：无 配置原则：只能填写通过LST VNFC命令查询到的管理代理标识，但不能填写0，0表示VNFP。                                  |

#### 使用实例

- 检查IP地址为10.137.144.1的主机是否可达：

  ```
  INNERPING: IPVERSION=IPv4, SOURCEIPV4ADDRESS="10.137.144.2", DESTIPV4ADDRESS="10.137.144.1",SERVICEINSTANCE="LINK_VNFC_999";
  ```

  ```
    PING 10.137.144.1: 56  data bytes, press CTRL_Q to break 
   
      Reply from 10.137.144.1: bytes=56 Sequence=1 ttl=255 time=1 ms 
   
      Reply from 10.137.144.1: bytes=56 Sequence=2 ttl=255 time=1 ms 
   
      Reply from 10.137.144.1: bytes=56 Sequence=3 ttl=255 time=1 ms 
   
      Reply from 10.137.144.1: bytes=56 Sequence=4 ttl=255 time=1 ms 
   
      Reply from 10.137.144.1: bytes=56 Sequence=5 ttl=255 time=1 ms 
   
    --- 10.137.144.1 ping statistics --- 
      5 packet(s) transmitted 
      5 packet(s) received 
      0% packet loss 
      round-trip min/avg/max=1/1/1 ms 
   
  共有9个报告 
  ---    END
  ```

- 检查IPv6地址为2001:db8::1的主机是否可达：

  ```
  INNERPING: IPVERSION=IPv6, SOURCEIPV6ADDRESS="2001:db8::2", DESTIPV6ADDRESS="2001:db8::1",SERVICEINSTANCE="LINK_VNFC_999";
  ```

  ```
    PING 2001:db8::1 : 56  data bytes, press CTRL_Q to break 
   
      Reply from 2001:db8::1 
      bytes=56 Sequence=1 hop limit=64 time=1 ms 
   
      Reply from 2001:db8::1 
      bytes=56 Sequence=2 hop limit=64 time=1 ms 
   
      Reply from 2001:db8::1 
      bytes=56 Sequence=3 hop limit=64 time=1 ms 
   
      Reply from 2001:db8::1 
      bytes=56 Sequence=4 hop limit=64 time=1 ms 
   
      Reply from 2001:db8::1 
      bytes=56 Sequence=5 hop limit=64 time=1 ms 
   
    --- 2001:db8::1 ping statistics --- 
      5 packet(s) transmitted 
      5 packet(s) received 
      0% packet loss 
      round-trip min/avg/max=1/1/1 ms 
   
  共有9个报告 
  ---    END
  ```