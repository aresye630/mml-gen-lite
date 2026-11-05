# 查询COLR业务(LST COLR)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

此操作用来查询COLR（被叫号码识别限制）业务的签约属性。

## 注意事项

IMSI和ISDN是条件可选参数，任何一个参数出现即可，但两个参数不能同时出现。

## 参数说明

| 参数标识        | 参数名称      | 参数说明                                                                               |
|:------------|:----------|:-----------------------------------------------------------------------------------|
| IMSI        | IMSI      | IMSI号码，E.212格式的编码，为6～15位的十进制数字。 可选参数。                                              |
| ISDN        | MSISDN    | MSISDN号码，E.164格式的编码，为1～15位的十进制数字。 可选参数。                                            |
| RECORDCOUNT | 用户个数      | 用户的数目，最大10000个。如果只有一个用户，该参数不必提供。 该参数提供，代表以指定的IMSI、MSISDN为起始号码，号码连续的RECORDCOUNT个用户。 |
| IMSIFILE    | IMSI文件名   | IMSIFILE文件名称，1～16个字母或数字组成。IMSIFILE包含多个不连续的IMSI号码。                                  |
| ISDNFILE    | MSISDN文件名 | ISDNFILE文件名称，1～16个字母或数字组成。ISDNFILE包含多个不连续的MSISDN号码。                                |

## 使用实例

查询IMSI号码为460000009012345的用户的COLR签约属性。例如：

```
LST COLR: IMSI="460000009012345";
```

```
%%LST COLR: IMSI="460000009012345";%%
RETCODE = 0 SUCCESS0001:操作成功

                          IMSI = 460000009012345
                          ISDN = 2013521
                        STATUS = NOTPROV

Total count = 3

There is together 1 report

---    END
```