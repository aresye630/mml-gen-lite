# 设置零流量计费事件忽略开关（SET ZEROCHGSKIPSW）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用NF：GGSN、SGW-C、PGW-C、SMF**

该命令用于设置零流量计费事件忽略开关。

#### 注意事项

- 该命令执行后立即生效。
- 该命令仅当软参DWORD519 BIT4取值为1时生效。
- 该命令最大记录数为1。
- 忽略零流量计费事件会导致某些计费信息缺失（如RAT更新信息、ULI改变信息），需要确认影响后使能该功能。
- UNC当前暂不支持基于位置的计费订阅和取消，SKIPULIBASEDCHG无实际生效场景。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识   | ZEROCHGSKIPSW   | SKIPRATCHNG   | SKIPSNCHNG   | SKIPTMZONECHNG   | SKIPPLMNCHNG   | SKIPTIMETHRESH   | SKIPCCFH   | SKIPFINALCDR   | SKIPPSFCI   | SKIPFOCGENCDR   | SKIPULIBASEDCHG   | SKIPQOSCHNG   | SKIPULICHNG   | SKIPTARIFFCHNG   |
|:-------|:----------------|:--------------|:-------------|:-----------------|:---------------|:-----------------|:-----------|:---------------|:------------|:----------------|:------------------|:--------------|:--------------|:-----------------|
| 初始值    | DISABLE         | DISABLE       | DISABLE      | DISABLE          | DISABLE        | DISABLE          | DISABLE    | DISABLE        | DISABLE     | DISABLE         | DISABLE           | DISABLE       | DISABLE       | DISABLE          |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识            | 参数名称                                | 参数说明                                                                                                                                                        |
|:----------------|:------------------------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ZEROCHGSKIPSW   | 零流量计费事件忽略总开关                        | 可选必选说明：必选参数 参数含义：该参数用于配置是否使能零流量计费事件忽略功能。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不使能。ENABLE：使能。 默认值：无 配置原则：无                                                           |
| SKIPRATCHNG     | 忽略RAT更新                             | 可选必选说明：条件可选参数 前提条件：该参数在“ZEROCHGSKIPSW”配置为“ENABLE”时为可选参数。 参数含义：忽略RAT更新。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不使能。ENABLE：使能。 默认值：无 配置原则：无                             |
| SKIPSNCHNG      | 忽略Serving Node地址改变                  | 可选必选说明：条件可选参数 前提条件：该参数在“ZEROCHGSKIPSW”配置为“ENABLE”时为可选参数。 参数含义：忽略Serving Node地址改变。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不使能。ENABLE：使能。 默认值：无 配置原则：无                  |
| SKIPTMZONECHNG  | 忽略MS时区改变                            | 可选必选说明：条件可选参数 前提条件：该参数在“ZEROCHGSKIPSW”配置为“ENABLE”时为可选参数。 参数含义：忽略MS时区改变。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不使能。ENABLE：使能。 默认值：无 配置原则：无                            |
| SKIPPLMNCHNG    | 忽略Serving Node PLMN标识改变             | 可选必选说明：条件可选参数 前提条件：该参数在“ZEROCHGSKIPSW”配置为“ENABLE”时为可选参数。 参数含义：忽略Serving Node PLMN标识改变。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不使能。ENABLE：使能。 默认值：无 配置原则：无             |
| SKIPTIMETHRESH  | 忽略时间阈值                              | 可选必选说明：条件可选参数 前提条件：该参数在“ZEROCHGSKIPSW”配置为“ENABLE”时为可选参数。 参数含义：忽略时间阈值。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不使能。ENABLE：使能。 默认值：无 配置原则：无                              |
| SKIPCCFH        | 忽略CCFH                              | 可选必选说明：条件可选参数 前提条件：该参数在“ZEROCHGSKIPSW”配置为“ENABLE”时为可选参数。 参数含义：忽略CCFH。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不使能。ENABLE：使能。 默认值：无 配置原则：无                              |
| SKIPFINALCDR    | 忽略去激活话单                             | 可选必选说明：条件可选参数 前提条件：该参数在“ZEROCHGSKIPSW”配置为“ENABLE”时为可选参数。 参数含义：忽略去激活话单。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不使能。ENABLE：使能。 默认值：无 配置原则：无                             |
| SKIPPSFCI       | 忽略PS-Furnish-Charging-Information改变 | 可选必选说明：条件可选参数 前提条件：该参数在“ZEROCHGSKIPSW”配置为“ENABLE”时为可选参数。 参数含义：忽略PS-Furnish-Charging-Information改变。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不使能。ENABLE：使能。 默认值：无 配置原则：无 |
| SKIPFOCGENCDR   | 忽略强制生成话单                            | 可选必选说明：条件可选参数 前提条件：该参数在“ZEROCHGSKIPSW”配置为“ENABLE”时为可选参数。 参数含义：忽略强制生成话单。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不使能。ENABLE：使能。 默认值：无 配置原则：无                            |
| SKIPULIBASEDCHG | 忽略基于位置的计费订阅和取消                      | 可选必选说明：条件可选参数 前提条件：该参数在“ZEROCHGSKIPSW”配置为“ENABLE”时为可选参数。 参数含义：忽略基于位置的计费订阅和取消。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不使能。ENABLE：使能。 默认值：无 配置原则：无                      |
| SKIPQOSCHNG     | 忽略QoS改变                             | 可选必选说明：条件可选参数 前提条件：该参数在“ZEROCHGSKIPSW”配置为“ENABLE”时为可选参数。 参数含义：忽略QoS改变。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不使能。ENABLE：使能。 默认值：无 配置原则：无                             |
| SKIPULICHNG     | 忽略ULI改变                             | 可选必选说明：条件可选参数 前提条件：该参数在“ZEROCHGSKIPSW”配置为“ENABLE”时为可选参数。 参数含义：忽略ULI改变。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不使能。ENABLE：使能。 默认值：无 配置原则：无                             |
| SKIPTARIFFCHNG  | 忽略费率切换                              | 可选必选说明：条件可选参数 前提条件：该参数在“ZEROCHGSKIPSW”配置为“ENABLE”时为可选参数。 参数含义：忽略费率切换。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不使能。ENABLE：使能。 默认值：无 配置原则：无                              |

#### 使用实例

设置零流量计费事件忽略开关，ZeroChgSkipSw为“ENABLE”，SkipFinalCDR为“ENABLE”，SkipFocGenCDR为“ENABLE”，其他参数都设为“ENABLE”：

```
SET ZEROCHGSKIPSW: ZEROCHGSKIPSW=ENABLE, SKIPRATCHNG=ENABLE, SKIPSNCHNG=ENABLE, SKIPTMZONECHNG=ENABLE, SKIPPLMNCHNG=ENABLE, SKIPTIMETHRESH=ENABLE, SKIPCCFH=ENABLE, SKIPFINALCDR=ENABLE, SKIPPSFCI=ENABLE, SKIPFOCGENCDR=ENABLE, SKIPULIBASEDCHG=ENABLE, SKIPQOSCHNG=ENABLE, SKIPULICHNG=ENABLE, SKIPTARIFFCHNG=ENABLE;
```