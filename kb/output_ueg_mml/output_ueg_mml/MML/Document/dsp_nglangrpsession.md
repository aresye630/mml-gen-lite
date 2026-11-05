# 显示5G LAN组会话上下文（DSP NGLANGRPSESSION）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：UPF**

用来查看指定5G LAN组会话上下文信息。

#### 注意事项

此命令包含个人数据，传出客户网络需要使用匿名化工具进行匿名化处理。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识          | 参数名称            | 参数说明                                                                                                                                                                                                                                                                                                                           |
|:--------------|:----------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| VNINSTANCE    | 5G LAN 组名称      | 可选必选说明：必选参数 参数含义：表示5G LAN组会话实例信息。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为18～37。VNINSTANCE以连字号分为4段，形式为GroupServiceID-MCC-MNC-LocalGroupID。其中，GroupServiceID长度为8，只能输入数字或者范围为A到F或a-f的字母；MCC长度为3，只能输入数字；MNC长度为2~3，只能输入数字；LocalGroupID长度为2~20的偶数，只能输入数字或者范围为A到F或a-f的字母。例如，A0000001-460-003-01，A0000001-460-003-A000000001。不区分大小写。 默认值：无 配置原则：无 |
| CPNODEIDSW    | Node ID开关       | 可选必选说明：可选参数 参数含义：该参数用于指定是否基于Node ID查询5G LAN组会话。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不使能。ENABLE：使能。 默认值：无 配置原则：无                                                                                                                                                                                                                       |
| CPNODEIDTYPE  | Node ID类型       | 可选必选说明：条件必选参数 前提条件：该参数在“CPNODEIDSW”配置为“ENABLE”时为必选参数。 参数含义：该参数用来指定Node ID 类型。 数据来源：全网规划 取值范围：枚举类型。 IPv4：表示Node ID类型为IPv4地址。IPv6：表示Node ID类型为IPv6地址。FQDN：表示Node ID类型为FQDN。 默认值：无 配置原则：无                                                                                                                                         |
| CPNODEIDIPV4  | Node ID中的IPv4地址 | 可选必选说明：条件必选参数 前提条件：该参数在“CPNODEIDTYPE”配置为“IPv4”时为必选参数。 参数含义：该参数用于指定，在根据Node ID查询CP信息时，Node ID中的IPv4地址。 数据来源：全网规划 取值范围：IPv4地址类型。 默认值：无 配置原则：无                                                                                                                                                                                    |
| CPNODEIDIPV6  | Node ID中的IPv6地址 | 可选必选说明：条件必选参数 前提条件：该参数在“CPNODEIDTYPE”配置为“IPv6”时为必选参数。 参数含义：该参数用于指定，在根据Node ID查询CP信息时，Node ID中的IPv6地址。 数据来源：全网规划 取值范围：IPv6地址类型。 默认值：无 配置原则：无                                                                                                                                                                                    |
| CPNODEFQDN    | Node ID的FQDN    | 可选必选说明：条件必选参数 前提条件：该参数在“CPNODEIDTYPE”配置为“FQDN”时为必选参数。 参数含义：该参数用于指定，在根据NODE ID查询CP信息时，Node ID中的FQDN。 数据来源：全网规划 取值范围：字符串类型，输入长度范围为1～255。不支持空格，必须是可见ASCII码，不区分大小写。 默认值：无 配置原则：无                                                                                                                                                   |
| IMSI          | IMSI            | 可选必选说明：可选参数 参数含义：5G LAN用户的IMSI。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～15。每个字符必须为0~9的数字。 IMSI由三部分组成： 1、Mobile Country Code (MCC)包含3个数字。MCC唯一标识移动用户的居住国家。 2、Mobile Network Code (MNC)包含2个或3个数字用于GSM/UMTS应用。MNC标识移动用户的归属PLMN。MNC的长度取决于MCC的值。 3、Mobile Subscriber Identification Number (MSIN)标识PLMN内的移动用户。 默认值：无 配置原则：无                   |
| IGMPGRPDISSW  | IGMP组播组信息显示开关   | 可选必选说明：可选参数 参数含义：该参数用于配置是否显示5G LAN组内的IGMP组播组信息。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不使能。ENABLE：使能。 默认值：无 配置原则：无                                                                                                                                                                                                                       |
| N6MACDISSW    | N6侧MAC地址显示开关    | 可选必选说明：可选参数 参数含义：该参数用于配置是否显示5G LAN组内从N6侧学习到的MAC地址信息。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不使能。ENABLE：使能。 默认值：无 配置原则：无                                                                                                                                                                                                                  |
| VTEPNAME      | VTEP名称          | 可选必选说明：条件可选参数 前提条件：该参数在“N6MACDISSW”配置为“ENABLE”时为可选参数。 参数含义：该参数用于配置VXLAN隧道端点名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。不区分大小写，不支持空格。 默认值：无 配置原则：该参数使用 ADD VTEP命令配置生成。                                                                                                                                                                 |
| DFSRPAIRDISSW | 双发选收结对信息显示开关    | 可选必选说明：可选参数 参数含义：双发选收结对信息显示开关。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不使能。ENABLE：使能。 默认值：无 配置原则：无                                                                                                                                                                                                                                        |
| DFSRPAIRID    | 双发选收结对ID        | 可选必选说明：条件可选参数 前提条件：该参数在“DFSRPAIRDISSW”配置为“ENABLE”时为可选参数。 参数含义：双发选收结对ID。 数据来源：本端规划 取值范围：整数类型，取值范围1-2048。 默认值：无 配置原则：无                                                                                                                                                                                                           |

