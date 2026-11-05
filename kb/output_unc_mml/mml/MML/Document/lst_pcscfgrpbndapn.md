# 查询APN和P-CSCF组关联关系（LST PCSCFGRPBNDAPN）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于查询APN与P-CSCF组之间的关系。可基于IMSI/MSISDN号段查询。

## 注意事项

无

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

## 参数说明

| 参数标识          | 参数名称            | 参数说明                                                                                                                                                                                                                        |
|:--------------|:----------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| APN           | APN名称           | 可选必选说明：可选参数  参数含义：该参数用于指定APN名称。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是1~63。只能由“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”。不支持空格及“_”、“#”、“$”、“&”、“%”、“^”、“（”、“）”、“，”、“/”、“;”、“:”、“””、“`”等特殊字符，不区分大小写。  默认值：无  配置原则：  该参数使用ADD APN命令配置生成。 |
| IMSIMSISDNSEG | IMSI/MSISDN号段名称 | 可选必选说明：可选参数  参数含义：该参数用于指定IMSI/MSISDN号段名称。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是1~31。只允许输入字母、数字、“.”、“_”和“-”。字母会被转换为小写字母进行存储和处理。  默认值：无  配置原则：  该参数使用ADD PCSCFIMSISDNSEG命令配置生成。                                                      |

## 使用实例

- 查询指定APN下所有的P-CSCF组绑定关系：

  ```
  LST PCSCFGRPBNDAPN: APN="huawei.com";
  RETCODE = 0  操作成功

  结果如下
  --------
  APN名称     IMSI/MSISDN号段名称  缺省标记         优先级  主IPv4P-CSCF组  备IPv4P-CSCF组  主IPv6P-CSCF组  备IPv6P-CSCF组  

  huawei.com  NULL                 缺省             0       mygroup         NULL            NULL            NULL            
  huawei.com  mypcscfimsisdnseg    IMSI/MSISDN号段  1       mygroup         NULL            NULL            NULL            
  (结果个数 = 2)

  ---    END
  ```
- 查询APN下指定号段和P-CSCF组绑定关系：

  ```
  LST PCSCFGRPBNDAPN: APN="huawei.com", IMSIMSISDNSEG="mypcscfimsisdnseg";
  RETCODE = 0  操作成功

  结果如下
  --------
              APN名称  =  huawei.com
  IMSI/MSISDN号段名称  =  mypcscfimsisdnseg
             缺省标记  =  IMSI/MSISDN号段
               优先级  =  1
       主IPv4P-CSCF组  =  mygroup
       备IPv4P-CSCF组  =  NULL
       主IPv6P-CSCF组  =  NULL
       备IPv6P-CSCF组  =  NULL
  (结果个数 = 1)

  ---    END
  ```

## 输出结果说明

| 输出项名称           | 输出项解释                                                                                                                                                                 |
|:----------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| APN名称           | 该参数用于指定APN名称。                                                                                                                                                         |
| IMSI/MSISDN号段名称 | 该参数用于指定IMSI/MSISDN号段名称。                                                                                                                                               |
| 缺省标记            | 该参数用于标识P-CSCF组是全局缺省配置，还是定制号段的。在业务处理过程中，如果指定APN的IMS功能开关为开（SET APNIMSATTR的IMSSWITCH参数配置为ENABLE），则优先按照APN下的P-CSCF组和号段的绑定关系进行P-CSCF组选择，只有当所有号段都匹配不成功时，才会选用APN下的缺省P-CSCF组。 |
| 优先级             | 用于指定P-CSCF分组与号段绑定关系的优先级，优先级不能重复。当一个IMSI/MSISDN匹配到两个或两个以上的P-CSCF组时，UNC优先选择优先级最高的P-CSCF组。                                                                               |
| 主IPv4P-CSCF组    | 该参数用于配置该APN的主IPv4 P-CSCF组。                                                                                                                                            |
| 备IPv4P-CSCF组    | 该参数用于配置该APN的备IPv4 P-CSCF组。                                                                                                                                            |
| 主IPv6P-CSCF组    | 该参数用于配置该APN的主IPv6 P-CSCF组。                                                                                                                                            |
| 备IPv6P-CSCF组    | 该参数用于配置该APN的备IPv6 P-CSCF组。                                                                                                                                            |