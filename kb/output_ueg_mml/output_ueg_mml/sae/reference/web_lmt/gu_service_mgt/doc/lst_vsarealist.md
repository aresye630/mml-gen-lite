# 查询VLR/SGSN漫游区域模板(LST VSAREALIST)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询VLR/SGSN漫游区域数据。

- 若需要查询全部的VLR/SGSN漫游区域数据，请输入“HLR序列号”参数，其他参数不输入。
- 若需要查询某一模板ID中所有模板类型的VLR/SGSN漫游区域数据，请同时输入“HLR序列号”和“模板ID”参数，其他参数不输入。
- 若需要查询某条VLR/SGSN漫游区域数据，请同时输入“HLR序列号”、“模板ID”和“模板类型”参数。

## 注意事项

当输入参数“模板类型”时，必须同时输入参数“模板ID”。

## 参数说明

| 参数标识    | 参数名称   | 参数说明                                                         |
|:--------|:-------|:-------------------------------------------------------------|
| HLRSN   | HLR序列号 | 用于指示系统按照哪个HLR序列号来查询VLR/SGSN漫游区域模板数据。                         |
| TPLID   | 模板ID   | 用于标识系统需要按照哪个模板ID来查询VLR/SGSN漫游区域模板数据；若不输入，则表示所有的模板ID。         |
| TPLTYPE | 模板类型   | 用于指示系统按照哪个模板类型来查询VLR/SGSN漫游区域模板数据；若不输入，则表示查询所有的VLR/SGSN类型数据。 |

## 使用实例

1. 查询“HLR序列号”为“1”的VLR/SGSN漫游区域模板数据记录：

   ```
   LST VSAREALIST: HLRSN=1;
   ```

   ```
   %%LST VSAREALIST: HLRSN=1;%%
   RETCODE = 0 SUCCESS0001:操作成功

   "VLR"
                  TPLID        TPLNAME
                  1            VSST

   "SGSN"
                  TPLID        TPLNAME
                  2            SNST

   Total count = 2

   There is together 1 report

   ---    END
   ```
2. 查询“HLR序列号”为“1”，“模板ID”为“1”的所有模板类型的VLR/SGSN漫游区域模板数据记录：

   ```
   LST VSAREALIST: HLRSN=1, TPLID=1;
   ```

   ```
   %%LST VSAREALIST: HLRSN=1, TPLID=1;%%
   RETCODE = 0 SUCCESS0001:操作成功

   "VLR"
                  TPLID        TPLNAME
                  1            VSST

   "SGSN"
                  TPLID        TPLNAME

   Total count = 1

   There is together 1 report

   ---    END
   ```
3. 查询“HLR序列号”为“1”，“模板ID”为“1”，“模板类型”为“VLR”的VLR/SGSN漫游区域模板数据记录：

   ```
   LST VSAREALIST: HLRSN=1, TPLID=1, TPLTYPE=VLR;
   ```

   ```
   %%LST VSAREALIST: HLRSN=1, TPLID=1, TPLTYPE=VLR;%%
   RETCODE = 0 SUCCESS0001:操作成功

                            HLRSN = 1
                            TPLID = 1
                          TPLNAME = VSST
                          TPLTYPE = VLR
                        VLRSGSNNO = 222

   Total count = 5

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数请参见**ADD VSAREALIST**命令的参数说明。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释   | 原因分析                                                              | 处理建议                                                                                                         |
|:--------|:--------|:------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------|
| ERR1009 | 参数丢失    | 当输入参数“模板类型”时，没有输入参数“模板ID”。                                        | 根据实际情况，重新输入参数，确保满足在输入参数“模板类型”时，必须同时输入参数“模板ID”的条件。                                                            |
| ERR3003 | 模板未定义   | 可能原因为如下之一：“HLR序列号”或者“模板ID”未定义。 “模板ID”和“模板类型”的匹配关系和数据库中实际存在的模板不一致。 | 根据实际情况，重新输入已定义的“HLR序列号”和“模板ID”，可通过LST HLRSN命令查询已定义的“HLR序列号”，通过LST VSAREALIST命令查询已定义的“模板ID”和“模板类型”在数据库中的匹配关系。 |