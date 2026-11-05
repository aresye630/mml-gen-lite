# 查询UPF向PDN服务器发送探测消息的探测路径配置（LST PDNROUTETSTPATH）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：PGW-U、UPF**

该命令用来查询UPF向PDN服务器自动发送探测消息的路径配置。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识     | 参数名称   | 参数说明                                                                                                                |
|:---------|:-------|:--------------------------------------------------------------------------------------------------------------------|
| PATHNAME | 路径名称   | 可选必选说明：可选参数 参数含义：该参数用于指定用于连通性探测的路径名。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。不支持空格，不区分大小写。 默认值：无 配置原则：配置的路径名称应满足路径名称的取值范围。 |

#### 使用实例

查询配置路径名称为test1的探测路径配置：

```
LST PDNROUTETSTPATH: PATHNAME="test1";
```

```
RETCODE = 0  Operation succeeded

UPF向PDN服务器发送探测消息的探测路径配置
------------------------
                      Path Name  =  test1
                      Path Type  =  DNS
                      Pool Name  =  pool-test
                IP Address Type  =  IPV4
       Destination IPv4 Address  =  10.1.1.1
Destination IPv6 Prefix Address  =  ::
                     DSCP Value  =  0
              Route Test Method  =  PING
          Packet Payload Length  =  100
            Traffic-Class Value  =  0
                         domain  =  NULL
(结果个数 = 1)
```

#### 输出结果说明

| 输出项名称                           | 输出项解释           |
|:--------------------------------|:----------------|
| Path Name                       | 路径名称。           |
| Path Type                       | 路径类型。           |
| Pool Name                       | 地址池名称。          |
| IP Address Type                 | IP类型。           |
| Destination IPv4 Address        | 目的IPV4地址。       |
| Destination IPv6 Prefix Address | 目的IPV6前缀地址。     |
| DSCP Value                      | DSCP值。          |
| Route Test Method               | 路由测试方法。         |
| Packet Payload Length           | 数据包有效负载长度。      |
| Traffic-Class Value             | Traffic-Class值。 |
| domain                          | 域名。             |