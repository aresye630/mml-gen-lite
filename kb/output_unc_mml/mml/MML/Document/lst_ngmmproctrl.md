# 查询5G移动性管理流程控制参数（LST NGMMPROCTRL）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：AMF**

此命令用于查询5G移动性管理流程控制参数。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|:-------|:-------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PROT   | 流程类型   | 可选必选说明：可选参数  参数含义：该参数用于指定流程类型，根据场景来确认是否需要配置相应的流程。  数据来源：全网规划 取值范围： “AUSF_DISCOVERY（AUSF发现流程）”：AUSF发现流程“AIR（获取鉴权集流程）”：获取鉴权集流程“AUTHENTICATION（鉴权流程）”：鉴权流程“SMC（安全算法协商流程）”：UE和NAS安全算法协商流程“CHECK_IMEI（检查IMEI流程）”：检查IMEI流程“UDM_DISCOVERY（UDM发现流程）”：UDM发现流程“UDM_REGISTRATION（UDM注册流程）”：到UDM注册流程“UDM_GET_SUBSCRIBER_DATA（UDM获取签约数据流程）”：从UDM获取签约数据流程“UDM_SUBSCIBE（UDM订阅流程）”：向UDM订阅流程“PCF_DISCOVERY（PCF发现流程）”：PCF发现流程“PCF_POLICY（PCF策略交互流程）”：向PCF创建/更新策略流程“OTHER_PROC（其它流程）”：其它流程“CAG（CAG限制）”：CAG限制  默认值：无  配置原则：无 |

## 使用实例

- 查询“流程类型”为“AUTHENTICATION（鉴权流程）”的5G移动性管理流程控制参数，执行如下命令：

  ```
  %%LST NGMMPROCTRL: PROT=AUTHENTICATION;%%
  RETCODE = 0  操作成功

  结果如下
  --------
          Authentication拒绝原因值(RES检查失败)  =  0
    Authentication拒绝原因值(UE返回MAC Failure)  =  0
  Authentication拒绝原因值(UE返回Synch failure)  =  0
                        AUTH HTTP过载拒绝原因值  =  0
                         AUTH HTR流控拒绝原因值  =  0
  (结果个数 = 1)

  ---    END
  ```
