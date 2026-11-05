# 查询CACHEM诊断信息（DSP CACHEMINNERDATA）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于查询CACHEM诊断信息。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识      | 参数名称        | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|:----------|:------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TYPE      | 内部数据类型      | 可选必选说明：必选参数 参数含义：该参数用来指定内部数据类型。 数据来源：本端规划 取值范围：枚举类型。 PATH：Path信息。PATH_BLACK_BOX：Path黑匣子。PARTNER：Partner组件信息。LOCAL：本地信息。PIDNODE：PID节点数据。QUERY_TABLE_COUNT：查询表项个数。SEGMENT：段信息。SEGMENT_STATISTIC：段统计计数。SEND_FLAG_STATISTIC：创建Path类型统计计数。QUERY_TABLE_INFO：查询表类型。 默认值：无                                                                                                                                                                                                          |
| PID       | APP组件PID    | 可选必选说明：条件必选参数 前提条件：该参数在“TYPE”配置为“PIDNODE”时为必选参数。 可选必选说明：条件可选参数 前提条件：该参数在“TYPE”配置为“PATH”时为可选参数。 参数含义：该参数用来指定APP的PID。 数据来源：本端规划 取值范围：十六进制整数类型，取值范围为0x0～0xFFFFFFFF。 默认值：无                                                                                                                                                                                                                                                                                                      |
| PATHID    | Path ID     | 可选必选说明：条件可选参数 前提条件：该参数在“TYPE”配置为“PATH”时为可选参数。 参数含义：该参数用来指定Path ID。 数据来源：本端规划 取值范围：十六进制整数类型，取值范围为0x0～0xFFFFFFFF。 默认值：无                                                                                                                                                                                                                                                                                                                                                       |
| INFOTYPE  | Partner信息类型 | 可选必选说明：条件必选参数 前提条件：该参数在“TYPE”配置为“PARTNER”时为必选参数。 参数含义：该参数用来指定Partner信息类型。 数据来源：本端规划 取值范围：枚举类型。 BASIC：Partner基本信息。EXTENDED：Partner扩展信息。 默认值：无                                                                                                                                                                                                                                                                                                                                |
| SEGMENTID | 段ID         | 可选必选说明：条件必选参数 前提条件：该参数在“TYPE”配置为“SEGMENT”时为必选参数。 参数含义：该参数用来指定段ID。 数据来源：本端规划 取值范围：整数类型，取值范围为0～4294967295。 默认值：无                                                                                                                                                                                                                                                                                                                                                              |
| TABLETYPE | 表类型         | 可选必选说明：条件必选参数 前提条件：该参数在“TYPE”配置为“QUERY_TABLE_INFO”时为必选参数。 参数含义：该参数用来指定表类型。 数据来源：本端规划 取值范围：枚举类型。 TBL_ROUTE：路由表。TBL_IF_INFO：接口信息表。TBL_ARP：ARP表。TBL_SRC_IP：源IPv4表。TBL_IF_TYPE：接口类型表。TBL_ROUTE6：IPv6路由表。TBL_ND：ND表。TBL_SRC_IP6：源IPv6表。TBL_PATHMTU：Path MTU表。TBL_TRUNK：Trunk表。TBL_IF_MTU4：接口MTU4表。TBL_IF_MTU6：接口MTU6表。TBL_IFNODE：接口节点表。TBL_PID_MAP：PID映射表。TBL_SUBIF_MAINIF：主、子接口关系表。TBL_PORTGRP_NODEID：Port Group与Node ID表。TBL_PORTGRP：Port Group表。TBL_PATH_LIMIT：Path限速表。 默认值：无 |

#### 使用实例

