---
id: ''
name: 激活ASN漫游计费
ne_type: UNC
type: feature
description: 部署对漫游用户进行区分计费，可以当在线漫游用户业务低峰期时启用该功能，如果在业务高峰期才启用该功能，GGSN/PGW-C不能立刻得到所有BGP路由表中的ASN值，影响对漫游用户的计费。  适用于GGSN、PGW-C。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","计费管理功能","WSFD-109006 ASN漫游计费","激活ASN漫游计费"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
部署对漫游用户进行区分计费，可以当在线漫游用户业务低峰期时启用该功能，如果在业务高峰期才启用该功能，GGSN/PGW-C不能立刻得到所有BGP路由表中的ASN值，影响对漫游用户的计费。适用于GGSN、PGW-C。

## 必备事项
前提条件

* 请仔细阅读WSFD-109006 ASN漫游计费。
* 完成激活Gy/Diameter在线计费。
* 不同PLMN间采用eBGP路由组网。
* 完成加载license（如果有需求，请联系华为技术支持工程师处理）。
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
    set_asnfunc_list:
      type: items
      properties:
        ASNSWITCH:
          name: 'ASN功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '配置ASN功能开关属性，将ASN作为漫游计费标识并在CCR中携带。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SYNCINTERVAL:
          name: 'ASN同步周期(小时)'
          type: integer
          minimum: 1
          maximum: 24
          required: false
          description: '设置获取ASN值的周期。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_defaultasn_list:
      type: items
      properties:
        ASNVALUE:
          name: '指定ASN值'
          type: string
          enum:
          - UNSPECIFIEDASN
          - SPECIFIEDASN
          required: true
          description: '不指定SGSN/SGW-C对应的缺省ASN值。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DEFAULTASN:
          name: '缺省ASN'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_staticasn_list:
      type: items
      properties:
        SRVNODEIP:
          name: 'Service Node信令IP地址'
          type: string
          maxLength: 15
          required: true
          description: '设置SGSN/SGW-C的信令地址和ASN映射的本地表项。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MASK:
          name: 'IP掩码'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ASN:
          name: 'ASN'
          type: integer
          minimum: 1
          maximum: 65535
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3W9ASNR11'
      SWITCH: ENABLE
    set_asnfunc_list:
    - ASNSWITCH: ENABLE
      SYNCINTERVAL: 5
    set_defaultasn_list:
    - ASNVALUE: UNSPECIFIEDASN
      DEFAULTASN: ''
    add_staticasn_list:
    - SRVNODEIP: '10.13.13.0'
      MASK: '255.255.255.0'
      ASN: 1
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 打开本特性的License开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 2 配置ASN功能开关属性。

```jinja2
{%- for item in set_asnfunc_list -%}
    SET ASNFUNC:
    {#- --- 可选参数 --- -#}
    {%- if item.ASNSWITCH is not none -%}
        ASNSWITCH={{item.ASNSWITCH}},
    {%- endif -%}
    {%- if item.SYNCINTERVAL is not none -%}
        SYNCINTERVAL={{item.SYNCINTERVAL}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 设置同步ASN的周期，同步刷新是指从刷新时间开始，到周期结束，整个路径和隧道上的ASN被刷新一次，一般情况下，ASN不会发生变化，所以在配置时，这个时间不要设置太小，太小会影响性能。

### 3 配置是否指定SGSN/SGW-C对应的缺省ASN值。

```jinja2
{%- for item in set_defaultasn_list -%}
    SET DEFAULTASN:
    {#- --- 必选参数 --- -#}
    ASNVALUE={{item.ASNVALUE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：ASNVALUE=SPECIFIEDASN 时必选 --- -#}
    {%- if item.ASNVALUE == 'SPECIFIEDASN' -%}
        DEFAULTASN={{item.DEFAULTASN}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 设置SGSN/SGW-C的信令地址和ASN映射的本地表项。

```jinja2
{%- for item in add_staticasn_list -%}
    ADD STATICASN:
    {#- --- 必选参数 --- -#}
    SRVNODEIP="{{item.SRVNODEIP}}",
    MASK="{{item.MASK}}",
    ASN={{item.ASN}},
    ;
{%- endfor -%}
```

