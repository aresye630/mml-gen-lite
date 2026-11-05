# 删除基于NFType设置NRF的各类功能开关（RMV NRFNFTYPEFUNC）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：NRF**

删除NRF基于NFType设置NRF的各类功能开关。

## 注意事项

- 该命令执行后立即生效。

- 单独删除客户端类型时，服务端类型应配置为NULL。
- 单独删除服务端类型时，客户端类型应配置为NULL。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识          | 参数名称    | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|:--------------|:--------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| REQUESTNFTYPE | 客户端NF类型 | 可选必选说明：必选参数  参数含义：该参数用于表示客户端NF类型。  数据来源：本端规划 取值范围： “NULL（空值）”：NF类型为空值。“NRF（NRF）”：NF类型为NRF。“UDM（UDM）”：NF类型为UDM。“AMF（AMF）”：NF类型为AMF。“SMF（SMF）”：NF类型为SMF。“AUSF（AUSF）”：NF类型为AUSF。“NEF（NEF）”：NF类型为NEF。“PCF（PCF）”：NF类型为PCF。“SMSF（SMSF）”：NF类型为SMSF。“NSSF（NSSF）”：NF类型为NSSF。“UDR（UDR）”：NF类型为UDR。“LMF（LMF）”：NF类型为LMF。“GMLC（GMLC）”：NF类型为GMLC。“EIR_5G（5G_EIR）”：NF类型为5G_EIR。“SEPP（SEPP）”：NF类型为SEPP。“UPF（UPF）”：NF类型为UPF。“N3IWF（N3IWF）”：NF类型为N3IWF。“AF（AF）”：NF类型为AF。“UDSF（UDSF）”：NF类型为UDSF。“BSF（BSF）”：NF类型为BSF。“CHF（CHF）”：NF类型为CHF。“NWDAF（NWDAF）”：NF类型为NWDAF。“PCSCF（PCSCF）”：NF类型为PCSCF。“CUSTOM_OCS（CUSTOM_OCS）”：NF类型为CUSTOM_OCS。“SCP（SCP）”：NF类型为SCP。“DRA（DRA）”：NF类型为DRA。“CBCF（CBCF）”：NF类型为CBCF。“HSS（HSS）”：NF类型为HSS。“UCMF（UCMF）”：NF类型为UCMF。“SOR_AF（SOR_AF）”：NF类型为SOR_AF。“SPAF（SPAF）”：NF类型为SPAF。“MME（MME）”：NF类型为MME。“SCSAS（SCSAS）”：NF类型为SCSAS。“SCEF（SCEF）”：NF类型为SCEF。“NSSAAF（NSSAAF）”：NF类型为NSSAAF。“ICSCF（ICSCF）”：NF类型为ICSCF。“SCSCF（SCSCF）”：NF类型为SCSCF。“IMS_AS（IMS_AS）”：NF类型为IMS_AS。“AANF（AANF）”：NF类型为AANF。“DDNMF_5G（5G_DDNMF）”：NF类型为5G_DDNMF。“NSACF（NSACF）”：NF类型为NSACF。“MFAF（MFAF）”：NF类型为MFAF。“EASDF（EASDF）”：NF类型为EASDF。“DCCF（DCCF）”：NF类型为DCCF。“MB_SMF（MB_SMF）”：NF类型为MB_SMF。“TSCTSF（TSCTSF）”：NF类型为TSCTSF。“ADRF（ADRF）”：NF类型为ADRF。“GBA_BSF（GBA_BSF）”：NF类型为GBA_BSF。“CEF（CEF）”：NF类型为CEF。“MB_UPF（MB_UPF）”：NF类型为MB_UPF。“NSWOF（NSWOF）”：NF类型为NSWOF。“PKMF（PKMF）”：NF类型为PKMF。“MNPF（MNPF）”：NF类型为MNPF。“SMS_GMSC（SMS_GMSC）”：NF类型为SMS_GMSC。“SMS_IWMSC（SMS_IWMSC）”：NF类型为SMS_IWMSC。“MBSF（MBSF）”：NF类型为MBSF。“MBSTF（MBSTF）”：NF类型为MBSTF。“UDN（UDN ）”：NF类型为UDN 。“PANF（PANF）”：NF类型为PANF。“DCSF（DCSF）”：NF类型为DCSF。“MRF（MRF）”：NF类型为MRF。“MRFP（MRFP）”：NF类型为MRFP。“DCMF（DCMF）”：NF类型为DCMF。  默认值：无  配置原则： 客户端类型和服务端类型不能同时配置为NULL（空值）。多条配置冲突时优先级如下：服务端+客户端>服务端>客户端 |
| TARGETNFTYPE  | 服务端NF类型 | 可选必选说明：必选参数  参数含义：该参数用于表示服务端NF类型。  数据来源：本端规划 取值范围： “NULL（空值）”：NF类型为空值。“NRF（NRF）”：NF类型为NRF。“UDM（UDM）”：NF类型为UDM。“AMF（AMF）”：NF类型为AMF。“SMF（SMF）”：NF类型为SMF。“AUSF（AUSF）”：NF类型为AUSF。“NEF（NEF）”：NF类型为NEF。“PCF（PCF）”：NF类型为PCF。“SMSF（SMSF）”：NF类型为SMSF。“NSSF（NSSF）”：NF类型为NSSF。“UDR（UDR）”：NF类型为UDR。“LMF（LMF）”：NF类型为LMF。“GMLC（GMLC）”：NF类型为GMLC。“EIR_5G（5G_EIR）”：NF类型为5G_EIR。“SEPP（SEPP）”：NF类型为SEPP。“UPF（UPF）”：NF类型为UPF。“N3IWF（N3IWF）”：NF类型为N3IWF。“AF（AF）”：NF类型为AF。“UDSF（UDSF）”：NF类型为UDSF。“BSF（BSF）”：NF类型为BSF。“CHF（CHF）”：NF类型为CHF。“NWDAF（NWDAF）”：NF类型为NWDAF。“PCSCF（PCSCF）”：NF类型为PCSCF。“CUSTOM_OCS（CUSTOM_OCS）”：NF类型为CUSTOM_OCS。“SCP（SCP）”：NF类型为SCP。“DRA（DRA）”：NF类型为DRA。“CBCF（CBCF）”：NF类型为CBCF。“HSS（HSS）”：NF类型为HSS。“UCMF（UCMF）”：NF类型为UCMF。“SOR_AF（SOR_AF）”：NF类型为SOR_AF。“SPAF（SPAF）”：NF类型为SPAF。“MME（MME）”：NF类型为MME。“SCSAS（SCSAS）”：NF类型为SCSAS。“SCEF（SCEF）”：NF类型为SCEF。“NSSAAF（NSSAAF）”：NF类型为NSSAAF。“ICSCF（ICSCF）”：NF类型为ICSCF。“SCSCF（SCSCF）”：NF类型为SCSCF。“IMS_AS（IMS_AS）”：NF类型为IMS_AS。“AANF（AANF）”：NF类型为AANF。“DDNMF_5G（5G_DDNMF）”：NF类型为5G_DDNMF。“NSACF（NSACF）”：NF类型为NSACF。“MFAF（MFAF）”：NF类型为MFAF。“EASDF（EASDF）”：NF类型为EASDF。“DCCF（DCCF）”：NF类型为DCCF。“MB_SMF（MB_SMF）”：NF类型为MB_SMF。“TSCTSF（TSCTSF）”：NF类型为TSCTSF。“ADRF（ADRF）”：NF类型为ADRF。“GBA_BSF（GBA_BSF）”：NF类型为GBA_BSF。“CEF（CEF）”：NF类型为CEF。“MB_UPF（MB_UPF）”：NF类型为MB_UPF。“NSWOF（NSWOF）”：NF类型为NSWOF。“PKMF（PKMF）”：NF类型为PKMF。“MNPF（MNPF）”：NF类型为MNPF。“SMS_GMSC（SMS_GMSC）”：NF类型为SMS_GMSC。“SMS_IWMSC（SMS_IWMSC）”：NF类型为SMS_IWMSC。“MBSF（MBSF）”：NF类型为MBSF。“MBSTF（MBSTF）”：NF类型为MBSTF。“UDN（UDN ）”：NF类型为UDN 。“PANF（PANF）”：NF类型为PANF。“DCSF（DCSF）”：NF类型为DCSF。“MRF（MRF）”：NF类型为MRF。“MRFP（MRFP）”：NF类型为MRFP。“DCMF（DCMF）”：NF类型为DCMF。  默认值：无  配置原则： 客户端类型和服务端类型不能同时配置为NULL（空值）。多条配置冲突时优先级如下：服务端+客户端>服务端>客户端 |

## 使用实例

运营商通过此命令删除基于NFType设置NRF的各类功能：设置客户端NF类型为AMF；服务端NF类型为UDM。

```
RMV NRFNFTYPEFUNC: REQUESTNFTYPE=AMF, TARGETNFTYPE=UDM;
```