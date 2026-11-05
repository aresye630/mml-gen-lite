# 查询批量路径探测结果（DSP PATHSTSTRESULT）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：SGW-U、PGW-U、UPF**

该命令用来查询路径批量探测命令的结果。此命令仅显示异常路径的结果，最多显示100条异常路径记录。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识        | 参数名称     | 参数说明                                                                                                             |
|:------------|:---------|:-----------------------------------------------------------------------------------------------------------------|
| VPNNAME     | vpn名字    | 可选必选说明：可选参数 参数含义：指定本端IP地址对应逻辑接口绑定的VPN，即对端网元所在的VPN实例名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～31。 默认值：无 配置原则：无            |
| SRCIPV4ADDR | 源IPv4地址  | 可选必选说明：条件必选参数 前提条件：该参数在“IPVERSION”配置为“IPV4”时为必选参数。 参数含义：探测源IP地址。 数据来源：本端规划 取值范围：IPv4地址类型。点分十进制形式。 默认值：无 配置原则：无   |
| IPVERSION   | IP地址版本类型 | 可选必选说明：必选参数 参数含义：IP地址版本类型。 数据来源：本端规划 取值范围：枚举类型。 IPV4：表示地址类型为IPv4。IPV6：表示地址类型为IPv6。 默认值：无 配置原则：无                  |
| SRCIPV6ADDR | 源IPv6地址  | 可选必选说明：条件必选参数 前提条件：该参数在“IPVERSION”配置为“IPV6”时为必选参数。 参数含义：指定源IPv6地址。 数据来源：本端规划 取值范围：IPv6地址类型。点分十进制形式。 默认值：无 配置原则：无 |

#### 使用实例

查询源IP是192.168.21.4的路径批量探测结果：

```
DSP PATHSTSTRESULT: IPVERSION=IPV4, SRCIPV4ADDR="192.168.21.4";
```

```
RETCODE = 0  Operation Success.

Paths Test Result Info
----------------------
Result  =  
Source IP: 192.168.21.4                            VPN-instance: NULL
Total Paths Number: 3   Detected Paths Number: 3   Abnormal Paths Number: 3
Start Time: 15:51:25  End Time: 15:52:02 
Abnormal Paths Information: 
---------------------------------------
Source IP                               Destination IP
192.168.21.4                            192.168.1.1
192.168.21.4                            192.168.1.2
192.168.21.4                            192.168.1.3
(Number of results = 1)
---    END
```

#### 输出结果说明

| 输出项名称                 | 输出项解释              |
|:----------------------|:-------------------|
| Source IP             | 路径探测的源IP地址。        |
| VPN-instance          | 路径探测的源IP地址绑定的VPN。  |
| Total Paths Number    | 本次需要探测的路径总数。       |
| Detected Paths Number | 执行查询命令时已经探测的路径数。   |
| Abnormal Paths Number | 执行查询命令时已经探测的异常路径数。 |
| Start Time            | 执行探测命令的时间。         |
| End Time              | 本次探测结束的时间。         |
| Destination IP        | 路径探测的目的IP地址。       |
| NE Type               | 路径探测的网元类型。         |