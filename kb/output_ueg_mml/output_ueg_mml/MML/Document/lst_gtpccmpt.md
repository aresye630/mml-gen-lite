# 查询GTP-C V0/V1协议兼容性配置(LST GTPCCMPT)

- 命令功能
- 注意事项
- 本地用户权限
- 网管用户权限
- 参数说明
- 使用实例
- 输出结果说明

#### 命令功能

**适用网元：SGSN、MME**

此命令用于查询GTP-C V0/V1协议兼容性配置。

#### 注意事项

此命令执行后立即生效。

#### 本地用户权限

manage-ug；system-ug；monitor-ug

#### 网管用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组；G\_3，用户级别命令组

#### 参数说明

| 参数标识       | 参数名称                            | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|:-----------|:--------------------------------|:--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| MSGCLS     | 消息分类                            | 可选必选说明：可选参数 参数含义：该参数用于指示消息分类。 取值范围：“PM(路径管理)”“TM(隧道管理)”“MM(移动管理)” 默认值：无  说明： 暂时不支持“PM(路径管理)”的消息类别。                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| MMMSGTYPE  | 消息类型                            | 可选必选说明：条件可选参数 参数含义：该参数用于指示消息分类为移动管理时的消息类型。 前提条件：当“MSGCLS”取值为“MM(移动管理)”时，该参数有效。 取值范围：“SGSN_CONTEXT_RESP(SGSN Context Response)”“FWD_RLC_REQ(Forward Relocation Request)”“FORWARD_SRNS_CONTEXT(Forward Srns Context)” 默认值：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| TMMSGTYPE  | 消息类型                            | 可选必选说明：条件可选参数 参数含义：该参数用于指示消息分类为隧道管理时的消息类型。 前提条件：当“MSGCLS”取值为“TM(隧道管理)”时，该参数有效。 取值范围：“CREATE_PDP_CONTEXT_REQUEST(Create PDP Context Request)”“UPDATE_PDP_CONTEXT_REQUEST(Update PDP Context Request)”“UPDATE_PDP_CONTEXT_RESPONSE(Update PDP Context Response)”“DELETE_PDP_CONTEXT_RESPONSE(Delete PDP Context Response)”“DELETE_PDP_CONTEXT_REQUEST(Delete PDP Context Request)” 默认值：无                                                                                                                                                                                                                                                                                                                                                                                                                  |
| CTXRSP     | SGSN Context Response的信元类型      | 可选必选说明：条件可选参数 参数含义：该参数用于指示消息类型为SGSN Context Response时的信元类型。 前提条件：当“MMMSGTYPE”取值为“SGSN_CONTEXT_RESP(SGSN Context Response)”时，该参数有效。 取值范围：“RAB_CONTEXT(RAB Context)”“CHR_CHARACTER(Charging Characteristics)”“IMEISV(IMEISV)”“PDP_CONTEXT(PDP Context)”“PDP_CONTEXT_PRIORITIZATION(PDP Context Prioritization)”“EVOL_ALLOC_RET_PRIORITY_II(Evolved Allocation/Retention Priority II)”“CO_LOC_GGSN_PGW_FQDN(Co-located GGSN-PGW FQDN)”“IMSI(IMSI)” 默认值：无                                                                                                                                                                                                                                                                                                                                                   |
| FWDRLCREQ  | Forward Relocation Request的信元类型 | 可选必选说明：条件可选参数 参数含义：该参数用于指示消息类型为Forward Relocation Request时的信元类型。 前提条件：当“MMMSGTYPE”取值为“FWD_RLC_REQ(Forward Relocation Request)”时，该参数有效。 取值范围：“CHR_CHARACTER(Charging Characteristics)”“IMEISV(IMEISV)”“PDP_CONTEXT(PDP Context)”“PDP_CONTEXT_PRIORITIZATION(PDP Context Prioritization)”“SELECTED_PLMN_ID(Selected PLMN ID)”：控制LTE到UMTS的系统切换流程，Forward Relocation Request消息是否携带Selected PLMN字段。“EVOL_ALLOC_RET_PRIORITY_II(Evolved Allocation/Retention Priority II)”“CO_LOC_GGSN_PGW_FQDN(Co-located GGSN-PGW FQDN)”“UE_NETWORK_CAPABILITY(UE Network Capability)”“SRVCCMMCTXT(Additional MM context for SRVCC)”“SRVCCFLG(Additional flags for SRVCC)”“STN-SR(Session Transfer Number for SRVCC)”“C-MSISDN(Correlation MSISDN)”“EXTENDED_RANAP_CAUSE(Extended RANAP Cause)”“ENODEB_ID(eNodeB ID)” 默认值：无 |
| FWDSRNSCTX | Forward Srns Context的信元类型       | 可选必选说明：条件可选参数 参数含义：该参数用于指示消息类型为Forward Srns Context时的信元类型。 前提条件：当“MMMSGTYPE”取值为“FORWARD_SRNS_CONTEXT(Forward Srns Context)”时，该参数有效。 取值范围：“SOURCE_RNC_PDCP_CONTEXT(Source RNC PDCP Context)” 默认值：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| CRTPDPREQ  | Create PDP Context Request信元类型  | 可选必选说明：条件可选参数 参数含义：该参数用于指示消息类型为Create PDP Context Request时的信元类型。 前提条件：当“TMMSGTYPE”取值为“CREATE_PDP_CONTEXT_REQUEST(Create PDP Context Request)”时，该参数有效。 取值范围：“COMMON_FLAGS(Common Flags)” 默认值：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| UPDPDPREQ  | Update PDP Context Request信元类型  | 可选必选说明：条件可选参数 参数含义：该参数用于指示消息类型为Update PDP Context Request时的信元类型。 前提条件：当“TMMSGTYPE”取值为“UPDATE_PDP_CONTEXT_REQUEST(Update PDP Context Request)”时，该参数有效。 取值范围：“COMMON_FLAGS(Common Flags)” 默认值：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| UPDPDPRES  | Update PDP Context Response信元类型 | 可选必选说明：条件可选参数 参数含义：该参数用于指示消息类型为Update PDP Context Response时的信元类型。 前提条件：当“TMMSGTYPE”取值为“UPDATE_PDP_CONTEXT_RESPONSE(Update PDP Context Response)”时，该参数有效。 数据来源：整网规划 取值范围：ULI(User Location Information)TZ(MS Time Zone) 默认值：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| DELPDPRES  | Delete PDP Context Response信元类型 | 可选必选说明：条件可选参数 参数含义：该参数用于指示消息类型为Delete PDP Context Response时的信元类型。 前提条件：当“TMMSGTYPE”取值为“DELETE_PDP_CONTEXT_RESPONSE(Delete PDP Context Response)”时，该参数有效。 数据来源：整网规划 取值范围：ULI(User Location Information)TZ(MS Time Zone) 默认值：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| DELPDPREQ  | Delete PDP Context Request信元类型  | 可选必选说明：条件可选参数 参数含义：该参数用于指示消息类型为Delete PDP Context Request时的信元类型。 前提条件：当“TMMSGTYPE”取值为“DELETE_PDP_CONTEXT_REQUEST(Delete PDP Context Request)”时，该参数有效。 数据来源：整网规划 取值范围：TZ(MS Time Zone) 默认值：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

#### 使用实例

查询GTP-C V0/V1协议兼容性配置：

LST GTPCCMPT:;

```
%%LST GTPCCMPT:;%%
RETCODE = 0  操作成功。

操作结果如下
------------
                    索引  =  0
                消息分类  =  移动管理
                消息类型  =  SGSN Context Response
                信元类型  =  PDP Context
                携带方式  =  NULL
             APNOI大小写  =  SGSN小写
是否支持Common Flags信元  =  NULL 
           UP功能选择指示 = NULL
(结果个数 = 1)

---    END
```

#### 输出结果说明

参见**ADD GTPCCMPT**命令的参数说明。