# 修改GPRS-CSI模板(MOD GPRSCSITPL)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

**须知** 

本命令属于高危命令，执行不当会使签约此模板的用户数据被同步修改，因此执行该命令前，需要与华为技术支持确认后才可以实施。

该命令用于对一条GPRS-CSI（GPRS CAMEL Subscription Information）模板数据记录的某些参数进行修改或调整，同时还用于为一条GPRS-CSI模板数据记录增加多个DP值。在该命令中，系统通过以下关键参数的组合来唯一标识一条GPRS-CSI模板数据记录：

- “HLR序列号”
- “模板ID”

## 注意事项

- 用户进行位置更新或触发其他涉及GPRS-CSI模板的流程时，系统会根据用户签约的GPRS-CSI模板ID下发模板中的数据，修改模板数据会使签约此模板的用户数据被同步修改，会影响在网用户，因此现网执行修改模板操作时需要慎重。
- “是否提供DP值”和“DP值”两个参数必须同时输入。
- 当“是否提供DP值”参数为“TRUE”、但指定的DP值在模板中不存在时，“SCP地址”、“业务键”和“缺省GPRS处理”参数是必选参数。
- 系统中同一个GPRS-CSI模板增加的DP值记录数不能超过20条，且所有GPRS-CSI模板增加的DP值总记录数不能超过5000条。

## 参数说明

| 参数标识           | 参数名称               | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|:---------------|:-------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HLRSN          | HLR序列号             | 标识一条GPRS-CSI模板数据记录的关键字段之一（其取值不能被修改），用于标识需要对哪一条GPRS-CSI模板数据记录的参数进行修改或调整，操作员可以使用LST HLRSN命令查询获得。                                                                                                                                                                                                                                                                                                                                                               |
| TPLID          | 模板ID               | 标识一条GPRS-CSI模板数据记录的关键字段之一（其取值不能被修改），用于标识需要对哪一条GPRS-CSI模板数据记录的参数进行修改或调整，操作员可以使用LST GPRSCSITPL命令查询获得。                                                                                                                                                                                                                                                                                                                                                          |
| TPLNAME        | 模板名                | 用于标识待修改模板在系统中的名称。 取值范围：1～60位字母或十进制数字组成的字符串。 默认值：无。                                                                                                                                                                                                                                                                                                                                                                                                           |
| CAMEL          | CAMEL业务处理能力        | 用于标识gsmSCF（GSM Service Control Function）在处理该项具体CAMEL业务时所需要的CAMEL协议阶段的支持。 取值范围：PHASE3，CAMEL特性应用于GPRS会话中。 默认值：无。                                                                                                                                                                                                                                                                                                                                               |
| USHNDL         | SGSN不支持CAMEL时的处理方式 | 用于标识当SGSN不支持GRPS-CSI所需要的CAMEL业务处理能力时HLR替代下发的处理方式。 取值范围：CALLBAR：呼叫闭锁，与签约了ODB-BAOC（闭锁所有呼出业务）相同。RR：漫游限制。NONCAMEL：业务流程被当作非CAMEL业务继续处理。 默认值：无。                                                                                                                                                                                                                                                                                                                    |
| PROV           | 是否提供DP值            | 用于标识执行该命令是增加/修改还是删除DP数据。如果待修改模板中只设置了一个DP值，该参数不能设置为FALSE。 取值范围：TRUE：增加/修改如果指定的DP值在模板中不存在，则与该DP值对应的数据将被增加到模板中。 FALSE：删除如果指定的DP值已经存在，与指定的DP值相关的数据将被删除。如果指定的DP值在模板中不存在，系统将会提示错误。 默认值：无。                                                                                                                                                                                                                                                                          |
| DP             | DP值                | 仅当本命令中的“是否提供DP值”参数为“TRUE”或“FALSE”时该参数有效。用于标识触发GPRS-CSI业务的检出点，GPRS-CSI没有定义触发准则，只要在DP点上检测到该DP点对应的GPRS事件，就可以触发到智能网元的处理。 取值范围：ATTACH：又称TDP1，MS请求附着在GPRS网络时触发GPRS-CSI。ATTACHCHGPOS：又称TDP2，附着在GPRS网上的MS更换到其它SGSN时触发GPRS-CSI。PDPCNTXEST：又称TDP11，MS请求激活PDP上下文时触发GPRS-CSI。PDPCNTXESTACK：又称TDP12，SGSN已经收到了GGSN发来的PDP上下文激活确认消息。PDPCNTXCHGPOS：又称TDP14，PDP上下文激活的用户更换位置到其它SGSN（路由区更新）触发GPRS-CSI。 默认值：无。                                                                    |
| GSMSCFADD      | SCP地址              | 仅当本命令中的“是否提供DP值”参数为“TRUE”时该参数有效。用于标识接入gsmSCF功能实体的地址。 取值范围：采用E.164编码方式，其最大长度为15位。 编码格式为：CC+NDC+LSP，例如，一个典型的“SCP地址”为：“86-139-00777”。各关键字段的含义是： CC（Country Code）：国家码，即SCP所处国家在国际PSTN编号计划中的国家码，它由ITU-T在全球范围内统一分配，其最大长度为3位。例如，中国的国家码为86、英国的国家码为44等。NDC（National Destination Code）：国内目的码，即移动业务接入码，它是由本国电信主管部门在本国范围内统一分配的PLMN网络号，其最大长度为3位。例如，某运营商使用的PLMN网络号为134～139。LSP（Locally Significant Part）：本地有效部分，它是由某个运营商在本PLMN网络运营范围内统一分配的、用于具体代表某个SCP的号码，其最大长度为9位。 默认值：无。 |
| SK             | 业务键                | 仅当本命令中的“是否提供DP值”参数为“TRUE”时该参数有效。用于标识用户在gsmSCF中签约的CAMEL业务。gprsSSF（GSM Service Switching Function）将业务键发给gsmSCF后，gsmSCF根据该业务键执行对应的业务逻辑。业务键是HLR与SCP的对接参数之一，用于在CAP/INAP消息中唯一标识一种智能业务，它是一种号码资源，需要由运营商向本国的电信主管部门申请获得。 取值范围：0～2147483647 默认值：无。                                                                                                                                                                                                                      |
| DEFGPRS        | 缺省GPRS处理           | 仅当本命令中的“是否提供DP值”参数为“TRUE”时该参数有效。用于标识当gprsSSF与gsmSCF之间的对话出现异常时，GPRS会话或PDP（Packet Data Protocol）上下文将被释放还是继续。 取值范围：ReleaseTransaction：释放ContinueTransaction：继续 默认值：无。                                                                                                                                                                                                                                                                                           |
| AVAILABLE_PLMN | GPRS-CSI模板使用范围     | 用于标识用户在不同的网络中漫游时是否下发GPRS-CSI数据。 取值范围：HPLMN：用户在HPLMN（Home Public Land Mobile Network）内漫游时，HLR向SGSN下发GPRS-CSI，否则不下发。FPLMN：用户在FPLMN（Forbidden PLMN）内漫游时，HLR向SGSN下发GPRS-CSI，否则不下发。INTERNATIONAL：用户漫游出本国时，HLR向SGSN下发GPRS-CSI，否则不下发。HPLMNC：用户在本国漫游时，HLR向SGSN下发GPRS-CSI，否则不下发。ALL_PLMN：用户在所有PLMN内漫游时，HLR均向SGSN下发GPRS-CSI。NOT_AVAILABLE：HLR不向SGSN下发GPRS-CSI。 默认值：无。                                                                                                  |

