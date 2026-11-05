# 设置多Serving Plmn增强功能（SET MULTISRVPLMNEN）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：AMF**

该命令用于控制AMF在多Serving Plmn组网场景下支持移动性管理流程增强处理。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| MULTISRVPLMNEN   | MOBENHPLCY   | AMFDEVINFNTFSMF   |   AMFGUAMIIDX |
|:-----------------|:-------------|:------------------|--------------:|
| NOT_SUPPORT      | SUPPORT      | NOT_SUPPORT       |           256 |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识            | 参数名称                | 参数说明                                                                                                                                                                                                                                                                                                                                                                          |
|:----------------|:--------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MULTISRVPLMNEN  | 支持多Serving Plmn功能增强 | 可选必选说明：可选参数  参数含义：该参数用于控制AMF是否支持对AMF内Serving Plmn改变的移动性管理流程增强处理。  数据来源：全网规划 取值范围： NOT_SUPPORT（不支持）SUPPORT（支持）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST MULTISRVPLMNEN查询当前参数配置值。  配置原则：无                                                                                                                                                                                       |
| MOBENHPLCY      | 移动性流程增强处理策略         | 可选必选说明：该参数在"MULTISRVPLMNEN"配置为"SUPPORT"时为条件可选参数。  参数含义：该参数用于控制对AMF内部Serving Plmn改变的移动性管理流程的处理策略。 当参数取值“拒绝”时，注册流程拒绝原因值受SET NGMMPROCTRL命令SRVPLMNCHGREG参数控制。  数据来源：全网规划 取值范围： “SUPPORT（支持）”：AMF支持处理Serving Plmn变更的移动性流程（包括移动、周期注册以及切换流程）。“REJECT（拒绝）”：AMF拒绝Serving Plmn变更的移动性管理流程（包括移动、周期注册以及切换流程）。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST MULTISRVPLMNEN查询当前参数配置值。  配置原则：无    |
| AMFDEVINFNTFSMF | AMF设备信息通知SMF        | 可选必选说明：该参数在"MULTISRVPLMNEN"配置为"SUPPORT"时为条件可选参数。  参数含义：该参数用于控制在AMF内Serving Plmn改变的移动性管理流程中，AMF在向SMF发送的Nsmf_PDUSession_UpdateSMContext Request消息中是否携带AMF设备信息（包括servingNfId、guami、servingNetwork）。  数据来源：全网规划 取值范围： NOT_SUPPORT（不支持）SUPPORT（支持）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST MULTISRVPLMNEN查询当前参数配置值。  配置原则：无                                                       |
| AMFGUAMIIDX     | AMF设备GUAMI索引        | 可选必选说明：该参数在"MULTISRVPLMNEN"配置为"SUPPORT"时为条件可选参数。  参数含义：该参数用于控制AMF在向UDM发送Nudm_UECM_RegistrationAMF3GppAccess Request消息时，通过该参数指定的GUAMI填充guami信元。如果不指定GUAMI索引，默认使用用户所在Serving PLMN对应的GUAMI。  数据来源：全网规划  取值范围：整数类型，取值范围是0~256。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST MULTISRVPLMNEN查询当前参数配置值。  配置原则：  本参数需要提前通过ADD GUAMI命令进行配置。  GUAMI索引的有效范围是0~255。当输入无效值（256）时，表示不指定GUAMI索引。 |

## 使用实例

设置AMF支持多Serving Plmn功能增强，执行如下命令：

```
SET MULTISRVPLMNEN:MULTISRVPLMNEN=SUPPORT;
```