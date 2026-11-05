# 查询ARP内部信息（DSP ARPINNERDATA）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于查看ARP内部信息。

#### 注意事项

- 参数CID只能是ARP组件号。
- 参数PID可以是LDM、SOCK、FES、IFM、EUM、RGM、LLA的进程号。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识         | 参数名称   | 参数说明                                                                                                                                                                                                                                                                                                                           |
|:-------------|:-------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| INFOTYPE     | 信息类型   | 可选必选说明：必选参数 参数含义：该参数用于指定查询信息的类型。 数据来源：本端规划 取值范围：枚举类型。 ArpByIP：根据IP地址查询表项。BlackBox：根据进程号查询表项。FesInfo：查询fes相关表项。Global：查询全局表项。IfData：根据接口索引查询表项。IfPolicy：根据接口索引查询表项。Local：查询本地表项。Partner：可根据进程号查询表项。PipeInfo：查询管道表项。ProbeInfoByMember：查询成员口探测表项。ProbeInfoBySession：查询探测会话表项。AttackMacList：查询攻击者MAC链。MacConflict：查询MAC冲突次数。 默认值：无 |
| IPADDRESS    | IP地址   | 可选必选说明：条件必选参数 前提条件：该参数在“INFOTYPE”配置为“ArpByIP”、“ProbeInfoBySession” 或 “AttackMacList”时为必选参数。 可选必选说明：条件可选参数 前提条件：该参数在“INFOTYPE”配置为“ProbeInfoByMember”时为可选参数。 参数含义：该参数用于显示指定IPv4地址的内部信息。 数据来源：本端规划 取值范围：IPv4地址类型。IP地址0.0.0.0～255.255.255.255。 默认值：无                                                                               |
| PID          | 进程号    | 可选必选说明：条件必选参数 前提条件：该参数在“INFOTYPE”配置为“BlackBox”时为必选参数。 可选必选说明：条件可选参数 前提条件：该参数在“INFOTYPE”配置为“Partner”时为可选参数。 参数含义：该参数用于显示指定进程号的内部信息。 数据来源：本端规划 取值范围：十六进制整数类型，取值范围为0～0xFFFFFFFF。 默认值：无                                                                                                                                            |
| IFNAME       | 接口名    | 可选必选说明：条件必选参数 前提条件：该参数在“INFOTYPE”配置为“IfData”、“IfPolicy”、“ProbeInfoByMember”、“ProbeInfoBySession” 或 “AttackMacList”时为必选参数。 可选必选说明：条件可选参数 前提条件：该参数在“INFOTYPE”配置为“ArpByIP”时为可选参数。 参数含义：该参数用于显示指定接口名的内部信息。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。以太网接口名称由接口类型和接口编号组成。 默认值：无 配置原则：请使用LST INTERFACE命令查看可用接口。                              |
| CID          | 组件号    | 可选必选说明：可选参数 参数含义：该参数用于显示指定组件号的内部信息。 数据来源：本端规划 取值范围：十六进制整数类型，取值范围为0～0xFFFFFFFF。 默认值：无                                                                                                                                                                                                                                           |
| MEMBERIFNAME | 成员口名称  | 可选必选说明：条件必选参数 前提条件：该参数在“INFOTYPE”配置为“ProbeInfoByMember”时为必选参数。 可选必选说明：条件可选参数 前提条件：该参数在“INFOTYPE”配置为“ProbeInfoBySession”时为可选参数。 参数含义：该参数用于显示指定成员口的内部信息。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。以太网接口名称由接口类型和接口编号组成。 默认值：无 配置原则：请使用LST INTERFACE命令查看可用接口。                                                                              |

#### 使用实例

