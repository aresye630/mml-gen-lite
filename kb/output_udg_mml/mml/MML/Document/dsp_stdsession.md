# 显示用户上下文（DSP STDSESSION）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：SGW-U、PGW-U、UPF**

用来查看指定用户上下文信息。

#### 注意事项

根据IMEI查询用户只匹配前14位。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识      | 参数名称         | 参数说明                                                                                                                                                                                                                                                                                                                                            |
|:----------|:-------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| QUERYTYPE | 查询方式         | 可选必选说明：必选参数 参数含义：查询方式。 数据来源：本端规划 取值范围：枚举类型。 IMSI：指定待查询用户的IMSI号。MSISDN：指定待查询用户的MSISDN号。IMEI：指定待查询用户的IMEI号。 默认值：无 配置原则：无                                                                                                                                                                                                                          |
| IMSI      | 用户的IMSI信息。   | 可选必选说明：条件必选参数 前提条件：该参数在“QUERYTYPE”配置为“IMSI”时为必选参数。 参数含义：用户的IMSI信息。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～15。每个字符必须为0~9的数字。 IMSI由三部分组成： 1、Mobile Country Code (MCC)包含3个数字。MCC唯一标识移动用户的居住国家。 2、Mobile Network Code (MNC)包含2个或3个数字用于GSM/UMTS应用。MNC标识移动用户的归属PLMN。MNC的长度取决于MCC的值。 3、Mobile Subscriber Identification Number (MSIN)标识PLMN内的移动用户。 默认值：无 配置原则：无 |
| IMEI      | 用户的IMEI信息。   | 可选必选说明：条件必选参数 前提条件：该参数在“QUERYTYPE”配置为“IMEI”时为必选参数。 参数含义：用户的IMEI信息。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～16。每个字符必须为0~9的数字。 IMEI号的组成： 1、前6位或者8位是型号核准码(TAC)，用来区分手机品牌和型号。 2、接着2位是最后装配号(FAC)，代表最终装配地代码，仅在早期机型中存在。 3、后6位是串号(SNR)，代表生成顺序号。 默认值：无 配置原则：无                                                                                                       |
| MSISDN    | 用户的MSISDN信息。 | 可选必选说明：条件必选参数 前提条件：该参数在“QUERYTYPE”配置为“MSISDN”时为必选参数。 参数含义：用户的MSISDN信息。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～15。每个字符必须为0~9的数字。 MSISDN号的组成： 1、用户注册的国家的Country Code (CC) 2、国家移动号，组成如下：National Destination Code (NDC)；Subscriber Number (SN)。 默认值：无 配置原则：无                                                                                                |

#### 使用实例

查询用户上下文，MSISDN为“85362641010”：

```
DSP STDSESSION: QUERYTYPE=MSISDN,MSISDN="85362641010";
```

```
RETCODE = 0  操作成功

上下文信息
------------

                    Pod Name  =  ssgpod-0
                        IMSI  =  60456789012342
                        IMEI  =  123456789012371
                      MSISDN  =  12341234
                  Local Seid  =  0x00000000008003f1
                   Peer Seid  =  0x0000000000000001
             Local Signal IP  =  172.16.24.91
              Peer Signal IP  =  192.168.31.24
           IPv4 VPN Instance  =  NULL
           IPv6 VPN Instance  =  NULL
                         APN  =  060apn1.com
            Virtual APN Name  =  NULL
                    PDP Type  =  IPv4
           IPv4 Address Type  =  EXTERNAL ALLOC IP ADDRESS
            IPv4 PDP Address  =  10.165.2.96
           IPv6 Address Type  =  NULL
            IPv6 PDP Address  =  NULL
        IPv4 Redundancy Flag  =  false
        IPv6 Redundancy Flag  =  NULL
          IPv4 Conflict Flag  =  NULL
          IPv6 Conflict Flag  =  NULL
            Delegated Prefix  =  NULL
                    RAT Type  =  NR
                   Role Type  =  UPF
                   User Type  =  home
                   DCNR Flag  =  false
  Overload QoS Control Level  =  NULL
               DNAI VPN Flag  =  false
Session Activation Timestamp  =  22:22:39 11/12/2024(MM/DD/YYYY)
                   DNAI Flag  =  false
   User Location Information  =  NULL
          Common Policy Name  =  NULL
                   L2TP Flag  =  false
                   CP NodeID  =  0.0.0.0
                      SNSSAI  =  NULL
       MultiDnn Session Type  =  NULL
            Tethering Switch  =  DISABLE
                    NAT Flag  =  false
(结果个数 = 1)

---    END
```

