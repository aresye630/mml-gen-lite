---
id: GWFD-030501
name: 激活终端二次鉴权
ne_type: UEG
type: feature
description: UPF下沉，DN-AAA部署到企业或园区，SMF与DN-AAA之间不能直接互通，需要UPF转发SMF与DN-AAA之间二次鉴权的消息。  适用于UPF、SMF。
tags: []
risk_level: ''
doc_source:
  - ["业务配置","风筝L","MEC 特性指南（风筝L）","GW-U&UPF特性指南","GWFD-030500 边缘安全防护","GWFD-030501 终端二次鉴权","激活终端二次鉴权"]
  - ["业务配置","风筝L","MEC 特性指南（风筝L）","GW-C&SMF特性指南","GWFD-030500 边缘安全防护","GWFD-030501 终端二次鉴权","激活终端二次鉴权"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
UPF下沉，DN-AAA部署到企业或园区，SMF与DN-AAA之间不能直接互通，需要UPF转发SMF与DN-AAA之间二次鉴权的消息。适用于UPF、SMF。

## 必备事项
前提条件

前提条件

* 请仔细阅读终端二次鉴权特性概述。
* 完成Radius鉴权接入配置。
* 完成Radius功能配置。

激活RADIUS功能中配置到AAA Server的数据（双平面+OSPF动态路由+BFD组网 ）里 步骤5.配置Gi逻辑接口和步骤7.配置APN下的Client-IP在终端二次鉴权场景下为**可选配置**。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_cpgtpuaddr_list:
      type: items
      properties:
        IPVERSION:
          name: 'IP地址类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4ADDR:
          name: 'IPV4ADDR'
          type: string
          maxLength: 15
          required: false
          description: '用于指定与UPF对接的本端GTP-U IPv4地址。(该参数在"IPVERSION"配置为"IPV4"时为条件必选参数。)  本特性中该参数取值是与UPF共同规划，是由SMF下发的分装GTPU报文的IP地址。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_uplist4rds_list:
      type: items
      properties:
        UPLISTNAME:
          name: 'UPLISTNAME'
          type: string
          maxLength: 63
          required: true
          description: 'UP列表名称,用于指定UP列表名称。  取值范围：字符串类型，输入长度范围为1～63。长度1到63的非空格字符串。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPINSTANCEID:
          name: 'UPINSTANCEID'
          type: string
          maxLength: 36
          required: true
          description: 'UP实例标识，用于指定UP实例标识。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_rdsupfctrl_list:
      type: items
      properties:
        UPLISTNAME:
          name: 'UP列表名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UPINSTANCEID:
          name: 'UP实例标识'
          type: string
          minLength: 1
          maxLength: 36
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PREFERENCE:
          name: '优先级'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCKED:
          name: '锁定'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_upfrdsclientip_list:
      type: items
      properties:
        CLIENTYPE:
          name: 'CLIENTYPE'
          type: string
          enum:
          - AUTHENTICATION
          - ACCOUNTING
          - ACCT_AND_AUTH
          required: true
          description: '指定RADIUS客户端类型。  取值范围：   * “AUTHENTICATION（鉴权客户端）”：表示鉴权客户端。 * “ACCOUNTING（计费客户端）”：表示计费客户端。 * “ACCT\_AND\_AUTH（计费和鉴权客户端）”：表示计费和鉴权客户端。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPVERSION:
          name: '客户端IP版本'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UPLISTNAME:
          name: 'UP列表名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VPNINSTANCE:
          name: 'VPNINSTANCE'
          type: string
          minLength: 1
          maxLength: 31
          required: false
          description: '指定VPN实例。本参数由UPF和DN-AAA共同规划，是UPF与DN-AAA对接的VPN。  取值范围：字符串类型，输入长度范围是1~31。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CLIENTIPV4:
          name: 'CLIENTIPV4'
          type: string
          maxLength: 15
          required: false
          description: '用于指定RADIUS客户端IPv4地址。SMF下发至UPF，经UPF转发的ClientIP。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_upfrdssvr_list:
      type: items
      properties:
        SERVERTYPE:
          name: 'SERVERTYPE'
          type: string
          enum:
          - AUTHENTICATION
          - ACCOUNTING
          required: true
          description: '指定RADIUS服务器类型。  取值范围：   * “AUTHENTICATION（鉴权服务器）”：表示鉴权服务器。 * “ACCOUNTING（计费服务器）”：表示计费服务器。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPVERSION:
          name: '服务器IP版本'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SERVERIPV4:
          name: 'SERVERIPV4'
          type: string
          maxLength: 15
          required: false
          description: 'RADIUS服务器IPv4地址。DN-AAA的IP地址。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        UPLISTNAME:
          name: 'UP列表名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_networkinstvpnmap_list:
      type: items
      properties:
        NETWORKINSTANCE:
          name: '网络实例名称'
          type: string
          minLength: 0
          maxLength: 100
          required: true
          description: '网络实例标识。客户进行网络部署时自行规划，与SMF端规划的网络实例保持一致。  取值范围：字符串类型，输入长度范围为1～100，单位是字节。由“\_”、“-”、数字、大小写字母和“.”组成，不能以“.”开头且不能出现连续两个“.”，不区分大小写。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        HASVPN:
          name: '绑定VPN'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        VPNINSTANCE:
          name: 'VPN实例名'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '用于指定IPv4 VPN实例名。本特性中该参数取值是与DN-AAA共同规划的VPN实例名称。  取值范围：字符串类型，输入长度范围为1～31。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        HASVPNIPV6:
          name: '绑定IPv6 VPN'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        VPNINSTANCEIPV6:
          name: 'IPv6 VPN实例名'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '用于指定IPv6 VPN实例名。本特性中该参数取值是与DN-AAA共同规划的VPN实例名称。  取值范围：字符串类型，输入长度范围为1～31。'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    add_cpgtpuaddr_list:
    - IPVERSION: IPV4
      IPV4ADDR: '192.168.0.20'
    add_uplist4rds_list:
    - UPLISTNAME: 'uplist1'
      UPINSTANCEID: 'up1'
    add_rdsupfctrl_list:
    - UPLISTNAME: 'uplist1'
      UPINSTANCEID: 'up1'
      PREFERENCE: 1
      LOCKED: ENABLE
    add_upfrdsclientip_list:
    - CLIENTYPE: AUTHENTICATION
      IPVERSION: IPV4
      UPLISTNAME: 'uplist1'
      VPNINSTANCE: 'vpnInstance1'
      CLIENTIPV4: '192.168.10.1'
    add_upfrdssvr_list:
    - SERVERTYPE: AUTHENTICATION
      IPVERSION: IPV4
      SERVERIPV4: '192.168.10.2'
      UPLISTNAME: 'uplist1'
    add_networkinstvpnmap_list:
    - NETWORKINSTANCE: 'net1'
      HASVPN: ENABLE
      VPNINSTANCE: 'VPN2auto'
      HASVPNIPV6: DISABLE
      VPNINSTANCEIPV6: 'vnp1'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 增加与UPF对接的本端GTP-U地址。

```jinja2
{%- for item in add_cpgtpuaddr_list -%}
    ADD CPGTPUADDR:
    {#- --- 必选参数 --- -#}
    IPVERSION={{item.IPVERSION}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV4' -%}
        IPV4ADDR="{{item.IPV4ADDR}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 增加中转使用的UP到RADIUS服务器使用的UPF列表。

```jinja2
{%- for item in add_uplist4rds_list -%}
    ADD UPLIST4RDS:
    {#- --- 必选参数 --- -#}
    UPLISTNAME="{{item.UPLISTNAME}}",
    UPINSTANCEID="{{item.UPINSTANCEID}}",
    ;
{%- endfor -%}
```

### 4 可选配置：增加RADIUS服务器使用的UPF列表中指定UPF的功能属性。

```jinja2
{%- if is_optional_add_upf_function_attribute -%}
    {%- for item in add_rdsupfctrl_list -%}
        ADD RDSUPFCTRL:
        {#- --- 必选参数 --- -#}
        UPLISTNAME="{{item.UPLISTNAME}}",
        UPINSTANCEID="{{item.UPINSTANCEID}}",
        PREFERENCE={{item.PREFERENCE}},
        LOCKED={{item.LOCKED}},
        ;
    {%- endfor -%}
{%- endif -%}
```

### 5 增加中转UPF与Radius客户端的绑定关系。

```jinja2
{%- for item in add_upfrdsclientip_list -%}
    ADD UPFRDSCLIENTIP:
    {#- --- 必选参数 --- -#}
    CLIENTYPE={{item.CLIENTYPE}},
    IPVERSION={{item.IPVERSION}},
    UPLISTNAME="{{item.UPLISTNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.VPNINSTANCE is not none -%}
        VPNINSTANCE="{{item.VPNINSTANCE}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV4' -%}
        CLIENTIPV4="{{item.CLIENTIPV4}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 6 新增中转UPF与Radius服务器的绑定关系。

```jinja2
{%- for item in add_upfrdssvr_list -%}
    ADD UPFRDSSVR:
    {#- --- 必选参数 --- -#}
    SERVERTYPE={{item.SERVERTYPE}},
    IPVERSION={{item.IPVERSION}},
    UPLISTNAME="{{item.UPLISTNAME}}",
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV4' -%}
        SERVERIPV4="{{item.SERVERIPV4}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 7 添加网络实例。用于规划UPF与DN-AAA之间的VPN。

```jinja2
{%- for item in add_networkinstvpnmap_list -%}
    ADD NETWORKINSTVPNMAP:
    {#- --- 必选参数 --- -#}
    NETWORKINSTANCE="{{item.NETWORKINSTANCE}}",
    {#- --- 可选参数 --- -#}
    {%- if item.HASVPN is not none -%}
        HASVPN={{item.HASVPN}},
    {%- endif -%}
    {%- if item.HASVPNIPV6 is not none -%}
        HASVPNIPV6={{item.HASVPNIPV6}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：HASVPN=ENABLE 时必选 --- -#}
    {%- if item.HASVPN == 'ENABLE' -%}
        VPNINSTANCE="{{item.VPNINSTANCE}}",
    {%- endif -%}
    {#- --- 条件必选：HASVPNIPV6=ENABLE 时必选 --- -#}
    {%- if item.HASVPNIPV6 == 'ENABLE' -%}
        VPNINSTANCEIPV6="{{item.VPNINSTANCEIPV6}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

