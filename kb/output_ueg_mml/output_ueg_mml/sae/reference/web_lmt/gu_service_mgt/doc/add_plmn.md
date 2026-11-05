# 增加PLMN信息（ADD PLMN）

- 命令功能
- 注意事项
- 参数说明
- 使用实例
- 输出结果说明

## 命令功能

此操作用来增加PLMN优选漫游配置。

## 注意事项

- 如果填充IMSIPREFIX，则能匹配到IMSIFREFIX的IMSI按IMSIRULE方式处理，其他IMSI按DEFIMSIRULE方式处理。如果IMSIPREFIX为空， 则所有IMSI按DEFIMSIRULE方式处理。
- VLRSGSNNO是非本网的VLR/SGSN。
- 系统中增加的PLMN优选漫游配置记录数不能超过5000条。
- 系统中所有PLMN优选漫游配置增加的VLR/SGSN前缀总记录数不能超过5000条。
- 系统中所有PLMN优选漫游配置增加的IMSI前缀总记录数不能超过5000条。

## 参数说明

| 参数标识          | 参数名称       | 参数说明                                                                                           |
|:--------------|:-----------|:-----------------------------------------------------------------------------------------------|
| HLRSN         | HLR序列号     | HLR序列号，在PGW支持容灾功能或虚拟HLR功能时设置。 取值范围：1～255。                                                      |
| PLMNID        | PLMN序列号    | PLMN序列号。 取值范围：0～999。                                                                           |
| DESCRIPTION   | PLMN描述     | PLMN描述。 取值范围：0～60个字符。                                                                          |
| PREFERREDTYPE | 优选漫游方式     | 优选漫游方式。 取值范围： PREFERRED：首选。ALLOWED：允许。RESTRICTED：受限。 缺省值：PREFERRED                             |
| VLRSGSNNO     | VLR/SGSN前缀 | VLR/SGSN前缀号码。 取值范围：1～14位的十进制数字。                                                                |
| CHECKIMSI     | 按IMSI进行检查  | 是否需要按IMSI检查用户在该PLMN的漫游规则。 取值范围： TRUE：按IMSI检查。FALSE：不按IMSI检查。 缺省值：FALSE                         |
| DEFIMSIRULE   | 默认IMSI检查规则 | 定义在PLMN需要按IMSI检查，但该PLMN没有定义IMSI前缀时的漫游规则。 取值范围： PERMISSION: 允许漫游。RESTRICT: 限制漫游。 缺省值：PERMISSION |
| IMSIPREFIX    | IMSI前缀     | IMSI前缀号码。 取值范围：1～15位的十进制数字。                                                                    |
| IMSIRULE      | IMSI前缀规则   | 属于IMSIPREFIX号段的用户漫游规则。 PERMISSION: 允许漫游。RESTRICT: 限制漫游。 缺省值：PERMISSION                         |

## 使用实例

增加PLMN优选漫游配置，运营商为VLR/SGSN前缀为8613780的网络，配置首选漫游方式，并按IMSI进行检查，默认IMSI检查规则为PERMISSION，IMSI前缀为460141，IMSI前缀规则为RESTRICT。

ADD PLMN: HLRSN=1, PLMNID=1, PREFERREDTYPE=PREFERRED, VLRSGSNNO="8613780", CHECKIMSI=TRUE, DEFIMSIRULE=PERMISSION, IMSIPREFIX="460141", IMSIRULE=RESTRICT;

## 输出结果说明

该命令执行正常，会返回命令执行成功的提示信息。

该命令执行异常，会返回对应的错误码。常见错误码如表1所示。

| 错误码     | 错误码解释   | 原因分析                                                                                                         | 处理建议                                                                                                                                                                        |
|:--------|:--------|:-------------------------------------------------------------------------------------------------------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| ERR3047 | 超过最大限制  | 可能原因为如下之一：增加的PLMN优选漫游配置记录数超过5000条。所有PLMN优选漫游配置增加的“VLR/SGSN前缀”总记录数超过5000条。所有PLMN优选漫游配置增加的“IMSI前缀”总记录数超过5000条。 | 根据实际情况，如需增加PLMN优选漫游配置，处理步骤如下：执行LST PLMN命令，查询已存在的PLMN优选漫游配置。执行RMV PLMN命令，删除不必要的PLMN优选漫游配置。或执行MOD PLMN命令，删除不必要的VLR/SGSN前缀或IMSI前缀。执行该命令增加PLMN优选漫游配置，确保增加的PLMN优选漫游配置记录数在规定范围之内。 |