# 查询本局数据(LST INTROFF)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询本局数据的配置信息。

## 注意事项

无。

## 参数说明

无。

## 使用实例

查询本局数据：

```
LST INTROFF:;
```

```
%%LST INTROFF:;%%
RETCODE = 0 SUCCESS0001:操作成功

              Local HLR Number = 8613901000

      Function ID of Local HLR = <NULL>
                  Country Code = 86
                            RN = <NULL>

Total count = 4

There is together 1 report

---    END
```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**SET INTROFF**命令的参数说明。