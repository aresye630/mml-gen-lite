# 修改缓存更新策略（MOD CACHEUPDATEPLCY）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：AMF、SMF、NRF、NSSF、SMSF、NCG、CBC、CBCF**

该命令用于修改缓存更新策略。

## 注意事项

该命令执行后立即生效。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识           | 参数名称                | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|:---------------|:--------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PEERTYPE       | 对端NF类型              | 可选必选说明：必选参数  参数含义：该参数用于指定对端NF类型。  数据来源：本端规划 取值范围： “NfInvalid（NfInvalid）”：NfInvalid“NfNRF（NfNRF）”：NfNRF“NfUDM（NfUDM）”：NfUDM“NfAMF（NfAMF）”：NfAMF“NfSMF（NfSMF）”：NfSMF“NfAUSF（NfAUSF）”：NfAUSF“NfNEF（NfNEF）”：NfNEF“NfPCF（NfPCF）”：NfPCF“NfSMSF（NfSMSF）”：NfSMSF“NfNSSF（NfNSSF）”：NfNSSF“NfUDR（NfUDR）”：NfUDR“NfLMF（NfLMF）”：NfLMF“NfGMLC（NfGMLC）”：NfGMLC“Nf5G_EIR（Nf5G_EIR）”：Nf5G_EIR“NfSEPP（NfSEPP）”：NfSEPP“NfUPF（NfUPF）”：NfUPF“NfN3IWF（NfN3IWF）”：NfN3IWF“NfAF（NfAF）”：NfAF“NfUDSF（NfUDSF）”：NfUDSF“NfBSF（NfBSF）”：NfBSF“NfCHF（NfCHF）”：NfCHF“NfCUSTOM_OCS（NfCUSTOM_OCS）”：NfCUSTOM_OCS“NfSCP（NfSCP）”：NfSCP“NfPCSCF（NfPCSCF）”：NfPCSCF“NfMBSMF（NfMBSMF）”：NfMBSMF“NfUDN（NfUDN）”：NfUDN“NfNWDAF（NfNWDAF）”：NfNWDAF“NfSCF（NfSCF）”：NfSCF“NfKMC（NfKMC）”：NfKMC  默认值：无  配置原则：无 |
| LINKFAULTUPDSW | 链路全故障触发服务发现开关       | 可选必选说明：可选参数  参数含义：该参数用于设置当从缓存中发现的NF的链路全部故障时是否去NRF服务发现。  当开关置为SUPPRESS时，每个Pod每3分钟最多触发一次向NRF的重新服务发现； 当开关置为NOTSUPPRESS时，不抑制向NRF的重新服务发现； 当开关置为FORBIDDEN时，不触发向NRF的重新服务发现。  数据来源：本端规划 取值范围： SUPPRESS（抑制去NRF服务发现）NOTSUPPRESS（不抑制去NRF服务发现）FORBIDDEN（禁止去NRF服务发现）  默认值：无  配置原则：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| UNREGQRYSW     | 目标NF全为非注册态时触发服务发现开关 | 可选必选说明：可选参数  参数含义：该参数用于设置当从缓存中发现的NF全部为非注册状态时是否去NRF服务发现。  当开关置为SUPPRESS时，每个Pod每30秒最多触发一次向NRF的重新服务发现； 当开关置为NOTSUPPRESS时，不抑制向NRF的重新服务发现； 当开关置为FORBIDDEN时，不触发向NRF的重新服务发现。  数据来源：本端规划 取值范围： SUPPRESS（抑制去NRF服务发现）NOTSUPPRESS（不抑制去NRF服务发现）FORBIDDEN（禁止去NRF服务发现）  默认值：无  配置原则：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

## 使用实例

运营商A需要修改缓存更新策略，对端NF类型为OCS，链路全故障触发服务发现开关为“禁止去NRF服务发现”，目标NF全为非注册态时触发服务发现开关为“禁止去NRF服务发现”。

```
MOD CACHEUPDATEPLCY: PEERTYPE=NfCUSTOM_OCS, LINKFAULTUPDSW=FORBIDDEN, UNREGQRYSW=FORBIDDEN;
```