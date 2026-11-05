---
id: ''
name: 配置CP白名单功能
ne_type: UEG
type: feature
description: 当前一个UPF最多与64个SMF建立偶联，为防止仿冒的SMF向N4接口发送PFCP消息，恶意消耗偶联资源或干扰已经建立的偶联工作，建议开启CP白名单功能，只允许白名单范围内的SMF与UPF建立偶联。  适用于SGW-U、PGW-U、UPF。
tags: []
risk_level: ''
doc_source:
  - ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝S”，入驻式）","虚机容器模式","配置安全数据（风筝S）","安全配置建议","可选配置","业务安全配置","配置CP白名单功能"]
  - ["网络部署","地市共享式（仅连接）","5GC toB 部署边缘站点（站点为“风筝S”，共享式）","配置安全数据（风筝S）","安全配置建议","可选配置","业务安全配置","配置CP白名单功能"]
  - ["网络部署","园区入驻+地市共享（连接+计算）","5GC toB 部署边缘站点（站点为“风筝S”，带计算）","配置安全数据（风筝S）","配置UEG安全数据","UPF安全数据","安全配置建议","可选配置","业务安全配置","配置CP白名单功能"]
  - ["网络部署","园区入驻+地市共享（连接+计算）","5GC toB 部署边缘站点（站点为“风筝S”，带计算）","配置安全数据（风筝S）","配置UEG安全数据","MPF安全数据","安全配置建议","可选配置","业务安全配置","配置CP白名单功能"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
当前一个UPF最多与64个SMF建立偶联，为防止仿冒的SMF向N4接口发送PFCP消息，恶意消耗偶联资源或干扰已经建立的偶联工作，建议开启CP白名单功能，只允许白名单范围内的SMF与UPF建立偶联。适用于SGW-U、PGW-U、UPF。

## 必备事项
前提条件

前提条件

无。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_cpaccesslistfunc_list:
      type: items
      properties:
        SWITCH:
          name: '开关标识'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_cpaccesslist_list:
      type: items
      properties:
        WHITELISTTYPE:
          name: '白名单参数类型'
          type: string
          enum:
          - IP
          - NODEID
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP地址版本类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CPNODEIDTYPE:
          name: 'CP Node ID类型'
          type: string
          enum:
          - FQDN
          - IPv4
          - IPv6
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        CPIPV4:
          name: 'CP IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CPIPV6:
          name: 'CP IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CPIPV4MASK:
          name: 'CP IPv4掩码长度'
          type: integer
          minimum: 1
          maximum: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CPIPV6MASK:
          name: 'CP IPv6掩码长度'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CPNODEIDIPV4:
          name: 'CP Node ID中的IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CPNODEIDIPV6:
          name: 'CP Node ID中的IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CPNODEIDFQDN:
          name: 'CP Node ID的FQDN'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
  examples:
    set_cpaccesslistfunc_list:
    - SWITCH: ENABLE
    add_cpaccesslist_list:
    - WHITELISTTYPE: NODEID
      IPVERSION: IP地址版本类型
      CPNODEIDTYPE: FQDN
      CPIPV4: 'CP IPv4地址'
      CPIPV6: 'CP IPv6地址'
      CPIPV4MASK: CP IPv4掩码长度
      CPIPV6MASK: CP IPv6掩码长度
      CPNODEIDIPV4: 'CP Node ID中的IPv4地址'
      CPNODEIDIPV6: 'CP Node ID中的IPv6地址'
      CPNODEIDFQDN: 'smf1'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 使能CP白名单开关。

```jinja2
{%- for item in set_cpaccesslistfunc_list -%}
    SET CPACCESSLISTFUNC:
    {#- --- 必选参数 --- -#}
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 2 配置CP白名单。

```jinja2
{%- for item in add_cpaccesslist_list -%}
    ADD CPACCESSLIST:
    {#- --- 必选参数 --- -#}
    WHITELISTTYPE={{item.WHITELISTTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：WHITELISTTYPE=IP 时必选 --- -#}
    {%- if item.WHITELISTTYPE == 'IP' -%}
        IPVERSION={{item.IPVERSION}},
    {%- endif -%}
    {#- --- 条件必选：WHITELISTTYPE=NODEID 时必选 --- -#}
    {%- if item.WHITELISTTYPE == 'NODEID' -%}
        CPNODEIDTYPE={{item.CPNODEIDTYPE}},
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV4' -%}
        CPIPV4="{{item.CPIPV4}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV6' -%}
        CPIPV6="{{item.CPIPV6}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV4' -%}
        CPIPV4MASK={{item.CPIPV4MASK}},
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV6' -%}
        CPIPV6MASK={{item.CPIPV6MASK}},
    {%- endif -%}
    {#- --- 条件必选：CPNODEIDTYPE=IPv4 时必选 --- -#}
    {%- if item.CPNODEIDTYPE == 'IPv4' -%}
        CPNODEIDIPV4="{{item.CPNODEIDIPV4}}",
    {%- endif -%}
    {#- --- 条件必选：CPNODEIDTYPE=IPv6 时必选 --- -#}
    {%- if item.CPNODEIDTYPE == 'IPv6' -%}
        CPNODEIDIPV6="{{item.CPNODEIDIPV6}}",
    {%- endif -%}
    {#- --- 条件必选：CPNODEIDTYPE=FQDN 时必选 --- -#}
    {%- if item.CPNODEIDTYPE == 'FQDN' -%}
        CPNODEIDFQDN="{{item.CPNODEIDFQDN}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

