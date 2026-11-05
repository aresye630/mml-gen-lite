# 业务Tracert功能（SRVTRACERT）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用NF：SGW-U、PGW-U、UPF**

该命令通过在用户面业务处理单元发起本端逻辑接口IP到对端网元的测试数据包，或者发起本地地址池中某个IP到网络侧的测试数据包，探测所经过的路径节点。

#### 注意事项

- 该命令执行后立即生效。
- 该命令同一时刻只能执行一次。
- 源地址必须为逻辑接口地址或地址池中的地址。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识         | 参数名称     | 参数说明                                                                                                                                                          |
|:-------------|:---------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SRCIPTYPE    | 源地址类型    | 可选必选说明：必选参数 参数含义：该参数用于指定源地址类型。 数据来源：本端规划 取值范围： LOGICINF：源地址类型为逻辑接口地址。POOL：源地址类型为地址池地址。 默认值：无 配置原则：无                                                           |
| LOGICINFNAME | 逻辑接口名称   | 可选必选说明：条件必选参数 前提条件：该参数在“SRCIPTYPE”配置为“LOGICINF”时为必选参数。 参数含义：该参数用于指定逻辑接口名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。 默认值：无 配置原则：该参数使用ADD LOGICINF命令配置生成。 |
| POOLNAME     | 地址池名称    | 可选必选说明：条件必选参数 前提条件：该参数在“SRCIPTYPE”配置为“POOL”时为必选参数。 参数含义：该参数用于指定地址池的名称。 数据来源：本端规划 取值范围：NA。 默认值：无 配置原则：该参数使用ADD POOL命令配置生成。                                     |
| IPVERSION    | IP地址类型   | 可选必选说明：必选参数 参数含义：该参数用于指定IP地址类型。 数据来源：本端规划 取值范围： IPv4：表示地址类型为IPv4。IPv6：表示地址类型为IPv6。 默认值：无 配置原则：无                                                               |
| SRCIPV4ADDR  | 源IPv4地址  | 可选必选说明：条件必选参数 前提条件：该参数在“IPVERSION”配置为“IPv4”时为必选参数。 参数含义：该参数用于指定源IPv4地址。 数据来源：全网规划 取值范围：IPv4地址类型。采用点分十进制"X.X.X.X"格式。 默认值：无 配置原则：无                              |
| SRCIPV6ADDR  | 源IPv6地址  | 可选必选说明：条件必选参数 前提条件：该参数在“IPVERSION”配置为“IPv6”时为必选参数。 参数含义：该参数用于指定源IPv6地址。 数据来源：全网规划 取值范围：IPv6地址类型。采用冒号分十六进制X:X:X:X:X:X:X:X格式。 默认值：无 配置原则：无                      |
| DSTIPV4ADDR  | 目的IPv4地址 | 可选必选说明：条件必选参数 前提条件：该参数在“IPVERSION”配置为“IPv4”时为必选参数。 参数含义：该参数用于指定目的主机IPv4地址。 数据来源：全网规划 取值范围：IPv4地址类型。采用点分十进制"X.X.X.X"格式。 默认值：无 配置原则：无                           |
| DSTIPV6ADDR  | 目的IPv6地址 | 可选必选说明：条件必选参数 前提条件：该参数在“IPVERSION”配置为“IPv6”时为必选参数。 参数含义：该参数用于指定目的主机IPv6地址。 数据来源：全网规划 取值范围：IPv6地址类型。采用冒号分十六进制X:X:X:X:X:X:X:X格式。 默认值：无 配置原则：无                   |
| PACKETNUM    | 发送报文次数   | 可选必选说明：可选参数 参数含义：该参数用于指定每次发送的探测数据包个数。 数据来源：全网规划 取值范围：整数类型，取值范围为1～65535。 默认值：5 配置原则：无                                                                          |
| PACKETSIZE   | 报文长度     | 可选必选说明：可选参数 参数含义：该参数用于指定ECHO-REQUEST报文长度（不包括IP和ICMP报文头）。 数据来源：全网规划 取值范围：整数类型，取值范围为20～9600。 默认值：80 配置原则：无                                                      |
| TIMEOUT      | 超时时间（ms） | 可选必选说明：可选参数 参数含义：该参数用于指定等待响应报文的超时时间。 数据来源：全网规划 取值范围：整数类型，取值范围为1～65535。 默认值：2000 配置原则：无                                                                        |
| FIRSTTTL     | 初始TTL    | 可选必选说明：可选参数 参数含义：该参数用于指定初始TTL的值。 数据来源：全网规划 取值范围：整数类型，取值范围为1～255。 默认值：1 配置原则：无                                                                                 |
| MAXTTL       | 最大TTL    | 可选必选说明：可选参数 参数含义：该参数用于指定最大TTL的值。 数据来源：全网规划 取值范围：整数类型，取值范围为1～255。 默认值：30 配置原则：无                                                                                |

#### 使用实例

