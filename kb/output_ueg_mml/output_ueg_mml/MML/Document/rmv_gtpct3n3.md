# 删除GTP-C T3N3参数（RMV GTPCT3N3）

- 命令功能
- 注意事项
- 参数说明
- 使用实例

## 命令功能

**适用NF：SGW-C、PGW-C、AMF、GGSN**

该命令用于删除GTP-C T3N3参数配置。

## 注意事项

- 该命令执行后立即生效。

- NODETYPE参数分别为SGW、PGW、GGSN、AMF时，对应的SGWMSGTYPE、PGWMSGTYPE、GGSNMSGTYPE、AMFMSGTYPE、SPGWMSGTYPE参数为ALL是系统初始记录，只能修改，不允许添加。
- 当SET AMFN26PLCY命令中N26ITFMODE取值为“COMBINE”时，当前命令无效，请使用命令SET T3N3配置。

#### 操作用户权限

G\_1，管理员级别命令组；G\_2，操作员级别命令组

## 参数说明

| 参数标识        | 参数名称       | 参数说明                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
|:------------|:-----------|:------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| NODETYPE    | 网元类型       | 可选必选说明：必选参数  参数含义：该参数用于指定设置T3N3参数的网元类型。  数据来源：全网规划 取值范围： SGW（SGW）PGW（PGW）GGSN（GGSN）AMF（AMF）SPGW（SPGW）  默认值：无  配置原则：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| SGWMSGTYPE  | SGW网元消息类型  | 可选必选说明：该参数在"NODETYPE"配置为"SGW"时为条件必选参数。  参数含义：该参数用于指定设置T3N3的SGW网元的消息类型。  数据来源：全网规划 取值范围： CRT_SESSION_REQ（Create Session Request）MOD_BEARER_REQ（Modify Bearer Request）DEL_SESSION_REQ（Delete Session Request）MOD_BEARER_CMD（Modify Bearer Command）CRT_BEARER_REQ（Create Bearer Request）UPD_BEARER_REQ（Update Bearer Request）DEL_BEARER_CMD（Delete Bearer Command）DEL_BEARER_REQ（Delete Bearer Request）DWLNK_DATA_NOTF（Downlink Data Notification）RMT_UE_RPT_NOTF（Remote UE Report Notification）CHG_NOTIF_REQ（Change Notification Request）BEARER_RES_CMD（Bearer Resource Command）SUSPEND_NOTIF（Suspend Notification）RESUME_NOTIF（Resume Notification）PGW_RST_NOTF（PGW Restart Notification）PGWDN_TRIG_NOTF（PGW Downlink Triggering Notification）ALL（All Messages）  默认值：无  配置原则：无 |
| PGWMSGTYPE  | PGW网元消息类型  | 可选必选说明：该参数在"NODETYPE"配置为"PGW"时为条件必选参数。  参数含义：参数用于指定设置T3N3的PGW网元的消息类型。  数据来源：全网规划 取值范围： CRT_BEARER_REQ（Create Bearer Request）UPD_BEARER_REQ（Update Bearer Request）DEL_BEARER_REQ（Delete Bearer Request）PGWDN_TRIG_NOTF（PGW Downlink Triggering Notification）ALL（All Messages）  默认值：无  配置原则：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| GGSNMSGTYPE | GGSN网元消息类型 | 可选必选说明：该参数在"NODETYPE"配置为"GGSN"时为条件必选参数。  参数含义：该参数用于指定设置T3N3的GGSN网元的消息类型。  数据来源：全网规划 取值范围： UPD_PDP_CTX_REQ（Update PDP Context Request）DEL_PDP_CTX_REQ（Delete PDP Context Request）INT_PDP_CTX_REQ（Initiate PDP Context Activation Request）ALL（All Messages）  默认值：无  配置原则：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| AMFMSGTYPE  | AMF网元消息类型  | 可选必选说明：该参数在"NODETYPE"配置为"AMF"时为条件必选参数。  参数含义：该参数用于指定设置T3N3的AMF网元的消息类型。  数据来源：全网规划 取值范围： IDENTIF_REQ（Identification Request）CONTEXT_REQ（Context Request）CONTEXT_RSP（Context Response）FWDRELOCATE_REQ（Forward Relocation Request）FWRELO_COM_NOTF（Forward Relocation Complete Notification）RELOC_CANCL_REQ（Relocation Cancel Request）ALL（All Messages）  默认值：无  配置原则：无                                                                                                                                                                                                                                                                                                                                                                                                            |
| SPGWMSGTYPE | SPGW网元消息类型 | 可选必选说明：该参数在"NODETYPE"配置为"SPGW"时为条件必选参数。  参数含义：参数用于指定设置T3N3的SPGW网元的消息类型。  数据来源：全网规划 取值范围： CRT_BEARER_REQ（Create Bearer Request）UPD_BEARER_REQ（Update Bearer Request）DWLNK_DATA_NOTF（Downlink Data Notification）ALL（All Messages）DEL_BEARER_REQ（Delete Bearer Request）  默认值：无  配置原则：无                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

## 使用实例

删除网元类型为SGW的Create Session Request消息的T3N3记录：

```
RMV GTPCT3N3:  NODETYPE=SGW, SGWMSGTYPE=CRT_SESSION_REQ;
```