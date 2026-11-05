---
id: GWFD-010102
name: 修改Echo消息的重发数据
ne_type: UDG
type: feature
description: 在组网改变、网络调整中修改调整系统参数中Echo消息的重发时间的间隔和最大尝试发送次数。  适用于SGW-U、PGW-U、UPF。
risk_level: ''
doc_source: ["特性部署","特性指南","UDG特性指南","基本接入功能","GWFD-010102 路径管理","修改Echo消息的重发数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
在组网改变、网络调整中修改调整系统参数中Echo消息的重发时间的间隔和最大尝试发送次数。适用于SGW-U、PGW-U、UPF。

## 必备事项
前提条件

* 请仔细阅读GWFD-010102 路径管理
* 完成配置GTP/PFCP路径管理参数。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_upgtppath_list:
      type: items
      properties:
        T3RESPONSE:
          name: 'GTP请求消息的重发时间间隔'
          type: integer
          minimum: 1
          maximum: 20
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        N3REQUEST:
          name: 'GTP请求消息的最大尝试发送次数'
          type: integer
          minimum: 1
          maximum: 6
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_upn4upath_list:
      type: items
      properties:
        N4T3RESPONSE:
          name: 'N4接口的GTP请求消息的重发时间间隔'
          type: integer
          minimum: 1
          maximum: 20
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        N4N3REQUEST:
          name: 'N4接口的GTP请求消息的最大尝试发送次数'
          type: integer
          minimum: 1
          maximum: 6
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_upgtppath_list:
    - T3RESPONSE: 10
      N3REQUEST: 3
    set_upn4upath_list:
    - N4T3RESPONSE: 10
      N4N3REQUEST: 3
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 设置UDG非N4/Sxb接口的GTP请求消息的重发时间间隔和最大尝试发送次数。

```jinja2
{%- for item in set_upgtppath_list -%}
    SET UPGTPPATH:
    {#- --- 可选参数 --- -#}
    {%- if item.T3RESPONSE is not none -%}
        T3RESPONSE={{item.T3RESPONSE}},
    {%- endif -%}
    {%- if item.N3REQUEST is not none -%}
        N3REQUEST={{item.N3REQUEST}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 设置UDGN4/Sxb接口的GTP请求消息的重发时间间隔和最大尝试发送次数。

```jinja2
{%- for item in set_upn4upath_list -%}
    SET UPN4UPATH:
    {#- --- 可选参数 --- -#}
    {%- if item.N4T3RESPONSE is not none -%}
        N4T3RESPONSE={{item.N4T3RESPONSE}},
    {%- endif -%}
    {%- if item.N4N3REQUEST is not none -%}
        N4N3REQUEST={{item.N4N3REQUEST}},
    {%- endif -%}
    ;
{%- endfor -%}
```