- 查看ArpByIP类型表项信息：

  ```
  DSP ARPINNERDATA:INFOTYPE=ArpByIP,IPADDRESS="10.1.1.1",IFNAME="Ethernet64/0/3",CID="0x8077000e";
  ```

  ```
          RETCODE = 0  操作成功。

          结果如下
          --------
          查询结果信息  =    ARP Cid:0x8077000e
            IpAddr            = 0xc0a82739
            ArpType           = 0x4
            VrfIndex          = 0x1
            VrIndex           = 0x0
            IfIndex           = 0x5
            WorkIfIndex       = 0x0
            uiWorkMainIfIndex = 0x0
            FlowId            = 0xffffffff
            NetRole           = 0x0
            UnAgeing          = 0x0
            BridgeID          = 0x0
            PeVid             = 0x0
            CeVid             = 0x0
            EgressNickName    = 0x0
            MacAddr           = 00E0-FC12-3456
            ArpStatusFlag     = 0x2
            ItermVer          = 0x0
            FixFlag           = 0x0
            DelFlag           = 0x0
            FlushFilterFlag   = 0x0
            TblControlFlag    = 0x0
            AskTimes          = 0x0
            LastUpdateTick    = 0x0
            SendAckUnlockTime = 0x0
            TimeoutType       = 0x0
            Encaptype         = 0x0
            BridgeType        = 0x0
            UpDateFlag        = 0x0
            ExpireTime (s)    = 0x0

          (结果个数 = 1)
          ---    END
  ```
- 查看BlackBox类型表项信息：

  ```
  DSP ARPINNERDATA:INFOTYPE=BlackBox,PID="8065000d";
  ```

  ```
          RETCODE = 0  操作成功。

          结果如下
          --------
          查询结果信息

            ARP Cid:0x8077000e
          =========================================================
            11-08 21:53:49:951 Receive component status change to : 0 (0:aval, 1:unaval)

            11-08 21:53:59:450 Receive pipe open request. pipeId = 1074266133 .

            11-08 21:53:59:450 Receive pipe open respond. pipeId = 524310, result = 0.

            11-08 21:53:59:952 Receive pipe open request. pipeId = 1074266135 .

            11-08 21:53:59:952 Receive pipe open respond. pipeId = 524312, result = 0.

          (结果个数 = 5)
          ---    END
  ```
- 查看FesInfo类型表项信息：

  ```
  DSP ARPINNERDATA:INFOTYPE=FesInfo;
  ```

  ```
          RETCODE = 0  操作成功。

          结果如下
          --------
          查询结果信息  =    ARP Cid:0x8077000e
          =========================================================
            CommPid         = 0x6a0013
            MsgTranNo       = 0
            RealSeqNo       = 8
            BatchSeqNo      = 5
            UpdateArpCnt    = 6
            DelArpCnt       = 0
            IsEventSent     = 1
            TblId           = 108
            InSmooth        = 5
            TblId           = 7
            InSmooth        = 5

          (结果个数 = 1)
          ---    END
  ```
- 查看Global类型表项信息：

  ```
  DSP ARPINNERDATA:INFOTYPE=Global;
  ```

  ```
          RETCODE = 0  操作成功。

          结果如下
          --------
          查询结果信息  =    ARP Cid:0x8077000e
          =========================================================
            VrID            = 0
            SysLearnStrict  = 0
            SysArpFixType   = 0
            SysDropGratArp  = 0
            ArpSrcMacCheck  = 0
            LogTrapTime     = 0
            IsVrSpecConfig  = 0
            MaxArpEntry     = 131072
            StaticArpNum    = 0
            DynArpNum       = 6
            FakeArpNum      = 0
            ProbeEnable     = 1
            ProbeMode       = 0
            ProbeTimes      = 3
            ProbeInterval   = 5
            ExpireTime      = 1200
            FakeExpireTime  = 3
            ConvergeMode    = 2
            ACLHandle       = 0
            GrattsEnable    = 0
            LooseLearnEn    = 0
            LoopSndGratArp  = 0
            SuppTime        = 0
            pktSrvHandle    = 2
            pktSrvSockStat  = 1
            pktSrvSockStep  = 2
            DupMacEnable    = 0x0

          (结果个数 = 1)
          ---    END
  ```
