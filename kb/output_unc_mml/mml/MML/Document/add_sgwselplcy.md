# 增加S-GW选择策略(ADD SGWSELPLCY)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例

#### 命令功能

**须知** 

- 参数（IMSI前缀）：为防止误操作，请务必确保IMSI前缀的取值合理有效。
- 参数（MSISDN前缀）：为防止误操作，请务必确保MSISDN前缀的取值合理有效。

**适用网元：SGSN、MME**

该命令用于增加S-GW选择策略，为不同的用户群指定S-GW，运营商可以灵活拨测与维护。用户群是指运营商根据自身的经营策略划分的一组用户。例如：基于MSISDN或IMSI，最小粒度为特定MSISDN或特定IMSI。

- S-GW新割接入网后，运营商指定用户接入新割接入网的S-GW，拨测S-GW设备是否工作正常，这样可以不对现网大部分用户的造成影响。 除上述场景外，4G业务部署的典型应用不应使用本命令的配置选择S-GW，请根据“WSFD-205004 S-GW/P-GW 拓扑选择”特性描述部署。
- 若使用本命令直接指定S-GW的查询域名，满足配置条件的用户使用指定的S-GW查询域名解析获得S-GW IP地址。未匹配的用户仍根据终端上报的TAI组装标准查询域名解析获得S-GW IP地址。若指定的S-GW查询域名采用NAPTR查询，“WSFD-205004 S-GW/P-GW 拓扑选择”特性和“WSFD-205006 基于P-GW锚点选择S-GW”特性继续生效。若指定的S-GW查询域名采用A查询，并且域名命名规则遵循3GPP TS 29.303协议的定义，“WSFD-205004 S-GW/P-GW 拓扑选择”特性和“WSFD-205006 基于P-GW锚点选择S-GW”特性继续生效。

#### 注意事项

- 使用本命令指定S-GW后，组网上要求用户移动范围内的eNodeB与指定的S-GW全互联。若用户移动出指定S-GW覆盖的eNodeB区域，会造成指定用户范围的业务中断。使用本命令拨测用户完毕后，请删除本命令以免后续影响该拨测用户。

- 该命令执行后对新的LTE Attach/LTE TAU/LTE Handover/（GnGp SGSN->MME）/（GnGp SGSN->S4 SGSN）/S4 SGSN PDP Context Activation /（S4 SGSN->S4 SGSN）/（S4 SGSN->MME）/（MME->S4 SGSN）流程生效。

- 该表最大记录数为128。

- 本命令启用后，“ADD SGWDNS”以及“ADD AREADNS”命令将不对本命令控制的用户群生效。

- “用户范围”（包含指定IMSI/MSISDN前缀）、“IMSI前缀”或者“MSISDN前缀”、“选择方法”的组合唯一确认一种S-GW选择策略。若上述组合均相同，指定的S-GW查询域名不能重复。

本命令中

“用户范围”

为

“MSISDN\_PREFIX(指定MSISDN前缀)”

的记录优先级高于

“用户范围”

为

“IMSI\_PREFIX(指定IMSI前缀)”

的记录，例如用户123030000000001，使用MSISDN为30808，系统中配置如表1所示，优先匹配

“MSISDN前缀”

为30808的记录2。

| 记录   | 用户范围                        | MSISDN前缀   | IMSI前缀          | 查询域名                                               |
|:-----|:----------------------------|:-----------|:----------------|:---------------------------------------------------|
| 记录1  | “IMSI_PREFIX(指定IMSI前缀)”     | -          | 123030000000001 | TOPON.ETH1.YTSDG.EPC.MNC003.MCC460.3GPPNETWORK.ORG |
| 记录2  | “MSISDN_PREFIX(指定MSISDN前缀)” | 30808      | -               | TOPON.ETH1.RBSEF.EPC.MNC003.MCC460.3GPPNETWORK.ORG |

当

“用户范围”

设置为

“IMSI\_PREFIX（指定IMSI前缀）”

时，如果IMSI前缀的组合同时匹配到多条记录，

“IMSI前缀”

长度不相等时，使用

“IMSI前缀”

最长匹配的记录。例如用户123030000000001，在表2所示场景下，匹配到记录2。

