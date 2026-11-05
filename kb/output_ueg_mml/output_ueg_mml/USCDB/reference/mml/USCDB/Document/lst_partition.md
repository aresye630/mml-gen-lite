# 查询Partition信息(LST PARTITION)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询USCDB网元内配置的Partition信息。

## 注意事项

无。

## 参数说明

| 参数标识        | 参数名称        | 参数说明                                            |
|:------------|:------------|:------------------------------------------------|
| PARTITIONID | Partition标识 | 用于指示系统按照哪个Partition标识来查询USCDB网元内配置的Partition信息。 |

## 使用实例

查询USCDB网元内配置的Partition信息：

```
LST PARTITION:;
```

```
%%LST PARTITION:;%%
RETCODE = 0  操作成功

操作结果如下
------------
Partition标识  =  1
Partition角色  =  云版本路由_服务
(结果个数 = 1)

---    END
```

## 输出结果说明

该命令执行正常，会返回命令操作成功的提示信息和相关参数，各参数含义请参见**SET PARTITION**命令的参数说明。