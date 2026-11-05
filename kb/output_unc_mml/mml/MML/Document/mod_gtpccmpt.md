# 修改GTP-C V0/V1协议兼容性配置(MOD GTPCCMPT)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例

#### 命令功能

**适用网元：SGSN、MME**

- 此命令用于修改GTP-C V0/V1协议兼容性配置，用于控制在SGSN或者MME发送的GTP消息中，是否允许携带特定的可选信元。

#### 注意事项

- 此命令执行后立即生效。

- Forward Srns Context消息仅在SGSN发送。

- SGSN发送GTP消息SGSN Context Response、Forward Relocation Request时，可以控制在GTP消息中是否允许携带R4协议版本新增加的可选信元RAB Context、Charging Characteristics等。当对端GGSN不支持这些R4版本的新信元时，可以通过**MOD GTPCCMPT**命令修改配置，使GTP消息中不携带这些信元。一般情况下，只要不是特别老的对端设备，应该都支持这些新特性的，所以一般建议在GTP消息中携带这些信元。

- 当没有指定在GTP消息中，是否允许携带特定的可选信元时，系统默认情况下将在GTP消息中携带这些可选信元。

- “消息分类”、“消息类型”和“信元类型”三个参数唯一确定一条记录。

消息类型、信元类型和携带方式的映射关系：

| 消息类型                        | 信元类型                                     | 携带方式             |
|:----------------------------|:-----------------------------------------|:-----------------|
| SGSN Context Response       | RAB Context                              | 不携带按协议定义携带按自定义携带 |
| SGSN Context Response       | Charging Characteristics                 | 不携带按协议定义携带按自定义携带 |
| SGSN Context Response       | IMEISV                                   | 不携带按协议定义携带按自定义携带 |
| SGSN Context Response       | PDP Context Prioritization               | 不携带按协议定义携带按自定义携带 |
| SGSN Context Response       | Evolved Allocation/Retention Priority II | 不携带按协议定义携带按自定义携带 |
| SGSN Context Response       | Co-located GGSN-PGW FQDN                 | 不携带按协议定义携带按自定义携带 |
| SGSN Context Response       | IMSI                                     | 不携带按协议定义携带按自定义携带 |
| Forward Relocation Request  | Charging Characteristics                 | 不携带按协议定义携带按自定义携带 |
| Forward Relocation Request  | IMEISV                                   | 不携带按协议定义携带按自定义携带 |
| Forward Relocation Request  | PDP Context Prioritization               | 不携带按协议定义携带按自定义携带 |
| Forward Relocation Request  | Evolved Allocation/Retention Priority II | 不携带按协议定义携带按自定义携带 |
| Forward Relocation Request  | Selected PLMN ID                         | 不携带按协议定义携带按自定义携带 |
| Forward Relocation Request  | Co-located GGSN-PGW FQDN                 | 不携带按协议定义携带按自定义携带 |
| Forward Relocation Request  | UE Network Capability                    | 不携带按协议定义携带按自定义携带 |
| Forward Relocation Request  | Additional MM context for SRVCC          | 不携带按协议定义携带按自定义携带 |
| Forward Relocation Request  | Additional flags for SRVCC               | 不携带按协议定义携带按自定义携带 |
| Forward Relocation Request  | Session Transfer Number for SRVCC        | 不携带按协议定义携带按自定义携带 |
| Forward Relocation Request  | Correlation MSISDN                       | 不携带按协议定义携带按自定义携带 |
| Forward Relocation Request  | Extended RANAP Cause                     | 不携带按协议定义携带按自定义携带 |
| Forward Relocation Request  | eNodeB ID                                | 不携带按协议定义携带按自定义携带 |
| Forward Srns Context        | Source RNC PDCP Context                  | 不携带按协议定义携带按自定义携带 |
| Update PDP Context Response | User Location Information                | 不携带按协议定义携带按自定义携带 |
| Update PDP Context Response | MS Time Zone                             | 不携带按协议定义携带按自定义携带 |
| Delete PDP Context Response | User Location Information                | 不携带按协议定义携带按自定义携带 |
| Delete PDP Context Response | MS Time Zone                             | 不携带按协议定义携带按自定义携带 |
| Delete PDP Context Request  | User Location Information                | 不携带按协议定义携带按自定义携带 |
| Delete PDP Context Request  | MS Time Zone                             | 不携带按协议定义携带按自定义携带 |

