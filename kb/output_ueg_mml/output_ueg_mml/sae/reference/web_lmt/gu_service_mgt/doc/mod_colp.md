# 修改COLP业务(MOD COLP)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

此操作用来提供、撤销COLP业务或修改COLP业务的属性。

签约COLP业务的用户，必须已经成功开户，并且未签约COLP业务。撤销COLP业务的用户，必须已经成功开户，并且已经签约COLP业务。

COLP业务提供后自动激活，不需要单独的激活操作。

执行此命令后，如果是给用户签约该业务，则会下发插入用户数据消息；如果是给用户去签约该业务，则会下发删除用户数据消息。

## 注意事项

- IMSI，ISDN，IMSIFILE和ISDNFILE是条件可选参数，任何一个参数出现即可。
- RECORDCOUNT一定不能与IMSIFILE或ISDNFILE同时存在。

- 如果提供COLP业务，PROV＝TRUE；如果撤销COLP业务，PROV= FALSE。
- 如果PROV=TRUE，OVERRIDE参数必须设置；如果PROV=FALSE，OVERRIDE参数不必设置。

## 参数说明

| 参数标识        | 参数名称          | 参数说明                                                                                                                                                                                                                               |
|:------------|:--------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IMSI        | IMSI          | IMSI号码，E.212格式的编码，为6～15位的十进制数字。 可选参数。                                                                                                                                                                                              |
| ISDN        | MSISDN        | MSISDN号码，E.164格式的编码，为1～15位的十进制数字。 可选参数。                                                                                                                                                                                            |
| RECORDCOUNT | 用户个数          | 用户的数目，最大100000个。如果只有一个用户，该参数不必提供。 该参数提供，代表以指定的IMSI、MSISDN为起始号码，号码连续的RECORDCOUNT个用户。                                                                                                                                                |
| IMSIFILE    | IMSI文件名       | IMSIFILE文件名称，1～16个字母或数字组成。IMSIFILE包含多个不连续的IMSI号码。 可选参数。                                                                                                                                                                            |
| ISDNFILE    | MSISDN文件名     | ISDNFILE文件名称，1～16个字母或数字组成。ISDNFILE包含多个不连续的MSISDN号码。 可选参数。                                                                                                                                                                          |
| PROV        | 是否提供COLP业务    | 提供还是撤销COLP业务。 TRUE：提供FALSE：撤销 必选参数。                                                                                                                                                                                                |
| OVERRIDE    | COLP超越属性      | 仅当本命令中的“是否提供COLP业务”参数为“TRUE”时该参数有效。超越被叫号码识别属性是否有效。 TRUE：有效FALSE：无效 可选参数。                                                                                                                                                           |
| BSGTYPE     | COLP基本业务组操作类型 | 仅当本命令中的“是否提供COLP业务”参数为“TRUE”时该参数有效。COLP基本业务组操作类型，对该基本业务组进行删除、添加和重置操作。同时配合参数BSGLIST中设置的具体业务进行配置。 取值范围： REMOVE: 删除ADD: 添加RESET: 重置                                                                                                   |
| BSGLIST     | COLP基本业务组     | 仅当本命令中的“是否提供COLP业务”参数为“TRUE”时该参数有效。COLP基本业务组。 取值范围： TS1X: Telephony Service，话音业务TS2X: Short Message Service，短消息业务TS6X: Facsimile Service Group，传真业务BS2X: Asynchronous Bearer Service，异步承载业务BS3X: Synchronous Bearer Service，同步承载业务 |

## 使用实例

运营商为IMSI号码是46000000012345的用户提供短消息COLP业务，超越属性设为FALSE。例如：

MOD COLP: IMSI="46000000012345", PROV=TRUE, OVERRIDE=FALSE, BSGTYPE=ADD, BSGLIST=TS2X;