#### 输出结果说明

| 输出项名称                                   | 输出项解释                                   |
|:----------------------------------------|:----------------------------------------|
| Pod名称                                   | Pod名称。                                  |
| 用户的IMSI信息。                              | 用户的IMSI信息。                              |
| 用户的IMEI信息。                              | 用户的IMEI信息。                              |
| 用户的MSISDN信息。                            | 用户的MSISDN信息。                            |
| 本端分配的Session Endpoint Identifier        | 本端分配的Session Endpoint Identifier。       |
| 对端分配的Session Endpoint Identifier        | 对端分配的Session Endpoint Identifier。       |
| 本端信令地址                                  | 本端信令地址。                                 |
| 对端信令地址                                  | 对端信令地址。                                 |
| IPv4 VPN实例。                             | IPv4 VPN实例。                             |
| IPv6 VPN实例。                             | IPv6 VPN实例。                             |
| APN名称。                                  | APN名称。                                  |
| 虚拟APN名称。                                | 虚拟APN名称。                                |
| PDP上下文类型。                               | PDP上下文类型。                               |
| IPv4用户地址分配方式。                           | IPv4用户地址分配方式。                           |
| 用户IPv4地址。                               | 用户IPv4地址。                               |
| IPv6用户地址分配方式。                           | IPv6用户地址分配方式。                           |
| 用户IPv6地址。                               | 用户IPv6地址。                               |
| IPv4用户地址路由冗余标记。                         | IPv4用户地址路由冗余标记。                         |
| IPv6用户地址路由冗余标记。                         | IPv6用户地址路由冗余标记。                         |
| IPv4用户地址冲突标记。                           | IPV4CONFFLAG。                           |
| IPv6用户地址冲突标记。                           | IPV6CONFFLAG。                           |
| IPv6 Conflict Flag                      | IPv6 Conflict Flag。                     |
| RAT类型。                                  | RAT类型。                                  |
| 形态类型：GGSN形态、SGW形态、PGW形态、SPGW形态、UPF形态。   | ROLETYPE。                               |
| 用户接入类型：归属用户、拜访用户、漫游用户。                  | 用户接入类型：归属用户、拜访用户、漫游用户。                  |
| true表示终端具备5G接入能力，false表示终端不具备5G接入能力。    | true表示终端具备5G接入能力，false表示终端不具备5G接入能力。    |
| 表示会话受过载限速控制及当前控制等级。                     | 表示会话受过载限速控制及当前控制等级。                     |
| DNAI VPN标识。                             | DNAI VPN标识。                             |
| 会话的在线时长。                                | 会话的在线时长。                                |
| true表示该激活消息携带了DNAI信元，false表示没有携带DNAI信元。 | true表示该激活消息携带了DNAI信元，false表示没有携带DNAI信元。 |
| 用户位置信息。                                 | 用户位置信息。                                 |
| 用户模板名称。                                 | 用户模板名称。                                 |
| L2TP标识。                                 | L2TP标识。                                 |
| CP的节点ID。                                | CP的节点ID。                                |
| 切片信息。                                   | 切片信息。                                   |
| 双DNN用户类型。                               | 双DNN用户类型。                               |
| Tethering标识。                            | Tethering标识。                            |
| NAT标识。                                  | NAT标识。                                  |