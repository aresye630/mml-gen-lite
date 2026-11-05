# 显示调试信息(DSP COMMONDBG)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用网元：SGSN、MME、AMF**

该命令用于查询系统内部运行信息，方便问题定位。

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
| RUNAME      | RU名称   | 可选必选说明：可选参数 参数含义：该参数用于指定SPU资源单元名。 取值范围：1~63位字符串 默认值：无                                                                                                                                          |
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

DSP COMMONDBG: MSTATE=MASTER, PROCTP="SGP", DBGINDEX=0, SERVICETYPE="LINK\_VNFC";

```
%%DSP COMMONDBG: MSTATE=MASTER, PROCTP="SGP", DBGINDEX=0, SERVICETYPE="LINK_VNFC";%%
RETCODE = 0  操作成功

操作结果如下
------------
名字                                                     结果值  服务名称   

DbgHelp                                                  0       LINK_VNFC  
query init time log                                      1       LINK_VNFC  
Query WhiteList Info                                     3       LINK_VNFC  
TrcRdtQueryExistTaskNum                                  5       LINK_VNFC  
TrcRdtQueryExistTask                                     6       LINK_VNFC  
TrcRdtQueryMsgSendStatics                                7       LINK_VNFC  
TrcRdtClearMsgSendStatics                                8       LINK_VNFC  
Reset Trace Msg Counter                                  9       LINK_VNFC  
Query Trace Task Error Code                              10      LINK_VNFC  
Query Trace Task Status                                  11      LINK_VNFC  
Query Trace Task Count                                   12      LINK_VNFC  
Query Trace Report Count                                 13      LINK_VNFC  
Query Trace APP Report Count                             14      LINK_VNFC  
Query UserTrace TaskID Info                              15      LINK_VNFC  
Query UserTrace Task Detail Info                         16      LINK_VNFC  
Query E2ETrace Task Detail Info                          17      LINK_VNFC  
Query RanUserTrace TaskID Info                           18      LINK_VNFC  
Query RanUserTrace Task Detail Info                      19      LINK_VNFC  
Query RanUserTrace Task Stat Info                        20      LINK_VNFC  
Query TRC_SFTD switch Info                               21      LINK_VNFC  
Query Dye Trace Trans Rule Success Rate Info             22      LINK_VNFC  
Query Trc Fc Stat                                        23      LINK_VNFC  
Query E2E Trace Error Stat                               24      LINK_VNFC  
Set TrcParaChkDebugPrint                                 25      LINK_VNFC  
Query Delta Tick                                         26      LINK_VNFC  
Query Tick Startup Phase                                 27      LINK_VNFC  
Query Ha ProcInfo                                        28      LINK_VNFC  
Set MsgPidStatOutputPara                                 29      LINK_VNFC  
Print DepMng Node                                        30      LINK_VNFC  
Show Alarm Buff                                          31      LINK_VNFC  
Query BRM Error Stat                                     33      LINK_VNFC  
Query BRM Normal Stat                                    34      LINK_VNFC  
Query Brm Buf Log By StartIndx Num                       36      LINK_VNFC  
Clear Brm Buf Log                                        37      LINK_VNFC  
Brm Set Log Switch                                       38      LINK_VNFC  
IF BRM                                                   39      LINK_VNFC  
Query Brm Res Key                                        40      LINK_VNFC  
Query All Cluster                                        42      LINK_VNFC  
Query Brm Res Occupy Key                                 43      LINK_VNFC  
Query Rm Lock Cache Num                                  44      LINK_VNFC  
Query All Cache Lock Flag                                45      LINK_VNFC  
Query Assign Cache Lock Flag                             46      LINK_VNFC  
Qry CSDB Callback Total Count                            49      LINK_VNFC  
Qry CSDB Callback Total Count By TblId                   50      LINK_VNFC  
Qry CSDB Callback Total Count By Opt Type                51      LINK_VNFC  
Clear CSDB Callback Total Count                          52      LINK_VNFC  
Qry CSDB Callback Period Count                           53      LINK_VNFC  
Qry CSDB Callback Period Count By TblId                  54      LINK_VNFC  
Qry CSDB Callback Period Count By Opt Type               55      LINK_VNFC  
Query Proc Total User Num                                59      LINK_VNFC  
Query User Num Per Token                                 60      LINK_VNFC  
Query Private Spec                                       61      LINK_VNFC  
Priv Spec Update Thrd                                    64      LINK_VNFC  
Res Scan Qry Stat[RmType]                                68      LINK_VNFC  
Res Scan Clr Stat[RmType]                                69      LINK_VNFC  
Query Brm Ccdb Migrate Hdl By RmType                     70      LINK_VNFC  
Query Brm Csdb Qry Err Stat                              71      LINK_VNFC  
Query All Crm Res State Perf                             72      LINK_VNFC  
Query Crm LocProc DynRes ClusterId to TokenId by RmType  73      LINK_VNFC  
Query Crm All Dyn Res TokenId Range                      74      LINK_VNFC  
Query Res Crm shift Event Cnt Stat By RmType             75      LINK_VNFC  
All Res Crm shift Event Cnt Stat Clean                   76      LINK_VNFC  
Query Crm RmNum On Ru by RuID                            77      LINK_VNFC  
Query Crm Res Trail Info                                 78      LINK_VNFC  
Query Res Pool Info                                      79      LINK_VNFC  
Query Process Pool Info                                  80      LINK_VNFC  
Brm Query NlsId Err                                      81      LINK_VNFC  
BrmDbgGetAllRmId                                         82      LINK_VNFC  
BrmDbgGetDialTestRmId                                    83      LINK_VNFC  
BrmDbgLocalRmId                                          84      LINK_VNFC  
BrmDbgGetNlsId                                           85      LINK_VNFC  
BrmDbgGetLocalNlsId                                      86      LINK_VNFC  
BrmDbgGetRmAndCpuid                                      87      LINK_VNFC  
BrmDbgGetProcNoInNls                                     88      LINK_VNFC  
BishengCollectFgoDataFrameSo                             89      LINK_VNFC  
Query Crmc Brm Chk Node                                  90      LINK_VNFC  
Brm Query Token State                                    91      LINK_VNFC  
Query Grace Scale Info                                   92      LINK_VNFC  
AdtQueryInnerCount                                       93      LINK_VNFC  
AdtClearInnerCount                                       94      LINK_VNFC  
Query Sdr Context Info                                   96      LINK_VNFC  
Query Sdr Error Stat                                     97      LINK_VNFC  
Query Comm Dscp Pri                                      98      LINK_VNFC  
Query Comm Dscp Stat                                     99      LINK_VNFC  
Comm Query Apptp Err Stat                                100     LINK_VNFC  
Comm Clear Apptp Err Stat                                101     LINK_VNFC  
Comm Send Inter-Nls Pkt                                  102     LINK_VNFC  
Comm Get Pid2Msgtp Mapping                               104     LINK_VNFC  
Comm Get Process Info                                    105     LINK_VNFC  
Comm Query Reliable Enhance Info                         107     LINK_VNFC  
GrayUpg MsgStat Query                                    108     LINK_VNFC  
Query Metrics                                            109     LINK_VNFC  
set grey msg version                                     110     LINK_VNFC  
clear grey msg version                                   111     LINK_VNFC  
query version                                            112     LINK_VNFC  
primary key debug                                        113     LINK_VNFC  
Qry CSDB HostID                                          114     LINK_VNFC  
Qry Pool Cache                                           116     LINK_VNFC  
Qry CSDB Local Act Num                                   117     LINK_VNFC  
Qry CSDB Local Max And Act Num                           118     LINK_VNFC  
UdrAdaptShowMsgSendStatics                               122     LINK_VNFC  
UdrAdaptClearMsgSendStatics                              123     LINK_VNFC  
Query Mti Error Stat                                     124     LINK_VNFC  
Query Mti SmsfOpc Stat                                   125     LINK_VNFC  
Query Mti SmsfSsn                                        126     LINK_VNFC  
Query Mti VlrOpc                                         127     LINK_VNFC  
Query Mti MscOpc                                         128     LINK_VNFC  
Clr Mti Error Stat                                       129     LINK_VNFC  
Query Mti FC Info                                        130     LINK_VNFC  
Query Mti FC Info By GtIdx                               131     LINK_VNFC  
Read SctpInitMsg FlowCtrl Info                           132     LINK_VNFC  
Query Select Spp Times(Iu)                               135     LINK_VNFC  
Query RANAP Info                                         136     LINK_VNFC  
3G Interface Stat                                        137     LINK_VNFC  
Get Ranap Fast Res Chk Status                            140     LINK_VNFC  
Qry Csdb Bm Buff Info                                    143     LINK_VNFC  
Get S1ap Fast Res Chk Status                             145     LINK_VNFC  
Query NgapLm Flowctrl Info                               148     LINK_VNFC  
Query NgapLm Fixed Flowctrl Info                         150     LINK_VNFC  
Query NgapLm Conn Info                                   152     LINK_VNFC  
Query NgapLm Inner Count                                 153     LINK_VNFC  
Query NgapLm Decode InitUe NasPdu Flag                   155     LINK_VNFC  
Query NgapLm LOGIFDSCP                                   157     LINK_VNFC  
Query NgapLm Dtls Para                                   158     LINK_VNFC  
Query NgapLm Dtls Link CB                                159     LINK_VNFC  
Query NgapLm Dtls Cert                                   160     LINK_VNFC  
Query NgapLm Ngsctppara                                  161     LINK_VNFC  
Query NgapLnk CheckTask Info                             162     LINK_VNFC  
Ngap Get Tx Buff All Assoc Detail                        163     LINK_VNFC  
Query N2 ServTbl Occupy Rate                             164     LINK_VNFC  
Query Ngap Conn Tbl Record                               165     LINK_VNFC  
Query Vlr info                                           166     LINK_VNFC  
Query sgsap check info                                   167     LINK_VNFC  
SgsapQueryDdbInfoByIdx                                   168     LINK_VNFC  
SgsapQuerySgslnkMigrateInfo                              169     LINK_VNFC  
SgsapQueryClrSgslnkMigrateInfo                           170     LINK_VNFC  
sgsap query vlr state msg count                          171     LINK_VNFC  
Sgsap debug alarm check                                  172     LINK_VNFC  
query sgsap msg                                          173     LINK_VNFC  
query vlr state                                          174     LINK_VNFC  
Query Vlr Sctp Info                                      175     LINK_VNFC  
Query M3ap Context Info                                  177     LINK_VNFC  
LST M3APPARA                                             179     LINK_VNFC  
LST M3CMPT                                               181     LINK_VNFC  
Query DDB lcsap link info                                182     LINK_VNFC  
Query Lcsap Err Stat                                     183     LINK_VNFC  
query rcap sdb ctx and conn para                         186     LINK_VNFC  
query rcap ddb info                                      187     LINK_VNFC  
query rcap link migrate info                             188     LINK_VNFC  
rcap ctrl link migrate info                              189     LINK_VNFC  
query rcap sctp info                                     190     LINK_VNFC  
query rcap udb info                                      191     LINK_VNFC  
query rcap err statistic                                 192     LINK_VNFC  
clr rcap err statistic                                   193     LINK_VNFC  
rcap log print                                           194     LINK_VNFC  
query sgssrap listen                                     195     LINK_VNFC  
query sgssrap err statistic                              196     LINK_VNFC  
clr sgssrap err statistic                                197     LINK_VNFC  
query sgssrap link migrate info                          198     LINK_VNFC  
sgssrap ctrl link migrate info                           199     LINK_VNFC  
query sgssrap cdb info                                   200     LINK_VNFC  
query sgssrap sdb ctx                                    201     LINK_VNFC  
query sgssrap ddb ctx                                    202     LINK_VNFC  
sgssrap log print                                        203     LINK_VNFC  
sgssrap message report                                   204     LINK_VNFC  
query sgssr mme valid info                               205     LINK_VNFC  
query sgssr fc Info                                      206     LINK_VNFC  
query sgssr fc Info by mme idx                           207     LINK_VNFC  
syslog                                                   208     LINK_VNFC  
Query Use Cname TTL Switch or Not                        209     LINK_VNFC  
Query All Server Fault or Not                            210     LINK_VNFC  
Sbcap Software Debug Proc Extend                         211     LINK_VNFC  
Query Sbcap Info                                         212     LINK_VNFC  
Query Select Spp Times(S1)                               213     LINK_VNFC  
Query Spp Index Protect Times                            214     LINK_VNFC  
Query Decor Buffed Msg Num                               215     LINK_VNFC  
4G Interface Stat                                        216     LINK_VNFC  
4G Interface Debug                                       217     LINK_VNFC  
S1apemSoftwareDebugProc                                  218     LINK_VNFC  
Query S1ap LNK Flash Cycle                               219     LINK_VNFC  
Query S1apemPagingMirrorData                             221     LINK_VNFC  
Query S1apemPackedPagingInfo                             222     LINK_VNFC  
Set Grey 4G S1Paging Log Level                           223     LINK_VNFC  
Set Grey 4G S1Paging Info Cri Log Level                  224     LINK_VNFC  
Query S1 ServTbl Occupy Rate                             225     LINK_VNFC  
QueryS1apemPagingErrTaiHistory                           227     LINK_VNFC  
S1ap Get Tx Buff All Assoc Detail                        228     LINK_VNFC  
Query S1aple Listen Assoc Info                           229     LINK_VNFC  
S1apE2eTrcEcmStat                                        230     LINK_VNFC  
S1AP_QUERY_ENB_SYNC_STATUS                               231     LINK_VNFC  
S1AP_QUERY_ENB_SYNC_QUE_INFO                             232     LINK_VNFC  
Query M3UA Comp                                          234     LINK_VNFC  
Query M3UA Cfg Trail Info                                235     LINK_VNFC  
Query M3UA Migrate Trail Info                            236     LINK_VNFC  
Alm M3UA Link Congestion Test                            237     LINK_VNFC  
SctpAdaptQuintupleDbgQuery                               238     LINK_VNFC  
Loop Query DMPE Idx in Busy State                        239     LINK_VNFC  
(结果个数 = 197)

仍有后续报告输出
---    END

+++    UEG/*MEID:5 MENAME:ueg*/        2024-06-13 11:17:01
O&M    #9378
%%DSP COMMONDBG: MSTATE=MASTER, PROCTP="SGP", DBGINDEX=0, SERVICETYPE="LINK_VNFC";%%
RETCODE = 0  操作成功

操作结果如下
------------
名字                                       结果值  服务名称   

Query Recover BusyState DMPE Times         240     LINK_VNFC  
Query Diam Rm Stat Info                    241     LINK_VNFC  
DmDbgGetConnParm                           242     LINK_VNFC  
DiamStatusDebug                            243     LINK_VNFC  
Query Diam Trc Switch Info                 244     LINK_VNFC  
Query Diam App Param                       245     LINK_VNFC  
QueryDiamLinkAssocIdByLinkId               246     LINK_VNFC  
Query Dm Brm Cbk Count                     247     LINK_VNFC  
UdmCmSoftwareDebug                         249     LINK_VNFC  
SctpCCtrlQueryInnerCount                   250     LINK_VNFC  
SctpCCtrlClearInnerCount                   251     LINK_VNFC  
SctpCCtrlQueryCongestCtrlInfo              252     LINK_VNFC  
SctpCCtrlPrintVppLog                       253     LINK_VNFC  
SctpCCtrlQueryCfg                          254     LINK_VNFC  
[SCCP]Query g_astSccpAllUicpLoadStatus     255     LINK_VNFC  
[SCCP]Clear Choose Number Stat             256     LINK_VNFC  
Query Sccp Comp                            257     LINK_VNFC  
Sigtp Query Mid Info                       258     LINK_VNFC  
Query Sccp Msg Stat                        259     LINK_VNFC  
Query SGSSDB TBL NUMS                      260     LINK_VNFC  
Query Dscp License                         261     LINK_VNFC  
Query re-route switch                      262     LINK_VNFC  
Query Dns Enum QoS to Desp Info            263     LINK_VNFC  
Query Dns Error Stat                       264     LINK_VNFC  
Query Use Weight Stat                      266     LINK_VNFC  
Query DnsErrDn UsedContainer Stat          267     LINK_VNFC  
Query Dns Adapt Moudle Info                268     LINK_VNFC  
Query Dns ENUM Socket Info                 269     LINK_VNFC  
Query Dns Enum Log Level                   270     LINK_VNFC  
Query Enum CM Dtc Timer Info               272     LINK_VNFC  
Query Enum CM Dtc Index                    273     LINK_VNFC  
Query Enum CM Link Info                    274     LINK_VNFC  
Query Enum CM Init Flag                    275     LINK_VNFC  
Query FlowctrlLogLevel                     276     LINK_VNFC  
Set FlowctrlLogLevel                       277     LINK_VNFC  
BishengCollectFgoDataProcSo                278     LINK_VNFC  
Query Cpu CooperationFc Para               280     LINK_VNFC  
Query MsgRate CooperationFc Para           282     LINK_VNFC  
Query Statistics Info for Flowctrl         283     LINK_VNFC  
Query Weight Info for Flowctrl             284     LINK_VNFC  
Query WAL Info for Flowctrl                285     LINK_VNFC  
Query FlowctrlSyncCpuInfo                  286     LINK_VNFC  
Dsp Msg stat for Flowctrl                  287     LINK_VNFC  
Query inter mme fc init cfg                288     LINK_VNFC  
Query inter mme fc alarm info              289     LINK_VNFC  
Query inter mme fc discard num in cur 15s  290     LINK_VNFC  
Query inter mme fc ctrl info               291     LINK_VNFC  
Query inter mme fc sample data in cur 5s   292     LINK_VNFC  
Print inter mme fc detail info             293     LINK_VNFC  
Query inter mme fc stat by softpara        296     LINK_VNFC  
Query inter mme fc cfg                     298     LINK_VNFC  
ExcessSctpCommDbgHash                      301     LINK_VNFC  
ExcessSctpCommDbgStat                      302     LINK_VNFC  
Query S1apemQueryPackedState               303     LINK_VNFC  
Query S1AP PACKED MM PAGING STAT           304     LINK_VNFC  
S1apSoftwareQueryDebug                     306     LINK_VNFC  
S1apE2eTrcUcmStat                          307     LINK_VNFC  
S1ap Dial Test Stat                        308     LINK_VNFC  
Tcap msg stat by length                    310     LINK_VNFC  
Tcap Print Smsf Mode                       311     LINK_VNFC  
Query M3UA Info                            313     LINK_VNFC  
Query M3UA CallInTimes                     314     LINK_VNFC  
Query M3ua Link Proc                       315     LINK_VNFC  
Sctp Software Debug Extend                 317     LINK_VNFC  
Sctp adapt query assoc info                318     LINK_VNFC  
SctpAdaptQueryAssocInfoRandom              319     LINK_VNFC  
Sctp Adapt Msg Stat                        320     LINK_VNFC  
Sctp Adapt Mem Pool                        321     LINK_VNFC  
Sctp Get SPM INFO                          322     LINK_VNFC  
Sctp Get Tx Buff Pool Param                323     LINK_VNFC  
Sctp Get App Tx Buff Free Count            324     LINK_VNFC  
Sctp Get Tx Buff One Assoc Detail          325     LINK_VNFC  
Sctp Get csp sdk value                     326     LINK_VNFC  
Sctp Print Tx Buff Used Assoc              327     LINK_VNFC  
Sctp Get Gloabl Value                      328     LINK_VNFC  
SctpDbgGetAllAppId                         329     LINK_VNFC  
SctpDbgGetTxBuffUsed                       330     LINK_VNFC  
DiamSoftwareQueryDebug                     331     LINK_VNFC  
VcomSoftwareQueryDebug                     333     LINK_VNFC  
SipStartDbgTrcMsg                          335     LINK_VNFC  
SipStopDbgTrcMsg                           336     LINK_VNFC  
SipShowDbgTrcMsg                           337     LINK_VNFC  
SipPrintDbgCounter                         338     LINK_VNFC  
SipClearDbgCounter                         339     LINK_VNFC  
Log Help                                   340     LINK_VNFC  
Show Log Switch                            341     LINK_VNFC  
Set Log Switch                             342     LINK_VNFC  
(结果个数 = 87)

共有284个结果
共有2个报告
---    END
```

