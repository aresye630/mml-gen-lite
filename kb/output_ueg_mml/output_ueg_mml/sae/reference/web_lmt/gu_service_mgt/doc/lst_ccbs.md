# 查询CCBS业务（LST CCBS）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

此操作用来查询CCBS业务的签约属性。

## 注意事项

- IMSI、ISDN、IMSIFILE、ISDNFILE是条件可选参数，有且只能有一个参数出现。
- RECORDCOUNT不能与IMSIFILE或ISDNFILE同时存在。

## 参数说明

| 参数标识        | 参数名称      | 参数说明                                                                               |
|:------------|:----------|:-----------------------------------------------------------------------------------|
| IMSI        | IMSI      | IMSI号码，E.212格式的编码。 取值范围：6～15位的十进制数字。                                               |
| ISDN        | MSISDN    | MSISDN号码，E.164格式的编码。 取值范围：1～15位的十进制数字。                                             |
| RECORDCOUNT | 用户个数      | 用户的数目，最大10000个。如果只有一个用户，该参数不必提供。 该参数提供，代表以指定的IMSI、MSISDN为起始号码，号码连续的RECORDCOUNT个用户。 |
| IMSIFILE    | IMSI文件名   | IMSIFILE文件名称，IMSIFILE包含多个不连续的IMSI号码，每个IMSI号码占一行，16个以内的字母或数字组成的字符串。                 |
| ISDNFILE    | MSISDN文件名 | ISDNFILE文件名称，ISDNFILE包含多个不连续的MSISDN号码，每个MSISDN号码占一行。16个以内的字母或数字组成的字符串。             |

## 使用实例

查询IMSI号码为460000009012345的用户的CCBS签约属性。

```
LST CCBS:IMSI="460000009012345";
```

```
%%LST CCBS: IMSI="460000009012345";%%
RETCODE = 0 SUCCESS0001:操作成功

                          IMSI = 460000009012345
                          ISDN = 2013521
                          CCBS = PROV
                    CCBSTARGET = PROV

Total count = 4

There is together 1 report

---    END
```