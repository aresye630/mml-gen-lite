# 设置字段映射关系（SET CDRFIELDTYPE）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：NCG**

该命令用于设置字段映射关系。

## 注意事项

- 该命令执行后立即生效。

- 该命令存在系统初始记录，参数的初始设置值如下。
- 当字段名称（FIELDNAME）为“RATTYPE”，RAT类型名称（RATTYPENAME）为“NR”，SSC类型名称（SSCTYPENAME）为“SSC\_MODE\_1”，PDU类型名称（PDUTYPENAME）为“IPV4”时，类型取值（TYPEVALUE）为51。
- 当字段名称（FIELDNAME）为“RATTYPE”，RAT类型名称（RATTYPENAME）为“EUTRA”，SSC类型名称（SSCTYPENAME）为“SSC\_MODE\_1”，PDU类型名称（PDUTYPENAME）为“IPV4”时，类型取值（TYPEVALUE）为6。
- 当字段名称（FIELDNAME）为“RATTYPE”，RAT类型名称（RATTYPENAME）为“WLAN”，SSC类型名称（SSCTYPENAME）为“SSC\_MODE\_1”，PDU类型名称（PDUTYPENAME）为“IPV4”时，类型取值（TYPEVALUE）为3。
- 当字段名称（FIELDNAME）为“RATTYPE”，RAT类型名称（RATTYPENAME）为“VIRTUAL”，SSC类型名称（SSCTYPENAME）为“SSC\_MODE\_1”，PDU类型名称（PDUTYPENAME）为“IPV4”时，类型取值（TYPEVALUE）为7。
- 当字段名称（FIELDNAME）为“RATTYPE”，RAT类型名称（RATTYPENAME）为“GERA”，SSC类型名称（SSCTYPENAME）为“SSC\_MODE\_1”，PDU类型名称（PDUTYPENAME）为“IPV4”时，类型取值（TYPEVALUE）为2。
- 当字段名称（FIELDNAME）为“RATTYPE”，RAT类型名称（RATTYPENAME）为“NBIOT”，SSC类型名称（SSCTYPENAME）为“SSC\_MODE\_1”，PDU类型名称（PDUTYPENAME）为“IPV4”时，类型取值（TYPEVALUE）为8。
- 当字段名称（FIELDNAME）为“RATTYPE”，RAT类型名称（RATTYPENAME）为“LTE\_M”，SSC类型名称（SSCTYPENAME）为“SSC\_MODE\_1”，PDU类型名称（PDUTYPENAME）为“IPV4”时，类型取值（TYPEVALUE）为9。
- 当字段名称（FIELDNAME）为“RATTYPE”，RAT类型名称（RATTYPENAME）为“UTRA”，SSC类型名称（SSCTYPENAME）为“SSC\_MODE\_1”，PDU类型名称（PDUTYPENAME）为“IPV4”时，类型取值（TYPEVALUE）为1。
- 当字段名称（FIELDNAME）为“SSCMODE”，RAT类型名称（RATTYPENAME）为“NR”，SSC类型名称（SSCTYPENAME）为“SSC\_MODE\_1”，PDU类型名称（PDUTYPENAME）为“IPV4”时，类型取值（TYPEVALUE）为1。
- 当字段名称（FIELDNAME）为“SSCMODE”，RAT类型名称（RATTYPENAME）为“NR”，SSC类型名称（SSCTYPENAME）为“SSC\_MODE\_2”，PDU类型名称（PDUTYPENAME）为“IPV4”时，类型取值（TYPEVALUE）为2。
- 当字段名称（FIELDNAME）为“SSCMODE”，RAT类型名称（RATTYPENAME）为“NR”，SSC类型名称（SSCTYPENAME）为“SSC\_MODE\_3”，PDU类型名称（PDUTYPENAME）为“IPV4”时，类型取值（TYPEVALUE）为3。
- 当字段名称（FIELDNAME）为“PDUSESSIONTYPE”，RAT类型名称（RATTYPENAME）为“NR”，SSC类型名称（SSCTYPENAME）为“SSC\_MODE\_1”，PDU类型名称（PDUTYPENAME）为“IPV4”时，类型取值（TYPEVALUE）为1。
- 当字段名称（FIELDNAME）为“PDUSESSIONTYPE”，RAT类型名称（RATTYPENAME）为“NR”，SSC类型名称（SSCTYPENAME）为“SSC\_MODE\_1”，PDU类型名称（PDUTYPENAME）为“IPV6”时，类型取值（TYPEVALUE）为2。
- 当字段名称（FIELDNAME）为“PDUSESSIONTYPE”，RAT类型名称（RATTYPENAME）为“NR”，SSC类型名称（SSCTYPENAME）为“SSC\_MODE\_1”，PDU类型名称（PDUTYPENAME）为“IPV4V6”时，类型取值（TYPEVALUE）为0。
- 当字段名称（FIELDNAME）为“PDUSESSIONTYPE”，RAT类型名称（RATTYPENAME）为“NR”，SSC类型名称（SSCTYPENAME）为“SSC\_MODE\_1”，PDU类型名称（PDUTYPENAME）为“UNSTRUCTURED”时，类型取值（TYPEVALUE）为3。
- 当字段名称（FIELDNAME）为“PDUSESSIONTYPE”，RAT类型名称（RATTYPENAME）为“NR”，SSC类型名称（SSCTYPENAME）为“SSC\_MODE\_1”，PDU类型名称（PDUTYPENAME）为“ETHERNET”时，类型取值（TYPEVALUE）为4。
- 当字段名称（FIELDNAME）为“PDUSESSIONTYPE”，RAT类型名称（RATTYPENAME）为“NR”，SSC类型名称（SSCTYPENAME）为“SSC\_MODE\_1”，PDU类型名称（PDUTYPENAME）为“NONIP”时，类型取值（TYPEVALUE）为50。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| FIELDNAME      | RATTYPENAME   | SSCTYPENAME   | PDUTYPENAME   |   TYPEVALUE |
|:---------------|:--------------|:--------------|:--------------|------------:|
| RATTYPE        | NR            | SSC_MODE_1    | IPV4          |          51 |
| RATTYPE        | EUTRA         | SSC_MODE_1    | IPV4          |           6 |
| RATTYPE        | WLAN          | SSC_MODE_1    | IPV4          |           3 |
| RATTYPE        | VIRTUAL       | SSC_MODE_1    | IPV4          |           7 |
| RATTYPE        | GERA          | SSC_MODE_1    | IPV4          |           2 |
| RATTYPE        | NBIOT         | SSC_MODE_1    | IPV4          |           8 |
| RATTYPE        | LTE_M         | SSC_MODE_1    | IPV4          |           9 |
| RATTYPE        | UTRA          | SSC_MODE_1    | IPV4          |           1 |
| SSCMODE        | NR            | SSC_MODE_1    | IPV4          |           1 |
| SSCMODE        | NR            | SSC_MODE_2    | IPV4          |           2 |
| SSCMODE        | NR            | SSC_MODE_3    | IPV4          |           3 |
| PDUSESSIONTYPE | NR            | SSC_MODE_1    | IPV4          |           1 |
| PDUSESSIONTYPE | NR            | SSC_MODE_1    | IPV6          |           2 |
| PDUSESSIONTYPE | NR            | SSC_MODE_1    | IPV4V6        |           0 |
| PDUSESSIONTYPE | NR            | SSC_MODE_1    | UNSTRUCTURED  |           3 |
| PDUSESSIONTYPE | NR            | SSC_MODE_1    | ETHERNET      |           4 |
| PDUSESSIONTYPE | NR            | SSC_MODE_1    | NONIP         |          50 |
| RATTYPE        | NR_REDCAP     | SSC_MODE_1    | IPV4          |          58 |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识        | 参数名称    | 参数说明                                                                                                                                                                                                                                                                                                                         |
|:------------|:--------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| FIELDNAME   | 字段名称    | 可选必选说明：必选参数  参数含义：该参数用于指定字段名称。  数据来源：本端规划 取值范围： RATTYPE（RAT类型）SSCMODE（SSC模式）PDUSESSIONTYPE（PDU会话类型）  默认值：无。  配置原则：无                                                                                                                                                                                                          |
| RATTYPENAME | RAT类型名称 | 可选必选说明：该参数在"FIELDNAME"配置为"RATTYPE"时为条件必选参数。  参数含义：该参数用于指定RAT类型名称。  数据来源：本端规划 取值范围： NR（New Radio）EUTRA（Evolved Universal Terrestrial Radio Access）WLAN（Wireless LAN）VIRTUAL（Virtual）GERA（GERA）NBIOT（NB IoT）LTE_M（LTE-M）UTRA（UTRA）NR_REDCAP（NR_REDCAP）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CDRFIELDTYPE查询当前参数配置值。  配置原则：无 |
| SSCTYPENAME | SSC类型名称 | 可选必选说明：该参数在"FIELDNAME"配置为"SSCMODE"时为条件必选参数。  参数含义：该参数用于指定SSC类型名称。  数据来源：本端规划 取值范围： SSC_MODE_1（SSCMode 1）SSC_MODE_2（SSCMode 2）SSC_MODE_3（SSCMode 3）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CDRFIELDTYPE查询当前参数配置值。  配置原则：无                                                                                                   |
| PDUTYPENAME | PDU类型名称 | 可选必选说明：该参数在"FIELDNAME"配置为"PDUSESSIONTYPE"时为条件必选参数。  参数含义：该参数用于指定PDU类型名称。  数据来源：本端规划 取值范围： IPV4（IPv4）IPV6（IPv6）IPV4V6（IPv4v6）UNSTRUCTURED（Unstructured）ETHERNET（Ethernet）NONIP（Non-IP）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CDRFIELDTYPE查询当前参数配置值。  配置原则：无                                                                |
| TYPEVALUE   | 类型取值    | 可选必选说明：可选参数  参数含义：该参数用于指定类型取值。  数据来源：本端规划  取值范围：整数类型，取值范围是0~255。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST CDRFIELDTYPE查询当前参数配置值。  配置原则：无                                                                                                                                                                                     |

## 使用实例

设置字段映射关系：

```
SET CDRFIELDTYPE: FIELDNAME=RATTYPE, RATTYPENAME=NR, TYPEVALUE=52;
```