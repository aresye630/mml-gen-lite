# 修改返回码控制（MOD RESULTCODECTRL）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用NF：PGW-C、SMF**

此命令用来修改当UNC收到指定结果码信息后执行何种操作。例如关闭动态PCC功能、执行缺省动作、执行宕机备份等。

#### 注意事项

- 该命令执行后立即生效。
- Gx接口时，不支持此命令的REACTREQ、DIRECTREACTREQ参数功能。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识            | 参数名称                           | 参数说明                                                                                                                                                                                                                                                                                                                           |
|:----------------|:-------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PCCTEMPLATE     | PCC模板名称                        | 可选必选说明：必选参数 参数含义：该参数用于设置该返回码所绑定的PCC模板。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。 默认值：无 配置原则：无                                                                                                                                                                                                                                          |
| INTFTYPE        | 接口类型                           | 可选必选说明：必选参数 参数含义：接口类型。 数据来源：对端协商 取值范围：枚举类型。 INTFTYPE_N7：N7接口类型。INTFTYPE_GX：Gx接口类型。 默认值：无 配置原则：无                                                                                                                                                                                                                                |
| N7RESULTCODEVAL | N7返回码                          | 可选必选说明：条件必选参数 前提条件：该参数在“INTFTYPE”配置为“INTFTYPE_N7”时为必选参数。 参数含义：N7返回码。 数据来源：对端协商 取值范围：字符串类型，输入长度范围为1～3。300-599或者3xx-5xx，不区分大小写。其中xx代表一个范围，例如3xx代表300~399。 默认值：无 配置原则： 超时返回码504不受该配置控制，而是执行一次failover操作，若failover失败则根据APN/DNN绑定的PCCTEMPLATE或全局用户PCCFAILACTION相关配置获取失败动作。其中，APN/DNN绑定的PCCTEMPLATE配置优先级高。配置的单个的返回码落在一个范围内时，单个的优先级高。 |
| VENDORID        | 设备提供商标识                        | 可选必选说明：条件必选参数 前提条件：该参数在“INTFTYPE”配置为“INTFTYPE_GX”时为必选参数。 参数含义：设备提供商标识。 数据来源：全网规划 取值范围：整数类型，取值范围为0～65535。 默认值：无 配置原则：无                                                                                                                                                                                                          |
| GXRESULTCODEVAL | Gx返回码                          | 可选必选说明：条件必选参数 前提条件：该参数在“INTFTYPE”配置为“INTFTYPE_GX”时为必选参数。 参数含义：返回码。 数据来源：对端协商 取值范围：字符串类型，输入长度范围为1～4。1000-9999，1xxx-9xxx，不区分大小写。其中xxxx代表一个范围，例如1xxx代表1000~1999。配置的单个的返回码落在一个范围内时，单个的优先级高。 默认值：无 配置原则：无                                                                                                                           |
| INITACTION      | Initial流程处理动作                  | 可选必选说明：可选参数 参数含义：控制创建响应消息中携带该返回码的行为。 数据来源：本端规划 取值范围：枚举类型。 DEFAULT：缺省动作。FAILOVER：宕机备份。TERMINATE：去活会话。LOCALPCC：回滚为本地PCC用户使用本地策略。INHERIT：继承全局动作。 默认值：无 配置原则：无                                                                                                                                                                     |
| INITHOLDTMSW    | Initial流程回滚后使能Holding-Time     | 可选必选说明：条件可选参数 前提条件：该参数在“INITACTION”配置为“LOCALPCC”时为可选参数。 参数含义：该参数用于设置创建响应控制的行为生效时是否根据holding-time设置时长保活用户，并在holding-time超时后去活用户。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不使能。ENABLE：使能。 默认值：无 配置原则：无                                                                                                                                       |
| UPDATEACTION    | Update流程处理动作                   | 可选必选说明：可选参数 参数含义：控制更新响应消息中携带该返回码的行为。 数据来源：本端规划 取值范围：枚举类型。 FAILOVER：宕机备份。TERMINATE：去活会话。LOCALPCC：回滚为本地PCC用户使用本地策略。INHERIT_PCC：回滚为本地PCC用户继续使用PCRF/PCF策略。CONTINUE：继续Gx/PCF会话。INHERIT：继承全局动作。 默认值：无 配置原则：无                                                                                                                         |
| UPDHOLDTMSW     | Update流程回滚后使能Holding-Time      | 可选必选说明：条件可选参数 前提条件：该参数在“UPDATEACTION”配置为“LOCALPCC” 或 “INHERIT_PCC”时为可选参数。 参数含义：该参数用于设置更新响应控制的行为生效时是否根据holding-time设置时长保活用户，并在holding-time超时后去活用户。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不使能。ENABLE：使能。 默认值：无 配置原则：无                                                                                                                     |
| TERMINACTION    | Terminate流程处理动作                | 可选必选说明：可选参数 参数含义：控制删除响应消息中携带该返回码的行为。 数据来源：本端规划 取值范围：枚举类型。 DEFAULT：缺省动作。FAILOVER：宕机备份。INHERIT：继承全局动作。 默认值：无 配置原则：无                                                                                                                                                                                                              |
| DIRECTINITACT   | 直连对端Initial流程处理动作              | 可选必选说明：可选参数 参数含义：控制直连对端创建响应消息中携带该返回码的行为。 数据来源：本端规划 取值范围：枚举类型。 DEFAULT：缺省动作，激活失败。FAILOVER：宕机备份。TERMINATE：去活会话。LOCALPCC：回滚为本地PCC用户使用本地策略。FAILOVERALL：全部用户执行宕机备份动作。INVALID：执行参数INITACTION配置的动作。 默认值：无 配置原则：当此参数配置为INVALID时，在查询返回码控制时显示为NULL。                                                                                      |
| DIRECTUPDACT    | 直连对端Update流程处理动作               | 可选必选说明：可选参数 参数含义：控制直连对端更新响应消息中携带该返回码的行为。 数据来源：本端规划 取值范围：枚举类型。 FAILOVER：宕机备份。TERMINATE：去活会话。LOCALPCC：回滚为本地PCC用户使用本地策略。INHERIT_PCC：回滚为本地PCC用户继续使用Gx/PCF策略。CONTINUE：继续Gx/PCF会话。FAILOVERALL：全部用户执行宕机备份动作。INVALID：执行参数UPDATEACTION配置的动作。 默认值：无 配置原则：当此参数配置为INVALID时，在查询返回码控制时显示为NULL。                                               |
| DIRECTTERMINACT | 直连对端Terminate流程处理动作            | 可选必选说明：可选参数 参数含义：控制直连对端删除响应消息中携带该返回码的行为。 数据来源：本端规划 取值范围：枚举类型。 DEFAULT：缺省动作，去活。FAILOVER：宕机备份。FAILOVERALL：全部用户执行宕机备份动作。INVALID：执行参数TERMINACTION配置的动作。 默认值：无 配置原则：当此参数配置为INVALID时，在查询返回码控制时显示为NULL。                                                                                                                               |
| DIRECTINITHTSW  | 直连对端Initial流程回滚后使能Holding-Time | 可选必选说明：条件可选参数 前提条件：该参数在“DIRECTINITACT”配置为“LOCALPCC”时为可选参数。 参数含义：该参数用于设置直连对端创建响应控制的行为生效时是否根据holding-time设置时长保活用户，并在holding-time超时后去活用户。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不使能。ENABLE：使能。 默认值：无 配置原则：无                                                                                                                                |
| DIRECTUPDHTSW   | 直连对端Update流程回滚后使能Holding-Time  | 可选必选说明：条件可选参数 前提条件：该参数在“DIRECTUPDACT”配置为“INHERIT_PCC” 或 “LOCALPCC”时为可选参数。 参数含义：该参数用于设置直连对端更新响应控制的行为生效时是否根据holding-time设置时长保活用户，并在holding-time超时后去活用户。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不使能。ENABLE：使能。 默认值：无 配置原则：无                                                                                                                 |
| REACTREQ        | 重新激活请求                         | 可选必选说明：条件可选参数 前提条件：该参数在“UPDATEACTION”配置为“TERMINATE”时为可选参数。 参数含义：该参数用于指示当用户因异常结果码被去活时，UNC是否通知用户重新激活。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不使能。ENABLE：使能。DEFAULT：缺省取值，对5002结果码其作用等同于ENABLE，对非5002结果码其作用等同于DISABLE。 默认值：无 配置原则：该参数配置为ENABLE，或配置为DEFAULT且结果码为5002，仅在ADD/MOD APN命令的REACWITHDEL参数配置打开时，发给左侧的去活消息才会携带重新激活标识。                  |
| DIRECTREACTREQ  | 直连对端重激活请求                      | 可选必选说明：条件可选参数 前提条件：该参数在“DIRECTUPDACT”配置为“TERMINATE”时为可选参数。 参数含义：该参数用于指示当用户因直连对端的异常结果码被去活时，UNC是否通知用户重新激活。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不使能。ENABLE：使能。DEFAULT：缺省取值，对5002结果码其作用等同于ENABLE，对非5002结果码其作用等同于DISABLE。 默认值：无 配置原则：无                                                                                                     |

#### 使用实例

修改PCC模板“pcctemplate”的RESULTCODECTRL返回码控制信息，对更新响应消息中“VENDORID”为10415，“RESULTCODEVAL”为“5140”的消息执行FAILOVER动作：

```
MOD RESULTCODECTRL:PCCTEMPLATE="pcctemplate",INTFTYPE=INTFTYPE_GX,VENDORID=10415,GXRESULTCODEVAL="5140",UPDATEACTION=FAILOVER;
```