# 修改PCC模板（MOD PCCTEMPLATE）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用NF：PGW-C、SMF**

该命令用于修改一个PCC模板配置。

#### 注意事项

- 该命令执行后只对新激活用户生效。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识             | 参数名称                            | 参数说明                                                                                                                                                                                                                                                                                                                     |
|:-----------------|:--------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PCCTEMPNAME      | PCC模板名称                         | 可选必选说明：必选参数 参数含义：该参数用于指定PCC模板的名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写，不允许命名为“global”。 默认值：无 配置原则：无                                                                                                                                                                                                             |
| REPORTLEVEL      | 缺省上报级别                          | 可选必选说明：可选参数 参数含义：该参数用于指定PCC功能使能情况下的缺省上报级别。 数据来源：对端协商 取值范围：枚举类型。 RG：基于Rating Group上报。SID：基于Service Identifier上报。 默认值：无 配置原则：无                                                                                                                                                                                             |
| METERMETHOD      | 缺省离线计费统计方式                      | 可选必选说明：可选参数 参数含义：该参数用于指定PCC功能使能情况下的缺省离线计费统计方式。 数据来源：对端协商 取值范围：枚举类型。 VOLUME：流量，基于流量计费。DURATION：时长，基于时长计费。DURATION_VOLUME：时长加流量，基于流量叠加时长计费。 默认值：无 配置原则：无                                                                                                                                                                   |
| ORGHOSTCCAI      | 基于CCA-I Origin-Host AVP触发PCRF重选 | 可选必选说明：可选参数 参数含义：该参数用于设置激活流程中，UNC是否支持由CCA-I触发的PCRF重选。即当UNC收到PCRF给UNC发送的CCA-I消息中携带新的Origin-Host名字的场景，UNC后续在给对端发送CCR消息时，是否会将Destination-Host更新成这个新的host名字。 数据来源：对端协商 取值范围：枚举类型。 DISABLE：否。ENABLE：是。 默认值：无 配置原则：无                                                                                                           |
| ORGHOSTCCAU      | 基于CCA-U Origin-Host AVP触发PCRF重选 | 可选必选说明：可选参数 参数含义：该参数用于设置更新流程中，UNC是否支持由CCA-U触发的PCRF重选。即当UNC收到PCRF给UNC发送的CCA-U消息中携带新的Origin-Host名字的场景，UNC后续在给对端发送CCR消息时，是否会将Destination-Host更新成这个新的host名字。 数据来源：对端协商 取值范围：枚举类型。 DISABLE：否。ENABLE：是。 默认值：无 配置原则：无                                                                                                           |
| ORGHOSTRAR       | 基于RAR Origin-Host AVP触发PCRF重选   | 可选必选说明：可选参数 参数含义：该参数用于设置更新流程中，UNC是否支持由RAR触发的PCRF重选。即当UNC收到PCRF给UNC发送的RAR消息中携带新的Origin-Host名字的场景，UNC后续在给对端发送CCR消息时，是否会将Destination-Host更新成这个新的host名字。 数据来源：对端协商 取值范围：枚举类型。 DISABLE：否。ENABLE：是。 默认值：无 配置原则：无                                                                                                               |
| SELPEERFAILACT   | 选择PCF/PCRF失败动作                  | 可选必选说明：可选参数 参数含义：该参数用于配置激活过程中根据号段匹配选择PCF、PcrfGroup和Realm失败情况下系统执行的动作。 数据来源：本端规划 取值范围：枚举类型。 DEFAULT：回滚为本地PCC用户。ROLLBACK：回滚为本地PCC用户。如果APN用户使能PCC功能，并且配置了缺省的PCRF group和realm，则选择缺省的PCRF group和realm；如果没有配置缺省的PCRF group和realm，则进行回滚处理。如果APN用户的PCC使能开关继承全局配置，全局配置使能PCC功能，则进行回滚处理。INHERIT：继承全局配置。FORBIDDEN：激活失败。 默认值：无 配置原则：无 |
| SELPEERLOCPCC    | 选择PCF/PCRF失败回滚为Local PCC用户类型    | 可选必选说明：条件可选参数 前提条件：该参数在“SELPEERFAILACT”配置为“ROLLBACK”时为可选参数。 参数含义：该参数用于配置激活过程中根据号段匹配选择PcrfGroup和Realm失败情况下使用本地User Profile进行回滚的处理结果。 数据来源：本端规划 取值范围：枚举类型。 LOCAL_PCC：表示回滚PCC用户为本地PCC用户。 默认值：无 配置原则：无                                                                                                                       |
| SELPEERRDSPCC    | 选择PCF/PCRF失败回滚为RADIUS PCC用户类型   | 可选必选说明：条件可选参数 前提条件：该参数在“SELPEERFAILACT”配置为“ROLLBACK”时为可选参数。 参数含义：该参数用于配置激活过程中根据号段匹配选择PcrfGroup和Realm失败情况下Radius Server下发单个User Profile场景下的回滚结果。 数据来源：本端规划 取值范围：枚举类型。 LOCAL_PCC：表示回滚RADIUS PCC用户为本地PCC用户。 默认值：无 配置原则：无                                                                                                    |
| INITIALFAILACT   | Initial流程故障处理动作                 | 可选必选说明：可选参数 参数含义：该参数用于指定激活过程中Gx/N7链路故障、流控丢消息或响应超时情况下系统执行的动作。 数据来源：本端规划 取值范围：枚举类型。 FORBIDDEN：激活失败。ROLLBACK：回滚。INHERIT：继承全局配置。 默认值：无 配置原则：无                                                                                                                                                                                |
| INITFAILLOCPCC   | Initial流程故障回滚为Local PCC用户类型     | 可选必选说明：条件可选参数 前提条件：该参数在“INITIALFAILACT”配置为“ROLLBACK”时为可选参数。 参数含义：该参数用于配置激活过程中Gx/N7链路故障、流控丢弃消息或响应超时情况下使用本地User Profile进行回滚的处理结果。 数据来源：本端规划 取值范围：枚举类型。 LOCAL_PCC：表示回滚PCC用户为本地PCC用户。 默认值：无 配置原则：无                                                                                                                           |
| INITFAILRDSPCC   | Initial流程故障回滚为RADIUS PCC用户类型    | 可选必选说明：条件可选参数 前提条件：该参数在“INITIALFAILACT”配置为“ROLLBACK”时为可选参数。 参数含义：该参数用于配置激活过程中Gx/N7链路故障、流控丢消息或响应超时情况下Radius Server下发单个User-Profile场景下的回滚结果。 数据来源：本端规划 取值范围：枚举类型。 LOCAL_PCC：表示回滚RADIUS PCC用户为本地PCC用户。 默认值：无 配置原则：无                                                                                                         |
| UPDATEFAILACT    | Update流程故障处理动作                  | 可选必选说明：可选参数 参数含义：该参数用于指定给PCRF/PCF发送更新消息过程中Gx/N7链路故障、流控丢弃消息或响应超时情况下系统执行的动作。 数据来源：本端规划 取值范围：枚举类型。 ROLLBACK：回滚。TERMINATE：去活用户。CONTINUE：继续与PCRF/PCF交互。INHERIT：继承全局配置。 默认值：无 配置原则：无                                                                                                                                           |
| UPDFAILLOCPCC    | Update流程故障回滚为Local PCC用户类型      | 可选必选说明：条件可选参数 前提条件：该参数在“UPDATEFAILACT”配置为“ROLLBACK”时为可选参数。 参数含义：该参数用于配置更新过程中Gx/N7链路故障、流控丢弃消息或响应超时情况下使用本地User Profile进行回滚的处理结果。 数据来源：本端规划 取值范围：枚举类型。 LOCAL_PCC：表示Update流程故障回滚PCC用户为本地PCC用户。INHERIT_PCC：表示Update流程故障回滚PCC用户为本地PCC用户并且继续使用PCRF/PCF策略。 默认值：无 配置原则：无                                                          |
| HOLDINGTIME      | 用户回滚后在线保持时长（分钟）                 | 可选必选说明：可选参数 参数含义：该参数用于设置用户回滚后的在线保持时长。 数据来源：本端规划 取值范围：整数类型，取值范围为0～1440，65535，单位是分钟。 默认值：无 配置原则： 如果时长配置为65535，表示继承全局PCC配置。如果时长配置为0，则用户回滚后保持在线，直到用户主动下线。如果时长配置为非0，则从用户自动放通开始计时，超时后UNC主动将用户去活。                                                                                                                               |
| ADJUSTRANGE      | 随机延迟范围（分钟）                      | 可选必选说明：可选参数 参数含义：该参数用于设置HOLDINGTIME超时后增加一个随机调整范围。 数据来源：本端规划 取值范围：整数类型，取值范围为0～60，单位是分钟。 默认值：无 配置原则： 不配置此参数表示不增补HoldingTime时长。当HoldingTime配置为0或者65535时，该参数配置不生效。                                                                                                                                                           |
| LOCSLCTMODE      | 本端主机名选择模式                       | 可选必选说明：可选参数 参数含义：该参数用于设置PCC本端主机名选择模式。 数据来源：本端规划 取值范围：枚举类型。 LOADSHARING：负荷分担模式，表示用户激活时轮选本端主机名。SPECIFIC：表示用户激活时，选择LOCALHOSTNAME指定的本端主机名所对应的链路进行消息交互。INHERIT：继承全局配置。UPFGRP：表示按照UPF Group粒度选择本端主机名，即按照UPFGLOCGBNDGNAME指定的本端主机组范围来选择。 默认值：无 配置原则：无                                                                            |
| LOCALHOSTNAME    | 本端主机名                           | 可选必选说明：条件必选参数 前提条件：该参数在“LOCSLCTMODE”配置为“SPECIFIC”时为必选参数。 参数含义：该参数用于设置PCC本端主机名。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～127。 默认值：无 配置原则： 该参数使用ADD DIAMLOCINFO命令配置生成。该参数对应的DIAMLOCINFO需为Gx应用使用的DIAMLOCINFO。                                                                                                                          |
| NTFRSRURI        | 基于Notify消息ResourceURI触发PCF重选    | 可选必选说明：可选参数 参数含义：该参数用于设置当收到PCF发送的UpdateNotify携带的ResourceURI与当前会话使用的PCF不同，是否允许触发PCF重定向。 数据来源：本端规划 取值范围：枚举类型。 INHERIT：继承全局N7RcvAttrCtrl配置。DISABLE：忽略PCF发送的UpdateNotify携带的ResourceURI，不触发PCF重选。ENABLE：根据PCF发送的UpdateNotify携带的ResourceURI触发PCF重选。 默认值：无 配置原则：无                                                               |
| N7FAILOVERSW     | N7 Failover功能开关                 | 可选必选说明：可选参数 参数含义：该参数用于此APN下用户是否支持N7接口failover功能。使能时，在与主PCF交互失败的情况下，SMF会执行Failover动作，将用户消息交互切换到备PCF上进行处理。 数据来源：对端协商 取值范围：枚举类型。 DISABLE：不使能APN的N7 Failover功能。ENABLE：使能N7 Failover功能。INHERIT：继承全局配置。 默认值：无 配置原则：无                                                                                                           |
| PCFLBPARA        | PCF负荷分担参数                       | 可选必选说明：可选参数 参数含义：本参数用于指定PCF负荷分担参数。 数据来源：对端协商 取值范围：枚举类型。 INHERIT：继承全局配置。GROUPID：根据GroupID负荷分担。PRIORITY：根据优先级负荷分担。 默认值：无 配置原则：无                                                                                                                                                                                            |
| UPFGLOCGBNDGNAME | UPF组与Diameter本端主机组的绑定关系组名称      | 可选必选说明：条件必选参数 前提条件：该参数在“LOCSLCTMODE”配置为“UPFGRP”时为必选参数。 参数含义：该参数设置UPF组与Diameter本端主机组的绑定关系组名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。 默认值：无 配置原则：该参数使用ADD UPFGLOCGBNDGRP命令配置生成。                                                                                                                                    |
| USEN15PCFSW      | 优先使用N15 PCF开关                   | 可选必选说明：可选参数 参数含义：本参数用于指定N7优先使用N15 PCF。 数据来源：全网规划 取值范围：枚举类型。 DISABLE：N7接口不优先使用N15 PCF。ENABLE：N7优先使用N15 PCF。INHERIT：继承全局配置。 默认值：无 配置原则：无                                                                                                                                                                                   |

#### 使用实例

因业务变更，需要修改一个APN对应的PCC功能，以便完成业务功能适配：

```
MOD PCCTEMPLATE: PCCTEMPNAME="new_pcc_template",REPORTLEVEL=RG,HOLDINGTIME=10,ADJUSTRANGE=1;
```