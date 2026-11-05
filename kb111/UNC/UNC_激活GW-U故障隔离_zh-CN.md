---
id: ''
name: 激活GW-U故障隔离
ne_type: UNC
type: feature
description: 当运营商需要部署GW-U故障隔离功能时，需要对本功能进行配置，确保本功能可以正常使用。  适用于GGSN、SGW-C、PGW-C。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","容灾功能","WSFD-213004 GW-U故障隔离","激活GW-U故障隔离"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当运营商需要部署GW-U故障隔离功能时，需要对本功能进行配置，确保本功能可以正常使用。适用于GGSN、SGW-C、PGW-C。

## 必备事项
前提条件

* 请仔细阅读WSFD-213004 GW-U故障隔离特性概述。
* 完成加载License。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_licenseswitch_list:
      type: items
      properties:
        LICITEM:
          name: 'License项'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SWITCH:
          name: '开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_upbinds11_list:
      type: items
      properties:
        NFINSTANCENAME:
          name: 'SGW-U实例名称'
          type: string
          minLength: 1
          maxLength: 36
          required: true
          description: '增加SGW-U与SGW-C侧S11接口的绑定关系'
          data_source: '本端规划'
          pattern: ''
          default: ''
        S11IPTYPE:
          name: 'S11口地址类型'
          type: string
          enum:
          - IPv4
          - IPv6
          - ALL
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        S11IPV4:
          name: 'S11口IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PRIORITY:
          name: 'S11口优先级'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        S11IPV6:
          name: 'S11口IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_upbindgngp_list:
      type: items
      properties:
        NFINSTANCENAME:
          name: 'GGSN实例名称'
          type: string
          minLength: 1
          maxLength: 36
          required: true
          description: '增加GGSN-U与GGSN-C侧Gn/Gp接口的绑定关系。  增加PGW-U与PGW-C侧S5_P/S8_P接口的绑定关系。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        GNGPIPTYPE:
          name: 'Gn/Gp口地址类型'
          type: string
          enum:
          - IPv4
          - IPv6
          - ALL
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        GNGPIPV4:
          name: 'Gn/Gp口IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        GNGPIPV6:
          name: 'Gn/Gp或S5/S8口IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_spgwcausectrl_list:
      type: items
      properties:
        PROCEDURETYPE:
          name: '流程类型'
          type: string
          enum:
          - CRT_SES_PROC
          - MOD_BR_PROC
          required: true
          description: '设置PGW-C发送给SGW-C的失败原因值。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CAUSESOURCE:
          name: '异常来源'
          type: string
          enum:
          - UPF
          - POLICY_PCF
          - CHG_3GPP
          - POLICY_PCRF
          - RADIUS_AUTH
          - INNER
          - RADIUS_CHG
          - DIAMETER_AAA
          - CHF_3GPP
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        CAUSEEXPIRATION:
          name: '周边网元响应超时导致流程拒绝的原因值'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 0
        CAUSEAPNLOCK:
          name: 'APN锁定或整机锁定导致流程拒绝的GTPv2原因值'
          type: string
          enum:
          - SRVNOTSUPPORTED
          - APNCONGESTION
          - NORESOURCESAVAILABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: SRVNOTSUPPORTED
        CAUSEBRLIMIT:
          name: '承载受限原因值'
          type: string
          enum:
          - NORESOURCESAVAILABLE
          - APNCONGESTION
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NORESOURCESAVAILABLE
        CAUSEFC:
          name: '发送消息流控导致流程拒绝的GTPv2原因值'
          type: string
          enum:
          - USERAUTHFAILED
          - NORESOURCESAVAILABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: USERAUTHFAILED
        CAUSEIPOCCUPIED:
          name: 'IP地址耗尽导致流程拒绝的GTPv2原因值'
          type: string
          enum:
          - APNCONGESTION
          - ALLIPOCCUPIED
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ALLIPOCCUPIED
        CAUSEREJGROUPID:
          name: '周边网元拒绝导致流程拒绝原因值组号'
          type: integer
          minimum: 0
          maximum: 127
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        CAUSESELFFC:
          name: 'CPU过载原因值'
          type: string
          enum:
          - NORESOURCESAVAILABLE
          - SRVNOTSUPPORTED
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NORESOURCESAVAILABLE
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3GWUISL01'
      SWITCH: ENABLE
    add_upbinds11_list:
    - NFINSTANCENAME: 'UPF1'
      S11IPTYPE: Ipv4
      S11IPV4: '192.168.1.2'
      PRIORITY: 3
      S11IPV6: ''
    add_upbindgngp_list:
    - NFINSTANCENAME: 'UPF1'
      GNGPIPTYPE: Ipv4
      GNGPIPV4: '192.168.1.12'
      GNGPIPV6: ''
    add_spgwcausectrl_list:
    - PROCEDURETYPE: CRT_SES_PROC
      CAUSESOURCE: UPF
      CAUSEEXPIRATION: 73
      CAUSEAPNLOCK: SRVNOTSUPPORTED
      CAUSEBRLIMIT: NORESOURCESAVAILABLE
      CAUSEFC: USERAUTHFAILED
      CAUSEIPOCCUPIED: ALLIPOCCUPIED
      CAUSEREJGROUPID: ''
      CAUSESELFFC: NORESOURCESAVAILABLE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 打开本特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 3 配置SGW-U和S11的绑定关系。

