# 业务Ping功能（SRVPING）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用NF：SGW-U、PGW-U、UPF**

该命令通过在用户面业务处理单元发起本端逻辑接口IP到对端网元的PING，或者发起本地/外部地址池中某个空闲IP到网络侧的PING，获取路由可达性以及通信来回旅程的时延以及报文的丢失情况。

#### 注意事项

- 该命令执行后立即生效。
- 该命令同一时刻只能执行一次。
- 源地址必须为逻辑接口地址或地址池中的地址。
- 若本地地址池中的源IP已被分配给UE，会导致用户去活。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识         | 参数名称           | 参数说明                                                                                                                                                                                               |
|:-------------|:---------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SRCIPTYPE    | 源地址类型          | 可选必选说明：必选参数 参数含义：该参数用于指定源地址类型。 数据来源：本端规划 取值范围： LOGICINF：源地址类型为逻辑接口地址。POOL：源地址类型为地址池地址。 默认值：无 配置原则：无                                                                                                |
| LOGICINFNAME | 逻辑接口名称         | 可选必选说明：条件必选参数 前提条件：该参数在“SRCIPTYPE”配置为“LOGICINF”时为必选参数。 参数含义：该参数用于指定逻辑接口名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。 默认值：无 配置原则：该参数使用ADD LOGICINF命令配置生成。                                      |
| POOLNAME     | 地址池名称          | 可选必选说明：条件必选参数 前提条件：该参数在“SRCIPTYPE”配置为“POOL”时为必选参数。 参数含义：该参数用于指定地址池的名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～79，单位是字节。由“_”、“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”，不区分大小写。 默认值：无 配置原则：该参数使用ADD POOL命令配置生成。 |
| IPVERSION    | IP地址类型         | 可选必选说明：必选参数 参数含义：该参数用于指定IP地址类型。 数据来源：本端规划 取值范围： IPv4：表示地址类型为IPv4。IPv6：表示地址类型为IPv6。 默认值：无 配置原则：无                                                                                                    |
| SRCIPV4ADDR  | 源IPv4地址        | 可选必选说明：条件必选参数 前提条件：该参数在“IPVERSION”配置为“IPv4”时为必选参数。 参数含义：该参数用于指定源IPv4地址。 数据来源：全网规划 取值范围：IPv4地址类型。采用点分十进制"X.X.X.X"格式。 默认值：无 配置原则：无                                                                   |
| SRCIPV6ADDR  | 源IPv6地址        | 可选必选说明：条件必选参数 前提条件：该参数在“IPVERSION”配置为“IPv6”时为必选参数。 参数含义：该参数用于指定源IPv6地址。 数据来源：全网规划 取值范围：IPv6地址类型。采用冒号分十六进制X:X:X:X:X:X:X:X格式。 默认值：无 配置原则：无                                                           |
| DSTIPV4ADDR  | 目的IPv4地址       | 可选必选说明：条件必选参数 前提条件：该参数在“IPVERSION”配置为“IPv4”时为必选参数。 参数含义：该参数用于指定目的主机IPv4地址。 数据来源：全网规划 取值范围：IPv4地址类型。采用点分十进制"X.X.X.X"格式。 默认值：无 配置原则：无                                                                |
| DSTIPV6ADDR  | 目的IPv6地址       | 可选必选说明：条件必选参数 前提条件：该参数在“IPVERSION”配置为“IPv6”时为必选参数。 参数含义：该参数用于指定目的主机IPv6地址。 数据来源：全网规划 取值范围：IPv6地址类型。采用冒号分十六进制X:X:X:X:X:X:X:X格式。 默认值：无 配置原则：无                                                        |
| PACKETNUM    | 发送报文次数         | 可选必选说明：可选参数 参数含义：该参数用于指定发送ECHO-REQUEST报文次数。 数据来源：全网规划 取值范围：整数类型，取值范围为1～65535。 默认值：5 配置原则：无                                                                                                         |
| PACKETSIZE   | 报文长度           | 可选必选说明：可选参数 参数含义：该参数用于指定ECHO-REQUEST报文长度（不包括IP和ICMP报文头）。 数据来源：全网规划 取值范围：整数类型，取值范围为20～9600。 默认值：80 配置原则：无                                                                                           |
| INTERVAL     | 报文发送间隔（ms）     | 可选必选说明：可选参数 参数含义：该参数用于指定发送下一个ECHO-REQUEST报文的等待时间。 数据来源：全网规划 取值范围：整数类型，取值范围为1～10000。 默认值：500 配置原则：无                                                                                                 |
| TIMEOUT      | 超时时间（ms）       | 可选必选说明：可选参数 参数含义：该参数用于指定发送完ECHO-REQUEST报文后，等待ECHO-REPLY报文的超时时间。 数据来源：全网规划 取值范围：整数类型，取值范围为1～65535。 默认值：2000 配置原则：无                                                                                  |
| TTL          | TTL值           | 可选必选说明：可选参数 参数含义：该参数用于指定TTL的值。 数据来源：全网规划 取值范围：整数类型，取值范围为1～255。 默认值：255 配置原则：无                                                                                                                      |
| DSCPV        | DSCP值          | 可选必选说明：条件可选参数 前提条件：该参数在“IPVERSION”配置为“IPv4”时为可选参数。 参数含义：该参数用于指定探测报文的DSCP值。 数据来源：本端规划 取值范围：整数类型，取值范围为0～63。 默认值：无 配置原则：无                                                                             |
| TCV          | Traffic-Class值 | 可选必选说明：条件可选参数 前提条件：该参数在“IPVERSION”配置为“IPv6”时为可选参数。 参数含义：Traffic-Class值。 数据来源：本端规划 取值范围：整数类型，取值范围为0～63。 默认值：无 配置原则：无                                                                                |

