# 修改用户签约的SMS-Route模板ID(MOD SMSROUTE)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

此操作用于修改用户签约的SMS-ROUTE模板ID。

## 注意事项

- IMSI、ISDN、IMSIFILE和ISDNFILE是条件可选参数，任何一个参数出现即可。
- RECORDCOUNT一定不能与IMSIFILE或ISDNFILE同时存在。

## 参数说明

| 参数标识        | 参数名称            | 参数说明                                                                                |
|:------------|:----------------|:------------------------------------------------------------------------------------|
| IMSI        | IMSI            | 主号用户的IMSI号码，对外提供的IMSI号码，E.212格式的编码，为6～15位的十进制数字。                                    |
| ISDN        | MSISDN          | 主号用户的MSISDN号码，E.164格式的编码，为1～15位的十进制数字。                                              |
| RECORDCOUNT | 用户个数            | 用户的数目，最大100000个。如果只有一个用户，该参数不必提供。 该参数提供，代表以指定的IMSI、MSISDN为起始号码，号码连续的RECORDCOUNT个用户。 |
| IMSIFILE    | IMSI文件名         | IMSI文件名称，1～16个字母或数字组成。IMSIFILE包含多个不连续的IMSI号码。                                       |
| ISDNFILE    | MSISDN文件名       | ISDN文件名称，1～16个字母或数字组成。ISDNFILE包含多个不连续的MSISDN号码。                                     |
| PROV        | 是否提供SMS-ROUTE业务 | 是否提供SMS-ROUTE业务。 TRUE：提供FALSE：撤销                                                    |
| TPLID       | SMS-ROUTE模板号    | 仅当本命令中的“是否提供SMS-ROUTE业务”参数为“TRUE”时该参数有效。SMS-ROUTE的模版号。取值范围：0～65534。                 |

## 使用实例

为IMSI起始号码为460000009123456的4个用户提供SMS-ROUTE业务，采用模板ID为4的SMS-ROUTE模板。命令如下：

MOD SMSROUTE: IMSI="460000009123456", RECORDCOUNT=4, PROV=TRUE, TPLID=4;