# 设置tethering事件上报的相关参数（SET TETHRPTCTRL）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用NF：PGW-U、UPF**

该命令用于设置tethering事件上报的相关参数。

#### 注意事项

- 该命令执行后对新数据流生效。
- 该命令最大记录数为1。
- 当SET TETHERDETGLBPARA的STATISTICMETHOD参数设为CONFIG时，每个用户下Tethering节点的最大个数，按照UserProfile下TetheringMaxNum参数配置值加1申请。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识   | TETHSTOPRPTSW   |   TETHHYSTIMER | TETHRPTEVTMODE   |
|:-------|:----------------|---------------:|:-----------------|
| 初始值    | DISABLE         |              0 | TETHER_BEHAVIOR  |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识           | 参数名称                      | 参数说明                                                                                                                                                                                                                                                                                                                   |
|:---------------|:--------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TETHSTOPRPTSW  | Tethering Stop消息上报开关      | 可选必选说明：必选参数 参数含义：该参数用于设置Tethering Stop消息上报开关。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：否。ENABLE：是。 默认值：无 配置原则： 当运营商需要上报Tethering Stop消息时，设置此参数值为ENABLE。当运营商不需要上报Tethering Stop消息时，设置此参数值为DISABLE。                                                                                                                                  |
| TETHHYSTIMER   | Tethering Stop消息上报迟滞时间（秒） | 可选必选说明：条件可选参数 前提条件：该参数在“TETHSTOPRPTSW”配置为“ENABLE”时为可选参数。 参数含义：该参数用于配置Tethering Stop消息上报迟滞时间。 数据来源：本端规划 取值范围：整数类型，取值范围为0～3600，单位是秒。 默认值：无 配置原则： 当单用户Tethering的Start和Stop消息上报过于频繁时，建议调大此参数。当希望Tethering的Start和Stop消息上报尽量精确时，建议调小此参数。该参数配置为0时，认为Tethering Stop延迟上报功能关闭。                                                   |
| TETHRPTEVTMODE | tethering上报事件模式           | 可选必选说明：可选参数 参数含义：该参数用于设置Tethering上报事件是基于Tethering行为还是基于Tethering接入的后台终端数。 数据来源：本端规划 取值范围：枚举类型。 TETHER_BEHAVIOR：代表基于Tethering用户行为触发事件上报。TETHER_TERMINAL_NUM：代表基于Tethering用户接入的后台终端数触发事件上报。 默认值：无 配置原则：当运营商需要上报基于用户是否发生Tethering访问行为时，设置此参数值为TETHER_BEHAVIOR。 当运营商需要上报基于Tethering用户接入的后台终端数时，设置此参数值为TETHER_TERMINAL_NUM。 |

#### 使用实例

- 需要上报Tethering Stop消息时，通过TethStopRptSw参数设置：

  ```
  SET TETHRPTCTRL: TETHSTOPRPTSW=ENABLE;
  ```
- 需要设置Tethering的Start和Stop消息上报频率时，通过TethHystimer参数设置：

  ```
  SET TETHRPTCTRL: TETHSTOPRPTSW=ENABLE, TETHHYSTIMER=10;
  ```
- 需要设置Tethering上报模式时，通过TethRptEvtMode参数设置：

  ```
  SET TETHRPTCTRL: TETHSTOPRPTSW=ENABLE, TETHRPTEVTMODE=TETHER_TERMINAL_NUM;
  ```