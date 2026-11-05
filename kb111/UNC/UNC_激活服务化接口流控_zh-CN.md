---
id: ''
name: 激活服务化接口流控
ne_type: UNC
type: feature
description: 本操作用于指导在运行网络中激活服务化接口流控。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","流控功能","WSFD-010801 系统过载控制功能","系统过载控制功能（服务化接口流控）","激活服务化接口流控"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作用于指导在运行网络中激活服务化接口流控。

## 必备事项
前提条件

请仔细阅读WSFD-010801 系统过载控制功能（服务化接口流控）特性概述。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_httpfcipgrp_list:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 0
          maximum: 4095
          required: true
          description: '设置流控组信息。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        GROUP:
          name: '流控组'
          type: integer
          minimum: 0
          maximum: 4095
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPTYPE:
          name: 'IP地址类型'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4ADDR:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4MASK:
          name: 'IPv4掩码'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESC:
          name: '描述'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6ADDR:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6MASK:
          name: 'IPv6前缀'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_httpfixedfc_list:
      type: items
      properties:
        GROUP:
          name: '流控组'
          type: integer
          minimum: 0
          maximum: 4095
          required: true
          description: '增加HTTP固定速率流控门限。  说明：  * 此处门限值为举例，请根据局点实际情况进行设置。 * UNC作为HTTP服务端，为保护自身系统不会过载，需要对接收的消息速率进行控制。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        GROUPTYPE:
          name: '流控组类型'
          type: string
          enum:
          - SERVER
          - CLIENT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: SERVER
        RECVTHD:
          name: '单链路接收消息流控门限(条/秒)'
          type: integer
          minimum: 1
          maximum: 1000000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        STATUSCODE:
          name: '状态码'
          type: string
          enum:
          - TooManyRequests
          - ServiceUnavailable
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: TooManyRequests
        RETRYAFTERFLAG:
          name: '是否携带Retry-After消息头'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESC:
          name: '描述'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TIMER:
          name: 'Retry-After时长(秒)'
          type: integer
          minimum: 0
          maximum: 3600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 180
    add_httpfixedfc_list_1:
      type: items
      properties:
        GROUP:
          name: '流控组'
          type: integer
          minimum: 0
          maximum: 4095
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GROUPTYPE:
          name: '流控组类型'
          type: string
          enum:
          - SERVER
          - CLIENT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: SERVER
        GLBRECVTHD:
          name: '整系统接收消息流控门限(条/秒)'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        STATUSCODE:
          name: '状态码'
          type: string
          enum:
          - TooManyRequests
          - ServiceUnavailable
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: TooManyRequests
        RETRYAFTERFLAG:
          name: '是否携带Retry-After消息头'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESC:
          name: '描述'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TIMER:
          name: 'Retry-After时长(秒)'
          type: integer
          minimum: 0
          maximum: 3600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 180
    set_httpfixedfcmsg_list:
      type: items
      properties:
        MSGTYPE:
          name: '流控消息类型'
          type: string
          enum:
          - NSMF_PDUSESSION_SMCONTEXTSCREATE
          - NSMF_PDUSESSION_RETRIEVESMCONTEXT
          - NNRF_NFMANAGEMENTSERVICE_NFSTATUSEVENTNOTIFY
          - NAMF_COMMUNICATION_UECONTEXTTRANSFER
          - NNRF_NFDISCOVERYSERVICE_SEARCHNFINSTANCES
          - NNRF_NFMANAGEMENTSERVICE_REGISTERNFINSTANCE
          - NNRF_NFMANAGEMENTSERVICE_GETNFINSTANCES
          - NNRF_NFMANAGEMENTSERVICE_GETNFINSTANCE
          - NNRF_NFMANAGEMENTSERVICE_CREATESUBSCRIPTION
          - NNRF_NFMANAGEMENTSERVICE_UPDATESUBSCRIPTION
          - NNSSF_NSSELECTION_NSSELECTIONGET
          - NNSSF_NSSAIAVAILABILITY_NSSAIAVAILABILITYPATCH
          - NNSSF_NSSAIAVAILABILITY_NSSAIAVAILABILITYPUT
          - NNSSF_NSSAIAVAILABILITY_NSSAIAVAILABILITYPOST
          - NSMSF_SMSERVICESERVICEAPI_SMSERVICEACTIVATION
          - NSMSF_SMSERVICESERVICEAPI_SENDSMS
          - NCHF_CONVERGEDCHARGING_CHARGINGDATACREATE
          - NCHF_CONVERGEDCHARGING_CHARGINGDATAREFCREATE
          - NNWDAF_EVENTSSUBSCRIPTION_SUBSCRIBE
          - NUPF_EVENTEXPOSURE_NOTIFY
          - NSMF_EVENTEXPOSURE_NOTIFY
          - NAMF_EVENTEXPOSURE_NOTIFY
          - NUDN_EVENTSSUBSCRIPTION_NOTIFY
          - NUDN_EVENTSSUBSCRIPTION_SUBSCRIBER
          - NUDN_RAILWAYSAMPLEDATARECORDR
          required: true
          description: '配置指定类型的消息是否开启固定速率流控。  说明：  此处仅以SMF收到AMF发送的Nsmf\_PDUSession\_CreateSMContext Request和Nsmf\_PDUSession\_RetrieveSMContext Request消息为例。请根据局点实际情况进行配置。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        FCSWITCH:
          name: '固定速率流控开关'
          type: string
          enum:
          - ON
          - OFF
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        THRESHOLD:
          name: '流控速率门限(个/秒)'
          type: integer
          minimum: 0
          maximum: 1000000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_httpofc_list:
      type: items
      properties:
        OFCIDX:
          name: '局向索引'
          type: integer
          minimum: 0
          maximum: 4095
          required: true
          description: '增加基于接口类型的固定速率流控生效的HTTP局向。  说明：  此处仅以SMF到AMF局向举例，请根据网络实际情况配置所有局向。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        OFCTYPE:
          name: '局向类型'
          type: string
          enum:
          - NFTYPE
          - IPGROUP
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PEERNFTYPE:
          name: '对端网元类型'
          type: string
          enum:
          - INVALID
          - NFTypeNRF
          - NFTypeUDM
          - NFTypeAMF
          - NFTypeSMF
          - NFTypeAUSF
          - NFTypeNEF
          - NFTypePCF
          - NFTypeSMSF
          - NFTypeNSSF
          - NFTypeUDR
          - NFTypeLMF
          - NFTypeGMLC
          - NFType5GEIR
          - NFTypeSEPP
          - NFTypeUPF
          - NFTypeN3IWF
          - NFTypeAF
          - NFTypeUDSF
          - NFTypeBSF
          - NFTypeCHF
          - NFTypeCUSTOM_OCS
          - NFTypeSCP
          - NFTypeNWDAF
          - NFTypePCSCF
          - NFTypeCBCF
          - NFTypeDRA
          - NFTypeMB_SMF
          - NFTypeUDN
          - NFTypeSFC
          - NFTypeUCBC
          - NFTypeCBE
          - NFTypeNEFEx
          - NFTypeSCF
          - NFTypeKMC
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        NFITEM:
          name: '基于NFTYPE控制项'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        LOCALNFTYPE:
          name: '本端网元类型'
          type: string
          enum:
          - INVALID
          - NFTypeNRF
          - NFTypeUDM
          - NFTypeAMF
          - NFTypeSMF
          - NFTypeAUSF
          - NFTypeNEF
          - NFTypePCF
          - NFTypeSMSF
          - NFTypeNSSF
          - NFTypeUDR
          - NFTypeLMF
          - NFTypeGMLC
          - NFType5GEIR
          - NFTypeSEPP
          - NFTypeUPF
          - NFTypeN3IWF
          - NFTypeAF
          - NFTypeUDSF
          - NFTypeBSF
          - NFTypeCHF
          - NFTypeCUSTOM_OCS
          - NFTypeSCP
          - NFTypeNWDAF
          - NFTypePCSCF
          - NFTypeCBCF
          - NFTypeDRA
          - NFTypeMB_SMF
          - NFTypeUDN
          - NFTypeSFC
          - NFTypeUCBC
          - NFTypeCBE
          - NFTypeNEFEx
          - NFTypeSCF
          - NFTypeKMC
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        OFCNAME:
          name: '局向名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPGROUP:
          name: 'IP组'
          type: integer
          minimum: 0
          maximum: 4095
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPGRPITEM:
          name: '基于IP组控制项'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_httpfixedfcinf_list:
      type: items
      properties:
        OFCIDX:
          name: '局向索引'
          type: integer
          minimum: 0
          maximum: 4095
          required: true
          description: '增加基于接口类型的固定速率流控的门限相关配置。  说明：  * 此处取值均为举例，请根据网络实际情况配置。 * UNC作为HTTP服务端，为保护自身系统不会过载，需要对接收的消息速率进行控制。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        LETYPE:
          name: '本端实体类型'
          type: string
          enum:
          - SERVER
          - CLIENT
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        RECVTHD:
          name: '接收消息流控门限(条/秒)'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        STATUSCODE:
          name: '状态码'
          type: string
          enum:
          - TooManyRequests
          - ServiceUnavailable
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: TooManyRequests
        RETRYAFTERFLAG:
          name: '是否携带Retry-After消息头'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: NO
        SENDTHD:
          name: '发送消息流控门限(条/秒)'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TIMER:
          name: 'Retry-After时长(秒)'
          type: integer
          minimum: 0
          maximum: 3600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 180
    set_httpglbfixedbwfc_list:
      type: items
      properties:
        SENDFCSWITCH:
          name: '全局固定带宽流控出局开关'
          type: string
          enum:
          - ON
          - OFF
          required: true
          description: '配置全局固定带宽流控相关信息。  说明：  此处理取值仅为举例，请根据局点实际情况进行配置。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        RECVFCSWITCH:
          name: '全局固定带宽流控入局开关'
          type: string
          enum:
          - ON
          - OFF
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SENDTHD:
          name: '发送消息带宽流控门限(KBytes/s)'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RECVTHD:
          name: '接收消息带宽流控门限(KBytes/s)'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SENDBIGPKTTHD:
          name: '发送消息大包阈值(KByte)'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RECVBIGPKTTHD:
          name: '接收消息大包阈值(KByte)'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        STATUSCODE:
          name: '状态码'
          type: string
          enum:
          - TooManyRequests
          - ServiceUnavailable
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_httpconf_list:
      type: items
      properties:
        REQCBFCSW:
          name: 'Reqcb流控开关'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: '开启ReqCB流控开关。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_httprescfg_list:
      type: items
      properties:
        INDEX:
          name: 'HTTP资源门限索引'
          type: integer
          minimum: 1
          maximum: 4096
          required: true
          description: '配置基于ReqCB资源的流控信息。  说明：  此处仅以本端作为HTTP Client为例，请根据局点实际情况进行配置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        RESTYPE:
          name: '资源类型'
          type: string
          enum:
          - REQCB
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LETYPE:
          name: '本端实体类型'
          type: string
          enum:
          - CLIENT
          - SERVER
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERIPTYPE:
          name: '对端地址IP类型'
          type: string
          enum:
          - IPv4
          - IPv6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERIPV4:
          name: '对端IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        THRESHOLD:
          name: '资源门限'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERIPV6:
          name: '对端IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_httpmemfc_list:
      type: items
      properties:
        MEMFCSWITCH:
          name: '内存流控开关'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: '开启内存流控开关并配置相关阈值。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MEMFCSTARTTHD:
          name: '内存流控起控阈值'
          type: integer
          minimum: 0
          maximum: 512
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MEMFCSTOPTHD:
          name: '内存流控停控阈值'
          type: integer
          minimum: 0
          maximum: 512
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MEMFCBIGPKTTHD:
          name: '内存流控大包阈值'
          type: integer
          minimum: 0
          maximum: 16384
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_httpfcipgrp_list:
    - INDEX: 1
      GROUP: 1
      IPTYPE: IPv4
      IPV4ADDR: '192.168.100.1'
      IPV4MASK: '255.255.255.0'
      DESC: 'AMF_instance1'
      IPV6ADDR: ''
      IPV6MASK: ''
    - INDEX: 3
      GROUP: 2
      IPTYPE: IPv4
      IPV4ADDR: '192.168.200.1'
      IPV4MASK: '255.255.255.0'
      DESC: 'AMF_instance1'
      IPV6ADDR: ''
      IPV6MASK: ''
    add_httpfixedfc_list:
    - GROUP: 1
      GROUPTYPE: SERVER
      RECVTHD: 1000
      STATUSCODE: TooManyRequests
      RETRYAFTERFLAG: NO
      DESC: 'LINK'
      TIMER: 180
    add_httpfixedfc_list_1:
    - GROUP: 2
      GROUPTYPE: SERVER
      GLBRECVTHD: 2000
      STATUSCODE: TooManyRequests
      RETRYAFTERFLAG: NO
      DESC: 'GLOBAL'
      TIMER: 180
    set_httpfixedfcmsg_list:
    - MSGTYPE: NSMF_PDUSESSION_SMCONTEXTSCREATE
      FCSWITCH: ON
      THRESHOLD: 1200
    add_httpofc_list:
    - OFCIDX: 1
      OFCTYPE: NFTYPE
      PEERNFTYPE: NFTypeAMF
      NFITEM: HTRINTF-0&FIXSPDFCINTF-1
      LOCALNFTYPE: NFTypeSMF
      OFCNAME: 'SMF2AMFFIXSPDFCINTF'
      IPGROUP: ''
      IPGRPITEM: ''
    add_httpfixedfcinf_list:
    - OFCIDX: 1
      LETYPE: SERVER
      RECVTHD: 1200
      STATUSCODE: TooManyRequests
      RETRYAFTERFLAG: NO
      SENDTHD: ''
      TIMER: 180
    set_httpglbfixedbwfc_list:
    - SENDFCSWITCH: ON
      RECVFCSWITCH: ON
      SENDTHD: 15000
      RECVTHD: 15000
      SENDBIGPKTTHD: 1024
      RECVBIGPKTTHD: 1024
      STATUSCODE: TooManyRequests
    set_httpconf_list:
    - REQCBFCSW: TRUE
    add_httprescfg_list:
    - INDEX: 1
      RESTYPE: REQCB
      LETYPE: CLIENT
      PEERIPTYPE: IPv4
      PEERIPV4: '192.168.1.1'
      THRESHOLD: 100
      PEERIPV6: '2001:0db8::1'
    set_httpmemfc_list:
    - MEMFCSWITCH: TRUE
      MEMFCSTARTTHD: 30
      MEMFCSTOPTHD: 50
      MEMFCBIGPKTTHD: 512
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 增加HTTP固定速率流控的IP地址组信息。

