# 去激活CFD业务(DEA CFD)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

此操作用来去激活CFD补充业务。CFD业务去激活后，用户签约登记信息在HLR中保留，但用户不能使用该业务。

执行此命令后，若用户在网，并处于可用的状态，系统将根据替代业务不同决定是否下发删除用户数据和插入用户数据信息。

## 注意事项

- “IMSI”、“ISDN”、“IMSIFILE”、“ISDNFILE”是条件可选参数，有且只能有一个参数出现。
- “RECORDCOUNT”一定不能与“IMSIFILE”或“ISDNFILE”同时存在。

## 参数说明

| 参数标识        | 参数名称      | 参数说明                                                                                                                                                                                                                                                                                     |
|:------------|:----------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IMSI        | IMSI      | IMSI号码，E.212格式的编码，为6～15位的十进制数字。                                                                                                                                                                                                                                                          |
| ISDN        | MSISDN    | MSISDN号码，E.164格式的编码，为1～15位的十进制数字。                                                                                                                                                                                                                                                        |
| RECORDCOUNT | 用户个数      | 用户的数目，最大100000个。如果只有一个用户，该参数不必提供。 该参数提供，代表以指定的IMSI、MSISDN为起始号码，号码连续的RECORDCOUNT个用户。                                                                                                                                                                                                      |
| IMSIFILE    | IMSI文件名   | IMSIFILE文件名称，1～16个字母或数字组成。IMSIFILE是由多个不连续的IMSI号码组成的批操作文件，每个IMSI号码占一行。                                                                                                                                                                                                                    |
| ISDNFILE    | MSISDN文件名 | ISDNFILE文件名称，1～16个字母或数字组成。ISDNFILE是由多个不连续的MSISDN号码组成的批操作文件，每个MSISDN号码占一行。                                                                                                                                                                                                                |
| BSG         | 基本业务组     | 区分CFD应用的基本业务类型。 取值范围： ALL：All Applicable services(TS1X，TS6X，BS2X，BS3X)，所有可应用的基本业务 TS1X：Telephony Service，话音业务 TS6X：Facsimile Service Group，传真业务 BS2X：Asynchronous Bearer Service，异步承载业务 BS3X：Synchronous Bearer Service，同步承载业务 TSDX: Custom supplementary service，自定义补充业务 缺省值为ALL。 可选参数。 |

## 使用实例

运营商为IMSI号码是460000009123456的用户去激活CFD业务。

DEA CFD: IMSI="460000009123456";