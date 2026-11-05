---
id: ''
name: 配置UPF数据
ne_type: UEG
type: feature
description: UPF与MPF对接时，需要配置Nxuc接口与MPF通过VXLAN（VXLAN-GPE）隧道互通。容灾场景下，两个MPF之间是负荷分担关系。容灾组网图如图1所示。  **图1** MPF容灾组网图
tags: []
risk_level: ''
doc_source: ["云网（连接+计算，入驻式或共享式）","业务发放","5GC toB 裸金属发放（云网，带计算）","通过MEAO发放（基于云管）","发放前准备","配置UPF/MPF与裸金属服务器的路由","主锚点UPF与MPF不共VNF（UE流量过MPF）","配置UPF数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
UPF与MPF对接时，需要配置Nxuc接口与MPF通过VXLAN（VXLAN-GPE）隧道互通。容灾场景下，两个MPF之间是负荷分担关系。容灾组网图如图1所示。**图1** MPF容灾组网图

## 必备事项
前提条件

* 此场景的配置是在UPF初始配置之后，增加的容灾相关配置，因此，需确保UPF、MPF均已完成初始配置。
* 两个MEC之间的路由互通配置已完成。
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
          minLength: 0
          maxLength: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_logicinf_list:
      type: items
      properties:
        NAME:
          name: '逻辑接口名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '一个VNF上最多可以配置31个Nxuc接口，最后一个数字取值范围是0～31。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPVERSION:
          name: '逻辑接口的IP版本'
          type: string
          enum:
          - IPV4
          - IPV6
          - IPVER_ALL
          required: true
          description: '如果规划逻辑接口使用IPv4v6双栈组网，则该参数取值为“IPVER\_ALL”，分别配置IPv4和IPv6地址。  UPF对接多个MPF时，可以复用此逻辑接口，无需配置多个。'
          data_source: '-'
          pattern: ''
          default: ''
        IPV4ADDRESS1:
          name: '逻辑接口的IPv4地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4MASK1:
          name: '逻辑接口的IPv4掩码1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        VPNINSTANCE:
          name: 'VPN实例名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '-'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_vxlangrp_list:
      type: items
      properties:
        GRPNAME:
          name: 'Vxlan隧道组名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: 'Vxlan链路组名称，网元内不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SRCINTF:
          name: '隧道源接口'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: 'UPF与MPF互通场景，此处使用的是UPF上Nxuc接口。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        HEARTBEAT:
          name: '健康检查标记'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '使能心跳检查功能。'
          data_source: '本端规划'
          pattern: ''
          default: ENABLE
        TIMETHRESHOLD:
          name: '时间阈值（秒）'
          type: integer
          minimum: 3
          maximum: 60
          required: false
          description: '两次心跳检测间的时间阈值。'
          data_source: '本端规划'
          pattern: ''
          default: 6
        HEARTSUCCLIMIT:
          name: '心跳检查成功次数'
          type: integer
          minimum: 1
          maximum: 10
          required: false
          description: '设置隧道状态为up所需的心跳检测连续成功次数。'
          data_source: '本端规划'
          pattern: ''
          default: 3
        HEARTFAILLIMIT:
          name: '心跳检查失败次数'
          type: integer
          minimum: 1
          maximum: 10
          required: false
          description: '设置隧道状态为down所需的心跳检测连续失败次数。'
          data_source: '本端规划'
          pattern: ''
          default: 3
        TIMEOUT:
          name: 'Ping探测超时时长（秒）'
          type: integer
          minimum: 1
          maximum: 59
          required: false
          description: '设置心跳检测的超时时长，该值需要小于TimeThreshold。'
          data_source: '本端规划'
          pattern: ''
          default: 2
    add_vtep_list:
      type: items
      properties:
        VTEPNAME:
          name: 'Vxlan隧道端点名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '设置UPF到MPF1和MPF2的Vxlan隧道名称，网元内不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP协议版本'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: 'UPF与MPF1和MPF2互通场景，此处使用的是MPF上Nxua逻辑接口的IP地址。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        VTEPIPV4:
          name: '隧道端点的IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
    add_vtepbindgrp_list:
      type: items
      properties:
        VXLANGRPNAME:
          name: 'Vxlan组名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: 'VTEP绑定Vxlan隧道组，并指定隧道主备类型。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VTEPNAME:
          name: 'VTEP名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PRIFLAG:
          name: '主备用类型'
          type: string
          enum:
          - PRIMARY
          - SECONDARY
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: PRIMARY
    add_vxlanbindapn_list:
      type: items
      properties:
        APN:
          name: 'APN'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '基于APN绑定一个链路组。UPF和MPF互通场景，链路组对端地址配置为MPF的Nxua接口地址，将命中Rule的报文发送到MPF的Nxua接口。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        VXLANGRPNAME:
          name: 'Vxlan组名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_vpnvnimap_list:
      type: items
      properties:
        VPNINSTANCE:
          name: 'VPN实例'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '与APN绑定的VPN实例相同。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        RULESWITCH:
          name: 'Rule开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: '此处以基于用户VPN映射到VNI为例。'
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
        VNI:
          name: 'VNI'
          type: integer
          minimum: 0
          maximum: 16777215
          required: true
          description: '配置VxLan隧道标识。  Vxlan隧道当前不支持配置隧道端口号，端口号统一固定使用默认端口号4790。'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    add_vpninst_list:
    - VPNINSTANCE: 'VPN_Nx'
    add_logicinf_list:
    - NAME: 'Nxucif1/1/0'
      IPVERSION: IPV4
      IPV4ADDRESS1: '10.1.8.1'
      IPV4MASK1: '255.255.255.255'
      VPNINSTANCE: 'VPN_Nx'
    add_vxlangrp_list:
    - GRPNAME: 'vxlan_grp01'
      SRCINTF: 'Nxucif1/1/0'
      HEARTBEAT: ENABLE
      TIMETHRESHOLD: 6
      HEARTSUCCLIMIT: 3
      HEARTFAILLIMIT: 3
      TIMEOUT: 2
    add_vtep_list:
    - VTEPNAME: 'VTEP1'
      IPVERSION: IPV4
      VTEPIPV4: '10.10.100.1'
    add_vtepbindgrp_list:
    - VXLANGRPNAME: 'vxlan_grp01'
      VTEPNAME: 'VTEP1'
      PRIFLAG: PRIMARY
    add_vxlanbindapn_list:
    - APN: 'apn1'
      VXLANGRPNAME: 'Vxlan1'
    add_vpnvnimap_list:
    - VPNINSTANCE: 'VRF_N6_Local_2B_001'
      RULESWITCH: DISABLE
      VNI: 1
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 配置Nxuc逻辑接口所属的VPN实例。

```jinja2
{%- for item in add_vpninst_list -%}
    ADD VPNINST:
    {#- --- 必选参数 --- -#}
    VPNINSTANCE="{{item.VPNINSTANCE}}",
    ;
{%- endfor -%}
```

### 2 配置Nxuc逻辑接口。

```jinja2
{%- for item in add_logicinf_list -%}
    ADD LOGICINF:
    {#- --- 必选参数 --- -#}
    NAME="{{item.NAME}}",
    IPVERSION={{item.IPVERSION}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPV4/IPVER_ALL 时必选 --- -#}
    {%- if item.IPVERSION in ['IPV4', 'IPVER_ALL'] -%}
        IPV4ADDRESS1="{{item.IPV4ADDRESS1}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV4/IPVER_ALL 时必选 --- -#}
    {%- if item.IPVERSION in ['IPV4', 'IPVER_ALL'] -%}
        IPV4MASK1="{{item.IPV4MASK1}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPVERSION=IPV4/IPVER_ALL/IPV6 时可选 --- -#}
    {%- if item.IPVERSION in ['IPV4', 'IPVER_ALL', 'IPV6'] -%}
        {%- if item.VPNINSTANCE is not none -%}
            VPNINSTANCE="{{item.VPNINSTANCE}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置VXLAN隧道组。

```jinja2
{%- for item in add_vxlangrp_list -%}
    ADD VXLANGRP:
    {#- --- 必选参数 --- -#}
    GRPNAME="{{item.GRPNAME}}",
    SRCINTF="{{item.SRCINTF}}",
    {#- --- 可选参数 --- -#}
    {%- if item.HEARTBEAT is not none -%}
        HEARTBEAT={{item.HEARTBEAT}},
    {%- endif -%}
    {%- if item.TIMETHRESHOLD is not none -%}
        TIMETHRESHOLD={{item.TIMETHRESHOLD}},
    {%- endif -%}
    {%- if item.HEARTSUCCLIMIT is not none -%}
        HEARTSUCCLIMIT={{item.HEARTSUCCLIMIT}},
    {%- endif -%}
    {%- if item.HEARTFAILLIMIT is not none -%}
        HEARTFAILLIMIT={{item.HEARTFAILLIMIT}},
    {%- endif -%}
    {%- if item.TIMEOUT is not none -%}
        TIMEOUT={{item.TIMEOUT}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 配置到MPF的VXLAN隧道端点（VTEP）。

```jinja2
{%- for item in add_vtep_list -%}
    ADD VTEP:
    {#- --- 必选参数 --- -#}
    VTEPNAME="{{item.VTEPNAME}}",
    IPVERSION={{item.IPVERSION}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV4' -%}
        VTEPIPV4="{{item.VTEPIPV4}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 配置VXLAN端点绑定VXLAN隧道组。

```jinja2
{%- for item in add_vtepbindgrp_list -%}
    ADD VTEPBINDGRP:
    {#- --- 必选参数 --- -#}
    VXLANGRPNAME="{{item.VXLANGRPNAME}}",
    VTEPNAME="{{item.VTEPNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.PRIFLAG is not none -%}
        PRIFLAG={{item.PRIFLAG}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 6 配置VXLAN隧道组绑定APN。

```jinja2
{%- for item in add_vxlanbindapn_list -%}
    ADD VXLANBINDAPN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    VXLANGRPNAME="{{item.VXLANGRPNAME}}",
    ;
{%- endfor -%}
```

### 7 配置VPN到VNI的映射。

```jinja2
{%- for item in add_vpnvnimap_list -%}
    ADD VPNVNIMAP:
    {#- --- 必选参数 --- -#}
    VPNINSTANCE="{{item.VPNINSTANCE}}",
    RULESWITCH={{item.RULESWITCH}},
    VNI={{item.VNI}},
    ;
{%- endfor -%}
```

