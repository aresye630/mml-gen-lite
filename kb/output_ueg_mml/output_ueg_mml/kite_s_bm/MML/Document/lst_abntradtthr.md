# 查询异常流量检测报文阈值（LST ABNTRADTTHR）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用于查询异常流量检测报文阈值。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

查询异常下行异常流量检测报文阈值个数：

```
LST ABNTRADTTHR:;
```

```
RETCODE = 0  Operation Success.

Abnormal Traffic detect threshold
---------------------------------
Abnormal Traffic detect threshold of packet  =  20
(Number of results = 1)
---    END
```

#### 输出结果说明

参见SET ABNTRADTTHR的参数说明。