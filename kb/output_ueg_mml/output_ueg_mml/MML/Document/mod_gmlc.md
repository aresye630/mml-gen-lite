# 修改GMLC配置(MOD GMLC)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用网元：SGSN、MME**

此命令用于修改配置互联的GMLC信息及对应的接口配置。

#### 注意事项

此命令执行后立即生效。

#### 本地用户权限

manage-ug；system-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识       | 参数名称        | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
|:-----------|:------------|:----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| GMLCID     | GMLC 标识     | 可选必选说明：必选参数 参数含义：该参数用于指定GMLC标识。 数据来源：整网规划 取值范围：0～639 默认值：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| MCC        | GMLC所属MCC   | 可选必选说明：可选参数 参数含义：该参数用于指定GMLC所属移动国家码。 数据来源：整网规划 取值范围：3位BCD码 默认值：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| MNC        | GMLC所属MNC   | 可选必选说明：可选参数 参数含义：该参数用于指定GMLC所属移动网码。 数据来源：整网规划 取值范围：2～3位的BCD码 默认值：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| GMLCIPT    | GMLC IP地址类型 | 可选必选说明：可选参数 参数含义：该参数用于指定GMLC IP地址类型。 数据来源：整网规划 取值范围：“IPV4(IPv4)”、“IPV6(IPv6)” 默认值：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| GMLCIPV4   | GMLC IPV4地址 | 可选必选说明：条件必选参数 参数含义：该参数用于指定GMLC IPV4地址。 前提条件：当“GMLC IP地址类型”设置为“IPV4(IPv4)”时本参数有效。 数据来源：整网规划 取值范围：0.0.0.0～255.255.255.255 默认值：无 配置原则： “GMLC IPV4地址”不能为“0.0.0.0”、“255.255.255.255”和“0.x.y.z”。“GMLC IPV4地址”不能为组播地址(“224.x.y.z”)和环回地址(“127.x.y.z”)。“GMLC IPV4地址”必须是A、B或者C类地址。                                                                                                                                                                                                                                                                                                                                                    |
| GMLCIPV6   | GMLC IPV6地址 | 可选必选说明：条件必选参数 参数含义：该参数用于指定GMLC IPV6地址。 前提条件：当“GMLC IP地址类型”设置为“IPV6(IPv6)”时本参数有效。 数据来源：整网规划 取值范围：::～FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF 默认值：无 配置原则：“GMLC IPV6地址”必须是全球单播地址，不能为“::”、“FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF”、环回地址(“::1”)、链路本地地址(“FE80::/10”)和组播地址(“FF00::/8”)。  说明： 目前不支持IPV6地址的配置。                                                                                                                                                                                                                                                                                                                       |
| GMLCNO     | GMLC 号码     | 可选必选说明：可选参数 参数含义：该参数用于指定GMLC号码。 数据来源：整网规划 取值范围：1～16位BCD码 默认值：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| HSNM       | GMLC 主机名    | 可选必选说明：可选参数 参数含义：该参数用于指定GMLC主机名，用于GMLC发送PLR时UNC会与消息中携带的orgin-host信元进行比较，如果消息中携带的orgin-host信元在本配置中找不到匹配记录，则返回失败。 数据来源：整网规划 取值范围：1～127位字符串 默认值：无 配置原则：不能为非法字符，只允许输入字母，数字，“.”和“-”，大小写不敏感。例如：gmlc.epc.mnc123.mcc123.3gppnetwork.org。在E-UTRAN网络中，GMLC主机名必须配置。                                                                                                                                                                                                                                                                                                                                                                    |
| IFTYPE     | 接口类型        | 可选必选说明：可选参数 参数含义：该参数用于指定GMLC和UNC之间的接口类型，用来区分不同网络的GMLC。 数据来源：整网规划 取值范围：“Lg”：表示该GMLC只支持Lg接口。“SLg”：表示该GMLC只支持SLg接口。“Lg-SLg”：表示该GMLC同时支持Lg和Slg接口。 默认值 ：无  说明： 在GERAN和UTRAN网络中，GMLC和UNC间的接口为Lg接口。在E-UTRAN网络中，GMLC和UNC间的接口为SLg接口。                                                                                                                                                                                                                                                                                                                                                                                                 |
| SPTLOCINFO | 支持定位信息      | 可选必选说明：可选参数 参数含义：该参数用于指定GMLC支持的定位信息。MME通过Subscriber Location Report和Provide Subscriber Location Answer消息将定位信息上报给GMLC（3GPP TS 29.172）。 数据来源：整网规划 配置原则：当“接口类型”参数“SLg(SLg)”被勾选时，该参数生效，请根据GMLC支持的实际情况勾选。 取值范围：“EUTRAN_CELL_ID(E-UTRAN Cell Identifier)”：ESMLC-Cell-Info信元中的ECGI字段。“CELL_PORTION_ID(Cell Portion ID)”：ESMLC-Cell-Info信元中的Cell-Portion-ID字段。“CIVIC_ADDR(Civic Address)”：Civic-Address信元。“BAR_PRESSURE(Barometric Pressure)”：Barometric-Pressure信元。“VEL_EST(Velocity Estimate)”：Velocity-Estimate信元。“ADD_POSIT_DATA(Additional Positioning Data)”：EUTRAN-Positioning-Data信元中的Additional Positioning Data字段。 默认值 ：无 |

#### 使用实例

修改“GMLC 标识”为“1”的GMLC配置记录，其中“GMLC IP地址类型”为“IPV4(IPv4)”，“GMLC IPV4地址”为“10.10.10.13”：

MOD GMLC: GMLCID=1, GMLCIPT=IPV4, GMLCIPV4="10.10.10.13";