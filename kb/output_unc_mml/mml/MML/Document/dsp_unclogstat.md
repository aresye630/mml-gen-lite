# 查询UNC日志状态（DSP UNCLOGSTAT）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：AMF、SMF、NRF、NSSF、SMSF、NCG、CBC、CBCF**

该命令用于查询UNCLOG的统计结果。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

| 参数标识         | 参数名称         | 参数说明                                                                                    |
|:-------------|:-------------|:----------------------------------------------------------------------------------------|
| LOGCTRLINDEX | UncLogCtrl索引 | 可选必选说明：可选参数  参数含义：UNCLOGCTRL的记录索引。  数据来源：本端规划  取值范围：整数类型，取值范围是1~255。  默认值：无  配置原则：无     |
| CSNAME       | CS名称         | 可选必选说明：可选参数  参数含义：创建logger时使用的CS名称。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是1~256。  默认值：无  配置原则：无 |
| FILE         | 文件或路径        | 可选必选说明：可选参数  参数含义：文件名或路径。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是0~1024。  默认值：无  配置原则：无          |
| LINE         | 行号           | 可选必选说明：可选参数  参数含义：代码行号。  数据来源：本端规划  取值范围：整数类型，取值范围是0~65535。  默认值：无  配置原则：无              |
| KEYWORD      | 关键字          | 可选必选说明：可选参数  参数含义：关键字，可输入多个，以空格分隔。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是1~256。  默认值：无  配置原则：无  |
| MAXNUM       | 最大返回记录数      | 可选必选说明：可选参数  参数含义：最多返回的记录数。  数据来源：本端规划  取值范围：整数类型，取值范围是1~255。  默认值：无  配置原则：无            |
| FUNC         | 函数           | 可选必选说明：可选参数  参数含义：函数名称。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是1~128。  默认值：无  配置原则：无             |

## 使用实例

如下实例用于查询一条日志

