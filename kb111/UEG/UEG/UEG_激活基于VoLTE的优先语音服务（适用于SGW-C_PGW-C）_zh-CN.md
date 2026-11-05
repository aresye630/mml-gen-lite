---
id: ''
name: 激活基于VoLTE的优先语音服务（适用于SGW-C/PGW-C）
ne_type: UEG
type: feature
description: 在UEG上激活基于VoLTE的优先语音服务，支持异常情况下的通话场景。  适用于SGW-C、PGW-C。
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝L”，入驻式）","配置业务数据（风筝L）","语音功能配置","MME&AMF&GW-C&SMF配置","VoLTE基本功能","激活基于VoLTE的优先语音服务（适用于SGW-C/PGW-C）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
在UEG上激活基于VoLTE的优先语音服务，支持异常情况下的通话场景。适用于SGW-C、PGW-C。

## 必备事项
前提条件

* 已经加载支持该特性的License。
* 请仔细阅读GWFD-025402 基于VoLTE的优先语音服务特性概述。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
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
          description: '控制SGW-C/PGW-C在Downlink Data Notification消息中是否携带EBI信元。'
          data_source: '本端规划'
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
          data_source: '本端规划'
          pattern: ''
          default: ''
        ARP:
          name: '携带ARP'
          type: string
          enum:
          - Disable
          - Enable
          required: false
          description: '控制SGW-C/PGW-C在Downlink Data Notification消息中是否携带ARP信元。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ARPVALUE:
          name: 'ARP值'
          type: string
          enum:
          - TriDDNBearer
          - DefaultBearer
          required: false
          description: ''
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
          description: '-'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PPDSWITCH:
          name: 'Ppd功能开关'
          type: string
          enum:
          - INHERIT
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: INHERIT
  examples:
    set_ddnattr_list:
    - EBI: Enable
      EBIVALUE: TriDDNBearer
      ARP: Enable
      ARPVALUE: TriDDNBearer
    add_cpapn_list:
    - APN: 'ims'
      PPDSWITCH: ENABLE
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 配置ARP参数。

```jinja2
{%- for item in set_ddnattr_list -%}
    SET DDNATTR:
    {#- --- 可选参数 --- -#}
    {%- if item.EBI is not none -%}
        EBI={{item.EBI}},
    {%- endif -%}
    {%- if item.ARP is not none -%}
        ARP={{item.ARP}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：EBI=Enable 时必选 --- -#}
    {%- if item.EBI == 'Enable' -%}
        EBIVALUE={{item.EBIVALUE}},
    {%- endif -%}
    {#- --- 条件必选：ARP=Enable 时必选 --- -#}
    {%- if item.ARP == 'Enable' -%}
        ARPVALUE={{item.ARPVALUE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 打开PPD功能开关。

```jinja2
{%- for item in add_cpapn_list -%}
    ADD CPAPN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.PPDSWITCH is not none -%}
        PPDSWITCH={{item.PPDSWITCH}},
    {%- endif -%}
    ;
{%- endfor -%}
```

