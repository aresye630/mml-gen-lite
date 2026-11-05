# 配置LMF消息控制参数（SET LMFMSGCTRL）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用NF：UPF**

该命令用于设置定时器的超时时间参数，定位算法类型开关状态以及发送Positioning Deactivation消息开关状态等功能。

#### 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 设置定时器的超时时间参数时，TXTIMER建议小于SGLLCSTX。
- 若ADD LCSPOSDEANRSW命令配置的基站标识段匹配中，则优先判断ADD LCSPOSDEANRSW命令中的发送Positioning Deactivation消息开关，否则此命令中的LMFPOSDEASW开关生效。
- LMF收到AMF发送的定位请求中不携带lpHapType字段时，执行SET LCSSOFTPARA命令将bit10置为1后LCSPerTriSw参数生效。
- 执行SET LMFMSGCTRL命令时，需要至少输入一个参数；否则，命令执行失败。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识   |   TXTIMER |   SGLLCSTX | ALGOSWITCH   | LMFPOSDEASW   | DIRECTREPORTSW   | TRPSW   | AMFLOCRPTSUBSW   | LPLCSPERTRISW   | LPLPPREQLOCSW   | LPLPPABORTSW   |   GNBNOMEARPTNUM |   GMLCEVTRSPFANUM |   PLTXTIMER | AMFREGRPTSUBSW   | LCSPERTRISW   |
|:-------|----------:|-----------:|:-------------|:--------------|:-----------------|:--------|:-----------------|:----------------|:----------------|:---------------|-----------------:|------------------:|------------:|:-----------------|:--------------|
| 初始值    |         3 |          3 | DISABLE      | ENABLE        | DISABLE          | DISABLE | DISABLE          | DISABLE         | DISABLE         | DISABLE        |                6 |                 5 |           6 | DISABLE          | DISABLE       |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识            | 参数名称                                    | 参数说明                                                                                                                                                                                                                           |
|:----------------|:----------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TXTIMER         | Tx定时器时长（秒）                              | 可选必选说明：可选参数 参数含义：该参数用于配置Tx定时器时长。 数据来源：全网规划 取值范围：整型数字类型，取值范围为1~10。 默认值：无 配置原则：无                                                                                                                                                 |
| SGLLCSTX        | LCS单次定位流程超时时长（秒）                        | 可选必选说明：可选参数 参数含义：该参数用于配置单次定位流程的超时时长。 数据来源：全网规划 取值范围：整型数字类型，取值范围3~10。 默认值：无 配置原则：无                                                                                                                                              |
| ALGOSWITCH      | 携带算法类型开关                                | 可选必选说明：可选参数 参数含义：该参数用于控制LMF给AMF或者GMLC发送定位通知时是否携带算法类型。当前只支持携带小站算法类型。 数据来源：全网规划 取值范围： DISABLE：开关去使能。ENABLE：携带算法开关使能。 默认值：无 配置原则：无                                                                                                |
| LMFPOSDEASW     | 发送Positioning Deactivation消息开关          | 可选必选说明：可选参数 参数含义：该参数用于配置是否发送Positioning Deactivation消息。 数据来源：全网规划 取值范围： DISABLE：开关去使能。ENABLE：开关使能。 默认值：无 配置原则：若ADD LCSPOSDEANRSW命令配置的基站标识段匹配中，则优先判断ADD LCSPOSDEANRSW命令中的发送Positioning Deactivation消息开关，否则此命令中的LMFPOSDEASW开关生效。 |
| DIRECTREPORTSW  | 定位结果直接上报开关                              | 可选必选说明：可选参数 参数含义：该参数用于设置是否开启定位结果直接上报功能，只对单次定位生效。 数据来源：全网规划 取值范围： DISABLE：开关去使能。ENABLE：开关使能。 默认值：无 配置原则：无                                                                                                                       |
| TRPSW           | TRP功能开关                                 | 可选必选说明：可选参数 参数含义：该参数用于设置是否开启TRP获取功能。 数据来源：全网规划 取值范围： DISABLE：开关去使能。ENABLE：开关使能。 默认值：无 配置原则：无                                                                                                                                   |
| AMFLOCRPTSUBSW  | 订阅位置变更消息开关                              | 可选必选说明：可选参数 参数含义：该参数用于配置是否向AMF发送订阅位置变更消息。 数据来源：全网规划 取值范围： DISABLE：开关去使能。ENABLE：开关使能。 默认值：无 配置原则：无                                                                                                                              |
| LPLCSPERTRISW   | 低功耗终端LCS Periodic-Triggered Invoke消息开关  | 可选必选说明：可选参数 参数含义：该参数用于配置是否向低功耗UE发送LCS Periodic-Triggered Invoke消息。 数据来源：全网规划 取值范围： DISABLE：开关去使能。ENABLE：开关使能。 默认值：无 配置原则：无                                                                                                     |
| LPLPPREQLOCSW   | 低功耗终端LPP RequestLocationInformation消息开关 | 可选必选说明：可选参数 参数含义：该参数用于配置是否向低功耗UE发送LPP RequestLocationInformation消息。 数据来源：全网规划 取值范围： DISABLE：开关去使能。ENABLE：开关使能。 默认值：无 配置原则：无                                                                                                    |
| LPLPPABORTSW    | 低功耗终端LPP Abort消息开关                      | 可选必选说明：条件必选参数 前提条件：该参数在“LPLPPREQLOCSW”配置为“ENABLE”时为必选参数。 参数含义：该参数用于配置是否向低功耗终端UE发送LPP Abort消息。 数据来源：全网规划 取值范围： DISABLE：开关去使能。ENABLE：开关使能。 默认值：无 配置原则：无                                                                          |
| GNBNOMEARPTNUM  | LMF连续未收到MEASUREMENT REPORT消息次数          | 可选必选说明：可选参数 参数含义：该参数用于配置周期定位过程中LMF连续几次未收到gNodeB的MEASUREMENT REPORT消息时发起取消周期定位流程。 数据来源：全网规划 取值范围：整型数字类型，取值范围为3~100。 默认值：无 配置原则：无                                                                                                |
| GMLCEVTRSPFANUM | LMF连续收到EventNotify失败响应消息次数              | 可选必选说明：可选参数 参数含义：该参数用于配置周期定位过程中LMF连续收到GMLC的EventNotify失败响应消息次数或者连续未收到GMLC的EventNotify响应消息，达到该次数时LMF发起取消周期定位流程。 数据来源：全网规划 取值范围：整型数字类型，取值范围为3~100。 默认值：无 配置原则：无                                                                  |
| PLTXTIMER       | 周期定位Tx定时器时长（秒）                          | 可选必选说明：可选参数 参数含义：该参数用于配置周期定位Tx定时器时长。 数据来源：全网规划 取值范围：整型数字类型，取值范围为3~10。 默认值：无 配置原则：无                                                                                                                                             |
| AMFREGRPTSUBSW  | 订阅注册状态变更消息开关                            | 可选必选说明：可选参数 参数含义：该参数用于配置是否向AMF发送订阅注册状态变更消息。 数据来源：全网规划 取值范围： DISABLE：开关去使能。ENABLE：开关使能。 默认值：无 配置原则：无                                                                                                                            |
| LCSPERTRISW     | 普通终端LCS Periodic-Triggered Invoke消息开关   | 可选必选说明：可选参数 参数含义：该参数用于配置是否向普通UE发送LCS Periodic-Triggered Invoke消息。 数据来源：全网规划 取值范围： DISABLE：开关去使能。ENABLE：开关使能。 默认值：无 配置原则：无                                                                                                      |

#### 使用实例

修改定时器超时时长，设置定位算法类型开关关闭，设置发送Positioning Deactivation消息开关打开：

```
SET LMFMSGCTRL: TXTIMER=5, SGLLCSTX=6, ALGOSWITCH=DISABLE, LMFPOSDEASW=ENABLE;
```