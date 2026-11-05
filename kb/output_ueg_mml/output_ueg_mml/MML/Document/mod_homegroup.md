# 修改Home Group（MOD HOMEGROUP）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：PGW-C、GGSN**

该命令用于修改Home Group的优先级、绑定的IMSI/MSISDN号码段组和计费特征组。

## 注意事项

- 该命令执行后立即生效。

- IMSIMSISDNGRPNAME和CCGROUPNAME两个参数必须至少有一个有效。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识            | 参数名称                 | 参数说明                                                                                                                                                                       |
|:----------------|:---------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HOMEGROUPINDX   | Home Group编号         | 可选必选说明：必选参数  参数含义：该参数用于设置Home Group的编号。  数据来源：本端规划  取值范围：整数类型，取值范围是1~128。  默认值：无  配置原则：无                                                                                   |
| HOMEGROUPPRI    | Home Group优先级        | 可选必选说明：可选参数  参数含义：该参数用于设置Home Group的优先级。  数据来源：本端规划  取值范围：整数类型，取值范围是1~65535。值越小优先级越高。  默认值：无  配置原则：无                                                                       |
| IMSIMSISDNSW    | 选择IMSI/MSISDN组开关     | 可选必选说明：可选参数  参数含义：该参数用于控制选择IMSI/MSISDN组。  数据来源：本端规划 取值范围： ENABLE（选择IMSI/MSISDN组）DISABLE（不选择IMSI/MSISDN号段组）  默认值：无  配置原则：无                                                  |
| IMSIMSISDNGRPNM | Home Group绑定的用户号码段组名 | 可选必选说明：该参数在"IMSIMSISDNSW"配置为"ENABLE"时为条件必选参数。  参数含义：该参数用于设置Home Group绑定的IMSI/MSISDN号码段组名。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是1~31。  默认值：无  配置原则：  该参数使用ADD PRIMSIMSISDNG命令配置生成。 |
| CCGROUPSW       | 选择计费属性组              | 可选必选说明：可选参数  参数含义：该参数用于控制选择计费策略组。  数据来源：本端规划 取值范围： ENABLE（选择计费属性组）DISABLE（不选择计费属性组）  默认值：无  配置原则：无                                                                         |
| CCGROUPNAME     | 计费特征组名称              | 可选必选说明：该参数在"CCGROUPSW"配置为"ENABLE"时为条件必选参数。  参数含义：该参数用于设置Home Group绑定的计费特征组名称。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是1~31。  默认值：无  配置原则：  该参数使用ADD CCGROUP命令配置生成。                   |
| MULTIDNNSW      | 2B2C漫游双DNN特性功能开关     | 可选必选说明：可选参数  参数含义：该参数用于HOMEGROUP支持2B2C漫游双DNN特性功能。  数据来源：本端规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：无  配置原则：无                                                                   |

## 使用实例

修改“Home Group编号”为“1”的Home Group配置的“选择计费属性组”为“不选择计费属性组”：

```
MOD HOMEGROUP: HOMEGROUPINDX=1, HOMEGROUPPRI=65535, IMSIMSISDNSW=ENABLE, IMSIMSISDNGRPNM="group1", CCGROUPSW=DISABLE;
```