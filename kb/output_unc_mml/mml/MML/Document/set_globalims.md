# 设置全局IMS互通配置信息（SET GLOBALIMS）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：PGW-C、SMF、GGSN、SGW-C**

该命令用来配置IMS互通相关的设置。包括：IMS功能开关、IMS信令空口增强开关、配置P-CSCF的缺省组。当IMS功能开关打开时，才可以对IMS信令空口增强开关以及P-CSCF缺省组进行配置。当运营商需要控制IMS互通相关的参数时，可使用该命令对全局IMS配置参数进行配置。

## 注意事项

- 命令执行后只对新接入用户生效。

- P-CSCF缺省组在系统内只能存在一个，未通过本命令明确指定时，则认为系统中没有缺省组。
- 当前版本不支持此命令的SIGNALRADIOPRE参数。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| IMSSWITCH   | SIGNALRADIOPRE   |   UPDATEMSGRATE | ENABLEGRPIPV4   | ENABLEGRPIPV6   | UDMPCSCF   | UDMPCSCFMODE   | HSSPCSCF   | HSSPCSCFMODE   |
|:------------|:-----------------|----------------:|:----------------|:----------------|:-----------|:---------------|:-----------|:---------------|
| DISABLE     | DISABLE          |            1000 | DISABLE         | DISABLE         | DISABLE    | PDUREACTIVATE  | DISABLE    | PDUREACTIVATE  |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识            | 参数名称                         | 参数说明                                                                                                                                                                                                                                                                                                                                              |
|:----------------|:-----------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IMSSWITCH       | IMS功能开关                      | 可选必选说明：可选参数  参数含义：该参数用于打开或关闭全局IMS功能开关。  数据来源：本端规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST GLOBALIMS查询当前参数配置值。  配置原则：无                                                                                                                                                                                               |
| SIGNALRADIOPRE  | IMS信令空口增强开关                  | 可选必选说明：该参数在"IMSSWITCH"配置为"ENABLE"时为条件可选参数。  参数含义：该参数用于设置IMS信令空口增强开关。  数据来源：本端规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST GLOBALIMS查询当前参数配置值。  配置原则：无                                                                                                                                                                 |
| DEFPCSCFGRPIPV4 | 缺省IPv4 P-CSCF组               | 可选必选说明：该参数在"ENABLEGRPIPV4"配置为"ENABLE"时为条件可选参数。  参数含义：该参数用于配置缺省IPv4类型的p-cscf组。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是0~63。只允许输入字母、数字、“.”、“_”和“-”。字母会被转换为小写字母进行存储和处理。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST GLOBALIMS查询当前参数配置值。  配置原则：  该参数使用ADD PCSCFGROUP命令，并配置该命令的IPVERSION参数为IPv4地址类型方可生成。当DEFPCSCFGRPIPV4为空格时执行清空功能。                                |
| DEFPCSCFGRPIPV6 | 缺省IPv6 P-CSCF组               | 可选必选说明：该参数在"ENABLEGRPIPV6"配置为"ENABLE"时为条件可选参数。  参数含义：该参数用于配置缺省IPv6类型的p-cscf组。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是0~63。只允许输入字母、数字、“.”、“_”和“-”。字母会被转换为小写字母进行存储和处理。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST GLOBALIMS查询当前参数配置值。  配置原则：  该参数使用ADD PCSCFGROUP命令，并配置该命令的IPVERSION参数为IPv6地址类型方可生成。当DEFPCSCFGRPIPV6为空格时执行清空功能。                                |
| UPDATEMSGRATE   | 发送更新消息速率(个/秒)                | 可选必选说明：可选参数  参数含义：该参数用于指定整系统更新承载或会话时消息发送的最大速率。  数据来源：本端规划  取值范围：整数类型，取值范围是10~5000。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST GLOBALIMS查询当前参数配置值。  配置原则：无                                                                                                                                                                                           |
| ENABLEGRPIPV4   | 缺省IPv4 P-CSCF组域名开关           | 可选必选说明：该参数在"IMSSWITCH"配置为"ENABLE"时为条件可选参数。  参数含义：该参数用于控制缺省IPv4 P-CSCF组域名是否为空。  数据来源：本端规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST GLOBALIMS查询当前参数配置值。  配置原则：无                                                                                                                                                        |
| ENABLEGRPIPV6   | 缺省IPv6 P-CSCF组域名开关           | 可选必选说明：该参数在"IMSSWITCH"配置为"ENABLE"时为条件可选参数。  参数含义：该参数用于控制缺省IPv6 P-CSCF组域名是否为空。  数据来源：本端规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST GLOBALIMS查询当前参数配置值。  配置原则：无                                                                                                                                                        |
| UDMPCSCF        | 基于UDM的P-CSCF Restoration功能开关 | 可选必选说明：可选参数  参数含义：该参数用于指示基于UDM的P-CSCF Restoration功能开关。  数据来源：本端规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST GLOBALIMS查询当前参数配置值。  配置原则：无                                                                                                                                                                               |
| UDMPCSCFMODE    | 基于UDM的P-CSCF Restoration功能模式 | 可选必选说明：该参数在"UDMPCSCF"配置为"ENABLE"时为条件可选参数。  参数含义：该参数用于指示基于UDM的P-CSCF Restoration功能模式。  数据来源：本端规划 取值范围： “PDUREACTIVATE（PDU会话重激活）”：基于UDM的P-CSCF故障恢复模式为释放PDU。“PCSCFADDRUPDATE（P-CSCF地址列表更新）”：按照协议根据UE能力0012H(P-CSCF Re-selection support)选择。其中，如果UE支持P-CSCF地址更新则发更新消息给UE，否则删除会话。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST GLOBALIMS查询当前参数配置值。  配置原则：无 |
| HSSPCSCF        | 基于HSS的P-CSCF Restoration功能开关 | 可选必选说明：可选参数  参数含义：该参数用于指示基于HSS的P-CSCF Restoration功能开关。  数据来源：本端规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST GLOBALIMS查询当前参数配置值。  配置原则：无                                                                                                                                                                               |
| HSSPCSCFMODE    | 基于HSS的P-CSCF Restoration功能模式 | 可选必选说明：该参数在"HSSPCSCF"配置为"ENABLE"时为条件可选参数。  参数含义：该参数用于指示基于HSS的P-CSCF Restoration功能模式。  数据来源：本端规划 取值范围： “PDUREACTIVATE（PDU会话重激活）”：基于HSS的P-CSCF故障恢复模式为释放PDU。“PCSCFADDRUPDATE（P-CSCF地址列表更新）”：按照协议根据UE能力0012H(P-CSCF Re-selection support)选择。其中，如果UE支持P-CSCF地址更新则发更新消息给UE，否则删除会话。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST GLOBALIMS查询当前参数配置值。  配置原则：无 |

## 使用实例

当用户需要配置全局IMS开关打开，并且打开IMS信令空口时，打开缺省IPv4 P-CSCF组域名开关，指定IPv4类型P-CSCF缺省组为“pcsf1”，配置发送更新消息速率为1000时，进行如下设置：

```
SET GLOBALIMS:IMSSWITCH=ENABLE,SIGNALRADIOPRE=ENABLE,ENABLEGRPIPV4=ENABLE,DEFPCSCFGRPIPV4="pcsf1",UPDATEMSGRATE=1000;
```