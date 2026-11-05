# 增加Diameter链路组(ADD DIAMCONNGRP)

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用NF：PGW-C、SMF**

该命令用于指定本端主机名与指定对端服务器之间建立一组Diameter链路。本端主机名，对端主机名唯一确定了一组Diameter链路。

#### 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1000。
- 配置LOCALHOSTNAME需要保证已经配置了Local Info。
- 配置PEERHOSTNAME时，需要保证已经配置了与APPLICATION对应类型的服务器。
- APPLICATION和对端主机名的应用类型必须一致。
- PEERHOSTNAME和LOCALHOSTNAME不能重复。
- 每个Peer与Gx/Gy应用最多绑定64个Local Host。
- 配置SELECTMODE为MASTER\_SLAVE时，删除Diameter链路组下配置的第一个Diameter链路或删除主链路的对端地址信息会导致主备链路切换，准确的主备关系未知。当前不支持用命令设置主链路，如果需要明确指定主链路，请删除并重新配置Diameter链路组下的Diameter链路，配置的第一个Diameter链路即对应主链路。
- 配置SELECTMODE为SESSION\_ID时，根据session-id选择Diameter链路状态异常时，会选择其他可用Diameter链路进行消息交互。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识          | 参数名称         | 参数说明                                                                                                                                                                               |
|:--------------|:-------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CONNGROUPNAME | Diameter链路组名 | 可选必选说明：必选参数 参数含义：该参数用于指定Diameter链路组名。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 默认值：无 配置原则：无                                                                                  |
| LOCALHOSTNAME | 本端主机名        | 可选必选说明：必选参数 参数含义：该参数用于指定Diameter链路组的本端主机名。 数据来源：全网规划 取值范围：字符串类型，输入长度范围为1～127。不支持空格，不区分大小写。 默认值：无 配置原则：该参数使用ADD DIAMLOCINFO命令配置生成。                                                  |
| APPLICATION   | Diameter应用   | 可选必选说明：必选参数 参数含义：该参数用于指定Diameter链路组的应用类型。 数据来源：全网规划 取值范围：枚举类型。 GX：Gx接口应用。GY：Gy接口应用。S6b：S6b接口应用。 默认值：无 配置原则：该参数所指定的应用必须与PEERHOSTNAME参数对应服务器的应用类型相同。                                 |
| PEERHOSTNAME  | 对端主机名        | 可选必选说明：必选参数 参数含义：该参数用于指定Diameter链路组的对端主机名。 数据来源：全网规划 取值范围：字符串类型，输入长度范围为1～127。不支持空格，不区分大小写。 默认值：无 配置原则：该参数使用ADD PCRF、ADD OCS、ADD DIAMETERAAA或ADD DRA命令配置生成。                         |
| SELECTMODE    | 链路选择模式       | 可选必选说明：可选参数 参数含义：该参数用于指定Diameter链路组的链路选择模式。 数据来源：全网规划 取值范围：枚举类型。 SESSION_ID：基于会话（Session-id）轮询方式进行链路选择。MASTER_SLAVE：基于主备方式进行链路选择。ROUND_ROBIN：基于消息轮询方式进行链路选择。 默认值：SESSION_ID 配置原则：无 |

#### 使用实例

如果希望为本端主机gxlocalhost和对端pcrf主机pcrfhost创建一个gx diameter链路组，可以使用该命令配置链路组：

```
ADD DIAMCONNGRP: CONNGROUPNAME="gxconngrp", LOCALHOSTNAME="gxlocalhost", APPLICATION=GX, PEERHOSTNAME="pcrfhost";
```