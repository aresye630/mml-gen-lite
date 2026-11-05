# 增加配置MODELC/D组网的SCP原因码控制（ADD RESULTCODESCP）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：SMF、PGW-C、GGSN**

此命令用来配置当UNC收到指定组网场景结果码信息后执行何种操作。例如关闭PCC功能、执行缺省动作、执行宕机备份等。

## 注意事项

- 该命令执行后立即生效。

- SCP返回异常码场景，该配置命令优先级高于ADD RESULTCODECTRL。
- 当PCCTEMPLATE配置为“global”时，表示全局配置，最多能配置100条记录；当PCCTEMPLATE配置为指定PCC模板时，表示该PCC模板下的配置，最多能配置100条记录。

- 最多可输入1100条记录。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识            | 参数名称                                  | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|:----------------|:--------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PCCTEMPLATE     | PCC模板名称                               | 可选必选说明：必选参数  参数含义：该参数用于设置该返回码所绑定的PCC模板。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是1~63。  默认值：无  配置原则：  如果配置为“global”则表示全局配置。  如果配置为非“global”，则必须是已经通过ADD PCCTEMPLATE配置过的PCC模板名称。                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| MODELTYPE       | 组网场景                                  | 可选必选说明：必选参数  参数含义：该参数用于设置该返回码所应用的组网场景。  数据来源：本端规划 取值范围： “MODELC（组网场景为ModelC）”：组网场景为ModelC“MODELD（组网场景为ModelD）”：组网场景为ModelD。“MODELC_D（组网场景为ModelC和ModelD）”：组网场景为ModelC和ModelD。  默认值：无  配置原则：无                                                                                                                                                                                                                                                                                                                                                                                                                         |
| N7RESULTCODEVAL | N7返回码                                 | 可选必选说明：必选参数  参数含义：本参数用于配置N7返回码。  数据来源：对端协商  取值范围：字符串类型，输入长度范围是1~3。300-599中的一个值或者3xx、4xx、5xx，不区分大小写。其中xx代表一个范围，例如3xx代表300~399。  默认值：无  配置原则：  配置的单个的返回码落在一个范围内时，单个的优先级高。                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ERRINFO         | 故障码对应的Protocol or application Error信息 | 可选必选说明：必选参数  参数含义：该参数用于指定自定义的故障码对应的Protocol or application Error信息。  数据来源：全网规划  取值范围：字符串类型，输入长度范围是0~128。如果配置为星号（*），表示通配，对该异常码携带所有Protocol or application Error信息都生效。参考3GPP协议29.500的Protocol or application Error。  默认值：无  配置原则：  （1）该参数只能由字母（A-Z或者a-z）、数字（0-9）、下划线（_）、星号（*）组成。该参数不区分大小写。  （2）配置为“*”，表示该异常码动作对于所有的Protocol or application Error信息都生效。                                                                                                                                                                                                                                                                 |
| INITACTION      | Initial流程处理动作                         | 可选必选说明：可选参数  参数含义：该参数用于控制激活响应消息中携带该返回码的行为。  数据来源：本端规划 取值范围： “DEFAULT（缺省动作）”：缺省动作。“FAILOVER（宕机备份）”：宕机备份。“TERMINATE（去活会话）”：去活会话。“LOCALPCC（回滚为本地PCC用户使用本地策略）”：回滚为本地PCC用户使用本地策略。“INHERIT（继承全局动作）”：继承全局动作。  默认值：无  配置原则： 当PCCTEMPLATE配置为“global”且未配置该参数时，默认值为DEFAULT。当PCCTEMPLATE配置为指定PCC模板且未配置该参数时，默认值为INHERIT。当此参数配置为DEFAULT时，则沿用流程默认动作，按照激活失败处理。当PCCTEMPLATE配置为指定PCC模板且配置动作为INHERIT时，则继承“global”PCCTEMPLATE模板的RESULTCODESCP动作，若PCCTEMPLATE配置为“global”的RESULTCODESCP动作未配置时,则沿用对应模板的RESULTCODECTRL动作，若未配置对应模板的RESULTCODECTRL动作，则执行流程缺省动作，按照激活失败处理。                                                                       |
| INITHOLDTMSW    | Initial流程回滚后使能Holding-Time            | 可选必选说明：该参数在"INITACTION"配置为"LOCALPCC"时为条件可选参数。  参数含义：该参数用于设置激活响应控制的行为生效时是否根据holding-time设置时长保活用户，并在holding-time超时后去活用户。  数据来源：本端规划 取值范围： “DISABLE（不使能）”：不使能。“ENABLE（使能）”：使能。  默认值：无  配置原则：无                                                                                                                                                                                                                                                                                                                                                                                                                           |
| UPDATEACTION    | Update流程处理动作                          | 可选必选说明：可选参数  参数含义：该参数用于控制更新响应消息中携带该返回码的行为。  数据来源：本端规划 取值范围： “FAILOVER（宕机备份）”：宕机备份。“TERMINATE（去活会话）”：去活会话。“LOCALPCC（回滚为本地PCC用户使用本地策略）”：回滚为本地PCC用户使用本地策略“INHERIT_PCC（回滚为本地PCC用户继续使用PCRF策略）”：回滚为本地PCC用户继续使用PCRF策略。“CONTINUE（继续N7会话）”：继续N7会话。“INHERIT（继承全局动作）”：继承全局动作。  默认值：无  配置原则： 当PCCTEMPLATE配置为“global”且未配置该参数时，默认值为CONTINUE。当PCCTEMPLATE配置为指定PCC模板且未配置该参数时，默认值为INHERIT。当此参数配置为DEFAULT时，则沿用流程默认动作，按照continue处理。当PCCTEMPLATE配置为指定PCC模板且配置动作为INHERIT时，则继承“global”PCCTEMPLATE模板的RESULTCODESCP动作，若PCCTEMPLATE配置为“global”的RESULTCODESCP动作未配置时,则沿用对应模板的RESULTCODECTRL动作，若未配置对应模板的RESULTCODECTRL动作，则执行流程缺省动作，按照Continue处理。 |
| UPDHOLDTMSW     | Update流程回滚后使能Holding-Time             | 可选必选说明：该参数在"UPDATEACTION"配置为"INHERIT_PCC"、"LOCALPCC"时为条件可选参数。  参数含义：该参数用于设置更新响应控制的行为生效时是否根据holding-time设置时长保活用户，并在holding-time超时后去活用户。  数据来源：本端规划 取值范围： “DISABLE（不使能）”：不使能。“ENABLE（使能）”：使能。  默认值：无  配置原则：无                                                                                                                                                                                                                                                                                                                                                                                                           |
| TERMINACTION    | Terminate流程处理动作                       | 可选必选说明：可选参数  参数含义：该参数用于控制删除响应消息中携带该返回码的行为。  数据来源：本端规划 取值范围： “DEFAULT（缺省动作）”：缺省动作。“FAILOVER（宕机备份）”：宕机备份。“INHERIT（继承全局动作）”：继承全局动作。  默认值：无  配置原则： 当PCCTEMPLATE配置为“global”且未配置该参数时，默认值为DEFAULT。当PCCTEMPLATE配置为指定PCC模板且未配置该参数时，默认值为INHERIT。当此参数配置为DEFAULT时，去活用户。当PCCTEMPLATE配置为指定PCC模板且配置动作为INHERIT时，则继承“global”PCCTEMPLATE模板的RESULTCODESCP动作，若PCCTEMPLATE配置为“global”的RESULTCODESCP动作未配置时,则沿用对应模板的RESULTCODECTRL动作，若未配置对应模板的RESULTCODECTRL动作，则执行流程缺省动作，继续执行去活操作。                                                                                                                                                          |
| REACTREQ        | 重新激活请求                                | 可选必选说明：该参数在"UPDATEACTION"配置为"TERMINATE"时为条件可选参数。  参数含义：该参数用于指示当用户因异常结果码被去活时，UNC是否通知用户重新激活。  数据来源：本端规划 取值范围： “DISABLE（不使能）”：不使能。“ENABLE（使能）”：使能。“DEFAULT（缺省取值）”：缺省取值。  默认值：无  配置原则：  当前版本暂不支持REACTREQ参数配置为DEFAULT，配置为DEFAULT时处理原则与DSIABLE保持一致。                                                                                                                                                                                                                                                                                                                                                                        |

## 使用实例

- 添加全局RESULTCODESCP返回码控制信息，对ModelC组网更新响应消息中“N7RESULTCODEVAL”为“5xx”的消息执行FAILOVER动作：

  ```
  ADD RESULTCODESCP:PCCTEMPLATE="global",MODELTYPE=MODELC,N7RESULTCODEVAL="5xx",ERRINFO="*",INITACTION=DEFAULT,UPDATEACTION=FAILOVER;
  ```
- 为PCC模板“pcctemplate”添加RESULTCODESCP返回码控制信息，对ModelC组网更新响应消息中“N7RESULTCODEVAL”为5xx的消息执行FAILOVER动作：

  ```
  ADD RESULTCODESCP:PCCTEMPLATE="pcctemplate",MODELTYPE=MODELC,N7RESULTCODEVAL="5xx",ERRINFO="*",INITACTION=DEFAULT,UPDATEACTION=FAILOVER;
  ```