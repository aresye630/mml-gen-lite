# 查询组ID模板(LST GROUPIDTPL)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询组ID模板的配置信息。

- 若需要查询某类组呼类型全部组ID模板的配置信息，请输入“HLR序列号”和“组类型”参数。
- 若需要查询某类组呼类型某个组ID模板的详细配置信息，请同时输入“HLR序列号”、“模板ID”和“组类型”参数。

## 注意事项

无。

## 参数说明

| 参数标识      | 参数名称   | 参数说明                                             |
|:----------|:-------|:-------------------------------------------------|
| HLRSN     | HLR序列号 | 用于指示系统按照哪个HLR序列号来查询组ID模板信息数据。                    |
| TPLID     | 模板ID   | 用于指示系统按照哪个模板ID来查询组ID信息数据；若不输入，则表示查询所有的组ID模板信息数据。 |
| GROUPTYPE | 组类型    | 用于指示系统按照哪个组呼类型来查询组ID信息数据。                        |

## 使用实例

1. 查询“HLR序列号”为“1”的HLR上的组ID模板数据记录。其中，“组类型”为“VGCS”：

   ```
   LST GROUPIDTPL: HLRSN=1, GROUPTYPE=VGCS;
   ```

   ```
   %%LST GROUPIDTPL: HLRSN=1, GROUPTYPE=VGCS;%%
   RETCODE = 0 SUCCESS0001:操作成功

                  TPLID        TPLNAME
                  1            test1_vgcs
                  3            test3_vgcs

   Total count = 2

   There is together 1 report

   ---    END
   ```
2. 查询“HLR序列号”为“1”的HLR上的组ID模板数据记录。其中，“模板号”为“1”，“组类型”为“VGCS”：

   ```
   LST GROUPIDTPL: HLRSN=1, TPLID=1, GROUPTYPE=VGCS;
   ```

   ```
   %%LST GROUPIDTPL: HLRSN=1, TPLID=1, GROUPTYPE=VGCS;%%
   RETCODE = 0 SUCCESS0001:操作成功

                            HLRSN = 1
                            TPLID = 1
                          TPLNAME = test1_vgcs
                 CAPINITONROAMING = TRUE
                         GROUPID1 = 1234

   Total count = 5

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数请参见**ADD GROUPIDTPL**命令的参数说明。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释   | 原因分析                                                             | 处理建议                                                                                                        |
|:--------|:--------|:-----------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------|
| ERR3003 | 模板未定义   | 可能原因为如下之一：“HLR序列号”或者“模板ID”未定义。 “模板ID”和“组类型”的匹配关系和数据库中实际存在的模板不一致。 | 根据实际情况，重新输入已定义的“HLR序列号”和“模板ID”，可通过LST HLRSN命令查询已定义的“HLR序列号”，通过LST GROUPIDTPL命令查询已定义的“模板ID”和“组类型”在数据库中的匹配关系。 |