- 查询全量5G移动性管理流程控制参数，执行如下命令：

  ```
  %%LST NGMMPROCTRL:;%%
  RETCODE = 0  操作成功

  操作结果如下
  ------------
                Authentication拒绝原因值(RES检查失败)  =  0
          Authentication拒绝原因值(UE返回MAC Failure)  =  0
        Authentication拒绝原因值(UE返回Synch failure)  =  0
                   Check IMEI拒绝原因值(IMEI检查失败)  =  0
                                   漫游受限拒绝原因值  =  0
                        AIR拒绝原因值(USER_NOT_FOUND)  =  0
        AIR拒绝原因值(SERVING_NETWORK_NOT_AUTHORIZED)  =  0
               AIR拒绝原因值(AUTHENTICATION_REJECTED)  =  0
      AIR拒绝原因值(INVALID_HN_PUBLIC_KEY_IDENTIFIER)  =  0
                     AIR拒绝原因值(CONTEXT_NOT_FOUND)  =  0
                 AIR拒绝原因值(INVALID_SCHEME_OUTPUT)  =  0
         AIR拒绝原因值(UNSUPPORTED_PROTECTION_SCHEME)  =  0
                    UDM注册拒绝原因值(USER_NOT_FOUND)  =  0
                 UDM注册拒绝原因值(CONTEXT_NOT_FOUND)  =  0
          UDM注册拒绝原因值(UNKNOWN_5GS_SUBSCRIPTION)  =  0
                UDM注册拒绝原因值(NO_PS_SUBSCRIPTION)  =  0
               UDM注册拒绝原因值(ROAMING_NOT_ALLOWED)  =  0
                UDM注册拒绝原因值(ACCESS_NOT_ALLOWED)  =  0
                   UDM注册拒绝原因值(RAT_NOT_ALLOWED)  =  0
         UDM注册拒绝原因值(REAUTHENTICATION_REQUIRED)  =  0
                                        强制向UDM注册  =  否
            UDM获取签约数据拒绝原因值(USER_NOT_FOUND)  =  0
            UDM获取签约数据拒绝原因值(DATA_NOT_FOUND)  =  0
                    UDM订阅拒绝原因值(USER_NOT_FOUND)  =  0
          UDM订阅拒绝原因值(UNSUPPORTED_RESOURCE_URI)  =  0
                AIR拒绝原因值(SUBSCRIPTION_NOT_FOUND)  =  0
                                   区域限制拒绝原因值  =  0
                                   接入限制拒绝原因值  =  0
                     AIR拒绝原因值(Too Many Requests)  =  0
                   AIR拒绝原因值(Service Unavailable)  =  0
                                  AIR拒绝原因值(超时)  =  0
    UDM获取签约数据拒绝原因值(SUBSCRIPTION_NOT_FOUND)  =  0
         UDM获取签约数据拒绝原因值(Too Many Requests)  =  0
       UDM获取签约数据拒绝原因值(Service Unavailable)  =  0
                      UDM获取签约数据拒绝原因值(超时)  =  0
                 UDM注册拒绝原因值(Too Many Requests)  =  0
               UDM注册拒绝原因值(Service Unavailable)  =  0
                              UDM注册拒绝原因值(超时)  =  0
                 UDM订阅拒绝原因值(Too Many Requests)  =  0
               UDM订阅拒绝原因值(Service Unavailable)  =  0
                              UDM订阅拒绝原因值(超时)  =  0
               AUSF发现失败拒绝原因值(USER_NOT_FOUND)  =  0
                         AUSF发现拒绝原因值(其他原因)  =  0
                             AUSF发现拒绝原因值(流控)  =  0
                         UDM发现拒绝原因值(Not Found)  =  0
                          UDM发现拒绝原因值(其他原因)  =  0
                        	     服务区域限制拒绝原因值  =  0
                             无可用网络切片拒绝原因值  =  0
                             TA级网络切片不可用原因值  =  0
                                          强制发现UDM  =  是
                         PCF发现拒绝原因值(Not Found)  =  0
                          PCF发现拒绝原因值(其他原因)  =  0
  PCF策略拒绝原因值(RESOURCE_URI_STRUCTURE_NOT_FOUND)  =  0
                          PCF策略拒绝原因值(其他原因)  =  0
                                        ODB拒绝原因值  =  0
                               终端消息非法拒绝原因值  =  0
                                        SMC拒绝原因值  =  2
                                        SMC超时原因值  =  3		      
                                        CAG拒绝原因值  =  0	  
                              AUTH HTTP过载拒绝原因值  =  0
                    获取UDM签约数据HTTP过载拒绝原因值  =  0
                       Serving Plmn变更注册拒绝原因值  =  0
                               AUTH HTR流控拒绝原因值  =  0
                     获取UDM签约数据HTR流控拒绝原因值  =  0
                          AIR拒绝原因值(SCP/SEPP故障)  =  0
                      UDM注册拒绝原因值(SCP/SEPP故障)  =  0
              UDM获取签约数据拒绝原因值(SCP/SEPP故障)  =  0
                      UDM订阅拒绝原因值(SCP/SEPP故障)  =  0
                      PCF策略拒绝原因值(SCP/SEPP故障)  =  0
                                         SCP/SEPP故障  =  0
              AIR SCP拒绝原因值(NF_DISCOVERY_FAILURE)  =  0
                 AIRSCP拒绝原因值(NF_DISCOVERY_ERROR)  =  0
               AIR SCP拒绝原因值(NF_SERVICE_FAILOVER)  =  0
           UDM注册SCP拒绝原因值(NF_DISCOVERY_FAILURE)  =  0
             UDM注册SCP拒绝原因值(NF_DISCOVERY_ERROR)  =  0
            UDM注册SCP拒绝原因值(NF_SERVICE_FAILOVER)  =  0
   UDM获取签约数据SCP拒绝原因值(NF_DISCOVERY_FAILURE)  =  0
     UDM获取签约数据SCP拒绝原因值(NF_DISCOVERY_ERROR)  =  0
    UDM获取签约数据SCP拒绝原因值(NF_SERVICE_FAILOVER)  =  0
  (结果个数 = 1)

  ---    END
  ```

