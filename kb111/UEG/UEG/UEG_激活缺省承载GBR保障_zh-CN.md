---
id: GWFD-021313
name: 激活缺省承载GBR保障
ne_type: UEG
type: feature
description: 需要为WBB用户创建一个可以提供带宽保障的any to any的GBR专有承载时，需要激活缺省承载GBR保障。  适用于PGW-C、SMF
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","GW-C&SMF特性指南","GWFD-021300 接口功能","GWFD-021313 缺省承载GBR保障","激活缺省承载GBR保障"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
需要为WBB用户创建一个可以提供带宽保障的any to any的GBR专有承载时，需要激活缺省承载GBR保障。适用于PGW-C、SMF

## 必备事项
前提条件

* 请仔细阅读GWFD-021313 缺省承载GBR保障。
* 完成激活PCC基本功能（本地PCC）。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_dftgbrbearer_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          maxLength: 63
          required: true
          description: '使用 **ADD CPAPN**定义的APN名称。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DFTGBRBEARERSW:
          name: '缺省GBR承载开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: '部署缺省承载GBR保障功能时，必须设置为“ENABLE”。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        LOCQOSQCI:
          name: '缺省GBR承载QCI值'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: '用于设置缺省GBR承载的QCI值。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        LOCQOSARP:
          name: '缺省GBR承载ARP值'
          type: integer
          minimum: 1
          maximum: 15
          required: false
          description: '用于设置缺省GBR承载的ARP值。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        LOCQOSPREEMPCAP:
          name: '缺省GBR承载Pre-emption-Capability值'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '用于设置缺省GBR承载的抢占能力。资源限制时，是否可以抢占更低优先级别的业务占有的资源。此处以不抢占为例。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        LOCQOSPREEMPVUL:
          name: '缺省GBR承载Pre-emption-Vulnerability值'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '用于设置缺省GBR承载的被抢占能力。资源限制时，业务是否可以被更高优先级别的业务抢占。此处以允许被抢占为例。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        LOCQOSMBRUL:
          name: '缺省GBR承载UL MBR值（千比特/秒）'
          type: integer
          minimum: 1
          maximum: 20000000
          required: false
          description: '缺省GBR承载上行方向允许的最大比特率。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        LOCQOSMBRDL:
          name: '缺省GBR承载DL MBR值(千比特/秒)'
          type: integer
          minimum: 1
          maximum: 20000000
          required: false
          description: '缺省GBR承载下行方向允许的最大比特率。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        LOCQOSGBRUL:
          name: '缺省GBR承载UL GBR值（千比特/秒）'
          type: integer
          minimum: 1
          maximum: 20000000
          required: false
          description: '缺省GBR承载上行方向允许的保障比特率。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        LOCQOSGBRDL:
          name: '缺省GBR承载DL GBR值（千比特/秒）'
          type: integer
          minimum: 1
          maximum: 20000000
          required: false
          description: '缺省GBR承载下行方向允许的保障比特率。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SESSIONTERMINSW:
          name: '缺省GBR承载去活时去活PDU会话'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '用于设置缺省GBR承载去活时是否去活PDU会话。此处以不去活PDU会话为例。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ACCTYPE:
          name: '用户接入类型'
          type: string
          enum:
          - ALL
          - RAT5G
          - RATNON5G
          required: false
          description: '用于指定缺省GBR承载适用的用户接入类型。此处以非5G接入类型为例。'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_dftgbrbearer_list:
    - APN: 'apn-test'
      DFTGBRBEARERSW: ENABLE
      LOCQOSQCI: 4
      LOCQOSARP: 15
      LOCQOSPREEMPCAP: DISABLE
      LOCQOSPREEMPVUL: ENABLE
      LOCQOSMBRUL: 64
      LOCQOSMBRDL: 64
      LOCQOSGBRUL: 64
      LOCQOSGBRDL: 64
      SESSIONTERMINSW: DISABLE
      ACCTYPE: RAT5G
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 配置缺省GBR承载保障的相关参数。

```jinja2
{%- for item in set_dftgbrbearer_list -%}
    SET DFTGBRBEARER:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    DFTGBRBEARERSW={{item.DFTGBRBEARERSW}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：DFTGBRBEARERSW=ENABLE 时可选 --- -#}
    {%- if item.DFTGBRBEARERSW == 'ENABLE' -%}
        {%- if item.LOCQOSQCI is not none -%}
            LOCQOSQCI={{item.LOCQOSQCI}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：DFTGBRBEARERSW=ENABLE 时可选 --- -#}
    {%- if item.DFTGBRBEARERSW == 'ENABLE' -%}
        {%- if item.LOCQOSARP is not none -%}
            LOCQOSARP={{item.LOCQOSARP}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：DFTGBRBEARERSW=ENABLE 时可选 --- -#}
    {%- if item.DFTGBRBEARERSW == 'ENABLE' -%}
        {%- if item.LOCQOSPREEMPCAP is not none -%}
            LOCQOSPREEMPCAP={{item.LOCQOSPREEMPCAP}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：DFTGBRBEARERSW=ENABLE 时可选 --- -#}
    {%- if item.DFTGBRBEARERSW == 'ENABLE' -%}
        {%- if item.LOCQOSPREEMPVUL is not none -%}
            LOCQOSPREEMPVUL={{item.LOCQOSPREEMPVUL}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：DFTGBRBEARERSW=ENABLE 时可选 --- -#}
    {%- if item.DFTGBRBEARERSW == 'ENABLE' -%}
        {%- if item.LOCQOSMBRUL is not none -%}
            LOCQOSMBRUL={{item.LOCQOSMBRUL}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：DFTGBRBEARERSW=ENABLE 时可选 --- -#}
    {%- if item.DFTGBRBEARERSW == 'ENABLE' -%}
        {%- if item.LOCQOSMBRDL is not none -%}
            LOCQOSMBRDL={{item.LOCQOSMBRDL}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：DFTGBRBEARERSW=ENABLE 时可选 --- -#}
    {%- if item.DFTGBRBEARERSW == 'ENABLE' -%}
        {%- if item.LOCQOSGBRUL is not none -%}
            LOCQOSGBRUL={{item.LOCQOSGBRUL}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：DFTGBRBEARERSW=ENABLE 时可选 --- -#}
    {%- if item.DFTGBRBEARERSW == 'ENABLE' -%}
        {%- if item.LOCQOSGBRDL is not none -%}
            LOCQOSGBRDL={{item.LOCQOSGBRDL}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：DFTGBRBEARERSW=ENABLE 时可选 --- -#}
    {%- if item.DFTGBRBEARERSW == 'ENABLE' -%}
        {%- if item.SESSIONTERMINSW is not none -%}
            SESSIONTERMINSW={{item.SESSIONTERMINSW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：DFTGBRBEARERSW=ENABLE 时可选 --- -#}
    {%- if item.DFTGBRBEARERSW == 'ENABLE' -%}
        {%- if item.ACCTYPE is not none -%}
            ACCTYPE={{item.ACCTYPE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

