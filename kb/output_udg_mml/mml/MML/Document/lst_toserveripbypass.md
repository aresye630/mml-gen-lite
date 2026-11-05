# 查询异常Server IP自动bypass功能配置（LST TOSERVERIPBYPASS）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：UPF**

该命令用于查询异常Server IP自动bypass功能配置。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

查询异常Server IP自动bypass功能配置：

```
LST TOSERVERIPBYPASS:;
```

```
RETCODE = 0  操作成功
 
异常Server IP自动bypass配置
-------------
异常Server IP自动bypass功能开关  =  ENABLE
老化时间（秒） =  86400
异常状态重置为初始状态时间（秒） =  21600
 
(结果个数 = 1)
 
--- END
```

#### 输出结果说明

参见SET TOSERVERIPBYPASS的参数说明。