# 显示本地用户组（LST LOCALUSERPROF）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：MPF**

该命令用于查询本地用户模板。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

假如运营商需要查询名称为testuserprofilename的本地用户模板：

```
LST LOCALUSERPROF:;
```

```
RETCODE = 0  操作成功

本地用户组
----------
用户组名称  =  testuserprofilename
(结果个数 = 1)

---    END
```

#### 输出结果说明

参见ADD LOCALUSERPROF的参数说明。