#### 使用实例

查询用户上下文：

```
DSP NGLANGRPSESSION: VNINSTANCE="a0000001-460-003-a123456789b987654321", IGMPGRPDISSW=ENABLE, N6MACDISSW=ENABLE, VTEPNAME="vtep", DFSRPAIRDISSW=ENABLE, DFSRPAIRID=1;
```

```
RETCODE = 0 操作成功

上下文信息
------------
Result  =  
PDP context on Pod: ssgpod-0
-------------------------------
                             IMSI  =  NULL
                             IMEI  =  NULL
                           MSISDN  =  NULL
                       Local Seid  =  0x0000000064000003
                        Peer Seid  =  0x000000000000000b
                  Local Signal IP  =  10.2.176.131
                   Peer Signal IP  =  10.70.176.15
                IPv4 VPN instance  =  NULL
                IPv6 VPN instance  =  NULL
                              APN  =  038apn1.com
                         PDP Type  =  ETH
                         RAT Type  =  NR
                        Role Type  =  UPF
                        User Type  =  home
                        DNAI Flag  =  false
                    DNAI VPN Flag  =  false
                        DCNR Flag  =  false
                  Maintained Flag  =  false
     Session Activation Timestamp  =  19:49:57 06/25/2023(MM/DD/YYYY)
                        Af Switch  =  DISABLE
           Ipv6InterfaceId Switch  =  DISABLE
                        L2TP Flag  =  false
    CU Configuration Inconsistent  =  false
          5G LAN GROUP VNINSTANCE  =  a0000001-460-003-a123456789b987654321
         High-Bandwidth User Flag  =  false
                        CP NodeID  =  smf1
                         UAC Flag  =  false
                         NAT Flag  =  false
                 Tethering Switch  =  DISABLE
           Content Filtering Flag  =  false

PDR Information
----------------
No  State     Priority    PDR ID  Src Intf        PDR TYPE      IMS   Classifier  TEIDU       QFI                 Bearer  QER               FAR         APP URR     IDLE URR    Usage URR      MULTIIDX  MULTIDNN              SNSSAI      RAT   Filter Indication   MULTIDNN URR
1   Active    1           1       5g-vn-internal  Dynamic       0     Disable     -           -                   255     -                 1           -           -           -              -         -                     -           -     -                   -              
2   Active    1           2       core            Dynamic       0     Disable     -           -                   255     -                 2           -           -           -              -         -                     -           -     -                   -              
PDI Information
----------------
PDR ID        Src Intf      Intf Type           TEIDU          Local Intf IPv4     Local Intf IPv6                                   QFI                 APP ID        Linked TEP    VPN Name      Filter ID   Filter Desc
1             5g-vn-internal  -                   -              -                   -                                                 -                   -             -             -             924738904   -
2             core          N6(-)               -              -                   -                                                 -                   -             -             -             924738904   -
FAR Information
----------------
FAR ID      Apply Action    Dst Intf        Intf Type   Peer Teidu  Peer Data IPv4      Peer Data IPv6                                  Src Port    Dst Port    Redirect  BAR ID  Classifier To Local    Unicast Para Num   Unicast Para DDF Num
1           FORW            core            N6(-)       -           -                   -                                               -           -           -         -       Disable                0                  -
2           FORW            5g-vn-internal  -           -           -                   -                                               -           -           -         -       Disable                0                  -
FAR Extra Information
----------------
FAR ID      Redirect Address                                Tos Value   Tos Mask    Linked TEP ID
1           -                                               -           -           -
2           -                                               -           -           -

                               UE  =  3045******2348
                      Mac Address  =  82-BB-CC-DD-EE-FF

                               UE  =  3045******2362
                      Mac Address  =  80-BB-CC-DD-EE-FF

                               UE  =  3045******2359

            IGMP Group IP Address  =  224.0.0.1
                               UE  =  3045******2362
                               UE  =  3045******2348

                        VTEP Name  =  vtep
                      Mac Address  =  F0-F2-F3-F4-F5-F6 

                      DFSR PAIR ID =  1
                               UE  =  3045******2359
                      Mac Address  =  F0-F2-F3-F4-F5-F6 
(Number of results = 1)

---    END
```

