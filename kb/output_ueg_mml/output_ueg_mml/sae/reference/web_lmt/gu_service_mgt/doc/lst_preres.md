# 查询显示/限制属性(LST PRERES)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

用户的显示/限制属性是针对识别显示类补充业务的，识别显示类补充业务有四个：CLIP、CLIR、COLP、COLR。查询用户的显示/限制属性就是查询对CLIR、CLIP、COLP、COLR的属性设置，例如：CLIR的模式类别、COLP或CLIP的超越级别属性是否有效等。

## 注意事项

IMSI、ISDN是条件可选参数，有且只能有一个出现。

## 参数说明

| 参数标识        | 参数名称      | 参数含义                                                                               |
|:------------|:----------|:-----------------------------------------------------------------------------------|
| IMSI        | IMSI      | IMSI号码，E.212格式的编码，为6～15位的十进制数字。                                                    |
| ISDN        | MSISDN    | MSISDN号码，E.164格式的编码，为1～15位的十进制数字。                                                  |
| RECORDCOUNT | 用户个数      | 用户的数目，最大10000个。如果只有一个用户，该参数不必提供。 该参数提供，代表以指定的IMSI、MSISDN为起始号码，号码连续的RECORDCOUNT个用户。 |
| IMSIFILE    | IMSI文件名   | IMSIFILE文件名称，1～16个字母或数字组成。IMSIFILE包含多个不连续的IMSI号码。                                  |
| ISDNFILE    | MSISDN文件名 | ISDNFILE文件名称，1～16个字母或数字组成。ISDNFILE包含多个不连续的MSISDN号码。                                |

## 使用实例

查询IMSI号码为460000009012345的用户的号码识别类业务的显示/限制属性，例如：

```
LST PRERES: IMSI="460000009012345";
```

```
%%LST PRERES: IMSI="460000009012345";%%
RETCODE = 0 SUCCESS0001:操作成功

                          IMSI = 460000009012345
                          ISDN = 2013521
                          CLIP = FALSE
                          CLIR = FALSE
                          COLP = TRUE
                      OVERRIDE = TRUE
                          COLR = FALSE

Total count = 7

There is together 1 report

---    END
```