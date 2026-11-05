# 查询tethering的TTL值（LST TETHERINGTTL）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：PGW-U、UPF**

该命令用于查询所有配置的TTL值。

#### 注意事项

该命令执行后立即生效。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

显示所有判断tethering的TTL值：

```
%%LST TETHERINGTTL:;
```

```
%%
RETCODE = 0  操作成功

Tethering TTL
-------------
Tethering TTL值  =  2
(结果个数 = 1)

---    END
```

#### 输出结果说明

参见ADD TETHERINGTTL的参数说明。