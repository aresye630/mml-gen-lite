# 查询整机操作系统级带宽管理开关（LST GLBOSLELBWMSW）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：PGW-U、UPF**

该命令用来查询整机操作系统级带宽管理开关。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

查询整机操作系统级带宽管理开关信息：

```
LST GLBOSLELBWMSW:;
```

```
RETCODE = 0 Operation Success.

Global OS Level Bandwidth Managament Switch Information
--------------------------------------------------------------------------------
 Global OS Level Bandwidth Managament Switch = ENABLE
(Number of results = 1)
--- END
```

#### 输出结果说明

参见SET GLBOSLELBWMSW的参数说明。