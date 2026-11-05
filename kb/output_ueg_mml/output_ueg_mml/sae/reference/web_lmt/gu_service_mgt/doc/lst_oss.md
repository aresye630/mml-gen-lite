# 查询其他补充业务(LST OSS)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

此操作用来查询用户其他补充业务签约状态。涉及到的补充业务包括：CWAIT、HOLD、MPTY、AOCC、AOCI、ECT、CCBS、CCBSTARGET。

## 注意事项

条件参数IMSI、ISDN必须且只能有一个存在。

## 参数说明

| 参数标识        | 参数名称      | 参数说明                                                                               |
|:------------|:----------|:-----------------------------------------------------------------------------------|
| IMSI        | IMSI      | IMSI号码，E.212格式的编码。 取值范围：6～15位的十进制数字。                                               |
| ISDN        | MSISDN    | MSISDN号码，E.164格式的编码。 取值范围：1～15位的十进制数字。                                             |
| DETAIL      | 是否返回详细信息  | 查询详细信息或者精简信息。 取值范围： TRUE：表示查询详细信息，返回所有补充业务的签约状态。FALSE：表示查询精简信息，只返回签约的补充业务状态。       |
| RECORDCOUNT | 用户个数      | 用户的数目，最大10000个。如果只有一个用户，该参数不必提供。 该参数提供，代表以指定的IMSI、MSISDN为起始号码，号码连续的RECORDCOUNT个用户。 |
| IMSIFILE    | IMSI文件名   | IMSIFILE文件名称，1～16个字母或数字组成。IMSIFILE包含多个不连续的IMSI号码。                                  |
| ISDNFILE    | MSISDN文件名 | ISDNFILE文件名称，1～16个字母或数字组成。ISDNFILE包含多个不连续的MSISDN号码。                                |

## 使用实例

1. 查询IMSI号码为460000009123456的用户的补充业务的详细信息。

   ```
   LST OSS: IMSI="460000009123456", DETAIL=TRUE;
   ```

   ```
   %%LST OSS: IMSI="460000009123456", DETAIL=TRUE;%%
   RETCODE = 0 SUCCESS0001:操作成功

                             IMSI = 460000009123456
                             ISDN = 2013521
                             HOLD = PROV
                             MPTY = PROV
                             AOCC = NOTPROV
                             AOCI = NOTPROV
                              ECT = PROV
                             CCBS = PROV
                       CCBSTARGET = PROV
   CWAIT
                            CWAIT = PROV

   Total count = 10

   There is together 1 report

   ---    END
   ```
2. 查询IMSI号码为460000009123456的用户已经签约的补充业务的精简信息。

   ```
   LST OSS: IMSI="460000009123456", DETAIL=FALSE;
   ```

   ```
   %%LST OSS: IMSI="460000009123456", DETAIL=FALSE;%%
   RETCODE = 0 SUCCESS0001:操作成功

                             IMSI = 460000009123456
                             ISDN = 2013521
                             HOLD = PROV
                             MPTY = PROV
                              ECT = PROV
                             CCBS = PROV
                       CCBSTARGET = PROV
   CWAIT
                            CWAIT = PROV

   Total count = 8

   There is together 1 report

   ---    END
   ```