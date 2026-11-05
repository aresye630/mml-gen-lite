---
id: ''
name: 配置BGP安全
ne_type: UEG
type: feature
description: 网络上对BGP协议的攻击方法主要有DoS攻击、注入大量BGP路由、构造错误BGP协议报文、网络报文攻击，为了提升安全性，需要进行BGP的安全加固配置。
tags: []
risk_level: ''
doc_source:
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网煤矿场景，入驻式）","配置安全数据","UEG安全加固","安全配置建议","可选配置","网络安全配置","配置路由业务安全功能","配置BGP安全"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网核电场景，入驻式）","配置安全数据","UEG安全加固","安全配置建议","可选配置","网络安全配置","配置路由业务安全功能","配置BGP安全"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网通用场景，入驻式）","配置安全数据","UEG安全加固","安全配置建议","可选配置","网络安全配置","配置路由业务安全功能","配置BGP安全"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（电力专网，入驻式）","配置安全数据","核心网网元安全加固","UEG安全加固","虚机容器模式UEG安全加固","安全配置建议","可选配置","网络安全配置","配置业务路由安全功能","配置BGP安全"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（电力专网，入驻式）","配置安全数据","核心网网元安全加固","UEG安全加固","虚机容器模式UEG安全加固","安全配置建议","可选配置","网络安全配置","配置路由业务安全功能","配置BGP安全"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（电力专网，入驻式）","配置安全数据","核心网网元安全加固","UEG安全加固","裸机容器模式UEG安全加固","安全配置建议","可选配置","网络安全配置","配置业务路由安全功能","配置BGP安全"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（电力专网，入驻式）","配置安全数据","核心网网元安全加固","UEG安全加固","裸机容器模式UEG安全加固","安全配置建议","可选配置","网络安全配置","配置路由业务功能","配置BGP安全"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（火电专网，入驻式）","部署配置指导","中心园区部署入驻式UEG-L","配置安全数据（风筝L）","安全配置（虚机容器）","安全配置建议","可选配置","网络安全配置","配置路由业务安全功能","配置BGP安全"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（火电专网，入驻式）","部署配置指导","子园区部署入驻式UEG-M","配置安全数据（风筝M）","安全配置（裸机容器）","安全配置建议","可选配置","网络安全配置","配置路由业务安全功能","配置BGP安全"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（火电专网，入驻式）","部署配置指导","子园区部署入驻式UEG-S","子园区UEG-S安全加固配置","安全配置建议","可选配置","网络安全配置","配置业务路由安全功能","配置BGP安全"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（火电专网，入驻式）","部署配置指导","子园区部署入驻式UEG-S","子园区UEG-S安全加固配置","安全配置建议","可选配置","网络安全配置","配置路由业务功能","配置BGP安全"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
网络上对BGP协议的攻击方法主要有DoS攻击、注入大量BGP路由、构造错误BGP协议报文、网络报文攻击，为了提升安全性，需要进行BGP的安全加固配置。

## 必备事项
前提条件

该操作无需具备特殊条件。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    mod_bgppeer_list:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERADDR:
          name: 'IPv4对等体地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PSWDTYPE:
          name: '密码类型'
          type: string
          enum:
          - cipher
          - 'null'
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PSWDCIPHERTEXT:
          name: '密码'
          type: string
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ADDRESSTYPE:
          name: '地址类型'
          type: string
          enum:
          - ipv4
          - ipv6
          - noaf
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_bgppeer_list_1:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERADDR:
          name: 'IPv4对等体地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        KEYCHAINNAME:
          name: 'Keychain名称'
          type: string
          maxLength: 47
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ADDRESSTYPE:
          name: '地址类型'
          type: string
          enum:
          - ipv4
          - ipv6
          - noaf
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_bgppeer_list_2:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERADDR:
          name: 'IPv4对等体地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VALIDTTLHOPS:
          name: '需要检测的TTL跳数值'
          type: integer
          minimum: 1
          maximum: 256
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ADDRESSTYPE:
          name: '地址类型'
          type: string
          enum:
          - ipv4
          - ipv6
          - noaf
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_bgppeeraf_list:
      type: items
      properties:
        VRFNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AFTYPE:
          name: '地址族类型'
          type: string
          enum:
          - ipv4uni
          - ipv4vpn
          - ipv6uni
          - ipv6vpn
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REMOTEADDRESS:
          name: 'IPv4对等体地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ROUTELIMIT:
          name: '路由超限阈值'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ADDRESSTYPE:
          name: '地址类型'
          type: string
          enum:
          - ipv4
          - ipv6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    mod_bgppeer_list:
    - VRFNAME: 'VPN实例名称'
      PEERADDR: '对等体地址'
      PSWDTYPE: 密码类型
      PSWDCIPHERTEXT: '密码'
      ADDRESSTYPE: ''
    mod_bgppeer_list_1:
    - VRFNAME: 'VPN实例名称'
      PEERADDR: '对等体地址'
      KEYCHAINNAME: 'Keychain名称'
      ADDRESSTYPE: ''
    mod_bgppeer_list_2:
    - VRFNAME: 'VPN实例名称'
      PEERADDR: '对等体地址'
      VALIDTTLHOPS: 指定需要检测的TTL跳数值
      ADDRESSTYPE: ''
    mod_bgppeeraf_list:
    - VRFNAME: 'VPN实例名称'
      AFTYPE: 地址族类型
      REMOTEADDRESS: 'IPv4对等体地址'
      ROUTELIMIT: 路由超限阈值
      ADDRESSTYPE: ''
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 配置MD5认证

