# 修改SMS-CSI模板(MOD SMSCSITPL)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**须知** 

本命令属于高危命令，执行不当会使签约此模板的用户数据被同步修改，因此执行该命令前，需要与华为技术支持确认后才可以实施。

该命令用于对一条SMS-CSI（Short Message Service CAMEL Subscription Information）模板数据记录的某些参数进行修改或调整，同时还用于为一条SMS-CSI模板数据记录增加多条触发准则。在该命令中，系统通过以下关键参数的组合来唯一标识一条SMS-CSI模板数据记录：

- “HLR序列号”
- “模板ID”

## 注意事项

用户进行位置更新或触发其他涉及SS-CSI模板的流程时，系统会根据用户签约的SMS-CSI模板ID下发模板中的数据，修改模板数据会使签约此模板的用户数据被同步修改，会影响在网用户，因此现网执行修改模板操作时需要慎重。

## 参数说明

| 参数标识           | 参数名称                   | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|:---------------|:-----------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HLRSN          | HLR序列号                 | 标识一条SMS-CSI模板数据记录的关键字段之一（其取值不能被修改），用于标识需要对哪一条SMS-CSI模板数据记录的参数进行修改或调整，操作员可以使用LST HLRSN命令查询获得。                                                                                                                                                                                                                                                                                                                                                                        |
| TPLID          | 模板ID                   | 标识一条SMS-CSI模板数据记录的关键字段之一（其取值不能被修改），用于标识需要对哪一条SMS-CSI模板数据记录的参数进行修改或调整，操作员可以使用LST SMSCSITPL命令查询获得。                                                                                                                                                                                                                                                                                                                                                                    |
| TPLNAME        | 模板名                    | 用于标识待修改模板在系统中的名称。 取值范围：1～60位字母或十进制数字组成的字符串。 默认值：无。                                                                                                                                                                                                                                                                                                                                                                                                                  |
| CAMEL          | CAMEL业务处理能力            | 用于标识gsmSCF（GSM Service Control Function）在处理该项具体CAMEL业务时所需要的CAMEL协议阶段的支持。CAMEL的发展经历了四个阶段，不同的阶段CAMEL特性的应用范围不同，可以按运营商的需要进行配置。该参数的配置应该与本命令中的“业务键”参数对应的具体CAMEL业务所要求支持的CAMEL支持能力一致。 取值范围：PHASE3：CAMEL特性应用于始发短消息业务（SMS MO）、GPRS会话和PDP上下文、HLR用户数据的控制和网络信令负荷。PHASE4：是PHASE3的增强，同时可应用于终结短消息业务（SMS MT）。 默认值：无。                                                                                                                                                                 |
| USHNDL         | VLR/SGSN不支持CAMEL时的处理方式 | 用于标识VLR或SGSN不支持MOSMSCSI或MTSMSCSI所需要的CAMEL业务处理能力时的处理方式。 取值范围：CALLBAR：呼叫闭锁，与签约了ODB-BAOC（闭锁所有呼出业务）相同。RR：漫游限制。NONCAMEL：短消息被当作非CAMEL业务继续处理。FORBIDDENSMSMO：仅禁止始发短消息功能，其它业务正常使用。 默认值：无。                                                                                                                                                                                                                                                                                    |
| PROV           | 是否提供DP值                | 用于标识执行该命令是增加/修改还是删除DP数据。如果待修改模板中只设置了一个DP值，该参数不能设置为FALSE。 取值范围：TRUE：增加/修改如果指定的DP值在模板中不存在，则与该DP值对应的数据将被增加到模板中。 FALSE：删除如果指定的DP值已经存在，与指定的DP值相关的数据将被删除。如果指定的DP值在模板中不存在，系统将会提示错误。 默认值：无。                                                                                                                                                                                                                                                                                 |
| MOMTSWITCH     | MOSMSCSI/MTSMSCSI开关    | 用于标识执行该命令是对MOSMSCSI进行操作还是对MTSMSCSI进行操作。 取值范围：MOSMSCSI：始发短消息用户CAMEL签约信息，仅当“CAMEL业务处理能力”参数选择“PHASE3”时，可以设置该枚举值。MTSMSCSI：终结短消息用户CAMEL签约信息，仅当“CAMEL业务处理能力”参数选择“PHASE4”时，可以设置该枚举值。 默认值：MOSMSCSI。                                                                                                                                                                                                                                                                         |
| DP             | DP值                    | 仅当本命令中的“是否提供DP值”参数为“TRUE”或“FALSE”时该参数有效。用于标识触发SMS-CSI业务的检出点，当在检出点满足相应的DP触发准则时，就会触发相应的CAMEL业务。 取值范围：SMSCOLLECTEDINFO：又称TDP1，当“MOSMSCSI/MTSMSCSI开关”参数选择“MOSMSCSI”时，没有触发准则，只要在检出点检测到MSC或SGSN从终端接收到短消息的事件即可触发CAMEL业务。SMS_Delivery_Request：又称TDP2，当“MOSMSCSI/MTSMSCSI开关”参数选择“MTSMSCSI”时，在检出点检测到MSC或SGSN请求发送短消息给目的终端的事件、同时满足DP触发准则即可触发CAMEL业务。 默认值：SMSCOLLECTEDINFO。                                                                                                      |
| DPCRITERIA     | DP准则                   | 仅当本命令中的“是否提供DP值”参数为“TRUE”时该参数有效。用于标识MTSMSCSI的DP触发准则。 取值范围：SMS_DELIVER：表示当短消息传输协议数据单元包含从SMSC发往MS的短消息用户数据时触发。SMS_SUBMIT_REPORT：表示当短消息传输协议数据单元包含从MS发往SMSC的短消息用户数据时触发。SMS_STATUS_REPORT：表示当短消息传输协议数据单元包含从SMSC发往MS通知其之前发送的短消息状态时触发。 默认值：无。 说明：用户可以签约多个DP准则，并用“&”连接，例如SMS_DELIVER-1&SMS_SUBMIT_REPORT-1&SMS_STATUS_REPORT-1。参数复选框中的灰化表示不修改系统原有值。                                                                                                                          |
| GSMSCFADD      | SCP地址                  | 仅当本命令中的“是否提供DP值”参数为“TRUE”时该参数有效。用于标识接入gsmSCF功能实体的地址。 取值范围：1～15位十进制数字组成的字符串。 采用E.164编码方式，编码格式为：CC+NDC+LSP，例如，一个典型的“SCP地址”为：“86-139-00777”。各关键字段的含义是： CC（Country Code）：国家码，即SCP所处国家在国际PSTN编号计划中的国家码，它由ITU-T在全球范围内统一分配，其最大长度为3位。例如，中国的国家码为86、英国的国家码为44等。NDC（National Destination Code）：国内目的码，即移动业务接入码，它是由本国电信主管部门在本国范围内统一分配的PLMN网络号，其最大长度为3位。例如，某运营商使用的PLMN网络号为134～139。LSP（Locally Significant Part）：本地有效部分，它是由某个运营商在本PLMN网络运营范围内统一分配的、用于具体代表某个SCP的号码，其最大长度为9位。 默认值：无。 |
| SK             | 业务键                    | 仅当本命令中的“是否提供DP值”参数为“TRUE”时该参数有效。用于标识用户在gsmSCF中签约的CAMEL业务。gsmSSF（GSM Service Switching Function）将业务键发给gsmSCF后，gsmSCF根据该业务键执行对应的业务逻辑。业务键是HLR与SCP的对接参数之一，用于在CAP/INAP消息中唯一标识一种智能业务，它是一种号码资源，需要由运营商向本国的电信主管部门申请获得。 取值范围：0～2147483647 默认值：无。                                                                                                                                                                                                                              |
| DEFSMS         | 缺省短消息处理                | 仅当本命令中的“是否提供DP值”参数为“TRUE”时该参数有效。用于标识当gsmSSF与gsmSCF之间的对话出现错误时，缺省短消息处理指示释放还是继续短消息处理流程。 取值范围：ReleaseTransaction：释放ContinueTransaction：继续 默认值：无。                                                                                                                                                                                                                                                                                                                        |
| AVAILABLE_PLMN | SMS-CSI模板使用范围          | 用于标识用户在不同的网络中漫游时是否下发SMS-CSI数据。 取值范围： HPLMN：用户在HPLMN（Home Public Land Mobile Network）内漫游时，HLR向VLR或SGSN下发SMS-CSI，否则不下发。FPLMN：用户在FPLMN（Forbidden PLMN）内漫游时，HLR向VLR或SGSN下发SMS-CSI，否则不下发。INTERNATIONAL：用户漫游出本国时，HLR向VLR或SGSN下发SMS-CSI，否则不下发。HPLMNC： 用户在本国漫游时，HLR向VLR或SGSN下发SMS-CSI，否则不下发。ALL_PLMN：用户在所有PLMN内漫游时，HLR均向VLR或SGSN下发SMS-CSI。NOT_AVAILABLE：HLR不向VLR或SGSN下发SMS-CSI。 默认值：无。                                                                                      |

