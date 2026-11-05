# 查询增强路由(LST ROUTECATEGORY)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

本命令用于查询用户的增强路由业务。

## 注意事项

IMSI、ISDN是条件可选参数，二者不能同时定义。

## 参数说明

| 参数标识        | 参数名称      | 参数说明                                                                              |
|:------------|:----------|:----------------------------------------------------------------------------------|
| IMSI        | IMSI      | IMSI号码，E.212格式的编码，6～15位的十进制数字。                                                    |
| ISDN        | MSISDN    | ISDN号码，E.164格式的编码，为1～15位的十进制数字。                                                   |
| RECORDCOUNT | 用户个数      | 用户的数目，最大10000个。如果只有一个用户，该参数不必提供。该参数提供，代表以指定的IMSI、MSISDN为起始号码，号码连续的RECORDCOUNT个用户。 |
| IMSIFILE    | IMSI文件名   | IMSI文件名称，IMSIFILE包含多个不连续的IMSI号码，每个IMSI号码占一行，16个以内的字母或数字组成的字符串。                    |
| ISDNFILE    | MSISDN文件名 | MSISDN文件名称，ISDNFILE包含多个不连续的MSISDN号码，每个MSISDN号码占一行。16个以内的字母或数字组成的字符串。              |

## 使用实例

查询IMSI号码为460100008001001的用户的增强路由业务。

```
LST ROUTECATEGORY: IMSI="460100008001001";
```

```
%%LST ROUTECATEGORY: IMSI="460100008001001";%%
RETCODE = 0 SUCCESS0001:操作成功

                          IMSI = 460100008001001
                          ISDN = 2013521
                 ROUTECATEGORY = 2

Total count = 3

There is together 1 report

---    END
```