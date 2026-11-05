# 增加语音部署配置(ADD VOICEDEPLOY)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用网元：MME**

该命令用于增加UE使用E-UTRAN网络接入时的IMS VoPS语音部署方案配置。UE使用E-UTRAN网络接入时可以选择两种语音部署方案：

- IMS VoPS（IMS Voice over PS session），即基于IMS网络提供语音业务。PS网络上部署专门的IMS APNNI，用于承载IMS业务相关的信令和数据。
- CSFB（Circuit Switched Fallback），利用现有的GSM /UMTS网络实现语音通话的一种语音解决方案。用户进行语音业务时，由EPS（Evolved Packet System）网络指示用户回落到目标GSM/UMTS电路域（CS）网络之后，再发起语音呼叫。

#### 注意事项

- 对于该命令执行后新接入的UE，该命令立即生效。该命令执行时已经在系统中注册过的UE，系统会在UE下一次进行Attach/TAU业务流程时，根据最新的配置对UE进行业务指示。
- 最多可以输入1024条记录。
- 此配置涉及用户群语音策略控制特性（特性编号：WSFD-201002，License项：LKV2VPCU01），执行命令请使用**DSP LICENSE**命令确认对应特性license是否得到授权，执行**LST LICENSESWITCH**命令确认特性开关状态为“ENABLE(打开)”。

#### 本地用户权限

