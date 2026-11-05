# 设置业务通信代理模型(SET SCPMODEL)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于设置目标NF类型的间接通信模型。

该命令的使用场景：当PCF作为客户端与对端CHF/BSF/SMF/AMF/VPCF/HPCF/AF/NWDAF对接的场景下，可使用本命令设置基于目标NF类型是否使能间接通信功能及通信代理模型。

## 注意事项

该命令存在系统初始记录，参数的初始设置值如下表：

| 网元类型   | 模型     |   API前缀 | API版本   | 开关   | 绑定级别           |
|:-------|:-------|--------:|:--------|:-----|:---------------|
| CHF    | MODELD |     nan | v1      | 非使能  | NFSET          |
| BSF    | MODELD |     nan | v1      | 非使能  | NFSET          |
| SMF    | MODELD |     nan | v1      | 非使能  | NFSET          |
| AMF    | MODELD |     nan | v1      | 非使能  | NFSET          |
| VPCF   | MODELD |     nan | v1      | 非使能  | NOBINDINGLEVEL |
| HPCF   | MODELD |     nan | v1      | 非使能  | NOBINDINGLEVEL |
| AF     | MODELD |     nan | v1      | 非使能  | NFSET          |
| NWDAF  | MODELD |     nan | v1      | 非使能  | NFSET          |

- 当本命令参数“开关”取值为“ENABLE(使能)”时，如果SCP网元全部故障，本版本不支持自动回落至直连模型，需要手动配置本命令，将参数“开关”设置为“DISABLE(非使能)”。

- 本命令执行后只针对新上线用户生效，如果需要对所有用户生效，请先执行**SND SSCR**命令将在线的用户下线，再让用户重新上线。

- 若SMF针对UPCF使能Model D，但UPCF针对SMF未使能Model D，则UPCF向SMF发送Npcf\_SMPolicyControl\_UpdateNotify Request消息时会按Model B模式发送给SMF。

- 本命令参数“开关”，只能控制UPCF发送给对端网元的请求消息是否经过SCP转发。UPCF返回对端网元的响应消息是否经过SCP转发，不受本命令参数“开关”取值的控制。当参数“开关”取值为“ENABLE(使能)”时，UPCF返回的响应消息中会携带Model D的相关头域信息。

## 参数说明

| 参数标识         | 参数名称   | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|:-------------|:-------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NFTYPE       | 网元类型   | 可选必选说明：必选参数 参数含义：用于设置目标NF。 取值范围： CHF(CHF)BSF(BSF)SMF(SMF)AMF(AMF)VPCF(VPCF)HPCF(HPCF)AF(AF)NWDAF(NWDAF) 默认值：无。 配置原则：无。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| MODEL        | 模型     | 可选必选参数：必选参数 参数含义：用于配置SCP模型，满足PCF作为客户端时灵活配置发现目标NF的方式。 取值范围： MODELD(MODELD) 默认值：无。 配置原则：无。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| APIPREFIX    | API前缀  | 可选必选说明：可选参数。 参数含义：用于配置{apiroot}中<apiprefix>字段的值。该参数当“模型”取值为“MODELD(MODELD)”时为条件可选参数。 取值范围：长度不超过128位字符串 默认值：无 配置原则：无。  说明： {apiroot}由以下部分组成：scheme：http或https。固定字符串："//"。authority：主机和可选端口。主机应使用运营商特定的FQDN表示。apiprefix：可选的deployment特定字符串，以“/”字符开头。 UPCF作为Consumer时，在Model D组网下只支持基于NF类型配置的SCP的apiprefix。如果使用本参数，则要求UPCF对接的所有SCP都支持该NF类型的apiprefix。                                                                                                                                                                                                                                                                                                                                                                                               |
| APIVERSION   | API版本  | 可选必选说明：可选参数 参数含义：用于配置URI（{apiroot}/<apiName>/<apiversion>/<apiSepcificResourceUriPart>）中<apiversion>字段的值。该参数当“模型”取值为“MODELD(MODELD)”时为条件必选参数。 取值范围： v0(v0)v1(v1)v2(v2) 默认值：v1(v1) 配置原则：无。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| SWITCH       | 开关     | 可选必选说明：必选参数 参数含义：用于配置针对目标NF是否使能SCP功能。 取值范围： DISABLE(非使能)ENABLE(使能) 默认值：DISABLE(非使能) 配置原则：无。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| BINDINGLEVEL | 绑定级别   | 可选必选说明：可选参数 参数含义：用于配置UPCF发送给对端的消息中3gpp-Sbi-Binding头域的填充方式。 取值范围： NFSET(NFSET)：表示3gpp-Sbi-Binding头域中的bl为nf-set。NFINSTANCE(NFINSTANCE)：表示3gpp-Sbi-Binding头域中的bl为nf-instance。NOBINDINGLEVEL(NOBINDINGLEVEL)：表示不下发3gpp-Sbi-Binding头域。 默认值：NFSET(NFSET) 配置原则：无。  说明： “绑定级别”的取值判断依赖于软参“VRM_MULTIPCFLOGICINSTSW”的设置。“VRM_MULTIPCFLOGICINSTSW”取值为“0”时，取值来源于PCF实例关联的nfset信息或PCF实例标识。“VRM_MULTIPCFLOGICINSTSW”取值为“1”时，取值来源于号段匹配的PCF实例关联的nfset信息或PCF实例标识。 “绑定级别”取值为“NFSET(NFSET)”时：nfset值来源于增加网元集合配置信息(ADD NFSET)命令中的配置信息，例如：3gpp-Sbi-Binding: bl=nf-set;nfset=setpcf001.pcfset.5gc.mnc003.mcc525。“绑定级别”取值为“NFINSTANCE(NFINSTANCE)”：nfinst值来源于增加网元实例信息(ADD NFSRV)命令中的配置信息，例如：3gpp-Sbi-Binding: bl=nf-instance; nfinst=54804518-4191-46b3-955c-ac631f953ed8。 |

## 使用实例

设置业务通信代理模型信息，其中，“网元类型”为“CHF(CHF)”，“模型”为“MODELD(MODELD)”，“API前缀”为“/1/2/3”，“API版本”为“v1(v1)”，“开关”为“ENABLE(使能)”，“绑定级别”为“NFSET(NFSET)”。

```
SET SCPMODEL: NFTYPE=CHF, MODEL=MODELD, APIPREFIX="/1/2/3", APIVERSION=v1, SWITCH=ENABLE, BINDINGLEVEL=NFSET;
```

## 输出结果说明

命令执行正常，会返回命令执行成功的提示信息。