# 增加NF支持的网络切片（ADD NFNS）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：AMF、SMF、NSSF、CBC、CBCF**

该命令用以给指定的NF增加其所支持的网络切片。

## 注意事项

- 该命令执行后立即生效。

- 当切片的NF类型为SMF时，需要通过命令ADD NSDNN添加对应的DNN，否则可能导致NF在NRF上注册或更新失败（NRF会严格检查切片下是否有DNN存在）。
- 如果启用了AMF与NSSF之间的网络切片可用性流程（NSSELPARA参数SYNSW设置为ON），那么当AMF新增支持网络切片，或者删除当前已支持的网络切片后，需要手工执行OPR NSAVLINFO向NSSF同步本AMF的网络切片可用性信息。

- 最多可输入8192条记录。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|:-------|:-------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NFTYPE | NF类型   | 可选必选说明：必选参数  参数含义：该参数用于表示NF类型。  数据来源：本端规划 取值范围： “NfInvalid（NfInvalid）”：无效的NF“NfNRF（NfNRF）”：NRF“NfUDM（NfUDM）”：UDM“NfAMF（NfAMF）”：AMF“NfSMF（NfSMF）”：SMF“NfAUSF（NfAUSF）”：AUSF“NfNEF（NfNEF）”：NEF“NfPCF（NfPCF）”：PCF“NfSMSF（NfSMSF）”：SMSF“NfNSSF（NfNSSF）”：NSSF“NfUDR（NfUDR）”：UDR“NfLMF（NfLMF）”：LMF“NfGMLC（NfGMLC）”：GMLC“Nf5G_EIR（Nf5G_EIR）”：5G_EIR“NfSEPP（NfSEPP）”：SEPP“NfUPF（NfUPF）”：UPF“NfN3IWF（NfN3IWF）”：N3IWF“NfAF（NfAF）”：AF“NfUDSF（NfUDSF）”：UDSF“NfBSF（NfBSF）”：BSF“NfCHF（NfCHF）”：CHF“NfNWDAF（NfNWDAF）”：NWDAF“NfTypeMAX（NfTypeMAX）”：NfTypeMAX“NfMBSMF（NfMBSMF）”：MBSMF“NfCBCF（NfCBCF）”：NfCBCF“NfSCF（NfSCF）”：NfSCF“NfSPF（NfSPF）”：NfSPF  默认值：无  配置原则：无 |
| NSIDX  | 网络切片索引 | 可选必选说明：必选参数  参数含义：该参数在系统中唯一标识某个网络切片。  数据来源：本端规划  取值范围：整数类型，取值范围是0~4294967295。本参数通过ADD PLMNNS命令进行配置。  默认值：无  配置原则：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| DESC   | 描述信息   | 可选必选说明：可选参数  参数含义：该参数表示对网络切片的描述信息。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是0~32。  默认值：无  配置原则：  输入单空格将删除该参数已有配置项。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

## 使用实例

AMF增加支持URLLC切片（索引值为11），执行如下命令：

```
ADD NFNS: NFTYPE=NfAMF, NSIDX=11, DESC="add urllc ns for amf";
```