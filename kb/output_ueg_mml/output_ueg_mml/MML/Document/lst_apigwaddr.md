# 查询API GW地址（LST APIGWADDR）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：UPF、MPF**

API GW使用主机型网络时，可使用该命令查询API GW的IP地址。

#### 注意事项

该命令执行后立即生效。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

查询API GW的IP地址：

```
LST APIGWADDR:;
```

```
RETCODE = 0  操作成功

API GW地址
----------
           访问地址类型  =  IPv4
        API GW IPv4地址  =  10.0.0.2
        API GW IPv4网关  =  10.0.0.1
    API GW IPv4掩码地址  =  255.255.255.0
        API GW IPv6地址  =  ::
        API GW IPv6网关  =  ::
API GW IPv6地址掩码长度  =  0
(结果个数 = 1)
```

#### 输出结果说明

参见ADD APIGWADDR的参数说明。