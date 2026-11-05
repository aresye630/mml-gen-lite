# 查询LDM诊断信息（DSP LDMINNERDATA）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于查询LDM诊断信息。不指定CID参数时，查询所有LDM的诊断信息，当指定CID参数时，查询指定LDM诊断信息。当内部数据类型为TCP\_CONTROL\_PACKET时，若SOCKID、PORTNUM不指定时，默认为0，不显示诊断信息数据。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识    | 参数名称         | 参数说明                                                                                                                                                                         |
|:--------|:-------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TYPE    | 内部数据类型       | 可选必选说明：必选参数 参数含义：该参数用来指定内部数据类型。 数据来源：本端规划 取值范围：枚举类型。 PIPE：管道信息。LOCAL：本地信息。PCT：PCT表信息。PCTEXT：PCTEXT表信息。TCP_CONTROL_PACKET：TCP控制报文。PARTNER：Partner组件信息。 默认值：无                  |
| PID     | Partner组件PID | 可选必选说明：条件必选参数 前提条件：该参数在“TYPE”配置为“PIPE”时为必选参数。 可选必选说明：条件可选参数 前提条件：该参数在“TYPE”配置为“PARTNER”时为可选参数。 参数含义：该参数用来指定Partner组件的PID。 数据来源：本端规划 取值范围：十六进制整数类型，取值范围为0x0～0xFFFFFFFF。 默认值：无 |
| CID     | LDM组件CID     | 可选必选说明：可选参数 参数含义：该参数用来指定LDM组件CID。 数据来源：本端规划 取值范围：十六进制整数类型，取值范围为0x0～0xFFFFFFFF。 默认值：无                                                                                         |
| IFINDEX | 接口索引         | 可选必选说明：条件可选参数 前提条件：该参数在“TYPE”配置为“PCT” 或 “PCTEXT”时为可选参数。 参数含义：该参数用于显示会话信息的接口索引。 数据来源：本端规划 取值范围：整数类型，取值范围为1～4294967294。 默认值：无                                                  |
| SOCKID  | Socket实例ID   | 可选必选说明：条件可选参数 前提条件：该参数在“TYPE”配置为“TCP_CONTROL_PACKET”时为可选参数。 参数含义：该参数用来指定Socket实例ID。 数据来源：本端规划 取值范围：整数类型，取值范围是0～4294967295。 默认值：无                                             |
| PORTNUM | 端口号          | 可选必选说明：条件可选参数 前提条件：该参数在“TYPE”配置为“TCP_CONTROL_PACKET”时为可选参数。 参数含义：该参数用来指定端口号。 数据来源：本端规划 取值范围：整数类型，取值范围为0～4294967295。 默认值：无                                                    |

#### 使用实例

- 查询LDM管道信息：

  ```
  DSP LDMINNERDATA: TYPE=PIPE, PID="0x660012", CID="0x80780008";
  ```

  ```
          RETCODE = 0  操作成功。

          结果如下
          --------
          诊断信息数据

          --------------------------------
          LDM Pid: 0x780008
          LDM Cid: 0x80780008
          ProcID : 4
          --------------------------------

          partnerPID    CompType  CID         CIDNo. PipeMessage         ChangeNum   LastTime
          ----------------------------------------------------------------------------------------------
          0x660012      102       -           -      OPEN                1           2016-12-26 17:1:49 653

          0x660012      102       -           -      CLOSE               1           2016-12-26 17:1:45 557

          0x660012      102       -           -      OPEN_FAIL           0           0-0-0 0:0:0 0

          0x660012      102       -           -      OPEN_RSP_OK         1           2016-12-26 17:1:49 658

          0x660012      102       -           -      OPEN_RSP_ERR        0           0-0-0 0:0:0 0

          0x660012      102       -           -      OPEN_REQ_ACCEPT     1           2016-12-26 17:1:52 564

          0x660012      102       -           -      OPEN_REQ_REJECT     1           2016-12-26 17:1:49 582

          0x660012      102       -           -      PIPE_CLOSE_REQ      0           0-0-0 0:0:0 0

          0x660012      102       -           -      PIPE_CLOSE_RSP      0           0-0-0 0:0:0 0

          0x660012      102       -           -      OPEN_REQ_ACCEPT_RSP 0           0-0-0 0:0:0 0

          0x660012      102       -           -      STAT_AVAILABLE      1           2016-12-26 17:1:49 653

          0x660012      102       -           -      STAT_UNAVAILABLE    1           2016-12-26 17:1:45 557

          0x660012      102       -           -      SEND_REG_OK         0           0-0-0 0:0:0 0

          0x660012      102       -           -      SEND_REG_ERR        0           0-0-0 0:0:0 0

          0x660012      102       -           -      PIPE_ID_ERROR       0           0-0-0 0:0:0 0

          0x660012      102       -           -      CID_INIT            0           0-0-0 0:0:0 0

          0x660012      102       -           -      CID_INIT_BYPID      0           0-0-0 0:0:0 0

          0x660012      102       -           -      CID_DEL             0           0-0-0 0:0:0 0

          (结果个数 = 19)
          ---    END
  ```