manage-ug；system-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识          | 参数名称                        | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|:--------------|:----------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SUBRANGE      | 用户范围                        | 可选必选说明：必选参数 参数含义：该参数用于指定所包含的用户范围。 数据来源：全网规划 取值范围：“ALL_USER（所有用户）”“HOME_USER（本网用户）”“FOREIGN_USER（外网用户）”“IMSI_PREFIX（指定IMSI前缀）” 默认值：无 配置原则：“SUBRANGE（用户范围）”的优先级从高到低为：“IMSI_PREFIX（指定IMSI前缀）”，“FOREIGN_USER（外网用户）”或“HOME_USER（本网用户）”，“ALL_USER（所有用户）”。系统优先查找高优先级的配置记录，如果查找不到，再查找低优先级的配置记录。                                                                                                                                                                                                                                                                                                                                                                       |
| NOID          | 运营商标识                       | 可选必选说明：条件必选参数 参数含义：该参数用于指定运营商标识。 前提条件：该参数在“SUBRANGE（用户范围）”配置为“FOREIGN_USER（外网用户）”或“HOME_USER（本网用户）”后生效。 数据来源：全网规划 取值范围：0～64，128～254 默认值：无 配置原则：当用户为MNO用户时，该参数需要配置为0或128～254之间的值，该取值必须和ADD MNO中配置的“MNOID”参数取值相同。若该参数需要配置为1～64之间的值时，须先在ADD MVNO中配置取值相同的“MVNOID”参数。  说明： 对于外网用户，该参数是与其归属运营商签订可漫游协议，为其提供服务的MNO/MVNO运营商标识。对于本网用户，该参数是为该用户归属的MNO/MVNO运营商标识。                                                                                                                                                                                                                                                                                                         |
| IMSIPRE       | IMSI前缀                      | 可选必选说明：条件必选参数 参数含义：该参数用于系统对用户的IMSI进行匹配，从而区分不同的用户群。 前提条件：此参数在“SUBRANGE（用户范围）”设置为“IMSI_PREFIX（指定IMSI前缀）”时有效。 数据来源：全网规划 取值范围：1～15位十进制数字字符串 默认值：无  说明： IMSI前缀的匹配方式采取由前向后的最长匹配，即若对于用户可以匹配到多个用户群，则使用IMSI前缀最长的用户群配置。比如：同时存在IMSI前缀为30801和3080101的配置，则优先使用3080101的配置。                                                                                                                                                                                                                                                                                                                                                                                                  |
| IMSVOPS       | IMS VoPS                    | 可选必选说明：必选参数 参数含义：该命令用于设置是否允许用户使用IMS VoPS业务。 数据来源：全网规划 取值范围：“NO（否）”“YES（是）” 默认值：无 配置原则： NO：表示系统不允许用户使用IMS VoPS业务。UE在E-UTRAN网络进行Attach/TAU流程时，系统通过置位Attach/TAU Accept消息中的EPS Network Feature Support信元的IMS VoPS指示位为0，通知UE不允许使用IMS VoPS业务，请参见3GPP TS 24.301。YES：表示系统允许用户使用IMS VoPS业务。如果用户签约了IMS APN网络标识，UE在E-UTRAN网络进行Attach/TAU流程时，系统通过置位Attach/TAU Accept消息EPS Network Feature Support信元的IMS VoPS指示位为1，通知UE可以使用IMS VoPS业务，请参见3GPP TS 24.301。                                                                                                                                                                                                                   |
| APNNI         | IMS APN网络标识                 | 可选必选说明：条件可选参数 参数含义：该参数表示UE的归属运营商网络用于IMS VoPS业务的APN网络标识。GSMA IR.92标准推荐使用“IMS”作为IMS APN。如果不输入，系统在决策是否允许UE使用IMS VoPS业务上时，不考虑UE是否签约了IMS APN。 前提条件：此参数在“IMSVOPS（IMS VoPS）”设置为“YES”时，才需要配置。 数据来源：全网规划 取值范围：字符串长度范围1~62。 默认值：无 配置原则： “APNNI”（APN网络标识）由一个或多个LABEL构成，各LABEL间用“.”间隔。每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”，字母不区分大小写。APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾，不能配置为“*”。  说明： UE签约了该APN网络标识，UNC系统才允许其使用IMS VoPS业务。UNC设备所属运营商的网络中必须部署了该APN网络标识用于IMS VoPS业务，UE才能正常使用IMS VoPS业务。如果配置错误，可能会导致UE在E-UTRAN网络无法正常使用语音业务，请谨慎设置。                                                                                                                          |
| UETYPE        | 终端类型                        | 可选必选说明：条件可选参数 参数含义：该参数表示系统在决定是否允许用户使用IMS VoPS业务时，针对哪类UE惯用类型（UE's usage setting）的终端考虑其SRVCC能力。当UE的类型和配置匹配时，如果网络或者UE不支持SRVCC时，系统不允许用户使用IMS VoPS业务。 前提条件：此参数在“IMSVOPS（IMS VoPS）”设置为“YES”时有效。 数据来源：全网规划 取值范围：“VOICE_CENTRIC(Voice Centric)”“DATA_CENTRIC(Data Centric)” 默认值：“VOICE_CENTRIC(Voice Centric)” 配置原则：当终端类型为“VOICE_CENTRIC(Voice Centric)”时，其语音业务具有更高的优先级，终端会主动保证语音业务的可用性。用户在进行VoLTE语音业务过程中移动到无E-UTRAN网络覆盖的区域时，会因为网络或UE不支持SRVCC而导致通话中断，无法保证语音业务的连续性。因此当网络或UE不支持SRVCC时，建议勾选此选项，系统不允许用户使用IMS VoPS业务。这样，终端会主动选择CSFB等其它方式保证语音业务，以避免上述语音业务不连续的问题。当终端类型“DATA_CENTRIC(Data Centric)”时，数据业务具有更高的优先级，终端不会主动保证语音的可用性，网络也没有必要保证其语音业务连续性，因此建议不选中这类终端。               |
| SUBRFSP       | 禁止特征RFSP用户使用IMS VoPS        | 可选必选说明：条件可选参数 参数含义：该参数表示系统是否禁止签约了特征RFSP的用户使用IMS VoPS业务。 前提条件：该参数在“IMSVOPS（IMS VoPS）”参数设置为“YES（是）”时，才需要配置。 数据来源：全网规划 取值范围：“NO（否）”“YES（是）” 默认值：“NO（否）” 配置原则：“NO（否）”：系统不禁止在HSS中签约了特征RFSP的用户使用IMS VoPS业务。“YES（是）”：系统禁止在HSS中签约了特征RFSP的用户使用IMS VoPS业务，但允许未签约特征RFSP的用户使用IMS VoPS业务。使用该选项时，运营商需要为希望受控的用户签约特征RFSP，并通过ADD SPECRFSPVALUE命令设置特征RFSP的取值范围。                                                                                                                                                                                                                                                                                                                 |
| RFSPIDX       | 特征RFSP索引                    | 可选必选说明：条件必选参数 参数含义：该参数用于指定禁止使用IMS VoPS业务用户的特征RFSP索引。 前提条件：此参数在“SUBRFSP（禁止特征RFSP用户使用IMS VoPS）”设置为“YES（是）”后生效。 数据来源：本端规划 取值范围：0~49 默认值：无  说明： 该特征RFSP索引必须已经通过ADD SPECRFSPVALUE命令添加，且其“TYPE（类型）”为“IMS_VOPS(IMS VoPS限制)”。可执行LST SPECRFSPVALUE进行查看。                                                                                                                                                                                                                                                                                                                                                                                                                |
| IMEICTRL      | 基于IMEI控制                    | 可选必选说明：条件可选参数 参数含义：该参数用于配置基于IMEI的IMS VoPS业务的控制方式。 前提条件：此参数在“IMSVOPS（IMS VoPS）”设置为“YES”时有效。 数据来源：本端规划 取值范围：“NO(否)”“WHITELIST(白名单)”“BLACKLIST(黑名单)” 默认值：“NO（否）” 配置原则：当需要根据IMEI控制IMS VoPS业务时才将参数设置为“WHITELIST(白名单)”或者“BLACKLIST(黑名单)”，例如需要限定只有某几款手机允许使用IMS VoPS功能，或者需要限定只有某几款手机不允许使用IMS VOPS功能。将参数设置为“WHITELIST(白名单)”或者“BLACKLIST(黑名单)”前，请确保已经通过ADD S1IMEICFG命令开启了GET IMEI功能，MME能获取到手机的IMEI信息。  说明： 当参数设置为“WHITELIST(白名单)”或者“BLACKLIST(黑名单)”时，“基于IMEI的语音策略控制”特性的相关license授权并开启后，此参数配置才生效（特性编号：WSFD-201004，License项：LKV2VPCI01）。                                                                                                                                  |
| IMEIGPID      | IMEI群组标识                    | 可选必选说明：条件必选参数 参数含义：IMEI群组的标识。 前提条件：该参数在“IMEICTRL(基于IMEI控制)”参数设置为“WHITELIST(白名单)”或者“BLACKLIST(黑名单)”时，有效。“IMEI群组标识”已经通过ADD IMEIGP配置。 数据来源：本端规划 取值范围：1~50 默认值：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| CSFBNOTPREIND | CS Fallback not preferred指示 | 可选必选说明：条件可选参数 参数含义：该命令用于设置是否向用户发送CS fallback not preferred指示。 前提条件：此参数在“IMSVOPS（IMS VoPS）”设置为“YES”时有效。 数据来源：全网规划 取值范围：“NO（否）”“YES（是）” 默认值：“NO（否）” 配置原则：在“CSFBNOTPREIND”配置为“No”的情况下：UNC不向UE发送CS fallback not preferred指示，UE根据Voice Domain Preference选择对应的语音业务。在“CSFBNOTPREIND”配置为“Yes”的情况下：如果UE成功为语音业务进行了CS域注册，并且UE的Voice Domain Preference为“CS voice preferred， IMS PS Voice as secondary”或“IMS PS Voice preferred， CS voice as secondary”，Attach/TAU Accept消息EPS Network Feature Support信元的IMS VoPS指示位为1，系统在Attach/TAU Accept消息通过置位Additional update result信元取值为1，向UE指示“CS Fallback Not Preferred”，请参见3GPP TS 24.301。  说明： 用户最终使用何种语音业务和各产商终端实现有关，目前推荐使用默认值。 |

