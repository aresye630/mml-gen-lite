# 查询Diameter漫游限制模板(LST DIAMRRTPL)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询Diameter漫游限制模板信息数据：

- 若需要查询全部Diameter漫游限制模板的配置信息，请只输入“HLR序列号”参数。
- 若需要查询某个Diameter漫游限制模板的详细配置信息，请同时输入“HLR序列号”和“模板ID”参数。

## 注意事项

无。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                             |
|:-------|:-------|:-------------------------------------------------|
| HLRSN  | HLR序列号 | 用于指示系统按照哪个HLR序列号来查询Diameter漫游限制模板。               |
| TPLID  | 模板ID   | 用于指示系统按照哪个模板ID来查询Diameter漫游限制数据；若不输入，则表示所有的模板ID。 |

## 使用实例

1. 查询Diameter漫游限制模板信息。“HLR序列号”为“1”：

   ```
   LST DIAMRRTPL: HLRSN=1;
   ```

   ```
   %%LST DIAMRRTPL: HLRSN=1;%%
   RETCODE = 0 SUCCESS0001:操作成功

   TPLID        TPLNAME                                                     DEFAULTRULE
   1            1                                                           PERMISSION
   2            test_2                                                      PERMISSION
   3            test_3                                                      RESTRICT

   Total count = 3

   There is together 1 report

   ---    END
   ```
2. 查询Diameter漫游限制模板信息。“HLR序列号”为“1”，“模板ID”为“1”：

   ```
   LST DIAMRRTPL: HLRSN=1, TPLID=1;
   ```

   ```
   %%LST DIAMRRTPL: HLRSN=1, TPLID=1;%%
   RETCODE = 0 SUCCESS0001:操作成功

                            TPLID = 1
                          TPLNAME = test_1
                      DEFAULTRULE = RESTRICT
                 DEF_SERRESTTPLID = 1
    
   Config information as the following
   -----------------------------------------------
    
   RULE           DIAMIDENTITYTYPE    DIAMIDENTITY                                                                                                                           REALMNAME
   PERMISSION     HOSTNAME            123                                                                                                                                    huawei.com

   Total count = 4

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**ADD DIAMRRTPL**命令的参数说明。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码息解释   | 原因分析                    | 处理建议                                                                                       |
|:--------|:---------|:------------------------|:-------------------------------------------------------------------------------------------|
| ERR3003 | 模板未定义    | “HLR序列号”未定义或者“模板ID”未定义。 | 根据实际情况，重新输入已定义的“HLR序列号”和“模板ID”，可通过LST HLRSN命令查询已定义的“HLR序列号”，通过LST DIAMRRTPL命令查询已定义的“模板ID”。 |