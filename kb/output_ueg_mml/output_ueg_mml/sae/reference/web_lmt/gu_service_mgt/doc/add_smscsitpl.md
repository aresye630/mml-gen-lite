# 增加SMS-CSI模板(ADD SMSCSITPL)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于为HLR在配置数据库中增加一条SMS-CSI（Short Message Service CAMEL Subscription Information）模板数据记录，根据运营商CAMEL网络的实际情况进行配置，相关参数由运营商提供。用户通过签约SMS-CSI模板ID签约SMS-CSI业务。

SMS-CSI是用户的短消息业务CAMEL签约信息，HLR管理和存储MOSMSCSI（始发短消息用户CAMEL签约信息）和MTSMSCSI（终结短消息用户CAMEL签约信息）签约信息，并在位置更新、数据恢复或MOSMSCSI或MTSMSCSI签约信息发生变化时下发给MSC/VLR或SGSN。MSC或SGSN在短消息的接收、发送过程中根据MOSMSCSI和MTSMSCSI配置信息向gsmSSF（GSM Service Switching Function）发送请求指令，使gsmSSF可以控制MSC或SGSN对短消息收、发的处理。

## 注意事项

- 该命令执行一次只能给一个模板增加MOSMSCSI（始发短消息用户CAMEL签约信息）或MTSMSCSI（终结短消息用户CAMEL签约信息）数据，如果需要同时增加MOSMSCSI和MTSMSCSI数据，则需要执行**ADD SMSCSITPL**命令两次。
- 系统中增加的MOSMSCSI/MTSMSCSI模板记录数分别不能超过5000条。

## 参数说明

