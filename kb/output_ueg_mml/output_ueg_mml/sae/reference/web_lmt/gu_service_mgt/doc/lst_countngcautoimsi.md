# 查询5G自动开户用户粒度黑白名单数量(LST COUNTNGCAUTOIMSI)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询5G自动开户用户粒度的黑白名单数量。

## 注意事项

无。

## 参数说明

无。

## 使用实例

查询5G自动开户用户粒度的黑白名单数量。

```
LST COUNTNGCAUTOIMSI: ;
```

```
%%LST COUNTNGCAUTOIMSI:;%%
RETCODE = 0 操作成功

            COUNTNGCAUTOIMSI = 1000

Total count = 1

There is together 1 report

---    END
```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，参数含义请参见表1。

| 输出项名称            | 输出项解释                 |
|:-----------------|:----------------------|
| COUNTNGCAUTOIMSI | 当前5G自动开户用户粒度的黑白名单的数量。 |