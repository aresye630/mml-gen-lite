# 5G LAN业务Ping功能（NGSRVPING）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用NF：UPF**

该命令通过在用户面业务处理单元发起层二5G LAN终端到对端网元的PING，获取路由可达性以及通信来回旅程的时延以及报文的丢失情况。

#### 注意事项

- 该命令执行后立即生效。
- 该命令同一时刻只能执行一次。
- 源MAC地址必须为UPF上UE学到的MAC地址。
- IP地址和MAC地址都需要客户提供。
- 已经上线的IMSI，可以执行DSP SESSIONINFO: QUERYTYPE=IMSI, IMSI="XXXXX";命令来获取5G LAN组 ID。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识        | 参数名称               | 参数说明                                                                                                                                                                                                                                                                                                                                                                                    |
|:------------|:-------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| VNINSTANCE  | 5G LAN组名称          | 可选必选说明：必选参数 参数含义：该参数用于指定5G LAN组名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为18～37。VNINSTANCE以连字号分为4段，形式为GroupServiceID-MCC-MNC-LocalGroupID。其中，GroupServiceID长度为8，只能输入数字或者范围为A到F或a-f的字母；MCC长度为3，只能输入数字；MNC长度为2~3，只能输入数字；LocalGroupID长度为2~20的偶数，只能输入数字或者范围为A到F或a-f的字母。例如，A0000001-460-003-01，A0000001-460-003-A000000001。不区分大小写。 默认值：无 配置原则： 该参数使用ADD NGVNINSTANCE命令配置生成。该参数可以使用LST NGVNINSTANCE命令查询。 |
| DIRECTION   | ECHO-REQUEST报文发送方向 | 可选必选说明：必选参数 参数含义：该参数用于指定ECHO-REQUEST报文的发送方向。 数据来源：本端规划 取值范围： TO_N3：ECHO-REQUEST报文发送到N3侧，TO_N3是UPF-CPE方向。TO_N6：ECHO-REQUEST报文发送到N6侧，TO_N6是UPF-DN(企业服务器)的方向。 默认值：无 配置原则：无                                                                                                                                                                                                                 |
| VTEPNAME    | Vxlan隧道端点名称        | 可选必选说明：条件可选参数 前提条件：该参数在“DIRECTION”配置为“TO_N6”时为可选参数。 参数含义：该参数用于指定VXLAN隧道端点名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。不区分大小写，不支持空格。 默认值：无 配置原则：无                                                                                                                                                                                                                                                |
| SOURCEMAC   | 源MAC地址             | 可选必选说明：必选参数 参数含义：该参数用于指定源MAC地址。 数据来源：全网规划 取值范围：NA。 默认值：无 配置原则：字符串类型，输入长度为17位。字符串应符合MAC地址格式，如11-11-11-11-11-11。                                                                                                                                                                                                                                                                          |
| DESTMAC     | 目的MAC地址            | 可选必选说明：必选参数 参数含义：该参数用于指定目的MAC地址。 数据来源：全网规划 取值范围：字符串类型，输入长度为17位。字符串应符合MAC地址格式，如11-11-11-11-11-11。 默认值：无 配置原则：无                                                                                                                                                                                                                                                                           |
| IPVERSION   | IP地址类型             | 可选必选说明：必选参数 参数含义：该参数用于指定IP地址类型。 数据来源：本端规划 取值范围： IPv4：表示地址类型为IPv4。IPv6：表示地址类型为IPv6。 默认值：无 配置原则：无                                                                                                                                                                                                                                                                                         |
| SRCIPV4ADDR | 源IPv4地址            | 可选必选说明：条件必选参数 前提条件：该参数在“IPVERSION”配置为“IPv4”时为必选参数。 参数含义：该参数用于指定源IPv4地址。 数据来源：全网规划 取值范围：IPv4地址类型。采用点分十进制"X.X.X.X"格式。 默认值：无 配置原则：无                                                                                                                                                                                                                                                        |
| SRCIPV6ADDR | 源IPv6地址            | 可选必选说明：条件必选参数 前提条件：该参数在“IPVERSION”配置为“IPv6”时为必选参数。 参数含义：该参数用于指定源IPv6地址。 数据来源：全网规划 取值范围：IPv6地址类型。采用冒号分十六进制X:X:X:X:X:X:X:X格式。 默认值：无 配置原则：无                                                                                                                                                                                                                                                |
| DSTIPV4ADDR | 目的IPv4地址           | 可选必选说明：条件必选参数 前提条件：该参数在“IPVERSION”配置为“IPv4”时为必选参数。 参数含义：该参数用于指定目的主机IPv4地址。 数据来源：全网规划 取值范围：IPv4地址类型。采用点分十进制"X.X.X.X"格式。 默认值：无 配置原则：无                                                                                                                                                                                                                                                     |
| DSTIPV6ADDR | 目的IPv6地址           | 可选必选说明：条件必选参数 前提条件：该参数在“IPVERSION”配置为“IPv6”时为必选参数。 参数含义：该参数用于指定目的主机IPv6地址。 数据来源：全网规划 取值范围：IPv6地址类型。采用冒号分十六进制X:X:X:X:X:X:X:X格式。 默认值：无 配置原则：无                                                                                                                                                                                                                                             |
| PACKETNUM   | 发送报文次数             | 可选必选说明：可选参数 参数含义：该参数用于指定发送ECHO-REQUEST报文次数。 数据来源：本端规划 取值范围：整数类型，取值范围为1～65535。 默认值：5 配置原则：无                                                                                                                                                                                                                                                                                              |
| PACKETSIZE  | 报文长度               | 可选必选说明：可选参数 参数含义：该参数用于指定ECHO-REQUEST报文长度（不包括以太、IP和ICMP报文头）。 数据来源：本端规划 取值范围：整数类型，取值范围为20～9600。 默认值：80 配置原则：无                                                                                                                                                                                                                                                                             |
| INTERVAL    | 报文发送间隔时间（毫秒）       | 可选必选说明：可选参数 参数含义：该参数用于指定发送下一个ECHO-REQUEST报文的等待时间。 数据来源：本端规划 取值范围：整数类型，取值范围为100～10000（毫秒）。 默认值：500 配置原则：无                                                                                                                                                                                                                                                                                |
| TIMEOUT     | 等待响应消息的超时时间（毫秒）    | 可选必选说明：可选参数 参数含义：该参数用于指定发送完ECHO-REQUEST报文后，等待ECHO-REPLY报文的超时时间。 数据来源：本端规划 取值范围：整数类型，取值范围为100～65535（毫秒）。 默认值：2000 配置原则：无                                                                                                                                                                                                                                                                 |