- 查看IfData类型表项信息：

  ```
  DSP ARPINNERDATA:INFOTYPE=IfData,IFNAME="Ethernet64/0/3";
  ```

  ```
          RETCODE = 0  操作成功。

          结果如下
          --------
          查询结果信息  =    ARP Cid:0x8077000e
          =========================================================
            IfIndex          = 0x5
            VrIndex          = 0x0
            VrfIndex         = 0x1
            GroupId          = 0x80000003
            MainIfIndex      = 0x0
            IfPhyType        = 0x1a
            SubIfVlanType    = 0x0
            MacAddr          = 00E0-FC12-3456
            IfServType       = 0x0
            IfStatus         = 0xd
            AuthFlag         = 0x0
            IpUnnumber       = 0x0
            ArpProxyFlag     = 0x0
            ArpBCastEnable   = 0x0
            ArpProbeEnable   = 0x0
            ArpProbeMode     = 0x0
            ArpProbeTimes    = 0x3
            ArpProbeInterval = 0x5
            ArpExpireTime    = 0x4b0
            ArpFakeTime      = 0x3
            ArpDynNum        = 0x6
            ArpStaNum        = 0x0
            ArpStrictLearn   = 0x3
            ArpLearnCheck    = 0x0
            ArpMacValid      = 0x0
            DropGratArp      = 0x0
            ArpFixType       = 0x0
            Portflag         = 0x0
            IfVlanID         = 0x0
            WaitSendNum      = 0x0
            TblDelMode       = 0x0

          (结果个数 = 1)
          ---    END
  ```
- 查看IfPolicy类型表项信息：

  ```
  DSP ARPINNERDATA:INFOTYPE=IfPolicy,IFNAME="Ethernet64/0/3";
  ```

  ```
          RETCODE = 0  操作成功。

          结果如下
          --------
          查询结果信息

            ARP Cid:0x8077000e
          =========================================================
            uiIpAddr       = 0xc0a80000
            NetMask        = 0xffff0000
            MacAddr        = 00E0-FC12-3456
            TblCnt         = 0x1
            MatchType      = 0x2
            PolicyType     = 0x1

            uiIpAddr       = 0xc0a82739
            NetMask        = 0xffff0000
            MacAddr        = 00E0-FC12-3457
            TblCnt         = 0x1
            MatchType      = 0x1
            PolicyType     = 0x1

          (结果个数 = 2)
          ---    END
  ```
- 查看Local类型表项信息：

  ```
  DSP ARPINNERDATA:INFOTYPE=Local;
  ```

  ```
          RETCODE = 0  操作成功。

          结果如下
          --------
          查询结果信息  =    ARP Cid:0x8077000e
          =========================================================
            CompPid          = 0x77000a
            CompCid          = 0x8077000e
            MastCompCid      = 0x8077000e
            SlaveCompCid     = 0x80770070
            CompWorkMode     = 0x0
            CompHaStage      = 0x2
            RecoveryFlag     = 0x0
            NodeId           = 0x0
            LrID             = 0x0
            HInitErr         = 0x0
            CpuOverState     = 0x1
            RcvTotalPkt      = 0x26
            TimeoutRate      = 0x0
            TimeoutNum       = 0x0
            TimerPrecision   = 0x1
            TimerQueueNum    = 0x4b1
            BrasTimerQueueNum= 0x0
            TimerMaxTimeOut  = 0x4b0
            TimerMoudleID    = 0x1
            TimerCurrQueue   = 0x4a0
            BrasTimerCurQueue= 0x0
            TimerCnt         = 0xc048
            TimerCreateErr   = 0x0
            LastTimeL        = 0x2ef4dca
            LastTimeH        = 0x0
            SendGratArp      = 0x0
            IfLearnMaxNum    = 0x10000
            DbgFlag          = 0x0
            FlushProbeNum    = 0x0
            DynArpEntryNum   = 0x6
            StaArpEntryNum   = 0x0
            DynArpNumMax     = 0x20000
            StaArpNumMax     = 0x4000
            UserTraceNum     = 0x0
            MissAmerNum      = 0x0
            ArpNodesCnt      = 0x8
            UserTraceNodesCnt= 0x0
            ArpSockCount     = 0x2
            Index = 0x0, val = 0x0

          (结果个数 = 1)
          ---    END
  ```
- 查看Partner类型表项信息：

  ```
  DSP ARPINNERDATA:INFOTYPE=Partner;
  ```

  ```
          RETCODE = 0  操作成功。

          结果如下
          --------
          查询结果信息  =    ARP Cid:0x8077000e
          =========================================================
            ComType          = 0x78
            Pid              = 0x780008
            LrId             = 0x0
            VrId             = 0x0
            NodeId           = 0x1ff01
            CompStatus       = 0x0
            ServiceState     = 0x0
            PushState        = 0x0
            SeqErrAckState   = 0x0
            BatchSeqNo       = 0x1
            ItemVer          = 0x0

          (结果个数 = 1)
          ---    END
  ```
