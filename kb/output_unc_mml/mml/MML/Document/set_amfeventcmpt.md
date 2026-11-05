# 设置AMF事件订阅兼容性参数（SET AMFEVENTCMPT）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：AMF**

该命令用于为AMF事件订阅通知消息设置兼容性控制参数。事件订阅为AMF与其它NF之间的服务化接口，通过本命令可以控制AMF是否在该接口的通知消息中携带指定的可选信元。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| GLOBALGNBID   | LOCRPTAGELOCSW   | LOCRPTAGELOCPLY   | SRCRPTUEREACHSW   | REACHACSTYPESW   |
|:--------------|:-----------------|:------------------|:------------------|:-----------------|
| NO            | NO               | ROUND_DOWN        | NO                | NO               |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识            | 参数名称                                 | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                     |
|:----------------|:-------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GLOBALGNBID     | UE当前驻留的基站全局标识                        | 可选必选说明：可选参数  参数含义：该参数用于控制上报事件订阅类型为LOCATION_REPORT、PRESENCE_IN_AOI_REPORT的通知消息时，是否携带UE当前驻留的基站全局标识。  数据来源：全网规划 取值范围： “YES（是）”：是“NO（否）”：否  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFEVENTCMPT查询当前参数配置值。  配置原则：无                                                                                                                                                                                           |
| LOCRPTAGELOCSW  | 位置事件上报ageOfLocationInformation信元携带开关 | 可选必选说明：可选参数  参数含义：该参数用于控制用户事件订阅类型为位置事件上报（LOCATION_REPORT）时，AMF是否在location中携ageOfLocationInformation信元。  数据来源：全网规划 取值范围： “YES（是）”：是“NO（否）”：否  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFEVENTCMPT查询当前参数配置值。  配置原则：无                                                                                                                                                                                      |
| LOCRPTAGELOCPLY | 位置事件上报ageOfLocationInformation信元填充策略 | 可选必选说明：该参数在"LOCRPTAGELOCSW"配置为"YES"时为条件可选参数。  参数含义：该参数用于控制用户事件订阅类型为位置事件上报（LOCATION_REPORT）时，AMF针对用户位置信息非实时获取的场景下ageOfLocationInfo不足1分钟的处理策略。  数据来源：全网规划 取值范围： “ROUND_DOWN（向下取整）”：ageOfLocationInformation不足1分钟时，向下取整为0分钟。“ROUND_UP（向上取值）”：ageOfLocationInformation不足1分钟时，向上取整为1分钟。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFEVENTCMPT查询当前参数配置值。  配置原则：  当对端NF需要严格基于用户最新位置信息下发相关策略时，需要将本参数设置为ROUND_UP。 |
| SRCRPTUEREACHSW | Inter移动性流程reportUeReachable信元携带开关    | 可选必选说明：可选参数  参数含义：该参数用于控制AMF间移动性流程中源测AMF是否在ueContext中携带reportUeReachable信元。 该参数设置为YES，若用户事件订阅类型为可达事件上报（REACHABILITY_REPORT）且reachabilityFilter取值为UE_REACHABLE_DL_TRAFFIC，用户发起AMF间移动性流程，源测AMF携带reportUeReachable信元取值为true。  数据来源：全网规划 取值范围： “YES（是）”：是“NO（否）”：否  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFEVENTCMPT查询当前参数配置值。  配置原则：  若AMF开启下行数据可达事件上报功能时，建议将本参数设置为YES。                                 |
| REACHACSTYPESW  | 下行数据可达事件上报accessTypeList信元携带开关       | 可选必选说明：可选参数  参数含义：该参数用于控制AMF上报下行数据可达事件时是否携带accessTypeList信元。 该参数设置为YES，若用户事件订阅类型为可达事件上报（REACHABILITY_REPORT）且reachabilityFilter取值为UE_REACHABLE_DL_TRAFFIC，当用户切换至连接态或可寻呼状态时，AMF上报下行数据可达事件携带accessTypeList信元。  数据来源：全网规划 取值范围： “YES（是）”：是“NO（否）”：否  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFEVENTCMPT查询当前参数配置值。  配置原则：  若AMF开启下行数据可达事件上报功能时，建议将本参数设置为YES。                                               |

## 使用实例

设置AMF事件订阅的兼容性参数"UE当前驻留的基站全局标识"为"YES"，执行如下命令。

```
%%SET AMFEVENTCMPT: GLOBALGNBID=YES;%%
```