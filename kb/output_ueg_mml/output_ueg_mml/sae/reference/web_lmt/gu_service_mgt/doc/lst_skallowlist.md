# 查询强制允许SK列表(LST SKALLOWLIST)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询强制允许SK列表的配置信息：

- 若要查询“TCSI”的数据信息，请输入“虚拟HLR序列号”参数及“业务键类型”参数选择“TCSI”。
- 若要查询“ETCSI”的数据信息，请输入“虚拟HLR序列号”参数及“业务键类型”参数选择“ETCSI”。

## 注意事项

无。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                        |
|:-------|:-------|:--------------------------------------------|
| HLRSN  | HLR序列号 | 用于指示系统按照哪个HLR序列号来查询强制允许SK列表。                |
| SKTYPE | 业务键类型  | 用于指示系统按照哪个业务键类型来查询强制允许SK列表。 取值范围： TCSIETCSI |

## 使用实例

1. 查询TCSI的强制允许SK列表，“HLR序列号”为“1”，“业务键类型”为“TCSI”。命令如下：

   ```
   LST SKALLOWLIST:HLRSN=1, SKTYPE=TCSI;
   ```

   ```
   %% LST SKALLOWLIST:HLRSN=1, SKTYPE=TCSI;%%
   RETCODE = 0 SUCCESS0001:Operation is successful

             "TCSI"
             123
             234

   Total count = 2

   There is together 1 report

   ---    END
   ```
2. 查询ETCSI的强制允许SK列表，“HLR序列号”为“1”，“业务键类型”为“ETCSI”。命令如下：

   ```
   LST SKALLOWLIST:HLRSN=1, SKTYPE=ETCSI;
   ```

   ```
   %% LST SKALLOWLIST:HLRSN=1, SKTYPE=ETCSI;%%
   RETCODE = 0 SUCCESS0001:Operation is successful

             "ETCSI"
             1
             999

   Total count = 2

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**SET SKALLOWLIST**命令的参数说明。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释   | 原因分析         | 处理建议                              |
|:--------|:--------|:-------------|:----------------------------------|
| ERR3007 | 记录不存在   | “HLR序列号”未定义。 | 根据实际情况，重新输入“HLR序列号”的取值，确保其取值符合要求。 |