- 查看PipeInfo类型表项信息：

  ```
  DSP ARPINNERDATA:INFOTYPE=PipeInfo;
  ```

  ```
          RETCODE = 0  操作成功。

          结果如下
          --------
          查询结果信息

            ARP Cid:0x8077000e
          =========================================================
            LLA SendPipeId      = 0x80013
            LLA SendServiceId   = 0x8077000e
            LLA SendPipeStatus  = 0x2
            LLA RevPipeId       = 0x0
            LLA RevServiceId    = 0x0
            Pid                 = 0x780008
            RevPipeId           = 0xc0200001
            RevServiceId        = 0x3
            SendPipeId          = 0x0
            SendServiceId       = 0x0
            SendPipeStatus      = 0x0

            Pid                 = 0x8065000d
            RevPipeId           = 0xffffffff
            RevServiceId        = 0x0
            SendPipeId          = 0x0
            SendServiceId       = 0x0
            SendPipeStatus      = 0x0

            Pid                 = 0x780009
            RevPipeId           = 0xc008002a
            RevServiceId        = 0x3
            SendPipeId          = 0x0
            SendServiceId       = 0x0
            SendPipeStatus      = 0x0

          (结果个数 = 3)
          ---    END
  ```
- 查看AttackMacList类型表项信息：

  ```
  DSP ARPINNERDATA:INFOTYPE=AttackMacList,IPADDRESS="10.1.1.1",IFNAME="Ethernet67/0/6";
  ```

  ```
          RETCODE = 0  操作成功。

          结果如下
          --------
          查询结果信息  =    ARP Cid:0x80770090
          =========================================================
           ======================================================
           IfIndex          = 19
           IpAddress        = 167837953
           TrustMac         = 00E0-FC12-3459
           TrustMacCount    = 6
           ==============================================
           ConflictMac      = 00E0-FC12-345A
           Count            = 23
           ==============================================
           ConflictMac      = 00E0-FC12-345B
           Count            = 22
           ======================================================

          (结果个数 = 1)
          ---    END
  ```
- 查看MacConflict类型表项信息：

  ```
  DSP ARPINNERDATA:INFOTYPE=MacConflict;
  ```

  ```
          RETCODE = 0  操作成功。

          结果如下
          --------
          查询结果信息  =    ARP Cid:0x80770090
          =========================================================
           ======================================================
           IfIndex          = 19
           IpAddress        = 167837953
           VrfIndex         = 0
           ConflictCount    = 187
           ======================================================

          (结果个数 = 1)
          ---    END
  ```

#### 输出结果说明

