# 删除VPN实例（RMV CPVPNINST）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**须知** 

此操作会去中断业务，请确认与该VPN相关的配置已经删除，比如逻辑接口、IPSQMSHAPING、跟踪重定向等配置。

**适用NF：SGW-C、PGW-C、SMF、GGSN**

该命令用于删除指定的VPN实例。

## 注意事项

- 该命令执行后立即生效。

- “\_public\_”是公网缺省VPN的实例名，不允许用户删除。
- 删除的VPN实例必须为已经创建的VPN实例名称。
- 执行RMV CPVPNINST前，需要执行LST CPLOGICINF、LST CPPCRF、LST OCS、LST DRA、LST RDSSVR、LST CPSCTPASSOC、LST CPADDRPOOL、LST BLACKLIST、LST CPAPN、LST DHCPSERVERGRP命令检查要被删除的VPN实例是否被某个对象绑定。当要被删除的VPN实例被其中一个对象绑定时，VPN实例不能被删除。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识        | 参数名称   | 参数说明                                                                                           |
|:------------|:-------|:-----------------------------------------------------------------------------------------------|
| VPNINSTANCE | VPN实例名 | 可选必选说明：必选参数  参数含义：该参数用于指定VPN实例。  数据来源：全网规划  取值范围：字符串类型，输入长度范围是1~31。区分大小写，不支持空格。  默认值：无  配置原则：无 |

## 使用实例

删除VPNInst业务配置，VPN实例名称为vpn1：

```
RMV CPVPNINST:VPNINSTANCE="vpn1";
```