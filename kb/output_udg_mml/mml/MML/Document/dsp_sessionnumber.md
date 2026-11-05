# 显示会话数（DSP SESSIONNUMBER）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于查询当前在线会话数。如果不输入参数表示显示整机的所有会话数。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识            | 参数名称            | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|:----------------|:----------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DISPLAYMODE     | 显示方式            | 可选必选说明：可选参数 参数含义：该参数用于指定显示方式。 数据来源：本端规划 取值范围：枚举类型。 APN：查询使用该APN激活的当前在线会话数。APN_RELATE：查询使用该别名APN激活的当前在线会话数。ONLINE：查询当前使用在线计费的会话数。在线计费会话是指N4接口下发online-urrid-switch信元值为enable或者N4接口下发在线计费类型URR（Create-URR携带volume-quota/time-quota/event-quota信元）的会话。OFFLINE：查询当前使用离线计费的会话数。离线计费会话是指下发offline-urrid-switch信元为enable或者不下发offline-urrid-switch信元的会话。NON_IP：查询激活的Non-IP用户会话数。NODEID：根据NODEID查询当前在线会话数。NSA：查询当前非独立组网激活的会话数。USERPROFILE：查询当前user profile激活的会话数。ANTIFRAUD：查询防欺诈的会话数。PODNAME：根据PODNAME查询当前在线会话数。L2TP：查询当前L2TP会话数。CU_CONFIGURATION_INCONSISTENCY：查询受CP和UP关键配置不一致影响的在线用户会话数。BWM：查询当前BWM会话数。UPLINKBWLEV：查询上行带宽级别的会话数。N4U_TUNNEL：查询基于N4建立GTPU隧道的设备级会话数。ROAMING：查询当前在线漫游用户数和拜访数。NGLAN：表示查询当前在线的5G LAN组会话和UE会话数。QOS_MONT：查询当前整机内的时延监测实时会话数。RAT：按照接入类型查询会话数。TRUNK：查询宽带集群用户会话数。DNAI：按照DNAI查询会话数。MultiDNN：按照MultiDNN类型查询会话数。HIGHSPEED：查询当前在线的高速用户会话数。MBS：表示查询当前在线的MBS会话数。IPSUIT：按照IPSuit查询会话数。RtsDNN：按照RtsDnn类型查询会话数。DEDICATEDLBO：查询专网UPF分流的独立ULCL会话数。MBMS：表示查询当前在线的MBMS会话数。NETWORKINSTANCE：表示查询当前在线的NETWORKINSTANCE会话数。IMS_BYPASS：查询UPF上IMS惯性运行会话数。QOS_ANA：查询当前提供服务质量分析的会话数。QOS_EXP：查询当前提供服务体验上报的会话数。 默认值：无 配置原则：无 |
| APN             | APN名称           | 可选必选说明：条件必选参数 前提条件：该参数在“DISPLAYMODE”配置为“APN”时为必选参数。 可选必选说明：条件可选参数 前提条件：该参数在“DISPLAYMODE”配置为“UPLINKBWLEV”、“RAT”、“MultiDNN”、“RtsDNN” 或 “DEDICATEDLBO”时为可选参数。 参数含义：该参数用于指定APN实例名。表示查询使用该APN激活的当前在线会话数，该APN必须在系统上已经配置。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。不支持空格及部分特殊字符。可以支持的特殊字符有“.”和“-”，“.”不可以是第一个字符且不可以连续出现。 默认值：无 配置原则：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| RELATEAPN       | APN别名           | 可选必选说明：条件必选参数 前提条件：该参数在“DISPLAYMODE”配置为“APN_RELATE”时为必选参数。 参数含义：该参数用于指定APN别名。表示查询使用该别名APN激活的当前在线会话数，该别名APN所对应的真实APN必须在系统上已经配置。如果输入真实APN，则显示与真实APN相关联的所有别名APN上的当前在线会话数。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。不支持空格及部分特殊字符。可以支持的特殊字符有“.”和“-”，“.”不可以是第一个字符且不可以连续出现。 默认值：无 配置原则：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| CPNODEIDSW      | Node ID开关       | 可选必选说明：条件可选参数 前提条件：该参数在“DISPLAYMODE”配置为“NGLAN”时为可选参数。 参数含义：该参数用于指定是否使用Node ID查询会话数。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不使能。ENABLE：使能。 默认值：无 配置原则：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| CPNODEIDTYPE    | Node ID类型       | 可选必选说明：条件必选参数 前提条件：该参数在“DISPLAYMODE”配置为“NODEID”时为必选参数。 可选必选说明：条件必选参数 前提条件：该参数在“CPNODEIDSW”配置为“ENABLE”时为必选参数。 参数含义：该参数用来指定Node ID 类型。 数据来源：全网规划 取值范围：枚举类型。 IPv4：表示Node ID类型为IPv4地址。IPv6：表示Node ID类型为IPv6地址。FQDN：表示Node ID类型为FQDN。 默认值：无 配置原则：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| CPNODEIDIPV4    | Node ID中的IPv4地址 | 可选必选说明：条件必选参数 前提条件：该参数在“CPNODEIDTYPE”配置为“IPv4”时为必选参数。 参数含义：该参数用于指定，在根据Node ID查询CP信息时，Node ID中的IPv4地址。 数据来源：全网规划 取值范围：IPv4地址类型。 默认值：无 配置原则：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| CPNODEIDIPV6    | Node ID中的IPv6地址 | 可选必选说明：条件必选参数 前提条件：该参数在“CPNODEIDTYPE”配置为“IPv6”时为必选参数。 参数含义：该参数用于指定，在根据Node ID查询CP信息时，Node ID中的IPv6地址。 数据来源：全网规划 取值范围：IPv6地址类型。 默认值：无 配置原则：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| CPNODEFQDN      | Node ID的FQDN    | 可选必选说明：条件必选参数 前提条件：该参数在“CPNODEIDTYPE”配置为“FQDN”时为必选参数。 参数含义：该参数用于指定，在根据NODE ID查询CP信息时，Node ID中的FQDN。 数据来源：全网规划 取值范围：字符串类型，输入长度范围为1～255。不支持空格，必须是可见ASCII码，不区分大小写。 默认值：无 配置原则：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| USERPROFILE     | 用户模板名称          | 可选必选说明：条件必选参数 前提条件：该参数在“DISPLAYMODE”配置为“USERPROFILE”时为必选参数。 参数含义：用户的userprofile名。该userprofile必须在系统上已经配置。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。 默认值：无 配置原则：该参数使用ADD USERPROFILE命令配置生成。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| PODNAME         | Pod名称           | 可选必选说明：条件必选参数 前提条件：该参数在“DISPLAYMODE”配置为“PODNAME”时为必选参数。 参数含义：该参数用于指定资源单元名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1~63，不支持空格，区分大小写。 默认值：无 配置原则：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| MNC             | 移动设备码           | 可选必选说明：条件可选参数 前提条件：该参数在“DISPLAYMODE”配置为“ROAMING”时为可选参数。 参数含义：该参数用于指定MNC移动网络码。表示查询使用该MNC激活的当前在线会话数。 数据来源：本端规划 取值范围：字符串类型，为3位数字，000～999。 默认值：无 配置原则：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| MCC             | 移动国家码           | 可选必选说明：条件可选参数 前提条件：该参数在“DISPLAYMODE”配置为“ROAMING”时为可选参数。 参数含义：该参数用于指定MCC移动国家码。表示查询使用该MCC激活的当前在线会话数。 数据来源：本端规划 取值范围：字符串类型，为3位数字，000～999。 默认值：无 配置原则：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| VNINSTANCE      | 5G LAN 组名称      | 可选必选说明：条件可选参数 前提条件：该参数在“DISPLAYMODE”配置为“NGLAN”时为可选参数。 参数含义：表示用户的VNINSTANCE信息。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为18～37。VNINSTANCE以连字号分为4段，形式为GroupServiceID-MCC-MNC-LocalGroupID。其中，GroupServiceID长度为8，只能输入数字或者范围为A到F或a-f的字母；MCC长度为3，只能输入数字；MNC长度为2~3，只能输入数字；LocalGroupID长度为2~20的偶数，只能输入数字或者范围为A到F或a-f的字母。例如，A0000001-460-003-01，A0000001-460-003-A000000001。不区分大小写。 默认值：无 配置原则：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| RATTYPE         | RAT类型           | 可选必选说明：条件必选参数 前提条件：该参数在“DISPLAYMODE”配置为“RAT”时为必选参数。 参数含义：该参数用来指定无线接入类型。表示查询该接入类型当前在线会话数。 数据来源：对端协商 取值范围：枚举类型。 UTRAN：通用陆地无线接入网。GERAN：GSM/EDGE无线接入网。WLAN：无线局域网。GAN：通用访问网络。HSPA：高速分组接入。EUTRAN：演进型通用陆地无线接入网。EUTRAN_NB_IOT：窄带物联网。LTE_M：低功耗窄带物联网。NR：5G用户。REDCAP：RedCap NR的5G用户。 默认值：无 配置原则：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| DNAI            | DNAI 名称         | 可选必选说明：条件必选参数 前提条件：该参数在“DISPLAYMODE”配置为“DNAI”时为必选参数。 参数含义：该参数用于指定DNAI实例名。表示查询使用该DNAI激活的当前在线会话数，该DNAI必须在系统上已经配置。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。 默认值：无 配置原则：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| IPSUITNAME      | IPSuit 名称       | 可选必选说明：条件必选参数 前提条件：该参数在“DISPLAYMODE”配置为“IPSUIT”时为必选参数。 参数含义：IP Suit的名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。此名称系统自动生成，取值为1~64。 默认值：无 配置原则：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| USERPROFILETYPE | UserProfile类型   | 可选必选说明：条件必选参数 前提条件：该参数在“DISPLAYMODE”配置为“USERPROFILE”时为必选参数。 参数含义：UserProfile类型。 数据来源：对端协商 取值范围：枚举类型。 COMMONPOLICY：COMMONPOLICY类型。PREDEFINEDRULE：预定义Rule类型。ALL：COMMONPOLICY和PREDEFINEDRULE类型。 默认值：无 配置原则：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| CONFLICTMODE    | 冲突会话类型          | 可选必选说明：条件可选参数 前提条件：该参数在“DISPLAYMODE”配置为“MultiDNN” 或 “RtsDNN”时为可选参数。 参数含义：表示查询当前在线的冲突会话数。 数据来源：本端规划 取值范围：枚举类型。 IPCONFLICT：用户IP地址和ServerIP冲突会话。 默认值：无 配置原则：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

