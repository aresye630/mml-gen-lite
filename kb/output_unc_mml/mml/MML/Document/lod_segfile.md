# 加载号段文件（LOD SEGFILE）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：NRF**

该命令用于加载IMSI、MSISDN、IMSIRT和MSISDNRT号段文件，加载成功后，号段文件会存储在号段数据备表中。

号段文件导入方式为：登录华为操作维护系统（OM Portal），通过“系统->文件传输->NRF号段导入文件”上传导入。

当运营商希望通过在NRF上配置服务提供方NF支持的大量IMSI、MSISDN、IMSIRT和MSISDNRT号段信息时，需要号段文件方式，避免手动逐条执行号段配置命令，提高效率。

系统通过A、B两个表实现号段文件的号段配置，A、B表状态分别互为主备，系统使用的当前系统的主表，表示某一NF支持的某类型的号段信息，对应的当前备表状态的表用于后续刷新NF支持的号段信息。初始时，两个表内容为空。系统只使用标识为主表中的号段配置数据，如果需要刷新号段配置数据（号段文件承载），新号段文件先通过此命令加载到当前备表，然后通过ACT SEGFILE命令将备表激活成主表，同时主表变成备表，此时系统开始使用新的号段配置数据。后续号段配置数据刷新方式同理。

号段文件需要符合一定格式要求，详细请联系华为技术支持。

## 注意事项

- 该命令执行后立即生效。

- 主备或双活组网的场景下，如果需要配置此命令，则两个NRF上均需执行此命令，且配置参数一致。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识           | 参数名称   | 参数说明                                                                                                                                                                                                                                         |
|:---------------|:-------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SEGPACKAGENAME | 号段文件名称 | 可选必选说明：必选参数  参数含义：该参数用于表示号段文件的名称。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是0~64。  默认值：无  配置原则：无                                                                                                                                                         |
| SEGTYPE        | 号段类型   | 可选必选说明：必选参数  参数含义：该参数用于表示号段类型。其中ALL代表IMSI、MSISDN、IMSIRT和MSISDNRT。  数据来源：本端规划 取值范围： IMSI（IMSI）MSISDN（MSISDN）IMSIRT（IMSIRT）MSISDNRT（MSISDNRT）ALL（ALL）  默认值：无  配置原则：无                                                                           |
| NFTYPEIMSI     | NF类型   | 可选必选说明：该参数在"SEGTYPE"配置为"IMSI"、"IMSIRT"时为条件必选参数。  参数含义：该参数用于表示IMSI、IMSIRT号段作用的NF类型，即哪些NF类型支持号段文件中给出的IMSI、IMSIRT号段信息。  数据来源：本端规划 取值范围： AUSF（AUSF）PCF（PCF）UDM（UDM）UDR（UDR）CHF（CHF）CUSTOM_OCS（CUSTOM_OCS）AUSFUDM（AUSFUDM）ALL（ALL）  默认值：无  配置原则：无 |
| NFTYPEMSISDN   | NF类型   | 可选必选说明：该参数在"SEGTYPE"配置为"MSISDN"、"MSISDNRT"时为条件必选参数。  参数含义：该参数用于表示MSISDN、MSISDNRT号段作用的NF类型，即哪些NF类型支持号段文件中给出的MSISDN、MSISDNRT号段信息。  数据来源：本端规划 取值范围： PCF（PCF）UDM（UDM）UDR（UDR）CHF（CHF）CUSTOM_OCS（CUSTOM_OCS）ALL（ALL）  默认值：无  配置原则：无               |
| NFTYPEALL      | NF类型   | 可选必选说明：该参数在"SEGTYPE"配置为"ALL"时为条件必选参数。  参数含义：该参数用于表示IMSI、MSISDN、IMSIRT和MSISDNRT号段作用的NF类型，即哪些NF类型支持号段文件中给出的所有号段信息。  数据来源：本端规划 取值范围： AUSF（AUSF）PCF（PCF）UDM（UDM）UDR（UDR）CHF（CHF）CUSTOM_OCS（CUSTOM_OCS）AUSFUDM（AUSFUDM）ALL（ALL）  默认值：无  配置原则：无    |

## 使用实例

运营商使用号段文件（名称为segpackage01）方式更新UDR支持的IMSI号段信息。通过此命令首先实现号段文件的加载。

```
LOD SEGFILE: SEGPACKAGENAME="segpackage01", SEGTYPE=IMSI, NFTYPEIMSI=UDR;
```