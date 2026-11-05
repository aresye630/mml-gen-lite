# 设置指定PFCP消息类型固定速率流控信息（SET PFCPFIXEDFC）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：SMF**

设置指定PFCP消息的固定速率门限。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| MSGTYPE               | FCSWITCH   |   THRESHOLD |
|:----------------------|:-----------|------------:|
| HEARTBEATREQ          | ON         |         500 |
| HEARTBEATRSP          | ON         |         500 |
| ASSOCIATIONSETUPREQ   | ON         |         500 |
| ASSOCIATIONSETUPRSP   | ON         |         500 |
| ASSOCIATIONUPDATEREQ  | ON         |         500 |
| ASSOCIATIONUPDATERSP  | ON         |         500 |
| ASSOCIATIONRELEASEREQ | ON         |         500 |
| ASSOCIATIONRELEASERSP | ON         |         500 |
| NOTSUPPORTRSP         | ON         |         500 |
| NODEREPORTREQ         | ON         |         500 |
| NODEREPORTRSP         | ON         |         500 |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识      | 参数名称        | 参数说明                                                                                                                                                                                                                                                                                                                                                 |
|:----------|:------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MSGTYPE   | 流控消息类型      | 可选必选说明：必选参数  参数含义：该参数用于设置被流控的PFCP消息类型。  数据来源：全网规划 取值范围： HEARTBEATREQ（心跳请求）HEARTBEATRSP（心跳响应）ASSOCIATIONSETUPREQ（偶联建立请求）ASSOCIATIONSETUPRSP（偶联建立响应）ASSOCIATIONUPDATEREQ（偶联更新请求）ASSOCIATIONUPDATERSP（偶联更新响应）ASSOCIATIONRELEASEREQ（偶联释放请求）ASSOCIATIONRELEASERSP（偶联释放响应）NOTSUPPORTRSP（版本不支持响应）NODEREPORTREQ（节点上报请求）NODEREPORTRSP（节点上报响应）  默认值：无。  配置原则：无 |
| FCSWITCH  | 固定速率流控开关    | 可选必选说明：必选参数  参数含义：该参数用于控制是否开启指定PFCP消息类型固定速率流控功能。  数据来源：全网规划 取值范围： OFF（关闭）ON（开启）  默认值：无。  配置原则：  当希望开启指定消息类型流控功能时，设置为"On"；当希望关闭指定消息类型流控功能时，设置为"Off"。                                                                                                                                                                                                  |
| THRESHOLD | 流控速率门限(个/秒) | 可选必选说明：该参数在"FCSWITCH"配置为"ON"时为条件必选参数。  参数含义：该参数用于设置指定PFCP消息的流控速率上限。该参数针对单POD指定消息类型进行流控。  数据来源：全网规划  取值范围：整数类型，取值范围是0~100000。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST PFCPFIXEDFC查询当前参数配置值。  配置原则：无                                                                                                                                                  |

## 使用实例

针对HEARTBEATREQ消息类型开启固定速率流控，速率门限是单POD 500个/秒，执行如下命令：

```
%%SET PFCPFIXEDFC: MSGTYPE= HEARTBEATREQ, FCSWITCH=ON, THRESHOLD=500;%%
RETCODE = 0  操作成功

---    END
```