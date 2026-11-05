---
id: GWFD-110941
name: 激活基于基站粒度的IPSQM
ne_type: UDG
type: feature
description: 为了避免流量突发导致丢包，避免报文重传导致带宽进一步恶化，提高终端用户的业务感受，在UDG上配置基于基站对下行用户面流量进行静态整形。  适用于SGW-U、UPF。
risk_level: ''
doc_source: ["特性部署","特性指南","UDG特性指南","QoS功能","GWFD-110941 基于基站粒度的IPSQM","激活基于基站粒度的IPSQM"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
为了避免流量突发导致丢包，避免报文重传导致带宽进一步恶化，提高终端用户的业务感受，在UDG上配置基于基站对下行用户面流量进行静态整形。适用于SGW-U、UPF。

## 必备事项
前提条件

* 请仔细阅读GWFD-110941 基于基站粒度的IPSQM特性概述。
* 完成**加载license**（如果有需求，请联系华为技术支持工程师处理）。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_licenseswitch_list:
      type: items
      properties:
        LICITEM:
          name: 'License项'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SWITCH:
          name: '开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ipsqmshaping_list:
      type: items
      properties:
        IPTYPE:
          name: 'IP地址类型'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: '静态整形的相关数据。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PEERIPV4:
          name: '对端IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        CIR:
          name: '承诺信息速率（兆比特/秒）'
          type: integer
          minimum: 1
          maximum: 10000
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PEERIPV6:
          name: '对端IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_ipsqmqdepth_list:
      type: items
      properties:
        DEPTH:
          name: '队列深度 （报文个数）'
          type: integer
          minimum: 1
          maximum: 1024
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_ipsqmadjust_list:
      type: items
      properties:
        THRESHOLD:
          name: '阈值（兆比特/秒）'
          type: integer
          minimum: 1
          maximum: 50
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        LOWBANDWIDTH:
          name: '低带宽域的最低保护值（千比特/秒）'
          type: integer
          minimum: 100
          maximum: 100000
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        LOWCBS:
          name: '低带宽域的突发尺寸（字节）'
          type: integer
          minimum: 500
          maximum: 100000000
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        HIGHBANDWIDTH:
          name: '高带宽域的最低保护值（千比特/秒）'
          type: integer
          minimum: 100
          maximum: 100000
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        HIGHCBS:
          name: '高带宽域的突发尺寸（字节）'
          type: integer
          minimum: 500
          maximum: 100000000
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_ipsqmviplist_list:
      type: items
      properties:
        USERID:
          name: '用户标识'
          type: string
          enum:
          - IMSI
          - MSISDN
          required: true
          description: 'VIP用户配置不做IPSQM流量整形。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        USERIDINFO:
          name: '用户ID信息'
          type: string
          minLength: 0
          maxLength: 15
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3G5IPSM01'
      SWITCH: ENABLE
    add_ipsqmshaping_list:
    - IPTYPE: IPv4
      PEERIPV4: '192.168.1.235'
      CIR: 100
      PEERIPV6: ''
    set_ipsqmqdepth_list:
    - DEPTH: 256
    set_ipsqmadjust_list:
    - THRESHOLD: 30
      LOWBANDWIDTH: 300
      LOWCBS: 2000
      HIGHBANDWIDTH: 1000
      HIGHCBS: 10000
    add_ipsqmviplist_list:
    - USERID: IMSI
      USERIDINFO: '461000000000001'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 打开本特性的License配置开关，使能整形功能。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 2 配置静态整形带宽。

```jinja2
{%- for item in add_ipsqmshaping_list -%}
    ADD IPSQMSHAPING:
    {#- --- 必选参数 --- -#}
    IPTYPE={{item.IPTYPE}},
    CIR={{item.CIR}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPTYPE=IPv4 时必选 --- -#}
    {%- if item.IPTYPE == 'IPv4' -%}
        PEERIPV4="{{item.PEERIPV4}}",
    {%- endif -%}
    {#- --- 条件必选：IPTYPE=IPv6 时必选 --- -#}
    {%- if item.IPTYPE == 'IPv6' -%}
        PEERIPV6="{{item.PEERIPV6}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 **可选：**配置整形队列深度。

```jinja2
{%- if is_optional_shaping_queue_depth -%}
    {%- for item in set_ipsqmqdepth_list -%}
        SET IPSQMQDEPTH:
        {#- --- 必选参数 --- -#}
        DEPTH={{item.DEPTH}},
        ;
    {%- endfor -%}
{%- endif -%}
```

### 4 **可选：**配置整形资源调整的业务处理节点（POD）的最低保护带宽及突发尺寸，缺省使用初始值。

```jinja2
{%- if is_optional_pod_min_protect_bandwidth_burst -%}
    {%- for item in set_ipsqmadjust_list -%}
        SET IPSQMADJUST:
        {#- --- 必选参数 --- -#}
        THRESHOLD={{item.THRESHOLD}},
        {#- --- 可选参数 --- -#}
        {%- if item.HIGHBANDWIDTH is not none -%}
            HIGHBANDWIDTH={{item.HIGHBANDWIDTH}},
        {%- endif -%}
        {%- if item.HIGHCBS is not none -%}
            HIGHCBS={{item.HIGHCBS}},
        {%- endif -%}
        {%- if item.LOWBANDWIDTH is not none -%}
            LOWBANDWIDTH={{item.LOWBANDWIDTH}},
        {%- endif -%}
        {%- if item.LOWCBS is not none -%}
            LOWCBS={{item.LOWCBS}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 5 **可选：**如果为保障VIP用户的业务体验，可配置VIP用户不做IPSQM流量整形。

```jinja2
{%- if is_optional_vip_user_no_ipsqm_shaping -%}
    {%- for item in add_ipsqmviplist_list -%}
        ADD IPSQMVIPLIST:
        {#- --- 必选参数 --- -#}
        USERID={{item.USERID}},
        USERIDINFO="{{item.USERIDINFO}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

