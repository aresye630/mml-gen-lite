# 修改S-GW特性对接配置(MOD SGWCHARACT)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用网元：SGSN、MME**

该命令用于修改MME与S-GW支持特性的能力交互配置策略。

#### 注意事项

- 该命令执行后立即生效。
- “对端设备范围”、“IP地址类型”、“IPv4地址”、“IPV4地址掩码”、“IPv6地址”、“IPV4地址掩码”这几个参数不能通过该命令修改。

#### 本地用户权限

manage-ug；system-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识          | 参数名称                                     | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                       |
|:--------------|:-----------------------------------------|:-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RANGE         | 对端设备范围                                   | 可选必选说明：必选参数 参数含义：该参数用于指定需要特性能力相互通知的对端设备S-GW范围。 数据来源：全网规划 取值范围：“ALL(所有S-GW)”“SPECIFIED(指定S-GW)” 默认值：无 配置原则：“ALL(所有S-GW)”为系统的缺省记录，不允许增加，也不允许删除，但可以修改。配置记录的优先级关系：“SPECIFIED(指定S-GW)” 高于 “ALL(所有S-GW)”。                                                                                                                                                                                                        |
| IPT           | IP地址类型                                   | 可选必选说明：条件必选参数 参数含义：该参数用于指定S-GW信令面IP地址类型。 前提条件：该参数在“对端设备范围”参数配置为“SPECIFIED(指定S-GW)”后生效。 数据来源：全网规划 取值范围：“IPV4(IPV4)”“IPV6(IPV6)” 默认值：无                                                                                                                                                                                                                                                                       |
| IPV4          | IPv4地址                                   | 可选必选说明：条件必选参数 参数含义：该参数用于指定S-GW信令面IPv4地址，系统中可以配置多条“SPECIFIED(指定S-GW)”的记录，但是IP网段区间不能相同，允许包含关系。当存在包含关系的IP网段记录时，以目标IP地址落入的最小IP网段记录为准。 前提条件：该参数在“IP地址类型”参数配置为“IPV4(IPV4)”后生效。 数据来源：全网规划 取值范围：0.0.0.1~255.255.255.254 默认值：无 配置原则：有效的IPv4地址不能为环回地址(127.x.y.z)。有效的IPv4地址必须是A、B或者C类地址。                                                                                                                              |
| IPV4MSK       | IPV4地址掩码                                 | 可选必选说明：条件必选参数 参数含义：该参数用于指定对端S-GW的信令面IPv4地址的掩码。 前提条件：该参数在“IP地址类型”参数配置为“IPV4(IPV4)”后生效。 数据来源：全网规划 取值范围：0.0.0.1~255.255.255.255 默认值：无 配置原则：输入的掩码要求对应的二进制值1和1之间不允许存在0。例如：“255.255.0.0”是有效掩码；“123.123.123.123”是无效掩码。因为123对应的二进制为“1111011”，1之间存在0。                                                                                                                                                               |
| IPV6          | IPv6地址                                   | 可选必选说明：条件必选参数 参数含义：该参数用于指定S-GW信令面IPv6地址，系统中可以配置多条“SPECIFIED(指定S-GW)”的记录，但是IP网段区间不能相同，允许包含关系。当存在包含关系的IP网段记录时，以目标IP地址落入的最小IP网段记录为准。 前提条件：该参数在“IP地址类型”参数配置为“IPV6(IPV6)”后生效。 数据来源：全网规划 取值范围：::~FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF 默认值：无                                                                                                                                                                   |
| IPV6MSK       | IPV6地址前缀长度                               | 可选必选说明：条件必选参数 参数含义：该参数用于指定IPv6地址的子网前缀的长度。 前提条件：该参数在“IP地址类型”参数配置为“IPV6(IPV6)”后生效。 数据来源：本端规划 取值范围：0~128 默认值：无 配置原则：0是无效掩码。                                                                                                                                                                                                                                                                                   |
| NTSR          | S-GW支持NTSR功能                             | 可选必选说明：可选参数 参数含义：该参数用于设置S-GW是否支持NTSR功能。 数据来源：对端协商 取值范围："YES(支持)""NO(不支持)" 默认值：无 配置原则：“MME链式备份”特性的相关license授权并开启后，此参数配置才生效（特性编号：WSFD-201201，license部件编码：LKV2MCR01）参数设置为“支持”时，发送给对应S-GW的Echo Request/Echo Respone消息的“Node Feature”信元中“NTSR”比特设置为1。参数设置为“不支持”时，发送给对应S-GW的Echo Request/Echo Respone消息的“Node Feature”信元中“NTSR”比特设置为0。当“Node Feature”信元所有bit为0，Echo Request/Echo Respone消息将不携带该信元。               |
| PRN           | S-GW支持PRN功能                              | 可选必选说明：可选参数 参数含义：该参数用于设置S-GW是否支持PRN功能。 数据来源：对端协商 取值范围："YES(支持)""NO(不支持)" 默认值：无 配置原则：“S-GW/P-GW故障下的业务恢复”特性的相关license授权并开启后，此参数配置才生效（特性编号：WSFD-201203，license部件编码：LKV2SRGF01）参数设置为“支持”时，发送给对应S-GW的Echo Request/Echo Respone消息的“Node Feature”信元中“PRN”比特设置为1。参数设置为“不支持”时，发送给对应S-GW的Echo Request/Echo Respone消息的“Node Feature”信元中“PRN”比特设置为0。当“Node Feature”信元所有bit为0，Echo Request/Echo Respone消息将不携带该信元。       |
| MMEID         | S-GW支持MME ID                             | 可选必选说明：可选参数 参数含义：该参数用于设置S-GW是否支持MME ID信元。 数据来源：对端协商 取值范围："YES(支持)""NO(不支持)" 默认值：无 配置原则：“S-GW/P-GW故障下的业务恢复”特性的相关license授权并开启后，此参数配置才生效（特性编号：WSFD-201203，license部件编码：LKV2SRGF01）参数设置为“支持”，发送给对应S-GW的Create Session Request/Modify Bearer Request消息携带“MME ID”信元。参数设置为“不支持”，发送给对应S-GW的Create Session Request/ModifyBearer Request消息不携带“MME ID”信元。                                                              |
| SECRATRPT     | S-GW支持Secondary RAT Usage Data Report    | 可选必选说明：可选参数 参数含义：该参数用于指定是否在MME发送给对应S-GW的Modify Bearer Request、Delete Session Request、Delete Bearer Response、Delete Bearer Command、Release Access Bearers Request、Change Notification Request等消息中携带“Secondary RAT Usage Data Report”信元。 数据来源：全网规划 取值范围："NO（不支持）""YES（支持）" 默认值：无                                                                                                                             |
| GTPUIPPLCY    | GTPU IP类型选择策略                            | 可选必选说明：可选参数 参数含义：该参数用于在MME用户面同时支持IPv4与IPv6地址的场景下，指定与SGW之间的用户面IP地址类型选择策略。 数据来源：对端协商 取值范围：IPV4PRE(与SGW之间的用户面IP地址类型优先选择IPv4地址类型)IPV6PRE(与SGW之间的用户面IP地址类型优先选择IPv6地址类型)GTPCPRE(与SGW之间的用户面IP地址类型优先选择与控制面地址类型相同) 默认值：无 配置原则：S-GW的S11U地址仅支持IPv4地址，则IP地址类型优先选择IPv4地址类型。S-GW的S11U地址仅支持IPv6地址，则IP地址类型优先选择IPv6地址类型。S-GW的S11U地址支持IPv4和IPv6地址，则IP地址类型优先选择与控制面地址类型相同的IP。  说明： 该参数仅在SET SMFUNC中“LTEUSERPLCYSW”配置为“YES”时生效。 |
| ULIFORSGW     | S-GW支持User Location Information For S-GW | 可选必选说明：可选参数 参数含义：该参数用于设置S-GW是否支持User Location Information For S-GW信元。 数据来源：对端协商 取值范围： "NO（不支持）""YES（支持）" 默认值："NO（不支持）" 配置原则： 参数设置为“YES(支持)”，发送给对应S-GW的Create Session Request/Modify Bearer Request消息携带该信元。参数设置为“NO(不支持)”，发送给对应S-GW的Create Session Request/Modify Bearer Request消息不携带该信元。                                                                                                                   |
| PSCELLIDCSR   | S-GW支持CSR消息携带PSCell ID                   | 可选必选说明：可选参数 参数含义：该参数用于指定在MME给对端S-GW发送的Create Session Request消息中是否支持携带“PSCell ID”信元。 数据来源：全网规划 取值范围： "NO（不支持）""YES（支持）" 默认值："NO（不支持）" 配置原则：NSA用户在本地有PSCell Information信息，且有双连接时，希望对端SGW支持Create Session Request消息中携带PSCell ID信元，设置本参数为“YES（支持）”；否则设置本参数为“NO（不支持）”。  说明： 23401协议中有描述需要携带给SGW，但是29274(i00)协议未在Create Session Request消息中添加该信元，因此在协议未更新前属于私有实现，只有对接华为的SGW才允许打开。                                 |
| PSCELLID      | S-GW支持PSCell ID                          | 可选必选说明：可选参数 参数含义：该参数用于指定是否在MME发送给对端S-GW的Create Bearer Response、Bearer Resource Command、Modify Bearer Request、Delete Session Request、Delete Bearer Response、Update Bearer Response、Delete Bearer Command、Release Access Bearers Request、Change Notification Request消息中支持携带“PSCell ID”信元。 数据来源：全网规划 取值范围： "NO（不支持）""YES（支持）" 默认值："NO（不支持）" 配置原则：如果对端SGW支持PSCell ID信元，设置本参数为“YES（支持）”；否则设置本参数为“NO（不支持）”。      |
| PGWRNSI       | S-GW支持PGWRNSI                            | 可选必选说明：可选参数 参数含义：该参数用于设置S-GW是否支持PGWRNSI(PGW Redirection due to mismatch with Network Slice subscribed by UE Support Indication)功能 数据来源：全网规划 取值范围： "NO（不支持）""YES（支持）" 默认值："NO（不支持）" 配置原则： 如果对端SGW支持PGWRNSI功能，设置本参数为“YES（支持）”；否则设置本参数为“NO（不支持）”。 参数设置为“支持”时，发送给对应S-GW的Create Session Request消息的“Indication Flags”信元中“PGWRNSI”比特设置为1。 说明： 启用PGW重定向功能后，无法保证P-GW和S-GW拓扑合一。                                      |
| PCSCFRESTOIND | S-GW支持P-CSCF Restoration Indication      | 可选必选说明：可选参数 参数含义：该参数用于指定是否在MME发送给对端S-GW的Modify Bearer Request消息中支持indication Flags信元内的“P-CSCF Restoration Indication”标志位。 数据来源：全网规划 取值范围： "NO（不支持）" "YES（支持）" 默认值："NO（不支持）" 配置原则： “ 基于HSS的P-CSCF故障恢复”特性的相关License授权并开启后，此参数配置才生效（特性编号：WSFD-201205，License部件编码：LKV2FRPH02） 如果对端S-GW支持“P-CSCF Restoration Indication”标志位，才设置本参数为“YES（支持）”；否则设置本参数为“NO（不支持）”。                                                 |
| DESC          | 描述                                       | 可选必选说明：可选参数 参数含义：该参数用于描述信息。 数据来源：本端规划 取值范围：0~32位字符串 默认值：无                                                                                                                                                                                                                                                                                                                                                  |

#### 使用实例

该命令用于修改MME与S-GW支持特性的能力交互配置策略，执行此命令：

MOD SGWCHARACT: RANGE=SPECIFIED, IPT=IPV4, IPV4="10.95.69.96", IPV4MSK="255.255.255.0", NTSR=YES, PRN=NO, MMEID=YES, SECRATRPT=NO;