- 目的地址可达情景，检查从发送主机到IP地址为10.0.0.15的主机所经过的网关：

  ```
  SRVTRACERT: SRCIPTYPE=LOGICINF, LOGICINFNAME="n3if1/1/0", IPVERSION=IPv4, SRCIPV4ADDR="10.1.1.12", DSTIPV4ADDR="10.0.0.15", PACKETNUM=3, MAXTTL=3;

  %%SRVTRACERT: SRCIPTYPE=LOGICINF, LOGICINFNAME="n3if1/1/0", IPVERSION=IPv4, SRCIPV4ADDR="10.1.1.12", DSTIPV4ADDR="10.0.0.15", PACKETNUM=3, MAXTTL=3;%%
  RETCODE = 99999  Real Time Report Success

  仍有后续报告输出
  ---    END

  %%SRVTRACERT: SRCIPTYPE=LOGICINF, LOGICINFNAME="n3if1/1/0", IPVERSION=IPv4, SRCIPV4ADDR="10.1.1.12", DSTIPV4ADDR="10.0.0.15", PACKETNUM=3, MAXTTL=3;%%
  RETCODE = 99999  Real Time Report Success

  1  10.1.1.255  12.402 ms  21.878 ms  18.237 ms

  仍有后续报告输出
  ---    END

  %%SRVTRACERT: SRCIPTYPE=LOGICINF, LOGICINFNAME="n3if1/1/0", IPVERSION=IPv4, SRCIPV4ADDR="10.1.1.12", DSTIPV4ADDR="10.0.0.15", PACKETNUM=3, MAXTTL=3;%%
  RETCODE = 99999  Real Time Report Success

  2  10.0.0.15  13.184 ms  13.522 ms  14.529 ms

  仍有后续报告输出
  ---    END

  %%SRVTRACERT: SRCIPTYPE=LOGICINF, LOGICINFNAME="n3if1/1/0", IPVERSION=IPv4, SRCIPV4ADDR="10.1.1.12", DSTIPV4ADDR="10.0.0.15", PACKETNUM=3, MAXTTL=3;%%
  RETCODE = 0  操作成功

  Trace Completed
  Total Receive : 6
  round-trip min/avg/max = 12.402/15.625/21.878 ms

  共有4个报告
  ---    END
  ```
- 目的地址不可达情景，检查从发送主机到IP地址为10.0.0.150的主机所经过的网关：

  ```
  SRVTRACERT: SRCIPTYPE=LOGICINF, LOGICINFNAME="n3if1/1/0", IPVERSION=IPv4, SRCIPV4ADDR="10.1.1.12", DSTIPV4ADDR="10.0.0.150", PACKETNUM=3, MAXTTL=3;

  %%SRVTRACERT: SRCIPTYPE=LOGICINF, LOGICINFNAME="n3if1/1/0", IPVERSION=IPv4, SRCIPV4ADDR="10.1.1.12", DSTIPV4ADDR="10.0.0.150", PACKETNUM=3, MAXTTL=3;%%
  RETCODE = 99999  Real Time Report Success

  仍有后续报告输出
  ---    END

  %%SRVTRACERT: SRCIPTYPE=LOGICINF, LOGICINFNAME="n3if1/1/0", IPVERSION=IPv4, SRCIPV4ADDR="10.1.1.12", DSTIPV4ADDR="10.0.0.150", PACKETNUM=3, MAXTTL=3;%%
  RETCODE = 99999  Real Time Report Success

  1  10.1.1.255  11.3 ms  13.753 ms  10.891 ms

  仍有后续报告输出
  ---    END

  %%SRVTRACERT: SRCIPTYPE=LOGICINF, LOGICINFNAME="n3if1/1/0", IPVERSION=IPv4, SRCIPV4ADDR="10.1.1.12", DSTIPV4ADDR="10.0.0.150", PACKETNUM=3, MAXTTL=3;%%
  RETCODE = 99999  Real Time Report Success

  2    *  *  *

  仍有后续报告输出
  ---    END

  %%SRVTRACERT: SRCIPTYPE=LOGICINF, LOGICINFNAME="n3if1/1/0", IPVERSION=IPv4, SRCIPV4ADDR="10.1.1.12", DSTIPV4ADDR="10.0.0.150", PACKETNUM=3, MAXTTL=3;%%
  RETCODE = 99999  Real Time Report Success

  3    *  *  *

  仍有后续报告输出
  ---    END

  %%SRVTRACERT: SRCIPTYPE=LOGICINF, LOGICINFNAME="n3if1/1/0", IPVERSION=IPv4, SRCIPV4ADDR="10.1.1.12", DSTIPV4ADDR="10.0.0.150", PACKETNUM=3, MAXTTL=3;%%
  RETCODE = 0  操作成功

  Trace Completed
  Total Receive : 3
  round-trip min/avg/max = 10.891/11.883/13.753 ms

  共有5个报告
  ---    END
  ```