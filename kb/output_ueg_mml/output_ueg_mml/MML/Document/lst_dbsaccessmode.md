# 查询DBS访问BE模式(LST DBSACCESSMODE)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明
- 参考信息

## 命令功能

该命令用于查询DBS访问的BE模式。

## 注意事项

- “访问模式”为“PRIORITY(按DBSRLOCATION的优先级访问BE)”或者“NONE(不访问BE)”时，“远端Location标识”取值固定为“0”，此时不是指代真正的BE LocationID。
- “访问模式”为“ASSIGN(指定访问Location的BE)”时，“远端Location标识”的取值为真正的BE LocationID。

## 参数说明

无。

## 使用实例

查询DBS访问的BE模式：

```
LST DBSACCESSMODE:;
```

```
%%LST DBSACCESSMODE:;%%
RETCODE = 0  操作成功

操作结果如下
------------
        访问模式  =  按DBSRLOCATION的优先级访问BE
远端Location标识  =  0
(结果个数 = 1)

---    END
```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见命令**SET DBSACCESSMODE**的参数说明。

## 参考信息

无。