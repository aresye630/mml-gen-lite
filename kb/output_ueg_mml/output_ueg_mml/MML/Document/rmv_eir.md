# 删除EIR配置(RMV EIR)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用网元：MME**

此命令用于删除EIR（Equipment Identity Register）表记录。MME（Mobility Management Entity）根据EIR表记录选择EIR。

#### 注意事项

- 此命令执行后立即生效。
- 删除后，将导致系统无法找到指定EIR。

#### 本地用户权限

manage-ug；system-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

无。

#### 使用实例

将EIR记录删除：

RMV EIR:;