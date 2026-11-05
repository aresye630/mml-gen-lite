# 查询LCS客户端信息（LST LCSCLIENTINFO）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：UPF**

该命令用于查询LCS Client与黑白名单MSISDN号段组的绑定关系。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

查询所有CLIENTINFO：

```
LST LCSCLIENTINFO:;
```

```
RETCODE = 0  操作成功

LCS客户端信息
-------------
        LCS客户端标识  =  app1
白名单MSISDN号段组名称  =  group1
黑名单MSISDN号段组开关  =  使能
黑名单MSISDN号段组名称  =  group2
(结果个数 = 1)

---    END
```

#### 输出结果说明

参见ADD LCSCLIENTINFO的参数说明。