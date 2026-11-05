# 增加SCP地址模板(ADD SCPTPL)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于在UDM中增加一个SCP（Service Control Point）地址模板。通过SCP地址模板，可以实现在当用户漫游到不同的网络位置时，进行O-CSI/T-CSI业务SCP数据的定制下发。

“SCP地址模板ID”在O-CSI模板和T-CSI模板中为可选参数，若在O-CSI模板和T-CSI模板中配置“SCP地址模板ID”时，系统的处理规则为：

- 当漫游用户当前所在网络与SCP模板定义的使用范围一致时，采用SCP地址模板定义的参数。
- 当漫游用户当前所在网络与SCP模板定义的使用范围不一致时，采用O-CSI模板/T-CSI模板定义的SCP地址相关参数。

## 注意事项

- 系统中增加的SCP地址模板记录数不能超过3000条。
- 系统中所有SCP地址模板增加的Camel版本记录数不能超过3000条。
- 系统中所有SCP地址模板增加的SCP地址总记录数不能超过5000条。

## 参数说明

| 参数标识          | 参数名称    | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|:--------------|:--------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HLRSN         | HLR序列号  | 用于标识一个HLR序列号。该参数必须先由ADD HLRSN命令定义，然后才能在此处引用。                                                                                                                                                                                                                                                                                                                                                                                          |
| TPLID         | 模板ID    | 用于标识SCP地址模板在系统中的序号。该参数在UDM中唯一，不能重复。 取值范围：0～65534 默认值：无。                                                                                                                                                                                                                                                                                                                                                                               |
| TPLNAME       | 模板名     | 用于标识SCP地址模板在系统中的名称。 取值范围：1～60位由字母或十进制数字组成的字符串。 默认值：无。                                                                                                                                                                                                                                                                                                                                                                                 |
| CAMEL         | CAMEL版本 | 用于标识gsmSCF（GSM Service Control Function）在处理CAMEL业务时所需要的CAMEL协议阶段的支持。可参考CAMEL业务管理。 取值范围： PHASE1：表示支持CAMEL phase 1，该CAMEL phase用于与移动始发和移动终结的呼叫相关的业务。 PHASE2：表示支持CAMEL phase 2，该CAMEL phase用于与补充业务调用相关的业务。 PHASE3：表示支持CAMEL phase 3，该CAMEL phase用于始发短消息业务（SMS MO）、GPRS会话和PDP上下文、HLR用户数据的控制和网络信令负荷。 PHASE4：表示支持CAMEL phase 4，该CAMEL phase用于终结短消息业务（SMS MT）。 默认值：无。                                                                        |
| AVAILABLEPLMN | 使用范围    | 用于标识SCP地址模板的使用范围。即当用户处在网络中的什么位置时才使用SCP地址模板中的SCP地址。 取值范围： LOCALDOMESTIC：国内本网。表示用户漫游地的VLR和用户归属HLR在同一个国家，且在同一个PLMN（Public Land Mobile Network）内。CROSSDOMESTIC：国内跨网。表示用户漫游地VLR和用户归属HLR在同一个国家，但在不同的PLMN内。LOCALINTERNATIONAL：国际本网。表示用户漫游地VLR和用户HLR不在同一个国家，但在相同的PLMN内。CROSSINTERNATIONAL：国际跨网。表示用户漫游地VLR和用户归属HLR不在同一个国家，也不在同一个PLMN内。 默认值：无。                                                                                                  |
| VLRPREFIX     | VLR号码前缀 | 用于标识具有相同号码前缀的VLR。VLR号码前缀支持最大匹配和精确匹配，即可以输入具有相同前缀的一组VLR号码的前缀，也可以输入一个VLR号码。 取值范围：1～15位十进制数字组成的字符串。 默认值：无。                                                                                                                                                                                                                                                                                                                                |
| SCPADDR       | SCP地址   | 用于标识接入gsmSCF功能实体的地址。 取值范围：采用E.164编码方式，15位以内的十进制数字组成的字符串。 编码格式为：CC+NDC+LSP，例如，一个典型的“SCP地址”为：“86-139-00777”。各关键字段的含义是： CC（Country Code）：国家码，即SCP所处国家在国际PSTN编号计划中的国家码，它由ITU-T在全球范围内统一分配，其最大长度为3位。例如，中国的国家码为86、英国的国家码为44等。NDC（National Destination Code）：国内目的码，即移动业务接入码，它是由本国电信主管部门在本国范围内统一分配的PLMN网络号，其最大长度为3位。例如，某运营商使用的PLMN网络号为134～139。LSP（Locally Significant Part）：本地有效部分，它是由某个运营商在本PLMN网络运营范围内统一分配的、用于具体代表某个SCP的号码，其最大长度为10位。 默认值：无。 |
| SK            | 业务键     | 用于标识用户在gsmSCF中签约的CAMEL业务。gsmSSF（GSM Service Switching Function）将业务键发给gsmSCF后，gsmSCF根据该业务键执行对应的业务逻辑。业务键是HLR与SCP的对接参数之一，用于在CAP/INAP消息中唯一标识一种智能业务，它是一种号码资源，需要由运营商向本国的电信主管部门申请获得。 取值范围：0～2147483647 默认值：无。                                                                                                                                                                                                                                |
| DEFCALL       | 缺省呼叫处理  | 用于标识当gsmSSF与gsmSCF之间的对话出现差错时或者呼叫受限于gsmSSF里的CallGap时，缺省呼叫处理指示出对呼叫应给予释放还是继续。 取值范围： RELEASECALL：gsmSCF指示gsmSSF释放呼叫。CONTINUECALL：gsmSCF指示gsmSSF继续呼叫。 默认值：无。                                                                                                                                                                                                                                                                               |
| NETTYPE       | 网络类型    | 用于标识用户使用该SCP地址模板时所指定的网络是否支持VoLTE。 取值范围：VoLTE：支持VoLTE。NON_VoLTE：不支持VoLTE。ALL：支持所有网络。 默认值：无。 说明：若不输入该参数，则默认为“ALL”。                                                                                                                                                                                                                                                                                                                      |

