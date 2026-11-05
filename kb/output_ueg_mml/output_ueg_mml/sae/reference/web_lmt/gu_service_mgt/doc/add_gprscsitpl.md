# 增加GPRS-CSI模板(ADD GPRSCSITPL)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于为HLR在配置数据库中增加一条GPRS-CSI（GPRS CAMEL Subscription Information）模板数据记录，根据运营商CAMEL网络的实际情况进行配置，相关参数由运营商提供。用户通过签约GPRS-CSI模板ID签约GPRS-CSI特性。

CAMEL的发展经历了四个阶段，不同的阶段CAMEL特性的应用范围不同，GPRS-CSI是CAMEL PHASE 3中的一个CAMEL签约项，是CAMEL支持GPRS网络的基础。HLR管理和存储GPRS-CSI签约信息，并在用户进行位置更新时下发给SGSN，当SGSN处理涉及CAMEL的GPRS业务时，SGSN监视所有的GPRS事件，当触发CAMEL业务时SGSN使用位置更新中收到的GPRS-CSI签约信息用内部接口向gprsSSF（GSM Service Switching Function）请求指示，使gprsSSF可以控制SGSN中的GPRS业务处理，按照用户签约的GPRS-CSI模板中的信息进行业务逻辑处理。

## 注意事项

- 该命令只能给一个模板增加一个DP值，如果需要增加多个DP值，请执行**MOD GPRSCSITPL**命令。
- 同一个“HLR序列号”中增加的GPRS-CSI模板记录数不能超过5000条。

## 参数说明

| 参数标识           | 参数名称               | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                |
|:---------------|:-------------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HLRSN          | HLR序列号             | 用于标识一个HLR序列号。该参数必须先由ADD HLRSN命令定义，然后才能在此处引用。                                                                                                                                                                                                                                                                                                                                                                                        |
| TPLID          | 模板ID               | 用于标识待增加模板在系统中的序号。 取值范围：0～65534 默认值：无。                                                                                                                                                                                                                                                                                                                                                                                               |
| TPLNAME        | 模板名                | 用于标识待增加模板在系统中的名称。 取值范围：1～60位字母或十进制数字组成的字符串。 默认值：无。                                                                                                                                                                                                                                                                                                                                                                                  |
| CAMEL          | CAMEL业务处理能力        | 用于标识gsmSCF（GSM Service Control Function）在处理该项具体CAMEL业务时所需要的CAMEL协议阶段的支持。 取值范围：PHASE3，CAMEL特性应用于GPRS会话中。 默认值：无。                                                                                                                                                                                                                                                                                                                      |
| USHNDL         | SGSN不支持CAMEL时的处理方式 | 用于标识当SGSN不支持GRPS-CSI所需要的CAMEL业务处理能力时HLR替代下发的处理方式。 取值范围：CALLBAR：呼叫闭锁，与签约了ODB-BAOC（闭锁所有呼出业务）相同。RR：漫游限制。NONCAMEL：业务流程被当作非CAMEL业务继续处理。 默认值：无。                                                                                                                                                                                                                                                                                           |
| DP             | DP值                | 用于标识触发GPRS-CSI业务的检出点，GPRS-CSI没有定义触发准则，只要在DP点上检测到该DP点对应的GPRS事件，就可以触发到智能网元的处理。 取值范围：ATTACH：又称TDP1，MS请求附着在GPRS网络时触发GPRS-CSI。ATTACHCHGPOS：又称TDP2，附着在GPRS网上的MS更换到其它SGSN时触发GPRS-CSI。PDPCNTXEST：又称TDP11，MS请求激活PDP上下文时触发GPRS-CSI。PDPCNTXESTACK：又称TDP12，SGSN已经收到了GGSN发来的PDP上下文激活确认消息。PDPCNTXCHGPOS：又称TDP14，PDP上下文激活的用户更换位置到其它SGSN（路由区更新）触发GPRS-CSI。 默认值：无。                                                                                   |
| GSMSCFADD      | SCP地址              | 用于标识接入gsmSCF功能实体的地址。 取值范围：1～15位十进制数字组成的字符串。 采用E.164编码方式，编码格式为：CC+NDC+LSP，例如，一个典型的“SCP地址”为：“86-139-00777”。各关键字段的含义是： CC（Country Code）：国家码，即SCP所处国家在国际PSTN编号计划中的国家码，它由ITU-T在全球范围内统一分配，其最大长度为3位。例如，中国的国家码为86、英国的国家码为44等。NDC（National Destination Code）：国内目的码，即移动业务接入码，它是由本国电信主管部门在本国范围内统一分配的PLMN网络号，其最大长度为3位。例如，某运营商使用的PLMN网络号为134～139。LSP（Locally Significant Part）：本地有效部分，它是由某个运营商在本PLMN网络运营范围内统一分配的、用于具体代表某个SCP的号码，其最大长度为9位。 默认值：无。 |
| SK             | 业务键                | 用于标识用户在gsmSCF中签约的CAMEL业务。gprsSSF将业务键发给gsmSCF后，gsmSCF根据该业务键执行对应的业务逻辑。业务键是HLR与SCP的对接参数之一，用于在CAP/INAP消息中唯一标识一种智能业务，它是一种号码资源，需要由运营商向本国的电信主管部门申请获得。 取值范围：0～2147483647 默认值：无。                                                                                                                                                                                                                                                             |
| DEFGPRS        | 缺省GPRS处理           | 用于标识当gprsSSF与gsmSCF之间的对话出现异常时，GPRS会话或PDP（Packet Data Protocol）上下文将被释放还是继续。 取值范围：ReleaseTransaction：释放ContinueTransaction：继续 默认值：无。                                                                                                                                                                                                                                                                                                  |
| AVAILABLE_PLMN | GPRS-CSI模板使用范围     | 用于标识用户在不同的网络中漫游时是否下发GPRS-CSI数据。 取值范围：HPLMN：用户在HPLMN（Home Public Land Mobile Network）内漫游时，HLR向SGSN下发GPRS-CSI，否则不下发。FPLMN：用户在FPLMN（Forbidden PLMN）内漫游时，HLR向SGSN下发GPRS-CSI，否则不下发。INTERNATIONAL：用户漫游出本国时，HLR向SGSN下发GPRS-CSI，否则不下发。HPLMNC：用户在本国漫游时，HLR向SGSN下发GPRS-CSI，否则不下发。ALL_PLMN：用户在所有PLMN内漫游时，HLR均向SGSN下发GPRS-CSI。NOT_AVAILABLE：HLR不向SGSN下发GPRS-CSI。 默认值：无。 说明：执行该命令并且不输入该参数时，系统会设置初始值ALL_PLMN。                                     |

