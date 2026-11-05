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

- 每种异常攻击报文每个POD最多显示10个用户，每个用户最多显示5条记录。
- 每个POD最多显示5个DNS服务器信息记录，每个服务器最多显示5个用户，每个用户最多显示5条业务流。
- 每个POD每个APN最多显示3个单通用户，不指定APN时最多显示30个用户。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识        | 参数名称       | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|:------------|:-----------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SCENE       | 异常用户场景     | 可选必选说明：必选参数 参数含义：异常用户场景。 数据来源：本端规划 取值范围： DATAFWD：数据转发异常用户场景。 默认值：无 配置原则：无                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| DATAFWD     | 数据转发异常用户场景 | 可选必选说明：条件必选参数 前提条件：该参数在“SCENE”配置为“DATAFWD”时为必选参数。 参数含义：数据转发异常用户场景。 数据来源：本端规划 取值范围： ABNPKTATT：异常报文攻击用户。ABNDNS：异常DNS访问用户。SGLPASS：单通用户。TOPDROP：TOP丢包用户。 默认值：无 配置原则：无                                                                                                                                                                                                                                                                                                                                                      |
| MESSAGETYPE | 异常报文类型     | 可选必选说明：条件必选参数 前提条件：该参数在“DATAFWD”配置为“ABNPKTATT”时为必选参数。 参数含义：异常报文类型。 数据来源：本端规划 取值范围： IPHDR：IP类型非v4或v6。UDPHDR：用户UDP协议的IPv4报文实际的长度小于(IPv4头长度+UDP头长度)。TCPHDR：用户TCP协议的IPv4报文实际的长度小于(IPv4头长度+TCP头长度)。IPLEN：报文长度（从IP头开始计算）小于IP头中的total length的值。DSTIP：上行目的地址非法(地址是0/环回)。ANTISPOOFING：报文anti-spoofing检查不过丢包。CHECKSUM：报文checksum检查错误丢包。TTL：上行用户IPv4/IPv6报文TTL小于等于1。V6EXTHDRLEN：IPv6报文的扩展头错误。EXCPFRAG：用户分片报文过多，分片资源耗尽丢包。DDOS：上行IPv4或者IPv6报文DDOS攻击丢包。FLOODATT：上行或者下行大流量攻击丢包。MUTICAST：上行目的地址为组播广播。FRAGMNODE：分片母节点耗尽丢包。 默认值：无 配置原则：无 |
| DNSIPTYPE   | 异常DNS地址类型  | 可选必选说明：条件可选参数 前提条件：该参数在“DATAFWD”配置为“ABNDNS”时为可选参数。 参数含义：异常DNS地址类型。 数据来源：本端规划 取值范围： IPv4：表示地址类型为IPv4。IPv6：表示地址类型为IPv6。 默认值：无 配置原则：无                                                                                                                                                                                                                                                                                                                                                                                     |
| DNSIPV4     | DNSIPV4地址  | 可选必选说明：条件必选参数 前提条件：该参数在“DNSIPTYPE”配置为“IPv4”时为必选参数。 参数含义：DNSIPV4地址。 数据来源：本端规划 取值范围：NA。 默认值：无 配置原则：无                                                                                                                                                                                                                                                                                                                                                                                                                     |
| DNSIPV6     | DNSIPV6地址  | 可选必选说明：条件必选参数 前提条件：该参数在“DNSIPTYPE”配置为“IPv6”时为必选参数。 参数含义：DNSIPV6地址。 数据来源：本端规划 取值范围：NA。 默认值：无 配置原则：无                                                                                                                                                                                                                                                                                                                                                                                                                     |
| APN         | APN名称      | 可选必选说明：条件可选参数 前提条件：该参数在“DATAFWD”配置为“SGLPASS”时为可选参数。 参数含义：APN名称。 数据来源：本端规划 取值范围：NA。 默认值：无 配置原则：无                                                                                                                                                                                                                                                                                                                                                                                                                        |
| PODNM       | POD名称      | 可选必选说明：条件可选参数 前提条件：该参数在“DATAFWD”配置为“TOPDROP”时为可选参数。 参数含义：查询指定pod的统计结果。 数据来源：本端规划 取值范围：NA。 默认值：无 配置原则：如果不输入该参数，则查询所有ssg pod的统计结果。                                                                                                                                                                                                                                                                                                                                                                                       |
| TOPNUM      | TOP数       | 可选必选说明：条件可选参数 前提条件：该参数在“DATAFWD”配置为“TOPDROP”时为可选参数。 参数含义：查询的top用户数。 数据来源：本端规划 取值范围：整数类型，取值范围为0～20。 默认值：无 配置原则：如果不输入该参数，则查询TOP 20的用户丢包统计结果。                                                                                                                                                                                                                                                                                                                                                                             |
| PERITYPE    | 周期类型       | 可选必选说明：条件可选参数 前提条件：该参数在“DATAFWD”配置为“TOPDROP”时为可选参数。 参数含义：查询周期时间范围内的用户丢包信息。 数据来源：本端规划 取值范围： LONG_PERIOD：查询长周期。SHORT_PERIOD：查询短周期。 默认值：无 配置原则：如果不输入该参数，则查询的周期类型为短周期。                                                                                                                                                                                                                                                                                                                                                     |
| LONGPERI    | 长周期        | 可选必选说明：条件可选参数 前提条件：该参数在“PERITYPE”配置为“LONG_PERIOD”时为可选参数。 参数含义：查询当前时间之前的第几个小时的用户丢包信息。 数据来源：本端规划 取值范围：整数类型，取值范围为0～23，单位是小时。 默认值：无 配置原则：如果不输入该参数，则查询当前一小时的统计结果。                                                                                                                                                                                                                                                                                                                                                           |
| SHORTPERI   | 短周期        | 可选必选说明：条件可选参数 前提条件：该参数在“PERITYPE”配置为“SHORT_PERIOD”时为可选参数。 参数含义：查询当前或上一个TOP丢包统计周期的用户丢包信息，TOP丢包统计周期由SET TOPDROPPARA命令配置。 数据来源：本端规划 取值范围：整数类型，取值范围为0～1，单位是分钟。 默认值：无 配置原则：0表示当前TOP丢包统计周期，1表示上一个TOP丢包统计周期。如果不输入该参数，则查询当前TOP丢包统计周期的统计结果。                                                                                                                                                                                                                                                                                     |

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
- 查询单通用户信息：

  ```
  DSP EXEPSESSINFO: SCENE=DATAFWD, DATAFWD=SGLPASS, APN="063apn1.com";
  ```

  ```
  %%DSP EXEPSESSINFO: SCENE=DATAFWD, DATAFWD=SGLPASS, APN="063apn1.com";%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  Abnormal user information  =  
  APN                                                             PODNAME                                                         IMSI                MSISDN              UEIPV4                                  UEIPV6                                  
  063apn1.com                                                     ssgpod-0                                                        10000000000001      12341236            10.97.91.0                              NULL                                       
  (结果个数 = 1)

  ---    END
  ```

#### 输出结果说明

| 输出项名称        | 输出项解释             |
|:-------------|:------------------|
| 异常用户信息       | 异常用户信息。           |
| sceneID(7)   | PDR匹配行为丢包。        |
| sceneID(16)  | IP版本不对。           |
| sceneID(64)  | 防欺诈：上行IPv4欺诈报文丢弃。 |
| sceneID(65)  | 防欺诈：上行IPv6欺诈报文丢弃。 |
| sceneID(66)  | 防欺诈：下行IPv4欺诈报文丢弃。 |
| sceneID(67)  | 防欺诈：下行IPv6欺诈报文丢弃。 |
| sceneID(80)  | 报文IP版本非法。         |
| sceneID(86)  | 上行流量监管丢包。         |
| sceneID(87)  | 下行流量监管丢包。         |
| sceneID(92)  | 流量监管丢包。           |
| sceneID(93)  | 流量整型丢包。           |
| sceneID(193) | PCC规则匹配失败丢包。      |
| sceneID(其他值) | 请联系华为技术支持。        |