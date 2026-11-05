# 删除NF UUID信息（RMV NFUUID）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**须知** 

如果未执行ACT NFOFFLINE就执行该命令，可能导致不可预知的系统异常及重大业务影响。

**适用NF：AMF、SMF、NRF、NSSF、SMSF、NCG、NEF、NWDAF、CBCF、SCF、SPF**

该命令用于删除NF实例标识（UUID）。删除UUID可能导致NF无法和其他NF正常通信，请谨慎操作。

## 注意事项

- 该命令执行后立即生效。

- 当NFINSTANCENAME参数被AMFINFO，ALLOWEDNFDOMAIN，ALLOWEDNFNS，ALLOWEDPLMN，N2INFAMFINFO，NFPROFILE，NFSERVICE，NFSERVICEVER，NFSRVNTFSUBS，NFTAI，NSILIST，NFSRVSCOPE，TAIRANGELIST，BSFINFO，BSFIPRANGEBIND，SMFINFO命令关联时，不能执行此命令。
- 对于已经存在的NF实例，若要修改其NF实例标识，则必须在修改后通过RMV SBIAPLE和ADD SBIAPLE命令删除并重建链路集。重建链路集会导致所有链路短暂中断。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|:-------|:-------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NFTYPE | NF类型   | 可选必选说明：必选参数  参数含义：本参数用于指定NF类型。  数据来源：全网规划 取值范围： NfInvalid（NfInvalid）NfNRF（NfNRF）NfUDM（NfUDM）NfAMF（NfAMF）NfSMF（NfSMF）NfAUSF（NfAUSF）NfNEF（NfNEF）NfPCF（NfPCF）NfSMSF（NfSMSF）NfNSSF（NfNSSF）NfUDR（NfUDR）NfLMF（NfLMF）NfGMLC（NfGMLC）Nf5G_EIR（Nf5G_EIR）NfSEPP（NfSEPP）NfUPF（NfUPF）NfN3IWF（NfN3IWF）NfAF（NfAF）NfUDSF（NfUDSF）NfBSF（NfBSF）NfCHF（NfCHF）NfNWDAF（NfNWDAF）“NfTypeMAX（NfTypeMAX）”：已废弃。NfMBSMF（NfMBSMF）NfCBCF（NfCBCF）NfSCF（NfSCF）NfSPF（NfSPF）  默认值：无  配置原则：  仅可以选择网元支持的NF实例。 |

## 使用实例

运营商需要删除类型为NfAMF实例对应的NF实例标识。

```
RMV NFUUID: NFTYPE=NfAMF;
```