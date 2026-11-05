# 查询NF服务实例（LST CPNFSERVICE）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：AMF、SMF、NSSF、NRF、NCG、SMSF、NEF、NWDAF**

该命令用于查询NF实例下的NFS实例信息。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

| 参数标识           | 参数名称   | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|:---------------|:-------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NFINSTANCENAME | NF实例名称 | 可选必选说明：可选参数  参数含义：该参数用于指定NFS实例所归属的NF实例名称。  数据来源：全网规划  取值范围：字符串类型，输入长度范围是1~50。  默认值：无  配置原则：  本参数来源于ADD NFUUID命令中的“NF实例名称”参数。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| SRVINSTANCEID  | 服务实例标识 | 可选必选说明：可选参数  参数含义：本参数用于指定NFS实例标识。  数据来源：全网规划  取值范围：字符串类型，输入长度范围是1~50。  默认值：无  配置原则：  本参数构成字符只能是字母A～Z或a～z、数字0～9、中划线“-”和下划线“_”，例如，Service_Instance_0。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| SERVICENAME    | 服务名称   | 可选必选说明：可选参数  参数含义：本参数用于指定服务名称。  数据来源：全网规划 取值范围： SrvNameINVALID（Invalid Service Name）NrfNfm（NRF提供的Nnrf_NFManagement服务）NnrfDisc（NRF提供的Nnrf_NFDiscovery服务）NudmSdm（UDM提供的Nudm_SubscriberDataManagement服务）NudmUecm（UDM提供的Nudm_UEContextManagement服务）NudmUeau（UDM提供的Nudm_UEAuthentication服务）NudmEe（UDM提供的Nudm_EventExposure服务）NudmPp（UDM提供的Nudm_ParameterProvision服务）NamfComm（AMF提供的Namf_Communication Service服务）NamfEvts（AMF提供的Namf_EventExposure服务）NamfMt（AMF提供的Namf_MT服务）NamfLoc（AMF提供的Namf_Location服务）NsmfPduSes（SMF提供的Nsmf_PDUSession服务）NsmfEventExp（SMF提供的Nsmf_EventExposure服务）NausfAuth（AUSF提供的Nausf_UEAuthentication服务）NausfSorprot（AUSF提供的Nausf_SoRPProtection服务）NnefPfdMgnt（NEF提供的Nnef_PFDManagement）NpcfAmPlcCtrl（PCF提供的Npcf_AMPolicyControl服务）NpcfSmPlcCtrl（PCF提供的Npcf_SMPolicyControl服务）NpcfPlcauth（PCF提供的Npcf_PolicyAuthorization服务）NpcfBdtplcCtrl（PCF提供的Npcf_BDTPolicyControl服务）NpcfEventEx（PCF提供的Npcf_EventExposure服务）NpcfUePcy（PCF提供的Npcf_UEPolicyControl服务）NsmsfSms（SMSF提供的Nsmsf_SMService服务）NnssfNsSel（NSSF提供的Nnssf_NSSelection服务）NnssfNssaiAvai（NSSF提供的Nnssf_NSSAIAvailability服务）NudrDr（UDR提供的Nudr_DataRepository服务）NlmfLoc（LMF提供的Nlmf_Location服务）N5gEirEic（5G-EIR提供的N5g-eir_EquipmentIdentityCheck服务）NbsfMgmt（BSF提供的Nbsf_Management服务）NchfSpdlmtCtrl（CHF提供的Nchf_SpendingLimitControl服务）NchfConvCharg（CHF提供的Nchf_Converged_Charging服务）NnwdafEvntSubs（NWDAF提供的Nnwdaf_EventsSubscription服务）NnwdafAnalInfo（NWDAF提供的Nnwdaf_AnalyticsInfo服务）“SrvNameMAX（Max Service Name）”：已废弃。NamfMbsBroadcast（AMF提供的Namf_MbsBroadcast服务）NmbSmfTmgi（MBSMF提供的NmbSmf_Tmgi服务）NmbSmfMbssession（MBSMF提供的NmbSmf_Mbssession服务）Nnef3gppAsSessionWithQos（NEF提供的Nnef_3gppAsSessionWithQos服务）Nnef3gppMonEvent（NEF提供的Nnef_3gppMonEvent服务）NnwdafDataManagement（NWDAF提供的Nnwdaf_DataManagement服务）  默认值：无  配置原则：无 |

## 使用实例

运营商A需要查询配置的服务实例信息。

```
%%LST CPNFSERVICE:;%%
RETCODE = 0  操作成功

结果如下
--------
  NF实例名称  =  SMF_Instance_0
服务实例标识  =  Service_Instance_0
    服务名称  =  SMF提供的Nsmf_PDUSession服务
支持的NF类型  =  NULL
服务实例状态  =  REGISTERED
        域名  =  NULL
  PLMN间域名  =  NULL
 API路径前缀  =  NULL
      优先级  =  0
        容量  =  100
        负载  =  0
    支持功能  =  NULL
     Scheme  =  AUTO
(结果个数 = 1)

---    END
```

## 输出结果说明

| 输出项名称   | 输出项解释                                                                                                                                                                        |
|:--------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NF实例名称  | 该参数用于指定NFS实例所归属的NF实例名称。                                                                                                                                                      |
| 服务实例标识  | 本参数用于指定NFS实例标识。                                                                                                                                                              |
| 服务名称    | 本参数用于指定服务名称。                                                                                                                                                                 |
| 支持的NF类型 | 本参数用于指定本NFS实例向NRF注册完成后，在后续的NF发现流程中能够访问本NFS实例的NF类型。如果不配置，表示允许所有类型的NF访问。 本参数的优先级高于ADD CPNFPROFILE命令为当前NFS所属NF实例配置的“支持的NF类型”的优先级，如果对NFS实例配置本参数，则NFS实例所归属的NF实例的“支持的NF类型”相关配置将失效。 |
| 服务实例状态  | 本参数用于指定NFS实例状态。                                                                                                                                                              |
| 域名      | 本参数用于指定服务实例的域名。本参数指定的域名中可以不包含PLMN信息，主要用于本网内的域名查询场景。                                                                                                                          |
| PLMN间域名 | 本参数用于指定服务实例的PLMN间域名。当NF涉及跨PLMN网络间的NFS发现时，需要为NFS配置“PLMN间域名”。                                                                                                                  |
| API路径前缀 | 本参数用于指定服务实例的API路径前缀。以满足特殊场景下其他NF以API root路径直接访问该NFS。                                                                                                                         |
| 优先级     | 本参数用于指定服务实例的优先级（与其他同类型NF实例的NFS相比）。在NF选择过程中，NF会选择高优先级的NFS，如果两个或多个NFS的优先级一样，NF则会根据“容量”做进一步的判断。                                                                                 |
| 容量      | 本参数用于指定NFS的相对权重（与其他同类型NF实例的NFS相比）。特别地，如果NFS容量的绝对值不超过本参数的取值范围，那么本参数可以直接取用容量绝对值。例如AMF可接入的用户数是50000，那么该AMF的容量就可以用50000表示。                                                       |
| 负载      | 本参数用于指定服务实例的负载。                                                                                                                                                              |
| 支持功能    | 本参数用于指定服务实例支持的功能。为后续版本预留使用。                                                                                                                                                  |
| Scheme  | 该参数用于指定服务实例的Scheme。                                                                                                                                                          |