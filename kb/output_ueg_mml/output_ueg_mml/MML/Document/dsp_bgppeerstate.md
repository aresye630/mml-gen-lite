# 查询BGP对等体状态信息（DSP BGPPEERSTATE）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于显示BGP对等体的状态信息。

#### 注意事项

该命令执行后立即生效。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识            | 参数名称      | 参数说明                                                                                                                                                                                |
|:----------------|:----------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| VRFNAME         | VPN实例名称   | 可选必选说明：可选参数 参数含义：该参数用于指定用户所配置的VPN实例名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～31。 默认值：_public_ 配置原则：使用LST L3VPNINST命令查看可用VPN。                                                                |
| AFTYPE          | 地址族类型     | 可选必选说明：必选参数 参数含义：该参数用于指定VRF的地址族类型。 数据来源：本端规划 取值范围：枚举类型。 ipv4uni：IPv4地址族。ipv4vpn：VPNv4地址族。ipv6uni：IPv6地址族。ipv6vpn：VPNv6地址族。 默认值：无                                                    |
| ADDRESSTYPE     | 地址类型      | 可选必选说明：条件必选参数 前提条件：该参数在“AFTYPE”配置为“ipv6uni”时为必选参数。 参数含义：该参数用于指定对等体的地址类型。 数据来源：本端规划 取值范围：枚举类型。 ipv4：IPv4。ipv6：IPv6。 默认值：无                                                            |
| REMOTEADDRESSV4 | 对等体IPv4地址 | 可选必选说明：条件必选参数 前提条件：该参数在“ADDRESSTYPE”配置为“ipv4”时为必选参数。 可选必选说明：条件必选参数 前提条件：该参数在“AFTYPE”配置为“ipv4uni”、“ipv4vpn” 或 “ipv6vpn”时为必选参数。 参数含义：该参数用于给定对等体IPv4地址。 数据来源：本端规划 取值范围：IPv4地址类型。 默认值：无 |
| REMOTEADDRESSV6 | 对等体IPv6地址 | 可选必选说明：条件必选参数 前提条件：该参数在“ADDRESSTYPE”配置为“ipv6”时为必选参数。 参数含义：该参数用于给定对等体IPv6地址。 数据来源：本端规划 取值范围：IPv6地址类型。 默认值：无                                                                          |
| SOURCEIFNAME    | 多源接口名称    | 可选必选说明：可选参数 参数含义：该参数用于给定多源对等体的接口名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。 默认值：无 配置原则：仅支持Ethernet及其子接口类型，不区分大小写。                                                                         |

#### 使用实例

显示BGP对等体状态信息：

```
DSP BGPPEERSTATE:VRFNAME="vpna",AFTYPE=ipv4uni,REMOTEADDRESSV4="10.1.1.1";
```

```
RETCODE = 0  操作成功。

结果如下
------------------------
BGP对等体状态信息  =
Last   Read     : -----
Last   Write    : -----
Last Try Connect: 2016-07-02 07:23:14
Last Try Create Connect Fail Reason: BNM_FAIL_SYNCHRONIZE_VRF_CFG
Last Peer Down Reason: 4
Last Recv Msg Time: -----
Last Send Msg Time: -----
BFD State: 0, BFD PrevState: 0, BFD Fsm Event: 0
BFD State: 0, BFD PrevState: 0, BFD Fsm Event: 0

Event Timers:
TimerID          Name        Type         Mode         TimerLeft(ms)     Expire
Times
0                CRTimer     CYCLIC       IDLE         -----             0

0                KATimer     CYCLIC       IDLE         -----             0

0                HLTimer     CYCLIC       IDLE         -----             0

139807697692080  IHTimer     CYCLIC       RUNNING      9000              7

0                DOTimer     CYCLIC       IDLE         -----             0

Out interface(4294967295) current state: 0
                     Listen SOCKET       Main SOCKET         Second SOCKET

Socket ID:           2                   -1                  0

Option Flag:         0                   0                   0

Current State:       2                   0                   0

Prev State:          2                   0                   0

Fsm Event:           53                  52                  0

Out Pipe(id/state): (4294967295/0)      (4294967295/0)      (0/0)
In Pipe(id/state):  (4294967295/0)      (4294967295/0)      (0/0)
InBD State:          3                   0                   0

OutBD State:         3                   0                   0

BD Require:          false               false               false

Congestion Flag:     0                   0                   0

Congestion Times:    0                   0                   0

Close Flag:          0                   0                   0

             LastCreateFail             LastNotifyError             LastCreateSeqError             LastCloseSocketSeqError
Socket ID:   -1                         -1                          -1                             -1
Error Code:  0                          0                           0                              0
Occur Time:  -----                      -----                       -----                          -----

(结果个数 = 1)
---    END
```

