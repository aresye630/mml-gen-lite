---
id: GWFD-020254
name: 配置VoLTE业务快速恢复
ne_type: UDG
type: feature
description: 在UDG上激活VoLTE业务快速恢复功能，让UE快速附着PS网络，降低网元故障对语音业务的影响。  适用于SGW-U、PGW-U。
risk_level: ''
doc_source: ["特性部署","特性指南","UDG特性指南","语音功能","GWFD-020254 VoLTE业务快速恢复","配置VoLTE业务快速恢复"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
在UDG上激活VoLTE业务快速恢复功能，让UE快速附着PS网络，降低网元故障对语音业务的影响。适用于SGW-U、PGW-U。

## 必备事项
前提条件

请仔细阅读GWFD-020254 VoLTE业务快速恢复。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_fastrecovery_list:
      type: items
      properties:
        RESTORPGWSWITCH:
          name: '故障重启业务恢复功能PGW开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: 'PGW打开网络侧触发的业务恢复功能。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PDTNSWITCH:
          name: 'PDTN功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: 'SGW-C故障重启场景下，开启PGW-U触发SGW-C业务恢复功能。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        RESTORSGWSWITCH:
          name: '故障重启业务恢复功能SGW开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: 'SGW打开网络侧触发的业务恢复功能。'
          data_source: '全网规划'
          pattern: ''
          default: ''
  examples:
    set_fastrecovery_list:
    - RESTORPGWSWITCH: ENABLE
      PDTNSWITCH: ENABLE
      RESTORSGWSWITCH: ENABLE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 设置VoLTE业务快速恢复功能。

```jinja2
{%- for item in set_fastrecovery_list -%}
    SET FASTRECOVERY:
    {#- --- 可选参数 --- -#}
    {%- if item.RESTORPGWSWITCH is not none -%}
        RESTORPGWSWITCH={{item.RESTORPGWSWITCH}},
    {%- endif -%}
    {%- if item.RESTORSGWSWITCH is not none -%}
        RESTORSGWSWITCH={{item.RESTORSGWSWITCH}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：RESTORPGWSWITCH=ENABLE 时可选 --- -#}
    {%- if item.RESTORPGWSWITCH == 'ENABLE' -%}
        {%- if item.PDTNSWITCH is not none -%}
            PDTNSWITCH={{item.PDTNSWITCH}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

