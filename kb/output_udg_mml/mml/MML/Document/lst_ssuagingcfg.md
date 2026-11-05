# 查询SSU容器业务相关老化功能配置（LST SSUAGINGCFG）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：PGW-U、UPF**

该命令用于查询SSU容器业务相关老化功能配置。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

查询SSU容器业务相关老化功能配置：

```
%%LST SSUAGINGCFG:;
```

```
%%
RETCODE = 0  Operation succeeded

Configuring the Aging Function for SSU Container Services
---------------------------------------------------------
Service flow aging time (s)  =  30
   Session Aging Time (min)  =  60
(Number of results = 1)

---    END
```

#### 输出结果说明

参见SET SSUAGINGCFG的参数说明。