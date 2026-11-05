# 查询BTDR单据上报参数（LST BTDRBASICCFG）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：PGW-U、UPF**

该命令用于查询BTDR单据上报参数。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

查询BTDR单据上报参数：

```
%%LST BTDRBASICCFG:;
```

```
%%
RETCODE = 0  Operation succeeded

Parameters for reporting BTDRs
------------------------------
                         Reporting Switch  =  ENABLE
                     Reporting Period (s)  =  50
UDP Packet Payload Maximum Length (bytes)  =  520
       Cache Duration of Sent Packets (s)  =  30
                  Pseudonymization Switch  =  ENABLE
                    Pseudonymization Mode  =  PRE_DEFINED
               Pseudonymization Algorithm  =  HMACSHA256
(Number of results = 1)

---    END
```

#### 输出结果说明

参见SET BTDRBASICCFG的参数说明。