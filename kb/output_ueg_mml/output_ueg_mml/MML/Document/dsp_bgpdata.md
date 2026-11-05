# 查询BGP数据结构信息（DSP BGPDATA）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于显示BGP数据结构信息。

#### 注意事项

该命令执行后立即生效。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识     | 参数名称       | 参数说明                                                                                    |
|:---------|:-----------|:----------------------------------------------------------------------------------------|
| BGPCID   | 组件标识       | 可选必选说明：必选参数 参数含义：组件标识。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～19。十六进制整数类型，取值范围为0-FFFFFFFF。 默认值：无 |
| DATATYPE | BGP数据类型    | 可选必选说明：必选参数 参数含义：BGP数据类型。 数据来源：本端规划 取值范围：整数类型，取值范围为0～4294967295。 默认值：无                  |
| VRFNAME  | VPN实例名称    | 可选必选说明：可选参数 参数含义：VPN名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～31。 默认值：无                         |
| IPV4ADDR | BGP IPv4地址 | 可选必选说明：可选参数 参数含义：BGP IPv4地址。 数据来源：对端协商 取值范围：IPv4地址类型。 默认值：无                             |
| IPV6ADDR | BGP IPv6地址 | 可选必选说明：可选参数 参数含义：BGP IPv6地址。 数据来源：对端协商 取值范围：IPv6地址类型。 默认值：无                             |
| PARAM3   | 数据结构类型     | 可选必选说明：可选参数 参数含义：数据结构类型。 数据来源：本端规划 取值范围：整数类型，取值范围为0～4294967295。 默认值：无                   |
| PARAM4   | 数据结构类型     | 可选必选说明：可选参数 参数含义：数据结构类型。 数据来源：本端规划 取值范围：整数类型，取值范围为0～4294967295。 默认值：无                   |
| PARAM5   | 数据结构类型     | 可选必选说明：可选参数 参数含义：数据结构类型。 数据来源：本端规划 取值范围：整数类型，取值范围为0～4294967295。 默认值：无                   |

#### 使用实例

显示BGP数据结构信息：

```
DSP BGPDATA:BGPCID="80140476",DATATYPE=0;
```

```
RETCODE = 0  操作成功。

结果如下
-------------------------
BGP数据信息  =  Usage:
Data Structure Name             Data Index  Param
-                               0           N/A
BRM_LOCAL_S                     1           N/A
BRM_VRF_S                       2           [vrf_name]
BRM_UPDATEPEERGROUP_S           3           [vrf_name] group_id
BRM_PEER_S                      4           [vrf_name] peer_id
COMP_HA_EVENT                   5           N/A
VRF_HA_EVENT                    6           [vpn-instance vrfname]
PEER_HA_EVENT                   7           [vpn-instance vrfname] peeraddr
COMP_APPLY_IID_LABEL_CNT        8           N/A
BRM_VM_DATA_S                   9           N/A
BRM_CM_NHM_DATA_S               10          N/A
BRM_LM_DATA_S                   11          N/A
BRM_FES_SUBSCRIBE_STATE_INFO_S  12          fes_pid
BRM_IM_NHM_DATA_S               13          [vpn-instance vrfname]
BRM_IM_VRM_DATA_S               14          [vpn-instance vrfname]
BRM_IM_VPNRO_DATA_S             15          [vpn-instance vrfname]
BRM_FES_DATA_S                  16          [vpn-instance vrfname]
BRM_IM_VPN_DATA_S               17          N/A
BRM_VPN_VD_NODE_S               18          vd_pid
BRM_VPN_VRF_NODE_S              19          [vpn-instance vrfname] vd_pid or vd_pid vrfId
RM_CONSUMER_VERIFY_STATE        20          N/A
RM_PRODUCER_VERIFY_STATE        21          N/A
LOG SWITCH ON(OFF)              22          0:off 1:log upg 2:log route-select data 3:clear route-select data 5: set hold log on
         6:set roa-db log 7:set brm record log switch on 22:display debugging struct
BRM_CFG_DEBUG_DATA              23          N/A or 0            : show class list
         1 [page]            : show brief log info sort by time(each page thirty records)
         2 class id [page]   : show class log info
         3 index             : show verbose log info
         252 update max count: (0~65535)set the debug max count of update msg
         253 action max count: (0~65535)set the debug max count of action msg
         254 query max count : (0~65535)set the debug max count of query msg
         255                 : clear all debug info
BRM_FLOW_VALIDATION_S           24          [vrf_name] validation_addr mask_len source_ip
BRM_FLOW_VALIDATION_S           25          [vrf_name] re_id [relation_breakpoint]
BRM_FLOW_VALIDATION_S           26          [vrf_name]
SWITCH ON(OFF) BACKUP TIMER     27          1 on 0 off
BlackBox Data                   28          boxid, 1~255
BRM_SET_WAIT_SELECT_COUNT       29          WaitCnt 1~1000000(default 10000), AgingTimer 1~3600000(default 5000)
RPKI Data                       30          N/A                 : show rpki data
         1 prefix masklen    : show pefix in RoaDB
EVPN Data                       32          N/A or 0          : show IFM data
          1                 : show VXLAN data
          2                 : show EVPN LocRib data
          3                 : show EVPN Ribin data

EVRF_DATA                       33          N/A
BRM_BMP_DATA                    31          N/A
BRM_SET_CONVERG_TEST_ACT        34          1 [1:bgp,2:bgp-study]: convergence test-begin
         0                    : convergence test-end
BRM_PIDM_PARTNER_INFO_S         35          pid/cid
BRM_PRODUCER_S                  36          [vpn-instance vrfname] dest_vrfid

(结果个数 = = 1)
---    END
```

#### 输出结果说明

| 输出项名称   | 输出项解释    |
|:--------|:---------|
| BGP数据信息 | BGP数据信息。 |