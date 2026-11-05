# 删除客户端或服务端超时时间配置（RMV HTTPNFCONF）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

该命令用于删除客户端或服务端等待响应超时时间配置。

## 注意事项

- 该命令执行后立即生效。

- 当参数“角色”配置为“客户端”时，配置的“等待响应超时时间”优先级大于SET HTTPCONF中配置的“客户端接收HTTP响应消息超时时间”。
- 当参数“角色”配置为“服务端”时，配置的“等待响应超时时间”优先级大于SET HTTPCONF中配置的“服务端回复HTTP响应消息超时时间”。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识        | 参数名称   | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|:------------|:-------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| LOCALNFTYPE | 本端网元类型 | 可选必选说明：必选参数  参数含义：该参数用于指定本端网元类型。  数据来源：本端规划 取值范围： “INVALID（INVALID）”：无效值“NFTypeNRF（NFTypeNRF）”：NF类型为NRF“NFTypeUDM（NFTypeUDM）”：NF类型为UDM“NFTypeAMF（NFTypeAMF）”：NF类型为AMF“NFTypeSMF（NFTypeSMF）”：NF类型为SMF“NFTypeAUSF（NFTypeAUSF）”：NF类型为AUSF“NFTypeNEF（NFTypeNEF）”：NF类型为NEF“NFTypePCF（NFTypePCF）”：NF类型为PCF“NFTypeSMSF（NFTypeSMSF）”：NF类型为SMSF“NFTypeNSSF（NFTypeNSSF）”：NF类型为NSSF“NFTypeUDR（NFTypeUDR）”：NF类型为UDR“NFTypeLMF（NFTypeLMF）”：NF类型为LMF“NFTypeGMLC（NFTypeGMLC）”：NF类型为GMLC“NFType5GEIR（NFType5GEIR）”：NF类型为5GEIR“NFTypeSEPP（NFTypeSEPP）”：NF类型为SEPP“NFTypeUPF（NFTypeUPF）”：NF类型为UPF“NFTypeN3IWF（NFTypeN3IWF）”：NF类型为N3IWF“NFTypeAF（NFTypeAF）”：NF类型为AF“NFTypeUDSF（NFTypeUDSF）”：NF类型为UDSF“NFTypeBSF（NFTypeBSF）”：NF类型为BSF“NFTypeCHF（NFTypeCHF）”：NF类型为CHF“NFTypeCUSTOM_OCS（NFTypeCUSTOM_OCS）”：NF类型为CUSTOM_OCS“NFTypeSCP（NFTypeSCP）”：NF类型为SCP“NFTypeNWDAF（NFTypeNWDAF）”：NF类型为NWDAF“NFTypePCSCF（NFTypePCSCF）”：NF类型为PCSCF“NFTypeCBCF（NFTypeCBCF）”：NF类型为CBCF“NFTypeDRA（NFTypeDRA）”：NF类型为DRA“NFTypeMB_SMF（NFTypeMB_SMF）”：NF类型为MB_SMF“NFTypeUDN（NFTypeUDN）”：NF类型为UDN“NFTypeSFC（NFTypeSFC）”：NF类型为SFC“NFTypeUCBC（NFTypeUCBC）”：NF类型为UCBC“NFTypeCBE（NFTypeCBE）”：NF类型为CBE“NFTypeNEFEx（NFTypeNEFEx）”：NF类型为NEFEx“NFTypeSCF（NFTypeSCF）”：NF类型为SCF“NFTypeKMC（NFTypeKMC）”：NF类型为KMC  默认值：无  配置原则：无 |
| PEERNFTYPE  | 对端网元类型 | 可选必选说明：必选参数  参数含义：该参数用于指定对端网元类型。  数据来源：本端规划 取值范围： “INVALID（INVALID）”：无效值“NFTypeNRF（NFTypeNRF）”：NF类型为NRF“NFTypeUDM（NFTypeUDM）”：NF类型为UDM“NFTypeAMF（NFTypeAMF）”：NF类型为AMF“NFTypeSMF（NFTypeSMF）”：NF类型为SMF“NFTypeAUSF（NFTypeAUSF）”：NF类型为AUSF“NFTypeNEF（NFTypeNEF）”：NF类型为NEF“NFTypePCF（NFTypePCF）”：NF类型为PCF“NFTypeSMSF（NFTypeSMSF）”：NF类型为SMSF“NFTypeNSSF（NFTypeNSSF）”：NF类型为NSSF“NFTypeUDR（NFTypeUDR）”：NF类型为UDR“NFTypeLMF（NFTypeLMF）”：NF类型为LMF“NFTypeGMLC（NFTypeGMLC）”：NF类型为GMLC“NFType5GEIR（NFType5GEIR）”：NF类型为5GEIR“NFTypeSEPP（NFTypeSEPP）”：NF类型为SEPP“NFTypeUPF（NFTypeUPF）”：NF类型为UPF“NFTypeN3IWF（NFTypeN3IWF）”：NF类型为N3IWF“NFTypeAF（NFTypeAF）”：NF类型为AF“NFTypeUDSF（NFTypeUDSF）”：NF类型为UDSF“NFTypeBSF（NFTypeBSF）”：NF类型为BSF“NFTypeCHF（NFTypeCHF）”：NF类型为CHF“NFTypeCUSTOM_OCS（NFTypeCUSTOM_OCS）”：NF类型为CUSTOM_OCS“NFTypeSCP（NFTypeSCP）”：NF类型为SCP“NFTypeNWDAF（NFTypeNWDAF）”：NF类型为NWDAF“NFTypePCSCF（NFTypePCSCF）”：NF类型为PCSCF“NFTypeCBCF（NFTypeCBCF）”：NF类型为CBCF“NFTypeDRA（NFTypeDRA）”：NF类型为DRA“NFTypeMB_SMF（NFTypeMB_SMF）”：NF类型为MB_SMF“NFTypeUDN（NFTypeUDN）”：NF类型为UDN“NFTypeSFC（NFTypeSFC）”：NF类型为SFC“NFTypeUCBC（NFTypeUCBC）”：NF类型为UCBC“NFTypeCBE（NFTypeCBE）”：NF类型为CBE“NFTypeNEFEx（NFTypeNEFEx）”：NF类型为NEFEx“NFTypeSCF（NFTypeSCF）”：NF类型为SCF“NFTypeKMC（NFTypeKMC）”：NF类型为KMC  默认值：无  配置原则：无 |
| ROLE        | 角色     | 可选必选说明：必选参数  参数含义：该参数用于指定当前角色为客户端或服务端。  数据来源：本端规划 取值范围： Client（客户端）Server（服务端）  默认值：无  配置原则：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

## 使用实例

删除本端网元类型为NRF，对端网元类型为UDM的服务端等待响应超时时间。

```
RMV HTTPNFCONF: LOCALNFTYPE=NFTypeNRF, PEERNFTYPE=NFTypeUDM, ROLE=Server;
```