# 查询ETCSI转换模板(LST ETCSICONVERTPL)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询ETCSI转换模板信息数据：

- 若需要查询全部ETCSI转换模板的配置信息，请只输入“HLR序列号”参数。
- 若需要查询某个ETCSI转换模板的详细配置信息，请同时输入“HLR序列号”和“ETCSI转换模板ID”参数。

## 注意事项

无。

## 参数说明

| 参数标识              | 参数名称        | 参数说明                                          |
|:------------------|:------------|:----------------------------------------------|
| HLRSN             | HLR序列号      | 用于指示系统按照哪个HLR序列号来查询ETCSI转换模板。                 |
| ETCSICONVER_TPLID | ETCSI转换模板ID | 用于指示系统按照哪个模板ID来查询ETCSI转换模板数据；若不输入，则表示所有的模板ID。 |

## 使用实例

1. 查询ETCSI转换模板信息。“HLR序列号”为“1”：

   ```
   LST ETCSICONVERTPL: HLRSN=1;
   ```

   ```
   %%LST ETCSICONVERTPL: HLRSN=1;%%
   RETCODE = 0 SUCCESS0001:Operation is successful

                  ETCSICONVER_TPLID   TPLNAME
                  1                   11

   Total count = 1

   There is together 1 report

   ---    END
   ```
2. 查询ETCSI转换模板信息。“HLR序列号”为“1”，“ETCSI转换模板ID”为“1”：

   ```
   LST ETCSICONVERTPL: HLRSN=1, ETCSICONVER_TPLID=1;
   ```

   ```
   %%LST ETCSICONVERTPL: HLRSN=1, ETCSICONVER_TPLID=1;%%
   RETCODE = 0 SUCCESS0001:Operation is successful

                            HLRSN = 1
                ETCSICONVER_TPLID = 1
                          TPLNAME = 11
                      MAP_VERSION = MAPV3
                      ETCSI_RANGE = HPLMN
                      DEP_SEVTYPE = NONE
               ETCSI_RESTRAIN_IND = FALSE
                ETCSI_CONVER_TYPE = EQUAL
               ETCSI_CONVER_VALUE = 123

   Total count = 9

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**SET ETCSICONVERTPL**命令的参数说明。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释   | 原因分析                           | 处理建议                                                                                         |
|:--------|:--------|:-------------------------------|:---------------------------------------------------------------------------------------------|
| ERR3003 | 模板未定义   | “HLR序列号”未定义或者“ETCSI转换模板ID”未定义。 | 根据实际情况，重新输入已定义的“HLR序列号”和“ETCSI转换模板ID”，可通过LST HLRSN命令查询已定义的“HLR序列号”，通过该命令查询已定义的“ETCSI转换模板ID”。 |