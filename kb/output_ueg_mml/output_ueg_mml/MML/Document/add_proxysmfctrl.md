# 增加proxy SMF控制（ADD PROXYSMFCTRL）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：SMF**

新增配置PROXYSMFCTRL，用于在对接归属地PGW/HSMF时配置代理功能控制。

## 注意事项

- 该命令执行后只对新激活用户生效。

- 业务匹配时，对同一MCCMNC，优先匹配DNN\_LEVEL的配置，如匹配失败，则匹配GLOBAL\_LEVEL。

- 最多可输入1024条记录。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识           | 参数名称                        | 参数说明                                                                                                                                                                                                                                                                                                                         |
|:---------------|:----------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MCC            | 移动国家码                       | 可选必选说明：必选参数  参数含义：该参数用于配置移动国家码信息。  数据来源：本端规划  取值范围：字符串类型，输入长度是3。  默认值：无  配置原则：无                                                                                                                                                                                                                                              |
| MNC            | 移动网号                        | 可选必选说明：必选参数  参数含义：该参数用于配置移动网号信息。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是2~3。  默认值：无  配置原则：无                                                                                                                                                                                                                                           |
| CTRLTYPE       | 控制类型                        | 可选必选说明：必选参数  参数含义：该参数用于指定控制类型。  数据来源：全网规划 取值范围： DNN_LEVEL（DNN级别）GLOBAL_LEVEL（整系统级别）  默认值：无  配置原则：无                                                                                                                                                                                                                           |
| DNN            | DNN                         | 可选必选说明：该参数在"CTRLTYPE"配置为"DNN_LEVEL"时为条件必选参数。  参数含义：该参数用于指定组成QoS控制的DNN，即用户请求的DNN。  数据来源：全网规划  取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。  默认值：无  配置原则：  输入的DNN名称需要符合DNN命名规则，仅支持配置APN NI（Network Identifier），例如“huawei.com”。 |
| PROXYQOSSOURCE | Proxy QoS来源                 | 可选必选说明：必选参数  参数含义：该参数用于控制Proxy SMF S8在获得PGW下发的Qos前所使用的Qos来源。  数据来源：本端规划 取值范围： “V-SMF（V-SMF）”：使用VplmnQos。“UDM（UDM）”：使用UDM下发的Qos。“NEGOTIATE（使用协商的方式决定QoS）”：使用VplmnQos与UDM Qos协商取小。  默认值：无  配置原则：无                                                                                                                              |
| TACCONVPOLICY  | TAC转换策略                     | 可选必选说明：必选参数  参数含义：该参数用于Proxy SMF S8给PGW发送消息时，如果消息中携带ULI，设置ULI中TAC的构造方式。  数据来源：本端规划 取值范围： “Default（默认策略）”：TAC取值为V-SMF携带的TAC去掉中间8BIT后的值。“Specify（指定值）”：使用参数TAC指定的值。  默认值：无  配置原则：无                                                                                                                                             |
| TAC            | TAC                         | 可选必选说明：该参数在"TACCONVPOLICY"配置为"Specify"时为条件必选参数。  参数含义：该参数用于Proxy SMF S8给PGW发送消息时，如果消息中携带ULI，设置ULI中TAC为配置值。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是1~6。十六进制，仅支持输入0x/X、a-f/A-F、0-9，允许不输入0x/X前缀，字母不区分大小写，取值范围0x0000~0xFFFF。输入长度范围是1~4（不包含0x/X前缀）/ 3~6（包含0x/X前缀）。  默认值：无  配置原则：无                                                          |
| CELLIDCONVPLY  | E-UTRAN Cell Identifier转换策略 | 可选必选说明：必选参数  参数含义：该参数用于Proxy SMF S8给PGW发送消息时，如果消息中携带ULI，设置ULI中E-UTRAN Cell Identifier的构造方式。  数据来源：本端规划 取值范围： “Default（默认策略）”：E-UTRAN Cell Identifier取值为Nr Cell Identifier去掉高位8BIT后的值。“Specify（指定值）”：使用参数ECELLID指定的值。  默认值：无  配置原则：无                                                                                          |
| ECELLID        | E-UTRAN Cell Identifier     | 可选必选说明：该参数在"CELLIDCONVPLY"配置为"Specify"时为条件必选参数。  参数含义：该参数用于Proxy SMF S8给PGW发送消息时，如果消息中携带ULI，设置ULI中E-UTRAN Cell Identifier为配置值。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是1~9。十六进制，仅支持输入0x/X、a-f/A-F、0-9，允许不输入0x前缀，字母不区分大小写，取值范围0x0000000~0xFFFFFFF。输入长度范围是1~7（不包含0x/X前缀）/ 3~9（包含0x/X前缀）。  默认值：无  配置原则：无                                  |
| ANALYSETYPE    | 解析方式                        | 可选必选说明：必选参数  参数含义：该参数用于控制Proxy SMF S8获取归属地PGW地址的方式。  数据来源：本端规划 取值范围： “LOCAL_FIRST（本地配置优先）”：本地配置未命中时尝试使用DNS Server数据。“SERVER_FIRST（DNS Server配置优先）”：DNS Server数据未命中时尝试使用本地配置。  默认值：无  配置原则：  配置为LOCAL_FIRST时，表示优先从本地配置获取归属PGW-C的IP；配置为SERVER_FIRST时，表示优先从DNS获取归属PGW-C的IP。                                                     |
| QUERYTYPE      | 查询类型                        | 可选必选说明：必选参数  参数含义：该参数用于控制Proxy SMF S8特性中根据本地配置查找归属地PGW地址时的查询类型。  数据来源：本端规划 取值范围： IMSI_FIRST（IMSI优先）MSISDN_FIRST（MSISDN优先）  默认值：无  配置原则：无                                                                                                                                                                                     |
| SUPPORTIPTYPE  | 支持的IP类型                     | 可选必选说明：必选参数  参数含义：该参数用于配置本网络可以为该漫游用户提供服务的IP地址类型。  数据来源：本端规划 取值范围： IPV4（IPV4）IPV6（IPV6）IPV4V6（IPV4V6）  默认值：无  配置原则：  该配置必须和网络规划一致，否则会导致用户激活失败。该参数将用于与用户签约IP地址类型、UE请求IP地址类型取交集作为Proxy SMF S8发送给PGW的IP地址类型。                                                                                                                     |
| HOMEROUTESW    | 语音业务回归属地功能开关                | 可选必选说明：可选参数  参数含义：该参数用于控制运营商语音业务回归属地。  数据来源：本端规划 取值范围： OFF（关闭）ON（开启）  默认值：无  配置原则：  当DNN是语音业务DNN时该参数生效。开关开启时，IMS语音业务接入时漫游网关作为Proxy SMF/Proxy SMF S8形态对接归属地HSMF/PGW；开关关闭时，IMS语音业务接入时漫游网关作为N16SMF形态，本地直出SVC。                                                                                                                   |
| IWKSW          | 互操作开关                       | 可选必选说明：该参数在"CTRLTYPE"配置为"DNN_LEVEL"时为条件可选参数。  参数含义：该参数用于配置本网络是否支持45G互操作。  数据来源：本端规划 取值范围： OFF（关闭）NR_TO_EPS_ENABLE（支持5G到4G切换）  默认值：无  配置原则：无                                                                                                                                                                                  |
| HOMEITFMODE    | 归属地接口模式                     | 可选必选说明：可选参数  参数含义：该参数用于指示归属地接口模式。  数据来源：本端规划 取值范围： “KEEP_S8（保持S8）”：保持S8“LINK_LEFT（与左侧联动）”：与左侧联动  默认值：无  配置原则：  当SMF作为ProxySMFS8部署时，配置参数取值为“KEEP_S8(保持S8)”并且SET SMFFUNC的PROSMFS8SUP参数需要配置为“Support(支持)”。当SMF作为proxy SMF部署时， 配置参数取值为“LINK_LEFT(与左侧联动)”。                                                                        |
| DATAHRSW       | 数据业务回归属地功能开关                | 可选必选说明：该参数在"HOMEITFMODE"配置为"LINK_LEFT"时为条件可选参数。  参数含义：该参数用于指示数据业务是否回归属地。  数据来源：本端规划 取值范围： “OFF（数据业务回归属地功能关闭）”：数据业务回归属地功能关闭“ON（数据业务回归属地功能开启）”：数据业务回归属地功能开启  默认值：无  配置原则：  本参数仅在HOMEITFMODE 配置为“LINK_LEFT(与左侧联动)”时生效。                                                                                                          |
| DNNFMT         | DNN格式                       | 可选必选说明：可选参数  参数含义：该参数用于PROXYSMF选择归属地SMF时，服务发现消息中携带的DNN的格式。  数据来源：全网规划 取值范围： NI（仅网络标识）NIANDOI（完整DNN）  默认值：无  配置原则：无                                                                                                                                                                                                           |

## 使用实例

假设运营商需要增加一个MCC为“460”、MNC为“00”、控制类型为整系统级别、Proxy QoS来源为V-SMF、TAC转换策略与E-UTRAN Cell Identifier转换策略均为默认方式、解析方式为本地配置优先并且支持的IP类型为IPV4V6、查询类型为IMSI\_FIRST的proxy SMF功能控制,DNN格式为仅网络标识时，添加PROXYSMFCTRL配置。

```
ADD PROXYSMFCTRL:MCC="460",MNC="00",CTRLTYPE=GLOBAL_LEVEL,PROXYQOSSOURCE=V-SMF,TACCONVPOLICY=Default,CELLIDCONVPLY=Default,ANALYSETYPE=LOCAL_FIRST,SUPPORTIPTYPE=IPV4V6,QUERYTYPE=IMSI_FIRST,DNNFMT=NI;
```