# 查询缺省的NCC模板(LST DEFNCC)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询VLR/SGSN/MME/S4SGSN/NGS缺省的NCC（Network Capability Configuration）模板的配置信息。

请输入“HLR序列号”参数查询某个虚拟HLR中所有VLR/SGSN/MME/S4SGSN/NGS缺省的NCC模板的配置信息。

## 注意事项

无。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                                |
|:-------|:-------|:----------------------------------------------------|
| HLRSN  | HLR序列号 | 用于指示系统需要按照哪个HLR序列号来查询VLR/SGSN/MME/S4SGSN缺省的NCC模板数据。 |

## 使用实例

查询VLR/SGSN/MME/S4SGSN/NGS缺省的NCC模板数据记录，“HLR序列号”为“1”：

```
LST DEFNCC: HLRSN=1;
```

```
%%LST DEFNCC: HLRSN=1;%%
RETCODE = 0 SUCCESS0001:操作成功

                     VLRNCCTPL = 1
                    SGSNNCCTPL = 1
                     MMENCCTPL = 1
                  S4SGSNNCCTPL = 1
                     NGSNCCTPL = 1

Total count = 5

There is together 1 report

---    END
```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**SET DEFNCC**命令的参数说明。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释   | 原因分析                  | 处理建议                                                  |
|:--------|:--------|:----------------------|:------------------------------------------------------|
| ERR1004 | 无效的参数值  | “HLR序列号”中含有不符合要求的字符串。 | 根据实际情况，重新输入合适的参数字符串。                                  |
| ERR3007 | 记录不存在   | “HLR序列号”未定义。          | 根据实际情况，重新输入已定义的“HLR序列号”，可通过LST HLRSN命令查询已定义的“HLR序列号”。 |