- 查询CACHEM Path信息：

  ```
  DSP CACHEMINNERDATA: TYPE=PATH, PID="0x650019", PATHID="0x1";
  ```

  ```
          RETCODE = 0  操作成功。

          结果如下
          --------
          诊断信息数据  =

          Path-Header Info:
          PATH-ID : 0x1             PATH-STATE  : ACTIVE          PATH-REASON: OK
          NEXT-PID: 0x650019        NEXT-SEGMENT: 67108969        EX-FLG     : 0
          VS-INDEX: 0               VRF-INDEX   : 1               SND-FLG    : 0
          IF-INDEX: 0               XC-INDEX    : 0               SRC-ADDR   : 192.168.0.2
          SPEC-IF : 0               DLD-STATE   : DOWNLOAD OK     DST-ADDR   : 192.168.0.1
          OPER-TYP: NA              TNL-ID      : 0               NXT-HOP    : 0.0.0.0
          NXT-OPER: NA              VLAN-ID     : 0               MAC-ADDR   : 0000-0000-0000
          PLIST-ID: 0               VSI-ID      : 0               TNL-TYPE   : 0
          NICKNAME: 0               OLD-SEGMENT : 4294967295      APPLY-PID  : 0x650019
          AGE-FLG : 0               OLD-STATE   : 0               IDENTIFY   : 9
          IS-MC   : 1               PATH-TYPE   : 1               BACKOFFCNT : 0

          RE-PROID: 0x01-0x00

          Black-Box:
          2016-11-17 10:20:0:149  create path
          2016-11-17 10:20:0:149  0->3(0),(0,1,0)
          2016-11-17 10:20:9:498  3->1(209),(52,2,0)
          2016-11-17 10:20:9:499  3->1(209),(5,2,0)
          2016-11-17 10:20:9:500  3->1(209),(2,2,0)

          IP-Segment Info:
          SEG-ID  : 67108969        NXT-SEGID   : 335544427       NXT-PID    : 6619161
          IN-IF   : 0               VR-INDEX    : 0               SRC-ADDR   : 192.168.0.2
          OUT-IF  : 3               VRF-INDEX   : 1               DST-ADDR   : 192.168.0.1
          MASK    : 0               RED-FLG     : 0               NEXT-HOP   : 0.0.0.0

          IPMC-Segment Info:
          SEG-ID  : 335544427       NXT-SEGID   : 4294967295      NXT-PID    : 0
          PID-CNT : 2               OUTIF-CNT   : 2
          PID-INFO:
          TYPE: 0 PID: 0x78000e PORTGRP: 0x0 SEGMENTID: 0x1800006e
          TYPE: 0 PID: 0x78000f PORTGRP: 0x0 SEGMENTID: 0x18000071

          IFPATH  : MCTBL_INDEX     OIFINDEX    : 0
          IFPATH  : MCTBL_INDEX     OIFINDEX    : 1

          TPCLONE-Segment Info:
          SEG-ID  : 402653294       NXT-SEGID   : 4294967295      NXT-PID    : 0
          ELB-CNT : 1               PORTGROUP   : 7864334
          IFINDEX : 4294967295      NXT-SEGID   : 268435565

          FRAG-Segment Info:
          SEG-ID  : 268435565       NXT-SEGID   : 201326700       NXT-PID    : 7864334
          MTU     : 1500            DF-FLAG     : 0

          ETH-Segment Info:
          SEG-ID  : 201326700       NXT-SEGID   : 4294967295      NXT-PID    : 0
          MTU     : 1500            LINK-TYPE   : 0               SRC-ADDR   : 0.0.0.0
          DF-FLAG : 0               KEY-TYPE    : 1               NXET-HOP   : 192.168.0.1
          PID     : 7864334         RAWLINK-FLG : 0               IF-INDEX   : 3
          VCD     : 0               CEV-ID      : 0               MAC-ADDR   : 0000-0000-0000
          WORK-IF : 4               PEV-ID      : 0

          (结果个数 = 1)
          ---    END
  ```
