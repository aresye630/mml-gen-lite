# NGTRACEROUTE（NGTRACEROUTE）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

该命令用来在网络连接中测试数据包从发送主机到目的地所经过的网关。对于网络中出现的故障，可以先执行**NGPING**命令，根据回应的报文查看网络连通的情况，然后使用该命令查看网络中出现故障的位置，为故障诊断提供依据。

## 注意事项

该命令执行后立即生效。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

| 参数标识        | 参数名称     | 参数说明                                                                                                     |
|:------------|:---------|:---------------------------------------------------------------------------------------------------------|
| IPTYPE      | IP类型     | 可选必选说明：可选参数  参数含义：该参数用于描述IP地址类型。  数据来源：全网规划 取值范围： IPv4（IPv4）IPv6（IPv6）  默认值：无  配置原则：无                    |
| VPNNAME     | VPN实例名称  | 可选必选说明：可选参数  参数含义：该参数用于指定VPN实例名。  数据来源：全网规划  取值范围：字符串类型，输入长度范围是1~31。  默认值：_public_  配置原则：无               |
| SRCIPV4ADDR | 源IPv4地址  | 可选必选说明：该参数在"IPTYPE"配置为"IPv4"时为条件必选参数。  参数含义：该参数用于指定源IPv4地址。  数据来源：全网规划  取值范围：IPv4地址类型。  默认值：无  配置原则：无    |
| DSTIPV4ADDR | 目的IPv4地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPv4"时为条件必选参数。  参数含义：该参数用于指定目的主机IPv4地址。  数据来源：全网规划  取值范围：IPv4地址类型。  默认值：无  配置原则：无 |
| SRCIPV6ADDR | 源IPv6地址  | 可选必选说明：该参数在"IPTYPE"配置为"IPv6"时为条件必选参数。  参数含义：该参数用于指定源IPv6地址。  数据来源：全网规划  取值范围：IPv6地址类型。  默认值：无  配置原则：无    |
| DSTIPV6ADDR | IPv6目的地址 | 可选必选说明：该参数在"IPTYPE"配置为"IPv6"时为条件必选参数。  参数含义：该参数用于指定目的主机IPv6地址。  数据来源：全网规划  取值范围：IPv6地址类型。  默认值：无  配置原则：无 |
| DSTPORT     | 目的端口号    | 可选必选说明：可选参数  参数含义：该参数用于指定目的主机的UDP端口号。当前不支持该参数。  数据来源：全网规划  取值范围：整数类型，取值范围是1~65535。  默认值：33333  配置原则：无    |
| TIMEOUT     | 超时时间(ms) | 可选必选说明：可选参数  参数含义：该参数用于指定等待响应报文的超时时间。  数据来源：全网规划  取值范围：整数类型，取值范围是1~65535。  默认值：5000  配置原则：无              |
| FIRSTTTL    | 初始TTL    | 可选必选说明：可选参数  参数含义：该参数用于指定初始TTL。  数据来源：全网规划  取值范围：整数类型，取值范围是1~255。  默认值：1  配置原则：无                         |
| MAXTTL      | 最大TTL    | 可选必选说明：可选参数  参数含义：该参数用于指定最大TTL。  数据来源：全网规划  取值范围：整数类型，取值范围是1~255。  默认值：30  配置原则：无                        |
| PACKETNUM   | 发包数      | 可选必选说明：可选参数  参数含义：该参数用于指定每次发送的探测数据包个数。  数据来源：全网规划  取值范围：整数类型，取值范围是1~65535。  默认值：3  配置原则：无                |
| PACKETSIZE  | 报文大小     | 可选必选说明：可选参数  参数含义：该参数用于指定报文大小。  数据来源：全网规划  取值范围：整数类型，取值范围是20~9600。  默认值：80  配置原则：无                       |

## 使用实例

- 目的地址可达情景，检查从发送主机到IP地址为fc00:135:189:242:0:0:0:181的主机所经过的网关。

  ```
  NGTRACEROUTE: IPTYPE=IPv6, SRCIPV6ADDR="fc00:135:193:135:0:0:0:108", DSTIPV6ADDR="fc00:135:189:242:0:0:0:181", PACKETNUM=1; 

  %%NGTRACEROUTE: IPTYPE=IPv6, SRCIPV6ADDR="fc00:135:193:135:0:0:0:108", DSTIPV6ADDR="fc00:135:189:242:0:0:0:181", PACKETNUM=1;%%
  RETCODE = 99999  Real Time Report Success

  1  fc00:135:193:136::254 27.453ms 

  仍有后续报告输出
  ---    END

  %%NGTRACEROUTE: IPTYPE=IPv6, SRCIPV6ADDR="fc00:135:193:135:0:0:0:108", DSTIPV6ADDR="fc00:135:189:242:0:0:0:181", PACKETNUM=1;%%
  RETCODE = 99999  Real Time Report Success

  2  fc00:135:189:242:0:0:0:181 8.629ms

  仍有后续报告输出
  ---    END

  %%NGTRACEROUTE: IPTYPE=IPv6, SRCIPV6ADDR="fc00:135:193:135:0:0:0:108", DSTIPV6ADDR="fc00:135:189:242:0:0:0:181", PACKETNUM=1;%%
  RETCODE = 0  操作成功

  Trace Completed
  Total Receive :2
  round-trip min/avg/max=8.629/18.041/27.453ms

  共有3个报告
  ---    END
  ```
- 目的地址不可达情景，检查从发送主机到IP地址为fc00:18:0:0:0:0:132:140的主机所经过的网关。

  ```
  NGTRACEROUTE: IPTYPE=IPv6, SRCIPV6ADDR="fc00:0:0:0:0:0:0:2", DSTIPV6ADDR="fc00:18:0:0:0:0:132:140", MAXTTL=3, PACKETNUM=1;

  %%NGTRACEROUTE: IPTYPE=IPv6, SRCIPV6ADDR="fc00:0:0:0:0:0:0:2", DSTIPV6ADDR="fc00:18:0:0:0:0:132:140", MAXTTL=3, PACKETNUM=1;%%
  RETCODE = 99999  Real Time Report Success

  1  * 

  仍有后续报告输出
  ---    END

  %%NGTRACEROUTE: IPTYPE=IPv6, SRCIPV6ADDR="fc00:0:0:0:0:0:0:2", DSTIPV6ADDR="fc00:18:0:0:0:0:132:140", MAXTTL=3, PACKETNUM=1;%%
  RETCODE = 99999  Real Time Report Success

  2  * 

  仍有后续报告输出
  ---    END

  %%NGTRACEROUTE: IPTYPE=IPv6, SRCIPV6ADDR="fc00:0:0:0:0:0:0:2", DSTIPV6ADDR="fc00:18:0:0:0:0:132:140", MAXTTL=3, PACKETNUM=1;%%
  RETCODE = 0  操作成功

  Trace Completed
  Total Receive :0
  round-trip min/avg/max=0.000/0.000/0.000ms

  共有3个报告
  ---    END
  ```