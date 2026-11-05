# 查询S10路径参数(LST EDGECFGS10GTP)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用网元：MME**

该命令用于查询配置是否根据ADD EDGEMMEPGWIP配置主动发送S10口echo消息。

#### 注意事项

无

#### 本地用户权限

manage-ug；system-ug；monitor-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无

#### 使用实例

查询是否根据ADD EDGEMMEPGWIP配置主动发送S10口echo消息，执行如下命令：

```
%%LST EDGECFGS10GTP:;%%
RETCODE = 0  操作成功

结果如下
------------------------
发送echo消息  =  ON
(结果个数 = 1)

---    END
```