## 使用实例

在“HLR序列号”为“1”的HLR上增加一条GPRS-CSI模板数据记录。其中，“模板ID”为“5”，“模板名称”为“GPRSCSITPL”，“CAMEL业务处理能力”为“PHASE3”，“SGSN不支持CAMEL时的处理方式”为“RR”，“DP值”为“ATTACH”，“SCP地址”为“8613908”，“业务键”为“129”，“缺省GPRS处理”为“ContinueTransaction”：

```
ADD GPRSCSITPL: HLRSN=1, TPLID=5, TPLNAME="GPRSCSITPL", CAMEL=PHASE3, USHNDL=RR, DP=ATTACH, GSMSCFADD="8613908", SK=129, DEFGPRS=ContinueTransaction;
```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释   | 原因分析                                 | 处理建议                                                                                                                                              |
|:--------|:--------|:-------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------|
| ERR3007 | 记录不存在   | “HLR序列号”未定义。                         | 根据实际情况，重新输入“HLR序列号”的取值，确保其取值符合要求。                                                                                                                 |
| ERR1004 | 无效的参数值  | 界面输入的非“HLR序列号”参数不在相应的参数取值范围内。        | 根据实际情况，重新输入提示错误的参数的取值，确保其取值符合要求。                                                                                                                  |
| ERR3004 | 模板已存在   | 本次操作输入的“模板ID”在数据库中已存在。               | 根据实际情况，重新输入参数，确保输入的“模板ID”和系统中已存在的不重复。可执行LST GPRSCSITPL命令查询系统中已存在的GPRS-CSI模板。                                                                      |
| ERR3047 | 超过最大限制  | 同一个“HLR序列号”中增加的GPRS-CSI模板记录数超过5000条。 | 根据实际情况，如需增加GPRS-CSI模板，处理步骤如下：执行LST GPRSCSITPL命令，查询已存在的GPRS-CSI模板。执行RMV GPRSCSITPL命令，删除不必要的GPRS-CSI模板。执行该命令增加GPRS-CSI模板，确保增加的GPRS-CSI模板记录数在规定范围之内。 |