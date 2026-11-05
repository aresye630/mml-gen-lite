# 修改PCC策略组（MOD PCCPOLICYGRP）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用NF：PGW-C、SMF**

此命令用于修改PccPolicyGrp配置，只有已经添加成功的PccPolicyGrp才能够修改。可以通过此命令，修改PCC策略组，包括计费属性、Qos属性、扩展属性等构成策略集，同时支持基于ServiceProp选择不同的非默认策略集。

#### 注意事项

- 该命令执行后立即生效。
- PccPolicyGrp可以包含URRGroupName(Charge porperty)，FupSessionExc，QosPropName，所有参数都是可选，如果一个都没有选，则配置一个空的PccPolicyGrp。
- PccPolicyGrp中最多可以配置十个URRGroupName，FupSessionExc的组合。一个默认组合，九个非默认组合，或者无默认组合时，可以配置十个非默认组合。
- 默认组合的PccPolicyGrp不含ServiceProp，即是以URRGroupName，FupSessionExc形成的组合。
- 非默认组合以ServiceProp作为组合的标识，通过ADD SRVPBINDPCCPG添加一个新的非默认组合，通过MOD SRVPBINDPCCPG修改ServiceProp，URRGroupName，FupSessionExc组合。
- 如果PccPolicyGrp配置了多种组合，则匹配优先级取决于SrvPBindPccPG下配置的ServiceProp优先级。默认组合的优先级最低。
- 被绑定的PccPolicyGrp不允许删除，必须先解除绑定关系。但是可以动态添加、修改、删除组合。
- URRGroupName，QosPropName参数如果输入为空格，则相当于清空本PccPolicyGrp中该属性的配置。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识           | 参数名称            | 参数说明                                                                                                                                                                                                                                                                                                                 |
|:---------------|:----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PCCPOLICYGRPNM | PCC策略组名称        | 可选必选说明：必选参数 参数含义：设置PCC策略组名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。 默认值：无 配置原则：无                                                                                                                                                                                                                             |
| URRGROUPNAME   | 使用量上报规则组名称      | 可选必选说明：可选参数 参数含义：设置URR组名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 默认值：无 配置原则： 该参数使用ADD URRGROUP命令配置生成。如果运营商需要定义该PCC策略组的计费策略时，建议配置用于计费处理的计费属性对象名称。                                                                                                                                                            |
| FUPSESSIONEXC  | Session级FUP累计标识 | 可选必选说明：可选参数 参数含义：设置Session级FUP流量累计标识。该参数会用于控制Gx接口向PCRF上报业务级和Session的流量累计方式。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不使能，表明该PccPolicyGrp对应的业务流量计入Session级流量。ENABLE：使能，表明该PccPolicyGrp对应的业务流量不计入Session级流量。 默认值：无 配置原则：如果运营商需要定义该PCC策略组业务级FUP流量累计时，是否同时累计到Session级流量，建议配置Session级FUP流量累计标识。该参数会用于控制Gx接口向PCRF上报业务级和Session的流量累计方式。 |
| QOSPROPNAME    | QoS属性名称         | 可选必选说明：可选参数 参数含义：设置QoS属性名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 默认值：无 配置原则： 该参数使用ADD QOSPROP命令配置生成。如果运营商需要定义该PCC策略组的QoS策略时，建议配置用于QoS控制的QoS属性对象名称。解绑时支持空格。                                                                                                                                                 |

#### 使用实例

假如运营商需要定义一个PCC策略组，要求在该PCC策略组中包含计费策略、QoS策略等。
修改PCC策略组，设置包括计费属性、Qos属性的默认组合；“PCCPOLICYGRPNM”为“TestPccPolicyGrpNm”，“URRGroupName”为“TestChargePropName”，“QOSPROPNAME”为“TestQoSPropName”：

```
MOD PCCPOLICYGRP:PCCPOLICYGRPNM="TestPccPolicyGrpNm",URRGroupName="TestChargePropName",QOSPROPNAME="TestQoSPropName";
```