#### 输出结果说明

| 输出项名称                         | 输出项解释                                                                                                |
|:------------------------------|:-----------------------------------------------------------------------------------------------------|
| IMSI                          | 国际移动用户标识，当用户接入不携带IMSI时，显示为“NULL”。                                                                    |
| IMEI                          | 国际移动设备标识，当用户接入不携带IMEI时，显示为“NULL”。                                                                    |
| MSISDN                        | 用户的MSISDN号。                                                                                          |
| Local Seid                    | 本端分配的Session Endpoint Identifier。                                                                    |
| Peer Seid                     | 对端分配的Session Endpoint Identifier。                                                                    |
| Local Signal IP               | 本端信令地址。                                                                                              |
| Peer Signal IP                | 对端信令地址。                                                                                              |
| IPv4 VPN instance             | IPv4 VPN实例。                                                                                          |
| IPv6 VPN instance             | IPv6 VPN实例。                                                                                          |
| APN                           | APN名称。                                                                                               |
| PDP type                      | PDP上下文类型。                                                                                            |
| RAT Type                      | RAT类型。                                                                                               |
| Role Type                     | 形态类型：GGSN形态、SGW形态、PGW形态、SPGW形态、UPF形态。                                                                |
| User Type                     | 用户接入类型：归属用户、拜访用户、漫游用户。                                                                               |
| DNAI Flag                     | true表示该激活消息携带了DNAI信元，false表示没有携带DNAI信元。                                                              |
| DNAI VPN Flag                 | DNAI VPN标识。                                                                                          |
| DCNR Flag                     | true表示终端具备5G接入能力，false表示终端不具备5G接入能力。                                                                 |
| Maintained Flag               | 承载保留标识。                                                                                              |
| Session Activation Timestamp  | 会话的在线时长。                                                                                             |
| Af Switch                     | ADC标识。                                                                                               |
| Ipv6InterfaceId Switch        | 是否用IMSI替换ipv6地址后64位开关。                                                                               |
| L2TP Flag                     | L2TP标识。                                                                                              |
| CU Configuration Inconsistent | CU配置不一致标识。                                                                                           |
| 5G LAN GROUP VNINSTANCE       | 5G LAN组服务实例ID。                                                                                       |
| High-Bandwidth User Flag      | 高带宽用户标识。                                                                                             |
| CP NodeID                     | CP的节点ID。                                                                                             |
| UAC Flag                      | 单网通用用户标识。                                                                                            |
| NAT Flag                      | NAT标识。                                                                                               |
| Tethering Switch              | Tethering标识。                                                                                         |
| Content Filtering Flag        | 当license LKV3G5UFBF01剩余资源可用，用户apn对应的APNCFFUNC配置CFSWITCHVALUE为ENABLE且用户绑定了cf profile的数量不为0时，此标记为TRUE。 |
| PDR Information               | PDR相关信息。                                                                                             |
| PDI Information               | PDI相关信息。                                                                                             |
| FAR Information               | FAR相关信息。                                                                                             |
| FAR Extra Information         | FAR扩展信息，包括5G LAN组会话下保存的UE、MAC地址、动态组播组、VTEP、双发选收结对等信息。                                                |