```
%%DSP UNCLOGSTAT:;%%
RETCODE = 0  操作成功

结果如下
--------
出现次数  日志级别  文件或路径                                                                  函数                                                 首次出现时间                

283       INFO      user/uem/exec/ds/msghandler/handle_ueam_msg.go:156                          msghandler.(*handlerImpl).handleUserConflict         2020-07-21 18:42:14.715991  18:52:04.704590   [AMF-UEM] [am/cellcore/cell-service-UemExecSvc/UemDomainSet583] 
849       INFO      user/uem/exec/ds/userrepo/repo_intra_impl.go:46                             userrepo.(*repoImpl).intraQuery                      2020-07-21 18:42:14.715928  18:52:07.143610   [AMF-UEM] [am/cellcore/cell-service-UemExecSvc/UemDomainSet583] 
283       INFO      user/uem/exec/ds/userrepo/repo_intra_impl.go:63                             userrepo.(*repoImpl).IntraUpdate                     2020-07-21 18:42:14.716106  18:52:04.704712   [AMF-UEM] [am/cellcore/cell-service-UemExecSvc/UemDomainSet583] 
286       INFO      user/secm/exec/do/action/ausfaction/authconfirm_req_ausf.go:45              ausfaction.(*authConfirmReq).Execute                 2020-07-21 18:42:14.631430  
286       INFO      user/secm/exec/do/action/ausfaction/authconfirm_req_ausf.go:71              ausfaction.(*authConfirmReq).HandleEvent             2020-07-21 18:42:14.650532  
286       INFO      user/secm/exec/do/action/ausfaction/authinfo_req_ausf.go:39                 ausfaction.(*authInfoReq).Execute                    2020-07-21 18:42:14.545203  
286       INFO      user/secm/exec/do/action/ausfaction/authinfo_req_ausf.go:64                 ausfaction.(*authInfoReq).HandleEvent                2020-07-21 18:42:14.564887  
286       INFO      user/secm/exec/do/action/ueamaction/auth_final.go:32                        ueamaction.(*authFinal).Execute                      2020-07-21 18:42:14.650812  
286       INFO      user/secm/exec/do/action/ueamaction/auth_init_ueam.go:33                    ueamaction.(*authInit).Execute                       2020-07-21 18:42:14.545147  
286       INFO      user/secm/exec/do/action/ueamaction/auth_init_ueam.go:44                    ueamaction.(*authInit).HandleEvent                   2020-07-21 18:42:14.545171  
286       INFO      user/secm/exec/do/action/ueamaction/auth_req_ueam.go:38                     ueamaction.(*authReq).Execute                        2020-07-21 18:42:14.564920  
286       INFO      user/secm/exec/do/action/ueamaction/auth_req_ueam.go:63                     ueamaction.(*authReq).HandleEvent                    2020-07-21 18:42:14.631374  
286       INFO      user/secm/exec/do/action/ueamaction/auth_rsp_timeout.go:31                  ueamaction.(*authRspTimeOut).Execute                 2020-07-21 18:42:14.631407  
286       INFO      user/secm/exec/do/action/ueamaction/authresult_rsp_ueam.go:31               ueamaction.(*authResultRsp).Execute                  2020-07-21 18:42:14.650585  
286       INFO      user/secm/exec/do/action/ueamaction/procedure_end.go:33                     ueamaction.(*procedureEnd).Execute                   2020-07-21 18:42:14.650669  
286       INFO      user/secm/exec/do/object/msgobj/auth_msg_object.go:31                       msgobj.(*AuthMsgObj).BuildAuthReqMsg                 2020-07-21 18:42:14.564942  
858       INFO      user/secm/exec/do/schedule/schedule.go:229                                  schedule.(*Scheduler).onProcessEvent                 2020-07-21 18:42:14.545371  18:52:06.619550   [AMF-SECM] [] Scheduler.onProcessEvent trans still working, transId:1, 
286       INFO      user/secm/exec/do/schedule/schedule.go:234                                  schedule.(*Scheduler).onProcessEvent                 2020-07-21 18:42:14.650843  
286       INFO      user/secm/exec/do/schedule/schedule.go:286                                  schedule.(*Scheduler).releaseDoActor                 2020-07-21 18:42:14.650884  
1430      INFO      user/secm/exec/ds/ds.go:44                                                  ds.(*SecmDomainSet).Receive                          2020-07-21 18:42:14.544995  18:52:06.639004   [AMF-SECM] [am/cellcore/cell-service-SecmExecSvc/SecmDomainSet77] 
1144      INFO      user/secm/exec/ds/ds_sdr.go:19                                              ds.(*SecmDomainSet).signalMsgProc                    2020-07-21 18:42:14.545023  18:52:06.638642   [AMF-SECM] [am/cellcore/cell-service-SecmExecSvc/SecmDomainSet77] 
307       INFO      user/secm/exec/do/action/ausfaction/authconfirm_req_ausf.go:45              ausfaction.(*authConfirmReq).Execute                 2020-07-21 18:42:15.618424  
307       INFO      user/secm/exec/do/action/ausfaction/authconfirm_req_ausf.go:71              ausfaction.(*authConfirmReq).HandleEvent             2020-07-21 18:42:15.638644  
307       INFO      user/secm/exec/do/action/ausfaction/authinfo_req_ausf.go:39                 ausfaction.(*authInfoReq).Execute                    2020-07-21 18:42:15.535989  
307       INFO      user/secm/exec/do/action/ausfaction/authinfo_req_ausf.go:64                 ausfaction.(*authInfoReq).HandleEvent                2020-07-21 18:42:15.556651  
(结果个数 = 25)

共有130个结果
共有6个报告
```

## 输出结果说明

| 输出项名称       | 输出项解释                                                                                                                                                                                                   |
|:------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 出现次数        | 计数。                                                                                                                                                                                                     |
| 日志级别        | 日志级别。 取值说明： “INVALID（INVALID）”：无效值“DEBUG（DEBUG）”：打开调试级别及以上的日志输出“INFO（INFO）”：打开提示级别及以上的日志输出“WARN（WARN）”：打开告警级别及以上的日志输出“ERROR（ERROR）”：打开错误级别及以上的日志输出“CRITICAL（CRITICAL）”：打开致命级别的日志输出“CLOSE（CLOSE）”：关闭日志输出 |
| 文件或路径       | 日志文件名及行号。                                                                                                                                                                                               |
| 函数          | 函数名称。                                                                                                                                                                                                   |
| 首次出现时间      | 日志首次出现时间。                                                                                                                                                                                               |
| 最后一次出现时间    | 日志最后一次出现时间。                                                                                                                                                                                             |
| 日志首次统计到时的内容 | 日志首次统计到时的内容。                                                                                                                                                                                            |