| 记录   | 用户范围                    |          IMSI前缀 | 查询域名                                               | 查询域名.1                                             |
|:-----|:------------------------|----------------:|:---------------------------------------------------|:---------------------------------------------------|
| 记录1  | “IMSI_PREFIX（指定IMSI前缀）” |           12303 | TOPON.ETH1.YTSDG.EPC.MNC003.MCC460.3GPPNETWORK.ORG | TOPON.ETH1.YTSDG.EPC.MNC003.MCC460.3GPPNETWORK.ORG |
| 记录2  | “IMSI_PREFIX（指定IMSI前缀）” | 123030000000001 | TOPON.ETH1.RBSEF.EPC.MNC003.MCC460.3GPPNETWORK.ORG | TOPON.ETH1.RBSEF.EPC.MNC003.MCC460.3GPPNETWORK.ORG |

当

“用户范围”

设置为

“MSISDN\_PREFIX(指定MSISDN前缀)”

时，如果MSISDN前缀的组合同时匹配到多条记录，

“MSISDN前缀”

长度不相等时，使用

“MSISDN前缀”

最长匹配的记录。例如用户MSISDN为3080888，在表3所示场景下，匹配到记录2。

| 记录   | 用户范围                        |   MSISDN前缀 | 查询域名                                               | 查询域名.1                                             |
|:-----|:----------------------------|-----------:|:---------------------------------------------------|:---------------------------------------------------|
| 记录1  | “MSISDN_PREFIX(指定MSISDN前缀)” |      30808 | TOPON.ETH1.YTSDG.EPC.MNC003.MCC460.3GPPNETWORK.ORG | TOPON.ETH1.YTSDG.EPC.MNC003.MCC460.3GPPNETWORK.ORG |
| 记录2  | “MSISDN_PREFIX(指定MSISDN前缀)” |    3080888 | TOPON.ETH1.RBSEF.EPC.MNC003.MCC460.3GPPNETWORK.ORG | TOPON.ETH1.RBSEF.EPC.MNC003.MCC460.3GPPNETWORK.ORG |

#### 本地用户权限

manage-ug；system-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识      | 参数名称           | 参数说明                                                                                                                                                                                                                                                                                      |
|:----------|:---------------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| SUBRANGE  | 用户范围           | 可选必选说明：必选参数 参数含义：该参数用于指定用户范围。 数据来源：整网规划 取值范围：“IMSI_PREFIX(指定IMSI前缀)”“MSISDN_PREFIX(指定MSISDN前缀)”“SPECIFIC_IMSI(特定IMSI)”“SPECIFIC_MSISDN(特定MSISDN)” 默认值：无 配置原则： S-GW选择策略优先级从高到低为：“SPECIFIC_MSISDN (特定MSISDN)”，“SPECIFIC_IMSI (特定IMSI)”， “MSISDN_PREFIX(指定MSISDN前缀)”，“IMSI_PREFIX(指定IMSI前缀)” |
| IMSIPRE   | IMSI前缀         | 可选必选说明：条件必选参数 参数含义：该参数用于指定IMSI前缀。 前提条件：只有“SUBRANGE（用户范围）”为“IMSI_PREFIX（指定IMSI前缀）”时，该参数才有效。 数据来源：整网规划 取值范围：1～15位十进制数字字符串 默认值：无                                                                                                                                                             |
| MSISDNPRE | MSISDN前缀       | 可选必选说明：条件必选参数 参数含义：该参数用于指定MSISDN前缀。 前提条件：只有“SUBRANGE（用户范围）”为“MSISDN_PREFIX(指定MSISDN前缀)”时，该参数才有效。 数据来源：整网规划 取值范围：1～15位十进制数字字符串 默认值：无                                                                                                                                                       |
| IMSI      | IMSI           | 可选必选说明：条件必选参数 参数说明：该参数用于指定国际移动用户标识。 前提条件：此参数在“用户范围”设置为“SPECIFIC_IMSI(特定IMSI)”后生效。 取值范围：15位十进制数字字符串 默认值：无                                                                                                                                                                                  |
| MSISDN    | MSISDN         | 可选必选说明：条件必选参数 参数说明：该参数用于指定移动台国际ISDN号码。 前提条件：此参数在“用户范围”设置为“SPECIFIC_MSISDN (特定MSISDN)”后生效。 取值范围：13位十进制数字字符串 默认值：无                                                                                                                                                                          |
| SLCTM     | 选择方法           | 可选必选说明：必选参数 参数含义：该参数用于指定选择方法。 数据来源：整网规划 取值范围：“S-GW_QNAME(指定S-GW的查询域名)”“S-GW_IP (指定S-GW的IP地址)” 默认值：无 配置原则： S-GW选择策略优先级从高到低为：“S-GW_IP (指定S-GW的IP地址)”，“S-GW_QNAME(指定S-GW的查询域名)” 说明： 当本参数取值配置为“S-GW_IP (指定S-GW的IP地址)”时，在异系统切换或重选场景下，该功能受软参"BYTE_EX_B76" BIT6控制，具体请参考该软参含义。                    |
| QNAME     | 查询域名           | 可选必选说明：条件必选参数 参数含义：该参数用于指定查询域名。 前提条件：只有“SLCTM（选择方法）”为“S-GW_QNAME(指定S-GW的查询域名)”时，该参数才有效。 数据来源：整网规划 取值范围：1~255位字符串 默认值：无 配置原则：该参数只能由字母（A-Z或者a-z）、数字（0-9）、连字符（-）和点（.）组成，字母不区分大小写。按照协议RFC1035规定，Hostname最大有效字符数为253，并且每个Label最大长度为63个字节。                                                      |
| IPV4      | S-GW的信令面IPv4地址 | 可选必选说明：条件可选参数 参数含义：该参数用于指定S-GW的信令面IPv4地址。 前提条件：该参数在“SLCTM（选择方法）”参数设置为“S-GW_IP（指定S-GW IP的地址）”值后生效。 数据来源：整网规划 取值范围：0.0.0.0～255.255.255.255 默认值：无 配置原则：IPV4地址不能配置为0.0.0.0、255.255.255.255和环回地址(127.x.y.z)。IPV4地址必须是A、B或者C类地址。                                                                |
| IPV6      | S-GW的信令面IPv6地址 | 可选必选说明：条件可选参数 参数含义：该参数用于指定S-GW的信令面IPv6地址。 前提条件：该参数在“SLCTM（选择方法）”参数设置为“S-GW_IP（指定S-GW IP地址）”值后生效。 数据来源：整网规划 取值范围：::～FFFF：FFFF：FFFF：FFFF：FFFF：FFFF：FFFF：FFFF 默认值：无 配置原则：IPV6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。           |