#### 使用实例

- 显示当前所有会话数：

  ```
  DSP SESSIONNUMBER:;
  ```

  ```
  RETCODE = 0 操作成功。

  会话数信息
  ----------
  Result  =  
                                  Pod Name = ssgpod-0
                           GGSN Session(s) = 0
                            SGW Session(s) = 0
                            PGW Session(s) = 0
                           SPGW Session(s) = 0
                            UPF Session(s) = 0
                    N4-U Tunnel Session(s) = 0
                          Trunk Session(s) = 0
                        UPF MBS Session(s) = 0

                       All GGSN Session(s) = 0
                        All SGW Session(s) = 0
                        All PGW Session(s) = 0
                       All SPGW Session(s) = 0
                        All UPF Session(s) = 0
                All N4-U Tunnel Session(s) = 0
                      All Trunk Session(s) = 0
                    All UPF MBS Session(s) = 0

                    ALL Session context(s) = 0
  (结果个数 = 1)
  ---    END
  ```
- 显示当前离线计费会话数：

  ```
  DSP SESSIONNUMBER: DISPLAYMODE=OFFLINE;
  ```

  ```
  RETCODE = 0 操作成功。

  会话数信息
  ----------
  Result  =  
                              Pod Name = ssgpod-0124-30-0-210
       Offline Charging Session(s) = 1

    All Offline Charging Session(s) = 1
  (结果个数 = 1)
  ---    END
  ```

