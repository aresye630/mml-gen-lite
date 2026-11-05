# 设置支持的Radius鉴权响应消息私有属性（SET RDSAUTHRSPATTR）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：PGW-C、GGSN、SMF**

该命令用于配置是否支持解析RADIUS鉴权服务器组返回的运营商私有信元。对于RADIUS鉴权服务器返回的鉴权响应消息中携带的运营商私有信元，通过该命令配置是否对其进行解析处理。

## 注意事项

- 该命令执行后立即生效。

- RADIUS鉴权服务器下发配置后，如果使用此命令配置为不支持解析计费过程所需的相关信元（Operator-Charging-Rule-Base-Name，Operator-Primary-Event-Charging-Function-Name、Operator-Second-Event-Charging-Function-Name或Operator-Vpn-Name信元），将可能导致计费不正确。
- 需要先执行ADD RDSSVRGRP命令，才能执行SET RDSAUTHRSPATTR命令。
- RDSSVRGRPNAME的值由ADD RDSSVRGRP命令添加，CHARGERULEBASE、EVENTFUNC、VPNINSTANCE的初始设置值是ENABLE，SESSIDLETIMESW的初始设置值是DISABLE。
- 当SESSIDLETIMESW设置值是ENABLE时，AAA下发的最大会话在线时长和空闲上下文时长比本端配置（APNIDLETIME或DFTIDLETIME）的优先级高。
- Access-Accept消息可以通过在标准属性中携带Primary-Dns（Attribute Number为135）和Secondary-Dns（Attribute Number为136）信元或在Vendor-Specific（Attribute Number为26）扩展属性中携带MS-Primary-DNS-Server（Vendor ID为311、Attribute Number为28）/MS-Secondary-DNS-Server（Vendor ID为311、Attribute Number为29）、CISCO-AVPair（Vendor ID为9、Attribute Number为1）信元、HW-Client-Primary-DNS（Vendor ID为2011、Attribute Number为135）和HW-Client-Secondary-DNS（Vendor ID为2011、Attribute Number为136）信元来下发主/备DNS服务器地址。

  - 当携带HW-Client-Primary-DNS/HW-Client-Secondary-DNS时，优先使用HW-Client-Primary-DNS/HW-Client-Secondary-DNS作为主/备DNS服务器地址。

  - 当未携带HW-Client-Primary-DNS/HW-Client-Secondary-DNS时，使用DNSSVRPRIORITY参数控制优先使用标准属性或Vendor-Specific扩展属性中携带的DNS服务器地址作为主/备DNS服务器地址。其中，Vendor-Specific扩展属性中的MS-Primary-DNS-Server/MS-Secondary-DNS-Server和CISCO-AVPair之间的优先级以携带顺序为准。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识           | 参数名称                             | 参数说明                                                                                                                                                                                                                                                                                                                                            |
|:---------------|:---------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RDSSVRGRPNAME  | RADIUS服务器组名称                     | 可选必选说明：必选参数  参数含义：该参数用于指定RADIUS服务器组名。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是1~31。  默认值：无。  配置原则：  需要确保RADIUS服务器组名称已经通过ADD RDSSVRGRP配置。                                                                                                                                                                                                                  |
| CHARGERULEBASE | Operator-Charging-Rule-Base-Name | 可选必选说明：可选参数  参数含义：该参数用于配置是否支持解析鉴权回应消息中的Operator-Charging-Rule-Base-Name信元。  数据来源：本端规划 取值范围： “DISABLE（禁止）”：否。“ENABLE（允许）”：是。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST RDSAUTHRSPATTR查询当前参数配置值。  配置原则：  Operator-Charging-Rule-Base-Name信元用于标识计费规则组名称，包含内容计费相关的所有计费策略和控制策略。  此参数当前版本不支持。                                                          |
| EVENTFUNC      | Event-Charging-Function-Name     | 可选必选说明：可选参数  参数含义：该参数用于配置是否支持解析鉴权回应消息中的Operator-Primary-Event-Charging-Function-Name和Operator-Second-Event-Charging-Function-Name信元。  数据来源：本端规划 取值范围： “DISABLE（禁止）”：否。“ENABLE（允许）”：是。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST RDSAUTHRSPATTR查询当前参数配置值。  配置原则：  Event-Charging-Function-Name信元用于标识OCS服务器组的名称，如果RADIUS鉴权服务器下发这个参数并解析，支持用户进行在线计费。 |
| VPNINSTANCE    | Operator-Vpn-Name                | 可选必选说明：可选参数  参数含义：该参数用于配置是否支持解析鉴权回应消息中的Operator-Vpn-Name信元。  数据来源：本端规划 取值范围： “DISABLE（禁止）”：否。“ENABLE（允许）”：是。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST RDSAUTHRSPATTR查询当前参数配置值。  配置原则：  Operator-Vpn-Name信元用于标识RADIUS鉴权服务器下发的真实APN名。                                                                                                             |
| SESSIDLETIMESW | 会话时长和空闲上下文时长开关                   | 可选必选说明：可选参数  参数含义：该参数用于设置最大会话在线时长和空闲上下文时长功能开关。  数据来源：本端规划 取值范围： “DISABLE（禁止）”：否。“ENABLE（允许）”：是。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST RDSAUTHRSPATTR查询当前参数配置值。  配置原则：  如果从DISABLE修改为ENABLE，则对新激活的用户生效。                                                                                                                                       |
| DNSSVRPRIORITY | DNS服务器信元取值优先级                    | 可选必选说明：可选参数  参数含义：该参数用于控制UNC使用Access-Accept消息中的DNS服务器地址优先从Access-Accept消息的标准属性中获取还是从Vendor-Specific扩展属性中获取。  数据来源：本端规划 取值范围： STDATTRIBUTES（标准属性优先级更高）VENDORSPECIFIC（Vendor-Specific扩展属性优先级更高）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST RDSAUTHRSPATTR查询当前参数配置值。  配置原则：无                                                                         |

## 使用实例

假如运营商需要配置名为“rds”的RADIUS服务器组的鉴权响应消息中，不解析Operator-Primary-Event-Charging-Function-Name和Operator-Second-Event-Charging-Function-Name信元，不解析Operator-Charging-Base-Rule信元，只解析Operator-Vpn-Name信元，则使用该实例：

```
SET RDSAUTHRSPATTR:RDSSVRGRPNAME="rds",CHARGERULEBASE=DISABLE,EVENTFUNC=DISABLE,VPNINSTANCE=ENABLE;
```