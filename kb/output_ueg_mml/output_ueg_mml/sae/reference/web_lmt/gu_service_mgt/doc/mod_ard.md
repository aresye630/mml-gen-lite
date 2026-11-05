# 修改ARD业务(MOD ARD)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于修改用户的接入限制数据。为未签约ARD（Access Restriction Data）业务的用户提供该业务，或者为已签约ARD业务的用户撤销该业务。

执行此命令后，如果是给用户签约该业务，则会下发插入用户数据消息。如果是给用户去签约该业务，则会下发位置取消消息。

## 注意事项

- IMSI、ISDN、IMSIFILE、ISDNFILE是条件可选参数，有且只能有一个参数出现。
- 如果“是否提供ARD业务”参数取值为“TRUE”，则表示提供ARD业务，此时“是否限制接入UTRAN”、“是否限制接入GERAN”、“是否限制接入GAN”、“是否限制接入I-HSPA-Evolution”、“是否限制接入E-UTRAN”、“是否限制接入Non-3GPP”、“是否限制接入NB-IoT”、“是否限制接入NGRAN”、“是否限制接入5GS NR”和“是否限制接入NR REDCAP”十个参数中至少提供一个。如果“是否提供ARD业务”参数取值为“FALSE”，则表示撤销ARD业务，此时上述十个参数均不可见。
- 如果“是否限制接入UTRAN”和“是否限制接入GERAN”参数都设为“TRUE”，可禁止用户上网，请谨慎操作。
- 当**SET MAPCONF**命令中，参数“是否支持ARD增强处理”设置为“TRUE”，且VLR/SGSN支持对RAT类型的检查时，执行该命令修改用户的接入限制数据后，会检查用户当前的RAT接入类型，如果当前RAT接入受限，则HSS会向VLR/SGSN发送Cancel Location消息。
- 当“是否提供ARD业务”参数取值为“FALSE”时，“是否限制接入WLAN”参数取值不变。

## 参数说明

