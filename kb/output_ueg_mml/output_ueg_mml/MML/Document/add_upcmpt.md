# 增加UP节点协议兼容性配置（ADD UPCMPT）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**须知** 

仅对接OpenUPF(异厂商UPF)需要配置，华为UPF不需要配置此UPCMPT，否则会导致建链失败。

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于增加UP节点协议兼容性配置。

## 注意事项

- 该命令执行后立即生效。

- 对接OpenUPF(异厂商UPF)时该配置需要在ADD PNFPROFILE之前添加。

- 最多可输入1024条记录。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识            | 参数名称                                  | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|:----------------|:--------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UPFINSTANCEID   | UPF实例标识                               | 可选必选说明：必选参数  参数含义：该参数用于指定UPF实例标识。  数据来源：全网规划  取值范围：字符串类型，输入长度范围是0~36。参数必须满足以下约束规则：1.如果输入为uuid格式（格式例如：a6a61c6f-0d3a-4221-b1da-424eda3ccf67）只能为A-F、a-f、0-9的字符。2.如果输入不为uuid格式，长度不能超过18且不允许输入只包含0-9和“.”的字符串，例如：1.2.3.4、不允许输入只包含十六进制数（A-F、a-f、0-9）和“:”的字符串，例如：1::2、FBFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF。不区分大小写。  默认值：无  配置原则：  该参数取值应与ADD UPNODE中参数“NFINSTANCENAME”保持一致，使用该前需通过ADD UPNODE添加一组记录。                                           |
| APNPOLICY       | APN/DNN编码格式                           | 可选必选说明：可选参数  参数含义：该参数用于指定SMF/SGW-C/PGW-C/GGSN发送给用户面的APN/DNN信元编码格式。  数据来源：对端协商 取值范围： “WITHOUTOI（不携带OI信息）”：APN或者DNN不携带APN OI或者DNN OI。“WITHOI（携带OI信息）”：APN或者DNN携带的是APNNI+APNOI或者DNNNI+DNNOI。  默认值：WITHOUTOI  配置原则：  如果用户面要求携带OI信息，则设置为WITHOI，否则默认为WITHOUTOI。                                                                                                                                                                                |
| SNSSAI          | 网络切片选择辅助信息                            | 可选必选说明：可选参数  参数含义：该参数用于指定SMF/SGW-C/PGW-C/GGSN发送给用户面的SNSSAI信元是否为标准信元。  数据来源：本端规划 取值范围： “INHERIT（继承）”：PFCP Session Establishment Request消息中S-NSSAI使用华为私有信元或协议标准的信元，继承SET PFCPPVTEXT命令配置中S_NSSAI功能是否开启。“OFF（关闭）”：PFCP Session Establishment Request消息中S-NSSAI使用华为私有信元。“ON（开启）”：PFCP Session Establishment Request消息中S-NSSAI使用协议标准的信元。  默认值：INHERIT  配置原则：无                                                                                  |
| NODEIDFQDNFMT   | Node ID信元FQDN编码格式                     | 可选必选说明：可选参数  参数含义：该参数用于指定SMF/SGW-C/PGW-C/GGSN发送给用户面的FQDN类型Node ID信元的编码格式。  数据来源：对端协商 取值范围： DOT（点分格式）LV（LV格式）  默认值：DOT  配置原则：无                                                                                                                                                                                                                                                                                                            |
| POOLPLACEHOLDER | 是否携带地址池占位符                            | 可选必选说明：可选参数  参数含义：该参数用于指定SMF/SGW-C/PGW-C/GGSN发送给用户面的PFCP消息是否携带地址池占位符。UNC向UDG申请双栈地址的时候，如果只有IPv6类型的地址池，则将IPv4地址池的位置用*代替，即为占位符。 以免对端将IPv6类型的地址池识别成IPv4类型。  数据来源：对端协商 取值范围： INHERIT（继承全局）TRUE（是）FALSE（否）  默认值：INHERIT  配置原则：  该参数取值为INHERIT时，应用SET PFCPCMPT中POOLPLACEHOLDER取值。                                                                                                                                                               |
| CUSTOMRATTYPE   | 是否携带运营商定制的RAT Type信元                  | 可选必选说明：可选参数  参数含义：该参数用于控制SMF/SGW-C/PGW-C/GGSN发送给用户面的PFCP Session Establishment/Modification Request消息中是否携带运营商定制的RAT Type信元。  数据来源：对端协商 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：DISABLE  配置原则：  当SMF/SGW-C/PGW-C/GGSN发送给用户面的PFCP Session Establishment/Modification Request消息中需要携带运营商定制的RAT Type信元时，配置为ENABLE。                                                                                                                                  |
| CUSTOML2TPPCO   | 是否携带运营商定制的L2TP User Info信元            | 可选必选说明：可选参数  参数含义：该参数用于控制SMF/SGW-C/PGW-C/GGSN发送给用户面的PFCP Session Establishment Request消息中是否携带运营商定制的L2TP User Info信元。  数据来源：对端协商 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：DISABLE  配置原则：  当SMF/SGW-C/PGW-C/GGSN发送给用户面的PFCP Session Establishment Request消息中需要携带运营商定制的L2TP User Info信元时，配置为ENABLE。                                                                                                                                                |
| CUSTOML2TPTNL   | 是否携带运营商定制的L2TP Tunnel Info信元          | 可选必选说明：可选参数  参数含义：该参数用于控制SMF/SGW-C/PGW-C/GGSN发送给用户面的PFCP Session Establishment Request消息中是否携带运营商定制的L2TP Tunnel Info信元。  数据来源：对端协商 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：DISABLE  配置原则：  当SMF/SGW-C/PGW-C/GGSN发送给用户面的PFCP Session Establishment Request消息中需要携带运营商定制的L2TP Tunnel Info信元时，配置为ENABLE。                                                                                                                                            |
| CUSTOMULI       | 是否携带运营商定制的User Location Information信元 | 可选必选说明：可选参数  参数含义：该参数用于控制SMF/SGW-C/PGW-C/GGSN发送给用户面的PFCP Session Establishment Request消息中是否携带运营商定制的User Location Information信元。  数据来源：对端协商 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：DISABLE  配置原则：  当SMF/SGW-C/PGW-C/GGSN发送给用户面的PFCP Session Establishment Request消息中需要携带运营商定制的User Location Information信元时，配置为ENABLE。                                                                                                                          |
| UEIPADDRSDFLAG  | 是否携带UE IP Address信元的S/D标记位            | 可选必选说明：可选参数  参数含义：该参数用于指定UE IP Address信元是否携带S/D标记位。  数据来源：对端协商 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：DISABLE  配置原则：  对接UPF校验UE IP Address信元中的S/D标记位时，配置为ENABLE。                                                                                                                                                                                                                                                                              |
| NWINSTDNFMT     | 网络实例Domian Name编码格式                   | 可选必选说明：可选参数  参数含义：该参数用于指定网络实例携带Domain Name时的编码格式。配置为点分格式时，部分场景下会使用点分格式。配置为LV格式时仅使用LV编码格式。  数据来源：对端协商 取值范围： DOT（点分格式）LV（LV格式）  默认值：DOT  配置原则：无                                                                                                                                                                                                                                                                                            |
| ISOPENUPF       | 是否支持OpenUPF                           | 可选必选说明：可选参数  参数含义：该参数用于指定对端UPF是否是OpenUPF。  数据来源：对端协商 取值范围： “DISABLE（不支持OpenUPF）”：不支持OpenUPF“ENABLE（支持OpenUPF）”：支持OpenUPF  默认值：DISABLE  配置原则：无                                                                                                                                                                                                                                                                                            |
| UPSTRICTPAITF   | UPF Pa接口配置严格匹配                        | 可选必选说明：可选参数  参数含义：该参数用于指定UPLOGICINTF的Pa接口(Gn/S5S8 Pgw/n9a)配置是否严格匹配。如果开关关闭，SMF上UPLOGICINTF的Pa接口(Gn/S5S8 Pgw/n9a)可以共用。如果开关开启，UPLOGICINTF配置的Pa接口(Gn/S5S8 Pgw/n9a)不可以共用。  数据来源：本端规划 取值范围： “DISABLE（关闭Pa接口严格匹配）”：关闭Pa接口严格匹配“ENABLE（开启Pa接口严格匹配）”：开启Pa接口严格匹配  默认值：DISABLE  配置原则：  当UPF为Open UPF或需要对UPLOGICINTF的Pa接口(Gn/S5S8 Pgw/n9a)进行严格匹配时，配置为ENABLE。                                                                                          |
| L2TPTNL         | L2TP隧道信息                              | 可选必选说明：可选参数  参数含义：该参数用于指定SMF/SGW-C/PGW-C/GGSN发送给UPF的L2TP隧道信息是否是华为私有信元格式。  数据来源：全网规划 取值范围： “INHERIT（继承）”：PFCP Session Establishment Request消息中L2TP隧道信元使用华为私有信元或协议标准信元，继承SET PFCPPVTEXT配置命令中L2TP_TNL功能是否开启。“ENABLE（使能）”：PFCP Session Establishment Request消息中L2TP隧道信息使用华为私有信元。“DISABLE（不使能）”：PFCP Session Establishment Request消息中L2TP隧道信息使用协议标准信元。  默认值：INHERIT  配置原则：  枚举项L2TPTNL和L2TPPCO同时使能或同时不使能，如果设置其中一个枚举值，另一个枚举值同时被设置。             |
| L2TPPCO         | L2TP用户PCO信息                           | 可选必选说明：可选参数  参数含义：该参数用于指定SMF/SGW-C/PGW-C/GGSN发送给UPF的L2TP用户PCO信息是否是华为私有信元格式。  数据来源：全网规划 取值范围： “INHERIT（继承）”：PFCP Session Establishment Request消息中L2TP用户PCO信息使用华为私有信元或协议标准信元，继承SET PFCPPVTEXT配置命令中L2TP_PCO功能是否开启。“ENABLE（使能）”：PFCP Session Establishment Request消息中L2TP用户PCO信息使用华为私有信元。“DISABLE（不使能）”：PFCP Session Establishment Request消息中L2TP用户PCO信息使用协议标准信元。  默认值：INHERIT  配置原则：  枚举项L2TPTNL和L2TPPCO同时使能或同时不使能，如果设置其中一个枚举值，另一个枚举值同时被设置。 |
| HTTPRDTDSTITF   | HTTP重定向对端接口值                          | 可选必选说明：可选参数  参数含义：该参数用于指定HTTP重定向对端接口值。  数据来源：全网规划 取值范围： Core（Core）Access（Access）  默认值：Core  配置原则：无                                                                                                                                                                                                                                                                                                                                       |
| CUSUEIPADDR     | 定制携带UE IP地址的方式                        | 可选必选说明：可选参数  参数含义：该参数用于通用DNN漫游分流特性中专网会话SMF是否通过运营商定制的信元格式携带大网UE IP地址信息给锚点UPF。  数据来源：对端协商 取值范围： “DISABLE（不使能）”：通过华为私有信元格式携带大网UE IP地址信息给锚点UPF。“ENABLE（使能）”：通过运营商定制的信元格式携带大网UE IP地址信息给锚点UPF。  默认值：DISABLE  配置原则：  如果对端专网UPF为华为设备，该参数配置为DISABLE；如果为其他厂商设备，该UPF支持处理PFCP消息中ReplacedUeIpAddress字段，参数配置为ENABLE。                                                                                                                                   |
| PMUSERIDFM      | 路径迁移UserID信元编码格式                      | 可选必选说明：该参数在"PMUSERIDSW"配置为"WITH"时为条件可选参数。  参数含义：该参数用于设置路径迁移UserID信元编码格式。  数据来源：全网规划 取值范围： CUSTOM（定制信元格式）STANDARD（标准信元格式）  默认值：CUSTOM  配置原则：无                                                                                                                                                                                                                                                                                             |
| PMUSERIDSW      | 路径迁移是否携带UserID信元                      | 可选必选说明：可选参数  参数含义：该参数用于设置路径迁移是否携带UserID信元。  数据来源：全网规划 取值范围： “WITH（携带）”：消息携带UserID信元“WITHOUT（不携带）”：消息不携带UserID信元  默认值：WITH  配置原则：无                                                                                                                                                                                                                                                                                                        |

## 使用实例

增加UP节点协议兼容性配置，UPF实例标识为upf\_instance\_1，APN/DNN编码格式为WITHOUTOI，执行如下命令：

```
ADD UPCMPT:UPFINSTANCEID="upf_instance_1",APNPOLICY=WITHOUTOI;
```