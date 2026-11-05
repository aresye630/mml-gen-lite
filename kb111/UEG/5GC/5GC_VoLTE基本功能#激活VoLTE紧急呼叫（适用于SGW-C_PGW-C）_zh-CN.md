---
id: ''
name: 激活VoLTE紧急呼叫（适用于SGW-C/PGW-C）
ne_type: UEG
type: feature
description: 在SGW-C/PGW-C上激活VoLTE紧急呼叫功能。  紧急呼叫不需要进行鉴权，建议紧急APN的地址分配方式采用本地分配或DHCP分配，本文档以本地地址分配为例。  VoLTE紧急呼叫和VoLTE普通呼叫使用不同的承载来传输，因此紧急呼叫的APN名称和相关数据需要分别规划，与普通呼叫的APN区分开。
tags: []
risk_level: ''
doc_source: ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（火电专网，入驻式）","部署配置指导","中心园区部署入驻式UEG-L","配置业务数据（风筝L）","语音功能配置","MME&AMF&GW-C&SMF配置","VoLTE基本功能","激活VoLTE紧急呼叫（适用于SGW-C/PGW-C）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
在SGW-C/PGW-C上激活VoLTE紧急呼叫功能。紧急呼叫不需要进行鉴权，建议紧急APN的地址分配方式采用本地分配或DHCP分配，本文档以本地地址分配为例。VoLTE紧急呼叫和VoLTE普通呼叫使用不同的承载来传输，因此紧急呼叫的APN名称和相关数据需要分别规划，与普通呼叫的APN区分开。

## 必备事项
前提条件

* 请仔细阅读GWFD-025403 VoLTE紧急呼叫。
* 完成加载License。
* 在MME、SGW-C、PGW-C、MSC、eNodeB等网元上完成VoLTE基本业务的数据配置。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
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
    add_cpvpninst_list:
      type: items
      properties:
        VPNINSTANCE:
          name: 'VPN实例名'
          type: string
          minLength: 1
          maxLength: 31
          required: true
          description: '配置APN所属的VPN实例。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_cpapn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '使能紧急呼叫功能。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        HASVPN:
          name: '绑定VPN'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
        VPNINSTANCE:
          name: 'VPN实例名'
          type: string
          minLength: 1
          maxLength: 31
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        EMERGENCYSWITCH:
          name: '支持紧急呼叫'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
    set_apnpccfunc_list:
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
        HOMEPCCSWITCH:
          name: '本地用户PCC功能'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: '使能紧急APN的PCC功能。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ROAMPCCSWITCH:
          name: '漫游用户PCC功能'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        VISITPCCSWITCH:
          name: '拜访用户PCC功能'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_apnidletime_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        INHERIT:
          name: '继承默认开关'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SCTXCHKSW:
          name: 'SGW-C空闲上下文核查开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PCTXCHKSW:
          name: 'PGW-C和SGW-C/PGW-C空闲上下文检查开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GCTXCHKSW:
          name: 'GGSN空闲上下文检查开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HCTXCHKSW:
          name: 'H-SMF空闲上下文核查开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ICTXCHKSW:
          name: 'I-SMF/V-SMF空闲上下文核查开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GULTIMERLEVEL:
          name: 'GUL承载级别参数'
          type: string
          enum:
          - SESSION
          - BEARER
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DFTBEARPOLICY:
          name: '缺省承载和默认GBR的定时器'
          type: string
          enum:
          - ONEDAY
          - OFF
          - USEBEARERTIMER
          - USESPECIFICVAL
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BEARERTIMER:
          name: '承载定时器(min)'
          type: integer
          minimum: 5
          maximum: 12000
          required: false
          description: '配置紧急呼叫结束后释放缺省承载。  对于“BEARERTIMER”时长参数，如果运营商没有特殊要求，建议保持默认值60分钟。'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3W9ECAL11'
      SWITCH: ENABLE
    add_cpvpninst_list:
    - VPNINSTANCE: 'vpn1'
    add_cpapn_list:
    - APN: 'sos'
      HASVPN: ENABLE
      VPNINSTANCE: 'vpn1'
      EMERGENCYSWITCH: ENABLE
    set_apnpccfunc_list:
    - APN: 'sos'
      HOMEPCCSWITCH: ENABLE
      ROAMPCCSWITCH: INHERIT
      VISITPCCSWITCH: INHERIT
    set_apnidletime_list:
    - APN: 'sos'
      INHERIT: NO
      SCTXCHKSW: ENABLE
      PCTXCHKSW: ENABLE
      GCTXCHKSW: ENABLE
      HCTXCHKSW: ENABLE
      ICTXCHKSW: ENABLE
      GULTIMERLEVEL: BEARER
      DFTBEARPOLICY: ONEDAY
      BEARERTIMER: 60
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 打开License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 3 配置APN参数。

