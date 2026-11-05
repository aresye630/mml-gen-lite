# 查询接口DSCP配置(LST IFDSCPMCR)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用网元：MME**

该命令用来查看MCR\_VNFC对外网元接口发送IP包时携带的DSCP值。

#### 注意事项

无。

#### 本地用户权限

manage-ug；system-ug；monitor-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

查询MCR\_VNFC对外网元接口发送IP包时携带的DSCP配置：

LST IFDSCPMCR:;

```
%%LST IFDSCPMCR:;%%

DSCP查询结果如下
--------------
接口类型                     DSCP值
未指定接口                   56
SDUP                         36

---    END
```

#### 输出结果说明

参见**SET IFDSCPMCR**的参数说明。