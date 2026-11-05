# 设置PDN自动探测功能开关（SET PDNAUTOTSTSW）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用NF：PGW-U、UPF**

设置PDN自动探测功能开关。

#### 注意事项

- 该命令执行后立即生效。
- 该命令最大记录数为1。
- 该命令存在系统初始记录，参数的初始设置值如下表：

| 参数标识   | SWITCH   | DNSKPIFTSW   | FAULTTRACERTSW   |
|:-------|:---------|:-------------|:-----------------|
| 初始值    | DISABLE  | DISABLE      | DISABLE          |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识           | 参数名称            | 参数说明                                                                                                                                     |
|:---------------|:----------------|:-----------------------------------------------------------------------------------------------------------------------------------------|
| SWITCH         | PDN侧路由自动探测开关    | 可选必选说明：必选参数 参数含义：PDN侧自动探测开关。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不使能。ENABLE：使能。 默认值：无 配置原则：无                                                    |
| DNSKPIFTSW     | DNS KPI故障自动探测开关 | 可选必选说明：可选参数 参数含义：DNS KPI故障自动探测开关。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不使能。ENABLE：使能。 默认值：DISABLE 配置原则：无                                         |
| FAULTTRACERTSW | 路径故障Tracert开关   | 可选必选说明：条件可选参数 前提条件：该参数在“DNSKPIFTSW”配置为“ENABLE”时为可选参数。 参数含义：路径故障Tracert开关。 数据来源：本端规划 取值范围：枚举类型。 DISABLE：不使能。ENABLE：使能。 默认值：DISABLE 配置原则：无 |

#### 使用实例

- 打开PDN自动探测功能开关：

  ```
  SET PDNAUTOTSTSW:SWITCH="ENABLE";
  ```
- 打开KPI异常检测开关：

  ```
  SET PDNAUTOTSTSW:SWITCH="ENABLE", DNSKPIFTSW="ENABLE";
  ```
- 打开路径故障自动探测开关：

  ```
  SET PDNAUTOTSTSW:SWITCH="ENABLE", FAULTTRACERTSW="ENABLE";
  ```