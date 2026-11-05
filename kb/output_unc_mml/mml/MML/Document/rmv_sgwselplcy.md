# 删除S-GW选择策略(RMV SGWSELPLCY)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例

#### 命令功能

**须知** 

- 参数（IMSI前缀）：即将删除匹配指定IMSI前缀的配置策略，请确认IMSI前缀的填写准确无误。
- 参数（MSISDN）：即将删除匹配指定MSISDN前缀的配置策略，请确认MSISDN前缀的填写准确无误。

**适用网元：SGSN、MME**

该命令用于删除S-GW选择策略。

#### 注意事项

- 该命令执行后对新的LTE Attach/LTE TAU/LTE Handover/（GnGp SGSN->MME）/（GnGp SGSN->S4 SGSN）/S4 SGSN PDP Context Activation/（S4 SGSN->S4 SGSN）/（S4 SGSN->MME）/（MME->S4 SGSN）流程生效。

#### 本地用户权限

manage-ug；system-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识      | 参数名称     | 参数说明                                                                                                                                                    |
|:----------|:---------|:--------------------------------------------------------------------------------------------------------------------------------------------------------|
| SUBRANGE  | 用户范围     | 可选必选说明：必选参数 参数含义：该参数用于指定用户范围。 数据来源：整网规划 取值范围：“IMSI_PREFIX(指定IMSI前缀)”“MSISDN_PREFIX(指定MSISDN前缀)”“SPECIFIC_IMSI(特定IMSI)”“SPECIFIC_MSISDN(特定MSISDN)” 默认值：无 |
| IMSIPRE   | IMSI前缀   | 可选必选说明：条件必选参数 参数含义：该参数用于指定IMSI前缀。 前提条件：只有“SUBRANGE（用户范围）”为“IMSI_PREFIX（指定IMSI前缀）”时，该参数才有效。 数据来源：整网规划 取值范围：1～15位十进制数字字符串 默认值：无                           |
| MSISDNPRE | MSISDN前缀 | 可选必选说明：条件必选参数 参数含义：该参数用于指定MSISDN前缀。 前提条件：只有“SUBRANGE（用户范围）”为“MSISDN_PREFIX(指定MSISDN前缀)”时，该参数才有效。 数据来源：整网规划 取值范围：1～15位十进制数字字符串 默认值：无                     |
| IMSI      | IMSI     | 可选必选说明：条件必选参数 参数说明：该参数用于指定国际移动用户标识。 前提条件：此参数在“用户范围”设置为“SPECIFIC_IMSI(特定IMSI)”后生效。 取值范围：15位十进制数字字符串 默认值：无                                                |
| MSISDN    | MSISDN   | 可选必选说明：条件必选参数 参数说明：该参数用于指定移动台国际ISDN号码。 前提条件：此参数在“用户范围”设置为“SPECIFIC_MSISDN (特定MSISDN)”后生效。 取值范围：13位十进制数字字符串 默认值：无                                        |
| SLCTM     | 选择方法     | 可选必选说明：可选参数 参数含义：该参数用于指定选择方法。 数据来源：整网规划 取值范围：“S-GW_QNAME(指定S-GW的查询域名)”“S-GW_IP (指定S-GW的IP地址)” 默认值：无                                                     |

#### 使用实例

1. 删除S-GW选择策略，通过“用户范围”为“MSISDN\_PREFIX(指定MSISDN前缀)”方式删除

   RMV SGWSELPLCY: SUBRANGE=MSISDN\_PREFIX, MSISDNPRE="83023";
2. 删除S-GW选择策略，通过“用户范围”为“IMSI\_PREFIX(指定IMSI前缀)”方式删除

   RMV SGWSELPLCY: SUBRANGE=IMSI\_PREFIX, IMSIPRE="12303";