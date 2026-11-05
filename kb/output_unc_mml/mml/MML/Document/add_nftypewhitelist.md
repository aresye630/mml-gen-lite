# 增加NF类型白名单（ADD NFTYPEWHITELIST）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**须知** 

该命令与SET NFTYPEWLSW配合使用，在白名单未设置完成时请勿打开NF类型白名单开关，否则未加入到白名单中的NF将无法正常注册、去注册、更新及维持到NRF的心跳功能。

**适用NF：NRF**

该命令用于增加NF类型白名单内的NF类型。白名单设置用于支撑NRF可以对不同类型NF进行区别处理，避免新升级NRF未经功能验证完善后就接入业务，导致错误业务导流。

## 注意事项

- 该命令执行后立即生效。

- 该命令与NF类型白名单开关SET NFTYPEWLSW配合使用，在白名单未设置完成时请勿打开NF类型白名单开关，否则影响未加入到白名单中NF的正常注册、去注册、更新及心跳功能。

- 最多可输入256条记录。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|:-------|:-------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NFTYPE | NF类型   | 可选必选说明：必选参数  参数含义：该参数用于表示需要增加到白名单中的NF类型。  数据来源：本端规划 取值范围： NRF（NRF）UDM（UDM）AMF（AMF）SMF（SMF）AUSF（AUSF）NEF（NEF）PCF（PCF）SMSF（SMSF）NSSF（NSSF）UDR（UDR）LMF（LMF）GMLC（GMLC）EIR_5G（EIR_5G）SEPP（SEPP）UPF（UPF）N3IWF（N3IWF）AF（AF）USDSF（USDSF）BSF（BSF）CHF（CHF）NWDAF（NWDAF）PCSCF（PCSCF）CUSTOM_OCS（CUSTOM_OCS）SCP（SCP）DRA（DRA）CBCF（CBCF）HSS（HSS）UCMF（UCMF）SOR_AF（SOR_AF）SPAF（SPAF）MME（MME）SCSAS（SCSAS）SCEF（SCEF）NSSAAF（NSSAAF）ICSCF（ICSCF）SCSCF（SCSCF）IMS_AS（IMS_AS）AANF（AANF）DDNMF_5G（DDNMF_5G）NSACF（NSACF）MFAF（MFAF）EASDF（EASDF）DCCF（DCCF）MB_SMF（MB_SMF）TSCTSF（TSCTSF）ADRF（ADRF）GBA_BSF（GBA_BSF）CEF（CEF）MB_UPF（MB_UPF）NSWOF（NSWOF）PKMF（PKMF）MNPF（MNPF）SMS_GMSC（SMS_GMSC）SMS_IWMSC（SMS_IWMSC）MBSF（MBSF）MBSTF（MBSTF）UDN（UDN）PANF（PANF）DCSF（DCSF）MRF（MRF）MRFP（MRFP）DCMF（DCMF）  默认值：无  配置原则：无 |

## 使用实例

添加NF类型为AMF的白名单记录，执行如下命令：

```
ADD NFTYPEWHITELIST: NFTYPE="AMF";
```