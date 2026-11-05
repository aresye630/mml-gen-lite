# 发送立即业务终止命令(SND ISTCMD)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**须知** 

本命令属于高危命令，执行该命令前，需要与华为技术支持确认后才可以实施。

此操作是在用户数据管理台上人为的向VMSC/GMSC下发IST COMMAND消息，以期立即终止用户活动。

## 注意事项

- IMSI、ISDN、IMSIFILE和ISDNFILE是可选参数，只有其中一个需要设置。
- RECORDCOUNT一定不能与IMSIFILE或ISDNFILE同时存在。
- 当指定MSC号码时，表示是向GMSC下发IST COMMAND消息，否则向用户当前所在的VMSC下发IST COMMAND消息。

## 参数说明

| 参数标识        | 参数名称      | 参数说明                                                                                |
|:------------|:----------|:------------------------------------------------------------------------------------|
| IMSI        | IMSI      | IMSI号码，6～15位的十进制数字。                                                                 |
| ISDN        | MSISDN    | MSISDN号码，1～15位的十进制数字。                                                               |
| RECORDCOUNT | 用户个数      | 用户的数目，最大100000个。如果只有一个用户，该参数不必提供。 该参数提供，代表以指定的IMSI、MSISDN为起始号码，号码连续的RECORDCOUNT个用户。 |
| IMSIFILE    | IMSI文件名   | IMSI文件名称，1~16个由字母、数字、下划线和点号组成的字符串。IMSIFILE是批操作文件名，包含非连续的IMSI号码，每个IMSI占一行。           |
| ISDNFILE    | MSISDN文件名 | ISDN文件名称，1~16个由字母、数字、下划线和点号组成的字符串。ISDNFILE是批操作文件名，包含非连续的MSISDN号码，每个MSISDN占一行。       |
| MSCNUM      | MSC号码     | MSC号码，E.164格式的编码，1～15位的十进制数字。                                                       |

## 使用实例

向IMSI号码为460000009123456的用户发送IST COMMAND消息，以期终止用户在GMSC的活动，GMSC号码为8613809002。命令如下：

SND ISTCMD: IMSI="460000009123456", MSCNUM="8613809002";