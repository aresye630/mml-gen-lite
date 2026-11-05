# 查询ND控制块信息（DSP NDINFO）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用来查询ND控制块信息。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识        | 参数名称    | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|:------------|:--------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NDQUERYTYPE | 查询类型    | 可选必选说明：必选参数 参数含义：该参数用来指定查询类型。 数据来源：本端规划 取值范围：枚举类型。 LOCAL：本地信息。PARTNER：Partner组件信息。HA：HA信息。IFM：IFM信息。FES：FES信息。DHCP：DHCP信息。EUM：EUM信息。LDM：LDM信息。PIPE：PIPE信息。VLAN：VLAN信息。INT：接口信息。PORT：端口信息。PV：PV信息。DAD：DAD信息。NB：邻居信息。BLACKBOX：黑匣子信息。NDSECURITY：ND安全信息。WRITEFILE：交互信息。NB_TIMEOUT：邻居超时信息。SOCK：SOCK信息。SOCK_BLACKBOX：SOCK黑匣子信息。PATH：路径信息。NB_OFFLINE：邻居静态物理接口信息。SOCKOPT：SOCKOPT信息。MCAST_PATH：多播路径信息。UCAST_PATH：单播路径信息。PATH_DEL：路径删除信息。SMA：SMA信息。FREENA：空闲NA信息。NBMIB_BLACKBOX：邻居MIB黑匣子信息。RM：RM信息。NBIFINDEX：邻居接口索引信息。HASOCK：HA SOCK信息。MACLIMIT：MAC地址限制邻居信息。IPUDM：静态UDM with IP信息。IPANDMACUDM：静态UDM with MAC信息。DYNUDM：动态UDM信息。NDLIMIT：邻居限制信息。NDSECCHKFAIL：ND安全检查失败信息。ALARM_IPCFLICT：IP冲突告警信息。DISCARDPACKET：丢包信息。GATEWAY：网关信息。 默认值：无 |
| IFQUERYTYPE | 查询接口类型  | 可选必选说明：条件可选参数 前提条件：该参数在“NDQUERYTYPE”配置为“IFM”、“DHCP”、“EUM”、“INT”、“DAD”、“NB”、“NDSECURITY”、“NB_OFFLINE”、“MCAST_PATH”、“UCAST_PATH”、“DISCARDPACKET” 或 “GATEWAY”时为可选参数。 参数含义：该参数用来指定接口查询类型。 数据来源：本端规划 取值范围：枚举类型。 IFINDEX：接口索引。IFNAME：接口名称。 默认值：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| IFINDEX     | 接口索引    | 可选必选说明：条件必选参数 前提条件：该参数在“IFQUERYTYPE”配置为“IFINDEX”时为必选参数。 参数含义：该参数用来指定接口索引。 数据来源：本端规划 取值范围：整数类型，取值范围为1～4294967294。 默认值：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| IFNAME      | 接口名称    | 可选必选说明：条件必选参数 前提条件：该参数在“IFQUERYTYPE”配置为“IFNAME”时为必选参数。 参数含义：该参数用于指定接口名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。接口名称由接口类型+接口编号组成。 默认值：无 配置原则：请使用LST INTERFACE命令查看可用接口。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| IPV6ADDR    | IPv6地址  | 可选必选说明：条件可选参数 前提条件：该参数在“NDQUERYTYPE”配置为“NB”、“UCAST_PATH” 或 “DYNUDM”时为可选参数。 参数含义：该参数用来指定IPv6地址。 数据来源：本端规划 取值范围：IPv6地址类型。 默认值：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| PID         | ND组件PID | 可选必选说明：条件可选参数 前提条件：该参数在“NDQUERYTYPE”配置为“LOCAL”、“PARTNER”、“HA”、“IFM”、“FES”、“DHCP”、“EUM”、“LDM”、“PIPE”、“VLAN”、“INT”、“PORT”、“PV”、“DAD”、“NB”、“BLACKBOX”、“NDSECURITY”、“SOCK”、“NB_OFFLINE”、“SOCKOPT”、“MCAST_PATH”、“UCAST_PATH”、“PATH_DEL”、“SMA”、“FREENA”、“HASOCK”、“MACLIMIT”、“IPUDM”、“IPANDMACUDM”、“DYNUDM” 或 “ALARM_IPCFLICT”时为可选参数。 参数含义：该参数用来指定ND组件的PID。 数据来源：本端规划 取值范围：十六进制整数类型，取值范围为0x0～0xFFFFFFFF。 默认值：无                                                                                                                                                                                                                                                                                                                   |
| ISSLAVE     | 主备类型    | 可选必选说明：可选参数 参数含义：该参数用来指定主备类型。 数据来源：本端规划 取值范围：枚举类型。 Master：主资源单元。Slave：备资源单元。 默认值：Master                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

