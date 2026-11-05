# 查询NF订阅条件（LST SUBCONDITION）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：AMF、SMF、NRF、NSSF、SMSF、NCG、NEF、NWDAF、SCF**

该命令用于查询订阅的目标NF的订阅条件等信息。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

| 参数标识   | 参数名称   | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|:-------|:-------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NFTYPE | NF类型   | 可选必选说明：可选参数  参数含义：该参数用于指定订阅的目标NF类型。  数据来源：本端规划 取值范围： “NfInvalid（NfInvalid）”：NfInvalid“NfNRF（NfNRF）”：NfNRF“NfUDM（NfUDM）”：NfUDM“NfAMF（NfAMF）”：NfAMF“NfSMF（NfSMF）”：NfSMF“NfAUSF（NfAUSF）”：NfAUSF“NfNEF（NfNEF）”：NfNEF“NfPCF（NfPCF）”：NfPCF“NfSMSF（NfSMSF）”：NfSMSF“NfNSSF（NfNSSF）”：NfNSSF“NfUDR（NfUDR）”：NfUDR“NfLMF（NfLMF）”：NfLMF“NfGMLC（NfGMLC）”：NfGMLC“Nf5G_EIR（Nf5G_EIR）”：Nf5G_EIR“NfSEPP（NfSEPP）”：NfSEPP“NfUPF（NfUPF）”：NfUPF“NfN3IWF（NfN3IWF）”：NfN3IWF“NfAF（NfAF）”：NfAF“NfUDSF（NfUDSF）”：NfUDSF“NfBSF（NfBSF）”：NfBSF“NfCHF（NfCHF）”：NfCHF“NfCUSTOM_OCS（NfCUSTOM_OCS）”：NfCUSTOM_OCS“NfSCP（NfSCP）”：NfSCP“NfPCSCF（NfPCSCF）”：NfPCSCF“NfMBSMF（NfMBSMF）”：NfMBSMF“NfUDN（NfUDN）”：NfUDN“NfNWDAF（NfNWDAF）”：NfNWDAF  默认值：无  配置原则：无 |

## 使用实例

查询目标NF类型为NFAMF的订阅信息。

```
%%LST SUBCONDITION:;%%
RETCODE = 0 操作成功

结果如下
---------
      NF类型 = NfAMF
    订阅条件 = NfInstanceId
    通知事件 = NF_REGISTERED
（结果个数 = 1）

----    END
```

## 输出结果说明

| 输出项名称   | 输出项解释             |
|:--------|:------------------|
| NF类型    | 该参数用于指定订阅的目标NF类型。 |
| 订阅条件    | 该参数用于指定订阅的条件类型。   |
| 通知事件    | 该参数用于指定订阅的通知事件类型。 |