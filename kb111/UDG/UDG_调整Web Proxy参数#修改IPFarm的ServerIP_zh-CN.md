---
id: GWFD-110282
name: 修改IPFarm的ServerIP
ne_type: UDG
type: feature
description: IPFarm的ServerIP不允许被修改，配置不同的IP会新增一个ServerIP。如果需要修改ServerIP，可以先删除原来的ServerIP，再配置一个新的ServerIP。  适用于PGW-U、UPF。
risk_level: ''
doc_source: ["特性部署","特性指南","UDG特性指南","智能策略控制功能","GWFD-110282 Web Proxy","调整Web Proxy参数","修改IPFarm的ServerIP"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
IPFarm的ServerIP不允许被修改，配置不同的IP会新增一个ServerIP。如果需要修改ServerIP，可以先删除原来的ServerIP，再配置一个新的ServerIP。适用于PGW-U、UPF。

## 必备事项
前提条件

* 请仔细阅读GWFD-110282 Web Proxy。
* 完成配置Web Proxy。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    rmv_ipfarmserver_list:
      type: items
      properties:
        IPFARMNAME:
          name: 'IP-Farm名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '配置的IPFarm名称，已通过**ADD IPFARM**命令配置完成，可以使用**LST IPFARM**命令进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP协议版本'
          type: string
          enum:
          - IPV4
          - IPV6
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SERVERIPV4:
          name: '服务器IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SERVERIPV6:
          name: '服务器IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ipfarmserver_list:
      type: items
      properties:
        IPFARMNAME:
          name: 'IP-Farm名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '配置的IPFarm名称，已通过**ADD IPFARM**命令配置完成，可以使用**LST IPFARM**命令进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP协议版本'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SERVERIPV4:
          name: '服务器IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SERVERIPV6:
          name: '服务器IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    rmv_ipfarmserver_list:
    - IPFARMNAME: 'farm_test'
      IPVERSION: IPV4
      SERVERIPV4: '10.10.253.251'
      SERVERIPV6: ''
    add_ipfarmserver_list:
    - IPFARMNAME: 'farm_test'
      IPVERSION: IPV4
      SERVERIPV4: '10.10.253.252'
      SERVERIPV6: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 删除原来的类型为IPv4的ServerIP。

```jinja2
{%- for item in rmv_ipfarmserver_list -%}
    RMV IPFARMSERVER:
    {#- --- 必选参数 --- -#}
    IPFARMNAME="{{item.IPFARMNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.IPVERSION is not none -%}
        IPVERSION={{item.IPVERSION}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV4' -%}
        SERVERIPV4="{{item.SERVERIPV4}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV6' -%}
        SERVERIPV6="{{item.SERVERIPV6}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 新增IPFarm的类型为IPv4的ServerIP。

```jinja2
{%- for item in add_ipfarmserver_list -%}
    ADD IPFARMSERVER:
    {#- --- 必选参数 --- -#}
    IPFARMNAME="{{item.IPFARMNAME}}",
    IPVERSION={{item.IPVERSION}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV4' -%}
        SERVERIPV4="{{item.SERVERIPV4}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV6' -%}
        SERVERIPV6="{{item.SERVERIPV6}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

