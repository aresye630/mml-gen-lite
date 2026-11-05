# 显示媒体中继DNS服务器状态（DSP RELAYDNSSTATUS）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用NF：UPF、PGW-U**

该命令用于显示媒体中继DNS服务器状态。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识          | 参数名称      | 参数说明                                                                                                                                                                          |
|:--------------|:----------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DNSSERVERNAME | DNS服务器名称  | 可选必选说明：必选参数 参数含义：该参数用于指定DNS服务器名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～31。不支持空格，不区分大小写。 默认值：无 配置原则： 该参数使用ADD RELAYDNSSERVER命令配置生成。该取值必须和ADD RELAYDNSSERVER中配置的“DNSSERVERNAME”参数取值相同。 |
| PODID         | PodID     | 可选必选说明：可选参数 参数含义：该参数用于指定查询的POD。 数据来源：本端规划 取值范围：字符串类型，输入长度范围是1~63。不支持空格，区分大小写。 默认值：无 配置原则：无                                                                                    |
| SERVICEID     | ServiceID | 可选必选说明：可选参数 参数含义：该参数用于指定查询的ServiceID。 数据来源：本端规划 取值范围：整数类型，取值范围0~39。 默认值：无 配置原则：无                                                                                              |

#### 使用实例

显示媒体中继DNS服务器状态：

```
DSP RELAYDNSSTATUS: DNSSERVERNAME="test01";
```

```
RETCODE = 0  操作成功

结果如下
------------------------
DNS服务器名称    PodID        ServiceID  IPv4主DNS服务器状态            IPv4备DNS服务器状态           IPv6主DNS服务器状态            IPv6备DNS服务器状态

test01           relay-pod-0  7          Normal                         Normal                        None                           None
test01           relay-pod-0  6          Normal                         Normal                        None                           None
test01           relay-pod-0  1          Normal                         Normal                        None                           None
test01           relay-pod-0  5          Normal                         Normal                        None                           None
test01           relay-pod-0  0          Normal                         Normal                        None                           None
test01           relay-pod-0  2          Normal                         Normal                        None                           None
test01           relay-pod-0  3          Normal                         Normal                        None                           None
test01           relay-pod-0  4          Normal                         Normal                        None                           None
(结果个数 = 8)

---    END
```

#### 输出结果说明

| 输出项名称         | 输出项解释             |
|:--------------|:------------------|
| DNS服务器名称      | 用于指定DNS服务器名称。     |
| PodID         | 用于指定查询的POD。       |
| ServiceID     | 用于指定查询的ServiceID。 |
| IPv4主DNS服务器状态 | 表示IPv4主DNS服务器状态。  |
| IPv4备DNS服务器状态 | 表示IPv4备DNS服务器状态。  |
| IPv6主DNS服务器状态 | 表示IPv6主DNS服务器状态。  |
| IPv6备DNS服务器状态 | 表示IPv6备DNS服务器状态。  |