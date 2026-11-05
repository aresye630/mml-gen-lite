# 修改NON-3GPP用户属性(MOD NONSUB)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

此命令用来修改NON-3GPP用户的属性。

## 注意事项

- IMSI、ISDN、IMSIFILE、ISDNFILE是条件可选参数，有且只能有一个参数出现。
- RECORDCOUNT一定不能与IMSIFILE或ISDNFILE同时存在。
- 签约NON-3GPP属性值的用户必须是EPS签约用户。
- 如果PROVMIP6=TRUE，参数MIP6FEAVEC为必选参数。
- 如果PROVTIMEOUT=TRUE，参数SESSIONTIMEOUT为必选参数。

## 参数说明

| 参数标识           | 参数名称             | 参数说明                                                                                                                                                                                                                                                                                                                        |
|:---------------|:-----------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IMSI           | IMSI             | 此参数用于设置IMSI号码。 取值范围：E.212格式的编码，6～15位的十进制数字。                                                                                                                                                                                                                                                                                 |
| ISDN           | MSISDN           | 此参数用于设置MSISDN号码。 取值范围：E.164格式的编码，1～15位的十进制数字。                                                                                                                                                                                                                                                                               |
| RECORDCOUNT    | 用户个数             | 用户的数目。如果只有一个用户，该参数不必提供。 该参数提供，代表以指定的IMSI、MSISDN为起始号码，号码连续的RECORDCOUNT个用户。 取值范围：1～100000。                                                                                                                                                                                                                                    |
| IMSIFILE       | IMSI文件名          | 此参数用于设置IMSI文件名称。IMSIFILE是由多个不连续的IMSI号码组成的批操作文件，每个IMSI号码占一行。 取值范围：1～16个字母或数字。                                                                                                                                                                                                                                                |
| ISDNFILE       | MSISDN文件名        | 此参数用于设置ISDN文件名称。ISDNFILE是由多个不连续的MSISDN号码组成的批操作文件，每个MSISDN号码占一行。 取值范围：1～16个字母或数字。                                                                                                                                                                                                                                            |
| NON3GPPSUPP    | 是否支持Non-3GPP接入   | 是否允许提供Non-3GPP属性。 取值范围： TRUE：提供。FALSE：不提供。 必选参数。                                                                                                                                                                                                                                                                            |
| NONARD         | Non-3GPP无线接入类型限制 | 仅当本命令中的“是否支持Non-3GPP接入”参数为“TRUE”时该参数有效。Non-3GPP无线接入类型限制。 取值范围： WLANNOTALLOWED：限制无线局域网。CDMA2000_1XNOTALLOWED：限制CDMA2000_1X接入网。HRPDNOTALLOWED：限制高速率包数据。UMBNOTALLOWED：限制超移动宽带。EHRPDNOTALLOWED：限制扩展高速率包数据。 缺省值：不限制接入类型。                                                                                                         |
| PROVMIP6       | 是否提供移动IP支持能力     | 仅当本命令中的“是否支持Non-3GPP接入”参数为“TRUE”时该参数有效。是否提供移动IP支持能力。 取值范围： TRUE：提供。FALSE：不提供。 可选参数。                                                                                                                                                                                                                                         |
| MIP6FEAVEC     | 移动IP支持能力         | 仅当本命令中的“是否支持Non-3GPP接入”参数为“TRUE”时该参数有效。Non-3GPP GW(GateWay)支持移动IP的能力。 取值范围： MIP6_INTEGRATED：支持基于DHCPv6的归属代理发现功能。 PMIP6_SUPPORTED：指示Non-3GPP GW使用PMIPV6。 IP4_HOA_SUPPORTED：指示Non-3GPP GW授权UE使用IPV4-HOA。 ASSIGN_LOCAL_IP：指示Non-3GPP GW给用户分配本地IP地址。 MIP4_SUPPORTED：指示Non-3GPP GW使用MIPv4。 GTPv2_SUPPORTED：指示Non-3GPP GW使用GTPv2。 |
| PROVTIMEOUT    | 是否提供会话超时时间       | 仅当本命令中的“是否支持Non-3GPP接入”参数为“TRUE”时该参数有效。是否提供会话超时时间。 取值范围： TRUE：提供。FALSE：不提供。 可选参数。                                                                                                                                                                                                                                           |
| SESSIONTIMEOUT | 会话超时时间           | 仅当本命令中的“是否提供会话超时时间”参数为“TRUE”时该参数有效。Non-3GPP接入方式下，一次Diameter消息会话的超时时间，单位为秒。 取值范围：1～4294967295                                                                                                                                                                                                                                |
| VOWIFI_TAG     | VoWIFI用户标志       | 仅当本命令中的“是否支持Non-3GPP接入”参数取值为“TRUE”时该参数有效。用于标识NON-3GPP用户是否为VoWIFI用户。 取值范围： VoWIFI：VoWIFI用户。Non_VoWIFI：非VoWIFI用户。 默认值：无。 说明：执行该命令并且不输入该参数时，系统会设置初始值“Non_VoWIFI”。                                                                                                                                                              |

## 使用实例

为“IMSI”号码是“460000009012345”的新用户设置NON-3GPP属性值，操作员需要进行以下操作流程：

