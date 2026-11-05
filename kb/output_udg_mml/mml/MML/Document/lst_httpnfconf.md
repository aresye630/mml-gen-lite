# 查询客户端或服务端超时时间配置（LST HTTPNFCONF）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询客户端或服务端等待响应超时时间配置。

## 注意事项

- 当参数“角色”配置为“客户端”时，配置的“等待响应超时时间”优先级大于SET HTTPCONF中配置的“客户端接收HTTP响应消息超时时间”。
- 当参数“角色”配置为“服务端”时，配置的“等待响应超时时间”优先级大于SET HTTPCONF中配置的“服务端回复HTTP响应消息超时时间”。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

| 参数标识        | 参数名称   | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|:------------|:-------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| LOCALNFTYPE | 本端网元类型 | 可选必选说明：可选参数  参数含义：该参数用于指定本端网元类型。  数据来源：本端规划 取值范围： “INVALID（INVALID）”：无效值“NFTypeNRF（NFTypeNRF）”：NF类型为NRF“NFTypeUDM（NFTypeUDM）”：NF类型为UDM“NFTypeAMF（NFTypeAMF）”：NF类型为AMF“NFTypeSMF（NFTypeSMF）”：NF类型为SMF“NFTypeAUSF（NFTypeAUSF）”：NF类型为AUSF“NFTypeNEF（NFTypeNEF）”：NF类型为NEF“NFTypePCF（NFTypePCF）”：NF类型为PCF“NFTypeSMSF（NFTypeSMSF）”：NF类型为SMSF“NFTypeNSSF（NFTypeNSSF）”：NF类型为NSSF“NFTypeUDR（NFTypeUDR）”：NF类型为UDR“NFTypeLMF（NFTypeLMF）”：NF类型为LMF“NFTypeGMLC（NFTypeGMLC）”：NF类型为GMLC“NFType5GEIR（NFType5GEIR）”：NF类型为5GEIR“NFTypeSEPP（NFTypeSEPP）”：NF类型为SEPP“NFTypeUPF（NFTypeUPF）”：NF类型为UPF“NFTypeN3IWF（NFTypeN3IWF）”：NF类型为N3IWF“NFTypeAF（NFTypeAF）”：NF类型为AF“NFTypeUDSF（NFTypeUDSF）”：NF类型为UDSF“NFTypeBSF（NFTypeBSF）”：NF类型为BSF“NFTypeCHF（NFTypeCHF）”：NF类型为CHF“NFTypeCUSTOM_OCS（NFTypeCUSTOM_OCS）”：NF类型为CUSTOM_OCS“NFTypeSCP（NFTypeSCP）”：NF类型为SCP“NFTypeNWDAF（NFTypeNWDAF）”：NF类型为NWDAF“NFTypePCSCF（NFTypePCSCF）”：NF类型为PCSCF“NFTypeCBCF（NFTypeCBCF）”：NF类型为CBCF“NFTypeDRA（NFTypeDRA）”：NF类型为DRA“NFTypeMB_SMF（NFTypeMB_SMF）”：NF类型为MB_SMF“NFTypeUDN（NFTypeUDN）”：NF类型为UDN“NFTypeSFC（NFTypeSFC）”：NF类型为SFC“NFTypeUCBC（NFTypeUCBC）”：NF类型为UCBC“NFTypeCBE（NFTypeCBE）”：NF类型为CBE“NFTypeNEFEx（NFTypeNEFEx）”：NF类型为NEFEx“NFTypeSCF（NFTypeSCF）”：NF类型为SCF“NFTypeKMC（NFTypeKMC）”：NF类型为KMC  默认值：无  配置原则：无 |
| PEERNFTYPE  | 对端网元类型 | 可选必选说明：可选参数  参数含义：该参数用于指定对端网元类型。  数据来源：本端规划 取值范围： “INVALID（INVALID）”：无效值“NFTypeNRF（NFTypeNRF）”：NF类型为NRF“NFTypeUDM（NFTypeUDM）”：NF类型为UDM“NFTypeAMF（NFTypeAMF）”：NF类型为AMF“NFTypeSMF（NFTypeSMF）”：NF类型为SMF“NFTypeAUSF（NFTypeAUSF）”：NF类型为AUSF“NFTypeNEF（NFTypeNEF）”：NF类型为NEF“NFTypePCF（NFTypePCF）”：NF类型为PCF“NFTypeSMSF（NFTypeSMSF）”：NF类型为SMSF“NFTypeNSSF（NFTypeNSSF）”：NF类型为NSSF“NFTypeUDR（NFTypeUDR）”：NF类型为UDR“NFTypeLMF（NFTypeLMF）”：NF类型为LMF“NFTypeGMLC（NFTypeGMLC）”：NF类型为GMLC“NFType5GEIR（NFType5GEIR）”：NF类型为5GEIR“NFTypeSEPP（NFTypeSEPP）”：NF类型为SEPP“NFTypeUPF（NFTypeUPF）”：NF类型为UPF“NFTypeN3IWF（NFTypeN3IWF）”：NF类型为N3IWF“NFTypeAF（NFTypeAF）”：NF类型为AF“NFTypeUDSF（NFTypeUDSF）”：NF类型为UDSF“NFTypeBSF（NFTypeBSF）”：NF类型为BSF“NFTypeCHF（NFTypeCHF）”：NF类型为CHF“NFTypeCUSTOM_OCS（NFTypeCUSTOM_OCS）”：NF类型为CUSTOM_OCS“NFTypeSCP（NFTypeSCP）”：NF类型为SCP“NFTypeNWDAF（NFTypeNWDAF）”：NF类型为NWDAF“NFTypePCSCF（NFTypePCSCF）”：NF类型为PCSCF“NFTypeCBCF（NFTypeCBCF）”：NF类型为CBCF“NFTypeDRA（NFTypeDRA）”：NF类型为DRA“NFTypeMB_SMF（NFTypeMB_SMF）”：NF类型为MB_SMF“NFTypeUDN（NFTypeUDN）”：NF类型为UDN“NFTypeSFC（NFTypeSFC）”：NF类型为SFC“NFTypeUCBC（NFTypeUCBC）”：NF类型为UCBC“NFTypeCBE（NFTypeCBE）”：NF类型为CBE“NFTypeNEFEx（NFTypeNEFEx）”：NF类型为NEFEx“NFTypeSCF（NFTypeSCF）”：NF类型为SCF“NFTypeKMC（NFTypeKMC）”：NF类型为KMC  默认值：无  配置原则：无 |
| ROLE        | 角色     | 可选必选说明：可选参数  参数含义：该参数用于指定当前角色为客户端或服务端。  数据来源：本端规划 取值范围： Client（客户端）Server（服务端）  默认值：无  配置原则：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

