# 查询冲突规则（LST SMFCONFLICTRULE）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于查询冲突规则。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

| 参数标识            | 参数名称    | 参数说明                                                                                        |
|:----------------|:--------|:--------------------------------------------------------------------------------------------|
| CSTYPE          | 指定CS类型  | 可选必选说明：可选参数  参数含义：该参数用于指定CS的类型。  数据来源：本端规划 取值范围： SMC_SM（会话管理控制cell服务的会话管理模块）  默认值：无  配置原则：无 |
| PROCTYPE        | 流程内部标识  | 可选必选说明：可选参数  参数含义：该参数用于指定流程内部标识。  数据来源：本端规划  取值范围：任意类型，取值范围是1~128。  默认值：无  配置原则：无           |
| NEWINITPROCTYPE | 新流程内部标识 | 可选必选说明：可选参数  参数含义：该参数用于指定新流程内部标识。  数据来源：本端规划  取值范围：任意类型，取值范围是1~128。  默认值：无  配置原则：无          |
| RULE            | 冲突流程规则  | 可选必选说明：可选参数  参数含义：该参数用于指定冲突流程规则。  数据来源：本端规划  取值范围：任意类型，取值范围是0~4096。  默认值：无  配置原则：无          |

## 使用实例

查询指定场景的冲突流程，PROCTYPE=ProcedureTypeN4DdnReportAsHsmfN11和NEWINITPROCTYPE=ProcedureTypeAmfIwkEpsIndChangeAsHsmfN11的冲突规则：

```
%%LST SMFCONFLICTRULE: CSTYPE=SMC_SM, PROCTYPE="ProcedureTypeN4DdnReportAsHsmfN11", NEWINITPROCTYPE="ProcedureTypeAmfIwkEpsIndChangeAsHsmfN11";%%
RETCODE = 0  操作成功

结果如下
--------
    指定CS类型  =  SMC_SM
  流程内部标识  =  "ProcedureTypeN4DdnReportAsHsmfN11"
新流程内部标识  =  "InitialMsgTypeUpdateSmContextReq"
  冲突流程规则  =  {"Name":"When","Children":[{"Name":"Not","Children":[{"Name":"TransLabelContainImpl","LabelCheck":"LabelNotifyRmvSess"}]},{"Name":"DiscardImpl","AnyWay":"false","NeedRespond":"false","RespondCause":"SmcCauseConflictBegin"}]}
(结果个数 = 1)

---    END
```

## 输出结果说明

| 输出项名称   | 输出项解释           |
|:--------|:----------------|
| 指定CS类型  | 该参数用于指定CS的类型。   |
| 流程内部标识  | 该参数用于指定流程内部标识。  |
| 新流程内部标识 | 该参数用于指定新流程内部标识。 |
| 冲突流程规则  | 该参数用于指定冲突流程规则。  |