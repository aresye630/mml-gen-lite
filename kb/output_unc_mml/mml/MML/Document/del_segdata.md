# 删除号段数据（DEL SEGDATA）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：NRF**

该命令用于删除某一NF支持的特定类型的备表中的号段数据，仅适用于号段文件的方式。

当运营商不想再使用规划好待使用的号段数据时，可以使用此命令删除规划数据。

## 注意事项

- 该命令执行后立即生效。

- 执行此命令不影响当前使用的主表中的数据，删除的内容仅为备表中规划待使用的数据。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识         | 参数名称   | 参数说明                                                                                                                                                                                                                                         |
|:-------------|:-------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SEGTYPE      | 号段类型   | 可选必选说明：必选参数  参数含义：该参数用于表示号段类型。  数据来源：本端规划 取值范围： IMSI（IMSI）MSISDN（MSISDN）IMSIRT（IMSIRT）MSISDNRT（MSISDNRT）ALL（ALL）  默认值：无  配置原则：无                                                                                                              |
| NFTYPEIMSI   | NF类型   | 可选必选说明：该参数在"SEGTYPE"配置为"IMSI"、"IMSIRT"时为条件必选参数。  参数含义：该参数用于表示IMSI、IMSIRT号段作用的NF类型，即哪些NF类型支持号段文件中给出的IMSI、IMSIRT号段信息。  数据来源：本端规划 取值范围： AUSF（AUSF）PCF（PCF）UDM（UDM）UDR（UDR）CHF（CHF）CUSTOM_OCS（CUSTOM_OCS）AUSFUDM（AUSFUDM）ALL（ALL）  默认值：无  配置原则：无 |
| NFTYPEMSISDN | NF类型   | 可选必选说明：该参数在"SEGTYPE"配置为"MSISDN"、"MSISDNRT"时为条件必选参数。  参数含义：该参数用于表示MSISDN、MSISDNRT号段作用的NF类型，即哪些NF类型支持号段文件中给出的MSISDN、MSISDNRT号段信息。  数据来源：本端规划 取值范围： PCF（PCF）UDM（UDM）UDR（UDR）CHF（CHF）CUSTOM_OCS（CUSTOM_OCS）ALL（ALL）  默认值：无  配置原则：无               |
| NFTYPEALL    | NF类型   | 可选必选说明：该参数在"SEGTYPE"配置为"ALL"时为条件必选参数。  参数含义：该参数用于表示IMSI、MSISDN、IMSIRT和MSISDNRT号段作用的NF类型，即哪些NF类型支持号段文件中给出的所有号段信息。  数据来源：本端规划 取值范围： AUSF（AUSF）PCF（PCF）UDM（UDM）UDR（UDR）CHF（CHF）CUSTOM_OCS（CUSTOM_OCS）AUSFUDM（AUSFUDM）ALL（ALL）  默认值：无  配置原则：无    |

## 使用实例

运营商之前规划了UDM支持的IMSI号段信息，规划数据已加载未激活。运营商想重新规划UDM支持的号段信息，不再使用之前的规划数据，需要执行此命令删除之前规划的号段数据。

```
DEL SEGDATA: SEGTYPE=IMSI, NFTYPEIMSI=UDM;
```