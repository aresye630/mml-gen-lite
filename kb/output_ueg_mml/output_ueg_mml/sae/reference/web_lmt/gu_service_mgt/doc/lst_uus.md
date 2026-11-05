# 查询UUS业务(LST UUS)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

操作员通过此命令可以查询用户UUS业务的设置。

## 注意事项

IMSI、ISDN是条件可选参数，此操作中，有且只能有一个参数出现。

## 参数说明

| 参数标识        | 参数名称      | 参数说明                                                                               |
|:------------|:----------|:-----------------------------------------------------------------------------------|
| IMSI        | IMSI      | IMSI号码， E.212格式的编码，6～15位的十进制数字。                                                    |
| ISDN        | MSISDN    | MSISDN号码，E.164格式的编码，1～15位的十进制数字。                                                   |
| RECORDCOUNT | 用户个数      | 用户的数目，最大10000个。如果只有一个用户，该参数不必提供。 该参数提供，代表以指定的IMSI、MSISDN为起始号码，号码连续的RECORDCOUNT个用户。 |
| IMSIFILE    | IMSI文件名   | IMSI文件名称，1～16个字母或数字组成。IMSIFILE包含多个不连续的IMSI号码。                                      |
| ISDNFILE    | MSISDN文件名 | ISDN文件名称，1～16个字母或数字组成。ISDNFILE包含多个不连续的MSISDN号码。                                    |

## 使用实例

查询IMSI号码为460000009123456的用户的UUS业务签约属性。

```
LST UUS: IMSI="460000009123456";
```

```
%%LST UUS: IMSI="460000009123456";%%
RETCODE = 0 SUCCESS0001:操作成功

                          IMSI = 460000009123456
                          ISDN = 2013521
                          UUS1 = PROV
                          UUS2 = NOTPROV
                          UUS3 = NOTPROV

Total count = 5

There is together 1 report

---    END
```