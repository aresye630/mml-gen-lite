---
id: ''
name: Gx Failover功能
ne_type: UNC
type: feature
description: 当用户初始激活或进行业务时，GGSN/PGW-C发送CCR请求消息给PCRF，在指定消息重传时间间隔时间内未收到PCRF的响应消息，即可判断PCRF服务器状态异常。如果**ADD PCRFGROUP**命令中“FAILOVERSW”参数值为“ENABLE”，则进行failover处理；否则按照**SET PCCFAILACTION**和**ADD PCCTEMPLATE**命令设置的动作进行处理。  GGSN/PGW-C向备PCRF重发消息，如果备PCRF也没有响应或者备PCRF因状态异常、消息发送速率超过wal值等导致不可用，可以根据**SET PCCFAILACTION**和**ADD PCCTEMPLATE**命令配置情况去活用户或者转为非PCC用户/本地PCC用户继续进行业务。  实现failover功能需要具备以下几个条件：  * PCRF采用负荷分担或者主备组网模式。 * GGSN/PGW-C本地配置支持failover功能。 * 主备PCRF存在LOCALHOSTNAME相同的Diameter链路组。 * PCRF支持failover功能，在PCRF使用failover时，PCRF发送给GGSN/PGW-C的CCA消息中携带的CC-Session-Failover AVP支持failover。 * PCRF支持热备份功能，即PCRF支持CC session的同步。    如果PCRF不支持热备份功能，为了保证PCRF切换后用户不掉线，GGSN/PGW-C需支持failover增强功能。备PCRF可根据GGSN/PGW-C重发的CCR-U中携带的信息重建IP-CAN会话，并发送CCA-U消息给GGSN/PGW-C，通过CCA-U消息中携带的会话重建AVP中的值为DELETE\_DEFAULT\_AND\_DEDICATED\_BEARER\_RULES (2)，指示UNC和UDG删除该用户的所有已安装规则及专有承载/二次PDP上下文，并为缺省承载/一次PDP上下文下发新的规则，相当于完成了一次初始激活。  适用于GGSN、PGW-C。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","智能PCC解决方案","WSFD-109101 PCC基本功能","PCC基本功能（2G/3G/4G，基于Gx接口）","激活PCC基本功能","Gx Failover功能"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当用户初始激活或进行业务时，GGSN/PGW-C发送CCR请求消息给PCRF，在指定消息重传时间间隔时间内未收到PCRF的响应消息，即可判断PCRF服务器状态异常。如果**ADD PCRFGROUP**命令中“FAILOVERSW”参数值为“ENABLE”，则进行failover处理；否则按照**SET PCCFAILACTION**和**ADD PCCTEMPLATE**命令设置的动作进行处理。GGSN/PGW-C向备PCRF重发消息，如果备PCRF也没有响应或者备PCRF因状态异常、消息发送速率超过wal值等导致不可用，可以根据**SET PCCFAILACTION**和**ADD PCCTEMPLATE**命令配置情况去活用户或者转为非PCC用户/本地PCC用户继续进行业务。实现failover功能需要具备以下几个条件：* PCRF采用负荷分担或者主备组网模式。* GGSN/PGW-C本地配置支持failover功能。* 主备PCRF存在LOCALHOSTNAME相同的Diameter链路组。* PCRF支持failover功能，在PCRF使用failover时，PCRF发送给GGSN/PGW-C的CCA消息中携带的CC-Session-Failover AVP支持failover。* PCRF支持热备份功能，即PCRF支持CC session的同步。  如果PCRF不支持热备份功能，为了保证PCRF切换后用户不掉线，GGSN/PGW-C需支持failover增强功能。备PCRF可根据GGSN/PGW-C重发的CCR-U中携带的信息重建IP-CAN会话，并发送CCA-U消息给GGSN/PGW-C，通过CCA-U消息中携带的会话重建AVP中的值为DELETE\_DEFAULT\_AND\_DEDICATED\_BEARER\_RULES (2)，指示UNC和UDG删除该用户的所有已安装规则及专有承载/二次PDP上下文，并为缺省承载/一次PDP上下文下发新的规则，相当于完成了一次初始激活。适用于GGSN、PGW-C。

## 必备事项
前提条件

前提条件

