# 查询AS主机名(LST HASHOST)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询AS对端实体和数据库中的ASID间的对应关系：

- 若需要查询所有的对应关系，请不要输入任何参数。
- 若需要查询某条指定记录，请输入“ASID”或“主机名”参数。

## 注意事项

执行该命令时，只需要输入“ASID”和“主机名”参数中的一个，两个参数同时输入会返回报错“参数冲突”。

## 参数说明

| 参数标识     | 参数名称   | 参数说明                                                |
|:---------|:-------|:----------------------------------------------------|
| ASID     | ASID   | 用于标识需要查询的AS对端实体的Diameter对端实体标识。 取值范围：0～65534 默认值：无。 |
| HOSTNAME | 主机名    | 用于标识需要查询的AS对端实体的网络主机名。 取值范围：长度不超过127的字符串。 默认值：无。    |

## 使用实例

1. 查询“ASID”为“1”的一条AS对端实体和ASID间的对应关系：

   ```
   LST HASHOST: ASID=1;
   ```

   ```
   %%LST HASHOST: ASID=1;%%
   RETCODE = 0 SUCCESS0001:Operation is successful

   SYSNO     ASID                HOSTNAME                       REALMNAME                 REPDATAFMTSW
   0         1                   as1.huawei.com                 huawei.com                NOT_CTRL

   Total count = 1

   There is together 1 report

   ---    END
   ```
2. 查询所有的AS对端实体和ASID间的对应关系：

   ```
   LST HASHOST:;
   ```

   ```
   %%LST HASHOST:;%%
   RETCODE = 0 SUCCESS0001:Operation is successful

   SYSNO     ASID                HOSTNAME                       REALMNAME                  REPDATAFMTSW               SERVICELIST
   0         1                   as1.huawei.com                 huawei.com                 NOT_CTRL                     
   0         1001                as1001.huawei.com              huawei.com                 NOT_CTRL
   0         1002                as1002.huawei.com              huawei.com                 CTRL                       CFD
   0         1003                as1003.huawei.com              huawei.com                 CTRL                       CFD
   0         1004                as1004.huawei.com              huawei.com                 CTRL                       NO_MEDIA
   0         1005                as1005.huawei.com              huawei.com                 CTRL                       CFD|NO_MEDIA

   Total count = 6

   There is together 1 report

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数请参见**ADD HASHOST**命令的输出结果说明。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

|       错误码 | 错误码解释   | 原因分析                                 | 处理建议                            |
|----------:|:--------|:-------------------------------------|:--------------------------------|
| 900003495 | AS信息不存在 | 该命令输入的“ASID”或“主机名”参数标识的记录不存在，参数输入有误。 | 执行本命令查询当前所有的数据记录，在输出结果中查找需要的记录。 |
| 900001009 | 参数冲突    | 执行命令时同时输入了“ASID”和“主机名”参数。            | 重新执行命令，确保只输入“ASID”和“主机名”参数中的一个。 |