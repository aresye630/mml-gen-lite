# 显示服务订阅缓存信息(DSP INSTCACHE)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询各个服务缓存的服务实例信息。

## 注意事项

无。

## 参数说明

| 参数标识            | 参数名称     | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|:----------------|:---------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SUBSCRIBINGINST | 订阅者实例号   | 可选必选说明：必选参数 参数含义：用于查询指定实例号服务实例信息。 取值范围：长度不超过32位的字符串 默认值：无。 配置原则：无。  说明： 本参数值可通过在OM Portal界面选择“应用管理 > MML”，在UPCF网元下执行以下命令行查看报文返回结果的“服务实例ID”来获取。 DSP SERVICEINST: TYPE=BYNAME, SERVICENAME="xxx"; （其中xxx对应服务名称，可通过DSP SERVICENAME命令查询获取。）                                                                                                                                                                                                      |
| SUBSCRIBEDTYPE  | 被订阅者服务类型 | 可选必选说明：可选参数 参数含义：用于查询指定被订阅服务类型的实例信息。 取值范围： PcfAppCtrlServicePcfNrfClientServicePcfLicenseCenterServicePcfDisCtrlServicePcfNotifyLogFileServicePcfHTTPLoadBalanceServicePcfDiamLoadBalanceServicePcfPolicyEngineServicePcfHttpAgentServicePcfOfflineTaskCtrlServicePcfOfflineTaskExecServicePcfGlobalDataServicePcfSgmServicePcfLdapServicePcfPolicyManagementServicePcfNotificationTaskServicePcfDataReportServiceUDRDbbroker 默认值：无。 配置原则：无。 |

## 使用实例

查询缓存实例资源信息，“订阅者实例号”为“18436326952659848623”。

```
%%DSP INSTCACHE: SUBSCRIBINGINST="18436326952659848623";%%
RETCODE = 0  操作成功

结果如下
------------------------
订阅者服务类型           订阅者实例号          被订阅者服务类型             被订阅者实例号         服务信息
PcfPolicyEngineService   18436326952659848623  PcfSgmService                18436555706913000892   {"podID":"pcf-all-pod20-1", "isReady":true, "isMaster":false, "NTS_SMS":false, "NTS_EMAIL":false, "NTS_SOAP":false, "token":0, "nodeId":"10.255.50.80"}     
PcfPolicyEngineService   18436326952659848623  PcfSgmService                18436555706913021372   {"podID":"pcf-all-pod20-0", "isReady":true, "isMaster":false, "NTS_SMS":false, "NTS_EMAIL":false, "NTS_SOAP":false, "token":0, "nodeId":"10.255.50.132"}    
PcfPolicyEngineService   18436326952659848623  PcfNotificationTaskService   18436362145688980913   {"podID":"pcf-all-pod20-1", "isReady":true, "isMaster":false, "NTS_SMS":true, "NTS_EMAIL":true, "NTS_SOAP":true, "token":10000, "nodeId":"10.255.50.80"}    
PcfPolicyEngineService   18436326952659848623  PcfNotificationTaskService   18436362145689001393   {"podID":"pcf-all-pod20-0", "isReady":true, "isMaster":false, "NTS_SMS":true, "NTS_EMAIL":true, "NTS_SOAP":true, "token":10001, "nodeId":"10.255.50.132"} 
(结果个数 = 4)

---    结束
```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义参见表1。

| 输出项名称    | 输出项解释                                                                                                                                                                                                                                                                                                                                                                                                  |
|:---------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 订阅者服务类型  | 用于返回订阅者服务类型。 取值范围： PcfAppCtrlServicePcfNrfClientServicePcfLicenseCenterServicePcfDisCtrlServicePcfNotifyLogFileServicePcfHTTPLoadBalanceServicePcfDiamLoadBalanceServicePcfPolicyEngineServicePcfHttpAgentServicePcfOfflineTaskCtrlServicePcfOfflineTaskExecServicePcfGlobalDataServicePcfSgmServicePcfLdapService                                                                                     |
| 订阅者实例号   | 用于返回订阅者实例号。 取值范围：长度不超过32位的字符串                                                                                                                                                                                                                                                                                                                                                                          |
| 被订阅者服务类型 | 用于返回被订阅者服务类型。 取值范围： PcfAppCtrlServicePcfNrfClientServicePcfLicenseCenterServicePcfDisCtrlServicePcfNotifyLogFileServicePcfHTTPLoadBalanceServicePcfDiamLoadBalanceServicePcfPolicyEngineServicePcfHttpAgentServicePcfOfflineTaskCtrlServicePcfOfflineTaskExecServicePcfGlobalDataServicePcfSgmServicePcfLdapServicePcfPolicyManagementServicePcfNotificationTaskServicePcfDataReportServiceUDRDbbroker |
| 被订阅者实例号  | 用于返回被订阅者实例号。 取值范围：长度不超过32位的字符串                                                                                                                                                                                                                                                                                                                                                                         |
| 服务信息     | 用于返回服务信息。 取值范围：长度不超过1024位的字符串                                                                                                                                                                                                                                                                                                                                                                          |