# 设置通用会话拓展功能（SET SMCOMMFUNC）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：SGW-C、PGW-C、SMF、GGSN**

此命令用于设置通用会话管理扩展功能。

## 注意事项

- 该命令执行后立即生效。

- GAGYCHGSW参数配置成不使能会导致GaGy计费功能不可用，请谨慎修改参数取值。
- PCRFQRYSW参数配置仅在RESTFULQRYSW参数配置开启时生效，如需支持通过Restful查询非异网漫游或非国漫场景下PCRF的地址，需先开启RESTFULQRYSW参数，再开启PCRFQRYSW。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| LOCREPORT   | RTBEHINDMSSW   | MULTIDNNSW   | UDMDEREGINSID   | PGWRNSSWITCH   | QOSANASW   | GAGYCHGSW   | RESTFULQRYSW   | QOSEXPSW   | LOCATIONCHSW   | EXPOSURELOCRPT   | PCRFQRYSW   |
|:------------|:---------------|:-------------|:----------------|:---------------|:-----------|:------------|:---------------|:-----------|:---------------|:-----------------|:------------|
| NotSupport  | DISABLE        | NotSupport   | DISABLE         | DISABLE        | NotSupport | ENABLE      | NotSupport     | NotSupport | NotSupport     | NotSupport       | NotSupport  |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识           | 参数名称                    | 参数说明                                                                                                                                                                                                                                                                                                                                   |
|:---------------|:------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| LOCREPORT      | 位置上报                    | 可选必选说明：可选参数  参数含义：该参数用于指定SMF/PGW-C/GGSN是否支持位置上报。若该参数配置为Support，当PCF/PCRF等网元下发位置TRIGGER时，SMF/PGW-C/GGSN会向AMF/MME/SGSN发起位置订阅，并且当AMF/MME/SGSN向SMF/PGW/GGSN上报位置时，SMF/PGW-C/GGSN会通知给PCF/PCRF。若该参数配置为NotSupport，则不会发起位置订阅。  数据来源：本端规划 取值范围： NotSupport（不支持）Support（支持）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMCOMMFUNC查询当前参数配置值。  配置原则：无 |
| RTBEHINDMSSW   | 手机后路由功能开关               | 可选必选说明：可选参数  参数含义：该参数用于设置是否支持从本地配置中获取手机后路由信息。  数据来源：本端规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMCOMMFUNC查询当前参数配置值。  配置原则：无                                                                                                                                                                            |
| MULTIDNNSW     | 2B2C漫游双DNN特性开关          | 可选必选说明：可选参数  参数含义：该参数用于指定SMF/PGW-C是否支持2B2C漫游双DNN特性。  数据来源：本端规划 取值范围： NotSupport（不支持）Support（支持）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMCOMMFUNC查询当前参数配置值。  配置原则：  如果修改该参数，仅对新激活的用户生效。                                                                                                                                              |
| UDMDEREGINSID  | 携带实例ID向UDM发起去注册         | 可选必选说明：可选参数  参数含义：该参数用于设置SMF是否携带实例ID向UDM发起去注册请求。  数据来源：全网规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMCOMMFUNC查询当前参数配置值。  配置原则：无                                                                                                                                                                         |
| PGWRNSSWITCH   | PGW重定向功能开关              | 可选必选说明：可选参数  参数含义：该参数用于指示SGW是否支持PGW重定向功能。  数据来源：本端规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMCOMMFUNC查询当前参数配置值。  配置原则：  该开关仅适用于独立部署的SGW-C。                                                                                                                                                             |
| QOSANASW       | QoS质差分析开关               | 可选必选说明：可选参数  参数含义：该参数用于设置SMF是否支持QoS质差分析。  数据来源：全网规划 取值范围： NotSupport（不支持）Support（支持）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMCOMMFUNC查询当前参数配置值。  配置原则：  如果需要使能质差分析能力开放订阅功能，需要执行SET SMFFUNC将EVENTEXPOSURE配置为Support。                                                                                                                 |
| GAGYCHGSW      | GaGy计费功能开关              | 可选必选说明：可选参数  参数含义：该参数用于控制是否支持GaGy计费功能。  数据来源：本端规划 取值范围： “ENABLE（使能）”：使能“DISABLE（去使能）”：去使能  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMCOMMFUNC查询当前参数配置值。  配置原则：  该参数配置成不使能会导致GaGy计费功能不可用，请谨慎修改参数取值。                                                                                                                                     |
| RESTFULQRYSW   | Restful接口查询PCF/PCRF地址开关 | 可选必选说明：可选参数  参数含义：该参数用于设置SMF/PGW-C是否支持Restful接口查询PCF/PCRF地址。 如果该开关配置为不支持时，会直接给SBC回复500，并且不携带PCF/PCRF地址。  数据来源：全网规划 取值范围： NotSupport（不支持）Support（支持）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMCOMMFUNC查询当前参数配置值。  配置原则：无                                                                                                              |
| QOSEXPSW       | 体验感知信息采集订阅开关            | 可选必选说明：可选参数  参数含义：该参数用于指定SMF是否支持体验感知信息采集事件订阅。  数据来源：全网规划 取值范围： NotSupport（不支持）Support（支持）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMCOMMFUNC查询当前参数配置值。  配置原则：  如果修改该参数，仅对新激活的用户生效。                                                                                                                                                    |
| LOCATIONCHSW   | 位置变更订阅开关                | 可选必选说明：可选参数  参数含义：该参数用于指定SMF是否支持位置变更相关事件订阅。位置变更相关事件包括SCELL_CH、SAREA_CH和SCNN_CH。  数据来源：全网规划 取值范围： NotSupport（不支持）Support（支持）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMCOMMFUNC查询当前参数配置值。  配置原则：无                                                                                                                                      |
| EXPOSURELOCRPT | 能力开放位置上报                | 可选必选说明：可选参数  参数含义：该参数用于指定SMF是否支持由能力开放订阅触发位置上报。  数据来源：本端规划 取值范围： NotSupport（不支持）Support（支持）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMCOMMFUNC查询当前参数配置值。  配置原则：无                                                                                                                                                                       |
| PCRFQRYSW      | 查询PCRF地址开关              | 可选必选说明：可选参数  参数含义：该参数用于设置SMF/PGW-C会话对接PCRF时，是否支持Restful接口查询PCRF地址。  数据来源：全网规划 取值范围： NotSupport（不支持）Support（支持）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMCOMMFUNC查询当前参数配置值。  配置原则：  该开关仅在Restful接口查询PCF/PCRF地址开关开启时生效。如果期望配置该参数为支持，需要先配置Restful接口查询PCF/PCRF地址开关为支持。                                                                   |

## 使用实例

设置SMF支持不携带IMSI的用户激活、关闭本地手机后路由功能、支持2B2C漫游双DNN特性，不携带实例ID向UDM发起去注册，SGW不支持PGW重定向功能，支持QoS质差分析，关闭GaGy计费功能，支持Restful接口查询PCF/PCRF地址，支持体验感知信息采集订阅，支持位置变更订阅，支持由能力开放订阅触发位置上报，支持Restful接口查询非异网漫游或者非国漫场景下的PCRF地址，执行如下命令：

```
SET SMCOMMFUNC: LOCREPORT=Support, RTBEHINDMSSW=DISABLE, MULTIDNNSW=Support, UDMDEREGINSID=DISABLE, PGWRNSSWITCH=DISABLE, QOSANASW=Support, GAGYCHGSW=DISABLE, RESTFULQRYSW=Support, QOSEXPSW=Support, LOCATIONCHSW=Support, EXPOSURELOCRPT=Support, PCRFQRYSW=Support;
```