#### 使用实例

- 检查N3侧的链路状态：

  ```
  NGSRVPING: VNINSTANCE="a0000001-460-003-01", DIRECTION=TO_N3, SOURCEMAC="76-BB-CC-DD-EE-20", DESTMAC="76-BB-CC-DD-EE-30", IPVERSION=IPv4, SRCIPV4ADDR="10.2.3.4", DSTIPV4ADDR="10.6.7.8";

  %% NGSRVPING: VNINSTANCE="a0000001-460-003-01", DIRECTION=TO_N3, SOURCEMAC="76-BB-CC-DD-EE-20", DESTMAC="76-BB-CC-DD-EE-30", IPVERSION=IPv4, SRCIPV4ADDR="10.2.3.4", DSTIPV4ADDR="10.6.7.8";%%

  RETCODE = 99999 Real Time Report Success

  仍有后续报告输出

  --- END

  %% NGSRVPING: VNINSTANCE="a0000001-460-003-01", DIRECTION=TO_N3, SOURCEMAC="76-BB-CC-DD-EE-20", DESTMAC="76-BB-CC-DD-EE-30", IPVERSION=IPv4, SRCIPV4ADDR="10.2.3.4", DSTIPV4ADDR="10.6.7.8";%%

  RETCODE = 99999 Real Time Report Success

  128 bytes from 10.6.7.8: icmp_seq=1 ttl=128 time=3.182 ms

  仍有后续报告输出

  --- END

  %% NGSRVPING: VNINSTANCE="a0000001-460-003-01", DIRECTION=TO_N3, SOURCEMAC="76-BB-CC-DD-EE-20", DESTMAC="76-BB-CC-DD-EE-30", IPVERSION=IPv4, SRCIPV4ADDR="10.2.3.4", DSTIPV4ADDR="10.6.7.8";%%

  RETCODE = 99999 Real Time Report Success

  Request time out.

  仍有后续报告输出

  --- END

  %% NGSRVPING: VNINSTANCE="a0000001-460-003-01", DIRECTION=TO_N3, SOURCEMAC="76-BB-CC-DD-EE-20", DESTMAC="76-BB-CC-DD-EE-30", IPVERSION=IPv4, SRCIPV4ADDR="10.2.3.4", DSTIPV4ADDR="10.6.7.8";%%
  RETCODE = 0 操作成功

  --- 10.6.7.8 ping statistics ---
  2 packet(s) transmitted
  1 packet(s) received
  50% packet loss
  round-trip min/avg/max = 3.182/3.182/3.182 ms

  共有4个报告
  --- END
  ```
