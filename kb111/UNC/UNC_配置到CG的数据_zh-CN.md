---
id: ''
name: 配置到CG的数据
ne_type: UNC
type: feature
description: 当运营商在部署分组交换网，新增CG或SGSN时，在配置完成SGSN到CG的路由数据后，可通过配置Ga接口数据建立SGSN到CG的逻辑连接。
risk_level: ''
doc_source: ["网络部署","初始配置","UNC初始配置与调测","组网对接配置","配置AMF&MME&SGSN","配置SGSN","配置到CG的数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当运营商在部署分组交换网，新增CG或SGSN时，在配置完成SGSN到CG的路由数据后，可通过配置Ga接口数据建立SGSN到CG的逻辑连接。

## 必备事项
前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020/MAE客户端或登录OM Portal）。

* UNC软件安装已完成。

* 请了解UNC各类接口的类型及协议，具体内容请参见业务组网与逻辑接口介绍。
* 对于IPv4组网，已完成自动部署配置动态路由OSPF+BFD组网（IPv4）、配置静态路由+BFD组网（IPv4）、配置BGP over OSPF/静态路由+BFD（IPv4）或手动部署配置动态路由OSPF+BFD组网（IPv4）、配置静态路由+BFD组网（IPv4）、配置BGP over OSPF/静态路由+BFD（IPv4）。
* 对于IPv6组网，已完成自动部署配置动态路由OSPFv3+BFD组网（IPv6）、配置静态路由+BFD组网（IPv6）、配置BGP over OSPFv3/静态路由+BFD（IPv6）或手动部署配置动态路由OSPFv3+BFD组网（IPv6）、配置静态路由+BFD组网（IPv6）、配置BGP over OSPFv3/静态路由+BFD（IPv6）。
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
          description: '配置Ga接口业务IP。'
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
        SERVICEIPV6:
          name: '业务IPv6地址'
          type: string
          maxLength: 39
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
    add_chgcdpip_list:
      type: items
      properties:
        IPT:
          name: 'IP地址类型'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: '增加CDP进程的IP地址。'
          data_source: ''
          pattern: ''
          default: ''
        IPV4ADDR:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PORTBGN:
          name: '起始端口号'
          type: integer
          minimum: 1024
          maximum: 65534
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1024
        PORTEND:
          name: '结束端口号'
          type: integer
          minimum: 1024
          maximum: 65534
          required: false
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
        IPV6ADDR:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_chgcg_list:
      type: items
      properties:
        IP:
          name: 'IP地址类型'
          type: string
          maxLength: 15
          required: false
          description: '配置CG的基本信息。'
          data_source: ''
          pattern: ''
          default: ''
        GRD:
          name: '优先级'
          type: integer
          minimum: 0
          maximum: 11
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        PRO:
          name: 'GTP承载协议'
          type: string
          enum:
          - TCP
          - UDP
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CGR:
          name: 'CG协议版本'
          type: string
          enum:
          - R4
          - R5
          - R6
          - R7
          - R9
          - R98
          - R99
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SPN:
          name: 'CG接收端口号'
          type: integer
          minimum: 1024
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 3386
        DEFAULTCG:
          name: '缺省CG'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
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
    set_chgga_list:
      type: items
      properties:
        GCR:
          name: 'GPRS CDR协议版本'
          type: string
          enum:
          - R4
          - R5
          - R6
          - R7
          - R9
          - R98
          - R99
          required: false
          description: '配置SGSN支持的计费协议版本。'
          data_source: ''
          pattern: ''
          default: ''
        UCR:
          name: 'UMTS CDR协议版本'
          type: string
          enum:
          - R4
          - R5
          - R6
          - R7
          - R9
          - R99
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CHGVER98:
          name: 'R98 CDR版本'
          type: string
          enum:
          - CMCCV130
          - GSM1215V760
          - USI1215V760
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CHGVER99:
          name: 'R99 CDR版本'
          type: string
          enum:
          - AIS32015V360
          - GPP32015V360
          - GPP32015V3A0
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CHGVER4:
          name: 'R4 CDR版本'
          type: string
          enum:
          - GPP32215V440
          - VOX32215V440
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CHGVER5:
          name: 'R5 CDR版本'
          type: string
          enum:
          - GPP32215V560
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CHGVER6:
          name: 'R6 CDR版本'
          type: string
          enum:
          - GPP32251V660
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CHGVER7:
          name: 'R7 CDR版本'
          type: string
          enum:
          - GPP32251V740
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CHGVER9:
          name: 'R9 CDR版本'
          type: string
          enum:
          - GPP32251V940
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ITVRES:
          name: 'CDR重发间隔（s）'
          type: integer
          minimum: 1
          maximum: 10
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RSNUM:
          name: 'CDR重发次数'
          type: integer
          minimum: 1
          maximum: 10
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HDDETH:
          name: '硬盘操作失败告警次数门限'
          type: integer
          minimum: 1
          maximum: 10
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HDDFSL:
          name: '硬盘空间不足门限（%）'
          type: integer
          minimum: 50
          maximum: 90
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_chgbeha_list:
      type: items
      properties:
        CB:
          name: '计费行为'
          type: string
          enum:
          - B1
          - B10
          - B11
          - B12
          - B2
          - B3
          - B4
          - B5
          - B6
          - B7
          - B8
          - B9
          required: true
          description: '增加计费行为参数。'
          data_source: ''
          pattern: ''
          default: ''
        BA:
          name: '行为属性'
          type: string
          enum:
          - CGIP
          - NOQOS
          - NOROAMING
          - PLT
          - PST
          - SMSC
          - SMSCMOMT
          - SMSCMT
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ACC:
          name: '支持的计费属性'
          type: string
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
        PURGELEN:
          name: '关闭空闲PDP定时器时长（min）'
          type: integer
          minimum: 30
          maximum: 1440
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SMSCADDR:
          name: 'SMSC地址'
          type: string
          maxLength: 16
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_chgchar_list:
      type: items
      properties:
        CC:
          name: '计费属性'
          type: string
          enum:
          - FLATRATE
          - HOTBILLING
          - NORMAL
          - PREPAID
          required: true
          description: '配置计费属性参数'
          data_source: ''
          pattern: ''
          default: ''
        SP:
          name: '生成S-CDR'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_chgplmnchar_list:
      type: items
      properties:
        PLMN:
          name: 'PLMN 类型'
          type: string
          enum:
          - HPLMN
          - VPLMN
          required: true
          description: '修改本地PLMN和拜访PLMN的用户计费属性的参数配置。'
          data_source: ''
          pattern: ''
          default: ''
        MP:
          name: '生成M-CDR'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SP:
          name: '生成S-CDR'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SMOP:
          name: '生成S-SMO-CDR'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SMTP:
          name: '生成S-SMT-CDR'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LCSMOP:
          name: '生成LCS-MO-CDR'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LCSMTP:
          name: '生成LCS-MT-CDR'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LCSNIP:
          name: '生成LCS-NI-CDR'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_chgwkdy_list:
      type: items
      properties:
        WKDAY:
          name: '星期序号'
          type: string
          enum:
          - FRI
          - MON
          - SAT
          - SUN
          - THURS
          - TUES
          - WED
          required: true
          description: '配置计费星期。'
          data_source: ''
          pattern: ''
          default: ''
        CC:
          name: '计费属性'
          type: string
          enum:
          - FLATRATE
          - HOTBILLING
          - NORMAL
          - PREPAID
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TT:
          name: '费率类型'
          type: string
          enum:
          - WEEKEND
          - WORK
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_chgtari_list:
      type: items
      properties:
        TT:
          name: '费率类型'
          type: string
          enum:
          - FESTIVAL
          - WEEKEND
          - WORK
          required: true
          description: '配置工作日的四种计费属性用户的费率时段。'
          data_source: ''
          pattern: ''
          default: ''
        ST:
          name: '起始时间'
          type: string
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: 'HH&MM&SS'
        ET:
          name: '结束时间'
          type: string
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: 'HH&MM&SS'
        CC:
          name: '计费属性'
          type: string
          enum:
          - FLATRATE
          - HOTBILLING
          - NORMAL
          - PREPAID
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_serviceip_list:
    - IPVERSION: IPv4
      SERVICEIPV4: '10.10.11.145'
      VPNINSTNAME: 'VPN_Billing'
      SERVICEIPV6: '2001:db8:2001:145'
      IPV6MTU: 1500
    add_chgcdpip_list:
    - IPT: IPv4
      IPV4ADDR: '10.10.11.145'
      PORTBGN: 3699
      PORTEND: 3700
      VPNNAME: 'VPN_Billing'
      IPV6ADDR: '2001:db8:2001:145'
    add_chgcg_list:
    - IP: '10.100.3.17'
      GRD: 1
      PRO: UDP
      CGR: R6
      SPN: 3380
      DEFAULTCG: YES
      IPT: IPV4
    set_chgga_list:
    - GCR: R6
      UCR: R6
      CHGVER98: CMCCV130
      CHGVER99: GPP32015V360
      CHGVER4: GPP32215V440
      CHGVER5: GPP32215V560
      CHGVER6: GPP32251V660
      CHGVER7: GPP32251V740
      CHGVER9: GPP32251V940
      ITVRES: 3
      RSNUM: 3
      HDDETH: 5
      HDDFSL: 70
    add_chgbeha_list:
    - CB: B1
      BA: NOROAMING
      ACC: HOTBILLING-1&FLATRATE-1&PREPAID-1&NORMAL-1
      IPT: IPV4
      PURGELEN: ''
      SMSCADDR: ''
    set_chgchar_list:
    - CC: HOTBILLING
      SP: YES
    set_chgplmnchar_list:
    - PLMN: VPLMN
      MP: YES
      SP: YES
      SMOP: YES
      SMTP: YES
      LCSMOP: YES
      LCSMTP: YES
      LCSNIP: YES
    set_chgwkdy_list:
    - WKDAY: SUN
      CC: HOTBILLING
      TT: WEEKEND
    add_chgtari_list:
    - TT: WORK
      ST: '00&00&00'
      ET: '00&00&00'
      CC: HOTBILLING
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 配置Ga接口业务IP。

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

### 3 配置CG数据。

#### 3.1 增加CDP进程的IP地址。

```jinja2
{%- for item in add_chgcdpip_list -%}
    ADD CHGCDPIP:
    {#- --- 必选参数 --- -#}
    IPT={{item.IPT}},
    {#- --- 可选参数 --- -#}
    {%- if item.PORTBGN is not none -%}
        PORTBGN={{item.PORTBGN}},
    {%- endif -%}
    {%- if item.PORTEND is not none -%}
        PORTEND={{item.PORTEND}},
    {%- endif -%}
    {%- if item.VPNNAME is not none -%}
        VPNNAME="{{item.VPNNAME}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPT=IPv4 时必选 --- -#}
    {%- if item.IPT == 'IPv4' -%}
        IPV4ADDR="{{item.IPV4ADDR}}",
    {%- endif -%}
    {#- --- 条件必选：IPT=IPv6 时必选 --- -#}
    {%- if item.IPT == 'IPv6' -%}
        IPV6ADDR="{{item.IPV6ADDR}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 3.2 配置CG的基本信息。

```jinja2
{%- for item in add_chgcg_list -%}
    ADD CHGCG:
    {#- --- 必选参数 --- -#}
    PRO={{item.PRO}},
    CGR={{item.CGR}},
    {#- --- 可选参数 --- -#}
    {%- if item.SPN is not none -%}
        SPN={{item.SPN}},
    {%- endif -%}
    {%- if item.DEFAULTCG is not none -%}
        DEFAULTCG={{item.DEFAULTCG}},
    {%- endif -%}
    {%- if item.IPT is not none -%}
        IPT={{item.IPT}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPT=IPV4 时必选 --- -#}
    {%- if item.IPT == 'IPV4' -%}
        IP="{{item.IP}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：DEFAULTCG=YES 时可选 --- -#}
    {%- if item.DEFAULTCG == 'YES' -%}
        {%- if item.GRD is not none -%}
            GRD={{item.GRD}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 3.3 配置SGSN支持的计费协议版本。

```jinja2
{%- for item in set_chgga_list -%}
    SET CHGGA:
    {#- --- 可选参数 --- -#}
    {%- if item.GCR is not none -%}
        GCR={{item.GCR}},
    {%- endif -%}
    {%- if item.UCR is not none -%}
        UCR={{item.UCR}},
    {%- endif -%}
    {%- if item.CHGVER98 is not none -%}
        CHGVER98={{item.CHGVER98}},
    {%- endif -%}
    {%- if item.CHGVER99 is not none -%}
        CHGVER99={{item.CHGVER99}},
    {%- endif -%}
    {%- if item.CHGVER4 is not none -%}
        CHGVER4={{item.CHGVER4}},
    {%- endif -%}
    {%- if item.CHGVER5 is not none -%}
        CHGVER5={{item.CHGVER5}},
    {%- endif -%}
    {%- if item.CHGVER6 is not none -%}
        CHGVER6={{item.CHGVER6}},
    {%- endif -%}
    {%- if item.CHGVER7 is not none -%}
        CHGVER7={{item.CHGVER7}},
    {%- endif -%}
    {%- if item.CHGVER9 is not none -%}
        CHGVER9={{item.CHGVER9}},
    {%- endif -%}
    {%- if item.ITVRES is not none -%}
        ITVRES={{item.ITVRES}},
    {%- endif -%}
    {%- if item.RSNUM is not none -%}
        RSNUM={{item.RSNUM}},
    {%- endif -%}
    {%- if item.HDDETH is not none -%}
        HDDETH={{item.HDDETH}},
    {%- endif -%}
    {%- if item.HDDFSL is not none -%}
        HDDFSL={{item.HDDFSL}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 3.4 增加计费行为参数。

```jinja2
{%- for item in add_chgbeha_list -%}
    ADD CHGBEHA:
    {#- --- 必选参数 --- -#}
    CB={{item.CB}},
    BA={{item.BA}},
    ACC={{item.ACC}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：BA=PLT/PST 时必选 --- -#}
    {%- if item.BA in ['PLT', 'PST'] -%}
        PURGELEN={{item.PURGELEN}},
    {%- endif -%}
    {#- --- 条件必选：BA=SMSC/SMSCMT/SMSCMOMT 时必选 --- -#}
    {%- if item.BA in ['SMSC', 'SMSCMT', 'SMSCMOMT'] -%}
        SMSCADDR="{{item.SMSCADDR}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：BA=CGIP 时可选 --- -#}
    {%- if item.BA == 'CGIP' -%}
        {%- if item.IPT is not none -%}
            IPT={{item.IPT}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 3.5 配置计费属性参数

```jinja2
{%- for item in set_chgchar_list -%}
    SET CHGCHAR:
    {#- --- 必选参数 --- -#}
    CC={{item.CC}},
    {#- --- 可选参数 --- -#}
    {%- if item.SP is not none -%}
        SP={{item.SP}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 3.6 修改本地PLMN和拜访PLMN的用户计费属性的参数配置。

```jinja2
{%- for item in set_chgplmnchar_list -%}
    SET CHGPLMNCHAR:
    {#- --- 必选参数 --- -#}
    PLMN={{item.PLMN}},
    {#- --- 可选参数 --- -#}
    {%- if item.MP is not none -%}
        MP={{item.MP}},
    {%- endif -%}
    {%- if item.SP is not none -%}
        SP={{item.SP}},
    {%- endif -%}
    {%- if item.SMOP is not none -%}
        SMOP={{item.SMOP}},
    {%- endif -%}
    {%- if item.SMTP is not none -%}
        SMTP={{item.SMTP}},
    {%- endif -%}
    {%- if item.LCSMOP is not none -%}
        LCSMOP={{item.LCSMOP}},
    {%- endif -%}
    {%- if item.LCSMTP is not none -%}
        LCSMTP={{item.LCSMTP}},
    {%- endif -%}
    {%- if item.LCSNIP is not none -%}
        LCSNIP={{item.LCSNIP}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 配置费率数据。

#### 4.1 配置计费星期。

```jinja2
{%- for item in set_chgwkdy_list -%}
    SET CHGWKDY:
    {#- --- 必选参数 --- -#}
    WKDAY={{item.WKDAY}},
    CC={{item.CC}},
    TT={{item.TT}},
    ;
{%- endfor -%}
```

#### 4.2 配置工作日的四种计费属性用户的费率时段。

```jinja2
{%- for item in add_chgtari_list -%}
    ADD CHGTARI:
    {#- --- 必选参数 --- -#}
    TT={{item.TT}},
    ST={{item.ST}},
    ET={{item.ET}},
    CC={{item.CC}},
    ;
{%- endfor -%}
```

