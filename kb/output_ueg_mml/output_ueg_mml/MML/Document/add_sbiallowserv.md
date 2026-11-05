# 增加基于服务的白名单（ADD SBIALLOWSERV）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

该命令用于增加基于服务类型的白名单，当系统作为服务端时，添加到白名单的服务只允许白名单中指定的网元类型的对端访问。未添加到白名单的服务则允许所有对端访问。

## 注意事项

- 该命令执行后立即生效。

- 命令中的网元实例ID参数目前不生效。

- 最多可输入255条记录。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识        | 参数名称   | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|:------------|:-------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| INDEX       | 索引     | 可选必选说明：必选参数  参数含义：该参数用于指定配置的白名单索引。  数据来源：本端规划  取值范围：整数类型，取值范围是1~255。  默认值：无  配置原则：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| SERVICENAME | 服务名称   | 可选必选说明：必选参数  参数含义：该参数用于指定添加到白名单的服务。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是0~255。  默认值：无  配置原则：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| NFTYPE      | 网元类型   | 可选必选说明：必选参数  参数含义：该参数用于指定允许访问白名单中服务的对端网元类型。  数据来源：本端规划 取值范围： “INVALID（INVALID）”：无效值“NFTypeNRF（NFTypeNRF）”：NF类型为NRF“NFTypeUDM（NFTypeUDM）”：NF类型为UDM“NFTypeAMF（NFTypeAMF）”：NF类型为AMF“NFTypeSMF（NFTypeSMF）”：NF类型为SMF“NFTypeAUSF（NFTypeAUSF）”：NF类型为AUSF“NFTypeNEF（NFTypeNEF）”：NF类型为NEF“NFTypePCF（NFTypePCF）”：NF类型为PCF“NFTypeSMSF（NFTypeSMSF）”：NF类型为SMSF“NFTypeNSSF（NFTypeNSSF）”：NF类型为NSSF“NFTypeUDR（NFTypeUDR）”：NF类型为UDR“NFTypeLMF（NFTypeLMF）”：NF类型为LMF“NFTypeGMLC（NFTypeGMLC）”：NF类型为GMLC“NFType5GEIR（NFType5GEIR）”：NF类型为5GEIR“NFTypeSEPP（NFTypeSEPP）”：NF类型为SEPP“NFTypeUPF（NFTypeUPF）”：NF类型为UPF“NFTypeN3IWF（NFTypeN3IWF）”：NF类型为N3IWF“NFTypeAF（NFTypeAF）”：NF类型为AF“NFTypeUDSF（NFTypeUDSF）”：NF类型为UDSF“NFTypeBSF（NFTypeBSF）”：NF类型为BSF“NFTypeCHF（NFTypeCHF）”：NF类型为CHF“NFTypeCUSTOM_OCS（NFTypeCUSTOM_OCS）”：NF类型为CUSTOM_OCS“NFTypeSCP（NFTypeSCP）”：NF类型为SCP“NFTypeNWDAF（NFTypeNWDAF）”：NF类型为NWDAF“NFTypePCSCF（NFTypePCSCF）”：NF类型为PCSCF“NFTypeCBCF（NFTypeCBCF）”：NF类型为CBCF“NFTypeDRA（NFTypeDRA）”：NF类型为DRA“NFTypeMB_SMF（NFTypeMB_SMF）”：NF类型为MB_SMF“NFTypeUDN（NFTypeUDN）”：NF类型为UDN“NFTypeSFC（NFTypeSFC）”：NF类型为SFC“NFTypeUCBC（NFTypeUCBC）”：NF类型为UCBC“NFTypeCBE（NFTypeCBE）”：NF类型为CBE 其中，INVALID为无效值，系统支持下发，但实际不生效。 默认值：无  配置原则：无 |
| NFID        | 网元实例ID | 可选必选说明：可选参数  参数含义：该参数用于指定允许访问白名单中服务的对端网元实例ID。目前本参数不生效。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是0~255。  默认值：无  配置原则：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

## 使用实例

若运营商想要指定只有nrf类型的网元可以访问“nnrf-nfm”服务，则执行如下命令。

```
ADD SBIALLOWSERV: INDEX=1, SERVICENAME="nnrf-nfm", NFTYPE=NFTypeNRF;
```