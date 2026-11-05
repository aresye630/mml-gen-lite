# 查询LLA诊断信息（DSP LLAINNERDATA）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于查询LLA诊断信息。不指定CID参数时，查询所有LLA的诊断信息，当指定CID参数时，查询指定LLA诊断信息。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识   | 参数名称         | 参数说明                                                                                                                                           |
|:-------|:-------------|:-----------------------------------------------------------------------------------------------------------------------------------------------|
| TYPE   | 内部数据类型       | 可选必选说明：必选参数 参数含义：该参数用来指定内部数据类型。 数据来源：本端规划 取值范围：枚举类型。 PIPE：管道信息。PCT：PCT表信息。PARTNER：Partner组件信息。LOCAL：本地信息。MBUF_DISCARD_BLACK_BOX：丢包黑匣子信息。 默认值：无 |
| PID    | Partner组件PID | 可选必选说明：条件必选参数 前提条件：该参数在“TYPE”配置为“PIPE”时为必选参数。 参数含义：该参数用来指定Partner组件的PID。 数据来源：本端规划 取值范围：十六进制整数类型，取值范围为0x0～0xFFFFFFFF。 默认值：无                    |
| CID    | LLA组件CID     | 可选必选说明：可选参数 参数含义：该参数用来指定LLA组件CID。 数据来源：本端规划 取值范围：十六进制整数类型，取值范围为0x0～0xFFFFFFFF。 默认值：无                                                           |

#### 使用实例

- 查询LLA管道信息：

  ```
  DSP LLAINNERDATA: TYPE=PIPE, PID="0x24001b";
  ```

  ```
          RETCODE = 0  操作成功。

          结果如下
          --------
          查询结果数据

          --------------------------------
          LLA Cid: 0x80240038
          --------------------------------

          partnerPID    CompType  CID         CIDNo. PipeMessage         ChangeNum   LastTime
          ----------------------------------------------------------------------------------------------
          0x24001b      36        -           -      OPEN                0           0-0-0 0:0:0 0

          0x24001b      36        -           -      CLOSE               0           0-0-0 0:0:0 0

          0x24001b      36        -           -      OPEN_FAIL           0           0-0-0 0:0:0 0

          0x24001b      36        -           -      OPEN_RSP_OK         0           0-0-0 0:0:0 0

          0x24001b      36        -           -      OPEN_RSP_ERR        0           0-0-0 0:0:0 0

          0x24001b      36        -           -      OPEN_REQ_ACCEPT     0           0-0-0 0:0:0 0

          0x24001b      36        -           -      OPEN_REQ_REJECT     0           0-0-0 0:0:0 0

          0x24001b      36        -           -      PIPE_CLOSE_REQ      0           0-0-0 0:0:0 0

          0x24001b      36        -           -      PIPE_CLOSE_RSP      0           0-0-0 0:0:0 0

          0x24001b      36        -           -      OPEN_REQ_ACCEPT_RSP 0           0-0-0 0:0:0 0

          0x24001b      36        -           -      STAT_AVAILABLE      1           2017-4-1 14:35:10 520

          0x24001b      36        -           -      STAT_UNAVAILABLE    0           0-0-0 0:0:0 0

          0x24001b      36        -           -      SEND_REG_OK         0           0-0-0 0:0:0 0

          0x24001b      36        -           -      SEND_REG_ERR        0           0-0-0 0:0:0 0

          0x24001b      36        -           -      PIPE_ID_ERROR       0           0-0-0 0:0:0 0

          0x24001b      36        -           -      CID_INIT            0           0-0-0 0:0:0 0

          0x24001b      36        -           -      CID_INIT_BYPID      0           0-0-0 0:0:0 0

          0x24001b      36        -           -      CID_DEL             0           0-0-0 0:0:0 0

          (结果个数 = 19)
          ---    END
  ```
