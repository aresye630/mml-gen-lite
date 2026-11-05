# 修改APN和P-CSCF组关联关系（MOD PCSCFGRPBNDAPN）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：PGW-C、SMF、GGSN**

此命令用来修改APN和P-CSCF组关联关系。

## 注意事项

- 该命令执行后立即生效。

- 可以修改已经配置的优先级的数值，但是必须保持唯一。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识          | 参数名称            | 参数说明                                                                                                                                                                                                                                       |
|:--------------|:----------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| APN           | APN名称           | 可选必选说明：必选参数  参数含义：该参数用于指定APN名称。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。  默认值：无  配置原则：  该参数使用ADD CPAPN命令配置生成。              |
| DEFAULTFLAG   | 缺省标记            | 可选必选说明：必选参数  参数含义：该参数用于指定缺省标记。  数据来源：本端规划 取值范围： DEFAULT（缺省）IMSI_MSISDN_SEG（IMSI/MSISDN号段）  默认值：无  配置原则：无                                                                                                                                   |
| IMSIMSISDNSEG | IMSI/MSISDN号段名称 | 可选必选说明：该参数在"DEFAULTFLAG"配置为"IMSI_MSISDN_SEG"时为条件必选参数。  参数含义：该参数用于指定IMSI/MSISDN号段名称。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是1~31。只允许输入字母、数字、“.”、“_”和“-”。字母会被转换为小写字母进行存储和处理。  默认值：无  配置原则：  该参数使用ADD PCSCFIMSISDNSEG命令配置生成。                           |
| PRIORITY      | 优先级             | 可选必选说明：该参数在"DEFAULTFLAG"配置为"IMSI_MSISDN_SEG"时为条件可选参数。  参数含义：该参数用于指定一个不重复的优先级。当一个IMSI/MSISDN匹配到两个或两个以上的P-CSCF组时，UNC优先选择优先级最高的P-CSCF组。  数据来源：本端规划  取值范围：整数类型，取值范围是1~65535。优先级不能重复。  默认值：无  配置原则：  取值越小，优先级越高。                                |
| MPCSCFGRPIPV4 | 主IPv4 P-CSCF组   | 可选必选说明：可选参数  参数含义：该参数用于配置该APN的主IPv4 P-CSCF组。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是1~63。只允许输入字母、数字、“.”、“_”和“-”。字母会被转换为小写字母进行存储和处理。  默认值：无  配置原则：  该参数由ADD PCSCFGROUP命令配置。  MPCSCFGRPIPV4和MPCSCFGRPIPV6至少填写1个。  MPCSCFGRPIPV4与SPCSCFGRPIPV4不能相同。    |
| SPCSCFGRPIPV4 | 备IPv4 P-CSCF组   | 可选必选说明：可选参数  参数含义：该参数用于配置该APN的备IPv4 P-CSCF组。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是0~63。只允许输入字母、数字、“.”、“_”和“-”。字母会被转换为小写字母进行存储和处理。  默认值：无  配置原则：  该参数使用ADD PCSCFGROUP命令配置生成。  MPCSCFGRPIPV4与SPCSCFGRPIPV4不能相同。                                     |
| MPCSCFGRPIPV6 | 主IPv6 P-CSCF组   | 可选必选说明：可选参数  参数含义：该参数用于配置该APN的主IPv6 P-CSCF组。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是1~63。只允许输入字母、数字、“.”、“_”和“-”。字母会被转换为小写字母进行存储和处理。  默认值：无  配置原则：  该参数使用ADD PCSCFGROUP命令配置生成。  MPCSCFGRPIPV4和MPCSCFGRPIPV6至少填写1个。  MPCSCFGRPIPV6与SPCSCFGRPIPV6不能相同。 |
| SPCSCFGRPIPV6 | 备IPv6 P-CSCF组   | 可选必选说明：可选参数  参数含义：该参数用于配置该APN的备IPv6 P-CSCF组。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是0~63。只允许输入字母、数字、“.”、“_”和“-”。字母会被转换为小写字母进行存储和处理。  默认值：无  配置原则：  该参数使用ADD PCSCFGROUP命令配置生成。  MPCSCFGRPIPV6与SPCSCFGRPIPV6不能相同。                                     |

## 使用实例

- 修改APN下某固定号段和P-CSCF组的绑定关系，将优先级为10，主IPv4 P-CSCF组group1，备IPv4 P-CSCF组group2，主IPv6 P-CSCF组group10，IPv6 P-CSCF组group11，绑定到APN名为huawei.com，号段名为imsiseg的固定号段上：

  ```
  MOD PCSCFGRPBNDAPN: APN="huawei.com", DEFAULTFLAG=IMSI_MSISDN_SEG, IMSIMSISDNSEG="imsiseg", PRIORITY=10, MPCSCFGRPIPV4="group1", SPCSCFGRPIPV4="group2", MPCSCFGRPIPV6="group10", SPCSCFGRPIPV6="group11";
  ```
- 修改APN下缺省的P-CSCF组绑定关系为主IPv4 P-CSCF组group1，备IPv4 P-CSCF组group2，主IPv6 P-CSCF组group10，IPv6 P-CSCF组group11：

  ```
  MOD PCSCFGRPBNDAPN: APN="huawei.com", DEFAULTFLAG=DEFAULT, MPCSCFGRPIPV4="group1", SPCSCFGRPIPV4="group2", MPCSCFGRPIPV6="group10", SPCSCFGRPIPV6="group11";
  ```