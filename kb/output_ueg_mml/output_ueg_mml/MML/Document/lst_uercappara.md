# 查询UE Radio Capability信元参数（LST UERCAPPARA）

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用网元：SGSN、MME**

该命令用于查看UE无线能力的告警阈值。

#### 注意事项

该命令执行后立即生效。

#### 本地用户权限

manage-ug；system-ug；monitor-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

查询UE Radio Capability信元参数“上报告警百分比”；

LST UERCAPPARA:;

```
%%LST UERCAPPARA:;%% 
RETCODE = 0  操作成功  
查询结果如下 
------------ 
上报告警百分比  =  95 
(结果个数 = 1)  
---    END
```

#### 输出结果说明

请参考**SET UERCAPPARA**命令的参数标识。