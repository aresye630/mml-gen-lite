---
id: ''
name: 激活接入控制
ne_type: UEG
type: feature
description: 当在线用户已用带宽过大，超出协商的最大带宽时，设置带宽接入的控制方式。  适用于SGW-U、PGW-U。
tags: []
risk_level: ''
doc_source:
  - ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝S”，入驻式）","虚机容器模式","配置安全数据（风筝S）","安全配置建议","可选配置","业务安全配置","激活接入控制"]
  - ["网络部署","地市共享式（仅连接）","5GC toB 部署边缘站点（站点为“风筝S”，共享式）","配置安全数据（风筝S）","安全配置建议","可选配置","业务安全配置","激活接入控制"]
  - ["网络部署","园区入驻+地市共享（连接+计算）","5GC toB 部署边缘站点（站点为“风筝S”，带计算）","配置安全数据（风筝S）","配置UEG安全数据","UPF安全数据","安全配置建议","可选配置","业务安全配置","激活接入控制"]
  - ["网络部署","园区入驻+地市共享（连接+计算）","5GC toB 部署边缘站点（站点为“风筝S”，带计算）","配置安全数据（风筝S）","配置UEG安全数据","MPF安全数据","安全配置建议","可选配置","业务安全配置","激活接入控制"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
当在线用户已用带宽过大，超出协商的最大带宽时，设置带宽接入的控制方式。适用于SGW-U、PGW-U。

## 必备事项
前提条件

请仔细阅读GWFD-020901 接入控制。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_apn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_apnqosattr_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CARSHAPEUL:
          name: '上行CAR/SHAPE开关'
          type: string
          enum:
          - CAR
          - SHAPE
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CARSHAPEDL:
          name: '下行CAR/SHAPE开关'
          type: string
          enum:
          - CAR
          - SHAPE
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CARSHAPESWDL:
          name: '下行Qos开关'
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
        CARSHAPESWUL:
          name: '上行Qos开关'
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
  examples:
    add_apn_list:
    - APN: 'apn'
    set_apnqosattr_list:
    - APN: 'apn'
      CARSHAPEUL: CAR
      CARSHAPEDL: CAR
      CARSHAPESWDL: ''
      CARSHAPESWUL: ''
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 增加APN实例。

```jinja2
{%- for item in add_apn_list -%}
    ADD APN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    ;
{%- endfor -%}
```

### 2 将带宽控制方式绑定到APN用例下。

```jinja2
{%- for item in set_apnqosattr_list -%}
    SET APNQOSATTR:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：CARSHAPESWUL=ENABLE 时必选 --- -#}
    {%- if item.CARSHAPESWUL == 'ENABLE' -%}
        CARSHAPEUL={{item.CARSHAPEUL}},
    {%- endif -%}
    {#- --- 条件必选：CARSHAPESWDL=ENABLE 时必选 --- -#}
    {%- if item.CARSHAPESWDL == 'ENABLE' -%}
        CARSHAPEDL={{item.CARSHAPEDL}},
    {%- endif -%}
    ;
{%- endfor -%}
```

