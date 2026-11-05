# 查询HTR流控安全边界配置（LST HTTPHTRMS）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询HTR流控安全边界配置。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

| 参数标识        | 参数名称   | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|:------------|:-------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| LOCALNFTYPE | 本端网元类型 | 可选必选说明：可选参数  参数含义：该参数用于设置本端NF类型。  数据来源：本端规划 取值范围： “INVALID（INVALID）”：无效值“NFTypeNRF（NFTypeNRF）”：NF类型为NRF“NFTypeUDM（NFTypeUDM）”：NF类型为UDM“NFTypeAMF（NFTypeAMF）”：NF类型为AMF“NFTypeSMF（NFTypeSMF）”：NF类型为SMF“NFTypeAUSF（NFTypeAUSF）”：NF类型为AUSF“NFTypeNEF（NFTypeNEF）”：NF类型为NEF“NFTypePCF（NFTypePCF）”：NF类型为PCF“NFTypeSMSF（NFTypeSMSF）”：NF类型为SMSF“NFTypeNSSF（NFTypeNSSF）”：NF类型为NSSF“NFTypeUDR（NFTypeUDR）”：NF类型为UDR“NFTypeLMF（NFTypeLMF）”：NF类型为LMF“NFTypeGMLC（NFTypeGMLC）”：NF类型为GMLC“NFType5GEIR（NFType5GEIR）”：NF类型为5GEIR“NFTypeSEPP（NFTypeSEPP）”：NF类型为SEPP“NFTypeUPF（NFTypeUPF）”：NF类型为UPF“NFTypeN3IWF（NFTypeN3IWF）”：NF类型为N3IWF“NFTypeAF（NFTypeAF）”：NF类型为AF“NFTypeUDSF（NFTypeUDSF）”：NF类型为UDSF“NFTypeBSF（NFTypeBSF）”：NF类型为BSF“NFTypeCHF（NFTypeCHF）”：NF类型为CHF“NFTypeCUSTOM_OCS（NFTypeCUSTOM_OCS）”：NF类型为CUSTOM_OCS“NFTypeSCP（NFTypeSCP）”：NF类型为SCP“NFTypeNWDAF（NFTypeNWDAF）”：NF类型为NWDAF“NFTypePCSCF（NFTypePCSCF）”：NF类型为PCSCF“NFTypeCBCF（NFTypeCBCF）”：NF类型为CBCF“NFTypeDRA（NFTypeDRA）”：NF类型为DRA“NFTypeMB_SMF（NFTypeMB_SMF）”：NF类型为MB_SMF“NFTypeUDN（NFTypeUDN）”：NF类型为UDN“NFTypeSFC（NFTypeSFC）”：NF类型为SFC“NFTypeUCBC（NFTypeUCBC）”：NF类型为UCBC“NFTypeCBE（NFTypeCBE）”：NF类型为CBE“NFTypeNEFEx（NFTypeNEFEx）”：NF类型为NEFEx“NFTypeSCF（NFTypeSCF）”：NF类型为SCF“NFTypeKMC（NFTypeKMC）”：NF类型为KMC 其中，INVALID为无效值，系统支持下发，但实际不生效。 默认值：无  配置原则：无 |
| PEERNFTYPE  | 对端网元类型 | 可选必选说明：可选参数  参数含义：该参数用于设置对端NF类型。  数据来源：全网规划 取值范围： “INVALID（INVALID）”：无效值“NFTypeNRF（NFTypeNRF）”：NF类型为NRF“NFTypeUDM（NFTypeUDM）”：NF类型为UDM“NFTypeAMF（NFTypeAMF）”：NF类型为AMF“NFTypeSMF（NFTypeSMF）”：NF类型为SMF“NFTypeAUSF（NFTypeAUSF）”：NF类型为AUSF“NFTypeNEF（NFTypeNEF）”：NF类型为NEF“NFTypePCF（NFTypePCF）”：NF类型为PCF“NFTypeSMSF（NFTypeSMSF）”：NF类型为SMSF“NFTypeNSSF（NFTypeNSSF）”：NF类型为NSSF“NFTypeUDR（NFTypeUDR）”：NF类型为UDR“NFTypeLMF（NFTypeLMF）”：NF类型为LMF“NFTypeGMLC（NFTypeGMLC）”：NF类型为GMLC“NFType5GEIR（NFType5GEIR）”：NF类型为5GEIR“NFTypeSEPP（NFTypeSEPP）”：NF类型为SEPP“NFTypeUPF（NFTypeUPF）”：NF类型为UPF“NFTypeN3IWF（NFTypeN3IWF）”：NF类型为N3IWF“NFTypeAF（NFTypeAF）”：NF类型为AF“NFTypeUDSF（NFTypeUDSF）”：NF类型为UDSF“NFTypeBSF（NFTypeBSF）”：NF类型为BSF“NFTypeCHF（NFTypeCHF）”：NF类型为CHF“NFTypeCUSTOM_OCS（NFTypeCUSTOM_OCS）”：NF类型为CUSTOM_OCS“NFTypeSCP（NFTypeSCP）”：NF类型为SCP“NFTypeNWDAF（NFTypeNWDAF）”：NF类型为NWDAF“NFTypePCSCF（NFTypePCSCF）”：NF类型为PCSCF“NFTypeCBCF（NFTypeCBCF）”：NF类型为CBCF“NFTypeDRA（NFTypeDRA）”：NF类型为DRA“NFTypeMB_SMF（NFTypeMB_SMF）”：NF类型为MB_SMF“NFTypeUDN（NFTypeUDN）”：NF类型为UDN“NFTypeSFC（NFTypeSFC）”：NF类型为SFC“NFTypeUCBC（NFTypeUCBC）”：NF类型为UCBC“NFTypeCBE（NFTypeCBE）”：NF类型为CBE“NFTypeNEFEx（NFTypeNEFEx）”：NF类型为NEFEx“NFTypeSCF（NFTypeSCF）”：NF类型为SCF“NFTypeKMC（NFTypeKMC）”：NF类型为KMC 其中，INVALID为无效值，系统支持下发，但实际不生效。 默认值：无  配置原则：无 |

## 使用实例

查询所有HTR流控安全边界配置，可以用如下命令：

```
%%LST HTTPHTRMS:;%%
RETCODE = 0  操作成功

结果如下
--------
本端网元类型  对端网元类型   最小流控速率(个/秒)  最大流控速率(个/秒)  

NFTypeAMF    NFTypeUDM         210               1500                                 
NFTypeAMF    NFTypeAUSF        210               1500                                 
NFTypeSMF    NFTypeUDM         160               1200                                 
NFTypeSMF    NFTypePCF         160               1200                                 
NFTypeCHF    NFTypeCUSTOM_OCS  1000              3000                                 
(结果个数 = 5)

---    END
```

## 输出结果说明

| 输出项名称       | 输出项解释                          |
|:------------|:-------------------------------|
| 本端网元类型      | 该参数用于设置本端NF类型。                 |
| 对端网元类型      | 该参数用于设置对端NF类型。                 |
| 最小流控速率(个/秒) | 该参数用于设置单HTTP POD放通阈值动态调整的最小速率。 |
| 最大流控速率(个/秒) | 该参数用于设置单HTTP POD放通阈值动态调整的最大速率。 |