| 参数标识           | 参数名称                   | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                |
|:---------------|:-----------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HLRSN          | HLR序列号                 | 用于标识一个HLR序列号。该参数必须先由ADD HLRSN命令定义，然后才能在此处引用。                                                                                                                                                                                                                                                                                                                                                                                        |
| TPLID          | 模板ID                   | 用于标识待增加模板在系统中的序号。 取值范围：0～65534 默认值：无。                                                                                                                                                                                                                                                                                                                                                                                               |
| TPLNAME        | 模板名                    | 用于标识待增加模板在系统中的名称。 取值范围：1～60位字母或十进制数字组成的字符串。 默认值：无。                                                                                                                                                                                                                                                                                                                                                                                  |
| CAMEL          | CAMEL业务处理能力            | 用于标识gsmSCF（GSM Service Control Function）在处理该项具体CAMEL业务时所需要的CAMEL协议阶段的支持。CAMEL的发展经历了四个阶段，不同的阶段CAMEL特性的应用范围不同，可以按运营商的需要进行配置。该参数的配置应该与本命令中的“业务键”参数对应的具体CAMEL业务所要求支持的CAMEL支持能力一致。 取值范围：PHASE3：CAMEL特性应用于始发短消息业务（SMS MO）、GPRS会话和PDP上下文、HLR用户数据的控制和网络信令负荷。PHASE4：是PHASE3的增强，同时可应用于终结短消息业务（SMS MT）。 默认值：PHASE3。                                                                                                                            |
| USHNDL         | VLR/SGSN不支持CAMEL时的处理方式 | 用于标识VLR或SGSN不支持MOSMSCSI或MTSMSCSI所需要的CAMEL业务处理能力时HLR替代下发的处理方式。 取值范围：CALLBAR：呼叫闭锁，与签约了ODB-BAOC（闭锁所有呼出业务）相同。RR：漫游限制。NONCAMEL：短消息被当作非CAMEL业务继续处理。FORBIDDENSMSMO：仅禁止始发短消息功能，其它业务正常使用。 默认值：无。                                                                                                                                                                                                                                             |
| MOMTSWITCH     | MOSMSCSI/MTSMSCSI开关    | 用于标识执行该命令是对MOSMSCSI进行操作还是对MTSMSCSI进行操作。 取值范围：MOSMSCSI：始发短消息用户CAMEL签约信息，仅当“CAMEL业务处理能力”参数选择“PHASE3”时，可以设置该枚举值。MTSMSCSI：终结短消息用户CAMEL签约信息，仅当“CAMEL业务处理能力”参数选择“PHASE4”时，可以设置该枚举值。 默认值：MOSMSCSI。                                                                                                                                                                                                                                         |
| DP             | DP值                    | 用于标识触发SMS-CSI业务的检出点，当在检出点满足相应的DP触发准则时，就会触发相应的CAMEL业务。 取值范围：SMSCOLLECTEDINFO：又称TDP1，当“MOSMSCSI/MTSMSCSI开关”参数选择“MOSMSCSI”时，没有触发准则，只要在检出点检测到MSC或SGSN从终端接收到短消息的事件即可触发CAMEL业务。SMS_Delivery_Request：又称TDP2，当“MOSMSCSI/MTSMSCSI开关”参数选择“MTSMSCSI”时，在检出点检测到MSC或SGSN请求发送短消息给目的终端的事件、同时满足DP触发准则即可触发CAMEL业务。 默认值：SMSCOLLECTEDINFO。                                                                                                              |
| DPCRITERIA     | DP准则                   | 仅当本命令中的“MOSMSCSI/MTSMSCSI开关”参数为“MTSMSCSI”时该参数有效。用于标识MTSMSCSI的DP触发准则。 取值范围：SMS_DELIVER：表示当短消息传输协议数据单元包含从SMSC（Short Message Service Center）发往MS的短消息用户数据时触发。SMS_SUBMIT_REPORT：表示当短消息传输协议数据单元包含从MS发往SMSC的短消息用户数据时触发。SMS_STATUS_REPORT：表示当短消息传输协议数据单元包含从SMSC发往MS通知其之前发送的短消息状态时触发。 默认值：无。 说明：用户可以签约多个DP准则，并用“&”连接，例如SMS_DELIVER-1&SMS_SUBMIT_REPORT-1&SMS_STATUS_REPORT-1。参数复选框中的灰化表示不修改系统原有值。                                            |
| GSMSCFADD      | SCP地址                  | 用于标识接入gsmSCF功能实体的地址。 取值范围：1～15位十进制数字组成的字符串。 采用E.164编码方式，编码格式为：CC+NDC+LSP，例如，一个典型的“SCP地址”为：“86-139-00777”。各关键字段的含义是： CC（Country Code）：国家码，即SCP所处国家在国际PSTN编号计划中的国家码，它由ITU-T在全球范围内统一分配，其最大长度为3位。例如，中国的国家码为86、英国的国家码为44等。NDC（National Destination Code）：国内目的码，即移动业务接入码，它是由本国电信主管部门在本国范围内统一分配的PLMN网络号，其最大长度为3位。例如，某运营商使用的PLMN网络号为134～139。LSP（Locally Significant Part）：本地有效部分，它是由某个运营商在本PLMN网络运营范围内统一分配的、用于具体代表某个SCP的号码，其最大长度为9位。 默认值：无。 |
| SK             | 业务键                    | 用于标识用户在gsmSCF中签约的CAMEL业务。gsmSSF（GSM Service Switching Function）将业务键发给gsmSCF后，gsmSCF根据该业务键执行对应的业务逻辑。业务键是HLR与SCP的对接参数之一，用于在CAP/INAP消息中唯一标识一种智能业务，它是一种号码资源，需要由运营商向本国的电信主管部门申请获得。 取值范围：0～2147483647 默认值：无。                                                                                                                                                                                                                              |
| DEFSMS         | 缺省短消息处理                | 用于标识当gsmSSF与gsmSCF之间的对话出现异常时，缺省短消息处理指示释放还是继续短消息处理流程。 取值范围：ReleaseTransaction：释放ContinueTransaction：继续 默认值：无。                                                                                                                                                                                                                                                                                                                        |
| AVAILABLE_PLMN | SMS-CSI模板使用范围          | 用于标识用户在不同的网络中漫游时是否下发SMS-CSI数据。 取值范围：HPLMN：用户在HPLMN（Home Public Land Mobile Network）内漫游时，HLR向VLR或SGSN下发SMS-CSI，否则不下发。FPLMN：用户在FPLMN（Forbidden PLMN）内漫游时，HLR向VLR或SGSN下发SMS-CSI，否则不下发。INTERNATIONAL：用户漫游出本国时，HLR向VLR或SGSN下发SMS-CSI，否则不下发。HPLMNC： 用户在本国漫游时，HLR向VLR或SGSN下发SMS-CSI，否则不下发。ALL_PLMN：用户在所有PLMN内漫游时，HLR均向VLR或SGSN下发SMS-CSI。NOT_AVAILABLE：HLR不向VLR或SGSN下发SMS-CSI。 默认值：无。 说明：执行该命令并且不输入该参数时，系统会设置初始值ALL_PLMN。                   |

