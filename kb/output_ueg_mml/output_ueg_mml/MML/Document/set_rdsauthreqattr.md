# 设置Radius鉴权请求消息携带的属性（SET RDSAUTHREQATTR）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：PGW-C、GGSN、SMF**

该命令用来设置RADIUS服务器组的可选鉴权消息属性。

## 注意事项

- 该命令执行后立即生效。

- 需要先执行ADD RDSSVRGRP命令，才能执行SET RDSAUTHREQATTR命令。
- RDSSVRGRPNAME的值由ADD RDSSVRGRP命令添加，ACCTSESSIONID、NASID、IMSI、CHARGINGID、PREPAIDIND、GGSNIP、SGSNIP、REQUESTAPN、GGSNVENDOR、GGGSNVERION、RQAUTHTICATOR、NASPORTIDSW、WLANADDR的初始设置值是DISABLE，ACCTMULSESSID、EVENTTIME、CALLINGSTATID的初始设置值是ENABLE，NASIDTYPE、NASPORTID的初始设置值是NULL，NASIDVALUE的初始设置值是UNC。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识          | 参数名称                            | 参数说明                                                                                                                                                                                                                                                                                                      |
|:--------------|:--------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RDSSVRGRPNAME | RADIUS服务器组名称                    | 可选必选说明：必选参数  参数含义：RADIUS服务器组名。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是1~31。  默认值：无。  配置原则：  需要确保RADIUS服务器组名称已经通过ADD RDSSVRGRP配置。                                                                                                                                                                                   |
| ACCTSESSIONID | Acct-Session-Id                 | 可选必选说明：可选参数  参数含义：指定是否支持鉴权请求消息中携带Acct-Session-Id属性。  数据来源：本端规划 取值范围： “DISABLE（禁止）”：否。“ENABLE（允许）”：是。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST RDSAUTHREQATTR查询当前参数配置值。  配置原则：无                                                                                                                            |
| NASID         | NAS-ID                          | 可选必选说明：可选参数  参数含义：指定是否支持鉴权请求消息中携带NAS-ID属性。  数据来源：本端规划 取值范围： “DISABLE（禁止）”：否。“ENABLE（允许）”：是。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST RDSAUTHREQATTR查询当前参数配置值。  配置原则：无                                                                                                                                     |
| NASIDTYPE     | NAS ID Type                     | 可选必选说明：该参数在"NASID"配置为"ENABLE"时为条件必选参数。  参数含义：指定NAS-ID类型。  数据来源：本端规划 取值范围： “APN（APN）”：携带的nas-id-value信元为用户所在的APN名。“SPECIFIC_VALUE（指定NAS ID值）”：携带的nas-id-value信元为用户自定义的字符串。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST RDSAUTHREQATTR查询当前参数配置值。  配置原则：无                                                       |
| NASIDVALUE    | NAS ID Value                    | 可选必选说明：该参数在"NASIDTYPE"配置为"SPECIFIC_VALUE"时为条件必选参数。  参数含义：指定NAS-ID类型具体值。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是1~63。不区分大小写。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST RDSAUTHREQATTR查询当前参数配置值。  配置原则：无                                                                                                              |
| IMSI          | IMSI                            | 可选必选说明：可选参数  参数含义：指定是否支持鉴权请求消息中携带224号IMSI属性。  数据来源：本端规划 取值范围： “DISABLE（禁止）”：否。“ENABLE（允许）”：是。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST RDSAUTHREQATTR查询当前参数配置值。  配置原则：无                                                                                                                                   |
| CHARGINGID    | Charging-ID                     | 可选必选说明：可选参数  参数含义：指定是否支持鉴权请求消息中携带225号Charging-ID属性。  数据来源：本端规划 取值范围： “DISABLE（禁止）”：否。“ENABLE（允许）”：是。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST RDSAUTHREQATTR查询当前参数配置值。  配置原则：无                                                                                                                            |
| PREPAIDIND    | Prepaid-ind                     | 可选必选说明：可选参数  参数含义：指定是否支持鉴权请求消息中携带226号Prepaid-ind属性。  数据来源：本端规划 取值范围： “DISABLE（禁止）”：否。“ENABLE（允许）”：是。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST RDSAUTHREQATTR查询当前参数配置值。  配置原则：无                                                                                                                            |
| GGSNIP        | GGSN-IP                         | 可选必选说明：可选参数  参数含义：指定是否支持鉴权请求消息中携带227号GGSN-IP属性。  数据来源：本端规划 取值范围： “DISABLE（禁止）”：否。“ENABLE（允许）”：是。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST RDSAUTHREQATTR查询当前参数配置值。  配置原则：无                                                                                                                                |
| SGSNIP        | SGSN (S-GW)-IP                  | 可选必选说明：可选参数  参数含义：指定是否支持鉴权请求消息中携带228号SGSN（SGW）-IP属性。  数据来源：本端规划 取值范围： “DISABLE（禁止）”：否。“ENABLE（允许）”：是。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST RDSAUTHREQATTR查询当前参数配置值。  配置原则：无                                                                                                                           |
| REQUESTAPN    | Requested-APN                   | 可选必选说明：可选参数  参数含义：指定是否支持鉴权请求消息中携带HW-Requested-APN属性。  数据来源：本端规划 取值范围： “DISABLE（禁止）”：否。“ENABLE（允许）”：是。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST RDSAUTHREQATTR查询当前参数配置值。  配置原则：无                                                                                                                           |
| GGSNVENDOR    | GGSN-Vendor                     | 可选必选说明：可选参数  参数含义：指定是否支持鉴权请求消息中携带GGSN-Vendor属性。  数据来源：本端规划 取值范围： “DISABLE（禁止）”：否。“ENABLE（允许）”：是。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST RDSAUTHREQATTR查询当前参数配置值。  配置原则：无                                                                                                                                |
| GGSNVERION    | GGSN-Version                    | 可选必选说明：可选参数  参数含义：指定是否支持鉴权请求消息中携带GGSN-Version属性。  数据来源：本端规划 取值范围： “DISABLE（禁止）”：否。“ENABLE（允许）”：是。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST RDSAUTHREQATTR查询当前参数配置值。  配置原则：无                                                                                                                               |
| RQAUTHTICATOR | Request Authenticator           | 可选必选说明：可选参数  参数含义：指定是否支持鉴权请求消息中携带Message-Authenticator属性。  数据来源：本端规划 取值范围： “DISABLE（禁止）”：否。“ENABLE（允许）”：是。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST RDSAUTHREQATTR查询当前参数配置值。  配置原则：无                                                                                                                      |
| ACCTMULSESSID | Acct-Multi-Session-Id           | 可选必选说明：可选参数  参数含义：指定是否支持鉴权请求消息中携带Acct-Multi-Session-ID属性。  数据来源：本端规划 取值范围： “DISABLE（禁止）”：否。“ENABLE（允许）”：是。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST RDSAUTHREQATTR查询当前参数配置值。  配置原则：无                                                                                                                      |
| EVENTTIME     | Event-Timestamp                 | 可选必选说明：可选参数  参数含义：指定是否支持鉴权请求消息中携带Event-Time属性。  数据来源：本端规划 取值范围： “DISABLE（禁止）”：否。“ENABLE（允许）”：是。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST RDSAUTHREQATTR查询当前参数配置值。  配置原则：无                                                                                                                                 |
| NASPORTIDSW   | NAS-Port-Id属性开关                 | 可选必选说明：可选参数  参数含义：指定是否支持携带NAS-Port-Id属性。  数据来源：本端规划 取值范围： “DISABLE（禁止）”：否。“ENABLE（允许）”：是。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST RDSAUTHREQATTR查询当前参数配置值。  配置原则：无                                                                                                                                       |
| NASPORTID     | NAS-Port-Id属性值                  | 可选必选说明：该参数在"NASPORTIDSW"配置为"ENABLE"时为条件可选参数。  参数含义：指定NAS-Port-Id信元携带的填充值。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是1~16。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST RDSAUTHREQATTR查询当前参数配置值。  配置原则：  输入单空格将删除该参数已有配置项。  当参数"NASPORTIDSW"由“DISABLE”到"ENABLE"时，如果该字段没有输入，默认配置“UNC”；由“ENABLE”到"ENABLE"时，如果该字段没有输入，默认用原配置。 |
| WLANADDR      | UE-Local-IP-Address和UE-UDP-Port | 可选必选说明：可选参数  参数含义：指定是否支持鉴权请求消息中携带WLAN地址。  数据来源：本端规划 取值范围： “DISABLE（禁止）”：否。“ENABLE（允许）”：是。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST RDSAUTHREQATTR查询当前参数配置值。  配置原则：无                                                                                                                                       |
| CALLINGSTATID | Calling-Station-Id              | 可选必选说明：可选参数  参数含义：该参数用于指定鉴权请求消息中是否携带Calling-Station-Id属性。  数据来源：本端规划 取值范围： “DISABLE（不使能）”：否。“ENABLE（使能）”：是。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST RDSAUTHREQATTR查询当前参数配置值。  配置原则：无                                                                                                                     |

## 使用实例

假如运营商需要配置名为“radiusgroup”的Radius服务器组为支持携带Acct-Session-ID属性，不携带NAS-ID属性，根据Radius鉴权消息中携带的这些消息属性字段进行相关的业务控制，则使用该实例：

```
SET RDSAUTHREQATTR:RDSSVRGRPNAME="radiusgroup",NASID=DISABLE;
```