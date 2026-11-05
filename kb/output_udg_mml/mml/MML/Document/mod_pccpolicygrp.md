# 修改PCC策略组（MOD PCCPOLICYGRP）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用NF：PGW-U、UPF**

此命令用于修改PccPolicyGrp配置，只有已经添加成功的PccPolicyGrp才能够修改。可以通过命令，修改PCC策略组，包括使用量上报规则组、PCC动作属性、扩展属性等构成策略集，同时支持基于ServiceProp选择不同的非默认策略集。

#### 注意事项

- 该命令执行后立即生效。
- PccPolicyGrp可以包含ServiceProp，URRGroupName，PccActionProp，FupSessionExc，ExtendProp，MMSChargeType，TokenSecretKey，SignalAssociate，SigURRGroupName，QosPropName所有参数都是可选，如果一个都没有选，则配置一个空的PccPolicyGrp。
- PccPolicyGrp中最多可以配置十一个ServiceProp，URRGroup，PccActionProp，FupSessionExc，ExtendProp的组合。一个默认组合，十个非默认组合。
- 默认组合的PccPolicyGrp不含ServiceProp，即是以URRGroup，PccActionProp，FupSessionExc，ExtendPropy形成的组合。
- 非默认组合以ServiceProp作为组合的标识，通过ADD SRVPBINDPCCPG添加一个新的非默认组合，通过MOD SRVPBINDPCCPG修改ServiceProp，URRGroup，PccActionProp ，FupSessionExc ，ExtendProp组合。
- 如果PccPolicyGrp配置了多种组合，则匹配优先级取决于SrvPBindPccPG下配置的ServiceProp优先级。默认组合的优先级最低。
- 被绑定的PccPolicyGrp不允许删除，必须先解除绑定关系。但是可以动态添加、修改、删除组合。
- ExtendProp，URRGroupName，PccActionProp，SigURRGroupName，QosPropName参数如果输入为空格，则相当于清空本PccPolicyGrp中该属性的配置。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识                  | 参数名称            | 参数说明                                                                                                                                                                                                                                                                                                                                          |
|:----------------------|:----------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PCCPOLICYGRPNM        | PCC策略组名称        | 可选必选说明：必选参数 参数含义：设置PCC策略组名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。 默认值：无 配置原则：无                                                                                                                                                                                                                                                      |
| PCCACTPROPNAME        | PCC动作属性名称       | 可选必选说明：可选参数 参数含义：设置PCC动作属性名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 默认值：无 配置原则： 该参数使用ADD PCCACTIONPROP命令配置生成。如果运营商需要定义该PCC策略组的PCC动作策略时，建议配置用于控制处理的PCC动作属性对象名称。                                                                                                                                                                       |
| EXTENDPROPNAME        | 扩展属性名称          | 可选必选说明：可选参数 参数含义：设置扩展属性名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。 默认值：无 配置原则： 该参数使用ADD EXTENDPROP命令配置生成。如果运营商需要定义该PCC策略组的扩展属性时，建议配置相应的扩展属性对象名称。                                                                                                                                                                                       |
| FUPSESSIONEXC         | Session级FUP累计标识 | 可选必选说明：可选参数 参数含义：设置Session级FUP流量累计标识。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不使能，表明该PccPolicyGrp对应的业务流量计入Session级流量。ENABLE：使能，表明该PccPolicyGrp对应的业务流量不计入Session级流量。 默认值：无 配置原则： 如果运营商需要定义该PCC策略组业务级FUP流量累计时，是否同时累计到Session级流量，建议配置Session级FUP流量累计标识。该参数会用于控制Gx接口向PCRF上报业务级和Session的流量累计方式。当前UPF不支持控制具体的PCC策略组不计入Session级FUP流量。                           |
| TOKENFUNCFLAG         | Token检测功能标识     | 可选必选说明：可选参数 参数含义：设置Token检测功能标识。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不使能（关闭）。ENABLE：使能（开启）。 默认值：无 配置原则：如果运营商需要定义RTSP业务流的Token检测功能时，需要通过配置本参数来设置。                                                                                                                                                                                                      |
| TOKENENCRYALG         | Token加密算法       | 可选必选说明：条件可选参数 前提条件：该参数在“TOKENFUNCFLAG”配置为“ENABLE”时为可选参数。 参数含义：设置Token加密算法。 数据来源：本端规划 取值范围：枚举类型。 SHA256：使用SHA256算法进行token加密。MD5：使用MD5算法进行Token加密，MD5算法为非安全算法，建议使用SHA算法。 默认值：无 配置原则：如果运营商需要设置RTSP业务流的Token加密功能时，需要通过配置本参数来设置加密算法。                                                                                                               |
| TOKENSECRETKEY        | Token密钥         | 可选必选说明：条件必选参数 前提条件：该参数在“TOKENFUNCFLAG”配置为“ENABLE”时为必选参数。 参数含义：设置Token校验密钥。 数据来源：本端规划 取值范围：密钥类型，输入长度范围为1～63。不支持空格。 默认值：无 配置原则：如果运营商需要定义RTSP业务流的Token检测功能时，需要通过配置本参数来设置Token检测时使用的密钥。                                                                                                                                                           |
| TOKENSECRETKEYCONFIRM | 确认Token密钥       | 可选必选说明：条件必选参数 前提条件：该参数在“TOKENFUNCFLAG”配置为“ENABLE”时为必选参数。 参数含义：确认Token校验密钥。 数据来源：本端规划 取值范围：密钥类型，输入长度范围为1～63。不支持空格。 默认值：无 配置原则：如果运营商需要定义RTSP业务流的Token检测功能时，需要通过配置本参数来设置Token检测时使用的密钥。                                                                                                                                                           |
| SIGNALASSOCIATE       | 信令关联计费标识        | 可选必选说明：可选参数 参数含义：设置信令关联标识。 数据来源：本端规划 取值范围：枚举类型。 ENABLE：使能信令关联标识，信令报文需要与业务报文进行关联计费。DISABLE：不使能信令关联标识，信令报文不需要与业务报文进行关联计费。 默认值：无 配置原则： 如果运营商需要定义建链信令报文的计费方式时，需要配置本参数。如果运营商希望每个业务流的建链信令报文与业务报文的计费方式一致，对外呈现一个计费属性，则配置该参数为ENABLE。如果运营商希望每个业务流的建链信令报文独立计费，不需要与业务报文的计费方式保持一致，对外呈现多个计费属性，则配置该参数为DISABLE。                                               |
| ADCMUTEFLAG           | ADC静默通知标识       | 可选必选说明：可选参数 参数含义：设置ADC静默通知标识。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不使能ADC静默通知标识，不静默应用检测通知消息，支持向PCRF/PCF的应用检测上报。ENABLE：使能ADC静默通知标识，静默应用检测通知消息，不支持向PCRF的应用检测上报。 默认值：无 配置原则： 如果运营商需要定义ADC（应用检测与控制）功能的静默通知标识，需要配置本参数。如果运营商希望不使能应用检测上报功能，不向PCRF上报检测到的应用标识和start/stop事件。则配置该参数为ENABLE。如果运营商希望使能应用检测上报功能，识别出应用的start/stop事件时，向PCRF上报检测到的应用标识。则配置该参数为DISABLE。 |
| QOSPROPNAME           | Qos属性名称         | 可选必选说明：可选参数 参数含义：设置QoS属性名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 默认值：无 配置原则： 该参数使用ADD QOSPROP命令配置生成。如果运营商需要定义该PCC策略组的QoS策略时，建议配置用于QoS控制的QoS属性对象名称。                                                                                                                                                                                  |
| HTTP2DEGRADESW        | HTTP2.0协议回落开关   | 可选必选说明：可选参数 参数含义：该参数用于设置HTTP2.0协议开关回落。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不使能，不支持HTTP2协议回落。ENABLE：使能，支持HTTP2协议回落。INHERIT：继承，HTTP2协议回落开关需要继承上一级回落开关。 默认值：无 配置原则：如果运营商需要修改Rule级的HTTP2协议回落开关时，可以配置本参数。                                                                                                                                                 |
| URRGROUPNAME          | URR组名称          | 可选必选说明：可选参数 参数含义：设置计费属性名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 默认值：无 配置原则： 该参数使用ADD URRGROUP命令配置生成。如果运营商需要定义该PCC策略组的使用量上报规则时，建议配置用于计费处理的使用量上报规则对象名称。                                                                                                                                                                               |
| SIGURRGRPNAME         | 信令URR组名称        | 可选必选说明：可选参数 参数含义：设置信令计费属性名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 默认值：无 配置原则： 该参数使用ADD URRGROUP命令配置生成。如果运营商需要定义该PCC策略组下信令报文的使用量上报规则时，建议配置用于计费处理的信令使用量上报规则对象名称。                                                                                                                                                                      |
| EVENTCHARGEFLAG       | 事件计费标识          | 可选必选说明：可选参数 参数含义：设置事件计费标识。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不使能事件计费功能。ENABLE：使能事件计费功能。 默认值：无 配置原则：如果运营商需要开启事件计费功能时，可以配置本参数。                                                                                                                                                                                                                       |
| EVENTCHGPOINT         | 事件计费点           | 可选必选说明：可选参数 参数含义：设置事件计费点。 数据来源：本端规划 取值范围：枚举类型。 REQUEST：收到事件请求作为计费点。RESPONSE：收到事件的第一个响应报文作为计费点。FINISH：收全事件的所有响应报文作为计费点。 默认值：无 配置原则：如果运营商需要设置事件计费的计费点时，可以配置本参数。                                                                                                                                                                                 |
| MMSCHARGETYPE         | 彩信计费类型          | 可选必选说明：可选参数 参数含义：设置彩信计费类型。 数据来源：本端规划 取值范围：枚举类型。 SINGLE：表示群发彩信按单条彩信计费。MULTI：表示群发彩信按多条彩信计费。 默认值：无 配置原则：彩信事件计费使能时，CC消息是按多条彩信计费或按单条彩信计费。                                                                                                                                                                                                          |
| CFGDOMAINNAME         | 配置域名称           | 可选必选说明：可选参数 参数含义：该参数表示命令所属公共配置域的名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～31。 默认值：无 配置原则：无                                                                                                                                                                                                                                                            |

#### 使用实例

假如运营商需要修改一个PCC策略组，要求在该PCC策略组中包含使用量上报规则组、PCC动作策略和QoS策略，建链信令报文需要与业务报文采用相同的计费策略。
修改PCC策略组，设置包括使用量上报规则组、PCC动作属性的默认组合，同时设置QoS属性和信令关联标识；“PCCPOLICYGRPNM”为“TestPccPolicyGrpNm”，“URRGROUPNAME”为“TestURRGrpName”，“PCCACTPROPNAME”为“TestPccActPropName”，“QOSPROPNAME”为“TestQoSPropName”，“SIGNALASSOCIATE”为“ENABLE”：

```
MOD PCCPOLICYGRP:PCCPOLICYGRPNM="TestPccPolicyGrpNm",URRGROUPNAME="TestURRGrpName",PCCACTPROPNAME="TestPccActPropName", QOSPROPNAME="TestQoSPropName",SIGNALASSOCIATE=ENABLE;
```