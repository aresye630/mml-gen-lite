# 显示调试信息(DSP COMMONDBGMCR)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用网元：MME**

该命令用于查询系统内部运行信息，不涉及用户敏感数据，方便问题定位。

#### 注意事项

- 该命令只允许在华为工程师指导下执行。
- 该命令执行后立即生效。
- 使用方法：“DBGINDEX(调试索引)”输入“0”时可以输出帮助信息，根据输出的帮助信息，在“DBGINDEX（调试索引）”参数中输入序列号，即可查询到该序列号对应的字符串表示的统计信息。例如，"Query Rpu Error Stat"对应的序列号为4，在“DBGINDEX（调试索引）”参数中输入“4”即可查询Rpu模块的错误统计信息。
- 输出的内部运行信息随着系统运行的时间和流程会有所不同。
- 同时输入“DBGINDEX（调试索引）”和“DBGSTR（调试名称）”时，根据“DBGINDEX（调试索引）”查询，如果“DBGINDEX（调试索引）”未输入，则根据“DBGSTR（调试名称）”的输入查询。

#### 本地用户权限

manage-ug；system-ug；monitor-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识      | 参数名称   | 参数说明                                                                           |
|:----------|:-------|:-------------------------------------------------------------------------------|
| RUNAME    | RU名称   | 可选必选说明：必选参数 参数含义：该参数用于指定SPU资源单元名。该参数可以通过DSP RU命令查询。 取值范围：1~31位字符串 默认值：无        |
| MSTATE    | 主备状态   | 参数含义：该参数用于指示待查询进程所在板的主备状态。 取值范围：“MASTER(主用状态)”“SLAVE(备用状态)” 默认值：“MASTER(主用状态)” |
| PROCTP    | 进程类型   | 可选必选说明：必选参数 参数含义：该参数用于指示进程类型。 取值范围：“SAP”“SRP”“OMP” 默认值：无                       |
| PROCNO    | 进程序号   | 可选必选说明：必选参数 参数含义：该参数用于指示待查询进程的内部序号。 取值范围：0~20 默认值：无                            |
| DBGINDEX  | 调试索引   | 参数含义：该参数指定具体的调试类型。 取值范围：0~4294967295 默认值：无                                     |
| DBGSTR    | 调试名称   | 参数含义：该参数指定具体查询类型的字符串名称。 长度范围：0~255 默认值：无                                       |
| DBGPARA1  | 调试参数1  | 参数含义：该参数指定第1个数值型的调试变量。 取值范围：0~4294967295 默认值：无                                 |
| DBGPARA2  | 调试参数2  | 参数含义：该参数指定第2个数值型的调试变量。 取值范围：0~4294967295 默认值：无                                 |
| DBGPARA3  | 调试参数3  | 参数含义：该参数指定第3个数值型的调试变量。 取值范围：0~4294967295 默认值：无                                 |
| DBGPARA4  | 调试参数4  | 参数含义：该参数指定第4个数值型的调试变量。 取值范围：0~4294967295 默认值：无                                 |
| DBGPARA5  | 调试参数5  | 参数含义：该参数指定第5个数值型的调试变量。 取值范围：0~4294967295 默认值：无                                 |
| DBGPARA6  | 调试参数6  | 参数含义：该参数指定第6个数值型的调试变量。 取值范围：0~4294967295 默认值：无                                 |
| DBGPARA7  | 调试参数7  | 参数含义：该参数指定第7个数值型的调试变量。 取值范围：0~4294967295 默认值：无                                 |
| DBGPARA8  | 调试参数8  | 参数含义：该参数指定第8个数值型的调试变量。 取值范围：0~4294967295 默认值：无                                 |
| DBGPARA9  | 调试参数9  | 参数含义：该参数指定第9个数值型的调试变量。 取值范围：0~4294967295 默认值：无                                 |
| DBGPARA10 | 调试参数10 | 参数含义：该参数指定第10个数值型的调试变量。 取值范围：0~4294967295 默认值：无                                |
| STRPARA1  | 字符串参数1 | 参数含义：该参数指定第1个字符型的调试变量。 长度范围：0~255 默认值：无                                        |
| STRPARA2  | 字符串参数2 | 参数含义：该参数指定第2个字符型的调试变量。 长度范围：0~255 默认值：无                                        |
| STRPARA3  | 字符串参数3 | 参数含义：该参数指定第3个字符型的调试变量。 长度范围：0~255 默认值：无                                        |
| STRPARA4  | 字符串参数4 | 参数含义：该参数指定第4个字符型的调试变量。 长度范围：0~255 默认值：无                                        |

#### 使用实例

