# 修改PLMN自定义补充业务(MOD PLMNSS)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

此操作用来为用户提供或撤销PLMNSS业务。

执行此命令后，如果是给用户签约该业务，则会下发插入用户数据消息；如果是给用户去签约该业务，则会下发删除用户数据消息。

## 注意事项

- IMSI、ISDN、IMSIFILE、ISDNFILE是条件可选参数，有且只能有一个参数出现。
- RECORDCOUNT一定不能与IMSIFILE或ISDNFILE同时存在。
- 如果提供SS业务，PROV=TRUE；如果撤销SS业务，PROV=FALSE。

## 参数说明

| 参数标识        | 参数名称            | 参数说明                                                                                                                                                                     |
|:------------|:----------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IMSI        | IMSI            | IMSI号码，E.212格式的编码，6～15位的十进制数字。                                                                                                                                           |
| ISDN        | MSISDN          | MSISDN号码，E.164格式的编码，1～15位的十进制数字。                                                                                                                                         |
| RECORDCOUNT | 用户个数            | 用户的数目，最大100000个。如果只有一个用户，该参数不必提供。 该参数提供，代表以指定的IMSI、MSISDN为起始号码，号码连续的RECORDCOUNT个用户。                                                                                      |
| IMSIFILE    | IMSI文件名         | IMSIFILE文件名称，由16个以内的数字或字母组成。IMSIFILE是由多个不连续的IMSI号码组成的批操作文件，每个IMSI号码占一行。                                                                                                  |
| ISDNFILE    | MSISDN文件名       | ISDNFILE文件名称，由16个以内的数字或字母组成。ISDNFILE是由多个不连续的MSISDN号码组成的批操作文件，每个MSISDN号码占一行。                                                                                              |
| PROV        | 是否提供PLMN自定义补充业务 | 提供还是撤销SS业务。                                                                                                                                                              |
| PLMNSPECSS  | PLMN自定义补充业务     | PLMN自定义补充业务类型。可以选择所有的业务，也可以选择其中的几种或一种。如选择多个业务，两个业务之间用“&”隔开。 取值范围为：PLMN-SS-1～PLMN-SS-9，PLMN-SS-A～PLMN-SS-F、ALLPLMN-SS。业务由运营商自定义，例如PLMN-SS-1定义为热计费业务，PLMN-SS-E定义为个性化回铃音业务。 |

## 使用实例

1. 为IMSI号码是460000009012345的用户提供SS业务。命令如下：

   MOD PLMNSS: IMSI="460000009012345", PROV=TRUE,PLMNSPECSS=PLMN-SS-1;
2. 为IMSI号码是460000009012345的用户撤销SS业务。命令如下：

   MOD PLMNSS: IMSI="460000009012345", PROV=FALSE,PLMNSPECSS=PLMN-SS-1&PLMN-SS-2;