# 查询UPF组与Diameter本端主机组的绑定关系组（LST UPFGLOCGBNDGRP）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：PGW-C、SMF**

此命令用于查询UPF组与Diameter本端主机组的绑定关系组。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

无。

#### 使用实例

查询UPF组与Diameter本端主机组的绑定关系组记录：

```
LST UPFGLOCGBNDGRP:;
```

```
RETCODE = 0 操作成功。

UPF组与Diameter本端主机组的绑定关系组
-----------------------------
UPF组与Diameter本端主机组的绑定关系组名称  =  huawei
(结果个数 = 1)
---    END
```

#### 输出结果说明

参见ADD UPFGLOCGBNDGRP的参数说明。