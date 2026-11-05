# 查询5G NCC模板(LST NGSNCCTPL)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询已配置的5G NCC（Network Capability Configuration）模板信息数据。

- 若需要查询全部5G NCC模板的配置信息，请输入“HLR序列号”。
- 若需要查询某个5G NCC模板的详细配置信息，请同时输入“HLR序列号”和“模板ID”参数。

## 注意事项

无。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                      |
|:-------|:-------|:--------------------------------------------------------------------------|
| HLRSN  | HLR序列号 | 用于指示系统按照哪个HLR序列号来查询NCC模板数据。 取值范围：1～255 默认值：无。                             |
| TPLID  | 模板ID   | 用于指示系统需要按照哪个模板ID来查询5G NCC模板信息；若不输入，则表示查询所有5G NCC模板ID。 取值范围：0～99998 默认值：无。 |

## 使用实例

1. 查询“HLR序列号”为“1”的UDM上的NCC模板数据记录：

   ```
   LST NGSNCCTPL: HLRSN=1;
   ```

   ```
   %%LST NGSNCCTPL: HLRSN=1;%%
   RETCODE = 0 SUCCESS0001:操作成功

             TPLID        TPLNAME
             3            TEST02
             5            TEST03
             8            TEST05

   Total count = 3

   There is together 1 report

   ---    END
   ```
2. 查询“HLR序列号”为“1”的UDM上的NCC模板数据记录。其中，“模板ID”为“3”：

   ```
   LST NGSNCCTPL: HLRSN=1, TPLID=3;
   ```

   ```
   %%LST NGSNCCTPL: HLRSN=1, TPLID=3;%%
   RETCODE = 0 SUCCESS0001:操作成功

                            HLRSN = 1
                            TPLID = 3
                          TPLNAME = TEST02
   NGC Service
                        BKAMFMODE = NONE
               ROAM_REQ_WITH_PORT = 0
               ROAM_CBK_WITH_PORT = 0
                   AMFHOTBACKMODE = INVALID
                    SUPPREDCAPPTW = SR

   Total count = 8

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**ADD NGSNCCTPL**命令的参数说明。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释   | 原因分析                    | 处理建议                                                                                       |
|:--------|:--------|:------------------------|:-------------------------------------------------------------------------------------------|
| ERR3003 | 模板未定义   | “HLR序列号”未定义或者“模板ID”未定义。 | 根据实际情况，重新输入已定义的“HLR序列号”和“模板ID”，可通过LST HLRSN命令查询已定义的“HLR序列号”，通过本命令且只输入“HLR序列号”查询已定义的“模板ID”。 |