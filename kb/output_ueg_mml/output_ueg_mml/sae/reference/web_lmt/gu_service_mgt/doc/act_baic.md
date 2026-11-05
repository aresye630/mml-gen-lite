# 激活BAIC业务(ACT BAIC)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

此操作用来激活BAIC业务。激活BAIC业务前，该用户必须已经开户，并且签约BAIC业务，否则系统会提示找不到该用户或用户未签约该业务。

如果UDM支持签约管理优化（执行**SET MAPCONF**命令将“用户被锁后是否允许操作相关补充业务”设置为“TRUE”），即使用户停机，包括运营商锁（LCK）和用户锁（SABLCK），用户的业务签约变更仍可继续进行。

## 注意事项

- IMSI、ISDN、IMSIFILE、ISDNFILE是条件可选参数，有且只能有一个参数出现。
- RECORDCOUNT一定不能与IMSIFILE或ISDNFILE同时存在。
- 补充业务BAIC必须首先签约，然后激活才能使用。签约BAIC，请使用MOD BAIC命令。

## 参数说明

| 参数标识        | 参数名称      | 参数说明                                                                                                                                                                                                                                                                                                          |
|:------------|:----------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IMSI        | IMSI      | IMSI号码，E.212格式的编码，6～15位的十进制数字。                                                                                                                                                                                                                                                                                |
| ISDN        | MSISDN    | MSISDN号码，E.164格式的编码，1～15位的十进制数字。                                                                                                                                                                                                                                                                              |
| RECORDCOUNT | 用户个数      | 用户的数目，最大100000个。如果只有一个用户，该参数不必提供。 该参数提供，代表以指定的IMSI、MSISDN为起始号码，号码连续的RECORDCOUNT个用户。                                                                                                                                                                                                                           |
| IMSIFILE    | IMSI文件名   | IMSIFILE文件名称，由16个以内的数字或字母组成。IMSIFILE是由多个不连续的IMSI号码组成的批操作文件，每个IMSI号码占一行。                                                                                                                                                                                                                                       |
| ISDNFILE    | MSISDN文件名 | ISDNFILE文件名称，由16个以内的数字或字母组成。ISDNFILE是由多个不连续的MSISDN号码组成的批操作文件，每个MSISDN号码占一行。                                                                                                                                                                                                                                   |
| BSG         | 基本业务组     | 区分BAIC应用的基本业务类型。 ALL：All Applicable services(TS1X，TS2X，TS6X，BS2X，BS3X)，所有可应用的基本业务TS1X：Telephony Service，话音业务TS2X：Short Message Service，短消息业务TS6X：Facsimile Service Group，传真业务BS2X：Asynchronous Bearer Service，异步承载业务BS3X：Synchronous Bearer Service，同步承载业务TSDX: Custom supplementary service，自定义补充业务 缺省值为ALL。 |

## 使用实例

激活IMSI号码为460000009123456的用户的BAIC业务。命令如下：

ACT BAIC: IMSI="460000009123456", BSG=ALL;