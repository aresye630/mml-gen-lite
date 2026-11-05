# 修改CSI-STATE业务(MOD CSISTATE)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

此操作可以用来修改单用户或批用户的CSI业务状态。

CSI状态是附加在用户签约的CSI信息上的一种状态标志，当该状态为Active(True)时表示其CSI可用，当状态为Deactive（False）时表示其CSI不可用。 HLR上用户签约某CSI且可用时才会处理该CSI数据，用户签约某CSI但不可用则不处理该CSI数据。 CSI状态可以通过MOD CSISTATE或者ATM MAP流程修改，用户开户时其所有CSI状态都为Active(True)。 CSI状态在激活去激活之间转换时，HLR上只记录状态改变结果不修改其CSI数据，但会通过ISD或DSD消息通知VLR/SGSN保存或者删除CSI数据。

## 注意事项

- IMSI、ISDN、IMSIFILE、ISDNFILE是条件可选参数，任何一个参数出现即可。
- RECORDCOUNT一定不能与IMSIFILE或ISDNFILE同时存在。
- 用户的某CAMEL业务对应CSI状态为FALSE时，修改此CAMEL业务，该CSI数据不会下发。

## 参数说明

| 参数标识        | 参数名称      | 参数说明                                                                                |
|:------------|:----------|:------------------------------------------------------------------------------------|
| IMSI        | IMSI      | IMSI号码，E.212格式的编码，为6～15位的十进制数字。                                                     |
| ISDN        | MSISDN    | MSISDN号码，E.164格式的编码，为1～15位的十进制数字。                                                   |
| RECORDCOUNT | 用户个数      | 用户的数目，最大100000个。如果只有一个用户，该参数不必提供。 该参数提供，代表以指定的IMSI、MSISDN为起始号码，号码连续的RECORDCOUNT个用户。 |
| IMSIFILE    | IMSI文件名   | IMSI文件名称，IMSIFILE包含多个不连续的IMSI号码，每个IMSI号码占一行，16个以内的字母或数字组成的字符串。                      |
| ISDNFILE    | MSISDN文件名 | MSISDN文件名称，ISDNFILE包含多个不连续的MSISDN号码，每个MSISDN号码占一行。16个以内的字母或数字组成的字符串。                |
| CSITYPE     | CSI类型     | 此参数用于表明CSI类型。 取值范围为MCSI。                                                            |
| CSISTATE    | CSI状态     | 此参数用于修改CSI状态。 取值范围： TRUE：激活 FALSE：去激活                                               |

## 使用实例

1. 修改IMSI号码为460000009123456的用户的MCSI状态为激活。命令如下：

   MOD CSISTATE: IMSI="460000009123456", CSITYPE=MCSI, CSISTATE=TRUE;
2. 修改IMSI起始号码为460000009123456的4个用户的MCSI状态为激活，命令如下：

   MOD CSISTATE: IMSI="460000009123456", RECORDCOUNT=4, CSITYPE=MCSI, CSISTATE=TRUE;
3. 批操作修改用户的MCSI状态为激活，ISDNFILE为"dddd.txt",命令如下：

   MOD CSISTATE: ISDNFILE="dddd.txt", CSITYPE=MCSI, CSISTATE=TRUE;