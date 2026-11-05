# 查询PLMN信息（LST PLMN）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

此操作用来查询PLMN优选漫游配置。

## 注意事项

无。

## 参数说明

| 参数标识   | 参数名称    | 参数说明                                      |
|:-------|:--------|:------------------------------------------|
| HLRSN  | HLR序列号  | HLR序列号，在PGW支持容灾功能或虚拟HLR功能时设置。 取值范围：1～255。 |
| PLMNID | PLMN序列号 | PLMN序列号。 取值范围：0～999。                      |

## 使用实例

查询PLMN优选漫游配置，运营商查询HLR序列号为1，PLMN序列号为0的网络的优选漫游配置:

```
LST PLMN: HLRSN=1, PLMNID=0;
```

```
%%LST PLMN: HLRSN=1, PLMNID=0;%%
RETCODE = 0 SUCCESS0001:Operation is successful

                         HLRSN = 1
                        PLMNID = 0
                 PREFERREDTYPE = PREFERRED
                     CHECKIMSI = TRUE
                   DEFIMSIRULE = PERMISSION

      "VLRSGSNNO"
      8613780

      "IMSIPREFIX"      "IMSIRULE"
      460141            RESTRICT

Total count = 7

There is together 1 report

---    END
```