- 查询LDM本地信息：

  ```
  DSP LDMINNERDATA: TYPE=LOCAL;
  ```

  ```
          RETCODE = 0  操作成功。

          结果如下
          --------
          诊断信息数据

          --------------------------------
          LDM Pid: 0x780008
          LDM Cid: 0x80780008
          ProcID : 4
          --------------------------------

          DeployInfo_0213:
                  PID=0x780008 CID=0x80780008 ProcID=4 CompState=3
                  DeployType=0(0:DeployFeNode 1:DeployByLoc 2:DeployByVR)
                  SVCType=186 LS=0 VS=0 NodeId=0x1ff01 PortGrpId=0x0 Fenodetype=0x1 Pos:0-1 PeerCid=0x0,
          GMplsErr=0 FesMsg:
                  Total=213 TypeErrN=0 TypeErr=0 LenErr=0
                  SeqErr=0 TblN=204 UpAll=0 UpErr=0
                  BatchB=1 Batch=5 BatchE=1 RegN=1 SubN=0
                  SmothQeqN=1 NotifyErrN=0 SeqErr=0 Flag=0
          FesTlv:
                  TypeErrTotal=0 TypeErrT=0 TypeErrL=0
                  LenErrTotal=0 LenErrT=0 LenErrL=0
          CtlMsg:
                  TypeErrTotal=0 TypeErrT=0 TypeErrL=0
                  LenErrTotal=0 LenErrT=0 LenErrL=0
          OtherInfo:
                  IssuRealSend=0 IssuRealRcv=0 FirstPktSwitch=0
                  IlmBuf=0 FesStat=0(0:AVALIBLE 1:UNAVALIBLE)

          StarWorkTime:2017-4-1 14-35-5:909
          GlobalInfo:0-0-0-1-0
          (108:3258597621/0:180075684 - 108:3268540764/0:180079517)tick/us
          (108:3437705538/0:180144731 - 108:3444167082/0:180147222)tick/us
          (108:3446007604/0:180147932 - 108:3605218621/0:180209309)tick/us

          (结果个数 = 2)
          ---    END
  ```
- 查询LDM PCT表信息：

  ```
  DSP LDMINNERDATA: TYPE=PCT, CID="0x80780008", IFINDEX=4;
  ```

  ```
          RETCODE = 0  操作成功。

          结果如下
          --------
          诊断信息数据

          --------------------------------
          LDM Pid: 0x780008
          LDM Cid: 0x80780008
          ProcID : 4
          --------------------------------

          Total number   : 6
          --------------------------------
          IfIndex    ChannelId  Port  Link  TBTP       VS   Vrf        BindIf     BindIf2    MainIf     IsMain NodeID     GroupID    Mtu   Mtu6  Mac            Vsi        BD         DPid1      DPid2      TrunkID Flag       ST/MA/IP/RV/SV Static     MemStat    TpIdMode   AcType     AcFlag
          --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
          1          0          18    255   0x0        0    0          0          0          0          0      0xffff0001 0x1        1500  0     0000-0000-0000 0          0          0x0        0x0        65535   0          0  0  0  0  0  0          0          0          0          0

          (结果个数 = 2)
          ---    END
  ```
