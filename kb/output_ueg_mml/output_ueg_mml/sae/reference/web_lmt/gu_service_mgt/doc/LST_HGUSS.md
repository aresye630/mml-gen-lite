# 查询GUSS数据(LST HGUSS)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该操作用于在HSS的业务数据库中查询指定IMPI的GUSS数据。

## 注意事项

无。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                              |
|:-------|:-------|:--------------------------------------------------------------------------------------------------|
| IMPI   | IMPI   | 标识一条IMPI的GUSS数据记录的关键参数，用于指定需要查询哪个IMPI的GUSS数据记录。要求输入的IMPI值符合NAI格式，字母区分大小写。 取值范围：长度不超过127的字符串 默认值：无 |

## 使用实例

查询GUSS数据,“IMPI”为“impiinfo”：

```
LST HGUSS: IMPI="impiinfo";
```

```
%%LST HGUSS: IMPI="impiinfo";%%
RETCODE = 0 操作成功

GSID   GAAAUTHFLAG    NAFGROUP    UICCTYPE    KEYCHOICE         TIMESTAMP   LIFETIME
4                     nafgroup    GBA         ME-based-key      123456789   86400
3                                       
2                                       
0                                       
1      1                   

Total count = 5

There is together 1 report

---    END
```

## 输出结果说明

请参见**ADD HGUSS**命令的参数说明。