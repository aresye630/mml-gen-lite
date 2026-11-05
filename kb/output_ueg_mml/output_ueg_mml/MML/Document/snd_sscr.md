# 发送用户下线请求(SND SSCR)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**须知** 

- 此命令是高危命令，如果执行不当会使在线用户下线，需联系华为技术支持确认后再执行。
- 该操作为系统高危操作，需要第二个具有二次授权权限的用户授权后才能执行该操作。请输入授权用户名和密码。

该命令用于UPCF主动发起用户下线请求。为了达到对全网或指定对端的用户实现管控的目的，UPCF支持通过MML接口发送用户下线请求消息，使全网或指定对端的用户下线。当执行该命令后，全网或指定对端的当前在线的用户会全部下线。

- 该命令执行后，会导致短时间内存在大量信令消息。各接口对应的消息类型如下：
  - Gx接口：RAR(ASR)、CCR
  - Rx接口：RAR(ASR)、STR
  - N5接口：Npcf\_PolicyAuthorization\_Notify Request（/terminate）、Npcf\_PolicyAuthorization\_Delete
  - N7接口：Npcf\_SMPolicyControl\_UpdateNotify Request（/terminate）、Npcf\_SMPolicyControl\_Delete Request
  - N15接口：Npcf\_AMPolicyControl\_UpdateNotify Request（/terminate）、Npcf\_AMPolicyControl\_Delete Request、Npcf\_UEPolicyControl\_UpdateNotify Request（/terminate）、Npcf\_UEPolicyControl\_Delete Request
  - N23接口：Nnwdaf\_EventsSubscription\_UnSubscribe Request
  - N24接口：Npcf\_AMPolicyControl\_UpdateNotify Request（/terminate）、Npcf\_AMPolicyControl\_Delete Request
  - N28接口：Nchf\_SpendingLimitControl\_Unsubscribe Request
- 该命令执行后，可以通过**DSP SSCSTATUS**命令查询用户下线状态信息。
- 该命令执行后，可以通过**STP SSCR**命令停止强制用户下线任务。

**说明** 

- UPCF不支持同时处理多个强制用户下线的任务，不论是全网强制用户下线任务或者向指定对端强制用户下线任务。执行该命令前请先执行查询命令**DSP SSCSTATUS**，如果已经有任务正在执行中，请等正在执行的任务完成后再执行，否则正在执行任务的服务会忽略对新任务的处理。
- **SND SSCR**命令执行返回结果后，在强制用户下线的过程中，新上线的会话不受影响。

## 注意事项

- 执行该命令会使全网所有用户或者指定对端的所有用户下线。已经被强制下线的用户再次上线可能会引起系统流控，请谨慎使用。当系统流控产生时会上报“ALM-34148 DLB流控控制告警”、“ALM-34150 PES流控控制告警”或“ALM-34147 HLB流量控制告警”，请参考告警帮助解决。
- 在全网用户下线任务启动前，可以通过如下软参设置下线任务，执行该命令后：
  - 根据软参“BLC\_DELSSINTERVAL（周期下线时间间隔）”设置的时间间隔，定时发送用户下线请求消息。
  - 根据软参“BLC\_DELSSINVALIDINTERVAL（下线任务有效期）”设置的有效期，判断下线任务是否到期。
  - 根据软参“BLC\_DELSSNUM（每次处理的会话个数）”设置的个数，发送RAR或者Npcf\_SMPolicyControl\_UpdateNotify消息释放会话。
- 踢会话下线速度不建议设置大于200，速度计算公式：1000/BLC\_DELSSINTERVAL \* BLC\_DELSSNUM。
- 踢会话下线的速度依赖对端能力，建议和对端协商。

## 参数说明