## 输出结果说明

| 输出项名称                                        | 输出项解释                                                                                                                                                                                              |
|:---------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| UDM发现拒绝原因值(Not Found)                        | 该参数用于设置UDM发现流程TOPO返回404 Not Found时，下发给UE的原因值。                                                                                                                                                      |
| UDM发现拒绝原因值(其他原因)                             | 该参数用于设置UDM发现流程TOPO返回404 Not Found以外的失败时，下发给UE的原因值。                                                                                                                                                 |
| 强制发现UDM                                      | 该参数用于控制在用户重新接入网络时，不直接使用静态上下文中存储的UDM信息，而是根据UDM的高低优先级和权重，重选UDM，确保选择优先级和权重高的UDM。 例如当UDM主备部署，在主用UDM故障后，用户注册到备用UDM，并且AMF的用户上下文中记录备用UDM地址信息，存在主用UDM恢复后，用户继续存在于备用UDM中的问题，此时打开本参数开关，可以强制用户重新选择优先级和权重高的UDM。 |
| Authentication拒绝原因值(RES检查失败)                 | 该参数用于设置因鉴权流程RES检查失败而导致拒绝接入时，下发给终端的原因值。                                                                                                                                                             |
| Authentication拒绝原因值(UE返回MAC Failure)         | 该参数用于设置因鉴权流程UE返回MAC failure而导致拒绝接入时，下发给终端的原因值。                                                                                                                                                     |
| Authentication拒绝原因值(UE返回Synch failure)       | 该参数用于设置因鉴权流程UE返回Synch Failure而导致拒绝接入时，下发给终端的原因值。                                                                                                                                                   |
| Check IMEI拒绝原因值(IMEI检查失败)                    | 该参数用于设置因IMEI检查失败而导致拒绝接入时，下发给终端的原因值。                                                                                                                                                                |
| 漫游受限拒绝原因值                                    | 该参数用于设置因漫游受限而导致拒绝接入时，下发给UE的原因值。                                                                                                                                                                    |
| AIR拒绝原因值(USER_NOT_FOUND)                     | 该参数用于设置AIR流程AUSF返回404 Not Found，携带的ProblemDetails为USER_NOT_FOUND时，下发给UE的原因值。                                                                                                                       |
| AIR拒绝原因值(SERVING_NETWORK_NOT_AUTHORIZED)     | 该参数用于设置AIR流程AUSF返回403 Forbidden，携带的ProblemDetails为SERVING_NETWORK_NOT_AUTHORIZED时，下发给UE的原因值。                                                                                                       |
| AIR拒绝原因值(AUTHENTICATION_REJECTED)            | 该参数用于设置AIR流程AUSF返回403 Forbidden，携带的ProblemDetails为AUTHENTICATION_REJECTED时，下发给UE的原因值。                                                                                                              |
| AIR拒绝原因值(INVALID_HN_PUBLIC_KEY_IDENTIFIER)   | 该参数用于设置AIR流程AUSF返回403 Forbidden，携带的ProblemDetails为INVALID_HN_PUBLIC_KEY_IDENTIFIER时，下发给UE的原因值。                                                                                                     |
| AIR拒绝原因值(CONTEXT_NOT_FOUND)                  | 该参数用于设置AIR流程AUSF返回404 Not Found，携带的ProblemDetails为CONTEXT_NOT_FOUND时，下发给UE的原因值。                                                                                                                    |
| AIR拒绝原因值(INVALID_SCHEME_OUTPUT)              | 该参数用于设置AIR流程AUSF返回403 Forbidden，携带的ProblemDetails为INVALID_SCHEME_OUTPUT时，下发给UE的原因值。                                                                                                                |
| AIR拒绝原因值(UNSUPPORTED_PROTECTION_SCHEME)      | 该参数用于设置AIR流程AUSF返回501 Not Implemented，携带的ProblemDetails为UNSUPPORTED_PROTECTION_SCHEME时，下发给UE的原因值。                                                                                                  |
| UDM注册拒绝原因值(USER_NOT_FOUND)                   | 该参数用于设置UDM注册流程UDM返回404 Not Found，携带的ProblemDetails为USER_NOT_FOUND时，下发给UE的原因值。                                                                                                                      |
| UDM注册拒绝原因值(UNKNOWN_5GS_SUBSCRIPTION)         | 该参数用于设置UDM注册流程UDM返回403 Forbidden，携带的ProblemDetails为UNKNOWN_5GS_SUBSCRIPTION时，下发给UE的原因值。                                                                                                            |
| UDM注册拒绝原因值(NO_PS_SUBSCRIPTION)               | 该参数用于设置UDM注册流程UDM返回403 Forbidden，携带的ProblemDetails为NO_PS_SUBSCRIPTION时，下发给UE的原因值。                                                                                                                  |
| UDM注册拒绝原因值(ROAMING_NOT_ALLOWED)              | 该参数用于设置UDM注册流程UDM返回403 Forbidden，携带的ProblemDetails为ROAMING_NOT_ALLOWED时，下发给UE的原因值。                                                                                                                 |
| UDM注册拒绝原因值(ACCESS_NOT_ALLOWED)               | 该参数用于设置UDM注册流程UDM返回403 Forbidden，携带的ProblemDetails为ACCESS_NOT_ALLOWED时，下发给UE的原因值。                                                                                                                  |
| UDM注册拒绝原因值(RAT_NOT_ALLOWED)                  | 该参数用于设置UDM注册流程UDM返回403 Forbidden，携带的ProblemDetails为RAT_NOT_ALLOWED时，下发给UE的原因值。                                                                                                                     |
| UDM注册拒绝原因值(REAUTHENTICATION_REQUIRED)        | 该参数用于设置UDM注册流程UDM返回403 Forbidden，携带的ProblemDetails为REAUTHENTICATION_REQUIRED时，下发给UE的原因值。                                                                                                           |
| UDM获取签约数据拒绝原因值(USER_NOT_FOUND)               | 该参数用于设置UDM获取签约数据流程UDM返回404 Not Found，携带的ProblemDetails为USER_NOT_FOUND时，下发给UE的原因值。                                                                                                                  |
| UDM获取签约数据拒绝原因值(DATA_NOT_FOUND)               | 该参数用于设置UDM获取签约数据流程UDM返回404 Not Found，携带的ProblemDetails为DATA_NOT_FOUND时，下发给UE的原因值。                                                                                                                  |
| UDM订阅拒绝原因值(USER_NOT_FOUND)                   | 该参数用于设置UDM订阅流程UDM返回404 Not Found，携带的ProblemDetails为USER_NOT_FOUND时，下发给UE的原因值。                                                                                                                      |
| UDM订阅拒绝原因值(UNSUPPORTED_RESOURCE_URI)         | 该参数用于设置UDM订阅流程UDM返回501 Not Implemented，携带的ProblemDetails为UNSUPPORTED_RESOURCE_URI时，下发给UE的原因值。                                                                                                      |
| AIR拒绝原因值(SUBSCRIPTION_NOT_FOUND)             | 该参数用于设置AIR流程AUSF返回404 Not Found，携带的ProblemDetails为SUBSCRIPTION_NOT_FOUND时，下发给UE的原因值。                                                                                                               |
| 强制向UDM注册                                     | 该参数用于表示当UE初始注册到AMF时，AMF不论本地是否存在该UE的上下文信息都强制向UDM发起注册流程。                                                                                                                                             |
| 区域限制拒绝原因值                                    | 该参数用于设置由于UE当前处于接入限制区域而拒绝接入时，下发给UE的原因值。处在接入限制区域内的UE被禁止注册到5GC。                                                                                                                                       |
| 接入限制拒绝原因值                                    | 该参数用于设置由于RAT限制或者核心网类型限制而拒绝接入时，下发给UE的原因值。                                                                                                                                                           |
| AIR拒绝原因值(Too Many Requests)                  | 该参数用于设置AIR流程AUSF返回429 Too Many Requests时，下发给UE的原因值。                                                                                                                                                |
| AIR拒绝原因值(Service Unavailable)                | 该参数用于设置AIR流程AUSF返回503 Service Unavailable时，下发给UE的原因值。                                                                                                                                              |
| AIR拒绝原因值(超时)                                 | 该参数用于设置AIR流程等待AUSF响应超时时，下发给UE的原因值。                                                                                                                                                                 |
| UDM获取签约数据拒绝原因值(SUBSCRIPTION_NOT_FOUND)       | 该参数用于设置UDM获取签约数据流程UDM返回404 Not Found，携带的ProblemDetails为SUBSCRIPTION_NOT_FOUND时，下发给UE的原因值。                                                                                                          |
| UDM获取签约数据拒绝原因值(Too Many Requests)            | 该参数用于设置UDM获取签约数据流程UDM返回429 Too Many Requests时，下发给UE的原因值。                                                                                                                                           |
| UDM获取签约数据拒绝原因值(Service Unavailable)          | 该参数用于设置UDM获取签约数据流程UDM返回503 Service Unavailable时，下发给UE的原因值。                                                                                                                                         |
| UDM获取签约数据拒绝原因值(超时)                           | 该参数用于设置UDM获取签约数据流程等待UDM响应超时时，下发给UE的原因值。                                                                                                                                                            |
| UDM注册拒绝原因值(Too Many Requests)                | 该参数用于设置UDM注册流程UDM返回429 Too Many Requests时，下发给UE的原因值。                                                                                                                                               |
| UDM注册拒绝原因值(Service Unavailable)              | 该参数用于设置UDM注册流程UDM返回503 Service Unavailable时，下发给UE的原因值。                                                                                                                                             |
| UDM注册拒绝原因值(超时)                               | 该参数用于设置UDM注册流程等待UDM响应超时时，下发给UE的原因值。                                                                                                                                                                |
| UDM订阅拒绝原因值(Too Many Requests)                | 该参数用于设置UDM订阅流程UDM返回429 Too Many Requests时，下发给UE的原因值。                                                                                                                                               |
| UDM订阅拒绝原因值(Service Unavailable)              | 该参数用于设置UDM订阅流程UDM返回503 Service Unavailable时，下发给UE的原因值。                                                                                                                                             |
| UDM订阅拒绝原因值(超时)                               | 该参数用于设置UDM订阅流程等待UDM响应超时时，下发给UE的原因值。                                                                                                                                                                |
| AUSF发现失败拒绝原因值(USER_NOT_FOUND)                | 该参数用于设置AUSF发现流程TOPO返回404 Not Found时，下发给UE的原因值。                                                                                                                                                     |
| AUSF发现拒绝原因值(其他原因)                            | 该参数用于设置AUSF发现流程TOPO返回404 Not Found以外的失败时，下发给UE的原因值。                                                                                                                                                |
| 服务区域限制拒绝原因值                                  | 该参数用于设置由于服务区域限制而拒绝UE的业务流程（如服务请求、PDU会话建立）时，下发给UE的原因值。                                                                                                                                               |
| 无可用网络切片拒绝原因值                                 | 该参数用于设置核心网为UE决策允许的网络切片（Allowed NSSAI）为空时，下发给UE的原因值。                                                                                                                                                |
| PCF发现拒绝原因值(Not Found)                        | 该参数用于设置PCF发现流程返回404 Not Found时，下发给UE的原因值。                                                                                                                                                          |
| PCF发现拒绝原因值(其他原因)                             | 该参数用于设置PCF发现流程返回404 Not Found以外的失败时，下发给UE的原因值。                                                                                                                                                     |
| PCF策略拒绝原因值(RESOURCE_URI_STRUCTURE_NOT_FOUND) | 该参数用于设置AMF创建/更新策略时PCF返回404 Not Found，下发给UE的原因值。                                                                                                                                                    |
| PCF策略拒绝原因值(其他原因)                             | 该参数用于设置AMF创建/更新策略时PCF返回404 Not Found以外的失败时，下发给UE的原因值。                                                                                                                                              |
| ODB拒绝原因值                                     | 该参数用于设置由于ODB限制接入下发给UE的原因值。                                                                                                                                                                         |
| UDM注册拒绝原因值(CONTEXT_NOT_FOUND)                | 该参数用于设置UDM注册流程UDM返回404 Not Found，携带的ProblemDetails为CONTEXT_NOT_FOUND时，下发给UE的原因值。                                                                                                                   |
| TA级网络切片不可用原因值                                | 该参数用于设置TA级切片不可用导致UE决策允许的网络切片（Allowed NSSAI）为空时，下发给UE的原因值。                                                                                                                                          |
| 终端消息非法拒绝原因值                                  | 该参数用于设置核心网收到终端的消息不符合3GPP标准协议，AMF拒绝用户接入，下发给UE的原因值。                                                                                                                                                  |
| AUSF发现拒绝原因值(流控)                              | 该参数用于设置注册流程中服务发现AUSF请求因自保流控被丢弃时，系统下发UE的原因值。                                                                                                                                                        |
| SMC拒绝原因值                                     | 该参数用于设置SMC流程AMF发送Security Mode Command消息后，UE回复Security Mode Reject，导致NAS安全算法协商失败，下发给UE的原因值。                                                                                                        |
| SMC超时原因值                                     | 该参数用于设置SMC流程AMF发送Security Mode Command消息后，UE响应超时导致NAS安全算法协商失败，下发给UE的原因值。                                                                                                                           |
| CAG拒绝原因值                                     | 该参数用于设置注册流程或服务请求流程中，非CAG用户非紧急场景下从CAG基站接入，导致请求被拒绝，AMF下发给UE的原因值。                                                                                                                                     |
| AUTH HTTP过载拒绝原因值                             | 该参数用于设置鉴权流程因HTTP过载而导致拒绝接入时，下发给终端的原因值。                                                                                                                                                              |
| 获取UDM签约数据HTTP过载拒绝原因值                         | 该参数用于设置UDM获取签约数据因HTTP过载而导致拒绝接入时，下发给终端的原因值。                                                                                                                                                         |
| Serving Plmn变更注册拒绝原因值                        | 该参数用于设置AMF在收到Serving PLMN变更的移动/周期注册，AMF拒绝用户接入时，下发给UE的原因值。                                                                                                                                          |
| AUTH HTR流控拒绝原因值                              | 该参数用于设置鉴权流程中因触发HTTP的HTR流控而导致拒绝接入时，AMF下发给终端的拒绝原因值。                                                                                                                                                  |
| 获取UDM签约数据HTR流控拒绝原因值                          | 该参数用于设置UDM获取签约数据因触发HTTP的HTR流控而导致拒绝接入时，AMF下发给终端的拒绝原因值。                                                                                                                                              |
| AIR拒绝原因值(SCP/SEPP故障)                         | 该参数用于设置AIR流程SCP/SEPP故障时，AMF下发给UE的原因值。                                                                                                                                                              |
| UDM注册拒绝原因值(SCP/SEPP故障)                       | 该参数用于设置UDM注册流程SCP/SEPP故障时，AMF下发给UE的原因值。                                                                                                                                                            |
| UDM获取签约数据拒绝原因值(SCP/SEPP故障)                   | 该参数用于设置向UDM获取签约数据流程SCP/SEPP故障时，AMF下发给UE的原因值。                                                                                                                                                       |
| UDM订阅拒绝原因值(SCP/SEPP故障)                       | 该参数用于设置UDM订阅流程SCP/SEPP故障时，AMF下发给UE的原因值。                                                                                                                                                            |
| PCF策略拒绝原因值(SCP/SEPP故障)                       | 该参数用于设置PCF策略交互流程SCP/SEPP故障时，AMF下发给UE的原因值。 该参数为预埋配置，当前版本暂不支持。                                                                                                                                       |
| SCP/SEPP故障                                   | 该参数用于设置其它业务流程SCP/SEPP故障时，AMF下发给UE的原因值。 该参数为预埋配置，当前版本暂不支持。                                                                                                                                          |
| AIR SCP拒绝原因值(NF_DISCOVERY_FAILURE)           | 该参数用于设置AIR流程SCP返回状态码为400且ProblemDetails为NF_DISCOVERY_FAILURE时，AMF下发给UE的原因值。                                                                                                                        |
| AIRSCP拒绝原因值(NF_DISCOVERY_ERROR)              | 该参数用于设置AIR流程SCP返回状态码为502且ProblemDetails为NF_DISCOVERY_ERROR时，AMF下发给UE的原因值。                                                                                                                          |
| AIR SCP拒绝原因值(NF_SERVICE_FAILOVER)            | 该参数用于设置AIR流程SCP返回状态码为500且ProblemDetails为NF_SERVICE_FAILOVER时，AMF下发给UE的原因值。                                                                                                                         |
| UDM注册SCP拒绝原因值(NF_DISCOVERY_FAILURE)          | 该参数用于设置UDM注册流程SCP返回状态码为400且ProblemDetails为NF_DISCOVERY_FAILURE时，AMF下发给UE的原因值。                                                                                                                      |
| UDM注册SCP拒绝原因值(NF_DISCOVERY_ERROR)            | 该参数用于设置UDM注册流程SCP返回状态码为502且ProblemDetails为NF_DISCOVERY_ERROR时，AMF下发给UE的原因值。                                                                                                                        |
| UDM注册SCP拒绝原因值(NF_SERVICE_FAILOVER)           | 该参数用于设置UDM注册流程SCP返回状态码为500且ProblemDetails为NF_SERVICE_FAILOVER时，AMF下发给UE的原因值。                                                                                                                       |
| UDM获取签约数据SCP拒绝原因值(NF_DISCOVERY_FAILURE)      | 该参数用于设置UDM获取签约数据流程SCP返回状态码为400且ProblemDetails为NF_DISCOVERY_FAILURE时，AMF下发给UE的原因值。                                                                                                                  |
| UDM获取签约数据SCP拒绝原因值(NF_DISCOVERY_ERROR)        | 该参数用于设置UDM获取签约数据流程SCP返回状态码为502且ProblemDetails为NF_DISCOVERY_ERROR时，AMF下发给UE的原因值。                                                                                                                    |
| UDM获取签约数据SCP拒绝原因值(NF_SERVICE_FAILOVER)       | 该参数用于设置UDM获取签约数据流程SCP返回状态码为500且ProblemDetails为NF_SERVICE_FAILOVER时，AMF下发给UE的原因值。                                                                                                                   |