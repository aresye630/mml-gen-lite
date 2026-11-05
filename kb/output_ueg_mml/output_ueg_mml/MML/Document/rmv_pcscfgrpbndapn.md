# 删除APN和P-CSCF组关联关系（RMV PCSCFGRPBNDAPN）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：PGW-C、SMF、GGSN**

此命令用来删除APN和P-CSCF组关联关系，且命令支持多种删除方式。如果DEFAULTFLAG字段的值为DEFAULT，删除APN的缺省P-CSCF Group，如果DEFAULTFLAG字段的值为IMSI\_MSISDN\_SEG，用于解除P-CSCF组与APN的绑定关系。如果P-CSCF组参数的值均为空，解除所有P-CSCF组绑定关系，如果P-CSCF组参数的值不为空，则解除对应P-CSCF组绑定关系。

## 注意事项

- 该命令执行后立即生效。

- 不指定号段，删除APN下缺省P-CSCF组名称绑定关系；指定号段，删除指定号段的P-CSCF组名称绑定。
- 不指定P-CSCF组，删除所有P-CSCF组名称绑定关系；指定P-CSCF组，删除对应P-CSCF组名称绑定关系。
- 删除后的P-CSCF组绑定关系需要满足配置约束。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识          | 参数名称            | 参数说明                                                                                                                                                                                                                                       |
|:--------------|:----------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| APN           | APN名称           | 可选必选说明：必选参数  参数含义：该参数用于指定APN名称。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。  默认值：无  配置原则：  该参数使用ADD CPAPN命令配置生成。              |
| DEFAULTFLAG   | 缺省标记            | 可选必选说明：必选参数  参数含义：该参数用于指定缺省标记。  数据来源：本端规划 取值范围： DEFAULT（缺省）IMSI_MSISDN_SEG（IMSI/MSISDN号段）  默认值：无  配置原则：无                                                                                                                                   |
| IMSIMSISDNSEG | IMSI/MSISDN号段名称 | 可选必选说明：该参数在"DEFAULTFLAG"配置为"IMSI_MSISDN_SEG"时为条件必选参数。  参数含义：该参数用于指定IMSI/MSISDN号段名称。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是1~31。只允许输入字母、数字、“.”、“_”和“-”。字母会被转换为小写字母进行存储和处理。  默认值：无  配置原则：  该参数使用ADD PCSCFIMSISDNSEG命令配置生成。                           |
| MPCSCFGRPIPV4 | 主IPv4 P-CSCF组   | 可选必选说明：可选参数  参数含义：该参数用于配置该APN的主IPv4 P-CSCF组。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是1~63。只允许输入字母、数字、“.”、“_”和“-”。字母会被转换为小写字母进行存储和处理。  默认值：无  配置原则：  该参数由ADD PCSCFGROUP命令配置。  MPCSCFGRPIPV4和MPCSCFGRPIPV6至少填写1个。  MPCSCFGRPIPV4与SPCSCFGRPIPV4不能相同。    |
| SPCSCFGRPIPV4 | 备IPv4 P-CSCF组   | 可选必选说明：可选参数  参数含义：该参数用于配置该APN的备IPv4 P-CSCF组。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是0~63。只允许输入字母、数字、“.”、“_”和“-”。字母会被转换为小写字母进行存储和处理。  默认值：无  配置原则：  该参数使用ADD PCSCFGROUP命令配置生成。  MPCSCFGRPIPV4与SPCSCFGRPIPV4不能相同。                                     |
| MPCSCFGRPIPV6 | 主IPv6 P-CSCF组   | 可选必选说明：可选参数  参数含义：该参数用于配置该APN的主IPv6 P-CSCF组。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是1~63。只允许输入字母、数字、“.”、“_”和“-”。字母会被转换为小写字母进行存储和处理。  默认值：无  配置原则：  该参数使用ADD PCSCFGROUP命令配置生成。  MPCSCFGRPIPV4和MPCSCFGRPIPV6至少填写1个。  MPCSCFGRPIPV6与SPCSCFGRPIPV6不能相同。 |
| SPCSCFGRPIPV6 | 备IPv6 P-CSCF组   | 可选必选说明：可选参数  参数含义：该参数用于配置该APN的备IPv6 P-CSCF组。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是0~63。只允许输入字母、数字、“.”、“_”和“-”。字母会被转换为小写字母进行存储和处理。  默认值：无  配置原则：  该参数使用ADD PCSCFGROUP命令配置生成。  MPCSCFGRPIPV6与SPCSCFGRPIPV6不能相同。                                     |

## 使用实例

- 删除APN下缺省的P-CSCF组绑定关系：

  ```
  RMV PCSCFGRPBNDAPN: APN="huawei.com", DEFAULTFLAG=DEFAULT;
  ```
- 删除APN下指定号段和P-CSCF组绑定关系：

  ```
  RMV PCSCFGRPBNDAPN: APN="huawei.com", DEFAULTFLAG=IMSI_MSISDN_SEG, IMSIMSISDNSEG="imsiseg";
  ```
- 删除APN下缺省的指定P-CSCF组绑定关系：

  ```
  RMV PCSCFGRPBNDAPN: APN="huawei.com", DEFAULTFLAG=DEFAULT, MPCSCFGRPIPV4="group1";
  ```
- 删除APN下指定号段的指定P-CSCF组绑定关系：

  ```
  RMV PCSCFGRPBNDAPN: APN="huawei.com", DEFAULTFLAG=IMSI_MSISDN_SEG, IMSIMSISDNSEG="imsiseg", MPCSCFGRPIPV6="group2", SPCSCFGRPIPV6="group10";
  ```