# 查询IMSI与ADD业务数据(LST IMSIADD)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询IMSI与ADD业务相关的数据信息。

- 若携带参数“IMSI前缀”，则只查询该“IMSI前缀”对应的记录。
- 若未携带参数“IMSI前缀”，则查询该“HLR序列号”对应的记录。

## 注意事项

无。

## 参数说明

| 参数标识    | 参数名称   | 参数说明                                                       |
|:--------|:-------|:-----------------------------------------------------------|
| HLRSN   | HLR序列号 | 用于指示系统需要按照哪个HLR序列号来查询IMSI与ADD业务的控制数据。                      |
| IMSIPRE | IMSI前缀 | 用于指示系统需要按照哪个IMSI号段来查询IMSI前缀与ADD业务的控制数据；若不输入，则表示查询所有IMSI号段。 |

## 使用实例

1. 查询“HLR序列号”为“1”，“IMSI前缀”为“12345”的数据记录：

   ```
   LST IMSIADD: HLRSN=1, IMSIPRE="12345";
   ```

   ```
   %%LST IMSIADD: HLRSN=1, IMSIPRE="12345";%%
   RETCODE = 0 SUCCESS0001:操作成功

   IMSIPRE               SENDADD               RECORDIMEI
   12345                 SOAP                  FALSE

   Total count = 1

   There is together 1 report

   ---    END
   ```
2. 查询“HLR序列号”为“1”的所有数据记录：

   ```
   LST IMSIADD: HLRSN=1;
   ```

   ```
   %%LST IMSIADD: HLRSN=1;%%
   RETCODE = 0 SUCCESS0001:Operation is successful

   IMSIPRE               SENDADD               RECORDIMEI
   12345                 SOAP                  FALSE
   678                   NONE                  TRUE

   Total count = 2

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**SET IMSIADD**命令的参数说明。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释   | 原因分析                             | 处理建议                                                  |
|:--------|:--------|:---------------------------------|:------------------------------------------------------|
| ERR1004 | 无效的参数值  | 参数“IMSI前缀”的取值不是1～15位十进制数字组成的字符串。 | 根据实际情况，重新输入“IMSI前缀”的取值，确保其取值符合要求。                     |
| ERR1009 | 参数丢失    | “HLR序列号”未输入。                     | 根据实际情况，重新输入参数。                                        |
| ERR1118 | 参数重复    | 重复输入了该命令中的任意参数。                  | 核实输入的命令，若命令中任意参数输入了两次以上，则删除多余的重复参数后，重新执行该命令。          |
| ERR3007 | 记录不存在   | “HLR序列号”未定义。                     | 根据实际情况，重新输入已定义的“HLR序列号”，可通过LST HLRSN命令查询已定义的“HLR序列号”。 |