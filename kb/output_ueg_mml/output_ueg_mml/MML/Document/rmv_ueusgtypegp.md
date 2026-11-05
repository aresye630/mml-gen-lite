# 删除UE USAGE TYPE群组(RMV UEUSGTYPEGP)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用网元：MME**

该命令用于删除UE USAGE TYPE群组记录。

#### 注意事项

- 该命令执行后立即生效。
- 删除UE USAGE TYPE群组时必须保证相关表中不存在该UE USAGE TYPE群组的相关记录，可执行**LST DNSN**查看相关记录。
- 删除UE USAGE TYPE群组时必须首先删除该UE USAGE TYPE群组下的所有成员，可执行**RMV UEUSGTYPEGPMEM**命令进行删除。

#### 本地用户权限

manage-ug；system-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识          | 参数名称              | 参数说明                                                                   |
|:--------------|:------------------|:-----------------------------------------------------------------------|
| UEUSGTYPEGPID | UE USAGE TYPE群组标识 | 可选必选说明：必选参数 参数含义：该参数用于指定UE USAGE TYPE群组标识。 数据来源：本端规划 取值范围：0～1023 默认值：无 |

#### 使用实例

删除一个“UEUSGTYPEGPID”为“0”的UE USAGE TYPE群组：

`RMV UEUSGTYPEGP: UEUSGTYPEGPID=0;`