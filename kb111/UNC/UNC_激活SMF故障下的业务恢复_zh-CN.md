---
id: ''
name: 激活SMF故障下的业务恢复
ne_type: UNC
type: feature
description: 本章节指导如何在运行的5G网络中激活SMF故障下的业务恢复。  在SMF故障或重启场景下，AMF感知到SMF故障后，协助用户及时恢复VoNR语音业务，实现设备的容灾功能。  适用于AMF。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","语音功能","WSFD-221005 SMF故障下的业务恢复","激活SMF故障下的业务恢复"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本章节指导如何在运行的5G网络中激活SMF故障下的业务恢复。在SMF故障或重启场景下，AMF感知到SMF故障后，协助用户及时恢复VoNR语音业务，实现设备的容灾功能。适用于AMF。

## 必备事项
前提条件

* 请仔细阅读WSFD-221005 SMF故障下的业务恢复。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_amfsmfreset_list:
      type: items
      properties:
        SMFRESEL:
          name: 'SMF故障重选开关'
          type: string
          enum:
          - OFF
          - ON
          required: true
          description: '通过扫描任务方式进行语音业务恢复'
          data_source: '全网规划'
          pattern: ''
          default: ''
        RATE:
          name: '扫描速率(个/秒)'
          type: integer
          minimum: 1
          maximum: 20
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        INTERVAL:
          name: '单位扫描时间(秒)'
          type: integer
          minimum: 1
          maximum: 600
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SCANNUM:
          name: '单位扫描个数'
          type: integer
          minimum: 1
          maximum: 20
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SCANRATESW:
          name: '自定义扫描速率开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SRRECOVERSW:
          name: '语音业务恢复开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: '通过数据业务请求方式进行语音业务恢复'
          data_source: '全网规划'
          pattern: ''
          default: ''
        VOICEDNN:
          name: '语音业务DNN'
          type: string
          minLength: 1
          maxLength: 63
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
  examples:
    set_amfsmfreset_list:
    - SMFRESEL: ON
      RATE: 1
      INTERVAL: 1
      SCANNUM: 5
      SCANRATESW: OFF
      SRRECOVERSW: ON
      VOICEDNN: 'IMS'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 设置SMF故障或重启时，AMF对语音业务的业务恢复策略。

#### 1.1 //设置业务恢复策略。

```jinja2
{%- for item in set_amfsmfreset_list -%}
    SET AMFSMFRESET:
    {#- --- 必选参数 --- -#}
    SMFRESEL={{item.SMFRESEL}},
    {#- --- 可选参数 --- -#}
    {%- if item.SRRECOVERSW is not none -%}
        SRRECOVERSW={{item.SRRECOVERSW}},
    {%- endif -%}
    {%- if item.VOICEDNN is not none -%}
        VOICEDNN="{{item.VOICEDNN}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：SMFRESEL=ON 时可选 --- -#}
    {%- if item.SMFRESEL == 'ON' -%}
        {%- if item.RATE is not none -%}
            RATE={{item.RATE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SCANRATESW=ON 时可选 --- -#}
    {%- if item.SCANRATESW == 'ON' -%}
        {%- if item.INTERVAL is not none -%}
            INTERVAL={{item.INTERVAL}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SCANRATESW=ON 时可选 --- -#}
    {%- if item.SCANRATESW == 'ON' -%}
        {%- if item.SCANNUM is not none -%}
            SCANNUM={{item.SCANNUM}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SMFRESEL=ON 时可选 --- -#}
    {%- if item.SMFRESEL == 'ON' -%}
        {%- if item.SCANRATESW is not none -%}
            SCANRATESW={{item.SCANRATESW}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