| 参数标识                  | 参数名称                   | 参数说明                                                                                                                                                                                                                                                 |
|:----------------------|:-----------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IMSI                  | IMSI                   | IMSI号码，E.212格式的编码，为6～15位的十进制数字。                                                                                                                                                                                                                      |
| ISDN                  | MSISDN                 | MSISDN号码，E.164格式的编码，为1～15位的十进制数字。                                                                                                                                                                                                                    |
| RECORDCOUNT           | 用户个数                   | 用户的数目，最大100000个。如果只有一个用户，该参数不必提供。 该参数提供，代表以指定的IMSI、MSISDN为起始号码，号码连续的RECORDCOUNT个用户。                                                                                                                                                                  |
| IMSIFILE              | IMSI文件名                | IMSI文件名称，IMSIFILE包含多个不连续的IMSI号码，每个IMSI号码占一行，16个以内的字母或数字组成的字符串。                                                                                                                                                                                       |
| ISDNFILE              | MSISDN文件名              | MSISDN文件名称，ISDNFILE包含多个不连续的MSISDN号码，每个MSISDN号码占一行。16个以内的字母或数字组成的字符串。                                                                                                                                                                                 |
| PROV                  | 是否提供ARD业务              | 提供还是撤销ARD业务。 TRUE：提供。FALSE：撤销。                                                                                                                                                                                                                       |
| UTRANNOTALLOWED       | 是否限制接入UTRAN            | 仅当本命令中的“是否提供ARD业务”参数设置为“TRUE”时该参数有效，用于标识是否限制接入UTRAN（Universal Terrestrial Radio Access Network）。 TRUE：限制 FALSE：不限制                                                                                                                                   |
| GERANNOTALLOWED       | 是否限制接入GERAN            | 仅当本命令中的“是否提供ARD业务”参数设置为“TRUE”时该参数有效，用于标识是否限制接入GERAN（GSM/EDGE Radio Access Network）。 TRUE：限制FALSE：不限制                                                                                                                                                 |
| GANNOTALLOWED         | 是否限制接入GAN              | 仅当本命令中的“是否提供ARD业务”参数设置为“TRUE”时该参数有效，用于标识是否限制接入GAN（General Access Network）。 取值范围： TRUE：限制FALSE：不限制 默认值：无。 说明：                                                                                                                                         |
| IHSPAENOTALLOWED      | 是否限制接入I-HSPA-Evolution | 仅当本命令中的“是否提供ARD业务”参数设置为“TRUE”时该参数有效，用于标识是否限制接入I-HSPA-Evolution。 取值范围： TRUE：限制FALSE：不限制。 默认值：无。                                                                                                                                                       |
| EUTRANNOTALLOWED      | 是否限制接入E-UTRAN          | 仅当本命令中的“是否提供ARD业务”参数设置为“TRUE”时该参数有效，用于标识是否限制接入E-UTRAN（Evolved Universal Terrestrial Radio Access Network）。 取值范围： TRUE：限制FALSE：不限制 默认值：无。                                                                                                             |
| N3GPPNOTALLOWED       | 是否限制接入Non-3GPP         | 仅当本命令中的“是否提供ARD业务”参数设置为“TRUE”时该参数有效，用于标识是否限制接入Non-3GPP。 取值范围： TRUE：限制FALSE：不限制 默认值：无。                                                                                                                                                                |
| EUTRANNBIOTNOTALLOWED | 是否限制接入NB-IoT           | 仅当本命令中的“是否提供ARD业务”参数设置为“TRUE”时该参数有效，用于标识UDM网元根据配置的ARD数据判断是否限制用户接入NB-IOT。NB-IoT是一种新型窄带无线技术，用以满足物联网需求。 取值范围： TRUE：限制FALSE：不限制 默认值：无。                                                                                                                   |
| NGRANNOTALLOWED       | 是否限制接入NGRAN            | 仅当本命令中的“是否提供ARD业务”参数设置为“TRUE”时该参数有效，用于标识是否限制NSA组网用户接入5G无线网络，该参数在NSA组网场景下应用。 取值范围：TRUE：限制，表示不允许NSA组网用户接入5G无线网络。FALSE：不限制，表示允许NSA组网用户接入5G无线网络。 默认值：无。                                                                                                  |
| NR5GSNOTALLOWED       | 是否限制接入5GS NR           | 仅当本命令中的“是否提供ARD业务”参数设置为“TRUE”时该参数有效，用于标识是否限制用户接入5G无线网络，该参数在SA组网场景下应用。 取值范围： TRUE：限制，表示不允许用户接入5G无线网络。 FALSE：不限制，表示允许用户接入5G无线网络。 默认值：无。                                                                                                                |
| NRREDCAPNOTALLOWED    | 是否限制接入NR REDCAP        | 仅当本命令中的“是否提供ARD业务”参数设置为“TRUE”时该参数有效，用于标识是否限制NR RedCap（Reduced Capability）类型用户接入5G无线网络，该参数在SA组网场景下应用。 取值范围： TRUE：限制，表示不允许NR RedCap类型用户接入5G无线网络。 FALSE：不限制，表示允许NR RedCap类型用户接入5G无线网络。 默认值：无。                                                           |
| WLANNOTALLOWED        | 是否限制接入WLAN             | 仅当本命令中的“是否提供ARD业务”参数设置为“TRUE”时该参数有效，用于标识是否限制接入WLAN（Wireless Local Area Network）网络。 取值范围： TRUE：限制，表示不允许接入WLAN网络。 FALSE：不限制，表示允许接入WLAN网络。 默认值：无。 配置原则： 当SET MAPCONF命令的“是否使用WLAN判断的Non-3GPP接入权限”参数设置为“TRUE”时，该参数功能生效。当“是否提供ARD业务”参数取值为“FALSE”时，本参数取值不变。 |

## 使用实例

**例1**

运营商为IMSI号码是460000009123456的用户提供ARD业务，并不允许该用户接入UTRAN、GERAN网络。

MOD ARD: IMSI="460000009123456", PROV=TRUE, UTRANNOTALLOWED=TRUE, GERANNOTALLOWED=TRUE;

**例2:**

为IMSI号码是460456789012345的用户撤销ARD业务。命令如下：

MOD ARD: IMSI="460456789012345", PROV=FALSE;

**例3:**

为IMSI号码是460000009123456的用户提供ARD业务，并不允许该用户接入UTRAN、GERAN、GAN、I-HSPA-Evolution、E-UTRAN以及Non-3GPP等所有网络。命令如下：

MOD ARD: IMSI="460000009123456", PROV=TRUE, UTRANNOTALLOWED=TRUE, GERANNOTALLOWED=TRUE, GANNOTALLOWED=TRUE, IHSPAENOTALLOWED=TRUE, EUTRANNOTALLOWED=TRUE, N3GPPNOTALLOWED=TRUE;

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释    | 原因分析                                                                       | 处理建议                                                                         |
|:--------|:---------|:---------------------------------------------------------------------------|:-----------------------------------------------------------------------------|
| ERR3111 | 系统不支持该特性 | SET MAPCONF命令的“是否使用WLAN判断的Non-3GPP接入权限”参数设置为“FALSE”时，本命令配置了“是否限制接入WLAN”参数。 | 执行LST MAPCONF命令查询“是否使用WLAN判断的Non-3GPP接入权限”参数取值，确保取值为“TRUE”时输入“是否限制接入WLAN”参数。 |
| ERR3016 | 基本业务未提供  | 用户为非EPS用户。                                                                 | 2G/3G用户不支持使用“是否限制接入WLAN”参数控制WLAN网络接入权限。                                      |