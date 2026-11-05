# 查询GGSN属性配置信息(LST GGSNCHARACT)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用网元：SGSN**

该命令用于查询GGSN的属性信息。

#### 注意事项

- 该命令执行后立即生效。
- 当不输入查询条件时，显示所有记录信息。

#### 本地用户权限

manage-ug；system-ug；monitor-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识     | 参数名称         | 参数说明                                                                                                                                                                                                                                      |
|:---------|:-------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RANGE    | 对端设备范围       | 可选必选说明：可选参数 参数含义：该参数用于指定需要设置属性信息的对端GGSN范围。 取值范围：“ALL_GGSN（所有GGSN）”“Gn_GGSN（Gn接口GGSN）”“Gp_GGSN（Gp接口GGSN）”、“SPECIAL_GGSN（指定GGSN）” 默认值：无                                                                                                     |
| IPT      | IP地址类型       | 可选必选说明：可选参数 参数含义：该参数用于指定GGSN信令面IP地址类型。 前提条件：只有在“RANGE”配置为“SPECIAL_GGSN（指定GGSN）”时，该参数有效。 取值范围：“IPV4(IPV4)”“IPV6(IPV6)” 默认值：无                                                                                                               |
| GGSNIPV4 | GGSN的信令面IP地址 | 可选必选说明：可选参数 参数含义：该参数用于指定GGSN信令面IPV4地址。 前提条件：只有在“IPT”配置为“IPV4”时，该参数有效。 取值范围：0.0.0.1～255.255.255.254 默认值：无 配置原则：有效的IPV4地址不能为0.0.0.0、255.255.255.255和环回地址（127.x.y.z）。有效的IPV4地址必须是A、B或者C类地址。                                                  |
| MASKV4   | 掩码           | 可选必选说明：可选参数 参数含义：该参数用于指定对端GGSN的信令面IPV4地址的掩码。 前提条件：只有在“IPT”配置为“IPV4”时，该参数有效。 取值范围：0.0.0.1～255.255.255.255 默认值： 无  说明： 输入的掩码要求对应的二进制值1和1之间不允许存在0。例如：“255.255.0.0”是有效掩码；“123.123.123.123”是无效掩码。因为123对应的二进制为“1111011”，1之间存在0。                 |
| GGSNIPV6 | GGSN的信令面IP地址 | 可选必选说明：可选参数 参数含义：该参数用于指定GGSN信令面IPV6地址。 前提条件：只有在“IPT”配置为“IPV6”时，该参数有效。 取值范围：::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF 默认值：无 配置原则：IPV6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址（::1）、链路本地地址（FE80::/10）和组播地址（FF00::/8） |
| MASKV6   | 子网前缀长度       | 可选必选说明：可选参数 参数含义：该参数用于指定子网前缀的长度。 前提条件：只有在“IPT”配置为“IPV6”时，该参数有效。 取值范围：1～128（数值型） 默认值： 无                                                                                                                                                    |

#### 使用实例

1. 不输入查询条件，查询表中全部GGSN的属性信息：

   LST GGSNCHARACT:;

   ```
   %%LST GGSNCHARACT:;%%
   RETCODE = 0  操作成功。

   GGSN属性配置表
   --------------
   对端设备范围    GGSN是否支持DirectTunnel    GGSN支持的QoS版本    GCDR/e-GCDR信息上报    发送私有信息    GnGp接口的GTP-C路径版本规则    GGSN是否支持Smart Paging    GGSN是否支持VIP    GGSN用户面IP地址类型    描述

   所有GGSN        不支持                      R99QOS               NULL                   OFF             V1                             否                          不支持             IPV4                    NULL
   Gn接口GGSN      不支持                      R99QOS               NULL                   OFF             V1                             否                          不支持             IPV4                    NULL
   Gp接口GGSN      不支持                      R99QOS               NULL                   OFF             V1                             否                          不支持             IPV4                    NULL
   (结果个数 = 3)
   ---    END
   ```
2. 查询“RANGE（对端设备范围）”为“Gn\_GGSN（Gn接口GGSN）”的配置数据:

   LST GGSNCHARACT: RANGE=Gn\_GGSN;

   ```
   %%LST GGSNCHARACT: RANGE=Gn_GGSN;%%
   RETCODE = 0  操作成功。

   GGSN属性配置表
   --------------
                  对端设备范围  =  Gn接口GGSN
      GGSN是否支持DirectTunnel  =  不支持
             GGSN支持的QoS版本  =  R99QOS
           GCDR/e-GCDR信息上报  =  NULL
                  发送私有信息  =  OFF
   GnGp接口的GTP-C路径版本规则  =  V1
      GGSN是否支持Smart Paging  =  否
               GGSN是否支持VIP  =  不支持
          GGSN用户面IP地址类型  =  IPV4
                          描述  =  NULL
   (结果个数 = 1)
   ---    END
   ```

#### 输出结果说明

请参考**ADD GGSNCHARACT**命令参数说明。