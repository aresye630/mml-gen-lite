# 查询Diameter参数（LST UPDIAMETERPARA）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：UPF**

该命令用于查询是否允许携带Destination-Host AVP的消息通过Diameter Realm路由发送的配置信息。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

查询当前是否允许携带Destination-Host AVP的消息通过Diameter Realm路由发送功能的配置信息：

```
LST UPDIAMETERPARA:;
```

```
RETCODE = 0  操作成功。
Diameter参数信息
----------------
基于域名的路由功能开关  =  允许
(结果个数 = 1)
---    END
```

#### 输出结果说明

参见SET UPDIAMETERPARA的参数说明。