# 查询消息优先级(LST MSGPRIORITY)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询消息优先级和最小消息数的配置信息：

- 若需要查询全部消息的配置信息，请不要输入任何参数。
- 若需要查询某些消息的配置信息，请输入“消息类型”参数或“消息类型”和“消息URL”这两个参数的组合。

## 注意事项

无。

## 参数说明

| 参数标识    | 参数名称   | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|:--------|:-------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MSGTYPE | 消息类型   | 可选必选说明：可选参数 参数含义：用于指示系统按照消息类型来查询消息优先级的配置信息；若不输入，则表示所有的消息类型。 取值范围： Nausf-AUTH(Nausf-AUTH)Nudm-UECM(Nudm-UECM)Nudm-SDM(Nudm-SDM)Nudm-EE(Nudm-EE)DefaultPri(DefaultPri)N5g-EIR-EIC(N5g-EIR-EIC) 默认值：无。 配置原则：无。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| URL     | 消息URL  | 可选必选说明：条件可选参数 参数含义：用于指示系统按照消息URL来查询消息优先级的配置信息；若不输入，则表示所有的消息URL。 取值范围：对应不同的“消息类型”，“消息URL”的取值范围不同。所有“消息URL”的取值范围如下所示： “消息类型”为“Nausf-AUTH(Nausf-AUTH)”时：Authentications(POST:nausf-auth/ue-authentications) “消息类型”为“Nudm-UECM(Nudm-UECM)”时：NudmAmf3gppReg(PUT:nudm-uecm/registrations/amf-3gpp-access)NamfPatch(PATCH:nudm-uecm/registrations/amf-3gpp-access)NudmAmfNon3gppReg(PUT:nudm-uecm/registrations/amf-non-3gpp-access)NamfN3gppPatch(PATCH:nudm-uecm/registrations/amf-non-3gpp-access)NamfGetData(GET:nudm-uecm/registrations/amf-3gpp-access)NamfGetN3gppData(GET:nudm-uecm/registrations/amf-non-3gpp-access)NsmfRegistration(PUT:nudm-uecm/registrations/smf-registrations)NsmfDeRegistration(DELETE:nudm-uecm/registrations/smf-registrations)NudmSmsf3gppReg(PUT:nudm-uecm/registrations/smsf-3gpp-access)NsmsfDeRegistration(DELETE:nudm-uecm/registrations/smsf-3gpp-access)NsmsfN3gppDeRegistration(DELETE:nudm-uecm/registrations/smsf-non-3gpp-access)NsmsfGetData(GET:nudm-uecm/registrations/smsf-3gpp-access)NsmsfN3gppGetData(GET:nudm-uecm/registrations/smsf-non-3gpp-access)NudmLocation(GET:nudm-uecm/registrations/location) “消息类型”为“Nudm-SDM(Nudm-SDM)”时：NudmSdmUnsubscription(DELETE:nudm-sdm/sdm-subscriptions)NudmSdmPatchSubscription(PATCH:nudm-sdm/sdm-subscriptions)NudmSdmSubscription(POST:nudm-sdm/sdm-subscriptions)NamfRegistration(GET:nudm-sdm/nssai)NsmsfRegistration(GET:nudm-sdm/sms-data)IDTranslation(GET:nudm-sdm/id-translation-result)DataSet(GET:nudm-sdm/dataset-names)Smdata(GET:nudm-sdm/sm-data)NsmfSelect(GET:nudm-sdm/smf-select-data)UeContext(GET:nudm-sdm/ue-context-in-smf-data)AmData(GET:nudm-sdm/am-data)NudmGetSmsMngData(GET:nudm-sdm/sms-mng-data)NudmGetUectxInSMSFData(GET:nudm-sdm/ue-context-in-smsf-data) “消息类型”为“Nudm-EE(Nudm-EE)”时：EeSubscription(POST:nudm-ee/ee-subscriptions)EeUnSubscription(DELETE:nudm-ee/ee-subscriptions)EeModifySubscription(PATCH:nudm-ee/ee-subscriptions) “消息类型”为“DefaultPri(DefaultPri)”时：otherMsgPri(otherMsg) “消息类型”为“N5g-EIR-EIC(N5g-EIR-EIC)”时：GetEquipmentStatus(GET:n5g-eir-eic/equipment-status) 默认值：无。 配置原则：仅当本命令中的“消息类型”参数取值不为空时该参数有效。 |

## 使用实例

