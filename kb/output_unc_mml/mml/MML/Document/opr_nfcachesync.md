# 操作远端NF缓存同步（OPR NFCACHESYNC）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**须知** 

该命令会根据输入远端NF实例标识尝试构建缓存，新缓存构建成功可能会影响后续对应业务的网元选择。

**适用NF：AMF、SMF、NCG、CBC、CBCF**

该命令用于从NRF获得指定的远端NF信息并构建到缓存数据中。如果本端缓存数据缺失或希望更新缓存中某一网元数据时可以执行该命令。

## 注意事项

- 该命令执行后立即生效。

- 该命令执行结果可利用DSP NFCACHE命令核查，若执行5分钟后未查询到结果，则该目标NF的缓存同步失败。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识         | 参数名称     | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|:-------------|:---------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NFID         | 对端NF实例标识 | 可选必选说明：必选参数  参数含义：该参数用于指定目标NF实例标识，通过该NF实例标识向远端NRF进行服务发现，并根据返回结果构建对应的缓存。  数据来源：本端规划  取值范围：字符串类型，输入长度是36。  默认值：无  配置原则：  该处需以该目标NF在NRF上注册的实例标识为准。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| TARGETNFTYPE | 目标NF类型   | 可选必选说明：必选参数  参数含义：该参数用于指定目标NF类型，作为远端服务发现参数。  数据来源：本端规划 取值范围： “NfNRF（NfNRF）”：NfNRF“NfUDM（NfUDM）”：NfUDM“NfAMF（NfAMF）”：NfAMF“NfSMF（NfSMF）”：NfSMF“NfAUSF（NfAUSF）”：NfAUSF“NfNEF（NfNEF）”：NfNEF“NfPCF（NfPCF）”：NfPCF“NfSMSF（NfSMSF）”：NfSMSF“NfNSSF（NfNSSF）”：NfNSSF“NfUDR（NfUDR）”：NfUDR“NfLMF（NfLMF）”：NfLMF“NfGMLC（NfGMLC）”：NfGMLC“Nf5G_EIR（Nf5G_EIR）”：Nf5G_EIR“NfSEPP（NfSEPP）”：NfSEPP“NfUPF（NfUPF）”：NfUPF“NfN3IWF（NfN3IWF）”：NfN3IWF“NfAF（NfAF）”：NfAF“NfUDSF（NfUDSF）”：NfUDSF“NfBSF（NfBSF）”：NfBSF“NfCHF（NfCHF）”：NfCHF“NfCUSTOM_OCS（NfCUSTOM_OCS）”：NfCUSTOM_OCS“NfSCP（NfSCP）”：NfSCP“NfPCSCF（NfPCSCF）”：NfPCSCF“NfMBSMF（NfMBSMF）”：NfMBSMF“NWDAF（NWDAF）”：NWDAF  默认值：无  配置原则：无 |
| REQNFTYPE    | 本端NF类型   | 可选必选说明：必选参数  参数含义：该参数用于指定本端NF类型，作为远端服务发现参数。  数据来源：本端规划 取值范围： “NfNRF（NfNRF）”：NfNRF“NfUDM（NfUDM）”：NfUDM“NfAMF（NfAMF）”：NfAMF“NfSMF（NfSMF）”：NfSMF“NfAUSF（NfAUSF）”：NfAUSF“NfNEF（NfNEF）”：NfNEF“NfPCF（NfPCF）”：NfPCF“NfSMSF（NfSMSF）”：NfSMSF“NfNSSF（NfNSSF）”：NfNSSF“NfUDR（NfUDR）”：NfUDR“NfLMF（NfLMF）”：NfLMF“NfGMLC（NfGMLC）”：NfGMLC“Nf5G_EIR（Nf5G_EIR）”：Nf5G_EIR“NfSEPP（NfSEPP）”：NfSEPP“NfUPF（NfUPF）”：NfUPF“NfN3IWF（NfN3IWF）”：NfN3IWF“NfAF（NfAF）”：NfAF“NfUDSF（NfUDSF）”：NfUDSF“NfBSF（NfBSF）”：NfBSF“NfCHF（NfCHF）”：NfCHF“NfCUSTOM_OCS（NfCUSTOM_OCS）”：NfCUSTOM_OCS“NfSCP（NfSCP）”：NfSCP“NfPCSCF（NfPCSCF）”：NfPCSCF“NfMBSMF（NfMBSMF）”：NfMBSMF“NWDAF（NWDAF）”：NWDAF  默认值：无  配置原则：无 |
| PLMN         | 目标方PLMN  | 可选必选说明：可选参数  参数含义：该参数用于指定待查询NF所在的PLMN。  数据来源：全网规划  取值范围：字符串类型，输入长度范围是5~6。  默认值：无  配置原则：  PLMN由MCC和MNC组成，MCC为3个十进制数字，MNC为2~3个十进制数字。例如PLMN=“12345”，其中MCC=“123”， MNC=“45”。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| REQPLMN      | 请求方PLMN  | 可选必选说明：可选参数  参数含义：该参数用于指定查询NF所在的PLMN。  数据来源：全网规划  取值范围：字符串类型，输入长度范围是5~6。  默认值：无  配置原则：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |

## 使用实例

如果本端缓存数据缺失或希望更新缓存中某一网元数据时，假设本端网元类型为SMF，目标网元类型为AMF，目标网元ID为“00000000-0000-0000-0000-000000000001”

```
OPR NFCACHESYNC:NFID="00000000-0000-0000-0000-000000000001",TARGETNFTYPE=NfAMF,REQNFTYPE=NfSMF;
```