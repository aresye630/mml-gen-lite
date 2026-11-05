# 查询VLR类型数据(LST VLRTYP)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询VLR类型信息：

- 若需要查询全部的VLR类型数据，请输入“HLR序列号”，其他参数不输入。
- 若需要查询某个VLR号码前缀的VLR类型数据的详细信息，请输入“HLR序列号”和“VLR号码前缀”。

## 注意事项

无。

## 参数说明

| 参数标识      | 参数名称    | 参数说明                                              |
|:----------|:--------|:--------------------------------------------------|
| HLRSN     | HLR序列号  | 用于指示系统按照哪个HLR序列号来查询VLR类型数据，该参数必须选择。               |
| VLRPREFIX | VLR号码前缀 | 用于指示系统按照哪个VLR号码前缀来查询VLR类型数据；若不输入，则表示查询所有的VLR类型数据。 |

## 使用实例

1. 查询“HLR序列号”为“4”的HLR上的VLR类型数据记录：

   ```
   LST VLRTYP: HLRSN=4;
   ```

   ```
   %%LST VLRTYP: HLRSN=4;%%
   RETCODE = 0 SUCCESS0001:操作成功

                  "VLR Number Prefix"  "VLR Number Type"  "NCCTPL"  "VLR Name"                     "Service Control"  "CAMELCAPTPL"       "ETCSIRESTTPLID"
                  6613413002           CROSSINTERNATIONAL NOTPROV   <NULL>                         PERMISSION         NOTPROV             NOTPROV
                  6613413005           LOCALINTERNATIONAL NOTPROV   <NULL>                         PERMISSION         NOTPROV             NOTPROV
                  86129801             LOCAL              NOTPROV   <NULL>                         PERMISSION         NOTPROV             NOTPROV
                  8613413001           LOCAL              NOTPROV   <NULL>                         PERMISSION         NOTPROV             NOTPROV
                  8613413003           LOCALDOMESTIC      NOTPROV   <NULL>                         PERMISSION         NOTPROV             NOTPROV
                  8613413004           CROSSDOMESTIC      NOTPROV   <NULL>                         PERMISSION         NOTPROV             NOTPROV
                  8613413006           LOCALAREA          NOTPROV   <NULL>                         PERMISSION         NOTPROV             NOTPROV
                  8613413007           CROSSAREA          NOTPROV   <NULL>                         PERMISSION         NOTPROV             NOTPROV

   Total count = 8

   There is together 1 report

   ---    END
   ```
2. 查询“HLR序列号”为“4”的HLR上的VLR类型数据记录。其中，“VLR号码前缀”为“8613800”：

   ```
   LST VLRTYP: HLRSN=1, VLRPREFIX="8613800";
   ```

   ```
   %%LST VLRTYP: HLRSN=1, VLRPREFIX="8613800";%%
   RETCODE = 0 SUCCESS0001:操作成功

          "VLR Number Prefix"  "VLR Number Type"  "NCCTPL"  "VLR Name"                     "Service Control"  "CAMELCAPTPL"       "ETCSIRESTTPLID"
           8613800              LOCALDOMESTIC      NOTPROV   VLR1                           PERMISSION         NOTPROV             NOTPROV

   Total count = 1

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**ADD VLRTYP**命令的参数说明。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释   | 原因分析                                | 处理建议                                                                                                                                                   |
|:--------|:--------|:------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------|
| ERR1004 | 无效的参数值  | 参数“VLR号码前缀”的取值中含有0～9以外的字符。          | 根据实际情况，重新输入“VLR号码前缀”，确保其取值为长度不超过14位的数字组成的字符串。                                                                                                          |
| ERR3007 | 记录不存在   | 可能原因为如下之一：“HLR序列号”未定义。“VLR号码前缀”未添加。 | 根据可能原因可按如下方法操作：根据实际情况，重新输入已定义的“HLR序列号”，已定义的“HLR序列号”可通过LST HLRSN命令查询。根据实际情况，仅输入“HLR序列号”，查询对应“HLR序列号”所有已添加的“VLR号码前缀”，若还是提示该错误，证明对应“HLR序列号”下无“VLR号码前缀”记录。 |