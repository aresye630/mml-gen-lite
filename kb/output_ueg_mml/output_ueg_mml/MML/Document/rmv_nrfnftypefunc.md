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

| 参数标识          | 参数名称    | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|:--------------|:--------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| REQUESTNFTYPE | 客户端NF类型 | 可选必选说明：必选参数  参数含义：该参数用于表示客户端NF类型。  数据来源：本端规划 取值范围： NULL（空值）NRF（NRF）UDM（UDM）AMF（AMF）SMF（SMF）AUSF（AUSF）NEF（NEF）PCF（PCF）SMSF（SMSF）NSSF（NSSF）UDR（UDR）LMF（LMF）GMLC（GMLC）EIR_5G（5G_EIR）SEPP（SEPP）UPF（UPF）N3IWF（N3IWF）AF（AF）UDSF（UDSF）BSF（BSF）CHF（CHF）NWDAF（NWDAF）PCSCF（PCSCF）CUSTOM_OCS（CUSTOM_OCS）SCP（SCP）DRA（DRA）CBCF（CBCF）HSS（HSS）UCMF（UCMF）SOR_AF（SOR_AF）SPAF（SPAF）MME（MME）SCSAS（SCSAS）SCEF（SCEF）NSSAAF（NSSAAF）ICSCF（ICSCF）SCSCF（SCSCF）IMS_AS（IMS_AS）AANF（AANF）DDNMF_5G（5G_DDNMF）NSACF（NSACF）MFAF（MFAF）EASDF（EASDF）DCCF（DCCF）MB_SMF（MB_SMF）TSCTSF（TSCTSF）ADRF（ADRF）GBA_BSF（GBA_BSF）CEF（CEF）MB_UPF（MB_UPF）NSWOF（NSWOF）PKMF（PKMF）MNPF（MNPF）SMS_GMSC（SMS_GMSC）SMS_IWMSC（SMS_IWMSC）MBSF（MBSF）MBSTF（MBSTF）UDN（UDN ）PANF（PANF）DCSF（DCSF）MRF（MRF）MRFP（MRFP ）DCMF（DCMF）  默认值：无  配置原则：  客户端类型和服务端类型不能同时配置为NULL。  多条配置冲突时优先级如下：服务端+客户端>服务端>客户端。 |
| TARGETNFTYPE  | 服务端NF类型 | 可选必选说明：必选参数  参数含义：该参数用于表示服务端NF类型。  数据来源：本端规划 取值范围： NULL（空值）NRF（NRF）UDM（UDM）AMF（AMF）SMF（SMF）AUSF（AUSF）NEF（NEF）PCF（PCF）SMSF（SMSF）NSSF（NSSF）UDR（UDR）LMF（LMF）GMLC（GMLC）EIR_5G（5G_EIR）SEPP（SEPP）UPF（UPF）N3IWF（N3IWF）AF（AF）UDSF（UDSF）BSF（BSF）CHF（CHF）NWDAF（NWDAF）PCSCF（PCSCF）CUSTOM_OCS（CUSTOM_OCS）SCP（SCP）DRA（DRA）CBCF（CBCF）HSS（HSS）UCMF（UCMF）SOR_AF（SOR_AF）SPAF（SPAF）MME（MME）SCSAS（SCSAS）SCEF（SCEF）NSSAAF（NSSAAF）ICSCF（ICSCF）SCSCF（SCSCF）IMS_AS（IMS_AS）AANF（AANF）DDNMF_5G（5G_DDNMF）NSACF（NSACF）MFAF（MFAF）EASDF（EASDF）DCCF（DCCF）MB_SMF（MB_SMF）TSCTSF（TSCTSF）ADRF（ADRF）GBA_BSF（GBA_BSF）CEF（CEF）MB_UPF（MB_UPF）NSWOF（NSWOF）PKMF（PKMF）MNPF（MNPF）SMS_GMSC（SMS_GMSC）SMS_IWMSC（SMS_IWMSC）MBSF（MBSF）MBSTF（MBSTF）UDN（UDN ）PANF（PANF）DCSF（DCSF）MRF（MRF）MRFP（MRFP ）DCMF（DCMF）  默认值：无  配置原则：  客户端类型和服务端类型不能同时配置为NULL。  多条配置冲突时优先级如下：服务端+客户端>服务端>客户端。 |

## 使用实例

运营商通过此命令删除基于NFType设置NRF的各类功能：设置客户端NF类型为AMF；服务端NF类型为UDM。

```
RMV NRFNFTYPEFUNC: REQUESTNFTYPE=AMF, TARGETNFTYPE=UDM;
```