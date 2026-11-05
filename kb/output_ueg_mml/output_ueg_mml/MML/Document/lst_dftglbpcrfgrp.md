# 查询全局缺省PCRF组（LST DFTGLBPCRFGRP）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：PGW-C、SMF**

此命令用来查询缺省全局PCRF分组。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

显示DFTGLBPCRFGRP：

```
LST DFTGLBPCRFGRP:;
```

```
RETCODE = 0  操作成功。

全局缺省PCRF组
--------------
PCRF组名称  =  pcr
(结果个数 = 1)
---    END
```

#### 输出结果说明

参见SET DFTGLBPCRFGRP的参数说明。