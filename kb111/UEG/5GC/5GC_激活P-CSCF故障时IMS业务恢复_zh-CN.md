---
id: ''
name: 激活P-CSCF故障时IMS业务恢复
ne_type: UEG
type: feature
description: 在UEG上激活P-CSCF故障时IMS业务恢复功能，降低P-CSCF服务器故障时对用户业务的影响。  适用于PGW-U、UPF。
tags: []
risk_level: ''
doc_source:
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网煤矿场景，入驻式）","配置基础业务","在UEG上配置业务数据","语音功能配置","GW-U&UPF配置","激活P-CSCF故障时IMS业务恢复"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网核电场景，入驻式）","配置基础业务","在UEG上配置业务数据","语音功能配置","GW-U&UPF配置","激活P-CSCF故障时IMS业务恢复"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网通用场景，入驻式）","配置基础业务","在UEG上配置业务数据","语音功能配置","GW-U&UPF配置","激活P-CSCF故障时IMS业务恢复"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
在UEG上激活P-CSCF故障时IMS业务恢复功能，降低P-CSCF服务器故障时对用户业务的影响。适用于PGW-U、UPF。

## 必备事项
前提条件

* 请仔细阅读GWFD-025501 P-CSCF故障时IMS业务恢复。
* 完成配置VoLTE基础语音业务。
* 完成**加载license**（如果有需求，请联系华为技术支持工程师处理）。
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
    set_ipfarmglobal_list:
      type: items
      properties:
        SERVERTYPE:
          name: '服务器类型'
          type: string
          enum:
          - IPMS
          - PCSCF
          - REDIRECT
          required: true
          description: '配置IP Farm心跳检测功能的相关参数'
          data_source: '本端规划'
          pattern: ''
          default: ''
        HEALTHSUCCLIMIT:
          name: '健康检查成功次数'
          type: integer
          minimum: 1
          maximum: 10
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        HEALTHFAILLIMIT:
          name: '健康检查失败次数'
          type: integer
          minimum: 1
          maximum: 10
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        TIMETHRESHOLD:
          name: '时间阈值'
          type: integer
          minimum: 6
          maximum: 60
          required: false
          description: ''
          data_source: '本端规划'
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
          description: 'IP Farm需要绑定的VPN'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_logicinf_list:
      type: items
      properties:
        NAME:
          name: '逻辑接口名称'
          type: string
          maxLength: 63
          required: true
          description: '配置逻辑接口'
          data_source: '全网规划'
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
          description: ''
          data_source: '全网规划'
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
        VPNINSTANCE:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
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
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_ipfarm_list:
      type: items
      properties:
        IPFARMNAME:
          name: 'IP-Farm名称'
          type: string
          maxLength: 31
          required: true
          description: 'IP-Farm1参数'
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
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SERVERTYPE:
          name: '服务器类型'
          type: string
          enum:
          - IPMS
          - PCSCF
          - REDIRECT
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: REDIRECT
        VPNINSTANCE:
          name: 'VPN实例'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        HEALTHCHECKFLAG:
          name: '健康检查标记'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ENABLE
        VIRTUALIP:
          name: '虚拟IP地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        INTERFACENAME:
          name: '心跳检测接口名称'
          type: string
          maxLength: 31
          required: false
          description: '已通过命令**ADD LOGICINF**进行配置，可以使用命令**LST LOGICINF**查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_ipfarmserver_list:
      type: items
      properties:
        IPFARMNAME:
          name: 'IP-Farm名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP协议版本'
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
          name: '服务器IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: 'IP-Farm1参数'
          data_source: '全网规划'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3G5IMSR01'
      SWITCH: ENABLE
    set_ipfarmglobal_list:
    - SERVERTYPE: PCSCF
      HEALTHSUCCLIMIT: 4
      HEALTHFAILLIMIT: 4
      TIMETHRESHOLD: 6
    add_vpninst_list:
    - VPNINSTANCE: 'ims_vpn'
    add_logicinf_list:
    - NAME: 'phif1/0/0'
      IPVERSION: IPV4
      IPV4ADDRESS1: '192.168.6.6'
      VPNINSTANCE: 'ims_vpn'
      IPV4MASK1: '255.255.255.255'
    add_ipfarm_list:
    - IPFARMNAME: 'farm_test'
      IPVERSION: IPV4
      SERVERTYPE: PCSCF
      VPNINSTANCE: 'ims_vpn'
      HEALTHCHECKFLAG: ENABLE
      VIRTUALIP: '10.1.1.1'
      INTERFACENAME: 'phif1/0/0'
    add_ipfarmserver_list:
    - IPFARMNAME: 'farm_test'
      IPVERSION: IPV4
      SERVERIPV4: '192.168.253.251'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 打开本特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 2 配置IP-Farm参数。

