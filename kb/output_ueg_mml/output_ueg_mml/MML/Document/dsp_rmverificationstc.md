# 查询路由管理对账统计信息（DSP RMVERIFICATIONSTC）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用来查询路由管理对账统计信息。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                                   |
|:-------|:-------|:-------------------------------------------------------------------------------------------------------|
| AFTYPE | 地址族    | 可选必选说明：必选参数 参数含义：该参数用于表示路由所属VPN的地址族。 数据来源：本端规划 取值范围：枚举类型。 ipv4unicast：IPv4单播。ipv6unicast：IPv6单播。 默认值：无 |

#### 使用实例

路由管理对账统计信息：

```
DSP RMVERIFICATIONSTC:AFTYPE=ipv4unicast;
```

```
RETCODE = 0  操作成功。

结果如下
--------
Partner ID    总的对帐次数    拒绝的对帐次数    最后一次对账开始的时间    最后一次对账结束的时间

0x1           0               0                 NULL                      NULL
0x0           0               0                 NULL                      NULL
0x10004       0               0                 NULL                      NULL
0x4000B       0               0                 NULL                      NULL
0x260005      0               0                 NULL                      NULL
0x60000D      0               0                 NULL                      NULL
0x660014      0               0                 NULL                      NULL
0x670013      0               0                 NULL                      NULL
0x690029      0               0                 NULL                      NULL
0x6A0016      0               0                 NULL                      NULL
0x6F0005      0               0                 NULL                      NULL
0x700007      0               0                 NULL                      NULL
0x72000F      0               0                 NULL                      NULL
0x74001F      0               0                 NULL                      NULL
0x77000B      0               0                 NULL                      NULL
0x790012      0               0                 NULL                      NULL
0x7A0011      0               0                 NULL                      NULL
0x8C0017      0               0                 NULL                      NULL
0x8F0015      0               0                 NULL                      NULL
0x97001E      0               0                 NULL                      NULL
0xA60021      0               0                 NULL                      NULL
0xB00022      0               0                 NULL                      NULL
0xCA2712      0               0                 NULL                      NULL
0xD5000E      0               0                 NULL                      NULL
0xE7000C      0               0                 NULL                      NULL
0x1970020     0               0                 NULL                      NULL
0x1DA0003     0               0                 NULL                      NULL
0x1DD000B     0               0                 NULL                      NULL
0x208001B     0               0                 NULL                      NULL
0x2FB003C     0               0                 NULL                      NULL
0x3DD000A     0               0                 NULL                      NULL
0x404001A     0               0                 NULL                      NULL
0xBEF001D     0               0                 NULL                      NULL
0xBF1001C     0               0                 NULL                      NULL
(结果个数 = 34)
---    END
```

#### 输出结果说明

| 输出项名称       | 输出项解释            |
|:------------|:-----------------|
| Partner ID  | 用于表示Partner ID。  |
| 总的对帐次数      | 用于表示总的对帐次数。      |
| 拒绝的对帐次数     | 用于表示拒绝的对帐次数。     |
| 最后一次对账开始的时间 | 用于表示最后一次对账开始的时间。 |
| 最后一次对账结束的时间 | 用于表示最后一次对账结束的时间。 |