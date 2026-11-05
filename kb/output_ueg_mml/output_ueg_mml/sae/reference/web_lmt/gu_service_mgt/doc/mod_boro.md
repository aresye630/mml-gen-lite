# 修改BORO业务(MOD BORO)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

此操作用来提供/撤销BORO业务。

签约BORO业务的用户，必须已经成功开户，并且未签约BORO业务。

撤销BORO业务的用户，必须已经成功开户，并且已经签约BORO业务。

用户的BORO业务处于激活状态，执行该命令去签约BORO业务，则会下发删除用户数据消息。

## 注意事项

- IMSI、ISDN、IMSIFILE、ISDNFILE是条件可选参数，有且只能有一个参数出现。
- RECORDCOUNT一定不能与IMSIFILE或ISDNFILE同时存在。
- 如果提供BORO业务，PROV=TRUE；如果撤销BORO业务，PROV=FALSE。
- 如果提供BORO业务，用户在VLR中的漫游限制状态不能是BAOCTS11。通过LST VSRR命令查询用户签约的VLR漫游限制模板，然后利用查询结果中的VLRTPLID通过LST VSLIST查询用户在VLR中的漫游限制状态。

## 参数说明

| 参数标识        | 参数名称       | 参数说明                                                                                |
|:------------|:-----------|:------------------------------------------------------------------------------------|
| IMSI        | IMSI       | IMSI号码， E.212格式的编码，6～15位的十进制数字。                                                     |
| ISDN        | MSISDN     | MSISDN号码，E.164格式的编码，1～15位的十进制数字。                                                    |
| RECORDCOUNT | 用户个数       | 用户的数目，最大100000个。如果只有一个用户，该参数不必提供。 该参数提供，代表以指定的IMSI、MSISDN为起始号码，号码连续的RECORDCOUNT个用户。 |
| IMSIFILE    | IMSI文件名    | IMSIFILE文件名称，由16个以内的数字或字母组成。IMSIFILE是由多个不连续的IMSI号码组成的批操作文件，每个IMSI号码占一行。             |
| ISDNFILE    | MSISDN文件名  | ISDNFILE文件名称，由16个以内的数字或字母组成。ISDNFILE是由多个不连续的MSISDN号码组成的批操作文件，每个MSISDN号码占一行。         |
| PROV        | 是否提供BORO业务 | 提供还是撤销BORO业务。 取值范围： TRUE：提供 FALSE：撤销                                                |

## 使用实例

1. 为IMSI号码是460000009012345的用户提供BORO业务。命令如下：

   MOD BORO: IMSI="460000009012345", PROV=TRUE;
2. 为IMSI号码是460000009012345的用户撤销BORO业务。命令如下：

   MOD BORO: IMSI="460000009012345", PROV=FALSE;