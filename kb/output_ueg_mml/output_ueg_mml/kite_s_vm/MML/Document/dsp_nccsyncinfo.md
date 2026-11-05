# 查询NETCONFC的配置同步信息（DSP NCCSYNCINFO）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

该命令用于查询NETCONFC的配置同步信息。

#### 注意事项

无。

#### 操作用户权限

G\_1，管理员级别命令组

#### 参数说明

| 参数标识            | 参数名称   | 参数说明                                                                                                         |
|:----------------|:-------|:-------------------------------------------------------------------------------------------------------------|
| PEERID          | 远端ID   | 可选必选说明：必选参数 参数含义：该参数用于表示远端设备ID。 数据来源：本端规划 取值范围：整数类型，取值范围为0～4294967295。 默认值：无                                 |
| DATATYPE        | 数据类型   | 可选必选说明：可选参数 参数含义：该参数用于表示配置对账信息的数据类型。 数据来源：本端规划 取值范围：枚举类型。 SYNCCONFIG：对账信息。 默认值：SYNCCONFIG                    |
| SERVICEINSTANCE | 服务实例   | 可选必选说明：必选参数 参数含义：该参数表示大颗粒服务实例名称。 数据来源：本端规划 取值范围：字符串类型，通过LST VNFC命令获取。 默认值：无 配置原则：只能填写通过LST VNFC命令查询到的管理代理标识。 |

#### 使用实例

- 查询VNF内NETCONFC的配置同步信息：

  ```
  DSP NCCSYNCINFO:PEERID=1025,SERVICEINSTANCE="vnfc";
  ```

  ```
  RETCODE = 0  操作成功

  结果如下:
  ------------------------
  配置同步的信息 =
  -----------------------------------------------------------
  Data sync base info:
     MaxRetryCount:    3          RetryCount:           0       
     MaxBackoffCount:  3          BackoffCount:         1       
     IsForbid:         FALSE      FsmState:             INIT
     Sync Reason:      PERIODICAL    
     PeriodSyncTime(rand in one hour):  03:00:00
     GetLocalAppDataTime(us):           8586484         
     GetPeerAppDataTime(us):            9997749         
     SyncingAppDataTime(us):            16431366        
  -----------------------------------------------------------
  ###########################################################
  Data sync process info:
     SyncRate:         100     
     SyncResult:       OK      
     SyncType:         PERIOD 
     SyncingApp:               
     BeginTime:        2018-06-13, 03:32:08:550
     EndTime:          2018-06-13, 03:32:28:188
  -----------------------------------------------------------
  APP: sampleAM_DEP
     ReadAppDBCount:    1           GetConfigCount:       2       
     LocalDataReady:    TRUE        PeerDataReady:        TRUE    
     SyncSucceed:       TRUE        GetPeerRetCode:       0x0       
     DiffRetCode:       0x0         SyncRetCode:          0x0       
     AppendXssCount:    310         MergeRpcCount:        0       
     DeleteRpcCount:    0       
     GetLocalAppDataTime(us):   90697           
     GetPeerAppDataTime(us):    133761          
     SyncingAppDataTime(us):    0               
  -----------------------------------------------------------
  APP: sampleAM_INDEP
     ReadAppDBCount:    1           GetConfigCount:       2       
     LocalDataReady:    TRUE        PeerDataReady:        TRUE    
     SyncSucceed:       TRUE        GetPeerRetCode:       0x0       
     DiffRetCode:       0x0         SyncRetCode:          0x0       
     AppendXssCount:    220         MergeRpcCount:        0       
     DeleteRpcCount:    0       
     GetLocalAppDataTime(us):   89419           
     GetPeerAppDataTime(us):    135418          
     SyncingAppDataTime(us):    0               
  -----------------------------------------------------------

  (结果个数 = 2)
  ---    END
  ```
