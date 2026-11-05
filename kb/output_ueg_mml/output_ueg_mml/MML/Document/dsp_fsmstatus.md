# 查询自动机状态(DSP FSMSTATUS)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询CSP服务管理中UDM各服务自动机的使用情况。

**说明** 

自动机：即业务流程处理对象，每个自动机会针对一种业务消息类型进行处理，例如针对注册流程的自动机，会对注册流程中的消息进行处理。

- 若要查询所有服务自动机的使用情况，请不要输入任何参数。
- 若要查询某个服务自动机的使用情况，请输入“服务类型”参数，或者“服务类型”和“SF实例号”参数的组合。

## 注意事项

无。

## 参数说明

| 参数标识         | 参数名称   | 参数说明                                                                                                                                                                                                                                                 |
|:-------------|:-------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SERVICETYPE  | 服务类型   | 可选必选说明：可选参数。 参数含义：用于指示CSP服务管理中UDM的服务类型；若不输入，则表示查询所有服务的自动机使用情况。该参数通过DSP UDMSERVICE命令获得。 取值范围： UdmSubService(UdmSubService)UdmAuthService(UdmAuthService)NRFClient(NRFClient)UdmHttpService(UdmHttpService)UdmAlbService(UdmAlbService) 默认值：无。 配置原则：无。 |
| SFINSTANCEID | SF实例号  | 可选必选说明：可选参数。 参数含义：用于指示CSP服务管理中UDM的SF实例号；若不输入，则表示查询指定服务的自动机使用情况。该参数通过DSP UDMSERVICE命令获得。 取值范围：长度不超过65位的字符串。 默认值：无。 配置原则：当“服务类型”参数配置时，此参数配置才生效。                                                                                                        |

## 使用实例

