# 查询SOCK黑匣子诊断信息（DSP SOCKBLACKBOX）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于查询SOCK黑匣子诊断信息。

不指定CID参数时，查询所有SOCK的诊断信息，当指定CID参数时，查询指定SOCK诊断信息。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识    | 参数名称        | 参数说明                                                                                                  |
|:--------|:------------|:------------------------------------------------------------------------------------------------------|
| TYPE    | 诊断数据类型      | 可选必选说明：必选参数 参数含义：该参数用来指定SOCK的诊断数据类型。 数据来源：本端规划 取值范围：枚举类型。 FILE：黑匣子文件信息。PIPE：黑匣子管道信息。HA：黑匣子HA信息。 默认值：无 |
| CID     | Socket组件CID | 可选必选说明：可选参数 参数含义：该参数用来指定Socket组件CID。 数据来源：本端规划 取值范围：十六进制整数类型，取值范围为0x0～0xFFFFFFFF。 默认值：无               |
| ISSLAVE | 主备类型        | 可选必选说明：可选参数 参数含义：该参数用来指定主备类型。 数据来源：本端规划 取值范围：枚举类型。 Master：主资源单元。Slave：备资源单元。 默认值：Master               |

#### 使用实例

- 查询SOCK黑匣子文件诊断信息：

  ```
  DSP SOCKBLACKBOX: TYPE=FILE, CID="0x8065002B";
  ```

  ```
          RETCODE = 0  操作成功。

          结果如下
          --------
          查询结果信息  =
          Cid:0x8065002b
          Info:
           32695 LAddr 0x29d001e8 PPort 0 PAddr 0x7fb7
          -------Path Info-------
          PathID 0x11 PathState 3  PathReason 0
          AllocKey: SendFlag 0
                    TunnelType 0  TunnelId 0  xcIndex 0
                    DstAddr 0xbd640705   SrcAddr 0xbd64070b
                    InIfIndex 0   SpecifyOutIf 0
          ------------------------

          s_cc 53, r_cc 0 datapkt 746 retransmit 0 soft_err 0, so_err 0

          Deleting Socket at 2017-4-1:15:23:43:92
          [FD = 5]  [SD = 5]  [APP = 2214723626]  [BD Require 0]  [Error 0]
          [AF_INET] [Proto = 6] [RX Pipe = 4294967295] [TX Pipe = 4294967295]
          From LDM 983  From IPV4_Lib 983 To App 341
          From APP 961  To LDM 754
          To APP at 2017-4-1:15:23:43:90
          To LDM at 2017-4-1:15:23:43:91
          From APP at 2017-4-1:15:23:43:91
          From LDM at 2017-4-1:15:23:43:92
          LPort 32695 LAddr 0x29d00878 PPort 0 PAddr 0x7fb7
          -------Path Info-------
          PathID 0x3 PathState 3  PathReason 0
          AllocKey: SendFlag 0
                    TunnelType 0  TunnelId 0  xcIndex 0
                    DstAddr 0xbd640705   SrcAddr 0xbd64070b
                    InIfIndex 0   SpecifyOutIf 0
          ------------------------

          (结果个数 = 1)
          ---    END
  ```
- 查询SOCK黑匣子管道诊断信息：

  ```
  DSP SOCKBLACKBOX: TYPE=PIPE, CID="0x8065002B";
  ```

  ```
          RETCODE = 0  操作成功。

          结果如下
          --------
          查询结果信息  =
          Cid:0x8065002b
          Info:
          2017-4-1 14:35:7:979-00:00  Pipe Open Rsp Error to Next Hop Comp [2155347976].
          2017-4-1 14:35:8:974-00:00  Try to Re-open pipe to Next Hop Comp [2155347976].
          2017-4-1 14:35:10:521-00:00  Reject pipe -1073217533 Open Req, Fail to find SendCb, PeerCid [6684690].

          (结果个数 = 1)
          ---    END
  ```
