# 查询BGP所有VPN对等体详细信息（DSP BGPPEERALLVERBOSE）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于显示BGP所有VPN对等体的详细信息。

#### 注意事项

该命令执行后立即生效。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识          | 参数名称        | 参数说明                                                                                                                                                                       |
|:--------------|:------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ALL           | BGP所有VPN对等体 | 可选必选说明：必选参数 参数含义：该参数用于指定是否输出BGP所有VPN对等体信息。 数据来源：本端规划 取值范围：枚举类型。 true：是。 默认值：无                                                                                              |
| AFTYPE        | 地址族类型       | 可选必选说明：必选参数 参数含义：该参数用于指定VPN的地址族类型。 数据来源：本端规划 取值范围：枚举类型。 ipv4vpn：VPNv4地址族。ipv6vpn：VPNv6地址族。 默认值：无 配置原则：此命令中ipv4vpn地址族可以支持VPNv4和私网IPv4单播的查询，ipv6vpn地址族可以支持VPNv6和私网IPv6单播的查询。 |
| REMOTEADDRESS | 对等体地址       | 可选必选说明：可选参数 参数含义：该参数用于指定对等体地址。 数据来源：对端协商 取值范围：字符串类型，输入长度范围为1～39。取值为一个IP地址。 默认值：无 配置原则：指定对等体地址时，查询结果是对应的VPNv4或VPNv6地址族下的对等体详细信息，不查询私网IPv4单播、私网IPv6单播地址族下的对等体详细信息。           |

#### 使用实例

显示BGP所有VPN对等体详细信息：

```
DSP BGPPEERALLVERBOSE:ALL=true,AFTYPE=ipv4vpn;
```

```
RETCODE = 0  操作成功。

结果如下
------------------------
BGP对等体详细信息 =
         BGP Peer is 10.1.1.2,  remote AS 300
         Type: EBGP link
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
Minimum route advertisement interval is  0seconds
Optional capabilities:
Route refresh capability has been enabled
4-byte-as capability has been enabled
Peer Preferred Value: 0
Routing policy configured:
No routing policy is configured

 IPv4-family for VPN instance:   vpna
         BGP Peer is 10.1.1.1,  remote AS 100
         Type: IBGP link
         BGP version 4, Remote router ID 0.0.0.0
         Update-group ID: 3
         BGP current state: Active
         BGP current event: TcpFail
         BGP last state: Connect
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

(结果个数 = 2)
---    END
```

#### 输出结果说明

| 输出项名称      | 输出项解释           |
|:-----------|:----------------|
| BGP对等体详细信息 | 用于输出BGP对等体详细信息。 |