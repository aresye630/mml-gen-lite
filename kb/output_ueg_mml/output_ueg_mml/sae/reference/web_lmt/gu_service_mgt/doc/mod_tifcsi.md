# 修改TIF-CSI业务(MOD TIFCSI)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

此操作用来给用户提供或撤销TIF-CSI（CAMEL）业务。

执行此命令后，如果是给用户签约该业务，则会下发插入用户数据消息；如果是给用户去签约该业务，则会下发删除用户数据消息。

## 注意事项

- IMSI、ISDN、IMSIFILE、ISDNFILE是条件可选参数，任何一个参数出现即可。
- RECORDCOUNT一定不能与IMSIFILE或ISDNFILE同时存在。

## 参数说明

| 参数标识        | 参数名称          | 参数说明                                                                                |
|:------------|:--------------|:------------------------------------------------------------------------------------|
| IMSI        | IMSI          | IMSI号码，E.212格式的编码，为6～15位的十进制数字。                                                     |
| ISDN        | MSISDN        | MSISDN号码，E.164格式的编码，为1～15位的十进制数字。                                                   |
| RECORDCOUNT | 用户个数          | 用户的数目，最大100000个。如果只有一个用户，该参数不必提供。 该参数提供，代表以指定的IMSI、MSISDN为起始号码，号码连续的RECORDCOUNT个用户。 |
| IMSIFILE    | IMSI文件名       | IMSI文件名称，IMSIFILE包含多个不连续的IMSI号码，每个IMSI号码占一行，16个以内的字母或数字组成的字符串。                      |
| ISDNFILE    | MSISDN文件名     | MSISDN文件名称，ISDNFILE包含多个不连续的MSISDN号码，每个MSISDN号码占一行。16个以内的字母或数字组成的字符串。                |
| PROV        | 是否提供TIF-CSI业务 | 是否提供TIF-CSI业务，必选参数。 TRUE：提供 FALSE：撤销                                                |

## 使用实例

1. 为IMSI起始号码为460000009123456的4个用户提供TIF-CSI业务，命令如下：

   MOD TIFCSI: IMSI="460000009123456", RECORDCOUNT=4, PROV=TRUE;
2. 为IMSI起始号码为460000009123456的2个用户撤销TIF-CSI业务，命令如下：

   MOD TIFCSI: IMSI="460000009123456", RECORDCOUNT=2, PROV=FALSE;