1. 添加K2和KI鉴权信息。
   1. 添加K2鉴权信息，“K2序列号”为“2”，“K2密钥输入方式”为“ClearKey”，“K2值”为“1234567890abcde1234567890abcde12”：

      ```
      ADD K2: HLRSN=1, K2SNO=2, KEYTYPE=ClearKey, K2VALUE="*****";
      ```
   2. 添加KI鉴权信息，“操作类型”为“ADD”，“KI值”为“1234567890abcde1234567890abcde12”，“卡类型”为“SIM”，“鉴权算法类型”为“COMP128\_3”：

      ```
      ADD KI: HLRSN=1, IMSI="460000009012345", OPERTYPE=ADD, KIVALUE="*****", CARDTYPE=SIM, ALG=COMP128_3, K2SNO=2;
      ```
2. 为该用户签约EPS业务，使其成为EPS用户。“MSISDN”号码为“460000009012345”，“卡类型”为“SIM”，“网络接入模式”为“BOTH”，“EPS业务标识”为“TRUE”，“缺省呼叫类型”为“TS11”，“UE最大上行带宽”为“22222”，“UE最大下行带宽”为“11111”：

   ```
   ADD SUB: HLRSN=1, IMSI="460000009012345", ISDN="460000009012345", CARDTYPE=SIM, NAM=BOTH, EPS=TRUE, DEFAULTCALL=TS11, AMBRMAXUL=22222, AMBRMAXDL=11111;
   ```
3. 为用户添加NON-3GPP属性信息，“IMSI”号码为“460000009012345”，“是否支持Non-3GPP接入”为“TRUE”，“Non-3GPP无线接入类型限制”为“WLANNOTALLOWED-1&CDMA2000\_1XNOTALLOWED-1&HRPDNOTALLOWED-1&UMBNOTALLOWED-1&EHRPDNOTALLOWED-1”，“是否提供移动IP支持能力”为“TRUE”，“移动IP支持能力”为“MIP6\_INTEGRATED”，“VoWIFI用户标志”为“VoWIFI”：

   ```
   MOD NONSUB: IMSI="460000009012345", NON3GPPSUPP=TRUE, NONARD=WLANNOTALLOWED-1&CDMA2000_1XNOTALLOWED-1&HRPDNOTALLOWED-1&UMBNOTALLOWED-1&EHRPDNOTALLOWED-1, PROVMIP6=TRUE, MIP6FEAVEC=MIP6_INTEGRATED, VOWIFI_TAG=VoWIFI;
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释               | 原因分析                                                                                               | 处理建议                                                                                                                    |
|:--------|:--------------------|:---------------------------------------------------------------------------------------------------|:------------------------------------------------------------------------------------------------------------------------|
| ERR1004 | 无效的参数值              | 可能原因为如下之一：参数“IMSI”的取值不是6～15位十进制数字组成的字符串。参数“MSISDN”的取值不是1～15位十进制数字组成的字符串。                           | 根据实际情况，重新输入“IMSI”或“MSISDN”的取值，确保其取值符合要求。                                                                                |
| ERR1009 | 参数丢失                | “IMSI”、“MSISDN”、“IMSI文件名”、“MSISDN文件名”四个参数一个都没有输入。                                                  | 根据实际情况，重新输入参数，并满足“IMSI”、“MSISDN”、“IMSI文件名”、“MSISDN文件名”四个参数必须有且只能有一个参数出现的条件。                                             |
| ERR1005 | 文件未找到               | “IMSI文件名”或“MSISDN文件名”对应的文件没有通过文件管理功能上传到PGW的指定目录。                                                   | 通过PGW Web LMT的文件上传功能上传预先编写的批操作资源文件到PGW的如下目录：“/opt/pgw/pgwtmpfile/SYSHLRSN+操作员名称”。具体请参见批操作资源文件存放位置。                      |
| ERR1010 | 参数冲突                | 可能原因为如下之一：“IMSI”、“MSISDN”、“IMSI文件名”、“MSISDN文件名”四个参数中有两个以上的参数被输入。“用户个数”与“IMSI文件名”或“MSISDN文件名”同时被输入。 | 根据实际情况，重新输入参数，确保满足以下两点：“IMSI”、“MSISDN”、“IMSI文件名”、“MSISDN文件名”四个参数是可选参数，必须有且只能有一个参数出现。“用户个数”不能与“IMSI文件名”或“MSISDN文件名”同时配置。 |
| ERR1025 | 批操作文件中格式非法          | 参数“IMSI文件名”或“MSISDN文件名”对应的批操作文件格式不正确。                                                              | 请根据IMSIFILE文件格式和ISDNFILE文件格式，重新确定对应的批操作文件格式。                                                                            |
| ERR3383 | 用户不是Non-3GPP用户或者未开户 | 输入的“IMSI”或“MSISDN”参数对应的用户未开户或者不是Non-3GPP用户。                                                        | 核实IMSI号码或MSISDN号码，确保其对应的用户为Non-3GPP用户并验证其正确性，如果确定输入无误，证明实际输入的参数“IMSI”或“MSISDN”对应的用户未开户，请参考本命令中的使用实例给用户开户。               |
| ERR3810 | 用户不是EPS用户或未开户       | 用户的IMSI号码或MSISDN号码输入错误，实际输入的参数“IMSI”或“MSISDN”对应的用户未开户或者不是EPS用户。                                    | 核实IMSI号码或MSISDN号码，确保其对应的用户为EPS用户并验证其正确性，如果确定输入无误，证明实际输入的参数“IMSI”或“MSISDN”对应的用户未开户，请参考本命令中的使用实例给用户开户。                    |