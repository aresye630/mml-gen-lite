# 查询主机域参数（LST HOSTDOMAINPARA）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：MPF**

该命令用来查看主机域相关参数配置。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

查看主机域相关参数配置：

```
%%LST HOSTDOMAINPARA:;
```

```
%%
RETCODE = 0  操作成功

Host Domain Parameter Configuration
-----------------------------------
Multi Host Study Switch  =  DISABLE
(Number of results = 1)

---    END
```

#### 输出结果说明

参见SET HOSTDOMAINPARA的参数说明。