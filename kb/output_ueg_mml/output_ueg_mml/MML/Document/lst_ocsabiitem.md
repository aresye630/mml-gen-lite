# 查询PCRF对端OCS能力字典项的配置信息（LST OCSABIITEM）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令为维护类命令，用于在配置数据库中查询对端OCS能力字典项的配置信息：

- 如果需要查询全部OCS能力项的配置信息，请不要输入任何参数。
- 如果需要查询某个OCS能力项的配置信息，请依据参数说明输入查询条件。

**说明** 

OCS能力字典项支持与UPCF直连的OCS配置，不支持通过DRA与UPCF连接OCS的配置。

## 注意事项

无。

## 参数说明

| 参数ID          | 参数名称    | 参数描述                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|:--------------|:--------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ABILITYDICTID | 能力字典ID  | 用于指示系统需要按照哪个能力字典ID来查询OCS能力字典项配置信息；若不输入，则表示所有的能力字典ID。 取值范围：0～15 默认值：无  说明： 所有通过DRA与UPCF连接的OCS都必须有能够支持“能力字典ID”为“0”的能力。“能力字典ID”取值为“0”的字典称为全局字典。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| ABILITYITEMID | 能力字典项ID | 用于指示系统需要按照哪个能力字典项ID来查询OCS能力项字典项配置信息；若不输入，则表示所有的能力字典项ID。 取值说明：CarryLocation(CarryLocation)CarryANGWAddress(CarryANGWAddress)CarryUserLocationInfo(CarryUserLocationInfo)CarryIMEI(CarryIMEI)CarryAPN(CarryAPN)CarryRATYPE(CarryRATYPE) 默认值：无  说明： 当“能力字典项ID”取值为“CarryAPN”时，与Gx会话或N7会话关联的Sy会话均支持该能力字典项。当“能力字典项ID”取值为非“CarryAPN”时，仅与Gx会话关联的Sy会话支持对应能力字典项，与N7会话关联的Sy会话不支持对应能力字典项。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| ABILITYVALUE  | 能力字典项值  | 用于指示系统需要按照哪个能力字典项的取值来查询OCS能力项字典项配置信息；若不输入，则表示所有的能力字典项的取值。 取值说明：CarryLocationSupportedCarryLocation：UPCF向对端OCS发送SLR-I消息时支持携带3GPP-SGSN-MCC-MNC，3GPP-SGSN-Address、3GPP-SGSN-Ipv6-Address。UnsupportedCarryLocation：UPCF向对端OCS发送SLR-I消息时不支持携带3GPP-SGSN-MCC-MNC，3GPP-SGSN-Address、3GPP-SGSN-Ipv6-Address。 CarryANGWAddressSupportCarryANGWAddress：UPCF向对端OCS发送SLR-I消息时支持携带Gx-AN-GW-Address。UnsupportCarryANGWAddress：UPCF向对端OCS发送SLR-I消息时不支持携带Gx-AN-GW-Address。 CarryUserLocationInfoSupportCarryUserLocationInfo：UPCF向对端OCS发送SLR-I消息时支持携带Gx-3GPP-User-Location-Info。UnsupportCarryUserLocationInfo：UPCF向对端OCS发送SLR-I消息时不支持携带Gx-3GPP-User-Location-Info。 CarryIMEISupportCarryIMEI：UPCF向对端OCS发送SLR-I消息时支持携带User-Equipment-Info-Type、User-Equipment-Info-Value。UnsupportCarryIMEI：UPCF向对端OCS发送SLR-I消息时不支持携带User-Equipment-Info-Type、User-Equipment-Info-Value。 CarryAPNSupportCarryAPN：UPCF向对端OCS发送SLR-I消息时支持携带Called-Station-ID。UnsupportCarryAPN：UPCF向对端OCS发送SLR-I消息时不支持携带Called-Station-ID。 CarryRATYPESupportCarryRATYPE：UPCF向对端OCS发送SLR-I消息时支持携带Gx-3GPP-RAT-Type。UnsupportCarryRATYPE：UPCF向对端OCS发送SLR-I消息时不支持携带Gx-3GPP-RAT-Type。  说明： 当“能力字典项值”取值为“Supportxxx”时，SLR-I消息会携带以上相应的AVP，AVP携带的信息从关联的Gx或N7会话获取，如果Gx会话没有携带AVP或是N7会话没有携带信元时，SLR-I消息则不携带。当会话恢复触发Sy会话重建时，如果“能力字典项值”取值为“Supportxxx”，SLR-I消息会携带以上相应的AVP，AVP携带的信息从Session备份数据中获取。 |

## 使用实例

1. 查询一条OCS能力项的配置信息。“能力字典ID”为“10”，“能力项ID”为“CarryLocation”。

   ```
   LST OCSABIITEM: ABILITYDICTID=10, ABILITYITEMID=CarryLocation;
   ```

   ```
   %%LST OCSABIITEM: ABILITYDICTID=10, ABILITYITEMID=CarryLocation;%%
   RETCODE = 0  操作成功

   操作结果如下:
   -------------
     能力字典ID  =  10
   能力字典项ID  =  CarryLocation
   能力字典项值  =  UnsupportedCarryLocation
   (结果个数 = 1)

   ---    END
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息和相关参数，各参数含义请参见本命令的参数说明。