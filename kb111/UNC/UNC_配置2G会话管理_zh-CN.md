---
id: ''
name: 配置2G会话管理
ne_type: UNC
type: feature
description: 本操作指导介绍在运行网络中配置会话管理特性的操作过程。  2G会话管理是MS获取网络服务的前提。在3G没有完全替代2G时，每台SGSN均需要配置2G会话管理功能。
risk_level: ''
doc_source: ["网络部署","初始配置","UNC初始配置与调测","组网对接配置","配置AMF&MME&SGSN","配置SGSN","配置会话管理","配置2G会话管理"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中配置会话管理特性的操作过程。2G会话管理是MS获取网络服务的前提。在3G没有完全替代2G时，每台SGSN均需要配置2G会话管理功能。

## 必备事项
前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020客户端或登录OM Portal）。

* UNC软件安装已完成。
* 已经完成HPLMN配置。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_gbsm_list:
      type: items
      properties:
        T3385:
          name: 'T3385（s）'
          type: integer
          minimum: 1
          maximum: 86400
          required: false
          description: '设置2G SM协议配置表信息。'
          data_source: '参见“水平网设LLD文档 ”。'
          pattern: ''
          default: ''
        N3385:
          name: 'N3385（times）'
          type: integer
          minimum: 0
          maximum: 5
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        T3386:
          name: 'T3386（s）'
          type: integer
          minimum: 1
          maximum: 86400
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        N3386:
          name: 'N3386（times）'
          type: integer
          minimum: 0
          maximum: 5
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        T3395:
          name: 'T3395（s）'
          type: integer
          minimum: 1
          maximum: 86400
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        N3395:
          name: 'N3395（times）'
          type: integer
          minimum: 0
          maximum: 5
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PFT_USED:
          name: '是否启用PFT'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SM_BSS_PFT_T9:
          name: 'BSS保留PFC的时长定时器（s）'
          type: integer
          minimum: 6
          maximum: 11160
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_gbsm_list:
    - T3385: 8
      N3385: 4
      T3386: 8
      N3386: 4
      T3395: 8
      N3395: 4
      PFT_USED: YES
      SM_BSS_PFT_T9: 40
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 设置2G SM协议配置表信息。

```jinja2
{%- for item in set_gbsm_list -%}
    SET GBSM:
    {#- --- 可选参数 --- -#}
    {%- if item.T3385 is not none -%}
        T3385={{item.T3385}},
    {%- endif -%}
    {%- if item.N3385 is not none -%}
        N3385={{item.N3385}},
    {%- endif -%}
    {%- if item.T3386 is not none -%}
        T3386={{item.T3386}},
    {%- endif -%}
    {%- if item.N3386 is not none -%}
        N3386={{item.N3386}},
    {%- endif -%}
    {%- if item.T3395 is not none -%}
        T3395={{item.T3395}},
    {%- endif -%}
    {%- if item.N3395 is not none -%}
        N3395={{item.N3395}},
    {%- endif -%}
    {%- if item.PFT_USED is not none -%}
        PFT_USED={{item.PFT_USED}},
    {%- endif -%}
    {%- if item.SM_BSS_PFT_T9 is not none -%}
        SM_BSS_PFT_T9={{item.SM_BSS_PFT_T9}},
    {%- endif -%}
    ;
{%- endfor -%}
```

