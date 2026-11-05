# 删除NF TAI区域信息（RMV TAIRANGELIST）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：AMF、SMF、NRF、NSSF、SMSF、NCG、CBC、CBCF**

该命令用于删除NF实例的TAI信息。当NF实例不再支持为某个TAI服务时，需要对TAI进行删除。当删除完一个NFINSTANCE关联的所有的NFTAI和TAIRANGELIST后，该NF将会通配支持所有TAI。

## 注意事项

- 该命令执行后立即生效。

- 当不输入BINDSMFINFOID时，将删除所有与NFINSTANCENAME，NFTYPE，MCC，MNC，TACRANGEINDEX匹配的配置。
- 当期望精确删除某一条配置时，BINDSMFINFOID不能为空。
- 这个命令执行后，建议提醒实时ACT NFUPDATE: 否则无法实时更新所支持的tac

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识            | 参数名称            | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|:----------------|:----------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NFINSTANCENAME  | NF实例名称          | 可选必选说明：必选参数  参数含义：本参数用于指定NF实例名称。  数据来源：全网规划  取值范围：字符串类型，输入长度范围是0~50。  默认值：无  配置原则：  本参数需要与ADD NFUUID命令中的NFINSTANCENAME值保持一致。                                                                                                                                                                                                                                                                                                                             |
| NFTYPE          | NF类型            | 可选必选说明：必选参数  参数含义：本参数用于指定NF类型。  数据来源：全网规划 取值范围： NfInvalid（NfInvalid）NfNRF（NfNRF）NfUDM（NfUDM）NfAMF（NfAMF）NfSMF（NfSMF）NfAUSF（NfAUSF）NfNEF（NfNEF）NfPCF（NfPCF）NfSMSF（NfSMSF）NfNSSF（NfNSSF）NfUDR（NfUDR）NfLMF（NfLMF）NfGMLC（NfGMLC）Nf5G_EIR（Nf5G_EIR）NfSEPP（NfSEPP）NfUPF（NfUPF）NfN3IWF（NfN3IWF）NfAF（NfAF）NfUDSF（NfUDSF）NfBSF（NfBSF）NfCHF（NfCHF）NfNWDAF（NfNWDAF）“NfTypeMAX（NfTypeMAX）”：已废弃。NfMBSMF（NfMBSMF）NfCBCF（NfCBCF）NfSCF（NfSCF）NfSPF（NfSPF）  默认值：无  配置原则：无 |
| MCC             | 移动国家代码          | 可选必选说明：必选参数  参数含义：本参数用于指定移动国家代码。  数据来源：全网规划  取值范围：字符串类型，输入长度是3。  默认值：无  配置原则：  本参数由3个十进制数字组成。                                                                                                                                                                                                                                                                                                                                                            |
| MNC             | 移动网号            | 可选必选说明：必选参数  参数含义：本参数用于指定移动网号。  数据来源：全网规划  取值范围：字符串类型，输入长度范围是2~3。  默认值：无  配置原则：  本参数由2~3个十进制数字组成。                                                                                                                                                                                                                                                                                                                                                        |
| TACRANGEINDEX   | TAC区域标识         | 可选必选说明：必选参数  参数含义：本参数用于指定TAC区域标识。  数据来源：全网规划  取值范围：整数类型，取值范围是0~2047。  默认值：无  配置原则：  本参数与ADD TACRANGE命令中的INDEX值一致时生效。                                                                                                                                                                                                                                                                                                                                     |
| BINDSMFINFOID   | 绑定的SMFINFO ID   | 可选必选说明：可选参数  参数含义：该参数用于指定绑定的SMFINFOEXT记录。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是0~32。该参数大小写不敏感。  默认值：无  配置原则：  BINDSMFINFOID需要与SMFINFOEXT中的SMFINFOID一致。                                                                                                                                                                                                                                                                                                          |
| BINDNWDAFINFOID | 绑定的NWDAFINFO ID | 可选必选说明：可选参数  参数含义：该参数用于指定绑定的NWDAFINFOEXT记录。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是0~32。该参数大小写不敏感。  默认值：无  配置原则：  BINDNWDAFINFOID需要与NWDAFINFOEXT中的ID一致。                                                                                                                                                                                                                                                                                                           |

## 使用实例

运营商A需要在标识为SMF\_Instance\_0的NF实例下删除类型为NfSMF，MCC为460，MNC为01，TACRANGEINDEX为0的TAI区域。

```
RMV TAIRANGELIST: NFINSTANCENAME="SMF_Instance_0", NFTYPE=NfSMF, MCC="460", MNC="01", TACRANGEINDEX=0;
```