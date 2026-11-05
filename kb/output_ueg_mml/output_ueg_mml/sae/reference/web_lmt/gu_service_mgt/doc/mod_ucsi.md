# 修改U-CSI业务(MOD UCSI)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

此操作可以用来给单用户或批用户提供或撤销U-CSI（CAMEL）业务。

执行该命令只能签约一个U-CSI模板。设置U-CSI模板，请参见“U-CSI模板管理 ”。

## 注意事项

- IMSI、ISDN、IMSIFILE、ISDNFILE是条件可选参数，任何一个参数出现即可。
- RECORDCOUNT一定不能与IMSIFILE或ISDNFILE同时存在。
- 仅当**SET MAPSERV**命令中“UCSI签约管理方式”参数值设置为“Template”时，该命令生效。

## 参数说明

| 参数标识        | 参数名称        | 参数说明                                                                                                         |
|:------------|:------------|:-------------------------------------------------------------------------------------------------------------|
| IMSI        | IMSI        | IMSI号码，E.212格式的编码，为6～15位的十进制数字。                                                                              |
| ISDN        | MSISDN      | MSISDN号码，E.164格式的编码，为1～15位的十进制数字。                                                                            |
| RECORDCOUNT | 用户个数        | 用户的数目，最大100000个。如果只有一个用户，该参数不必提供。 该参数提供，代表以指定的IMSI、MSISDN为起始号码，号码连续的RECORDCOUNT个用户。                          |
| IMSIFILE    | IMSI文件名     | IMSI文件名称，IMSIFILE包含多个不连续的IMSI号码，每个IMSI号码占一行，16个以内的字母或数字组成的字符串。                                               |
| ISDNFILE    | MSISDN文件名   | MSISDN文件名称，ISDNFILE包含多个不连续的MSISDN号码，每个MSISDN号码占一行。16个以内的字母或数字组成的字符串。                                         |
| PROV        | 是否提供U-CSI业务 | 是否提供U-CSI业务，必选参数。 TRUE：提供 FALSE：撤销                                                                           |
| TPLID       | 模板ID        | 仅当本命令中的“是否提供U-CSI业务”参数为“TRUE”时该参数有效。用于标识为用户签约的UCSI模板ID，该参数必须先由ADD UCSITPL命令定义，然后才能在此处引用。 取值范围：0～65534 默认值：无。 |

## 使用实例

1. 为IMSI起始号码为460000009123456的4个用户提供U-CSI业务，采用预先设置的TPLID=2的模板，命令如下：

   MOD UCSI: IMSI="460000009123456", RECORDCOUNT=4, PROV=TRUE, TPLID=2;
2. 为IMSI起始号码为460000009123456的2个用户撤销U-CSI业务，命令如下：

   MOD UCSI: IMSI="460000009123456", RECORDCOUNT=2, PROV=FALSE;
3. 为IMSI起始号码为460000009123457的用户提供U-CSI业务，采用预先设置的TPLID=3的模板，命令如下：

   MOD UCSI: IMSI="460000009123457", PROV=TRUE, TPLID=3;