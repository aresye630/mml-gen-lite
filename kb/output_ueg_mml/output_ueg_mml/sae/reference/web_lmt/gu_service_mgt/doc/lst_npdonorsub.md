# 查询本网携出用户(LST NPDONORSUB)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

此操作用于查询携出用户数据。

## 注意事项

IMSI、ISDN是条件可选参数，此操作中，有且只能有一个参数出现。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                             |
|:-------|:-------|:---------------------------------|
| IMSI   | IMSI   | IMSI号码，E.212格式的编码，为6～15位的十进制数字。  |
| ISDN   | MSISDN | MSISDN号码，E.164格式的编码，1～15位的十进制数字。 |

## 使用实例

查询IMSI号码为4601075003001的携出用户数据。命令如下：

```
LST NPDONORSUB: IMSI="4601075003001";
```

```
%%LST NPDONORSUB: IMSI="4601075003001";%%
RETCODE = 0 SUCCESS0001:Operation is successful

                          IMSI = 4601075003001
                          ISDN = 86131075003001
                            RN = 1112
                        HLRNUM = <NULL>

Total count = 4

There is together 1 report

---    END
```