# 查询限制Partition营帐操作配置(LST PROVRESTRICTED)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询限制Partition营帐操作配置信息。

## 注意事项

无。

## 参数说明

无。

## 使用实例

查询限制Partition营帐操作配置信息。

```
LST PROVRESTRICTED;
```

```
%%LST PROVRESTRICTED;%%
RETCODE = 0  操作成功

操作结果如下
------------------------
    Partition标识  =  1
 是否返回响应报文  =  NO
(结果个数 = 1)

---    END
```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数请参见**ADD PROVRESTRICTED**命令的参数说明。