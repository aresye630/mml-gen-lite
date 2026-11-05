# 查询Service Partition本局数据(LST SPINTROFF)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询Service Partition本局信息。

## 注意事项

无。

## 参数说明

| 参数标识   | 参数名称                | 参数说明                                                     |
|:-------|:--------------------|:---------------------------------------------------------|
| PID    | Service Partition标识 | 用于指示系统需要按照哪个Service Partition标识来查询Service Partition本局信息。 |

## 使用实例

查询Service Partition本局信息：

```
LST SPINTROFF: PID=20;
```

```
%%LST SPINTROFF: PID=20;%%
RETCODE = 0 SUCCESS0001:操作成功

           Service PartitionID = 20
              Local HLR Number = 1
      Function ID of Local HLR = 3
                  Country Code = 1
                            RN = <NULL>

Total count = 5

There is together 1 report

---    END
```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**SET SPINTROFF**命令的参数说明。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释                | 原因分析                                                                    | 处理建议                                                                                                   |
|:--------|:---------------------|:------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------|
| ERR1145 | 获取用户归属的Partition信息失败 | 在混合组网中，输入的“Service Partition标识”参数未在“USCDB MML命令”界面上ADD RPARTITION命令中定义。 | 重新输入“Service Partition标识”参数，确保其值已定义。已定义的“Service Partition标识”参数可以通过“USCDB MML命令”界面上LST RPARTITION命令查询。 |
| ERR3111 | 系统不支持该特性             | 当前组网不是云部署组网，该命令仅能在云部署组网下执行。                                             | 请先配置组网为云部署组网，再执行该命令。                                                                                   |
| ERR3342 | PartitionID不存在       | 在云部署组网中，输入的“Service Partition标识”参数未在“USCDB MML命令”界面上ADD RPARTITION命令定义。 | 重新输入“Service Partition标识”参数，确保其值已定义。已定义的“Service Partition标识”参数可以通过“USCDB MML命令”界面上LST RPARTITION命令查询。 |