## 使用实例

1. 修改“HLR序列号”为“1”的HLR上的SMS-CSI模板数据记录。其中，“模板ID”为“2”，“MOSMSCSI/MTSMSCSI开关”为“MOSMSCSI”，“DP值”为“SMSCOLLECTEDINFO”，“SMS-CSI模板使用范围”为“HPLMN”：

   ```
   MOD SMSCSITPL: HLRSN=1, TPLID=2, PROV=TRUE, MOMTSWITCH=MOSMSCSI, DP=SMSCOLLECTEDINFO, AVAILABLE_PLMN=HPLMN;
   ```
2. 修改“HLR序列号”为“1”的HLR上的SMS-CSI模板数据记录。其中，“模板ID”为“2”，“MOSMSCSI/MTSMSCSI开关”为“MTSMSCSI”，“DP值”为“SMS\_Delivery\_Request”，“SMS-CSI模板使用范围”为“HPLMNC”：

   ```
   MOD SMSCSITPL: HLRSN=1, TPLID=1, PROV=TRUE, MOMTSWITCH=MTSMSCSI, DP=SMS_Delivery_Request, AVAILABLE_PLMN=HPLMNC;
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释   | 原因分析                                                                                                                                                   | 处理建议                                                                                                                                   |
|:--------|:--------|:-------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------|
| ERR1010 | 参数冲突    | “VLR/SGSN不支持CAMEL时的处理方式”和“MOSMSCSI/MTSMSCSI开关”参数取值未遵循参数配置规范。“MOSMSCSI/MTSMSCSI开关”和“DP值”参数取值未遵循参数配置规范。“CAMEL业务处理能力”和“MOSMSCSI/MTSMSCSI开关”参数取值未遵循参数配置规范。 | 根据实际情况，参考参数配置规范重新输入参数： “VLR/SGSN不支持CAMEL时的处理方式”和“MOSMSCSI/MTSMSCSI开关”。“MOSMSCSI/MTSMSCSI开关”和“DP值”。“CAMEL业务处理能力”和“MOSMSCSI/MTSMSCSI开关”。 |
| ERR3003 | 模板未定义   | “HLR序列号”和“模板ID”对应的SMS-CSI模板数据记录不存在。                                                                                                                    | 使用LST SMSCSITPL命令查询后，重新确认要修改哪个“HLR序列号”和“模板ID”对应的SMS-CSI模板数据记录。                                                                         |
| ERR1004 | 无效的参数值  | 界面输入的非“HLR序列号”和“模板ID”参数不在相应的参数取值范围内。                                                                                                                   | 根据实际情况，重新输入提示错误的参数的取值，确保其取值符合要求。                                                                                                       |