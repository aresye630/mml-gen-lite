# 设置APN PCC功能（SET APNPCCFUNC）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用NF：PGW-C、SMF**

此命令用于使能或关闭指定APN/DNN用户的动态PCC功能。

PCC即策略和计费控制，当运营商需要通过动态PCC功能对计费策略和计费的粒度进行灵活控制，从而优化运营商的计费手段，提高收益时，可以通过此命令使能指定APN用户的动态PCC功能。

#### 注意事项

- 该命令执行后只对新激活用户生效。
- 该命令最大记录数为10000。
- 在每次执行ADD CPAPN命令时会自动为本命令增加一条记录，记录中参数的初始设置值如下：HOMEPCCSWITCH=INHERIT,RoamPCCSwitch=INHERIT,VisitPCCSwitch=INHERIT,PCCTEMPLATE=NULL,PCFSelectMode=NULL。
- 当HOMEPCCSWITCH、ROAMPCCSWITCH、VISITPCCSWITCH配置为ENABLE，且需要绑定PCRF时，请参考章节“配置动态PCC功能”中的表一“PCRF选择原则”进行配置。
- 当HOMEPCCSWITCH、ROAMPCCSWITCH、VISITPCCSWITCH配置为INHERIT时，通过读取配置ADD GLBDIAMREALM获取域名；当HOMEPCCSWITCH、ROAMPCCSWITCH、VISITPCCSWITCH配置为ENABLE时，通过读取配置ADD REALMBINDAPN获取域名。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识           | 参数名称        | 参数说明                                                                                                                                                                                                                                                                        |
|:---------------|:------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| APN            | APN名称       | 可选必选说明：必选参数 参数含义：该参数用于指定APN实例名称。 数据来源：全网规划 取值范围：字符串类型，输入长度范围为1～63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”特殊字符，不区分大小写。 默认值：无 配置原则：该参数必须已经通过命令ADD CPAPN配置。                                                   |
| HOMEPCCSWITCH  | 本地用户动态PCC功能 | 可选必选说明：可选参数 参数含义：该参数用于指定APN的本地用户动态PCC功能是否使能。 数据来源：对端协商 取值范围：枚举类型。 DISABLE：不使能APN的动态PCC功能。ENABLE：使能APN的动态PCC功能。INHERIT：和SET PCCFUNC内该参数取值保持一致。 默认值：无 配置原则：无                                                                                                                  |
| ROAMPCCSWITCH  | 漫游用户动态PCC功能 | 可选必选说明：可选参数 参数含义：该参数用于指定APN的漫游用户动态PCC功能是否使能。 数据来源：对端协商 取值范围：枚举类型。 DISABLE：不使能APN的动态PCC功能。ENABLE：使能APN的动态PCC功能。INHERIT：和SET PCCFUNC内该参数取值保持一致。 默认值：无 配置原则：无                                                                                                                  |
| VISITPCCSWITCH | 拜访用户动态PCC功能 | 可选必选说明：可选参数 参数含义：该参数用于指定APN的拜访用户动态PCC功能是否使能。 数据来源：对端协商 取值范围：枚举类型。 DISABLE：不使能APN的动态PCC功能。ENABLE：使能APN的动态PCC功能。INHERIT：和SET PCCFUNC内该参数取值保持一致。 默认值：无 配置原则：无                                                                                                                  |
| PCCTEMPLATE    | PCC模板名称     | 可选必选说明：可选参数 参数含义：该参数用于指定APN绑定的PCC模板。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63，不区分大小写。字符串中不能出现空格。 默认值：无 配置原则： 输入单空格将删除该参数已有配置项。该参数必须已经通过命令ADD PCCTEMPLATE配置。该参数若不配置，则继承通过SET PCCFUNC、SET PCCPCRFMSGATTR、SET PCCFAILACTION、SET PCCTIMER命令配置的全局PCC。                                    |
| PCFSELECTMODE  | 选择PCF方式     | 可选必选说明：可选参数 参数含义：配置PCF的选择策略。 数据来源：全网规划 取值范围：位域类型。 DNN：根据DNN选择PCF。IMSI：根据IMSI选择PCF。GPSI：根据GPSI选择PCF。SNSSAIS：根据S-NSSAIs选择PCF。PLMN：根据PLMN选择PCF。NFLOC：根据优选区域选择PCF(取值使用ADD CPNFPROFILE命令配置)。SERVINGSCOPE：根据ServingScope选择PCF。 默认值：无 配置原则：该参数若不配置，则继承通过SET PCCFUNC命令配置的全局选择PCF方式。 |
| DISCCUSTOM     | PCF状态过滤参数   | 可选必选说明：可选参数 参数含义：配置标准服务发现时PCF状态过滤参数。 数据来源：本端规划 取值范围：枚举类型。 MUTIL_SORTED_RES：不忽略NF及Service状态与链路状态。MUTIL_SORTED_RES_IGN_NF_ALL_STATUS_IGN_LINK_STAT：忽略NF及Service所有状态、忽略链路状态。INHERIT：继承SET PCCFUNC的该参数取值。 默认值：无 配置原则：无                                                          |

#### 使用实例

通过APN isp接入的用户希望激活成动态PCC用户，并使用PCC模板pcctp1配置，则可以按如下配置：

```
SET APNPCCFUNC:APN="isp",HOMEPCCSWITCH=ENABLE,PCCTEMPLATE="pcctp1";
```