开启用户SIP消息跟踪，“DBGSTR”参数输入“SipStartDbgTrcMsg”,“STRPARA1”参数输入用户的IMSI“46000000000000”：

DSP COMMONDBG: MSTATE=MASTER, PROCTP="SGP", DBGSTR="SipStartDbgTrcMsg", STRPARA1="46000000000000", SERVICETYPE="LINK\_VNFC";

```
%%DSP COMMONDBG: MSTATE=MASTER, PROCTP="SGP", DBGSTR="SipStartDbgTrcMsg", STRPARA1="46000000000000", SERVICETYPE="LINK_VNFC";%%
RETCODE = 0  操作成功

操作结果如下
------------
    名字  =  Process Result: success!
  结果值  =  NULL
服务名称  =  LINK_VNFC
(结果个数 = 1)

---    END
```

显示用户SIP消息跟踪数据，“DBGSTR”参数输入“SipShowDbgTrcMsg”：

DSP COMMONDBG: MSTATE=MASTER, PROCTP="SGP", DBGSTR="SipShowDbgTrcMsg", SERVICETYPE="LINK\_VNFC";

```
%%DSP COMMONDBG: MSTATE=MASTER, PROCTP="SGP", DBGSTR="SipShowDbgTrcMsg", SERVICETYPE="LINK_VNFC";%%
RETCODE = 0  操作成功

操作结果如下
------------
    名字  =  Process Result: success!
  结果值  =  NULL
服务名称  =  LINK_VNFC
(结果个数 = 1)

---    END
```

