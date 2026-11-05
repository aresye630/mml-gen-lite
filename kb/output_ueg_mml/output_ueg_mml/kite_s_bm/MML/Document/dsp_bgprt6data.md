# 查询BGP IPv6路由数据结构信息（DSP BGPRT6DATA）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于显示BGP IPv6路由数据结构信息。

#### 注意事项

该命令执行后立即生效。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识     | 参数名称       | 参数说明                                                                                                                               |
|:---------|:-----------|:-----------------------------------------------------------------------------------------------------------------------------------|
| VRFNAME  | VPN实例名称    | 可选必选说明：可选参数 参数含义：该参数用于指定VPN名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～31。 默认值：_public_ 配置原则：使用LST L3VPNINST命令查看可用VPN。                       |
| AFTYPE   | BGP地址族类型   | 可选必选说明：可选参数 参数含义：该参数用于指定BGP地址族类型。 数据来源：本端规划 取值范围：枚举类型。 ipv6uni：IPv6地址族。ipv6vpn：VPNv6地址族。 默认值：ipv6uni                               |
| IPV6ADDR | BGP IPv6地址 | 可选必选说明：必选参数 参数含义：该参数用于指定BGP IPv6地址。 数据来源：对端协商 取值范围：IPv6地址类型。 默认值：无                                                                 |
| MASK     | 掩码长度       | 可选必选说明：可选参数 参数含义：该参数用于指定前缀长度。 数据来源：本端规划 取值范围：整数类型，取值范围为0～128。 默认值：无                                                                |
| UPGINDEX | BGP打包组索引   | 可选必选说明：可选参数 参数含义：该参数用于指定BGP打包组索引。 数据来源：本端规划 取值范围：整数类型，取值范围为0～4294967295。 默认值：无 配置原则：通过display bgp update-peer-group命令可以查询BGP打包组索引。 |

#### 使用实例

显示BGP IPv6路由数据结构信息：

```
DSP BGPRT6DATA:IPV6ADDR="2001:db8:2:2:2:2:2:2";
```

```
RETCODE = 0  操作成功。

结果如下
-------------------------
BGP数据信息  =
 BGP local router ID : 10.1.1.11
 Local AS number : 100

 Route Head Information:
 RtEntryCount = 1
 RefCount = 2
 BitSetForSuppressRt = 0
 AppliedLabel = 4294967295
 InTobeUpdateCount = 0
 AdvSuppCount = 0
 AdvSuppFlagFst = 0
 AdvSuppFlagSec: 0
 InTobeUpdSllFst = 0
 InTobeUpdSllSec: 0
 RthUpgFlags = 0
 LblRiboutCount = 0
 RtHeadFlags = 256

 BGP routing table entry information of 2001:db8:2:2:2:2:2:2/128:
 From: 2001:db8:2:2:2:2:2:21 (10.1.1.21)
, origin incomplete, MED 0, localpref 100, pref-val 0, valid, internal, best, se
lect, pre 255

 Route Entry Information:
 RtEntryFlags = 540016641
 ExtraFlags = 0
 AttrChangeFlags = 0
 TimeStamp = 82345
 ReceivedLabel = 4294967295
 Version = 1
 WorseReason = 0

 Public Attribute Information:
 Refcount = 2
 PrefVal = 0
 Preference = 255
 LocalPathID = 255
 RecvPathID = 0

 Attribute Information:
 AttributeFlag = 786463
 AttrID = 16777217
 RtRefCount = 2
 ActiveRtRefCount = 2
 BestRtRefCount = 2
 TotalRefCount = 2
 RtAdvRefCount = 0
 VpnroRibOutFst = 0
 VpnroRibOutSec: 0
 AttrStRibOutFst = 0
 AttrStRibOutSec: 0
 AttrUpgFlags = 0

 Nexthop Information:
 TotalRef = 3
 Type = 0
 RelayStatus = 65536
 DeleteStatus = true
 Version = 0

 RouteQuery Info:
 RtqBestRtRef = 2
 RtqActiveRtRef = 2
 RtqRtRef = 3
 RtqTotalRef = 1
 RtqQueryType = 0
 RtqRelayStatus = 68609
 RtqFlag = 268435456

 IIDInfo:
 RtqIIDInfoFlag = 1
 qr_qry_fsm_state = 3
 RtqIIDCBIID = 1828716980
 RtqIIDCBType = 0
 RtqStIIDUpgFlg = 268435456
 RtqStIIDRef = 1

 RelayInfo:
 qr_qry_fsm_state = 3
 RtqCost = 0
 RtqRelayNum = 1
 RtqIterDepth = 1
 RtqDest = 1507329
 RtqMask = 64

(结果数量 = 1)
---    END
```

#### 输出结果说明

| 输出项名称   | 输出项解释                               |
|:--------|:------------------------------------|
| BGP数据信息 | 用于指定BGP路由头部信息、下一跳信息、公共属性、路径属性等数据信息。 |