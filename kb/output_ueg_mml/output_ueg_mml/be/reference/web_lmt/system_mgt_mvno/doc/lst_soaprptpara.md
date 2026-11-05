# 查询指定命令的白名单参数(LST SOAPRPTPARA)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询指定命令的白名单参数信息。

- 若需要查询所有配置了白名单参数的命令，则不输入任何参数。
- 若需要查询某个命令配置的白名单参数信息，请输入“命令名”参数。

## 注意事项

无。

## 参数说明

| 参数标识    | 参数名称   | 参数说明                                           |
|:--------|:-------|:-----------------------------------------------|
| CMDNAME | 命令名    | 用于指示系统需要查询哪个命令配置的白名单参数信息。若不输入则查询所有配置了白名单参数的命令。 |

## 使用实例

1. 查询所有配置了白名单参数的命令。

   ```
   LST SOAPRPTPARA:;
   ```

   ```
   %%LST SOAPRPTPARA:;%%
   RETCODE = 0 操作成功

           "CMD name"
           LST EXPLOGTASK
           LST LINKSTATE
           LST SUINFO

   Total count = 3

   There is together 1 report

   ---    END
   ```
2. 查询“LST EXPLOGTASK”命令配置的白名单参数信息。

   ```
   LST SOAPRPTPARA: CMDNAME="LST EXPLOGTASK";
   ```

   ```
   %%LST SOAPRPTPARA: CMDNAME="LST EXPLOGTASK";%%
   RETCODE = 0 操作成功

                  CMD name = LST EXPLOGTASK
                 Para list = EXPTASKID&SERVERNAME&FETYPE&TASKTYPE&CYCLEUNIT&EXPCYCLE&STARTTIME&F
                             IELD&FILTER&FILENAME&TITLES

   Total count = 2

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**ADD SOAPRPTPARA**命令的参数说明。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

|   错误码 | 错误码解释   | 原因分析                         | 处理建议                                            |
|------:|:--------|:-----------------------------|:------------------------------------------------|
|  1004 | 无效的参数值。 | 输入的参数值不在其取值范围内或者输入的参数值不符合要求。 | 根据实际情况，重新输入提示错误的参数的取值，确保其取值符合要求。                |
|  1038 | 记录不存在。  | 输入的“命令名”参数所对应的记录不存在。         | 请确保输入的“命令名”参数所对应的记录存在。已存在的记录可以通过执行本命令不输入任何参数查询。 |