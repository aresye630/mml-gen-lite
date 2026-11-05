# 修改PLMN信息（MOD PLMN）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

此操作用来修改PLMN优选漫游配置。

## 注意事项

- 当VSPROV填充时，必须填充VLRSGSNNO。当VSPROV为TRUE时，若该VLRSGSNNO在数据库中不存在则增加，若存在则不再增加，最多可增加1000个前缀。当VSPROV为FALSE时，为删除该VLRSGSNNO。
- 当IMSIPROV填充时，必须填充IMSI前缀IMSIPREFIX。当IMSIPROV为TRUE时，若在数据库中不存在该IMSIPREFIX，则增加该IMSIPREFIX及相应属性，最多可增加1000个前缀；若已存在该IMSIPREFIX，则修改其对应的IMSIRULE规则。当IMSIPROV为FALSE时，则删除该IMSIPREFIX。
- 整条命令中，对PLMNID、VLRSGSNNO、IMSIPREFIX及各自的参数修改，若有一个修改不成功，则命令执行不成功。如：增加VLRSGSNNO时，修改IMSIRULE的IMSIPREFIX不存在，则整个命令都不会执行，返回记录不存在。
- 系统中同一个PLMN优选漫游配置增加的VLR/SGSN前缀记录数不能超过1000条，且所有PLMN优选漫游配置增加的VLR/SGSN前缀总记录数不能超过5000条。
- 系统中同一个PLMN优选漫游配置增加的IMSI前缀记录数不能超过1000条，且所有PLMN优选漫游配置增加的IMSI前缀总记录数不能超过5000条。

## 参数说明

| 参数标识          | 参数名称         | 参数说明                                                                                           |
|:--------------|:-------------|:-----------------------------------------------------------------------------------------------|
| HLRSN         | HLR序列号       | HLR序列号，在PGW支持容灾功能或虚拟HLR功能时设置。 取值范围：1～255。                                                      |
| PLMNID        | PLMN序列号      | PLMN序列号。 取值范围：0～999。                                                                           |
| DESCRIPTION   | PLMN描述       | PLMN描述。 取值范围：0～60个字符。                                                                          |
| PREFERREDTYPE | 优选漫游方式       | 优选漫游方式。 取值范围： PREFERRED：首选。ALLOWED：允许。RESTRICTED：受限。 缺省值：PREFERRED                             |
| CHECKIMSI     | 按IMSI进行检查    | 是否需要按IMSI检查用户在该PLMN的漫游规则。 取值范围： TRUE：按IMSI检查。FALSE：不按IMSI检查。 缺省值：FALSE                         |
| DEFIMSIRULE   | 默认IMSI检查规则   | 定义在PLMN需要按IMSI检查，但该PLMN没有定义IMSI前缀时的漫游规则。 取值范围： PERMISSION: 允许漫游。RESTRICT: 限制漫游。 缺省值：PERMISSION |
| VSPROV        | 提供VLR/SGSN前缀 | 对VLR/SGSN前缀进行增加和删除操作。 取值范围： TRUE：增加VLR/SGSN前缀。FALSE：删除VLR/SGSN前缀。                              |
| VLRSGSNNO     | VLR/SGSN前缀   | 仅当本命令中的“提供VLR/SGSN前缀”参数为“TRUE”或“FALSE”时该参数有效。VLR/SGSN前缀号码。 取值范围：1～14位的十进制数字。                   |
| IMSIPROV      | 提供IMSI前缀     | 对IMSI前缀进行增加和删除操作。 取值范围： TRUE：增加IMSI前缀或修改IMSI前缀的IMSIRULE规则。FALSE：删除IMSI前缀。                      |
| IMSIPREFIX    | IMSI前缀       | 仅当本命令中的“提供IMSI前缀”参数为“TRUE”或“FALSE”时该参数有效。IMSI前缀号码。 取值范围：1～15位的十进制数字。                           |
| IMSIRULE      | IMSI前缀规则     | 仅当本命令中的“提供IMSI前缀”参数为“TRUE”时该参数有效。属于IMSIPREFIX号段的用户漫游规则。 PERMISSION: 允许漫游。RESTRICT: 限制漫游。       |

## 使用实例

修改PLMN优选漫游配置，运营商修改PLMN序列号为1的网络的优选漫游配置属性，漫游方式为首选，并按IMSI进行检查，默认IMSI检查规则为PERMISSION，增加VLR/SGSN前缀8613880，增加IMSI前缀460142，IMSI前缀规则为RESTRICT。

MOD PLMN: HLRSN=1, PLMNID=1, PREFERREDTYPE=PREFERRED, CHECKIMSI=TRUE, DEFIMSIRULE=PERMISSION, VSPROV=TRUE, VLRSGSNNO="8613880", IMSIPROV=TRUE, IMSIPREFIX="460142", IMSIRULE=RESTRICT;

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释   | 原因分析                                                                                                                                                               | 处理建议                                                                                                                                                          |
|:--------|:--------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ERR3047 | 超过最大限制  | 可能原因为如下之一：同一个PLMN优选漫游配置增加的“VLR/SGSN前缀”数据记录数超过1000条。所有PLMN优选漫游配置增加的“VLR/SGSN前缀”总记录数超过5000条。同一个PLMN优选漫游配置增加的“IMSI前缀”数据记录数超过1000条。所有PLMN优选漫游配置增加的“IMSI前缀”总记录数超过5000条。 | 根据实际情况，如需增加VLR/SGSN前缀或IMSI前缀，处理步骤如下：执行LST PLMN命令，查询已存在的VLR/SGSN前缀或IMSI前缀。执行该命令删除不必要的VLR/SGSN前缀或IMSI前缀。执行该命令增加VLR/SGSN前缀或IMSI前缀，确保增加的VLR/SGSN前缀或IMSI前缀在规定范围之内。 |