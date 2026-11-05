# 查询全局RADIUS Accounting配置（LST GLBRDSACCT）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：PGW-C、SMF**

LST GLBRDSACCT命令用来显示全局Radius计费配置的信息。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

查询全局RADIUS Accounting配置：

```
LST GLBRDSACCT:;
```

```
RETCODE = 0  操作成功。

全局AAA计费配置
---------------
  发送RADIUS Accounting On/Off消息附加次数  =  1
每秒钟尝试发送Accounting Start消息的用户数  =  10
(结果个数 = 1)
---    END
```

#### 输出结果说明

参见SET GLBRDSACCT的参数说明。