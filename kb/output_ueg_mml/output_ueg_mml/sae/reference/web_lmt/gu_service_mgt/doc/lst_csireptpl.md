# 查询CSI替代模板(LST CSIREPTPL)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询CSI（CAMEL Subscription Information）替代模板的配置信息：

- 若需要查询某个HLR序列号下全部CSI替代模板的概要配置信息，请只输入“HLR序列号”。
- 若需要查询某个HLR序列号下某个CSI替代模板的详细配置信息，请输入“HLR序列号”和“替代模板ID”。

## 注意事项

无。

## 参数说明

| 参数标识     | 参数名称   | 参数说明                                              |
|:---------|:-------|:--------------------------------------------------|
| HLRSN    | HLR序列号 | 用于指示系统按照哪个HLR序列号来查询CSI替代模板信息数据。                   |
| REPTPLID | 替代模板ID | 用于指示系统按照哪个替代模板ID来查询CSI替代模板信息数据。若不输入，则表示所有的替代模板ID。 |

## 使用实例

1. 查询CSI替代模板信息，“HLR序列号”为“1”：

   ```
   LST CSIREPTPL: HLRSN=1;
   ```

   ```
   %%LST CSIREPTPL: HLRSN=1;%%
   RETCODE = 0 SUCCESS0001:操作成功

                  REPTPLID     TPLNAME
                  1            CSIREPTPL1
                  2            CSIREPTPL2

   Total count = 2

   There is together 1 report

   ---    END
   ```
2. 查询CSI替代模板信息，“HLR序列号”为“1”，“替代模板ID”为“1”：

   ```
   LST CSIREPTPL: HLRSN=1, REPTPLID=1;
   ```

   ```
   %%LST CSIREPTPL: HLRSN=1, REPTPLID=1;%%
   RETCODE = 0 SUCCESS0001:操作成功

                            HLRSN = 1
                         REPTPLID = 1
                          TPLNAME = CSIREPTPL1
    
    
   VSAREATPLID  UCSITPLID
   1            2

   Total count = 4

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**SET CSIREPTPL**命令的参数说明。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释   | 原因分析                      | 处理建议                                                                                           |
|:--------|:--------|:--------------------------|:-----------------------------------------------------------------------------------------------|
| ERR3003 | 模板未定义   | “HLR序列号”未定义或者“替代模板ID”未定义。 | 根据实际情况，重新输入已定义的“HLR序列号”和“替代模板ID”，可通过LST HLRSN命令查询已定义的“HLR序列号”，通过LST CSIREPTPL命令查询已定义的“替代模板ID”。 |