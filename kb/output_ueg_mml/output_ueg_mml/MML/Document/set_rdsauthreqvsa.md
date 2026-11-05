# 设置RADIUS鉴权请求携带的私有扩展属性（SET RDSAUTHREQVSA）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：PGW-C、GGSN、SMF**

该命令用来设置RADIUS服务器组的鉴权请求消息中是否支持各个3GPP（26/10415）扩展属性。

## 注意事项

- 该命令执行后立即生效。

- 使用该命令设置RADIUS服务器组的可选鉴权消息属性，当有用户需要去这个RADIUS服务器组鉴权时，依据这条命令的配置携带或者不携带某些鉴权消息属性。
- 需要先执行ADD RDSSVRGRP命令，才能执行SET RDSAUTHREQVSA命令。
- RDSSVRGRPNAME的值由ADD RDSSVRGRP命令添加，THREEGPP、CGIPV6ADDRESS的初始设置值是DISABLE，IMSI、CHARGINGID、PDPTYPE、CGADDRESS、NEGOTIAEDQOS、SGSNSGWADDRESS、GGSNADDRESS、IMSIMCCMNC、GGSNMCCMNC、NSAPI、SELECTIONMODE、CHARGINGCHAR、SGSNSGWMCCMNC、IMEISV、RATTYPE、ULI、MSTIMEZONE、NEGOTIAEDDSCP、SGSNIPV6ADDRESS、GGSNIPV6ADDRESS的初始设置值是ENABLE。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识            | 参数名称                             | 参数说明                                                                                                                                                                                                                              |
|:----------------|:---------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RDSSVRGRPNAME   | RADIUS服务器组名称                     | 可选必选说明：必选参数  参数含义：该参数用于指定鉴权服务器组名。  数据来源：对端协商  取值范围：字符串类型，输入长度范围是1~31。  默认值：无。  配置原则：  配置RADIUS服务器组名前，需要先使用ADD RDSSVRGRP命令配置RADIUS服务器组信息。                                                                                          |
| THREEGPP        | 3GPP私有扩展属性开关                     | 可选必选说明：可选参数  参数含义：该参数用于配置是否支持鉴权请求消息中携带26/10415这组属性。  数据来源：对端协商 取值范围： “DISABLE（禁止）”：否。“ENABLE（允许）”：是。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST RDSAUTHREQVSA查询当前参数配置值。  配置原则：无                                                     |
| IMSI            | 3GPP-IMSI                        | 可选必选说明：该参数在"THREEGPP"配置为"ENABLE"时为条件可选参数。  参数含义：该参数用于配置是否支持鉴权请求消息中携带3GPP-IMSI属性。  数据来源：对端协商 取值范围： “DISABLE（禁止）”：否。“ENABLE（允许）”：是。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST RDSAUTHREQVSA查询当前参数配置值。  配置原则：无                        |
| CHARGINGID      | 3GPP-Charging-ID                 | 可选必选说明：该参数在"THREEGPP"配置为"ENABLE"时为条件可选参数。  参数含义：该参数用于配置是否支持鉴权请求消息中携带3GPP-Charging-ID属性。  数据来源：对端协商 取值范围： “DISABLE（禁止）”：否。“ENABLE（允许）”：是。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST RDSAUTHREQVSA查询当前参数配置值。  配置原则：无                 |
| PDPTYPE         | 3GPP-PDP-Type                    | 可选必选说明：该参数在"THREEGPP"配置为"ENABLE"时为条件可选参数。  参数含义：该参数用于配置是否支持鉴权请求消息中携带3GPP-PDP-Type属性。  数据来源：对端协商 取值范围： “DISABLE（禁止）”：否。“ENABLE（允许）”：是。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST RDSAUTHREQVSA查询当前参数配置值。  配置原则：无                    |
| CGADDRESS       | 3GPP-CG-Address                  | 可选必选说明：该参数在"THREEGPP"配置为"ENABLE"时为条件可选参数。  参数含义：该参数用于配置是否支持鉴权请求消息中携带3GPP-CG-Address属性。  数据来源：对端协商 取值范围： “DISABLE（禁止）”：否。“ENABLE（允许）”：是。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST RDSAUTHREQVSA查询当前参数配置值。  配置原则：无                  |
| NEGOTIAEDQOS    | 3GPP-GPRS-Negotiated-QoS-Profile | 可选必选说明：该参数在"THREEGPP"配置为"ENABLE"时为条件可选参数。  参数含义：该参数用于配置是否支持鉴权请求消息中携带3GPP-GPRS-Negotiated-QoS-Profile属性。  数据来源：对端协商 取值范围： “DISABLE（禁止）”：否。“ENABLE（允许）”：是。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST RDSAUTHREQVSA查询当前参数配置值。  配置原则：无 |
| SGSNSGWADDRESS  | 3GPP-SGSN(SGW)-Address           | 可选必选说明：该参数在"THREEGPP"配置为"ENABLE"时为条件可选参数。  参数含义：该参数用于配置是否支持鉴权请求消息中携带3GPP-SGSN（SGW）-Address属性。  数据来源：对端协商 取值范围： “DISABLE（禁止）”：否。“ENABLE（允许）”：是。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST RDSAUTHREQVSA查询当前参数配置值。  配置原则：无           |
| GGSNADDRESS     | 3GPP-GGSN-Address                | 可选必选说明：该参数在"THREEGPP"配置为"ENABLE"时为条件可选参数。  参数含义：该参数用于配置是否支持鉴权请求消息中携带3GPP-GGSN-Address属性。  数据来源：对端协商 取值范围： “DISABLE（禁止）”：否。“ENABLE（允许）”：是。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST RDSAUTHREQVSA查询当前参数配置值。  配置原则：无                |
| IMSIMCCMNC      | 3GPP-IMSI-MCC-MNC                | 可选必选说明：该参数在"THREEGPP"配置为"ENABLE"时为条件可选参数。  参数含义：该参数用于配置是否支持鉴权请求消息中携带3GPP-IMSI-MCC-MNC属性。  数据来源：对端协商 取值范围： “DISABLE（禁止）”：否。“ENABLE（允许）”：是。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST RDSAUTHREQVSA查询当前参数配置值。  配置原则：无                |
| GGSNMCCMNC      | 3GPP-GGSN-MCC-MNC                | 可选必选说明：该参数在"THREEGPP"配置为"ENABLE"时为条件可选参数。  参数含义：该参数用于配置是否支持鉴权请求消息中携带3GPP-GGSN-MCC-MNC属性。  数据来源：对端协商 取值范围： “DISABLE（禁止）”：否。“ENABLE（允许）”：是。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST RDSAUTHREQVSA查询当前参数配置值。  配置原则：无                |
| NSAPI           | 3GPP-NSAPI                       | 可选必选说明：该参数在"THREEGPP"配置为"ENABLE"时为条件可选参数。  参数含义：该参数用于配置是否支持鉴权请求消息中携带3GPP-NSAPI属性。  数据来源：对端协商 取值范围： “DISABLE（禁止）”：否。“ENABLE（允许）”：是。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST RDSAUTHREQVSA查询当前参数配置值。  配置原则：无                       |
| SELECTIONMODE   | 3GPP-Selection-Mode              | 可选必选说明：该参数在"THREEGPP"配置为"ENABLE"时为条件可选参数。  参数含义：该参数用于配置是否支持鉴权请求消息中携带3GPP-Selection-Mode属性。  数据来源：对端协商 取值范围： “DISABLE（禁止）”：否。“ENABLE（允许）”：是。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST RDSAUTHREQVSA查询当前参数配置值。  配置原则：无              |
| CHARGINGCHAR    | 3GPP-Charging-Characteristics    | 可选必选说明：该参数在"THREEGPP"配置为"ENABLE"时为条件可选参数。  参数含义：该参数用于配置是否支持鉴权请求消息中携带3GPP-Charging-Characteristics属性。  数据来源：对端协商 取值范围： “DISABLE（禁止）”：否。“ENABLE（允许）”：是。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST RDSAUTHREQVSA查询当前参数配置值。  配置原则：无    |
| SGSNSGWMCCMNC   | 3GPP-SGSN(SGW)-MCC-MNC           | 可选必选说明：该参数在"THREEGPP"配置为"ENABLE"时为条件可选参数。  参数含义：该参数用于配置是否支持鉴权请求消息中携带3GPP-SGSN（SGW）-MCC-MNC属性。  数据来源：对端协商 取值范围： “DISABLE（禁止）”：否。“ENABLE（允许）”：是。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST RDSAUTHREQVSA查询当前参数配置值。  配置原则：无           |
| IMEISV          | 3GPP-IMEISV                      | 可选必选说明：该参数在"THREEGPP"配置为"ENABLE"时为条件可选参数。  参数含义：该参数用于配置是否支持鉴权请求消息中携带3GPP-IMEISV属性。  数据来源：对端协商 取值范围： “DISABLE（禁止）”：否。“ENABLE（允许）”：是。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST RDSAUTHREQVSA查询当前参数配置值。  配置原则：无                      |
| RATTYPE         | 3GPP-RAT-Type                    | 可选必选说明：该参数在"THREEGPP"配置为"ENABLE"时为条件可选参数。  参数含义：该参数用于配置是否支持鉴权请求消息中携带3GPP-RAT-Type属性。  数据来源：对端协商 取值范围： “DISABLE（禁止）”：否。“ENABLE（允许）”：是。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST RDSAUTHREQVSA查询当前参数配置值。  配置原则：无                    |
| ULI             | 3GPP-User-Location-Info          | 可选必选说明：该参数在"THREEGPP"配置为"ENABLE"时为条件可选参数。  参数含义：该参数用于配置是否支持鉴权请求消息中携带3GPP-User-Location-Info属性。  数据来源：对端协商 取值范围： “DISABLE（禁止）”：否。“ENABLE（允许）”：是。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST RDSAUTHREQVSA查询当前参数配置值。  配置原则：无          |
| MSTIMEZONE      | 3GPP-MS-TimeZone                 | 可选必选说明：该参数在"THREEGPP"配置为"ENABLE"时为条件可选参数。  参数含义：该参数用于配置是否支持鉴权请求消息中携带3GPP-MS-TimeZone属性。  数据来源：对端协商 取值范围： “DISABLE（禁止）”：否。“ENABLE（允许）”：是。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST RDSAUTHREQVSA查询当前参数配置值。  配置原则：无                 |
| NEGOTIAEDDSCP   | 3GPP-Negotiated-DSCP             | 可选必选说明：该参数在"THREEGPP"配置为"ENABLE"时为条件可选参数。  参数含义：该参数用于配置是否支持鉴权请求消息中携带3GPP-Negotiated-DSCP属性。  数据来源：对端协商 取值范围： “DISABLE（禁止）”：否。“ENABLE（允许）”：是。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST RDSAUTHREQVSA查询当前参数配置值。  配置原则：无             |
| SGSNIPV6ADDRESS | 3GPP-SGSN-IPv6-Address           | 可选必选说明：该参数在"THREEGPP"配置为"ENABLE"时为条件可选参数。  参数含义：该参数用于配置是否支持鉴权请求消息中携带3GPP-SGSN-IPv6-Address属性。  数据来源：对端协商 取值范围： “DISABLE（禁止）”：否。“ENABLE（允许）”：是。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST RDSAUTHREQVSA查询当前参数配置值。  配置原则：无           |
| GGSNIPV6ADDRESS | 3GPP-GGSN-IPv6-Address           | 可选必选说明：该参数在"THREEGPP"配置为"ENABLE"时为条件可选参数。  参数含义：该参数用于配置是否支持鉴权请求消息中携带3GPP-GGSN-IPv6-Address属性。  数据来源：对端协商 取值范围： “DISABLE（禁止）”：否。“ENABLE（允许）”：是。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST RDSAUTHREQVSA查询当前参数配置值。  配置原则：无           |
| CGIPV6ADDRESS   | 3GPP-CG-IPv6-Address             | 可选必选说明：该参数在"THREEGPP"配置为"ENABLE"时为条件可选参数。  参数含义：该参数用于配置是否支持鉴权请求消息中携带3GPP-CG-IPv6Address属性。  数据来源：对端协商 取值范围： “DISABLE（禁止）”：否。“ENABLE（允许）”：是。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST RDSAUTHREQVSA查询当前参数配置值。  配置原则：无              |

## 使用实例

配置鉴权请求消息中不支持携带3GPP-GPRS-Negotiated-QoS-Profile属性，其余属性使用默认值，也即支持携带：

```
SET RDSAUTHREQVSA:RDSSVRGRPNAME="rds",THREEGPP=ENABLE,NEGOTIAEDQoS=DISABLE;
```