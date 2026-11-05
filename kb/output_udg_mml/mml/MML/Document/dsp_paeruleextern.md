# 显示PAE上外联口规则信息（DSP PAERULEEXTERN）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于显示PAE外联口的分发规则。

PAE接收到报文，根据配置的规则，找到对应的虚拟通信端口后将报文从对应的端口发送出去。

通过该命令可查看PAE模块端口的分发规则，通过获取的信息，可了解配置是否正常，并进行故障诊断。

#### 注意事项

该命令执行后立即生效。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识         | 参数名称   | 参数说明                                                                                                                                                                    |
|:-------------|:-------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CELLTYPE     | 微服务类型  | 可选必选说明：必选参数 参数含义：该参数用于指定微服务类型。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为0～63。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。 默认值：无 配置原则：使用DSP PAENODE查看微服务类型。    |
| CELLINSTANCE | 微服务实例号 | 可选必选说明：必选参数 参数含义：该参数用于指定微服务实例号。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为0～127。数字“0～9”、大写字母“A～Z”、小写字母“a～z”、特殊字符“-”、“_”、“.”、“+”、空格符以及中文字符，其他均为非法字符。 默认值：无 配置原则：使用DSP PAENODE查看微服务实例号。 |

#### 使用实例

显示微服务类型为“aa”微服务实例为“aa”的外联口的分发规则：

```
DSP PAERULEEXTERN:CELLTYPE="aa", CELLINSTANCE="aa";
```

```
RETCODE = 0  操作成功。

结果如下
-------------------------
端口ID    默认队列ID    负载均衡哈希值类型     下一个表项    QoS负载均衡类型          默认队列组ID    TB低32位地址    TP        TB高16位地址    VPN实例索引    特殊类型报文TP
 
2         0             PAE_HASH_DEEP_PARSE    0             PAE_QOSBATYPE_DEFAULT    0x0             0x0             0x1001    0x0             0              0xffffffff  
3         0             PAE_HASH_DEEP_PARSE    0             PAE_QOSBATYPE_DEFAULT    0x0             0x0             0x1001    0x0             0              0xffffffff
4         0             PAE_HASH_DEEP_PARSE    0             PAE_QOSBATYPE_DEFAULT    0x0             0x0             0x1001    0x0             0              0xffffffff
5         0             PAE_HASH_DEEP_PARSE    0             PAE_QOSBATYPE_DEFAULT    0x0             0x0             0x1001    0x0             0              0xffffffff
6         0             PAE_HASH_DEEP_PARSE    0             PAE_QOSBATYPE_DEFAULT    0x0             0x0             0x1001    0x0             0              0xffffffff
7         0             PAE_HASH_DEEP_PARSE    0             PAE_QOSBATYPE_DEFAULT    0x0             0x0             0x1001    0x0             0              0xffffffff
8         0             PAE_HASH_DEEP_PARSE    0             PAE_QOSBATYPE_DEFAULT    0x0             0x0             0x1001    0x0             0              0xffffffff
9         0             PAE_HASH_DEEP_PARSE    0             PAE_QOSBATYPE_DEFAULT    0x0             0x0             0x1001    0x0             0              0xffffffff
(结果个数 = 8)
---    END
```

#### 输出结果说明

| 输出项名称     | 输出项解释                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|:----------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 端口ID      | 端口ID。                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 默认队列ID    | 默认队列ID。                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| 负载均衡哈希值类型 | 虚拟机（裸机）或容器上流量负载均衡的哈希值计算规则类型： PAE_HASH_DEFAULT：缺省处理，使用默认的哈希值。PAE_HASH_ETHTYPE：EthType规则，以以太类型为key计算哈希值。PAE_HASH_PORT：Port规则，以端口号为key计算哈希值。PAE_HASH_VLAN：VLAN规则，以VLAN ID为key计算哈希值。PAE_HASH_VPN_IP3T：三元组规则，以IP协议类型、源IP、目的IP为key计算哈希值。PAE_HASH_VPN_IP5T：五元组规则，以IP协议类型、源IP、目的IP、源端口、目的端口为key计算哈希值。PAE_HASH_DEEP_PARSE：深度解析规则，根据不同的报文类型匹配不同的规则计算哈希值。PAE_HASH_INNER_IP5T：内层五元组规则，以内层IP协议类型、源IP、目的IP、源端口、目的端口为key计算哈希值。                                                               |
| 下一个表项     | 报文处理时，下一步需要查询的表项。                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| QoS负载均衡类型 | 报文优先级到内部优先级映射规则类型： PAE_QOSBATYPE_DEFAULT：缺省处理，不查表，使用默认值作为队列优先级。PAE_QOSBATYPE_8021P：802.1P映射规则，根据VLAN优先级字段为key查表。PAE_QOSBATYPE_DSCP：DSCP映射规则，根据IP头中DSCP字段为key查表。PAE_QOSBATYPE_TOS：TOS映射规则，根据IP头中TOS字段为key查表。PAE_QOSBATYPE_EXP：EXP映射规则，根据MPLS头中EXP字段为key查表。PAE_QOSBATYPE_PROTOCOL：PROTOCOL映射规则，根据报文类型为key查表。PAE_QOSBATYPE_AUTO_DSCP：AUTO_DSCP映射规则；对IP报文，根据IP头中DSCP字段为key查表；对非IP报文，根据报文类型为key查表。PAE_QOSBATYPE_AUTO_TOS：AUTO_TOS映射规则；对IP报文，根据IP头中TOS字段为key查表；对非IP报文，根据报文类型为key查表。 |
| 默认队列组ID   | 默认队列组ID。                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| TB低32位地址  | 协议报文中TB低32位地址。                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| TP        | 协议报文中目标TP。                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| TB高16位地址  | 协议报文中TB高16位地址。                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| VPN实例索引   | VPN索引，取值范围：{0~65535}。                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| 特殊类型报文TP  | 外联口收到诸如CSLB等特殊类型报文时，会上送到该TP下绑定的channel中                                                                                                                                                                                                                                                                                                                                                                                                                                       |