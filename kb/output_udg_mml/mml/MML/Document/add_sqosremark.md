# 增加重标记配置（ADD SQOSREMARK）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

该命令用来增加重标记。

可以对匹配的报文进行DSCP、DF、TOS、IP-precedence等重标记。在一个流行为下只能添加一次Remark动作，再添加或修改Remark动作时需要使用MOD SQOSREMARK命令。

#### 注意事项

- 该命令最大记录数为65535。
- 需要使用ADD MQCBEHAVIOR命令先配置流行为。
- V4DSCPVALUE和V4TOSVALUE、V4PRECEDENCE互斥，不能同时配置。
- V6DSCPVALUE和V6TOSVALUE、V6PRECEDENCE互斥，不能同时配置。
- 该命令仅适用于非NP卡场景和NP卡非加速模式场景。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识         | 参数名称       | 参数说明                                                                                                                                                                                                                         |
|:-------------|:-----------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BEHAVIORNAME | 流行为名称      | 可选必选说明：必选参数 参数含义：该参数用于指定流行为名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～31。 默认值：无 配置原则：区分大小写，不支持空格。                                                                                                                                     |
| V4DSCPVALUE  | IPv4的DSCP值 | 可选必选说明：可选参数 参数含义：该参数用于指定配置IPv4的DSCP（差分服务码点）值。 数据来源：本端规划 取值范围：整数类型，取值范围为0～255。其中有效值为0～63，255为无效值，表示没有配置。 默认值：255 配置原则：至少选择一个有效的参数（V4DSCPValue，V6DSCPValue，DFValue，V4TOSVALUE，V4PRECEDENCE，V6TOSVALUE，V6PRECEDENCE，VLAN8021P）。 |
| V6DSCPVALUE  | IPv6的DSCP值 | 可选必选说明：可选参数 参数含义：该参数用于指定配置IPv6的DSCP（差分服务码点）值。 数据来源：本端规划 取值范围：整数类型，取值范围为0～255。其中有效值为0～63，255为无效值，表示没有配置。 默认值：255 配置原则：至少选择一个有效的参数（V4DSCPValue，V6DSCPValue，DFValue，V4TOSVALUE，V4PRECEDENCE，V6TOSVALUE，V6PRECEDENCE，VLAN8021P）。 |
| DFVALUE      | DF值        | 可选必选说明：可选参数 参数含义：该参数用于指定配置DF（不分片标记）值。 数据来源：本端规划 取值范围：整数类型，取值范围为0～255。其中有效值为0～1，255为无效值，表示没有配置。 默认值：255 配置原则：至少选择一个有效的参数（V4DSCPValue，V6DSCPValue，DFValue，V4TOSVALUE，V4PRECEDENCE，V6TOSVALUE，V6PRECEDENCE，VLAN8021P）。          |
| V4TOSVALUE   | IPv4的TOS值  | 可选必选说明：可选参数 参数含义：该参数用于指定配置IPv4的TOS（服务类型）值。 数据来源：本端规划 取值范围：整数类型，取值范围为0～255。其中有效值为0～15，255为无效值，表示没有配置。 默认值：255 配置原则：至少选择一个有效的参数（V4DSCPValue，V6DSCPValue，DFValue，V4TOSVALUE，V4PRECEDENCE，V6TOSVALUE，V6PRECEDENCE，VLAN8021P）。    |
| V4PRECEDENCE | IPv4的优先级   | 可选必选说明：可选参数 参数含义：该参数用于指定配置IPv4的优先级。 数据来源：本端规划 取值范围：整数类型，取值范围为0～255。其中有效值为0～7，255为无效值，表示没有配置。 默认值：255 配置原则：至少选择一个有效的参数（V4DSCPValue，V6DSCPValue，DFValue，V4TOSVALUE，V4PRECEDENCE，V6TOSVALUE，V6PRECEDENCE，VLAN8021P）。            |
| V6TOSVALUE   | IPv6的TOS值  | 可选必选说明：可选参数 参数含义：该参数用于指定配置IPv6的TOS（服务类型）值。 数据来源：本端规划 取值范围：整数类型，取值范围为0～255。其中有效值为0～15，255为无效值，表示没有配置。 默认值：255 配置原则：至少选择一个有效的参数（V4DSCPValue，V6DSCPValue，DFValue，V4TOSVALUE，V4PRECEDENCE，V6TOSVALUE，V6PRECEDENCE，VLAN8021P）。    |
| V6PRECEDENCE | IPv6的优先级   | 可选必选说明：可选参数 参数含义：该参数用于指定配置IPv6的优先级。 数据来源：本端规划 取值范围：整数类型，取值范围为0～255。其中有效值为0～7，255为无效值，表示没有配置。 默认值：255 配置原则：至少选择一个有效的参数（V4DSCPValue，V6DSCPValue，DFValue，V4TOSVALUE，V4PRECEDENCE，V6TOSVALUE，V6PRECEDENCE，VLAN8021P）。            |
| VLAN8021P    | 802.1p值    | 可选必选说明：可选参数 参数含义：该参数用于指定VLAN报文的802.1p值。 数据来源：本端规划 取值范围：整数类型，取值范围为0～255。其中有效值为0～7，255为无效值，表示没有配置。 默认值：255 配置原则：至少选择一个有效的参数（V4DSCPValue，V6DSCPValue，DFValue，V4TOSVALUE，V4PRECEDENCE，V6TOSVALUE，V6PRECEDENCE，VLAN8021P）。        |

#### 使用实例

增加重标记配置：

```
ADD SQOSREMARK:BEHAVIORNAME="b1",DFVALUE=1,V4TOSVALUE=2,V6TOSVALUE=2,V6PRECEDENCE=2,VLAN8021P=2;
```