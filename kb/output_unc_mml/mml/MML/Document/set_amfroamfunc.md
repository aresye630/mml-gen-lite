# 设置AMF漫游功能管理参数（SET AMFROAMFUNC）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：AMF**

此命令用于设置AMF漫游功能管理参数。

## 注意事项

- 该命令执行后立即生效。

- 系统部署完成后，已经存在初始记录，参数的初始记录值如下表：

| SUBAREARSTSW   | HOSRCRSTSW   | HOSNDSRVPLMN   | HOJUDGETYPE           | SRCRLSLBOSW   | ROAMFQDNCHKSW   |   ROAMNOFQDNCAUSE | VGMLCSW   | VGMLCCTYPE          |
|:---------------|:-------------|:---------------|:----------------------|:--------------|:----------------|------------------:|:----------|:--------------------|
| NO             | NO           | YES            | PREFER_SERVINGNETWORK | YES           | NO              |                15 | NO        | NOT_USE_CLIENT_TYPE |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识            | 参数名称                        | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|:----------------|:----------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SUBAREARSTSW    | 签约区域限制信息是否生效                | 可选必选说明：可选参数  参数含义：该参数用于控制UDM签约的区域类限制类信息(禁止区域、服务区限制)对漫游用户和即将漫出场景的本网用户是否生效。  数据来源：全网规划  取值范围：当本参数设置为“NO”时，AMF忽略UDM下发的禁止区域和服务区限制信息，如果AMF本地配置了区域漫游限制信息和服务区限制，则使用本地配置进行限制检查，具体参考WSFD-105003 区域漫游限制（适用于AMF）和WSFD-105006 服务区域限制。 AMF给基站携带的移动限制信息和AMF最终使用的保持一致。 Inter注册和切换流程通过N14接口给其他AMF携带的接入限制类信息不受本参数控制。 “NO（否）”：否“YES（是）”：是  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFROAMFUNC查询当前参数配置值。  配置原则：  如果UDM下发的是归属网络签约的移动限制类信息，不适合对漫游用户和即将漫出场景的本网用户生效，推荐本参数设置为“NO”。                                                                                                                                                               |
| HOSRCRSTSW      | N2切换源侧AMF签约区域限制信息是否在目标AMF生效 | 可选必选说明：可选参数  参数含义：该参数用于控制漫游用户和跨运营商的N2切换流程中目标AMF是否使用源侧AMF携带的区域限制类信息(禁止区域、服务区限制)。  数据来源：全网规划  取值范围：当本参数设置为“NO”时，漫游用户和跨运营商的N2切换流程目标AMF不使用源侧AMF携带的区域限制类信息。如果AMF本地配置了限制类信息，则使用本地配置进行限制检查，具体参考WSFD-105003 区域漫游限制（适用于AMF）和WSFD-105006 服务区域限制。 AMF给基站携带的区域限制类信息和AMF最终使用的保持一致。 “NO（否）”：否“YES（是）”：是  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFROAMFUNC查询当前参数配置值。  配置原则：  漫游用户和跨运营商的N2切换流程中，源侧AMF携带的区域限制类信息仅代表归属地PLMN网络的移动限制诉求，不建议目标侧PLMN网络的AMF使用，否则会导致限制结果不符合预期，推荐本参数设置为“NO”。                                                                                                                                                     |
| HOSNDSRVPLMN    | 切换流程源侧AMF是否携带SRVPLMN        | 可选必选说明：可选参数  参数含义：该参数用于控制漫游场景下的切换流程源侧AMF是否给目标侧AMF携带源侧的servingNetwork。AMF可以在Namf_Communication_CreateUEContext消息中携带servingNetwork信元标识源侧的ServingPLMN。  数据来源：全网规划 取值范围： “NO（否）”：否“YES（是）”：是  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFROAMFUNC查询当前参数配置值。  配置原则：  目标侧AMF可以根据源侧的ServingPLMN判断本次切换流程是否为跨PLMN场景，从而针对跨PLMN切换场景做业务增强处理，推荐本参数设置为“YES”。                                                                                                                                                                                                                                                                            |
| HOJUDGETYPE     | 目标侧AMF识别跨PLMN切换流程方法         | 可选必选说明：可选参数  参数含义：该参数用于控制切换流程中目标侧AMF使用Namf_Communication_CreateUEContext消息中的哪个信元来识别本次切换流程是否为跨PLMN场景。针对跨PLMN的切换流程，AMF可以做漫游场景的业务增强处理。  数据来源：全网规划 取值范围： “PREFER_SERVINGNETWORK（优先使用servingNetwork信元）”：优先使用Namf_Communication_CreateUEContext消息中的servingNetwork信元。如果servingNetwork信元不存在，则使用n2NotifyUri信元。“N2NOTIFYURI（使用n2NotifyUri信元）”：使用Namf_Communication_CreateUEContext消息中的n2NotifyUri信元。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFROAMFUNC查询当前参数配置值。  配置原则：  29518 g80协议推荐使用servingNetwork信元来判断N2切换流程是否跨PLMN，推荐本参数设置为“PREFER_SERVINGNETWORK”。                                                                        |
| SRCRLSLBOSW     | Inter移动性流程源侧AMF是否释放LBO模式会话  | 可选必选说明：可选参数  参数含义：该参数用于控制跨PLMN的移动性流程（5G内切换流程、注册流程、5到4切换、5到4注册流程）中源侧AMF是否释放漫游LBO模式会话。  数据来源：本端规划 取值范围： “NO（否）”：否“YES（是）”：是  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFROAMFUNC查询当前参数配置值。  配置原则：  源侧AMF在跨PLMN的移动性流程释放漫游LBO模式会话，可以简化目标侧AMF/MME的会话处理，避免目标侧AMF/MME再通知源侧AMF释放LBO会话，推荐本参数设置为“YES”。                                                                                                                                                                                                                                                                                                                              |
| ROAMFQDNCHKSW   | 漫游场景通信FQDN检查开关              | 可选必选说明：可选参数  参数含义：该参数用于控制漫游用户的所有注册流程/UDM故障重选/UDM Bypass恢复流程中AMF和对端NF(AUSF/UDM/5G-EIR/AMF)通过SEPP或SCP进行跨运营商通信时，AMF是否检查对端NF的服务发现结果中的InterPlmnFqdn。如果本参数设置为“YES（是）”，AMF检查对端NF的服务发现结果，如果没有InterPlmnFqdn，则不允许用户接入，注册拒绝原因值受ROAMNOFQDNCAUSE控制。如果本参数设置为“NO（否）”，AMF不检查对端NF的服务发现结果中是否有InterPlmnFqdn，尝试和对端NF通信，若通信失败则不允许用户接入，注册拒绝原因值固定为#111。  数据来源：全网规划 取值范围： “NO（否）”：否“YES（是）”：是  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFROAMFUNC查询当前参数配置值。  配置原则：  AMF在跨运营商通信前提前对服务发现结果中的InterPlmnFqdn做检查，可以减少和对端NF的无效消息交互，缩短异常流程时长，建议本参数设置为“YES（是）”。                                                                                           |
| ROAMNOFQDNCAUSE | 漫游场景通信无FQDN注册拒绝原因值          | 可选必选说明：该参数在"ROAMFQDNCHKSW"配置为"YES"时为条件必选参数。  参数含义：该参数用于控制漫游用户的所有注册流程中AMF和对端NF(AUSF/UDM/5G-EIR/AMF)跨运营商通信时，如果AMF没有对端NF的InterPlmnFqdn时拒绝用户接入或去注册用户时，下发给UE的原因值。  数据来源：全网规划  取值范围：整数类型，取值范围是0~111。  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFROAMFUNC查询当前参数配置值。  配置原则：  参数取值为0，表示不使用特殊指定原因值，发生该异常时系统将下发#15（No suitable cells in tracking area）原因值。  原因值为1表示非协议定义原因值，不建议配置。  参数修改为非0值，可能会改变相应拒绝类话统指标的变化和终端的行为。                                                                                                                                                                                                               |
| VGMLCSW         | 否携带V-GMLC地址                 | 可选必选说明：可选参数  参数含义：该参数用于控制漫游用户向UDM注册时是否携带V-GMLC地址。当本参数设置为“YES（是）”时，AMF向UDM发送Nudm_UEContextManagement_Registration请求消息时携带vgmlcAddress信元，当网络侧需要向漫游用户发起定位时，H-GMLC从UDM获取到V-GMLC地址后，通过V-GMLC向用户所在的AMF发起定位流程，从而获得用户位置。 ADD AMFN8CMPTPLCY命令的GMLCSW参数开关优先级高于SET AMFROAMFUNC命令的VGMLCSW参数开关。优先按照号段匹配ADD AMFN8CMPTPLCY命令的GMLCSW参数开关，匹配到则按照ADD AMFN8CMPTPLCY命令的GMLCSW参数开关进行控制，匹配不到则按SET AMFROAMFUNC命令的VGMLCSW参数开关进行控制。  数据来源：全网规划 取值范围： “YES（是）”：是“NO（否）”：否  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFROAMFUNC查询当前参数配置值。  配置原则：  当网络侧需要对漫游用户定位，且H-GMLC不支持服务发现获取V-GMLC地址时，推荐本参数设置为“YES”。                                              |
| VGMLCCTYPE      | V-GMLC客户端类型                 | 可选必选说明：可选参数  参数含义：该参数用于控制漫游用户选择V-GMLC时使用的客户端类型。当VGMLCSW设置为“YES（是）”时，AMF使用本参数配置的客户端类型服务发现V-GMLC。  数据来源：全网规划 取值范围： NOT_USE_CLIENT_TYPE（不使用ClientType发现V-GMLC）EMERGENCY_SERVICES（紧急服务的外部客户端）VALUE_ADDED_SERVICES（增值业务外部客户端）PLMN_OPERATOR_SERVICES（PLMN运营商业务外部客户端）LAWFUL_INTERCEPT_SERVICES（合法拦截服务的外部客户端）PLMN_OPERATOR_BROADCAST_SERVICES（PLMN运营商广播业务外部客户端）PLMN_OPERATOR_OM（PLMN运营商运维外部客户端）PLMN_OPERATOR_ANONYMOUS_STATISTICS（PLMN操作员匿名统计外部客户端）PLMN_OPERATOR_TARGET_MS_SERVICE_SUPPORT（PLMN运营商目标MS服务支持的外部客户端）  默认值：无。执行命令并不输入该参数时，该参数保持系统当前配置不变，可通过LST AMFROAMFUNC查询当前参数配置值。  配置原则：  若漫游用户开启定位功能时，建议本参数设置为“PLMN_OPERATOR_OM”。 |

## 使用实例

设置漫游用户，不使用UDM下发的移动限制接入类信息，跨PLMN切换流程不使用源侧AMF携带的移动限制接入类信息，执行如下命令：

```
SET AMFROAMFUNC:SUBAREARSTSW=NO,HOSRCRSTSW=NO;
```