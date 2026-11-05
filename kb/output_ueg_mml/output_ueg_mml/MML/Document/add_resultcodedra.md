# 增加DRA返回码控制（ADD RESULTCODEDRA）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：PGW-C、GGSN**

此命令用来配置当UNC收到DRA回复的指定结果码信息后执行何种操作。例如关闭PCC功能、执行缺省动作、执行宕机备份等。

## 注意事项

- 该命令执行后立即生效。

- DRA返回异常码场景，该配置命令优先级高于ADD RESULTCODECTRL。
- 当PCCTEMPLATE配置为“global”时，表示全局配置，最多能配置100条记录；当PCCTEMPLATE配置为指定PCC模板时，表示该PCC模板下的配置，最多能配置10条记录。

- 最多可输入1100条记录。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识          | 参数名称                       | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|:--------------|:---------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PCCTEMPLATE   | PCC模板名称                    | 可选必选说明：必选参数  参数含义：该参数用于设置该返回码所绑定的PCC模板。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是1~63。  默认值：无  配置原则：  如果配置为“global”则表示全局配置。  如果配置为非“global”，则必须是已经通过ADD PCCTEMPLATE配置过的PCC模板名称。                                                                                                                                                                                                                                                                                                                 |
| VENDORID      | 设备提供商标识                    | 可选必选说明：必选参数  参数含义：设备提供商标识。  数据来源：全网规划  取值范围：整数类型，取值范围是0~65535。  默认值：无  配置原则：无                                                                                                                                                                                                                                                                                                                                                                                                        |
| RESULTCODEVAL | 返回码                        | 可选必选说明：必选参数  参数含义：返回码。  数据来源：对端协商  取值范围：字符串类型，输入长度范围是1~4。1000-9999，1xxx-9xxx，不区分大小写。其中xxxx代表一个范围，例如1xxx代表1000~1999。配置的单个的返回码落在一个范围内时，单个的优先级高。  默认值：无  配置原则：无                                                                                                                                                                                                                                                                                                                         |
| INITACTION    | Initial流程处理动作              | 可选必选说明：可选参数  参数含义：控制创建响应消息中携带该返回码的行为。  数据来源：本端规划 取值范围： “DEFAULT（缺省动作）”：缺省动作。“FAILOVER（宕机备份）”：宕机备份。“TERMINATE（去活会话）”：去活会话。“LOCALPCC（回滚为本地PCC用户使用本地策略）”：回滚为本地PCC用户使用本地策略。“INHERIT（继承全局动作）”：继承全局动作。  默认值：无  配置原则：  当PCCTEMPLATE配置为“global”时，默认值为DEFAULT。当PCCTEMPLATE配置为指定PCC模板时，默认值为INHERIT。  当此参数配置为DEFAULT时，UNC在收到PCRF的消息（携带的VENDORID和RESULTCODEVAL分别为前面指定的值）后，将执行缺省此参数，即按接收到的RESULTCODEVAL做具体处理，例如激活时收到此RESULTCODEVAL激活失败、更新时收到此RESULTCODEVAL去活承载等，详细此参数可参考SET PCCFAILACTION命令的使用指南。 |
| INITHOLDTMSW  | Initial流程回滚后使能Holding-Time | 可选必选说明：该参数在"INITACTION"配置为"LOCALPCC"时为条件可选参数。  参数含义：该参数用于设置创建响应控制的行为生效时是否根据holding-time设置时长保活用户，并在holding-time超时后去活用户。  数据来源：本端规划 取值范围： “DISABLE（不使能）”：不使能。“ENABLE（使能）”：使能。  默认值：DISABLE  配置原则：无                                                                                                                                                                                                                                                                                     |
| UPDATEACTION  | Update流程处理动作               | 可选必选说明：可选参数  参数含义：控制更新响应消息中携带该返回码的行为。  数据来源：本端规划 取值范围： “FAILOVER（宕机备份）”：宕机备份。“TERMINATE（去活会话）”：去活会话。“LOCALPCC（回滚为本地PCC用户使用本地策略）”：回滚为本地PCC用户使用本地策略“INHERIT_PCC（回滚为本地PCC用户继续使用PCRF策略）”：回滚为本地PCC用户继续使用PCRF策略。“CONTINUE（继续Gx会话）”：继续Gx会话。“INHERIT（继承全局动作）”：继承全局动作。  默认值：无  配置原则：  当PCCTEMPLATE配置为“global”时，默认值为CONTINUE。当PCCTEMPLATE配置为指定PCC模板时，默认值为INHERIT。                                                                                                                              |
| UPDHOLDTMSW   | Update流程回滚后使能Holding-Time  | 可选必选说明：该参数在"UPDATEACTION"配置为"INHERIT_PCC"、"LOCALPCC"时为条件可选参数。  参数含义：该参数用于设置更新响应控制的行为生效时是否根据holding-time设置时长保活用户，并在holding-time超时后去活用户。  数据来源：本端规划 取值范围： “DISABLE（不使能）”：不使能。“ENABLE（使能）”：使能。  默认值：DISABLE  配置原则：无                                                                                                                                                                                                                                                                     |
| TERMINACTION  | Terminate流程处理动作            | 可选必选说明：可选参数  参数含义：控制删除响应消息中携带该返回码的行为。  数据来源：本端规划 取值范围： “DEFAULT（缺省动作）”：缺省动作。“FAILOVER（宕机备份）”：宕机备份。“INHERIT（继承全局动作）”：继承全局动作。  默认值：无  配置原则：  当PCCTEMPLATE配置为“global”时，默认值为DEFAULT。当PCCTEMPLATE配置为指定PCC模板时，默认值为INHERIT。  当此参数配置为DEFAULT时，去活用户。                                                                                                                                                                                                                                          |
| REACTREQ      | 重新激活请求                     | 可选必选说明：该参数在"UPDATEACTION"配置为"TERMINATE"时为条件可选参数。  参数含义：该参数用于指示当用户因异常结果码被去活时，UNC是否通知用户重新激活。  数据来源：本端规划 取值范围： “DISABLE（不使能）”：不使能。“ENABLE（使能）”：使能。“DEFAULT（缺省取值）”：缺省取值，对5002结果码其作用等同于ENABLE，对非5002结果码其作用等同于DISABLE。  默认值：DEFAULT  配置原则：  该参数配置为ENABLE，或配置为DEFAULT且结果码为5002，仅在ADD/MOD CPAPN命令的REACWITHDEL参数配置打开时，发给左侧的去活消息才会携带重新激活标识。                                                                                                                                                    |

## 使用实例

- 添加全局RESULTCODEDRA返回码控制信息，对更新响应消息中“VENDORID”为0，“RESULTCODEVAL”为“5xxx”的消息执行FAILOVER动作：

  ```
  ADD RESULTCODEDRA:PCCTEMPLATE="global",VENDORID=0,RESULTCODEVAL="5xxx",INITACTION=DEFAULT,UPDATEACTION=FAILOVER;
  ```
- 为PCC模板“pcctemplate”添加RESULTCODEDRA返回码控制信息，对创建响应消息中“VENDORID”为10415，“RESULTCODEVAL”为“5140”的消息执行LOCALPCC动作：

  ```
  ADD RESULTCODEDRA:PCCTEMPLATE="pcctemplate",VENDORID=10415,RESULTCODEVAL="5140",INITACTION=LOCALPCC,UPDATEACTION=LOCALPCC;
  ```