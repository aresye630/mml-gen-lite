---
id: ''
name: 去使能容灾模式（负荷分担）
ne_type: UEG
type: feature
description: 去使能负荷分担容灾模式时（比如进行网元卸载、容灾模式改造等），需要参考本页面进行配置。  本页面中的命令均为高危命令，请在华为工程师指导下执行。否则可能导致业务受损。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","UEG容灾方案介绍（风筝L）","负荷分担容灾原理","容灾部署与调测","负荷分担容灾模式","去使能容灾模式（负荷分担）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
去使能负荷分担容灾模式时（比如进行网元卸载、容灾模式改造等），需要参考本页面进行配置。本页面中的命令均为高危命令，请在华为工程师指导下执行。否则可能导致业务受损。

## 必备事项
前提条件

园区内两套UEG已完成负荷分担容灾模式配置。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_drcouplingreset_list:
      type: items
      properties:
        COUPLINGRESET:
          name: '是否使能负荷分担容灾功能'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: '去使能负荷分担容灾模式时需要将这些参数的值设置为“NO”。'
          data_source: '固定取值'
          pattern: ''
          default: NO
    set_drkeynf_list:
      type: items
      properties:
        MME:
          name: '是否监控MME服务'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: NO
        AMF:
          name: '是否监控AMF服务'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: NO
        HSS:
          name: '是否监控HSS服务'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: NO
        UDM:
          name: '是否监控UDM服务'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: NO
        SMF:
          name: '是否监控SMF服务'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: NO
        GWC:
          name: '是否监控GW-C服务'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: NO
        PCF:
          name: '是否监控PCF服务'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: NO
        PCRF:
          name: '是否监控PCRF服务'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: NO
        UPF:
          name: '是否监控UPF服务'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: NO
        UDR:
          name: '是否监控UDR服务'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: NO
  examples:
    set_drcouplingreset_list:
    - COUPLINGRESET: NO
    set_drkeynf_list:
    - MME: NO
      AMF: NO
      HSS: NO
      UDM: NO
      SMF: NO
      GWC: NO
      PCF: NO
      PCRF: NO
      UPF: NO
      UDR: NO
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 关闭负荷分担容灾功能。

```jinja2
{%- for item in set_drcouplingreset_list -%}
    SET DRCOUPLINGRESET:
    {#- --- 可选参数 --- -#}
    {%- if item.COUPLINGRESET is not none -%}
        COUPLINGRESET={{item.COUPLINGRESET}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 将监控的服务都设置为不监控。

```jinja2
{%- for item in set_drkeynf_list -%}
    SET DRKEYNF:
    {#- --- 可选参数 --- -#}
    {%- if item.AMF is not none -%}
        AMF={{item.AMF}},
    {%- endif -%}
    {%- if item.UDM is not none -%}
        UDM={{item.UDM}},
    {%- endif -%}
    {%- if item.SMF is not none -%}
        SMF={{item.SMF}},
    {%- endif -%}
    {%- if item.UPF is not none -%}
        UPF={{item.UPF}},
    {%- endif -%}
    {%- if item.UDR is not none -%}
        UDR={{item.UDR}},
    {%- endif -%}
    {%- if item.HSS is not none -%}
        HSS={{item.HSS}},
    {%- endif -%}
    {%- if item.PCF is not none -%}
        PCF={{item.PCF}},
    {%- endif -%}
    {%- if item.MME is not none -%}
        MME={{item.MME}},
    {%- endif -%}
    {%- if item.GWC is not none -%}
        GWC={{item.GWC}},
    {%- endif -%}
    {%- if item.PCRF is not none -%}
        PCRF={{item.PCRF}},
    {%- endif -%}
    ;
{%- endfor -%}
```

