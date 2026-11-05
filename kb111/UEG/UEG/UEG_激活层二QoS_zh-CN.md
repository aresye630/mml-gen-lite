---
id: GWFD-031101
name: 激活层二QoS
ne_type: UEG
type: feature
description: 当运营商期望根据UEG本地配置的层二规则和QoS参数为指定5G LAN业务提供专有QoS Flow时，需要参考本页面进行配置。  适用于SMF。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","GW-C&SMF特性指南","GWFD-031101 支持层二QoS","激活层二QoS"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
当运营商期望根据UEG本地配置的层二规则和QoS参数为指定5G LAN业务提供专有QoS Flow时，需要参考本页面进行配置。适用于SMF。

## 必备事项
前提条件

* 请仔细阅读GWFD-031101 支持层二QoS特性概述。
* 完成加载License（如果有需求，请联系华为技术支持工程师）。
* 完成配置APN**ADD CPAPN**。
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
          name: 'LICITEM'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: '配置License配置开关'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SWITCH:
          name: 'SWITCH'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_imsimsisdnseg_list:
      type: items
      properties:
        SEGMENTNAME:
          name: 'IMSI/MSISDN号段名称'
          type: string
          maxLength: 31
          required: true
          description: '配置IMSI号码段。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SEGMENTTYPE:
          name: 'IMSI/MSISDN号段类型'
          type: string
          enum:
          - IMSI
          - IMSIWILDCARD
          - MSISDN
          - MSISDNWILDCARD
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SEGSTART:
          name: '号段起始字符串'
          type: string
          maxLength: 17
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SEGEND:
          name: '号段结束字符串'
          type: string
          maxLength: 17
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_cpqosprop_list:
      type: items
      properties:
        QOSPROPNAME:
          name: 'QoS属性名称'
          type: string
          maxLength: 31
          required: true
          description: '存在多条记录时，不能重复。  以5G LAN用户使用的QoS属性名称qosprop\_501\_L2为例。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        EMPCAP:
          name: 'QoS抢占能力'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '该业务可以抢占已经分配给其他低优先级业务流的资源时，设置为ENABLE。此处以不抢占为例。'
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
        EMPVUL:
          name: 'QoS被抢占设置'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '其他高优先级业务不能抢占本业务流的资源时，设置为DISABLE。此处以被抢占为例。'
          data_source: '本端规划'
          pattern: ''
          default: ENABLE
        GBRUPLKVALUE:
          name: '保证的上行比特率'
          type: integer
          minimum: 0
          maximum: 20000000
          required: false
          description: '此处数据仅为举例，请根据业务模型进行规划。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        GBRDNLKVALUE:
          name: '保证的下行比特率'
          type: integer
          minimum: 0
          maximum: 20000000
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        MBRUPLKVALUE:
          name: '最大上行比特率'
          type: integer
          minimum: 0
          maximum: 20000000
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        MBRDNLKVALUE:
          name: '最大下行比特率'
          type: integer
          minimum: 0
          maximum: 20000000
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        QOSTYPE:
          name: 'QoS属性类型'
          type: string
          enum:
          - QOS_BEARER_PARA
          - QOS_FLOW_PARA
          - QOS_L2_PARA
          required: true
          description: '层二QoS使用QOS\_L2\_PARA。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ARPVALUE:
          name: '分配保留优先级'
          type: integer
          minimum: 1
          maximum: 15
          required: false
          description: '该参数值越高优先级越低。  “QOSTYPE”为“QOS\_L2\_PARA”时需要规划。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        FQI:
          name: '5G QoS标识'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: '“QOSTYPE”为“QOS\_L2\_PARA”时需要规划。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_l2filter_list:
      type: items
      properties:
        FILTERNAME:
          name: '层二过滤器名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SRCMACADDR:
          name: '源MAC地址'
          type: string
          minLength: 0
          maxLength: 14
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        DESTMACADDR:
          name: '目的MAC地址'
          type: string
          minLength: 0
          maxLength: 14
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        VID:
          name: 'VLAN标识符'
          type: integer
          minimum: 0
          maximum: 4096
          required: false
          description: '此处数据仅为举例，具体需以现网调研情况为准。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PCP:
          name: '优先级编码点'
          type: integer
          minimum: 0
          maximum: 8
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        DEI:
          name: '丢弃指示器'
          type: string
          enum:
          - ALL
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ETHERTYPE:
          name: '以太类型'
          type: string
          enum:
          - ALL
          - IPv4
          - IPv6
          - ARP
          - PROFINET
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_l2rule_list:
      type: items
      properties:
        L2RULENAME:
          name: '层二规则名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        QOSPROPNAME:
          name: 'QoS属性名称'
          type: string
          minLength: 1
          maxLength: 31
          required: true
          description: '该参数使用**ADD CPQOSPROP**命令配置生成的QOSPROPNAME，且该**ADD CPQOSPROP**定义的“QOSTYPE”必须为“QOS\_L2\_PARA”。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        L2FILTERNAME:
          name: '层二过滤器名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '该参数使用**ADD L2FILTER**命令配置生成的FILTERNAME。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_l2rulegroup_list:
      type: items
      properties:
        L2RULEGROUPNAME:
          name: '层二规则组名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '配置层二规则组名称。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_l2rulebindgrp_list:
      type: items
      properties:
        L2RULEGROUPNAME:
          name: '层二规则组名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '该参数使用**ADD L2RULEGROUP**命令配置生成的L2RULEGROUPNAME。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        L2RULENAME:
          name: '层二规则名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '该参数使用**ADD L2RULE**命令配置生成的L2RULENAME。  同一个**ADD L2RULEGROUP**下最多可绑定16个**ADD L2RULE**。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_l2rulegrpbind_list:
      type: items
      properties:
        GRPBINDNAME:
          name: '层二规则组绑定名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SEGMENTNAME:
          name: 'IMSI号段名称'
          type: string
          minLength: 1
          maxLength: 31
          required: true
          description: '该参数使用**ADD IMSIMSISDNSEG**命令配置生成的SEGMENTNAME，且该**ADD IMSIMSISDNSEG**定义的“SEGMENTTYPE”必须为“IMSI”或“IMSIWILDCARD”。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '该参数使用**ADD CPAPN**命令配置生成的APN。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SST:
          name: '切片业务类型'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SD:
          name: '切片细分标识'
          type: string
          minLength: 0
          maxLength: 6
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        L2RULEGRPNAME:
          name: '层二规则组名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '该参数使用**ADD L2RULEGROUP**命令配置生成的L2RULEGROUPNAME。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV2LAYER2SM01'
      SWITCH: ENABLE
    add_imsimsisdnseg_list:
    - SEGMENTNAME: 'imsi1'
      SEGMENTTYPE: IMSI
      SEGSTART: '189000000000000'
      SEGEND: '189499999999999'
    add_cpqosprop_list:
    - QOSPROPNAME: 'qosprop_501_L2'
      EMPCAP: DISABLE
      EMPVUL: ENABLE
      GBRUPLKVALUE: 600
      GBRDNLKVALUE: 6000
      MBRUPLKVALUE: 1000
      MBRDNLKVALUE: 10000
      QOSTYPE: QOS_L2_PARA
      ARPVALUE: 5
      FQI: 2
    add_l2filter_list:
    - FILTERNAME: 'filter1'
      SRCMACADDR: '00E0-FC12-3456'
      DESTMACADDR: '00E0-FC12-3457'
      VID: 1
      PCP: 1
      DEI: ENABLE
      ETHERTYPE: PROFINET
    add_l2rule_list:
    - L2RULENAME: 'rule1'
      QOSPROPNAME: 'qosprop_501_L2'
      L2FILTERNAME: 'filter1'
    add_l2rulegroup_list:
    - L2RULEGROUPNAME: 'rulegrp1'
    add_l2rulebindgrp_list:
    - L2RULEGROUPNAME: 'rulegrp1'
      L2RULENAME: 'rule1'
    add_l2rulegrpbind_list:
    - GRPBINDNAME: 'bind1'
      SEGMENTNAME: 'imsi1'
      APN: 'huawei.com'
      SST: 1
      SD: '010101'
      L2RULEGRPNAME: 'rulegrp1'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 打开本特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 3 配置IMSI号码段。

