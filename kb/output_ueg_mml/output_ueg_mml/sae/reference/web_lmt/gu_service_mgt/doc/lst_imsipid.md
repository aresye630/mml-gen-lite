# 查询IMSI与云分区数据(LST IMSIPID)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

此命令用于查询IMSI号段与云分区的映射关系。

## 注意事项

无。

## 参数说明

| 参数标识     | 参数名称   | 参数说明                                                |
|:---------|:-------|:----------------------------------------------------|
| IMSIPRFX | IMSI前缀 | 与云分区建立映射关系的IMSI号段。 取值范围：1～15位的十进制数字组成的字符串。 说明：可选参数。 |

## 使用实例

查询IMSI号段为460123的相关数据，命令如下：

```
LST IMSIPID: IMSIPRFX="460123";
```

```
%%LST IMSIPID: IMSIPRFX="460123";%%
RETCODE = 0 SUCCESS0001:Operation is successful

          "IMSIPRFX"         "Partition ID"
          460123            1

Total count = 1

There is together 1 report

---    END
```

## 输出结果说明

输出项的详细说明请参见ADD IMSIPID命令的参数说明。