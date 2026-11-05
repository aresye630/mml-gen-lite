# 修改IST业务(MOD IST)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

IST即立即终止业务，运营商可以通过IST操作立即终止用户在VPLMN/IPLMN的所有正在进行的活动。MOD IST命令就是用来修改用户的IST业务数据的。

执行此命令后，如果是给用户签约该业务，则会下发插入用户数据消息；如果是给用户去签约该业务，则会下发删除用户数据消息。

## 注意事项

- IMSI、ISDN、IMSIFILE、ISDNFILE是条件可选参数，有且只能有一个参数出现。
- RECORDCOUNT一定不能与IMSIFILE或ISDNFILE同时存在。
- 第一次执行此命令，PROV=TRUE时，参数ISTTIMER和参数ISTRSP至少选择一个。若不选择参数ISTTIMER，则ISTTIMER将取默认值255；若不选择参数ISTRSP，则ISTRSP将取默认值TERMINATECALLACTIVITYREFERRED。

## 参数说明

| 参数标识        | 参数名称      | 参数说明                                                                                                                                                                                |
|:------------|:----------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IMSI        | IMSI      | IMSI号码，E.212格式的编码，6～15位的十进制数字。                                                                                                                                                      |
| ISDN        | MSISDN    | MSISDN号码，E.164格式的编码，1～15位的十进制数字。                                                                                                                                                    |
| RECORDCOUNT | 用户个数      | 用户的数目，最大100000个。如果只有一个用户，该参数不必提供。 该参数提供，代表以指定的IMSI、MSISDN为起始号码，号码连续的RECORDCOUNT个用户。                                                                                                 |
| IMSIFILE    | IMSI文件名   | IMSIFILE文件名称，1~16个由字母、数字、下划线和点号组成的字符串。IMSIFILE是由多个不连续的IMSI号码组成的批操作文件，每个IMSI号码占一行。                                                                                                   |
| ISDNFILE    | MSISDN文件名 | ISDNFILE文件名称，1~16个由字母、数字、下划线和点号组成的字符串。ISDNFILE是由多个不连续的MSISDN号码组成的批操作文件，每个MSISDN号码占一行。                                                                                               |
| PROV        | 是否提供IST业务 | 是否提供IST业务数据。 TRUE：提供IST业务数据，如果用户已签约IST业务，则表示修改用户的IST业务数据。FALSE：去签约用户的IST业务。                                                                                                         |
| ISTTIMER    | IST定时周期   | 仅当本命令中的“是否提供IST业务”参数为“TRUE”时该参数有效。IST定时周期，下发给VMSC/GMSC，被VMSC/GMSC用于控制IST提醒消息的上报周期。值域15～255。                                                                                         |
| ISTRSP      | IST响应处理   | 仅当本命令中的“是否提供IST业务”参数为“TRUE”时该参数有效。当HLR收到IST提醒时，HLR的处理方式。 EMPTY：不处理NEW_ALERT_TIMER：使用新的定时周期TERMINATECALLACTIVITYREFERRED：立即终止当前活动TERMINATEALLCALLACTIVITIES：立即终止所有活动WITHDRAW：取消IST业务 |

## 使用实例

为IMSI号码为460000009123456的用户修改IST业务数据, IST定时周期为15，IST响应处理为NEW\_ALERT\_TIMER，命令如下：

MOD IST: IMSI="460000009123456", PROV=TRUE, ISTTIMER=15, ISTRSP=NEW\_ALERT\_TIMER;