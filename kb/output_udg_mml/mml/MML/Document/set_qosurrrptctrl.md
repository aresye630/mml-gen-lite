# 设置QoS URR上报的相关参数（SET QOSURRRPTCTRL）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用NF：PGW-U、UPF**

该命令用于设置QoS URR上报的相关参数。

#### 注意事项

- 该命令执行后对新数据流生效。
- 该命令最大记录数为1。
- 当用户五元组老化时间（通过命令SET FLOWAGETIME设置）到达后，业务触发的专有承载的URR会上报Stop，QOSURRAGETIME参数（通过命令SET UPGLBPMPARA设置）触发的URR Stop与五元组老化触发的URR Stop没有关联。通常建议QOSURRAGETIME大于等于五元组老化时间。
- 如果配置了QoS类型URR Stop上报迟滞时间（通过命令SET QOSURRRPTCTRL的QOSURRHYSTIMER参数配置），此功能仅在五元组老化后开始计算迟滞，与QOSURRAGETIME参数没有关联，通常建议QOSURRAGETIME大于等于五元组老化时间和迟滞时间的总和。
- QBGRPT开关开启时，仅对新用户或更新场景，且SMF下发质差保障标识后生效。
  QBGRPT开关关闭时，立即生效，同时对于配置为ADD QOSPROP（QBGRPT=ENABLE）的Rule专载策略不再生效。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识   |   QOSURRHYSTIMER | RULEDELRPTSTOP   | QBGRPT   |
|:-------|-----------------:|:-----------------|:---------|
| 初始值    |                0 | DISABLE          | DISABLE  |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识           | 参数名称                       | 参数说明                                                                                                                                                                                                   |
|:---------------|:---------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| QOSURRHYSTIMER | QoS类型URR Stop上报迟滞时间（秒）     | 可选必选说明：可选参数 参数含义：该参数用于配置QoS类型URR Stop上报迟滞时间。 数据来源：本端规划 取值范围：整数类型，取值范围为0～3600，单位是秒。 默认值：无 配置原则： 当单用户一个URR的Start和Stop消息上报过于频繁时，建议调大此参数。当希望一个URR的Start和Stop消息上报尽量精确时，建议调小此参数。该参数配置为0时，认为QoS类型URR延迟上报功能关闭。 |
| RULEDELRPTSTOP | Rule删除时触发QoS URR Stop上报的开关 | 可选必选说明：可选参数 参数含义：该参数用于配置Rule删除时是否触发QoS URR Stop上报的开关。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：否。ENABLE：是。 默认值：无 配置原则：当希望业务触发专载的预定义规则去激活时，触发已创建的专载上报STOP，设置此参数值为ENABLE，系统在检测到会话的QoS URR无关联的预定义规则时，上报该URR的STOP消息。   |
| QBGRPT         | QoS质差分析上报开关                | 可选必选说明：可选参数 参数含义：该参数用于决定匹配中QoS Rule之后，上报URR之前是否需要检测到质差。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：否。ENABLE：是。 默认值：无 配置原则：DISABLE：匹配中QoS Rule立即上报URR。ENABLE：匹配中QoS Rule且检测到质差后上报URR。关联命令ADD QOSPROP。                 |

#### 使用实例

在需要配置QoS类型URR Stop上报迟滞时间时，执行该命令设置QoS URR上报Stop迟滞时间：

```
SET QOSURRRPTCTRL: QOSURRHYSTIMER=20;
```