- 查询CACHEM本地信息：

  ```
  DSP CACHEMINNERDATA: TYPE=LOCAL;
  ```

  ```
          RETCODE = 0  操作成功。

          结果如下
          --------
          诊断信息数据  =

          -------------------------------------
                    Cid: 0x80670018
          -------------------------------------
          Local data:
          MyPid              : 0x670011        MyCid             : 0x80670018      Pp4Pid            : 0x660012
          FesPid             : 0x6a0013        IfmPid            : 0x7a000f        SmpPid            : 0x0
          Pp6Pid             : 0x0             Tnl6Pid           : 0x0             IpSecPid          : 0x0
          DiagSwitch         : OFF             DumpSwitch        : OFF             PrvtLogSw         : OFF
          DebugSw            : OFF             WorkRole          : PRIMARY         SmoothStage       : FALSE
          SlaveReady         : NotReady        PathIdOnWalk      : NoOnWalk        CachemFsm         : ACTIVE
          ServiceState       : AVAILABLE       LogLevelSw        : 255             Sequence          : 187
          TmHandle           : 200
          LogBuffUsedLen     : 0               DebugBuffUsedLen  : 0               VerifyTimerFlg     : TRUE
          SecondNow          : 7017            LastSendDataMsgSec: 7015            LastSendEventMsgSec: 7017
          MsgBlockIsReady    : Ready           DelInvalidTimes   : 0               SegmentIdTree.Nodes: 31
          PathIdTree.Nodes   : 9               LastAllocSegmentId: 302             LowPriorityRcvStat : 8

          DebugInfo:
          Verbose            : FALSE           CompPid           : 0x0             IidType           : 0
          DebugFlag          : 0               MsgNum            : 0               MsgCnt            : 4294967295

          PathmLocal:
          GlobalPathNum      : 0               VerifyTime        : 0               OnWalk            : NoOnWalk
          ToCheckList        : Empty           CheckIngList      : Empty           BatchDwlList      : Empty
          SmoothOldSegIdTree.Nodes   : 0
          --------------------------------------

          (结果个数 = 1)
          ---    END
  ```
- 查询CACHEM表项个数：

  ```
  DSP CACHEMINNERDATA: TYPE=QUERY_TABLE_COUNT;
  ```

  ```
          RETCODE = 0  操作成功。

          结果如下
          --------
          诊断信息数据  =

          ----------------------------------------------------
          QueryType     Num           TableName
          ----------------------------------------------------
          1             3             ROUTE
          2             4             IF_INFO
          3             2             ARP
          5             4             IF_TYPE
          21            4             MTU4
          34            1             IF_GROUP
          50            1             PORTGRP_NODEID_ENTRY
          51            1             PORTGRP
          52            2             LMIFACTIVE_ENTRY
          79            2             LAG TBL
          96            2             RM_SERVICE
          ----------------------------------------------------

          (结果个数 = 1)
          ---    END
  ```
- 查询CACHEM段信息：

  ```
  DSP CACHEMINNERDATA: TYPE=SEGMENT, SEGMENTID=67109094;
  ```

  ```
          RETCODE = 0  操作成功。

          结果如下
          --------
          诊断信息数据  =

          IP Segment :
          Common Seg :
          SegmnetId      : 67109094        NextSegmentId : 0x140000e8      PathId        : 45
          Pid            : 0x650018        NextPid       : 0x650018        State         : 1
          EncapType      : IP-COMMON-ROUTE NextType      : 0               UpdateFlg     : FALSE
          VersionNum     : 1               UpdateReason  : 0               SegmentPidCnt : 1
          McSegId        : 4294967295      PreSegId      : 45

          Alloc Key :
          VsIndex        : 0               VrfIndex      : 2               SendFlg       : 0
          Family         : Ipv4            ExtFlg        : 0               SrcAddr       : 192.168.0.1
          DstAddr        : 192.168.0.5      InIfIndex     : 0               PhyIf         : 0
          InPhyIf        : 0               SpcifyOutIf   : 0               TunnelID      : 0
          XcIndex        : 0               VlanId        : 0               NickName      : 0
          TunnelType     : 0               PortListId    : 0               VsiId         : 0
          PortGrpId      : 0               MAC           : 0000-0000-0000

          IP Common :
          SrcAddr        : 192.168.0.1      OutIfIndex    : 4               Mtu           : 1500
          PathMtu        : 0               DF            : 0               Loopbackflg   : 0
          DstAddrType    : 0               CtrlDscp      : 255             MngDscp       : 255
          OtherDscp      : 255
          NextHop        : 0.0.0.0         Mask          : 0               InLabel       : 4294967295
          RedirectFlag   : 0

          (结果个数 = 1)
          ---    END
  ```

#### 输出结果说明

| 输出项名称   | 输出项解释       |
|:--------|:------------|
| 诊断信息数据  | 用来指定诊断信息数据。 |