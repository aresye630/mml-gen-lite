# 修改Radius服务器组（MOD RDSSVRGRP）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用NF：PGW-C、SMF**

该命令用来修改RADIUS SERVER GROUP配置。

#### 注意事项

该命令执行后立即生效。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识           | 参数名称                                  | 参数说明                                                                                                                                                                                                                                                   |
|:---------------|:--------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RDSSVRGRPNAME  | Radius Server Group名称                 | 可选必选说明：必选参数 参数含义：该参数用于指定RADIUS服务器组名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～31。 默认值：无 配置原则：无                                                                                                                                                                   |
| MODE           | 模式                                    | 可选必选说明：可选参数 参数含义：该参数用于指定RADIUS服务器组模式。 数据来源：全网规划 取值范围：枚举类型。 MASTER_SLAVE：配置RADIUS服务器组为主备模式。ROUND_ROBIN：配置RADIUS服务器组为负荷分担模式。 默认值：无 配置原则：无                                                                                                                |
| ACCTONACTIVE   | Accounting Request ON应答之前是否激活用户       | 可选必选说明：条件可选参数 前提条件：该参数在“SIGOPTACCTMSG”配置为“ENABLE”时为可选参数。 参数含义：该参数用于指定Accounting Request ON应答之前是否允许激活用户。 数据来源：全网规划 取值范围：枚举类型。 DISABLE：Accounting Request ON应答之前不允许激活用户。ENABLE：Accounting Request ON应答之前允许激活用户。 默认值：无 配置原则：无                             |
| ACCTTOAUTH     | 利用鉴权服务器计费                             | 可选必选说明：可选参数 参数含义：该参数用于指定RADIUS服务器组是否支持利用鉴权服务器计费特性。 数据来源：全网规划 取值范围：枚举类型。 DISABLE：表示RADIUS服务器组不支持利用鉴权服务器计费特性。ENABLE：表示RADIUS服务器组支持利用鉴权服务器计费特性。 默认值：无 配置原则：无                                                                                              |
| DSCPV          | DSCP值                                 | 可选必选说明：可选参数 参数含义：该参数用于指定信令报文的DSCP值。 数据来源：全网规划 取值范围：整数类型，取值范围为0～63，255。 默认值：无 配置原则：无                                                                                                                                                                    |
| SIGOPTACCTMSG  | 支持可选计费消息                              | 可选必选说明：可选参数 参数含义：该参数用于指定是否支持可选计费消息。 数据来源：全网规划 取值范围：枚举类型。 DISABLE：表示不支持可选计费消息。即UNC重新启动后不发送Accounting Request OFF消息和Accounting Request ON消息。ENABLE：表示支持可选计费消息，即UNC重新启动后先发Accounting Request OFF消息，再发送Accounting Request ON消息通知已配置的AAA计费服务器。 默认值：无 配置原则：无 |
| ONOFFWAITTIME  | Accounting Request On/Off消息间的时间间隔（秒）  | 可选必选说明：条件可选参数 前提条件：该参数在“SIGOPTACCTMSG”配置为“ENABLE”时为可选参数。 参数含义：该参数用于指定Accounting Request On/Off消息间的时间间隔。 数据来源：全网规划 取值范围：整数类型，取值范围为0～999。 默认值：无 配置原则：无                                                                                                   |
| ONRETRANSMIT   | Accounting Request On重发次数             | 可选必选说明：条件可选参数 前提条件：该参数在“SIGOPTACCTMSG”配置为“ENABLE”时为可选参数。 参数含义：该参数用于指定Accounting Request On重发次数。当取值为255时表示不限制重发次数。 数据来源：全网规划 取值范围：整数类型，取值范围为0～5，255。 默认值：无 配置原则：该参数在“SIGOPTACCTMSG”配置为“ENABLE”时为条件可选参数。                                                 |
| ONTIMEOUT      | Accounting Request On超时时间 (秒)         | 可选必选说明：条件可选参数 前提条件：该参数在“SIGOPTACCTMSG”配置为“ENABLE”时为可选参数。 参数含义：该参数用于指定Accounting Request On超时时间。 数据来源：全网规划 取值范围：整数类型，取值范围为3～120，单位是秒。 默认值：无 配置原则：该参数在“SIGOPTACCTMSG”配置为“ENABLE”时为条件可选参数。                                                                |
| OFFRETRANSMIT  | Accounting Request Off重发次数            | 可选必选说明：条件可选参数 前提条件：该参数在“SIGOPTACCTMSG”配置为“ENABLE”时为可选参数。 参数含义：该参数用于指定Accounting Request Off重发次数。 数据来源：全网规划 取值范围：整数类型，取值范围为0～5。 默认值：无 配置原则：该参数在“SIGOPTACCTMSG”配置为“ENABLE”时为条件可选参数。                                                                      |
| OFFTIMEOUT     | Accounting Request Off超时时间(秒)         | 可选必选说明：条件可选参数 前提条件：该参数在“SIGOPTACCTMSG”配置为“ENABLE”时为可选参数。 参数含义：该参数用于指定Accounting Request Off超时时间。 数据来源：全网规划 取值范围：整数类型，取值范围为3～120，单位是秒。 默认值：无 配置原则：该参数在“SIGOPTACCTMSG”配置为“ENABLE”时为条件可选参数。                                                               |
| ACCTTIMEOUT    | Radius Accounting Request超时时间 (秒)     | 可选必选说明：可选参数 参数含义：该参数用于指定Radius计费消息超时时间。 数据来源：全网规划 取值范围：整数类型，取值范围为1～10，单位是秒。 默认值：无 配置原则：无                                                                                                                                                               |
| ACCTRETRANSMIT | Radius Accounting Request重发次数         | 可选必选说明：可选参数 参数含义：该参数用于指定UNC在未收到Radius计费响应消息时的重发请求消息最大次数，重发次数为0表示不重发。 数据来源：全网规划 取值范围：整数类型，取值范围为0～5。 默认值：无 配置原则：无                                                                                                                                        |
| AUTHTIMEOUT    | Radius Authentication Request超时时间 (秒) | 可选必选说明：可选参数 参数含义：该参数用于指定Radius鉴权消息超时时间。 数据来源：全网规划 取值范围：整数类型，取值范围为1～10，单位是秒。 默认值：无 配置原则：无                                                                                                                                                               |
| AUTHRETRANSMIT | Radius Authentication Request重发次数     | 可选必选说明：可选参数 参数含义：该参数用于指定UNC在未收到Radius鉴权响应消息时的重发请求消息最大次数，重发次数为0表示不重发。 数据来源：全网规划 取值范围：整数类型，取值范围为0～5。 默认值：无 配置原则：无                                                                                                                                        |
| ACCTSVRTOUT    | Radius Accounting超时时长 (秒)             | 可选必选说明：可选参数 参数含义：该参数用于指定Radius计费服务器超时时长。在该时间内如果未收到Radius计费服务器任何响应，UNC则将该Radius计费服务器状态设置为DOWN。 数据来源：全网规划 取值范围：整数类型，取值范围为1～60，单位是秒。 默认值：无 配置原则：无                                                                                                         |
| ACCTSVRDTIME   | Radius计费服务器Down状态保持时长 (秒)             | 可选必选说明：可选参数 参数含义：该参数用于指定Radius计费服务器Down状态的保持时长。超时后，UNC会认为该Radius计费服务器状态恢复可继续向其发送消息。 数据来源：全网规划 取值范围：整数类型，取值范围为1～3600，单位是秒。 默认值：无 配置原则：无                                                                                                                 |
| AUTHSVRTOUT    | Radius鉴权服务器超时时长 (秒)                   | 可选必选说明：可选参数 参数含义：该参数用于指定Radius鉴权服务器超时时长。在该时间内如果未收到Radius鉴权服务器任何响应，UNC则将该Radius鉴权服务器状态设置为DOWN。 数据来源：全网规划 取值范围：整数类型，取值范围为1～60，单位是秒。 默认值：无 配置原则：无                                                                                                         |
| AUTHSVRDTIME   | Radius鉴权服务器Down状态保持时长 (秒)             | 可选必选说明：可选参数 参数含义：该参数用于指定Radius鉴权服务器Down状态的保持时长。超时后，UNC会认为该Radius鉴权服务器状态恢复可继续向其发送消息。 数据来源：全网规划 取值范围：整数类型，取值范围为1～3600，单位是秒。 默认值：无 配置原则：无                                                                                                                 |

#### 使用实例

修改Radius服务器组：Radius Server Group名称为rsg，支持可选计费消息为DISABLE：

```
MOD RDSSVRGRP:RDSSVRGRPNAME="rsg",MODE=ROUND_ROBIN,SIGOPTACCTMSG=DISABLE;
```