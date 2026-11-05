# 修改ACR业务(MOD ACR)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

此操作用来为用户签约或去签约ACR业务。

为用户签约ACR业务前，先执行以下操作：

- 确认用户已开户。
- 执行**LST MAPSERV**命令，查询“ACR\_PLMNSS”参数取值是否为“PLMN-SS-1”～“PLMN-SS-F”。如果不是，请执行**SET MAPSERV**命令进行修改。
- 确认用户已签约CLIP业务。

ACR业务签约后自动激活，不需要单独的激活操作。

## 注意事项

- “IMSI”、“ISDN”、“IMSIFILE”、“ISDNFILE”是条件可选参数，有且只能有一个参数出现。
- “RECORDCOUNT”一定不能与“IMSIFILE”或“ISDNFILE”同时存在。

## 参数说明

| 参数标识        | 参数名称      | 参数说明                                                                                |
|:------------|:----------|:------------------------------------------------------------------------------------|
| IMSI        | IMSI      | IMSI号码，E.212格式的编码，为6～15位的十进制数字。                                                     |
| ISDN        | MSISDN    | MSISDN号码，E.164格式的编码，为1～15位的十进制数字。                                                   |
| RECORDCOUNT | 用户个数      | 用户的数目，最大100000个。如果只有一个用户，该参数不必提供。 该参数提供，代表以指定的IMSI、MSISDN为起始号码，号码连续的RECORDCOUNT个用户。 |
| IMSIFILE    | IMSI文件名   | IMSI文件名称，1～16个字母或数字组成。IMSIFILE是由多个不连续的IMSI号码组成的批操作文件，每个IMSI号码占一行。                   |
| ISDNFILE    | MSISDN文件名 | ISDN文件名称，1～16个字母或数字组成。ISDNFILE是由多个不连续的MSISDN号码组成的批操作文件，每个MSISDN号码占一行。               |
| PROV        | 是否提供ACR业务 | 是否提供ACR业务。 TRUE(1)：提供FALSE(0)：不提供                                                   |

## 使用实例

1. 为IMSI号码为460000009123456的用户提供ACR业务。

   MOD ACR: IMSI="460000009123456", PROV=TRUE;
2. 为IMSI号码为460000009123456的用户撤销ACR业务。

   MOD ACR: IMSI="460000009123456", PROV=FALSE;