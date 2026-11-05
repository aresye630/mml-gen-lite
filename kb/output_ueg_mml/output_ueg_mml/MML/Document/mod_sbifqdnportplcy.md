# 修改FQDN端口策略（MOD SBIFQDNPORTPLCY）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：AMF、SMF、NSSF、SMSF、NCG、NEF、NWDAF、SCF**

该命令用于修改FQDN使用端口号的策略。

## 注意事项

该命令执行后只对新激活用户生效。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识     | 参数名称   | 参数说明                                                                                                                                                                                                 |
|:---------|:-------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SCENE    | 场景     | 可选必选说明：必选参数  参数含义：该参数用于指定端口策略适用的场景。  数据来源：全网规划 取值范围： “TARGETADDR（TARGETADDR）”：根据对端FQDN组装对端Uri“LOCALURI（LOCALURI）”：根据本端FQDN组装本端CallbackUri或Location等Uri  默认值：无  配置原则：无                                |
| SCOPE    | 范围     | 可选必选说明：必选参数  参数含义：该参数用于指定FQDN端口策略的适用范围。  数据来源：全网规划 取值范围： “INTERPLMNDEFAULT（INTERPLMNDEFAULT）”：PLMN间默认策略“BYPLMN（BYPLMN）”：指定PLMN的策略  默认值：无  配置原则：  如果同时有默认策略和基于PLMN的策略，优先使用基于PLMN的策略。                  |
| PLMN     | 对端PLMN | 可选必选说明：该参数在"SCOPE"配置为"BYPLMN"时为条件必选参数。  参数含义：该参数用于指定策略适用的对端PLMN。  数据来源：全网规划  取值范围：字符串类型，输入长度范围是0~6。  默认值：无  配置原则：  PLMN由MCC和MNC组成， MCC为3个十进制数字， MNC为2~3个十进制数字。例如PLMN=“12303”， 其中MCC=“123”， MNC=“03”。 |
| PORTPLCY | 端口策略   | 可选必选说明：必选参数  参数含义：该参数用于指定FQDN使用端口号的策略。  数据来源：全网规划 取值范围： “USEPORT（USEPORT）”：使用端口号“NOTUSEPORT（NOTUSEPORT）”：不使用端口号  默认值：无  配置原则：无                                                                       |

## 使用实例

- 修改根据对端FQDN组装对端Uri场景下，PLMN间默认策略为FQDN使用端口号。

  ```
  MOD SBIFQDNPORTPLCY:SCENE=TARGETADDR,SCOPE=INTERPLMNDEFAULT,PORTPLCY=USEPORT;
  ```
- 修改根据对端FQDN组装对端Uri场景下，对端PLMN为"12303"时，策略为FQDN不使用端口号。

  ```
  MOD SBIFQDNPORTPLCY:SCENE=TARGETADDR,SCOPE=BYPLMN,PLMN="12303",PORTPLCY=NOTUSEPORT;
  ```