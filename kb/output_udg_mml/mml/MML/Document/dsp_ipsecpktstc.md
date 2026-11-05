# 查询IPsec报文统计信息（DSP IPSECPKTSTC）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于查询IPsec报文统计信息。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

查询IPsec报文统计信息：

```
DSP IPSECPKTSTC:;
```

```
RETCODE = 0  操作成功。

结果如下
--------
组件ID        IPv6 ESP socket入向总报文数    IPv6 ESP socket入向处理成功报文数    IPv6 ESP socket入向丢弃报文数    IPv6 ESP socket出向总报文数    IPv6 ESP socket出向处理成功报文数    IPv6 ESP socket出向丢弃报文数    IPv6 AH socket入向总报文数    IPv6 AH socket入向处理成功报文数    IPv6 AH socket入向丢弃报文数    IPv6 AH socket出向总报文数    IPv6 AH socket出向处理成功报文数    IPv6 AH socket出向丢弃报文数    IPv4 ESP socket入向总报文数    IPv4 ESP socket入向处理成功报文数    IPv4 ESP socket入向丢弃报文数    IPv4 ESP socket出向总报文数    IPv4 ESP socket出向处理成功报文数    IPv4 ESP socket出向丢弃报文数    IPv4 AH socket入向总报文数    IPv4 AH socket入向处理成功报文数    IPv4 AH socket入向丢弃报文数    IPv4 AH socket出向总报文数    IPv4 AH socket出向处理成功报文数    IPv4 AH socket出向丢弃报文数

0x803f0098    0                              0                                    0                                0                              0                                    0                                0                             0                                   0                               0                             0                                   0                               0                              0                                    0                                0                              0                                    0                                0                             0                                   0                               0                             0                                   0                           
0x803f0022    0                              0                                    0                                0                              0                                    0                                0                             0                                   0                               0                             0                                   0                               0                              0                                    0                                0                              0                                    0                                0                             0                                   0                               0                             0                                   0                           
0x803f0021    0                              0                                    0                                0                              0                                    0                                0                             0                                   0                               0                             0                                   0                               0                              0                                    0                                0                              0                                    0                                0                             0                                   0                               0                             0                                   0                           
(结果个数 = 3)
---    END
```

#### 输出结果说明

| 输出项名称                    | 输出项解释                     |
|:-------------------------|:--------------------------|
| 组件ID                     | 组件ID。                     |
| IPv6 ESP socket入向总报文数    | IPv6 ESP socket入向总报文数。    |
| IPv6 ESP socket入向处理成功报文数 | IPv6 ESP socket入向处理成功报文数。 |
| IPv6 ESP socket入向丢弃报文数   | IPv6 ESP socket入向丢弃报文数。   |
| IPv6 ESP socket出向总报文数    | IPv6 ESP socket出向总报文数。    |
| IPv6 ESP socket出向处理成功报文数 | IPv6 ESP socket出向处理成功报文数。 |
| IPv6 ESP socket出向丢弃报文数   | IPv6 ESP socket出向丢弃报文数。   |
| IPv6 AH socket入向总报文数     | IPv6 AH socket入向总报文数。     |
| IPv6 AH socket入向处理成功报文数  | IPv6 AH socket入向处理成功报文数。  |
| IPv6 AH socket入向丢弃报文数    | IPv6 AH socket入向丢弃报文数。    |
| IPv6 AH socket出向总报文数     | IPv6 AH socket出向总报文数。     |
| IPv6 AH socket出向处理成功报文数  | IPv6 AH socket出向处理成功报文数。  |
| IPv6 AH socket出向丢弃报文数    | IPv6 AH socket出向丢弃报文数。    |
| IPv4 ESP socket入向总报文数    | IPv4 ESP socket入向总报文数。    |
| IPv4 ESP socket入向处理成功报文数 | IPv4 ESP socket入向处理成功报文数。 |
| IPv4 ESP socket入向丢弃报文数   | IPv4 ESP socket入向丢弃报文数。   |
| IPv4 ESP socket出向总报文数    | IPv4 ESP socket出向总报文数。    |
| IPv4 ESP socket出向处理成功报文数 | IPv4 ESP socket出向处理成功报文数。 |
| IPv4 ESP socket出向丢弃报文数   | IPv4 ESP socket出向丢弃报文数。   |
| IPv4 AH socket入向总报文数     | IPv4 AH socket入向总报文数。     |
| IPv4 AH socket入向处理成功报文数  | IPv4 AH socket入向处理成功报文数。  |
| IPv4 AH socket入向丢弃报文数    | IPv4 AH socket入向丢弃报文数。    |
| IPv4 AH socket出向总报文数     | IPv4 AH socket出向总报文数。     |
| IPv4 AH socket出向处理成功报文数  | IPv4 AH socket出向处理成功报文数。  |
| IPv4 AH socket出向丢弃报文数    | IPv4 AH socket出向丢弃报文数。    |