# 查询BGP HA状态信息（DSP BGPHASTATE）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于查询BGP HA状态信息。

#### 注意事项

该命令执行后立即生效。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识    | 参数名称     | 参数说明                                                                                                  |
|:--------|:---------|:------------------------------------------------------------------------------------------------------|
| AFTYPE  | BGP地址族类型 | 可选必选说明：可选参数 参数含义：BGP地址族类型。 数据来源：本端规划 取值范围：枚举类型。 ipv4uni：IPv4地址族。ipv6uni：IPv6地址族。 默认值：无                |
| VRFNAME | VPN实例名称  | 可选必选说明：可选参数 参数含义：VPN名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～31。 默认值：_public_ 配置原则：使用LST L3VPNINST命令查看可用VPN。 |

#### 使用实例

查询BGP HA状态信息：

```
DSP BGPHASTATE:;
```

```
RETCODE = 0  操作成功。

结果如下
------------------------
BGP HA状态信息  =
BRM : HA Mode      : BRM_HA_SUPPORT_NSR
      HA COMP State: BRM_HAS_PROTECT

                     CROSSATTR State   : BRM_HA_DATA_REALTIME_BACKUP
                     CROSSIID  State   : BRM_HA_DATA_REALTIME_BACKUP
                     MVRFPRIATTR  State: BRM_HA_DATA_REALTIME_BACKUP
      IPv4 Unicast : BRM_HAS_INSTANCE_PROTECT

                     ATTRID State   : BRM_HA_DATA_REALTIME_BACKUP
                     NEXTHOP State  : BRM_HA_DATA_REALTIME_BACKUP
                     IID State      : BRM_HA_DATA_REALTIME_BACKUP
                     IMPRT State    : BRM_HA_DATA_REALTIME_BACKUP
                     NTKRT State    : BRM_HA_DATA_REALTIME_BACKUP
                     AGGRRT State   : BRM_HA_DATA_REALTIME_BACKUP
                     AUTOSUM State  : BRM_HA_DATA_REALTIME_BACKUP
                     UPG State      : BRM_HA_DATA_REALTIME_BACKUP
                     RIBIN State    : BRM_HA_DATA_BOUNDARY_DECISION_OVER
                     RIBOUT State   : BRM_HA_DATA_BOUNDARY_DECISION_OVER
                     LABEL State    : BRM_HA_DATA_REALTIME_BACKUP
                     XCID State     : BRM_HA_DATA_REALTIME_BACKUP
                     LIFN State     : BRM_HA_DATA_REALTIME_BACKUP
                     VDCFG State    : BRM_HA_DATA_NO_BACKUP
                     VDRT State     : BRM_HA_DATA_NO_BACKUP
                     CROSSRT State  : BRM_HA_DATA_NO_BACKUP
                     FLOW RT  State : BRM_HA_DATA_NO_BACKUP
                     RULE State     : BRM_HA_DATA_NO_BACKUP
                     REMOTEIID State: BRM_HA_DATA_NO_BACKUP
                     INSIMPRT State : BRM_HA_DATA_REALTIME_BACKUP

BNM: HA Mode      : BNM_HA_SUPPORT_NSR
     HA COMP State: BNM_HAS_PROTECT

     _public_     : BNM_HAS_VRF_PROTECT

                     PEERINFO State : BNM_HA_DATA_BOUNDARY_DECISION_OVER
                     IPv4 Unicast   : BNM_HA_VRF_AF_REALTIME_BACKUP
                     UPG State      : BNM_HA_DATA_REALTIME_BACKUP
                     AGENTPEER State: BNM_HA_DATA_REALTIME_BACKUP
                     Router Id State: BNM_HA_DATA_REALTIME_BACKUP

(结果个数 = 1)
---    END
```

#### 输出结果说明

| 输出项名称      | 输出项解释       |
|:-----------|:------------|
| BGP HA状态信息 | BGP HA状态信息。 |