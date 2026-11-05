# 查询LB灰度升级阶段（LST LBUPGSTAGE）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于查询CSLB灰度升级阶段。

#### 注意事项

该命令执行后立即生效。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

查询CSLB灰度升级阶段。

```
%%LST LBUPGSTAGE:;%% RETCODE = 0  Operation succeeded
The result is as follows:
-------------------------
CSLB Gray Upgrade Stage  =  Steady Stage
(Number of results = 1)
---    END
```

#### 输出结果说明

参见**SET LBUPGSTAGE**的参数说明。