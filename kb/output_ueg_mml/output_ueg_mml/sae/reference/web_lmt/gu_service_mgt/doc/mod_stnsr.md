# 修改用户STNSR地址(MOD STNSR)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

此操作用于提供/撤销用户的STNSR(Session Transfer Number for SRVCC)号码。

## 注意事项

- “IMSI”、“ISDN”、“IMSIFILE”、“ISDNFILE”、“IMSISTNSRFILE”、“ISDNSTNSRFILE”是互斥参数，有且只能有一个参数出现。
- “RECORDCOUNT”存在时，“IMSIFILE”和“ISDNFILE”不能存在；“IMSI”或“ISDN”必须存在一个。

## 参数说明

| 参数标识          | 参数名称            | 参数说明                                                                                                                                                                                                                                                       |
|:--------------|:----------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IMSI          | IMSI            | IMSI号码。 取值范围：E.212格式的编码，6～15位的十进制数字。 默认值：无。 说明：可选参数。                                                                                                                                                                                                       |
| ISDN          | MSISDN          | MSISDN号码。 取值范围：E.164格式的编码，1～15位的十进制数。 默认值：无。 说明：可选参数。                                                                                                                                                                                                      |
| RECORDCOUNT   | 用户个数            | 用户数量，用于连续号段批操作。代表以指定的IMSI、MSISDN为起始号码，号码连续的RECORDCOUNT个用户。 取值范围：整数类型，1～10000。如果只有一个用户，该参数不必提供。 默认值：无。 说明：可选参数。                                                                                                                                             |
| IMSIFILE      | IMSI文件名         | IMSI文件名称，IMSIFILE是由多个不连续的IMSI号码组成的批操作文件，每个IMSI号码占一行。 取值范围：字符串类型，由1～16个字母或数字组成，不包含文件的绝对路径。 默认值：无。 说明：可选参数。文件后缀名为.txt，通常通过Web UI上的文件选项将文件上传到指定位置。                                                                                                            |
| ISDNFILE      | MSISDN文件名       | MSISDN文件名称，ISDNFILE是由多个不连续的MSISDN号码组成的批操作文件，每个MSISDN号码占一行。 取值范围：字符串类型，由1～16个字母或数字组成，不包含文件的绝对路径。 默认值：无。 说明：可选参数。文件后缀名为.txt，通常通过Web UI上的文件选项将文件上传到指定位置。                                                                                                      |
| IMSISTNSRFILE | IMSI/STNSR文件名   | IMSI/STNSR文件名称，IMSISTNSRFILE是由多个不连续的IMSI号码和对应的STNSR号码组成的批操作文件，每个IMSI号码和STNSR号码占一行。 取值范围：字符串类型，由1～16个字母或数字组成，不包含文件的绝对路径。 默认值：无。 说明：可选参数。文件后缀名为.txt，通常通过Web UI上的文件选项将文件上传到指定位置。                                                                              |
| ISDNSTNSRFILE | MSISDN/STNSR文件名 | MSISDN/STNSR文件名称，ISDNSTNSRFILE是由多个不连续的MSISDN号码和对应的STNSR号码组成的批操作文件，每个MSISDN号码和STNSR号码占一行。 取值范围：字符串类型，由1～16个字母或数字组成，不包含文件的绝对路径。 默认值：无。 说明： 说明：可选参数。文件后缀名为.txt，通常通过Web UI上的文件选项将文件上传到指定位置。                                                                    |
| PROV          | 提供或撤销STN-SR     | 是否提供STN-SR。 取值范围： TRUE：提供FALSE：撤销 默认值：无。 说明：必选参数。当“IMSISTNSRFILE”或“ISDNSTNSRFILE”存在时，参数“PROV”必须为“TRUE”。当“RECORDCOUNT”、“IMSIFILE”、“ISDNFILE”任何一个参数存在时，参数“PROV”必须为“FALSE”。                                                                                   |
| STNSR         | SRVCC会话传输号码     | SRVCC会话传输号码。MME(Mobility Management Entity)使用它获取从PS域到CS域的网址路径会话传递。 取值范围：E.164格式的编码，3～15位的十进制数字。 默认值：无。 说明：当“PROV”为“TRUE”时，参数“STNSR”可见。当“IMSISTNSRFILE”或“ISDNSTNSRFILE”存在时，不能输入参数“STNSR”。当“IMSISTNSRFILE”与“ISDNSTNSRFILE”都不存在，并且“PROV”为“TRUE”时“STNSR”为必选参数。 |

## 使用实例

修改IMSI号码为460000009123456的用户的STNSR地址为8613484929766。命令如下：

`MOD STNSR: IMSI="460000009123456", PROV=TRUE, STNSR="8613484929766";`

批量修改用户的STNSR地址：

(1) 编写IMSISTNSRFILE批操作文件。

文件名IMSISTNSR.txt

文件格式为：

460000009012345 8613484929766

460000009012346 8613584929766

460000009012347 8613684929766

460000009012348 8613784929766

(2) 将IMSISTNSRFILE批操作文件传到指定位置。

通过Web UI上的文件选项将本地文件上传到指定位置

(3) 修改用户的STNSR地址，命令如下：

`MOD STNSR: IMSISTNSRFILE="IMSISTNSR.txt", PROV=TRUE;`