---
id: ''
name: 配置上报APN属性（有语音业务+相同DNN/APN）
ne_type: UEG
type: feature
description: 当总部园区和各子园区采用相同语音DNN/APN和数据DNN/APN业务接入时，如果总部园区UPF/GW-U向周边网元发送信息携带用户签约DNN/APN，则需要执行本章节配置；如果向周边网元发送信息携带真实DNN/APN，则无需执行本操作。
tags: []
risk_level: ''
doc_source: ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（风筝多园区，入驻式）","风筝L+S多园区方案（非跨级容灾）","方案配置","在UEG-L配置与UEG-S对接（UEG-L虚机）","子园区UPF主备冷备容灾","配置UPF/GW-U数据","配置上报APN属性（有语音业务+相同DNN/APN）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
当总部园区和各子园区采用相同语音DNN/APN和数据DNN/APN业务接入时，如果总部园区UPF/GW-U向周边网元发送信息携带用户签约DNN/APN，则需要执行本章节配置；如果向周边网元发送信息携带真实DNN/APN，则无需执行本操作。

## 必备事项
前提条件

无。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_apnreportattr_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '映射后真实DNN/APN名称。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        HEADERENRICH:
          name: '上报给头增强的APN名'
          type: string
          enum:
          - REQUESTED
          - SERVICE
          required: false
          description: 'UPF/GW-U向周边网元发送信息使用映射前DNN/APN。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PERFORMANCE:
          name: '上报给话统的APN名'
          type: string
          enum:
          - REQUESTED
          - SERVICE
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SERVICEREPORT:
          name: '业务报表使用的APN名'
          type: string
          enum:
          - REQUESTED
          - SERVICE
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
  examples:
    set_apnreportattr_list:
    - APN: 'Real.data.APN1'
      HEADERENRICH: REQUESTED
      PERFORMANCE: REQUESTED
      SERVICEREPORT: REQUESTED
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 配置上报APN属性。

```jinja2
{%- for item in set_apnreportattr_list -%}
    SET APNREPORTATTR:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.HEADERENRICH is not none -%}
        HEADERENRICH={{item.HEADERENRICH}},
    {%- endif -%}
    {%- if item.PERFORMANCE is not none -%}
        PERFORMANCE={{item.PERFORMANCE}},
    {%- endif -%}
    {%- if item.SERVICEREPORT is not none -%}
        SERVICEREPORT={{item.SERVICEREPORT}},
    {%- endif -%}
    ;
{%- endfor -%}
```