1. 查询所有服务的自动机使用情况。

   ```
   DSP FSMSTATUS:;
   ```

   ```
   %%DSP FSMSTATUS:;%%
   RETCODE = 0  操作成功

   操作结果如下:
   -------------
   服务类型        SF实例号              自动机类型                                         空闲自动机数量  正在使用自动机数量  使用率  

   UdmHttpService  13637885775234378270  CLIENT-CONTEXT                                     0               0                   0       
   UdmHttpService  13637885775234378270  SERVER-CONTEXT                                     0               0                   0       
   UdmAuthService  13635929769818367985  GET:ninternal-ausf/auth-req-num                    1               0                   0       
   UdmAuthService  13635929769818367985  POST:nausf-auth/ue-authentications                 0               0                   0       
   UdmAuthService  13635929769818367985  POST:ninternal-dcs/lic-ctrl-notification           0               0                   0       
   UdmSubService   13636420126234552524  POST:internalmsg/v1/notifydcs                      0               0                   0       
   UdmSubService   13636420126234552524  POST:internalmsg/v1/refreshDbCache                 0               1                   1       
   UdmSubService   13636420126234552524  POST:ninterwork/iwf/iwf5glocation                  0               0                   0       
   UdmSubService   13636420126234552524  POST:namf-evts/ee-notification                     0               0                   0       
   UdmSubService   13636420126234552524  POST:ninterwork/AmfIPReachSub                      0               0                   0       
   UdmSubService   13636420126234552524  DELETE:nudm-uecm/registrations/smsf-3gpp-access    0               0                   0       
   UdmSubService   13636420126234552524  POST:ninterwork/udmpcscfrestoration                0               0                   0       
   UdmSubService   13636420126234552524  GET:nudm-sdm/sms-data                              0               0                   0       
   UdmSubService   13636420126234552524  POST:internalmsg/ue-context-in-smsf-data           0               0                   0       
   UdmSubService   13636420126234552524  POST:internalmsg/v1/actorStatusManager             0               0                   0       
   UdmSubService   13636420126234552524  PATCH:nudm-uecm/registrations/amf-3gpp-access      0               0                   0       
   UdmSubService   13636420126234552524  PUT:nudm-uecm/registrations/amf-non-3gpp-access    0               0                   0       
   UdmSubService   13636420126234552524  GET:nudm-uecm/registrations/amf-non-3gpp-access    0               0                   0       
   UdmSubService   13636420126234552524  POST:ninterwork/iwf/idr-usrinfo                    0               0                   0       
   UdmSubService   13636420126234552524  POST:ninterwork/iwf/idr-usrstatus                  0               0                   0       
   UdmSubService   13636420126234552524  POST:namf-evts/ipreachnotify                       0               0                   0       
   UdmSubService   13636420126234552524  PUT:nudm-uecm/registrations/smsf-3gpp-access       0               0                   0       
   UdmSubService   13636420126234552524  POST:ninterwork/iwf/idr-ipreach                    0               0                   0       
   UdmSubService   13636420126234552524  GET:nudm-sdm/am-data                               0               0                   0       
   UdmSubService   13636420126234552524  GET:nudm-sdm/sm-data                               0               0                   0       
   UdmSubService   13636420126234552524  POST:nudm-sdm/sdm-subscriptions                    0               0                   0       
   UdmSubService   13636420126234552524  GET:nudm-sdm/id-translation-result                 0               0                   0       
   UdmSubService   13636420126234552524  POST:internalmsg/v1/dciPackMsg                     0               0                   0       
   UdmSubService   13636420126234552524  PUT:nudm-uecm/registrations/amf-3gpp-access        0               0                   0       
   UdmSubService   13636420126234552524  GET:nudm-sdm/trace-data                            0               0                   0       
   UdmSubService   13636420126234552524  DELETE:nudm-ee/ee-subscriptions                    0               0                   0       
   UdmSubService   13636420126234552524  POST:internalmsg/v1/refreshBEStatus                0               1                   1       
   UdmSubService   13636420126234552524  PATCH:nudm-uecm/registrations/amf-non-3gpp-access  0               0                   0       
   UdmSubService   13636420126234552524  POST:ninterwork/TADS                               0               0                   0       
   UdmSubService   13636420126234552524  GET:nudm-sdm/ue-context-in-smsf-data               0               0                   0       
   UdmSubService   13636420126234552524  POST:internalmsg/v1/refreshServiceStatus           0               1                   1       
   UdmSubService   13636420126234552524  POST:mtntrace/e2e/trace-notification               0               0                   0       
   UdmSubService   13636420126234552524  POST:ninterwork/iwf/mod-imsi                       0               0                   0       
   UdmSubService   13636420126234552524  POST:ninterwork/iwf/idr-tads                       0               0                   0       
   UdmSubService   13636420126234552524  GET:nudm-sdm/ue-context-in-smf-data                0               0                   0       
   UdmSubService   13636420126234552524  POST:ninterwork/pcscfrestoration                   0               0                   0       
   UdmSubService   13636420126234552524  GET:nudm-sdm/sms-mng-data                          0               0                   0       
   UdmSubService   13636420126234552524  POST:ninterwork/provide-loc-info                   0               0                   0       
   UdmSubService   13636420126234552524  POST:ninterwork/iwf/clr                            0               0                   0       
   UdmSubService   13636420126234552524  POST:ninterwork/userstate                          0               0                   0       
   UdmSubService   13636420126234552524  POST:ninterwork/ue-context-in-smf-data             0               0                   0       
   UdmSubService   13636420126234552524  POST:ninterwork/iwf/dsr                            0               0                   0       
   UdmSubService   13636420126234552524  GET:nudm-uecm/registrations/amf-3gpp-access        0               0                   0       
   UdmSubService   13636420126234552524  DELETE:nudm-uecm/registrations/smf-registrations   0               0                   0       
   UdmSubService   13636420126234552524  GET:nudm-sdm/dataset-names                         0               0                   0       
   UdmSubService   13636420126234552524  POST:internalmsg/v1/refreshLicData                 0               1                   1       
   UdmSubService   13636420126234552524  POST:internalmsg/v1/autoprovisioning               0               0                   0       
   UdmSubService   13636420126234552524  GET:ninternal-sub/id-translation-result            2               0                   0       
   UdmSubService   13636420126234552524  POST:internalmsg/v1/notifysau                      0               0                   0       
   UdmSubService   13636420126234552524  POST:ninterwork/SendAmfDeregMsgID                  0               0                   0       
   UdmSubService   13636420126234552524  POST:ninternal-dcs/e2etracenotify                  0               0                   0       
   UdmSubService   13636420126234552524  POST:ninterwork/sendPurMsg                         0               0                   0       
   UdmSubService   13636420126234552524  POST:ninterwork/udmipreachnotify                   0               0                   0       
   UdmSubService   13636420126234552524  PATCH:nudm-uecm/registrations/smsf-3gpp-access     0               0                   0       
   UdmSubService   13636420126234552524  GET:nudm-uecm/registrations/smsf-3gpp-access       0               0                   0       
   UdmSubService   13636420126234552524  POST:internalmsg/v1/insertBackupAmf                0               0                   0       
   UdmSubService   13636420126234552524  POST:internalmsg/v1/timeDelayManager               0               0                   0       
   UdmSubService   13636420126234552524  POST:ninterwork/iwf/idr-update                     0               0                   0       
   UdmSubService   13636420126234552524  PUT:nudm-uecm/registrations/smf-registrations      0               0                   0       
   UdmSubService   13636420126234552524  GET:nudm-sdm/nssai                                 0               0                   0       
   UdmSubService   13636420126234552524  POST:internalmsg/v1/notifyhlb                      0               0                   0       
   UdmSubService   13636420126234552524  POST:internalmsg/v1/refreshGlbData                 0               1                   1       
   UdmSubService   13636420126234552524  POST:ninterwork/nssai                              0               0                   0       
   UdmSubService   13636420126234552524  POST:ninterwork/iwf/idr-cscf                       0               0                   0       
   UdmSubService   13636420126234552524  DELETE:nudm-sdm/sdm-subscriptions                  0               0                   0       
   UdmSubService   13636420126234552524  POST:nudm-ee/ee-subscriptions                      0               0                   0       
   UdmSubService   13636420126234552524  POST:ninterwork/AMFDeregistration                  0               0                   0       
   UdmSubService   13636420126234552524  POST:namf-evts/iwfipreachnotify                    0               0                   0       
   UdmSubService   13636420126234552524  GET:nudm-sdm/smf-select-data                       0               0                   0       
   UdmSubService   13636420126234552524  PATCH:nudm-sdm/sdm-subscriptions                   0               0                   0       
   UdmSubService   13636420126234552524  GET:ninterwork/timedetect                          0               0                   0       
   UdmSubService   13636420126234552524  POST:mcinotify/userdata                            1               0                   0       
   UdmSubService   13636420126234552524  POST:ninterwork/ueReachability                     0               0                   0       
   UdmSubService   13636420126234552524  GET:nudm-uecm/registrations/location               0               0                   0
   NRFClient       13635203997654758192  NFSRV                                              0               0                   0       
   NRFClient       13635203997654758192  GET:nnrf-disc/nf-instances                         0               0                   0       
   NRFClient       13635203997654758192  NFSUBSCRDATA                                       0               0                   0       
   NRFClient       13635203997654758192  DiscSubscrActor                                    0               0                   0       
   NRFClient       13635203997654758192  HeartBeatActor                                     0               0                   0       
   NRFClient       13635203997654758192  POST:nnrf-oauth2/token                             0               0                   0       
   UdmAlbService   13637885775234378276  CLIENT-CONTEXT                                     0               0                   0
   UdmSubService   13636420126234552524  PATCH:nudm-ee/ee-subscriptions                     0               0                   0         
   (结果个数 = 87)

   ---    END
   ```
