# 查询NAT用户会话信息（DSP NATSESSION）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：UPF**

该命令用于查询NAT用户会话信息。

#### 注意事项

该命令执行后立即生效。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识      | 参数名称   | 参数说明                                                                                                                                                                                                                                                                                                                                   |
|:----------|:-------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| QUERYTYPE | 查询类型   | 可选必选说明：必选参数 参数含义：查询类型。 数据来源：本端规划 取值范围：枚举类型。 MSISDN：MSISDN。IMSI：IMSI。IPV4：IPV4。IPV6：IPV6。 默认值：无 配置原则：无                                                                                                                                                                                                                                  |
| MSISDN    | MSISDN | 可选必选说明：条件必选参数 前提条件：该参数在“QUERYTYPE”配置为“MSISDN”时为必选参数。 参数含义：MSISDN。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～15。每个字符必须为0~9的数字。MSISDN号的组成：1、用户注册的国家的Country Code (CC)。2、国家移动号，组成如下：National Destination Code (NDC)；Subscriber Number (SN)。 默认值：无 配置原则：无                                                                                              |
| IMSI      | IMSI   | 可选必选说明：条件必选参数 前提条件：该参数在“QUERYTYPE”配置为“IMSI”时为必选参数。 参数含义：IMSI。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～15。每个字符必须为0~9的数字。IMSI由三部分组成：1、Mobile Country Code (MCC)包含3个数字。MCC唯一标识移动用户的居住国家。2、Mobile Network Code (MNC)包含2个或3个数字用于GSM/UMTS应用。MNC标识移动用户的归属PLMN。MNC的长度取决于MCC的值。3、Mobile Subscriber Identification Number (MSIN)标识PLMN内的移动用户。 默认值：无 配置原则：无 |
| VPNNAME   | VPN名称  | 可选必选说明：条件必选参数 前提条件：该参数在“QUERYTYPE”配置为“IPV4” 或 “IPV6”时为必选参数。 参数含义：VPN名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～31。 默认值：无 配置原则：无                                                                                                                                                                                                                 |
| IPV4      | IPv4地址 | 可选必选说明：条件必选参数 前提条件：该参数在“QUERYTYPE”配置为“IPV4”时为必选参数。 参数含义：IPv4地址。 数据来源：本端规划 取值范围：IPv4地址类型。 默认值：无 配置原则：无                                                                                                                                                                                                                                  |
| IPV6      | IPv6地址 | 可选必选说明：条件必选参数 前提条件：该参数在“QUERYTYPE”配置为“IPV6”时为必选参数。 参数含义：IPv6地址。 数据来源：本端规划 取值范围：IPv6地址类型。 默认值：无 配置原则：无                                                                                                                                                                                                                                  |

#### 使用实例

该命令用于查询指定NAT用户会话信息：

```
DSP NATSESSION: QUERYTYPE=MSISDN, MSISDN="151258745316000";
```

```
RETCODE = 0  Operation Success.

Session Information:
----------------
VPN Instance Name    Source IP Address    Source Port    Source NAT IP Address    Source NAT Port    Destination IP Address    Destination Port    Destination NAT IP Address    Protocol    Direction

SrvVpn               10.2.2.7              2969           10.12.2.7                1858               10.12.1.1                 80                  10.14.1.1                     UDP         DOWNLINK     
SrvVpn               10.2.2.7              2970           10.12.2.7                1859               10.12.1.1                 80                  10.14.1.1                     UDP         DOWNLINK
(Number of results = 2)
---    END
```

#### 输出结果说明

| 输出项名称      | 输出项解释       |
|:-----------|:------------|
| VPN名称      | VPN名称。      |
| 源IP地址      | 源IP地址。      |
| 源端口        | 源端口。        |
| NAT后源IP地址  | NAT后源IP地址。  |
| NAT后源端口    | NAT后源端口。    |
| 目的IP地址     | 目的IP地址。     |
| 目的端口       | 目的端口。       |
| NAT后目的IP地址 | NAT后目的IP地址。 |
| 协议         | 协议。         |
| 方向         | 方向。         |