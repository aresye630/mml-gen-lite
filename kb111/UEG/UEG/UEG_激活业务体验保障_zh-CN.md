---
id: GWFD-030202
name: 激活业务体验保障
ne_type: UEG
type: feature
description: 适用于PGW-U、UPF。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝S","MEC 特性指南（风筝S）","UEG特性指南","本地分流功能","GWFD-030202 业务体验保障","激活业务体验保障"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
适用于PGW-U、UPF。

## 必备事项
前提条件

* 请仔细阅读GWFD-030202 业务体验保障特性概述。
* UEG完成与周边网元的对接。
* 完成**加载license**（如果有需求，请联系华为技术支持工程师处理）
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_bwmcontroller_list:
      type: items
      properties:
        BWMCNAME:
          name: '带宽管理控制器名称'
          type: string
          maxLength: 31
          required: true
          description: '推荐配置：  * CIR = 0.5 * PIR （最大带宽建议为保证带宽的2倍） * CBS >=CIR * 1.5 * 1000 / 8 （保证1.5秒数据的队列缓存能力） * PBS >= PIR * 1.5 * 1000 / 8 （保证1.5秒数据的队列缓存能力）'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CTRLTYPE:
          name: '带宽管理控制类型'
          type: string
          enum:
          - CAR
          - SHAPING
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        CIR:
          name: '承诺信息速率（千比特/秒）'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        CBS:
          name: '承诺突发能缓存信息的数量（字节）'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PIR:
          name: '峰值信息速率（千比特/秒）'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PBS:
          name: '峰值突发能缓存信息的数量（字节）'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        GREEN:
          name: '绿色'
          type: string
          enum:
          - DISCARD
          - PASS
          - REMARK
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: PASS
        YELLOW:
          name: '黄色'
          type: string
          enum:
          - DISCARD
          - PASS
          - REMARK
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: PASS
        RED:
          name: '红色'
          type: string
          enum:
          - DISCARD
          - PASS
          - REMARK
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: PASS
        PRIORITYISAWARE:
          name: 'BWM CAR优先级是否敏感'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
    set_bandwidthmng_list:
      type: items
      properties:
        RANGE:
          name: '带宽管理生效范围'
          type: string
          enum:
          - CPU
          - SYSTEM
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        CIRMINTHRES:
          name: '承诺信息速率最低保护值（千比特每秒）'
          type: integer
          minimum: 0
          maximum: 629145600
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PIRMINTHRES:
          name: '峰值信息速率最低保护值（千比特每秒）'
          type: integer
          minimum: 0
          maximum: 629145600
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_bwmusergroup_list:
      type: items
      properties:
        USERGROUPTYPE:
          name: '用户组类型'
          type: string
          enum:
          - DEFAULT_GROUP
          - SPECIFIC_GROUP
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        USERGROUPNAME:
          name: '用户组名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        USERGROUPPRI:
          name: '用户组优先级'
          type: integer
          minimum: 1
          maximum: 32768
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        USERLEVSRVTYPE:
          name: '用户级业务类型'
          type: string
          enum:
          - NONTOS
          - TOS
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: TOS
        USERGLEVSRVTYPE:
          name: '用户组级业务类型'
          type: string
          enum:
          - NONTOS
          - TOS
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: TOS
    add_bwmrule_list:
      type: items
      properties:
        USERGROUPTYPE:
          name: '用户组类型'
          type: string
          enum:
          - DEFAULT_GROUP
          - SPECIFIC_GROUP
          required: true
          description: 'BwmController已通过  **ADD BWMCONTROLLER**命令配置。  说明：  该带宽管理功能不区分用户的业务类型，无需和BWM Service关联。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        USERGROUPNAME:
          name: '用户组名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        BWMRULETYPE:
          name: '带宽管理规则类型'
          type: string
          enum:
          - GROUP_DEFAULT
          - GROUP_SPECIFIC
          - SUBSCRIBER_DEFAULT
          - SUBSCRIBER_SPECIFIC
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPBWMCTRLNAME1:
          name: '上行带宽管理控制器名称一'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DNBWMCTRLNAME1:
          name: '下行带宽管理控制器名称一'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_snssai_list:
      type: items
      properties:
        SST:
          name: '切片/服务类型'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: '业务体验保障使用的切片。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SD:
          name: '切片区分码'
          type: string
          minLength: 6
          maxLength: 6
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_snssaibwmusrg_list:
      type: items
      properties:
        USERGROUPNAME:
          name: '用户组名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '切片绑定的带宽用户组名称，已经通过**ADD BWMUSERGROUP**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SST:
          name: '切片/服务类型'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: '已经通过**ADD SNSSAI**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SD:
          name: '切片区分码'
          type: string
          minLength: 0
          maxLength: 6
          required: false
          description: ''
          data_source: '已配置数据中获取'
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
          description: 'N3逻辑接口使用的VPN实例。'
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
          description: ''
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
        VPNINSTANCE:
          name: 'VPN实例名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '使用的VPN实例已经通过**ADD VPNINST**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_snssaiupintf_list:
      type: items
      properties:
        SST:
          name: '切片/服务类型'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: '使用的切片已经通过**ADD SNSSAI**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SD:
          name: '切片区分码'
          type: string
          minLength: 0
          maxLength: 6
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        N3LOGICINF:
          name: 'N3逻辑接口名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '使用的N3逻辑接口已经通过**ADD LOGICINF**命令配置。'
          data_source: '已配置数据中获取'
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
          description: '配置业务体验保障使用的APN/DNN。'
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
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
        HASVPNIPV6:
          name: '绑定IPv6 VPN'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
    add_apnbindbwmusrg_list:
      type: items
      properties:
        USERGROUPNAME:
          name: '用户组名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '已经通过**ADD BWMUSERGROUP**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '已经通过**ADD APN**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
  examples:
    add_bwmcontroller_list:
    - BWMCNAME: 'bwm_ctrl'
      CTRLTYPE: CAR
      CIR: 2000000
      CBS: 320000000
      PIR: 4000000
      PBS: 800000000
      GREEN: PASS
      YELLOW: PASS
      RED: DISCARD
      PRIORITYISAWARE: DISABLE
    set_bandwidthmng_list:
    - RANGE: SYSTEM
      CIRMINTHRES: 300000
      PIRMINTHRES: 500000
    add_bwmusergroup_list:
    - USERGROUPTYPE: SPECIFIC_GROUP
      USERGROUPNAME: 'ug_test'
      USERGROUPPRI: 1
      USERLEVSRVTYPE: NONTOS
      USERGLEVSRVTYPE: NONTOS
    add_bwmrule_list:
    - USERGROUPTYPE: SPECIFIC_GROUP
      USERGROUPNAME: 'ug_test'
      BWMRULETYPE: GROUP_DEFAULT
      UPBWMCTRLNAME1: 'bwm_ctrl'
      DNBWMCTRLNAME1: 'bwm_ctrl'
    add_snssai_list:
    - SST: 10
      SD: '123456'
    add_snssaibwmusrg_list:
    - USERGROUPNAME: 'ug_test'
      SST: 10
      SD: '123456'
    add_vpninst_list:
    - VPNINSTANCE: 'vpn_bwm'
    add_logicinf_list:
    - NAME: 'n3if1/1/1'
      IPVERSION: IPV4
      IPV4ADDRESS1: '192.168.1.1'
      IPV4MASK1: '255.255.255.255'
      VPNINSTANCE: 'vpn_bwm'
    add_snssaiupintf_list:
    - SST: 10
      SD: '123456'
      N3LOGICINF: 'n3if1/1/1'
    add_apn_list:
    - APN: 'apn-test'
      HASVPN: DISABLE
      HASVPNIPV6: DISABLE
    add_apnbindbwmusrg_list:
    - USERGROUPNAME: 'ug_test'
      APN: 'apn-test'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 配置业务体验保障使用的带宽管理业务。

