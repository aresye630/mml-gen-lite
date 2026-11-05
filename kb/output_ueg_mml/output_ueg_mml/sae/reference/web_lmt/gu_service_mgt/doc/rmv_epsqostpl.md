# 删除EPS QoS模板(RMV EPSQOSTPL)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于删除EPS QoS模板数据记录。

## 注意事项

如果该模板已经通过其他命令关联，例如**ADD EPSAPNQOSTPL**/**MOD EPSAPNQOSTPL**、**ADD PSAPNQOSTPL**/**MOD PSAPNQOSTPL**、**ADD OPTGPRSTPL**/**MOD OPTGPRSTPL**、**ADD RSITPL**/**MOD RSITPL**或**MOD OPTGPRS**命令，当执行该命令删除EPS QoS模板时，系统会提示“ERR3005:模板已经被使用”的错误信息，该EPS QoS模板不能被删除。如果要删除该EPS QoS模板，必须先执行关联命令的修改命令，例如**MOD EPSAPNQOSTPL**、**MOD PSAPNQOSTPL**、**MOD OPTGPRSTPL**、**MOD RSITPL**或**MOD OPTGPRS**，去掉对应模板（例如EPS模板、PS模板）与EPS QoS模板的关联关系。

## 参数说明

| 参数标识   | 参数名称    | 参数说明                                                                        |
|:-------|:--------|:----------------------------------------------------------------------------|
| HLRSN  | HLR序列号  | 标识EPS QoS模板数据记录的关键字段之一，用于指定在哪个HLR上删除EPS QoS模板的数据记录，操作员可以使用LST HLRSN命令查询获得。  |
| TPLID  | QoS模板ID | 标识EPS QoS模板数据记录的关键字段之一，用于指定需要删除哪条EPS QoS模板的数据记录，操作员可以使用LST EPSQOSTPL命令查询获得。 |

## 使用实例

删除“HLR序列号”为1，“QoS模板ID”为10的EPS QoS模板。命令如下：

```
RMV EPSQOSTPL: HLRSN=1, TPLID=10;
```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释   | 原因分析                                                                                                                                                              | 处理建议                                                                                                                                                                             |
|:--------|:--------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ERR3003 | 模板未定义   | “HLR序列号”未定义或者“模板ID”未定义。                                                                                                                                           | 根据实际情况，重新输入已定义的“HLR序列号”和“模板ID”，可通过LST HLRSN命令查询已定义的“HLR序列号”，通过LST EPSQOSTPL命令查询已定义的“模板ID”。                                                                                       |
| ERR3005 | 模板已经被使用 | 待删除的EPS QoS模板已经通过执行其他命令被使用，例如ADD EPSAPNQOSTPL/MOD EPSAPNQOSTPL、ADD PSAPNQOSTPL/MOD PSAPNQOSTPL、ADD OPTGPRSTPL/MOD OPTGPRSTPL、ADD RSITPL/MOD RSITPL或MOD OPTGPRS命令。 | 根据实际情况，确定是否要删除该模板。如果确实需要删除，需要执行以下步骤： 执行关联命令的修改命令，例如MOD EPSAPNQOSTPL、MOD PSAPNQOSTPL、MOD OPTGPRSTPL、MOD RSITPL或MOD OPTGPRS，去掉对应模板（例如EPS模板、PS模板）与EPS QoS模板的关联关系。执行该命令删除该EPS QoS模板。 |