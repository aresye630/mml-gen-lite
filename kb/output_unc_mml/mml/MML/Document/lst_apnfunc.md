# 查询APNNI功能配置(LST APNFUNC)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用网元：SGSN**

该命令用于查询APNNI功能。

#### 注意事项

无。

#### 本地用户权限

manage-ug；system-ug；monitor-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

查询所有APNNI的属性信息：

**LST APNFUNC:;**

```
%%LST APNFUNC:;%% 
RETCODE = 0    执行成功。       

操作结果如下 
---------------
APN网络标识   APN用途

HUAWEI1.COM  VIP 用户
HUAWEI2.COM  VIP 用户
（结果个数 = 2）

---    END
```

#### 输出结果说明

请参考**ADD APNFUNC**命令的参数标识。