#### 使用实例

- 目的地址可达情景，检查IP地址为10.0.0.15的主机链路：

  ```
  SRVPING: SRCIPTYPE=LOGICINF, LOGICINFNAME="n3if1/1/0", IPVERSION=IPv4, SRCIPV4ADDR="10.1.1.12", DSTIPV4ADDR="10.0.0.15", PACKETNUM=3;

  %%SRVPING: SRCIPTYPE=LOGICINF, LOGICINFNAME="n3if1/1/0", IPVERSION=IPv4, SRCIPV4ADDR="10.1.1.12", DSTIPV4ADDR="10.0.0.15", PACKETNUM=3;%%
  RETCODE = 99999 Real Time Report Success

  仍有后续报告输出
  --- END

  %%SRVPING: SRCIPTYPE=LOGICINF, LOGICINFNAME="n3if1/1/0", IPVERSION=IPv4, SRCIPV4ADDR="10.1.1.12", DSTIPV4ADDR="10.0.0.15", PACKETNUM=3;%%
  RETCODE = 99999 Real Time Report Success

  108 bytes from 10.0.0.15: icmp_seq=1 ttl=62 time=14.863 ms

  仍有后续报告输出
  --- END

  %%SRVPING: SRCIPTYPE=LOGICINF, LOGICINFNAME="n3if1/1/0", IPVERSION=IPv4, SRCIPV4ADDR="10.1.1.12", DSTIPV4ADDR="10.0.0.15", PACKETNUM=3;%%
  RETCODE = 99999 Real Time Report Success

  108 bytes from 10.0.0.15: icmp_seq=2 ttl=62 time=9.893 ms

  仍有后续报告输出
  --- END

  %%SRVPING: SRCIPTYPE=LOGICINF, LOGICINFNAME="n3if1/1/0", IPVERSION=IPv4, SRCIPV4ADDR="10.1.1.12", DSTIPV4ADDR="10.0.0.15", PACKETNUM=3;%%
  RETCODE = 99999 Real Time Report Success

  108 bytes from 10.0.0.15: icmp_seq=3 ttl=62 time=14.195 ms

  仍有后续报告输出
  --- END

  %%SRVPING: SRCIPTYPE=LOGICINF, LOGICINFNAME="n3if1/1/0", IPVERSION=IPv4, SRCIPV4ADDR="10.1.1.12", DSTIPV4ADDR="10.0.0.15", PACKETNUM=3;%%
  RETCODE = 0 操作成功

  --- 10.0.0.15 ping statistics ---
  3 packet(s) transmitted
  3 packet(s) received
  0% packet loss
  round-trip min/avg/max = 9.893/12.984/14.863 ms

  共有5个报告
  --- END
  ```
- 目的地址不可达情景，检查IP地址为10.0.0.150的主机链路：

  ```
  SRVPING: SRCIPTYPE=LOGICINF, LOGICINFNAME="n3if1/1/0", IPVERSION=IPv4, SRCIPV4ADDR="10.1.1.12", DSTIPV4ADDR="10.0.0.150", PACKETNUM=3;

  %%SRVPING: SRCIPTYPE=LOGICINF, LOGICINFNAME="n3if1/1/0", IPVERSION=IPv4, SRCIPV4ADDR="10.1.1.12", DSTIPV4ADDR="10.0.0.150", PACKETNUM=3;%%
  RETCODE = 99999 Real Time Report Success

  仍有后续报告输出
  --- END

  %%SRVPING: SRCIPTYPE=LOGICINF, LOGICINFNAME="n3if1/1/0", IPVERSION=IPv4, SRCIPV4ADDR="10.1.1.12", DSTIPV4ADDR="10.0.0.150", PACKETNUM=3;%%
  RETCODE = 99999 Real Time Report Success

  Request time out.

  仍有后续报告输出
  --- END

  %%SRVPING: SRCIPTYPE=LOGICINF, LOGICINFNAME="n3if1/1/0", IPVERSION=IPv4, SRCIPV4ADDR="10.1.1.12", DSTIPV4ADDR="10.0.0.150", PACKETNUM=3;%%
  RETCODE = 99999 Real Time Report Success

  Request time out.

  仍有后续报告输出
  --- END

  %%SRVPING: SRCIPTYPE=LOGICINF, LOGICINFNAME="n3if1/1/0", IPVERSION=IPv4, SRCIPV4ADDR="10.1.1.12", DSTIPV4ADDR="10.0.0.150", PACKETNUM=3;%%
  RETCODE = 99999 Real Time Report Success

  Request time out.

  仍有后续报告输出
  --- END

  %%SRVPING: SRCIPTYPE=LOGICINF, LOGICINFNAME="n3if1/1/0", IPVERSION=IPv4, SRCIPV4ADDR="10.1.1.12", DSTIPV4ADDR="10.0.0.150", PACKETNUM=3;%%
  RETCODE = 0 操作成功

  --- 10.0.0.150 ping statistics ---
  3 packet(s) transmitted
  0 packet(s) received
  100% packet loss
  round-trip min/avg/max = 0.0/0.0/0.0 ms

  共有5个报告
  --- END
  ```