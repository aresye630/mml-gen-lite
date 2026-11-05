# 删除NF类型白名单（RMV NFTYPEWHITELIST）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**须知** 

该命令与SET NFTYPEWLST配合使用，当NF类型被从白名单中删除且NF类型白名单开关打开时被删除的NF类型将无法正常注册、去注册，更新以及维持到NRF的心跳。

**适用NF：NRF**

该命令用于删除NF类型白名单内的NF类型。白名单设置用于支撑NRF可以对不同NF类型进行区别处理，避免新升级NRF未经功能验证完善后就接入业务，导致错误业务导流。

该命令与NF白名单开关SET NFTYPEWLSW配合使用，当NF类型被从白名单中删除且NF类型白名单开关打开时被删除的NF类型将无法正常注册、去注册，更新以及维持到NRF的心跳。

## 注意事项

该命令执行后立即生效。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|:-------|:-------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NFTYPE | NF类型   | 可选必选说明：必选参数  参数含义：该参数用于表示需要增加到白名单中的NF类型。  数据来源：本端规划 取值范围： NRF（NRF）UDM（UDM）AMF（AMF）SMF（SMF）AUSF（AUSF）NEF（NEF）PCF（PCF）SMSF（SMSF）NSSF（NSSF）UDR（UDR）LMF（LMF）GMLC（GMLC）EIR_5G（EIR_5G）SEPP（SEPP）UPF（UPF）N3IWF（N3IWF）AF（AF）USDSF（USDSF）BSF（BSF）CHF（CHF）NWDAF（NWDAF）PCSCF（PCSCF）CUSTOM_OCS（CUSTOM_OCS）SCP（SCP）DRA（DRA）CBCF（CBCF）HSS（HSS）UCMF（UCMF）SOR_AF（SOR_AF）SPAF（SPAF）MME（MME）SCSAS（SCSAS）SCEF（SCEF）NSSAAF（NSSAAF）ICSCF（ICSCF）SCSCF（SCSCF）IMS_AS（IMS_AS）AANF（AANF）DDNMF_5G（DDNMF_5G）NSACF（NSACF）MFAF（MFAF）EASDF（EASDF）DCCF（DCCF）MB_SMF（MB_SMF）TSCTSF（TSCTSF）ADRF（ADRF）GBA_BSF（GBA_BSF）CEF（CEF）MB_UPF（MB_UPF）NSWOF（NSWOF）PKMF（PKMF）MNPF（MNPF）SMS_GMSC（SMS_GMSC）SMS_IWMSC（SMS_IWMSC）MBSF（MBSF）MBSTF（MBSTF）UDN（UDN）PANF（PANF）DCSF（DCSF）MRF（MRF）MRFP（MRFP）DCMF（DCMF）  默认值：无  配置原则：无 |

## 使用实例

删除NF类型为AMF的白名单记录，执行如下命令：

```
RMV NFTYPEWHITELIST: NFTYPE="AMF";
```