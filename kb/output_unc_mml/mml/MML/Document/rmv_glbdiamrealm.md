# 删除全局Diameter域（RMV GLBDIAMREALM）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用NF：PGW-C、SMF**

该命令用于解除全局Diameter域与指定IMSI/MSISDN号段的绑定关系，或撤销指定IMSI/MSISDN号段Diameter域信息通过IMSI构造的方式。

#### 注意事项

该命令执行后只对新激活用户生效。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识        | 参数名称            | 参数说明                                                                                                                                                                                                                                               |
|:------------|:----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| APPLICATION | Diameter应用      | 可选必选说明：必选参数 参数含义：该参数用于指定全局Diameter域所属的Diameter应用。 数据来源：全网规划 取值范围：枚举类型。 GY：Gy接口应用。GX：Gx接口应用。S6B：S6b接口应用。 默认值：无 配置原则：根据实际应用场景选择对应的枚举值。                                                                                                               |
| SCOPE       | 指定IMSI/MSISDN号段 | 可选必选说明：可选参数 参数含义：该参数用于选择是否指定IMSI/MSISDN号段删除Diameter域。 数据来源：本端规划 取值范围：枚举类型。 UNSPECIFIED：无IMSI/MSISDN号段。SPECIFIED：有IMSI/MSISDN号段。 默认值：无 配置原则： 设置为UNSPECIFIED，则删除不带号段绑定的Diameter域。设置为SPECIFIED，则删除指定IMSI/MSISDN号段绑定的Diameter域。不设置则表示删除所有对应的Diameter域。 |
| SEGMENTNAME | IMSI/MSISDN号段名称 | 可选必选说明：条件必选参数 前提条件：该参数在“SCOPE”配置为“SPECIFIED”时为必选参数。 参数含义：该参数用于指定要与Diameter域绑定的IMSI/MSISDN号段的名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 默认值：无 配置原则：无                                                                                        |

#### 使用实例

号段imsi\_msisdn\_segment\_1不再使用Gx应用，则使用命令删除Gx应用的Diameter域和指定号段imsi\_msisdn\_segment\_1的绑定：

```
RMV GLBDIAMREALM: APPLICATION=GX, SCOPE=SPECIFIED, SEGMENTNAME="imsi_msisdn_segment_1";
```