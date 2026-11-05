# 设置LDP全局配置（SET LDPGLOBAL）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

该命令用于设置LDP全局配置。

#### 注意事项

- 该命令执行后立即生效。
- 可选参数至少选一项。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| MTUSIGNALING   | MTUAPPLYSIGNAL   | TRIGGERMODE   | GRENABLE   |   RECONNECTTIME |   RECOVERYTIME |   PEERLIVETIME |   BACKOFFINITTIME |   BACKOFFMAXTIME | ANNOUNCEMENTCAP   | PROXYEGRLSPDIS   |
|:---------------|:-----------------|:--------------|:-----------|----------------:|---------------:|---------------:|------------------:|-----------------:|:------------------|:-----------------|
| ENABLE         | DISABLE          | HOST          | DISABLE    |             300 |            300 |            600 |                15 |              120 | DISABLE           | False            |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识            | 参数名称                 | 参数说明                                                                                                                                                                                                                                                                                                                                                         |
|:----------------|:---------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MTUSIGNALING    | MTU私有信令能力            | 可选必选说明：可选参数 参数含义：该参数用于指定MTU私有信令能力。使能时表示发送标签映射消息时携带的MTU TLV类型为华为私有的MTU TLV。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不使能。ENABLE：使能。 默认值：无                                                                                                                                                                                                                                 |
| MTUAPPLYSIGNAL  | MTU标准信令能力            | 可选必选说明：条件可选参数 前提条件：该参数在“MTUSIGNALING”配置为“DISABLE”时为可选参数。 参数含义：该参数用于指定MTU标准信令能力。使能时表示发送标签映射消息时携带的MTU TLV类型为RFC中定义的标准MTU TLV。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不使能。ENABLE：使能。 默认值：无                                                                                                                                                                                |
| TRIGGERMODE     | 触发策略                 | 可选必选说明：可选参数 参数含义：该参数用于指定触发策略。 如果触发策略为“HOST”，即允许32位地址的主机IP路由触发LDP建立LSP。 如果触发策略为“ALL”，则允许所有IGP路由项触发LDP建立LSP。BGP公网路由和缺省路由不能触发LDP建立LSP。 如果触发策略为“IP-PREFIX”，则只有通过IP地址前缀列表过滤的FEC项才允许触发LDP建立LSP。 如果触发策略为“NONE”，则不允许触发LDP建立LSP。 数据来源：本端规划 取值范围：枚举类型。 ALL：全局。所有静态路由和IGP路由项触发建立LSP。HOST：主机。32位地址的IP路由触发建立LSP。NONE：不使能。不触发建立LSP。IP-PREFIX：IP前缀。根据IP地址前缀列表触发建立LSP。 默认值：无 |
| IPPREFIXNAME    | IP地址前缀名称             | 可选必选说明：条件必选参数 前提条件：该参数在“TRIGGERMODE”配置为“IP-PREFIX”时为必选参数。 参数含义：该参数用于指定IP地址前缀名称。 如果触发策略为ip-prefix，则只有通过该参数过滤的FEC项才允许触发LDP建立LSP。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～169。 默认值：无 配置原则：所用的IP前缀名需提前配好。                                                                                                                                                                  |
| GRENABLE        | GR能力                 | 可选必选说明：可选参数 参数含义：该参数用于指定是否使能Graceful Restart能力。缺省情况下，LDP GR能力被禁止。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不使能。ENABLE：使能。 默认值：无 配置原则： 使能或去使能Graceful Restart能力都会导致所有LDP会话重建。目前LDP仅支持GR Helper。                                                                                                                                                                           |
| RECONNECTTIME   | 会话重链接时间（s）           | 可选必选说明：条件可选参数 前提条件：该参数在“GRENABLE”配置为“ENABLE”时为可选参数。 参数含义：该参数用于指定会话重链接时间。GR Restarter发生主备倒换后，GR Helper检测到和GR Restarter的LDP会话失败，将启动Reconnect定时器，等待LDP会话的重新建立。 数据来源：本端规划 取值范围：整数类型，取值范围为3～259200，单位是秒。 默认值：无                                                                                                                                                    |
| RECOVERYTIME    | LSP恢复时间（s）           | 可选必选说明：条件可选参数 前提条件：该参数在“GRENABLE”配置为“ENABLE”时为可选参数。 参数含义：该参数用于指定LSP恢复时间。LDP会话重新建立后，GR Helper启动Recovery定时器，等待LSP的恢复。 数据来源：本端规划 取值范围：整数类型，取值范围为3～259200，单位是秒。 默认值：无                                                                                                                                                                                            |
| PEERLIVETIME    | 对端存活定时器时间（s）         | 可选必选说明：条件可选参数 前提条件：该参数在“GRENABLE”配置为“ENABLE”时为可选参数。 参数含义：该参数用于指定对端存活定时器时间（s）。 数据来源：本端规划 取值范围：整数类型，取值范围为3～259200，单位是秒。 默认值：无                                                                                                                                                                                                                                  |
| BACKOFFINITTIME | BackOff初始时间（s）       | 可选必选说明：可选参数 参数含义：该参数用于指定BackOff初始时间（s）。 数据来源：本端规划 取值范围：整数类型，取值范围为5～2147483，单位是秒。 默认值：无 配置原则：建议配置指数回退定时器初始值不小于15s。                                                                                                                                                                                                                                            |
| BACKOFFMAXTIME  | BackOff最大时间（s）       | 可选必选说明：可选参数 参数含义：该参数用于指定BackOff最大时间（s）。 数据来源：本端规划 取值范围：整数类型，取值范围为5～2147483，单位是秒。 默认值：无 配置原则：建议配置指数回退定时器最大值不小于120s。                                                                                                                                                                                                                                           |
| ANNOUNCEMENTCAP | 动态通告能力使能             | 可选必选说明：可选参数 参数含义：该参数用于指定动态通告能力使能。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不使能。ENABLE：使能。 默认值：无                                                                                                                                                                                                                                                                          |
| PROXYEGRLSPDIS  | 禁止建立代理Egress LDP LSP | 可选必选说明：可选参数 参数含义：该参数用于指定禁止建立代理Egress LDP LSP能力。 数据来源：本端规划 取值范围：布尔类型，输入格式为“TRUE”或者“FALSE”。 默认值：无 配置原则： TRUE：禁止建立代理Egress LDP LSP。FALSE：允许建立代理Egress LDP LSP。                                                                                                                                                                                                  |

#### 使用实例

设置LDP全局配置：

```
SET LDPGLOBAL:TRIGGERMODE=IP-PREFIX,IPPREFIXNAME="bb",GRENABLE=ENABLE,MTUSIGNALING=DISABLE,MTUAPPLYSIGNAL=ENABLE,RECONNECTTIME=300,RECOVERYTIME=300,PEERLIVETIME=600,BACKOFFINITTIME=15,BACKOFFMAXTIME=120,ANNOUNCEMENTCAP=DISABLE,PROXYEGRLSPDIS=FALSE;
```