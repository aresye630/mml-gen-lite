# 增加对端NF的服务发现策略（ADD PNFDISCPLCY）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：AMF、SMF、NRF、NSSF、NCG、NEF、NWDAF、SCF**

该命令用于增加对端NF的服务发现策略。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入26条记录。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|:-------|:-------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NFTYPE | NF类型   | 可选必选说明：必选参数  参数含义：该参数用于指定对端NF类型。  数据来源：本端规划 取值范围： “NfInvalid（NfInvalid）”：NfInvalid“NfNRF（NfNRF）”：NfNRF“NfUDM（NfUDM）”：NfUDM“NfAMF（NfAMF）”：NfAMF“NfSMF（NfSMF）”：NfSMF“NfAUSF（NfAUSF）”：NfAUSF“NfNEF（NfNEF）”：NfNEF“NfPCF（NfPCF）”：NfPCF“NfSMSF（NfSMSF）”：NfSMSF“NfNSSF（NfNSSF）”：NfNSSF“NfUDR（NfUDR）”：NfUDR“NfLMF（NfLMF）”：NfLMF“NfGMLC（NfGMLC）”：NfGMLC“Nf5G_EIR（Nf5G_EIR）”：Nf5G_EIR“NfSEPP（NfSEPP）”：NfSEPP“NfUPF（NfUPF）”：NfUPF“NfN3IWF（NfN3IWF）”：NfN3IWF“NfAF（NfAF）”：NfAF“NfUDSF（NfUDSF）”：NfUDSF“NfBSF（NfBSF）”：NfBSF“NfCHF（NfCHF）”：NfCHF“NfCUSTOM_OCS（NfCUSTOM_OCS）”：NfCUSTOM_OCS“NfSCP（NfSCP）”：NfSCP“NfPCSCF（NfPCSCF）”：NfPCSCF“NfMBSMF（NfMBSMF）”：NfMBSMF“NfUDN（NfUDN）”：NfUDN“NfNWDAF（NfNWDAF）”：NfNWDAF  默认值：无  配置原则：无 |
| POLICY | 服务发现策略 | 可选必选说明：必选参数  参数含义：该参数用于指定服务发现策略。  数据来源：本端规划 取值范围： “LOCAL_FIRST（LOCAL_FIRST）”：本地优先，先从本地配置查找满足服务发现条件的网元，如没有命中服务发现条件则再去缓存查找（如果缓存功能关闭，则跳过此步），如仍无命中则再去NRF查找。“LOCAL_ONLY（LOCAL_ONLY）”：仅本地查找，只从本地配置查找。“REMOTE_ONLY（REMOTE_ONLY）”：仅远端查找，先在缓存查找（如果缓存功能关闭，则跳过此步），如没命中则再去NRF查找。“REMOTE_FIRST（REMOTE_FIRST）”：远端优先，先在缓存查找满足服务发现条件的网元（如果缓存功能关闭，则跳过此步），如没有命中服务发现条件则去NRF查找，如仍无命中再在本地配置查找。  默认值：无  配置原则：  本地和远端为互补或相互备份的关系，如果在某一策略下能在某一数据来源中找到匹配服务发现条件的网元，则此处不会在另一数据来源中再进行服务发现。  如果同时配置PNFDISCPLY和NFDISCPLCY，以PNFDISCPLY的服务发现策略为准。                                                                                                                                                                                              |

## 使用实例

添加对端NF的服务发现策略：NF类型为NfSMSF，POLICY为LOCAL\_FIRST。

```
ADD PNFDISCPLCY: NFTYPE=NfSMSF, POLICY=LOCAL_FIRST;
```