关闭用户SIP消息跟踪，“DBGSTR”参数输入“SipStopDbgTrcMsg”：

DSP COMMONDBG: MSTATE=MASTER, PROCTP="SGP", DBGSTR="SipStopDbgTrcMsg", SERVICETYPE="LINK\_VNFC";

```
%%DSP COMMONDBG: MSTATE=MASTER, PROCTP="SGP", DBGSTR="SipStopDbgTrcMsg", SERVICETYPE="LINK_VNFC";%%
RETCODE = 0  操作成功

操作结果如下
------------
    名字  =  Process Result: success!
  结果值  =  NULL
服务名称  =  LINK_VNFC
(结果个数 = 1)

---    END
```

显示SIP消息计数，“DBGSTR”参数输入“SipPrintDbgCounter”：

DSP COMMONDBG: MSTATE=MASTER, PROCTP="SGP", DBGSTR="SipPrintDbgCounter", SERVICETYPE="LINK\_VNFC";

```
%%DSP COMMONDBG: MSTATE=MASTER, PROCTP="SGP", DBGSTR="SipPrintDbgCounter", SERVICETYPE="LINK_VNFC";%%
RETCODE = 0  操作成功

操作结果如下
------------
名字                                结果值  服务名称   

SIP_CNT_VCFUNCIP_RESUME_ENTER       2       LINK_VNFC  
SIP_CNT_VCFUNCIP_RESUME_QUERY_FAIL  2       LINK_VNFC  
SIP_CNT_VCFUNCPARA_RESUME_ENTER     2       LINK_VNFC  
SIP_CNT_VCFUNCPARA_RESUME_SUCCESS   2       LINK_VNFC  
SIP_CNT_VCFUNCSW_RESUME_ENTER       2       LINK_VNFC  
SIP_CNT_VCFUNCSW_RESUME_SUCCESS     2       LINK_VNFC  
SIP_CNT_LISTEN_LINK                 0       LINK_VNFC  
SIP_CNT_PHYSICAL_LINK               0       LINK_VNFC  
(结果个数 = 8)

---    END
```

