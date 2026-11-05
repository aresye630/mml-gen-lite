# 设置APN L2TP CTRL配置（SET APNL2TPCTRL）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于设置APN L2TP CTRL配置。

## 注意事项

- 该命令执行后立即生效。

- 在每次执行ADD APN命令时会自动为本命令增加一条记录，记录中参数的初始设置值如下：L2TPSWITCH：DISABLE，ICCN\_PROXYAUTH：DISABLE，COMMONUSERUSED：DISABLE，DEDICATEDBEARSW：DISABLE，PASSWORD：\*\*\*\*\*，CFMPASSWORD：\*\*\*\*\*，USERNAMEPLCY：DISABLE，PASSWORDPLCY：DISABLE，USERNAME：NULL。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识            | 参数名称                   | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|:----------------|:-----------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| APN             | APN名称                  | 可选必选说明：必选参数  参数含义：APN名称。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是0~63。字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“ ” ”、“ ` ”特殊字符，不区分大小写。  默认值：无。  配置原则：  该参数使用ADD APN命令配置生成。                                                                                                                                                                                                                                                                                                       |
| L2TPSWITCH      | 支持L2TP功能               | 可选必选说明：可选参数  参数含义：该参数用于指定是否支持L2TP功能。  数据来源：本端规划 取值范围： DISABLE（ 不使能）ENABLE（使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNL2TPCTRL查询当前参数配置值。  配置原则：无                                                                                                                                                                                                                                                                                                                                                                                             |
| ICCN_PROXYAUTH  | MSISDN作为ICCN代理认证用户名    | 可选必选说明：该参数在"L2TPSWITCH"配置为"ENABLE"时为条件可选参数。  参数含义：控制UNC在指定APN下的L2TP用户接入时，是否支持MSISDN作为用户名带给UPF，UPF通过ICCN消息中proxy-auth-username信元带给LNS，后续流程的鉴权方式为PAP。该参数与参数PASSWORD配合使用，该参数配置为ENABLE且参数PASSWORD没有配置密码场景，默认密码为password。  数据来源：本端规划 取值范围： DISABLE（ 不使能）ENABLE（使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNL2TPCTRL查询当前参数配置值。  配置原则：  “USERNAMEPLCY”和“PASSWORDPLCY”的优先级高于本参数。                                                                                                                                                                     |
| COMMONUSERUSED  | 与LNS进行用户鉴权的用户名密码使用公用配置 | 可选必选说明：该参数在"L2TPSWITCH"配置为"ENABLE"时为条件可选参数。  参数含义：控制UNC在指定APN下的L2TP用户接入，UPF充当LAC与LNS进行用户鉴权时，UNC是否使用SET APNAUTHATTR配置的CommonUserName和CommonUserPass作为用户名密码通过UPF带给LNS，用户名密码替换后的后续流程的鉴权方式为PAP。CommonUserName和CommonUserPass没有配置时，UNC通过UPF发给LNS的ICCN消息不带用户名密码。如果APN_BYTE2、BIT574，SET APNL2TPCTRL的ICCN_PROXYAUTH参数配置不是0，用户名和密码还会根据APN_BYTE2、BIT574，SET APNL2TPCTRL的ICCN_PROXYAUTH参数的配置再次进行替换。  数据来源：本端规划 取值范围： DISABLE（ 不使能）ENABLE（使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNL2TPCTRL查询当前参数配置值。  配置原则：  “USERNAMEPLCY”和“PASSWORDPLCY”的优先级高于本参数。 |
| DEDICATEDBEARSW | L2TP支持专有承载功能开关         | 可选必选说明：该参数在"L2TPSWITCH"配置为"ENABLE"时为条件可选参数。  参数含义：配置指定APN是否支持创建L2TP专有承载。  数据来源：本端规划 取值范围： DISABLE（ 不使能）ENABLE（使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNL2TPCTRL查询当前参数配置值。  配置原则：无                                                                                                                                                                                                                                                                                                                                                         |
| PASSWORD        | L2TP用户鉴权密码             | 可选必选说明：该参数在"L2TPSWITCH"配置为"ENABLE"时为条件可选参数。  参数含义：L2TP用户鉴权密码。  数据来源：本端规划  取值范围：Pwd，取值范围是1~128。输入PASSWORD时，必须同时输入确认密码CFMPASSWORD，且密码相同。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNL2TPCTRL查询当前参数配置值。  配置原则：无                                                                                                                                                                                                                                                                                                                                    |
| CFMPASSWORD     | 确认L2TP用户鉴权密码           | 可选必选说明：该参数在"L2TPSWITCH"配置为"ENABLE"时为条件可选参数。  参数含义：确认L2TP用户鉴权密码。  数据来源：本端规划  取值范围：Pwd，取值范围是1~128。输入CFMPASSWORD时，必须同时输入确认密码PASSWORD，且密码相同。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNL2TPCTRL查询当前参数配置值。  配置原则：无                                                                                                                                                                                                                                                                                                                                  |
| USERNAMEPLCY    | L2TP鉴权用户名使用策略          | 可选必选说明：该参数在"L2TPSWITCH"配置为"ENABLE"时为条件可选参数。  参数含义：该参数用于指定L2TP用户鉴权时，SMF向UPF发送的消息中携带用户名的策略。  数据来源：本端规划 取值范围： “DISABLE（不使能）”：按照COMMONUSERUSED参数含义中的处理原则实现。“USECONFIG（使用配置）”：使用参数USERNAME的取值。“PCOPRIOR（优先使用PCO）”：优先使用PCO中的取值，如果PCO中取值为空则用使用参数USERNAME的取值。“USEPCO（使用PCO）”：使用PCO中的取值。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNL2TPCTRL查询当前参数配置值。  配置原则：无                                                                                                                                                                                           |
| PASSWORDPLCY    | L2TP鉴权密码使用策略           | 可选必选说明：该参数在"L2TPSWITCH"配置为"ENABLE"时为条件可选参数。  参数含义：该参数用于指定L2TP用户鉴权时，SMF向UPF发送的消息中携带用户密码的策略。  数据来源：本端规划 取值范围： “DISABLE（不使能）”：按照COMMONUSERUSED参数含义中的处理原则实现。“USECONFIG（使用配置）”：使用参数PASSWORD的取值。“PCOPRIOR（优先使用PCO）”：优先使用PCO中的取值，如果PCO中取值为空则用使用参数PASSWORD的取值。“USEPCO（使用PCO）”：使用PCO中的取值。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNL2TPCTRL查询当前参数配置值。  配置原则：  当鉴权方式为CHAP时，该参数不生效。                                                                                                                                                                      |
| USERNAME        | L2TP用户鉴权用户名            | 可选必选说明：该参数在"L2TPSWITCH"配置为"ENABLE"时为条件可选参数。  参数含义：该参数用于指定L2TP用户鉴权时，SMF向UPF发送的消息中携带的用户名。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是0~63。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST APNL2TPCTRL查询当前参数配置值。  配置原则：  输入单空格将删除该参数已有配置项。                                                                                                                                                                                                                                                                                                                             |

## 使用实例

设置APN为huawei.com的用户使用L2TP方式激活：

```
SET APNL2TPCTRL: APN="huawei.com", L2TPSWITCH=ENABLE;
```