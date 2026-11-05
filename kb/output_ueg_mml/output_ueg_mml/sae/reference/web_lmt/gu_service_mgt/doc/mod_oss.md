# 修改其他补充业务(MOD OSS)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

此操作用来为用户签约或去签约其他补充业务，涉及的补充业务包括：CWAIT、HOLD、MPTY、AOCC、AOCI、ECT、CCBS、CCBSTARGET。

执行此命令后，如果是给用户签约该业务，则会下发插入用户数据消息；如果是给用户去签约该业务，则会下发删除用户数据消息。

## 注意事项

- 条件参数IMSI、ISDN必须且只能有一个存在。
- 签约MPTY、ECT业务需要保证已经签约呼叫保持业务HOLD、ECT才能正常使用。
- 参数CWAIT、HOLD、MPTY、AOCC、AOCI、ECT、CCBS、CCBSTARGET至少选一个，且AOCC和AOCI是互斥的两个业务，仅能选择一个。

## 参数说明

| 参数标识           | 参数名称              | 参数说明                                                                                                                                                                                                                                                                                                                                                                                               |
|:---------------|:------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IMSI           | IMSI              | IMSI号码，E.212格式的编码。 取值范围：6～15位的十进制数字。                                                                                                                                                                                                                                                                                                                                                               |
| ISDN           | MSISDN            | MSISDN号码，E.164格式的编码。 取值范围：1～15位的十进制数字。                                                                                                                                                                                                                                                                                                                                                             |
| RECORDCOUNT    | 用户个数              | 用户的数目，最大100000个。如果只有一个用户，该参数不必提供。 该参数提供，代表以指定的IMSI、MSISDN为起始号码，号码连续的RECORDCOUNT个用户。                                                                                                                                                                                                                                                                                                                |
| IMSIFILE       | IMSI文件名           | IMSIFILE文件名称，IMSIFILE包含多个不连续的IMSI号码，每个IMSI号码占一行，16个以内的字母或数字组成的字符串。                                                                                                                                                                                                                                                                                                                                 |
| ISDNFILE       | MSISDN文件名         | ISDNFILE文件名称，ISDNFILE包含多个不连续的MSISDN号码，每个MSISDN号码占一行。16个以内的字母或数字组成的字符串。                                                                                                                                                                                                                                                                                                                             |
| CWAIT          | 是否提供CW业务          | 签约或去签约呼叫等待业务。 取值范围： TRUE：签约 FALSE：去签约 可选参数。                                                                                                                                                                                                                                                                                                                                                        |
| ACTDEACWAIT    | 激活或者去激活CW业务       | 激活或者去激活CW业务。 取值范围： ACT：激活CW业务 DEA：去激活CW业务  可选参数。                                                                                                                                                                                                                                                                                                                                                   |
| ACTDEACWAITBSG | 激活或去激活基本业务组       | 激活或去激活何种基本业务类型上的CW业务。 取值范围： ALL：在所有可应用的基本业务(TS1X，TS6X，BS2X，BS3X，TSDX)上激活呼叫等待业务 TS1X：Telephony Service，在话音业务上激活呼叫等待业务 TS6X：Facsimile Service Group，在传真业务上激活呼叫等待业务 BS2X：Asynchronous Bearer Service，在异步承载业务上激活呼叫等待业务 BS3X：Synchronous Bearer Service，在同步承载业务上激活呼叫等待业务 TSDX: Custom supplementary service，在自定义补充业务上激活呼叫等待业务 缺省值为ALL。 当参数“激活或者去激活CW业务”取值为“ACT”或“DEA”时，该参数为必选，表示激活或去激活某个基本业务组上的CWAIT业务。 |
| HOLD           | 是否提供HOLD业务        | 签约或去签约呼叫保持业务。 取值范围： TRUE：签约 FALSE：去签约 可选参数。                                                                                                                                                                                                                                                                                                                                                        |
| MPTY           | 是否提供MPTY业务        | 签约或去签约多方通话业务。 取值范围： TRUE:签约FALSE：去签约 签约MPTY业务需要保证已经签约呼叫保持业务HOLD，MPTY业务才能正常使用。 可选参数。                                                                                                                                                                                                                                                                                                                |
| AOCC           | 是否提供AOCC业务        | 签约或去签约计费通知（计费）业务。 取值范围： TRUE：签约 FALSE：去签约 可选参数，AOCC和AOCI仅能选择一个。                                                                                                                                                                                                                                                                                                                                    |
| AOCI           | 是否提供AOCI业务        | 签约或去签约计费通知（信息）业务。 取值范围： TRUE：签约FALSE：去签约 可选参数，AOCC和AOCI仅能选择一个。                                                                                                                                                                                                                                                                                                                                     |
| ECT            | 是否提供ECT业务         | 签约或去签约显式呼叫转移业务。 取值范围： TRUE：签约 FALSE：去签约 签约ECT业务需要保证已经签约呼叫保持业务HOLD，ECT业务才能正常使用。 可选参数。                                                                                                                                                                                                                                                                                                               |
| CCBS           | 是否提供CCBS业务        | 是否提供CCBS业务。 取值范围： TRUE：提供FALSE：不提供                                                                                                                                                                                                                                                                                                                                                                 |
| CCBSTARGET     | 是否提供CCBS TARGET业务 | 是否提供CCBS TARGET业务。 取值范围： TRUE：提供FALSE：不提供                                                                                                                                                                                                                                                                                                                                                          |

## 使用实例

1. 为IMSI号码是460000009123456的用户提供呼叫等待、呼叫保持业务。

   MOD OSS: IMSI="460000009123456", CWAIT=TRUE, HOLD=TRUE;
2. 为IMSI号码是460000009123456的用户提供呼叫等待、呼叫保持以及在话音业务上激活呼叫等待业务。

   MOD OSS: IMSI="460000009123456", CWAIT=TRUE, ACTDEACWAIT=ACT, ACTDEACWAITBSG=TS1X, HOLD=TRUE;