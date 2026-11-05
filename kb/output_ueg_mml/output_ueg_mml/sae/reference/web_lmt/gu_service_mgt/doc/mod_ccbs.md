# 修改CCBS业务(MOD CCBS)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

此操作用来为用户签约CCBS业务。

签约CCBS业务的用户，必须已经成功开户，并且未签约CCBS业务。撤销CCBS业务的用户，必须已经成功开户，并且已经签约CCBS业务。

CCBS业务提供后自动激活，不需要单独的激活操作。

## 注意事项

- IMSI、ISDN、IMSIFILE、ISDNFILE是条件可选参数，有且只能有一个参数出现。
- RECORDCOUNT不能与IMSIFILE或ISDNFILE同时存在。
- CCBS与CCBSTARGET参数必选一个。

## 参数说明

| 参数标识        | 参数名称              | 参数说明                                                                                |
|:------------|:------------------|:------------------------------------------------------------------------------------|
| IMSI        | IMSI              | IMSI号码，E.212格式的编码。 取值范围：6～15位的十进制数字。                                                |
| ISDN        | MSISDN            | MSISDN号码，E.164格式的编码。 取值范围：1～15位的十进制数字。                                              |
| RECORDCOUNT | 用户个数              | 用户的数目，最大100000个。如果只有一个用户，该参数不必提供。 该参数提供，代表以指定的IMSI、MSISDN为起始号码，号码连续的RECORDCOUNT个用户。 |
| IMSIFILE    | IMSI文件名           | IMSIFILE文件名称，IMSIFILE包含多个不连续的IMSI号码，每个IMSI号码占一行，16个以内的字母或数字组成的字符串。                  |
| ISDNFILE    | MSISDN文件名         | ISDNFILE文件名称，ISDNFILE包含多个不连续的MSISDN号码，每个MSISDN号码占一行。16个以内的字母或数字组成的字符串。              |
| CCBS        | 是否提供CCBS业务        | 是否提供CCBS业务。 TRUE：提供 FALSE：撤销                                                        |
| CCBSTARGET  | 是否提供CCBS TARGET业务 | 是否提供CCBS TARGET业务。 TRUE：提供 FALSE：撤销                                                 |

## 使用实例

1. 为IMSI为4600000091234564的用户提供CCBS业务和CCBS TARGET业务。

   MOD
   CCBS:IMSI="460000009123456", CCBS=TRUE, CCBSTARGET=TRUE;
2. 为IMSI为460000009123456的用户撤销CCBS业务和CCBS TARGET业务。

   MOD CCBS:IMSI="460000009123456",
   CCBS=FALSE, CCBSTARGET=FALSE;