# 显示路由队列信息(DSP ROUTELOG)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于请求系统显示异常路由校验消息队列和异常路由快速校验队列的信息。

## 注意事项

无。

## 参数说明

| 参数标识        | 参数名称       | 参数说明                                                                            |
|:------------|:-----------|:--------------------------------------------------------------------------------|
| SERVICETYPE | 业务类型       | 用于请求系统显示指定业务类型的异常路由校验消息队列和异常路由快速校验队列信息。若不输入，则表示显示所有业务类型的路由校验队列信息。               |
| CID         | Cluster标识  | 用于请求系统显示需要查询异常路由校验消息队列和异常路由快速校验队列信息的Cluster标识。若不输入，则表示显示所有Cluster标识的路由校验队列信息。   |
| LID         | Location标识 | 用于请求系统显示需要查询异常路由校验消息队列和异常路由快速校验队列信息的Location标识。若不输入，则表示显示所有Location标识的路由校验队列信息。 |

## 使用实例

显示“业务类型”为“SUP-FE”的异常路由校验消息队列和异常路由快速校验队列信息，“Cluster”“标识”为“1101”，“Location标识”为“5”：

```
DSP ROUTELOG: SERVICETYPE="SUP-FE", CID=1101, LID=5;
```

```
%%DSP ROUTELOG: SERVICETYPE="SUP-FE", CID=1101, LID=5;%%
RETCODE = 0  操作成功
 
操作结果如下
------------------------
 业务类型  Cluster标识  节点标识  Location标识  主表表名                   复制队列消息数量  异常路由快速校验队列对象数量
 
 SUP-FE    1101         1101      5             ROUTE_AUC1_5201            0                 0
 SUP-FE    1101         1101      5             ROUTE_SUB1_5202            0                 0
 SUP-FE    1101         1101      5             ROUTE_SUB2_5256            0                 0
 SUP-FE    1101         1101      5             ROUTE_SUB3_5204            0                 0
 SUP-FE    1101         1101      5             ROUTE_SUB4_5270            0                 0
 SUP-FE    1101         1101      5             ROUTE_SUID_5200            0                 0
 SUP-FE    1101         1101      5             ROUTE_STRSUID_5300         0                 0
 SUP-FE    1101         1101      5             ROUTE_STRUSER_5301         0                 0
 SUP-FE    1101         1101      5             ROUTE_INT4SUID_5600        0                 0
 SUP-FE    1101         1101      5             ROUTE_INT4USER_5601        0                 0
 SUP-FE    1101         1101      5             ROUTE_INT8SUID_5400        0                 0
 SUP-FE    1101         1101      5             ROUTE_INT8USER_5401        0                 0
 SUP-FE    1101         1101      5             ROUTE_IPV6ADDR_5570        0                 0
 SUP-FE    1101         1101      5             ROUTE_USERNAME_5252        0                 0
 SUP-FE    1101         1101      5             ROUTE_INT4SUID2_5265       0                 0
 SUP-FE    1101         1101      5             ROUTE_INT4USER2_5266       0                 0
 SUP-FE    1101         1101      5             ROUTE_PREFIX_STRSUID_5700  0                 0
 SUP-FE    1101         1101      5             ROUTE_PREFIX_STRUSER_5701  0                 0
 SUP-FE    1101         1102      5             ROUTE_AUC1_5201            0                 0
 SUP-FE    1101         1102      5             ROUTE_SUB1_5202            0                 0
 SUP-FE    1101         1102      5             ROUTE_SUB2_5256            0                 0
 SUP-FE    1101         1102      5             ROUTE_SUB3_5204            0                 0
 SUP-FE    1101         1102      5             ROUTE_SUB4_5270            0                 0
 SUP-FE    1101         1102      5             ROUTE_SUID_5200            0                 0
 SUP-FE    1101         1102      5             ROUTE_STRSUID_5300         0                 0
 SUP-FE    1101         1102      5             ROUTE_STRUSER_5301         0                 0
 SUP-FE    1101         1102      5             ROUTE_INT4SUID_5600        0                 0
 SUP-FE    1101         1102      5             ROUTE_INT4USER_5601        0                 0
 SUP-FE    1101         1102      5             ROUTE_INT8SUID_5400        0                 0
 SUP-FE    1101         1102      5             ROUTE_INT8USER_5401        0                 0
 SUP-FE    1101         1102      5             ROUTE_IPV6ADDR_5570        0                 0
 SUP-FE    1101         1102      5             ROUTE_USERNAME_5252        0                 0
 SUP-FE    1101         1102      5             ROUTE_INT4SUID2_5265       0                 0
 SUP-FE    1101         1102      5             ROUTE_INT4USER2_5266       0                 0
 SUP-FE    1101         1102      5             ROUTE_PREFIX_STRSUID_5700  0                 0
 SUP-FE    1101         1102      5             ROUTE_PREFIX_STRUSER_5701  0                 0
(结果个数 = 36)
 
---    END
```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数。

