# 查询NON-3GPP用户属性(LST NONSUB)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

此命令用来查询NON-3GPP用户的属性数据。

## 注意事项

IMSI、ISDN是条件可选参数，任何一个参数出现即可，但两个参数不能同时出现。

## 参数说明

| 参数标识        | 参数名称      | 参数说明                                                                                    |
|:------------|:----------|:----------------------------------------------------------------------------------------|
| IMSI        | IMSI      | 此参数用于设置IMSI号码。 取值范围：E.212格式的编码，6～15位的十进制数字。                                             |
| ISDN        | MSISDN    | 此参数用于设置MSISDN号码。 取值范围：E.164格式的编码，1～15位的十进制数字。                                           |
| RECORDCOUNT | 用户个数      | 用户的数目。如果只有一个用户，该参数不必提供。 该参数提供，代表以指定的IMSI、MSISDN为起始号码，号码连续的RECORDCOUNT个用户。 取值范围：1～10000。 |
| IMSIFILE    | IMSI文件名   | 此参数用于设置IMSI文件名称。IMSIFILE是由多个不连续的IMSI号码组成的批操作文件，每个IMSI号码占一行。 取值范围：1～16个字母或数字。            |
| ISDNFILE    | MSISDN文件名 | 此参数用于设置ISDN文件名称。ISDNFILE是由多个不连续的MSISDN号码组成的批操作文件，每个MSISDN号码占一行。 取值范围：1～16个字母或数字。        |

## 使用实例

1. 查询IMSI号码为“460000009012345”的用户的NON-3GPP属性信息：

   ```
   LST NONSUB: IMSI="460000009012345";
   ```

   ```
   %%LST NONSUB: IMSI="460000009012345";%%
   RETCODE = 0 SUCCESS0001:操作成功

                             IMSI = 460000009012345
                             ISDN = 460000009012345
                      NON3GPPSUPP = TRUE
                   WLANNOTALLOWED = TRUE
            CDMA2000_1XNOTALLOWED = TRUE
                   HRPDNOTALLOWED = TRUE
                    UMBNOTALLOWED = TRUE
                  EHRPDNOTALLOWED = TRUE
                       MIP6FEAVEC = MIP6_INTEGRATED
                       VOWIFI_TAG = VoWIFI

   Total count = 10

   There is together 1 report

   ---    END
   ```
2. 查询第一个MSISDN号码为“460000009012345”的连续3个用户的NON-3GPP属性信息：

   ```
   LST NONSUB: ISDN="460000009012345", RECORDCOUNT=3;
   ```

   ```
   %%LST NONSUB: ISDN="460000009012345", RECORDCOUNT=3;%%
   RETCODE = 0 SUCCESS0001:操作成功 批操作ID：1. 使用CHK BATSTAT指令可查看此批操作的执行情况

   There is together 1 report

   ---    END
   ```
3. 查询“MSISDN文件名”为“lstnonsub.txt”的用户的NON-3GPP属性信息：

   ```
   LST NONSUB: ISDNFILE="lstnonsub.txt";
   ```

   ```
   %%LST NONSUB: ISDNFILE="lstnonsub.txt";%%
   RETCODE = 0 SUCCESS0001:操作成功 批操作ID：3432333. 使用CHK BATSTAT指令可查看此批操作的执行情况

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见

**MOD NONSUB**

命令的参数说明，表1列出的是未包含在

**MOD NONSUB**

命令参数说明中的输出项。

| 输出项名称   | 输出项解释                                      |
|:--------|:-------------------------------------------|
| 批操作ID   | 用于返回批操作的任务号。通过执行CHK BATSTAT命令可以查询该任务的详细信息。 |

该命令执行异常，会返回对应的错误码。常见错误码如表2所示。

| 错误码     | 错误码解释      | 原因分析                                                                                               | 处理建议                                                                                                                    |
|:--------|:-----------|:---------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------|
| ERR1004 | 无效的参数值     | 可能原因为如下之一：参数“IMSI”的取值不是6～15位十进制数字组成的字符串。参数“MSISDN”的取值不是1～15位十进制数字组成的字符串。                           | 根据实际情况，重新输入“IMSI”或“MSISDN”的取值，确保其取值符合要求。                                                                                |
| ERR1009 | 参数丢失       | “IMSI”、“MSISDN”、“IMSI文件名”、“MSISDN文件名”四个参数一个都没有输入。                                                  | 根据实际情况，重新输入参数，并满足“IMSI”、“MSISDN”、“IMSI文件名”、“MSISDN文件名”四个参数必须有且只能有一个参数出现的条件。                                             |
| ERR1005 | 文件未找到      | “IMSI文件名”或“MSISDN文件名”对应的文件没有通过文件管理功能上传到PGW的指定目录。                                                   | 通过PGW Web LMT的文件上传功能上传预先编写的批操作资源文件到PGW的如下目录：“/opt/pgw/pgwtmpfile/SYSHLRSN+操作员名称”。具体请参见批操作资源文件存放位置。                      |
| ERR1010 | 参数冲突       | 可能原因为如下之一：“IMSI”、“MSISDN”、“IMSI文件名”、“MSISDN文件名”四个参数中有两个以上的参数被输入。“用户个数”与“IMSI文件名”或“MSISDN文件名”同时被输入。 | 根据实际情况，重新输入参数，确保满足以下两点：“IMSI”、“MSISDN”、“IMSI文件名”、“MSISDN文件名”四个参数是可选参数，必须有且只能有一个参数出现。“用户个数”不能与“IMSI文件名”或“MSISDN文件名”同时配置。 |
| ERR1025 | 批操作文件中格式非法 | 参数“IMSI文件名”或“MSISDN文件名”对应的批操作文件格式不正确。                                                              | 请根据IMSIFILE文件格式和ISDNFILE文件格式，重新确定对应的批操作文件格式。                                                                            |
| ERR3001 | 用户未开户      | 用户的IMSI号码或MSISDN号码输入错误，实际输入的参数“IMSI”或“MSISDN”对应的用户未开户。                                             | 请参考本命令中的使用实例给用户开户。                                                                                                      |