## 使用实例

1. 在“HLR序列号”为“1”的HLR上增加一条MOSMSCSI模板数据记录。其中，“模板ID”为“4”，“模板名称”为“SMSCSI”，“CAMEL业务处理能力”为“PHASE3”，MOSMSCSI/MTSMSCSI开关为“MOSMSCSI”，“VLR/SGSN不支持CAMEL时的处理方式”为“CALLBAR”，“DP值”为“SMSCOLLECTEDINFO”，“SCP地址”为“8613911111”，“业务键”为“45”，“缺省短消息处理”为“ContinueTransaction”：

   ```
   ADD SMSCSITPL: HLRSN=1, TPLID=4, TPLNAME="SMSCSI", CAMEL=PHASE3, MOMTSWITCH=MOSMSCSI, USHNDL=CALLBAR, DP=SMSCOLLECTEDINFO, GSMSCFADD="8613911111", SK=45, DEFSMS=ContinueTransaction;
   ```
2. 在实例1的同一模板上增加MTSMSCSI模板数据记录。其中，“HLR序列号”为“1”，“模板ID”为“4”，“CAMEL业务处理能力”为“PHASE4”，MOSMSCSI/MTSMSCSI开关为“MTSMSCSI”，“DP值”为“SMS\_Delivery\_Request”，“SCP地址”为“8613911111”，“业务键”为“46”，“缺省短消息处理”为“ReleaseTransaction”：

   ```
   ADD SMSCSITPL: HLRSN=1, TPLID=4, CAMEL=PHASE4, USHNDL=CALLBAR, MOMTSWITCH=MTSMSCSI, DP=SMS_Delivery_Request, GSMSCFADD="8613911111", SK=46, DEFSMS=ReleaseTransaction;
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释   | 原因分析                                                                                                                                                   | 处理建议                                                                                                                                                                                         |
|:--------|:--------|:-------------------------------------------------------------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ERR1010 | 参数冲突    | “VLR/SGSN不支持CAMEL时的处理方式”和“MOSMSCSI/MTSMSCSI开关”参数取值未遵循参数配置规范。“MOSMSCSI/MTSMSCSI开关”和“DP值”参数取值未遵循参数配置规范。“CAMEL业务处理能力”和“MOSMSCSI/MTSMSCSI开关”参数取值未遵循参数配置规范。 | 根据实际情况，参考参数配置规范重新输入参数： “VLR/SGSN不支持CAMEL时的处理方式”和“MOSMSCSI/MTSMSCSI开关”。“MOSMSCSI/MTSMSCSI开关”和“DP值”。“CAMEL业务处理能力”和“MOSMSCSI/MTSMSCSI开关”。                                                       |
| ERR3007 | 记录不存在   | “HLR序列号”未定义。                                                                                                                                           | 根据实际情况，重新输入“HLR序列号”的取值，确保其取值符合要求。                                                                                                                                                            |
| ERR1004 | 无效的参数值  | 界面输入的非“HLR序列号”参数不在相应的参数取值范围内。                                                                                                                          | 根据实际情况，重新输入提示错误的参数的取值，确保其取值符合要求。                                                                                                                                                             |
| ERR3004 | 模板已存在   | 本次操作输入的“模板ID”在数据库中已存在。                                                                                                                                 | 根据实际情况，重新输入参数，确保输入的“模板ID”和系统中已存在的不重复。可执行LST SMSCSITPL命令查询系统中已存在的SMS-CSI模板。                                                                                                                   |
| ERR3047 | 超过最大限制  | 可能原因为如下之一：增加的MOSMSCSI模板记录数超过5000条。增加的MTSMSCSI模板记录数超过5000条。                                                                                             | 根据实际情况，如需增加MOSMSCSI/MTSMSCSI模板，处理步骤如下：执行LST SMSCSITPL命令，查询已存在的MOSMSCSI/MTSMSCSI模板。执行RMV SMSCSITPL命令，删除不必要的MOSMSCSI/MTSMSCSI模板。执行该命令增加MOSMSCSI/MTSMSCSI模板，确保增加的MOSMSCSI/MTSMSCSI模板记录数在规定范围之内。 |