#### 输出结果说明

| 输出项名称                                           | 输出项解释                            |
|:------------------------------------------------|:---------------------------------|
| GGSN Session(s)                                 | 指定ISU GGSN上激活的会话数。               |
| SGW Session(s)                                  | 指定ISU SGW上激活的会话数。                |
| PGW Session(s)                                  | 指定ISU SGW上激活的会话数。                |
| SPGW Session(s)                                 | 指定ISU PGW上激活的会话数。                |
| UPF Session(s)                                  | 指定ISU SPGW上激活的会话数。               |
| N4-U Tunnel Session(s)                          | 指定ISU N4U Tunnel上激活的会话数。         |
| Trunk Session(s)                                | 指定ISU 上激活的宽带集群群组会话数。             |
| All GGSN Session(s)                             | 所有ISU GGSN上激活的会话数。               |
| All SGW Session(s)                              | 所有ISU SGW上激活的会话数。                |
| All PGW Session(s)                              | 所有ISU PGW上激活的会话数。                |
| All SPGW Session(s)                             | 所有ISU SPGW上激活的会话数。               |
| All UPF Session(s)                              | 所有ISU UPF上激活的会话数。                |
| ALL N4-U Tunnel Session(s)                      | 所有ISU N4U Tunnel上激活的会话数。         |
| All Trunk Session(s)                            | 所有ISU 上激活的宽带集群群组会话数。             |
| ALL Session context(s)                          | 所有ISU 会话数。                       |
| 5G LAN ETHERNET GROUP Session(s)                | 指定层二5GLAN组会话数。                   |
| 5G LAN ETHERNET UE Session(s)                   | 指定层二5GLAN组下的UE会话数。               |
| 5G LAN IP GROUP Session(s)                      | 指定层三5GLAN组会话数。                   |
| 5G LAN IP UE Session(s)                         | 指定层三5GLAN组下的UE会话数。               |
| All 5G LAN ETHERNET GROUP Session(s)            | 所有ISU上层二5GLAN组会话数。               |
| All 5G LAN ETHERNET UE Session(s)               | 所有ISU上层二5GLAN组下的UE会话数。           |
| All 5G LAN IP GROUP Session(s)                  | 所有ISU上层三5GLAN组会话数。               |
| All 5G LAN IP UE Session(s)                     | 所有ISU上层三5GLAN组下的UE会话数。           |
| UPF MBS Session(s)                              | 指定ISU上激活的MBS会话数。                 |
| All UPF MBS Session(s)                          | 所有ISU上激活的MBS会话数。                 |
| RTSDNN CommonDnn Anchor Session(s)              | 指定ISU 通用DNN漫游分流的通用DNN锚点+ULCL会话数。 |
| RTSDNN SpecialDnn I-UPF Session(s)              | 指定ISU 通用DNN漫游分流的专用DNN I-UPF会话数。  |
| RTSDNN SpecialDnn Anchor Session(s)             | 指定ISU 通用DNN漫游分流的专用DNN锚点会话数。      |
| All RTSDNN CommonDnn Anchor Session(s)          | 所有ISU上通用DNN漫游分流的通用DNN锚点+ULCL会话数。 |
| All RTSDNN SpecialDnn I-UPF Session(s)          | 所有ISU上通用DNN漫游分流的专用DNN I-UPF会话数。  |
| All RTSDNN SpecialDnn Anchor Session(s)         | 所有ISU上通用DNN漫游分流的专用DNN锚点会话数。      |
| RTSDNN CommonDnn Conflict Anchor Session(s)     | 指定ISU 通用DNN漫游分流IP冲突会话数。          |
| MultiDnn Conflict PSA Session(s)                | 指定ISU 双DNN IP冲突会话数。              |
| All RTSDNN CommonDnn Conflict Anchor Session(s) | 所有ISU上通用DNN漫游分流冲突会话数。            |
| All MultiDnn Conflict PSA Session(s)            | 所有ISU上双DNN IP冲突会话数。              |
| MultiDnn PSA Session(s)                         | 指定ISU 双DNN PSA会话数。               |
| MultiDnn I-UPF Session(s)                       | 指定ISU 双DNN I-UPF会话数。             |
| All MultiDnn CommonDnn session(s)               | 所有ISU上双DNN的通用DNN会话数。             |
| All MultiDnn SpecialDnn session(s)              | 所有ISU上双DNN的专用DNN会话数。             |
| DedicatedLBO ULCL Session(s)                    | 指定ISU上专网UPF分流的独立ULCL会话数。         |
| All DedicatedLBO ULCL Session(s)                | 所有ISU上专网UPF分流的独立ULCL会话数。         |
| ToH Session(s)                                  | 指定ISU上激活的家庭会话数，仅当查询所有会话数时才显示该项。  |
| All ToH Session(s)                              | 所有ISU上激活的家庭会话数，仅当查询所有会话数时才显示该项。  |