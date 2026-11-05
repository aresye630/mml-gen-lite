# 显示调试信息(DSP COMMONDBG)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用网元：SGSN、MME**

该命令用于查询系统内部运行信息，不涉及用户敏感数据，方便问题定位。

#### 注意事项

- 该命令只允许在华为工程师指导下执行。
- 该命令用于查询产品内部模块的运行状态是否正常。
- 该命令执行后立即生效。
- 使用方法：“DBGINDEX(调试索引)”输入“0”时可以输出帮助信息，根据输出的帮助信息，在“DBGINDEX（调试索引）”参数中输入序列号，即可查询到该序列号对应的字符串表示的统计信息。例如，"Query Rpu Error Stat"对应的序列号为4，在“DBGINDEX（调试索引）”参数中输入“4”即可查询Rpu模块的错误统计信息。
- 输出的内部运行信息随着系统运行的时间和流程会有所不同。
- 同时输入“DBGINDEX（调试索引）”和“DBGSTR（调试名称）”时，根据“DBGINDEX（调试索引）”查询，如果“DBGINDEX（调试索引）”未输入，则根据“DBGSTR（调试名称）”的输入查询。输入参数“调试名称”和“调试索引”不能同时为空。

#### 本地用户权限

manage-ug；system-ug；monitor-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识        | 参数名称   | 参数说明                                                                                                                                                                                           |
|:------------|:-------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RUNAME      | RU名称   | 可选必选说明：可选参数 参数含义：该参数用于指定SPU资源单元名。该参数可以通过DSP RU命令查询。 取值范围：1~63位字符串 默认值：无                                                                                                                        |
| MSTATE      | 主备状态   | 可选必选说明：可选参数 参数含义：该参数用于指示待查询进程所在板的主备状态。 取值范围：“MASTER(主用状态)”“SLAVE(备用状态)” 默认值：“MASTER(主用状态)”                                                                                                     |
| PROCTP      | 进程类型   | 可选必选说明：必选参数 参数含义：该参数用于指示进程类型。 取值范围：“SPP”“SGP”“GBP”“CDP”“UPP”“LCP”“OMP” 默认值：无                                                                                                                   |
| PROCNO      | 进程序号   | 可选必选说明：可选参数 参数含义：该参数用于指示待查询进程的内部序号。 取值范围：0~20 默认值：无                                                                                                                                            |
| DBGINDEX    | 调试索引   | 可选必选说明：可选参数 参数含义：该参数指定具体的调试类型。 取值范围：0~4294967295 默认值：无                                                                                                                                         |
| DBGSTR      | 调试名称   | 可选必选说明：可选参数 参数含义：该参数指定具体查询类型的字符串名称。 长度范围：0~255 默认值：无                                                                                                                                           |
| DBGPARA1    | 调试参数1  | 可选必选说明：可选参数 参数含义：该参数指定第1个数值型的调试变量。 取值范围：0~4294967295 默认值：无                                                                                                                                     |
| DBGPARA2    | 调试参数2  | 可选必选说明：可选参数 参数含义：该参数指定第2个数值型的调试变量。 取值范围：0~4294967295 默认值：无                                                                                                                                     |
| DBGPARA3    | 调试参数3  | 可选必选说明：可选参数 参数含义：该参数指定第3个数值型的调试变量。 取值范围：0~4294967295 默认值：无                                                                                                                                     |
| DBGPARA4    | 调试参数4  | 可选必选说明：可选参数 参数含义：该参数指定第4个数值型的调试变量。 取值范围：0~4294967295 默认值：无                                                                                                                                     |
| DBGPARA5    | 调试参数5  | 可选必选说明：可选参数 参数含义：该参数指定第5个数值型的调试变量。 取值范围：0~4294967295 默认值：无                                                                                                                                     |
| DBGPARA6    | 调试参数6  | 可选必选说明：可选参数 参数含义：该参数指定第6个数值型的调试变量。 取值范围：0~4294967295 默认值：无                                                                                                                                     |
| DBGPARA7    | 调试参数7  | 可选必选说明：可选参数 参数含义：该参数指定第7个数值型的调试变量。 取值范围：0~4294967295 默认值：无                                                                                                                                     |
| DBGPARA8    | 调试参数8  | 可选必选说明：可选参数 参数含义：该参数指定第8个数值型的调试变量。 取值范围：0~4294967295 默认值：无                                                                                                                                     |
| DBGPARA9    | 调试参数9  | 可选必选说明：可选参数 参数含义：该参数指定第9个数值型的调试变量。 取值范围：0~4294967295 默认值：无                                                                                                                                     |
| DBGPARA10   | 调试参数10 | 可选必选说明：可选参数 参数含义：该参数指定第10个数值型的调试变量。 取值范围：0~4294967295 默认值：无                                                                                                                                    |
| STRPARA1    | 字符串参数1 | 可选必选说明：可选参数 参数含义：该参数指定第1个字符型的调试变量。 长度范围：0~255 默认值：无                                                                                                                                            |
| STRPARA2    | 字符串参数2 | 可选必选说明：可选参数 参数含义：该参数指定第2个字符型的调试变量。 长度范围：0~255 默认值：无                                                                                                                                            |
| STRPARA3    | 字符串参数3 | 可选必选说明：可选参数 参数含义：该参数指定第3个字符型的调试变量。 长度范围：0~255 默认值：无                                                                                                                                            |
| STRPARA4    | 字符串参数4 | 可选必选说明：可选参数 参数含义：该参数指定第4个字符型的调试变量。 长度范围：0~255 默认值：无                                                                                                                                            |
| SERVICETYPE | 服务名称   | 可选必选说明：必选参数 参数含义：此参数用于指定待查询的服务名称，可以通过LST VNFC命令查询得到。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～31。数字“0~9”，大写字母“A~Z”，小写字母“a~z”，特殊字符“-”，“_”，其他均为非法字符，并且首字符必须为字母。 默认值：无 配置原则：服务名称的填写根据进程类型填写。进程和服务的对应关系如表1所示。 |

