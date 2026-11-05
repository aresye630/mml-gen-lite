# 同步OCS用户数据（SYN POCSUSRDATA）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

本命令用于OCS通知UPCF重新获取用户信息。当OCS中存储的用户签约信息发生变化时，OCS会通知UPCF去获取用户最新数据，UPCF收到通知后会发送SLR消息去OCS查询用户最新数据，以便调整策略控制。

本命令应用的操作原理如图1所示。

**图1** 同步OCS用户数据

1. 用户签约业务发生变化，Provisioning System/OCS通过SOAP接口发送synOCSUsrdataRequest请求给UPCF，通知UPCF同步用户数据。
2. UPCF回复响应消息给Provisioning System/OCS。
3. UPCF通过Sy接口向OCS发起SLR-Intermediate请求消息查询用户配额状态。
4. OCS根据用户标识查询配额状态，并向UPCF返回SLA-Intermediate响应消息携带Policy-Counter-Status-Report AVP。
5. UPCF根据最新的配额状态、用户签约信息以及本地配置的策略进行策略决策，生成新的规则，通过RAR请求消息下发到PCEF。
6. PCEF删除旧规则安装新规则，并返回RAA响应消息给UPCF。

## 注意事项

- 只有当用户在线时，UPCF才会发起SLR消息向OCS获取用户最新配额状态。
- 当OCS通知的对象为组用户时，UPCF发送SLR消息的速度受“VRM\_SYNUSRDATASPEED”软参控制。
- “用户标识”和“组用户标识”参数只支持输入其中一个。

## 参数说明

| 参数标识          | 参数名称   | 参数说明                                                                                |
|:--------------|:-------|:------------------------------------------------------------------------------------|
| USRIDENTIFIER | 用户标识   | 用于指示UPCF需要同步数据的用户标识。用户标识可以设置为用户第一标识或用户第二标识来同步OCS用户数据。 取值范围：长度不超过255的字符串。 默认值：无。     |
| GRPIDENTIFIER | 组用户标识  | 用于指示UPCF需要同步数据的组用户标识。组用户标识可以设置为组用户第一标识或组用户第二标识来同步OCS用户数据。 取值范围：长度不超过255的字符串。 默认值：无。 |

## 使用实例

同步OCS用户数据：“用户标识”为“46010381014\*\*\*\*”。

```
SYN POCSUSRDATA: USRIDENTIFIER="46010381014****";
```