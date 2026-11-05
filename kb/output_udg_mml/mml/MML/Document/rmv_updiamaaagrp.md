# 删除Diameter AAA服务器组（RMV UPDIAMAAAGRP）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用NF：UPF**

此命令用于删除一个Diameter AAA组。当某个Diameter AAA组没有绑定到任何APN下，且该组不再被使用时，操作员可以执行此命令删除该组。

#### 注意事项

- 该命令执行后立即生效。
- 如果Diameter AAA组已经绑定到APN，则不允许删除。
  如果Diameter AAA组下已经绑定了Diameter AAA，则相应的Diameter AAA绑定关系（DiamAAABndGrp）会删除。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识      | 参数名称           | 参数说明                                                                              |
|:----------|:---------------|:----------------------------------------------------------------------------------|
| GROUPNAME | Diameter AAA组名 | 可选必选说明：必选参数 参数含义：该参数用于指定Diameter AAA组名。 数据来源：本端规划 取值范围：不支持空格，不区分大小写。 默认值：无 配置原则：无 |

#### 使用实例

根据网络规划，删除名称为“diametergroup”的Diameter AAA组：

```
RMV UPDIAMAAAGRP:GROUPNAME="diametergroup";
```