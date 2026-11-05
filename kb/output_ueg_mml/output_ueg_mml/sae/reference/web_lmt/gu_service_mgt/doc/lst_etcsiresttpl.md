# 查询ETCSI限制模板（LST ETCSIRESTTPL）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询ETCSI限制模板信息。

- 若需要查询某个“HLR序列号”上全部ETCSI限制模板信息，请输入“HLR序列号”，其他参数不输入。
- 若需要查询某个ETCSI限制模板的详细信息，请输入“HLR序列号”和“模板ID”。

## 注意事项

无。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                                  |
|:-------|:-------|:------------------------------------------------------|
| HLRSN  | HLR序列号 | 用于指示系统按照哪个HLR序列号来查询ETCSI限制模板信息。                       |
| TPLID  | 模板ID   | 用于指示系统按照哪个模板ID来查询ETCSI限制模板信息；若不输入，则表示查询所有的ETCSI限制模板信息 |

## 使用实例

1. 查询“HLR序列号”为“1”的全部ETCSI限制模板信息。命令如下：

   ```
   LST ETCSIRESTTPL: HLRSN=1;
   ```

   ```
   %%LST ETCSIRESTTPL: HLRSN=1;%%
   RETCODE = 0 SUCCESS0001:Operation is successful

                  TPLID          TPLNAME
                  1              ETCSI1
                  2              ETCSI2
                  3              ETCSI3

   Total count = 3

   There is together 1 report

   ---    END
   ```
2. 查询“HLR序列号”为“1”、“模板ID”为“2”的ETCSI限制模板信息。命令如下：

   ```
   LST ETCSIRESTTPL: HLRSN=1, TPLID=2;
   ```

   ```
   %%LST ETCSIRESTTPL: HLRSN=1, TPLID=2;%%
   RETCODE = 0 SUCCESS0001:Operation is successful

                            HLRSN = 1
                            TPLID = 2
                          TPLNAME = ETCSI2
                         ETCSI_SK = 1

   Total count = 4

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**ADD ETCSIRESTTPL**命令的参数说明。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释   | 原因分析                    | 处理建议                                                                           |
|:--------|:--------|:------------------------|:-------------------------------------------------------------------------------|
| ERR3003 | 模板未定义   | “HLR序列号”未定义或者“模板ID”未定义。 | 根据实际情况，重新输入已定义的“HLR序列号”和“模板ID”，可通过LST HLRSN命令查询已定义的“HLR序列号”，通过该命令查询已定义的“模板ID”。 |