```jinja2
{%- for item in add_imsimsisdnseg_list -%}
    ADD IMSIMSISDNSEG:
    {#- --- 必选参数 --- -#}
    SEGMENTNAME="{{item.SEGMENTNAME}}",
    SEGMENTTYPE={{item.SEGMENTTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：SEGMENTTYPE=IMSI/MSISDN 时必选 --- -#}
    {%- if item.SEGMENTTYPE in ['IMSI', 'MSISDN'] -%}
        SEGSTART="{{item.SEGSTART}}",
    {%- endif -%}
    {#- --- 条件必选：SEGMENTTYPE=IMSI/MSISDN 时必选 --- -#}
    {%- if item.SEGMENTTYPE in ['IMSI', 'MSISDN'] -%}
        SEGEND="{{item.SEGEND}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 配置QoS属性，“QOSTYPE”设置为“QOS\_L2\_PARA”。

```jinja2
{%- for item in add_cpqosprop_list -%}
    ADD CPQOSPROP:
    {#- --- 必选参数 --- -#}
    QOSPROPNAME="{{item.QOSPROPNAME}}",
    QOSTYPE={{item.QOSTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.EMPCAP is not none -%}
        EMPCAP={{item.EMPCAP}},
    {%- endif -%}
    {%- if item.EMPVUL is not none -%}
        EMPVUL={{item.EMPVUL}},
    {%- endif -%}
    {%- if item.GBRUPLKVALUE is not none -%}
        GBRUPLKVALUE={{item.GBRUPLKVALUE}},
    {%- endif -%}
    {%- if item.GBRDNLKVALUE is not none -%}
        GBRDNLKVALUE={{item.GBRDNLKVALUE}},
    {%- endif -%}
    {%- if item.MBRUPLKVALUE is not none -%}
        MBRUPLKVALUE={{item.MBRUPLKVALUE}},
    {%- endif -%}
    {%- if item.MBRDNLKVALUE is not none -%}
        MBRDNLKVALUE={{item.MBRDNLKVALUE}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：QOSTYPE=QOS_FLOW_PARA/QOS_L2_PARA 时必选 --- -#}
    {%- if item.QOSTYPE in ['QOS_FLOW_PARA', 'QOS_L2_PARA'] -%}
        FQI={{item.FQI}},
    {%- endif -%}
    {#- --- 条件必选/可选参数 --- -#}
    {#- --- 分配保留优先级: 条件必选(QoS属性类型=QOS_FLOW_PARA|QOS_L2_PARA) / 条件可选(QoS属性类型=QOS_BEARER_PARA) --- -#}
    {%- if (item.QOSTYPE in ['QOS_FLOW_PARA', 'QOS_L2_PARA']) -%}
        ARPVALUE={{item.ARPVALUE}},
    {%- elif (item.QOSTYPE == 'QOS_BEARER_PARA') -%}
        {%- if item.ARPVALUE is not none -%}
            ARPVALUE={{item.ARPVALUE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 查询指定APN实例，查询结果为huawei.com。

### 6 配置SMF上的本地L2Filter（层二过滤器）。

```jinja2
{%- for item in add_l2filter_list -%}
    ADD L2FILTER:
    {#- --- 必选参数 --- -#}
    FILTERNAME="{{item.FILTERNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.SRCMACADDR is not none -%}
        SRCMACADDR="{{item.SRCMACADDR}}",
    {%- endif -%}
    {%- if item.DESTMACADDR is not none -%}
        DESTMACADDR="{{item.DESTMACADDR}}",
    {%- endif -%}
    {%- if item.VID is not none -%}
        VID={{item.VID}},
    {%- endif -%}
    {%- if item.PCP is not none -%}
        PCP={{item.PCP}},
    {%- endif -%}
    {%- if item.DEI is not none -%}
        DEI={{item.DEI}},
    {%- endif -%}
    {%- if item.ETHERTYPE is not none -%}
        ETHERTYPE={{item.ETHERTYPE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 7 绑定L2Filter（层二过滤器）与QoS属性的关系，“QOSPROPNAME”使用**ADD CPQOSPROP**命令配置的“QOSPROPNAME”参数值。

```jinja2
{%- for item in add_l2rule_list -%}
    ADD L2RULE:
    {#- --- 必选参数 --- -#}
    L2RULENAME="{{item.L2RULENAME}}",
    QOSPROPNAME="{{item.QOSPROPNAME}}",
    L2FILTERNAME="{{item.L2FILTERNAME}}",
    ;
{%- endfor -%}
```

### 8 配置SMF上的本地L2RULEGROUP（层二规则组）。

```jinja2
{%- for item in add_l2rulegroup_list -%}
    ADD L2RULEGROUP:
    {#- --- 必选参数 --- -#}
    L2RULEGROUPNAME="{{item.L2RULEGROUPNAME}}",
    ;
{%- endfor -%}
```

### 9 绑定L2RULEGROUP（层二规则组）与L2Rule（层二规则）的关系，一个L2RULEGROUP支持绑定多个L2Rule。

```jinja2
{%- for item in add_l2rulebindgrp_list -%}
    ADD L2RULEBINDGRP:
    {#- --- 必选参数 --- -#}
    L2RULEGROUPNAME="{{item.L2RULEGROUPNAME}}",
    L2RULENAME="{{item.L2RULENAME}}",
    ;
{%- endfor -%}
```

### 10 绑定L2RULEGROUP（层二规则组）与指定用户群的关系，“SEGMENTNAME”使用**ADD IMSIMSISDNSEG**命令配置的“SEGMENTNAME”参数值。

```jinja2
{%- for item in add_l2rulegrpbind_list -%}
    ADD L2RULEGRPBIND:
    {#- --- 必选参数 --- -#}
    GRPBINDNAME="{{item.GRPBINDNAME}}",
    SEGMENTNAME="{{item.SEGMENTNAME}}",
    APN="{{item.APN}}",
    SST={{item.SST}},
    L2RULEGRPNAME="{{item.L2RULEGRPNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.SD is not none -%}
        SD="{{item.SD}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

