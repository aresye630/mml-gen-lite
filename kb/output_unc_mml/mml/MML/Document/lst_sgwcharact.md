# 查询S-GW特性对接配置(LST SGWCHARACT)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用网元：SGSN、MME**

该命令用于查询MME与S-GW支持能力交互配置策略。

输出结果顺序：

“ALL(所有S-GW)”

“SPECIFIED(指定S-GW)”的IPv4记录

“SPECIFIED(指定S-GW)”的IPv6记录

#### 注意事项

该命令执行后立即生效。

#### 本地用户权限

manage-ug；system-ug；monitor-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

无。

#### 使用实例

查询MME与S-GW支持特性的能力交互配置策略记录：

LST SGWCHARACT:;

```
%%LST SGWCHARACT:;%%
RETCODE = 0  操作成功。

所有S-GW查询结果如下
--------------------
                              对端设备范围  =  所有S-GW
                          S-GW支持NTSR功能  =  不支持
                           S-GW支持PRN功能  =  不支持
                            S-GW支持MME ID  =  不支持
   S-GW支持Secondary RAT Usage Data Report  =  不支持
                       GTPU IP类型选择策略  =  优先使用IPv4地址
S-GW支持User Location Information For S-GW  =  不支持
              S-GW支持CSR消息携带PSCELL ID  =  不支持
                         S-GW支持PSCell ID  =  不支持
                           S-GW支持PGWRNSI  =  不支持
     S-GW支持P-CSCF Restoration Indication  =  不支持
                                      描述  =  NULL
(结果个数 = 1)

指定S-GW IPv4查询结果如下
-------------------------
对端设备范围    IP地址类型    IPv4地址           IPV4地址掩码    S-GW支持NTSR功能    S-GW支持PRN功能    S-GW支持MME ID    S-GW支持Secondary RAT Usage Data Report    GTPU IP类型选择策略    S-GW支持User Location Information For S-GW    S-GW支持CSR消息携带PSCELL ID    S-GW支持PSCell ID    S-GW支持PGWRNSI    S-GW支持P-CSCF Restoration Indication    描述

指定S-GW        IPV4         10.141.149.100     255.0.0.0      不支持              不支持             不支持           不支持                                      优先使用IPv4地址       不支持                                        不支持                         不支持               不支持              不支持                                   NULL
指定S-GW        IPV4         10.141.149.180     255.255.0.0    不支持              不支持             不支持           不支持                                      优先使用IPv4地址       不支持                                        不支持                         不支持               不支持              不支持                                   NULL
指定S-GW        IPV4         10.141.149.190     255.255.0.0    不支持              不支持             不支持           不支持                                      优先使用IPv4地址       不支持                                        不支持                         不支持               不支持              不支持                                   NULL
(结果个数 = 3)

指定S-GW IPv6查询结果如下
-------------------------
对端设备范围    IP地址类型    IPv6地址                       IPV6地址前缀长度    S-GW支持NTSR功能    S-GW支持PRN功能    S-GW支持MME ID    S-GW支持Secondary RAT Usage Data Report    GTPU IP类型选择策略    S-GW支持User Location Information For S-GW    S-GW支持CSR消息携带PSCELL ID    S-GW支持PSCell ID    S-GW支持PGWRNSI    S-GW支持P-CSCF Restoration Indication    描述

指定S-GW        IPV6         2001:db8:10:19:44:55:10:12     128                不支持              不支持             不支持           不支持                                     优先使用IPv6地址       不支持                                        不支持                          不支持                不支持             不支持                                   NULL
指定S-GW        IPV6         2001:db8:10:19:44:55:10:15     128                不支持              不支持             不支持           不支持                                     优先使用IPv6地址       不支持                                        不支持                          不支持                不支持             不支持                                   NULL
(结果个数 = 2)
---    END
```

#### 输出结果说明

参见**ADD SGWCHARACT**的参数说明。