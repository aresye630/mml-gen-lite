# 设置NSA控制处理配置（SET NSACTRLPROP）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：SGW-C、PGW-C**

该命令用于设置NSA相关的控制处理配置。

## 注意事项

- 该命令执行后立即生效。

- 当参数“NSAIDENTIFYMD”设置为“SRUDR（SRUDR）”，需要设置参数“SRUDRSW”为“ENABLE（使能）”。
- 当参数“NSAIDENTIFYMD”设置为“AUTOSTUDYNR（AUTOSTUDYNR）”时，需要设置参数“SGWTOPGWNRSW”为“ENABLE（使能）”。
- 当通过该命令修改参数“NCGISW”为“DISABLE（不使能）”时，对应的参数“SGWS5TOPGWNCGI”和“SGWS8TOPGWNCGI”的取值会被同步修改成“DISABLE（不使能）”。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| NSAIDENTIFYMD   | SGWTOPGWNRSW   | SRUDRSW   | S1RELTRACTRLSW   | NCGISW   | SGWS5TOPGWNCGI   | SGWS8TOPGWNCGI   | EPSTO5GSSRUDRSW   |
|:----------------|:---------------|:----------|:-----------------|:---------|:-----------------|:-----------------|:------------------|
| DCNR            | DISABLE        | ENABLE    | DISABLE          | DISABLE  | DISABLE          | DISABLE          | DISABLE           |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识            | 参数名称                       | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|:----------------|:---------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NSAIDENTIFYMD   | NSA用户的判断方法                 | 可选必选说明：可选参数  参数含义：该参数用于NSA用户的判断。  数据来源：本端规划 取值范围： “SRUDR（SRUDR）”：用户激活使用DCNR判断，后续根据连接态是否上报过5G流量识别5G用户。(S1Release消息只发给SGW-C，对于SGW-C和PGW-C分离场景下PGW-C无法同步NSA状态，华为通过私有实现当SGW-C收到S1Release消息NSA发生变化SGW-C通过ChangeNotificationRequest消息告知PGW-C用户4G/5G NSA形态的切换，PGW-C根据UsageDataUL判断4G/5G NSA形态变化。) “DCNR（DCNR）”：仅使用Create session request消息中的DCNR标记识别5G用户。“AUTOSTUDYNR（AUTOSTUDYNR）”：先根据create session request的DCNR标记识别，后续根据MME把基站地址的自学习结果通过MBR消息带给SGW私有信元识别。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NSACTRLPROP查询当前参数配置值。  配置原则：无 |
| SGWTOPGWNRSW    | SGW-C发送NR标记给PGW-C          | 可选必选说明：可选参数  参数含义：该参数用于是否使能SGW-C向PGW-C发送Modify Bearer Request消息中包含私有扩展信元的NSA标识类型。  数据来源：本端规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NSACTRLPROP查询当前参数配置值。  配置原则：无                                                                                                                                                                                                                                                                                                                             |
| SRUDRSW         | 支持5G流量上报                   | 可选必选说明：可选参数  参数含义：该参数用于支持5G流量上报。  数据来源：本端规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NSACTRLPROP查询当前参数配置值。  配置原则：无                                                                                                                                                                                                                                                                                                                                                                              |
| S1RELTRACTRLSW  | S1 Release中SGW-C累加5G流量     | 可选必选说明：可选参数  参数含义：该参数控制在S1 Release流程中，SGW-C收到Change Notification Request消息时（消息中未携带S1 Release流程开始时获取到的用户流量）是否支持将S1 Release流程开始时Release Access Bearers Request消息中携带的5G流量累加后通知PGW-C。  数据来源：本端规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NSACTRLPROP查询当前参数配置值。  配置原则：无                                                                                                                                                                                                                             |
| NCGISW          | 支持5G小区位置功能开关               | 可选必选说明：可选参数  参数含义：该参数用于控制GTPCV2信令消息中携带的5G小区位置信息是否使能处理。  数据来源：本端规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NSACTRLPROP查询当前参数配置值。  配置原则：  本参数为“ENABLE（使能）”时：当Ga接口需要支持NCGI必须开启软参DWORD518 BIT5，按需开启软参DWORD518 BIT6；当Gy接口需要支持NCGI必须开启软参DWORD518 BIT17，按需开启软参DWORD518 BIT18。                                                                                                                                                                                                                         |
| SGWS5TOPGWNCGI  | SGW-C S5接口发送5G小区位置信息给PGW-C | 可选必选说明：该参数在"NCGISW"配置为"ENABLE"时为条件可选参数。  参数含义：该参数用于控制是否使能SGW-C S5接口发送5G小区位置信息给PGW-C。  数据来源：本端规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NSACTRLPROP查询当前参数配置值。  配置原则：  该参数仅在“NCGISW”取值为“ENABLE（使能）”才能生效。                                                                                                                                                                                                                                                                                        |
| SGWS8TOPGWNCGI  | SGW-C S8接口发送5G小区位置信息给PGW-C | 可选必选说明：该参数在"NCGISW"配置为"ENABLE"时为条件可选参数。  参数含义：该参数用于控制是否使能SGW-C S8接口发送5G小区位置信息给PGW-C。  数据来源：本端规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NSACTRLPROP查询当前参数配置值。  配置原则：  该参数仅在“NCGISW”取值为“ENABLE（使能）”才能生效。                                                                                                                                                                                                                                                                                        |
| EPSTO5GSSRUDRSW | 支持EPS到5GS切换流程中5G流量上报       | 可选必选说明：可选参数  参数含义：该参数用于控制SMF是否处理EPS到5GS切换流程中AMF上报的5G流量。  数据来源：本端规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST NSACTRLPROP查询当前参数配置值。  配置原则：无                                                                                                                                                                                                                                                                                                                                                       |

## 使用实例

- 配置指定5G NSA用户识别方法为SRUDR，支持SGW-C发送NR标记给PGW-C，支持5G流量上报，支持5G流量累加后通知PGW-C，支持EPS到5GS切换流程中5G流量上报：

  ```
  SET NSACTRLPROP: NSAIDENTIFYMD=SRUDR, SGWTOPGWNRSW=ENABLE, SRUDRSW=ENABLE, S1RELTRACTRLSW=ENABLE, EPSTO5GSSRUDRSW=ENABLE;
  ```
- 配置支持5G小区位置功能，支持SGW-C S5接口发送5G小区位置信息给PGW-C，支持SGW-C S8接口发送5G小区位置信息给PGW-C：

  ```
  SET NSACTRLPROP: NCGISW=ENABLE, SGWS5TOPGWNCGI=ENABLE, SGWS8TOPGWNCGI=ENABLE;
  ```