# 查询MERBT业务(LST MERBT)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

本命令用来查询用户的MERBT业务属性。

## 注意事项

IMSI、ISDN是条件可选参数，有且只能有一个参数出现。

## 参数说明

| 参数标识        | 参数名称      | 参数说明                                                                               |
|:------------|:----------|:-----------------------------------------------------------------------------------|
| IMSI        | IMSI      | IMSI号码，E.212格式的编码，6～15位的十进制数字。                                                     |
| ISDN        | MSISDN    | ISDN号码，E.164格式的编码，为1～15位的十进制数字。                                                    |
| RECORDCOUNT | 用户个数      | 用户的数目，最大10000个。如果只有一个用户，该参数不必提供。 该参数提供，代表以指定的IMSI、MSISDN为起始号码，号码连续的RECORDCOUNT个用户。 |
| IMSIFILE    | IMSI文件名   | IMSI文件名称，1～16个字母或数字组成的字符串。IMSIFILE包含多个不连续的IMSI号码。                                  |
| ISDNFILE    | MSISDN文件名 | MSISDN文件名称，1～16个字母或数字组成的字符串。ISDNFILE包含多个不连续的MSISDN号码。                              |

## 使用实例

查询IMSI号码为460000001234567的用户的MERBT业务属性。

```
LST MERBT: IMSI="460000001234567";
```

```
%%LST MERBT: IMSI="460000001234567";%%
RETCODE = 0 SUCCESS0001:操作成功

                          IMSI = 460000001234567
                          ISDN = 2013521
                         MERBT = PROV

Total count = 3

There is together 1 report

---    END
```