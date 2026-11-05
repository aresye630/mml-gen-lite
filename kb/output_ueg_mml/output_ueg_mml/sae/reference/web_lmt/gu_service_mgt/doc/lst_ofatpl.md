# 查询OFA模板(LST OFATPL)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询OFA模板中的配置信息：

- 若要查询全部的OFA模板数据信息，请将“HLR序列号”参数输入，其他参数不输入。
- 若需要查询某个OFA模板的详细信息，请输入全部参数。

## 注意事项

无。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                         |
|:-------|:-------|:-----------------------------------------------------------------------------|
| HLRSN  | HLR序列号 | 用于指示系统在哪个HLR中查询OFA模板数据。该参数必须先由ADD HLRSN命令定义，然后才能在此处引用。                       |
| TPLID  | 模板ID   | 用于指示系统需要进行查询的OFA模板的模板ID。用于指示系统需要按照哪个“模板ID”来查询OFA模板数据；若不输入，则查询出所有的OFA模板和模板名称。 |

## 使用实例

1. 查询“HLR序列号”为“1”的HLR上的OFA模板数据记录。其中，“模板ID”为“1”：

   ```
   LST OFATPL: HLRSN=1, TPLID=1;
   ```

   ```
   %%LST OFATPL: HLRSN=1, TPLID=1;%%
   RETCODE = 0 SUCCESS0001:Operation is successful

                            HLRSN = 1
                            TPLID = 1
                          TPLNAME = ofi1
                     DEFAULT RULE = TRUE

           <PREFIX>                        <RULE>         <REMOVIND>     <ADDEDDIGIT>   <TREEOPTION>   <NEXTINDEX>    <PROCESSIND>
           86755100                        TRUE           0                             NONE                          NO PROCESS
           86755200                        TRUE           0                             NONE                          NO PROCESS
           86755300                        FALSE          0                             NONE                          NO PROCESS

   Total count = 7

   There is together 1 report

   ---    END
   ```
2. 查询“HLR序列号”为“1”的HLR上的OFA模板数据记录：

   ```
   LST OFATPL: HLRSN=1;
   ```

   ```
   %%LST OFATPL: HLRSN=1;%%
   RETCODE = 0 SUCCESS0001:Operation is successful

                  TPLID        TPLNAME
                  0            ofi0
                  1            ofi1
                  2            ofi2

   Total count = 3

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**ADD OFATPL**命令的参数说明。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释   | 原因分析                                | 处理建议                                                                                        |
|:--------|:--------|:------------------------------------|:--------------------------------------------------------------------------------------------|
| ERR3003 | 模板未定义   | “HLR序列号”未定义或者“模板ID”对应的OFA模板数据记录不存在。 | 根据实际情况，重新输入已定义的“HLR序列号”和已存在的“模板ID”，可通过LST HLRSN命令查询已定义的“HLR序列号”，通过LST OFATPL命令查询已存在的“模板ID”。 |