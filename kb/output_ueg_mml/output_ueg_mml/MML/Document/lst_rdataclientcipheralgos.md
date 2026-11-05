# 查询数据同步客户端支持的加密算法（LST RDATACLIENTCIPHERALGOS）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于查询数据同步客户端支持的加密算法。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

查询数据同步客户端支持的加密算法：

```
LST RDATACLIENTCIPHERALGOS:;
```

```
RETCODE = 0  操作成功

数据同步客户端支持的加密算法
-------------------------------------------------------
chacha20-poly1305@openssh.com 加密算法  =  TRUE
       aes128-gcm@openssh.com 加密算法  =  TRUE
                   aes128-ctr 加密算法  =  TRUE
                   aes192-ctr 加密算法  =  TRUE
                   aes256-ctr 加密算法  =  TRUE
(结果个数 = 1)

---    END
```

#### 输出结果说明

参见SET RDATACLIENTCIPHERALGOS的参数说明。