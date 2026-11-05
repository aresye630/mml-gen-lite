# 设置APN访问控制参数（SET CPAPNACCESSCTRL）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：SMF、GGSN、SGW-C、PGW-C**

该命令用于设置APN访问控制策略相关参数信息。

## 注意事项

- 该命令执行后立即生效。

- 在每次执行ADD CPAPN命令时会自动为本命令增加一条记录，记录中参数的初始设置值如下：SMFPGWGGSNVIACC：ENABLE，MAXBANDWIDTH：0，MAXGBRBANDWIDTH：0，MAXPDBNUMBER：0，NULLMSISDN：ENABLE，RESTRICTCHECK：ENABLE，RESTRICTSWITCH：DISABLE，RESTRICTVALUE：0，SELECTMODECHECK：DISABLE，SELECTMODEMS：DISABLE，SELECTMODEMSNET：ENABLE，SELECTMODENET：DISABLE，SMFSGWROACC：ENABLE，SMFSGWVIACC：ENABLE，SMFPGWGGSNROACC：ENABLE，SMFSELMODECHECK：DISABLE，NULLIMSI：INHERIT，PROVRORESTRICT：DISABLE。
- 当前版本不支持此命令的MAXBANDWIDTH、MAXGBRBANDWIDTH参数。
- 当PROVRORESTRICT参数使能，专用APN/DNN用户跨省漫游时，PDN/PDU会话速率会限制为0，需谨慎开启。
- 当PROVRORESTRICT参数从“DISABLE（不使能）”改为“ENABLE（使能）”时，会在新会话建立、发生移动性变更后生效。当PS data off功能开关从“ENABLE（使能）”改为“DISABLE（不使能）”时，立即生效。
- 4G用户接入，开启虚拟APN功能，BIT1833控制是否采用真实APN对应的SET CPAPNACCESSCTRL配置对用户携带的选择模式信息进行检查。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识            | 参数名称                       | 参数说明                                                                                                                                                                                                                                                                                                                                              |
|:----------------|:---------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| APN             | APN名称                      | 可选必选说明：必选参数  参数含义：该参数用于指示APN名称。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是0~63。  默认值：无。  配置原则：  该参数使用ADD CPAPN命令配置生成。                                                                                                                                                                                                                                         |
| SMFPGWGGSNVIACC | SMF/P-GW/GGSN拜访用户接入功能开关    | 可选必选说明：可选参数  参数含义：该参数用于指示是否允许拜访用户接入GGSN或PGW-C或SMF的指定APN。  数据来源：本端规划  取值范围：当取值为DISABLE时，表明拜访用户不允许接入；当取值为ENABLE时，表明允许拜访用户接入；当取值为PROHIBIT时，表明允许接入但是禁止数传。 “DISABLE（不使能）”：拜访用户不允许接入。“ENABLE（使能）”：拜访用户允许接入。“PROHIBIT（禁止）”：拜访用户允许接入，但是不允许数传。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CPAPNACCESSCTRL查询当前参数配置值。  配置原则：无                                  |
| MAXBANDWIDTH    | 最大带宽(兆比特/秒)                | 可选必选说明：可选参数  参数含义：该参数用于指示最大带宽(GBR)。  数据来源：本端规划  取值范围：整数类型，取值范围是0~250000，单位是兆比特每秒。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CPAPNACCESSCTRL查询当前参数配置值。  配置原则：无                                                                                                                                                                                      |
| MAXGBRBANDWIDTH | 最大保证带宽(兆比特/秒)              | 可选必选说明：可选参数  参数含义：该参数用于指示最大保证带宽(GBR)。  数据来源：本端规划  取值范围：整数类型，取值范围是0~3000，单位是兆比特每秒。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CPAPNACCESSCTRL查询当前参数配置值。  配置原则：  该参数已弃用。                                                                                                                                                                              |
| MAXPDBNUMBER    | 最大PDP数目                    | 可选必选说明：可选参数  参数含义：该参数用于指示APN下允许激活的最大PDP上下文数，包含2345G承载数，0表示不控。  数据来源：本端规划  取值范围：整数类型，取值范围是0~16000000。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CPAPNACCESSCTRL查询当前参数配置值。  配置原则：无                                                                                                                                                                   |
| NULLMSISDN      | 不携带MSISDN用户激活策略            | 可选必选说明：可选参数  参数含义：该参数用于指示APN下是否允许不携带MSISDN的用户激活。  数据来源：本端规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CPAPNACCESSCTRL查询当前参数配置值。  配置原则：无                                                                                                                                                                               |
| RESTRICTCHECK   | Apn-restriction本地校验功能开关    | 可选必选说明：可选参数  参数含义：该参数用于指示当开启支持Apn-restriction功能时是否支持对Apn-restriction的本地校验。  数据来源：本端规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CPAPNACCESSCTRL查询当前参数配置值。  配置原则：无                                                                                                                                                     |
| RESTRICTSWITCH  | Apn-restriction功能开关        | 可选必选说明：可选参数  参数含义：该参数用于指示是否支持Apn-restriction功能。用来确定该APN下的用户是否可以在别的APN上建立上下文。  数据来源：本端规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CPAPNACCESSCTRL查询当前参数配置值。  配置原则：无                                                                                                                                                   |
| RESTRICTVALUE   | Apn-restriction最大值         | 可选必选说明：可选参数  参数含义：该参数用于指示允许接入的Apn-restriction的最大值。  数据来源：本端规划  取值范围：整数类型，取值范围是0~4。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CPAPNACCESSCTRL查询当前参数配置值。  配置原则：无                                                                                                                                                                                     |
| SELECTMODECHECK | 用户选择模式检查功能开关               | 可选必选说明：可选参数  参数含义：该参数用于指示是否检查2/3/4G用户携带的选择模式信息。  数据来源：本端规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CPAPNACCESSCTRL查询当前参数配置值。  配置原则：无                                                                                                                                                                                |
| SMFSELMODECHECK | SMF用户选择模式检查功能开关            | 可选必选说明：可选参数  参数含义：该参数用于指示是否检查通过SMF接入的用户携带的选择模式信息。  数据来源：本端规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CPAPNACCESSCTRL查询当前参数配置值。  配置原则：无                                                                                                                                                                              |
| SELECTMODEMS    | Ms提供APN用户激活策略              | 可选必选说明：可选参数  参数含义：该参数用于指示当用户激活消息中携带的Selection Mode取值为1或者用户创建SM上下文消息中携带的信元DnnSelectionMode为UE_DNN_NOT_VERIFIED时，是否允许用户激活。Selection Mode取值为1或者UE_DNN_NOT_VERIFIED，表示激活消息中携带的APN属于如下类型：MS provided APN，subscription not verified。  数据来源：本端规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CPAPNACCESSCTRL查询当前参数配置值。  配置原则：无 |
| SELECTMODEMSNET | Ms/Network提供APN用户激活策略      | 可选必选说明：可选参数  参数含义：该参数用于指示当用户激活消息中携带的Selection Mode取值为0或者用户创建SM上下文消息中携带的信元DnnSelectionMode为VERIFIED时，是否允许用户激活。Selection Mode取值为0或者VERIFIED，表示激活消息中携带的APN属于如下类型：MS or network provided APN， subscribed verified。  数据来源：本端规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CPAPNACCESSCTRL查询当前参数配置值。  配置原则：无                 |
| SELECTMODENET   | Network提供APN用户激活策略         | 可选必选说明：可选参数  参数含义：该参数用于指示当用户激活消息中携带的Selection Mode取值为2或者用户创建SM上下文消息中携带的信元DnnSelectionMode为NW_DNN_NOT_VERIFIED时，是否允许用户激活。Selection Mode取值为2，表示激活消息中携带的APN属于如下类型：Network provided APN，subscription not verified。  数据来源：本端规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CPAPNACCESSCTRL查询当前参数配置值。  配置原则：无                 |
| SMFSGWROACC     | SMF/S-GW上控制漫游用户接入功能开关      | 可选必选说明：可选参数  参数含义：该参数用于指示是否允许漫游用户接入SGW-C或者Proxy SGW-C或者V-SMF的指定APN。  数据来源：本端规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CPAPNACCESSCTRL查询当前参数配置值。  配置原则：无                                                                                                                                                            |
| SMFSGWVIACC     | SMF/S-GW上控制拜访用户接入功能开关      | 可选必选说明：可选参数  参数含义：该参数用于指示SGW-C或者Proxy SGW-C或者I-SMF指定APN是否允许拜访用户接入。  数据来源：本端规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CPAPNACCESSCTRL查询当前参数配置值。  配置原则：无                                                                                                                                                             |
| SMFPGWGGSNROACC | SMF/P-GW/GGSN上控制漫游用户接入功能开关 | 可选必选说明：可选参数  参数含义：该参数用于指示GGSN或者PGW-C或者H-SMF指定APN是否允许漫游用户接入。  数据来源：本端规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CPAPNACCESSCTRL查询当前参数配置值。  配置原则：无                                                                                                                                                                    |
| NULLIMSI        | 不携带IMSI用户激活策略              | 可选必选说明：可选参数  参数含义：该参数用于指定APN下是否允许不携带IMSI的用户激活。  数据来源：本端规划 取值范围： DISABLE（不使能）ENABLE（使能）INHERIT（继承全局）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CPAPNACCESSCTRL查询当前参数配置值。  配置原则：  该参数仅适用于234G的用户，当配置为INHERIT时，需要继承SET SMGTPPROT中的NULLIMSI参数取值。                                                                                                       |
| PROVRORESTRICT  | APN跨省漫游限制开关                | 可选必选说明：可选参数  参数含义：该参数用于控制是否开启APN跨省漫游限制策略。当开关开启后，专用APN/DNN用户跨省漫游时会话继续保持，PDN/PDU会话速率限制为0。该参数可以与ADD APNWHITENODE配合使用。  数据来源：本端规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CPAPNACCESSCTRL查询当前参数配置值。  配置原则：无                                                                                                             |

## 使用实例

在运营商网络中，规划S-GW支持拜访用户接入时，使用该命令进行配置，举例：

```
SET CPAPNACCESSCTRL: APN="huawei.com",SMFSGWVIACC=ENABLE;
```