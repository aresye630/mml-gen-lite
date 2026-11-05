# 查询K7(LST K7)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询所有K7密钥的序列号。

## 注意事项

无。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                     |
|:-------|:-------|:-------------------------|
| HLRSN  | HLR序列号 | 用于标识系统按照哪个HLR序列号来查询K7数据。 |

## 使用实例

在HSS/HLR中查询“HLR序列号”为“1”的K7信息：

```
LST K7: HLRSN=1;
```

```
%%LST K7: HLRSN=1;%%
RETCODE = 0 SUCCESS0001:操作成功

        "HLRSN"       "K7SNO"       "STATE"       "PKEYSNO"     "KEYNAME"               "K7HASH"                 "MBKSLOTNO"    "ALGTYPE"

        1             1             EXIST         0                                                                               AES128                                                   
        1             2             EXIST         0                                                                               AES128                                                   
        1             3             LOSE          0                                                                               AES256                                                   
        1             4             LOSE          0                                                                               AES128                                                   
        1             5             LOSE          0                                                                               AES128                                                   

Total count = 5

There is together 1 report

---    END
```

## 输出结果说明

请参见**ADD K7**命令的参数说明。表1列出的是未包含在**ADD K7**命令参数说明中的输出项。

| 输出项名称   | 输出项解释                                                                                |
|:--------|:-------------------------------------------------------------------------------------|
| STATE   | 用于标识当前K7数据状态。 “STATE”为“EXIST”说明数据正常。 “STATE”为“LOSE”说明数据丢失，此时需要通过ADD K7命令再次添加丢失的K7密钥。 |