# 显示异常用户（DSP EXEPSESSINFO）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：UPF、PGW-U、SGW-U**

该命令通过查询异常用户，来获取异常用户的信息。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识        | 参数名称       | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|:------------|:-----------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SCENE       | 异常用户场景     | 可选必选说明：必选参数 参数含义：异常用户场景。 数据来源：本端规划 取值范围： DATAFWD：数据转发异常用户场景。 默认值：无 配置原则：无                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| DATAFWD     | 数据转发异常用户场景 | 可选必选说明：条件必选参数 前提条件：该参数在“SCENE”配置为“DATAFWD”时为必选参数。 参数含义：数据转发异常用户场景。 数据来源：本端规划 取值范围： ABNPKTATT：异常报文攻击用户。ABNDNS：异常DNS访问用户。 默认值：无 配置原则：无                                                                                                                                                                                                                                                                                                                                                                                   |
| MESSAGETYPE | 异常报文类型     | 可选必选说明：条件必选参数 前提条件：该参数在“DATAFWD”配置为“ABNPKTATT”时为必选参数。 参数含义：异常报文类型。 数据来源：本端规划 取值范围： IPHDR：IP类型非v4或v6。UDPHDR：用户UDP协议的IPv4报文实际的长度小于(IPv4头长度+UDP头长度)。TCPHDR：用户TCP协议的IPv4报文实际的长度小于(IPv4头长度+TCP头长度)。IPLEN：报文长度（从IP头开始计算）小于IP头中的total length的值。DSTIP：上行目的地址非法(地址是0/环回)。ANTISPOOFING：报文anti-spoofing检查不过丢包。CHECKSUM：报文checksum检查错误丢包。TTL：上行用户IPv4/IPv6报文TTL小于等于1。V6EXTHDRLEN：IPv6报文的扩展头错误。EXCPFRAG：用户分片报文过多，分片资源耗尽丢包。DDOS：上行IPv4或者IPv6报文DDOS攻击丢包。FLOODATT：上行或者下行大流量攻击丢包。MUTICAST：上行目的地址为组播广播。FRAGMNODE：分片母节点耗尽丢包。 默认值：无 配置原则：无 |
| DNSIPTYPE   | 异常DNS地址类型  | 可选必选说明：条件可选参数 前提条件：该参数在“DATAFWD”配置为“ABNDNS”时为可选参数。 参数含义：异常DNS地址类型。 数据来源：本端规划 取值范围： IPv4：表示地址类型为IPv4。IPv6：表示地址类型为IPv6。 默认值：无 配置原则：无                                                                                                                                                                                                                                                                                                                                                                                     |
| DNSIPV4     | DNSIPV4地址  | 可选必选说明：条件必选参数 前提条件：该参数在“DNSIPTYPE”配置为“IPv4”时为必选参数。 参数含义：DNSIPV4地址。 数据来源：本端规划 取值范围：NA。 默认值：无 配置原则：无                                                                                                                                                                                                                                                                                                                                                                                                                     |
| DNSIPV6     | DNSIPV6地址  | 可选必选说明：条件必选参数 前提条件：该参数在“DNSIPTYPE”配置为“IPv6”时为必选参数。 参数含义：DNSIPV6地址。 数据来源：本端规划 取值范围：NA。 默认值：无 配置原则：无                                                                                                                                                                                                                                                                                                                                                                                                                     |

#### 使用实例

- 查询DDOS异常攻击报文用户的信息：

  ```
  DSP EXEPSESSINFO: SCENE=DATAFWD, DATAFWD=ABNPKTATT, MESSAGETYPE=DDOS;
  ```

  ```
  %%DSP EXEPSESSINFO: SCENE=DATAFWD, DATAFWD=ABNPKTATT, MESSAGETYPE=IPHDR;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  Abnormal user information  =  
  ATT reason = The IP header of the packet is incorrect
  Record user number = 0
  PodName = ssgpod-0
  (结果个数 = 1)

  ---    END
  ```
- 查询异常DNS访问用户的信息：

  ```
  DSP EXEPSESSINFO: SCENE=DATAFWD, DATAFWD=ABNDNS;
  ```

  ```
  %%DSP EXEPSESSINFO: SCENE=DATAFWD, DATAFWD=ABNDNS;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  Abnormal user information  =  
  PodName = ssgpod-0
  	DnsIpAddr[10.1.2.3]
  	    imsi(26456789012342):
  	        msIp[10.1.2.4],severIp[10.1.2.3],msPort[22222],serverPort[53],l4Protocol[17],upDnsNum[22],downDnsNum[10]

  (结果个数 = 1)

  ---    END
  ```

#### 输出结果说明

| 输出项名称   | 输出项解释   |
|:--------|:--------|
| 异常用户信息  | 异常用户信息。 |