# 修改CAMEL业务(MOD CAMEL)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

此操作用来为用户签约或去签约CAMEL业务，CAMEL业务包括：OCSI（Originating CAMEL Subscription Information）、TCSI（Terminating CAMEL Subscription Information）、VTCSI、UCSI、SSCSI、TIFCSI、MCSI、SMSCSI、GPRSCSI、DCSI、IMOCSI、IMVTCSI。

执行此命令后，如果是给用户签约该业务，则会下发插入用户数据消息；如果是给用户去签约该业务，则会下发删除用户数据消息。

## 注意事项

- IMSI、ISDN、IMSIFILE、ISDNFILE是条件可选参数，任何一个参数出现即可。
- RECORDCOUNT一定不能与IMSIFILE或ISDNFILE同时存在。
- 至少签约、去签约一个CSI（CAMEL Subscription Information）业务。
- 签约CSI业务时需要指定相应业务的模板号。

## 参数说明

| 参数标识          | 参数名称                     | 参数说明                                                                                                                              |
|:--------------|:-------------------------|:----------------------------------------------------------------------------------------------------------------------------------|
| IMSI          | IMSI                     | IMSI号码，E.212格式的编码。 取值范围：6～15位的十进制数字。                                                                                              |
| ISDN          | MSISDN                   | MSISDN号码，E.164格式的编码。 取值范围：1～15位的十进制数字。                                                                                            |
| RECORDCOUNT   | 用户个数                     | 用户的数目，最大100000个。如果只有一个用户，该参数不必提供。 该参数提供，代表以指定的IMSI、MSISDN为起始号码，号码连续的RECORDCOUNT个用户。                                               |
| IMSIFILE      | IMSI文件名                  | IMSI文件名称，IMSIFILE包含多个不连续的IMSI号码，每个IMSI号码占一行，16个以内的字母或数字组成的字符串。                                                                    |
| ISDNFILE      | MSISDN文件名                | MSISDN文件名称，ISDNFILE包含多个不连续的MSISDN号码，每个MSISDN号码占一行。16个以内的字母或数字组成的字符串。                                                              |
| OCSIPROV      | 签约或去签约主叫CAMEL签约信息业务      | 是否提供O-CSI业务。 TRUE：提供FALSE：撤销                                                                                                      |
| OCSITPLID     | OCSI模板ID                 | 仅当本命令中的“签约或去签约主叫CAMEL签约信息业务”参数为“TRUE”时该参数有效。用于标识为用户签约的OCSI模板ID，该参数必须先由ADD OCSITPL命令定义，然后才能在此处引用。 取值范围：0～65534之间的十进制数字。            |
| TCSIPROV      | 签约或去签约被叫CAMEL签约信息业务      | 是否提供T-CSI业务。 TRUE：提供FALSE：撤销                                                                                                      |
| TCSITPLID     | TCSI模板ID                 | 仅当本命令中的“签约或去签约被叫CAMEL签约信息业务”参数为“TRUE”时该参数有效。用于标识为用户签约的TCSI模板ID，该参数必须先由ADD TCSITPL命令定义，然后才能在此处引用。 取值范围：0～65534之间的十进制数字。            |
| VTCSIPROV     | 签约或去签约VMSC被叫CAMEL签约信息业务  | 是否提供VT-CSI业务。 TRUE：提供FALSE：撤销                                                                                                     |
| VTCSITPLID    | VTCSI模板ID                | 仅当本命令中的“签约或去签约VMSC被叫CAMEL签约信息业务”参数为“TRUE”时该参数有效。用于标识为用户签约的VTCSI模板ID，该参数必须先由ADD VTCSITPL命令定义，然后才能在此处引用。 取值范围：0～65534之间的十进制数字。      |
| UCSIPROV      | 签约或去签约USSD CAMEL签约信息业务   | 是否提供U-CSI业务。 TRUE：提供FALSE：撤销                                                                                                      |
| UCSITPLID     | UCSI模板ID                 | 仅当本命令中的“签约或去签约USSD CAMEL签约信息业务”参数为“TRUE”时该参数有效。 用于标识为用户签约的UCSI模板ID，该参数必须先由ADD UCSITPL命令定义，然后才能在此处引用。 取值范围：0～65534之间的十进制数字。        |
| SSCSIPROV     | 签约或去签约补充业务调用提示CSI业务      | 是否提供SS-CSI业务。 TRUE：提供FALSE：撤销                                                                                                     |
| SSCSITPLID    | SSCSI模板ID                | 仅当本命令中的“签约或去签约补充业务调用提示CSI业务”参数为“TRUE”时该参数有效。用于标识为用户签约的SSCSI模板ID，该参数必须先由ADD SSCSITPL命令定义，然后才能在此处引用。 取值范围：0～65534之间的十进制数字。          |
| TIFCSIPROV    | 签约或去签约翻译信息标志CSI业务        | 是否提供TIF-CSI业务。 TRUE：提供FALSE：撤销                                                                                                    |
| MCSIPROV      | 签约或去签约移动管理CAMEL签约信息业务    | 是否提供M-CSI业务。 TRUE：提供FALSE：撤销                                                                                                      |
| MCSITPLID     | MCSI模板ID                 | 仅当本命令中的“签约或去签约移动管理CAMEL签约信息业务”参数为“TRUE”时该参数有效。用于标识为用户签约的MCSI模板ID，该参数必须先由ADD MCSITPL命令定义，然后才能在此处引用。 取值范围：0～65534之间的十进制数字。          |
| MOSMSCSIPROV  | 签约或去签约始发短消息业务CAMEL签约信息业务 | 是否提供MOSMS-CSI业务。 TRUE：提供FALSE：撤销                                                                                                  |
| MOSMSCSITPLID | MOSMSCSI模板ID             | 仅当本命令中的“签约或去签约始发短消息业务CAMEL签约信息业务”参数为“TRUE”时该参数有效。用于标识为用户签约的MOSMSCSI模板ID，该参数必须先由ADD SMSCSITPL命令定义，然后才能在此处引用。 取值范围：0～65534之间的十进制数字。 |
| MTSMSCSIPROV  | 签约或去签约终结短消息业务CAMEL签约信息业务 | 是否提供MTSMS-CSI业务。 TRUE：提供FALSE：撤销                                                                                                  |
| MTSMSCSITPLID | MTSMSCSI模板ID             | 仅当本命令中的“签约或去签约终结短消息业务CAMEL签约信息业务”参数为“TRUE”时该参数有效。用于标识为用户签约的MTSMSCSI模板ID，该参数必须先由ADD SMSCSITPL命令定义，然后才能在此处引用。 取值范围：0～65534之间的十进制数字。 |
| GPRSCSIPROV   | 签约或去签约GPRS CAMEL签约信息业务   | 是否提供GPRS-CSI业务。 TRUE：提供FALSE：撤销                                                                                                   |
| GPRSCSITPLID  | GPRSCSI模板ID              | 仅当本命令中的“签约或去签约GPRS CAMEL签约信息业务”参数为“TRUE”时该参数有效。用于标识为用户签约的GPRSCSI模板ID，该参数必须先由ADD GPRSCSITPL命令定义，然后才能在此处引用。 取值范围：0～65534之间的十进制数字。   |
| DCSIPROV      | 签约或去签约拨号业务CAMEL签约信息业务    | 是否提供D-CSI业务。 TRUE：提供FALSE：撤销                                                                                                      |
| DCSITPLID     | DCSI模板ID                 | 仅当本命令中的“签约或去签约拨号业务CAMEL签约信息业务”参数为“TRUE”时该参数有效。用于标识为用户签约的DCSI模板ID，该参数必须先由ADD DCSITPL命令定义，然后才能在此处引用。 取值范围：0～65534之间的十进制数字。          |
| IMOCSIPROV    | 签约或去签约O-IM-CSI业务         | 是否提供O-IM-CSI业务。 TRUE：提供FALSE：撤销                                                                                                   |
| IMOCSITPLID   | O-IM-CSI模板ID             | 仅当本命令中的“签约或去签约O-IM-CSI业务”参数为“TRUE”时该参数有效。用于标识为用户签约的O-IM-CSI模板ID，该参数必须先由ADD OCSITPL命令定义，然后才能在此处引用。 取值范围：0～65534之间的十进制数字。           |
| IMVTCSIPROV   | 签约或去签约VT-IM-CSI业务        | 是否提供VT-IM-CSI业务。 TRUE：提供FALSE：撤销                                                                                                  |
| IMVTCSITPLID  | VT-IM-CSI模板ID            | 仅当本命令中的“签约或去签约VT-IM-CSI业务”参数为“TRUE”时该参数有效。用于标识为用户签约的VT-IM-CSI模板ID，该参数必须先由ADD VTCSITPL命令定义，然后才能在此处引用。 取值范围：0～65534之间的十进制数字。        |

## 使用实例

1. 为IMSI起始号码为460000009123456的用户提供O-CSI业务，采用预先设置的TPLID=2的模板，命令如下：

   **MOD CAMEL**: IMSI="460000009123456", OCSIPROV=TRUE, OCSITPLID=2;
2. 为IMSI起始号码为460000009123456的用户撤销O-CSI业务，命令如下：

   **MOD CAMEL**: IMSI="460000009123456", OCSIPROV=FALSE;
3. 为IMSI起始号码为460000009123456的用户提供O-CSI和T-CSI业务，O-CSI采用预先设置的TPLID=2的模板，T-CSI采用预先设置的TPLID=8的模板，命令如下：

   **MOD CAMEL**: IMSI="460000009123456", OCSIPROV=TRUE, OCSITPLID=2, TCSIPROV=TRUE, TCSITPLID=8;