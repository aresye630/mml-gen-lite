---
id: ''
name: 配置话单字段
ne_type: UNC
type: feature
description: 本指导描述话单中某些字段携带规则的配置过程。  对于话单中标识为可选（C）或条件可选（OC）或条件必选（OM）的字段，UNC支持自定义配置是否携带该字段，运营商可根据需要选择配置。  话单可选字段可以基于APN、全局进行配置，它们的优先级顺序是APN > 全局配置 > 默认值。如果高级别的没有配置，则取用低级别的话单字段模板，否则取用默认值。  UNC支持为不同的话单类型绑定不同的CDRFieldTemp话单字段模板，可以分别独立控制SGW-CDR、PGW-CDR、G-CDR话单携带的字段，增强话单字段的灵活度。  * 系统升级时，需注意先升级CG，再升级UNC，以防止UNC先升级后话单中有CG不识别的字段。 * 话单字段修改前需要与对端CG确认是否支持。
risk_level: ''
doc_source: ["网络部署","业务专题","5G Core 计费解决方案","计费解决方案概述","计费方案部署与调测","方案二：部署NCG且基于传统Ga/Gy接口计费组网方案","SMF配置","离线计费配置","离线计费模板及交互配置","配置话单字段"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本指导描述话单中某些字段携带规则的配置过程。对于话单中标识为可选（C）或条件可选（OC）或条件必选（OM）的字段，UNC支持自定义配置是否携带该字段，运营商可根据需要选择配置。话单可选字段可以基于APN、全局进行配置，它们的优先级顺序是APN > 全局配置 > 默认值。如果高级别的没有配置，则取用低级别的话单字段模板，否则取用默认值。UNC支持为不同的话单类型绑定不同的CDRFieldTemp话单字段模板，可以分别独立控制SGW-CDR、PGW-CDR、G-CDR话单携带的字段，增强话单字段的灵活度。* 系统升级时，需注意先升级CG，再升级UNC，以防止UNC先升级后话单中有CG不识别的字段。* 话单字段修改前需要与对端CG确认是否支持。

## 必备事项
前提条件

前提条件

* 请仔细阅读Ga/Gy接口离线/在线计费。

* 已完成计费属性、APN、User Profile创建。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_cdrfieldtemp_list:
      type: items
      properties:
        TEMPLATENAME:
          name: '话单字段模板名'
          type: string
          maxLength: 63
          required: true
          description: '配置单字段模板，控制话单中是否携带对应字段。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        APNNETWORKID:
          name: 'apn-network-identifier'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '配置话单中是否包含APN网络节点标识信息，默认值是“ENABLE”。'
          data_source: ''
          pattern: ''
          default: ENABLE
        MSTIMEZONE:
          name: 'ms-time-zone'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '配置话单中是否携带ms-time-zone字段。该字段记录用户所在的时区信息。  默认值是“ENABLE”。'
          data_source: ''
          pattern: ''
          default: ENABLE
        APNSELECTMODE:
          name: 'apn-selection-mode'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '配置话单中是否包含APN选择模式信息。该字段记录APN选择模式。默认值是“ENABLE”。'
          data_source: ''
          pattern: ''
          default: ENABLE
        CCSELETIONMODE:
          name: 'charge-characteristic-selection-mode'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '配置话单中是否包含计费属性选择模式标志。该字段记录计费属性的选择模式，是使用用户激活消息中所携带的SGSN/S-GW/MME计费属性，还是使用GGSN/SGW-C/PGW-C所配置的计费属性。  默认值是“ENABLE”。'
          data_source: ''
          pattern: ''
          default: ENABLE
        DIAGNOSTICS:
          name: 'diagnostics'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '配置话单中是否携带diagnostics字段。该字段可记录用户去激活的原因。  默认值是“ENABLE”。'
          data_source: ''
          pattern: ''
          default: ENABLE
        DYNADDRFLAG:
          name: 'dynamic-address-flag'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '配置话单中是否携带dynamic-address-flag字段。该字段标识用户地址是否为动态地址分配 。  默认值是“ENABLE”。'
          data_source: ''
          pattern: ''
          default: ENABLE
        EXTCHARGEID:
          name: 'external-charging-identifier'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '配置话单中是否携带external-charging-identifier字段。该字段记录从非EPC网络或者外网接收的计费标识，例如P-GW从IMS网络接收的IMS计费标识。  默认值是“ENABLE”。'
          data_source: ''
          pattern: ''
          default: ENABLE
        IMSSIGCONTEXT:
          name: 'ims-signalling-context'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '配置话单中是否携带ims-signalling-context字段。该字段标识IP-CAN承载是否用于IMS信令。仅当IP-CAN承载是IMS信令承载时才存在。  默认值是“ENABLE”。'
          data_source: ''
          pattern: ''
          default: ENABLE
        LOSD:
          name: 'list-of-service-data'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '配置话单中是否携带list-of-service-data字段。  该字段包含一个或者多个业务数据容器。  默认值是“ENABLE”。'
          data_source: ''
          pattern: ''
          default: ENABLE
        LOTV:
          name: 'list-of-traffic-volume'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '配置话单中是否携带List of Traffic Volumes字段。该字段包含一个或者多个流量数据容器。  默认值是“ENABLE”。'
          data_source: ''
          pattern: ''
          default: ENABLE
        LOCALRECSEQNUM:
          name: 'local-record-sequence-number'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '配置话单中是否携带本地话单序列号字段。该字段标识UNC的节点上累计产生的话单序号，每个序号在UNC的节点上唯一。  默认值是“ENABLE”。'
          data_source: ''
          pattern: ''
          default: ENABLE
        MSISDN:
          name: 'MSISDN'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '配置话单中是否包含用户MSISDN信息。默认值是“ENABLE”。'
          data_source: ''
          pattern: ''
          default: ENABLE
        NETINITPDPCONT:
          name: 'network-initiated-pdp-context'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '配置话单中是否携带network-initiated-pdp-context字段。该字段记录用户PDP上下文/EPS承载是由网络侧激活的。  默认值是“ENABLE”。'
          data_source: ''
          pattern: ''
          default: ENABLE
        NODEID:
          name: 'node-id'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '配置话单中是否包含网络节点标识信息。该字段记录UNC的节点标识。  默认值是“ENABLE”。  说明：  如果配置为“ENABLE”，则必须通过**SET OFCCDRPARA**配置“GSNNODEIDPREFIX”为非空才能生效。'
          data_source: ''
          pattern: ''
          default: ENABLE
        PDPTYPE:
          name: 'pdp-type'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '配置话单中是否包含PDP上下文类型信息。默认值是“ENABLE”。'
          data_source: ''
          pattern: ''
          default: ENABLE
        PGWADDRESSIPV6:
          name: 'pgw-address-ipv6'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '配置话单中是否携带pgw-address-ipv6字段。该字段标识PGW控制面IPv6地址。  默认值是“ENABLE”。'
          data_source: ''
          pattern: ''
          default: ENABLE
        PSFCI:
          name: 'ps-furnish-charging-information'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '配置话单中是否携带ps-furnish-charging-information字段。该字段包含OCS在CCA消息中携带的计费信息以及计费信息是否附加在前一个计费信息后。  默认值是“ENABLE”。'
          data_source: ''
          pattern: ''
          default: ENABLE
        RATTYPE:
          name: 'rat-type'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '配置话单中是否携带rat-type字段。该字段表示用户的接入类型。  默认值是“ENABLE”。'
          data_source: ''
          pattern: ''
          default: ENABLE
        RECSEQNUMBER:
          name: 'record-sequence-number'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '配置话单中是否携带record-sequence-number字段。该字段标识IP-CAN bearer生成的话单的序号，当仅产生一张话单时，不携带该字段。  默认值是“ENABLE”。'
          data_source: ''
          pattern: ''
          default: ENABLE
        SERVEDIMEISV:
          name: 'served-imeisv'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '配置话单中是否携带served-imeisv字段。该字段标识用户的IMEISV。  默认值是“ENABLE”。'
          data_source: ''
          pattern: ''
          default: ENABLE
        SERVEDPDPADDR:
          name: 'served-pdp-address'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '配置话单中是否携带served-pdp-address字段。该字段表示用户的IP地址。  默认值是“ENABLE”。'
          data_source: ''
          pattern: ''
          default: ENABLE
        SGSNSGWPLMNID:
          name: 'sgsn-sgw-plmn-identifier'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '配置在话单中是否包含sgsn-sgw-plmn-identifier标志。该字段包含服务节点（SGSN/S-GW/MME/ePDG/HSGW）的PLMN标识。  默认值是“ENABLE”。'
          data_source: ''
          pattern: ''
          default: ENABLE
        THREEGPP2USRLOC:
          name: 'threegpp2-user-location'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '配置话单中是否携带threegpp2-user-location字段。该字段包含3GPP2 用户位置信息（3GPP2-BSID）。  默认值是“ENABLE”。'
          data_source: ''
          pattern: ''
          default: ENABLE
        ULI:
          name: 'user-location-information'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '配置话单中是否携带user-location-information字段。该字段承载用户的3GPP位置信息。  默认值是“ENABLE”。'
          data_source: ''
          pattern: ''
          default: ENABLE
        PDNCONNECTIONID:
          name: 'pdn-connection-id'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '配置话单中是否包含pdn-connection-id信息。该字段定义PDN连接的计费标识，用于标识同一PDN连接的不同话单记录。  默认值是“DISABLE”。'
          data_source: ''
          pattern: ''
          default: DISABLE
        PGWADDRESSUSED:
          name: 'pgw-address-used'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '配置话单中是否携带pgw-address-used字段。该字段标识PGW的控制面地址，如果PGW控制面地址为双栈地址，该字段表示IPv4地址。默认值是“DISABLE”。'
          data_source: ''
          pattern: ''
          default: DISABLE
        PGWPLMNID:
          name: 'pgw-plmn-identifier'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '配置话单中是否携带pgw-plmn-identifier字段，该字段表示PGW的PLMN标识。  默认值是“DISABLE”。'
          data_source: ''
          pattern: ''
          default: DISABLE
        STARTTIME:
          name: 'start-time'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '配置话单中是否携带start time字段。该字段记录IP-CAN会话的开始时间，即第一个承载激活时间。  默认值是“DISABLE”。'
          data_source: ''
          pattern: ''
          default: DISABLE
        STOPTIME:
          name: 'stop-time'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '配置话单中是否携带stop time字段。该字段记录IP-CAN会话的结束时间，即最后一个承载去激活时间。  默认值是“DISABLE”。'
          data_source: ''
          pattern: ''
          default: DISABLE
        SGWADDRESSIPV6:
          name: 'sgw-address-ipv6'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '配置话单中是否携带sgw-address-ipv6字段。该字段表示SGW控制面IPv6地址。  默认值是“ENABLE”。'
          data_source: ''
          pattern: ''
          default: ENABLE
        RECORDEXTENTION:
          name: 'record-extensions开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '配置话单中是否携带recordExtensions字段。该字段表示网络运营商或者设备制造商自定义的扩展信息。  默认值是“DISABLE”。'
          data_source: ''
          pattern: ''
          default: DISABLE
        RECORDEXTTYPE:
          name: '运营商record-extensions'
          type: string
          enum:
          - CCB
          - CMHK
          - COMM
          - DT
          - GLB
          - HP
          - TAG
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: CCB
        ULIWLAN:
          name: 'ULI携带WLAN地址信息'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
    set_glbcdrfldtemp_list:
      type: items
      properties:
        PGWCDRTEMPLATE:
          name: 'PGW-CDR话单字段模板名'
          type: string
          maxLength: 63
          required: false
          description: '配置全局绑定话单字段模板'
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_apnchargectrl_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          maxLength: 63
          required: true
          description: '为APN实例绑定话单字段模板。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PGWCDRTEMPLATE:
          name: 'PGW-CDR话单字段模板名'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_ofccdrpara_list:
      type: items
      properties:
        GSNNODEIDPREFIX:
          name: 'gsn-node-id字段前缀'
          type: string
          maxLength: 17
          required: false
          description: '配置话单中的gsn-node-id字段的前缀。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        GNIDELIMITER:
          name: 'gsn-node-id字段分隔符'
          type: string
          maxLength: 1
          required: false
          description: '配置话单中的gsn-node-id字段的分隔符。'
          data_source: ''
          pattern: ''
          default: ''
        PGWCDRLOTVSW:
          name: 'PGW-CDR携带List of Traffic Volume'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '配置PGW-CDR中是否携带listOfTrafficVolume字段。'
          data_source: ''
          pattern: ''
          default: ''
        PGWCDRLOSDRATSW:
          name: 'PGW-CDR话单的List of Service Data携带RAT-Type'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '配置PGW-CDR话单List of Service Data中是否携带RAT-Type信元。'
          data_source: ''
          pattern: ''
          default: ''
        PGWCDRLOSDAMBR:
          name: 'PGW-CDR话单List of Service Data容器携带APN-AMBR开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '配置控制PGW-CDR话单List of Service Data容器携带APN-AMBR。'
          data_source: ''
          pattern: ''
          default: ''
        SRVNODEADDR:
          name: 'GCDR话单的sgsnAddress值'
          type: string
          enum:
          - GTPC_ADDRESS
          - GTPU_ADDRESS
          required: false
          description: '配置sgsnAddress字段是携带SGSN的数据面地址还是控制面地址。'
          data_source: ''
          pattern: ''
          default: ''
        SGWLOTVQOSEXT:
          name: 'SGW-CDR流量容器携带扩展Qos参数开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '配置SGW-CDR的List of Traffic Volumes EPC Qos中携带扩展Qos参数。'
          data_source: ''
          pattern: ''
          default: ''
        PGWLOTVQOSEXT:
          name: 'PGW-CDR流量容器携带扩展Qos参数开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '配置PGW-CDR的List of Traffic Volumes EPC Qos中携带扩展Qos参数。'
          data_source: ''
          pattern: ''
          default: ''
        PGWLOSDQOSEXT:
          name: 'PGW-CDR业务容器携带扩展Qos参数开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '配置PGW-CDR的List of Service Data EPC Qos中携带扩展Qos参数。'
          data_source: ''
          pattern: ''
          default: ''
        SGWLOTVCPEPS:
          name: 'SGW-CDR话单的LoTV携带CP CIoT EPS Optimisation Indicator'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '配置SGW-CDR的话单List of Traffic Volumes是否携带CP CIoT EPS Optimisation Indicator。'
          data_source: ''
          pattern: ''
          default: ''
        SGWLOTVSPRATE:
          name: 'SGW-CDR话单的LoTV携带Serving PLMN Rate Control'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '配置SGW-CDR话单的List of Traffic Volumes是否携带Serving PLMN Rate Control。'
          data_source: ''
          pattern: ''
          default: ''
        PGWLOSDSPRATE:
          name: 'PGW-CDR话单LoSD携带Serving PLMN Rate Control'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '配置PGW-CDR话单的List of Service Data是否携带Serving PLMN Rate Control。'
          data_source: ''
          pattern: ''
          default: ''
        PGWLOSDAPNRATE:
          name: 'PGW-CDR话单的LoSD携带APN Rate Control'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '配置PGW-CDR话单的List of Service Data是否携带APN Rate Control。'
          data_source: ''
          pattern: ''
          default: ''
        PGWIPV6IFID:
          name: 'G-CDR/PGW-CDR中用户IPv6地址Interface Identifier填写方式'
          type: string
          enum:
          - INTERFACE_ID_EMPTY
          - INTERFACE_ID_REAL
          required: false
          description: '配置G-CDR/PGW-CDR中用户IPv6地址Interface Identifier填写方式。'
          data_source: ''
          pattern: ''
          default: ''
        SGWIPV6IFID:
          name: 'SGW-CDR中用户IPv6地址Interface Identifier填写方式'
          type: string
          enum:
          - INTERFACE_ID_EMPTY
          - INTERFACE_ID_REAL
          required: false
          description: '配置SGW-CDR中用户IPv6地址Interface Identifier填写方式。'
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_cdrfieldtemp_list:
    - TEMPLATENAME: 'cdrfield-test'
      APNNETWORKID: ENABLE
      MSTIMEZONE: ENABLE
      APNSELECTMODE: ENABLE
      CCSELETIONMODE: ENABLE
      DIAGNOSTICS: ENABLE
      DYNADDRFLAG: ENABLE
      EXTCHARGEID: ENABLE
      IMSSIGCONTEXT: ENABLE
      LOSD: ENABLE
      LOTV: ENABLE
      LOCALRECSEQNUM: ENABLE
      MSISDN: ENABLE
      NETINITPDPCONT: ENABLE
      NODEID: ENABLE
      PDPTYPE: ENABLE
      PGWADDRESSIPV6: ENABLE
      PSFCI: ENABLE
      RATTYPE: ENABLE
      RECSEQNUMBER: ENABLE
      SERVEDIMEISV: ENABLE
      SERVEDPDPADDR: ENABLE
      SGSNSGWPLMNID: ENABLE
      THREEGPP2USRLOC: ENABLE
      ULI: ENABLE
      PDNCONNECTIONID: ENABLE
      PGWADDRESSUSED: ENABLE
      PGWPLMNID: ENABLE
      STARTTIME: ENABLE
      STOPTIME: ENABLE
      SGWADDRESSIPV6: ENABLE
      RECORDEXTENTION: DISABLE
      RECORDEXTTYPE: CCB
      ULIWLAN: DISABLE
    set_glbcdrfldtemp_list:
    - PGWCDRTEMPLATE: 'cdrfield-test'
    set_apnchargectrl_list:
    - APN: 'apn-test'
      PGWCDRTEMPLATE: 'cdrfield-test'
    set_ofccdrpara_list:
    - GSNNODEIDPREFIX: 'gsn.huawei'
      GNIDELIMITER: '@'
      PGWCDRLOTVSW: ENABLE
      PGWCDRLOSDRATSW: DISABLE
      PGWCDRLOSDAMBR: DISABLE
      SRVNODEADDR: GTPC_ADDRESS
      SGWLOTVQOSEXT: DISABLE
      PGWLOTVQOSEXT: DISABLE
      PGWLOSDQOSEXT: DISABLE
      SGWLOTVCPEPS: DISABLE
      SGWLOTVSPRATE: DISABLE
      PGWLOSDSPRATE: DISABLE
      PGWLOSDAPNRATE: DISABLE
      PGWIPV6IFID: INTERFACE_ID_EMPTY
      SGWIPV6IFID: INTERFACE_ID_EMPTY
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置话单字段模板。

### UNC默认携带话单可选字段，如果不需要携带某个字段，将对应字段设置为**DISABLE**。

```jinja2
{%- for item in add_cdrfieldtemp_list -%}
    ADD CDRFIELDTEMP:
    {#- --- 必选参数 --- -#}
    TEMPLATENAME="{{item.TEMPLATENAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.PDNCONNECTIONID is not none -%}
        PDNCONNECTIONID={{item.PDNCONNECTIONID}},
    {%- endif -%}
    {%- if item.PGWADDRESSUSED is not none -%}
        PGWADDRESSUSED={{item.PGWADDRESSUSED}},
    {%- endif -%}
    {%- if item.PGWPLMNID is not none -%}
        PGWPLMNID={{item.PGWPLMNID}},
    {%- endif -%}
    {%- if item.STARTTIME is not none -%}
        STARTTIME={{item.STARTTIME}},
    {%- endif -%}
    {%- if item.STOPTIME is not none -%}
        STOPTIME={{item.STOPTIME}},
    {%- endif -%}
    {%- if item.APNNETWORKID is not none -%}
        APNNETWORKID={{item.APNNETWORKID}},
    {%- endif -%}
    {%- if item.APNSELECTMODE is not none -%}
        APNSELECTMODE={{item.APNSELECTMODE}},
    {%- endif -%}
    {%- if item.CCSELETIONMODE is not none -%}
        CCSELETIONMODE={{item.CCSELETIONMODE}},
    {%- endif -%}
    {%- if item.DIAGNOSTICS is not none -%}
        DIAGNOSTICS={{item.DIAGNOSTICS}},
    {%- endif -%}
    {%- if item.DYNADDRFLAG is not none -%}
        DYNADDRFLAG={{item.DYNADDRFLAG}},
    {%- endif -%}
    {%- if item.EXTCHARGEID is not none -%}
        EXTCHARGEID={{item.EXTCHARGEID}},
    {%- endif -%}
    {%- if item.IMSSIGCONTEXT is not none -%}
        IMSSIGCONTEXT={{item.IMSSIGCONTEXT}},
    {%- endif -%}
    {%- if item.LOCALRECSEQNUM is not none -%}
        LOCALRECSEQNUM={{item.LOCALRECSEQNUM}},
    {%- endif -%}
    {%- if item.LOSD is not none -%}
        LOSD={{item.LOSD}},
    {%- endif -%}
    {%- if item.LOTV is not none -%}
        LOTV={{item.LOTV}},
    {%- endif -%}
    {%- if item.MSISDN is not none -%}
        MSISDN={{item.MSISDN}},
    {%- endif -%}
    {%- if item.MSTIMEZONE is not none -%}
        MSTIMEZONE={{item.MSTIMEZONE}},
    {%- endif -%}
    {%- if item.NETINITPDPCONT is not none -%}
        NETINITPDPCONT={{item.NETINITPDPCONT}},
    {%- endif -%}
    {%- if item.NODEID is not none -%}
        NODEID={{item.NODEID}},
    {%- endif -%}
    {%- if item.PDPTYPE is not none -%}
        PDPTYPE={{item.PDPTYPE}},
    {%- endif -%}
    {%- if item.PGWADDRESSIPV6 is not none -%}
        PGWADDRESSIPV6={{item.PGWADDRESSIPV6}},
    {%- endif -%}
    {%- if item.PSFCI is not none -%}
        PSFCI={{item.PSFCI}},
    {%- endif -%}
    {%- if item.RATTYPE is not none -%}
        RATTYPE={{item.RATTYPE}},
    {%- endif -%}
    {%- if item.RECORDEXTENTION is not none -%}
        RECORDEXTENTION={{item.RECORDEXTENTION}},
    {%- endif -%}
    {%- if item.RECSEQNUMBER is not none -%}
        RECSEQNUMBER={{item.RECSEQNUMBER}},
    {%- endif -%}
    {%- if item.SERVEDIMEISV is not none -%}
        SERVEDIMEISV={{item.SERVEDIMEISV}},
    {%- endif -%}
    {%- if item.SERVEDPDPADDR is not none -%}
        SERVEDPDPADDR={{item.SERVEDPDPADDR}},
    {%- endif -%}
    {%- if item.SGSNSGWPLMNID is not none -%}
        SGSNSGWPLMNID={{item.SGSNSGWPLMNID}},
    {%- endif -%}
    {%- if item.SGWADDRESSIPV6 is not none -%}
        SGWADDRESSIPV6={{item.SGWADDRESSIPV6}},
    {%- endif -%}
    {%- if item.THREEGPP2USRLOC is not none -%}
        THREEGPP2USRLOC={{item.THREEGPP2USRLOC}},
    {%- endif -%}
    {%- if item.ULI is not none -%}
        ULI={{item.ULI}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：RECORDEXTENTION=ENABLE 时必选 --- -#}
    {%- if item.RECORDEXTENTION == 'ENABLE' -%}
        RECORDEXTTYPE={{item.RECORDEXTTYPE}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：ULI=ENABLE 时可选 --- -#}
    {%- if item.ULI == 'ENABLE' -%}
        {%- if item.ULIWLAN is not none -%}
            ULIWLAN={{item.ULIWLAN}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 配置全局话单字段模板。

```jinja2
{%- for item in set_glbcdrfldtemp_list -%}
    SET GLBCDRFLDTEMP:
    {#- --- 可选参数 --- -#}
    {%- if item.PGWCDRTEMPLATE is not none -%}
        PGWCDRTEMPLATE="{{item.PGWCDRTEMPLATE}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置APN实例的话单字段模板。

```jinja2
{%- for item in set_apnchargectrl_list -%}
    SET APNCHARGECTRL:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.PGWCDRTEMPLATE is not none -%}
        PGWCDRTEMPLATE="{{item.PGWCDRTEMPLATE}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 通过全局参数配置某些话单字段携带规则。

```jinja2
{%- for item in set_ofccdrpara_list -%}
    SET OFCCDRPARA:
    {#- --- 可选参数 --- -#}
    {%- if item.GSNNODEIDPREFIX is not none -%}
        GSNNODEIDPREFIX="{{item.GSNNODEIDPREFIX}}",
    {%- endif -%}
    {%- if item.GNIDELIMITER is not none -%}
        GNIDELIMITER="{{item.GNIDELIMITER}}",
    {%- endif -%}
    {%- if item.PGWCDRLOTVSW is not none -%}
        PGWCDRLOTVSW={{item.PGWCDRLOTVSW}},
    {%- endif -%}
    {%- if item.PGWCDRLOSDAMBR is not none -%}
        PGWCDRLOSDAMBR={{item.PGWCDRLOSDAMBR}},
    {%- endif -%}
    {%- if item.PGWCDRLOSDRATSW is not none -%}
        PGWCDRLOSDRATSW={{item.PGWCDRLOSDRATSW}},
    {%- endif -%}
    {%- if item.PGWIPV6IFID is not none -%}
        PGWIPV6IFID={{item.PGWIPV6IFID}},
    {%- endif -%}
    {%- if item.PGWLOSDAPNRATE is not none -%}
        PGWLOSDAPNRATE={{item.PGWLOSDAPNRATE}},
    {%- endif -%}
    {%- if item.PGWLOSDQOSEXT is not none -%}
        PGWLOSDQOSEXT={{item.PGWLOSDQOSEXT}},
    {%- endif -%}
    {%- if item.PGWLOSDSPRATE is not none -%}
        PGWLOSDSPRATE={{item.PGWLOSDSPRATE}},
    {%- endif -%}
    {%- if item.PGWLOTVQOSEXT is not none -%}
        PGWLOTVQOSEXT={{item.PGWLOTVQOSEXT}},
    {%- endif -%}
    {%- if item.SGWIPV6IFID is not none -%}
        SGWIPV6IFID={{item.SGWIPV6IFID}},
    {%- endif -%}
    {%- if item.SGWLOTVCPEPS is not none -%}
        SGWLOTVCPEPS={{item.SGWLOTVCPEPS}},
    {%- endif -%}
    {%- if item.SGWLOTVQOSEXT is not none -%}
        SGWLOTVQOSEXT={{item.SGWLOTVQOSEXT}},
    {%- endif -%}
    {%- if item.SGWLOTVSPRATE is not none -%}
        SGWLOTVSPRATE={{item.SGWLOTVSPRATE}},
    {%- endif -%}
    {%- if item.SRVNODEADDR is not none -%}
        SRVNODEADDR={{item.SRVNODEADDR}},
    {%- endif -%}
    ;
{%- endfor -%}
```

