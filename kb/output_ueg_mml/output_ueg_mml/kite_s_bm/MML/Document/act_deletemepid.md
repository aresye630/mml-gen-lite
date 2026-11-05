# 删除MEP标识信息（ACT DELETEMEPID）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用NF：MPF**

该命令用于删除当通过SET MPFATTR命令配置Mm5接口消息类型为SPEC\_RULE时，动态DNS Rule或动态Traffic Rule下发携带的MepId标识信息。

#### 注意事项

- 该命令执行后立即生效。
- 当MPF上存在动态DNS Rule或动态Traffic Rule时，不允许删除MepId标识信息。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

无。

#### 使用实例

删除MepId标识信息：

```
ACT DELETEMEPID:;
RETCODE = 0 操作成功

--- END
```