#### 使用实例

- 查询ND控制块本地信息：

  ```
  DSP NDINFO:NDQUERYTYPE=LOCAL,PID="0x73003a";
  ```

  ```
  RETCODE = 0  操作成功。

  结果如下
  --------
  查询结果数据  =    Param:
      ParamNo               : 3
      CmdKey                : 1
      IfIndex               : 0
      Param1                : 0
      Param2                : 0
      Addr                  : ::0
      Pid                   : 0x73003a
    Pid: 0x73003a
      Cid        : 0x8073007b
    LOCAL:
      Pid        : 0x73003a
      Cid        : 0x8073007b
      TmHandle   : 0xac
      WorkMode   : 0x0
      BackupMode : 0x0
      SlaveCid   : 0x0
      CompType   : 0x73
      PromptPrimaryFlag   : 0x0
      DIMENSION  : 3
      BoardId    : 0
      SlotLastAlarmTime : 0
      SlotName   :
      InterfaceNode : 0
      SemAgentPid: 0x80030076
      IFM        : PID(0x7a0011)  Status(0x0)  SubFlag(0x1)
      LLA        : PID(0x240038)  Status(0x0)  SubFlag(0x1)
      EUM        : PID(0xa60021)  Status(0x0)  SubFlag(0x1)
      Partner    : 5
      FESTree    : 2
        IfmTimer   : Stop
      SspSubscribeTimer   : Stop
      NdState    : 0x1
      SendCtlTime: 0x0
      SeqNumber  : 0x1
      TransNum   : 0x0
      HaOnWalk   : 0x0
      NbHaTree   : 0x0
      IfTree     : 0x0
      BatchUpdateList   : 0x0
      BackupBatchUpdateList   : 0x0
      RealUpdateList   : 0x0
      SockHaTree   : 0
      NdPafVal    : 65536
      NdIfPafVal : 16384
      TotalEntryNum  : 0
      StaticEntryNum   : 0
      DynamicEntryNum   : 0
      EUM PID: 0xA60021        State: 5
          AuthIf = 0    SendSmoothBeginTime = 4    SendSmoothEndTime = 4    Auth Number = 0    AuthWaitAck Number = 0
          DeAuth Number = 0    DeAuthWaitAck Number = 0    AuthBackup Number = 0    UserTrace Number = 0
      NdEumEntry Number = 0    NdEumEntry State = 6    EumEntry    SeqNum = 3    LastTime of send ERROR MSG = 0
      LLA PID: 0x240038
      CPU OverloadState: UNOVERLOAD, OverloadState:2
      CpuOverloadCnt   : 0
      CpuUnOverloadCnt : 0
      ProcDadNum       : 100

  (结果个数 = 1)
  ---    END
  ```
