---
id: ''
name: 激活服务化接口流控
ne_type: UNC
type: feature
description: 本操作用于指导在运行网络中激活服务化接口流控。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","流控功能","WSFD-010802 周边网元过载保护","服务化接口流控功能","激活服务化接口流控"]
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

请仔细阅读WSFD-010802 周边网元过载保护特性概述（服务化接口流控）。
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
          description: '设置流控组信息。  说明：  本端网元作为客户端的业务，选择对端网元的IP地址作为流控组的IP地址，如果是间接路由场景，选择下一跳（例如SCP）的IP地址作为流控组的IP地址；本端网元作为服务端的业务，选择本端网元配置的HTTPLE的服务端IP作为流控组的IP地址。'
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
        SENDTHD:
          name: '单链路发送消息流控门限(条/秒)'
          type: integer
          minimum: 1
          maximum: 1000000
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
        GLBSENDTHD:
          name: '整系统发送消息流控门限(条/秒)'
          type: integer
          minimum: 1
          maximum: 4294967295
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
          description: '增加基于接口类型的固定速率流控生效的HTTP局向。  说明：  此处仅以AMF到UDM的局向举例，请根据网络实际情况配置所有局向。'
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
          description: '增加基于接口类型的固定速率流控的门限相关配置。  说明：  * 此处取值均为举例，请根据网络实际情况配置。 * UNC作为HTTP客户端，为保护周边网元不会过载，需要对发送的消息速率进行控制。'
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
        SENDTHD:
          name: '发送消息流控门限(条/秒)'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
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
          data_source: ''
          pattern: ''
          default: ''
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
          default: NO
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
  examples:
    add_httpfcipgrp_list:
    - INDEX: 1
      GROUP: 1
      IPTYPE: IPv4
      IPV4ADDR: '192.168.100.1'
      IPV4MASK: '255.255.255.0'
      DESC: 'UDM_instance1'
      IPV6ADDR: ''
      IPV6MASK: ''
    add_httpfixedfc_list:
    - GROUP: 1
      GROUPTYPE: CLIENT
      SENDTHD: 1000
      DESC: 'LINK'
      GLBSENDTHD: 2000
    add_httpofc_list:
    - OFCIDX: 0
      OFCTYPE: NFTYPE
      PEERNFTYPE: NFTypeUDM
      NFITEM: HTRINTF-0&FIXSPDFCINTF-1
      LOCALNFTYPE: NFTypeAMF
      OFCNAME: 'AMF2UDMFIXSPDFCINTF'
      IPGROUP: ''
      IPGRPITEM: ''
    add_httpfixedfcinf_list:
    - OFCIDX: 0
      LETYPE: CLIENT
      SENDTHD: 1000
      RECVTHD: ''
      RETRYAFTERFLAG: NO
      STATUSCODE: TooManyRequests
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 增加HTTP固定速率流控的IP地址组信息。

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

```jinja2
{%- for item in add_httpfixedfc_list -%}
    ADD HTTPFIXEDFC:
    {#- --- 必选参数 --- -#}
    GROUP={{item.GROUP}},
    {#- --- 可选参数 --- -#}
    {%- if item.GROUPTYPE is not none -%}
        GROUPTYPE={{item.GROUPTYPE}},
    {%- endif -%}
    {%- if item.SENDTHD is not none -%}
        SENDTHD={{item.SENDTHD}},
    {%- endif -%}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    {%- if item.GLBSENDTHD is not none -%}
        GLBSENDTHD={{item.GLBSENDTHD}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 增加基于接口类型的固定速率流控生效的HTTP局向。

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

### 4 配置基于接口类型的固定速率流控。

```jinja2
{%- for item in add_httpfixedfcinf_list -%}
    ADD HTTPFIXEDFCINF:
    {#- --- 必选参数 --- -#}
    OFCIDX={{item.OFCIDX}},
    LETYPE={{item.LETYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：LETYPE=CLIENT 时必选 --- -#}
    {%- if item.LETYPE == 'CLIENT' -%}
        SENDTHD={{item.SENDTHD}},
    {%- endif -%}
    {#- --- 条件必选：LETYPE=SERVER 时必选 --- -#}
    {%- if item.LETYPE == 'SERVER' -%}
        RECVTHD={{item.RECVTHD}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：LETYPE=SERVER 时可选 --- -#}
    {%- if item.LETYPE == 'SERVER' -%}
        {%- if item.RETRYAFTERFLAG is not none -%}
            RETRYAFTERFLAG={{item.RETRYAFTERFLAG}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：LETYPE=SERVER 时可选 --- -#}
    {%- if item.LETYPE == 'SERVER' -%}
        {%- if item.STATUSCODE is not none -%}
            STATUSCODE={{item.STATUSCODE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