| 输出项名称          | 输出项解释                                                                                |
|:---------------|:-------------------------------------------------------------------------------------|
| 业务类型           | 用于返回路由校验队列的业务类型信息。                                                                   |
| Cluster标识      | 用于返回DSU Cluster，此参数在同一USCDB下唯一。                                                      |
| 节点标识           | 用于返回DSU节点，此参数在Location内唯一。为方便维护，节点标识和模块号的取值通常相同。                                     |
| Location标识     | 用于返回Location。                                                                        |
| 主表表名           | 用于返回节点中对应的路由数据表的名称。                                                                  |
| 复制队列消息数量       | 用于返回该节点中复制队列消息中堆积的异常路由校验消息个数。队列最大长度固定为10000个。 当系统正常运行情况下，复制消息队列大小显示为0。节点一般不会堆积复制消息。  |
| 异常路由快速校验队列对象数量 | 用于返回该节点中等待异常路由快速校验的用户个数。异常路由快速校验队列长度固定为90000个。 当系统正常运行情况下，校验消息队列大小显示为0。节点一般不会堆积校验消息。 |

该命令执行异常，会返回对应的错误码。常见错误码如表2所示。

|   错误码 | 错误码解释             | 原因分析                               | 处理建议                                                                                                      |
|------:|:------------------|:-----------------------------------|:----------------------------------------------------------------------------------------------------------|
|  1710 | 无可用模块。            | 所有DSU模块全部异常。                       | 请参见产品手册的“模块故障”进行处理。                                                                                       |
|  2059 | 指定的业务类型不存在。       | 指定的“业务类型”不存在。                      | 通过LST FEPLUG命令查询加载的“FE类型名称”，即“业务类型”。 若业务类型加载成功，请输入正确的业务类型名称。若业务类型加载不成功或者没有加载，通过LOD FEPLUG命令加载成功后，重新执行该命令。 |
|  2131 | 未配置Location。      | 未配置“Location标识”。                   | 执行SET LOCATION命令配置Location，再重新执行此命令确保Location已配置。                                                         |
|  2132 | 指定Location不存在。    | 未配置指定的“Location标识”。                | 执行SET LOCATION命令配置指定的Location信息，重新执行此命令确保指定的Location已配置。                                                  |
|  2133 | 未配置Cluster。       | 未配置“Cluster标识”。                    | 先执行LST CLUSTER命令查询Cluster信息，再执行ADDCLUSTER配置Cluster信息，确保Cluster已配置。                                        |
|  2135 | 没有可用模块。           | 输入的“Cluster标识”下未配置相应的“节点”。         | 先执行LSTCLUSTER命令查询Cluster信息，再执行ADD NODE命令添加所需的“节点”，确保成功添加后，重新执行本命令。                                        |
| 26023 | 指定的DSU Cluster不存在 | 输入的“Cluster标识”不是DSU或与输入的“业务类型”不匹配。 | 执行LST CLUSTER命令查询DSU Cluster信息，确保指定的“Cluster标识”为DSU Cluster且与输入“业务类型”匹配。                                  |