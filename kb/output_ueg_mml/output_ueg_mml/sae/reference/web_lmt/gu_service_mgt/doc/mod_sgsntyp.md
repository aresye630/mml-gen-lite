# 修改SGSN类型数据(MOD SGSNTYP)

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**须知** 

本命令属于高危命令，执行不当会使用户漫游到该SGSN区域后出现位置更新失败，因此执行该命令前，需要与华为技术支持确认后才可以实施。

此操作用于修改SGSN类型。

## 注意事项

该命令不允许进行批操作。

## 参数说明

| 参数标识        | 参数名称                | 参数说明                                                                                                                                                            |
|:------------|:--------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| HLRSN       | HLR序列号              | HLR序列号，有效值域为1～255，在PGW支持容灾功能或虚拟HLR功能时设置。                                                                                                                        |
| SGSNPREFIX  | SGSN号码前缀            | SGSN号码前缀，SGSN号码的前一段，用于标识有相同前缀的SGSN号属性，14位以内的数字。                                                                                                                 |
| NAME        | SGSN名称              | SGSN名称，30个以内的字母或数字组成的字符串，用于标识不同的SGSN。                                                                                                                           |
| TYPE        | SGSN号相对于本HLR所属的网络类型 | 标明此VLR号相对于本HLR所属的网络类型。 取值如下：LOCAL：本地。 LOCALDOMESTIC：国内本网。 CROSSDOMESTIC：国内跨网。 LOCALINTERNATIONAL：国际本网。 CROSSINTERNATIONAL：国际跨网。 LOCALAREA：省内本网。 CROSSAREA：省内跨网。 |
| NCCPROV     | 是否提供NCC模板           | 修改SGSN类型时是否提供NCC模板。 TRUE：提供 FALSE：不提供                                                                                                                           |
| NCCTPL      | NCC模板ID             | 仅当本命令中的“是否提供NCC模板”参数为“TRUE”时该参数有效。NCC模板的ID，取值范围：0～99998。                                                                                                        |
| SERVICETY   | 是否允许签约OKSC业务        | SGSN是否允许签约业务区域限制。 取值范围：PERMISSION：业务允许 RESTRICT：业务限制 缺省值：PERMISSION。                                                                                            |
| PROVCAPTPL  | 是否提供CAMEL能力模板       | 是否提供CAMEL能力模板。 取值范围： TRUE：提供FALSE：不提供 缺省值：FALSE。                                                                                                                |
| CAMELCAPTPL | CAMEL能力模板ID         | 仅当本命令中的“是否提供CAMEL能力模板”参数为“TRUE”时该参数有效。CAMELCAP模板ID。 取值范围：0～65534。                                                                                               |

## 使用实例

修改SGSN类型数据，修改SGSN号码前缀为0091的记录，对应的TYPE为CROSSINTERNATIONAL。命令如下：

MOD SGSNTYP: HLRSN=1, SGSNPREFIX="0091",TYPE=CROSSINTERNATIONAL;