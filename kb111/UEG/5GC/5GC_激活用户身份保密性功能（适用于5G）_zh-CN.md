---
id: ''
name: 激活用户身份保密性功能（适用于5G）
ne_type: UEG
type: feature
description: 新建部署后配置GUTI重分配策略和定时器，或运维阶段需要修改GUTI重分配策略和定时器时，执行本操作。  适用于AMF。
tags: []
risk_level: ''
doc_source:
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网煤矿场景，入驻式）","配置安全数据","UEG安全加固","安全配置建议","必选配置","业务安全配置","激活用户身份保密性功能（适用于5G）"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网核电场景，入驻式）","配置安全数据","UEG安全加固","安全配置建议","必选配置","业务安全配置","激活用户身份保密性功能（适用于5G）"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网通用场景，入驻式）","配置安全数据","UEG安全加固","安全配置建议","必选配置","业务安全配置","激活用户身份保密性功能（适用于5G）"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（火电专网，入驻式）","部署配置指导","中心园区部署入驻式UEG-L","配置安全数据（风筝L）","安全配置（虚机容器）","安全配置建议","必选配置","业务安全配置","激活用户身份保密性功能（适用于5G）"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（火电专网，入驻式）","部署配置指导","子园区部署入驻式UEG-M","配置安全数据（风筝M）","安全配置（裸机容器）","安全配置建议","必选配置","业务安全配置","激活用户身份保密性功能（适用于5G）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
新建部署后配置GUTI重分配策略和定时器，或运维阶段需要修改GUTI重分配策略和定时器时，执行本操作。适用于AMF。

## 必备事项
前提条件

请仔细阅读GWFD-021504 用户身份保密性功能特性概述（适用于5G）。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_ngmmpara_list:
      type: items
      properties:
        GUTIREALLOC:
          name: 'GUTI重分配'
          type: string
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        GUTITMR:
          name: 'GUTI重分配定时器（h）'
          type: integer
          minimum: 0
          maximum: 24
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        GUTIREALLOCTMR:
          name: 'GUTI重分配最大间隔（h）'
          type: integer
          minimum: 0
          maximum: 24
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
  examples:
    set_ngmmpara_list:
    - GUTIREALLOC: INIT_REG-1&MOBIL_REG-1
      GUTITMR: 1
      GUTIREALLOCTMR: 1
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 配置GUTI重分配策略和定时器。

```jinja2
{%- for item in set_ngmmpara_list -%}
    SET NGMMPARA:
    {#- --- 可选参数 --- -#}
    {%- if item.GUTIREALLOC is not none -%}
        GUTIREALLOC={{item.GUTIREALLOC}},
    {%- endif -%}
    {%- if item.GUTITMR is not none -%}
        GUTITMR={{item.GUTITMR}},
    {%- endif -%}
    {%- if item.GUTIREALLOCTMR is not none -%}
        GUTIREALLOCTMR={{item.GUTIREALLOCTMR}},
    {%- endif -%}
    ;
{%- endfor -%}
```

