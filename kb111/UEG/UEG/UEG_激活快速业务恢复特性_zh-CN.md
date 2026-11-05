---
id: GWFD-021407
name: 激活快速业务恢复特性
ne_type: UEG
type: feature
description: 当存在PGW-U/UPF与数据网络之间的接口故障场景时，可以激活快速业务恢复特性。激活快速业务恢复特性，需要在PGW-U/UPF侧和PGW-C/SMF侧分别进行配置。PGW-U/UPF侧配置请参考本章节进行操作。请在PGW-C/SMF侧完成配置后，然后在PGW-U/UPF侧进行配置。  适用于PGW-U、UPF。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝S","MEC 特性指南（风筝S）","UEG特性指南","可靠性功能","GWFD-021407 快速业务恢复","激活快速业务恢复特性"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
当存在PGW-U/UPF与数据网络之间的接口故障场景时，可以激活快速业务恢复特性。激活快速业务恢复特性，需要在PGW-U/UPF侧和PGW-C/SMF侧分别进行配置。PGW-U/UPF侧配置请参考本章节进行操作。请在PGW-C/SMF侧完成配置后，然后在PGW-U/UPF侧进行配置。适用于PGW-U、UPF。

## 必备事项
前提条件

* 请仔细阅读GWFD-021407 快速业务恢复特性概述。
* 完成加载license（如果有需求，请联系华为技术支持工程师处理）。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
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
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        SWITCH:
          name: '开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: true
          description: '-'
          data_source: '固定取值'
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
          description: '* 逻辑接口的VPN一定要与其对应的外联口的VPN相同，否则从逻辑接口发出去的报文会查询路由失败。 * VPN必须与探测路径关联的APN的VPN保持一致。'
          data_source: '本端规划'
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
          description: '-'
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
          description: '请根据实际规划配置地址类型。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        VPNINSTANCE:
          name: 'VPN实例名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '已通过**ADD VPNINST**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IPV6ADDRESS1:
          name: '逻辑接口的IPv6地址1'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV6PREFIXLEN1:
          name: 'IPv6前缀长度1'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_detectpath_list:
      type: items
      properties:
        PATHNAME:
          name: '路径名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        LOCALINF:
          name: '本端逻辑接口名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '已通过**ADD LOGICINF**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP地址版本类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: '配置为探测服务器或探测服务器某近端的路由器地址，请根据实际规划配置地址类型。'
          data_source: '全网规划'
          pattern: ''
          default: IPV4
        PEERIPV6:
          name: '对端IPV6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        REDUNDRDTSW:
          name: '探测路径的重定向开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '与静态路由冗余特性叠加使用时，需要开启此开关。  对应的重定向IP已通过**ADD REDUNDRDTIP**进行配置。'
          data_source: '全网规划'
          pattern: ''
          default: DISABLE
        REDUNDRDTIPV6:
          name: '探测路径的重定向IPV6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_apn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '探测路径关联的APN名称。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        HASVPN:
          name: '绑定VPN'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: DISABLE
        VPNINSTANCE:
          name: 'VPN实例名'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '已通过**ADD VPNINST**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_apnbindpath_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '已通过**ADD APN**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DETECTPATH:
          name: '路径名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '与通过**ADD DETECTPATH**命令配置的路径名称保持一致。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    set_apntnlstatusrpt_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '已通过**ADD APN**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SWITCH:
          name: '隧道状态上报开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_rptperiod_list:
      type: items
      properties:
        RPTPERIOD:
          name: 'APN N6故障状态周期上报时长'
          type: integer
          minimum: 0
          maximum: 72
          required: true
          description: '该数值要小于SMF上**SET PFCPPARA**设置的老化时间。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_apnsglpass_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '与静态路由冗余特性叠加使用时，需要基于APN开启单通检测。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SWITCH:
          name: '开关标识'
          type: string
          enum:
          - PF_ACT_DISABLE
          - PF_ACT_ENABLE
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_apnsoftpara_list:
      type: items
      properties:
        APN:
          name: 'APN'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DT:
          name: '软参记录数据类型'
          type: string
          enum:
          - BIT
          - BYTE
          - STRING
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3G5N6FL01'
      SWITCH: ENABLE
    add_vpninst_list:
    - VPNINSTANCE: 'VRF_CN'
    add_logicinf_list:
    - NAME: 'phif1/0/1'
      IPVERSION: IPV6
      VPNINSTANCE: 'VRF_CN'
      IPV6ADDRESS1: 'FC00::4:1'
      IPV6PREFIXLEN1: 128
    add_detectpath_list:
    - PATHNAME: 'testpath1'
      LOCALINF: 'phif1/0/1'
      IPVERSION: IPV6
      PEERIPV6: 'FC00:0:0:0:0:0:0:1'
      REDUNDRDTSW: DISABLE
      REDUNDRDTIPV6: 'fc00:3::1'
    add_apn_list:
    - APN: 'huawei.com'
      HASVPN: ENABLE
      VPNINSTANCE: 'VRF_CN'
    add_apnbindpath_list:
    - APN: 'huawei.com'
      DETECTPATH: 'testpath1'
    set_apntnlstatusrpt_list:
    - APN: 'huawei.com'
      SWITCH: ENABLE
    set_rptperiod_list:
    - RPTPERIOD: 4
    set_apnsglpass_list:
    - APN: 'huawei.com'
      SWITCH: PF_ACT_ENABLE
    set_apnsoftpara_list:
    - APN: ''
      DT: ''
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 开启License开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 2 配置逻辑口的VPN实例。

