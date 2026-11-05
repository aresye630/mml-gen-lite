# 增加网元服务发现功能管理参数（ADD NFDISCMGMTPARA）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：AMF、SMF、NCG、SMSF、CBC、CBCF**

该命令用于增加网元服务发现功能管理参数。以NFType为粒度配置不同的服务发现匹配策略。

## 注意事项

- 该命令执行后立即生效。

- 当AMF的TAI精细化选择开关打开时，不允许将AMF的“TAI上报策略”配置为TAIRANGELIST和TAIRANGELISTFIRST。否则同一AMF Pool内TAI Range最小的AMF总是会被优先选择，可能导致用户分布不均。AMF的"TAI上报策略"开关通过LST AMFPROFILEPLCY命令查询TAIPPTPLCY参数来获取。需要结合实际业务情况，决策AMF的“TAI精细化选择开关”和“TAI上报策略”的配置选择。
- 同时开启SUPI精细化选择功能与GPSI精细化选择功能时，SUPI精细化选择功能优先级高于GPSI精细化选择功能。

- 最多可输入23条记录。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识           | 参数名称        | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
|:---------------|:------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NFTYPE         | 网元类型        | 可选必选说明：必选参数  参数含义：该参数用于指定目标NF类型。  数据来源：本端规划 取值范围： “NfNRF（NfNRF）”：NfNRF“NfUDM（NfUDM）”：NfUDM“NfAMF（NfAMF）”：NfAMF“NfSMF（NfSMF）”：NfSMF“NfAUSF（NfAUSF）”：NfAUSF“NfNEF（NfNEF）”：NfNEF“NfPCF（NfPCF）”：NfPCF“NfSMSF（NfSMSF）”：NfSMSF“NfNSSF（NfNSSF）”：NfNSSF“NfUDR（NfUDR）”：NfUDR“NfLMF（NfLMF）”：NfLMF“NfGMLC（NfGMLC）”：NfGMLC“Nf5G_EIR（Nf5G_EIR）”：Nf5G_EIR“NfSEPP（NfSEPP）”：NfSEPP“NfUPF（NfUPF）”：NfUPF“NfN3IWF（NfN3IWF）”：NfN3IWF“NfAF（NfAF）”：NfAF“NfUDSF（NfUDSF）”：NfUDSF“NfBSF（NfBSF）”：NfBSF“NfCHF（NfCHF）”：NfCHF“NfCUSTOM_OCS（NfCUSTOM_OCS）”：NfCUSTOM_OCS“NfSCP（NfSCP）”：NfSCP“NfPCSCF（NfPCSCF）”：NfPCSCF“NfMBSMF（NfMBSMF）”：NfMBSMF“NWDAF（NWDAF）”：NWDAF  默认值：无  配置原则：无 |
| TAIRANGESELSW  | TAI精细化选择开关  | 可选必选说明：该参数在"NFTYPE"配置为"NfAMF"、"NfSMF"时为条件可选参数。  参数含义：该参数用于指定服务发现过程中是否开启TAI精细化选择功能。若开关设置为ON时，服务发现会优选TAI区间更精细的网元。若开关设置为OFF时，服务发现不开启TAI精细化选择功能。精细化选择功能仅作用于本地配置命中或者缓存命中的服务发现结果。顺序在优先级选择功能在之后，在本大区locality优选之前。  数据来源：本端规划 取值范围： “OFF（OFF）”：功能关闭“ON（ON）”：功能开启  默认值：无  配置原则：无                                                                                                                                                                                                                                                                                                                                                                              |
| SUPIRANGESELSW | SUPI精细化选择开关 | 可选必选说明：该参数在"NFTYPE"配置为"NfUDM"、"NfAUSF"、"NfPCF"、"NfCHF"、"NfCUSTOM_OCS"时为条件可选参数。  参数含义：该参数用于指定服务发现过程中是否开启SUPI精细化选择功能。若开关设置为ON时，服务发现会优选SUPI区间更精细的网元。若开关设置为OFF时，服务发现不开启SUPI精细化选择功能。精细化选择功能仅作用于本地配置命中或者缓存命中的服务发现结果。顺序在优先级选择功能在之后，在本大区locality优选之前。  数据来源：本端规划 取值范围： “OFF（OFF）”：功能关闭“ON（ON）”：功能开启  默认值：无  配置原则：无                                                                                                                                                                                                                                                                                                                                           |
| GPSIRANGESELSW | GPSI精细化选择开关 | 可选必选说明：该参数在"NFTYPE"配置为"NfUDM"、"NfNEF"、"NfPCF"、"NfCHF"、"NfCUSTOM_OCS"时为条件可选参数。  参数含义：该参数用于指定服务发现过程中是否开启GPSI精细化选择功能。若开关设置为ON时，服务发现会优选GPSI区间更精细的网元。若开关设置为OFF时，服务发现不开启GPSI精细化选择功能。精细化选择功能仅作用于本地配置命中或者缓存命中的服务发现结果。顺序在优先级选择功能在之后，在本大区locality优选之前。  数据来源：本端规划 取值范围： “OFF（OFF）”：功能关闭“ON（ON）”：功能开启  默认值：无  配置原则：无                                                                                                                                                                                                                                                                                                                                            |

## 使用实例

- 服务发现AMF时，开启TAI精细化选择功能。

  ```
  ADD NFDISCMGMTPARA:NFTYPE=NfAMF,TAIRANGESELSW=ON;
  ```
- 服务发现UDM时，开启SUPI精细化选择功能。

  ```
  ADD NFDISCMGMTPARA:NFTYPE=NfUDM,SUPIRANGESELSW=ON,GPSIRANGESELSW=OFF;
  ```
- 服务发现PCF时，同时开启SUPI和GPSI的精细化选择功能。

  ```
  ADD NFDISCMGMTPARA:NFTYPE=NfPCF,SUPIRANGESELSW=ON,GPSIRANGESELSW=ON;
  ```