| 输出项名称   | 输出项解释                      |
|:--------|:---------------------------|
| SPP     | USN_VNFC                   |
| CDP     | USN_VNFC                   |
| SGP     | LINK_VNFC                  |
| GBP     | GB_VNFC                    |
| LCP     | USN_VNFC；LINK_VNFC；GB_VNFC |
| UPP     | USN_VNFC；LINK_VNFC；GB_VNFC |
| OMP     | USN_VNFC；LINK_VNFC；GB_VNFC |

#### 使用实例

查询调试命令使用帮助，DBGINDEX参数输入0：

DSP COMMONDBG: RUNAME="USN\_SP\_RU\_0065", PROCTP="upp", PROCNO=0, DBGINDEX=0, SERVICETYPE="USN\_VNFC";

```
%%DSP COMMONDBG: RUNAME="USN_SP_RU_0065", PROCTP="upp", PROCNO=0, DBGINDEX=0, SERVICETYPE="USN_VNFC";%%
RETCODE = 0  操作成功。

操作结果如下
------------
名字                                                       结果值

DbgHelp                                                    0     
Query Gtpc List Statistics                                 1     
query init time log                                        2     
Log Help                                                   3     
Show Log Switch                                            4     
Set Log Switch                                             5     
Query WhiteList Info                                       6     
Reset Trace Msg Counter                                    8     
Query Trace Task Error Code                                9     
Query Trace Task Status                                    10    
Query Trace Task Count                                     11    
Query Trace Report Count                                   12    
Query Trace APP Report Count                               13    
Query UserTrace TaskID Info                                14    
Query UserTrace Task Detail Info                           15    
Query RanUserTrace TaskID Info                             16    
Query RanUserTrace Task Detail Info                        17    
Query RanUserTrace Task Stat Info                          18    
Query TRC_SFTD switch Info                                 19    
Query Dye Trace Trans Rule Success Rate Info               20    
Query Ha ProcInfo                                          21    
SctpAgtSoftwareDebug                                       22    
S1AgtSoftwareDebug                                         23    
Query BRM Error Stat                                       25    
Query BRM Normal Stat                                      26    
Query Brm Buf Log By StartIndx Num                         28    
Clear Brm Buf Log                                          29    
Query Brm Res Key                                          30    
Query All Cluster                                          32    
Query Brm Res Occupy Key                                   33    
Query Rm Lock Cache Num                                    34    
Query All Cache Lock Flag                                  35    
Query Assign Cache Lock Flag                               36    
Qry CSDB Callback Total Count                              39    
Qry CSDB Callback Total Count By TblId                     40    
Qry CSDB Callback Total Count By Opt Type                  41    
Clear CSDB Callback Total Count                            42    
Qry CSDB Callback Period Count                             43    
Qry CSDB Callback Period Count By TblId                    44    
Qry CSDB Callback Period Count By Opt Type                 45    
Qry CSDB Local Act Num                                     49    
Qry CSDB Local Max And Act Num                             50    
Qry CSDB Bm Buff Info                                      51    
Query Res Srv Info[RmType/ResId]                           52    
Mod Res Srv Info[RmType/ResId/Data]                        53    
Res Scan Start Task[RmType/ResId/Para]                     54    
Res Scan Query Task[RmType/ResId/TaskType]                 55    
Res Scan Stop Task[RmType/ResId/TaskType]                  56    
Res Scan Qry Stat[RmType]                                  57    
Res Scan Clr Stat[RmType]                                  58    
Query Brm Ccdb Migrate Hdl By RmType                       59    
Query Private Spec                                         60    
Query Brm CSDB Qry Err Stat                                63    
Query All Crm Res State Perf                               64    
Query Crm LocProc DynRes ClusterId to TokenId by RmType    65    
Query Crm All Dyn Res TokenId Range                        66    
Query Res Crm shift Event Cnt Stat By RmType               67    
All Res Crm shift Event Cnt Stat Clean                     68    
Query Crm RmNum On Ru by RuID                              69    
Query Crm Res Trail Info                                   70    
Query Res Pool Info                                        71    
Query Process Pool Info                                    72    
Query Crmc Brm Chk Node                                    73    
S102agtSoftwareDebugProc                                   74    
S102agtSoftwareDebugProc                                   75    
Query Comm Dscp Pri                                        76    
Query Comm Dscp Stat                                       77    
Query GtpPath Comm Ex Head Statistics                      78    
Query Gtpc Path Error Statistics                           80    
Query Gtpc Parse Error Statistics                          82    
Query Gtpc Cycle Statistics                                84    
Query GtpPath Comm Statistics                              85    
PF Query Triple Key Info(Pro/Port/IP)                      86    
仍有后续报告输出
---    END

%%DSP COMMONDBG: RUNAME="USN_SP_RU_0065", PROCTP="upp", PROCNO=0, DBGINDEX=0, SERVICETYPE="USN_VNFC";%%
RETCODE = 0  操作成功。

操作结果如下
------------
名字                                                          结果值

PF Query Quintuple Key Info(Pro/Port/IP/Port/IP)              87    
PF Query Quintuple Key Miss Rec                               88    
PF Query Quintuple Key Miss Rec                               89    
PF Query Invalid Free Pbuf(Index)                             95    
PF Query Simple FlowCtrl Para(FlowType)                       97    
PF Stat IPINFO Stub                                           99    
Print CSDB Xml Def                                            100   
Query Gtpc devs adpt info                                     101   
Query g_ucSysProtocolVer                                      102   
Query g_asGtpcPathSigIp(Index)                                103   
Query Dscp License                                            104   
Query g_udwGtpcPathSigTos                                     105   
Query g_asGtpEchoN3                                           106   
Query g_asGtpEchoT3                                           107   
Query g_sGtpScanConf                                          108   
Query g_sGtpcPathGtpConf                                      109   
Query GtpcPath SoftPara                                       110   
Query g_asgtpcpathdp                                          111   
Query GtpcPathNodeFeatureSw                                   112   
Query Eipc VPN INFO                                           113   
Query Eipc Upp Proc Info                                      114   
Query Eipc PortRoute Info                                     115   
Query Policy Info(PolicyId/Begin Index/End Index)             116   
Query NextHop Info(Index)                                     117   
Query Eipc Register MPF Service Info                          118   
Query Eipc MPF Service Topo DDB Tbl Info                      120   
Query ResChk Object Info                                      121   
Query ResChk Event Info                                       122   
Query ResChk plug State                                       123   
Query Nls Fault Type Info(DDB)                                124   
Query Nls Fault Type Info(Local)                              125   
Query g_EipcResChkFuncIsSupport                               126   
Query Eipc Timer                                              128   
EIPC Trigger LB check by event ID (E_EIPC_RESCHK_EVENT_ID)    131   
EIPC LB Policy Distribute(para1-num)                          132   
Query Eipc Error Statistics                                   133   
Query g_ucGtpProcIndex                                        134   
Query M_PFP_GTPU_GTP_CFG_DDR_HOST_ADDR                        135   
Query M_PFP_GTPU_IP_MAPPED_CPUID_TBL_DDR_HOST_ADDR            136   
Query Process Info                                            137   
Query g_sGtpuCdbUsrCtrlTbl                                    138   
Query g_sGtpuCdbQchatService                                  139   
Query g_sGtpuCdbSoftPara                                      140   
Query g_sGtpuCdbResManageTbl                                  141   
Query g_sGtpuCdbSeqChkTbl                                     142   
Query g_sGtpuCdbQosToDscpTbl                                  143   
Query g_sGtpuCdbPdpCarTbl                                     144   
Query g_bRabReqFlowCtrl                                       145   
Query user plane Timer                                        147   
Query g_psGtpuIpTbl[i]                                        148   
Query g_psGtpuApnoiTbl[i]                                     149   
Query g_psGtpuApnNiTbl[i]                                     150   
Query g_sGtpuIpUsedNum                                        151   
Query g_udwGtpuApnoiUsedNum                                   152   
Query g_udwGtpuApnNiUsedNum                                   153   
Query g_udwApnniVolReportPerScan                              154   
Query g_udwApnniVolScanIndex                                  155   
Query GtpuBlock Alarm flag                                    156   
Query GtpuBlock flag                                          157   
Query g_GtpuPagingPkgCatchInfo                                158   
Query g_Gtp_ShMem_Chk_Tsk                                     159   
Query PfGib DataPos                                           169   
Query GTP PDP NUM                                             170   
Query M_PFP_GTP_PROCCESS_CHG_CONTAINER_DDR_HOST_ADDR          171   
Query g_asGtpuUeTypeVol[i]                                    173   
Query g_ucSupportRabUptType                                   174   
Query g_asGtpuPfDscpPriTbl                                    175   
Query Pf Dscp-Qos Map                                         176   
Query Extend_VFNC FlowCtrl Info                               177   
Query PF Share Mem Process State                              178   
Query PF GIB Segment Mapinfo                                  179   
Query PF DataInd FlowCtrl Node(Teid)                          181   
Query PF cared res info                                       182   
仍有后续报告输出
---    END

%%DSP COMMONDBG: RUNAME="USN_SP_RU_0065", PROCTP="upp", PROCNO=0, DBGINDEX=0, SERVICETYPE="USN_VNFC";%%
RETCODE = 0  操作成功。

操作结果如下
------------
名字                                                                结果值

Query PF WRED PARA Info                                             183   
Query PF QUELEN PARA Info                                           184   
Query PF SEQ KEEP PARA Info                                         185   
Query PF REMARK PARA Info                                           186   
Query PF QoS TO DSCP Info                                           187   
Query PF MSS CFG Info                                               188   
Query PF RAB PARA Info                                              189   
Query PF PFP CPIUD Info                                             190   
Query PF Pcp Index Info                                             191   
Query PF GtpuPara Info                                              192   
Query PF GtpuCtrl Info                                              193   
Query PF Pdp Car Info                                               194   
Query M_PFP_GTPU_IP_TABLE_DDR_HOST_ADDR                             195   
Query M_PFP_GTPU_IP_HASH_TABLE_DDR_HOST_ADDR                        196   
Query g_eGtpuTraitCaptureStatus                                     200   
Query Gtpu Trait Capture ShareMem                                   201   
Query Usr Stat Info                                                 202   
Query Usr Stat Hash Info                                            203   
Query g_audwMntGtpRcvMsgStat[i]                                     204   
Query GtpuMsgStat                                                   205   
Query GtpCylce_Mng task info by index(index)                        206   
Query GtpCylce_Mng task info by pid(pid)                            207   
Query GtpCylce_Mng error code                                       208   
Query g_PerfStatToPlmn by index                                     209   
Query g_PerfStatToPlmn by MCC&MNC(eg/460:03)                        210   
Query Plmn Hash List by index                                       211   
Query Plmn Hash List by MCC%MNC(eg/460:03)                          212   
Query SysSpec Error Stat                                            216   
Query GTP Spec                                                      217   
Query g_astSysSpecRegCallBackItem[]                                 218   
Query g_udwMultiTimes                                               219   
Query Gptu Perf Pf Spec                                             220   
Query Gtpu Perf Limit                                               221   
Query g_udwCurRptRncIdIdx                                           222   
Query g_udwPerfObjRncIdNum                                          223   
Query g_psPerfObjRncId[i]                                           224   
Query g_PerfStatToRnc[i]                                            225   
Query g_udwCurRptPeerIPIdx                                          226   
Query g_udwPerfObjPeerIpNum                                         227   
Query g_psPerfObjPeerIp[i]                                          228   
Query g_PerfStatToPeerIP[i]                                         229   
Query g_sPerfStatToGngpIP                                           230   
Query Gtpu Err Stat                                                 231   
Query Gtpu Stat                                                     232   
Query Gtpu Udp Check Stat                                           235   
Query g_SdbCycleTaskDesc[i]                                         236   
Query PDP Context By Teid                                           238   
Query PDP Context By Tid                                            239   
Query PDP Context By PeerIp Teid(Teid/PathIndex/udwPeerNodeType)    240   
DSP Sdb Backup State                                                248   
Gtpu Pf Trace stat                                                  266   
Gtpu Pf Dye Rdt Trace info                                          267   
Gtpu Pf Dye Trace FlowCtrl                                          268   
Gtpu g_udwGtpu_Idp_Count                                            270   
Packet forward PPS statictics                                       272   
Query Res Sync Proc Info(LogicCpuid)                                275   
Query Res Sync Proc Info(Index)                                     276   
Query Res Sync Msg Cnt Info                                         277   
Query Res Sync PDP Num Info                                         278   
Query Rpu Error Stat                                                279   
LST PFRESSTAT(MEM)                                                  281   
Query Process Resource Detail                                       284   
Query Rpup History Max Pdp Num                                      285   
Query Rpup Max Pdp Num                                              286   
Query Pdp Num Thresh(%)                                             287   
Query Pdp Num Thresh Value                                          288   
Query Rpup Static Bw Info                                           290   
Query Rpub Cpu Id                                                   291   
Query Rpup Process CPU Info                                         292   
Query Rpup Process Rpub Sync Msg Flg                                294   
Query S1 Interface brd chk info                                     297   
Query Rpub Res State                                                298   
仍有后续报告输出
---    END

%%DSP COMMONDBG: RUNAME="USN_SP_RU_0065", PROCTP="upp", PROCNO=0, DBGINDEX=0, SERVICETYPE="USN_VNFC";%%
RETCODE = 0  操作成功。

操作结果如下
------------
名字                                                结果值

Query Rpup Num                                      299   
Query Rpup Cpu Id                                   300   
Query Rpub Res Detail                               301   
Query Rpub History Max Gtpu Path Num                302   
Query Rpub Max Gtpu Path Num                        303   
Query Gtpu Path Thresh(%)                           304   
Query Gtpu Path Thresh Value                        305   
Query Rpub Bw Cfg                                   306   
Query Rpub Bw Info                                  307   
Query Rpus Cpu Id                                   308   
Query License Usr Bw                                309   
Query Rpub Pf Spec                                  310   
Query Rpub Bw Res Thresh                            311   
Query Static Res Thresh Value                       313   
Query Static Alm Thresh Value                       314   
Query Rpup Bw Sample                                315   
Query Dynamic Bw Res Thresh Value                   316   
Query Dynamic Bw Alm Thresh Value                   317   
Query Package Forward Speed Thresh Value            318   
Query Fabric BandWidth Thresh Value                 319   
Query Dynamic Bw By PFT                             321   
Query License CAR                                   324   
Query Board Res State Sync Info                     326   
Query g_udwUgfuResType                              327   
Query g_ucSelectMode                                328   
Query g_abSelectPdpBrd                              329   
Query g_udwLnkRncNum                                331   
Query Iu Ip Candi by index                          332   
Query Group Gn Ip Candi                             334   
Query g_asRpubInfo                                  336   
Query g_psBrdCfgGtpuIp                              337   
Query g_bUseOtherRackIpFlag                         338   
Query g_audwGtpuIPForDriver                         339   
Query driver configuration ip                       340   
Query g_aucRpubIuLinkType                           342   
Query Gtpu Path Error Stat                          343   
QueryGtpuPathFullProcLst(fulllisttype/pos)          345   
FindGtpuPath(LocIp/PeerIp/Type)                     347   
FindGtpuPath(PathIndex)                             348   
FindGtpuPath(IdlePointer)                           349   
FindGtpuPath(BusyPoniter)                           350   
Query g_sGtpuPathHdl                                362   
Query Detect flag                                   364   
Query Gtpu Share Path By Index                      365   
Query g_udwGtpuPathIdleThres                        367   
Query fault dtc path idle thresh                    370   
Query g_udwGtpuPathIntfIndexCheckTask               372   
Query g_sGtpuPathMsgInCfg                           373   
Query g_sGtpuPathMsgOutCfg                          375   
Query g_udwSigTos                                   376   
Query Dscp License(GTPU)                            377   
Query MsgMerge RegInfo(By RegIdx)                   379   
Query MsgMerge MsgDataBufInfo(By RegIdx)            380   
Query g_asGtpuBrdPathModuleState                    381   
Query gtpu path UPPs info                           382   
Query g_udwGtpuBrdPathChkMsgMergeRegIndx            383   
Query g_udwGtpuBrdPathChkTask                       384   
Query g_udwGtpuBrdPathSyncChkMsgMergeRegIndx        385   
Query g_udwGtpuBrdPathSyn2IntfTask                  386   
Query g_udwGtpuBrdPathSync2VMCChkMsgMergeRegIndx    387   
Query g_udwGtpuBrdPathSyn2VMCTask                   388   
Query Sync task info                                389   
Query gtpu path ip info(path index)                 390   
Query VMC info                                      391   
Query UPP info                                      392   
Query g_sGtpuPathDetNodeMng                         393   
Query g_sGtpuPathDetNode(index)                     394   
Query g_sGtpuPathSnCtrl                             395   
Query Sn Node                                       396   
Query Gtpu Brd Path Resource Used Info              397   
Query g_sGtpuPathDetSwitch                          399   
Query g_udwSwCloseGtpuPathAlmScan                   400   
Query gtpupathdp                                    401   
Query g_stGtpuPathConf                              402   
仍有后续报告输出
---    END

%%DSP COMMONDBG: RUNAME="USN_SP_RU_0065", PROCTP="upp", PROCNO=0, DBGINDEX=0, SERVICETYPE="USN_VNFC";%%
RETCODE = 0  操作成功。

操作结果如下
------------
名字                                                             结果值

Query g_stGtpuPathT3Hdl                                          403   
Query g_udwGtpuPathNormalDetectTask                              404   
Query g_udwGtpuPathErrorDetectTask                               405   
Query Gtpu Path Common Task                                      406   
Query GtpuPath Intf Switch                                       407   
Query GtpuPath Intf Info [i]                                     408   
Query g_asGtpuPathObsvrCpuid                                     410   
Query g_psGtpuPathObsvrIndex by path index                       411   
Query g_udwGtpuPathObsvrFreshTaskIndex                           412   
Query g_udwGtpuPathStateSyncMsgMergeRegIndx                      413   
Query g_udwGtpuProPathChkAckMsgMergeRegIndx                      414   
Query g_audwGtpuSigMsgDirectionStat                              415   
Query g_udwGtpcAgentInitFinishFlag                               416   
Query M_PFP_GTPC_IP_TSN_TABLE_DDR_HOST_ADDR(Index)               417   
Query M_PFP_GTPC_SPP_AVAIL_CPUID_TBL_DDR_HOST_ADDR               418   
Query M_PFP_GTPC_SPP_CPUID_TBL_DDR_HOST_ADDR                     419   
Query M_PFP_GTPC_IP_HASH_TABLE_DDR_HOST_ADDR(Index)              420   
Query M_PFP_GTPC_IP_TABLE_DDR_HOST_ADDR(Index)                   421   
Query M_PFP_GTPC_SN_TABLE_DDR_HOST_ADDR(Index)                   422   
Query g_udwMaxT3N3                                               423   
Query g_eGtpcAgentTimerStartFlag                                 424   
Query M_PFP_GTPC_IP_MAPPED_CPUID_TBL_DDR_HOST_ADDR               425   
Query g_sGtpcPathHdl                                             426   
Query Gtpc Path Hash List Length By IP(LocIp/PeerIp)             427   
Query Gtpc Path Hash List Length By Index(Index)                 430   
Query Gtpc Path Hash List Statistics                             431   
Query g_audwAttrIdleThres                                        432   
Query g_udwIdleDetectPathIdx                                     433   
Query gtpcpath check task index                                  435   
Query Echo Rsp FlowCtrl Info                                     438   
Query GtpcPathSgwCharactInfo                                     440   
Query Gtpc Detect Ctrl Info                                      441   
Query g_stGtpcPathDetectT3Hdl                                    442   
Query Max and Min Sn by path index(pathindex)                    444   
Query Gtpc Path Detect Cycle Task Index                          445   
Query Virtual Detect Min Sig path mng info                       446   
Query Virtual Detect task index                                  447   
Query g_pucGtpcPathSyncFlg(GtpcPathIndex)                        451   
Query sync_used_info module global variable                      453   
Query pathnum sync timeout Cnt                                   454   
Query g_asGtpcPerfByIp(Index)                                    455   
Query g_asGtpcPathNumReferPerf(Index)                            456   
Query GtpcCommon PathNumAlm Global Info                          457   
Query GtpcCommon Error Stat                                      458   
Query GtpcCommon Error Stat print sw                             459   
Query g_udwPreAntiAttackDropNum                                  462   
Query g_ucAlmOrRstCount                                          463   
Query g_ucAntiAttackAlm                                          464   
Query g_udwGtpcPathAlmMskIPNum                                   465   
Query g_asGtpcPathAlmMskIP(Index)                                466   
Query g_udwEchoSwGtpcPathAlmScan                                 467   
Query g_udwGtpcPathAlmMskNum                                     468   
Query g_asGtpcPathStatusAlmMask(Index)                           469   
Query g_ucGtpcLocIpAlmFlag                                       470   
Query g_ucGtpcPathConstAlmFlag                                   471   
Query Gtpc Path White List Info                                  476   
Query Gtpc Path White List Hash Index By CbIndex                 477   
Query Gtpc Path White List Hash Info By Hash Index               478   
Get g_eGtpcTrcType(0:normal/1:abnormal)                          479   
Query g_bIsRmvBindGtpcIpFlag                                     482   
Query Protocol Message Statistics                                483   
Query Discard Receive Message Statistics                         484   
Query Discard Send Message Statistics                            485   
Query Received Packets UDP Check Result Statistics               486   
Query Local Gtpc Path By IP(LocIp/PeerIp/IntfType)               488   
Query Local Gtpc Path By Index(Path Index)                       489   
Query Local Gtpc Path By Idle List Pointer(Idle List Pointer)    490   
Query Local Gtpc Path By Busy List Pointer(Busy List Pointer)    491   
(结果个数 = 360)
共有5个报告
---    END
```

查询Rpu模块的统计信息，“DBGINDEX”参数输入“4”：

DSP COMMONDBG: RUNAME="USN\_SP\_RU\_0064", PROCTP="UPP", PROCNO=0, DBGINDEX=4, SERVICETYPE="USN\_VNFC";

```
%%DSP COMMONDBG: RUNAME="USN_SP_RU_0064", PROCTP="UPP", PROCNO=0, DBGINDEX=4, SERVICETYPE="USN_VNFC";%%
RETCODE = 0  操作成功。

操作结果如下
------------
  名字  =  Switch
结果值  =  0
(结果个数 = 1)
---    END
```

#### 输出结果说明

| 输出项名称   | 输出项解释     |
|:--------|:----------|
| 名字      | 查询结果名称。   |
| 结果值     | 查询第1列结果值。 |