# 查询K2(LST K2)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询HSS/HLR中所有的K2配置信息。

## 注意事项

查询结果中“算法类型”显示为“NONE”、“HSM密钥索引”不为空时，表示K2为HSM类型；“算法类型”不为“NONE”，表示K2保存在本地。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                     |
|:-------|:-------|:-------------------------|
| HLRSN  | HLR序列号 | 用于标识系统按照哪个HLR序列号来查询K2数据。 |

## 使用实例

查询K2数据，“HLR序列号”为“1”：

```
LST K2: HLRSN=1;
```

```
%%LST K2: HLRSN=1;%%
RETCODE = 0 SUCCESS0001:操作成功

        "HLRSN"       "K2SNO"       "K7SNO"       "KEYNAME"       "ALGTYPE"        "HSMKEYINDEX"
        1             1             NONE                            AES128
        1             2             2                               AES128

Total count = 2

There is together 1 report

---    END
```

## 输出结果说明

请参见**ADD K2**命令的参数说明。