* 请仔细阅读PCC基本功能（2G/3G/4G，基于Gx接口）。
* 完成配置与PCRF对接数据。
* 部署主备PCRF组，且PCRF组支持failover，即在CCA消息中CC-Session-Failover AVP支持failover。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_pcrf_list:
      type: items
      properties:
        HOSTNAME:
          name: 'PCRF主机名'
          type: string
          maxLength: 127
          required: true
          description: '配置PCRF的基本信息。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        REALMNAME:
          name: 'PCRF域名'
          type: string
          maxLength: 127
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_diampeeraddr_list:
      type: items
      properties:
        HOSTNAME:
          name: '主机名称'
          type: string
          maxLength: 127
          required: true
          description: '配置PCRF的IP地址。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        ADDRTYPE:
          name: '地址类型'
          type: string
          enum:
          - IPv4
          - IPv6
          - SCTP
          required: true
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        IPV4ADDRESS:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        IPV6ADDRESS:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PORT:
          name: '端口号'
          type: integer
          minimum: 1
          maximum: 65534
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 3868
        SCTPENDPOINT:
          name: 'SCTP端点名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_pcrfgroup_list:
      type: items
      properties:
        PCRFGRPNAME:
          name: 'PCRF组名称'
          type: string
          maxLength: 128
          required: true
          description: 'PCRF group信息。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        LOADBALANCEMODE:
          name: '负荷分担模式'
          type: string
          enum:
          - LOAD_BALANCE
          - MASTER_SLAVE
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: MASTER_SLAVE
        FAILOVERSW:
          name: '宕机备份开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
    add_pcrfbindgrp_list:
      type: items
      properties:
        PCRFGRPNAME:
          name: 'PCRF组名称'
          type: string
          maxLength: 128
          required: true
          description: '添加PCRF到PCRF分组中。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PCRFHOSTNAME:
          name: 'PCRF主机名称'
          type: string
          maxLength: 127
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    set_masterpcrf_list:
      type: items
      properties:
        PCRFGRPNAME:
          name: 'PCRF组名称'
          type: string
          maxLength: 128
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MASTERPCRF:
          name: '主用PCRF主机名'
          type: string
          maxLength: 127
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_pcctimer_list:
      type: items
      properties:
        APPRETRYTIMEOUT:
          name: '应用层重传时间间隔（秒）'
          type: integer
          minimum: 0
          maximum: 10
          required: false
          description: 'Tx定时器。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_pcrfgrpbndapn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DEFAULTFLAG:
          name: '缺省标记'
          type: string
          enum:
          - DEFAULT
          - IMSI_MSISDN_SEG
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PCRFGRPNAME:
          name: 'PCRF组名称'
          type: string
          maxLength: 128
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMSIMSISDNSEG:
          name: 'IMSI/MSISDN号段名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_smfsoftpara_list:
      type: items
      properties:
        DT:
          name: '数据类型'
          type: string
          enum:
          - Dw
          - Bit
          - Byte
          - String
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BITNUM:
          name: 'Bit索引'
          type: integer
          minimum: 1
          maximum: 4000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BITVALUE:
          name: 'Bit值'
          type: integer
          minimum: 0
          maximum: 1
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BYTENUM:
          name: 'Byte索引'
          type: integer
          minimum: 1
          maximum: 1200
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BYTEVALUE:
          name: 'Byte值'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DWORDNUM:
          name: 'Dword索引'
          type: integer
          minimum: 1
          maximum: 1500
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DWORDVALUE:
          name: 'Dword值'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        STRINGNUM:
          name: 'String索引'
          type: integer
          minimum: 1
          maximum: 30
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        STRINGVALUE:
          name: 'String值'
          type: string
          minLength: 1
          maxLength: 64
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_pccmsgattr_list:
      type: items
      properties:
        MSGTYPE:
          name: '消息类型'
          type: string
          enum:
          - CCRI
          - CCRT
          - CCRU
          - RAA
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MSISDN:
          name: 'Subscription-Id-Type和Subscription-Id携带MSISDN开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CALLEDSTATIONID:
          name: 'Called-Station-ID AVP开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USREQUIPINFO:
          name: 'User-Equipment-Info AVP开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FRAMEDIPADDRESS:
          name: 'Framed-IP-Address AVP开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FRAMEDIPV6PREF:
          name: 'Framed-IPv6-Prefix AVP开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ANCHARGINGADDR:
          name: 'Access-Network-Charging-Address AVP开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INVALID
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ANCHARGINGID:
          name: 'Access-Network-Charging-Identifier-Value AVP开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CHARGINGRULE:
          name: 'Charging-Rule-Base-Name和Charging-Rule-Name子AVP开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CLHONEGOBCM:
          name: 'CL切换更新时携带Network-Request-Support AVP开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DFTEPSBEARERQOS:
          name: 'Default-EPS-Bearer-QoS AVP开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DYNADDRFLG:
          name: 'Dynamic-Address-Flag AVP开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DYNADDRFLGEXT:
          name: 'Dynamic-Address-Flag-Extension AVP开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EXPERRESULTCODE:
          name: 'Experiment-Result-Code AVP开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        G3CC:
          name: '3GPP-Charging-Characteristics AVP开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        G3GGSNADDR:
          name: '3GPP-GGSN-Address AVP开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        G3PPRATTYPE:
          name: '3GPP-RAT-Type AVP开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        G3SELECTMODE:
          name: '3GPP-Selection-Mode AVP开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        G3SGSNADDR:
          name: '3GPP-SGSN-Address AVP开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        G3SGSNMCCMNC:
          name: '3GPP-SGSN-MCC-MNC AVP开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        G3ULI:
          name: '3GPP-User-Location-Info AVP开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMSI:
          name: 'Subscription-Id-Type和Subscription-Id携带IMSI开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MSTIMEZONE:
          name: '3GPP-MS-TimeZone AVP开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NETLOCACCESS:
          name: 'NetLoc-Access-Support AVP开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PDNCCHARGINGID:
          name: 'PDN-Connection-Charging-ID AVP开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        QOSINFORMATION:
          name: 'QoS-Information AVP开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RATTYPE:
          name: 'RAT-Type AVP开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ULITIME:
          name: 'User-Location-Info-Time AVP开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_pccmsgattr_list_1:
      type: items
      properties:
        MSGTYPE:
          name: '消息类型'
          type: string
          enum:
          - CCRI
          - CCRT
          - CCRU
          - RAA
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MSISDN:
          name: 'Subscription-Id-Type和Subscription-Id携带MSISDN开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CALLEDSTATIONID:
          name: 'Called-Station-ID AVP开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ANCHARGINGADDR:
          name: 'Access-Network-Charging-Address AVP开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INVALID
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ANCHARGINGID:
          name: 'Access-Network-Charging-Identifier-Value AVP开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CHARGINGRULE:
          name: 'Charging-Rule-Base-Name和Charging-Rule-Name子AVP开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CLHONEGOBCM:
          name: 'CL切换更新时携带Network-Request-Support AVP开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DFTEPSBEARERQOS:
          name: 'Default-EPS-Bearer-QoS AVP开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DYNADDRFLG:
          name: 'Dynamic-Address-Flag AVP开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DYNADDRFLGEXT:
          name: 'Dynamic-Address-Flag-Extension AVP开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EXPERRESULTCODE:
          name: 'Experiment-Result-Code AVP开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FRAMEDIPADDRESS:
          name: 'Framed-IP-Address AVP开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FRAMEDIPV6PREF:
          name: 'Framed-IPv6-Prefix AVP开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        G3CC:
          name: '3GPP-Charging-Characteristics AVP开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        G3GGSNADDR:
          name: '3GPP-GGSN-Address AVP开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        G3PPRATTYPE:
          name: '3GPP-RAT-Type AVP开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        G3SELECTMODE:
          name: '3GPP-Selection-Mode AVP开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        G3SGSNADDR:
          name: '3GPP-SGSN-Address AVP开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        G3SGSNMCCMNC:
          name: '3GPP-SGSN-MCC-MNC AVP开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        G3ULI:
          name: '3GPP-User-Location-Info AVP开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMSI:
          name: 'Subscription-Id-Type和Subscription-Id携带IMSI开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MSTIMEZONE:
          name: '3GPP-MS-TimeZone AVP开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NETLOCACCESS:
          name: 'NetLoc-Access-Support AVP开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PDNCCHARGINGID:
          name: 'PDN-Connection-Charging-ID AVP开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        QOSINFORMATION:
          name: 'QoS-Information AVP开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RATTYPE:
          name: 'RAT-Type AVP开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ULITIME:
          name: 'User-Location-Info-Time AVP开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USREQUIPINFO:
          name: 'User-Equipment-Info AVP开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_pcrf_list:
    - HOSTNAME: 'pcrf1'
      REALMNAME: 'host1.example.com'
    add_diampeeraddr_list:
    - HOSTNAME: 'pcrf1'
      ADDRTYPE: IPv4
      IPV4ADDRESS: '10.10.10.1'
      IPV6ADDRESS: ''
      PORT: 3868
      SCTPENDPOINT: ''
    add_pcrfgroup_list:
    - PCRFGRPNAME: 'pcrf.group.1'
      LOADBALANCEMODE: MASTER_SLAVE
      FAILOVERSW: ENABLE
    add_pcrfbindgrp_list:
    - PCRFGRPNAME: 'pcrf.group.1'
      PCRFHOSTNAME: 'pcrf1'
    set_masterpcrf_list:
    - PCRFGRPNAME: ''
      MASTERPCRF: ''
    set_pcctimer_list:
    - APPRETRYTIMEOUT: 10
    add_pcrfgrpbndapn_list:
    - APN: 'apn1'
      DEFAULTFLAG: DEFAULT
      PCRFGRPNAME: 'pcrf.group.1'
      IMSIMSISDNSEG: ''
      PRIORITY: ''
    set_smfsoftpara_list:
    - DT: BIT
      BITNUM: 1202
      BITVALUE: 1
      BYTENUM: ''
      BYTEVALUE: ''
      DWORDNUM: ''
      DWORDVALUE: ''
      STRINGNUM: ''
      STRINGVALUE: ''
    set_pccmsgattr_list:
    - MSGTYPE: CCRU
      MSISDN: ENABLE
      CALLEDSTATIONID: ENABLE
      USREQUIPINFO: ENABLE
      FRAMEDIPADDRESS: ENABLE
      FRAMEDIPV6PREF: ENABLE
      ANCHARGINGADDR: ''
      ANCHARGINGID: ''
      CHARGINGRULE: ''
      CLHONEGOBCM: ''
      DFTEPSBEARERQOS: ''
      DYNADDRFLG: ''
      DYNADDRFLGEXT: ''
      EXPERRESULTCODE: ''
      G3CC: ''
      G3GGSNADDR: ''
      G3PPRATTYPE: ''
      G3SELECTMODE: ''
      G3SGSNADDR: ''
      G3SGSNMCCMNC: ''
      G3ULI: ''
      IMSI: ''
      MSTIMEZONE: ''
      NETLOCACCESS: ''
      PDNCCHARGINGID: ''
      QOSINFORMATION: ''
      RATTYPE: ''
      ULITIME: ''
    set_pccmsgattr_list_1:
    - MSGTYPE: CCRT
      MSISDN: ENABLE
      CALLEDSTATIONID: ENABLE
      ANCHARGINGADDR: ''
      ANCHARGINGID: ''
      CHARGINGRULE: ''
      CLHONEGOBCM: ''
      DFTEPSBEARERQOS: ''
      DYNADDRFLG: ''
      DYNADDRFLGEXT: ''
      EXPERRESULTCODE: ''
      FRAMEDIPADDRESS: ''
      FRAMEDIPV6PREF: ''
      G3CC: ''
      G3GGSNADDR: ''
      G3PPRATTYPE: ''
      G3SELECTMODE: ''
      G3SGSNADDR: ''
      G3SGSNMCCMNC: ''
      G3ULI: ''
      IMSI: ''
      MSTIMEZONE: ''
      NETLOCACCESS: ''
      PDNCCHARGINGID: ''
      QOSINFORMATION: ''
      RATTYPE: ''
      ULITIME: ''
      USREQUIPINFO: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 配置PCRF信息。