#### 2.1 **可选：**配置整机的IP Farm心跳检测功能的相关参数。

```jinja2
{%- if is_optional_ip_farm_heartbeat_params -%}
    {%- for item in set_ipfarmglobal_list -%}
        SET IPFARMGLOBAL:
        {#- --- 必选参数 --- -#}
        SERVERTYPE={{item.SERVERTYPE}},
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：SERVERTYPE=REDIRECT/IPMS/PCSCF 时可选 --- -#}
        {%- if item.SERVERTYPE in ['REDIRECT', 'IPMS', 'PCSCF'] -%}
            {%- if item.HEALTHSUCCLIMIT is not none -%}
                HEALTHSUCCLIMIT={{item.HEALTHSUCCLIMIT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SERVERTYPE=REDIRECT/IPMS/PCSCF 时可选 --- -#}
        {%- if item.SERVERTYPE in ['REDIRECT', 'IPMS', 'PCSCF'] -%}
            {%- if item.HEALTHFAILLIMIT is not none -%}
                HEALTHFAILLIMIT={{item.HEALTHFAILLIMIT}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SERVERTYPE=REDIRECT/IPMS/PCSCF 时可选 --- -#}
        {%- if item.SERVERTYPE in ['REDIRECT', 'IPMS', 'PCSCF'] -%}
            {%- if item.TIMETHRESHOLD is not none -%}
                TIMETHRESHOLD={{item.TIMETHRESHOLD}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 如果运营商没有特殊要求，建议保持默认值。

#### 2.2 配置VPN。

```jinja2
{%- for item in add_vpninst_list -%}
    ADD VPNINST:
    {#- --- 必选参数 --- -#}
    VPNINSTANCE="{{item.VPNINSTANCE}}",
    ;
{%- endfor -%}
```

#### 如果运营商规划该IP Farm在指定VPN网络中，则需要对该IP Farm绑定相应的VPN。

#### 2.3 配置逻辑接口。

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
    {#- --- 条件可选：IPVERSION=IPV4/IPV6/IPVER_ALL 时可选 --- -#}
    {%- if item.IPVERSION in ['IPV4', 'IPV6', 'IPVER_ALL'] -%}
        {%- if item.VPNINSTANCE is not none -%}
            VPNINSTANCE="{{item.VPNINSTANCE}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.4 创建IP Farm实例，配置IP Farm对应的虚拟IP地址，使能IP Farm心跳检测功能。

```jinja2
{%- for item in add_ipfarm_list -%}
    ADD IPFARM:
    {#- --- 必选参数 --- -#}
    IPFARMNAME="{{item.IPFARMNAME}}",
    IPVERSION={{item.IPVERSION}},
    {#- --- 可选参数 --- -#}
    {%- if item.SERVERTYPE is not none -%}
        SERVERTYPE={{item.SERVERTYPE}},
    {%- endif -%}
    {%- if item.VPNINSTANCE is not none -%}
        VPNINSTANCE="{{item.VPNINSTANCE}}",
    {%- endif -%}
    {%- if item.HEALTHCHECKFLAG is not none -%}
        HEALTHCHECKFLAG={{item.HEALTHCHECKFLAG}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPVERSION=IPV4 时可选 --- -#}
    {%- if item.IPVERSION == 'IPV4' -%}
        {%- if item.VIRTUALIP is not none -%}
            VIRTUALIP="{{item.VIRTUALIP}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件必选/可选参数 --- -#}
    {#- --- 心跳检测接口名称: 条件必选(健康检查标记=ENABLE) / 条件可选(健康检查标记=DISABLE) --- -#}
    {%- if (item.HEALTHCHECKFLAG == 'ENABLE') -%}
        INTERFACENAME="{{item.INTERFACENAME}}",
    {%- elif (item.HEALTHCHECKFLAG == 'DISABLE') -%}
        {%- if item.INTERFACENAME is not none -%}
            INTERFACENAME="{{item.INTERFACENAME}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.5 在IP Farm中加入P-CSCF服务器地址。

```jinja2
{%- for item in add_ipfarmserver_list -%}
    ADD IPFARMSERVER:
    {#- --- 必选参数 --- -#}
    IPFARMNAME="{{item.IPFARMNAME}}",
    IPVERSION={{item.IPVERSION}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV4' -%}
        SERVERIPV4="{{item.SERVERIPV4}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### IP Farm配置完成后，可以执行命令**DSP IPFARMSERVER**查询IP Farm中server的状态。为确保业务正常进行，需保证至少有一个server的状态为up。