## 使用实例

1. 修改“HLR序列号”为“1”的HLR的GPRS-CSI模板数据记录，增加一个DP值。其中，“模板ID”为“2”，“SGSN不支持CAMEL时的处理方式”为“NONCAMEL”，“是否提供DP值”为“TRUE”，“DP值”为“ATTACH”，“SCP地址”为“86138”，“业务键”为“1”，“缺省GPRS处理”为“ReleaseTransaction”：

   ```
   MOD GPRSCSITPL: HLRSN=1, TPLID=2, USHNDL=NONCAMEL, PROV=TRUE, DP=ATTACH, GSMSCFADD="86138", SK=1, DEFGPRS=ReleaseTransaction;
   ```
2. 修改“HLR序列号”为“1”的HLR的GPRS-CSI模板数据记录，修改GPRS-CSI模板使用范围。其中，“模板ID”为“5”，“GPRS-CSI模板使用范围”为“HPLMN”：

   ```
   MOD GPRSCSITPL: HLRSN=1, TPLID=5, AVAILABLE_PLMN=HPLMN;
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释   | 原因分析                                                                   | 处理建议                                                                                          |
|:--------|:--------|:-----------------------------------------------------------------------|:----------------------------------------------------------------------------------------------|
| ERR3003 | 模板未定义   | “HLR序列号”和“模板ID”对应的GPRS-CSI模板数据记录不存在。                                   | 使用LST GPRSCSITPL命令查询后，重新确认要修改哪个“HLR序列号”和“模板ID”对应的GPRS-CSI模板数据记录。                              |
| ERR3047 | 超过最大限制  | 可能原因为如下之一：同一个“模板ID”增加的“DP值”数据记录数超过20条。所有GPRS-CSI模板增加的“DP值”总记录数超过5000条。 | 根据实际情况，如需增加DP值，处理步骤如下：执行LST GPRSCSITPL命令，查询已存在的DP值。执行该命令删除不必要的DP值。执行该命令增加DP值，确保增加的DP值在规定范围之内。 |
| ERR1004 | 无效的参数值  | 界面输入的非“HLR序列号”和“模板ID”参数不在相应的参数取值范围内。                                   | 根据实际情况，重新输入提示错误的参数的取值，确保其取值符合要求。                                                              |