查询调试命令使用帮助，DBGINDEX参数输入0：

DSP COMMONDBGMCR: RUNAME="MCR\_SP\_RU\_0064", PROCTP="SRP", PROCNO=0, DBGINDEX=0;

```
%%DSP COMMONDBGMCR: RUNAME="MCR_SP_RU_0064", PROCTP="SRP", PROCNO=0, DBGINDEX=0;%%
RETCODE = 0  操作成功

操作结果如下
-------------------------
 名字                                                                 结果值1

DbgHelp                                                       0           
query init time log                                           1           
Query WhiteList Info                                          2           
Reset Trace Msg Counter                                       4           
Query Trace Task Error Code                                   5           
Query Trace Task Status                                       6           
Query Trace Task Count                                        7           
Query Trace Report Count                                      8           
Query Trace APP Report Count                                  9           
Query UserTrace TaskID Info                                   10          
Query UserTrace Task Detail Info                              11          
Query TRC_SFTD switch Info                                    12          
Query Dye Trace Trans Rule Success Rate Info                  13          
Query Ha ProcInfo                                             14          
Query Comm Dscp Pri                                           15          
Query Comm Dscp Stat                                          16          
PF Query Triple Key Info(Pro/Port/IP)                         17          
PF Query Quintuple Key Info(Pro/Port/IP/Port/IP)              18          
PF Query Quintuple Key Miss Rec                               19          
PF Query Quintuple Key Miss Rec                               20          
PF Query Invalid Free Pbuf(Index)                             26          
PF Query Simple FlowCtrl Para(FlowType)                       28          
Query Eipc VPN INFO                                           30          
Query Eipc Upp Proc Info                                      31          
Query Eipc PortRoute Info                                     32          
Query Policy Info(PolicyId/Begin Index/End Index)             33          
Query NextHop Info(Index)                                     34          
Query Eipc Register MPF Service Info                          35          
Query Eipc MPF Service Topo DDB Tbl Info                      37          
Query ResChk Object Info                                      38          
Query ResChk Event Info                                       39          
Query ResChk plug State                                       40          
Query Nls Fault Type Info(DDB)                                41          
Query Nls Fault Type Info(Local)                              42          
Query g_EipcResChkFuncIsSupport                               43          
Query Eipc Timer                                              45          
EIPC Trigger LB check by event ID (E_EIPC_RESCHK_EVENT_ID)    48          
EIPC LB Policy Distribute(para1-num)                          49          
Query Eipc Error Statistics                                   50          
Query Sdup Error Stat                                         51          
Query Sdup Normal Stat                                        52          
Query Primary Process Info                                    54          
Query Ctx Ref Tbl Info                                        55          
Query Ctx Ref Hash Info                                       56          
Query Ctx Ref By IMSI                                         57          
Query Ctx Ref By STMSI                                        58          
Query Ctx Ref By Index                                        59          
Query user plane Timer                                        60          
Query MsgMerge RegInfo(By RegIdx)                             61          
Query MsgMerge MsgDataBufInfo(By RegIdx)                      62          
Query GtpCylce_Mng task info by index(index)                  63          
Query GtpCylce_Mng task info by pid(pid)                      64          
Query GtpCylce_Mng error code                                 65          
Query SDSRM Ctx Res Detail                                    67          
Query SDSRM Ctx Res Samples(SerialNo)                         68          
Query SDSRM Ctx Res State                                     69          
Query Private Spec                                            71          
Query SdupAgent Err Stat                                      74          
Query g_pstSdupAgentSapChooseInfo                             75          
Query g_stSdupAgentSapInfo                                    76          
Query MCR Plugin Server Ctrl Adapt Info                       77          
Query MCR Plugin Server Ctrl Info                             78            
(结果个数 = 62)

---    END
```

查询SDIM模块的主控信息，“DBGINDEX”参数输入“18”：

DSP COMMONDBGMCR: RUNAME="MCR\_SP\_RU\_0064", PROCTP="SAP", PROCNO=0, DBGINDEX=18;

```
%%DSP COMMONDBGMCR: RUNAME="MCR_SP_RU_0064", PROCTP="SAP", PROCNO=0, DBGINDEX=18;%%
RETCODE = 0  操作成功

操作结果如下
-------------------------
 名字                                结果值1

control sdim cpuid                   570426363 0 0 0                        
control sdim module No.              1019 0 0 0                             
sdim module mast control changed:    824483968 824261824 824275648 824468544          
(结果个数 = 3)

---    END
```

#### 输出结果说明

| 输出项名称   | 输出项解释     |
|:--------|:----------|
| 名字      | 查询结果名称。   |
| 结果值     | 查询第1列结果值。 |