# 查询VLR/SGSN漫游限制模板(LST VSLIST)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询VLR/SGSN漫游限制数据。

- 若需要查询全部的VLR/SGSN漫游限制数据，请输入“HLR序列号”参数，其他参数不输入。
- 若需要查询某条VLR/SGSN漫游限制数据，请同时输入“HLR序列号”、“模板ID”和“模板类型”参数。
- 若需要查询某种漫游区域配置方式的VLR/SGSN漫游限制数据，请同时输入“HLR序列号”、“模板ID”、“模板类型”和“漫游区域配置方式”参数。

## 注意事项

当输入参数“漫游区域配置方式”时，参数“模板ID”和“模板类型”必须输入。

## 参数说明

| 参数标识       | 参数名称     | 参数说明                                                           |
|:-----------|:---------|:---------------------------------------------------------------|
| HLRSN      | HLR序列号   | 用于指示系统按照哪个HLR序列号来查询VLR/SGSN漫游限制模板数据。                           |
| TPLID      | 模板ID     | 用于标识系统需要按照哪个模板ID来查询VLR/SGSN漫游限制模板数据；若不输入，则表示所有的模板ID。           |
| TPLTYPE    | 模板类型     | 用于指示系统按照哪个模板类型来查询VLR/SGSN漫游限制模板数据；若不输入，则表示查询所有的VLR/SGSN类型数据。   |
| VSAREATYPE | 漫游区域配置方式 | 用于指示系统按照哪个漫游区域配置方式来查询VLR/SGSN漫游限制模板数据；若不输入，则表示查询所有的漫游区域配置方式数据。 |

## 使用实例

1. 查询“HLR序列号”为“128”的HLR上的VLR/SGSN漫游限制模板数据记录：

   ```
   LST VSLIST: HLRSN=128;
   ```

   ```
   %%LST VSLIST: HLRSN=128;%%
   RETCODE = 0 SUCCESS0001:操作成功

   "VLR"
                  TPLID        TPLNAME
                  1            TEST

   "SGSN"
                  TPLID        TPLNAME
                  2            TEST2
                  251          VSLIST-SGSN

   Total count = 3

   There is together 1 report

   ---    END
   ```
2. 查询“HLR序列号”为“128”的HLR上的VLR/SGSN漫游限制模板数据记录。其中，“模板ID”为“1”，“模板类型”为“VLR”：

   ```
   LST VSLIST: HLRSN=128, TPLID=1, TPLTYPE=VLR;
   ```

   ```
   %%LST VSLIST: HLRSN=128, TPLID=1, TPLTYPE=VLR;%%
   RETCODE = 0 SUCCESS0001:操作成功

                            HLRSN = 128
                            TPLID = 1
                          TPLNAME = TEST
                          TPLTYPE = VLR
                  ROAMDEFAULTRULE = PERMISSION
                        VLRSGSNNO = 029
                         ROAMRULE = PERMISSION
                         SUPERARD = FALSE
                  GERANNOTALLOWED = FALSE
                  UTRANNOTALLOWED = FALSE

                      VSAREATPLID = 3
                         ROAMRULE = PERMISSION
                         SUPERARD = FALSE
                  GERANNOTALLOWED = FALSE
                  UTRANNOTALLOWED = FALSE

   Total count = 15

   There is together 1 report

   ---    END
   ```
3. 查询“HLR序列号”为“128”的HLR上的VLR/SGSN漫游限制模板数据记录。其中，“模板ID”为“1”，“模板类型”为“VLR”，“漫游区域配置方式”为“VSAREA\_TPL\_TYPE”：

   ```
   LST VSLIST: HLRSN=128, TPLID=1, TPLTYPE=VLR, VSAREATYPE=VSAREA_TPL_TYPE;
   ```

   ```
   %%LST VSLIST: HLRSN=128, TPLID=1, TPLTYPE=VLR, VSAREATYPE=VSAREA_TPL_TYPE;%%
   RETCODE = 0 SUCCESS0001:Operation is successful

                            HLRSN = 128
                            TPLID = 1
                          TPLNAME = TEST
                          TPLTYPE = VLR
                  ROAMDEFAULTRULE = PERMISSION
                      VSAREATPLID = 3
                         ROAMRULE = PERMISSION
                         SUPERARD = FALSE
                  GERANNOTALLOWED = FALSE
                  UTRANNOTALLOWED = FALSE

   Total count = 10

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数请参见**ADD VSLIST**命令的参数说明。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释   | 原因分析                                                              | 处理建议                                                                                                     |
|:--------|:--------|:------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------|
| ERR3003 | 模板未定义   | 可能原因为如下之一：“HLR序列号”或者“模板ID”未定义。 “模板ID”和“模板类型”的匹配关系和数据库中实际存在的模板不一致。 | 根据实际情况，重新输入已定义的“HLR序列号”和“模板ID”，可通过LST HLRSN命令查询已定义的“HLR序列号”，通过LST VSLIST命令查询已定义的“模板ID”和“模板类型”在数据库中的匹配关系。 |
| ERR1009 | 参数丢失    | 当输入参数“漫游区域配置方式”时，参数“模板ID”或“模板类型”没有输入。                             | 根据实际情况，重新输入参数，确保满足当输入参数“漫游区域配置方式”时，参数“模板ID”和“模板类型”必须输入的条件。                                               |