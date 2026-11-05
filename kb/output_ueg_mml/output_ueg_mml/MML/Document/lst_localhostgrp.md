# 查询Diameter本端信息组（LST LOCALHOSTGRP）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：PGW-C、SMF**

此命令用于查询Diameter本端主机组名称。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

无。

#### 使用实例

查询Diamter本端主机组记录：

```
LST LOCALHOSTGRP:;
```

```
RETCODE = 0  操作成功

Diameter 本端主机组
-------------------
Diameter本端信息组名称  =  zk
(结果个数 = 1)

---    END
```

#### 输出结果说明

参见ADD LOCALHOSTGRP的参数说明。