# 删除业务IP(RMV SERVICEIP)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用NF：SGSN、MME、AMF**

该命令用于删除业务IP地址。

#### 注意事项

- 该命令执行后立即生效。
- 如果要删除的业务IP地址已经被命令**ADD S1APLE**、**ADD DMLNK**、**ADD M3LNK**、**ADD GTPCLE**、**ADD SGSLNK**、**ADD GTPULE**、**ADD DNSLE**、**ADD GBEPPOOL**、**ADD GBIPLOCENDPT**、**ADD CHGCDPIP**、**ADD LCSAPLNK**、**ADD SBCAPLE**、**ADD SBCAPLNK**、**ADD SCTPLE**引用，需要先通过**RMV S1APLE**、**RMV DMLNK**、**RMV M3LNK**、**RMV GTPCLE**、**RMV SGSLNK**、**RMV GTPULE**、**RMV DNSLE**、**RMV GBEPPOOL**、**RMV GBIPLOCENDPT**、**RMV CHGCDPIP**、**RMV LCSAPLNK**、**RMV SBCAPLE**、**RMV SBCAPLNK**、**RMV SCTPLE**命令删除业务，然后再执行此命令。
- 如果要删除的业务IP所属VPN实例已经被命令引用，且该VPN实例下仅有一条业务IP，需要先通过命令删除重定向配置记录，然后再执行此命令。

#### 本地用户权限

manage-ug；system-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识        | 参数名称     | 参数说明                                                                                                                                                                                                                                                                                                               |
|:------------|:---------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| IPVERSION   | IP版本     | 可选必选说明：必选参数 参数含义：该参数用于指定需要删除的业务IP的IP版本。 数据来源：本端规划 取值范围："IPv4(IPv4地址)""IPv6(IPv6地址)" 默认值：IPv4(IPv4地址) 配置原则：根据选择的IP版本，输入相应格式的IP地址。                                                                                                                                                                                   |
| SERVICEIPV4 | 业务IPv4地址 | 可选必选说明：条件必选参数 参数含义：该参数用于指定需要删除的业务IPv4地址。 前提条件：该参数在“IP版本”配置为“IPv4(IPv4地址)”后生效。 数据来源：全网规划 取值范围：0.0.0.0~255.255.255.255 默认值：无 配置原则：业务地址不能配置为0.0.0.0、255.255.255.255和环回地址(127.x.y.z)。业务地址必须是A、B或者C类地址。该参数的掩码缺省为255.255.255.255，不可更改。                                                                                   |
| SERVICEIPV6 | 业务IPv6地址 | 可选必选说明：条件必选参数 参数含义：该参数用于指定需要删除的业务IPv6地址。 前提条件：该参数在“IP版本”配置为“IPv6(IPv6地址)”后生效。 数据来源：全网规划 取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF 默认值：无 配置原则：IPv6地址必须是全球单播地址，不能为::、FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF、环回地址(::1)、链路本地地址(FE80::/10)和组播地址(FF00::/8)。该参数的掩码缺省为FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF，不可更改。 |
| VPNINSTNAME | VPN实例名称  | 可选必选说明：可选参数 参数含义：该参数用于指定需要删除的业务IP所属的VPN实例名称。 数据来源：本端规划 取值范围：1~31位字符串 默认值：无 配置原则：本参数需要与ADD L3VPNINST命令中的VPN实例名称保持一致。不指定VPN实例名称则默认业务IP所属的VPN为公网VPN"_public_"。一个业务IP只能属于一个VPN实例。若VPN非"_public_"必须输入实际VPNINSTNAME参数。                                                                                                   |

#### 使用实例

删除IP版本号为IPV4，业务IPv4地址为192.168.52.1，VPN实例名称为\_abc\_

RMV SERVICEIP: IPVERSION=IPv4, SERVICEIPV4="192.168.52.1", VPNINSTNAME="\_abc\_";