# 查询全局软参(LST FUNCCONF)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询全局软参数据的配置信息。

## 注意事项

无。

## 参数说明

无。

## 使用实例

查询全局软参数据：

```
LST FUNCCONF:;
```

```
%%LST FUNCCONF:;%%
RETCODE = 0 SUCCESS0001:操作成功

                       LOCFUNC = NPHLR
                  SRI4SM_ROUTE = IndirectQuery
                 SUPP_ROUTLOOP = FALSE
                    ROAMNATION = RoamingNation_Normal
                     FAKE_IMSI = 460030913121002

Total count = 5

There is together 1 report

---    END
```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**SET FUNCCONF**命令的参数说明。