| 参数标识       | 参数名称       | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
|:-----------|:-----------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SSTYPE     | 会话类型       | 用于标识会话类型。 取值范围： ALL(ALL)：支持将全网用户（从Gx、Rx、N5、N7和N15接口上线的用户）强制下线SpecificPCEF(SpecificPCEF)：支持将指定PCEF的Gx会话强制下线DRA_SpecificPCEF(DRA_SpecificPCEF)：支持将指定DRA-PCEF的Gx会话强制下线SpecificAF(SpecificAF)：支持将指定AF的Rx会话强制下线DRA_SpecificAF(DRA_SpecificAF)：支持将指定DRA-AF的Rx会话强制下线SUBLIST(SUBLIST)：支持按用户列表强制用户下线该用户列表是通过SET SERDBG: CMDTYPE=STR_STAT_SUBLIST, ATTRID=对象属性列表, ATTRSTRINGVALUE=对象属性值; 命令收集查询到当前系统满足指定条件的所有在线用户的列表。 VoLTE(VoLTE)：支持将VoLTE默认承载会话强制下线 说明： 当参数取值为“VoLTE”时，不会将正在进行VoLTE呼叫的Gx会话强制下线。 KABAK(KABAK)：支持按对端保活超时时保存的会话信息强制用户下线PSUB(PSUB)：支持将指定用户的会话强制下线SpecificAMF(SpecificAMF)：支持将指定AMF的N15会话强制下线 默认值：ALL。  说明： 如果SND SSCR执行时不携带该参数，则按照默认值“ALL”处理。                                                                                                                                                                                                                                                                               |
| PCEFID     | 对端PCEF标识   | 用于标识对端PCEF实体。该参数必须先由ADD PPCEF命令定义，然后才能在此处索引。 当“SSTYPE”选择“SpecificPCEF”时，需要设置该参数。 取值范围： 0～1023 默认值： 无。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| HOSTID     | 目的主机标识     | 用于标识目的主机。该参数必须先由ADD PDHOSTCFG命令定义，然后才能在此处索引。 当“SSTYPE”选择“DRA_SpecificPCEF”或“DRA_SpecificAF”时，需要设置该参数。 取值范围：0～511 默认值：无。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| AFID       | 对端AF标识     | 用于标识对端AF实体。该参数必须先由ADD PAF命令定义，然后才能在此处索引。 当“SSTYPE”选择“SpecificAF”时，需要设置该参数。 取值范围：0～15 默认值：无。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| VOLTEDEA   | 去激活VoLTE会话 | 用于标识是否去激活正在进行VoLTE呼叫的用户会话。仅当“SSTYPE”选择“ALL”时，该参数可显并为可选参数。 取值范围： Yes：强制下线时去激活正在呼叫的VoLTE会话。No：强制下线时不去激活正在呼叫的VoLTE会话。 默认值：无。  说明： 执行SND SSCR命令时，如果参数“SSTYPE”取值为“ALL”，且该参数为空，则按照该参数的默认值“Yes”处理。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| APNTYPE    | APN类型      | 用于标识需要去激活的用户会话的接入APN类型。仅当“SSTYPE”选择“SUBLIST”时，该参数可显并为可选参数。 取值范围： ALL：按照用户列表强制用户下线时将用户绑定的所有会话全部去激活。Non-VoLTE-APN：按照用户列表强制用户下线时将用户非VoLTE-APN接入的会话全部去激活。 默认值：无。  说明： 执行SND SSCR命令时，如果参数“SSTYPE”取值为“SUBLIST”，且该参数为空，则按照该参数的默认值“ALL”处理。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| SUBID      | 用户标识       | 用于指定需要去激活用户的用户标识。仅当“SSTYPE”选择“PSUB”时，该参数需要设置。 取值范围：长度不超过255的字符串。 默认值：无。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| SUBTYPE    | 用户类型       | 用于指定需要去激活的用户类型。仅当“SSTYPE”选择“PSUB”时，该参数需要设置。 取值范围：SingleSub：单个用户。 SubGroup：用户组。 默认值：SingleSub。  说明： 当“用户类型”取值“SubGroup”时，该命令强制用户组的所有用户下线，此时“用户标识”必须填写为用户组中组用户的用户标识。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| INTERFACE  | 接口类型       | 用于指定需要去激活用户的接口会话。仅当“SSTYPE”选择“PSUB”时，该参数需要设置。 取值范围：Gx(Gx) Rx(Rx) N7(N7) N5(N5)N23(N23)ReleaseAllOnly(只释放所有资源) ReleaseAll(强制所有会话下线)N15-AM(N15-AM)N15-UE(N15-UE)N24-AM(N24-AM)  说明： 接口类型取值为Gx(Gx)时：表示去激活Gx会话，同时依赖于该Gx会话的子会话（比如Rx、Sy）也会被去激活。 接口类型取值为Rx(Rx)时：表示仅去激活Rx会话。 接口类型取值为N7(N7)时：表示去激活N7会话，同时依赖于该N7会话的子会话（比如Rx/N5）也会被去激活。接口类型取值为(N5)时：表示仅去激活N5会话。接口类型取值为N23(N23)时：表示仅去激活N23会话。接口类型取值为ReleaseAllOnly(只释放所有资源)时，有如下处理逻辑： 释放UPCF用户的所有资源，释放的资源包括：Gx、Rx、Sy、Sd、N28、N7、N5、N15、N23、N24； N28/Sy接口会发起Nchf_SpendingLimitControl_Unsubscribe请求/STR消息通知对端用户下线。 接口类型取值为ReleaseAll(强制所有会话下线)时：表示强制用户所有会话下线，包括Gx、Rx、Sy、Sd、N28、N7、N5、N15、N23、N24，并通知各对端。 当会话类型选择PSUB(PSUB)，用户类型选择SubGroup时，PES遍历组内所有用户，按INTERFACE参数所携带的接口类型，强制对应的会话下线。接口类型取值为N15-AM(N15-AM)时：表示去激活N15接口的AMPolicy会话，同时依赖于该N15 AM会话的子会话（比如N24 AM会话）也会被去激活。接口类型取值为N15-UE(N15-UE)时：表示仅去激活N15接口的UEPolicy会话。接口类型取值为N24-AM(N24-AM)时：表示仅去激活N24接口的AMPolicy会话。 默认值：ReleaseAll(强制所有会话下线) |
| VOICEIF    | 语音接口类型     | 用于标识强制默认承载会话下线的语音接口类型。 取值范围： Gx(Gx)N7(N7)All(All) 默认值：All(All)                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| AMFID      | AMF标识      | 用于标识AMF对端，该参数需要与N15接口消息guami信元中的amfId属性保持一致。 仅当“SSTYPE”选择“SpecificAMF”时，该参数需要设置。 取值范围：长度为6的字符串 默认值：无。  说明： 当“SSTYPE”取值为“SpecificAMF”，若不输入该参数取值，执行SND SSCR命令将释放所有AMF对端的N15会话。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| POLICYTYPE | 策略类型       | 用于指定需要去激活的N15会话类型。仅当“SSTYPE”选择“SpecificAMF”时，该参数需要设置。 取值范围：AMPolicy(AMPolicy) UEPolicy(UEPolicy) ALL(ALL) 默认值：ALL(ALL)  说明： 执行SND SSCR命令时，如果参数“SSTYPE”取值为“SpecificAMF”，且该参数为空，则按照该参数的默认值“ALL”处理。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |

## 使用实例

发送用户下线请求，“会话类型”为“ALL”。

```
SND SSCR: SSTYPE=ALL;
```

```
%%SND SSCR: SSTYPE=ALL;%%
RETCODE = 0  操作成功

没有查到相应结果
---    END
```

## 输出结果说明

| 参数名称   | 参数说明                                                       |
|:-------|:-----------------------------------------------------------|
| 容器名称   | 用于描述PES服务的容器名称。 取值范围：长度不超过128的字符串。                         |
| 实例号    | 用于描述PES服务的实例号。 取值范围：长度不超过256的字符串。                          |
| 结果     | 用于描述执行任务的结果。 取值范围： 成功操作失败已经有任务在执行中，请稍后再尝试正在备份没有备份          |
| 用户标识   | 用于描述去激活用户的用户标识。 取值范围：长度不超过255的字符串。                         |
| 用户类型   | 用于描述去激活用户的用户类型。 取值范围：单个用户 主从用户或用户组                         |
| 状态     | 用于描述去激活用户的会话状态。 取值范围： 用户会话已去激活正在去激活用户会话正在去激活用户组会话去活用户组会话失败 |