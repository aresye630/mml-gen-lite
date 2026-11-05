# 查询非携转全局数据(LST NPPREFIXRN)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

此操作用于查询携转用户数据配置。

## 注意事项

无。

## 参数说明

| 参数标识        | 参数名称     | 参数说明                                         |
|:------------|:---------|:---------------------------------------------|
| ISDN_PREFIX | MSISDN前缀 | MSISDN前缀号码，E.164格式的编码，为1～15位的十进制数字。 说明：可选参数。 |

## 使用实例

查询MSISDN前缀号码为86131075003003的非携转用户数据配置。命令如下：

```
LST NPPREFIXRN: ISDN_PREFIX="86131075003003";
```

```
%%LST NPPREFIXRN: ISDN_PREFIX="86131075003003";%%
RETCODE = 0 SUCCESS0001:Operation is successful

        "ISDNPREFIX"        "RN"                "MSCID"
        86131075003003      1112                

Total count = 1

There is together 1 report

---    END
```