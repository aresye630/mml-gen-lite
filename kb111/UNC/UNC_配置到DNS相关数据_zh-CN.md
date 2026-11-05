---
id: ''
name: 配置到DNS相关数据
ne_type: UNC
type: feature
description: 当运营商在部署分组交换网，新增MME时，在配置完成MME到DNS的路由数据后，可通过配置S10接口数据建立MME到DNS的逻辑连接，用于MME在以下流程中进行域名解析：  * 在Attach流程、PDN连接建立流程、Handover/TAU流程及GUL互操作流程中，根据DNS数据解析S-GW、P-GW、对等MME、SGSN网元的IP地址。 * 在基于Sv接口部署SRVCC的场景下，根据DNS数据解析MSC的IP地址。  进行域名解析可以使用三种手段：使用DNS服务器、通过Cache查询或使用本地主机信息表（Hostfile），通常主要使用DNS服务器进行域名解析，Hostfile作为辅助手段。其中：  * DNS服务器是网络中专门提供域名解析服务的服务器。 * DNS Cache是DNS服务器解析到的域名和IP地址在UNC的缓存，用于快速解析域名，以减少访问DNS服务器的次数，其记录具有一定的生命周期，生命周期结束后，该记录失效。生命周期由DNS响应消息中的TTL携带。 * 本地主机信息表Hostfile则保存在本地MME中，包含的记录比较少。  MME进行域名解析时默认按照以下顺序进行：首先查找HOSTFILE中的主机信息记录；如果没有相应的记录，则查找DNS Cache中的记录。如果没有相应的记录，向DNS服务器发送解析请求进行解析。
risk_level: ''
doc_source: ["网络部署","初始配置","UNC初始配置与调测","组网对接配置","配置AMF&MME&SGSN","配置MME","配置到DNS相关数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当运营商在部署分组交换网，新增MME时，在配置完成MME到DNS的路由数据后，可通过配置S10接口数据建立MME到DNS的逻辑连接，用于MME在以下流程中进行域名解析：* 在Attach流程、PDN连接建立流程、Handover/TAU流程及GUL互操作流程中，根据DNS数据解析S-GW、P-GW、对等MME、SGSN网元的IP地址。* 在基于Sv接口部署SRVCC的场景下，根据DNS数据解析MSC的IP地址。进行域名解析可以使用三种手段：使用DNS服务器、通过Cache查询或使用本地主机信息表（Hostfile），通常主要使用DNS服务器进行域名解析，Hostfile作为辅助手段。其中：* DNS服务器是网络中专门提供域名解析服务的服务器。* DNS Cache是DNS服务器解析到的域名和IP地址在UNC的缓存，用于快速解析域名，以减少访问DNS服务器的次数，其记录具有一定的生命周期，生命周期结束后，该记录失效。生命周期由DNS响应消息中的TTL携带。* 本地主机信息表Hostfile则保存在本地MME中，包含的记录比较少。MME进行域名解析时默认按照以下顺序进行：首先查找HOSTFILE中的主机信息记录；如果没有相应的记录，则查找DNS Cache中的记录。如果没有相应的记录，向DNS服务器发送解析请求进行解析。

## 必备事项
前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020客户端或登录OM Portal）。

* UNC软件安装已完成。

* 请了解UNC各类接口的类型及命名规范，具体内容请参见逻辑接口介绍。
* MME上的S10接口路由配置已经完成。

  MME侧通过S10接口路由与DNS互通，因此只需确保MME上的S10接口路由配置完成，那么MME到DNS的路由配置也就完成了。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_serviceip_list:
      type: items
      properties:
        IPVERSION:
          name: 'IP版本'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: '配置业务IP参数。'
          data_source: '参见“水平网设LLD文档 ”。'
          pattern: ''
          default: IPv4
        SERVICEIPV4:
          name: '业务IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VPNINSTNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6MTU:
          name: 'IPv6 MTU大小'
          type: integer
          minimum: 1280
          maximum: 65534
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1500
        SERVICEIPV6:
          name: '业务IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_dnsle_list:
      type: items
      properties:
        IPT:
          name: 'IP地址类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: '配置DNS本端实体。   * 通过单端口方式配置DNS参数时，一个IP地址配置一个本地端口号即可。 * 通过多端口方式配置DNS参数时，一个IP地址配置多个本地端口号。'
          data_source: ''
          pattern: ''
          default: ''
        IPV4:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCPORT:
          name: '本地端口号'
          type: integer
          minimum: 15000
          maximum: 65535
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VPNNAME:
          name: 'VPN名称 '
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LENAME:
          name: 'DNS本端实体名称'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_dnss_list:
      type: items
      properties:
        IP:
          name: 'IP地址'
          type: string
          maxLength: 15
          required: false
          description: '配置DNS服务器。   * 每个通用DNS服务器都具有不同的优先级。 * 专用DNS服务器只用于PDN承载激活过程中的域名解析，并且只供特定APN OI或者特定PLMN的用户使用。'
          data_source: ''
          pattern: ''
          default: ''
        PRI:
          name: '域名服务器优先级'
          type: string
          enum:
          - PRI1
          - PRI2
          - PRI3
          - PRI4
          - PRI5
          - PRI6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPT:
          name: 'IP地址类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: IPV4
    set_dns_list:
      type: items
      properties:
        DDS:
          name: 'DNS探测开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: '配置DNS运行参数，包括一些定时器、计数器等参数。  系统为DNS运行参数提供了缺省值，一般不需要用户修改。'
          data_source: ''
          pattern: ''
          default: ''
        DDI:
          name: 'DNS探测间隔（s）'
          type: integer
          minimum: 1
          maximum: 120
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SFT:
          name: '故障判定阈值'
          type: integer
          minimum: 1
          maximum: 10
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FAILTM:
          name: '持续失败最大时长（s）'
          type: integer
          minimum:
          - 0
          - 60
          maximum:
          - 0
          - 6000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RCUPDTM:
          name: '二级Cache提前刷新时间（s）'
          type: integer
          minimum:
          - 0
          - 400
          maximum:
          - 0
          - 6000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_serviceip_list:
    - IPVERSION: IPv4
      SERVICEIPV4: '192.168.140.17'
      VPNINSTNAME: 'VPN_CN'
      IPV6MTU: 1500
      SERVICEIPV6: ''
    add_dnsle_list:
    - IPT: IPV4
      IPV4: '192.168.140.17'
      LOCPORT: 15001
      VPNNAME: 'VPN_CN'
      LENAME: 'Dnsle'
      IPV6: ''
    add_dnss_list:
    - IP: '10.176.152.1'
      PRI: PRI1
      IPT: IPV4
    set_dns_list:
    - DDS: ON
      DDI: 10
      SFT: 5
      FAILTM: 0
      RCUPDTM: 0
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 配置业务IP。

```jinja2
{%- for item in add_serviceip_list -%}
    ADD SERVICEIP:
    {#- --- 必选参数 --- -#}
    IPVERSION={{item.IPVERSION}},
    {#- --- 可选参数 --- -#}
    {%- if item.VPNINSTNAME is not none -%}
        VPNINSTNAME="{{item.VPNINSTNAME}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPv4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv4' -%}
        SERVICEIPV4="{{item.SERVICEIPV4}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPv6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        SERVICEIPV6="{{item.SERVICEIPV6}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPVERSION=IPv6 时可选 --- -#}
    {%- if item.IPVERSION == 'IPv6' -%}
        {%- if item.IPV6MTU is not none -%}
            IPV6MTU={{item.IPV6MTU}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置DNS数据。

#### 3.1 配置DNS客户端。

```jinja2
{%- for item in add_dnsle_list -%}
    ADD DNSLE:
    {#- --- 必选参数 --- -#}
    IPT={{item.IPT}},
    LOCPORT={{item.LOCPORT}},
    {#- --- 可选参数 --- -#}
    {%- if item.VPNNAME is not none -%}
        VPNNAME="{{item.VPNNAME}}",
    {%- endif -%}
    {%- if item.LENAME is not none -%}
        LENAME="{{item.LENAME}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPT=IPV4 时必选 --- -#}
    {%- if item.IPT == 'IPV4' -%}
        IPV4="{{item.IPV4}}",
    {%- endif -%}
    {#- --- 条件必选：IPT=IPV6 时必选 --- -#}
    {%- if item.IPT == 'IPV6' -%}
        IPV6="{{item.IPV6}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 3.2 配置DNS服务器。

```jinja2
{%- for item in add_dnss_list -%}
    ADD DNSS:
    {#- --- 必选参数 --- -#}
    PRI={{item.PRI}},
    {#- --- 可选参数 --- -#}
    {%- if item.IPT is not none -%}
        IPT={{item.IPT}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPT=IPV4 时必选 --- -#}
    {%- if item.IPT == 'IPV4' -%}
        IP="{{item.IP}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 3.3 配置DNS运行参数。

```jinja2
{%- for item in set_dns_list -%}
    SET DNS:
    {#- --- 可选参数 --- -#}
    {%- if item.DDS is not none -%}
        DDS={{item.DDS}},
    {%- endif -%}
    {%- if item.DDI is not none -%}
        DDI={{item.DDI}},
    {%- endif -%}
    {%- if item.SFT is not none -%}
        SFT={{item.SFT}},
    {%- endif -%}
    {%- if item.FAILTM is not none -%}
        FAILTM={{item.FAILTM}},
    {%- endif -%}
    {%- if item.RCUPDTM is not none -%}
        RCUPDTM={{item.RCUPDTM}},
    {%- endif -%}
    ;
{%- endfor -%}
```

