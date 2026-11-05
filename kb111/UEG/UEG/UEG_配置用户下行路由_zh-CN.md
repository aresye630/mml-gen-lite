---
id: ''
name: 配置用户下行路由
ne_type: UEG
type: feature
description: 为保证用户下行数据包能正常到达MPF，通过MPF访问APP服务器的UE地址段需要在网络中发布，并最终能传递到APP服务器。
tags: []
risk_level: ''
doc_source:
  - ["网络部署","园区入驻+地市共享（连接+计算）","5GC toB 部署边缘站点（站点为“风筝S”，带计算）","UEG初始配置（风筝S）","初始配置与调测（MPF）","初始配置与调测（MPF，非SDN）","参考：详细配置指导","配置MPF","配置用户下行路由"]
  - ["网络部署","园区入驻+地市共享（连接+计算）","5GC toB 部署边缘站点（站点为“风筝S”，带计算）","UEG初始配置（风筝S）","初始配置与调测（MPF）","初始配置与调测（MPF，SDN）","参考：详细配置指导","配置MPF","配置用户下行路由"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
为保证用户下行数据包能正常到达MPF，通过MPF访问APP服务器的UE地址段需要在网络中发布，并最终能传递到APP服务器。

## 必备事项
前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录MAE客户端或登录OM Portal）。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_vpninst_list:
      type: items
      properties:
        VPNINSTANCE:
          name: 'VPN实例名'
          type: string
          maxLength: 31
          required: true
          description: '与N6x外联口的VPN相同。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_mpfroute_list:
      type: items
      properties:
        MPFROUTEID:
          name: 'MPF路由标识'
          type: string
          maxLength: 31
          required: true
          description: '唯一标识一条UE地址段。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VPNINSTANCE:
          name: 'VPN实例名'
          type: string
          maxLength: 31
          required: false
          description: '索引**ADD VPNINST**命令配置的VPN实例名。  与N6x外联口的VPN相同。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IPVERSION:
          name: 'MPF地址类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        V4STARTIP:
          name: 'IPv4起始地址'
          type: string
          maxLength: 15
          required: false
          description: '必须包含与UPF上通过MPF访问APP服务器的所有UE IPv4地址。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        V4ENDIP:
          name: 'IPv4结束地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_mpfroute_list_1:
      type: items
      properties:
        MPFROUTEID:
          name: 'MPF路由标识'
          type: string
          maxLength: 31
          required: true
          description: '唯一标识一条UE地址段。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VPNINSTANCE:
          name: 'VPN实例名'
          type: string
          maxLength: 31
          required: false
          description: '索引**ADD VPNINST**命令配置的VPN实例名。  与N6x外联口的VPN相同。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IPVERSION:
          name: 'MPF地址类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        V6PREFIXSTART:
          name: 'IPv6前缀起始地址'
          type: string
          maxLength: 39
          required: false
          description: '必须包含与UPF上通过MPF访问APP服务器的所有UE IPv6地址。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        V6PREFIXEND:
          name: 'IPv6前缀结束地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
  examples:
    add_vpninst_list:
    - VPNINSTANCE: 'VRF_N6x'
    add_mpfroute_list:
    - MPFROUTEID: 'UEIPSEG_01'
      VPNINSTANCE: 'VRF_N6x'
      IPVERSION: IPV4
      V4STARTIP: '10.10.1.1'
      V4ENDIP: '10.10.1.254'
    add_mpfroute_list_1:
    - MPFROUTEID: 'UEIPSEG_02'
      VPNINSTANCE: 'VRF_N6x'
      IPVERSION: IPV6
      V6PREFIXSTART: 'FC00:1::1:1'
      V6PREFIXEND: 'FC00:1::1:254'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 配置VPN实例。

```jinja2
{%- for item in add_vpninst_list -%}
    ADD VPNINST:
    {#- --- 必选参数 --- -#}
    VPNINSTANCE="{{item.VPNINSTANCE}}",
    ;
{%- endfor -%}
```

### 3 配置UE地址段。

#### 3.1 //配置UE IPv4地址段。

```jinja2
{%- if is_scenario_ipv4 -%}
    {%- for item in add_mpfroute_list -%}
        ADD MPFROUTE:
        {#- --- 必选参数 --- -#}
        MPFROUTEID="{{item.MPFROUTEID}}",
        IPVERSION={{item.IPVERSION}},
        {#- --- 可选参数 --- -#}
        {%- if item.VPNINSTANCE is not none -%}
            VPNINSTANCE="{{item.VPNINSTANCE}}",
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
        {%- if item.IPVERSION == 'IPV4' -%}
            V4STARTIP="{{item.V4STARTIP}}",
        {%- endif -%}
        {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
        {%- if item.IPVERSION == 'IPV4' -%}
            V4ENDIP="{{item.V4ENDIP}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.2 //配置UE IPv6地址段。

```jinja2
{%- if is_scenario_ipv6 -%}
    {%- for item in add_mpfroute_list_1 -%}
        ADD MPFROUTE:
        {#- --- 必选参数 --- -#}
        MPFROUTEID="{{item.MPFROUTEID}}",
        IPVERSION={{item.IPVERSION}},
        {#- --- 可选参数 --- -#}
        {%- if item.VPNINSTANCE is not none -%}
            VPNINSTANCE="{{item.VPNINSTANCE}}",
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IPVERSION=IPV6 时必选 --- -#}
        {%- if item.IPVERSION == 'IPV6' -%}
            V6PREFIXSTART="{{item.V6PREFIXSTART}}",
        {%- endif -%}
        {#- --- 条件必选：IPVERSION=IPV6 时必选 --- -#}
        {%- if item.IPVERSION == 'IPV6' -%}
            V6PREFIXEND="{{item.V6PREFIXEND}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

