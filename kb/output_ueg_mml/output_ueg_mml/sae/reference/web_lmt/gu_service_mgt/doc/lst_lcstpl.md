# 查询LCS模板(LST LCSTPL)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询LCS（Location Services）模板的配置信息。

- 若需要查询某个虚拟HSS/HLR中所有LCS模板的配置信息，请只输入“HLR序列号”参数。
- 若需要查询某个虚拟HSS/HLR中某条LCS模板的详细配置信息，请同时输入“HLR序列号”和“模板ID”参数。

## 注意事项

无。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                        |
|:-------|:-------|:--------------------------------------------|
| HLRSN  | HLR序列号 | 用于标识系统需要按照哪个HLR序列号来查询LCS模板数据。               |
| TPLID  | 模板ID   | 用于标识系统需要按照哪个模板ID来查询LCS模板数据；若不输入，则表示所有的模板ID。 |

## 使用实例

1. 查询“HLR序列号”为“1”的HLR上的LCS模板数据记录：

   ```
   LST LCSTPL: HLRSN=1;
   ```

   ```
   %%LST LCSTPL: HLRSN=1;%%
   RETCODE = 0 SUCCESS0001:操作成功

                  TPLID        TPLNAME
                  2            LCS1
                  5            huawei

   Total count = 2

   There is together 1 report

   ---    END
   ```
2. 查询“HLR序列号”为“1”的HLR上的LCS模板数据记录。其中，“模板ID”为“5”：

   ```
   LST LCSTPL: HLRSN=1, TPLID=5;
   ```

   ```
   %%LST LCSTPL: HLRSN=1, TPLID=5;%%
   RETCODE = 0 SUCCESS0001:Operation is successful

                            HLRSN = 1
                            TPLID = 5
                          TPLNAME = huawei
                              PLF = MSC
                           PECODE = Callrelated
                             NTMU = NotifyLocationAllowed
                            EC1EA = 8613800001111
                            EC1GR = Gmlclist
                          EC1NTMU = NotifyAndVerify-LocationAllowedIfNoResponse
                        MOLR1CODE = AutonomousSelfLocation
                        MOLR2CODE = BasicSelfLocation

   Total count = 11

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**ADD LCSTPL**命令的参数说明。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释   | 原因分析                    | 处理建议                                                                                    |
|:--------|:--------|:------------------------|:----------------------------------------------------------------------------------------|
| ERR3003 | 模板未定义   | “HLR序列号”未定义或者“模板ID”未定义。 | 根据实际情况，重新输入已定义的“HLR序列号”和“模板ID”，可通过LST HLRSN命令查询已定义的“HLR序列号”，通过LST LCSTPL命令查询已定义的“模板ID”。 |