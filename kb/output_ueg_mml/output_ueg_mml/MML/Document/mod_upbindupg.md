# 修改用户模板组和用户模板的绑定关系（MOD UPBINDUPG）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用NF：PGW-C、SMF**

本命令用于修改用户模板组和用户模板的绑定关系，可以基于特定条件进行绑定，如UserProfile优先级、IMSI/MSISDN号码段名称、IMEISV号码段名称、RAT、Roaming值、ChargeChar值及UsrLocationGrp名称，也可以指定缺省UserProfile。

#### 注意事项

- 该命令执行后立即生效。
- 当UPBINDTYPE指定为SPECIFIC时，ImsiMsSegName、ImeisvSegName、Rat、Roaming、ChargeChar和LocGroupName至少要设置其中任意一个。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识            | 参数名称                     | 参数说明                                                                                                                                                                                                                                                                                                                                                                    |
|:----------------|:-------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| USERPROFGNAME   | 用户模板组名称                  | 可选必选说明：必选参数 参数含义：该参数用于指定用户模板组名称。 数据来源：全网规划 取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。 默认值：无 配置原则： 该参数使用ADD USRPROFGROUP命令配置生成。配置的USERPROFGNAME必须是系统已经存在的UsrProfGroup对象名称。                                                                                                                                                                                                     |
| UPBINDTYPE      | 用户模板绑定类型                 | 可选必选说明：必选参数 参数含义：参数用于设置用户模板绑定类型。 数据来源：全网规划 取值范围：枚举类型。 SPECIFIC：指定被绑定的用户模板。DEFAULT：指定默认用户模板。ULCL：指定ULCL用户模板。 默认值：无 配置原则：无                                                                                                                                                                                                                                                |
| PRIORITY        | 优先级                      | 可选必选说明：条件必选参数 前提条件：该参数在“UPBINDTYPE”配置为“SPECIFIC”时为必选参数。 参数含义：该参数用于设置UserProfile绑定到UsrProfGroup时的优先级。 数据来源：本端规划 取值范围：整数类型，取值范围为1～65534。取值范围为1到65534（65535用于用户绑定类型为默认的优先级）。值越小优先级越高。 默认值：无 配置原则：无                                                                                                                                                                         |
| USERPROFILENAME | 用户模板名称                   | 可选必选说明：条件必选参数 前提条件：该参数在“UPBINDTYPE”配置为“SPECIFIC” 或 “DEFAULT”时为必选参数。 参数含义：该参数用于指定UserProfile对象名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。 默认值：无 配置原则： 该参数使用ADD CPUSERPROFILE命令配置生成。配置的USERPROFILENAME必须是系统已经存在的UserProfile对象名称。                                                                                                                                   |
| RAT             | RAT                      | 可选必选说明：条件可选参数 前提条件：该参数在“UPBINDTYPE”配置为“SPECIFIC”时为可选参数。 参数含义：参数用于设置无线接入技术类型。 数据来源：全网规划 取值范围：枚举类型。 NONE：不指定无线技术接入类型。UTRAN：UMTS陆地无线接入网。GERAN：GSM/EDGE无线接入网。WLAN：无线局域网。GAN：通用接入网络。HSPA：高速分组接入。EUTRAN：通用陆基无线接入网。NR：5G无线接入(New Radio)。NBIOT：窄带物联网。EMTC：增强型机器类通信。REDCAP：轻量能力。 默认值：无 配置原则：无                                                                                    |
| ROAMING         | 漫游属性                     | 可选必选说明：条件可选参数 前提条件：该参数在“UPBINDTYPE”配置为“SPECIFIC”时为可选参数。 参数含义：该参数用于设置用户漫游属性。 数据来源：全网规划 取值范围：枚举类型。 NONE：不指定用户归属的属性。HOME：基于本地用户控制规则。ROAMING：基于漫游用户控制规则。VISITING：基于拜访用户控制规则。 默认值：无 配置原则：无                                                                                                                                                                                   |
| CCCONFIGMODE    | 计费属性配置模式                 | 可选必选说明：条件可选参数 前提条件：该参数在“UPBINDTYPE”配置为“SPECIFIC”时为可选参数。 参数含义：该参数用于设置计费属性配置模式。 数据来源：全网规划 取值范围：枚举类型。 NORMAL：表示计费特征为普通计费。消息中携带的MAPPINGVALUE信元值为2048（0x0800）。HOTBILLING：表示计费特征为热计费。消息中携带的MAPPINGVALUE信元值为256（0x0100）。PREPAID：表示计费特征为预付费。消息中携带的MAPPINGVALUE信元值为1024（0x0400）。FLATBILLING：表示计费特征为统一费率计费。消息中携带的MAPPINGVALUE信元值为512（0x0200）。SPECIFIC：表示指定配置的其他计费特征。 默认值：无 配置原则：无 |
| CHARGECHAR      | 计费属性                     | 可选必选说明：条件必选参数 前提条件：该参数在“CCCONFIGMODE”配置为“SPECIFIC”时为必选参数。 参数含义：该参数用于设置计费属性。 数据来源：全网规划 取值范围：字符串类型，输入长度范围为1～6。十六进制，仅支持输入0x/0X、a-f/A-F、0-9，允许不输入0x/0X前缀，字母不区分大小写，取值范围0x0~0xffff。 默认值：无 配置原则：无                                                                                                                                                                              |
| CCMASK          | 计费属性掩码                   | 可选必选说明：条件可选参数 前提条件：该参数在“CCCONFIGMODE”配置为“SPECIFIC”时为可选参数。 参数含义：该参数用于设置计费属性掩码。 数据来源：全网规划 取值范围：字符串类型，输入长度范围为1～6。十六进制，仅支持输入0x/0X、a-f/A-F、0-9，允许不输入0x/0X前缀，字母不区分大小写，取值范围0x1~0xFFFF。 默认值：无 配置原则：无                                                                                                                                                                            |
| IMSIMSSEGNAME   | IMSI/MSISDN号段名称          | 可选必选说明：条件可选参数 前提条件：该参数在“UPBINDTYPE”配置为“SPECIFIC”时为可选参数。 参数含义：该参数用于指定IMSI/MSISDN的号码段。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 默认值：无 配置原则： 该参数使用ADD IMSIMSISDNSEG命令配置生成。配置的IMSIMSSEGNAME必须是系统已经存在的ImsiMsisdnSeg对象名称。                                                                                                                                               |
| IMEISVSEGNAME   | IMEISV号段名称               | 可选必选说明：条件可选参数 前提条件：该参数在“UPBINDTYPE”配置为“SPECIFIC”时为可选参数。 参数含义：该参数用于指定IMEISV的号码段。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 默认值：无 配置原则： 该参数使用ADD IMEISVSEG命令配置生成。配置的IMEIVSEGNAME必须是系统已经存在的ImeisvSeg对象名称。                                                                                                                                                             |
| LOCGROUPNAME    | 位置组名称                    | 可选必选说明：条件可选参数 前提条件：该参数在“UPBINDTYPE”配置为“SPECIFIC”时为可选参数。 参数含义：该参数用于指定位置组名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。 默认值：无 配置原则： 该参数使用ADD USRLOCATIONGRP命令配置生成。配置的LOCGROUPNAME必须是系统已经存在的UsrLocationGrp对象名称。                                                                                                                                                        |
| SEGGROUPNAME    | IMSI/MSISDN/IMEISV 号段组名称 | 可选必选说明：条件可选参数 前提条件：该参数在“UPBINDTYPE”配置为“SPECIFIC”时为可选参数。 参数含义：该参数用于指定IMSI/MSISDN/IMEISV号码段组名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 默认值：无 配置原则：该参数使用ADD SUBSCRIBERIDSEGGRP命令配置生成。                                                                                                                                                                              |
| LOCALPCCSELECT  | 本地PCC策略选择模式              | 可选必选说明：可选参数 参数含义：该参数用于指定UNC本地PCC策略选择模式。 数据来源：本端规划 取值范围：枚举类型。 INHERIT：继承全局配置SET PCCFUNC下的LOCALPCCSELECT参数配置。LOCAL_PCC_DEACTIVE：本地PCC策略不激活。LOCAL_PCC_ACTIVE：本地PCC策略激活。LOCAL_PCC_NO_CRBN_ACT：未下发计费规则组时本地PCC策略激活。LOCAL_PCC_NO_RULE_ACT：未下发任意计费规则时本地PCC策略激活。 默认值：无 配置原则：无                                                                                                    |

#### 使用实例

运营商要修改用户模板组和用户模板的绑定关系，Rat为utran，Roaming为home：

```
MOD UPBINDUPG:USERPROFGNAME="userprofg1",UPBINDTYPE=SPECIFIC,PRIORITY=10,USERPROFILENAME="userprofile1",RAT=UTRAN,ROAMING=HOME;
```