```jinja2
{%- for item in add_upbinds11_list -%}
    ADD UPBINDS11:
    {#- --- 必选参数 --- -#}
    NFINSTANCENAME="{{item.NFINSTANCENAME}}",
    S11IPTYPE={{item.S11IPTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.PRIORITY is not none -%}
        PRIORITY={{item.PRIORITY}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：S11IPTYPE=IPv4 时必选 --- -#}
    {%- if item.S11IPTYPE == 'IPv4' -%}
        S11IPV4="{{item.S11IPV4}}",
    {%- endif -%}
    {#- --- 条件必选：S11IPTYPE=IPv6 时必选 --- -#}
    {%- if item.S11IPTYPE == 'IPv6' -%}
        S11IPV6="{{item.S11IPV6}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 配置GGSN-U/PGW-U和Gn/Gp/S5/S8接口的绑定关系。

```jinja2
{%- for item in add_upbindgngp_list -%}
    ADD UPBINDGNGP:
    {#- --- 必选参数 --- -#}
    NFINSTANCENAME="{{item.NFINSTANCENAME}}",
    GNGPIPTYPE={{item.GNGPIPTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：GNGPIPTYPE=IPv4 时必选 --- -#}
    {%- if item.GNGPIPTYPE == 'IPv4' -%}
        GNGPIPV4="{{item.GNGPIPV4}}",
    {%- endif -%}
    {#- --- 条件必选：GNGPIPTYPE=IPv6 时必选 --- -#}
    {%- if item.GNGPIPTYPE == 'IPv6' -%}
        GNGPIPV6="{{item.GNGPIPV6}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 设置PGW-C发送给SGW-C的失败原因值。

```jinja2
{%- for item in add_spgwcausectrl_list -%}
    ADD SPGWCAUSECTRL:
    {#- --- 必选参数 --- -#}
    PROCEDURETYPE={{item.PROCEDURETYPE}},
    CAUSESOURCE={{item.CAUSESOURCE}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：CAUSESOURCE=UPF/CHG_3GPP/RADIUS_AUTH/POLICY_PCF/POLICY_PCRF/RADIUS_CHG/DIAMETER_AAA/CHF_3GPP 时可选 --- -#}
    {%- if item.CAUSESOURCE in ['UPF', 'CHG_3GPP', 'RADIUS_AUTH', 'POLICY_PCF', 'POLICY_PCRF', 'RADIUS_CHG', 'DIAMETER_AAA', 'CHF_3GPP'] -%}
        {%- if item.CAUSEEXPIRATION is not none -%}
            CAUSEEXPIRATION={{item.CAUSEEXPIRATION}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CAUSESOURCE=INNER 时可选 --- -#}
    {%- if item.CAUSESOURCE == 'INNER' -%}
        {%- if item.CAUSEAPNLOCK is not none -%}
            CAUSEAPNLOCK={{item.CAUSEAPNLOCK}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CAUSESOURCE=INNER 时可选 --- -#}
    {%- if item.CAUSESOURCE == 'INNER' -%}
        {%- if item.CAUSEBRLIMIT is not none -%}
            CAUSEBRLIMIT={{item.CAUSEBRLIMIT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CAUSESOURCE=POLICY_PCF/POLICY_PCRF 时可选 --- -#}
    {%- if item.CAUSESOURCE in ['POLICY_PCF', 'POLICY_PCRF'] -%}
        {%- if item.CAUSEFC is not none -%}
            CAUSEFC={{item.CAUSEFC}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CAUSESOURCE=INNER 时可选 --- -#}
    {%- if item.CAUSESOURCE == 'INNER' -%}
        {%- if item.CAUSEIPOCCUPIED is not none -%}
            CAUSEIPOCCUPIED={{item.CAUSEIPOCCUPIED}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CAUSESOURCE=UPF/CHG_3GPP/RADIUS_AUTH/POLICY_PCF/POLICY_PCRF/RADIUS_CHG/DIAMETER_AAA/CHF_3GPP 时可选 --- -#}
    {%- if item.CAUSESOURCE in ['UPF', 'CHG_3GPP', 'RADIUS_AUTH', 'POLICY_PCF', 'POLICY_PCRF', 'RADIUS_CHG', 'DIAMETER_AAA', 'CHF_3GPP'] -%}
        {%- if item.CAUSEREJGROUPID is not none -%}
            CAUSEREJGROUPID={{item.CAUSEREJGROUPID}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CAUSESOURCE=INNER 时可选 --- -#}
    {%- if item.CAUSESOURCE == 'INNER' -%}
        {%- if item.CAUSESELFFC is not none -%}
            CAUSESELFFC={{item.CAUSESELFFC}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

