# 设置NF携带参数处理规则（SET NRFTAKEPARARULE）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**须知** 

在设置NF携带参数处理规则时，NOSEGGUARDSW由开变关，号段防呆功能失效，会导致未携带号段的网元被发现，影响业务引流，可能引起业务失败。

**适用NF：NRF**

该命令用于设置NF携带参数处理规则。

## 注意事项

- 该命令执行后立即生效。

- 主备或双活组网的场景下，如果需要配置此命令，则两个NRF上均需执行此命令，且配置参数一致。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| NFTYPE     | NOSEGGUARDSW   | NOTAISW   | NOIPRANGESW   | REGUPDSW   | MATCHALLSW   | RULE   | IPRULE   |
|:-----------|:---------------|:----------|:--------------|:-----------|:-------------|:-------|:---------|
| AMF        | -              | FUNC_OFF  | -             | -          | -            | -      | -        |
| SMF        | -              | FUNC_OFF  | -             | -          | -            | -      | -        |
| BSF        | -              | -         | FUNC_OFF      | FUNC_OFF   | FUNC_OFF     | -      | -        |
| UDM        | FUNC_OFF       | -         | -             | FUNC_OFF   | FUNC_OFF     | -      | -        |
| UDR        | FUNC_OFF       | -         | -             | FUNC_OFF   | FUNC_OFF     | -      | -        |
| AUSF       | FUNC_OFF       | -         | -             | FUNC_OFF   | FUNC_OFF     | -      | -        |
| PCF        | FUNC_OFF       | -         | -             | FUNC_OFF   | FUNC_OFF     | -      | -        |
| CHF        | FUNC_OFF       | -         | -             | FUNC_OFF   | FUNC_OFF     | -      | -        |
| CUSTOM_OCS | FUNC_OFF       | -         | -             | FUNC_OFF   | FUNC_OFF     | -      | -        |
| SMSF       | FUNC_OFF       | -         | -             | FUNC_OFF   | FUNC_OFF     | -      | -        |
| NWDAF      | -              | FUNC_OFF  | -             | -          | -            | -      | -        |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识         | 参数名称       | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|:-------------|:-----------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NFTYPE       | 网元类型       | 可选必选说明：必选参数  参数含义：该参数用于表示配置携带参数处理规则的目标网元类型。  数据来源：本端规划 取值范围： UDM（UDM）AMF（AMF）SMF（SMF）AUSF（AUSF）PCF（PCF）UDR（UDR）BSF（BSF）CHF（CHF）CUSTOM_OCS（CUSTOM_OCS）SMSF（SMSF）NWDAF（NWDAF）  默认值：无。  配置原则：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| NOSEGGUARDSW | NF号段防呆开关   | 可选必选说明：该参数在"NFTYPE"配置为"UDM"、"UDR"、"AUSF"、"CUSTOM_OCS"、"CHF"、"PCF"、"SMSF"时为条件可选参数。  参数含义：该参数用于表示NRF上的号段NF所携带的号段信元不满足设置的规则时，是否需要上报告警、是否可以被发现/检索以及该NF发生变更时通知已订阅NF的开关。开关设置为“FUNC_ON”，号段NF所携带的号段信元在不满足设置的控制规则或默认规则时，需要上报告警“ALM-100315 NF携带信元防呆”；不满足默认规则情况下，通知里的NF状态为SUSPENDED；检索时不满足默认规则不可被检索；服务发现时与RULE控制规则取交集，按交集进行判断，既需满足控制规则也需满足默认规则，没有交集时需满足默认规则，若均不满足则不可被发现。 例如： UDM号段只配置MSISDN，服务发现参数只携带IMSI，开关关闭情况下，全匹配； UDM号段只配置MSISDN，服务发现参数只携带IMSI，规则勾选IMSI，开关打开，此场景不可被发现。 UDM号段只配置MSISDN，服务发现参数只携带IMSI，规则只勾选MSISDN，全匹配。  数据来源：本端规划 取值范围： “FUNC_ON（打开）”：功能开关打开“FUNC_OFF（关闭）”：功能开关关闭  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NRFTAKEPARARULE查询当前参数配置值。  配置原则：无                                         |
| NOTAISW      | NF无TAI处理开关 | 可选必选说明：该参数在"NFTYPE"配置为"AMF"、"SMF"、"NWDAF"时为条件可选参数。  参数含义：该参数用于表示是否开启NF未携带TAI（包括TAILIST和TAIRANGELIST）的控制开关。开关设置为“FUNC_ON”，NF未携带TAI（TAILIST和TAIRANGELIST均未携带）时，需要上报告警“ALM-100315 NF携带信元防呆”；通知里的NF状态为SUSPENDED；服务发现和检索时不可被发现和检索。  数据来源：本端规划 取值范围： “FUNC_ON（打开）”：功能开关打开“FUNC_OFF（关闭）”：功能开关关闭  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NRFTAKEPARARULE查询当前参数配置值。  配置原则：  当网元类型为AMF/SMF/NWDAF时，可配置此开关。  当网元类型为BSF时，不可配置此开关。                                                                                                                                                                                                                                                                        |
| NOIPRANGESW  | NF无IP处理开关  | 可选必选说明：该参数在"NFTYPE"配置为"BSF"时为条件可选参数。  参数含义：该参数用于表示是否开启NF未携带IP地址的控制开关。开关设置为“FUNC_ON”，NF所携带的IP地址信元在不满足设置的控制规则或默认规则时，需要上报告警“ALM-100315 NF携带信元防呆”；不满足默认规则情况下，通知里的NF状态为SUSPENDED；检索时不满足默认规则不可被检索；服务发现时发现条件与RULE控制规则取交集，按交集进行判断，既需满足控制规则也需满足默认规则，没有交集时需满足默认规则，若均不满足则不可被发现。  数据来源：本端规划 取值范围： “FUNC_ON（打开）”：功能开关打开“FUNC_OFF（关闭）”：功能开关关闭  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NRFTAKEPARARULE查询当前参数配置值。  配置原则：  当网元类型为AMF/SMF/NWDAF时，不可配置此开关。  当网元类型为BSF时，可配置此开关。                                                                                                                                                                                                                                 |
| REGUPDSW     | 注册更新处理开关   | 可选必选说明：该参数在"NOIPRANGESW"配置为"FUNC_ON"时为条件可选参数。该参数在"NOSEGGUARDSW"配置为"FUNC_ON"时为条件可选参数。该参数在"NOTAISW"配置为"FUNC_ON"时为条件可选参数。  参数含义：该参数用于表示NF所携带的信元不满足设置的规则时，NRF是否允许该NF注册/更新成功。开关设置为“FUNC_ON”， NF注册不满足设置的控制规则或默认规则，或NF更新前满足且更新后不满足设置的控制规则或默认规则时，NRF拒绝本次请求，返回“400 Bad Request”错误响应；开关设置为“FUNC_OFF”，则NRF正常处理。  数据来源：本端规划 取值范围： “FUNC_ON（打开）”：功能开关打开“FUNC_OFF（关闭）”：功能开关关闭  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NRFTAKEPARARULE查询当前参数配置值。  配置原则：无                                                                                                                                                                                                                                                   |
| MATCHALLSW   | 全匹配开关      | 可选必选说明：该参数在"NOIPRANGESW"配置为"FUNC_OFF"时为条件可选参数。该参数在"NOSEGGUARDSW"配置为"FUNC_OFF"时为条件可选参数。  参数含义：该参数用于表示当NF号段防呆开关处理开关或NF无IP处理开关为关闭时，是否启用对应信元的全匹配功能。开关设置为“FUNC_ON”，表示启用全匹配功能，功能描述如下： 对于号段类NF，如果注册时没有携带IMSI号段或MSISDN号段或ROUTINGINDICATOR，并且NRF上也没有为NF配置对应支持的号段，NRF服务发现时认为该NF支持对应号段的所有值。当发现参数同时携带IMSI和MSISDN，NRF匹配同时满足两个号段的发现条件才认为该NF满足发现条件。 对于BSF，若NF注册时没有携带Ipv4AddressRanges和Ipv6PrefixRanges，NRF服务发现时认为该NF支持ue-ipv4-address、ue-ipv6-prefix的所有值。  数据来源：本端规划 取值范围： “FUNC_ON（打开）”：功能开关打开“FUNC_OFF（关闭）”：功能开关关闭  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NRFTAKEPARARULE查询当前参数配置值。  配置原则：无                                                                                                             |
| RULE         | 规则         | 可选必选说明：该参数在"NOSEGGUARDSW"配置为"FUNC_ON"时为条件可选参数。  参数含义：该参数用于表示NF使用的号段控制规则。  数据来源：本端规划 取值范围： IMSI（IMSI）MSISDN（MSISDN）ROUTINGINDICATOR（ROUTINGINDICATOR）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NRFTAKEPARARULE查询当前参数配置值。  配置原则：  UDR/CHF/PCF/OCS/SMSF网元只能勾选IMSI/MSISDN，UDM网元可以勾选IMSI/MSISDN/ROUTINGINDICATOR，AUSF网元只能勾选IMSI/ROUTINGINDICATOR。  当未勾选任何规则取值范围时，表示号段防呆使用默认防呆规则。  默认防呆规则：  号段类型NF(UDR、PCF、CHF、CUSTOM_OCS和SMSF)必须携带IMSI/MSISDN中的一种信元；AUSF必须携带IMSI/ROUTINGINDICATOR中的一种信元；UDM必须携带IMSI/MSISDN/ROUTINGINDICATOR中的一种信元。  注意：独立部署的IMS PCF支持全网用户（号段），这种PCF不受默认防呆规则约束。  NRF通过比较PCF携带的DNN与配置的DNN来判断PCF是否是独立部署的IMS PCF。当PCF携带的DNN全部配置时认为该PCF是独立部署的IMS PCF，反之则认为不是。DNN信息通过ADD NRFIMSDNN命令配置。 |
| IPRULE       | IP地址控制规则   | 可选必选说明：该参数在"NOIPRANGESW"配置为"FUNC_ON"时为条件可选参数。  参数含义：该参数用于表示BSF的IP地址控制规则。  数据来源：本端规划 取值范围： IPV4（IPV4）IPV6（IPV6）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NRFTAKEPARARULE查询当前参数配置值。  配置原则： 当IPV4和IPV6均不勾选时，使用默认规则：即IPV4地址或IPV6地址必须携带其中一种；当勾选IPV4时，必须携带IPV4地址；当勾选IPV6时，必须携带IPV6地址；当勾选IPV4和IPV6时，IPV4地址和IPV6地址必须全部携带。                                                                                                                                                                                                                                                                                                                                                                            |

## 使用实例

网元类型为AUSF，开启NF号段防呆开关，规则同时使用IMSI和ROUTINGINDICATOR。

```
SET NRFTAKEPARARULE:NFTYPE=AUSF,NOSEGGUARDSW=FUNC_ON,RULE=IMSI-1&ROUTINGINDICATOR-1;
```