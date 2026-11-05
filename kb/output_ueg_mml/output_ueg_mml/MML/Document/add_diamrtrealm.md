# 增加Diameter路由域名信息（ADD DIAMRTREALM）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用NF：PGW-C、SMF**

此命令用于添加指定Diameter应用和realm的Diameter路由相关参数，或者设置指定Diameter应用的缺省Diameter路由的相关参数。

#### 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为256。
- 应用和realm唯一确定一条记录。
- 主备路由选择模式下，如果主用下一跳被删除，则第一个备用下一跳升主。
- 网关发送的请求消息中携带的Destination-Realm AVP值用于Realm路由表匹配，根据消息的应用类型以及Destination-Realm AVP值匹配到Diameter路由时，UNC按照select-mode设置选择下一跳。如无法匹配到某Diameter应用所有指定的路由，同时该应用配置了缺省路由，该请求消息按照缺省路由发送。
- 基于会话轮循的路由选择模式下，根据Session-id选择的DRA状态异常时，会选择Diameter路由中下一个链路正常的DRA进行消息交互。后续DRA状态恢复正常后，只有新激活用户会根据Session-id可能选择该状态恢复的DRA。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识           | 参数名称         | 参数说明                                                                                                                                                   |
|:---------------|:-------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------|
| REALMNAME      | Diameter域名名称 | 可选必选说明：必选参数 参数含义：该参数用于指定Diameter路由的realm名。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～127。不支持空格，必须是可见ASCII码，由软参BIT 150控制是否区分大小写。 默认值：无 配置原则：如果配置为default则表示缺省路由。    |
| APPLICATION    | Diameter应用   | 可选必选说明：必选参数 参数含义：该参数用于指定Diameter路由的Diameter应用。 数据来源：本端规划 取值范围：枚举类型。 GY：Gy接口应用。GX：Gx接口应用。S6B：S6b接口应用。 默认值：无 配置原则：无                                      |
| SELECTMODE     | 路由选择模式       | 可选必选说明：可选参数 参数含义：该参数用于指定到同一realm的多条路由的路由选择模式。 数据来源：本端规划 取值范围：枚举类型。 MASTER_SLAVE：主备模式。SESSION_ID：基于会话的轮循模式。ROUND_ROBIN：基于消息的轮循模式。 默认值：SESSION_ID 配置原则：无 |
| FAILOVERSW     | Failover开关   | 可选必选说明：可选参数 参数含义：该参数用于指定Diameter路由的Failover开关是否开启。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：否。ENABLE：是。 默认值：DISABLE 配置原则：无                                         |
| AUTOFAILBACKSW | 自动倒回开关       | 可选必选说明：可选参数 参数含义：该参数用于指定Diameter路由的自动倒回开关是否开启。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：否。ENABLE：是。 默认值：DISABLE 配置原则：无                                             |

#### 使用实例

- 添加一个Gy接口的缺省Diameter路由参数，路由选择模式为基于会话的轮循（session-id）：

  ```
  ADD DIAMRTREALM: REALMNAME="default", APPLICATION=GY,SELECTMODE=SESSION_ID;
  ```
- 添加一个指定realm名为example.com的Gx应用的Diameter路由参数，模式为主备，支持failover处理，支持主动failback到主用下一跳：

  ```
  ADD DIAMRTREALM: REALMNAME="example.com", APPLICATION=GX, SELECTMODE=MASTER_SLAVE, FAILOVERSW=ENABLE, AUTOFAILBACKSW=ENABLE;
  ```