# 设置会话管理GTP协议功能参数配置（SET SMGTPPROT）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：SGW-C、PGW-C、GGSN**

该命令用于设置会话管理GTP协议功能参数。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| GTPVERSION   | BEARERPCOSW   | REACWITHDEL   | REACTTRANS   | MULTIBEARERS5S8   | MULTIBEARERS2B   | NBEPCOIE   | NULLMSISDN   | PCOQOS   | PPDSWITCH   | NULLIMSI   | NWINTSECACTSW   | LTE2GUDEDBRSW   | LTEULCLSW   |
|:-------------|:--------------|:--------------|:-------------|:------------------|:-----------------|:-----------|:-------------|:---------|:------------|:-----------|:----------------|:----------------|:------------|
| GTPV2        | DISABLE       | DISABLE       | ENABLE       | DISABLE           | DISABLE          | NEG_MODE   | ENABLE       | ENABLE   | DISABLE     | DISABLE    | DISABLE         | DISABLE         | DISABLE     |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识            | 参数名称                         | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                      |
|:----------------|:-----------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GTPVERSION      | GTP协议版本                      | 可选必选说明：可选参数  参数含义：该参数用于指定GTP协议版本。  数据来源：本端规划 取值范围： “GTPV2（GTPV2）”：支持GTP协议版本为V1和V2版本。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMGTPPROT查询当前参数配置值。  配置原则：无                                                                                                                                                                                                                                                                 |
| BEARERPCOSW     | 承载级PCO开关                     | 可选必选说明：可选参数  参数含义：该参数用于配置是否支持承载级PCO处理。配置为ENABLE时，SMF作为PGW、S+PGW发送Create Bearer Rquest/Update Bearer Request消息时支持通过承载级的PCO/ePCO携带相关信息，支持单消息多承载；配置为DISABLE时，SMF作为PGW、S+PGW发送Create Bearer Rquest/Update Bearer Request消息时仅支持通过消息级的PCO携带相关信息，不支持单消息多承载。  数据来源：本端规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMGTPPROT查询当前参数配置值。  配置原则：无                                                         |
| REACWITHDEL     | 去活消息携带reactivation-request开关 | 可选必选说明：可选参数  参数含义：表示去活缺省承载消息携带reactivation-requested标识开关。在异常情况下，用户被删除缺省承载，如果没有及时接入网络，用户被叫失败。配置“去活缺省承载消息携带reactivation-requested标识开关”可以在删除缺省承载时，通过去激活请求消息中的cause值携带reactivation-requested标志要求用户重新接入网络，以达到快速的恢复IMS语音业务的目的，故而建议在配置IMS业务的情况下开启本功能开关。仅适用于SGW-C独立部署，并且SGW-C上没有配置语音APN的场景。  数据来源：全网规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMGTPPROT查询当前参数配置值。  配置原则：  适用网元为SGW-C。              |
| REACTTRANS      | 透明传输reactivation-request开关   | 可选必选说明：可选参数  参数含义：该参数表示当收到携带cause信元值为“reactivation requested”的Delete Bearer Request消息去活缺省承载时，SGW发送的Delete Bearer Request消息中是否携带cause信元值为“reactivation requested”。仅适用于SGW-C独立部署，并且SGW-C上没有配置语音APN的场景。  数据来源：全网规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMGTPPROT查询当前参数配置值。  配置原则：  适用网元为SGW-C。                                                                                             |
| MULTIBEARERS5S8 | S5S8接口支持多承载开关                | 可选必选说明：可选参数  参数含义：该参数用于设置S5S8接口支持单个GTP消息携带多个承载功能。  数据来源：全网规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMGTPPROT查询当前参数配置值。  配置原则：无                                                                                                                                                                                                                                                            |
| MULTIBEARERS2B  | S2b接口支持多承载开关                 | 可选必选说明：可选参数  参数含义：该参数用于设置S2b接口支持单个GTP消息携带多个承载功能。  数据来源：全网规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMGTPPROT查询当前参数配置值。  配置原则：无                                                                                                                                                                                                                                                             |
| NBEPCOIE        | NB-IoT场景ePCO信元携带方式           | 可选必选说明：可选参数  参数含义：该软参用于控制PGW-C在Create Session Response响应消息中携带ePCO原则。  数据来源：对端协商 取值范围： “NEG_MODE（协商模式）”：UNC按照Create Session Request消息中Indication中的EPCOSI指示携带，如果EPCOSI为0，携带PCO给左侧；如果EPCOSI为1，携带ePCO。“ENFORCING_EPCO（强制携带ePCO）”：UNC在Create Session Response响应消息中携带ePCO。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMGTPPROT查询当前参数配置值。  配置原则：  当需要强制在Create Session Response响应消息中携带ePCO时，该参数需要配置为ENFORCING-EPCO。否则配置为NEG-MODE。 |
| NULLMSISDN      | 不携带MSISDN用户激活策略              | 可选必选说明：可选参数  参数含义：该参数用于指定UNC是否允许不携带MSISDN的用户激活。 如果SET CPAPNACCESSCTRL中也配置了NULLMSISDN开关，业务流程中会优先使用该开关，不会使用本参数的配置。  数据来源：本端规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMGTPPROT查询当前参数配置值。  配置原则：  UNC作为独立SGW-C存在的业务流程中，可以不配置SET CPAPNACCESSCTRL中的NULLMSISDN开关，这个时候就使用本参数的配置。例如物联网终端，本身不携带MSISDN，可以通过本参数的配置开关，来决定是否激活此类型的会话。                                                                   |
| PCOQOS          | PCO携带QoS开关                   | 可选必选说明：可选参数  参数含义：该参数用于设置PCO/ePCO是否携带QoS信息。配置为ENABLE时PCO信元携带QoS信息，配置为DISABLE时PCO信元不携带QoS信息。  数据来源：本端规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMGTPPROT查询当前参数配置值。  配置原则：  该参数配置为DISABLE时，仅在SMF作为PGW、S+PGW且策略接口为Gx的场景下生效。其他场景下系统默认该配置为ENABLE。                                                                                                                                               |
| PPDSWITCH       | Ppd功能开关                      | 可选必选说明：可选参数  参数含义：该参数用于指定PPD（寻呼策略差异化）功能开关。  数据来源：本端规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMGTPPROT查询当前参数配置值。  配置原则：无                                                                                                                                                                                                                                                                   |
| NULLIMSI        | 不携带IMSI用户激活策略                | 可选必选说明：可选参数  参数含义：该参数用于指定是否允许不携带IMSI的用户激活。  数据来源：本端规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMGTPPROT查询当前参数配置值。  配置原则：  当UNC未配置基于APN的NULLIMSI开关时，即SET CPAPNACCESSCTRL中的NULLIMSI开关，使用本参数的配置。                                                                                                                                                                                               |
| NWINTSECACTSW   | 23G网络侧发起的二次激活开关              | 可选必选说明：可选参数  参数含义：该参数用来配置是否开启23G网络侧二次激活功能。  数据来源：本端规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMGTPPROT查询当前参数配置值。  配置原则：无                                                                                                                                                                                                                                                                   |
| LTE2GUDEDBRSW   | LTE到GU专有承载切换开关               | 可选必选说明：可选参数  参数含义：该参数用来配置LTE切GU场景下，是否允许专有承载进行切换。  数据来源：本端规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMGTPPROT查询当前参数配置值。  配置原则：无                                                                                                                                                                                                                                                             |
| LTEULCLSW       | 4G UL CL功能开关                 | 可选必选说明：可选参数  参数含义：该参数用来配置是否开启4G UL CL功能。  数据来源：本端规划 取值范围： DISABLE（不使能）ENABLE（使能）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST SMGTPPROT查询当前参数配置值。  配置原则：无                                                                                                                                                                                                                                                                     |

## 使用实例

设置SMGTPPROT配置，承载级PCO开关配置为ENABLE。

```
SET SMGTPPROT: GTPVERSION = GTPV2, BEARERPCOSW = ENABLE;
```