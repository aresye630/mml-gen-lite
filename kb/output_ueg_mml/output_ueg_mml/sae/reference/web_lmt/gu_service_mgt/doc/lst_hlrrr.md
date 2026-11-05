# 查询用户漫游限制(LST HLRRR)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询HLR中用户的漫游限制状态：

- 若需要查询缺省漫游限制状态，则输入“HLR序列号”，“操作类型”选择“DEFRULE”。
- 若需要查询用户在所有“VLR或SGSN号码前缀”对应端局下的漫游限制状态，则输入“HLR序列号”，“操作类型”选择“ALL”。
- 若需要查询用户在指定的“VLR或SGSN号码前缀”对应的端局下的漫游限制状态，则输入“HLR序列号”，“操作类型”选择“ONE”，并且输入指定的“VLR或SGSN号码前缀”。

## 注意事项

无。

## 参数说明

| 参数标识      | 参数名称         | 参数说明                                                                                                                                  |
|:----------|:-------------|:--------------------------------------------------------------------------------------------------------------------------------------|
| HLRSN     | HLR序列号       | 用于指示系统按照哪个HLR序列号来查询用户的漫游限制状态，该参数必须输入。                                                                                                 |
| OPTYPE    | 操作类型         | 用于指示系统按照哪种操作类型来查询用户的漫游限制状态。 取值范围： DEFRULE：查询缺省漫游限制状态。 ALL：查询用户在所有“VLR或SGSN号码前缀”对应端局下的漫游限制状态。 ONE：查询用户在指定的“VLR或SGSN号码前缀”对应的端局下的漫游限制状态。 |
| VLRSGSNNO | VLR/SGSN号码前缀 | 仅当“操作类型”参数取值为“ONE”时，该参数有效。用于指示系统需要在哪个“VLR或SGSN号码前缀”对应的端局下查询用户漫游限制状态。                                                                  |

## 使用实例

1. 查询缺省漫游限制状态：

   `LST HLRRR: HLRSN=1, OPTYPE=DEFRULE;`

   ```
   %%LST HLRRR: HLRSN=1, OPTYPE=DEFRULE;%%
   RETCODE = 0 SUCCESS0001:Operation is successful

                            HLRSN = 1
                  ROAMDEFAULTRULE = PERMISSION

   Total count = 2

   There is together 1 report

   ---    END
   ```
2. 查询用户在所有“VLR或SGSN号码前缀”对应端局下的漫游限制状态：

   `LST HLRRR: HLRSN=1, OPTYPE=ALL;`

   ```
   %%LST HLRRR: HLRSN=1, OPTYPE=ALL;%%
   RETCODE = 0 SUCCESS0001:Operation is successful

         "VLRSGSNNO"       "ROAMRULE"
         123456789123455   PERMISSION
         12345678912345    PERMISSION

   Total count = 2

   There is together 1 report

   ---    END
   ```
3. 查询“VLR或SGSN号码前缀”为“12345678912345”对应的端局下用户漫游限制状态：

   `LST HLRRR: HLRSN=1, OPTYPE=ONE, VLRSGSNNO="12345678912345";`

   ```
   %%LST HLRRR: HLRSN=1, OPTYPE=ONE, VLRSGSNNO="12345678912345";%%
   RETCODE = 0 SUCCESS0001:Operation is successful

         "VLRSGSNNO"       "ROAMRULE"
         12345678912345    PERMISSION

   Total count = 1

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释   | 原因分析                               | 处理建议                                                                                         |
|:--------|:--------|:-----------------------------------|:---------------------------------------------------------------------------------------------|
| ERR3007 | 记录不存在   | “HLR序列号”未定义或者输入的“VLR/SGSN号码前缀”未配置。 | 根据实际情况，重新输入参数“HLR序列号”，确保输入的“HLR序列号”已定义。 执行本命令查看HLR所配置的“VLR/SGSN号码前缀”，确保输入的“VLR/SGSN号码前缀”已配置。 |