---
id: ''
name: 配置到DNS相关数据
ne_type: UNC
type: feature
description: 当运营商在部署分组交换网，在配置完成UNC到DNS的路由数据后，可通过配置N26接口数据建立UNC到DNS的逻辑连接，用于在以下流程中进行域名解析：  * 在Attach流程、PDN连接建立流程、Handover/TAU流程及GUL互操作流程中，根据DNS数据解析S-GW、P-GW、对等MME、SGSN网元的IP地址。 * 在基于Sv接口部署SRVCC的场景下，根据DNS数据解析MSC的IP地址。  进行域名解析可以使用三种手段：使用DNS服务器、通过Cache查询或使用本地主机信息表（Hostfile），通常主要使用DNS服务器进行域名解析，Hostfile作为辅助手段。其中：  * DNS服务器是网络中专门提供域名解析服务的服务器。 * DNS Cache是DNS服务器解析到的域名和IP地址在UNC的缓存，用于快速解析域名，以减少访问DNS服务器的次数，其记录具有一定的生命周期，生命周期结束后，该记录失效。生命周期由DNS响应消息中的TTL携带。 * 本地主机信息表Hostfile则保存在本地，包含的记录比较少。  UNC进行域名解析时默认按照以下顺序进行：首先查找Hostfile中的主机信息记录；如果没有相应的记录，则查找DNS Cache中的记录。如果没有相应的记录，向DNS服务器发送解析请求进行解析。
risk_level: ''
doc_source: ["网络部署","初始配置","UNC初始配置与调测","组网对接配置","配置AMF&MME&SGSN","配置AMF","配置到DNS相关数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当运营商在部署分组交换网，在配置完成UNC到DNS的路由数据后，可通过配置N26接口数据建立UNC到DNS的逻辑连接，用于在以下流程中进行域名解析：* 在Attach流程、PDN连接建立流程、Handover/TAU流程及GUL互操作流程中，根据DNS数据解析S-GW、P-GW、对等MME、SGSN网元的IP地址。* 在基于Sv接口部署SRVCC的场景下，根据DNS数据解析MSC的IP地址。进行域名解析可以使用三种手段：使用DNS服务器、通过Cache查询或使用本地主机信息表（Hostfile），通常主要使用DNS服务器进行域名解析，Hostfile作为辅助手段。其中：* DNS服务器是网络中专门提供域名解析服务的服务器。* DNS Cache是DNS服务器解析到的域名和IP地址在UNC的缓存，用于快速解析域名，以减少访问DNS服务器的次数，其记录具有一定的生命周期，生命周期结束后，该记录失效。生命周期由DNS响应消息中的TTL携带。* 本地主机信息表Hostfile则保存在本地，包含的记录比较少。UNC进行域名解析时默认按照以下顺序进行：首先查找Hostfile中的主机信息记录；如果没有相应的记录，则查找DNS Cache中的记录。如果没有相应的记录，向DNS服务器发送解析请求进行解析。

## 必备事项
前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020客户端或登录OM Portal）。

* UNC软件安装已完成。

* 请了解UNC各类接口的类型及命名规范，具体内容请参见业务组网与逻辑接口介绍。
* UNC上的N26接口路由配置已经完成。

  UNC侧通过N26接口路由与DNS互通，因此只需确保N26接口路由配置完成，那么UNC到DNS的路由配置也就完成了。
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
          name: 'VPN名称'
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
    set_ngdns_list:
      type: items
      properties:
        MMESWITCH:
          name: '优选融合MME开关'
          type: string
          enum:
          - MME_ON
          - MME_OFF
          required: false
          description: '-'
          data_source: ''
          pattern: ''
          default: ''
    add_ngipv4dnsh_list:
      type: items
      properties:
        HSINDEX:
          name: '主机名索引'
          type: integer
          minimum: 1
          maximum: 1024
          required: true
          description: '指定主机名的索引。'
          data_source: ''
          pattern: ''
          default: ''
        HOSTNAME:
          name: '主机名'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: '配置主机名。'
          data_source: ''
          pattern: ''
          default: ''
        ADDRSECTION:
          name: '地址区间号'
          type: string
          enum:
          - SECTION1
          - SECTION2
          - SECTION3
          - SECTION4
          - SECTION5
          - SECTION6
          - SECTION7
          - SECTION8
          required: true
          description: '用于划分IP地址区间。  一个域名最多可以配置64个IP地址，使用该参数将64个IP地址划分为8个区间，每个区间配置8个IP地址，减少了配置复杂度。所有区间的IP地址按照优先级和权重进行排序。'
          data_source: ''
          pattern: ''
          default: ''
        IPV4ADDR1:
          name: 'IPV4地址1'
          type: string
          maxLength: 15
          required: false
          description: '指定主机对应的IPv4地址。'
          data_source: ''
          pattern: ''
          default: ''
    add_ngdnsn_list:
      type: items
      properties:
        FQDN:
          name: 'FQDN'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: '表示由RAI、TAI、APN、MME等构建的域名，用来进行网元查询。'
          data_source: ''
          pattern: ''
          default: ''
        HSINDEX:
          name: '主机名索引'
          type: integer
          minimum: 1
          maximum: 2048
          required: true
          description: '指定主机名的索引。'
          data_source: ''
          pattern: ''
          default: ''
        ENTITY:
          name: '网元类型'
          type: string
          enum:
          - MME
          - NG
          required: true
          description: '指定接口网元的类型。'
          data_source: ''
          pattern: ''
          default: ''
        INTYPE:
          name: '接口类型'
          type: string
          enum:
          - N26
          - SBI
          required: true
          description: '指定接口对应的类型。'
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
    set_ngdns_list:
    - MMESWITCH: MME_ON
    add_ngipv4dnsh_list:
    - HSINDEX: 10
      HOSTNAME: 'smf1.cluster1.net2.smf.5gc.mnc003.mcc123.3gppnetwork.org'
      ADDRSECTION: SECTION1
      IPV4ADDR1: '172.16.1.5'
    add_ngdnsn_list:
    - FQDN: 'amf1.cluster1.net2.amf.5gc.mnc003.mcc123.3gppnetwork.org'
      HSINDEX: 10
      ENTITY: MME
      INTYPE: N26
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

```jinja2
{%- for item in set_ngdns_list -%}
    SET NGDNS:
    {#- --- 可选参数 --- -#}
    {%- if item.MMESWITCH is not none -%}
        MMESWITCH={{item.MMESWITCH}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 （可选）配置N26接口的A记录。

```jinja2
{%- if is_optional_n26_a_record -%}
    {%- for item in add_ngipv4dnsh_list -%}
        ADD NGIPV4DNSH:
        {#- --- 必选参数 --- -#}
        HSINDEX={{item.HSINDEX}},
        HOSTNAME="{{item.HOSTNAME}}",
        ADDRSECTION={{item.ADDRSECTION}},
        {#- --- 可选参数 --- -#}
        {%- if item.IPV4ADDR1 is not none -%}
            IPV4ADDR1="{{item.IPV4ADDR1}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 5 （可选）配置N26接口的N记录。

```jinja2
{%- if is_optional_n26_n_record -%}
    {%- for item in add_ngdnsn_list -%}
        ADD NGDNSN:
        {#- --- 必选参数 --- -#}
        FQDN="{{item.FQDN}}",
        HSINDEX={{item.HSINDEX}},
        ENTITY={{item.ENTITY}},
        INTYPE={{item.INTYPE}},
        ;
    {%- endfor -%}
{%- endif -%}
```

### 和AMF有交互的MME覆盖的TAC和MMEID都要进行配置；MME覆盖TAC、MMEID以及MME IP地址请根据实际网络数据进行配置。

### ADD NGDNSN命令中HSINDEX参数值需要和ADD NGIPV4DNSH命令中的HSINDEX参数值匹配。

