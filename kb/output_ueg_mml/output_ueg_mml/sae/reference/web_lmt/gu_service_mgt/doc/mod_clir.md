# 修改CLIR业务(MOD CLIR)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

此操作用来提供、撤销CLIR业务或修改CLIR业务的属性。

签约CLIR业务的用户，必须已经成功开户，并且未签约CLIR业务。撤销CLIR业务的用户，必须已经成功开户，并且已经签约CLIR业务。

CLIR业务提供后自动激活，不需要单独的激活操作。

执行此命令后，如果是给用户签约该业务，则会下发插入用户数据消息；如果是给用户去签约该业务，则会下发删除用户数据消息。

## 注意事项

- IMSI，ISDN，IMSIFILE和ISDNFILE是条件可选参数，任何一个参数出现即可。
- RECORDCOUNT一定不能与IMSIFILE或ISDNFILE同时存在。

- 如果提供CLIR业务，PROV＝TRUE；如果撤销CLIR业务，PROV=FALSE。
- 如果PROV=TRUE，MODE参数必须设置；如果PROV=FALSE，MODE参数不必设置。

## 参数说明

| 参数标识        | 参数名称          | 参数说明                                                                                                                                                                                                                                                                         |
|:------------|:--------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IMSI        | IMSI          | IMSI号码，E.212格式的编码，为6～15位的十进制数字。 默认值：无。                                                                                                                                                                                                                                       |
| ISDN        | MSISDN        | MSISDN号码，E.164格式的编码，为1～15位的十进制数字。 默认值：无。                                                                                                                                                                                                                                     |
| RECORDCOUNT | 用户个数          | 用户的数目，最大100000个。如果只有一个用户，该参数不必提供。 该参数提供，代表以指定的IMSI、MSISDN为起始号码，号码连续的RECORDCOUNT个用户。 默认值：无。                                                                                                                                                                                   |
| IMSIFILE    | IMSI文件名       | IMSIFILE文件名称，1～16个字母或数字组成。IMSIFILE包含多个不连续的IMSI号码。 默认值：无。                                                                                                                                                                                                                     |
| ISDNFILE    | MSISDN文件名     | ISDNFILE文件名称，1～16个字母或数字组成。ISDNFILE包含多个不连续的MSISDN号码。 默认值：无。                                                                                                                                                                                                                   |
| PROV        | 是否提供CLIR业务    | 提供还是撤销CLIR业务。 TRUE：提供FALSE：撤销 默认值：无。                                                                                                                                                                                                                                         |
| MODE        | 限制模式          | 仅当本命令中的“是否提供CLIR业务”参数取值为“TRUE”时，该参数有效。用于标识移动用户作主叫时，网络限制向被叫用户提供主叫用户号码的方式。 取值范围： PERMANENT：永久限制。对所有出呼叫有效。移动用户作主叫时，不允许网络向被叫用户提供主叫用户的号码。TEMPALLOWED：缺省主叫号码显示允许。网络仅在移动用户在呼叫前拨“#31#被叫号码”抑制主叫号码显示时才激活CLIR业务。TEMPRESTRICTED：缺省限制。网络会自动激活CLIR业务，除非移动用户在呼叫前拨“*31#被叫号码”抑制CLIR业务。 默认值：无。 |
| BSGTYPE     | CLIR基本业务组操作类型 | 仅当本命令中的“是否提供CLIR业务”参数取值为“TRUE”时，该参数有效。CLIR基本业务组操作类型，对该基本业务组进行删除、添加和重置操作。同时配合参数BSGLIST中设置的具体业务进行配置。 取值范围： REMOVE: 删除ADD: 添加RESET: 重置 默认值：无。                                                                                                                                   |
| BSGLIST     | CLIR基本业务组     | 仅当本命令中的“是否提供CLIR业务”参数取值为“TRUE”时，该参数有效。CLIR基本业务组。 取值范围： TS1X: Telephony Service，话音业务TS2X: Short Message Service，短消息业务TS6X: Facsimile Service Group，传真业务BS2X: Asynchronous Bearer Service，异步承载业务BS3X: Synchronous Bearer Service，同步承载业务 默认值：无。                                 |

## 使用实例

将IMSI为460000009012345的用户短消息的CLIR业务属性修改为永久限制。例如：

MOD CLIR: IMSI="460000009012345", PROV=TRUE, MODE=PERMANENT, BSGTYPE=ADD, BSGLIST=TS2X;