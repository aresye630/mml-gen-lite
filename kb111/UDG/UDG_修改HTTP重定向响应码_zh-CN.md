---
id: GWFD-110281
name: 修改HTTP重定向响应码
ne_type: UDG
type: feature
description: 当用户的http协议的报文需要被重定向时，UDG向用户发送重定向响应报文，报文中的重定向响应码标识了重定向的类型。  适用于PGW-U、UPF。
risk_level: ''
doc_source: ["特性部署","特性指南","UDG特性指南","智能策略控制功能","GWFD-110281 用户Portal","调整用户Portal参数","修改HTTP重定向响应码"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当用户的http协议的报文需要被重定向时，UDG向用户发送重定向响应报文，报文中的重定向响应码标识了重定向的类型。适用于PGW-U、UPF。

## 必备事项
前提条件

该操作无需具备特殊条件。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_srvcommonpara_list:
      type: items
      properties:
        HTTPREDIRCODE:
          name: 'HTTP重定向返回码'
          type: string
          enum:
          - RSP_CODE_200
          - RSP_CODE_301
          - RSP_CODE_302
          - RSP_CODE_303
          - RSP_CODE_307
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_srvcommonpara_list:
    - HTTPREDIRCODE: RSP_CODE_302
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 基于全局配置HTTP协议的GET请求回应的重定向响应码。

```jinja2
{%- for item in set_srvcommonpara_list -%}
    SET SRVCOMMONPARA:
    {#- --- 可选参数 --- -#}
    {%- if item.HTTPREDIRCODE is not none -%}
        HTTPREDIRCODE={{item.HTTPREDIRCODE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

