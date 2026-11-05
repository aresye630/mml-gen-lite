# 配置离线计费容器产生开关（SET CONTAINERTRIGGER）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用NF：SGW-C、PGW-C、SMF**

此命令用来配置离线计费容器产生开关。

#### 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为100。
- 只有配置了离线计费模板才能配置此命令。
- 当前版本不支持此命令的CONTTRIGENB参数。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识   | CONTTRIGRATCHNG   | CONTTRIGQOSCHNG   | PCCINIT   | CONTTRIGSNCHNG   | CONTTRIGCGISAI   | CONTTRIGECGI   | CONTTRIGTAI   | CONTTRIGULI   | CONTTRIGPLMNID   | CONTTRIGRAI   | CONTTRIGTARRIF   | CONTTRIGENB   | USERPLANECHNG   | SPLMNRATECHNG   | APNRATECHNG   | APNRATECHNGCLOSECAUSE           |
|:-------|:------------------|:------------------|:----------|:-----------------|:-----------------|:---------------|:--------------|:--------------|:-----------------|:--------------|:-----------------|:--------------|:----------------|:----------------|:--------------|:--------------------------------|
| 初始值    | ENABLE            | ENABLE            | DISABLE   | ENABLE           | ENABLE           | ENABLE         | ENABLE        | ENABLE        | ENABLE           | ENABLE        | ENABLE           | ENABLE        | ENABLE          | ENABLE          | ENABLE        | SERVINGPLMN_RATE_CONTROL_CHANGE |

