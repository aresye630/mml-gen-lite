# 查询UPF系统开工流程消息的参数（LST UPFSTARTPARA）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：UPF**

该命令用来查看系统开工流程消息的相关属性。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

查询系统开工流程消息的相关属性：

```
LST UPFSTARTPARA:;
```

```
RETCODE = 0  Operation Success.

UPF start procedure message configuration is
--------------------------------------------
Start Procedure Interval  =  80
(Number of results = 1)
---    END
```

#### 输出结果说明

参见SET UPFSTARTPARA的参数说明。