- 查询ND控制块Partner组件信息：

  ```
  DSP NDINFO:NDQUERYTYPE=PARTNER,PID="0x73003a";
  ```

  ```
  RETCODE = 0  操作成功。

  结果如下
  --------
  查询结果数据  =    Param:
      ParamNo               : 3
      CmdKey                : 2
      IfIndex               : 0
      Param1                : 0
      Param2                : 0
      Addr                  : ::0
      Pid                   : 0x73003a
    Pid: 0x73003a
      Cid        : 0x8073007b
    Partner:
      PartnerTreeNode    : 8
      Pid = 0X6a0012, CompType = 106, SubFlag = 1, CompStatus = 0, ReferCount = 1, NodeId = 4259585
      Pid = 0X6a0016, CompType = 106, SubFlag = 1, CompStatus = 0, ReferCount = 1, NodeId = 0
      Pid = 0X78000f, CompType = 120, SubFlag = 1, CompStatus = 1, ReferCount = 1, NodeId = 130817
      Pid = 0X780010, CompType = 120, SubFlag = 1, CompStatus = 1, ReferCount = 1, NodeId = 196353
      Pid = 0X780011, CompType = 120, SubFlag = 1, CompStatus = 1, ReferCount = 1, NodeId = 4259585
      Pid = 0X8078000f, CompType = 120, SubFlag = 1, CompStatus = 0, ReferCount = 0, NodeId = 0
      Pid = 0X80780010, CompType = 120, SubFlag = 1, CompStatus = 0, ReferCount = 0, NodeId = 0
      Pid = 0X80780011, CompType = 120, SubFlag = 1, CompStatus = 0, ReferCount = 0, NodeId = 0
      RMPartnerTreeNode  : 1
      Pid = 0X230008, SubFlag = 1, CompStatus = 0
      Pid = 0Xa60021, SubFlag = 1, CompStatus = 0

  (结果个数 = 1)
  ---    END
  ```
- 查询ND控制块HA信息：

  ```
  DSP NDINFO:NDQUERYTYPE=HA,PID="0x73003a";
  ```

  ```
  RETCODE = 0  操作成功。

  结果如下
  --------
  查询结果数据  =    Param:
      ParamNo               : 3
      CmdKey                : 3
      IfIndex               : 0
      Param1                : 0
      Param2                : 0
      Addr                  : ::0
      Pid                   : 0x73003a
    Pid: 0x73003a
      Cid        : 0x8073007b

  (结果个数 = 1)
  ---    END
  ```
- 查询ND控制块动态UDM信息：

  ```
  DSP NDINFO:NDQUERYTYPE=DYNUDM,IPV6ADDR="2001:db8::1",PID="0x73003a";
  ```

  ```
  RETCODE = 0  操作成功。

  结果如下
  --------
  查询结果数据  =    Param:
      ParamNo               : 4
      CmdKey                : 39
      IfIndex               : 0
      Param1                : 0
      Param2                : 0
      Addr                  : 2001:db8::1
      Pid                   : 0x73003a
    Pid: 0x73003a
      Cid        : 0x8073007b
    DynNodes:0 IasL2UsrListNum:0

  (结果个数 = 1)
  ---    END
  ```
- 查询ND控制块邻居信息：

  ```
  DSP NDINFO:NDQUERYTYPE=NB,IFQUERYTYPE=IFNAME,IFNAME="Ethernet64/0/3",IPV6ADDR="2001:db8::1",PID="0x73003a";
  ```

  ```
  RETCODE = 0  操作成功。

  结果如下
  --------
  查询结果数据  =    Param:
      ParamNo               : 5
      CmdKey                : 16
      IfIndex               : 6
      Param1                : 0
      Param2                : 0
      Addr                  : 2001:db8::1
      Pid                   : 0x73003a
    Pid: 0x73003a
      Cid        : 0x8073007b

  (结果个数 = 1)
  ---    END
  ```
- 查询ND控制块单播路径信息：

  ```
  DSP NDINFO:NDQUERYTYPE=UCAST_PATH,IFQUERYTYPE=IFINDEX,IFINDEX=6,IPV6ADDR="2001:db8::1",PID="0x73003a";
  ```

  ```
  RETCODE = 0  操作成功。

  结果如下
  --------
  查询结果数据  =    Param:
      ParamNo               : 5
      CmdKey                : 28
      IfIndex               : 6
      Param1                : 0
      Param2                : 0
      Addr                  : 2001:db8::1
      Pid                   : 0x73003a
    Pid: 0x73003a
      Cid        : 0x8073007b
    UcastPath(If=6,D=2001:db8::1):
      NB Not Exitst:

  (结果个数 = 1)
  ---    END
  ```

#### 输出结果说明

| 输出项名称   | 输出项解释                 |
|:--------|:----------------------|
| 查询结果数据  | 用于显示查询ND控制块信息得到的结果数据。 |