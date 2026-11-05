# 增加相同APN建立多个PDP/PDN连接的网关选择策略(ADD SCNDGWSELPLCY)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用网元：SGSN、MME**

该命令用于根据用户范围及接入类型配置使用相同APN建立多个PDP/PDN连接场景下，系统选择GGSN/P-GW的策略。当指定用户建立第1个PDP/PDN连接时，系统通过相应APN到DNS解析获取GGSN/P-GW的IP地址（IP1），在发给GGSN/S-GW的Create PDP Context Request/Create Session Request消息中携带IP1（接口IP）。GGSN/S-GW回复给USN的Create PDP Context Response/Create Session Response消息中会携带IP2（业务IP），IP1和IP2可能相同，也可能不同，若不相同，当使用相同APN建立第二个或更多PDP/PDN连接时，根据本命令选择在Create PDP Context Request/Create Session Request消息中携带的IP类型。

#### 注意事项

- 该命令执行后只对新激活PDN生效。
- 本命令最大记录数为256。
- 本命令指定的相同APN网关选择策略参数优先级高于**SET SMFUNC**中的“LTE场景相同APN选择网关策略”或“GU场景相同APN选择网关策略”参数。

#### 本地用户权限

manage-ug; system-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识        | 参数名称             | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                          |
|:------------|:-----------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RATTYPE     | 接入类型             | 可选必选说明：必选参数 参数含义：该参数用以指定网关地址选择策略的适用用户的接入方式。 数据来源：整网规划 取值范围：“LTE(LTE)”：指定的接入类型是LTE。“GPRS_UMTS(GPRS&UMTS)”：指定的接入类型是GPRS或者UMTS。 默认值：无                                                                                                                                                                                                                                                                                            |
| SUBRANGE    | 用户范围             | 可选必选说明：必选参数 参数含义：该参数用以指定网关地址选择策略的适用用户范围。 数据来源：整网规划 取值范围：“ALL_USER（所有用户）”：所有指定接入类型的用户。“HOME_USER（本网用户）”：所有指定接入类型的本网用户。“FOREIGN_USER（外网用户）”：所有指定接入类型的外网用户。“IMSI_PREFIX（指定IMSI前缀）”：所有指定接入类型且指定IMSI前缀的用户。 默认值：无 配置原则：如果一个用户在多个用户范围内，该参数生效的优先级从高到低：“IMSI_PREFIX（指定IMSI前缀）”，“HOME_USER（本网用户）”或“FOREIGN_USER（外网用户）”，“ALL_USER（所有用户）”。                                                                                                |
| IMSIPRE     | IMSI前缀           | 可选必选说明：条件必选参数 参数含义：该参数用以指定网关地址选择策略的适用用户IMSI前缀。 前提条件：该参数在“用户范围”参数配置为“指定IMSI前缀”后生效。 数据来源：整网规划 取值范围：5~15位数字。 默认值：无                                                                                                                                                                                                                                                                                                               |
| LTEGWPREFER | LTE模式相同APN网关选择策略 | 可选必选说明：条件必选参数 参数含义：该参数用于控制在LTE场景下，一个用户使用相同APN建立多个PDN连接时的P-GW选择策略。 前提条件：该参数在“接入类型”参数配置为“LTE”后生效。 数据来源：整网规划 取值范围：“INTERFACE_IP（使用接口IP）”：如果接口IP有效，使用接口IP作为P-GW的IP地址。如果接口IP无效，软参DWORD_EX34 BIT20的取值为“0”且P-GW Hostname有效时，使用P-GW Hostname进行DNS解析获取P-GW的IP地址。否则依次通过配置数据、签约数据或APN DNS解析来获取P-GW的IP地址。“SERVICE_IP（使用业务IP）”：使用业务IP作为GGSN/P-GW的IP地址。 默认值：无                                                                               |
| GUGWPREFER  | GU模式相同APN网关选择策略  | 可选必选说明：条件必选参数 参数含义：该参数用于控制在GSM/UMTS场景下，一个用户使用相同APN建立多个PDP/PDN连接时的GGSN/P-GW选择策略。 前提条件：该参数在“接入类型”参数配置为“GPRS_UMTS”后生效。 数据来源：整网规划 取值范围：“INTERFACE_IP（使用接口IP）”：如果接口IP有效，使用接口IP作为GGSN/P-GW的IP地址。如果接口IP无效，GGSN/P-GW Hostname有效，使用GGSN/P-GW Hostname进行DNS解析获取GGSN/P-GW的IP地址。否则，依次通过配置数据、签约数据或APN DNS解析来获取GGSN/P-GW的IP地址。“SERVICE_IP（使用业务IP）”：使用业务IP作为GGSN/P-GW的IP地址。“APNDNS（DNS解析获取）”：依次通过配置数据、签约数据或APN DNS解析来获取GGSN/P-GW的IP地址。 默认值：无 |
| DESC        | 描述信息             | 可选必选说明：可选参数 参数含义：该参数是使用相同APN建立多个PDP/PDN连接时网关选择策略的描述。 数据来源：本端规划 取值范围：0～32位字符串 默认值：无                                                                                                                                                                                                                                                                                                                                            |

#### 使用实例

运营商定义LTE接入类型的所有外网用户使用相同APN建立第二个或更多PDN连接时，使用Create Session Request消息中携带的接口IP作为P-GW的IP地址，LTE接入类型其他用户使用Create Session Response消息中携带的业务IP作为P-GW的IP地址：

1. 设置LTE接入类型整系统相同APN使用业务IP建立多个PDP/PDN连接的网关：

   SET SMFUNC: LTEGWSELPLCY=SERVICE\_IP;或者ADD SCNDGWSELPLCY: RATTYPE=LTE, SUBRANGE=ALL\_USER, LTEGWPREFER=SERVICE\_IP;
2. 设置LTE接入类型所有外网用户相同APN使用接口IP建立多个PDP/PDN连接的网关：

   ADD SCNDGWSELPLCY: RATTYPE=LTE, SUBRANGE=FOREIGN\_USER, LTEGWPREFER=INTERFACE\_IP;