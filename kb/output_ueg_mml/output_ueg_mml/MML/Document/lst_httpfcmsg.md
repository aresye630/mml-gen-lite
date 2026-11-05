# 查询HTTP流控消息类型（LST HTTPFCMSG）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于查询HTTP流控消息类型。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

| 参数标识        | 参数名称    | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|:------------|:--------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NFTYPE      | 网元类型    | 可选必选说明：可选参数  参数含义：本参数用于指定NF类型。  数据来源：本端规划 取值范围： “INVALID（INVALID）”：无效值“NFTypeNRF（NFTypeNRF）”：NF类型为NRF“NFTypeUDM（NFTypeUDM）”：NF类型为UDM“NFTypeAMF（NFTypeAMF）”：NF类型为AMF“NFTypeSMF（NFTypeSMF）”：NF类型为SMF“NFTypeAUSF（NFTypeAUSF）”：NF类型为AUSF“NFTypeNEF（NFTypeNEF）”：NF类型为NEF“NFTypePCF（NFTypePCF）”：NF类型为PCF“NFTypeSMSF（NFTypeSMSF）”：NF类型为SMSF“NFTypeNSSF（NFTypeNSSF）”：NF类型为NSSF“NFTypeUDR（NFTypeUDR）”：NF类型为UDR“NFTypeLMF（NFTypeLMF）”：NF类型为LMF“NFTypeGMLC（NFTypeGMLC）”：NF类型为GMLC“NFType5GEIR（NFType5GEIR）”：NF类型为5GEIR“NFTypeSEPP（NFTypeSEPP）”：NF类型为SEPP“NFTypeUPF（NFTypeUPF）”：NF类型为UPF“NFTypeN3IWF（NFTypeN3IWF）”：NF类型为N3IWF“NFTypeAF（NFTypeAF）”：NF类型为AF“NFTypeUDSF（NFTypeUDSF）”：NF类型为UDSF“NFTypeBSF（NFTypeBSF）”：NF类型为BSF“NFTypeCHF（NFTypeCHF）”：NF类型为CHF“NFTypeCUSTOM_OCS（NFTypeCUSTOM_OCS）”：NF类型为CUSTOM_OCS“NFTypeSCP（NFTypeSCP）”：NF类型为SCP“NFTypeNWDAF（NFTypeNWDAF）”：NF类型为NWDAF“NFTypePCSCF（NFTypePCSCF）”：NF类型为PCSCF“NFTypeCBCF（NFTypeCBCF）”：NF类型为CBCF“NFTypeDRA（NFTypeDRA）”：NF类型为DRA“NFTypeMB_SMF（NFTypeMB_SMF）”：NF类型为MB_SMF“NFTypeUDN（NFTypeUDN）”：NF类型为UDN“NFTypeSFC（NFTypeSFC）”：NF类型为SFC“NFTypeUCBC（NFTypeUCBC）”：NF类型为UCBC“NFTypeCBE（NFTypeCBE）”：NF类型为CBE 其中，INVALID为无效值，系统支持下发，但实际不生效。 默认值：无  配置原则：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| SBIPROTOCOL | SBI协议类型 | 可选必选说明：可选参数  参数含义：本参数用于指定SBI协议类型。  数据来源：本端规划 取值范围： “SBIProtocol29571（SBIProtocol29571）”：SBI协议为29571“SBIProtocolSMF29502（SBIProtocolSMF29502）”：SBI协议为SMF29502“SBIProtocolUDM29503（SBIProtocolUDM29503 ）”：SBI协议为UDM29503“SBIProtocolUDR29505（SBIProtocolUDR29505）”：SBI协议为UDR29505“SBIProtocolPCF29507（SBIProtocolPCF29507）”：SBI协议为PCF29507“SBIProtocolAUSF29509（SBIProtocolAUSF29509）”：SBI协议为AUSF29509“SBIProtocolNRF29510（SBIProtocolNRF29510）”：SBI协议为NRF29510“SBIProtocol5GEIR29511（SBIProtocol5GEIR29511）”：SBI协议为5GEIR29511“SBIProtocolPCF29512（SBIProtocolPCF29512）”：SBI协议为PCF29512“SBIProtocolPCF29514（SBIProtocolPCF29514）”：SBI协议为PCF29514“SBIProtocolAMF29518（SBIProtocolAMF29518）”：SBI协议为AMF29518“SBIProtocolUDR29519（SBIProtocolUDR29519）”：SBI协议为UDR29519“SBIProtocolBSF29521（SBIProtocolBSF29521）”：SBI协议为BSF29521“SBIProtocolNSSF29531（SBIProtocolNSSF29531）”：SBI协议为NSSF29531“SBIProtocolLMF29572（SBIProtocolLMF29572）”：SBI协议为LMF29572“SBIProtocolCHF32291（SBIProtocolCHF32291）”：SBI协议为CHF32291“SBIProtocolSMF29508（SBIProtocolSMF29508）”：SBI协议为SMF29508“SBIProtocolNWDAF29520（SBIProtocolNWDAF29520）”：SBI协议为NWDAF29520“SBIProtocolPCF29525（SBIProtocolPCF29525）”：SBI协议为PCF29525“SBIProtocolMEC20001（SBIProtocolMEC20001）”：SBI协议为MEC20001“SBIProtocolSMSF29540（SBIProtocolSMSF29540）”：SBI协议为SMSF29540“SBIProtocolGMLC29515（SBIProtocolGMLC29515）”：SBI协议为GMLC29515“SBIProtocolNEF29122（SBIProtocolNEF29122）”：SBI协议为NEF29122“SBIProtocolMBSMF29532（SBIProtocolMBSMF29532）”：SBI协议为MBSMF29532“SBIProtocolNEF29551（SBIProtocolNEF29551）”：SBI协议为NEF29551“SBIProtocolNEF29522（SBIProtocolNEF29522）”：SBI协议为NEF29522“SBIProtocolUPF29564（SBIProtocolUPF29564）”：SBI协议为UPF29564“SBIProtocolUDN10000（SBIProtocolUDN10000）”：SBI协议为UDN10000“SBIProtocolNEF29541（SBIProtocolNEF29541）”：SBI协议为NEF29541“SBIProtocolBSF10500（SBIProtocolBSF10500）”：SBI协议为BSF10500“SBIProtocolSFC20005（SBIProtocolSFC20005）”：SBI协议为SFC20005“SBIProtocolCBCF10000（SBIProtocolCBCF10000）”：SBI协议为CBCF10000  默认值：无  配置原则：无 |
| MSGINDEX    | 消息索引    | 可选必选说明：可选参数  参数含义：本参数用于指定消息索引。  数据来源：本端规划  取值范围：整数类型，取值范围是0~4294967295。  默认值：无  配置原则：  由于此命令配置后影响较大，流控消息索引的配置规则请联系华为技术支持。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| FCTYPE      | 流控类型    | 可选必选说明：可选参数  参数含义：该参数用于指定流控类型。  数据来源：全网规划 取值范围： “FIXSPDFCGRP（基于流控组固定速率流控）”：基于流控组固定速率流控“FIXBWFCGLB（全局固定带宽流控）”：全局固定带宽流控“SELFFC（自保流控）”：自保流控“PBUF（PBUF流控）”：PBUF流控“MEMORY（内存流控）”：内存流控“FIXSPDFCINTF（基于接口类型固定速率流控）”：基于接口类型固定速率流控“TCPBPFC（TCP反压流控）”：TCP反压流控  默认值：无  配置原则：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |

