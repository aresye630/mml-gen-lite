# 设置语音PCF/PCRF故障Bypass场景功能（SET IMSBYPASSFUNC）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：PGW-C、SMF**

该命令用于设置语音PCF/PCRF故障Bypass场景功能。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| ACTNODEDBEARER   | ACTWITDEDBEARER   | FAILLOCPCC   | TSTUPDATEREQSW   | REACTREQ   |
|:-----------------|:------------------|:-------------|:-----------------|:-----------|
| INHERIT          | INHERIT           | LOCAL_PCC    | DISABLE          | DISABLE    |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识            | 参数名称                             | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|:----------------|:---------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ACTNODEDBEARER  | 无语音专载时的故障非预期Bypass场景的异常处理动作      | 可选必选说明：可选参数  参数含义：该参数用来配置无语音专载时的激活或更新流程故障非预期Bypass场景的异常处理动作。  数据来源：本端规划 取值范围： INHERIT（继承）TERMINATE（去活）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST IMSBYPASSFUNC查询当前参数配置值。  配置原则：  该参数仅适用于非预期Bypass场景，包括：1. 更新流程Gx接口不支持Failover场景、2. 直连场景Failover后收到备PCRF/PCF返回异常码场景、3. 非直连场景Failover后收到DRA返回非RESULTCODEDRA配置的异常码场景、4. 非直连场景Failover后收到SCP返回非RESULTCODESCP配置的异常码场景。参数取值为“INHERIT”时，继承原有的PCCTEMPLATE、PCCFAILACTION、RESULTCODECTRL等响应超时或异常码配置动作处理；参数取值为“TERMINATE”时，去活会话。            |
| ACTWITDEDBEARER | 存在语音专载时的更新流程故障非预期Bypass场景的异常处理动作 | 可选必选说明：可选参数  参数含义：该参数用来配置存在语音专载时的更新流程故障非预期Bypass场景的异常处理动作。  数据来源：本端规划 取值范围： INHERIT（继承）FASTROLLBACK（短暂回滚）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST IMSBYPASSFUNC查询当前参数配置值。  配置原则：  该参数仅适用于非预期Bypass场景，包括：1. 更新流程Gx接口不支持Failover场景、2. 直连场景Failover后收到备PCRF/PCF返回异常码场景、3. 非直连场景Failover后收到DRA返回非RESULTCODEDRA配置的异常码场景、4. 非直连场景Failover后收到SCP返回非RESULTCODESCP配置的异常码场景。参数取值为“INHERIT”时，继承原有的PCCTEMPLATE、PCCFAILACTION、RESULTCODECTRL等响应超时或异常码配置动作处理；参数取值为“FASTROLLBACK”时，短暂回滚本地PCC。 |
| FAILLOCPCC      | 存在语音专载时更新流程故障回滚为Local PCC用户类型    | 可选必选说明：该参数在"ACTWITDEDBEARER"配置为"FASTROLLBACK"时为条件可选参数。  参数含义：该参数用于指定存在语音专载时更新流程故障回滚为Local PCC用户类型。  数据来源：全网规划 取值范围： LOCAL_PCC（回滚PCC用户为本地PCC用户）INHERIT_PCC（回滚PCC用户为本地PCC用户并且继续使用PCRF/PCF策略）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST IMSBYPASSFUNC查询当前参数配置值。  配置原则：无                                                                                                                                                                                                             |
| TSTUPDATEREQSW  | 非直连场景下退出Bypass发送探测消息开关           | 可选必选说明：可选参数  参数含义：该参数用于配置非直连场景下退出Bypass时是否需要发送探测消息。  数据来源：本端规划 取值范围： DISABLE（不发送探测消息）ENABLE（发送探测消息）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST IMSBYPASSFUNC查询当前参数配置值。  配置原则：无                                                                                                                                                                                                                                                                                                    |
| REACTREQ        | 重新激活请求                           | 可选必选说明：可选参数  参数含义：该参数用于指示当语音用户因Holdingtime超时去活时，UNC是否通知用户重新激活。  数据来源：本端规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST IMSBYPASSFUNC查询当前参数配置值。  配置原则：  该参数使能时需要同时打开语音用户ADD CPAPN命令的REACWITHDEL参数。                                                                                                                                                                                                                                                      |

## 使用实例

配置无语音专载时的故障非预期Bypass场景的异常处理动作为“去活”：

```
SET IMSBYPASSFUNC: ACTNODEDBEARER=TERMINATE;
```