- 查询SOCK黑匣子HA诊断信息：

  ```
  DSP SOCKBLACKBOX: TYPE=HA, CID="0x80650007";
  ```

  ```
          RETCODE = 0  操作成功。

          结果如下
          --------
          查询结果信息  =
          Cid:0x80650007
          Info:
          s notify, app [2149974025]'s old/new status is 0/0

          2017-4-1 14:35:5:712-00:00  Receive Comp FSM Event Sock Comp Event App Status Availiable
          2017-4-1 14:35:5:712-00:00  APP[0x80260009] Trans from State Sock App Fsm Init into State Sock App Fsm Standalone, Event Sock App Event Available Standalone.
          2017-4-1 14:35:5:712-00:00  SOCK Comp Trans from State Sock Comp Fsm Standalone into State Sock Comp Fsm Standalone, Event Sock Comp Event App Status Availiable.
          2017-4-1 14:35:6:122-00:00  SSP Notify Partner Info ID 2155347976 State 0 SubState 0 HaRole 0 Cause 0
          2017-4-1 14:35:10:538-00:00  SSP Notify Partner Info ID 7995407 State 0 SubState 0 HaRole 0 Cause 0
          2017-4-1 14:35:10:538-00:00  SSP Notify Partner Info ID 6750225 State 0 SubState 0 HaRole 0 Cause 0
          2017-4-1 14:35:10:538-00:00  Cachem Partner status notify, Cachem's status is 2

          2017-4-1 14:35:10:538-00:00  SSP Notify Partner Info ID 6684690 State 0 SubState 0 HaRole 0 Cause 0
          2017-4-1 14:35:10:538-00:00  stb(0x660012) Partner status notify, status is 0
          2017-4-1 14:35:10:538-00:00  CACHEMLIB:Cachem Up, Smooth Fsm(0),Service State(3)
          2017-4-1 14:35:10:538-00:00  send table request msg,TableSmoothState(1)
          2017-4-1 14:35:10:549-00:00  Rev table smooth begin msg, TableSmoothState(2)
          2017-4-1 14:35:10:556-00:00  Rev table smooth end msg, TableSmoothState(4)
          2017-4-1 14:35:10:574-00:00  [PORTGRP]Rev table update msg, PortGroup(1), PrimaryLdmPid(7864328)
          2017-4-1 14:35:15:108-00:00  CACHEMLIB:Rcv Smooth Request, Smooth Fsm(1),Service State(3), TRANSNO(0, 1)
          2017-4-1 14:35:15:108-00:00  CACHEMLIB:Snd Smooth Begin, Smooth Fsm(1),Service State(3)
          2017-4-1 14:35:15:108-00:00  CACHEMLIB:Snd Smooth End Msg, Smooth Fsm(1),Service State(3)
          2017-4-1 14:35:15:317-00:00  CACHEMLIB:Snd Sub Service Msg, Smooth Fsm(4),Cachem Service State(3),Service State(3)
          2017-4-1 14:35:15:317-00:00  CACHEMLIB:Rcv Sub Scribe Ack Smooth Fsm(4), Service State(3)
          2017-4-1 14:35:15:317-00:00  CACHEMLIB:Rcv Cachem Service State old(3)->new(1)
          2017-4-1 14:35:15:317-00:00  CACHEMLIB: old enServiceState 3
          2017-4-1 14:35:15:317-00:00  CACHEMLIB: Service State 1
          2017-4-1 14:35:16:98-00:00  CACHEMLIB:Rcv Notify Msg Smooth Fsm(4), Service State(1)
          2017-4-1 14:35:16:98-00:00  CACHEMLIB:Rcv Cachem Service State old(1)->new(0)
          2017-4-1 14:35:16:98-00:00  CACHEMLIB: old enServiceState 1
          2017-4-1 14:35:16:98-00:00  CACHEMLIB: TableSmoothState = CACHEMLIB_SMOOTH_TABLE_OK
          2017-4-1 14:35:16:98-00:00  CACHEMLIB: Service State 0
          2017-4-1 15:35:10:563-00:00  [PORTGRP]Rev table update msg, PortGroup(1), PrimaryLdmPid(7864328)

          (结果个数 = 1)
          ---    END
  ```

#### 输出结果说明

| 输出项名称   | 输出项解释            |
|:--------|:-----------------|
| 查询结果信息  | 用来显示SOCK的查询结果数据。 |