- 查询LDM PCTEXT表信息：

  ```
  DSP LDMINNERDATA: TYPE=PCTEXT, CID="0x80780008", IFINDEX=5;
  ```

  ```
          RETCODE = 0  操作成功。

          结果如下
          --------
          诊断信息数据

          --------------------------------
          LDM Pid: 0x780008
          LDM Cid: 0x80780008
          ProcID : 4
          --------------------------------

          Total number   : 6
          ----------------------------------------------------------------------------------------------------------
          IfIndex   LinkType L2L3 DftVlan Type CType VlanID MuxEn IPSG Eth/CrType PolicyAddr pEth2 pEth2Next pBitMap
          ----------------------------------------------------------------------------------------------------------
          3         0        0    0       0    0     4095   0     0    0          0          0     0         0

          (结果个数 = 2)
          ---    END
  ```
- 查询LDM TCP控制报文信息：

  ```
  DSP LDMINNERDATA: TYPE=TCP_CONTROL_PACKET, SOCKID=7, PORTNUM=22;
  ```

  ```
          RETCODE = 0  操作成功。

          结果如下
          --------
          诊断信息数据

          --------------------------------
          LDM Pid: 0x780008
          LDM Cid: 0x80780008
          ProcID : 4
          --------------------------------

          TotalTcpCtrlPkt:231 TotalTcpSpecialPortPkt:51 SockID:7 Port:22

          No:133, Time:24/11:12:4.50, SockID=7, Src-Ip=192.168.0.6:54225, Dst-Ip=192.168.0.1:22, Seq=33981, Ack=0, Flag:[0x2]SYN  Direction: RECEIVE.

          No:143, Time:24/11:12:7.359, SockID=7, Src-Ip=192.168.0.6:57535, Dst-Ip=192.168.0.1:22, Seq=25531, Ack=0, Flag:[0x2]SYN  Direction: RECEIVE.

          No:156, Time:24/11:12:27.589, SockID=7, Src-Ip=192.168.0.11:61380, Dst-Ip=192.168.0.1:22, Seq=38325, Ack=0, Flag:[0x2]SYN  Direction: RECEIVE.

          No:166, Time:24/11:12:30.405, SockID=7, Src-Ip=192.168.0.11:64198, Dst-Ip=192.168.0.1:22, Seq=29400, Ack=0, Flag:[0x2]SYN  Direction: RECEIVE.

          --------------------------------
          LDM Pid: 0x780009
          LDM Cid: 0x80780009
          ProcID : 8
          --------------------------------

          TotalTcpCtrlPkt:0 TotalTcpSpecialPortPkt:0 SockID:7 Port:22

          There is no record to display!

          (结果个数 = 8)
          ---    END
  ```
- 查询LDM Partner组件信息：

  ```
  DSP LDMINNERDATA: TYPE=PARTNER, PID="0x670011", CID="0x80780008";
  ```

  ```
          RETCODE = 0  操作成功。

          结果如下
          --------
          诊断信息数据

          --------------------------------
          LDM Pid: 0x780008
          LDM Cid: 0x80780008
          ProcID : 4
          --------------------------------

          Total number   : 15
          --------------------------------
          PartnerPid   CompType  LsId  VsId/FeNodeId LocIndex   Cid         Status  HaRole  PipeID      ServerID  RcvPipeID   PipeState
          ---------------------------------------------------------------------------------------------------------------------------
          0x670011     103       0     0             0x0        -           0       -       0xffffffff  13959170  0xffffffff  0

          (结果个数 = 2)
          ---    END
  ```

#### 输出结果说明

| 输出项名称   | 输出项解释       |
|:--------|:------------|
| 诊断信息数据  | 用来指定诊断信息数据。 |