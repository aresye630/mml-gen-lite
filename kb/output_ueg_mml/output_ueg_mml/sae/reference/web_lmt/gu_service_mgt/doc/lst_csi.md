# 查询CSI业务(LST CSI)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

此操作用来查询用户的CSI参数，只有签约的CSI数据才会在查询结果中显示出来。

## 注意事项

IMSI、ISDN是条件可选参数，任何一个参数出现即可，但两个参数不能同时出现。

## 参数说明

| 参数标识        | 参数名称      | 参数说明                                                                                                                                                                     |
|:------------|:----------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IMSI        | IMSI      | IMSI号码，E.212格式的编码，为6～15位的十进制数字。 可选参数。                                                                                                                                    |
| ISDN        | MSISDN    | MSISDN号码，E.164格式的编码，为1～15位的十进制数字。 可选参数。                                                                                                                                  |
| CSITYPE     | CSI类型     | 该参数表示CSI类型，CSITYPE是可选参数，如果该参数在命令中没有出现，则查询结果会返回用户签约的所有CSI数据。 取值范围： ALLOCSITCSIVTCSIUCSITIFCSIMCSISSCSIGPRSCSIDCSISMSCSIMTSMSCSIIMOCSIIMVTCSI 缺省值：ALL。具体说明请参见“CAMEL业务管理 ”。 |
| RECORDCOUNT | 用户个数      | 用户的数目，最大10000个。如果只有一个用户，该参数不必提供。 该参数提供，代表以指定的IMSI、MSISDN为起始号码，号码连续的RECORDCOUNT个用户。                                                                                       |
| IMSIFILE    | IMSI文件名   | IMSI文件名称，1～16个字母或数字组成。IMSIFILE包含多个不连续的IMSI号码。                                                                                                                            |
| ISDNFILE    | MSISDN文件名 | ISDN文件名称，1～16个字母或数字组成。ISDNFILE包含多个不连续的MSISDN号码。                                                                                                                          |

## 使用实例

查询IMSI号码为460000009123456的用户签约的CSI信息。例如：

```
LST CSI: IMSI="460000009123456";
```

```
%%LST CSI: IMSI="460000009123456";%%
RETCODE = 0 SUCCESS0001:操作成功

                          IMSI = 460000009123456
                          ISDN = 2013521
                        CSITYPE = TIFCSI
                        TIFCSI = PROV
                         STATE = TRUE

Total count = 4

There is together 1 report

---    END
```