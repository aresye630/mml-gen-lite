# 增加签约数据纠正参数(ADD SMSUBDATA)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用网元：SGSN、MME**

该命令用于增加一条签约数据修改的记录，修改IMSI号段、PDP TYPE、APN匹配的用户群的签约数据类型。使用该命令时建议设置软参DWORD\_EX26 BIT13的值为1。

#### 注意事项

- 该命令执行后立即生效。
- 该表最大记录数为1024。

#### 本地用户权限

manage-ug；system-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识               | 参数名称                 | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                             |
|:-------------------|:---------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SUBRANGE           | 用户范围                 | 可选必选说明：必选参数 参数含义：该参数用于指定签约数据纠正参数所包含的用户范围，用来设定该命令的作用范围。 数据来源：整网规划 取值范围：“ALL_USER(所有用户)”：表示所有用户，增加全局约束的时候添加。“SPECIAL_USER(指定用户)”：表示指定的用户，增加指定用户配置的时候添加。 默认值：无 配置原则：相同APNNI，PDPTYPE时，只能配置一条“SUBRANGE(用户范围)”为“所有用户”的记录。                                                                                                                                                                                                                              |
| IMSIPRE            | IMSI前缀               | 可选必选说明：条件必选参数 参数含义：该参数用于指定用户的IMSIPRE(IMSI前缀)，用来确定命令的作用范围，即当为选择SPECIAL USER时，才可以配置IMSIPRE。 前提条件：该参数在“SUBRANGE(用户范围)”参数设置为“SPECIAL_USER(指定用户)”时，才需要配置。 数据来源：整网规划 取值范围：5～15位数字 默认值：无  说明： “IMSIPRE(IMSI前缀)”为全局唯一。                                                                                                                                                                                                                                   |
| TYPE               | 匹配条件                 | 可选必选说明：必选参数 参数含义：该参数用于指定合适的匹配条件。 数据来源：本端规划 取值范围：“SUBSCRIBED_PARAMETER(签约参数)”：指定使用签约的参数来作为匹配条件。“Context_ID(Context ID)”：指定使用上下文标识来作为匹配条件。 默认值：无                                                                                                                                                                                                                                                                                                   |
| CTXID              | 上下文标识                | 可选必选说明：条件必选参数 参数含义：该参数用于指定PDP上下文标识。 前提条件：该参数在“TYPE(匹配条件)”参数设置为“Context_ID(Context ID)”时，才需要配置。 数据来源：整网规划 取值范围：0～255 默认值：无                                                                                                                                                                                                                                                                                                                        |
| APNNIRANGE         | 签约APNNI范围            | 可选必选说明：条件必选参数 参数含义：该参数用于指定合适的签约APNNI范围。 前提条件：该参数在“TYPE(匹配条件)”参数设置为“SUBSCRIBED_PARAMETER(签约参数)”时，才需要配置。 数据来源：本端规划 取值范围：“APNNI_ALL(所有签约APNNI)”：用于增加一条修改所有的APNNI的记录。“APNNI_SPECIAL(指定签约APNNI)”：用于增加一条修改指定APNNI的记录。 默认值：无                                                                                                                                                                                                                            |
| APNNI              | 签约APNNI              | 可选必选说明：条件必选参数 参数含义：该参数用于指定APN网络标识。 前提条件：该参数在“APNNIRANGE(签约APNNI范围)”参数设置为“APNNI_SPECIAL(指定签约APNNI)”时，才需要配置。 数据来源：本端规划 取值范围：1～62位字符串 默认值：无 配置原则：APN网络标识地址由一个或多个LABEL构成，各LABEL间用“.”间隔。每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”，字母不区分大小写。APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾，不能取值为“*”。输入的APNNI参数应为类似于XXX.XXX的形式，如“123.net”。如果配置的APNNI不正确，可能因DNS解析失败而导致激活流程失败。                                                                           |
| PDPTYPE            | 签约PDP/PDN类型          | 可选必选说明：条件必选参数 参数含义：该参数用于指定PDP类型。 前提条件：该参数在“TYPE(匹配条件)”参数设置为“SUBSCRIBED_PARAMETER(签约参数)”时，才需要配置。 数据来源：整网规划 取值范围：“IPV4(IPv4地址)”：表示IPv4协议，为UE分配IPv4地址。“IPV6(IPv6地址)”：表示IPv6协议，为UE分配IPv6地址。“PPP(PPP)”：表示点对点通信协议，和UE之间使用PPP协议通信。“IPV4V6(IPv4v6)”：表示IPV4V6双栈协议，同时为UE分配IPv4地址和IPv6地址。“IPV4/IPV6(IPv4/IPv6)”：表示支持IPv4协议或者IPv6协议，由系统自动选择支持哪种协议，优先选择IPv4协议。“ALL_PDP_TYPE(ALL PDP Type)”：表示支持所有PDP协议类型，不包含Non-IP类型，当指定IMSEPRE的PDP类型不存在之前类型时，选择所有协议类型。 默认值：无 |
| IPV4PDPADDRTYPE    | 签约IPv4 PDP/PDN地址分配类型 | 可选必选说明：条件必选参数 参数含义：该参数用于指定签约IPv4 PDP/PDN地址分配类型。 前提条件：该参数在“PDPTYPE(签约PDP/PDN类型)”参数设置为“IPV4(IPv4地址)”或“IPV4V6(IPv4v6)”或“IPV4/IPV6(IPv4/IPv6)”时，才需要配置。 数据来源：整网规划 取值范围：“ALLOCATION_IPV4PDP_DYNAMIC(动态分配)”“ALL_STATIC_IPV4PDP_ADDR(所有静态分配的PDP地址)”“SPECIAL_STATIC_IPV4PDP_ADDR(指定静态分配的PDP地址)” 默认值：无                                                                                                                                                     |
| IPV4               | 签约IPv4 PDP/PDN地址     | 可选必选说明：条件必选参数 参数含义：该参数用于指定UE的IPv4地址。 前提条件：该参数在“IPV4PDPADDRTYPE（签约IPv4 PDP/PDN地址分配类型）”参数设置为“SPECIAL_STATIC_IPV4PDP_ADDR(指定静态分配的PDP地址)”时，才需要配置。 数据来源：整网规划 取值范围：0.0.0.0～255.255.255.255 默认值：无                                                                                                                                                                                                                                                       |
| IPV6PDPADDRTYPE    | 签约IPv6 PDP/PDN地址分配类型 | 可选必选说明：条件必选参数 参数含义：该参数用于指定签约IPv6 PDP/PDN地址分配类型。 前提条件：该参数在“PDPTYPE(签约PDP/PDN类型)”参数设置为“IPV6(IPv6地址)”或“IPv4v6(IPv4v6)”或“IPv4/IPv6(IPv4/IPv6)”时，才需要配置。 数据来源：整网规划 取值范围：“DYNAMIC(动态分配)”“ALL_STATIC_IPV6PDP_ADDR(所有静态分配的PDP地址)”“SPECIAL_STATIC_IPV6PDP_ADDR(指定静态分配的PDP地址)” 默认值：无                                                                                                                                                                        |
| IPV6               | 签约IPv6 PDP/PDN地址     | 可选必选说明：条件必选参数 参数含义：该参数用于指定UE的IPv6地址。 前提条件：该参数在“IPV6PDPADDRTYPE（签约IPv6 PDP/PDN地址分配类型）”参数设置为“SPECIAL_STATIC_IPV6PDP_ADDR(指定静态分配的PDP地址)”时显示。 数据来源：整网规划 取值范围：0:0:0:0:0:0:0:0～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF 默认值：无                                                                                                                                                                                                                           |
| CORRECTAPNNI       | 修改签约APNNI            | 可选必选说明：可选参数 参数含义：该参数用于标识是否要修改签约的APNNI。 数据来源：本端规划 取值范围：“YES(是)”：用于增加一条修改签约的APNNI记录。“NO(否)” 默认值：“NO(否)”。                                                                                                                                                                                                                                                                                                                                           |
| NEWAPNNI           | 新的签约APNNI            | 可选必选说明：条件必选参数 参数含义：该参数用于指定新的APN网络标识。 前提条件：该参数在“CORRECTAPNNI(修改签约APNNI)”参数设置为“YES(是)”时，才需要配置。 数据来源：本端规划 取值范围：1～62位字符串 默认值：无 配置原则：APN网络标识地址由一个或多个LABEL构成，各LABEL间用“.”间隔。每个LABEL的构成字符只能是字母A～Z或a～z、数字0～9和中划线“-”。APN网络标识地址不能以“rac”、“lac”、“sgsn”或“rnc”开头，不能以“.gprs”结尾，不能取值为“*”。输入的APN NI参数应为类似于XXX.XXX的形式，如“123.net”。如果配置的APN NI不正确，可能因DNS解析失败而导致激活流程失败。                                                                                                |
| NEWPDPTYPE         | 新的签约PDP类型            | 可选必选说明：可选参数 参数含义：该参数用于指定新的PDP类型，如果签约的PDP类型为Non-IP类型，本参数不生效。 数据来源：整网规划 取值范围：“IPV4(IPv4地址)”“IPV6(IPv6地址)”“PPP(PPP)”“IPV4V6(IPv4v6)”“IPV4/IPV6(IPv4/IPv6)”“NOT_MODIFY(不修改)” 默认值：无  说明： 注意“NEWPDPTYPE(新的签约PDP类型)”参数不输入时，“NEWPDPTYPE(新的签约PDP类型)”参数取值为“IPV4(IPv4地址)”，“NEWIPV4PDPADDRTYPE(新的签约IPv4 PDP地址分配类型)”取值为“DYNAMIC(动态分配)”。                                                                                                                       |
| NEWIPV4PDPADDRTYPE | 新的签约IPv4 PDP地址分配类型   | 可选必选说明：条件必选参数 参数含义：该参数用于指定新的签约IPv4 PDP地址分配类型。 前提条件：该参数在“NEWPDPTYPE(新的签约PDP类型)”参数设置为“IPV4(IPV4地址)”或“IPV4V6(IPv4v6)”或“IPV4/IPV6(IPv4/IPv6)”时，才需要配置。 数据来源：整网规划 取值范围：“DYNAMIC(动态分配)”“STATIC(静态分配)” 默认值：无                                                                                                                                                                                                                                             |
| NEWIPV4            | 新的IPv4 PDP/PDN地址     | 可选必选说明：条件必选参数 参数含义：该参数用于指定新的IPv4地址。 前提条件：该参数在“NEWIPV4PDPADDRTYPE（新的签约IPv4 PDP/PDN地址分配类型）”参数设置为“STATIC(静态分配)”时，才需要配置。 数据来源：整网规划 取值范围：0.0.0.0～255.255.255.255 默认值：无                                                                                                                                                                                                                                                                                |
| NEWIPV6PDPADDRTYPE | 新的签约IPv6 PDP地址分配类型   | 可选必选说明：条件必选参数 参数含义：该参数用于指定新的签约IPv6 PDP地址分配类型。 前提条件：该参数在“NEWPDPTYPE(新的签约PDP/PDN类型)”参数设置为“IPV6(IPv6地址)”或“IPV4V6(IPv4v6)”或“IPV4/IPV6(IPv4/IPv6)”时，才需要配置。 数据来源：整网规划 取值范围：“DYNAMIC(动态分配)”“STATIC(静态分配)” 默认值：无                                                                                                                                                                                                                                         |
| NEWIPV6            | 新的IPv6 PDP/PDN地址     | 可选必选说明：条件必选参数 参数含义：该参数用于指定新的IPv6地址。 前提条件：该参数在“NEWIPV6PDPADDRTYPE（新的签约IPv6 PDP/PDN地址分配类型）”参数设置为“STATIC(静态分配)”时显示。 数据来源：整网规划 取值范围：0:0:0:0:0:0:0:0～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF 默认值：无                                                                                                                                                                                                                                                    |

#### 使用实例

增加一条签约数据纠正参数信息，其用户范围为所有用户，匹配条件为签约数据，签约APNNI范围为所有APNNI，PDP协议类型为PPP协议，不修改签约APNNI，不修改新的PDP类型：

ADD SMSUBDATA: SUBRANGE=ALL\_USER, TYPE=SUBSCRIBED\_PARAMETER, APNNIRANGE=APNNI\_ALL, PDPTYPE=PPP, CORRECTAPNNI=NO, NEWPDPTYPE=NOT\_MODIFY;