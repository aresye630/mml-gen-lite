# 增加CAMEL查询模板(ADD CAMELINTERTPL)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

该命令用于在HLR中增加支持CAMEL（Customized Applications for Mobile network Enhanced Logic）查询协议的GMSC（Gateway Mobile Switching Center）号码前缀。

当需要限制用户在某些GMSC区域内使用CAMEL业务时，操作员可以先通过该命令预先设置GSMC号码前缀（通过该命令将GMSC的号码前缀添加到CAMEL查询协议模板中，就认为该GMSC与HLR有CAMEL查询协议），然后通过**ADD OCSITPL**和**ADD TCSITPL**命令设置CAMEL业务的支持能力，包括与某GMSC是否有CAMEL查询协议。对于已签约O-CSI和T-CSI业务的用户，HLR在进行CAMEL业务处理时，根据SRI请求消息带上的GMSC地址，结合系统配置的CAMEL查询协议表来确定GMSC与HLR是否有CAMEL查询协议，根据支持能力下发相应的CAMEL业务规则。

## 注意事项

同一个“HLR序列号”中增加的CAMEL查询模板记录数不能超过2000条，且系统中所有CAMEL查询模板增加的GMSC号码前缀总记录数不能超过5000条。

## 参数说明

| 参数标识    | 参数名称     | 参数说明                                                    |
|:--------|:---------|:--------------------------------------------------------|
| HLRSN   | HLR序列号   | 用于标识一个HLR序列号。该参数必须先由ADD HLRSN命令定义，然后才能在此处引用。            |
| TPLID   | 模板ID     | 用于标识待增加模板在系统中的序号。 取值范围：0～65534 默认值：无。                   |
| TPLNAME | 模板名      | 用于标识CAMEL查询协议模板的名称。 取值范围：1～60个字母或十进制数字组成的字符串。 默认值：无。    |
| GMSCNP  | GMSC号码前缀 | 用于标识支持CAMEL查询协议的GMSC号码前缀。 取值范围：1～15位十进制数字组成的字符串。 默认值：无。 |

## 使用实例

为用户签约CAMEL查询协议模板操作员需要配置以下数据。

1. 增加CAMEL查询协议模板。“HLR序列号”为“1”，“模板ID”为“3”，“模板名”为“CAMELINTERTPL”，“GMSC号码前缀”为“12345678912”：

   ```
   ADD CAMELINTERTPL: HLRSN=1, TPLID=3, TPLNAME="CAMELINTERTPL", GMSCNP="12345678912";
   ```
2. 执行**ADD OCSITPL**命令增加O-CSI模板，关联CAMEL查询协议模板。在“HLR序列号”为“1”的HLR上增加一条O-CSI模板数据记录。其中，“模板ID”为“2”，“CAMEL业务处理能力”为“PHASE3”，“DP值”为“COLLECTINFO”，“SCP地址”为“8613911111”，“业务键”为“11”，“缺省呼叫处理”为“continueCall”，VLR/MSC和GMSC的处理方式均采用参数表中第一项，“CAMEL查询模板ID”为“3”：

   ```
   ADD OCSITPL: HLRSN=1, TPLID=2, CAMEL=PHASE3, DP=COLLECTINFO, GSMSCFADD="8613911111", SK=11, DEFCALL=continueCall, WITHROAMAGRE_SUPCAMEL=ReturnO-CSI, WITHOUTROAMAGRE_SUPCAMEL=ReturnO-CSI, HPLMNROAM_SUPCAMEL=ReturnO-CSI, WITHROAMAGRE_SUPLPCAMEL=ReturnLPO-CSI, WITHOUTROAMAGRE_SUPLPCAMEL=ReturnLPO-CSI, HPLMNROAM_SUPLPCAMEL=ReturnLPO-CSI, WITHROAMAGRE_NOTSUPCAMEL=AllowLocationUpdateWithMOCall, WITHOUTROAMAGRE_NOTSUPCAMEL=AllowLocationUpdateWithMOCall, HPLMNROAM_NOTSUPCAMEL=AllowLocationUpdateWithMOCall, WITHROAMAGRE_SUPHPCAMEL=NoProcess, WITHINTERAGRE_SUPCAMEL=ReturnO-CSI, WITHOUTINTERAGRE_SUPCAMEL=ReturnO-CSI, HPLMNINTER_SUPCAMEL=ReturnO-CSI, WITHINTERAGRE_SUPLPCAMEL=ReturnLPO-CSI, WITHOUTINTERAGRE_SUPLPCAMEL=ReturnLPO-CSI, HPLMNINTER_SUPLPCAMEL=ReturnLPO-CSI, WITHINTERAGRE_NOTSUPCAMEL=AllowMTCall, WITHOUTINTERAGRE_NOTSUPCAMEL=AllowMTCall, HPLMNINTER_NOTSUPCAMEL=AllowMTCall, CAMELINTERTPL=3;
   ```
3. 执行**MOD OCSI**命令给用户签约O-CSI业务。

   ```
   MOD OCSI: IMSI="460000009123457", PROV=TRUE, TPLID=2;
   ```

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释   | 原因分析                                                                              | 处理建议                                                                                                                                                                                     |
|:--------|:--------|:----------------------------------------------------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ERR3007 | 记录不存在   | “HLR序列号”未定义。                                                                      | 根据实际情况，重新输入“HLR序列号”的取值，确保其取值符合要求。                                                                                                                                                        |
| ERR1004 | 无效的参数值  | 界面输入的非“HLR序列号”参数不在相应的参数取值范围内。                                                     | 根据实际情况，重新输入提示错误的参数的取值，确保其取值符合要求。                                                                                                                                                         |
| ERR3004 | 模板已存在   | “模板ID”在数据库中已存在。                                                                   | 根据实际情况，重新输入参数，确保输入的“模板ID”和系统中已存在的不重复。可执行LST CAMELINTERTPL命令查询系统中已存在的CAMEL查询协议模板。                                                                                                         |
| ERR3047 | 超过最大限制  | 可能原因为如下之一：同一个“HLR序列号”中增加的CAMEL查询模板记录数超过2000条。所有CAMEL查询模板增加的“GMSC号码前缀”总记录数超过5000条。 | 根据实际情况，如需增加CAMEL查询模板，处理步骤如下：执行LST CAMELINTERTPL命令，查询已存在的CAMEL查询模板。执行RMV CAMELINTERTPL命令，删除不必要的CAMEL查询模板。或执行MOD CAMELINTERTPL命令，删除不必要的GMSC号码前缀。执行该命令增加CAMEL查询模板，确保增加的CAMEL查询模板记录数在规定范围之内。 |