| 消息类型                       | 信元类型        | APNOI大小写            |
|:---------------------------|:------------|:--------------------|
| SGSN Context Response      | PDP Context | 缺省值SGSN小写SGSN和MME小写 |
| Forward Relocation Request | PDP Context | 缺省值SGSN小写SGSN和MME小写 |

| 消息类型                       | 信元类型         | 是否支持COMMON FLAGS   |
|:---------------------------|:-------------|:-------------------|
| Create PDP Context Request | Common Flags | NOYES              |
| Update PDP Context Request | Common Flags | NOYES              |

#### 本地用户权限

manage-ug；system-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

#### 参数说明

| 参数标识       | 参数名称                                   | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|:-----------|:---------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MSGCLS     | 消息分类                                   | 可选必选说明：必选参数 参数含义：该参数用于指示消息分类。 数据来源：整网规划 取值范围：“PM(路径管理)”“TM(隧道管理)”“MM(移动管理)” 默认值：无  说明： 暂时不支持“PM(路径管理)”的消息类别。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| MMMSGTYPE  | 消息类型                                   | 可选必选说明：条件必选参数 参数含义：该参数用于指示消息分类为移动管理时的消息类型。 前提条件：当“MSGCLS”取值为“MM(移动管理)”时，该参数有效。 数据来源：整网规划 取值范围：“SGSN_CONTEXT_RESP(SGSN Context Response)”“FWD_RLC_REQ(Forward Relocation Request)”“FORWARD_SRNS_CONTEXT(Forward Srns Context)” 默认值：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| TMMSGTYPE  | 消息类型                                   | 可选必选说明：条件必选参数 参数含义：该参数用于指示消息分类为隧道管理时的消息类型。 前提条件：当“MSGCLS”取值为“TM(隧道管理)”时，该参数有效。 数据来源：整网规划 取值范围：“CREATE_PDP_CONTEXT_REQUEST(Create PDP Context Request)”“UPDATE_PDP_CONTEXT_REQUEST(Update PDP Context Request)”“UPDATE_PDP_CONTEXT_RESPONSE(Update PDP Context Response)”“DELETE_PDP_CONTEXT_RESPONSE(Delete PDP Context Response)”“DELETE_PDP_CONTEXT_REQUEST(Delete PDP Context Request)” 默认值：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| CTXRSP     | SGSN Context Response的信元类型             | 可选必选说明：条件必选参数 参数含义：该参数用于指示消息类型为SGSN Context Response时的信元类型。 前提条件：当“MMMSGTYPE”取值为“SGSN_CONTEXT_RESP(SGSN Context Response)”时，该参数有效。 数据来源：整网规划 取值范围：“RAB_CONTEXT(RAB Context)”“CHR_CHARACTER(Charging Characteristics)”“IMEISV(IMEISV)”“PDP_CONTEXT(PDP Context)”“PDP_CONTEXT_PRIORITIZATION(PDP Context Prioritization)”“EVOL_ALLOC_RET_PRIORITY_II(Evolved Allocation/Retention Priority II)”“CO_LOC_GGSN_PGW_FQDN(Co-located GGSN-PGW FQDN)”“IMSI(IMSI)” 默认值：无  说明： “IMSI(IMSI)”用于控制当旧侧SGSN向新侧SGSN发送带PTMSI签名不匹配原因值的SGSN Context Response/Context Response消息时，是否携带IMSI信元。                                                                                                                                                                                                                                                                                                                              |
| FWDRLCREQ  | Forward Relocation Request的信元类型        | 可选必选说明：条件必选参数 参数含义：该参数用于指示消息类型为Forward Relocation Request时的信元类型。 前提条件：当“MMMSGTYPE”取值为“FWD_RLC_REQ(Forward Relocation Request)”时，该参数有效。 数据来源：整网规划 取值范围：“CHR_CHARACTER(Charging Characteristics)”“IMEISV(IMEISV)”“PDP_CONTEXT(PDP Context)”“PDP_CONTEXT_PRIORITIZATION(PDP Context Prioritization)”“SELECTED_PLMN_ID(Selected PLMN ID)”：控制LTE到UMTS的系统切换流程，Forward Relocation Request消息是否携带Selected PLMN字段。“EVOL_ALLOC_RET_PRIORITY_II(Evolved Allocation/Retention Priority II)”“CO_LOC_GGSN_PGW_FQDN(Co-located GGSN-PGW FQDN)”“UE_NETWORK_CAPABILITY(UE Network Capability)”“SRVCCMMCTXT(Additional MM context for SRVCC)”“SRVCCFLG(Additional flags for SRVCC)”“STN-SR(Session Transfer Number for SRVCC)”“C-MSISDN(Correlation MSISDN)”“EXTENDED_RANAP_CAUSE(Extended RANAP Cause)”“ENODEB_ID(eNodeB ID)” 默认值：无                                                                                      |
| FWDSRNSCTX | Forward Srns Context的信元类型              | 可选必选说明：条件必选参数 参数含义：该参数用于指示消息类型为Forward Srns Context时的信元类型。 前提条件：当“MMMSGTYPE”取值为“FORWARD_SRNS_CONTEXT(Forward Srns Context)”时，该参数有效。 数据来源：整网规划 取值范围：“SOURCE_RNC_PDCP_CONTEXT(Source RNC PDCP Context)” 默认值：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| CRTPDPREQ  | Create PDP Context Request信元类型         | 可选必选说明：条件必选参数 参数含义：该参数用于指示消息类型为Create PDP Context Request时的信元类型。 前提条件：当“TMMSGTYPE”取值为“CREATE_PDP_CONTEXT_REQUEST(Create PDP Context Request)”时，该参数有效。 数据来源：整网规划 取值范围：“COMMON_FLAGS(Common Flags)”“UPSELIND(UP Function Selection Indication Flag)” 默认值：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| UPDPDPREQ  | Update PDP Context Request信元类型         | 可选必选说明：条件必选参数 参数含义：该参数用于指示消息类型为Update PDP Context Request时的信元类型。 前提条件：当“TMMSGTYPE”取值为“UPDATE_PDP_CONTEXT_REQUEST(Update PDP Context Request)”时，该参数有效。 数据来源：整网规划 取值范围：“COMMON_FLAGS(Common Flags)” 默认值：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| UPDPDPRES  | Update PDP Context Response信元类型        | 可选必选说明：条件必选参数 参数含义：该参数用于指示消息类型为Update PDP Context Response时的信元类型。 前提条件：当“TMMSGTYPE”取值为“UPDATE_PDP_CONTEXT_RESPONSE(Update PDP Context Response)”时，该参数有效。 数据来源：整网规划 取值范围：ULI(User Location Information)TZ(MS Time Zone) 默认值：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| DELPDPRES  | Delete PDP Context Response信元类型        | 可选必选说明：条件必选参数 参数含义：该参数用于指示消息类型为Delete PDP Context Response时的信元类型。 前提条件：当“TMMSGTYPE”取值为“DELETE_PDP_CONTEXT_RESPONSE(Delete PDP Context Response)”时，该参数有效。 数据来源：整网规划 取值范围：ULI(User Location Information)TZ(MS Time Zone) 默认值：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| DELPDPREQ  | Delete PDP Context Request信元类型         | 可选必选说明：条件必选参数 参数含义：该参数用于指示消息类型为Delete PDP Context Request时的信元类型。 前提条件：当“TMMSGTYPE”取值为“DELETE_PDP_CONTEXT_REQUEST(Delete PDP Context Request)”时，该参数有效。 数据来源：整网规划 取值范围：TZ(MS Time Zone) 默认值：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| INCLUDE    | 携带方式                                   | 可选必选说明：条件必选参数 参数含义：该参数用于控制在SGSN发送的GTP消息中，是否允许携带特定的可选信元。 前提条件：当“FWDSRNSCTX”取值为“SOURCE_RNC_PDCP_CONTEXT(Source RNC PDCP Context)”，或者“CTXRSP”取值不为“PDP_CONTEXT(PDP Context)”，或者“FWDRLCREQ”取值不为“PDP_CONTEXT(PDP Context)”，或者“UPDPDPRES”取值为“ULI(User Location Information)”、“TZ(MS Time Zone)”，或者“DELPDPRES”取值为“ULI(User Location Information)”、“TZ(MS Time Zone)”，或者“DELPDPREQ”取值为“TZ(MS Time Zone)”时，该参数有效。 数据来源：整网规划 取值范围：“NOT_CARRY(不携带)”“PRO_DEFINE(按协议定义携带)”“SELF_DEFINE(按自定义携带)” 默认值：无 配置原则：取值为“NOT_CARRY(不携带)”时，表示在SGSN发送的GTP消息中，不携带特定的可选信元。取值为“PRO_DEFINE(按协议定义携带)”时，表示在SGSN发送的GTP消息中，携带特定的可选信元。取值为“SELF_DEFINE(按自定义携带)”：UNC暂时不支持这种携带方式。  说明： 当“FWDRLCREQ”取值为“SRVCCMMCTXT(Additional MM context for SRVCC)”、“SRVCCFLG(Additional flags for SRVCC)”、“STN-SR(Session Transfer Number for SRVCC)”、“C-MSISDN(Correlation MSISDN)”、“EXTENDED_RANAP_CAUSE(Extended RANAP Cause)”中的某一个时，该参数为条件必选，其余情况为条件可选 |
| APNOICASE  | APNOI大小写                               | 可选必选说明：条件必选参数 参数含义：该参数用于控制Inter RAU或Relocation流程中，是否将旧侧SGSN或旧侧MME在发送给新侧的GTP-C V0/V1协议消息SGSN Context Response或Forward Relocation Request中携带的APNOI强制转换成小写格式。 前提条件：当“CTXRSP”或者“FWDRLCREQ”取值为“PDP_CONTEXT(PDP Context)”时，该参数有效。 数据来源：整网规划 取值范围：“DEFAULT(缺省值)”“LOWERCASE(SGSN小写)”“LOWERCASEGUL(SGSN和MME小写)” 默认值：无 配置原则：取值为“DEFAULT(缺省值)”时，旧侧SGSN和旧侧MME均不转换成小写，其大小写格式根据系统配置情况发送。取值为“LOWERCASE(SGSN小写)”时，旧侧SGSN发送GTP-C V0/V1协议消息SGSN Context Response或Forward Relocation Request时将APNOI转换成小写。MME不转换，MME的大小写格式根据系统配置情况发送。取值为“LOWERCASEGUL(SGSN和MME小写)”时，旧侧SGSN和旧侧MME发送GTP-C V0/V1协议消息SGSN Context Response或Forward Relocation Request时均将APNOI转换成小写。                                                                                                                                                                                                                                                            |
| CMFLG      | 是否支持Common Flags信元                     | 可选必选说明：条件必选参数 参数含义：该参数用于控制在SGSN发送的GTP消息中，是否支持Common Flags信元。 前提条件：当“CRTPDPREQ”或者“UPDPDPREQ”取值为“COMMON_FLAGS(Common Flags)”时，该参数有效。 数据来源：整网规划 取值范围：“NO(No)”“YES(Yes)” 默认值：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| UPSELFLAG  | UP Function Selection Indication Flags | 可选必选说明：条件必选参数 参数含义：该参数用于指定信元类型为UP Function Selection Indication Flag时允许携带的标志位。 前提条件：当“CRTPDPREQ”取值为“UPSELIND(UP Function Selection Indication Flag)”时，该参数有效。 数据来源：整网规划 取值范围：“DCNR(Dual connectivity with NR) ” 默认值：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |

#### 使用实例

修改一条GTP-C V0/V1协议兼容性配置，将消息分类为MM(移动管理)，消息类型为SGSN\_CONTEXT\_RESP(SGSN Context Response)，信元类型为RAB\_CONTEXT(RAB Context)的配置记录的携带方式修改为PRO\_DEFINE(按协议定义携带)：

MOD GTPCCMPT: MSGCLS=MM, MMMSGTYPE=SGSN\_CONTEXT\_RESP, CTXRSP=RAB\_CONTEXT, INCLUDE=PRO\_DEFINE;