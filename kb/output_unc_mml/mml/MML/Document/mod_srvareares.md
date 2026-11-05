# 修改本地服务区域限制（MOD SRVAREARES）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：AMF**

该命令用于修改本地配置的服务区域限制。

## 注意事项

该命令执行后立即生效。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识         | 参数名称      | 参数说明                                                                                                                                                                                                                                                                                                                                                                                              |
|:-------------|:----------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SUBRANGE     | 用户范围      | 可选必选说明：必选参数  参数含义：该参数用于表示AMF上配置Service Area Restriction参数的用户范围。  数据来源：全网规划 取值范围： “ALL_USER（所有用户）”：所有用户“HOME_USER（本网用户）”：本网用户“FOREIGN_USER（外网用户）”：外网用户“IMSI_PREFIX（IMSI前缀）”：IMSI前缀“IMSI（IMSI）”：IMSI  默认值：无  配置原则：  对于指定的用户（群），策略匹配的优先级从高到低依次为：“IMSI(指定IMSI)”，“IMSI_PREFIX(IMSI前缀)”、“HOME_USER(本网用户)”或“FOREIGN_USER(外网用户)”、“ALL_USER(所有用户)”。  当SUBRANGE取值为“IMSI(指定IMSI)”时，匹配用户的方式为全匹配。              |
| IMSIPRE      | IMSI前缀    | 可选必选说明：该参数在"SUBRANGE"配置为"IMSI_PREFIX"时为条件必选参数。  参数含义：该参数用于指定应用本地配置Service Area Restriction参数的用户的IMSI前缀。  数据来源：全网规划  取值范围：字符串类型，输入长度范围是1~15。只允许输入十进制数字（0-9）。  默认值：无  配置原则：无                                                                                                                                                                                                                        |
| IMSI         | IMSI      | 可选必选说明：该参数在"SUBRANGE"配置为"IMSI"时为条件必选参数。  参数含义：该参数用于指定应用本地配置Service Area Restriction参数的用户的IMSI。  数据来源：全网规划  取值范围：字符串类型，输入长度范围是14~15。只允许输入十进制数字（0-9）。  默认值：无  配置原则：无                                                                                                                                                                                                                                |
| SARPRIORITY  | 服务区域限制优先级 | 可选必选说明：可选参数  参数含义：该参数用于指定本地配置和签约Service Area Restriction的优先级。  数据来源：全网规划 取值范围： “SUB_FIRST（签约优先）”：表示如果用户签约Service Area Restriction，优先使用用户签约的Service Area Restriction，如果用户未签约Service Area Restriction，使用本命令指定的Service Area Restriction。“CFG_FIRST（配置优先）”：表示无论用户是否签约Service Area Restriction，均优先使用本命令指定的Service Area Restriction。  默认值：无  配置原则：无                                                     |
| AREACODE     | 区域码       | 可选必选说明：可选参数  参数含义：该参数用于指定应用接入限制的某个区域。  数据来源：全网规划  取值范围：字符串类型，输入长度范围是0~128。该区域编码必须先通过ADD AREACODE进行添加；而区域内的跟踪区列表则通过ADD AREAMEM进行添加。该命令中参数AREACODE输入单空格等同于不输入。  默认值：无  配置原则：  如果该参数没有配置，“区域群属性”为“ALLOWED_AREAS”，则表示所有区域都允许接入，“区域群属性”为“NOT_ALLOWED_AREAS”，则表示所有区域都不允许接入。                                                                                                                             |
| RESTYPE      | 区域群属性     | 可选必选说明：可选参数  参数含义：该参数用于指定区域群属性。  数据来源：全网规划 取值范围： ALLOWED_AREAS（允许接入区域）NOT_ALLOWED_AREAS（不允许接入区域）  默认值：无  配置原则：无                                                                                                                                                                                                                                                                                   |
| NOSUBSARPLCY | 未签约处理策略   | 可选必选说明：可选参数  参数含义：UDM没有签约Service Area Restriction的场景AMF是否将Service Area Restriction携带给PCF。  数据来源：全网规划 取值范围： “YES（是）”：是“NO（否）”：否  默认值：无  配置原则：无                                                                                                                                                                                                                                                     |
| MAXNUMOFTAS  | 最大跟踪区个数   | 可选必选说明：该参数在"RESTYPE"配置为"ALLOWED_AREAS"、"NOT_ALLOWED_AREAS"时为条件可选参数。  参数含义：该参数表示最大跟踪区个数。  数据来源：全网规划  取值范围：整数类型，取值范围是0~20000。  默认值：无  配置原则：  当RESTYPE为“允许接入区域”时，MAXNUMOFTAS参数含义为最大允许跟踪区TA个数。当RESTYPE为“不允许接入区域”时，MAXNUMOFTAS参数含义为最大不允许跟踪区TA个数。  当配置的MAXNUMOFTAS为0且SARPRIORITY为“本地配置优先”时，AMF携带给PCF的MAXNUMOFTAS以实际配置的TA个数为准。  当配置的MAXNUMOFTAS不为0且SARPRIORITY为“本地配置优先”时，AMF携带给PCF的MAXNUMOFTAS以本命令配置值为准。 |

## 使用实例

针对所有用户，修改本地服务区域限制策略，执行如下命令：

```
MOD SRVAREARES: SUBRANGE=ALL_USER;
```