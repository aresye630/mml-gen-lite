# 查询AGF的功能参数（LST AGFFUNCPARA）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：NCG**

该命令用于查询AGF的功能参数。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

| 参数标识            | 参数名称               | 参数说明                                                                                                                                                                                                                                                                                                            |
|:----------------|:-------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| OCSRETRYCNT     | 计费消息重发次数           | 可选必选说明：可选参数  参数含义：该参数用于指定NCG等待OCS计费响应超时重发次数。  数据来源：本端规划  取值范围：整数类型，取值范围是0~1。  默认值：无  配置原则：无                                                                                                                                                                                                                     |
| OCSDISCPLCY     | OCS选择策略            | 可选必选说明：可选参数  参数含义：该参数用于指定选择OCS时使用的参数。  数据来源：本端规划 取值范围： “SUPI（SUPI）”：根据SUPI选择OCS“GPSI（GPSI）”：根据GPSI选择OCS“DNN（DNN）”：根据DNN选择OCS  默认值：无  配置原则：  OCS选择策略选项中至少选择一个。                                                                                                                                                   |
| CDFIPKGPLCY     | CDF I包抄送策略         | 可选必选说明：可选参数  参数含义：该参数用于指定CDF I包抄送策略。  数据来源：本端规划  取值范围： TRUE(TRUE)FALSE(FALSE)  默认值：无  配置原则：  FALSE表示不抄送。  TRUE表示抄送。                                                                                                                                                                                             |
| QBCCHGSWITCH    | H-CHF QBC计费开关      | 可选必选说明：可选参数  参数含义：是否开启H-CHF QBC计费模式。  数据来源：本端规划  取值范围： TRUE(TRUE)FALSE(FALSE)  默认值：无  配置原则：无                                                                                                                                                                                                                    |
| VSMFJUDGEMODE   | V-SMF判断模式          | 可选必选说明：可选参数  参数含义：该参数用于指定V-SMF的判断模式。  数据来源：本端规划 取值范围： HUAWEIQBCINDICATION_MODE（根据huaweiQBCIndication判断）NETWORKFUNCTIONALITY_MODE（根据networkFunctionality判断）PLMN_MODE（根据plmn判断）  默认值：无  配置原则：无                                                                                                                    |
| OCSRSPFOFHPLCY  | 是否忽略OCS的Failover策略 | 可选必选说明：可选参数  参数含义：该参数用于指定是否忽略OCS的Failover策略。  数据来源：本端规划  取值范围： TRUE(TRUE)FALSE(FALSE)  默认值：无  配置原则：  FALSE表示向前端网元透传OCS响应中sessionFailover与failureHandling值。  TRUE表示忽略OCS响应中sessionFailover为FAILOVER_NOT_SUPPORTED的值，固定填为FAILOVER_SUPPORTED；忽略OCS响应中failureHandling为TERMINATE或RETRY_AND_TERMINATE的值，固定填为CONTINUE。 |
| SMSFCHGSWITCH   | SMSF计费开关           | 可选必选说明：可选参数  参数含义：该参数用于指定是否开启SMSF计费模式。  数据来源：全网规划  取值范围： TRUE(TRUE)FALSE(FALSE)  默认值：无  配置原则：无                                                                                                                                                                                                                  |
| OPTIMIZEISOLATE | 是否立即为老会话隔离OCS      | 可选必选说明：可选参数  参数含义：该参数用于指定老会话是否立即隔离OCS。  数据来源：本端规划  取值范围： TRUE(TRUE)FALSE(FALSE)  默认值：无  配置原则：无                                                                                                                                                                                                                  |

## 使用实例

查询计费重发次数为1的记录：

```
LST AGFFUNCPARA: OCSRETRYCNT=1;
RETCODE = 0  操作成功

结果如下
--------
   计费消息重发次数  =  1
        OCS选择策略  =  SUPI
    CDF I包抄送策略  =  是
  H-CHF QBC计费开关  =  否
      V-SMF判断模式  =  根据huaweiQBCIndication判断
是否忽略OCS的Failover策略 = 否
SMSF计费开关 = 否
老会话是否立即隔离OCS = 否
(结果个数 = 1)

---    END
```

## 输出结果说明

| 输出项名称              | 输出项解释                      |
|:-------------------|:---------------------------|
| 计费消息重发次数           | 该参数用于指定NCG等待OCS计费响应超时重发次数。 |
| OCS选择策略            | 该参数用于指定选择OCS时使用的参数。        |
| CDF I包抄送策略         | 该参数用于指定CDF I包抄送策略。         |
| H-CHF QBC计费开关      | 是否开启H-CHF QBC计费模式。         |
| V-SMF判断模式          | 该参数用于指定V-SMF的判断模式。         |
| 是否忽略OCS的Failover策略 | 该参数用于指定是否忽略OCS的Failover策略。 |
| SMSF计费开关           | 该参数用于指定是否开启SMSF计费模式。       |
| 是否立即为老会话隔离OCS      | 该参数用于指定老会话是否立即隔离OCS。       |