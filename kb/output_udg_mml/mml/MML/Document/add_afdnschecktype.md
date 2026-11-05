# 增加需要进行防欺诈检查的DNS报文类型（ADD AFDNSCHECKTYPE）

- 命令功能
- 注意事项
- 操作用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用NF：PGW-U、UPF**

该命令用于增加需要进行DNS防欺诈检查的DNS报文类型值，例如要对DNS头域“type”字段取值为10的DNS报文做防欺诈检查，则通过此命令增加type为10的记录。

#### 注意事项

- 该命令执行后对新数据流生效。
- 该命令最大记录数为255。
- 支持配置的Type值对应表。

| 参数标识   | 类型名称     | 含义                                         |   类型值 |
|:-------|:---------|:-------------------------------------------|------:|
| 初始值    | A        | a host address                             |     1 |
| 初始值    | NS       | an authoritative name server               |     2 |
| 初始值    | MD       | a mail destination                         |     3 |
| 初始值    | MF       | a mail forwarder                           |     4 |
| 初始值    | CNAME    | the canonical name for an alias            |     5 |
| 初始值    | SOA      | marks the start of a zone of authority     |     6 |
| 初始值    | MB       | a mailbox domain name                      |     7 |
| 初始值    | MG       | a mail group member                        |     8 |
| 初始值    | MR       | a mail rename domain name                  |     9 |
| 初始值    | nan      | a null RR                                  |    10 |
| 初始值    | WKS      | a well known service description           |    11 |
| 初始值    | PTR      | a domain name pointer                      |    12 |
| 初始值    | HINFO    | host information                           |    13 |
| 初始值    | MINFO    | mailbox or mail list information           |    14 |
| 初始值    | MX       | mail exchange                              |    15 |
| 初始值    | TXT      | text strings                               |    16 |
| 初始值    | RP       | responsible person                         |    17 |
| 初始值    | AFSDB    | AFS cell database                          |    18 |
| 初始值    | X25      | X_25 calling address                       |    19 |
| 初始值    | ISDN     | ISDN calling address                       |    20 |
| 初始值    | RT       | router                                     |    21 |
| 初始值    | NSAP     | NSAP address                               |    22 |
| 初始值    | NSAP_PTR | reverse NSAP lookup (deprecated)           |    23 |
| 初始值    | SIG      | security signature                         |    24 |
| 初始值    | KEY      | security key                               |    25 |
| 初始值    | PX       | X.400 mail mapping                         |    26 |
| 初始值    | GPOS     | geographical position (withdrawn)          |    27 |
| 初始值    | AAAA     | IP6 Address                                |    28 |
| 初始值    | LOC      | Location Information                       |    29 |
| 初始值    | NXT      | Next Valid Name in Zone                    |    30 |
| 初始值    | EID      | Endpoint identifier                        |    31 |
| 初始值    | NIMLOC   | Nimrod locator                             |    32 |
| 初始值    | SRV      | Server selection                           |    33 |
| 初始值    | ATMA     | ATM Address                                |    34 |
| 初始值    | NAPTR    | Naming Authority PoinTeR                   |    35 |
| 初始值    | A6       | IPv6 address with indirection (RFC 2874)   |    38 |
| 初始值    | AXFR     | A request for a transfer of an entire zone |   252 |
| 初始值    | MAILB    | A request for mailbox-related records      |   253 |
| 初始值    | MAILA    | A request for mail agent RRs               |   254 |
| 初始值    | STAR     | A request for all records                  |   255 |

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识      | 参数名称        | 参数说明                                                                                    |
|:----------|:------------|:----------------------------------------------------------------------------------------|
| TYPEVALUE | DNS防欺诈检查类型值 | 可选必选说明：必选参数 参数含义：该参数用于配置需要进行防欺诈判断的DNS报文类型。 数据来源：本端规划 取值范围：整数类型，取值范围为1～255。 默认值：无 配置原则：无 |

#### 使用实例

如果运营商需要增加对类型值为10的DNS报文进行防欺诈检查，则配置命令如下：

```
ADD AFDNSCHECKTYPE: TYPEVALUE=10;
```