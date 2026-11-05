# 激活BORO业务(ACT BORO)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

此操作用来激活BORO业务。激活BORO业务前，该用户必须已经开户，并且签约BORO业务。

如果用户漫游出国且有激活的前转，不能激活BORO；如果BORO激活且用户漫游出国，则前转不能登记或激活；如果有激活的BORO和前转，用户漫游出国，前转被激活禁止。

执行此命令后，如果用户国际漫游，系统将向VLR下发插入用户数据消息。

## 注意事项

- IMSI、ISDN、IMSIFILE、ISDNFILE是条件可选参数，有且只能有一个参数出现。
- RECORDCOUNT一定不能与IMSIFILE或ISDNFILE同时存在。
- 补充业务BORO必须首先签约，然后激活才能使用。签约BORO，请使用MOD BORO命令。

## 参数说明

| 参数标识        | 参数名称      | 参数说明                                                                                                                                                                                                                                                                                                                |
|:------------|:----------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IMSI        | IMSI      | IMSI号码，E.212格式的编码。 取值范围：6～15位的十进制数字。                                                                                                                                                                                                                                                                                |
| ISDN        | MSISDN    | MSISDN号码，E.164格式的编码。 取值范围：1～15位的十进制数字。                                                                                                                                                                                                                                                                              |
| RECORDCOUNT | 用户个数      | 用户的数目。如果只有一个用户，该参数不必提供。 该参数提供，代表以指定的IMSI、MSISDN为起始号码，号码连续的RECORDCOUNT个用户。 取值范围：1～100000                                                                                                                                                                                                                             |
| IMSIFILE    | IMSI文件名   | IMSIFILE文件名称。IMSIFILE是由多个不连续的IMSI号码组成的批操作文件，每个IMSI号码占一行。 取值范围：1～16个字母或数字组成的字符串。                                                                                                                                                                                                                                     |
| ISDNFILE    | MSISDN文件名 | ISDNFILE文件名称。ISDNFILE是由多个不连续的MSISDN号码组成的批操作文件，每个MSISDN号码占一行。 取值范围：1～16个字母或数字组成的字符串。                                                                                                                                                                                                                                 |
| BSG         | 基本业务组     | 区分BORO应用的基本业务类型。 取值范围： ALL：All Applicable services(TS1X，TS2X，TS6X，BS2X，BS3X)，所有可应用的基本业务TS1X：Telephony Service，话音业务TS2X：Short Message Service，短消息业务TS6X：Facsimile Service Group，传真业务BS2X：Asynchronous Bearer Service，异步承载业务BS3X：Synchronous Bearer Service，同步承载业务TSDX: Custom supplementary service，自定义补充业务 缺省值为ALL。 |

## 使用实例

激活IMSI号码为460000009123456的用户的BORO业务。命令如下：

ACT BORO: IMSI="460000009123456", BSG=ALL;