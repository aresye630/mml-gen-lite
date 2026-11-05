# 修改NF订阅条件（MOD SUBCONDITION）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：AMF、SMF、NRF、NSSF、SMSF、NCG、NEF、NWDAF、SCF**

该命令用于修改订阅的目标NF类型的订阅条件等信息。

## 注意事项

- 该命令执行后立即生效。

- 该命令只修改订阅条件，对于已经生成的订阅无法生效。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识          | 参数名称   | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|:--------------|:-------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NFTYPE        | NF类型   | 可选必选说明：必选参数  参数含义：该参数用于指定订阅的目标NF类型。  数据来源：本端规划 取值范围： “NfInvalid（NfInvalid）”：NfInvalid“NfNRF（NfNRF）”：NfNRF“NfUDM（NfUDM）”：NfUDM“NfAMF（NfAMF）”：NfAMF“NfSMF（NfSMF）”：NfSMF“NfAUSF（NfAUSF）”：NfAUSF“NfNEF（NfNEF）”：NfNEF“NfPCF（NfPCF）”：NfPCF“NfSMSF（NfSMSF）”：NfSMSF“NfNSSF（NfNSSF）”：NfNSSF“NfUDR（NfUDR）”：NfUDR“NfLMF（NfLMF）”：NfLMF“NfGMLC（NfGMLC）”：NfGMLC“Nf5G_EIR（Nf5G_EIR）”：Nf5G_EIR“NfSEPP（NfSEPP）”：NfSEPP“NfUPF（NfUPF）”：NfUPF“NfN3IWF（NfN3IWF）”：NfN3IWF“NfAF（NfAF）”：NfAF“NfUDSF（NfUDSF）”：NfUDSF“NfBSF（NfBSF）”：NfBSF“NfCHF（NfCHF）”：NfCHF“NfCUSTOM_OCS（NfCUSTOM_OCS）”：NfCUSTOM_OCS“NfSCP（NfSCP）”：NfSCP“NfPCSCF（NfPCSCF）”：NfPCSCF“NfMBSMF（NfMBSMF）”：NfMBSMF“NfUDN（NfUDN）”：NfUDN“NfNWDAF（NfNWDAF）”：NfNWDAF  默认值：无  配置原则：无 |
| CONDITION     | 订阅条件   | 可选必选说明：可选参数  参数含义：该参数用于指定订阅的条件类型。  数据来源：全网规划 取值范围： “NfInstanceId（NfInstanceId）”：NfInstanceId“NFType（NFType）”：NFType“ServiceName（ServiceName）”：ServiceName“AmfRegionId（AmfRegionId）”：AmfRegionId“AmfSetId（AmfSetId）”：AmfSetId“GuamiList（GuamiList）”：GuamiList“PlmnId（PlmnId）”：PlmnId“NetworkSlice（NetworkSlice）”：NetworkSlice“NfGroup（NfGroup）”：NfGroup“Rev1（Rev1）”：Rev1“Rev2（Rev2）”：Rev2“Rev3（Rev3）”：Rev3  默认值：无  配置原则： 推荐使用NfInstanceId-1或NFType-1。同一条命令勾选不同的订阅条件会生成多条订阅。不支持单独配置AmfSetId订阅，只支持AmfRegionId+AmfSetId组合或者单独AmfRegionId订阅。                                                                                                                                                                           |
| REQNOTIFEVENT | 通知事件   | 可选必选说明：可选参数  参数含义：该参数用于指定订阅的通知事件类型。  数据来源：对端协商 取值范围： “NF_REGISTERED（NF_REGISTERED）”：NF上线通知事件，当NF上线时，NRF会通知NF。“NF_DEREGISTERED（NF_DEREGISTERED）”：NF下线通知事件，当NF下线时，NRF会通知NF。“NF_PROFILE_CHANGED（NF_PROFILE_CHANGED）”：NF Profile变化通知事件，当NF Profile变化时，NRF会通知NF。  默认值：无  配置原则：  推荐使用NF_REGISTERED-1，NF_DEREGISTERED-1，NF_PROFILE_CHANGED-1。                                                                                                                                                                                                                                                                                                                                                                            |

## 使用实例

修改目标NF类型为NFAMF的订阅条件等信息，订阅条件修改为NF\_REGISTERED，通知事件修改为NfInstanceId。

```
MOD SUBCONDITION: NFTYPE=NfAMF, CONDITION=NfInstanceId-1&NFType-1&ServiceName-0&AmfRegionId-0&AmfSetId-0&GuamiList-0&PlmnId-0&NetworkSlice-0&NfGroup-0&Rev1-0&Rev2-0&Rev3-0, REQNOTIFEVENT=NF_REGISTERED-1&NF_DEREGISTERED-1&NF_PROFILE_CHANGED-1;
```