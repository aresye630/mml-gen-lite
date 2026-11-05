# 查询用户的EPS数据(LST EPS)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询用户的EPS（Evolved Packet System）数据：

- 若需要查询单个用户的EPS业务数据，请输入“IMSI”或“MSISDN”。
- 若需要查询多个连续用户的EPS业务数据，请输入“IMSI”或“MSISDN”与“用户个数”的组合。
- 若需要查询多个不连续用户的EPS业务数据，请输入“IMSI文件名”或“MSISDN文件名”。

## 注意事项

- “IMSI”、“MSISDN”、“IMSI文件名”、“MSISDN文件名”四个参数是可选参数，必须有且只能有一个参数出现。
- “用户个数”不能与“IMSI文件名”或“MSISDN文件名”同时配置。
- 一号多卡单profile场景下，该命令只支持查询主卡用户签约的UE应用类型。

## 参数说明

| 参数标识        | 参数名称      | 参数说明                                   |
|:------------|:----------|:---------------------------------------|
| IMSI        | IMSI      | 用于指示系统需要查询哪个IMSI号码的用户的EPS业务数据。         |
| ISDN        | MSISDN    | 用于指示系统需要查询哪个MSISDN号码的用户的EPS业务数据。       |
| RECORDCOUNT | 用户个数      | 用于指示系统需要查询连续多少个用户的EPS业务数据。             |
| IMSIFILE    | IMSI文件名   | 用于指示系统需要查询哪个IMSI批操作文件中包含的用户的EPS业务数据。   |
| ISDNFILE    | MSISDN文件名 | 用于指示系统需要查询哪个MSISDN批操作文件中包含的用户的EPS业务数据。 |

## 使用实例

1. 查询IMSI号码为“460001480000001”的用户的EPS业务数据：

   ```
   LST EPS: IMSI="460001480000001";
   ```

   ```
   %%LST EPS: IMSI="460001480000001";%%
   RETCODE = 0 SUCCESS0001:Operation is successful
                             IMSI = 460001480000001
                             ISDN = 460001480000001
                              EPS = PROV
                        AMBRMAXUL = 4294967295
                        AMBRMAXDL = 4294967295
                           ANCHOR = FALSE
                           ICSIND = FALSE
                              MPS = FALSE
                         TAUTIMER = 0
                              MDT = NOTGIVEN
                      LTEAUTOPROV = FALSE
                       RELAY_NODE = FALSE
                        EPSODBPOS = NOBPOS
                     LTE_M2M_FLAG = FALSE
                      RAUTAUTIMER = 0
                            WBPTW = 12
                            NBPTW = 12
   Total count = 17
   There is together 1 report
   ---    END
   ```
2. 查询第一个MSISDN号码为“13310911001”的连续3个用户的EPS业务数据：

   ```
   LST EPS: ISDN="13310911001", RECORDCOUNT=3;
   ```

   ```
   %%LST EPS: ISDN="13310911001", RECORDCOUNT=3;%%
   RETCODE = 0 SUCCESS0001:操作成功 批操作ID：7. 使用CHK BATSTAT指令可查看此批操作的执行情况

   There is together 1 report

   ---    END
   ```
3. 查询“MSISDN文件名”为“lsteps.txt”的用户的EPS业务数据：

   ```
   LST EPS: ISDNFILE="lsteps.txt";
   ```

   ```
   %%LST EPS: ISDNFILE="lsteps.txt";%%
   RETCODE = 0 SUCCESS0001:操作成功 批操作ID：268435464. 使用CHK BATSTAT指令可查看此批操作的执行情况

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见

**MOD EPS**

命令的参数说明，表1列出的是未包含在

**MOD EPS**

命令参数说明中的输出项。

| 输出项名称             | 输出项解释                                                                                             |
|:------------------|:--------------------------------------------------------------------------------------------------|
| 批操作ID             | 用于返回批操作的任务号。通过执行CHK BATSTAT命令可以查询该任务的详细信息。                                                        |
| EPSLCKOPTGPRSFLAG | 用于记录用户当前的停复机状态。 TRUE(1)：停机状态FALSE(0)：复机状态 执行LST EPS命令，报文不显示“EPSLCKOPTGPRSFLAG”字段时，表示系统不支持停复机绿通功能。 |

该命令执行异常，会返回对应的错误码。常见错误码如表2所示。

| 错误码     | 错误码解释      | 原因分析                                                                                               | 处理建议                                                                                                                    |
|:--------|:-----------|:---------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------|
| ERR1004 | 无效的参数值     | 可能原因为如下之一：参数“IMSI”的取值不是6～15位十进制数字组成的字符串。参数“MSISDN”的取值不是1～15位十进制数字组成的字符串。                           | 根据实际情况，重新输入“IMSI”或“MSISDN”的取值，确保其取值符合要求。                                                                                |
| ERR1009 | 参数丢失       | “IMSI”、“MSISDN”、“IMSI文件名”、“MSISDN文件名”四个参数一个都没有输入。                                                  | 根据实际情况，重新输入参数，并满足“IMSI”、“MSISDN”、“IMSI文件名”、“MSISDN文件名”四个参数必须有且只能有一个参数出现的条件。                                             |
| ERR1005 | 文件未找到      | “IMSI文件名”或“MSISDN文件名”对应的文件没有通过文件管理功能上传到PGW的指定目录。                                                   | 通过PGW Web LMT的文件上传功能上传预先编写的批操作资源文件到PGW的如下目录：“/opt/pgw/pgwtmpfile/SYSHLRSN+操作员名称”。具体请参见批操作资源文件存放位置。                      |
| ERR1010 | 参数冲突       | 可能原因为如下之一：“IMSI”、“MSISDN”、“IMSI文件名”、“MSISDN文件名”四个参数中有两个以上的参数被输入。“用户个数”与“IMSI文件名”或“MSISDN文件名”同时被输入。 | 根据实际情况，重新输入参数，确保满足以下两点：“IMSI”、“MSISDN”、“IMSI文件名”、“MSISDN文件名”四个参数是可选参数，必须有且只能有一个参数出现。“用户个数”不能与“IMSI文件名”或“MSISDN文件名”同时配置。 |
| ERR3001 | 用户未开户      | 用户的IMSI号码或MSISDN号码输入错误，实际输入的参数“IMSI”或“MSISDN”对应的用户未开户。                                             | 核实用户的IMSI号码或MSISDN号码，如果确定输入无误，证明实际输入的参数“IMSI”或“MSISDN”对应的用户未开户，请先通过ADD SUB命令给用户开户。                                      |
| ERR1025 | 批操作文件中格式非法 | 参数“IMSI文件名”或“MSISDN文件名”对应的批操作文件格式不正确。                                                              | 请根据IMSIFILE文件格式和ISDNFILE文件格式，重新确定对应的批操作文件格式。                                                                            |