- 查询VNF间NETCONFC的配置同步信息：

  ```
  DSP NCCSYNCINFO:PEERID=3,SERVICEINSTANCE="vnfc";
  ```

  ```
  RETCODE = 0  操作成功

  结果如下:
  ------------------------
  配置同步的信息 =
  -------------------------------------------
  PeriodSyncTime(rand in one hour): 03:00:00
  IsForbid:         FALSE   
  Sync Time:        2018-06-13, 03:27:52:547 - 2018-06-13, 03:28:09:541
  Get Local:        2018-06-13, 03:27:53:367 - 2018-06-13, 03:27:57:710
  File Trans:       2018-06-13, 03:27:57:710 - 2018-06-13, 03:27:59:510
  Sync-cfg-id:      4               
  Num of APP:       14              
  Progress:         100%
  SyncResult:       Sync-cfg success
  SyncType:         PERIOD   
  Sync Reason:      PERIODICAL    
  -------------------------------------------
  Feature-Name:        sampleSYS_INDEP    
  SyncConfig-Status:   Success         
  OperationState:      --              
  ErrorAppTag:         0               
  ErrClassName:        --              
  ErrorMessage:        --              
  Feature-Name:        samplePF_INDEP     
  SyncConfig-Status:   Success         
  OperationState:      --              
  ErrorAppTag:         0               
  ErrClassName:        --              
  ErrorMessage:        --              
  Feature-Name:        sampleCM_INDEP     
  SyncConfig-Status:   Success         
  OperationState:      --              
  ErrorAppTag:         0               
  ErrClassName:        --              
  ErrorMessage:        --              
  Feature-Name:        sampleAM_INDEP     
  SyncConfig-Status:   Success         
  OperationState:      --              
  ErrorAppTag:         0               
  ErrClassName:        --              
  ErrorMessage:        --              
  Feature-Name:        sampleSM_INDEP     
  SyncConfig-Status:   Success         
  OperationState:      --              
  ErrorAppTag:         0               
  ErrClassName:        --              
  ErrorMessage:        --              
  Feature-Name:        sampleDIAM_INDEP   
  SyncConfig-Status:   Success         
  OperationState:      --              
  ErrorAppTag:         0               
  ErrClassName:        --              
  ErrorMessage:        --              
  Feature-Name:        samplePCC_INDEP    
  SyncConfig-Status:   Success         
  OperationState:      --              
  ErrorAppTag:         0               
  ErrClassName:        --              
  ErrorMessage:        --              
  Feature-Name:        samplePF_DEP       
  SyncConfig-Status:   Success         
  OperationState:      --              
  ErrorAppTag:         0               
  ErrClassName:        --              
  ErrorMessage:        --              
  Feature-Name:        sampleDIAM_DEP     
  SyncConfig-Status:   Success         
  OperationState:      --              
  ErrorAppTag:         0               
  ErrClassName:        --              
  ErrorMessage:        --              
  Feature-Name:        sampleCM_DEP       
  SyncConfig-Status:   Success         
  OperationState:      --              
  ErrorAppTag:         0               
  ErrClassName:        --              
  ErrorMessage:        --              
  Feature-Name:        sampleAM_DEP       
  SyncConfig-Status:   Success         
  OperationState:      --              
  ErrorAppTag:         0               
  ErrClassName:        --              
  ErrorMessage:        --              
  Feature-Name:        samplePCC_DEP      
  SyncConfig-Status:   Success         
  OperationState:      --              
  ErrorAppTag:         0               
  ErrClassName:        --              
  ErrorMessage:        --              
  Feature-Name:        sampleSM_DEP       
  SyncConfig-Status:   Success         
  OperationState:      --              
  ErrorAppTag:         0               
  ErrClassName:        --              
  ErrorMessage:        --              
  Feature-Name:        sampleCOMM         
  SyncConfig-Status:   Success         
  OperationState:      --              
  ErrorAppTag:         0               
  ErrClassName:        --              
  ErrorMessage:        --              

  (结果个数 = 1)
  ---    END
  ```

#### 输出结果说明

