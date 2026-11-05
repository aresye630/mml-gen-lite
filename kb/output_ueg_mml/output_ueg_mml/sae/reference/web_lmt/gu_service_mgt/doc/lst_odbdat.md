# 查询ODB数据(LST ODBDAT)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

通过查询ODB参数，可以得到运营商给该用户设置的ODB业务。

## 注意事项

IMSI和ISDN是条件可选参数，任何一个参数出现即可，但两个参数不能同时出现。

## 参数说明

| 参数标识        | 参数名称      | 参数说明                                                                               |
|:------------|:----------|:-----------------------------------------------------------------------------------|
| IMSI        | IMSI      | IMSI号码，E.212格式的编码，为6～15位的十进制数字。                                                    |
| ISDN        | MSISDN    | MSISDN号码，E.164格式的编码，为1～15位的十进制数字。                                                  |
| RECORDCOUNT | 用户个数      | 用户的数目，最大10000个。如果只有一个用户，该参数不必提供。 该参数提供，代表以指定的IMSI、MSISDN为起始号码，号码连续的RECORDCOUNT个用户。 |
| IMSIFILE    | IMSI文件名   | IMSI文件名称，1～16个字母或数字组成。IMSIFILE包含多个不连续的IMSI号码。                                      |
| ISDNFILE    | MSISDN文件名 | MSISDN文件名称，1～16个字母或数字组成。ISDNFILE包含多个不连续的MSISDN号码。                                  |

## 使用实例

查询IMSI号码为460000009123456的用户的ODB业务参数设置。命令如下：

```
LST ODBDAT: IMSI="460000009123456";
```

```
%%LST ODBDAT: IMSI="460000009123456";%%
RETCODE = 0 SUCCESS0001:操作成功

                          IMSI = 460000009123456
                          ISDN = 460000009123456
                         ODBSS = FALSE
                         ODBIC = NOBIC
                         ODBOC = NOBOC
                        ODBPB1 = FALSE
                        ODBPB2 = FALSE
                        ODBPB3 = FALSE
                        ODBPB4 = FALSE
                       ODBENTE = FALSE
                       ODBINFO = FALSE
                       ODBROAM = NOBAR
                        ODBRCF = NOBRCF
                        ODBECT = NOBECT
                       ODBDECT = FALSE
                       ODBMECT = FALSE
                        ODBPOS = NOBPOS
                    ODBPOSTYPE = BOTH
                   ODBENTEROAM = FALSE
                   ODBINFOROAM = FALSE
                BROLOCDOMEGPRS = FALSE
          BROCROSSDOMESTICGPRS = FALSE
               BROLOCINTERGPRS = FALSE
             BROCROSSINTERGPRS = FALSE

Total count = 24

There is together 1 report

---    END
```