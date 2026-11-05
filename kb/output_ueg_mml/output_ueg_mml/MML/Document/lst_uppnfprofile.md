# 查询对端NF实例概述信息（LST UPPNFPROFILE）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：UPF**

该命令用于查询本地配置的对端NF实例的概述信息。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

查询对端LMF实例的概述信息：

```
LST UPPNFPROFILE:;
```

```
RETCODE = 0  操作成功

对端NF实例概述信息
------------------
NF实例标识                            NF类型  NF状态      域名      IP地址类型  IPV4地址1     IPV4地址2  IPV4地址3  IPV4地址4  IPV6地址1         IPV6地址2  IPV6地址3  IPV6地址4  端口号  容量  优先级  负载  协议模式
   
43_udm_instance_0                     NfUDM   Registered  NULL      IPv4v6      192.168.0.1   0.0.0.0    0.0.0.0    0.0.0.0    ::                ::         ::         ::         8080    100   0       0     NULL           
scp_instance_0                        NfSCP   Registered  scp1.com  IPv4        192.168.0.2   0.0.0.0    0.0.0.0    0.0.0.0    ::                ::         ::         ::         5064    100   1       0     http           
scp_instance_1                        NfSCP   Registered  scp2.com  IPv4        192.168.0.3   0.0.0.0    0.0.0.0    0.0.0.0    ::                ::         ::         ::         5064    100   2       0     http 
(结果个数 = 3)

---    END
```

#### 输出结果说明

参见ADD UPPNFPROFILE的参数说明。