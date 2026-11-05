# 查询NG接入CHR流程控制模板（LST NGACCCHRPRCTMPL）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：AMF**

该命令用于查询NG接入CHR流程控制模板。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

| 参数标识    | 参数名称     | 参数说明                                                                                                                      |
|:--------|:---------|:--------------------------------------------------------------------------------------------------------------------------|
| TMPLIDX | 流程控制模板索引 | 可选必选说明：可选参数  参数含义：流程控制模板索引。  数据来源：本端规划  取值范围：整数类型，取值范围是0~127。  默认值：无  配置原则：  该参数值非0和1，需要使用SET NGACCCHRCFG命令设置NG接入CHR上报策略。 |

## 使用实例

- 查询系统配置“流程控制模板索引”为“0”的NG接入CHR流程控制模板，执行如下命令：

  ```
  %%LST NGACCCHRPRCTMPL: TMPLIDX=0;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
            流程控制模板索引  =  0
   NG接入CHR成功流程上报选项  =  NULL
   NG接入CHR失败流程上报选项  =  OTHER(Other Procedure)&Initial Registration&Mobility Registration&Deregistration&Inter System Change&Service Request&Paging&AN Release&N2 Handover&Xn Handover&Pdu Session Establishment&Pdu Session Modification&Pdu Session Release&Ue Configuration Update&LOCATIONREPORT&RESERVED2&RESERVED3&RESERVED4&RESERVED5&RESERVED6
  NG接入成功信令事件上报选项  =  NULL
  NG接入失败信令事件上报选项  =  NULL
  (结果个数 = 1)

  ---    END
  ```
- 查询系统配置的所有NG接入CHR流程控制模板，执行如下命令：

  ```
  %%LST NGACCCHRPRCTMPL:;%%
  RETCODE = 0  操作成功

  结果如下
  ------------------------
  流程控制模板索引                  NG接入CHR成功流程上报选项                            NG接入CHR失败流程上报选项                                                                                                                                                                                                                                                                                                                                                                              NG接入成功信令事件上报选项                             NG接入失败信令事件上报选项

  0                                 NULL                                                 OTHER(Other Procedure)&Initial Registration&Mobility Registration&Deregistration&Inter System Change&Service Request&Paging&AN Release&N2 Handover&Xn Handover&Pdu Session Establishment&Pdu Session Modification&Pdu Session Release&Ue Configuration Update&LOCATIONREPORT&RESERVED2&RESERVED3&RESERVED4&RESERVED5&RESERVED6  NULL                                                   NULL
  1                                 NULL                                                 OTHER(Other Procedure)&Initial Registration&Mobility Registration&Deregistration&Inter System Change&Service Request&Paging&AN Release&N2 Handover&Xn Handover&Pdu Session Establishment&Pdu Session Modification&Pdu Session Release&Ue Configuration Update&LOCATIONREPORT&RESERVED2&RESERVED3&RESERVED4&RESERVED5&RESERVED6  NULL                                                   NULL
  (结果个数 = 2)

  ---    END
  ```

## 输出结果说明

| 输出项名称           | 输出项解释            |
|:----------------|:-----------------|
| 流程控制模板索引        | 流程控制模板索引。        |
| NG接入CHR成功流程上报选项 | NG接入CHR成功流程上报选项。 |
| NG接入CHR失败流程上报选项 | NG接入CHR失败流程上报选项。 |
| NG接入成功信令事件上报选项  | NG接入成功信令事件上报选项。  |
| NG接入失败信令事件上报选项  | NG接入失败信令事件上报选项。  |