# 查询攻击用户去活报文的阈值（LST ANTISPOOFINGTHD）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：UPF**

该参数用于查询攻击用户去活报文的阈值。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

使用LST ANTISPOOFINGTHD命令查询当前配置的ANTISPOOFING对攻击用户使用的阈值：

```
LST ANTISPOOFINGTHD:;
```

```
RETCODE = 0  Operation succeeded

AntiSpoofingThd Value
---------------------
Anti-spoofing Threshold for Subscriber Deactivation  =  100
(Number of results = 1)
```

#### 输出结果说明

参见SET ANTISPOOFINGTHD的参数说明。