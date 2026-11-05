# 设置对端网元的通知抑制时间（SET PNFNTFPLCY）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：AMF、SMF、SMSF、CBC、CBCF**

对端NF状态频繁变更时，本端NF不需要频繁感知并处理，本命令用于抑制向本端NF通知对端NF状态变化的频率，配置通知对端NF状态变化的抑制时间。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

**说明** 

此处仅展示前20条初始记录值，您可以通过相关查询命令查看全部记录值。

| NFTYPE   |   NTFTIME |
|:---------|----------:|
| NfUDM    |         5 |
| NfSMF    |         2 |
| NfPCF    |         0 |
| NfSMSF   |         5 |
| NfCHF    |         0 |
| NfPCSCF  |         1 |
| NfNRF    |         0 |
| NfAMF    |         5 |
| NfAUSF   |         0 |
| NfNEF    |         0 |
| NfNSSF   |         0 |
| NfUDR    |         0 |
| NfLMF    |         0 |
| NfGMLC   |         0 |
| Nf5G_EIR |         5 |
| NfSEPP   |         0 |
| NfUPF    |         0 |
| NfN3IWF  |         0 |
| NfAF     |         0 |
| NfUDSF   |         0 |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识    | 参数名称       | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|:--------|:-----------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NFTYPE  | NF类型       | 可选必选说明：必选参数  参数含义：该参数用于指定NF类型。  数据来源：全网规划 取值范围： “NfInvalid（NfInvalid）”：NfInvalid“NfNRF（NfNRF）”：NfNRF“NfUDM（NfUDM）”：NfUDM“NfAMF（NfAMF）”：NfAMF“NfSMF（NfSMF）”：NfSMF“NfAUSF（NfAUSF）”：NfAUSF“NfNEF（NfNEF）”：NfNEF“NfPCF（NfPCF）”：NfPCF“NfSMSF（NfSMSF）”：NfSMSF“NfNSSF（NfNSSF）”：NfNSSF“NfUDR（NfUDR）”：NfUDR“NfLMF（NfLMF）”：NfLMF“NfGMLC（NfGMLC）”：NfGMLC“Nf5G_EIR（Nf5G_EIR）”：Nf5G_EIR“NfSEPP（NfSEPP）”：NfSEPP“NfUPF（NfUPF）”：NfUPF“NfN3IWF（NfN3IWF）”：NfN3IWF“NfAF（NfAF）”：NfAF“NfUDSF（NfUDSF）”：NfUDSF“NfBSF（NfBSF）”：NfBSF“NfCHF（NfCHF）”：NfCHF“NfCUSTOM_OCS（NfCUSTOM_OCS）”：NfCUSTOM_OCS“NfSCP（NfSCP）”：NfSCP“NfPCSCF（NfPCSCF）”：NfPCSCF“NfMBSMF（NfMBSMF）”：NfMBSMF“NfUDN（NfUDN）”：NfUDN“NfNWDAF（NfNWDAF）”：NfNWDAF“NfSCF（NfSCF）”：NfSCF“NfKMC（NfKMC）”：NfKMC  默认值：无。  配置原则：无 |
| NTFTIME | 通知抑制时间(分钟) | 可选必选说明：必选参数  参数含义：参数用于指定向本端NF通知对端NF状态变更的抑制时间(分钟)。  数据来源：本端规划  取值范围：整数类型，取值范围是0~4294967295，单位是分钟。  默认值：无。  配置原则：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |

## 使用实例

设置对端网元SMF状态变化满10分钟后才通知本端NF。

```
SET PNFNTFPLCY: NFTYPE=NfSMF, NTFTIME=10;
```