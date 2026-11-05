---
id: GWFD-110282
name: 修改被IPFarm绑定的心跳检测接口
ne_type: UDG
type: feature
description: IP Farm绑定的心跳检测接口需要修改。  适用于PGW-U、UPF。
risk_level: ''
doc_source: ["特性部署","特性指南","UDG特性指南","智能策略控制功能","GWFD-110282 Web Proxy","调整Web Proxy参数","修改被IPFarm绑定的心跳检测接口"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
IP Farm绑定的心跳检测接口需要修改。适用于PGW-U、UPF。

## 必备事项
前提条件

* 请仔细阅读GWFD-110282 Web Proxy。
* 完成配置Web Proxy。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
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
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV4ADDRESS1:
          name: '逻辑接口的IPv4地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV4MASK1:
          name: '逻辑接口的IPv4掩码1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV4ADDRESS2:
          name: '逻辑接口的IPv4地址2'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4MASK2:
          name: '逻辑接口的IPv4掩码2'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4MTU:
          name: 'IPv4逻辑接口MTU（字节）'
          type: integer
          minimum: 328
          maximum: 9600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1500
        IPV6ADDRESS1:
          name: '逻辑接口的IPv6地址1'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6ADDRESS2:
          name: '逻辑接口的IPv6地址2'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6MTU:
          name: 'IPv6逻辑接口MTU（字节）'
          type: integer
          minimum: 1280
          maximum: 9600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1800
        IPV6PREFIXLEN1:
          name: 'IPv6前缀长度1'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6PREFIXLEN2:
          name: 'IPv6前缀长度2'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VPNINSTANCE:
          name: 'VPN实例名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    rmv_rule_list:
      type: items
      properties:
        RULENAME:
          name: '规则名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_ipfarm_list:
      type: items
      properties:
        IPFARMNAME:
          name: 'IP-Farm名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '配置的IPFarm名称，已通过**ADD IPFARM**命令配置完成，可以使用**LST IPFARM**命令进行查询。'
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
          data_source: ''
          pattern: ''
          default: ''
        INTERFACENAME:
          name: '心跳检测接口名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '配置的心跳接口名称，已通过**ADD LOGICINF**命令配置完成，可以使用**ADD LOGICINF**命令进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_rule_list:
      type: items
      properties:
        RULENAME:
          name: '规则名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        POLICYTYPE:
          name: '策略类型'
          type: string
          enum:
          - ADC
          - BWM
          - FIREWALL
          - HEADEN
          - IPREDIR
          - LBO
          - PCC
          - QOS
          - REMARK_FPI
          - SMARTREDIRECT
          - SRV_TRIGGER
          - TRAFFICCLASS
          - WEBPROXY
          - WORKER
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FILTERINGMODE:
          name: '流过滤器或流过滤器组选择'
          type: string
          enum:
          - FLOWFILTER
          - FLOWFILTERGRP
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY:
          name: '全局优先级'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 4294967295
        POLICYNAME:
          name: '策略名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FLWFLTRGRPNAME:
          name: '流过滤器组名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ADCMUTEFLAG:
          name: 'ADC静默通知标识'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ENABLE
        ALGSWITCH:
          name: 'ALG功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        RDSTRIGGERFLAG:
          name: 'Radius消息触发标识'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        REDIRIPVERFLAG:
          name: 'IP重定向虚拟IP协议版本'
          type: string
          enum:
          - IPV4
          - IPV6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REMARKFPISEL:
          name: '重标记、FPI或SAI选择'
          type: string
          enum:
          - FPI
          - REMARK
          - REMARKANDFPI
          - SAI
          - REMARKANDSAI
          - FPIANDSAI
          - RMKFPISAI
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: REMARK
        SRVLBOFLAG:
          name: '本地业务分流标识'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        WORKERNAME:
          name: '通用Rule子策略名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        WORKERPARA:
          name: '通用策略参数'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_logicinf_list:
    - NAME: 'phif1/0/1'
      IPVERSION: IPV4
      IPV4ADDRESS1: '10.10.16.16'
      IPV4MASK1: '255.255.255.255'
      IPV4ADDRESS2: ''
      IPV4MASK2: ''
      IPV4MTU: 1500
      IPV6ADDRESS1: ''
      IPV6ADDRESS2: ''
      IPV6MTU: 1800
      IPV6PREFIXLEN1: ''
      IPV6PREFIXLEN2: ''
      VPNINSTANCE: ''
    rmv_rule_list:
    - RULENAME: 'rule_test1'
    mod_ipfarm_list:
    - IPFARMNAME: 'farm_test'
      HEALTHCHECKFLAG: ENABLE
      INTERFACENAME: 'phif1/0/1'
    add_rule_list:
    - RULENAME: 'rule_test1'
      POLICYTYPE: WEBPROXY
      FILTERINGMODE: FLOWFILTER
      FLOWFILTERNAME: 'flow-l34'
      PRIORITY: 10
      POLICYNAME: 'farm_test'
      FLWFLTRGRPNAME: ''
      ADCMUTEFLAG: ENABLE
      ALGSWITCH: DISABLE
      RDSTRIGGERFLAG: DISABLE
      REDIRIPVERFLAG: ''
      REMARKFPISEL: REMARK
      SRVLBOFLAG: DISABLE
      WORKERNAME: ''
      WORKERPARA: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置IPFarm的心跳检测接口。

#### 1.1 //配置IPFarm的心跳检测接口。

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
    {#- --- 条件必选：IPVERSION=IPVER_ALL/IPV6 时必选 --- -#}
    {%- if item.IPVERSION in ['IPVER_ALL', 'IPV6'] -%}
        IPV6ADDRESS1="{{item.IPV6ADDRESS1}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPVER_ALL/IPV6 时必选 --- -#}
    {%- if item.IPVERSION in ['IPVER_ALL', 'IPV6'] -%}
        IPV6PREFIXLEN1={{item.IPV6PREFIXLEN1}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPVERSION=IPV4/IPVER_ALL 时可选 --- -#}
    {%- if item.IPVERSION in ['IPV4', 'IPVER_ALL'] -%}
        {%- if item.IPV4ADDRESS2 is not none -%}
            IPV4ADDRESS2="{{item.IPV4ADDRESS2}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVERSION=IPV4/IPVER_ALL 时可选 --- -#}
    {%- if item.IPVERSION in ['IPV4', 'IPVER_ALL'] -%}
        {%- if item.IPV4MASK2 is not none -%}
            IPV4MASK2="{{item.IPV4MASK2}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVERSION=IPV4/IPVER_ALL 时可选 --- -#}
    {%- if item.IPVERSION in ['IPV4', 'IPVER_ALL'] -%}
        {%- if item.IPV4MTU is not none -%}
            IPV4MTU={{item.IPV4MTU}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVERSION=IPVER_ALL/IPV6 时可选 --- -#}
    {%- if item.IPVERSION in ['IPVER_ALL', 'IPV6'] -%}
        {%- if item.IPV6ADDRESS2 is not none -%}
            IPV6ADDRESS2="{{item.IPV6ADDRESS2}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVERSION=IPVER_ALL/IPV6 时可选 --- -#}
    {%- if item.IPVERSION in ['IPVER_ALL', 'IPV6'] -%}
        {%- if item.IPV6MTU is not none -%}
            IPV6MTU={{item.IPV6MTU}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVERSION=IPVER_ALL/IPV6 时可选 --- -#}
    {%- if item.IPVERSION in ['IPVER_ALL', 'IPV6'] -%}
        {%- if item.IPV6PREFIXLEN2 is not none -%}
            IPV6PREFIXLEN2={{item.IPV6PREFIXLEN2}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVERSION=IPV4/IPVER_ALL/IPV6 时可选 --- -#}
    {%- if item.IPVERSION in ['IPV4', 'IPVER_ALL', 'IPV6'] -%}
        {%- if item.VPNINSTANCE is not none -%}
            VPNINSTANCE="{{item.VPNINSTANCE}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 修改心跳检测接口。

#### 2.1 //修改心跳检测接口。

```jinja2
{%- for item in rmv_rule_list -%}
    RMV RULE:
    {#- --- 必选参数 --- -#}
    RULENAME="{{item.RULENAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in mod_ipfarm_list -%}
    MOD IPFARM:
    {#- --- 必选参数 --- -#}
    IPFARMNAME="{{item.IPFARMNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.HEALTHCHECKFLAG is not none -%}
        HEALTHCHECKFLAG={{item.HEALTHCHECKFLAG}},
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

```jinja2
{%- for item in add_rule_list -%}
    ADD RULE:
    {#- --- 必选参数 --- -#}
    RULENAME="{{item.RULENAME}}",
    POLICYTYPE={{item.POLICYTYPE}},
    FILTERINGMODE={{item.FILTERINGMODE}},
    {#- --- 可选参数 --- -#}
    {%- if item.PRIORITY is not none -%}
        PRIORITY={{item.PRIORITY}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：FILTERINGMODE=FLOWFILTER 时必选 --- -#}
    {%- if item.FILTERINGMODE == 'FLOWFILTER' -%}
        FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
    {%- endif -%}
    {#- --- 条件必选：POLICYTYPE=PCC/BWM/HEADEN/SMARTREDIRECT/TRAFFICCLASS/FIREWALL/QOS/WEBPROXY 时必选 --- -#}
    {%- if item.POLICYTYPE in ['PCC', 'BWM', 'HEADEN', 'SMARTREDIRECT', 'TRAFFICCLASS', 'FIREWALL', 'QOS', 'WEBPROXY'] -%}
        POLICYNAME="{{item.POLICYNAME}}",
    {%- endif -%}
    {#- --- 条件必选：POLICYTYPE=ADC 时必选 --- -#}
    {%- if item.POLICYTYPE == 'ADC' -%}
        ADCMUTEFLAG={{item.ADCMUTEFLAG}},
    {%- endif -%}
    {#- --- 条件必选：FILTERINGMODE=FLOWFILTERGRP 时必选 --- -#}
    {%- if item.FILTERINGMODE == 'FLOWFILTERGRP' -%}
        FLWFLTRGRPNAME="{{item.FLWFLTRGRPNAME}}",
    {%- endif -%}
    {#- --- 条件必选：POLICYTYPE=SRV_TRIGGER 时必选 --- -#}
    {%- if item.POLICYTYPE == 'SRV_TRIGGER' -%}
        RDSTRIGGERFLAG={{item.RDSTRIGGERFLAG}},
    {%- endif -%}
    {#- --- 条件必选：POLICYTYPE=IPREDIR 时必选 --- -#}
    {%- if item.POLICYTYPE == 'IPREDIR' -%}
        REDIRIPVERFLAG={{item.REDIRIPVERFLAG}},
    {%- endif -%}
    {#- --- 条件必选：POLICYTYPE=REMARK_FPI 时必选 --- -#}
    {%- if item.POLICYTYPE == 'REMARK_FPI' -%}
        REMARKFPISEL={{item.REMARKFPISEL}},
    {%- endif -%}
    {#- --- 条件必选：POLICYTYPE=LBO 时必选 --- -#}
    {%- if item.POLICYTYPE == 'LBO' -%}
        SRVLBOFLAG={{item.SRVLBOFLAG}},
    {%- endif -%}
    {#- --- 条件必选：POLICYTYPE=WORKER 时必选 --- -#}
    {%- if item.POLICYTYPE == 'WORKER' -%}
        WORKERNAME="{{item.WORKERNAME}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：POLICYTYPE=WEBPROXY 时可选 --- -#}
    {%- if item.POLICYTYPE == 'WEBPROXY' -%}
        {%- if item.ALGSWITCH is not none -%}
            ALGSWITCH={{item.ALGSWITCH}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：POLICYTYPE=WORKER 时可选 --- -#}
    {%- if item.POLICYTYPE == 'WORKER' -%}
        {%- if item.WORKERPARA is not none -%}
            WORKERPARA="{{item.WORKERPARA}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

