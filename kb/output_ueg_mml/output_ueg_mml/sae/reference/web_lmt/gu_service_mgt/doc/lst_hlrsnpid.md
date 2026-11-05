# 查询HLRSN与云分区数据(LST HLRSNPID)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于在数据库中查询一条HLRSN与云分区映射关系的数据记录。参数“HLR序列号”和“分区ID”可以都不输入，或者只能输入一个:

- 不输入任何参数时，查询所有的HLRSN与云分区映射关系的数据记录。
- 输入“HLRSN”时，查询“HLR序列号”对应的“分区ID”。
- 输入“PID”时，查询“分区ID”对应的所有的“HLR序列号”信息。

## 注意事项

无。

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                 |
|:-------|:-------|:-------------------------------------|
| HLRSN  | HLR序列号 | 用于指示系统按照哪个HLR序列号来查询HLRSN与云分区的映射关系数据。 |
| PID    | 分区ID   | 用于指示系统按照哪个分区ID来查询HLRSN与云分区的映射关系数据。   |

## 使用实例

1. 在数据库中查询所有的HLRSN与云分区映射关系的数据记录:

   ```
   LST HLRSNPID:;
   ```

   ```
   %%LST HLRSNPID:;%%
   RETCODE = 0 SUCCESS0001:操作成功

   "Partition ID"   "HLRSN"
   2                5
   1                26
   2                209
   ```
2. 在数据库中查询“HLR序列号”为“5”对应的分区ID：

   ```
   LST HLRSNPID: HLRSN=5;
   ```

   ```
   %%LST HLRSNPID: HLRSN=5;%%
   RETCODE = 0 SUCCESS0001:操作成功

         "Partition ID" = 2

   Total count = 1

   There is together 1 report

   ---    END
   ```
3. 在数据库中查询“分区ID”为“2”对应的HLR序列号：

   ```
   LST HLRSNPID: PID=2;
   ```

   ```
   %%LST HLRSNPID: PID=2;%%
   RETCODE = 0 SUCCESS0001:操作成功

   "Partition ID"   "HLRSN"
   2                5
   2                209

   Total count = 2

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，参数含义请参见**ADD HLRSNPID**命令的参数说明。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释   | 原因分析                                   | 处理建议                                    |
|:--------|:--------|:---------------------------------------|:----------------------------------------|
| ERR1010 | 参数冲突    | 参数HLRSN和PID同时输入。                       | HLRSN和PID只能输入一个或者不输入。                   |
| ERR3007 | 记录不存在   | 输入的HLR序列号未在ADD HLRSNPID命令中添加与云分区的对应关系。 | 请检查确保输入的HLRSN已由ADD HLRSNPID命令添加，然后重新输入。 |