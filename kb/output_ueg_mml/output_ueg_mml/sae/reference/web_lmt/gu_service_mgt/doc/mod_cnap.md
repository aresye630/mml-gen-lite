# 修改CNAP业务(MOD CNAP)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

此操作用来提供、撤销CNAP业务或修改CNAP业务的属性。

签约CNAP业务的用户，必须已经成功开户，并且未签约CNAP业务。撤销CNAP业务的用户，必须已经成功开户，并且已经签约CNAP业务。

CNAP业务提供后自动激活，不需要单独的激活操作。

## 注意事项

- IMSI，ISDN，IMSIFILE和ISDNFILE是条件可选参数，任何一个参数出现即可。
- RECORDCOUNT一定不能与IMSIFILE或ISDNFILE同时存在。

- 如果提供CNAP业务，PROV＝TRUE；如果撤销CNAP业务，PROV=FALSE。
- 如果PROV=TRUE，OVERRIDE参数必须设置；如果PROV=FALSE，OVERRIDE参数不必设置。

## 参数说明

| 参数标识        | 参数名称       | 参数说明                                                                                |
|:------------|:-----------|:------------------------------------------------------------------------------------|
| IMSI        | IMSI       | IMSI号码，E.212格式的编码，为6～15位的十进制数字。 说明：可选参数。                                            |
| ISDN        | MSISDN     | MSISDN号码，E.164格式的编码，为1～15位的十进制数字。 说明：可选参数。                                          |
| RECORDCOUNT | 用户个数       | 用户的数目，最大100000个。如果只有一个用户，该参数不必提供。 该参数提供，代表以指定的IMSI、MSISDN为起始号码，号码连续的RECORDCOUNT个用户。 |
| IMSIFILE    | IMSI文件名    | IMSIFILE文件名称，1～16个字母或数字组成。IMSIFILE包含多个不连续的IMSI号码。 说明：可选参数。                          |
| ISDNFILE    | MSISDN文件名  | ISDNFILE文件名称，1～16个字母或数字组成。ISDNFILE包含多个不连续的MSISDN号码。 说明：可选参数。                        |
| PROV        | 是否提供CNAP业务 | 是否提供CNAP（主叫名片显示）业务。 取值范围： TRUE：提供。FALSE：不提供。 说明：必选参数。                               |
| OVERRIDE    | CNAP超越属性   | 超越主叫名片显示属性是否有效。 取值范围： TRUE：有效。FALSE：无效。 说明：当PROV=TRUE时，参数OVERRIDE为必选参数。             |

## 使用实例

运营商为IMSI号码是460000009012345的用户提供CNAP业务，超越主叫号码识别属性无效。例如：

MOD CNAP: IMSI="460000009012345", PROV=TRUE, OVERRIDE=FALSE;