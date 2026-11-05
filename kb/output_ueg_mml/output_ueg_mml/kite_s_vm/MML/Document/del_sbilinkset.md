# 删除服务化接口链路集（DEL SBILINKSET）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**须知** 

该命令用于删除SBI链路集，删除对应链路集后，可能会导致该链路集上业务受损。

该命令用于删除SBI链路集。

## 注意事项

- 该命令执行后立即生效。

- 该命令用于删除SBI链路集，删除对应链路集后，可能会导致该链路集上业务受损。该操作会清除所有被删除的链路集已上报的告警。
- 两个输入参数至少需要填写其中一个。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识       | 参数名称   | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|:-----------|:-------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PEERNFTYPE | 对端NF类型 | 可选必选说明：可选参数  参数含义：该参数用于指定目的NF的类型。  数据来源：本端规划 取值范围： “INVALID（INVALID）”：无效值“NFTypeNRF（NFTypeNRF）”：NF类型为NRF“NFTypeUDM（NFTypeUDM）”：NF类型为UDM“NFTypeAMF（NFTypeAMF）”：NF类型为AMF“NFTypeSMF（NFTypeSMF）”：NF类型为SMF“NFTypeAUSF（NFTypeAUSF）”：NF类型为AUSF“NFTypeNEF（NFTypeNEF）”：NF类型为NEF“NFTypePCF（NFTypePCF）”：NF类型为PCF“NFTypeSMSF（NFTypeSMSF）”：NF类型为SMSF“NFTypeNSSF（NFTypeNSSF）”：NF类型为NSSF“NFTypeUDR（NFTypeUDR）”：NF类型为UDR“NFTypeLMF（NFTypeLMF）”：NF类型为LMF“NFTypeGMLC（NFTypeGMLC）”：NF类型为GMLC“NFType5GEIR（NFType5GEIR）”：NF类型为5GEIR“NFTypeSEPP（NFTypeSEPP）”：NF类型为SEPP“NFTypeUPF（NFTypeUPF）”：NF类型为UPF“NFTypeN3IWF（NFTypeN3IWF）”：NF类型为N3IWF“NFTypeAF（NFTypeAF）”：NF类型为AF“NFTypeUDSF（NFTypeUDSF）”：NF类型为UDSF“NFTypeBSF（NFTypeBSF）”：NF类型为BSF“NFTypeCHF（NFTypeCHF）”：NF类型为CHF“NFTypeCUSTOM_OCS（NFTypeCUSTOM_OCS）”：NF类型为OCS“NFTypeSCP（NFTypeSCP）”：NF类型为SCP“NFTypeMBSMF（NFTypeMB_SMF）”：NF类型为MB_SMF“NFTypeNWDAF（NFTypeNWDAF）”：NF类型为NWDAF“NFTypeUDN（NFTypeUDN）”：NF类型为UDN“NFTypeSFC（NFTypeSFC）”：NF类型为SFC“NFTypeUCBC（NFTypeUCBC）”：NF类型为UCBC“NFTypeCBE（NFTypeCBE）”：NF类型为CBE 其中，INVALID为无效值，系统支持下发，但实际不生效。 默认值：无  配置原则：  当NF类型为Callback或Location时，该参数设置为INVALID。 |
| LINKSETID  | 链路集标识  | 可选必选说明：可选参数  参数含义：该参数用于指定需要删除的链路集标识。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是0~256。  默认值：无  配置原则：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |

## 使用实例

若运营商想要删除NFTYPE为UDM的链路集，可以执行如下命令。

```
DEL SBILINKSET:PEERNFTYPE=NFTypeUDM;
```