清除SIP消息计数，“DBGSTR”参数输入“SipClearDbgCounter”：

DSP COMMONDBG: MSTATE=MASTER, PROCTP="SGP", DBGSTR="SipClearDbgCounter", SERVICETYPE="LINK\_VNFC";

```
%%DSP COMMONDBG: MSTATE=MASTER, PROCTP="SGP", DBGSTR="SipClearDbgCounter", SERVICETYPE="LINK_VNFC";%%
RETCODE = 0  操作成功

操作结果如下
------------
    名字  =  Process Result: success!
  结果值  =  NULL
服务名称  =  LINK_VNFC
(结果个数 = 1)

---    END
```

查看容灾漫游探测路径信息，“DBGSTR”参数输入“QueryMmePgwEchoPath”：

DSP COMMONDBG: MSTATE=MASTER, PROCTP="upp", DBGSTR="QueryMmePgwEchoPath", SERVICETYPE="LINK\_VNFC";

```
%%DSP COMMONDBG: MSTATE=MASTER, PROCTP="upp", DBGSTR="QueryMmePgwEchoPath", SERVICETYPE="LINK_VNFC";%%
RETCODE = 0  操作成功

操作结果如下
------------
名字                                                     结果值  服务名称 
Path(1): TimeStamp=1732299550, mmeIp=192.168.0.1         NULL    LINK_VNFC
--pgwIPv4=192.168.1.1, pgwIpv6=fc00::1
Path(1): TimeStamp=1732299660, mmeIp=192.168.0.2         NULL    LINK_VNFC
--pgwIPv4=192.168.1.2, pgwIpv6=fc00::2
(结果个数 = 2)

---    END
```

查看通过MML配置触发的GTPC路径信息，“DBGSTR”参数输入“QueryMmePgwGtpcPath”：

DSP COMMONDBG: MSTATE=MASTER, PROCTP="upp", DBGSTR="QueryMmePgwGtpcPath", SERVICETYPE="LINK\_VNFC";

```
%%DSP COMMONDBG: MSTATE=MASTER, PROCTP="upp", DBGSTR="QueryMmePgwGtpcPath", SERVICETYPE="LINK_VNFC";%%
RETCODE = 0  操作成功

操作结果如下
------------
名字                                        结果值  服务名称 
Path(1): LocalIP=192.168.0.3                NULL    LINK_VNFC
--PeerIP=192.168.1.3, Status=1, Ver=2
Path(1): LocalIP=192.168.0.4                NULL    LINK_VNFC
--PeerIP=192.168.1.4, Status=1, Ver=2
(结果个数 = 2)

---    END
```

#### 输出结果说明

| 输出项名称   | 输出项解释        |
|:--------|:-------------|
| 名字      | 查询结果名称。      |
| 结果值     | 查询结果值。       |
| 服务名称    | 查询结果所在服务的名称。 |