#### 2.1 配置PCRF信息。重复执行本步骤可增加多个PCRF信息。

```jinja2
{%- for item in add_pcrf_list -%}
    ADD PCRF:
    {#- --- 必选参数 --- -#}
    HOSTNAME="{{item.HOSTNAME}}",
    REALMNAME="{{item.REALMNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_diampeeraddr_list -%}
    ADD DIAMPEERADDR:
    {#- --- 必选参数 --- -#}
    HOSTNAME="{{item.HOSTNAME}}",
    ADDRTYPE={{item.ADDRTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：ADDRTYPE=IPv4 时必选 --- -#}
    {%- if item.ADDRTYPE == 'IPv4' -%}
        IPV4ADDRESS="{{item.IPV4ADDRESS}}",
    {%- endif -%}
    {#- --- 条件必选：ADDRTYPE=IPv6 时必选 --- -#}
    {%- if item.ADDRTYPE == 'IPv6' -%}
        IPV6ADDRESS="{{item.IPV6ADDRESS}}",
    {%- endif -%}
    {#- --- 条件必选：ADDRTYPE=SCTP 时必选 --- -#}
    {%- if item.ADDRTYPE == 'SCTP' -%}
        SCTPENDPOINT="{{item.SCTPENDPOINT}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：ADDRTYPE=IPv4/IPv6 时可选 --- -#}
    {%- if item.ADDRTYPE in ['IPv4', 'IPv6'] -%}
        {%- if item.PORT is not none -%}
            PORT={{item.PORT}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.2 配置PCRF组。

```jinja2
{%- for item in add_pcrfgroup_list -%}
    ADD PCRFGROUP:
    {#- --- 必选参数 --- -#}
    PCRFGRPNAME="{{item.PCRFGRPNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.LOADBALANCEMODE is not none -%}
        LOADBALANCEMODE={{item.LOADBALANCEMODE}},
    {%- endif -%}
    {%- if item.FAILOVERSW is not none -%}
        FAILOVERSW={{item.FAILOVERSW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_pcrfbindgrp_list -%}
    ADD PCRFBINDGRP:
    {#- --- 必选参数 --- -#}
    PCRFGRPNAME="{{item.PCRFGRPNAME}}",
    PCRFHOSTNAME="{{item.PCRFHOSTNAME}}",
    ;
{%- endfor -%}
```

#### 2.3 **可选：**如果PCRF组的工作模式为主备模式，可使用如下命令修改PCRF分组内的缺省主用PCRF。

```jinja2
{%- if is_optional_modify_default_master_pcrf -%}
    {%- for item in set_masterpcrf_list -%}
        SET MASTERPCRF:
        {#- --- 必选参数 --- -#}
        MASTERPCRF="{{item.MASTERPCRF}}",
        PCRFGRPNAME="{{item.PCRFGRPNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

### 3 **可选：**配置PCC定时器的消息重传时间间隔。缺省使用默认值。

```jinja2
{%- if is_optional_configure_pcc_timer_retransmission_interval -%}
    {%- for item in set_pcctimer_list -%}
        SET PCCTIMER:
        {#- --- 可选参数 --- -#}
        {%- if item.APPRETRYTIMEOUT is not none -%}
            APPRETRYTIMEOUT={{item.APPRETRYTIMEOUT}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 4 将指定的PCRF分组绑定到指定APN。

```jinja2
{%- for item in add_pcrfgrpbndapn_list -%}
    ADD PCRFGRPBNDAPN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    DEFAULTFLAG={{item.DEFAULTFLAG}},
    PCRFGRPNAME="{{item.PCRFGRPNAME}}",
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：DEFAULTFLAG=IMSI_MSISDN_SEG 时必选 --- -#}
    {%- if item.DEFAULTFLAG == 'IMSI_MSISDN_SEG' -%}
        IMSIMSISDNSEG="{{item.IMSIMSISDNSEG}}",
    {%- endif -%}
    {#- --- 条件必选：DEFAULTFLAG=IMSI_MSISDN_SEG 时必选 --- -#}
    {%- if item.DEFAULTFLAG == 'IMSI_MSISDN_SEG' -%}
        PRIORITY={{item.PRIORITY}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 **可选：**如果PCRF不支持热备份功能，GGSN/PGW-C上需要开启failover增强功能。

#### 5.1 GGSN/PGW-C上开启failover增强功能。

```jinja2
{%- if is_optional_enable_failover_enhancement -%}
    {%- for item in set_smfsoftpara_list -%}
        SET SMFSOFTPARA:
        {#- --- 必选参数 --- -#}
        DT={{item.DT}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：DT=Bit 时必选 --- -#}
        {%- if item.DT == 'Bit' -%}
            BITNUM={{item.BITNUM}},
        {%- endif -%}
        {#- --- 条件必选：DT=Bit 时必选 --- -#}
        {%- if item.DT == 'Bit' -%}
            BITVALUE={{item.BITVALUE}},
        {%- endif -%}
        {#- --- 条件必选：DT=Byte 时必选 --- -#}
        {%- if item.DT == 'Byte' -%}
            BYTENUM={{item.BYTENUM}},
        {%- endif -%}
        {#- --- 条件必选：DT=Byte 时必选 --- -#}
        {%- if item.DT == 'Byte' -%}
            BYTEVALUE={{item.BYTEVALUE}},
        {%- endif -%}
        {#- --- 条件必选：DT=Dw 时必选 --- -#}
        {%- if item.DT == 'Dw' -%}
            DWORDNUM={{item.DWORDNUM}},
        {%- endif -%}
        {#- --- 条件必选：DT=Dw 时必选 --- -#}
        {%- if item.DT == 'Dw' -%}
            DWORDVALUE={{item.DWORDVALUE}},
        {%- endif -%}
        {#- --- 条件必选：DT=String 时必选 --- -#}
        {%- if item.DT == 'String' -%}
            STRINGNUM={{item.STRINGNUM}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：DT=String 时可选 --- -#}
        {%- if item.DT == 'String' -%}
            {%- if item.STRINGVALUE is not none -%}
                STRINGVALUE="{{item.STRINGVALUE}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 详细描述请参见BIT1202 控制Gx Failover增强功能是否生效。

#### 5.2 配置GGSN/PGW-C发送的CCR-U消息中携带信元Called-Station-ID、User-Equipment-Info、Framed-IP-Address、Framed-IPv6-Prefix，Subscription-Id-Type和Subscription-Id携带MSISDN开关。

```jinja2
{%- if is_optional_enable_failover_enhancement -%}
    {%- for item in set_pccmsgattr_list -%}
        SET PCCMSGATTR:
        {#- --- 必选参数 --- -#}
        MSGTYPE={{item.MSGTYPE}},
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：MSGTYPE=CCRU/CCRT 时可选 --- -#}
        {%- if item.MSGTYPE in ['CCRU', 'CCRT'] -%}
            {%- if item.MSISDN is not none -%}
                MSISDN={{item.MSISDN}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：MSGTYPE=CCRU/CCRT 时可选 --- -#}
        {%- if item.MSGTYPE in ['CCRU', 'CCRT'] -%}
            {%- if item.CALLEDSTATIONID is not none -%}
                CALLEDSTATIONID={{item.CALLEDSTATIONID}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：MSGTYPE=CCRU/CCRT 时可选 --- -#}
        {%- if item.MSGTYPE in ['CCRU', 'CCRT'] -%}
            {%- if item.USREQUIPINFO is not none -%}
                USREQUIPINFO={{item.USREQUIPINFO}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：MSGTYPE=CCRU/CCRT 时可选 --- -#}
        {%- if item.MSGTYPE in ['CCRU', 'CCRT'] -%}
            {%- if item.FRAMEDIPADDRESS is not none -%}
                FRAMEDIPADDRESS={{item.FRAMEDIPADDRESS}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：MSGTYPE=CCRU/CCRT 时可选 --- -#}
        {%- if item.MSGTYPE in ['CCRU', 'CCRT'] -%}
            {%- if item.FRAMEDIPV6PREF is not none -%}
                FRAMEDIPV6PREF={{item.FRAMEDIPV6PREF}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：MSGTYPE=CCRU/CCRT 时可选 --- -#}
        {%- if item.MSGTYPE in ['CCRU', 'CCRT'] -%}
            {%- if item.ANCHARGINGADDR is not none -%}
                ANCHARGINGADDR={{item.ANCHARGINGADDR}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：MSGTYPE=CCRU/CCRT/RAA 时可选 --- -#}
        {%- if item.MSGTYPE in ['CCRU', 'CCRT', 'RAA'] -%}
            {%- if item.ANCHARGINGID is not none -%}
                ANCHARGINGID={{item.ANCHARGINGID}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：MSGTYPE=CCRI 时可选 --- -#}
        {%- if item.MSGTYPE == 'CCRI' -%}
            {%- if item.CHARGINGRULE is not none -%}
                CHARGINGRULE={{item.CHARGINGRULE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：MSGTYPE=CCRU 时可选 --- -#}
        {%- if item.MSGTYPE == 'CCRU' -%}
            {%- if item.CLHONEGOBCM is not none -%}
                CLHONEGOBCM={{item.CLHONEGOBCM}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：MSGTYPE=CCRU 时可选 --- -#}
        {%- if item.MSGTYPE == 'CCRU' -%}
            {%- if item.DFTEPSBEARERQOS is not none -%}
                DFTEPSBEARERQOS={{item.DFTEPSBEARERQOS}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：MSGTYPE=CCRI 时可选 --- -#}
        {%- if item.MSGTYPE == 'CCRI' -%}
            {%- if item.DYNADDRFLG is not none -%}
                DYNADDRFLG={{item.DYNADDRFLG}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：MSGTYPE=CCRI 时可选 --- -#}
        {%- if item.MSGTYPE == 'CCRI' -%}
            {%- if item.DYNADDRFLGEXT is not none -%}
                DYNADDRFLGEXT={{item.DYNADDRFLGEXT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：MSGTYPE=RAA 时可选 --- -#}
        {%- if item.MSGTYPE == 'RAA' -%}
            {%- if item.EXPERRESULTCODE is not none -%}
                EXPERRESULTCODE={{item.EXPERRESULTCODE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：MSGTYPE=CCRI 时可选 --- -#}
        {%- if item.MSGTYPE == 'CCRI' -%}
            {%- if item.G3CC is not none -%}
                G3CC={{item.G3CC}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：MSGTYPE=CCRI 时可选 --- -#}
        {%- if item.MSGTYPE == 'CCRI' -%}
            {%- if item.G3GGSNADDR is not none -%}
                G3GGSNADDR={{item.G3GGSNADDR}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：MSGTYPE=CCRI/CCRU 时可选 --- -#}
        {%- if item.MSGTYPE in ['CCRI', 'CCRU'] -%}
            {%- if item.G3PPRATTYPE is not none -%}
                G3PPRATTYPE={{item.G3PPRATTYPE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：MSGTYPE=CCRI 时可选 --- -#}
        {%- if item.MSGTYPE == 'CCRI' -%}
            {%- if item.G3SELECTMODE is not none -%}
                G3SELECTMODE={{item.G3SELECTMODE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：MSGTYPE=CCRU 时可选 --- -#}
        {%- if item.MSGTYPE == 'CCRU' -%}
            {%- if item.G3SGSNADDR is not none -%}
                G3SGSNADDR={{item.G3SGSNADDR}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：MSGTYPE=CCRU 时可选 --- -#}
        {%- if item.MSGTYPE == 'CCRU' -%}
            {%- if item.G3SGSNMCCMNC is not none -%}
                G3SGSNMCCMNC={{item.G3SGSNMCCMNC}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：MSGTYPE=CCRU 时可选 --- -#}
        {%- if item.MSGTYPE == 'CCRU' -%}
            {%- if item.G3ULI is not none -%}
                G3ULI={{item.G3ULI}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：MSGTYPE=CCRI/CCRU/CCRT 时可选 --- -#}
        {%- if item.MSGTYPE in ['CCRI', 'CCRU', 'CCRT'] -%}
            {%- if item.IMSI is not none -%}
                IMSI={{item.IMSI}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：MSGTYPE=CCRI/CCRU 时可选 --- -#}
        {%- if item.MSGTYPE in ['CCRI', 'CCRU'] -%}
            {%- if item.MSTIMEZONE is not none -%}
                MSTIMEZONE={{item.MSTIMEZONE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：MSGTYPE=RAA 时可选 --- -#}
        {%- if item.MSGTYPE == 'RAA' -%}
            {%- if item.NETLOCACCESS is not none -%}
                NETLOCACCESS={{item.NETLOCACCESS}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：MSGTYPE=CCRI 时可选 --- -#}
        {%- if item.MSGTYPE == 'CCRI' -%}
            {%- if item.PDNCCHARGINGID is not none -%}
                PDNCCHARGINGID={{item.PDNCCHARGINGID}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：MSGTYPE=CCRU 时可选 --- -#}
        {%- if item.MSGTYPE == 'CCRU' -%}
            {%- if item.QOSINFORMATION is not none -%}
                QOSINFORMATION={{item.QOSINFORMATION}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：MSGTYPE=CCRU 时可选 --- -#}
        {%- if item.MSGTYPE == 'CCRU' -%}
            {%- if item.RATTYPE is not none -%}
                RATTYPE={{item.RATTYPE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：MSGTYPE=CCRU/CCRT 时可选 --- -#}
        {%- if item.MSGTYPE in ['CCRU', 'CCRT'] -%}
            {%- if item.ULITIME is not none -%}
                ULITIME={{item.ULITIME}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 5.3 配置GGSN/PGW-C发送的CCR-T消息中携带信元Called-Station-ID，Subscription-Id-Type和Subscription-Id携带MSISDN开关。

```jinja2
{%- if is_optional_enable_failover_enhancement -%}
    {%- for item in set_pccmsgattr_list_1 -%}
        SET PCCMSGATTR:
        {#- --- 必选参数 --- -#}
        MSGTYPE={{item.MSGTYPE}},
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：MSGTYPE=CCRU/CCRT 时可选 --- -#}
        {%- if item.MSGTYPE in ['CCRU', 'CCRT'] -%}
            {%- if item.MSISDN is not none -%}
                MSISDN={{item.MSISDN}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：MSGTYPE=CCRU/CCRT 时可选 --- -#}
        {%- if item.MSGTYPE in ['CCRU', 'CCRT'] -%}
            {%- if item.CALLEDSTATIONID is not none -%}
                CALLEDSTATIONID={{item.CALLEDSTATIONID}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：MSGTYPE=CCRU/CCRT 时可选 --- -#}
        {%- if item.MSGTYPE in ['CCRU', 'CCRT'] -%}
            {%- if item.ANCHARGINGADDR is not none -%}
                ANCHARGINGADDR={{item.ANCHARGINGADDR}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：MSGTYPE=CCRU/CCRT/RAA 时可选 --- -#}
        {%- if item.MSGTYPE in ['CCRU', 'CCRT', 'RAA'] -%}
            {%- if item.ANCHARGINGID is not none -%}
                ANCHARGINGID={{item.ANCHARGINGID}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：MSGTYPE=CCRI 时可选 --- -#}
        {%- if item.MSGTYPE == 'CCRI' -%}
            {%- if item.CHARGINGRULE is not none -%}
                CHARGINGRULE={{item.CHARGINGRULE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：MSGTYPE=CCRU 时可选 --- -#}
        {%- if item.MSGTYPE == 'CCRU' -%}
            {%- if item.CLHONEGOBCM is not none -%}
                CLHONEGOBCM={{item.CLHONEGOBCM}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：MSGTYPE=CCRU 时可选 --- -#}
        {%- if item.MSGTYPE == 'CCRU' -%}
            {%- if item.DFTEPSBEARERQOS is not none -%}
                DFTEPSBEARERQOS={{item.DFTEPSBEARERQOS}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：MSGTYPE=CCRI 时可选 --- -#}
        {%- if item.MSGTYPE == 'CCRI' -%}
            {%- if item.DYNADDRFLG is not none -%}
                DYNADDRFLG={{item.DYNADDRFLG}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：MSGTYPE=CCRI 时可选 --- -#}
        {%- if item.MSGTYPE == 'CCRI' -%}
            {%- if item.DYNADDRFLGEXT is not none -%}
                DYNADDRFLGEXT={{item.DYNADDRFLGEXT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：MSGTYPE=RAA 时可选 --- -#}
        {%- if item.MSGTYPE == 'RAA' -%}
            {%- if item.EXPERRESULTCODE is not none -%}
                EXPERRESULTCODE={{item.EXPERRESULTCODE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：MSGTYPE=CCRU/CCRT 时可选 --- -#}
        {%- if item.MSGTYPE in ['CCRU', 'CCRT'] -%}
            {%- if item.FRAMEDIPADDRESS is not none -%}
                FRAMEDIPADDRESS={{item.FRAMEDIPADDRESS}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：MSGTYPE=CCRU/CCRT 时可选 --- -#}
        {%- if item.MSGTYPE in ['CCRU', 'CCRT'] -%}
            {%- if item.FRAMEDIPV6PREF is not none -%}
                FRAMEDIPV6PREF={{item.FRAMEDIPV6PREF}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：MSGTYPE=CCRI 时可选 --- -#}
        {%- if item.MSGTYPE == 'CCRI' -%}
            {%- if item.G3CC is not none -%}
                G3CC={{item.G3CC}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：MSGTYPE=CCRI 时可选 --- -#}
        {%- if item.MSGTYPE == 'CCRI' -%}
            {%- if item.G3GGSNADDR is not none -%}
                G3GGSNADDR={{item.G3GGSNADDR}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：MSGTYPE=CCRI/CCRU 时可选 --- -#}
        {%- if item.MSGTYPE in ['CCRI', 'CCRU'] -%}
            {%- if item.G3PPRATTYPE is not none -%}
                G3PPRATTYPE={{item.G3PPRATTYPE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：MSGTYPE=CCRI 时可选 --- -#}
        {%- if item.MSGTYPE == 'CCRI' -%}
            {%- if item.G3SELECTMODE is not none -%}
                G3SELECTMODE={{item.G3SELECTMODE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：MSGTYPE=CCRU 时可选 --- -#}
        {%- if item.MSGTYPE == 'CCRU' -%}
            {%- if item.G3SGSNADDR is not none -%}
                G3SGSNADDR={{item.G3SGSNADDR}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：MSGTYPE=CCRU 时可选 --- -#}
        {%- if item.MSGTYPE == 'CCRU' -%}
            {%- if item.G3SGSNMCCMNC is not none -%}
                G3SGSNMCCMNC={{item.G3SGSNMCCMNC}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：MSGTYPE=CCRU 时可选 --- -#}
        {%- if item.MSGTYPE == 'CCRU' -%}
            {%- if item.G3ULI is not none -%}
                G3ULI={{item.G3ULI}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：MSGTYPE=CCRI/CCRU/CCRT 时可选 --- -#}
        {%- if item.MSGTYPE in ['CCRI', 'CCRU', 'CCRT'] -%}
            {%- if item.IMSI is not none -%}
                IMSI={{item.IMSI}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：MSGTYPE=CCRI/CCRU 时可选 --- -#}
        {%- if item.MSGTYPE in ['CCRI', 'CCRU'] -%}
            {%- if item.MSTIMEZONE is not none -%}
                MSTIMEZONE={{item.MSTIMEZONE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：MSGTYPE=RAA 时可选 --- -#}
        {%- if item.MSGTYPE == 'RAA' -%}
            {%- if item.NETLOCACCESS is not none -%}
                NETLOCACCESS={{item.NETLOCACCESS}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：MSGTYPE=CCRI 时可选 --- -#}
        {%- if item.MSGTYPE == 'CCRI' -%}
            {%- if item.PDNCCHARGINGID is not none -%}
                PDNCCHARGINGID={{item.PDNCCHARGINGID}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：MSGTYPE=CCRU 时可选 --- -#}
        {%- if item.MSGTYPE == 'CCRU' -%}
            {%- if item.QOSINFORMATION is not none -%}
                QOSINFORMATION={{item.QOSINFORMATION}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：MSGTYPE=CCRU 时可选 --- -#}
        {%- if item.MSGTYPE == 'CCRU' -%}
            {%- if item.RATTYPE is not none -%}
                RATTYPE={{item.RATTYPE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：MSGTYPE=CCRU/CCRT 时可选 --- -#}
        {%- if item.MSGTYPE in ['CCRU', 'CCRT'] -%}
            {%- if item.ULITIME is not none -%}
                ULITIME={{item.ULITIME}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：MSGTYPE=CCRU/CCRT 时可选 --- -#}
        {%- if item.MSGTYPE in ['CCRU', 'CCRT'] -%}
            {%- if item.USREQUIPINFO is not none -%}
                USREQUIPINFO={{item.USREQUIPINFO}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

