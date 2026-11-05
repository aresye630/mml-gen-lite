# 查询数据同步客户端支持的密钥交换算法（LST RDATACLIENTKEXALGOS）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于查询数据同步客户端支持的密钥交换算法。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

查询数据同步客户端支持的密钥交换算法：

```
LST RDATACLIENTKEXALGOS:;
```

```
RETCODE = 0  操作成功
数据同步客户端支持的密钥交换算法
--------------------------------------------------------------------
                   curve25519-sha256 密钥交换算法  =  TRUE
        curve25519-sha256@libssh.org 密钥交换算法  =  TRUE
diffie-hellman-group-exchange-sha256 密钥交换算法  =  TRUE
                  ecdh-sha2-nistp256 密钥交换算法  =  FALSE
                  ecdh-sha2-nistp384 密钥交换算法  =  FALSE
                  ecdh-sha2-nistp521 密钥交换算法  =  FALSE
(结果个数 = 1)

---    END
```

#### 输出结果说明

参见SET RDATACLIENTKEXALGOS的参数说明。