#### 1.1 配置带宽管理控制器。

```jinja2
{%- for item in add_bwmcontroller_list -%}
    ADD BWMCONTROLLER:
    {#- --- 必选参数 --- -#}
    BWMCNAME="{{item.BWMCNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.CTRLTYPE is not none -%}
        CTRLTYPE={{item.CTRLTYPE}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：CTRLTYPE=CAR 时必选 --- -#}
    {%- if item.CTRLTYPE == 'CAR' -%}
        CIR={{item.CIR}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：CTRLTYPE=CAR 时可选 --- -#}
    {%- if item.CTRLTYPE == 'CAR' -%}
        {%- if item.CBS is not none -%}
            CBS={{item.CBS}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CTRLTYPE=CAR 时可选 --- -#}
    {%- if item.CTRLTYPE == 'CAR' -%}
        {%- if item.PIR is not none -%}
            PIR={{item.PIR}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CTRLTYPE=CAR 时可选 --- -#}
    {%- if item.CTRLTYPE == 'CAR' -%}
        {%- if item.PBS is not none -%}
            PBS={{item.PBS}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CTRLTYPE=CAR 时可选 --- -#}
    {%- if item.CTRLTYPE == 'CAR' -%}
        {%- if item.GREEN is not none -%}
            GREEN={{item.GREEN}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CTRLTYPE=CAR 时可选 --- -#}
    {%- if item.CTRLTYPE == 'CAR' -%}
        {%- if item.YELLOW is not none -%}
            YELLOW={{item.YELLOW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CTRLTYPE=CAR 时可选 --- -#}
    {%- if item.CTRLTYPE == 'CAR' -%}
        {%- if item.RED is not none -%}
            RED={{item.RED}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CTRLTYPE=CAR 时可选 --- -#}
    {%- if item.CTRLTYPE == 'CAR' -%}
        {%- if item.PRIORITYISAWARE is not none -%}
            PRIORITYISAWARE={{item.PRIORITYISAWARE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.2 配置BWM控制器中的用户组级业务带宽配置数据基于整机生效。

```jinja2
{%- for item in set_bandwidthmng_list -%}
    SET BANDWIDTHMNG:
    {#- --- 可选参数 --- -#}
    {%- if item.RANGE is not none -%}
        RANGE={{item.RANGE}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：RANGE=SYSTEM 时可选 --- -#}
    {%- if item.RANGE == 'SYSTEM' -%}
        {%- if item.CIRMINTHRES is not none -%}
            CIRMINTHRES={{item.CIRMINTHRES}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：RANGE=SYSTEM 时可选 --- -#}
    {%- if item.RANGE == 'SYSTEM' -%}
        {%- if item.PIRMINTHRES is not none -%}
            PIRMINTHRES={{item.PIRMINTHRES}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.3 定义带宽管理用户组，配置优先级和业务类型。

```jinja2
{%- for item in add_bwmusergroup_list -%}
    ADD BWMUSERGROUP:
    {#- --- 必选参数 --- -#}
    USERGROUPTYPE={{item.USERGROUPTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.USERLEVSRVTYPE is not none -%}
        USERLEVSRVTYPE={{item.USERLEVSRVTYPE}},
    {%- endif -%}
    {%- if item.USERGLEVSRVTYPE is not none -%}
        USERGLEVSRVTYPE={{item.USERGLEVSRVTYPE}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：USERGROUPTYPE=SPECIFIC_GROUP 时必选 --- -#}
    {%- if item.USERGROUPTYPE == 'SPECIFIC_GROUP' -%}
        USERGROUPNAME="{{item.USERGROUPNAME}}",
    {%- endif -%}
    {#- --- 条件必选：USERGROUPTYPE=SPECIFIC_GROUP 时必选 --- -#}
    {%- if item.USERGROUPTYPE == 'SPECIFIC_GROUP' -%}
        USERGROUPPRI={{item.USERGROUPPRI}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.4 配置一条用户组级带宽控制规则。

```jinja2
{%- for item in add_bwmrule_list -%}
    ADD BWMRULE:
    {#- --- 必选参数 --- -#}
    USERGROUPTYPE={{item.USERGROUPTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：USERGROUPTYPE=SPECIFIC_GROUP 时必选 --- -#}
    {%- if item.USERGROUPTYPE == 'SPECIFIC_GROUP' -%}
        USERGROUPNAME="{{item.USERGROUPNAME}}",
    {%- endif -%}
    {#- --- 条件必选：USERGROUPTYPE=DEFAULT_GROUP/SPECIFIC_GROUP 时必选 --- -#}
    {%- if item.USERGROUPTYPE in ['DEFAULT_GROUP', 'SPECIFIC_GROUP'] -%}
        BWMRULETYPE={{item.BWMRULETYPE}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：BWMRULETYPE=GROUP_DEFAULT/SUBSCRIBER_DEFAULT/GROUP_SPECIFIC/SUBSCRIBER_SPECIFIC 时可选 --- -#}
    {%- if item.BWMRULETYPE in ['GROUP_DEFAULT', 'SUBSCRIBER_DEFAULT', 'GROUP_SPECIFIC', 'SUBSCRIBER_SPECIFIC'] -%}
        {%- if item.UPBWMCTRLNAME1 is not none -%}
            UPBWMCTRLNAME1="{{item.UPBWMCTRLNAME1}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：BWMRULETYPE=GROUP_DEFAULT/SUBSCRIBER_DEFAULT/GROUP_SPECIFIC/SUBSCRIBER_SPECIFIC 时可选 --- -#}
    {%- if item.BWMRULETYPE in ['GROUP_DEFAULT', 'SUBSCRIBER_DEFAULT', 'GROUP_SPECIFIC', 'SUBSCRIBER_SPECIFIC'] -%}
        {%- if item.DNBWMCTRLNAME1 is not none -%}
            DNBWMCTRLNAME1="{{item.DNBWMCTRLNAME1}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 配置基于切片的带宽控制。

#### 2.1 配置UPF网络切片选择标识。

```jinja2
{%- for item in add_snssai_list -%}
    ADD SNSSAI:
    {#- --- 必选参数 --- -#}
    SST={{item.SST}},
    {#- --- 可选参数 --- -#}
    {%- if item.SD is not none -%}
        SD="{{item.SD}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.2 将切片与带宽管理用户组绑定。

```jinja2
{%- for item in add_snssaibwmusrg_list -%}
    ADD SNSSAIBWMUSRG:
    {#- --- 必选参数 --- -#}
    USERGROUPNAME="{{item.USERGROUPNAME}}",
    SST={{item.SST}},
    {#- --- 可选参数 --- -#}
    {%- if item.SD is not none -%}
        SD="{{item.SD}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.3 **（可选）**配置N3接口。

```jinja2
{%- if is_optional_n3_interface -%}
    {%- for item in add_vpninst_list -%}
        ADD VPNINST:
        {#- --- 必选参数 --- -#}
        VPNINSTANCE="{{item.VPNINSTANCE}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_optional_n3_interface -%}
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
        {#- --- 条件可选：IPVERSION=IPV4/IPVER_ALL/IPV6 时可选 --- -#}
        {%- if item.IPVERSION in ['IPV4', 'IPVER_ALL', 'IPV6'] -%}
            {%- if item.VPNINSTANCE is not none -%}
                VPNINSTANCE="{{item.VPNINSTANCE}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 可以基于实际需求，考虑利用UEG已经配置好的N3接口。这种情况下此步骤可跳过。

#### 2.4 将切片与N3接口绑定。

```jinja2
{%- for item in add_snssaiupintf_list -%}
    ADD SNSSAIUPINTF:
    {#- --- 必选参数 --- -#}
    SST={{item.SST}},
    N3LOGICINF="{{item.N3LOGICINF}}",
    {#- --- 可选参数 --- -#}
    {%- if item.SD is not none -%}
        SD="{{item.SD}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置基于DNN的带宽控制。

#### 3.1 配置APN/DNN。

```jinja2
{%- for item in add_apn_list -%}
    ADD APN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.HASVPN is not none -%}
        HASVPN={{item.HASVPN}},
    {%- endif -%}
    {%- if item.HASVPNIPV6 is not none -%}
        HASVPNIPV6={{item.HASVPNIPV6}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 3.2 将APN/DNN下的用户包含到带宽管理业务中。

```jinja2
{%- for item in add_apnbindbwmusrg_list -%}
    ADD APNBINDBWMUSRG:
    {#- --- 必选参数 --- -#}
    USERGROUPNAME="{{item.USERGROUPNAME}}",
    APN="{{item.APN}}",
    ;
{%- endfor -%}
```

