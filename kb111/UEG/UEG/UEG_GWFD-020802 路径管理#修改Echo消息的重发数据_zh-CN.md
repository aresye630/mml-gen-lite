---
id: GWFD-020802
name: 修改Echo消息的重发数据
ne_type: UEG
type: feature
description: 在组网改变、网络调整中修改调整系统参数中Echo消息的重发时间的间隔和最大尝试发送次数。  适用于SGW-U、PGW-U、UPF。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝S","MEC 特性指南（风筝S）","UEG特性指南","基本接入功能","GWFD-020802 路径管理","修改Echo消息的重发数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
在组网改变、网络调整中修改调整系统参数中Echo消息的重发时间的间隔和最大尝试发送次数。适用于SGW-U、PGW-U、UPF。

## 必备事项
前提条件

前提条件

* 请仔细阅读GWFD-020802 路径管理
* 完成配置GTP/PFCP路径管理参数。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
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
  examples:
    set_upgtppath_list:
    - T3RESPONSE: 10
      N3REQUEST: 3
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 设置UEGGTP请求消息的重发时间间隔和最大尝试发送次数。

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

