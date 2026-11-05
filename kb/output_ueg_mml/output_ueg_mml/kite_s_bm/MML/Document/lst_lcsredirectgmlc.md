# 查询LCS重定向GMLC配置（LST LCSREDIRECTGMLC）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：UPF**

该命令用于查询重定向GMLC参数。

#### 注意事项

该命令执行后立即生效。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

查询重定向GMLC参数：

```
LST LCSREDIRECTGMLC:;
```

```
RETCODE = 0  操作成功

LCS重定向GMLC配置
-----------------
   重定向GMLC开关  =  使能
重定向GMLC IP版本  =  IPv4
    GMLC IPv4地址  =  192.168.0.0
    GMLC IPv6地址  =  ::
(结果个数 = 1)

---    END
```

#### 输出结果说明

参见SET LCSREDIRECTGMLC的参数说明。