1. 查询所有消息的配置信息。

   ```
   LST MSGPRIORITY:;
   ```

   ```
   %%LST MSGPRIORITY:;%%
   RETCODE = 0  操作成功

   操作结果如下:
   -------------
   消息类型     消息URL                                              消息优先级  默认优先级别  微服务最小消息数  

   Nausf-AUTH   POST:nausf-auth/ue-authentications                   NORMAL(3)   NORMAL(3)     200               
   Nudm-UECM    PUT:nudm-uecm/registrations/amf-3gpp-access          HIGH(4)     HIGH(4)       200               
   Nudm-UECM    PATCH:nudm-uecm/registrations/amf-3gpp-access        HIGH(4)     HIGH(4)       100               
   Nudm-UECM    PUT:nudm-uecm/registrations/amf-non-3gpp-access      HIGH(4)     HIGH(4)       10                
   Nudm-UECM    PATCH:nudm-uecm/registrations/amf-non-3gpp-access    HIGH(4)     HIGH(4)       10                
   Nudm-UECM    GET:nudm-uecm/registrations/amf-3gpp-access          LOW(2)      LOW(2)        50                
   Nudm-UECM    GET:nudm-uecm/registrations/amf-non-3gpp-access      LOW(2)      LOW(2)        10                
   Nudm-UECM    PUT:nudm-uecm/registrations/smf-registrations        HIGH(4)     HIGH(4)       100               
   Nudm-UECM    DELETE:nudm-uecm/registrations/smf-registrations     HIGH(4)     HIGH(4)       50                
   Nudm-UECM    PUT:nudm-uecm/registrations/smsf-3gpp-access         NORMAL(3)   NORMAL(3)     50                
   Nudm-UECM    DELETE:nudm-uecm/registrations/smsf-3gpp-access      NORMAL(3)   NORMAL(3)     10                
   Nudm-UECM    DELETE:nudm-uecm/registrations/smsf-non-3gpp-access  NORMAL(3)   NORMAL(3)     10                
   Nudm-UECM    GET:nudm-uecm/registrations/smsf-3gpp-access         LOW(2)      LOW(2)        10                
   Nudm-UECM    GET:nudm-uecm/registrations/smsf-non-3gpp-access     LOW(2)      LOW(2)        10                
   Nudm-UECM    GET:nudm-uecm/registrations/location                 LOW(2)      LOW(2)        50                
   Nudm-SDM     DELETE:nudm-sdm/sdm-subscriptions                    HIGH(4)     HIGH(4)       50                
   Nudm-SDM     PATCH:nudm-sdm/sdm-subscriptions                     HIGH(4)     HIGH(4)       10                
   Nudm-SDM     POST:nudm-sdm/sdm-subscriptions                      HIGH(4)     HIGH(4)       100               
   Nudm-SDM     GET:nudm-sdm/nssai                                   HIGH(4)     HIGH(4)       200               
   Nudm-SDM     GET:nudm-sdm/sms-data                                HIGH(4)     HIGH(4)       50                
   Nudm-SDM     GET:nudm-sdm/id-translation-result                   LOW(2)      LOW(2)        50                
   Nudm-SDM     GET:nudm-sdm/dataset-names                           HIGH(4)     HIGH(4)       200               
   Nudm-SDM     GET:nudm-sdm/sm-data                                 HIGH(4)     HIGH(4)       10                
   Nudm-SDM     GET:nudm-sdm/smf-select-data                         HIGH(4)     HIGH(4)       10                
   Nudm-SDM     GET:nudm-sdm/ue-context-in-smf-data                  HIGH(4)     HIGH(4)       10                
   Nudm-SDM     GET:nudm-sdm/am-data                                 HIGH(4)     HIGH(4)       10                
   Nudm-SDM     GET:nudm-sdm/sms-mng-data                            LOW(2)      LOW(2)        10                
   Nudm-SDM     GET:nudm-sdm/ue-context-in-smsf-data                 NORMAL(3)   NORMAL(3)     10                
   Nudm-EE      POST:nudm-ee/ee-subscriptions                        LOWEST(1)   LOWEST(1)     10                
   Nudm-EE      DELETE:nudm-ee/ee-subscriptions                      LOWEST(1)   LOWEST(1)     10                
   Nudm-EE      PATCH:nudm-ee/ee-subscriptions                       LOWEST(1)   LOWEST(1)     10  
   DefaultPri   otherMsg                                             LOWEST(1)   LOWEST(1)     NULL              
   N5g-EIR-EIC  GET:n5g-eir-eic/equipment-status                     HIGH(4)     HIGH(4)       200     
   (结果个数 = 33)

   ---    END
   ```
2. 查询“消息类型”为“DefaultPri(DefaultPri)”，“消息URL”为“otherMsgPri(otherMsg)”的配置信息：

   ```
   LST MSGPRIORITY: MSGTYPE=DefaultPri, URL=otherMsgPri;
   ```

   ```
   %%LST MSGPRIORITY: MSGTYPE=DefaultPri, URL=otherMsgPri;%% 
   RETCODE = 0  操作成功  
   操作结果如下: 
   -------------
            消息类型  =  DefaultPri
             消息URL  =  otherMsg
          消息优先级  =  LOWEST(1)
        默认优先级别  =  LOWEST(1)
    微服务最小消息数  =  NULL
    (结果个数 = 1)  
   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见**MOD MSGPRIORITY**命令的参数说明。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

|    错误码 | 错误码解释       | 原因分析           | 处理建议                                                |
|-------:|:------------|:---------------|:----------------------------------------------------|
| 100016 | 参数的值不在指定范围内 | 报错的参数值不在取值范围内。 | 系统上报此错误码会提示具体的参数标识，请根据报错的参数取值范围，重新输入正确的参数值后执行本命令修改。 |