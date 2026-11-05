# 查询被叫号码分析数据(LST CALLEDNA)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询被叫号码分析数据的配置信息。

- 若需要查询某个虚拟HLR中所有被叫号码分析数据的配置信息，请只输入“HLR序列号”参数。
- 若需要查询某个虚拟HLR中某条被叫号码分析数据的详细配置信息，请同时输入“HLR序列号”和“呼叫字冠”参数。

## 注意事项

无。

## 参数说明

| 参数标识       | 参数名称   | 参数说明                                             |
|:-----------|:-------|:-------------------------------------------------|
| HLRSN      | HLR序列号 | 用于标识系统需要按照哪个HLR序列号来查询被叫号码分析数据。                   |
| CALLPREFIX | 呼叫字冠   | 用于标识系统需要按照哪个呼叫字冠来查询被叫号码分析数据；若不输入，则表示所有的被叫号码分析数据。 |

## 使用实例

1. 查询被叫号码分析数据记录，“HLR序列号”为“1”：

   ```
   LST CALLEDNA: HLRSN=1;
   ```

   ```
   %%LST CALLEDNA: HLRSN=1;%%
   RETCODE = 0 SUCCESS0001:操作成功

           "Called Number Prefix"    "Service Property"    "INFOFLAG"    "ENTERFLAG"   "VMSFLAG"   "MINLEN"  "MAXLEN"
           00                        INTERNATIONAL         FALSE         FALSE         FALSE                 
           0                         NATIONAL              FALSE         FALSE         FALSE                 
           1101000                   LOCAL                 TRUE          TRUE          FALSE                 
           13                        PLMN                  FALSE         FALSE         FALSE                 
           15                        PLMN                  FALSE         FALSE         FALSE                 
           1                         LOCAL                 FALSE         FALSE         FALSE                 
           2                         LOCAL                 FALSE         FALSE         FALSE                 
           3                         LOCAL                 FALSE         FALSE         FALSE                 
           4                         LOCAL                 FALSE         FALSE         FALSE                 
           5                         LOCAL                 FALSE         FALSE         FALSE                 
           6                         LOCAL                 FALSE         FALSE         FALSE                 
           7                         LOCAL                 FALSE         FALSE         FALSE                 
           8                         LOCAL                 FALSE         FALSE         FALSE                 
           9                         LOCAL                 FALSE         FALSE         FALSE                 

   Total count = 14

   There is together 1 report

   ---    END
   ```
2. 查询被叫号码分析数据记录，“HLR序列号”为“1”，“呼叫字冠”为“00”：

   ```
   LST CALLEDNA: HLRSN=1, CALLPREFIX="00";
   ```

   ```
   %%LST CALLEDNA: HLRSN=1, CALLPREFIX="00";%%
   RETCODE = 0 SUCCESS0001:操作成功

           "Called Number Prefix"    "Service Property"    "INFOFLAG"    "ENTERFLAG"   "VMSFLAG"   "MINLEN"  "MAXLEN"
           00                        INTERNATIONAL         FALSE         FALSE         FALSE                 

   Total count = 1

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**ADD CALLEDNA**命令的参数说明。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释   | 原因分析                    | 处理建议                                                                                      |
|:--------|:--------|:------------------------|:------------------------------------------------------------------------------------------|
| ERR3007 | 记录不存在   | “HLR序列号”未定义或者“呼叫字冠”未定义。 | 根据实际情况，重新输入已定义的“HLR序列号”和“呼叫字冠”，可通过LST HLRSN命令查询已定义的“HLR序列号”，通过LST CALLEDNA命令查询已定义的“呼叫字冠”。 |