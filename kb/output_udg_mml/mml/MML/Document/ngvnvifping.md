# 5G LAN虚拟接口ping功能（NGVNVIFPING）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用NF：UPF**

该命令通过在用户面业务处理单元发起层二5G LAN虚拟接口到对端设备的PING，获取路由可达性以及通信来回旅程的时延以及报文的丢失情况。

#### 注意事项

- 该命令执行后立即生效。
- 该命令同一时刻只能执行一次。
- 该命令与NGSRVPING命令同一时刻只能执行一次。
- 该命令与TST NGVXLANCONNECT命令同一时刻只能执行一次。
- 该命令执行前需要执行ADD NGVNINSTANCE配置5G LAN组。
- 该命令执行前需要执行ADD NGVNVIF命令配置5G LAN组的虚拟接口，该虚拟接口的IPv4地址用于填充发送ARP报文和PING报文的源IP地址。
- 该命令执行前需要SET UPETHSRVPARA命令配置用户面以太业务的MAC地址，该MAC地址用于填充发送ARP报文和PING报文的源MAC地址。
- 该命令的目的IPv4地址不能与ADD NGVNVIF命令中的虚拟接口IP地址相同。
- 该命令最多发送3次ARP请求，单次ARP请求的超时时间为2s，期间没有收到ARP响应，命令执行失败。
- 组会话未激活时，如果执行该命令，5分钟内组会话会激活失败。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识        | 参数名称            | 参数说明                                                                                                                                                                                                                                                                                                                            |
|:------------|:----------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| VNINSTANCE  | 5G LAN组名称       | 可选必选说明：必选参数 参数含义：该参数用于指定5G LAN组名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为18～37。VNINSTANCE以连字号分为4段，形式为GroupServiceID-MCC-MNC-LocalGroupID。其中，GroupServiceID长度为8，只能输入数字或者范围为A到F或a-f的字母；MCC长度为3，只能输入数字；MNC长度为2~3，只能输入数字；LocalGroupID长度为2~20的偶数，只能输入数字或者范围为A到F或a-f的字母。例如，A0000001-460-003-01，A0000001-460-003-A000000001。不区分大小写。 默认值：无 配置原则：无 |
| DSTIPV4ADDR | 目的IPv4地址        | 可选必选说明：必选参数 参数含义：该参数用于指定目的主机IPv4地址。 数据来源：全网规划 取值范围：IPv4地址类型。采用点分十进制"X.X.X.X"格式。 默认值：无 配置原则：无                                                                                                                                                                                                                                    |
| PACKETNUM   | 发送报文次数          | 可选必选说明：可选参数 参数含义：该参数用于指定发送ECHO-REQUEST报文次数。 数据来源：本端规划 取值范围：整数类型，取值范围为1～15。 默认值：5 配置原则：无                                                                                                                                                                                                                                         |
| PACKETSIZE  | 报文长度            | 可选必选说明：可选参数 参数含义：该参数用于指定ECHO-REQUEST报文长度（不包括以太、IP和ICMP报文头）。 数据来源：本端规划 取值范围：整数类型，取值范围为20～9600。 默认值：80 配置原则：无                                                                                                                                                                                                                     |
| INTERVAL    | 报文发送间隔时间（毫秒）    | 可选必选说明：可选参数 参数含义：该参数用于指定发送下一个ECHO-REQUEST报文的等待时间。 数据来源：本端规划 取值范围：整数类型，取值范围为100～10000（毫秒）。 默认值：500 配置原则：无                                                                                                                                                                                                                        |
| TIMEOUT     | 等待响应消息的超时时间（毫秒） | 可选必选说明：可选参数 参数含义：该参数用于指定发送完ECHO-REQUEST报文后，等待ECHO-REPLY报文的超时时间。 数据来源：本端规划 取值范围：整数类型，取值范围为100～20000（毫秒）。 默认值：2000 配置原则：无                                                                                                                                                                                                         |

#### 使用实例

检查对端设备的链路状态：

