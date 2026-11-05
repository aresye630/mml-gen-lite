# 设置全局业务快速恢复配置（SET FASTRECOVERY）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：SGW-C、PGW-C**

该命令主要用于配置快速恢复功能。如果配置成功，当网络侧、MME、SGW发生故障或重启时可以快速恢复业务。

## 注意事项

- 该命令执行后只对新激活用户生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

|   PRTFRQBRKTIME |   HOLDONTIME | NTSRSWITCH   | RESTORPGWSWITCH   | PDTNSWITCH   | RESTORSGWSWITCH   | BROADCASTSWITCH   |
|----------------:|-------------:|:-------------|:------------------|:-------------|:------------------|:------------------|
|             120 |           59 | DISABLE      | DISABLE           | DISABLE      | DISABLE           | DISABLE           |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识            | 参数名称            | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|:----------------|:----------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PRTFRQBRKTIME   | 防闪断定时器时长(秒)     | 可选必选说明：可选参数  参数含义：该参数用于指定防闪断定时器时长。MME故障场景，SGW通过ECHO消息探测发现MME故障，等待防闪断定时器时长后再进行批量保留承载的操作。SGW故障场景，PGW通过ECHO消息探测发现SGW故障，等待防闪断定时器时长后再进行批量保留承载的操作。  数据来源：本端规划  取值范围：整数类型，取值范围是0~300，单位是秒。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST FASTRECOVERY查询当前参数配置值。  配置原则：  该定时器可以防止网络闪断对设备的影响，但同时会增加业务恢复时间，若为快速启动VoLTE业务恢复，可以关闭该定时器，即设置为0。                                                                                                                    |
| HOLDONTIME      | 保留承载的超时时长(分钟)   | 可选必选说明：可选参数  参数含义：该参数用于指定保留承载的超时时长。当保留承载的时长到达配置值时，系统将保留承载删除。  数据来源：本端规划  取值范围：整数类型，取值范围是1~120，单位是分钟。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST FASTRECOVERY查询当前参数配置值。  配置原则：无                                                                                                                                                                                                                                                                   |
| NTSRSWITCH      | 网络侧触发业务恢复功能功能开关 | 可选必选说明：可选参数  参数含义：该参数用于设置是否开启全局的网络侧触发的业务恢复功能。  数据来源：本端规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST FASTRECOVERY查询当前参数配置值。  配置原则： 配置为ENABLE时，对于具备网络侧触发业务恢复功能的用户，在感知MME故障或重启时会保留承载不去活。前置条件：1. SGW上GTP路径配置为S11接口发送echo request消息时通知MME具备网络侧触发业务恢复的能力。2. MME上GTP路径配置为S11接口发送echo request消息时通知SGW具备网络侧触发业务恢复的能力。有保留承载用户存在时允许修改该命令，NTSRSWITCH修改为DISABLE时已经是保留承载的用户等待保留承载定时器超时后删除。                                        |
| RESTORPGWSWITCH | 故障重启业务恢复功能PGW开关 | 可选必选说明：可选参数  参数含义：该参数用于设置PGW是否打开网络侧触发的业务恢复功能。  数据来源：本端规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST FASTRECOVERY查询当前参数配置值。  配置原则：  该参数只对PGW生效，控制PGW是否具备SGW故障重启场景下的业务恢复功能。该参数使能的情况下，PGW支持保留承载。                                                                                                                                                                                                                       |
| PDTNSWITCH      | PDTN功能开关        | 可选必选说明：该参数在"RESTORPGWSWITCH"配置为"ENABLE"时为条件可选参数。  参数含义：该参数用于设置是否打开PGW触发的SGW故障重启场景下的业务恢复功能。  数据来源：本端规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST FASTRECOVERY查询当前参数配置值。  配置原则： 该参数使能的情况下，PGW上的保留承载在收到下行信令或者下行数据时触发向SGW发送PGW Downlink Triggering Notification消息。该参数不使能的情况下，PGW上的保留承载在收到下行信令或者下行数据时不触发PGW Downlink Triggering Notification消息。                                                                         |
| RESTORSGWSWITCH | 故障重启业务恢复功能SGW开关 | 可选必选说明：可选参数  参数含义：该参数用于设置SGW是否打开网络侧触发的业务恢复功能。  数据来源：本端规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST FASTRECOVERY查询当前参数配置值。  配置原则：  该参数使能的情况下，支持收到PGW的PGW Downlink Triggering Notification时向MME发送PGW Downlink Triggering Notification消息和处理MME返回的PGW Downlink Triggering Acknowledge响应消息。                                                                                                                             |
| BROADCASTSWITCH | PDTN广播功能开关      | 可选必选说明：该参数在"RESTORSGWSWITCH"配置为"ENABLE"时为条件可选参数。  参数含义：该参数用于设置当MME发送的PGW Downlink Triggering Acknowledge消息携带context-not-found原因值的失败响应时，SGW是否支持再次向MME POOL中的MME群发PGW Downlink Triggering Notification消息。  数据来源：本端规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST FASTRECOVERY查询当前参数配置值。  配置原则：  该参数使能的情况下，SGW发送PDTN消息后如果收到context-not-found的失败响应并且消息中携带IMSI和MME ID时，SGW会向MME POOL内除响应消息中携带的MME ID以外的其它所有MME再次发送PDTN消息。 |

## 使用实例

若系统刚搭建好，需要配置故障或重启快速业务恢复功能时，进行如下配置：

```
SET FASTRECOVERY:
PRTFRQBRKTIME=30,HOLDONTIME=30,NTSRSWITCH=ENABLE,RESTORPGWSWITCH=ENABLE,PDTNSWITCH=ENABLE,RESTORSGWSWITCH=ENABLE,BROADCASTSWITCH=ENABLE;
```