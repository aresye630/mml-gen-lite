# 增加APN Radius Client IP接口（ADD APNRDSCLIENTIP）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用NF：PGW-C、SMF**

该命令用于配置APN实例鉴权或计费请求消息的radius client ip，即鉴权或者计费请求消息的源IP地址。将Gi接口与APN实例进行绑定时将配置此命令。该命令为radius access request和radius accounting request消息指定Gi接口。当发送radius access request和radius accounting request消息时，消息中携带的源地址为指定的Gi接口IP。

#### 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为6000。
- 对象ApnRdsClientIp中的APN对应的IntfName和AuthOrAcct的组合记录数不大于6，并且不能有相同记录，则添加成功。
- RADIUS server仅选择相同IP版本的逻辑接口通信。
- RADIUS group内同时配置IPv4和IPv6 RADIUS server时，Client IP对应的逻辑接口也需要同时配置IPv4和IPv6地址。
- 当APN和radius server group下都配置了radius client ip，并且绑定的Gi接口的VPN相同的情况下，APN下配置的radius client ip的优先级高于radius server group下面配置的radius client ip。
- 当APN和radius server group下都没有配置radius client ip，或者没有配置相关的Giif，或者radius server group和APN下radius client ip都配置错误，会导致发送鉴权或计费请求消息失败。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识       | 参数名称   | 参数说明                                                                                                                                                                                                                                                                                |
|:-----------|:-------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| APN        | APN名称  | 可选必选说明：必选参数 参数含义：该参数用于指定radius client ip需要绑定的APN名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。不支持空格及部分特殊字符。可以支持的特殊字符有“.”和“-”，“.”不可以是第一个字符且不可以连续出现。 默认值：无 配置原则：该参数必须已经通过命令ADD CPAPN配置。                                                                                                        |
| AUTHORACCT | 鉴权或计费  | 可选必选说明：必选参数 参数含义：该参数用于指定是鉴权时的radius client ip还是计费时的radius client ip。 数据来源：本端规划 取值范围：枚举类型。 ACCOUNTING：表示指定的Gi接口的IP地址是计费时的radius client ip。AUTHENTICATION：表示指定的Gi接口的IP地址是鉴权时的radius client ip。ACCT_AND_AUTH：表示指定的Gi接口的IP地址既是鉴权时的radius client ip，也是计费时的radius client ip。 默认值：无 配置原则：无 |
| INTFNAME   | 接口名称   | 可选必选说明：必选参数 参数含义：该参数用于指定该radius client ip配置在哪个接口上。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～13。 默认值：无 配置原则：无                                                                                                                                                                                   |

#### 使用实例

- 当需要配置APN实例鉴权请求消息的radius client ip接口时，可按如下配置：

  ```
  ADD APNRDSCLIENTIP:APN="huawei.com",AUTHORACCT=AUTHENTICATION,INTFNAME="giif1/0/0";
  ```
- 当需要配置APN实例计费请求消息的radius client ip接口时，可按如下配置：

  ```
  ADD APNRDSCLIENTIP:APN="huawei.com",AUTHORACCT=ACCOUNTING,INTFNAME="giif1/0/0";
  ```