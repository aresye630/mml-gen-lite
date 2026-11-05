# 设置DDN消息参数以及Delay信元处理开关（SET DDNATTR）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：SGW-C**

该命令用来设置Downlink Data Notification消息中是否支持携带EBI和ARP信元，以及控制SGW-C是否基于DownlinkData Notification Ack消息和Modify Bearer Request消息中的Delay信元进行处理。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| EBI     | EBIVALUE     | ARP     | ARPVALUE     | DELAYSW   |
|:--------|:-------------|:--------|:-------------|:----------|
| Disable | TriDDNBearer | Disable | TriDDNBearer | DISABLE   |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识     | 参数名称        | 参数说明                                                                                                                                                                                                                                                                                                     |
|:---------|:------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| EBI      | 携带EBI       | 可选必选说明：可选参数  参数含义：设置系统是否支持在Downlink Data Notification消息中携带EBI信元。  数据来源：本端规划 取值范围： “Disable（不使能）”：DDN消息中不携带该信元。“Enable（使能）”：DDN消息中携带该信元。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DDNATTR查询当前参数配置值。  配置原则：无                                                                                               |
| EBIVALUE | EBI值        | 可选必选说明：该参数在"EBI"配置为"Enable"时为条件必选参数。  参数含义：设置Downlink Data Notification消息中的EBI信元取值原则。  数据来源：本端规划 取值范围： “TriDDNBearer（触发DDN消息的承载）”：DDN消息中该信元取值为触发DDN消息的承载的ID。“DefaultBearer（缺省承载）”：DDN消息中该信元取值为触发DDN消息的承载所关联的缺省承载的ID。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DDNATTR查询当前参数配置值。  配置原则：无                  |
| ARP      | 携带ARP       | 可选必选说明：可选参数  参数含义：设置系统是否支持在Downlink Data Notification消息中携带ARP信元。  数据来源：全网规划 取值范围： “Disable（不使能）”：DDN消息中不携带该信元。“Enable（使能）”：DDN消息中携带该信元。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DDNATTR查询当前参数配置值。  配置原则：无                                                                                               |
| ARPVALUE | ARP值        | 可选必选说明：该参数在"ARP"配置为"Enable"时为条件必选参数。  参数含义：设置Downlink Data Notification消息中的ARP信元取值原则。  数据来源：本端规划 取值范围： “TriDDNBearer（触发DDN消息的承载）”：DDN消息中该信元取值为触发DDN消息的承载的ID。“DefaultBearer（缺省承载）”：DDN消息中该信元取值为触发DDN消息的承载所关联的缺省承载的ID。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DDNATTR查询当前参数配置值。  配置原则：无                  |
| DELAYSW  | Delay信元处理开关 | 可选必选说明：可选参数  参数含义：该参数用于控制SGW-C是否支持对DownlinkData Notification Ack消息和Modify Bearer Request消息中Delay信元进行处理。如果支持处理，SGW-C会指示SGW-U针对本MME-SGW所在路径所有用户会话延迟发送DDN。  数据来源：本端规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST DDNATTR查询当前参数配置值。  配置原则：  该参数只有当PFCPCMPT命令中Bar参数设置为SUPPORT时才生效。 |

## 使用实例

设置Downlink Data Notification消息中携带EBI信元，并且携带缺省承载的EBI；同时设置消息中携带ARP信元，并且携带缺省承载的ARP；同时设置SGW-C支持对DownlinkData Notification Ack消息和Modify Bearer Request消息中的Delay信元进行处理：

```
SET DDNATTR: EBI=Enable, EBIVALUE=DefaultBearer, ARP=Enable, ARPVALUE=DefaultBearer,DELAYSW=ENABLE;
```