#### 3.1 配置APN所属的VPN实例。

```jinja2
{%- for item in add_cpvpninst_list -%}
    ADD CPVPNINST:
    {#- --- 必选参数 --- -#}
    VPNINSTANCE="{{item.VPNINSTANCE}}",
    ;
{%- endfor -%}
```

#### 3.2 创建APN实例，使能紧急呼叫功能。

```jinja2
{%- for item in add_cpapn_list -%}
    ADD CPAPN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.HASVPN is not none -%}
        HASVPN={{item.HASVPN}},
    {%- endif -%}
    {%- if item.EMERGENCYSWITCH is not none -%}
        EMERGENCYSWITCH={{item.EMERGENCYSWITCH}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：HASVPN=ENABLE 时必选 --- -#}
    {%- if item.HASVPN == 'ENABLE' -%}
        VPNINSTANCE="{{item.VPNINSTANCE}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 若此APN上已有用户，则已接入的用户仍然按照普通APN处理，新接入的用户按照紧急呼叫用户处理。

#### 3.3 使能APN的PCC功能。

```jinja2
{%- for item in set_apnpccfunc_list -%}
    SET APNPCCFUNC:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.HOMEPCCSWITCH is not none -%}
        HOMEPCCSWITCH={{item.HOMEPCCSWITCH}},
    {%- endif -%}
    {%- if item.ROAMPCCSWITCH is not none -%}
        ROAMPCCSWITCH={{item.ROAMPCCSWITCH}},
    {%- endif -%}
    {%- if item.VISITPCCSWITCH is not none -%}
        VISITPCCSWITCH={{item.VISITPCCSWITCH}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 配置紧急呼叫结束后释放缺省承载。

```jinja2
{%- for item in set_apnidletime_list -%}
    SET APNIDLETIME:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.INHERIT is not none -%}
        INHERIT={{item.INHERIT}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：INHERIT=NO 时可选 --- -#}
    {%- if item.INHERIT == 'NO' -%}
        {%- if item.SCTXCHKSW is not none -%}
            SCTXCHKSW={{item.SCTXCHKSW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：INHERIT=NO 时可选 --- -#}
    {%- if item.INHERIT == 'NO' -%}
        {%- if item.PCTXCHKSW is not none -%}
            PCTXCHKSW={{item.PCTXCHKSW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：INHERIT=NO 时可选 --- -#}
    {%- if item.INHERIT == 'NO' -%}
        {%- if item.GCTXCHKSW is not none -%}
            GCTXCHKSW={{item.GCTXCHKSW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：INHERIT=NO 时可选 --- -#}
    {%- if item.INHERIT == 'NO' -%}
        {%- if item.HCTXCHKSW is not none -%}
            HCTXCHKSW={{item.HCTXCHKSW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：INHERIT=NO 时可选 --- -#}
    {%- if item.INHERIT == 'NO' -%}
        {%- if item.ICTXCHKSW is not none -%}
            ICTXCHKSW={{item.ICTXCHKSW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：INHERIT=NO 时可选 --- -#}
    {%- if item.INHERIT == 'NO' -%}
        {%- if item.GULTIMERLEVEL is not none -%}
            GULTIMERLEVEL={{item.GULTIMERLEVEL}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：INHERIT=NO 时可选 --- -#}
    {%- if item.INHERIT == 'NO' -%}
        {%- if item.DFTBEARPOLICY is not none -%}
            DFTBEARPOLICY={{item.DFTBEARPOLICY}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：INHERIT=NO 时可选 --- -#}
    {%- if item.INHERIT == 'NO' -%}
        {%- if item.BEARERTIMER is not none -%}
            BEARERTIMER={{item.BEARERTIMER}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 紧急呼叫缺省承载创建以后，除非用户关机，否则缺省承载不会被删除。这样系统资源会被一直占用，为了回收系统资源，需要配置**SET APNIDLETIME**命令来释放缺省承载，考虑到可能会有回呼的场景，“BEARERTIMER”的时间不能设置为0，建议保持缺省值60分钟。