- 该命令设定后的数据，需要通过LST OFCTEMPLATE命令进行查看。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识                  | 参数名称                            | 参数说明                                                                                                                                                                                                                                    |
|:----------------------|:--------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| OFCTEMPLATENAME       | 离线计费模板名                         | 可选必选说明：必选参数 参数含义：配置离线模板名称。 数据来源：本端规划 取值范围：字符串类型，输入长度范围为1～63。不支持空格。 默认值：无 配置原则：该参数使用ADD OFCTEMPLATE命令配置生成。                                                                                                                               |
| CONTTRIGRATCHNG       | Container RAT更新                 | 可选必选说明：可选参数 参数含义：这是个开关参数，表示发生RAT更新时是否产生容器，该Trigger开始支持的话单版本为r6v660gcdr。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不使能。ENABLE：使能。 默认值：无 配置原则：无                                                                                                        |
| CONTTRIGQOSCHNG       | QoS更新                           | 可选必选说明：可选参数 参数含义：这是个开关参数，表示发生QoS更新时是否产生容器，该Trigger开始支持的话单版本为r98cmccv130。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不使能。ENABLE：使能。 默认值：无 配置原则：无                                                                                                       |
| PCCINIT               | PCRF发起的QoS更新                    | 可选必选说明：条件可选参数 前提条件：该参数在“CONTTRIGQOSCHNG”配置为“ENABLE”时为可选参数。 参数含义：这是个开关参数，表示部署IP-CAN-Type为3GPP-EPS的Gx接口时，仅根据Gx接口上PCRF指示的APN-AMBR或缺省承载QCI/ARP的更新情况触发生成新的PGW-CDR容器。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不使能。ENABLE：使能。 默认值：无 配置原则：无                |
| CONTTRIGSNCHNG        | Serving Node更新                  | 可选必选说明：可选参数 参数含义：这是个开关参数，表示发生Serving Node更新时是否产生容器。该Trigger开始支持的话单版本为r98cmccv130。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不使能。ENABLE：使能。 默认值：无 配置原则：无                                                                                              |
| CONTTRIGCGISAI        | CGI/SAI更新                       | 可选必选说明：可选参数 参数含义：这是个开关参数，表示发生CGI（Cell Global Identification）/SAI（Service Area Identifier）更新时是否产生容器，该Trigger开始支持的话单版本为r6v660gcdr。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不使能。ENABLE：使能。 默认值：无 配置原则：无                                               |
| CONTTRIGECGI          | ECGI更新                          | 可选必选说明：可选参数 参数含义：这是个开关参数，表示发生ECGI更新时是否产生容器。该Trigger开始支持的话单版本为r8v850sgwcdr。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不使能。ENABLE：使能。 默认值：无 配置原则：无                                                                                                     |
| CONTTRIGTAI           | TAI更新                           | 可选必选说明：可选参数 参数含义：这是个开关参数，表示发生TAI更新时是否产生容器。该Trigger开始支持的话单版本为r8v850sgwcdr。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不使能。ENABLE：使能。 默认值：无 配置原则：无                                                                                                      |
| CONTTRIGULI           | ULI更新                           | 可选必选说明：可选参数 参数含义：这是个开关参数，表示发生ULI更新时是否产生容器。该Trigger开始支持的话单版本为r8v850sgwcdr。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不使能。ENABLE：使能。 默认值：无 配置原则：无                                                                                                      |
| CONTTRIGPLMNID        | Container Serving Node PLMN标识更新 | 可选必选说明：可选参数 参数含义：这是个开关参数，表示发生Serving Node PLMN标识更新时是否产生容器。该Trigger开始支持的话单版本为r99v3a0。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不使能。ENABLE：使能。 默认值：无 配置原则：无                                                                                           |
| CONTTRIGRAI           | RAI更新                           | 可选必选说明：可选参数 参数含义：这是个开关参数，表示发生RAI更新时是否产生容器。该Trigger开始支持的话单版本为r7v740gcdr。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不使能。ENABLE：使能。 默认值：无 配置原则：无                                                                                                        |
| CONTTRIGTARRIF        | 费率切换                            | 可选必选说明：可选参数 参数含义：这是个开关参数，表示发生费率切换时是否产生容器。该Trigger开始支持的话单版本为r98cmccv130。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不使能。ENABLE：使能。 默认值：无 配置原则：无                                                                                                        |
| CONTTRIGENB           | eNodeB更新                        | 可选必选说明：可选参数 参数含义：这是个开关参数，表示发生eNodeB更新时是否产生容器。该Trigger开始支持的话单版本为r8v850sgwcdr。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不使能。ENABLE：使能。 默认值：无 配置原则：无                                                                                                   |
| USERPLANECHNG         | 用户面更新                           | 可选必选说明：可选参数 参数含义：该参数用于指定用户面改变时是否产生话单容器。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不使能。ENABLE：使能。 默认值：无 配置原则：无                                                                                                                                        |
| SPLMNRATECHNG         | 服务PLMN控制速率改变                    | 可选必选说明：可选参数 参数含义：该参数用于指定服务PLMN控制速率改变时是否产生话单容器。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不使能。ENABLE：使能。 默认值：无 配置原则：无                                                                                                                                 |
| APNRATECHNG           | APN控制速率改变                       | 可选必选说明：可选参数 参数含义：该参数用于指定APN控制速率改变时是否产生话单容器。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不使能。ENABLE：使能。 默认值：无 配置原则：无                                                                                                                                    |
| APNRATECHNGCLOSECAUSE | APN速率控制改变流量容器关闭原因值              | 可选必选说明：条件可选参数 前提条件：该参数在“APNRATECHNG”配置为“ENABLE”时为可选参数。 参数含义：该参数用于指定APN控制速率改变时填充的流量容器关闭原因值。 数据来源：对端协商 取值范围：枚举类型。 SERVINGPLMN_RATE_CONTROL_CHANGE：流量容器关闭原因值填充为SPLMNRateChng。APN_RATE_CONTROL_CHANGE：流量容器关闭原因值填充为APNRateChng。 默认值：无 配置原则：无 |

#### 使用实例

设置名称为“test”的离线模板的容器产生开关参数都设为默认值：

```
SET CONTAINERTRIGGER:OFCTEMPLATENAME="test";
```