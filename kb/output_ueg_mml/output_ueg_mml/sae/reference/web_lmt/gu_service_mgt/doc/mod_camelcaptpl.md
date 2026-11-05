# 修改CAMEL能力模板(MOD CAMELCAPTPL)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**须知** 

该操作会修改CAMEL能力模板数据，是否继续？

此操作用于修改CAMEL能力配置模版。

## 注意事项

修改CAMEL能力配置模版时，除参数“HLRSN”、“TPLID”、“TPLNAME”外，至少输入一个其它参数才可进行修改操作。

## 参数说明

| 参数标识         | 参数名称          | 参数说明                                                                                                                                       |
|:-------------|:--------------|:-------------------------------------------------------------------------------------------------------------------------------------------|
| HLRSN        | HLR序列号        | HLR序列号。 取值范围：1～255。 说明：在PGW支持容灾功能或虚拟HLR功能时设置。                                                                                              |
| TPLID        | 模板ID          | CAMELCAP模板ID。 取值范围：0～65534。                                                                                                                |
| TPLNAME      | 模板名           | CAMELCAP模板名称，为1～60个字母或数字组成的字符串。                                                                                                            |
| SUPPORTPHASE | 网元CAMEL支持能力   | 指示网元的CAMEL支持能力。 取值范围： UNRESTRICT：不限制PHASE1：支持CAMEL phase 1PHASE2：支持CAMEL phase 2PHASE3：支持CAMEL phase 3PHASE4：支持CAMEL phase 4 说明：该参数暂时不使用。  |
| O_CSI        | O_CSI支持能力     | 此参数用于说明VLR/SGSN对O-CSI业务的支持能力。 取值范围： UNRESTRICT：不限制PHASE1：支持CAMEL phase 1PHASE2：支持CAMEL phase 2PHASE3：支持CAMEL phase 3PHASE4：支持CAMEL phase 4 |
| T_CSI        | T_CSI支持能力     | 此参数用于说明VLR/SGSN对T-CSI业务的支持能力。 取值范围： UNRESTRICT：不限制PHASE1：支持CAMEL phase 1PHASE2：支持CAMEL phase 2PHASE3：支持CAMEL phase 3PHASE4：支持CAMEL phase 4 |
| SS_CSI       | SS_CSI支持能力    | 此参数用于说明VLR/SGSN对SS-CSI业务的支持能力。 取值范围： UNRESTRICT：不限制PHASE2：支持CAMEL phase 2PHASE3：支持CAMEL phase 3PHASE4：支持CAMEL phase 4                      |
| VT_CSI       | VT_CSI支持能力    | 此参数用于说明VLR/SGSN对VT-CSI业务的支持能力。 取值范围： UNRESTRICT：不限制PHASE3：支持CAMEL phase 3PHASE4：支持CAMEL phase 4UNSUPPORTED：不支持VT-CSI业务                     |
| D_CSI        | D_CSI支持能力     | 此参数用于说明VLR/SGSN对D-CSI业务的支持能力。 取值范围： UNRESTRICT：不限制PHASE3：支持CAMEL phase 3PHASE4：支持CAMEL phase 4                                             |
| SMS_CSI      | SMS_CSI支持能力   | 此参数用于说明VLR/SGSN对SMS-CSI业务的支持能力。 取值范围： UNRESTRICT：不限制PHASE3：支持CAMEL phase 3PHASE4：支持CAMEL phase 4                                           |
| M_CSI        | M_CSI支持能力     | 此参数用于说明VLR/SGSN对M-CSI业务的支持能力。 取值范围： UNRESTRICT：不限制PHASE3：支持CAMEL phase 3PHASE4：支持CAMEL phase 4                                             |
| GPRS_CSI     | GPRS_CSI支持能力  | 此参数用于说明VLR/SGSN对GPRS-CSI业务的支持能力。 取值范围： UNRESTRICT：不限制PHASE3：支持CAMEL phase 3PHASE4：支持CAMEL phase 4                                          |
| MTSMS_CSI    | MTSMS_CSI支持能力 | 此参数用于说明VLR/SGSN对MTSMS-CSI业务的支持能力。 取值范围： UNRESTRICT：不限制PHASE4：支持CAMEL phase 4                                                               |

## 使用实例

修改虚拟HLR1上模板ID为“1”、模板名称为“CAMELCAPTPL1”的CAMEL能力配置模板，将其O-CSI业务支持能力设置为“PHASE1”，命令如下：

MOD CAMELCAPTPL:HLRSN=1, TPLID=1, TPLNAME="CAMELCAPTPL1", O\_CSI=PHASE1;