```jinja2
{%- for item in add_vpninst_list -%}
    ADD VPNINST:
    {#- --- 必选参数 --- -#}
    VPNINSTANCE="{{item.VPNINSTANCE}}",
    ;
{%- endfor -%}
```

### 逻辑接口的VPN一定要与其对应的外联口的VPN相同，否则从逻辑接口发出去的报文会查询路由失败。

### VPN必须与探测路径关联的APN的VPN保持一致。

### 3 配置本端逻辑接口。

```jinja2
{%- for item in add_logicinf_list -%}
    ADD LOGICINF:
    {#- --- 必选参数 --- -#}
    NAME="{{item.NAME}}",
    IPVERSION={{item.IPVERSION}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPVER_ALL/IPV6 时必选 --- -#}
    {%- if item.IPVERSION in ['IPVER_ALL', 'IPV6'] -%}
        IPV6ADDRESS1="{{item.IPV6ADDRESS1}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPVER_ALL/IPV6 时必选 --- -#}
    {%- if item.IPVERSION in ['IPVER_ALL', 'IPV6'] -%}
        IPV6PREFIXLEN1={{item.IPV6PREFIXLEN1}},
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

### 4 配置探测路径。一般建议一个APN下至少配置2条路径。

```jinja2
{%- for item in add_detectpath_list -%}
    ADD DETECTPATH:
    {#- --- 必选参数 --- -#}
    PATHNAME="{{item.PATHNAME}}",
    LOCALINF="{{item.LOCALINF}}",
    IPVERSION={{item.IPVERSION}},
    {#- --- 可选参数 --- -#}
    {%- if item.REDUNDRDTSW is not none -%}
        REDUNDRDTSW={{item.REDUNDRDTSW}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPV6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV6' -%}
        PEERIPV6="{{item.PEERIPV6}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：REDUNDRDTSW=ENABLE 时可选 --- -#}
    {%- if item.REDUNDRDTSW == 'ENABLE' -%}
        {%- if item.REDUNDRDTIPV6 is not none -%}
            REDUNDRDTIPV6="{{item.REDUNDRDTIPV6}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 配置DNN/APN实例。

```jinja2
{%- for item in add_apn_list -%}
    ADD APN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.HASVPN is not none -%}
        HASVPN={{item.HASVPN}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：HASVPN=ENABLE 时必选 --- -#}
    {%- if item.HASVPN == 'ENABLE' -%}
        VPNINSTANCE="{{item.VPNINSTANCE}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 6 配置DNN/APN与探测路径的关联关系。

```jinja2
{%- for item in add_apnbindpath_list -%}
    ADD APNBINDPATH:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    DETECTPATH="{{item.DETECTPATH}}",
    ;
{%- endfor -%}
```

### 7 使能PGW-U/UPF与数据网络间基于DNN/APN粒度的隧道链路状态上报功能。

```jinja2
{%- for item in set_apntnlstatusrpt_list -%}
    SET APNTNLSTATUSRPT:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 8 设置APN N6故障状态上报SMF周期。

```jinja2
{%- for item in set_rptperiod_list -%}
    SET RPTPERIOD:
    {#- --- 必选参数 --- -#}
    RPTPERIOD={{item.RPTPERIOD}},
    ;
{%- endfor -%}
```

### 9 与静态路由冗余特性叠加使用时，需要使能单通检测功能。

```jinja2
{%- for item in set_apnsglpass_list -%}
    SET APNSGLPASS:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

```jinja2
{%- for item in set_apnsoftpara_list -%}
    SET APNSOFTPARA:
    {#- --- 必选参数 --- -#}
    DT={{item.DT}},
    APN="{{item.APN}}",
    ;
{%- endfor -%}
```