## 使用实例

当用户漫游到不同的网络位置时，通过O-CSI业务进行SCP数据的定制下发。数据配置过程如下：

1. 增加SCP地址模板，“HLR序列号”为“1”，“模板号”为“1”，“CAMEL版本”为“PHASE1”，“使用范围”为“LOCALDOMESTIC”，“SCP地址”为“8613911111”，“业务键”为“56”，“缺省呼叫处理”为“RELEASECALL”。命令如下：

   ```
   ADD SCPTPL: HLRSN=1, TPLID=1, CAMEL=PHASE1, AVAILABLEPLMN=LOCALDOMESTIC, SCPADDR="8613911111", SK=56, DEFCALL=RELEASECALL;
   ```
2. 增加O-CSI模板数据记录，“HLR序列号”为“1”，“模板ID”为“2”，“模板名”为“OCSI1”，“CAMEL业务处理能力”为“PHASE3”，“DP值”为“COLLECTINFO”，“SCP地址”为“8613911111”，“业务键”为“11”，“缺省呼叫处理”为“continueCall”，“SCP地址模板ID”为“1”，VLR/MSC和GMSC的处理方式均采用参数表中第一项，命令如下：

   ```
   ADD OCSITPL: HLRSN=1, TPLID=2, TPLNAME="OCSI1", CAMEL=PHASE3, DP=COLLECTINFO, GSMSCFADD="8613911111", SK=11, DEFCALL=continueCall, WITHROAMAGRE_SUPCAMEL=ReturnO-CSI, WITHOUTROAMAGRE_SUPCAMEL=AllowLocationUpdateWithMOCall, HPLMNROAM_SUPCAMEL=ReturnO-CSI, WITHROAMAGRE_SUPLPCAMEL=ReturnLPO-CSI, WITHOUTROAMAGRE_SUPLPCAMEL=ReturnLPO-CSI, HPLMNROAM_SUPLPCAMEL=AllowLocationUpdateWithMOCall, WITHROAMAGRE_NOTSUPCAMEL=AllowLocationUpdateWithMOCall, WITHOUTROAMAGRE_NOTSUPCAMEL=AllowLocationUpdateWithMOCall, HPLMNROAM_NOTSUPCAMEL=AllowLocationUpdateWithMOCall, WITHROAMAGRE_SUPHPCAMEL=NoProcess, WITHINTERAGRE_SUPCAMEL=ReturnO-CSI, WITHOUTINTERAGRE_SUPCAMEL=ReturnBAIC, HPLMNINTER_SUPCAMEL=ReturnO-CSI, WITHINTERAGRE_SUPLPCAMEL=ReturnLPO-CSI, WITHOUTINTERAGRE_SUPLPCAMEL=ReturnBAIC, HPLMNINTER_SUPLPCAMEL=ReturnLPO-CSI, WITHINTERAGRE_NOTSUPCAMEL=AllowMTCall, WITHOUTINTERAGRE_NOTSUPCAMEL=ReturnBAIC, HPLMNINTER_NOTSUPCAMEL=AllowMTCall, SCP_TPLID=1;
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释     | 原因分析                                                                                              | 处理建议                                                                                                                                                           |
|:--------|:----------|:--------------------------------------------------------------------------------------------------|:---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ERR1010 | 参数冲突      | “VLR号码前缀”输入时，同时输入了“使用范围”或“网络类型”。                                                                  | 根据实际情况，确保输入“VLR号码前缀”时，不输入“使用范围”或“网络类型”。                                                                                                                        |
| ERR3004 | 模板已存在     | “模板ID”在数据库中已存在。                                                                                   | 根据实际情况，重新输入参数，确保输入的“模板ID”和系统中已存在的不重复。可执行LST SCPTPL命令查询系统中已存在的模板ID。                                                                                             |
| ERR3047 | 超过最大限制    | 可能原因为如下之一：增加的SCP地址模板记录数超过3000条。 系统中所有SCP地址模板增加的“Camel版本”记录数超过3000条。所有SCP地址模板增加的“SCP地址”记录数超过5000条。 | 根据实际情况，如需增加SCP地址模板，处理步骤如下：执行LST SCPTPL命令，查询已存在的SCP地址模板。执行RMV SCPTPL命令，删除不必要的SCP地址模板。或执行MOD SCPTPL命令，删除不必要的Camel版本/SCP地址。执行该命令增加SCP地址模板，确保增加的SCP地址模板记录数在规定范围之内。 |
| ERR3097 | HLR序列号未定义 | “HLR序列号”未定义。                                                                                      | 根据实际情况，重新输入“HLR序列号”的取值，确保其取值符合要求。                                                                                                                              |