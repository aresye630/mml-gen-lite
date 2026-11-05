# 增加对端NWDAF信息（ADD PNFNWDAFEVENT）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：AMF、SMF、NSSF、SMSF、NCG、NEF、NWDAF、SCF**

该命令用于增加本地配置对端NWDAF的信息。该命令用于在网络中没有部署NRF，或对端NF没有注册到NRF，或网络中存在NRF但需基于运营商策略本地配置周边NF的场景下，配置对端NF实例相关的信息。

## 注意事项

- 该命令执行后立即生效。

- 最多可输入1024条记录。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识         | 参数名称        | 参数说明                                                                                                                                                   |
|:-------------|:------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------|
| NFINSTANCEID | NF实例标识      | 可选必选说明：必选参数  参数含义：该参数用于唯一指定某一个NWDAF实例。  数据来源：全网规划  取值范围：字符串类型，输入长度范围是1~38。本参数的构成字符只能是字母A~Z或a~z、数字0~9、下划线“_”和中划线“-”，例如，NWDAF_Instance_0。  默认值：无  配置原则：无 |
| NWDAFINFOID  | NwdafInfo标识 | 可选必选说明：可选参数  参数含义：该参数用于唯一标识NWDAF实例中的某个NwdafInfo。  数据来源：本端规划  取值范围：字符串类型，输入长度范围是0~32。该参数大小写不敏感。  默认值：无  配置原则：无                                          |
| NWDAFEVENTS  | NWDAF数据分析事件 | 可选必选说明：必选参数  参数含义：该参数用于指定NWDAF支持的分析事件类型。  数据来源：本端规划 取值范围： QOS_ANALYSIS（QOS分析）QOS_EXP_ANALYSIS（体验感知信息分析）  默认值：无  配置原则：无                                 |

## 使用实例

增加对端NWDAF信息，NF实例标识为NWDAF\_Instance\_1，NwdafInfo标识为central，NWDAF数据分析事件为QOS\_ANALYSIS。

```
ADD PNFNWDAFEVENT: NFINSTANCEID="NWDAF_Instance_1", NWDAFINFOID="central", NWDAFEVENTS=QOS_ANALYSIS-1&QOS_EXP_ANALYSIS-0;
```