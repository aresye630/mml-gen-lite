# 查询SCP地址模板(LST SCPTPL)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询SCP（Service Control Point）地址模板中的配置信息：

- 若需要查询某个HLR序列号下全部SCP地址模板的概要配置信息，请只输入“HLR序列号”。
- 若需要查询某个HLR序列号下某个SCP地址模板的详细配置信息，请输入“HLR序列号”和“模板ID”。

## 注意事项

无。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                          |
|:-------|:-------|:----------------------------------------------|
| HLRSN  | HLR序列号 | 用于指示系统按照哪个HLR序列号来查询SCP地址模板信息数据。               |
| TPLID  | 模板ID   | 用于指示系统按照哪个模板ID来查询SCP地址模板信息数据；若不输入，则表示所有的模板ID。 |

## 使用实例

1. 查询SCP地址模板，“HLR序列号”为“1”。命令如下：

   ```
   LST SCPTPL: HLRSN=1;
   ```

   ```
   %%LST SCPTPL: HLRSN=1;%%
   RETCODE = 0 SUCCESS0001:操作成功

                  TPLID        TPLNAME
                  1            scp001
                  0            scp002

   Total count = 2

   There is together 1 report

   ---    END
   ```
2. 查询SCP地址模板，“HLR序列号”为“1”，“模板ID”为“001”。命令如下：

   ```
   LST SCPTPL: HLRSN=1, TPLID=001;
   ```

   ```
   %%LST SCPTPL: HLRSN=1, TPLID=001;%%
   RETCODE = 0 SUCCESS0001:操作成功

                            HLRSN = 1
                            TPLID = 1
                          TPLNAME = scp001
                            CAMEL = PHASE1
                    AVAILABLEPLMN = LOCALDOMESTIC
                          SCPADDR = 111111111111111
                               SK = 222
                          DEFCALL = RELEASECALL

   Total count = 8

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**ADD SCPTPL**命令的参数说明。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释     | 原因分析                           | 处理建议                                                                        |
|:--------|:----------|:-------------------------------|:----------------------------------------------------------------------------|
| ERR3003 | 模板未定义     | “HLR序列号”和“模板ID”参数对应的模板数据记录不存在。 | 根据实际情况，重新输入参数，确保“HLR序列号”和“模板ID”参数对应的模板数据记录已存在。已存在的模板数据记录可以通过LST SCPTPL命令查询。 |
| ERR3097 | HLR序列号未定义 | “HLR序列号”未定义。                   | 根据实际情况，重新输入“HLR序列号”的取值，确保其取值符合要求。                                           |