# 增加CAMEL能力模板(ADD CAMELCAPTPL)

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

此操作用于增加CAMEL能力配置模板。

## 注意事项

系统中增加的CAMEL能力模板记录数不能超过3000条。

## 参数说明

| 参数标识         | 参数名称          | 参数说明                                                                                                                         |
|:-------------|:--------------|:-----------------------------------------------------------------------------------------------------------------------------|
| HLRSN        | HLR序列号        | HLR序列号。 取值范围：1～255。 说明： 在PGW支持容灾功能或虚拟HLR功能时设置。                                                                               |
| TPLID        | 模板ID          | 模板ID。 取值范围：0～65534。                                                                                                          |
| TPLNAME      | 模板名           | 模板名称，为1～60个字母或数字组成的字符串。                                                                                                      |
| SUPPORTPHASE | 网元CAMEL支持能力   | 指示网元的CAMEL支持能力。 取值范围： PHASE1：支持CAMEL phase 1PHASE2：支持CAMEL phase 2PHASE3：支持CAMEL phase 3PHASE4：支持CAMEL phase 4 说明：该参数暂时不使用。  |
| O_CSI        | O_CSI支持能力     | 此参数用于说明VLR/SGSN对O-CSI业务的支持能力。 取值范围： PHASE1：支持CAMEL phase 1PHASE2：支持CAMEL phase 2PHASE3：支持CAMEL phase 3PHASE4：支持CAMEL phase 4 |
| T_CSI        | T_CSI支持能力     | 此参数用于说明VLR/SGSN对T-CSI业务的支持能力。 取值范围： PHASE1：支持CAMEL phase 1PHASE2：支持CAMEL phase 2PHASE3：支持CAMEL phase 3PHASE4：支持CAMEL phase 4 |
| SS_CSI       | SS_CSI支持能力    | 此参数用于说明VLR/SGSN对SS-CSI业务的支持能力。 取值范围： PHASE2：支持CAMEL phase 2PHASE3：支持CAMEL phase 3PHASE4：支持CAMEL phase 4                      |
| VT_CSI       | VT_CSI支持能力    | 此参数用于说明VLR/SGSN对VT-CSI业务的支持能力。 取值范围： PHASE3：支持CAMEL phase 3PHASE4：支持CAMEL phase 4UNSUPPORTED：不支持VT-CSI业务                     |
| D_CSI        | D_CSI支持能力     | 此参数用于说明VLR/SGSN对D-CSI业务的支持能力。 取值范围： PHASE3：支持CAMEL phase 3PHASE4：支持CAMEL phase 4                                             |
| SMS_CSI      | SMS_CSI支持能力   | 此参数用于说明VLR/SGSN对SMS-CSI业务的支持能力。 取值范围： PHASE3：支持CAMEL phase 3PHASE4：支持CAMEL phase 4                                           |
| M_CSI        | M_CSI支持能力     | 此参数用于说明VLR/SGSN对M-CSI业务的支持能力。 取值范围： PHASE3：支持CAMEL phase 3PHASE4：支持CAMEL phase 4                                             |
| GPRS_CSI     | GPRS_CSI支持能力  | 此参数用于说明VLR/SGSN对GPRS-CSI业务的支持能力。 取值范围： PHASE3：支持CAMEL phase 3PHASE4：支持CAMEL phase 4                                          |
| MTSMS_CSI    | MTSMS_CSI支持能力 | 此参数用于说明VLR/SGSN对MTSMS-CSI业务的支持能力。 取值范围： PHASE4：支持CAMEL phase 4                                                               |

## 使用实例

为虚拟HLR1增加模板ID为“1”，模板名称为“CAMELCAPTPL1”，O-CSI业务支持能力为“PHASE1”的CAMEL能力配置模板，命令如下：

ADD CAMELCAPTPL:HLRSN=1, TPLID=1, TPLNAME="CAMELCAPTPL1", O\_CSI=PHASE1;

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释   | 原因分析                    | 处理建议                                                                                                                                           |
|:--------|:--------|:------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------|
| ERR3047 | 超过最大限制  | 增加的CAMEL能力模板记录数超过3000条。 | 根据实际情况，如需增加CAMEL能力模板，处理步骤如下：执行LST CAMELCAPTPL命令，查询已存在的CAMEL能力模板。执行RMV CAMELCAPTPL命令，删除不必要的CAMEL能力模板。执行该命令增加CAMEL能力模板，确保增加的CAMEL能力模板记录数在规定范围之内。 |