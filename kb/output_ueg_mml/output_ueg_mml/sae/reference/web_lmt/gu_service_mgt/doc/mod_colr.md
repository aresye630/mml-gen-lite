# 修改COLR业务(MOD COLR)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

此操作用来提供、撤销COLR业务或修改COLR业务的属性。

签约COLR业务的用户，必须已经成功开户，并且未签约COLR业务。撤销COLR业务的用户，必须已经成功开户，并且已经签约COLR业务。

COLR业务提供后自动激活，不需要单独的激活操作。

执行此命令后，如果是给用户签约该业务，则会下发插入用户数据消息；如果是给用户去签约该业务，则会下发删除用户数据消息。

## 注意事项

- IMSI、ISDN、IMSIFILE、ISDNFILE是条件可选参数，有且只能有一个参数出现。
- RECORDCOUNT一定不能与IMSIFILE或ISDNFILE同时存在。
- 如果提供COLR业务，PROV＝TRUE；如果撤销COLR业务，PROV= FALSE。

## 参数说明

| 参数标识        | 参数名称          | 参数说明                                                                                                                                                                                                                               |
|:------------|:--------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IMSI        | IMSI          | IMSI号码，E.212格式的编码，为6～15位的十进制数字。 可选参数。                                                                                                                                                                                              |
| ISDN        | MSISDN        | MSISDN号码，E.164格式的编码，为1～15位的十进制数字。 可选参数。                                                                                                                                                                                            |
| RECORDCOUNT | 用户个数          | 用户的数目，最大100000个。如果只有一个用户，该参数不必提供。 该参数提供，代表以指定的IMSI、MSISDN为起始号码，号码连续的RECORDCOUNT个用户。                                                                                                                                                |
| IMSIFILE    | IMSI文件名       | IMSIFILE文件名称，1～16个字母或数字组成。IMSIFILE包含多个不连续的IMSI号码。 可选参数。                                                                                                                                                                            |
| ISDNFILE    | MSISDN文件名     | ISDNFILE文件名称，1～16个字母或数字组成。ISDNFILE包含多个不连续的MSISDN号码。 可选参数。                                                                                                                                                                          |
| PROV        | 是否提供COLR业务    | 提供还是撤销COLR业务。 TRUE：提供FALSE：撤销 必选参数。                                                                                                                                                                                                |
| BSGTYPE     | COLR基本业务组操作类型 | 仅当本命令中的“是否提供COLR业务”参数为“TRUE”时该参数有效。COLR基本业务组操作类型，对该基本业务组进行删除、添加和重置操作。同时配合参数BSGLIST中设置的具体业务进行配置。 取值范围： REMOVE: 删除ADD: 添加RESET: 重置                                                                                                   |
| BSGLIST     | COLR基本业务组     | 仅当本命令中的“是否提供COLR业务”参数为“TRUE”时该参数有效。COLR基本业务组。 取值范围： TS1X: Telephony Service，话音业务TS2X: Short Message Service，短消息业务TS6X: Facsimile Service Group，传真业务BS2X: Asynchronous Bearer Service，异步承载业务BS3X: Synchronous Bearer Service，同步承载业务 |

## 使用实例

运营商为IMSI号码是460000009012345的用户提供短消息COLR业务，例如：

MOD COLR: IMSI="460000009012345", PROV=TRUE, BSGTYPE=ADD, BSGLIST=TS2X;