## 使用实例

- 本端网元类型为NRF，对端网元类型为UDM，查询客户端等待响应超时时间。

  ```
  %%LST HTTPNFCONF: LOCALNFTYPE=NFTypeNRF, PEERNFTYPE=NFTypeUDM, ROLE=Client;%%
  RETCODE = 0  操作成功

  结果如下
  --------
      本端网元类型  =  NFTypeNRF
      对端网元类型  =  NFTypeUDM
              角色  =  客户端
  等待响应超时时间  =  10
  (结果个数 = 1)

  ---    END
  ```
- 查询所有基于本对端网元类型，客户端和服务端等待响应超时时间。

  ```
  %%LST HTTPNFCONF:;%%
  RETCODE = 0  操作成功

  结果如下
  --------
  本端网元类型  对端网元类型  角色    等待响应超时时间  

  NFTypeNRF     NFTypeUDM     客户端  10                
  NFTypeNRF     NFTypeAMF     服务端  10                
  (结果个数 = 2)

  ---    END
  ```

## 输出结果说明

| 输出项名称    | 输出项解释                |
|:---------|:---------------------|
| 本端网元类型   | 该参数用于指定本端网元类型。       |
| 对端网元类型   | 该参数用于指定对端网元类型。       |
| 角色       | 该参数用于指定当前角色为客户端或服务端。 |
| 等待响应超时时间 | 该参数用于配置等待响应超时时间。     |