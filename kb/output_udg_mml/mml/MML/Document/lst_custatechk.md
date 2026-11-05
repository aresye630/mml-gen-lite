# 查询SMF和UPF时间一致性检测（LST CUSTATECHK）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：UPF**

查询SMF和UPF时间一致性检测参数。

#### 注意事项

该命令执行后立即生效。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

查询SMF和UPF时间一致性检测参数：

```
%%LST CUSTATECHK:;
```

```
%%
RETCODE = 0  Operation succeeded

Time Inconsistency Between SMF and UPF
--------------------------------------
UTC Time Consistency Check Switch  =  ENABLE
        Detection error threshold  =  1000
           Alarm Report Threshold  =  10
            Alarm Clear Threshold  =  5
(Number of results = 1)

---    END
```

#### 输出结果说明

参见SET CUSTATECHK的参数说明。