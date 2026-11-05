# 查询是否检查Serving Node携带的CC（LST CHARGECHARCHK）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：PGW-C、SMF**

该命令用来查询是否检查Serving Node携带的charge-characteristic。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

查询是否检查Serving Node携带的charge-characteristic：

```
LST CHARGECHARCHK:;
```

```
RETCODE = 0  操作成功。

结果如下
--------
检查Serving Node携带的charge-characteristic  =  允许
(结果个数 = 1)
---    END
```

#### 输出结果说明

参见SET CHARGECHARCHK的参数说明。