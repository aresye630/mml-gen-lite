---
id: ''
name: 激活VoLTE基础语音业务（适用于SGW-C/PGW-C）
ne_type: UEG
type: feature
description: 本操作指导介绍在运行网络中激活VoLTE基础语音业务的操作过程。
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝L”，入驻式）","配置业务数据（风筝L）","语音功能配置","MME&AMF&GW-C&SMF配置","VoLTE基本功能","激活VoLTE基础语音业务（适用于SGW-C/PGW-C）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活VoLTE基础语音业务的操作过程。

## 必备事项
前提条件

* 请仔细阅读GWFD-025401 VoLTE基础语音业务特性概述
* 本特性受License控制，请先完成加载License。
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
    set_pccfunc_list:
      type: items
      properties:
        HOMEPCCSWITCH:
          name: '本地用户动态PCC功能'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
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
          name: '本地用户动态PCC功能'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: ''
          data_source: ''
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
    set_cpapnimsattr_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMSSWITCH:
          name: 'IMS开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: '开启IMS功能开关。  业务处理过程中优先应用APN下的设置，只有当APN下配置为“INHERIT”时才应用全局下的设置。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SIGNALRADIOPRE:
          name: '信令空口增强开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '用于开启IMS信令空口增强功能。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_ddnattr_list:
      type: items
      properties:
        EBI:
          name: '携带EBI'
          type: string
          enum:
          - Disable
          - Enable
          required: false
          description: '配置支持在Downlink Data Notification消息中携带EBI信元。  协议中Downlink Data Notification消息中的Bearer ID为可选信元，为确保MME能够通过Downlink Data Notification消息中的Bearer ID识别VoLTE语音被叫，需要配置此功能。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        EBIVALUE:
          name: 'EBI值'
          type: string
          enum:
          - TriDDNBearer
          - DefaultBearer
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_confctrl_list:
      type: items
      properties:
        EPSRETRYTIMES:
          name: 'EPS消息缓存重发的次数'
          type: integer
          minimum: 0
          maximum: 15
          required: false
          description: '配置Create Bearer Request/Update Bearer Request/Delete Bearer Request消息缓存重发的次数。次数达到设置值时，消息将被丢弃。  说明：  EPSRETRYTIMES建议默认值为3。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        EPSTIMEOUT:
          name: 'EPS消息缓存重发的时间间隔(s)'
          type: integer
          minimum: 1
          maximum: 4
          required: false
          description: '配置从收到Create Bearer Response/Update Bearer Response/Delete Bearer Response消息开始，到重发Create Bearer Request/Update Bearer Request/Delete Bearer Request消息的时间间隔(s)。'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3W9IMSA12'
      SWITCH: ENABLE
    set_pccfunc_list:
    - HOMEPCCSWITCH: ENABLE
    set_apnpccfunc_list:
    - APN: 'ims'
      HOMEPCCSWITCH: ENABLE
    add_pcrfgrpbndapn_list:
    - APN: 'ims'
      DEFAULTFLAG: DEFAULT
      PCRFGRPNAME: 'aaa'
    set_cpapnimsattr_list:
    - APN: 'ims'
      IMSSWITCH: ENABLE
      SIGNALRADIOPRE: ENABLE
    set_ddnattr_list:
    - EBI: Enable
      EBIVALUE: DefaultBearer
    set_confctrl_list:
    - EPSRETRYTIMES: 3
      EPSTIMEOUT: 2
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 打开License配置开关。

#### 1.1 进入“MML命令行-UEG”窗口。

#### 1.2 打开License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

#### 1.3 开启全局缺省PCC开关。

```jinja2
{%- for item in set_pccfunc_list -%}
    SET PCCFUNC:
    {#- --- 可选参数 --- -#}
    {%- if item.HOMEPCCSWITCH is not none -%}
        HOMEPCCSWITCH={{item.HOMEPCCSWITCH}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.4 开启APN下的PCC开关。

```jinja2
{%- for item in set_apnpccfunc_list -%}
    SET APNPCCFUNC:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.HOMEPCCSWITCH is not none -%}
        HOMEPCCSWITCH={{item.HOMEPCCSWITCH}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.5 将指定的PCRF分组及号段信息绑定到指定APN。

```jinja2
{%- for item in add_pcrfgrpbndapn_list -%}
    ADD PCRFGRPBNDAPN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    DEFAULTFLAG={{item.DEFAULTFLAG}},
    PCRFGRPNAME="{{item.PCRFGRPNAME}}",
    ;
{%- endfor -%}
```

### 2 配置基于APN的IMS业务

#### 2.1 配置IMS使能开关和IMS信令空口增强开关，绑定到指定APN实例下。

```jinja2
{%- for item in set_cpapnimsattr_list -%}
    SET CPAPNIMSATTR:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.IMSSWITCH is not none -%}
        IMSSWITCH={{item.IMSSWITCH}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IMSSWITCH=ENABLE 时可选 --- -#}
    {%- if item.IMSSWITCH == 'ENABLE' -%}
        {%- if item.SIGNALRADIOPRE is not none -%}
            SIGNALRADIOPRE={{item.SIGNALRADIOPRE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.2 配置支持在Downlink Data Notification消息中携带EBI信元。

```jinja2
{%- for item in set_ddnattr_list -%}
    SET DDNATTR:
    {#- --- 可选参数 --- -#}
    {%- if item.EBI is not none -%}
        EBI={{item.EBI}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：EBI=Enable 时必选 --- -#}
    {%- if item.EBI == 'Enable' -%}
        EBIVALUE={{item.EBIVALUE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.3 配置Create Bearer Request/Update Bearer Request/Delete Bearer Request消息缓存重发的次数；配置从收到Create Bearer Response/Update Bearer Response/Delete Bearer Response消息开始，到重发Create Bearer Request/Update Bearer Request/Delete Bearer Request消息的时间间隔(s)。

```jinja2
{%- for item in set_confctrl_list -%}
    SET CONFCTRL:
    {#- --- 可选参数 --- -#}
    {%- if item.EPSRETRYTIMES is not none -%}
        EPSRETRYTIMES={{item.EPSRETRYTIMES}},
    {%- endif -%}
    {%- if item.EPSTIMEOUT is not none -%}
        EPSTIMEOUT={{item.EPSTIMEOUT}},
    {%- endif -%}
    ;
{%- endfor -%}
```