| 输出项名称              | 输出项解释             |
|:-------------------|:------------------|
| IpAddr             | 该参数表示IPv4地址。      |
| ArpType            | 该参数表示ARP类型。       |
| VrfIndex           | 该参数表示VPN实例索引。     |
| VrIndex            | 该参数表示VR索引。        |
| IfIndex            | 该参数表示接口索引。        |
| WorkIfIndex        | 该参数表示工作接口索引。      |
| uiWorkMainIfIndex  | 该参数表示工作主接口索引。     |
| FlowId             | 该参数表示流ID。         |
| NetRole            | 该参数表示网络角色。        |
| UnAgeing           | 该参数表示老化状态。        |
| BridgeID           | 该参数表示广播域ID。       |
| PeVid              | 该参数表示外层VLAN ID。   |
| CeVid              | 该参数表示内层VLAN ID。   |
| EgressNickName     | 该参数表示出网络名。        |
| MacAddr            | 该参数表示MAC地址。       |
| ArpStatusFlag      | 该参数表示ARP状态标记。     |
| ItermVer           | 该参数表示ARP版本号。      |
| FixFlag            | 该参数表示固定标记。        |
| DelFlag            | 该参数表示删除标记。        |
| FlushFilterFlag    | 该参数表示刷新过滤标记。      |
| TblControlFlag     | 该参数表示表控制标记。       |
| AskTimes           | 该参数表示请求次数。        |
| LastUpdateTick     | 该参数表示最新更新时间。      |
| SendAckUnlockTime  | 该参数表示发应答解锁时间。     |
| TimeoutType        | 该参数表示超时类型。        |
| Encaptype          | 该参数表示封装类型。        |
| BridgeType         | 该参数表示桥类型。         |
| UpDateFlag         | 该参数表示更新标记。        |
| ExpireTime         | 该参数表示到期时间。        |
| uiIpAddr           | 该参数表示IPv4地址。      |
| NetMask            | 该参数表示网络掩码。        |
| TblCnt             | 该参数表示表计数。         |
| MatchType          | 该参数表示匹配类型。        |
| PolicyType         | 该参数表示策略类型。        |
| GroupId            | 该参数表示组号。          |
| IfPhyType          | 该参数表示接口物理类型。      |
| SubIfVlanType      | 该参数表示子接口VLAN类型。   |
| IfServType         | 该参数表示接口服务类型。      |
| IfStatus           | 该参数表示接口状态。        |
| AuthFlag           | 该参数表示授权标记。        |
| IpUnnumber         | 该参数表示地址借用。        |
| ArpProxyFlag       | 该参数表示ARP代理标记。     |
| ArpBCastEnable     | 该参数表示ARP广播使能。     |
| ArpProbeEnable     | 该参数表示ARP探测使能。     |
| ArpProbeMode       | 该参数表示ARP探测模式。     |
| ArpProbeTimes      | 该参数表示ARP探测次数。     |
| ArpProbeInterval   | 该参数表示ARP探测间隔。     |
| ArpExpireTime      | 该参数表示ARP到期时间。     |
| ArpFakeTime        | 该参数表示ARP假表项时间。    |
| ArpDynNum          | 该参数表示动态ARP数量。     |
| ArpStaNum          | 该参数表示ARP表项数量。     |
| ArpStrictLearn     | 该参数表示ARP严格学习。     |
| ArpLearnCheck      | 该参数表示ARP学习检查。     |
| ArpMacValid        | 该参数表示MAC有效标记。     |
| DropGratArp        | 该参数表示免费ARP丢弃。     |
| Portflag           | 该参数表示端口标记。        |
| ArpFixType         | 该参数表示ARP修复类型。     |
| IfVlanID           | 该参数表示接口VLAN。      |
| WaitSendNum        | 该参数表示待发报文数。       |
| TblDelMode         | 该参数表示表项删除模式。      |
| CommPid            | 该参数表示组件进程号。       |
| MsgTranNo          | 该参数表示发送报文号。       |
| RealSeqNo          | 该参数表示实际序列号。       |
| BatchSeqNo         | 该参数表示批量序列号。       |
| UpdateArpCnt       | 该参数表示更新ARP数量。     |
| DelArpCnt          | 该参数表示删除ARP数量。     |
| IsEventSent        | 该参数表示事件发送标记。      |
| TblId              | 该参数表示表项号。         |
| InSmooth           | 该参数表示是否在平滑。       |
| SysLearnStrict     | 该参数表示系统严格学习。      |
| SysDropGratArp     | 该参数表示系统免费ARP丢弃。   |
| ArpSrcMacCheck     | 该参数表示源MAC检查标记。    |
| LogTrapTime        | 该参数表示日志上报时间。      |
| IsVrSpecConfig     | 该参数表示虚拟路由特殊定制标记。  |
| MaxArpEntry        | 该参数表示最大ARP表项。     |
| StaticArpNum       | 该参数表示静态ARP数量。     |
| DynArpNum          | 该参数表示动态ARP数量。     |
| FakeArpNum         | 该参数表示ARP假表项数量。    |
| ProbeEnable        | 该参数表示ARP探测使能。     |
| ProbeMode          | 该参数表示ARP探测模式。     |
| ProbeTimes         | 该参数表示ARP探测次数。     |
| ProbeInterval      | 该参数表示ARP探测间隔。     |
| FakeExpireTime     | 该参数表示假表项到期时间。     |
| ConvergeMode       | 该参数表示聚合模式。        |
| ACLHandle          | 该参数表示ACL句柄。       |
| GrattsEnable       | 该参数表示免费ARP发送使能。   |
| LooseLearnEn       | 该参数表示宽松学习使能。      |
| LoopSndGratArp     | 该参数表示循环发送免费ARP。   |
| SuppTime           | 该参数表示抑制时间。        |
| pktSrvHandle       | 该参数表示包服务句柄。       |
| pktSrvSockStat     | 该参数表示包服务套接字状态。    |
| pktSrvSockStep     | 该参数表示包服务套接字步长。    |
| DupMacEnable       | 该参数表示重复MAC使能。     |
| CompCid            | 该参数表示组件号。         |
| MastCompCid        | 该参数表示主组件号。        |
| SlaveCompCid       | 该参数表示备组件号。        |
| CompWorkMode       | 该参数表示组件工作模式。      |
| CompHaStage        | 该参数表示组件HA阶段。      |
| RecoveryFlag       | 该参数表示恢复标记。        |
| NodeId             | 该参数表示节点号。         |
| LrID               | 该参数表示逻辑路由号。       |
| HInitErr           | 该参数表示初始化错误句柄。     |
| CpuOverState       | 该参数表示CPU过载状态。     |
| RcvTotalPkt        | 该参数表示接收包总数。       |
| TimeoutRate        | 该参数表示超时速率。        |
| TimeoutNum         | 该参数表示超时数量。        |
| TimerPrecision     | 该参数表示定时器精度。       |
| TimerQueueNum      | 该参数表示定时器队列数。      |
| BrasTimerQueueNum  | 该参数表示BRAS定时器队列数。  |
| TimerMaxTimeOut    | 该参数表示定时器最大超时次数。   |
| TimerMoudleID      | 该参数表示定时器模块号。      |
| TimerCurrQueue     | 该参数表示当前定时器队列。     |
| BrasTimerCurQueue  | 该参数表示当前BRAS定时器队列。 |
| TimerCnt           | 该参数表示定时器计数。       |
| TimerCreateErr     | 该参数表示定时器创建错误。     |
| LastTimeL          | 该参数表示最新时间的低位。     |
| LastTimeH          | 该参数表示最新时间的高位。     |
| SendGratArp        | 该参数表示发送免费ARP。     |
| IfLearnMaxNum      | 该参数表示接口学习最大数。     |
| DbgFlag            | 该参数表示调试标记。        |
| FlushProbeNum      | 该参数表示刷新探测数。       |
| DynArpEntryNum     | 该参数表示动态ARP表项数。    |
| StaArpEntryNum     | 该参数表示静态ARP表项数。    |
| DynArpNumMax       | 该参数表示最大动态ARP数。    |
| StaArpNumMax       | 该参数表示最大静态ARP数。    |
| UserTraceNum       | 该参数表示用户跟踪数。       |
| MissAmerNum        | 该参数表示抑制丢失数量。      |
| ArpNodesCnt        | 该参数表示ARP节点计数。     |
| UserTraceNodesCnt  | 该参数表示用户跟踪节点计数。    |
| ArpSockCount       | 该参数表示ARP套接字计数。    |
| Index              | 该参数表示索引。          |
| val                | 该参数表示索引对应的值。      |
| LLA SendPipeId     | 该参数表示LLA发送管道号。    |
| LLA SendServiceId  | 该参数表示LLA发送服务号。    |
| LLA SendPipeStatus | 该参数表示LLA发送管道状态。   |
| LLA RevPipeId      | 该参数表示LLA接收管道号。    |
| LLA RevServiceId   | 该参数表示LLA接收服务号。    |
| Pid                | 该参数表示进程号。         |
| RevPipeId          | 该参数表示接收管道号。       |
| RevServiceId       | 该参数表示接收服务号。       |
| SendPipeId         | 该参数表示发送管道号。       |
| SendServiceId      | 该参数表示发送服务号。       |
| SendPipeStatus     | 该参数表示发送管道状态。      |
| ComType            | 该参数表示组件状态。        |
| VrId               | 该参数表示虚拟路由号。       |
| CompStatus         | 该参数表示组件状态。        |
| ServiceState       | 该参数服务状态。          |
| PushState          | 该参数表示推送注册消息状态。    |
| SeqErrAckState     | 该参数等待序列号错误回应状态。   |
| BatchSeqNo         | 该参数表示批备序列号。       |
| ItemVer            | 该参数表示用户版本号。       |