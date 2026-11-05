# 删除用户模板组（RMV USRPROFGROUP）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用NF：PGW-C、SMF**

此命令用于删除UsrProfGroup。如果指定UsrProfGroup名字，只删除该UsrProfGroup，如果没有指定UsrProfGroup名字，则删除系统内的所有UsrProfGroup。

#### 注意事项

- 该命令执行后立即生效。
- 删除一个UsrProfGroup的同时会删除此UsrProfGroup下所有的和UserProfile的绑定关系。
- 如果UsrProfGroup已经绑定在APN下，则不允许删除，需要先解除绑定关系后再删除。
- 业务进行中删除UsrProfGroup时，如果有用户在使用此UsrProfGroup下绑定的UserProfile，则不允许删除。
- 业务进行中删除UsrProfGroup时，如果有AAA下发UsrProfGroup的用户使用此UsrProfGroup，则不允许删除。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识          | 参数名称    | 参数说明                                                                                          |
|:--------------|:--------|:----------------------------------------------------------------------------------------------|
| USERPROFGNAME | 用户模板组名称 | 可选必选说明：可选参数 参数含义：该参数用于指定用户模板组的名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。 默认值：无 配置原则：无 |

#### 使用实例

删除指定名称的UsrProfGroup配置：

```
RMV USRPROFGROUP:USERPROFGNAME="userprofg1";
```