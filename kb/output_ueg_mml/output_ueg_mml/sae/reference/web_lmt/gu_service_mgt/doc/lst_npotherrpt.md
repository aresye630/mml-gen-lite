# 查询它网携转用户数据(LST NPOTHERRPT)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

此操作用于查询它网携转用户数据。

## 注意事项

无。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                     |
|:-------|:-------|:-----------------------------------------|
| ISDN   | MSISDN | MSISDN号码，E.164格式的编码，1～15位的十进制数字。 说明：必选参数 |

## 使用实例

查询MSISDN号码为86131075003001的它网携转用户数据。命令如下：

```
LST NPOTHERRPT: ISDN="86131075003001";
```

```
%%LST NPOTHERRPT: ISDN="86131075003001";%%
RETCODE = 0 SUCCESS0001:Operation is successful

                          ISDN = 86131075003001
                            RN = 1112
Total count = 2

There is together 1 report

---    END
```