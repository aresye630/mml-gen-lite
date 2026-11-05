# 查询增强VLR/SGSN漫游限制(LST ERR)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

此操作用于查询HLR的增强用户VLR/SGSN漫游限制状态。

## 注意事项

无。

## 参数说明

| 参数标识      | 参数名称         | 参数说明                                     |
|:----------|:-------------|:-----------------------------------------|
| HLRSN     | HLR序列号       | HLR序列号，取值范围为1～255，在PGW支持容灾功能或虚拟HLR功能时设置。 |
| VLRSGSNNO | VLR/SGSN号码前缀 | VLR或SGSN号码前缀，E.164格式的编码，为1～6位的十进制数字。     |

## 使用实例

查询HLR的增强用户VLR/SGSN漫游限制状态，参数HLRSN＝1，例如：

LST ERR: HLRSN=1;

```
%%LST ERR: HLRSN=1;%%
RETCODE = 0 SUCCESS0001:操作成功

        "VLR/SGSN Number""RZONE Key"
        861380           9

Total count = 1

There is together 1 report

---    END
```