#### 输出结果说明

| 输出项名称      | 输出项解释                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|:-----------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| BGP对等体状态信息 | 该参数用于输出BGP对等体状态信息。其中：Last Try Create Connect Fail Reason表示上次建立连接失败的原因。 BNM_UNDER_UNDO：VPN实例或者邻居处于删除状态。BNM_LOCAL_ADDR_INVALID：本端源地址无效。BNM_FAIL_SYNCHRONIZE_VRF_CFG：VPN其它配置同步失败。BNM_FAIL_SYNCHRONIZE_NEIGHBOUR_CFG：邻居配置同步失败。BNM_IGNORE_CFGED：配置了peer ignore。BNM_EMPTY_ADDR_FAMILY_LIST：本端使能的地址族为空。BNM_BRM_UNAVAILABLE：BRM组件未ready。BNM_WAITING_PEER_DOWN_ACK：等待BRM回应peer down ack。BNM_UNDER_RESET：处于reset状态。BNM_OVER_LIMIT：处于路由超限或者idle保持状态。BNM_IDLE_FOREVER：路由超限永久保持idle。BNM_SOCKET_UNREGIST：SOCK组件注册失败。BNM_SECOND_CONNECT_EXIST：第二连接已经存在。BNM_DOWN_BACKUP_NOT_OVER：Peer down备份未完成。BNM_MISSING_MAXHOP_OR_CONNECT_INTERFACE_CFG：缺少ebgp-max-hop或valid-ttl-hops配置。BNM_CONNECT_CPU_OVERLOAD：CPU过载。BNM_LINKLOCAL_PEER_WITHOUT_LOCAL_ADDR：Link-local地址的peer未配置connect-interface。BNM_BFD_SESSION_EXIST：残留bfd会话。BNM_CONNECT_LIMIT：建立TCP连接的消息超过限制。BNM_SHUTDOWN_CFGED：配置了shutdown。BNM_AS_NUM_ZERO：BGP AS号为0。BNM_V4ROUTER_ID_ZERO：V4 RouterId为0。BNM_V6ROUTER_ID_ZERO：V6 RouterId为0。BNM_PEER_AS_SYN_INCOMPLETE：PeerAS未同步完成。BNM_REMOTE_AS_SYN_INCOMPLETE：RemoteAS未同步完成。BNM_FAKE_AS_SYN_INCOMPLETE：FakeAs未同步完成。BNM_PEER_TYPE_SYN_INCOMPLETE：PeerType未同步完成。BNM_CONNECT_INTERFACE_SYN_INCOMPLETE：ConnectInt未同步完成。BNM_VRF_ROUTER_ID_SYN_STATE_INCOMPLETE：Vrf RouterId未同步完成。BNM_VRF_AS_SYN_STATE_INCOMPLETE：Vrf AS未同步完成。BNM_GREVENT_CFGED：手动触发graceful event。BNM_BIS_UPGRADE_STATE_UNAVAIBLE：升级时设置unavailable。BNM_BIS_UPGRADE_STATE_UPGRADE_READ：升级时设置upgrade。 其中：Last Peer Down Reason表示上次邻居Down原因。 BGP_PEERDOWN_HOLD_TIMER：定时器超时。BGP_PEERDOWN_TCP_FAIL：TCP建连失败。BGP_PEERDOWN_OPEN_RF：触发GR事件断开对等体。BGP_PEERDOWN_OTHER：其他原因。BGP_PEERDOWN_INTERFACE_DOWN：直连接口DOWN触发BGP对等体断连。BGP_PEERDOWN_BFD_DOWN：BFD去使能或BFD DOWN导致BGP对等体断连。BGP_PEERDOWN_PATH_INACTIVE：Peer tracking检测触发BGP对等体断连。BGP_PEERDOWN_ERR_CODE：NOTIFICATION事件导致BGP对等体断连。BGP_PEERDOWN_AS_NOMATCH：对端AS编号不匹配导致BGP对等体断连。BGP_PEERDOWN_4_BYTE_AS_CAPABILITY_SET：配置对等体4字节AS号功能。BGP_PEERDOWN_ADD_PATH_CAPABILITY_SET：配置对等体ADD-PATH路由功能。BGP_PEERDOWN_ADDR_FAMILY_ENABLE：在地址族下使能对等体。BGP_PEERDOWN_UNDO_ADDR_FAMILY：在地址族下去使能对等体。BGP_PEERDOWN_BGP_RESET：复位BGP导致对等体断连。BGP_PEERDOWN_BGP_SHUTDOWN：中断本端与所有BGP对等体的协议会话。BGP_PEERDOWN_BNM_RCV_BRM_SN_MISMATCH：BNM和BRM组件消息接口key不匹配。BGP_PEERDOWN_CONFED_ID_SET：配置BGP联盟ID。BGP_PEERDOWN_CONFED_PEER_AS_SET：配置联盟的子自治系统号。BGP_PEERDOWN_CONFED_NONSTANDARD_SET：配置与非标准的AS联盟兼容。BGP_PEERDOWN_CONNECT_ONLY_SET：配置对等体（组）仅主动发送连接请求，而不侦听连接请求功能。BGP_PEERDOWN_CONVENTIONAL_CAPABILITY_SET：配置对等体的常规路由器功能。BGP_PEERDOWN_EBGP_MAX_HOP_SET：配置同非直连网络上的对等体建立EBGP连接间允许的最大跳数。BGP_PEERDOWN_FAKE_AS_SET：配置对等体伪AS号。BGP_PEERDOWN_ADMIN_GR_EVENT：触发主动GR事件断开对等体。BGP_PEERDOWN_GRACEFUL_RESTART_SET：配置GR能力。BGP_PEERDOWN_GR_TIME_SET：配置对端从发现本端重启到重新建立BGP会话的最大等待时间。BGP_PEERDOWN_CONNECT_INTERFACE_CHANGED：配置发送BGP报文的源接口名。BGP_PEERDOWN_CONNECT_IP_ADDR_CHANGED：配置发送BGP报文的源接口地址。BGP_PEERDOWN_LABEL_ROUTE_CAPABILITY_SET：配置标签路由能力。BGP_PEERDOWN_LISTEN_ONLY_SET：配置对等体（组）仅侦听连接请求，而不主动发送连接请求功能。BGP_PEERDOWN_LOCAL_AS_CHANGED：修改本地AS编号。BGP_PEERDOWN_REMOTE_AS_CHANGED：修改对端AS编号。BGP_PEERDOWN_MBUF_ERR：MBUF错误。BGP_PEERDOWN_MULTI_SRC_CREATED：创建多源对等体。BGP_PEERDOWN_SENT_NOTIFICATION：发送NOTIFICATION报文主动断连。BGP_PEERDOWN_NO_SUPPORT_ROUTE_REFRESH：不支持ROUTER REFRESH导致对等体断连。BGP_PEERDOWN_ORF_CAPABILITY_SET：配置对等体ORF能力。BGP_PEERDOWN_PARSE_MSG_HEAD_ERR：解析报文头失败。BGP_PEERDOWN_PEER_IGNORE_SET：配置禁止与对等体（组）建立会话。BGP_PEERDOWN_PEER_RESET：复位对等体。BGP_PEERDOWN_PEER_TIMER_SET：配置BGP的存活时间与保持时间间隔。BGP_PEERDOWN_RCV_ERR_ROUTER_REFRESH：收到ROUTER REFRESH报文。BGP_PEERDOWN_RCV_UPDATE_ATTRIBUTE_ERR：收到的UPDATE报文属性错误。BGP_PEERDOWN_RCV_NOTIFICATION：收到NOTIFICATION报文。BGP_PEERDOWN_RCV_OPEN_IN_ESTABLISHED：在ESTABLISHED状态下收到OPEN报文。BGP_PEERDOWN_ROUTER_ID_CHANGED：本地Router ID更改。BGP_PEERDOWN_ROUTE_POLICY_DISTRIBUTE_SET：配置对等体RPD能力。BGP_PEERDOWN_ROUTE_REFRESH_CAPABILITY_SET：配置对等体ROUTE REFRESH能力。BGP_PEERDOWN_TCP_MSS_SET：配置与对等体（组）建立TCP连接时所使用的TCP MSS值。BGP_PEERDOWN_PACKET_SENT_TIME_OUT：发送packet失败。BGP_PEERDOWN_UNDO_PEER：删除对等体。BGP_PEERDOWN_VALID_TTL_HOPS_SET：配置对等体GTSM功能。 |