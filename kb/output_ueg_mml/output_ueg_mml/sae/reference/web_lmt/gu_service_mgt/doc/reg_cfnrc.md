# 登记CFNRc业务(REG CFNRC)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

登记操作主要用来登记CFNRc前转的前转号码。CFNRc前转业务登记即激活，不需单独操作。

如果UDM支持签约管理优化（执行**SET MAPCONF**命令将“用户被锁后是否允许操作相关补充业务”设置为“TRUE”），即使用户停机，包括运营商锁（LCK）和用户锁（SABLCK），闭锁入呼叫和出呼叫，用户的业务签约变更仍可继续进行。

执行此命令后，系统将向VLR下发插入用户数据消息。

## 注意事项

- “IMSI”、“MSISDN”、“IMSI文件名”、“MSISDN文件名”四个参数是可选参数，必须有且只能有一个参数出现。
- “用户个数”不能与“IMSI文件名”或“MSISDN文件名”同时配置。

## 参数说明

| 参数标识        | 参数名称      | 参数说明                                                                                                                                                                                                                                                                                |
|:------------|:----------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IMSI        | IMSI      | IMSI号码，E.212格式的编码，为6～15位的十进制数字。                                                                                                                                                                                                                                                     |
| ISDN        | MSISDN    | MSISDN号码，E.164格式的编码，为1～15位的十进制数字。                                                                                                                                                                                                                                                   |
| RECORDCOUNT | 用户个数      | 用户的数目，最大100000个。如果只有一个用户，该参数不必提供。 该参数提供，代表以指定的IMSI、MSISDN为起始号码，号码连续的RECORDCOUNT个用户。                                                                                                                                                                                                 |
| IMSIFILE    | IMSI文件名   | IMSIFILE文件名称，1～16个字母或数字组成。IMSIFILE包含多个不连续的IMSI号码。                                                                                                                                                                                                                                   |
| ISDNFILE    | MSISDN文件名 | ISDNFILE文件名称，1～16个字母或数字组成。ISDNFILE包含多个不连续的MSISDN号码。                                                                                                                                                                                                                                 |
| FTN         | 前转号码      | 用于标识用户需要登记的前转号码。具体格式可参见前转号码格式。 取值范围：1～28位十进制数字组成的字符串。 默认值：无。 说明：如果在SET MAPCONF命令中设置“是否支持Long FTN”参数为“TRUE”，则前转号码长度最多为28位。如果在SET MAPCONF命令中设置“是否支持Long FTN”参数为“FALSE”，则根据在SET MAPCONF命令中设置“是否限制前转号码长度”参数决定前转号码长度最多为15位还是16位。                                                         |
| PROPERTY    | 前转号码属性    | 前转号码的属性。 取值范围： INTERNATIONAL：国际号码 NATIONAL：国内号码                                                                                                                                                                                                                                     |
| BSG         | 基本业务组     | CFNRc业务适用的基本业务群。 取值范围： ALL：All Applicable Services(TS1X，TS6X，BS2X，BS3X，TSDX)，所有可应用的基本业务 TS1X：Telephony Service，话音业务TS6X：Facsimile Service Group，传真业务BS2X：Asynchronous Bearer Service，异步承载业务BS3X：Synchronous Bearer Service，同步承载业务TSDX：Custom Supplementary Service，自定义补充业务 缺省值为ALL． |

## 使用实例

为IMSI号码为460000009123456的用户登记CFNRc业务，前转号码为本地固定号码66668888。命令如下：

REG CFNRC: IMSI="460000009123456", FTN="66668888", PROPERTY=NATIONAL, BSG=ALL;