# 查询USSD控制数据(LST USSDDAT)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询USSD控制表信息。

- 若需要查询全部的USSD控制数据，请输入“HLR序列号”即可。
- 若需要查询某个业务码相关的USSD控制数据的详细信息，请输入“HLR序列号”和“业务码”。

## 注意事项

无。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                            |
|:-------|:-------|:------------------------------------------------|
| HLRSN  | HLR序列号 | 用于指示系统按照哪个HLR序列号来查询USSD控制数据，该参数必须选择。            |
| SRCODE | 业务码    | 用于指示系统按照哪个业务码来查询USSD控制数据；若不输入，则表示查询所有的USSD控制数据。 |

## 使用实例

1. 查询“HLR序列号”为“1”的HLR上的USSD控制数据记录：

   ```
   LST USSDDAT: HLRSN=1;
   ```

   ```
   %%LST USSDDAT: HLRSN=1;%%
   RETCODE = 0 SUCCESS0001:操作成功

           "Service Code"      "Function"          "Forwarded Address"    "Pussd Option"     "Specific"     "Match Rule"    "SSN"    "ISDNGTTPL_ID"
           166                 GSMMODE             86123001                                  FALSE          MAX_MATCH       GMLC     1
           167                 GSMMODE             86123002                                  FALSE          MAX_MATCH       GMLC     2
           168                 GSMMODE             86123003                                  FALSE          MAX_MATCH       GMLC     3
           169                 GSMMODE             86123004                                  FALSE          MAX_MATCH       GMLC     4
           170                 GSMMODE             86123005                                  FALSE          MAX_MATCH       GMLC     5

   Total count = 5

   There is together 1 report

   ---    END
   ```
2. 查询“HLR序列号”为“1”的HLR上的USSD控制数据记录。其中“业务码”为“168”：

   ```
   LST USSDDAT: HLRSN=1, SRCODE="168";
   ```

   ```
   %%LST USSDDAT: HLRSN=1;%%
   RETCODE = 0 SUCCESS0001:操作成功

           "Service Code"      "Function"          "Forwarded Address"    "Pussd Option"     "Specific"     "Match Rule"    "SSN"     "ISDNGTTPL_ID"

           168                 GSMMODE             86123003                                  FALSE          MAX_MATCH       GMLC      3

   Total count = 1

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**ADD USSDDAT**命令的参数说明。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释   | 原因分析                               | 处理建议                                                                                    |
|:--------|:--------|:-----------------------------------|:----------------------------------------------------------------------------------------|
| ERR1004 | 无效的参数值  | 参数“业务码”的取值中含有0～9、“*”和“#”以外的字符。     | 根据实际情况，重新输入“业务码”，确保其取值为长度不超过14位的数字组成的字符串。                                               |
| ERR3007 | 记录不存在   | 有两点原因：HLR序列号未定义。HLR序列号对应的“业务码”未添加。 | 对于第一点原因，执行LST HLRSN命令查询出已定义的HLRSN，然后在执行命令时输入即可。 对于第二点原因，在执行LST USSDDAT命令时只输入“HLR序列号”即可。 |