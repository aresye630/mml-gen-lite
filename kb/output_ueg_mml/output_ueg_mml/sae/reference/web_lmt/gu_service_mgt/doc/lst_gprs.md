# 查询GPRS业务(LST GPRS)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

此命令用于为用户查询GPRS参数。

## 注意事项

- “IMSI”、“MSISDN”、“IMSI文件名”、“MSISDN文件名”四个参数是可选参数，必须有且只能有一个参数出现。
- “用户个数”不能与“IMSI文件名”或“MSISDN文件名”同时配置。

## 参数说明

| 参数标识        | 参数名称      | 参数说明                                                                               |
|:------------|:----------|:-----------------------------------------------------------------------------------|
| IMSI        | IMSI      | IMSI号码，E.212格式的编码，为6～15位的十进制数字。                                                    |
| ISDN        | MSISDN    | MSISDN号码，E.164格式的编码，为1～15位的十进制数字。                                                  |
| RECORDCOUNT | 用户个数      | 用户的数目，最大10000个。如果只有一个用户，该参数不必提供。 该参数提供，代表以指定的IMSI、MSISDN为起始号码，号码连续的RECORDCOUNT个用户。 |
| IMSIFILE    | IMSI文件名   | IMSI文件名称，1～16个字母或数字组成。IMSIFILE包含多个不连续的IMSI号码。                                      |
| ISDNFILE    | MSISDN文件名 | ISDN文件名称，1～16个字母或数字组成。ISDNFILE包含多个不连续的MSISDN号码。                                    |

## 使用实例

查询IMSI号码为460000009123456用户的GPRS业务。执行命令如下：

```
LST GPRS: IMSI="460000009123456";
```

```
%%LST GPRS: IMSI="460000009123456";%%
RETCODE = 0 SUCCESS0001:操作成功

                          IMSI = 460000009123456
                          ISDN = 2013521
                 CHARGE_GLOBAL = NONE
                        CNTXID = 2
                       PDPTYPE = IPV4
                        ADDIND = DYNAMIC ADDRESS
                        RELCLS = ACKALLPRODT
                      DELAYCLS = DELAY2
                        PRECLS = NORMAL
                       PEAKTHR = 8,000 OCT
                       MEANTHR = 200 OCT
                    ARPRIORITY = NORMAL
                        ERRSDU = NODETECT
                      DELIVERY = NO
                    TRAFFICCLS = CONVER
                    MAXSDUSIZE = 10 OCT
                      MAXBRUPL = 1K
                      MAXBRDWL = 1K
                        RESBER = 0.05
                        SDUERR = 0.01
                   TRANSFERDEL = 10MS
                    TRAFFICPRI = PRIORITY1
                     MAXGBRUPL = 1K
                     MAXGBRDWL = 1K
                           APN = APN1
                         VPLMN = TRUE
                        CHARGE = PREPAID
                 SIGNALLINGIND = YES

Total count = 28

There is together 1 report

---    END
```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。各参数含义请见**MOD GPRS**命令。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释      | 原因分析                                                                                                                 | 处理建议                                                                                                                    |
|:--------|:-----------|:---------------------------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------|
| ERR1004 | 无效的参数值     | 可能原因为如下之一：参数“IMSI”的取值不是6～15位十进制数字组成的字符串。参数“MSISDN”的取值不是1～15位十进制数字组成的字符串。                                             | 根据实际情况，重新输入“IMSI”或“MSISDN”的取值，确保其取值符合要求。                                                                                |
| ERR1005 | 文件未找到      | “IMSI文件名”或“MSISDN文件名”对应的文件没有通过文件管理功能上传到PGW的指定目录。                                                                     | 通过PGW Web LMT的文件上传功能上传预先编写的批操作资源文件到PGW的如下目录：“/opt/pgw/pgwtmpfile/SYSHLRSN+操作员名称”。具体请参见批操作资源文件存放位置。                      |
| ERR1009 | 参数丢失       | “IMSI”、“MSISDN”、“IMSI文件名”、“MSISDN文件名”四个参数一个都没有输入。                                                                    | 根据实际情况，重新输入参数，并满足“IMSI”、“MSISDN”、“IMSI文件名”、“MSISDN文件名”四个参数必须有且只能有一个参数出现的条件。                                             |
| ERR1010 | 参数冲突       | 可能原因为如下之一：“IMSI”、“MSISDN”、“IMSI文件名”、“MSISDN文件名”四个参数中有两个以上的参数被输入。“用户个数”与“IMSI文件名”或“MSISDN文件名”同时被输入。                   | 根据实际情况，重新输入参数，确保满足以下两点：“IMSI”、“MSISDN”、“IMSI文件名”、“MSISDN文件名”四个参数是可选参数，必须有且只能有一个参数出现。“用户个数”不能与“IMSI文件名”或“MSISDN文件名”同时配置。 |
| ERR1025 | 批操作文件中格式非法 | 参数“IMSI文件名”或“MSISDN文件名”对应的批操作文件格式不正确。                                                                                | 请根据IMSIFILE文件格式和ISDNFILE文件格式，重新确定对应的批操作文件格式。                                                                            |
| ERR3001 | 用户未开户      | 用户的IMSI号码或MSISDN号码输入错误，实际输入的参数“IMSI”或“MSISDN”对应的用户未开户。                                                               | 核实用户的IMSI号码或MSISDN号码，如果确定输入无误，证明实际输入的参数“IMSI”或“MSISDN”对应的用户未开户，请先通过ADD SUB命令给用户开户。                                      |
| ERR3111 | 系统不支持该特性   | 该命令不支持GPRS优化管理或者PS/EPS独立模板管理，即仅当SET MAPSERV命令中“GPRS管理方式”取值为“NotSupportGPRSManager” 或“SupportGPRSManager”时，该命令才能执行成功。 | 联系华为技术支持，确认当前局点软参“GPRS管理方式”是否设置正确、当前局点使用的GPRS管理方式是否正确。详情见“GPRS管理方式”软参描述。                                                |