#### 使用实例

1. 运营商A允许本网用户和签约了特征RFSP的用户使用VoLTE语音业务，且优先使用VoLTE语音业务，不允许外网用户使用VoLTE语音业务：
   - 配置本网用户的语音策略：

     ```
     ADD VOICEDEPLOY: SUBRANGE=HOME_USER, NOID=0, IMSVOPS=YES, APNNI="IMS", SUBRFSP=NO, CSFBNOTPREIND=YES;
     ```
   - 配置外网用户的语音策略：

     ```
     ADD VOICEDEPLOY: SUBRANGE=FOREIGN_USER, NOID=0, IMSVOPS=NO;
     ```
2. 运营商A允许特定型号终端的本网用户使用VoLTE语音业务，且优先使用VoLTE语音业务，不允许外网用户使用VoLTE语音业务：
   - 配置本网用户的语音策略：

     ```
     ADD VOICEDEPLOY: SUBRANGE=HOME_USER, NOID=0, IMSVOPS=YES, APNNI="IMS", IMEICTRL=WHITELIST, IMEIGPID=1, CSFBNOTPREIND=YES;
     ```
   - 配置外网用户的语音策略：

     ```
     ADD VOICEDEPLOY: SUBRANGE=FOREIGN_USER, NOID=0, IMSVOPS=NO;
     ```