#### 使用实例

拨测MSISDN为13515000001的用户选择IP地址为"192.168.183.1"的S-GW，以UNC本地A记录解析为例，进行如下配置:

1. 配置MSISDN=“13515000001”指定S-GW的查询域名ADD SGWSELPLCY: SUBRANGE=MSISDN\_PREFIX, MSISDNPRE="13515000001", SLCTM=S-GW\_QNAME, QNAME="TOPON.ETH1.RTYBG.EPC.MNC003.MCC460.3GPPNETWORK.ORG";
2. 配置域名“TOPON.ETH1.RTYBG.EPC.MNC003.MCC460.3GPPNETWORK.ORG”的查询方式为A查询ADD DNSQ: SUBRANGE=All, DNSUF="TOPON.ETH1.RTYBG.EPC.MNC003.MCC460.3GPPNETWORK.ORG", DNSQUERYMODE=AAAA/A, GROUPID=0;
3. 配置域名“TOPON.ETH1.RTYBG.EPC.MNC003.MCC460.3GPPNETWORK.ORG”解析的IP地址ADD IPV4DNSH: HSINDEX=1000, HOSTNAME="TOPON.ETH1.RTYBG.EPC.MNC003.MCC460.3GPPNETWORK.ORG", ADDRSECTION=SECTION1, IPV4ADDR1="192.168.183.1";

拨测MSISDN为13515000001的用户选择IP地址为"192.168.179.1"的S-GW，以UNC本地进行NAPTR查询配置，进行如下配置:

1. 配置MSISDN=“13515000001”指定S-GW的查询域名ADD SGWSELPLCY: SUBRANGE=MSISDN\_PREFIX, MSISDNPRE="13515000001", SLCTM=S-GW\_QNAME, QNAME="TEST.TAC-LB42.TAC-HB40.TAC.EPC.MNC003.MCC460.3GPPNETWORK.ORG";
2. 配置域名“TEST.TAC-LB42.TAC-HB40.TAC.EPC.MNC003.MCC460.3GPPNETWORK.ORG”的查询方式为NAPTR查询ADD DNSN: FQDN="TEST.TAC-LB42.TAC-HB40.TAC.EPC.MNC003.MCC460.3GPPNETWORK.ORG", HSINDEX=1000, ENTITY=SGW, INTYPE=S11;
3. 配置域名“TOPON.ETH1.SHANGHAI.EPC.MNC003.MCC460.3GPPNETWORK.ORG”解析的IP地址ADD IPV4DNSH: HSINDEX=1000, HOSTNAME="TOPON.ETH1.SHANGHAI.EPC.MNC003.MCC460.3GPPNETWORK.ORG", ADDRSECTION=SECTION1, IPV4ADDR1="192.168.179.1";