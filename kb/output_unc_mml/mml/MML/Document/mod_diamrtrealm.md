# 修改Diameter路由域名信息（MOD DIAMRTREALM）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用NF：PGW-C、SMF**

该命令用于修改Diameter路由的配置信息。

#### 注意事项

- 该命令执行后立即生效。
- 应用和realm对应的Diameter路由需已经通过ADD DIAMRTREALM添加成功才可修改。
- 基于会话轮循的路由选择模式下，根据Session-id选择的DRA状态异常时，会选择Diameter路由中下一个链路正常的DRA进行消息交互。后续DRA状态恢复正常后，只有新激活用户会根据Session-id可能选择该状态恢复的DRA。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识           | 参数名称         | 参数说明                                                                                                                                                |
|:---------------|:-------------|:----------------------------------------------------------------------------------------------------------------------------------------------------|
| REALMNAME      | Diameter域名名称 | 可选必选说明：必选参数 参数含义：该参数用于指定Diameter路由的realm名。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～127。不支持空格，必须是可见ASCII码，由软参BIT 150控制是否区分大小写。 默认值：无 配置原则：如果配置为default则表示缺省路由。 |
| APPLICATION    | Diameter应用   | 可选必选说明：必选参数 参数含义：该参数用于指定Diameter路由的Diameter应用。 数据来源：本端规划 取值范围：枚举类型。 GY：Gy接口应用。GX：Gx接口应用。S6B：S6b接口应用。 默认值：无 配置原则：无                                   |
| SELECTMODE     | 路由选择模式       | 可选必选说明：可选参数 参数含义：该参数用于指定到同一realm的多条路由的路由选择模式。 数据来源：本端规划 取值范围：枚举类型。 MASTER_SLAVE：主备模式。SESSION_ID：基于会话的轮循模式。ROUND_ROBIN：基于消息的轮循模式。 默认值：无 配置原则：无       |
| FAILOVERSW     | Failover开关   | 可选必选说明：可选参数 参数含义：该参数用于指定Diameter路由的Failover开关是否开启。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：否。ENABLE：是。 默认值：无 配置原则：无                                            |
| AUTOFAILBACKSW | 自动倒回开关       | 可选必选说明：可选参数 参数含义：该参数用于指定Diameter路由的自动倒回开关是否开启。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：否。ENABLE：是。 默认值：无 配置原则：无                                                |

#### 使用实例

修改Gx应用且realm名为example.com的Diameter路由选择模式为基于会话的轮循(session-id)：

```
MOD DIAMRTREALM: REALMNAME="example.com", APPLICATION=GX, SELECTMODE=SESSION_ID, FAILOVERSW=ENABLE, AUTOFAILBACKSW=ENABLE;
```