# 查询默认K2(LST DEFAULTK2SNO)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询密钥加密的默认K2密钥的索引数据。

## 注意事项

无。

## 参数说明

无。

## 使用实例

查询密钥加密的默认K2密钥的索引数据：

```
LST DEFAULTK2SNO:;
```

```
%%LST DEFAULTK2SNO:;%%
RETCODE = 0 SUCCESS0001:操作成功

TYPE                  HLRSN                 K2SNO
K2                    174                   0
K2                    190                   0
K2                    221                   0
K2                    246                   0
HK2                                         22
GK2                                         1

Total count = 6

There is together 1 report

---    END
```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**SET DEFAULTK2SNO**命令的参数说明。