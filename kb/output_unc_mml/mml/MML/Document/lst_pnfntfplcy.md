# 查询对端网元的通知抑制时间（LST PNFNTFPLCY）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：AMF、SMF、SMSF、CBC、CBCF**

该命令用于查询对端网元的通知抑制时间。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|:-------|:-------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NFTYPE | NF类型   | 可选必选说明：可选参数  参数含义：该参数用于指定NF类型。  数据来源：全网规划 取值范围： “NfInvalid（NfInvalid）”：NfInvalid“NfNRF（NfNRF）”：NfNRF“NfUDM（NfUDM）”：NfUDM“NfAMF（NfAMF）”：NfAMF“NfSMF（NfSMF）”：NfSMF“NfAUSF（NfAUSF）”：NfAUSF“NfNEF（NfNEF）”：NfNEF“NfPCF（NfPCF）”：NfPCF“NfSMSF（NfSMSF）”：NfSMSF“NfNSSF（NfNSSF）”：NfNSSF“NfUDR（NfUDR）”：NfUDR“NfLMF（NfLMF）”：NfLMF“NfGMLC（NfGMLC）”：NfGMLC“Nf5G_EIR（Nf5G_EIR）”：Nf5G_EIR“NfSEPP（NfSEPP）”：NfSEPP“NfUPF（NfUPF）”：NfUPF“NfN3IWF（NfN3IWF）”：NfN3IWF“NfAF（NfAF）”：NfAF“NfUDSF（NfUDSF）”：NfUDSF“NfBSF（NfBSF）”：NfBSF“NfCHF（NfCHF）”：NfCHF“NfCUSTOM_OCS（NfCUSTOM_OCS）”：NfCUSTOM_OCS“NfSCP（NfSCP）”：NfSCP“NfPCSCF（NfPCSCF）”：NfPCSCF“NfMBSMF（NfMBSMF）”：NfMBSMF“NfUDN（NfUDN）”：NfUDN“NfNWDAF（NfNWDAF）”：NfNWDAF“NfSCF（NfSCF）”：NfSCF“NfKMC（NfKMC）”：NfKMC  默认值：无  配置原则：无 |

## 使用实例

查询对端网元SMF的通知抑制时间。

```
%%LST PNFNTFPLCY: NFTYPE=NfSMF;%%
RETCODE = 0 操作成功

结果如下
--------
              网元类型 = NfSMF
          通知抑制时间(分钟) = 10
（结果个数 = 1）

----  END
```

## 输出结果说明

| 输出项名称      | 输出项解释                           |
|:-----------|:--------------------------------|
| NF类型       | 该参数用于指定NF类型。                    |
| 通知抑制时间(分钟) | 参数用于指定向本端NF通知对端NF状态变更的抑制时间(分钟)。 |