### BGP的MD5认证只是为TCP连接设置MD5认证密码，由TCP完成认证。如果认证失败，则不建立TCP连接。

### 在“MML命令行-VNRS\_VNFC”窗口上执行：

```jinja2
{%- for item in mod_bgppeer_list -%}
    MOD BGPPEER:
    {#- --- 必选参数 --- -#}
    VRFNAME="{{item.VRFNAME}}",
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：ADDRESSTYPE=noaf/ipv4 时必选 --- -#}
    {%- if item.ADDRESSTYPE in ['noaf', 'ipv4'] -%}
        PEERADDR="{{item.PEERADDR}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：ADDRESSTYPE=noaf/ipv4/ipv6 时可选 --- -#}
    {%- if item.ADDRESSTYPE in ['noaf', 'ipv4', 'ipv6'] -%}
        {%- if item.PSWDTYPE is not none -%}
            PSWDTYPE={{item.PSWDTYPE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：PSWDTYPE=cipher 时可选 --- -#}
    {%- if item.PSWDTYPE == 'cipher' -%}
        {%- if item.PSWDCIPHERTEXT is not none -%}
            PSWDCIPHERTEXT="{{item.PSWDCIPHERTEXT}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 为了保证更好的安全性，建议不要使用MD5算法。

### 2 配置Keychain认证

### BGP对等体两端必须都配置Keychain认证，且配置的Keychain必须使用相同的加密算法和密码，才能正常建立TCP连接，交互BGP消息。

### 在“MML命令行-VNRS\_VNFC”窗口上执行：

```jinja2
{%- for item in mod_bgppeer_list_1 -%}
    MOD BGPPEER:
    {#- --- 必选参数 --- -#}
    VRFNAME="{{item.VRFNAME}}",
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：ADDRESSTYPE=noaf/ipv4 时必选 --- -#}
    {%- if item.ADDRESSTYPE in ['noaf', 'ipv4'] -%}
        PEERADDR="{{item.PEERADDR}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：ADDRESSTYPE=noaf/ipv4/ipv6 时可选 --- -#}
    {%- if item.ADDRESSTYPE in ['noaf', 'ipv4', 'ipv6'] -%}
        {%- if item.KEYCHAINNAME is not none -%}
            KEYCHAINNAME="{{item.KEYCHAINNAME}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置BGP GTSM功能

### 配置GTSM功能，通过检测IP报文头中的TTL值是否在一个预先定义好的特定范围内来对设备进行保护。

### 在“MML命令行-VNRS\_VNFC”窗口上执行：

```jinja2
{%- for item in mod_bgppeer_list_2 -%}
    MOD BGPPEER:
    {#- --- 必选参数 --- -#}
    VRFNAME="{{item.VRFNAME}}",
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：ADDRESSTYPE=noaf/ipv4 时必选 --- -#}
    {%- if item.ADDRESSTYPE in ['noaf', 'ipv4'] -%}
        PEERADDR="{{item.PEERADDR}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：ADDRESSTYPE=noaf/ipv4/ipv6 时可选 --- -#}
    {%- if item.ADDRESSTYPE in ['noaf', 'ipv4', 'ipv6'] -%}
        {%- if item.VALIDTTLHOPS is not none -%}
            VALIDTTLHOPS={{item.VALIDTTLHOPS}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 设置BGP路由超限

### BGP使用邻居路由限定为一个BGP路由器设置允许从其对等体收到的最大路由数量，超限路由被直接丢弃。

### 在“MML命令行-VNRS\_VNFC”窗口上执行：

```jinja2
{%- for item in mod_bgppeeraf_list -%}
    MOD BGPPEERAF:
    {#- --- 必选参数 --- -#}
    VRFNAME="{{item.VRFNAME}}",
    AFTYPE={{item.AFTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：ADDRESSTYPE=ipv4 时必选 --- -#}
    {%- if item.ADDRESSTYPE == 'ipv4' -%}
        REMOTEADDRESS="{{item.REMOTEADDRESS}}",
    {#- --- 条件必选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时必选 --- -#}
    {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
        REMOTEADDRESS="{{item.REMOTEADDRESS}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：ADDRESSTYPE=ipv4/ipv6 时可选 --- -#}
    {%- if item.ADDRESSTYPE in ['ipv4', 'ipv6'] -%}
        {%- if item.ROUTELIMIT is not none -%}
            ROUTELIMIT={{item.ROUTELIMIT}},
        {%- endif -%}
    {#- --- 条件可选：AFTYPE=ipv4uni/ipv4vpn/ipv6vpn 时可选 --- -#}
    {%- elif item.AFTYPE in ['ipv4uni', 'ipv4vpn', 'ipv6vpn'] -%}
        {%- if item.ROUTELIMIT is not none -%}
            ROUTELIMIT={{item.ROUTELIMIT}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