#### 1.1 //配置流控组信息。

```jinja2
{%- for item in add_httpfcipgrp_list -%}
    ADD HTTPFCIPGRP:
    {#- --- 必选参数 --- -#}
    INDEX={{item.INDEX}},
    GROUP={{item.GROUP}},
    IPTYPE={{item.IPTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPTYPE=IPv4 时必选 --- -#}
    {%- if item.IPTYPE == 'IPv4' -%}
        IPV4ADDR="{{item.IPV4ADDR}}",
    {%- endif -%}
    {#- --- 条件必选：IPTYPE=IPv4 时必选 --- -#}
    {%- if item.IPTYPE == 'IPv4' -%}
        IPV4MASK="{{item.IPV4MASK}}",
    {%- endif -%}
    {#- --- 条件必选：IPTYPE=IPv6 时必选 --- -#}
    {%- if item.IPTYPE == 'IPv6' -%}
        IPV6ADDR="{{item.IPV6ADDR}}",
    {%- endif -%}
    {#- --- 条件必选：IPTYPE=IPv6 时必选 --- -#}
    {%- if item.IPTYPE == 'IPv6' -%}
        IPV6MASK={{item.IPV6MASK}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 增加HTTP固定速率流控门限。

#### 2.1 //配置流控速率。

```jinja2
{%- for item in add_httpfixedfc_list -%}
    ADD HTTPFIXEDFC:
    {#- --- 必选参数 --- -#}
    GROUP={{item.GROUP}},
    {#- --- 可选参数 --- -#}
    {%- if item.GROUPTYPE is not none -%}
        GROUPTYPE={{item.GROUPTYPE}},
    {%- endif -%}
    {%- if item.RECVTHD is not none -%}
        RECVTHD={{item.RECVTHD}},
    {%- endif -%}
    {%- if item.STATUSCODE is not none -%}
        STATUSCODE={{item.STATUSCODE}},
    {%- endif -%}
    {%- if item.RETRYAFTERFLAG is not none -%}
        RETRYAFTERFLAG={{item.RETRYAFTERFLAG}},
    {%- endif -%}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：RETRYAFTERFLAG=YES 时可选 --- -#}
    {%- if item.RETRYAFTERFLAG == 'YES' -%}
        {%- if item.TIMER is not none -%}
            TIMER={{item.TIMER}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.2 //配置流控速率。

```jinja2
{%- for item in add_httpfixedfc_list_1 -%}
    ADD HTTPFIXEDFC:
    {#- --- 必选参数 --- -#}
    GROUP={{item.GROUP}},
    {#- --- 可选参数 --- -#}
    {%- if item.GROUPTYPE is not none -%}
        GROUPTYPE={{item.GROUPTYPE}},
    {%- endif -%}
    {%- if item.GLBRECVTHD is not none -%}
        GLBRECVTHD={{item.GLBRECVTHD}},
    {%- endif -%}
    {%- if item.STATUSCODE is not none -%}
        STATUSCODE={{item.STATUSCODE}},
    {%- endif -%}
    {%- if item.RETRYAFTERFLAG is not none -%}
        RETRYAFTERFLAG={{item.RETRYAFTERFLAG}},
    {%- endif -%}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：RETRYAFTERFLAG=YES 时可选 --- -#}
    {%- if item.RETRYAFTERFLAG == 'YES' -%}
        {%- if item.TIMER is not none -%}
            TIMER={{item.TIMER}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置指定类型的消息是否开启固定速率流控。

#### 3.1 //配置指定消息类型的固定速率流控。

```jinja2
{%- for item in set_httpfixedfcmsg_list -%}
    SET HTTPFIXEDFCMSG:
    {#- --- 必选参数 --- -#}
    MSGTYPE={{item.MSGTYPE}},
    FCSWITCH={{item.FCSWITCH}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：FCSWITCH=ON 时可选 --- -#}
    {%- if item.FCSWITCH == 'ON' -%}
        {%- if item.THRESHOLD is not none -%}
            THRESHOLD={{item.THRESHOLD}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 增加基于接口类型的固定速率流控生效的HTTP局向。

#### 4.1 //增加基于接口类型的固定速率流控生效的HTTP局向。

```jinja2
{%- for item in add_httpofc_list -%}
    ADD HTTPOFC:
    {#- --- 必选参数 --- -#}
    OFCIDX={{item.OFCIDX}},
    OFCTYPE={{item.OFCTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.LOCALNFTYPE is not none -%}
        LOCALNFTYPE={{item.LOCALNFTYPE}},
    {%- endif -%}
    {%- if item.OFCNAME is not none -%}
        OFCNAME="{{item.OFCNAME}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：OFCTYPE=NFTYPE 时必选 --- -#}
    {%- if item.OFCTYPE == 'NFTYPE' -%}
        PEERNFTYPE={{item.PEERNFTYPE}},
    {%- endif -%}
    {#- --- 条件必选：OFCTYPE=NFTYPE 时必选 --- -#}
    {%- if item.OFCTYPE == 'NFTYPE' -%}
        NFITEM={{item.NFITEM}},
    {%- endif -%}
    {#- --- 条件必选：OFCTYPE=IPGROUP 时必选 --- -#}
    {%- if item.OFCTYPE == 'IPGROUP' -%}
        IPGROUP={{item.IPGROUP}},
    {%- endif -%}
    {#- --- 条件必选：OFCTYPE=IPGROUP 时必选 --- -#}
    {%- if item.OFCTYPE == 'IPGROUP' -%}
        IPGRPITEM={{item.IPGRPITEM}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 配置基于接口类型的固定速率流控。

#### 5.1 //配置基于接口类型的固定速率流控。

```jinja2
{%- for item in add_httpfixedfcinf_list -%}
    ADD HTTPFIXEDFCINF:
    {#- --- 必选参数 --- -#}
    OFCIDX={{item.OFCIDX}},
    LETYPE={{item.LETYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：LETYPE=SERVER 时必选 --- -#}
    {%- if item.LETYPE == 'SERVER' -%}
        RECVTHD={{item.RECVTHD}},
    {%- endif -%}
    {#- --- 条件必选：LETYPE=CLIENT 时必选 --- -#}
    {%- if item.LETYPE == 'CLIENT' -%}
        SENDTHD={{item.SENDTHD}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：LETYPE=SERVER 时可选 --- -#}
    {%- if item.LETYPE == 'SERVER' -%}
        {%- if item.STATUSCODE is not none -%}
            STATUSCODE={{item.STATUSCODE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：LETYPE=SERVER 时可选 --- -#}
    {%- if item.LETYPE == 'SERVER' -%}
        {%- if item.RETRYAFTERFLAG is not none -%}
            RETRYAFTERFLAG={{item.RETRYAFTERFLAG}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：RETRYAFTERFLAG=YES 时可选 --- -#}
    {%- if item.RETRYAFTERFLAG == 'YES' -%}
        {%- if item.TIMER is not none -%}
            TIMER={{item.TIMER}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 6 配置全局固定带宽流控相关信息。

#### 6.1 //配置全局固定带宽流控。

```jinja2
{%- for item in set_httpglbfixedbwfc_list -%}
    SET HTTPGLBFIXEDBWFC:
    {#- --- 必选参数 --- -#}
    SENDFCSWITCH={{item.SENDFCSWITCH}},
    RECVFCSWITCH={{item.RECVFCSWITCH}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：SENDFCSWITCH=ON 时必选 --- -#}
    {%- if item.SENDFCSWITCH == 'ON' -%}
        SENDTHD={{item.SENDTHD}},
    {%- endif -%}
    {#- --- 条件必选：SENDFCSWITCH=ON 时必选 --- -#}
    {%- if item.SENDFCSWITCH == 'ON' -%}
        SENDBIGPKTTHD={{item.SENDBIGPKTTHD}},
    {%- endif -%}
    {#- --- 条件必选：RECVFCSWITCH=ON 时必选 --- -#}
    {%- if item.RECVFCSWITCH == 'ON' -%}
        RECVTHD={{item.RECVTHD}},
    {%- endif -%}
    {#- --- 条件必选：RECVFCSWITCH=ON 时必选 --- -#}
    {%- if item.RECVFCSWITCH == 'ON' -%}
        RECVBIGPKTTHD={{item.RECVBIGPKTTHD}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：SENDFCSWITCH=ON 时可选 --- -#}
    {%- if item.SENDFCSWITCH == 'ON' -%}
        {%- if item.STATUSCODE is not none -%}
            STATUSCODE={{item.STATUSCODE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 7 开启ReqCB流控开关。

#### 7.1 //开启ReqCB流控开关。

```jinja2
{%- for item in set_httpconf_list -%}
    SET HTTPCONF:
    {#- --- 可选参数 --- -#}
    {%- if item.REQCBFCSW is not none -%}
        REQCBFCSW={{item.REQCBFCSW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 8 配置基于ReqCB资源的流控信息。

#### 8.1 //配置基于ReqCB资源的流控信息。

```jinja2
{%- for item in add_httprescfg_list -%}
    ADD HTTPRESCFG:
    {#- --- 必选参数 --- -#}
    INDEX={{item.INDEX}},
    RESTYPE={{item.RESTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：RESTYPE=REQCB 时必选 --- -#}
    {%- if item.RESTYPE == 'REQCB' -%}
        LETYPE={{item.LETYPE}},
    {%- endif -%}
    {#- --- 条件必选：RESTYPE=REQCB 时必选 --- -#}
    {%- if item.RESTYPE == 'REQCB' -%}
        PEERIPTYPE={{item.PEERIPTYPE}},
    {%- endif -%}
    {#- --- 条件必选：PEERIPTYPE=IPv4 时必选 --- -#}
    {%- if item.PEERIPTYPE == 'IPv4' -%}
        PEERIPV4="{{item.PEERIPV4}}",
    {%- endif -%}
    {#- --- 条件必选：RESTYPE=REQCB 时必选 --- -#}
    {%- if item.RESTYPE == 'REQCB' -%}
        THRESHOLD={{item.THRESHOLD}},
    {%- endif -%}
    {#- --- 条件必选：PEERIPTYPE=IPv6 时必选 --- -#}
    {%- if item.PEERIPTYPE == 'IPv6' -%}
        PEERIPV6="{{item.PEERIPV6}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 9 配置基于内存的流控信息。

#### 9.1 //配置基于内存资源的流控信息。

```jinja2
{%- for item in set_httpmemfc_list -%}
    SET HTTPMEMFC:
    {#- --- 可选参数 --- -#}
    {%- if item.MEMFCSWITCH is not none -%}
        MEMFCSWITCH={{item.MEMFCSWITCH}},
    {%- endif -%}
    {%- if item.MEMFCSTARTTHD is not none -%}
        MEMFCSTARTTHD={{item.MEMFCSTARTTHD}},
    {%- endif -%}
    {%- if item.MEMFCSTOPTHD is not none -%}
        MEMFCSTOPTHD={{item.MEMFCSTOPTHD}},
    {%- endif -%}
    {%- if item.MEMFCBIGPKTTHD is not none -%}
        MEMFCBIGPKTTHD={{item.MEMFCBIGPKTTHD}},
    {%- endif -%}
    ;
{%- endfor -%}
```

