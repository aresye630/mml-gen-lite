# 设置AMF服务化接口兼容性参数（SET AMFSBICMPT）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：AMF**

该命令用于设置AMF服务化接口兼容性参数，以满足运营商实现对现网设备兼容性特殊控制的需求。

## 注意事项

- 该命令执行后立即生效。

- 当ADD AMUEPLCYCTRL命令中的“NEARBYACCSW”参数设置为“YES（是）”，且用户签约的DNN前缀匹配“NEARBYKEYWD”配置的关键字时，本命令的HAMPCFID参数不生效。
- AMF Pool用户迁移场景下，N14接口是否传递AM策略和UE策略相关信元同时受本命令参数、SET AMFPLCYFUNC命令参数和软参DWORD80 BIT2、DWORD80 BIT10控制。
- N14接口传递如下AM策略和UE策略相关信元时参数取值需保持一致，否则会导致PCF上AM策略偶联或UE策略偶联残留，具体信元如下：
- N14接口是否携带pcfId（OLDPCFID）、N14接口是否携带pcfSetId（OLDPCFSETID）、N14接口是否携带pcfAmPolicyUri（OLDAMPLCYURI）、N14接口是否携带hpcfId（OLDHPCFID）和N14接口是否携带pcfUePolicyUri（OLDUEPLCYURI）。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| SBITYPE   | N11MSGTYPE   | SNDUPTZ   | SNDRATTYPE   | SNDREDCAPIND   | SNDPRVEDRXINFO   | SNDPCFRFSP   | AMPCFNI   | RADIOCAPPAGING   | HAMPCFID   | OLDPCFID   | OLDPCFSETID   | OLDAMPLCYURI   | OLDAMPLCYTRIG   | OLDHPCFID   | OLDSMFSELINFO   | SNDPEIPSINFO   | OLDUEPLCYURI   | OLDUEPLCYTRIG   | SUBRSPN2CLASS   | EVTPERIOD   | EVTGNBLST   |
|:----------|:-------------|:----------|:-------------|:---------------|:-----------------|:-------------|:----------|:-----------------|:-----------|:-----------|:--------------|:---------------|:----------------|:------------|:----------------|:---------------|:---------------|:----------------|:----------------|:------------|:------------|
| N11       | UPDATE       | NO        | NO           | YES            | NO               | NO           | NO        | NO               | NO         | YES        | YES           | YES            | YES             | YES         | YES             | NO             | YES            | YES             | NO              | NO          | NO          |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识           | 参数名称                               | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                       |
|:---------------|:-----------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SBITYPE        | 服务化接口类型                            | 可选必选说明：必选参数  参数含义：该参数用于指定服务化接口类型，根据接口类型来确认是否需要配置相应的消息接口兼容性。  数据来源：全网规划 取值范围： N8（AMF与UDM之间的接口）N11（AMF与SMF之间的接口）N12（AMF与AUSF之间的接口）N14（AMF与AMF之间的接口）N15（AMF与PCF之间的接口）N17（AMF与5G-EIR之间的接口）N20（AMF与SMSF之间的接口）N22（AMF与NSSF之间的接口）N50（AMF与CBCF之间的接口）  默认值：无。  配置原则：无                                                                                                                                                                               |
| N11MSGTYPE     | N11接口消息类型                          | 可选必选说明：该参数在"SBITYPE"配置为"N11"时为条件可选参数。  参数含义：该参数用于指定N11接口消息类型，根据消息类型来确认是否需要配置相应的消息接口兼容性。  数据来源：全网规划 取值范围： UPDATE（更新会话上下文请求）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFSBICMPT查询当前参数配置值。  配置原则：无                                                                                                                                                                                                                                           |
| SNDUPTZ        | 时区变更是否通知SMF                        | 可选必选说明：该参数在"N11MSGTYPE"配置为"UPDATE"时为条件可选参数。  参数含义：该参数用于控制AMF是否单独在向SMF发送Update SM Context Request消息更新时区或者夏令时信息。随路消息中携带时区和夏令时信息不受本参数控制。  数据来源：全网规划 取值范围： “NO（否）”：否“YES（是）”：是  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFSBICMPT查询当前参数配置值。  配置原则：无                                                                                                                                                                                           |
| SNDRATTYPE     | 是否给SMSF携带RATTYPE                   | 可选必选说明：该参数在"SBITYPE"配置为"N20"时为条件可选参数。  参数含义：该参数用于控制AMF向SMSF发送Nsmsf_SMService_Activate Request消息时是否携带ratType信元。  数据来源：全网规划 取值范围： “YES（是）”：是“NO（否）”：否  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFSBICMPT查询当前参数配置值。  配置原则：  当SMSF需要使用RatType用于话单导出时，可以将该参数设置为“YES(是)”。                                                                                                                                                                       |
| SNDREDCAPIND   | 是否携带RedCap指示                       | 可选必选说明：该参数在"SBITYPE"配置为"N14"时为条件可选参数。  参数含义：该参数用于控制RedCap用户的5G内Inter移动性流程中，AMF和对端AMF交互用户上下文时UeContext信元中是否携带redCapInd子信元。  数据来源：全网规划 取值范围： “NO（否）”：否“YES（是）”：是  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFSBICMPT查询当前参数配置值。  配置原则：  按3GPP协议定义，AMF应在Inter移动性流程中向对端AMF提供RedCap指示（redCapInd为True表示该用户为RedCap用户）。注册重定向流程，如果初始AMF不向目标AMF提供RedCap指示，则目标AMF会将该用户当作普通NR用户处理。                                                                      |
| SNDPRVEDRXINFO | 是否携带eDRX私有信元                       | 可选必选说明：该参数在"SBITYPE"配置为"N14"时为条件可选参数。  参数含义：该参数用于控制AMF Pool迁移流程中，AMF向目标AMF传递用户上下文时UeContext信元中是否携带eDRX相关的私有信元，包括eDRX寻呼周期和寻呼窗口时长。  数据来源：全网规划 取值范围： “NO（否）”：否“YES（是）”：是  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFSBICMPT查询当前参数配置值。  配置原则：  当AMF Pool内有异厂商AMF时，需要将本参数设置为“NO（否）”。  当AMF Pool内无异厂商AMF且本AMF开通了eDRX特性时，建议将本参数设置为“YES（是）”。  如果eDRX用户迁移到目标AMF时不携带eDRX相关私有信元，会导致迁移用户在目标AMF上下行寻呼成功率降低，直到用户在目标AMF上重新进行一次注册流程并协商eDRX参数后，寻呼成功率才能恢复正常。 |
| SNDPCFRFSP     | 是否携带PcfRfsp                        | 可选必选说明：该参数在"SBITYPE"配置为"N14"时为条件可选参数。  参数含义：该参数用于控制用户的5G内Inter移动性流程中，AMF和对端AMF交互用户上下文时UeContext信元中是否携带pcfRfsp子信元。  数据来源：全网规划 取值范围： “NO（否）”：否“YES（是）”：是  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFSBICMPT查询当前参数配置值。  配置原则：无                                                                                                                                                                                                               |
| AMPCFNI        | 是否携带动态NI                           | 可选必选说明：该参数在"SBITYPE"配置为"N14"时为条件可选参数。  参数含义：该参数用于控制Inter AMF流程与POOL迁移流程中老侧AMF是否在UeContext携带中携带AM-PCF下发的签约动态NI。  数据来源：全网规划 取值范围： “NO（否）”：否“YES（是）”：是  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFSBICMPT查询当前参数配置值。  配置原则：无                                                                                                                                                                                                                  |
| RADIOCAPPAGING | 是否携带UE Radio Capability for Paging | 可选必选说明：该参数在"SBITYPE"配置为"N14"时为条件可选参数。  参数含义：该参数用于控制5G内Inter移动性流程中，AMF和对端AMF交互用户上下文时UeContext信元中是否携带UE Radio Capability for Paging子信元。  数据来源：全网规划 取值范围： “NO（否）”：否“YES（是）”：是  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFSBICMPT查询当前参数配置值。  配置原则：无                                                                                                                                                                                           |
| HAMPCFID       | N15接口是否携带hpcfId                    | 可选必选说明：该参数在"SBITYPE"配置为"N15"时为条件可选参数。  参数含义：该参数用于控制用户创建AM策略偶联时，AMF是否携带hpcfId信元给AM-PCF。  数据来源：全网规划 取值范围： “NO（否）”：否“YES（是）”：是  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFSBICMPT查询当前参数配置值。  配置原则：无                                                                                                                                                                                                                                          |
| OLDPCFID       | N14接口是否携带pcfId                     | 可选必选说明：该参数在"SBITYPE"配置为"N14"时为条件可选参数。  参数含义：该参数用于控制inter-AMF移动性注册（切换）时，老侧AMF是否携带pcfId信元给新侧AMF。  数据来源：全网规划 取值范围： “NO（否）”：否“YES（是）”：是  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFSBICMPT查询当前参数配置值。  配置原则：  AMF在N14接口是否传递pcfId信元同时受本参数和SET AMFPLCYFUNC中参数OLDAMPLCY的控制。  该信元需要与pcfSetId（OLDPCFSETID）、pcfAmPolicyUri（OLDAMPLCYURI）、hpcfId（OLDHPCFID）和pcfUePolicyUri（OLDUEPLCYURI）信元参数取值保持一致。                                                   |
| OLDPCFSETID    | N14接口是否携带pcfSetId                  | 可选必选说明：该参数在"SBITYPE"配置为"N14"时为条件可选参数。  参数含义：该参数用于控制inter-AMF移动性注册（切换）时，老侧AMF是否携带pcfSetId信元给新侧AMF。  数据来源：全网规划 取值范围： “NO（否）”：否“YES（是）”：是  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFSBICMPT查询当前参数配置值。  配置原则：  AMF在N14接口是否传递pcfSetId信元同时受本参数和SET AMFPLCYFUNC中参数OLDAMPLCY的控制。  该信元需要与pcfId（OLDPCFID）、pcfAmPolicyUri（OLDAMPLCYURI）、hpcfId（OLDHPCFID）和pcfUePolicyUri（OLDUEPLCYURI）信元参数取值保持一致。                                                   |
| OLDAMPLCYURI   | N14接口是否携带pcfAmPolicyUri            | 可选必选说明：该参数在"SBITYPE"配置为"N14"时为条件可选参数。  参数含义：该参数用于控制inter-AMF移动性注册（切换）时，老侧AMF是否携带pcfAmPolicyUri信元给新侧AMF。  数据来源：全网规划 取值范围： “NO（否）”：否“YES（是）”：是  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFSBICMPT查询当前参数配置值。  配置原则：  AMF在N14接口是否传递pcfAmPolicyUri信元同时受本参数和SET AMFPLCYFUNC中参数OLDAMPLCY的控制。  该信元需要与pcfId（OLDPCFID）、pcfSetId（OLDPCFSETID）、hpcfId（OLDHPCFID）和pcfUePolicyUri（OLDUEPLCYURI）信元参数取值保持一致。                                              |
| OLDAMPLCYTRIG  | N14接口是否携带amPolicyReqTriggerList    | 可选必选说明：该参数在"SBITYPE"配置为"N14"时为条件可选参数。  参数含义：该参数用于控制inter-AMF移动性注册（切换）时，老侧AMF是否携带amPolicyReqTriggerList信元给新侧AMF。  数据来源：全网规划 取值范围： “NO（否）”：否“YES（是）”：是  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFSBICMPT查询当前参数配置值。  配置原则：  AMF在N14接口是否传递amPolicyReqTriggerList信元同时受本参数和SET AMFPLCYFUNC中参数OLDAMPLCY的控制。                                                                                                                                     |
| OLDHPCFID      | N14接口是否携带hpcfId                    | 可选必选说明：该参数在"SBITYPE"配置为"N14"时为条件可选参数。  参数含义：该参数用于控制inter-AMF移动性注册（切换）时，老侧AMF是否携带hpcfId信元给新侧AMF。  数据来源：全网规划 取值范围： “NO（否）”：否“YES（是）”：是  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFSBICMPT查询当前参数配置值。  配置原则：  AMF在N14接口是否传递hpcfId信元同时受本参数和SET AMFPLCYFUNC中参数OLDAMPLCY的控制。  该信元需要与pcfId（OLDPCFID）、pcfSetId（OLDPCFSETID）、pcfAmPolicyUri（OLDAMPLCYURI）和pcfUePolicyUri（OLDUEPLCYURI）信元参数取值保持一致。                                                   |
| OLDSMFSELINFO  | N14接口是否携带smfSelInfo                | 可选必选说明：该参数在"SBITYPE"配置为"N14"时为条件可选参数。  参数含义：该参数用于控制inter-AMF移动性注册（切换）时，老侧AMF是否携带smfSelInfo信元给新侧AMF。  数据来源：全网规划 取值范围： “NO（否）”：否“YES（是）”：是  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFSBICMPT查询当前参数配置值。  配置原则：  AMF在N14接口是否传递smfSelInfo信元同时受本参数和SET AMFPLCYFUNC中参数OLDAMPLCY的控制。                                                                                                                                                             |
| SNDPEIPSINFO   | N14接口是否携带PEIPS信元以及寻呼分组标识           | 可选必选说明：该参数在"SBITYPE"配置为"N14"时为条件可选参数。  参数含义：该参数用于控制AMF Pool迁移流程中，AMF向目标AMF传递用户上下文时UeContext信元中是否携带PEIPS信元以及寻呼分组标识。  数据来源：对端协商 取值范围： “NO（否）”：否“YES（是）”：是  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFSBICMPT查询当前参数配置值。  配置原则：  当AMF Pool内有异厂商AMF时，需要将本参数设置为“NO（否）”。  当AMF Pool内无异厂商AMF且本AMF支持PEIPS特性时，建议将本参数设置为“YES（是）”。  如果PEIPS用户迁移到目标AMF时不携带PEIPS相关私有信元，可能会导致迁移用户无法支持基于分组的智能寻呼。                                                          |
| OLDUEPLCYURI   | N14接口是否携带pcfUePolicyUri            | 可选必选说明：该参数在"SBITYPE"配置为"N14"时为条件可选参数。  参数含义：该参数用于控制inter-AMF移动性注册（切换）时，老侧AMF是否携带pcfUePolicyUri信元给新侧AMF。  数据来源：全网规划 取值范围： “NO（否）”：否“YES（是）”：是  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFSBICMPT查询当前参数配置值。  配置原则：  AMF在N14接口是否传递pcfUePolicyUri信元同时受本参数和SET AMFPLCYFUNC中参数OLDUEPLCY的控制。  该信元需要与pcfId（OLDPCFID）、pcfSetId（OLDPCFSETID）、pcfAmPolicyUri（OLDAMPLCYURI）和hpcfId（OLDHPCFID）信元参数取值保持一致。                                              |
| OLDUEPLCYTRIG  | N14接口是否携带uePolicyReqTriggerList    | 可选必选说明：该参数在"SBITYPE"配置为"N14"时为条件可选参数。  参数含义：该参数用于控制inter-AMF移动性注册（切换）时，老侧AMF是否携带uePolicyReqTriggerList信元给新侧AMF。  数据来源：全网规划 取值范围： “NO（否）”：否“YES（是）”：是  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFSBICMPT查询当前参数配置值。  配置原则：  AMF在N14接口是否传递uePolicyReqTriggerList信元同时受本参数和SET AMFPLCYFUNC中参数OLDUEPLCY的控制。                                                                                                                                     |
| SUBRSPN2CLASS  | 是否携带N2InformationClass             | 可选必选说明：该参数在"SBITYPE"配置为"N50"时为条件可选参数。  参数含义：该参数用于控制AMF向CBCF发送Namf_Communication_NonUeN2InfoSubscribe Response时，是否携带N2InformationClass信元。  数据来源：对端协商 取值范围： “NO（否）”：否“YES（是）”：是  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFSBICMPT查询当前参数配置值。  配置原则：无                                                                                                                                                                                        |
| EVTPERIOD      | N14接口是否携带repPeriod                 | 可选必选说明：该参数在"SBITYPE"配置为"N14"时为条件可选参数。  参数含义：该参数用于控制inter-AMF移动性注册（切换）时，老侧AMF是否携带repPeriod信元给新侧AMF。  数据来源：全网规划 取值范围： “NO（否）”：否“YES（是）”：是  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFSBICMPT查询当前参数配置值。  配置原则：  若AMF支持周期性订阅，建议将本参数设置为“YES（是）”。                                                                                                                                                                                               |
| EVTGNBLST      | N14接口是否携带GlobalGnbIdList           | 可选必选说明：该参数在"SBITYPE"配置为"N14"时为条件可选参数。  参数含义：该参数用于控制inter-AMF移动性注册（切换）时，老侧AMF是否携带GlobalGnbIdList信元给新侧AMF。  数据来源：全网规划 取值范围： “NO（否）”：否“YES（是）”：是  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFSBICMPT查询当前参数配置值。  配置原则：  若AMF支持类型为UE_LOCATION_TRENDS的周期性事件订阅，建议将本参数设置为“YES（是）”。                                                                                                                                                                 |

## 使用实例

- 当AMF支持单独向SMF发送Nsmf\_PDUSession\_UpdateSmContext Request消息用于更新时区或者夏令时信息，执行如下命令：

  ```
  SET AMFSBICMPT:SBITYPE=N11,N11MSGTYPE=UPDATE,SNDUPTZ=YES;
  ```
- 当需要AMF向SMSF发送Nsmsf\_SMService\_Activate Request消息携带ratType信元时，执行如下命令：

  ```
  SET AMFSBICMPT:SBITYPE=N20,SNDRATTYPE=YES;
  ```
- 当AMF和对端AMF交互用户上下文时UeContext信元中需要携带redCapInd子信元，执行如下命令：

  ```
  SET AMFSBICMPT: SBITYPE=N14, SNDREDCAPIND=YES;
  ```
- 当AMF向目标AMF传递用户上下文时UeContext信元中需要携带eDRX相关的私有信元，执行如下命令：

  ```
  SET AMFSBICMPT: SBITYPE=N14, SNDPRVEDRXINFO=YES;
  ```