# 查询NF向NRF注册状态（DSP NFREGNRFSTATUS）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：AMF、SMF、NCG、NRF、NSSF、SMSF、CBC、CBCF**

查询NF向NRF注册状态。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

| 参数标识           | 参数名称   | 参数说明                                                                                |
|:---------------|:-------|:------------------------------------------------------------------------------------|
| NFINSTANCENAME | NF实例名称 | 可选必选说明：可选参数  参数含义：该参数用于显示NF实例名称。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是0~36。  默认值：无  配置原则：无 |

## 使用实例

查询NF向NRF注册状态。

```
%%DSP NFREGNRFSTATUS:;%%
RETCODE = 0  操作成功

结果如下
--------
  NF实例名称  =  AMF_Instance_0
      NF类型  =  NfAMF
 NRF实例名称  =  NRF_Instance_0
  NF注册状态  =  Success/Registered
注册成功时间  =  2024-08-25T04:53:07+08:00
注册失败原因  =  Normal
    失败次数  =  0
  重注册时间  =  NULL
(结果个数 = 1)

---    END
```

## 输出结果说明

| 输出项名称   | 输出项解释                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|:--------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NF实例名称  | 该参数用于显示NF实例名称。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| NF类型    | 该参数用于显示NF类型。 取值说明： “NfInvalid（NfInvalid）”：NfInvalid“NfNRF（NfNRF）”：NfNRF“NfUDM（NfUDM）”：NfUDM“NfAMF（NfAMF）”：NfAMF“NfSMF（NfSMF）”：NfSMF“NfAUSF（NfAUSF）”：NfAUSF“NfNEF（NfNEF）”：NfNEF“NfPCF（NfPCF）”：NfPCF“NfSMSF（NfSMSF）”：NfSMSF“NfNSSF（NfNSSF）”：NfNSSF“NfUDR（NfUDR）”：NfUDR“NfLMF（NfLMF）”：NfLMF“NfGMLC（NfGMLC）”：NfGMLC“Nf5G_EIR（Nf5G_EIR）”：Nf5G_EIR“NfSEPP（NfSEPP）”：NfSEPP“NfUPF（NfUPF）”：NfUPF“NfN3IWF（NfN3IWF）”：NfN3IWF“NfAF（NfAF）”：NfAF“NfUDSF（NfUDSF）”：NfUDSF“NfBSF（NfBSF）”：NfBSF“NfCHF（NfCHF）”：NfCHF“NfCUSTOM_OCS（NfCUSTOM_OCS）”：NfCUSTOM_OCS“NfSCP（NfSCP）”：NfSCP“NfPCSCF（NfPCSCF）”：NfPCSCF“NfMBSMF（NfMBSMF）”：NfMBSMF“NfUDN（NfUDN）”：NfUDN“NfNWDAF（NfNWDAF）”：NfNWDAF“NfSCF（NfSCF）”：NfSCF“NfKMC（NfKMC）”：NfKMC |
| NRF实例名称 | 该参数用于显示当前注册的NRF实例名称。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| NF注册状态  | 该参数用于显示NF的注册状态。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 注册成功时间  | 该参数用于显示NF成功的时间。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| 注册失败原因  | 该参数用于显示NF注册失败的原因。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| 失败次数    | 该参数用于显示向NRF连续注册失败的次数。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| 重注册时间   | 该参数用于显示下一次重新注册的时间。如果值为1970-01-01T08:00:00+08:00，则说明没有注册失败进行注册退避，可以忽略。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |