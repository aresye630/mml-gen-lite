# 检查导入号段配置文件合法性（CHK SEGFILE）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：NRF**

该命令用于核查号段导入文件的数据合法性，建议核查成功后再加载号段文件，否则存在不合法数据时，加载号段文件会失败。

号段文件需要符合一定格式要求，详细请联系华为技术支持。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识           | 参数名称   | 参数说明                                                                                                                                                                                                                                         |
|:---------------|:-------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SEGPACKAGENAME | 号段文件名称 | 可选必选说明：必选参数  参数含义：该参数用于表示号段文件的名称。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是0~64。  默认值：无  配置原则：无                                                                                                                                                         |
| SEGTYPE        | 号段类型   | 可选必选说明：必选参数  参数含义：该参数用于表示号段文件中支持的号段类型。其中ALL代表IMSI、MSISDN、IMSIRT和MSISDNRT。  数据来源：本端规划 取值范围： IMSI（IMSI）MSISDN（MSISDN）IMSIRT（IMSIRT）MSISDNRT（MSISDNRT）ALL（ALL）  默认值：无  配置原则：无                                                                   |
| NFTYPEIMSI     | NF类型   | 可选必选说明：该参数在"SEGTYPE"配置为"IMSI"、"IMSIRT"时为条件必选参数。  参数含义：该参数用于表示IMSI、IMSIRT号段作用的NF类型，即哪些NF类型支持号段文件中给出的IMSI、IMSIRT号段信息。  数据来源：本端规划 取值范围： AUSF（AUSF）PCF（PCF）UDM（UDM）UDR（UDR）CHF（CHF）CUSTOM_OCS（CUSTOM_OCS）AUSFUDM（AUSFUDM）ALL（ALL）  默认值：无  配置原则：无 |
| NFTYPEMSISDN   | NF类型   | 可选必选说明：该参数在"SEGTYPE"配置为"MSISDN"、"MSISDNRT"时为条件必选参数。  参数含义：该参数用于表示MSISDN、MSISDNRT号段作用的NF类型，即哪些NF类型支持号段文件中给出的MSISDN、MSISDNRT号段信息。  数据来源：本端规划 取值范围： PCF（PCF）UDM（UDM）UDR（UDR）CHF（CHF）CUSTOM_OCS（CUSTOM_OCS）ALL（ALL）  默认值：无  配置原则：无               |
| NFTYPEALL      | NF类型   | 可选必选说明：该参数在"SEGTYPE"配置为"ALL"时为条件必选参数。  参数含义：该参数用于表示IMSI和MSISDN号段作用的NF类型，即哪些NF类型支持号段文件中给出的所有号段信息。  数据来源：本端规划 取值范围： AUSF（AUSF）PCF（PCF）UDM（UDM）UDR（UDR）CHF（CHF）CUSTOM_OCS（CUSTOM_OCS）AUSFUDM（AUSFUDM）ALL（ALL）  默认值：无  配置原则：无                    |
| RECNUM         | 错误信息条数 | 可选必选说明：可选参数  参数含义：该参数用于表示指定核查NF类型和号段类型对应导入文件的错误信息条数。  数据来源：本端规划  取值范围：整数类型，取值范围是1~1000，单位是条。  默认值：无  配置原则：无                                                                                                                                  |

## 使用实例

运营商导入号段文件segdata1591149233424568600.zip后在加载号段文件之前核查压缩包中ausf-imsi.dat文件及其数据文件合法性时，执行此命令。

```
%%CHK SEGFILE: SEGPACKAGENAME="segdata1591149233424568600.zip", SEGTYPE=IMSI, NFTYPEIMSI=AUSF, RECNUM=5;%%
RETCODE = 0  操作成功

结果如下
------------------------
号段文件名称                    号段类型  NF类型   核查结果

segdata1591149233424568600.zip  IMSI      ausf     download zip file err,please check file name is right   
(结果个数 = 1)
```