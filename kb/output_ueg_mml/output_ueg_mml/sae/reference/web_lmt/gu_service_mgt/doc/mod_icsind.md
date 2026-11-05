# 修改用户ICSIND(MOD ICSIND)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

本命令用于设置用户ICS业务，包括签约或去签约用户的ICS能力。

执行此命令后，如果是给用户签约该业务，则会下发插入用户数据消息；如果是给用户去签约该业务，则会下发删除用户数据消息。

## 注意事项

- 当使用连续批操作时需定义RECORDCOUNT与IMSI/ISDN参数，当使用非连续批操作时需定义IMSIFILE/ISDNFILE参数。
- IMSI、ISDN、IMSIFILE、ISDNFILE是条件可选参数，有且只能有一个参数出现。
- RECORDCOUNT一定不能与IMSIFILE或ISDNFILE同时存在。

## 参数说明

| 参数标识        | 参数名称      | 参数说明                                                                                |
|:------------|:----------|:------------------------------------------------------------------------------------|
| IMSI        | IMSI      | IMSI号码，E.212格式的编码，6～15位的十进制数字。                                                      |
| ISDN        | MSISDN    | ISDN号码，E.164格式的编码，为1～15位的十进制数字。                                                     |
| RECORDCOUNT | 用户个数      | 用户的数目，最大100000个。如果只有一个用户，该参数不必提供。 该参数提供，代表以指定的IMSI、MSISDN为起始号码，号码连续的RECORDCOUNT个用户。 |
| IMSIFILE    | IMSI文件名   | IMSI文件名称，IMSIFILE包含多个不连续的IMSI号码，每个IMSI号码占一行，16个以内的字母或数字组成的字符串。                      |
| ISDNFILE    | MSISDN文件名 | MSISDN文件名称，ISDNFILE包含多个不连续的MSISDN号码，每个MSISDN号码占一行。16个以内的字母或数字组成的字符串。                |
| ICSIND      | ICSIND    | 用户是否具备ICS能力。 该参数必选。 TRUE：具备FALSE：不具备                                                |

## 使用实例

为IMSI号码是460000009123456的用户提供ICS支持能力。

MOD ICSIND: IMSI="460000009123456", ICSIND=TRUE;