```
%%NGVNVIFPING: VNINSTANCE="a0000001-460-01-01", DSTIPV4ADDR="192.168.0.2";%%
RETCODE = 99999  Real Time Report Success

仍有后续报告输出
---    END

%%NGVNVIFPING: VNINSTANCE="a0000001-460-01-01", DSTIPV4ADDR="192.168.0.2";%%
RETCODE = 99999  Real Time Report Success

108 bytes from 192.168.0.2: icmp_seq=1 ttl=255 time=103.560 ms

仍有后续报告输出
---    END

%%NGVNVIFPING: VNINSTANCE="a0000001-460-01-01", DSTIPV4ADDR="192.168.0.2";%%
RETCODE = 99999  Real Time Report Success

108 bytes from 192.168.0.2: icmp_seq=1 ttl=255 time=103.560 ms

仍有后续报告输出
---    END

%%NGVNVIFPING: VNINSTANCE="a0000001-460-01-01", DSTIPV4ADDR="192.168.0.2";%%
RETCODE = 99999  Real Time Report Success

108 bytes from 192.168.0.2: icmp_seq=1 ttl=255 time=103.560 ms

仍有后续报告输出
---    END

%%NGVNVIFPING: VNINSTANCE="a0000001-460-01-01", DSTIPV4ADDR="192.168.0.2";%%
RETCODE = 99999  Real Time Report Success

108 bytes from 192.168.0.2: icmp_seq=2 ttl=255 time=123.010 ms

仍有后续报告输出
---    END

%%NGVNVIFPING: VNINSTANCE="a0000001-460-01-01", DSTIPV4ADDR="192.168.0.2";%%
RETCODE = 99999  Real Time Report Success

108 bytes from 192.168.0.2: icmp_seq=2 ttl=255 time=123.010 ms

仍有后续报告输出
---    END

%%NGVNVIFPING: VNINSTANCE="a0000001-460-01-01", DSTIPV4ADDR="192.168.0.2";%%
RETCODE = 99999  Real Time Report Success

108 bytes from 192.168.0.2: icmp_seq=2 ttl=255 time=123.010 ms

仍有后续报告输出
---    END

%%NGVNVIFPING: VNINSTANCE="a0000001-460-01-01", DSTIPV4ADDR="192.168.0.2";%%
RETCODE = 99999  Real Time Report Success

108 bytes from 192.168.0.2: icmp_seq=3 ttl=255 time=733.068 ms

仍有后续报告输出
---    END

%%NGVNVIFPING: VNINSTANCE="a0000001-460-01-01", DSTIPV4ADDR="192.168.0.2";%%
RETCODE = 99999  Real Time Report Success

108 bytes from 192.168.0.2: icmp_seq=3 ttl=255 time=733.068 ms

仍有后续报告输出
---    END

%%NGVNVIFPING: VNINSTANCE="a0000001-460-01-01", DSTIPV4ADDR="192.168.0.2";%%
RETCODE = 99999  Real Time Report Success

108 bytes from 192.168.0.2: icmp_seq=3 ttl=255 time=733.068 ms

仍有后续报告输出
---    END

%%NGVNVIFPING: VNINSTANCE="a0000001-460-01-01", DSTIPV4ADDR="192.168.0.2";%%
RETCODE = 99999  Real Time Report Success

108 bytes from 192.168.0.2: icmp_seq=4 ttl=255 time=106.079 ms

仍有后续报告输出
---    END

%%NGVNVIFPING: VNINSTANCE="a0000001-460-01-01", DSTIPV4ADDR="192.168.0.2";%%
RETCODE = 99999  Real Time Report Success

108 bytes from 192.168.0.2: icmp_seq=4 ttl=255 time=106.079 ms

仍有后续报告输出
---    END

%%NGVNVIFPING: VNINSTANCE="a0000001-460-01-01", DSTIPV4ADDR="192.168.0.2";%%
RETCODE = 99999  Real Time Report Success

108 bytes from 192.168.0.2: icmp_seq=4 ttl=255 time=106.079 ms

仍有后续报告输出
---    END

%%NGVNVIFPING: VNINSTANCE="a0000001-460-01-01", DSTIPV4ADDR="192.168.0.2";%%
RETCODE = 99999  Real Time Report Success

108 bytes from 192.168.0.2: icmp_seq=5 ttl=255 time=182.130 ms

仍有后续报告输出
---    END

%%NGVNVIFPING: VNINSTANCE="a0000001-460-01-01", DSTIPV4ADDR="192.168.0.2";%%
RETCODE = 99999  Real Time Report Success

108 bytes from 192.168.0.2: icmp_seq=5 ttl=255 time=182.130 ms

仍有后续报告输出
---    END

%%NGVNVIFPING: VNINSTANCE="a0000001-460-01-01", DSTIPV4ADDR="192.168.0.2";%%
RETCODE = 0  操作成功

--- 192.168.0.2 ping statistics ---
5 packet(s) transmitted
5 packet(s) received
0% packet loss
round-trip min/avg/max = 103.560/249.569/733.068 ms

共有16个报告
---    END
```