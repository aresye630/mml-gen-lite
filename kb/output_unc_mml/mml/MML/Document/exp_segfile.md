# 导出号段文件（EXP SEGFILE）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：NRF**

该命令用于将已经导入到NRF系统中的号段数据导出成二进制文件并打包成压缩文件，导出的文件通过“系统->文件传输->NRF号段导出文件”下载。

## 注意事项

该命令执行后立即生效。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识         | 参数名称   | 参数说明                                                                                                                                                                                                                                         |
|:-------------|:-------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SEGTYPE      | 号段类型   | 可选必选说明：必选参数  参数含义：该参数用于表示号段类型。  数据来源：本端规划 取值范围： IMSI（IMSI）MSISDN（MSISDN）IMSIRT（IMSIRT）MSISDNRT（MSISDNRT）ALL（ALL）  默认值：无  配置原则：无                                                                                                              |
| NFTYPEIMSI   | NF类型   | 可选必选说明：该参数在"SEGTYPE"配置为"IMSI"、"IMSIRT"时为条件必选参数。  参数含义：该参数用于表示IMSI、IMSIRT号段作用的NF类型，即哪些NF类型支持号段文件中给出的IMSI、IMSIRT号段信息。  数据来源：本端规划 取值范围： AUSF（AUSF）PCF（PCF）UDM（UDM）UDR（UDR）CHF（CHF）CUSTOM_OCS（CUSTOM_OCS）AUSFUDM（AUSFUDM）ALL（ALL）  默认值：无  配置原则：无 |
| NFTYPEMSISDN | NF类型   | 可选必选说明：该参数在"SEGTYPE"配置为"MSISDN"、"MSISDNRT"时为条件必选参数。  参数含义：该参数用于表示MSISDN、MSISDNRT号段作用的NF类型，即哪些NF类型支持号段文件中给出的MSISDN、MSISDNRT号段信息。  数据来源：本端规划 取值范围： PCF（PCF）UDM（UDM）UDR（UDR）CHF（CHF）CUSTOM_OCS（CUSTOM_OCS）ALL（ALL）  默认值：无  配置原则：无               |
| NFTYPEALL    | NF类型   | 可选必选说明：该参数在"SEGTYPE"配置为"ALL"时为条件必选参数。  参数含义：该参数用于表示所有类型的号段。  数据来源：本端规划 取值范围： AUSF（AUSF）PCF（PCF）UDM（UDM）UDR（UDR）CHF（CHF）CUSTOM_OCS（CUSTOM_OCS）AUSFUDM（AUSFUDM）ALL（ALL）  默认值：无  配置原则：无                                                         |

## 使用实例

导出号段类型为IMSI的号段文件：

```
EXP SEGFILE: SEGTYPE=IMSI, NFTYPEIMSI=AUSF;
```