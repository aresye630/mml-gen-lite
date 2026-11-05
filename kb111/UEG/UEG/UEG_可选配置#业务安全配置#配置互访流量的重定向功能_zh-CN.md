---
id: ''
name: 配置互访流量的重定向功能
ne_type: UEG
type: feature
description: 重定向功能可以防止上行报文可能存在的报文攻击问题。通过重定向功能的设置保证了在同一UEG内部同一VPN的UE用户之间报文转发的安全。  * 适用于PGW-U、UPF。 * 本文中的重定向设备以Firewall为例。 * PGW-U/UPF内置NAT功能时，不支持UE互访。  UEG报文重定向示意图如图1所示。  **图1** UEG报文重定向示意图  如图1，采用DC-GW上基于ACL+重定向IP实现重定向方案时，组网要求如下：  * DC-GW上需完成ACL及重定向IP等策略路由的相关配置。 * UEG发送上行报文（重定向报文和普通N6/SGi报文）和接收用户下行报文的子接口复用（单子接口），VLAN复用，VPN复用，IP地址段复用。
tags: []
risk_level: ''
doc_source:
  - ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝S”，入驻式）","虚机容器模式","配置安全数据（风筝S）","安全配置建议","可选配置","业务安全配置","配置互访流量的重定向功能"]
  - ["网络部署","地市共享式（仅连接）","5GC toB 部署边缘站点（站点为“风筝S”，共享式）","配置安全数据（风筝S）","安全配置建议","可选配置","业务安全配置","配置互访流量的重定向功能"]
  - ["网络部署","园区入驻+地市共享（连接+计算）","5GC toB 部署边缘站点（站点为“风筝S”，带计算）","配置安全数据（风筝S）","配置UEG安全数据","UPF安全数据","安全配置建议","可选配置","业务安全配置","配置互访流量的重定向功能"]
  - ["网络部署","园区入驻+地市共享（连接+计算）","5GC toB 部署边缘站点（站点为“风筝S”，带计算）","配置安全数据（风筝S）","配置UEG安全数据","MPF安全数据","安全配置建议","可选配置","业务安全配置","配置互访流量的重定向功能"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
重定向功能可以防止上行报文可能存在的报文攻击问题。通过重定向功能的设置保证了在同一UEG内部同一VPN的UE用户之间报文转发的安全。* 适用于PGW-U、UPF。* 本文中的重定向设备以Firewall为例。* PGW-U/UPF内置NAT功能时，不支持UE互访。UEG报文重定向示意图如图1所示。**图1** UEG报文重定向示意图如图1，采用DC-GW上基于ACL+重定向IP实现重定向方案时，组网要求如下：* DC-GW上需完成ACL及重定向IP等策略路由的相关配置。* UEG发送上行报文（重定向报文和普通N6/SGi报文）和接收用户下行报文的子接口复用（单子接口），VLAN复用，VPN复用，IP地址段复用。

## 必备事项
前提条件

如果运营商规划采用VPN组网方式，则操作员在执行本操作前应已创建了相应的VPN实例。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_giredirectfunc_list:
      type: items
      properties:
        V4GIREDIRSWITCH:
          name: 'IPV4全局Gi重定向开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: '**SET GIREDIRECTFUNC**'
          data_source: '本端规划'
          pattern: ''
          default: ''
        V6GIREDIRSWITCH:
          name: 'IPV6全局Gi重定向开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_giredirectpara_list:
      type: items
      properties:
        VPNINSTANCE:
          name: '需绑定的VPN实例名'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '此处是基于VPN实现UE互访，即：VPN和一个APN关联时，则是同一APN内的UE互访；VPN和多个APN关联时，则是同一APN内的UE互访+不同APN间的UE互访。  **ADD GIREDIRECTPARA**   * “IPv4重定向IP地址（IPV4ADDRESS）”是重定向设备的IPv4地址。 * “IPv6重定向IP地址（IPV6ADDRESS）”是重定向设备的IPv6地址。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPTYPE:
          name: '重定向的目的地址类型'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        V4REDIRIPTYPE:
          name: 'IPv4重定向动作'
          type: string
          enum:
          - BLACKHOLE
          - IPADDRESS
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4ADDRESS:
          name: 'IPv4重定向IP地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_l3vpninst_list:
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
    add_vpninstaf_list:
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
          - ipv6uni
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VRFRD:
          name: '路由标识'
          type: string
          maxLength: 21
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_giredirectpara_list_1:
      type: items
      properties:
        VPNINSTANCE:
          name: '需绑定的VPN实例名'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '此处是基于VPN实现UE互访，即：VPN和一个APN关联时，则是同一APN内的UE互访；VPN和多个APN关联时，则是同一APN内的UE互访+不同APN间的UE互访。  **ADD GIREDIRECTPARA**   * “IPv4重定向IP地址（IPV4ADDRESS）”是重定向设备的IPv4地址。 * “IPv6重定向IP地址（IPV6ADDRESS）”是重定向设备的IPv6地址。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPTYPE:
          name: '重定向的目的地址类型'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        V4REDIRIPTYPE:
          name: 'IPv4重定向动作'
          type: string
          enum:
          - BLACKHOLE
          - IPADDRESS
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4ADDRESS:
          name: 'IPv4重定向IP地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_giredirectpara_list_2:
      type: items
      properties:
        VPNINSTANCE:
          name: '需绑定的VPN实例名'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPTYPE:
          name: '重定向的目的地址类型'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        V6REDIRIPTYPE:
          name: 'IPv6重定向动作'
          type: string
          enum:
          - BLACKHOLE
          - IPADDRESS
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV6ADDRESS:
          name: 'IPv6重定向IP地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_giredirectpara_list_3:
      type: items
      properties:
        VPNINSTANCE:
          name: '需绑定的VPN实例名'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '此处是基于VPN实现UE互访，即：VPN和一个APN关联时，则是同一APN内的UE互访；VPN和多个APN关联时，则是同一APN内的UE互访+不同APN间的UE互访。  **ADD GIREDIRECTPARA**   * “IPv4重定向IP地址（IPV4ADDRESS）”是重定向设备的IPv4地址。 * “IPv6重定向IP地址（IPV6ADDRESS）”是重定向设备的IPv6地址。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPTYPE:
          name: '重定向的目的地址类型'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        V4REDIRIPTYPE:
          name: 'IPv4重定向动作'
          type: string
          enum:
          - BLACKHOLE
          - IPADDRESS
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4ADDRESS:
          name: 'IPv4重定向IP地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_giredirectpara_list_4:
      type: items
      properties:
        VPNINSTANCE:
          name: '需绑定的VPN实例名'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '此处是基于VPN实现UE互访，即：VPN和一个APN关联时，则是同一APN内的UE互访；VPN和多个APN关联时，则是同一APN内的UE互访+不同APN间的UE互访。  **ADD GIREDIRECTPARA**   * “IPv4重定向IP地址（IPV4ADDRESS）”是重定向设备的IPv4地址。 * “IPv6重定向IP地址（IPV6ADDRESS）”是重定向设备的IPv6地址。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPTYPE:
          name: '重定向的目的地址类型'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        V4REDIRIPTYPE:
          name: 'IPv4重定向动作'
          type: string
          enum:
          - BLACKHOLE
          - IPADDRESS
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4ADDRESS:
          name: 'IPv4重定向IP地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_giredirectpara_list_5:
      type: items
      properties:
        VPNINSTANCE:
          name: '需绑定的VPN实例名'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPTYPE:
          name: '重定向的目的地址类型'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        V6REDIRIPTYPE:
          name: 'IPv6重定向动作'
          type: string
          enum:
          - BLACKHOLE
          - IPADDRESS
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV6ADDRESS:
          name: 'IPv6重定向IP地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_giredirectpara_list_6:
      type: items
      properties:
        VPNINSTANCE:
          name: '需绑定的VPN实例名'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPTYPE:
          name: '重定向的目的地址类型'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        V6REDIRIPTYPE:
          name: 'IPv6重定向动作'
          type: string
          enum:
          - BLACKHOLE
          - IPADDRESS
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV6ADDRESS:
          name: 'IPv6重定向IP地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
  examples:
    set_giredirectfunc_list:
    - V4GIREDIRSWITCH: ENABLE
      V6GIREDIRSWITCH: ENABLE
    add_giredirectpara_list:
    - VPNINSTANCE: 'ispvpn1'
      IPTYPE: IPv4
      V4REDIRIPTYPE: IPADDRESS
      IPV4ADDRESS: '10.1.1.1'
    add_l3vpninst_list:
    - VRFNAME: 'ispvpn1'
    add_vpninst_list:
    - VPNINSTANCE: 'ispvpn1'
    add_vpninstaf_list:
    - VRFNAME: 'ispvpn1'
      AFTYPE: ipv4uni
      VRFRD: '192.168.225.138:100'
    - VRFNAME: 'ispvpn1'
      AFTYPE: ipv6uni
      VRFRD: '192.168.225.138:100'
    add_giredirectpara_list_1:
    - VPNINSTANCE: 'ispvpn1'
      IPTYPE: IPv4
      V4REDIRIPTYPE: IPADDRESS
      IPV4ADDRESS: '10.1.1.1'
    add_giredirectpara_list_2:
    - VPNINSTANCE: 'ispvpn1'
      IPTYPE: IPv6
      V6REDIRIPTYPE: IPADDRESS
      IPV6ADDRESS: 'FC00::10:1:1:1'
    add_giredirectpara_list_3:
    - VPNINSTANCE: '\_public\_'
      IPTYPE: IPv4
      V4REDIRIPTYPE: IPADDRESS
      IPV4ADDRESS: '10.1.1.1'
    add_giredirectpara_list_4:
    - VPNINSTANCE: '_public_'
      IPTYPE: IPv4
      V4REDIRIPTYPE: IPADDRESS
      IPV4ADDRESS: '10.1.1.1'
    add_giredirectpara_list_5:
    - VPNINSTANCE: '_public_'
      IPTYPE: IPv6
      V6REDIRIPTYPE: IPADDRESS
      IPV6ADDRESS: 'FC00::10:1:1:1'
    add_giredirectpara_list_6:
    - VPNINSTANCE: 'VPN Instance to Bind'
      IPTYPE: IPv6
      V6REDIRIPTYPE: IPADDRESS
      IPV6ADDRESS: 'FC00::10:1:1:1'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 以下命令在“MML命令行 - UEG”窗口上执行。设置全局的SGi重定向开关。

```jinja2
{%- for item in set_giredirectfunc_list -%}
    SET GIREDIRECTFUNC:
    {#- --- 必选参数 --- -#}
    V4GIREDIRSWITCH={{item.V4GIREDIRSWITCH}},
    V6GIREDIRSWITCH={{item.V6GIREDIRSWITCH}},
    ;
{%- endfor -%}
```

### 当全局的SGi接口重定向开关为不使能时，整个UEG的所有VPN的SGi接口重定向功能都会被关闭。使能全局的SGi接口重定向后，还要根据各个VPN的重定向配置来决定是否进行SGi接口的重定向。

### 2 设置基于某个VPN的SGi重定向开关及重定向报文的目的地址。

```jinja2
{%- for item in add_giredirectpara_list -%}
    ADD GIREDIRECTPARA:
    {#- --- 必选参数 --- -#}
    VPNINSTANCE="{{item.VPNINSTANCE}}",
    IPTYPE={{item.IPTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPTYPE=IPv4 时必选 --- -#}
    {%- if item.IPTYPE == 'IPv4' -%}
        V4REDIRIPTYPE={{item.V4REDIRIPTYPE}},
    {%- endif -%}
    {#- --- 条件必选：V4REDIRIPTYPE=IPADDRESS 时必选 --- -#}
    {%- if item.V4REDIRIPTYPE == 'IPADDRESS' -%}
        IPV4ADDRESS="{{item.IPV4ADDRESS}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### //IPv4, IPv6, or IPv4v6:

```jinja2
{%- for item in add_l3vpninst_list -%}
    ADD L3VPNINST:
    {#- --- 必选参数 --- -#}
    VRFNAME="{{item.VRFNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_vpninst_list -%}
    ADD VPNINST:
    {#- --- 必选参数 --- -#}
    VPNINSTANCE="{{item.VPNINSTANCE}}",
    ;
{%- endfor -%}
```

### //IPv4:

```jinja2
{%- for item in add_vpninstaf_list -%}
    ADD VPNINSTAF:
    {#- --- 必选参数 --- -#}
    VRFNAME="{{item.VRFNAME}}",
    AFTYPE={{item.AFTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.VRFRD is not none -%}
        VRFRD="{{item.VRFRD}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### //IPv6:

#### 2.1 //IPv4：

```jinja2
{%- for item in add_giredirectpara_list_1 -%}
    ADD GIREDIRECTPARA:
    {#- --- 必选参数 --- -#}
    VPNINSTANCE="{{item.VPNINSTANCE}}",
    IPTYPE={{item.IPTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPTYPE=IPv4 时必选 --- -#}
    {%- if item.IPTYPE == 'IPv4' -%}
        V4REDIRIPTYPE={{item.V4REDIRIPTYPE}},
    {%- endif -%}
    {#- --- 条件必选：V4REDIRIPTYPE=IPADDRESS 时必选 --- -#}
    {%- if item.V4REDIRIPTYPE == 'IPADDRESS' -%}
        IPV4ADDRESS="{{item.IPV4ADDRESS}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.2 //IPv6：

```jinja2
{%- for item in add_giredirectpara_list_2 -%}
    ADD GIREDIRECTPARA:
    {#- --- 必选参数 --- -#}
    VPNINSTANCE="{{item.VPNINSTANCE}}",
    IPTYPE={{item.IPTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPTYPE=IPv6 时必选 --- -#}
    {%- if item.IPTYPE == 'IPv6' -%}
        V6REDIRIPTYPE={{item.V6REDIRIPTYPE}},
    {%- endif -%}
    {#- --- 条件必选：V6REDIRIPTYPE=IPADDRESS 时必选 --- -#}
    {%- if item.V6REDIRIPTYPE == 'IPADDRESS' -%}
        IPV6ADDRESS="{{item.IPV6ADDRESS}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 设置默认VPN（\_public\_）用户的SGi重定向开关及重定向报文的目的地址。

```jinja2
{%- for item in add_giredirectpara_list_3 -%}
    ADD GIREDIRECTPARA:
    {#- --- 必选参数 --- -#}
    VPNINSTANCE="{{item.VPNINSTANCE}}",
    IPTYPE={{item.IPTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPTYPE=IPv4 时必选 --- -#}
    {%- if item.IPTYPE == 'IPv4' -%}
        V4REDIRIPTYPE={{item.V4REDIRIPTYPE}},
    {%- endif -%}
    {#- --- 条件必选：V4REDIRIPTYPE=IPADDRESS 时必选 --- -#}
    {%- if item.V4REDIRIPTYPE == 'IPADDRESS' -%}
        IPV4ADDRESS="{{item.IPV4ADDRESS}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 3.1 //IPv4：

```jinja2
{%- for item in add_giredirectpara_list_4 -%}
    ADD GIREDIRECTPARA:
    {#- --- 必选参数 --- -#}
    VPNINSTANCE="{{item.VPNINSTANCE}}",
    IPTYPE={{item.IPTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPTYPE=IPv4 时必选 --- -#}
    {%- if item.IPTYPE == 'IPv4' -%}
        V4REDIRIPTYPE={{item.V4REDIRIPTYPE}},
    {%- endif -%}
    {#- --- 条件必选：V4REDIRIPTYPE=IPADDRESS 时必选 --- -#}
    {%- if item.V4REDIRIPTYPE == 'IPADDRESS' -%}
        IPV4ADDRESS="{{item.IPV4ADDRESS}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 3.2 //IPv6：

```jinja2
{%- for item in add_giredirectpara_list_5 -%}
    ADD GIREDIRECTPARA:
    {#- --- 必选参数 --- -#}
    VPNINSTANCE="{{item.VPNINSTANCE}}",
    IPTYPE={{item.IPTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPTYPE=IPv6 时必选 --- -#}
    {%- if item.IPTYPE == 'IPv6' -%}
        V6REDIRIPTYPE={{item.V6REDIRIPTYPE}},
    {%- endif -%}
    {#- --- 条件必选：V6REDIRIPTYPE=IPADDRESS 时必选 --- -#}
    {%- if item.V6REDIRIPTYPE == 'IPADDRESS' -%}
        IPV6ADDRESS="{{item.IPV6ADDRESS}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 设置IPv6 Gi redirect。

```jinja2
{%- for item in add_giredirectpara_list_6 -%}
    ADD GIREDIRECTPARA:
    {#- --- 必选参数 --- -#}
    VPNINSTANCE="{{item.VPNINSTANCE}}",
    IPTYPE={{item.IPTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPTYPE=IPv6 时必选 --- -#}
    {%- if item.IPTYPE == 'IPv6' -%}
        V6REDIRIPTYPE={{item.V6REDIRIPTYPE}},
    {%- endif -%}
    {#- --- 条件必选：V6REDIRIPTYPE=IPADDRESS 时必选 --- -#}
    {%- if item.V6REDIRIPTYPE == 'IPADDRESS' -%}
        IPV6ADDRESS="{{item.IPV6ADDRESS}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

