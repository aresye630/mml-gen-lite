# 查询UDP报文是否携带checksum（LST UDPCHECKSUM）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用来查询系统发送的UDP报文是否携带checksum。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

查询系统发送的UDP报文是否携带checksum：

```
LST UDPCHECKSUM:;
```

```
RETCODE = 0  操作成功。

结果如下
--------
UDP Type     Checksum 开关

L2TP-CTRL    使能       
L2TP-DATA    不使能           
PFCP         使能          
(结果个数 = 3)
---    END
```

#### 输出结果说明

参见SET UDPCHECKSUM的参数说明。