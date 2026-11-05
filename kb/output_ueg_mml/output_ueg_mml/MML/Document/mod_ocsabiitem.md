# 修改PCRF对端OCS能力字典项(MOD OCSABIITEM)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**须知** 

此命令是高危命令，如果执行不当会影响UPCF与OCS相关的业务的正常使用，需联系华为技术支持确认后再执行。

OCS能力字典项支持与UPCF直连的OCS配置，不支持通过DRA与UPCF连接OCS的配置。

该命令为配置类命令，用于修改或调整配置数据库中的一条对端OCS能力字典项的数据记录的某些参数。在该命令中，系统通过“能力字典ID”和“能力字典项ID”参数来唯一标识一条OCS能力字典记录。

## 注意事项

在缺省的情况下，新增“能力字典”时默认为“能力字典项ID”参数的每个字典项进行了赋值，预置的“能力字典项值”如下（以其中一个“能力字典ID”为“0”作为例子）：

```
能力字典ID  能力字典项ID           能力字典项值                    

0           CarryLocation          UnsupportedCarryLocation        
0           CarryANGWAddress       UnsupportCarryANGWAddress       
0           CarryUserLocationInfo  UnsupportCarryUserLocationInfo  
0           CarryIMEI              UnsupportCarryIMEI              
0           CarryAPN               UnsupportCarryAPN               
0           CarryRATYPE            UnsupportCarryRATYPE
```

## 参数说明

| 参数ID          | 参数名称    | 参数描述                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|:--------------|:--------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ABILITYDICTID | 能力字典ID  | 用于标识OCS能力字典的编号。 取值范围：0～15 默认值：无  说明： 所有通过DRA与UPCF连接的OCS都必须有能够支持“能力字典ID”为“0”的能力。“能力字典ID”取值为“0”的字典称为全局字典。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| ABILITYITEMID | 能力字典项ID | 用于标识OCS能力字典项。 取值说明：CarryLocation(CarryLocation)CarryANGWAddress(CarryANGWAddress)CarryUserLocationInfo(CarryUserLocationInfo)CarryIMEI(CarryIMEI)CarryAPN(CarryAPN)CarryRATYPE(CarryRATYPE) 默认值：无  说明： 当“能力字典项ID”取值为“CarryAPN”时，与Gx会话或N7会话关联的Sy会话均支持该能力字典项。当“能力字典项ID”取值为非“CarryAPN”时，仅与Gx会话关联的Sy会话支持对应能力字典项，与N7会话关联的Sy会话不支持对应能力字典项。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| ABILITYVALUE  | 能力字典项值  | 用于标识能力字典项的取值。 取值说明：CarryLocationSupportedCarryLocation：UPCF向对端OCS发送SLR-I消息时支持携带3GPP-SGSN-MCC-MNC，3GPP-SGSN-Address、3GPP-SGSN-Ipv6-Address。UnsupportedCarryLocation：UPCF向对端OCS发送SLR-I消息时不支持携带3GPP-SGSN-MCC-MNC，3GPP-SGSN-Address、3GPP-SGSN-Ipv6-Address。 CarryANGWAddressSupportCarryANGWAddress：UPCF向对端OCS发送SLR-I消息时支持携带Gx-AN-GW-Address。UnsupportCarryANGWAddress：UPCF向对端OCS发送SLR-I消息时不支持携带Gx-AN-GW-Address。 CarryUserLocationInfoSupportCarryUserLocationInfo：UPCF向对端OCS发送SLR-I消息时支持携带Gx-3GPP-User-Location-Info。UnsupportCarryUserLocationInfo：UPCF向对端OCS发送SLR-I消息时不支持携带Gx-3GPP-User-Location-Info。 CarryIMEISupportCarryIMEI：UPCF向对端OCS发送SLR-I消息时支持携带User-Equipment-Info-Type、User-Equipment-Info-Value。UnsupportCarryIMEI：UPCF向对端OCS发送SLR-I消息时不支持携带User-Equipment-Info-Type、User-Equipment-Info-Value。 CarryAPNSupportCarryAPN：UPCF向对端OCS发送SLR-I消息时支持携带Called-Station-ID。UnsupportCarryAPN：UPCF向对端OCS发送SLR-I消息时不支持携带Called-Station-ID。 CarryRATYPESupportCarryRATYPE：UPCF向对端OCS发送SLR-I消息时支持携带Gx-3GPP-RAT-Type。UnsupportCarryRATYPE：UPCF向对端OCS发送SLR-I消息时不支持携带Gx-3GPP-RAT-Type。  说明： 当“能力字典项值”取值为“Supportxxx”时，SLR-I消息会携带以上相应的AVP，AVP携带的信息从关联的Gx或N7会话获取，如果Gx会话没有携带AVP或是N7会话没有携带信元时，SLR-I消息则不携带。当会话恢复触发Sy会话重建时，如果“能力字典项值”取值为“Supportxxx”，SLR-I消息会携带以上相应的AVP，AVP携带的信息从Session备份数据中获取。 |

## 使用实例

修改OCS能力字典项。“能力字典ID”为“15”，“能力字典项ID”为“CarryLocation”，“能力字典项值”为“UnsupportedCarryLocation”。

```
MOD OCSABIITEM: ABILITYDICTID=15, ABILITYITEMID=CarryLocation, ABILITYVALUE=UnsupportedCarryLocation;
```

```
%%MOD OCSABIITEM: ABILITYDICTID=15, ABILITYITEMID=CarryLocation, ABILITYVALUE=UnsupportedCarryLocation, CONFIRM=Y;%%
RETCODE = 0  操作成功

---    END
```