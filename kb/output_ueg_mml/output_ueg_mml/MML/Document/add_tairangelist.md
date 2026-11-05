# 增加NF TAI区域信息（ADD TAIRANGELIST）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：AMF、SMF、NRF、NSSF、SMSF、NCG、NEF、NWDAF、SCF**

该命令用于添加NF实例支持的TAI信息。

- 当NF实例只支持为某些TAI服务时，需要对支持的TAI进行配置。
- 当SMF向NRF注册时，如果BINDSMFINFOID不为空或者“null”，则必须在ADD SMFINFOEXT中配置ID与BINDSMFINFOID相同的记录，否则该命令将不生效。
- 当NWDAF向NRF注册时，如果BINDNWDAFINFOID不为空或者“null”，则必须在ADD NWDAFINFOEXT中配置ID与BINDNWDAFINFOID相同的记录，否则该命令将不生效。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入2048条记录。
- 当NF类型为SMF时，TAC号段需要精确配置。如果配置成通用号段，如000000~FFFFFF，注册到NRF后，消费者NF带着TAI参数（此TAI在通用号段内，但是不在此SMF支持的号段内）到NRF进行服务发现时，此SMF也会被返回。这样可能会导致消费者NF选错SMF，业务流程达不到预期。

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

运营商A需要给NF实例名称为SMF\_Instance\_0，类型为NfSMF的NF实例增加MCC为460，MNC为01，TACRANGEINDEX为0的TAI区域。

```
ADD TAIRANGELIST: NFINSTANCENAME="SMF_Instance_0", NFTYPE=NfSMF, MCC="460", MNC="01", TACRANGEINDEX=0;
```