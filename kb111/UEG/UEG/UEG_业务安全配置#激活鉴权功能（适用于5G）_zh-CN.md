---
id: ''
name: 激活鉴权功能（适用于5G）
ne_type: UEG
type: feature
description: 对于建议强制鉴权的流程（包括初始注册、移动性INTER注册、空闲态EPS到5GS注册流程），系统默认开启鉴权功能。新建部署或运维阶段，可以执行本操作对所需流程开启强制鉴权功能，或者修改强制鉴权的流程。  适用于AMF。
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻+地市共享（连接+计算）","5GC toB 部署边缘站点（站点为“风筝M”，带计算）","配置安全数据（风筝M）","安全配置（虚机容器）","安全配置建议","必选配置","业务安全配置","激活鉴权功能（适用于5G）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
对于建议强制鉴权的流程（包括初始注册、移动性INTER注册、空闲态EPS到5GS注册流程），系统默认开启鉴权功能。新建部署或运维阶段，可以执行本操作对所需流程开启强制鉴权功能，或者修改强制鉴权的流程。适用于AMF。

## 必备事项
前提条件

请仔细阅读GWFD-021503 鉴权功能特性概述（适用于5G）。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_ngusrsecpara_list:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - IMSI_PREFIX
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        AUTHEVENT:
          name: '鉴权事件'
          type: string
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        AUTHPERIOD:
          name: '鉴权周期(h)'
          type: integer
          minimum: 0
          maximum: 24
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: 24
  examples:
    add_ngusrsecpara_list:
    - SUBRANGE: ALL_USER
      AUTHEVENT: INIT_REG-1&MOBL_INTRA_REG-0&MOBL_INTER_REG-1&PROD_REG-0&REG_AFT_INTRAHO-0&REG_AFT_INTERHO-0&IDLE_SYSCHG_REG-1&CONN_SYSCHG_REG-0&DEREGISTRATION-0&SERVICE_REQUEST-0&CONNECT_MOD-0
      AUTHPERIOD: 0
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 设置需要强制鉴权的流程。

#### 2.1 //配置所有用户在服务请求流程中需要鉴权。

```jinja2
{%- for item in add_ngusrsecpara_list -%}
    ADD NGUSRSECPARA:
    {#- --- 必选参数 --- -#}
    SUBRANGE={{item.SUBRANGE}},
    {#- --- 可选参数 --- -#}
    {%- if item.AUTHEVENT is not none -%}
        AUTHEVENT={{item.AUTHEVENT}},
    {%- endif -%}
    {%- if item.AUTHPERIOD is not none -%}
        AUTHPERIOD={{item.AUTHPERIOD}},
    {%- endif -%}
    ;
{%- endfor -%}
```

