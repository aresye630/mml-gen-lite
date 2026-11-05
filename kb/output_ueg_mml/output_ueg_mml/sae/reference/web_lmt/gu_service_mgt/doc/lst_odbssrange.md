# 查询补充业务限制号段(LST ODBSSRANGE)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

此操作用于查询补充业务限制号段表。

## 注意事项

无。

## 参数说明

无。

## 使用实例

查询补充业务限制号段表，命令如下：

LST ODBSSRANGE:;

```
%%LST ODBSSRANGE:;%%
RETCODE = 0 SUCCESS0001:操作成功

        "BEGIN RANGE"                  "END RANGE"
        460000000000001                460000000000009

Total count = 1

There is together 1 report

---    END
```