## 使用实例

例如查询AMF网元的所有流控消息

```
%%LST HTTPFCMSG: NFTYPE=NFTypeAMF;%%
RETCODE = 0  操作成功

结果如下
------------------------
        网元类型  =  NFTypeAMF
     SBI协议类型  =  SBIProtocolAMF29518
        消息索引  =  1
            角色  =  客户端
            方向  =  发送
        流控类型  =  PBUF流控
        流控开关  =  打开
      IP地址索引  =  0
          流控组  =  0
      流控优先级  =  0
        局向索引  =  0

(结果个数 = 1)

---    END
```

## 输出结果说明

| 输出项名称   | 输出项解释                                                                                     |
|:--------|:------------------------------------------------------------------------------------------|
| 网元类型    | 本参数用于指定NF类型。                                                                              |
| SBI协议类型 | 本参数用于指定SBI协议类型。                                                                           |
| 消息索引    | 本参数用于指定消息索引。                                                                              |
| 角色      | 该参数用于指定本端NF角色。                                                                            |
| 方向      | 该参数用于指定消息方向。                                                                              |
| 流控类型    | 该参数用于指定流控类型。                                                                              |
| 流控开关    | 该参数用于控制流控功能是否开启。                                                                          |
| IP地址索引  | 该参数用于标识具有相同前缀的一组IP地址。此参数无需配置，配置后也无实际意义。                                                   |
| 流控组     | 该参数用于指定HTTP固定速率流控组的唯一标识。该参数来源于ADD HTTPFCIPGRP命令的“流控组”参数，可通过LST HTTPFCIPGRP命令查询获取。         |
| 流控优先级   | 该参数用于指定自保流控消息优先级。                                                                         |
| 局向索引    | 该参数用于指定基于接口类型固定速率流控的局向索引。该参数来源于ADD HTTPFIXEDFCINF命令的“局向索引”参数，可通过LST HTTPFIXEDFCINF命令查询获取。 |