# 查询ISU POD业务CPU过载告警阈值（LST ISUPODCPUTHD）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：SGW-U、PGW-U、UPF**

查询ISU POD业务CPU过载告警阈值。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

查询ISU POD业务CPU过载告警阈值：

```
LST ISUPODCPUTHD:;
```

```
RETCODE = 0  Operation succeeded

The result is as follows
------------------------
Alarm Reporting Threshold  =  85
 Alarm Recovery threshold  =  75
(Number of results = 1)

---    END
```

#### 输出结果说明

参见SET ISUPODCPUTHD的参数说明。