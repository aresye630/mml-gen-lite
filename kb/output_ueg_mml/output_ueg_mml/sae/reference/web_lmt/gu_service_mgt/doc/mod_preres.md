# 修改号码识别业务(MOD PRERES)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

此操作用来同时签约或同时去签约号码识别业务（CLIP、COLP、CLIR和COLR）与该业务的显示和限制设置。

执行此命令后，如果是给用户签约该业务，则会下发插入用户数据消息；如果是给用户去签约该业务，则会下发删除用户数据消息。

## 注意事项

- 条件参数IMSI、ISDN必须且只能有一个存在。
- 当CLIP为TRUE时，条件参数CLIPOVERRIDE必须指定。
- 当COLP为TRUE时，条件参数COLPOVERRIDE必须指定。
- 当CLIR为TRUE时，条件参数CLIRMODE必须指定。

## 参数说明

| 参数标识         | 参数名称          | 参数说明                                                                                                                                                                                                                                              |
|:-------------|:--------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IMSI         | IMSI          | IMSI号码，E.212格式的编码。 取值范围：6～15位的十进制数字。                                                                                                                                                                                                              |
| ISDN         | MSISDN        | MSISDN号码，E.164格式的编码。 取值范围：1～15位的十进制数字。                                                                                                                                                                                                            |
| RECORDCOUNT  | 用户个数          | 用户的数目，最大100000个。如果只有一个用户，该参数不必提供。 该参数提供，代表以指定的IMSI、MSISDN为起始号码，号码连续的RECORDCOUNT个用户。                                                                                                                                                               |
| IMSIFILE     | IMSI文件名       | IMSIFILE文件名称，IMSIFILE包含多个不连续的IMSI号码，每个IMSI号码占一行，16个以内的字母或数字组成的字符串。                                                                                                                                                                                |
| ISDNFILE     | MSISDN文件名     | ISDNFILE文件名称，ISDNFILE包含多个不连续的MSISDN号码，每个MSISDN号码占一行。16个以内的字母或数字组成的字符串。                                                                                                                                                                            |
| CLIP         | 是否提供CLIP业务    | 是否提供CLIP业务。 取值范围： TRUE：是FALSE：否 可选参数。                                                                                                                                                                                                             |
| CLIPOVERRIDE | CLIP超越属性      | 仅当本命令中的“是否提供CLIP业务”参数为“TRUE”时该参数有效。是否签约超越主叫号码识别属性。 取值范围： TRUE:签约FALSE:去签约                                                                                                                                                                         |
| CLIPTYPE     | CLIP基本业务组操作类型 | 仅当本命令中的“是否提供CLIP业务”参数为“TRUE”时该参数有效。CLIP基本业务组操作类型，对该基本业务组进行删除、添加和重置操作。同时配合参数BSGCLIP中设置的具体业务进行配置。 取值范围： REMOVE: 删除ADD: 添加RESET: 重置                                                                                                                  |
| BSGCLIP      | CLIP基本业务组     | 仅当本命令中的“是否提供CLIP业务”参数为“TRUE”时该参数有效。CLIP基本业务组。 取值范围： TS1X: Telephony Service，话音业务TS2X: Short Message Service，短消息业务TS6X: Facsimile Service Group，传真业务BS2X: Asynchronous Bearer Service，异步承载业务BS3X: Synchronous Bearer Service，同步承载业务                |
| CLIR         | 是否提供CLIR业务    | 是否提供CLIR业务。 取值范围： TRUE: 是FALSE: 否 可选参数。                                                                                                                                                                                                           |
| CLIRMODE     | 主叫线识别限制模式     | 仅当本命令中的“是否提供CLIR业务”参数为“TRUE”时该参数有效。设置主叫线识别限制模式。 取值范围： PERMANENT：永久限制，对所有出呼叫有效。选中此项，移动用户作主叫时，不允许网络向被叫用户提供主叫用户的号码。TEMPALLOWED：缺省主叫号码显示允许，网络仅在移动用户在呼叫前拨“#31#被叫号码”抑制主叫号码显示时才激活CLIR业务。TEMPRESTRICTED：缺省限制。网络会自动激活CLIR业务，除非移动用户在呼叫前拨“*31#被叫号码”抑制CLIR业务。 |
| CLIRTYPE     | CLIR基本业务组操作类型 | 仅当本命令中的“是否提供CLIR业务”参数为“TRUE”时该参数有效。CLIR基本业务组操作类型，对该基本业务组进行删除、添加和重置操作。同时配合参数BSGCLIR中设置的具体业务进行配置。 取值范围： REMOVE: 删除ADD: 添加RESET: 重置                                                                                                                  |
| BSGCLIR      | CLIR基本业务组     | 仅当本命令中的“是否提供CLIR业务”参数为“TRUE”时该参数有效。CLIR基本业务组。 取值范围： TS1X: Telephony Service，话音业务TS2X: Short Message Service，短消息业务TS6X: Facsimile Service Group，传真业务BS2X: Asynchronous Bearer Service，异步承载业务BS3X: Synchronous Bearer Service，同步承载业务                |
| COLP         | 是否提供COLP业务    | 是否提供COLP业务。 取值范围： TRUE：是FALSE：否 可选参数。                                                                                                                                                                                                             |
| COLPOVERRIDE | COLP超越属性      | 仅当本命令中的“是否提供COLP业务”参数为“TRUE”时该参数有效。是否签约超越被叫号码识别属性。 取值范围： TRUE:签约FALSE: 去签约                                                                                                                                                                        |
| COLPTYPE     | COLP基本业务组操作类型 | 仅当本命令中的“是否提供COLP业务”参数为“TRUE”时该参数有效。COLP基本业务组操作类型，对该基本业务组进行删除、添加和重置操作。同时配合参数BSGCOLP中设置的具体业务进行配置。 取值范围： REMOVE: 删除ADD: 添加RESET: 重置                                                                                                                  |
| BSGCOLP      | COLP基本业务组     | 仅当本命令中的“是否提供COLP业务”参数为“TRUE”时该参数有效。COLP基本业务组。 取值范围： TS1X: Telephony Service，话音业务TS2X: Short Message Service，短消息业务TS6X: Facsimile Service Group，传真业务BS2X: Asynchronous Bearer Service，异步承载业务BS3X: Synchronous Bearer Service，同步承载业务                |
| COLR         | 是否提供COLR业务    | 是否提供COLR业务。 取值范围： TRUE: 是FALSE: 否 可选参数。                                                                                                                                                                                                           |
| COLRTYPE     | COLR基本业务组操作类型 | 仅当本命令中的“是否提供COLR业务”参数为“TRUE”时该参数有效。COLR基本业务组操作类型，对该基本业务组进行删除、添加和重置操作。同时配合参数BSGCOLR中设置的具体业务进行配置。 取值范围： REMOVE: 删除ADD: 添加RESET: 重置                                                                                                                  |
| BSGCOLR      | COLR基本业务组     | 仅当本命令中的“是否提供COLR业务”参数为“TRUE”时该参数有效。COLR基本业务组。 取值范围： TS1X: Telephony Service，话音业务TS2X: Short Message Service，短消息业务TS6X: Facsimile Service Group，传真业务BS2X: Asynchronous Bearer Service，异步承载业务BS3X: Synchronous Bearer Service，同步承载业务                |

## 使用实例

1. 为IMSI号码为460000009123456的用户语音业务签约主叫线识别显示、签约超越主叫号码识别属性、签约短消息业务主叫线识别限制业务、签约永久限制。

   MOD PRERES: IMSI="460000009123456", CLIP=TRUE, CLIPOVERRIDE=TRUE, CLIPTYPE=ADD, BSGCLIP=TS1X, CLIR=TRUE, CLIRMODE=PERMANENT, CLIRTYPE=ADD, BSGCLIR=TS2X;
2. 为IMSI号码为460000009123456的用户去签约主叫线识别显示、去签约主叫线识别限制业务、去签约被叫线识别显示业务、去签约被叫线识别限制业务。

   MOD PRERES: IMSI="460000009123456", CLIP=FALSE, CLIR=FALSE, COLP=FALSE, COLR= FALSE;