| 输出项名称   | 输出项解释                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|:--------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 配置同步的信息 | 该参数用于显示VNF内配置同步的信息。 Data sync base info：对账基本信息。MaxRetryCount：对账失败后，重试对账的最大次数。RetryCount：已经重试对账的次数。MaxBackoffCount：最大退避次数。BackoffCount：已经退避次数。IsForbid：对账功能是否被禁用。FsmState：对账状态机状态。取值范围：枚举类型。INIT：初始状态。GETTING_LOCAL：获取本地数据。GETTING_PEER：获取远端数据。SYNCING：正在同步数据。PeriodSyncTime(rand in one hour)：周期对账时间，NETCONFC会周期性的自动触发对账，该字段用于显示周期对账的时间点。GetLocalAppDataTime(us)：获取本地数据的时间，单位为微秒。GetPeerAppDataTime(us)：获取远端数据的时间，单位为微秒。SyncingAppDataTime(us)：同步数据差异至远端设备的时间，单位为微秒。Data sync process info：对账处理信息。SyncRate：对账操作的进度。SyncResult：同步的结果。取值范围：枚举类型。INIT：Session尚未建好。OK：成功。ERR_COLLECT：获取本地、远端配置时失败。ERR_DIFF：比较配置时失败。ERR_SYNC：下发配置差异时失败。MANUAL_STOP：手工停止。LOCAL_ERR：本地处理失败。FORCE_STOP：强制停止。SyncingApp：正在同步的APP。BeginTime：对账开始的时间。EndTime：对账结束的时间。APP：配置对账的业务名称。ReadAppDBCount：获取本地数据的次数。GetConfigCount：获取远端数据的次数。LocalDataReady：本地数据是否已获取完毕。PeerDataReady：远端数据是否已获取完毕。SyncSucceed：是否对账成功。GetPeerRetCode：获取远端的错误码。DiffRetCode：差异比对返回码。SyncRetCode：同步数据返回码。AppendXssCount：加载xss lib的次数。MergeRpcCount：需要下发的Merge报文个数。DeleteRpcCount：需要下发的Delete报文个数。APP GetConfigErr info：同步数据至远端的错误信息。Sync Reason：对账原因。取值范围：枚举类型。NEVER_DS：未对账。MANUAL：手工对账。PERIODICAL：定时对账。SYSBUSY：对账系统忙。INCOMPLETE：对账上报失败。TMOUT：超过校验次数。FIRST_DS：首次对账。NON_INC_SYNC：不具备增量对账能力。QUE_OVERFLOW：增量对账队列满。TRANSNOTMATCH：无RPC缓存，事务号不一致。ALARM：告警对账。IMNO_NOTMATCH：远端与实际下发事务号不一致。CACHE_NOTMATCH：有RPC缓存，远端事务号不在缓存RPC内。FTP_TRANS_FAIL：对账ftp传输失败，重新对账。DIS_CFG_SN：收到action消息，断开cfg session，重新建联之后，对账。CONFIG_NEED_SYNC：对账过程中，收到配置下发请求，触发再次对账。PATCH_NEED_SYNC：对账或者配置下发过程中，加载南向资源补丁，触发对账。SyncType：对账类型。取值范围：枚举类型。NA：未对账。AUTO：自动对账。MANUAL：手动对账。PERIOD：周期对账。 该参数用于显示VNF间的配置同步信息。 Sync Time: 对账时间。Get Local: 获取本地数据的时间。File Trans: 文件传输时间。Sync-cfg-id: 对账配置标识。Num of APP: 配置对账的业务的数量。Progress: 对账进度。SyncResult: 对账结果。Feature-Name: 特性名称。SyncConfig-Status: 配置对账状态。取值范围：枚举类型。In-progress：正处于配置对账中。success：配置对账成功。fail：配置对账失败。此字段表示的是某个对账的APP在对账操作结束（或异常终止）前的最后状态而不是当前状态。此字段不保证和SyncResult字段保持一致。OperationState: 对账操作状态。--:此APP未开始对账。QUERY：查询本端配置。COMPARE：将本端的配置和远端进行比较。EDIT：编辑配置。ErrorAppTag: 配置对账失败的业务标签。ErrClassName: 配置对账失败的类名称。ErrorMessage: 配置对账失败的信息。 |