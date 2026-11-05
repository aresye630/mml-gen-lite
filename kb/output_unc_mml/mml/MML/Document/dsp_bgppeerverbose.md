# 查询BGP对等体详细信息（DSP BGPPEERVERBOSE）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于显示BGP对等体的详细信息。

#### 注意事项

该命令执行后立即生效。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识            | 参数名称      | 参数说明                                                                                                                                                                                |
|:----------------|:----------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| VRFNAME         | VPN实例名称   | 可选必选说明：可选参数 参数含义：该参数用于指定用户所配置的VPN实例名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～31。 默认值：_public_ 配置原则：使用LST L3VPNINST命令查看可用VPN。                                                                |
| AFTYPE          | 地址族类型     | 可选必选说明：必选参数 参数含义：该参数用于指定VRF的地址族类型。 数据来源：本端规划 取值范围：枚举类型。 ipv4uni：IPv4地址族。ipv4vpn：VPNv4地址族。ipv6uni：IPv6地址族。ipv6vpn：VPNv6地址族。 默认值：无                                                    |
| ADDRESSTYPE     | 地址类型      | 可选必选说明：条件可选参数 前提条件：该参数在“AFTYPE”配置为“ipv6uni”时为可选参数。 参数含义：该参数用于指定对等体的地址类型。 数据来源：本端规划 取值范围：枚举类型。 ipv4：IPv4。ipv6：IPv6。 默认值：无                                                            |
| REMOTEADDRESSV4 | 对等体IPv4地址 | 可选必选说明：条件可选参数 前提条件：该参数在“ADDRESSTYPE”配置为“ipv4”时为可选参数。 可选必选说明：条件可选参数 前提条件：该参数在“AFTYPE”配置为“ipv4uni”、“ipv4vpn” 或 “ipv6vpn”时为可选参数。 参数含义：该参数用于给定对等体IPv4地址。 数据来源：本端规划 取值范围：IPv4地址类型。 默认值：无 |
| REMOTEADDRESSV6 | 对等体IPv6地址 | 可选必选说明：条件可选参数 前提条件：该参数在“ADDRESSTYPE”配置为“ipv6”时为可选参数。 参数含义：该参数用于给定对等体IPv6地址。 数据来源：本端规划 取值范围：IPv6地址类型。 默认值：无                                                                          |
| SOURCEIFNAME    | 多源接口名称    | 可选必选说明：可选参数 参数含义：该参数用于给定多源对等体的接口名。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。 默认值：无 配置原则：仅支持Ethernet及其子接口类型，不区分大小写。                                                                          |

#### 使用实例

显示BGP对等体详细信息：

```
DSP BGPPEERVERBOSE:VRFNAME="vpna",AFTYPE=ipv4uni,REMOTEADDRESSV4="10.1.1.1";
```

```
RETCODE = 0  操作成功。

结果如下
------------------------
BGP对等体详细信息  =
         BGP Peer is 10.1.1.1,  remote AS 100
         Type: IBGP link
         BGP version 4, Remote router ID 0.0.0.0
         Update-group ID: 3
         BGP current state: Idle
         BGP current event: IHTimerExpired
         BGP last state: Idle
         BGP Peer Up count: 0
         Configured: Connect-retry Time: 32 sec
Received: Total 0  messages
                  Update messages               0
                  Open messages                 0
                  KeepAlive messages            0
                  Notification messages         0
                  Refresh messages              0
Sent: Total 0  messages
                  Update messages               0
                  Open messages                 0
                  KeepAlive messages            0
                  Notification messages         0
                  Refresh messages              0
Authentication type configured: None
No keepalive received since peer has been configured
No keepalive sent since peer has been configured
No update received since peer has been configured
No update sent since peer has been configured
No refresh received since peer has been configured
No refresh sent since peer has been configured
Minimum route advertisement interval is  15seconds
Optional capabilities:
Route refresh capability has been enabled
4-byte-as capability has been enabled
Peer Preferred Value: 0
Routing policy configured:
No routing policy is configured

(结果个数 = 1)
 ---    END
```

#### 输出结果说明

| 输出项名称      | 输出项解释           |
|:-----------|:----------------|
| BGP对等体详细信息 | 用于输出BGP对等体详细信息。 |