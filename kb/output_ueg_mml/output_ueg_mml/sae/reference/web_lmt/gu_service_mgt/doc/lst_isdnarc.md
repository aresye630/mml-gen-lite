# 查询MSISDN与区号数据(LST ISDNARC)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询MSISDN与区号数据的配置信息。

- 若需要查询某个虚拟HLR中所有MSISDN与区号数据的配置信息，请只输入“HLR序列号”参数。
- 若需要查询某个虚拟HLR中某条MSISDN与区号数据的详细配置信息，请同时输入“HLR序列号”和“MSISDN前缀”参数。

## 注意事项

无。

## 参数说明

| 参数标识       | 参数名称     | 参数说明                                                       |
|:-----------|:---------|:-----------------------------------------------------------|
| HLRSN      | HLR序列号   | 用于标识系统需要按照哪个HLR序列号来查询MSISDN与区号数据。                          |
| ISDNPREFIX | MSISDN前缀 | 用于标识系统需要按照哪个MSISDN前缀来查询MSISDN与区号数据；若不输入，则表示所有的MSISDN与区号数据。 |

## 使用实例

1. 查询MSISDN与区号数据记录，“HLR序列号”为“1”：

   ```
   LST ISDNARC: HLRSN=1;
   ```

   ```
   %%LST ISDNARC: HLRSN=1;%%
   RETCODE = 0 SUCCESS0001:操作成功

           "ISDN Number"    "Area Code"
           1380270          755
           1380271          10

   Total count = 2

   There is together 1 report

   ---    END
   ```
2. 查询MSISDN与区号数据记录，“HLR序列号”为“1”，“MSISDN前缀”为“1380270”：

   ```
   LST ISDNARC: HLRSN=1, ISDNPREFIX="1380270";
   ```

   ```
   %%LST ISDNARC: HLRSN=1, ISDNPREFIX="1380270";%%
   RETCODE = 0 SUCCESS0001:操作成功

           "ISDN Number"    "Area Code"
           1380270          755

   Total count = 1

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**ADD ISDNARC**命令的参数说明。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释   | 原因分析                        | 处理建议                                                                                             |
|:--------|:--------|:----------------------------|:-------------------------------------------------------------------------------------------------|
| ERR3007 | 记录不存在   | “HLR序列号”未定义或者“MSISDN前缀”未定义。 | 根据实际情况，重新输入已定义的“HLR序列号”和“MSISDN前缀”，可通过LST HLRSN命令查询已定义的“HLR序列号”，通过LST ISDNARC命令查询已定义的“MSISDN前缀”。 |