2. 查询“服务类型”为“UdmSubService(UdmSubService)”的自动机使用情况。

   ```
   DSP FSMSTATUS: SERVICETYPE=UdmSubService;
   ```

   ```
   %%DSP FSMSTATUS: SERVICETYPE=UdmSubService;%%
   RETCODE = 0  操作成功

   操作结果如下:
   -------------
   服务类型       SF实例号              自动机类型                                         空闲自动机数量  正在使用自动机数量  使用率  

   UdmSubService  12582740665704361421  GET:nudm-sdm/dataset-names                         0               0                   0       
   UdmSubService  12582740665704361421  GET:nudm-sdm/id-translation-result                 0               0                   0       
   UdmSubService  12582740665704361421  POST:ninterwork/AmfIPReachSub                      0               0                   0       
   UdmSubService  12582740665704361421  POST:ninterwork/pcscfrestoration                   0               0                   0       
   UdmSubService  12582740665704361421  POST:ninterwork/iwf/idr-ipreach                    0               0                   0       
   UdmSubService  12582740665704361421  PATCH:nudm-uecm/registrations/amf-non-3gpp-access  0               0                   0       
   UdmSubService  12582740665704361421  DELETE:nudm-uecm/registrations/smf-registrations   0               0                   0       
   UdmSubService  12582740665704361421  GET:nudm-sdm/nssai                                 0               0                   0       
   UdmSubService  12582740665704361421  DELETE:nudm-ee/ee-subscriptions                    0               0                   0       
   UdmSubService  12582740665704361421  POST:ninterwork/iwf/clr                            0               0                   0       
   UdmSubService  12582740665704361421  POST:ninterwork/iwf/idr-usrinfo                    0               0                   0       
   UdmSubService  12582740665704361421  POST:ninterwork/iwf/idr-tads                       0               0                   0       
   UdmSubService  12582740665704361421  PUT:nudm-uecm/registrations/amf-non-3gpp-access    0               0                   0       
   UdmSubService  12582740665704361421  PUT:nudm-uecm/registrations/smf-registrations      0               0                   0       
   UdmSubService  12582740665704361421  GET:nudm-sdm/ue-context-in-smf-data                0               0                   0       
   UdmSubService  12582740665704361421  POST:nudm-sdm/sdm-subscriptions                    1               0                   0       
   UdmSubService  12582740665704361421  GET:nudm-uecm/registrations/amf-3gpp-access        0               0                   0       
   UdmSubService  12582740665704361421  GET:nudm-sdm/smf-select-data                       0               0                   0       
   UdmSubService  12582740665704361421  POST:ninterwork/TADS                               0               0                   0       
   UdmSubService  12582740665704361421  POST:ninterwork/provide-loc-info                   0               0                   0       
   UdmSubService  12582740665704361421  POST:ninterwork/udmipreachnotify                   0               0                   0       
   UdmSubService  12582740665704361421  GET:ninternal-sub/id-translation-result            1               0                   0       
   UdmSubService  12582740665704361421  POST:ninterwork/iwf/idr-update                     0               0                   0       
   UdmSubService  12582740665704361421  POST:ninterwork/iwf/iwf5glocation                  0               0                   0       
   UdmSubService  12582740665704361421  PATCH:nudm-uecm/registrations/amf-3gpp-access      1               0                   0       
   UdmSubService  12582740665704361421  POST:ninterwork/udmpcscfrestoration                0               0                   0       
   UdmSubService  12582740665704361421  POST:ninterwork/ue-context-in-smf-data             0               0                   0       
   UdmSubService  12582740665704361421  POST:ninterwork/iwf/idr-cscf                       0               0                   0       
   UdmSubService  12582740665704361421  POST:ninterwork/iwf/dsr                            0               0                   0       
   UdmSubService  12582740665704361421  GET:nudm-uecm/registrations/amf-non-3gpp-access    0               0                   0       
   UdmSubService  12582740665704361421  GET:nudm-sdm/sm-data                               0               0                   0       
   UdmSubService  12582740665704361421  POST:nudm-ee/ee-subscriptions                      0               0                   0       
   UdmSubService  12582740665704361421  POST:namf-evts/iwfipreachnotify                    0               0                   0       
   UdmSubService  12582740665704361421  PUT:nudm-uecm/registrations/amf-3gpp-access        1               0                   0       
   UdmSubService  12582740665704361421  GET:nudm-sdm/am-data                               0               0                   0       
   UdmSubService  12582740665704361421  DELETE:nudm-sdm/sdm-subscriptions                  0               0                   0       
   UdmSubService  12582740665704361421  POST:namf-evts/ee-notification                     0               0                   0       
   UdmSubService  12582740665704361421  POST:mcinotify/userdata                            2               0                   0       
   UdmSubService  12582740665704361421  POST:ninterwork/iwf/idr-usrstatus                  0               0                   0       
   UdmSubService  12582740665704361421  POST:namf-evts/ipreachnotify                       0               0                   0       
   UdmSubService  12582740665704361421  POST:ninterwork/AMFDeregistration                  1               0                   0       
   UdmSubService  12582740665704361421  POST:ninterwork/userstate                          0               0                   0       
   UdmSubService  12582740665704361421  POST:ninterwork/autoprovisioning                   0               0                   0       
   UdmSubService  12582740665704361421  POST:ninterwork/ueReachability                     0               0                   0       
   UdmSubService  12582740665704361421  POST:ninterwork/iwf/mod-imsi                       0               0                   0       
   UdmSubService  12582740665704361421  GET:nudm-uecm/registrations/location               0               0                   0       
   UdmSubService  12582740665704361421  PATCH:nudm-ee/ee-subscriptions                     0               0                   0   
   (结果个数 = 47)

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见表1所示。

| 输出项名称     | 输出项解释                                        |
|:----------|:---------------------------------------------|
| 服务类型      | 用于返回CSP服务管理中UDM的服务类型。                        |
| SF实例号     | 用于返回CSP服务管理中UDM的SF实例号。                       |
| 自动机类型     | 用于返回服务中自动机所处理的消息类型，包括鉴权、注册、去注册、订阅通知等。        |
| 空闲自动机数量   | 用于返回服务中处于空闲状态的自动机数量。                         |
| 正在使用自动机数量 | 用于返回服务中处于正在使用状态的自动机数量。                       |
| 使用率       | 用于返回服务自动机的使用率。该参数将根据UDMFsmNum(UDM自动机数量)软参计算。 |

该命令执行异常，会返回对应的错误码。常见错误码如表2所示。

|    错误码 | 错误码解释   | 原因分析                                                | 处理建议                        |
|-------:|:--------|:----------------------------------------------------|:----------------------------|
| 360041 | 参数值不合法。 | 当查询某个服务的自动机使用情况时，在未输入“服务类型”的前提下输入参数“SF实例号”，不符合配置原则。 | 输入“服务类型”后，再输入参数“SF实例号”执行命令。 |
| 360133 | 查询部分成功。 | 当查询所有服务的自动机使用情况时，部分服务查询成功，部分服务查询失败。                 | 请联系华为技术支持处理。                |