- 检查N6侧的链路状态：

  ```
  NGSRVPING: VNINSTANCE="a0000001-460-003-01", DIRECTION=TO_N6, VTEPNAME="vtep1", SOURCEMAC="76-BB-CC-DD-EE-20", DESTMAC="76-BB-CC-DD-EE-30", IPVERSION=IPv4, SRCIPV4ADDR="10.2.3.4", DSTIPV4ADDR="10.6.7.8";

  %% NGSRVPING: VNINSTANCE="a0000001-460-003-01", DIRECTION=TO_N6, VTEPNAME="vtep1", SOURCEMAC="76-BB-CC-DD-EE-20", DESTMAC="76-BB-CC-DD-EE-30", IPVERSION=IPv4, SRCIPV4ADDR="10.2.3.4", DSTIPV4ADDR="10.6.7.8";%%
  RETCODE = 99999 Real Time Report Success

  仍有后续报告输出
  --- END

  %% NGSRVPING: VNINSTANCE="a0000001-460-003-01", DIRECTION=TO_N6, VTEPNAME="vtep1", SOURCEMAC="76-BB-CC-DD-EE-20", DESTMAC="76-BB-CC-DD-EE-30", IPVERSION=IPv4, SRCIPV4ADDR="10.2.3.4", DSTIPV4ADDR="10.6.7.8";%%
  RETCODE = 99999 Real Time Report Success

  128 bytes from 10.6.7.8: icmp_seq=1 ttl=128 time=3.005 ms

  仍有后续报告输出
  --- END

  %% NGSRVPING: VNINSTANCE="a0000001-460-003-01", DIRECTION=TO_N6, VTEPNAME="vtep1", SOURCEMAC="76-BB-CC-DD-EE-20", DESTMAC="76-BB-CC-DD-EE-30", IPVERSION=IPv4, SRCIPV4ADDR="10.2.3.4", DSTIPV4ADDR="10.6.7.8";%%
  RETCODE = 99999 Real Time Report Success

  Request time out.

  仍有后续报告输出
  --- END

  %% NGSRVPING: VNINSTANCE="a0000001-460-003-01", DIRECTION=TO_N6, VTEPNAME="vtep1", SOURCEMAC="76-BB-CC-DD-EE-20", DESTMAC="76-BB-CC-DD-EE-30", IPVERSION=IPv4, SRCIPV4ADDR="10.2.3.4", DSTIPV4ADDR="10.6.7.8";%%
  RETCODE = 0 操作成功

  --- 10.6.7.8 ping statistics ---
  2 packet(s) transmitted
  1 packet(s) received
  50% packet loss
  round-trip min/avg/max = 3.005/3.005/3.005 ms

  共有4个报告
  --- END
  ```