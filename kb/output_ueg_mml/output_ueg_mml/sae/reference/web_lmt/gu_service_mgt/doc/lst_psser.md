# 查询PS业务(LST PSSER)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

该命令用于查询用户的PS业务数据。

## 注意事项

- “IMSI”、“MSISDN”、“IMSI文件名”、“MSISDN文件名”四个参数是可选参数，必须有且只能有一个参数出现。
- “用户个数”不能与“IMSI文件名”或“MSISDN文件名”同时配置。

## 参数说明

| 参数标识        | 参数名称      | 参数说明                                                                                                                                                                                                                          |
|:------------|:----------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IMSI        | IMSI      | 用于标识要查询哪个IMSI号码对应的PS业务数据。                                                                                                                                                                                                     |
| ISDN        | MSISDN    | 用于标识要查询哪个MSISDN号码对应的PS业务数据。                                                                                                                                                                                                   |
| RECORDCOUNT | 用户个数      | 用于标识需要查询的签约PS业务的用户数目。 当需要查询连续多个号码的签约PS业务的用户时配置该参数，配置后，系统将会从已指定的IMSI号码或MSISDN号码开始，查询签约PS业务的连续多个号码的用户。 取值范围：1～10000 默认值：无。 说明： 该参数是查询签约PS业务的连续号码的多个用户，当只有一个用户时，该参数不必配置。 当一次设置的用户个数很多时，对系统性能无影响，但设置的用户个数越多，消耗的时间越长，一般从几分钟到几小时不等。 |
| IMSIFILE    | IMSI文件名   | 用于标识IMSI批操作文件。 IMSI批操作文件包含多个不连续的需要查询的用户的IMSI号码，为文本编辑器编辑的文本文件（编码格式为ANSI），如“lstpsser.txt”，通过文件管理功能上传到指定目录，具体请参见批操作资源文件存放位置。文件格式请参见IMSIFILE文件格式。 取值范围：1～16位字母或数字组成的字符串。                                                          |
| ISDNFILE    | MSISDN文件名 | 用于标识MSISDN批操作文件。 MSISDN批操作文件包含多个不连续的需要查询的用户的MSISDN号码，为文本编辑器编辑的文本文件（编码格式为ANSI），如“lstpsser.txt”，通过文件管理功能上传到指定目录，具体请参见批操作资源文件存放位置。文件格式请参见ISDNFILE文件格式。 取值范围：1～16位字母或数字组成的字符串。                                                    |
| DETAIL      | 是否返回详细信息  | 用于标识系统是否返回查询的详细信息： 取值范围： TRUE：显示用户详细信息，查询结果包括IMSI、ISDN、PDP地址信息，APN、以及完整的QOS参数。FALSE：显示用户精简信息，查询结果包含IMSI、ISDN、CNTXID、APNQOSTPLID、PDP地址信息。 默认值：FALSE。                                                                           |

## 使用实例

1. 查询IMSI号码为“460000009123456”的用户的PS数据，且不返回详细信息：

   ```
   LST PSSER: IMSI="460000009123456", DETAIL=FALSE;
   ```

   ```
   %%LST PSSER: IMSI="460000009123456", DETAIL=FALSE;%%
   RETCODE = 0 SUCCESS0001:操作成功

                             IMSI = 460000009123456
                             ISDN = 460000009012389
                           CNTXID = 1
                      APNQOSTPLID = 1
                      OTHERADDIND = DYNAMIC ADDRESS
                           CNTXID = 2
                      APNQOSTPLID = 2
                      OTHERADDIND = DYNAMIC ADDRESS
                           CNTXID = 3
                      APNQOSTPLID = 3
                      OTHERADDIND = DYNAMIC ADDRESS

   Total count = 11

   There is together 1 report

   ---    END
   ```
2. 查询MSISDN号码为“460000009123456”的用户PS数据，且返回详细信息：

   ```
   LST PSSER: IMSI="460000009123456", DETAIL=TRUE;
   ```

   ```
   %%LST PSSER: IMSI="460000009123456", DETAIL=TRUE;%%
   RETCODE = 0 SUCCESS0001:操作成功

                             IMSI = 460000009123456
                             ISDN = 460000009012389
                           CNTXID = 1
                      OTHERADDIND = DYNAMIC ADDRESS
                           RELCLS = ACKALLPRODT
                         DELAYCLS = DELAY1
                           PRECLS = HIGH
                          PEAKTHR = 32,000 OCT
                          MEANTHR = 10,000 OCT
                              APN = APN1
                           CNTXID = 2
                      OTHERADDIND = DYNAMIC ADDRESS
                           RELCLS = ACKALLPRODT
                         DELAYCLS = DELAY1
                           PRECLS = HIGH
                          PEAKTHR = 32,000 OCT
                          MEANTHR = 10,000 OCT
                              APN = APN2
                           CNTXID = 3
                      OTHERADDIND = DYNAMIC ADDRESS
                           RELCLS = ACKALLPRODT
                         DELAYCLS = DELAY1
                           PRECLS = HIGH
                          PEAKTHR = 32,000 OCT
                          MEANTHR = 10,000 OCT
                              APN = APN3

   Total count = 26

   There is together 1 report

   ---    END
   ```