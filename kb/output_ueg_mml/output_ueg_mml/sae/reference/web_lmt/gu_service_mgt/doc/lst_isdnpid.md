# 查询MSISDN与云分区数据(LST ISDNPID)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

此命令用于查询MSISDN号段与云分区的映射关系。

- 若需要查询所有的MSISDN号段与云分区的映射关系，则不需要输入参数“MSISDN号段”。
- 若需要查询某个MSISDN号段与云分区的映射关系，请输入参数“MSISDN号段”。

## 注意事项

无。

## 参数说明

| 参数标识     | 参数名称     | 参数说明                                                  |
|:---------|:---------|:------------------------------------------------------|
| ISDNPRFX | MSISDN号段 | 用于标识系统需要按照哪个MSISDN号段来查询与云分区的映射关系；若不输入，则表示所有的MSISDN号段。 |

## 使用实例

1. 查询“MSISDN号段”为“86139”的相关数据，命令如下：

   ```
   LST ISDNPID: ISDNPRFX="86139";
   ```

   ```
   %%LST ISDNPID: ISDNPRFX="86139";%%
   RETCODE = 0 SUCCESS0001:操作成功

             "ISDNPRFX"         "Partition ID"
             86139               7

   Total count = 1

   There is together 1 report

   ---    END
   ```
2. 查询所有的MSISDN号段的数据，命令如下：

   ```
   LST ISDNPID:;
   ```

   ```
   %%LST ISDNPID:;%%
   RETCODE = 0 SUCCESS0001:操作成功

             "ISDNPRFX"         "Partition ID"
             86139               7
             86136               1
             86138               5

   Total count = 3

   There is together 1 report

   ---    END
   ```

## 输出结果说明

输出项的详细说明请参见ADD ISDNPID命令的参数说明。