- 查询LLA PCT表信息：

  ```
  DSP LLAINNERDATA: TYPE=PCT, CID="0x80240038";
  ```

  ```
          RETCODE = 0  操作成功。

          结果如下
          --------
          查询结果数据

          --------------------------------
          LLA Cid: 0x80240038
          --------------------------------

          ------------------------------------------------------------------------------------------------------------------
          IfIndex  PortType   LinkType   VS         VrfIndex   NodeId       GroupId      IfType     HWCpyFlag  IfExternValue
          ------------------------------------------------------------------------------------------------------------------
          1        0x12       0xff       0x0        0x0        0xffff0001   0x1          0x12       0x0        0x0

          2        0x11       0xff       0x0        0x0        0xffff0001   0x2          0x11       0x0        0x0

          3        0x1a       0x0        0x0        0x1        0xffff0001   0x80000003   0x1a       0x0        0x0

          4        0x4f       0x0        0x0        0x2        0xffff0001   0x80000004   0x4f       0x0        0x0

          5        0x50       0x0        0x0        0x0        0x1          0x80000005   0x50       0x0        0x0

          6        0x22       0x0        0x0        0x1        0x1          0x80000006   0x22       0x0        0x0

          (结果个数 = 7)
          ---    END
  ```
- 查询LLA Partner组件信息：

  ```
  DSP LLAINNERDATA: TYPE=PARTNER, CID="0x80240038";
  ```

  ```
          RETCODE = 0  操作成功。

          结果如下
          --------
          查询结果数据

          --------------------------------
          LLA Cid: 0x80240038
          --------------------------------

          --------------------------------------------------------------------------------------------------------------------------------------------------------
          ComType    Pid        ComGrp     LsId       VsId       DeployMode   MngEntityId   CompStatus   CompEvent   PipeId      ServiceId   RcvPipeId   PipeState
          --------------------------------------------------------------------------------------------------------------------------------------------------------
          0x24       0x24001b   0x19       0x0        0x0        0xe          0x3e8         0x0          0x0         0xffffffff  0x1         0xffffffff  0x0

          0x6a       0x6a0013   0x0        0x0        0x0        0x1          0x0           0x0          0x0         0xffffffff  0x1         0xffffffff  0x0

          0x77       0x77000a   0xb5       0x0        0x0        0xb          0x80000003    0x0          0x0         0xffffffff  0x1         0x4008000e  0x0

          0x78       0x780008   0xba       0x0        0x0        0xc          0x1ff01       0x1          0x0         0x8008000d  0x0         0xffffffff  0x2
          0x78       0x780008   0xba       0x0        0x0        0xc          0x1ff01       0x1          0x0         0x0         0x0         0x0         0x0
          0x78       0x780008   0xba       0x0        0x0        0xc          0x1ff01       0x1          0x0         0x0         0x0         0x0         0x0

          (结果个数 = 5)
          ---    END
  ```
- 查询LLA本地信息：

  ```
  DSP LLAINNERDATA: TYPE=LOCAL, CID="0x80240038";
  ```

  ```
          RETCODE = 0  操作成功。

          结果如下
          --------
          查询结果数据

          --------------------------------
          LLA Cid: 0x80240038
          --------------------------------

          -------------------------------------------------
          LocCid               = 0x80240038
          LocPid               = 0x24001b
          PeerCid              = 0x0
          CompState            = START_WORK
          LocationId           = 1000
          DcProductType        = 0
          CompWorkMode         = HA_BE_PRIMARY
          FesSeqErrFlag        = 0x0
          NodeId               = 0x0
          Flag                 = 0x0
          CachemCompStatus     = HA_PARTNER_STATE_AVAILABLE
          CachemServiceStatus  = LLA_MSG_RET_OK
          CachemSmoothEndFlag  = LLA_CACHEM_SMOOTH_INIT
          SrvSmoothEndFlag     = LLA_SRV_SMOOTH_OK
          PathIssuState        = 5
          MsgRetransTimerId    = 0
          MsgCacheTimerId      = 1
          DiscardPktMum        = 0
          IssuBatchStat        = LLA_ISSU_BEGIN
          IssuBatchSeq         = 0
          IssuRealSeq          = 0
          LogicMngEPort        = 4
          ActiveMngEPort       = 5
          BackAcMngEPort       = 4294967295
          LogicMngBPort        = 3
          ActiveMngBPort       = 6
          BackAcMngBPort       = 4294967295
          FirstArpTime         = 2017-4-1 14:35:13 645
          -------------------------------------------------

          (结果个数 = 2)
          ---    END
  ```

#### 输出结果说明

| 输出项名称   | 输出项解释       |
|:--------|:------------|
| 查询结果数据  | 用来显示查询结果数据。 |