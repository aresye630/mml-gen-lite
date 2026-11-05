# 显示冲突规则生效状态（DSP SMFCONFLICTRULE）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于显示冲突规则生效状态。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

| 参数标识            | 参数名称    | 参数说明                                                                                       |
|:----------------|:--------|:-------------------------------------------------------------------------------------------|
| CSTYPE          | 指定CS类型  | 可选必选说明：必选参数  参数含义：该参数用于指定CS类型。  数据来源：本端规划 取值范围： SMC_SM（会话管理控制cell服务的会话管理模块）  默认值：无  配置原则：无 |
| PROCTYPE        | 流程内部标识  | 可选必选说明：必选参数  参数含义：该参数用于指定流程内部标识。  数据来源：本端规划  取值范围：任意类型，取值范围是1~128。  默认值：无  配置原则：无          |
| NEWINITPROCTYPE | 新流程内部标识 | 可选必选说明：必选参数  参数含义：该参数用于指定新流程内部标识。  数据来源：本端规划  取值范围：任意类型，取值范围是1~128。  默认值：无  配置原则：无         |
| RULE            | 冲突流程规则  | 可选必选说明：可选参数  参数含义：该参数用于指定冲突流程规则。  数据来源：本端规划  取值范围：任意类型，取值范围是0~4096。  默认值：无  配置原则：无         |

## 使用实例

查询该条规则是否生效，规则如下: HsmfN11形态N4DdnReport流程中，收到名为ProcedureTypeAmfIwkEpsIndChangeAsHsmfN11的流程首消息，执行丢弃策略生效：

```
%%DSP SMFCONFLICTRULE: CSTYPE=SMC_SM, PROCTYPE="ProcedureTypeN4DdnReportAsHsmfN11", NEWINITPROCTYPE="ProcedureTypeAmfIwkEpsIndChangeAsHsmfN11", RULE="{\"Name\":\"When\",\"Children\":[{\"Name\":\"Not\",\"Children\":[{\"Name\":\"TransLabelContainImpl\",\"LabelCheck\":\"LabelNotifyRmvSess\"}]},{\"Name\":\"DiscardImpl\",\"AnyWay\":\"false\",\"NeedRespond\":\"false\",\"RespondCause\":\"SmcCauseConflictBegin\"}]}";%%
RETCODE = 0  操作成功

结果如下
--------
冲突流程生效规则  =  Enable
(结果个数 = 1)

---    END
```

## 输出结果说明

| 输出项名称    | 输出项解释              |
|:---------|:-------------------|
| 冲突流程生效规则 | 该参数用于显示冲突流程生效规则结果。 |