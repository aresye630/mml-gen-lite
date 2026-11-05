---
id: ''
name: 激活NAS信令加密与完整性保护（适用于5G）
ne_type: UEG
type: feature
description: 新建部署后配置指定用户支持的保护算法以及算法优先级，或运维阶段需要修改保护算法及优先级时，执行本操作。  适用于AMF。
tags: []
risk_level: ''
doc_source:
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网煤矿场景，入驻式）","配置安全数据","UEG安全加固","安全配置建议","必选配置","业务安全配置","激活NAS信令加密与完整性保护（适用于5G）"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网核电场景，入驻式）","配置安全数据","UEG安全加固","安全配置建议","必选配置","业务安全配置","激活NAS信令加密与完整性保护（适用于5G）"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网通用场景，入驻式）","配置安全数据","UEG安全加固","安全配置建议","必选配置","业务安全配置","激活NAS信令加密与完整性保护（适用于5G）"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（火电专网，入驻式）","部署配置指导","中心园区部署入驻式UEG-L","配置安全数据（风筝L）","安全配置（虚机容器）","安全配置建议","必选配置","业务安全配置","激活NAS信令加密与完整性保护（适用于5G）"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（火电专网，入驻式）","部署配置指导","子园区部署入驻式UEG-M","配置安全数据（风筝M）","安全配置（裸机容器）","安全配置建议","必选配置","业务安全配置","激活NAS信令加密与完整性保护（适用于5G）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
新建部署后配置指定用户支持的保护算法以及算法优先级，或运维阶段需要修改保护算法及优先级时，执行本操作。适用于AMF。

## 必备事项
前提条件

请仔细阅读GWFD-021505 NAS信令加密与完整性保护特性概述（适用于5G）。
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
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        INTEGALG:
          name: '完整性算法'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ENCRYALG:
          name: '加密算法'
          type: string
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_ngalgpriority_list:
      type: items
      properties:
        ALGTYPE:
          name: '算法类型'
          type: string
          enum:
          - CIPH
          - INTE
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ALGINTE:
          name: '完整性算法'
          type: string
          enum:
          - NIA1
          - NIA2
          - NIA3
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ALGPRI:
          name: '算法优先级'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_ngalgpriority_list_2:
      type: items
      properties:
        ALGTYPE:
          name: '算法类型'
          type: string
          enum:
          - CIPH
          - INTE
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ALGCIPH:
          name: '加密算法'
          type: string
          enum:
          - NEA0
          - NEA1
          - NEA2
          - NEA3
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ALGPRI:
          name: '算法优先级'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
  examples:
    add_ngusrsecpara_list:
    - SUBRANGE: ALL_USER
      INTEGALG: NIA1-1&NIA2-1&NIA3-1
      ENCRYALG: NEA0-1&NEA1-1&NEA2-1&NEA3-1
    add_ngalgpriority_list:
    - ALGTYPE: INTE
      ALGINTE: NIA1
      ALGPRI: 0
    add_ngalgpriority_list_2:
    - ALGTYPE: CIPH
      ALGCIPH: NEA1
      ALGPRI: 0
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 配置指定用户支持的保护算法。

#### 2.1 //配置所有用户支持所有保护算法

```jinja2
{%- for item in add_ngusrsecpara_list -%}
    ADD NGUSRSECPARA:
    {#- --- 必选参数 --- -#}
    SUBRANGE={{item.SUBRANGE}},
    {#- --- 可选参数 --- -#}
    {%- if item.INTEGALG is not none -%}
        INTEGALG={{item.INTEGALG}},
    {%- endif -%}
    {%- if item.ENCRYALG is not none -%}
        ENCRYALG={{item.ENCRYALG}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置算法优先级。

#### 3.1 //在完整性算法中指定NIA1(SNOW 3G完整性算法)的优先级为0、NIA2(AES完整性算法)的优先级为1

```jinja2
{%- for item in add_ngalgpriority_list -%}
    ADD NGALGPRIORITY:
    {#- --- 必选参数 --- -#}
    ALGTYPE={{item.ALGTYPE}},
    ALGPRI={{item.ALGPRI}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：ALGTYPE=INTE 时必选 --- -#}
    {%- if item.ALGTYPE == 'INTE' -%}
        ALGINTE={{item.ALGINTE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 3.2 //在加密算法中指定NEA1(SNOW 3G加密算法)的优先级为0、NEA2(AES加密算法)的优先级为1

```jinja2
{%- for item in add_ngalgpriority_list_2 -%}
    ADD NGALGPRIORITY:
    {#- --- 必选参数 --- -#}
    ALGTYPE={{item.ALGTYPE}},
    ALGPRI={{item.ALGPRI}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：ALGTYPE=CIPH 时必选 --- -#}
    {%- if item.ALGTYPE == 'CIPH' -%}
        ALGCIPH={{item.ALGCIPH}},
    {%- endif -%}
    ;
{%- endfor -%}
```

