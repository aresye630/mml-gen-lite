# 查询用户签约的私有短信业务(LST NSMSIN)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

该操作用于查询用户签约的私有短信业务。

## 注意事项

- IMSI、ISDN、IMSIFILE、ISDNFILE是条件可选参数，有且只能有一个参数出现。
- RECORDCOUNT一定不能与IMSIFILE或ISDNFILE同时出现。

## 参数说明

| 参数标识        | 参数名称      | 参数说明                                                                               |
|:------------|:----------|:-----------------------------------------------------------------------------------|
| IMSI        | IMSI      | IMSI号码，E.212格式的编码，为6～15位的十进制数字。                                                    |
| ISDN        | MSISDN    | MSISDN号码，E.164格式的编码，为1～15位的十进制数字。                                                  |
| RECORDCOUNT | 用户个数      | 用户的数目，最大10000个。如果只有一个用户，该参数不必提供。 该参数提供，代表以指定的IMSI、MSISDN为起始号码，号码连续的RECORDCOUNT个用户。 |
| IMSIFILE    | IMSI文件名   | IMSI文件名称，1～16个字母或数字组成。IMSIFILE是由多个不连续的IMSI号码组成的批操作文件，每个IMSI号码占一行。                  |
| ISDNFILE    | MSISDN文件名 | ISDN文件名称，1～16个字母或数字组成。ISDNFILE是由多个不连续的MSISDN号码组成的批操作文件，每个MSISDN号码占一行。              |

## 使用实例

查询IMSI号码为460000009123456的私有短信业务。命令如下：

```
LST NSMSIN: IMSI="460000009123456";
```

```
%%LST NSMSIN: IMSI="460000009123456";%%
RETCODE = 0 SUCCESS0001:操作成功

                          IMSI = 460000009123456
                        MSISDN = 2013521
                        SCPADD = 8613911111
                          SKEY = 1
                            DP = MO
                          TAMM = TRUE
                        STATUS = ACT

Total count = 7

There is together 1 report

---    END
```