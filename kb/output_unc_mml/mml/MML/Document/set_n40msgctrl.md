# 设置N40接口消息的控制参数（SET N40MSGCTRL）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：PGW-C、SMF、GGSN**

该命令用于设置N40接口消息的控制参数。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| ROAMOFFSTARTSW   | UPFID23G   | PRAINFO23G   | SLICINGINFO23G   | SSCMODE23G   | DNNSELMODE23G   | STOPINDICTR23G   | UCITIMER23G   | FINALREPORT   | HOMEOFFSTARTSW   | RELAYREPORTSW   |
|:-----------------|:-----------|:-------------|:-----------------|:-------------|:----------------|:-----------------|:--------------|:--------------|:-----------------|:----------------|
| DISABLE          | ENABLE     | ENABLE       | ENABLE           | ENABLE       | ENABLE          | ENABLE           | ENABLE        | ENABLE        | ENABLE           | DISABLE         |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识           | 参数名称                                                 | 参数说明                                                                                                                                                                                                                                                                                                            |
|:---------------|:-----------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ROAMOFFSTARTSW | 国际漫游场景更新流程中仅离线新业务预申请上报CHF开关                          | 可选必选说明：可选参数  参数含义：该参数用于控制国际漫游场景下SMF与CHF的更新流程仅离线新业务预申请时是否上报CHF。  数据来源：本端规划 取值范围： “DISABLE（不使能）”：国际漫游场景更新流程中仅离线新业务预申请时上报CHF。“ENABLE（使能）”：国际漫游场景更新流程中仅离线新业务预申请时不上报CHF。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST N40MSGCTRL查询当前参数配置值。  配置原则：无                                                                       |
| UPFID23G       | GERAN/UTRAN接入场景携带UPFID                               | 可选必选说明：可选参数  参数含义：该参数用于控制GERAN/UTRAN接入场景是否携带UPFID。  数据来源：本端规划 取值范围： “DISABLE（不使能）”：GERAN/UTRAN接入场景不携带UPFID。“ENABLE（使能）”：GERAN/UTRAN接入场景携带UPFID。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST N40MSGCTRL查询当前参数配置值。  配置原则：无                                                                                           |
| PRAINFO23G     | GERAN/UTRAN接入场景携带Presence Reporting Area Information | 可选必选说明：可选参数  参数含义：该参数用于控制GERAN/UTRAN接入场景是否携带Presence Reporting Area Information。  数据来源：本端规划 取值范围： “DISABLE（不使能）”：GERAN/UTRAN接入场景不携带Presence Reporting Area Information。“ENABLE（使能）”：GERAN/UTRAN接入场景携带Presence Reporting Area Information。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST N40MSGCTRL查询当前参数配置值。  配置原则：无 |
| SLICINGINFO23G | GERAN/UTRAN接入场景携带Network Slicing Information         | 可选必选说明：可选参数  参数含义：该参数用于控制GERAN/UTRAN接入场景是否携带Network Slicing Information。  数据来源：本端规划 取值范围： “DISABLE（不使能）”：GERAN/UTRAN接入场景不携带Network Slicing Information。“ENABLE（使能）”：GERAN/UTRAN接入场景携带Network Slicing Information。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST N40MSGCTRL查询当前参数配置值。  配置原则：无                         |
| SSCMODE23G     | GERAN/UTRAN接入场景携带SSC Mode                            | 可选必选说明：可选参数  参数含义：该参数用于控制GERAN/UTRAN接入场景是否携带SSC Mode。  数据来源：本端规划 取值范围： “DISABLE（不使能）”：GERAN/UTRAN接入场景不携带SSC Mode。“ENABLE（使能）”：GERAN/UTRAN接入场景携带SSC Mode。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST N40MSGCTRL查询当前参数配置值。  配置原则：无                                                                                  |
| DNNSELMODE23G  | GERAN/UTRAN接入场景携带DNN Selection Mode                  | 可选必选说明：可选参数  参数含义：该参数用于控制GERAN/UTRAN接入场景是否携带DNN Selection Mode。  数据来源：本端规划 取值范围： “DISABLE（不使能）”：GERAN/UTRAN接入场景不携带DNN Selection Mode。“ENABLE（使能）”：GERAN/UTRAN接入场景携带DNN Selection Mode。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST N40MSGCTRL查询当前参数配置值。  配置原则：无                                                    |
| STOPINDICTR23G | GERAN/UTRAN接入场景携带Session Stop Indicator              | 可选必选说明：可选参数  参数含义：该参数用于控制GERAN/UTRAN接入场景是否携带Session Stop Indicator。  数据来源：本端规划 取值范围： “DISABLE（不使能）”：GERAN/UTRAN接入场景不携带Session Stop Indicator。“ENABLE（使能）”：GERAN/UTRAN接入场景携带Session Stop Indicator。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST N40MSGCTRL查询当前参数配置值。  配置原则：无                                        |
| UCITIMER23G    | GERAN/UTRAN接入场景携带Unit Count Inactivity Timer         | 可选必选说明：可选参数  参数含义：该参数用于控制GERAN/UTRAN接入场景是否携带Unit Count Inactivity Timer。  数据来源：本端规划 取值范围： “DISABLE（不使能）”：GERAN/UTRAN接入场景不携带Unit Count Inactivity Timer。“ENABLE（使能）”：GERAN/UTRAN接入场景携带Unit Count Inactivity Timer。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST N40MSGCTRL查询当前参数配置值。  配置原则：无                         |
| FINALREPORT    | 去活消息中usedUnitContainer中triggerType支持填写FINAL          | 可选必选说明：可选参数  参数含义：该参数用于控制去活消息中，usedUnitContainer信元中的triggerType是否支持填写FINAL。  数据来源：本端规划 取值范围： “ENABLE（使能）”：去活消息中，支持usedUnitContainer中的triggerType填写FINAL。“DISABLE（不使能）”：去活消息中，不支持usedUnitContainer中的triggerType填写为FINAL。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST N40MSGCTRL查询当前参数配置值。  配置原则：无                   |
| HOMEOFFSTARTSW | 非国际漫游场景更新流程中仅离线新业务预申请上报CHF开关                         | 可选必选说明：可选参数  参数含义：该参数用于控制非国际漫游场景下SMF与CHF的更新流程仅离线新业务预申请时是否上报CHF。  数据来源：本端规划 取值范围： “DISABLE（不使能）”：非国际漫游场景更新流程中仅离线新业务预申请时不上报CHF。“ENABLE（使能）”：非国际漫游场景更新流程中仅离线新业务预申请时上报CHF。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST N40MSGCTRL查询当前参数配置值。  配置原则：无                                                                    |
| RELAYREPORTSW  | N40消息支持携带媒体中继流量开关                                    | 可选必选说明：可选参数  参数含义：该参数用于控制是否支持在N40消息中携带媒体中继上下行流量。  数据来源：本端规划 取值范围： “DISABLE（不使能）”：不支持在N40消息中携带媒体中继上下行流量。“ENABLE（使能）”：支持在N40消息中携带媒体中继上下行流量。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST N40MSGCTRL查询当前参数配置值。  配置原则：无                                                                                                 |

## 使用实例

设置国际漫游场景下在更新流程中仅离线新业务预申请不需要上报CHF：

```
SET N40MSGCTRL: ROAMOFFSTARTSW=ENABLE;
```