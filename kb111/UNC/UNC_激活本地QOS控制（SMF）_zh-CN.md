---
id: ''
name: 激活本地QOS控制（SMF）
ne_type: UNC
type: feature
description: 运营商根据UNC本地配置的QoS参数对用户数据进行控制。  适用于SMF。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","QoS功能","WSFD-109203 本地QOS控制","激活本地QOS控制（SMF）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
运营商根据UNC本地配置的QoS参数对用户数据进行控制。适用于SMF。

## 必备事项
前提条件

* 请仔细阅读WSFD-109203 本地QOS控制特性概述。
* 完成配置普通APN**ADD APN** 。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_qci2arp_list:
      type: items
      properties:
        QCI:
          name: '标准QCI'
          type: integer
          minimum:
          - 1
          - 65
          - 69
          maximum:
          - 9
          - 66
          - 70
          required: true
          description: '可选：配置5QI和ARP的对应关系。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ARPPCI:
          name: 'ARP的可抢占能力'
          type: integer
          minimum: 0
          maximum: 1
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ARPPL:
          name: 'ARP的优先级别'
          type: integer
          minimum: 1
          maximum: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ARPPVI:
          name: 'QCI的被抢占能力'
          type: integer
          minimum: 0
          maximum: 1
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_5gcsubqos_list:
      type: items
      properties:
        FIVEQI:
          name: '标准5QI'
          type: integer
          minimum: 5
          maximum: 80
          required: true
          description: '配置5G用户的签约QoS属性。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        QOS5QIPL:
          name: '5QI的优先级别'
          type: integer
          minimum: 0
          maximum: 127
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ARPPL:
          name: 'ARP的优先级别'
          type: integer
          minimum: 1
          maximum: 15
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AMBRDL:
          name: '下行Session AMBR(kbps)'
          type: integer
          minimum: 0
          maximum: 20000000
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AMBRUL:
          name: '上行Session AMBR(kbps)'
          type: integer
          minimum: 0
          maximum: 20000000
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SUBQOSINDEX:
          name: '用户QOS索引'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_5gcqoscorrt_list:
      type: items
      properties:
        FIVEQI:
          name: '5QI值'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: '配置5G QoS纠错参数。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        QOS5QIPL:
          name: '5QI优先级'
          type: integer
          minimum: 1
          maximum: 127
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ARPVALUE:
          name: 'ARP值'
          type: integer
          minimum: 1
          maximum: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AMBRDL:
          name: '下行Session AMBR(千比特/秒)'
          type: integer
          minimum: 0
          maximum: 20000000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AMBRUL:
          name: '上行Session AMBR(千比特/秒)'
          type: integer
          minimum: 0
          maximum: 20000000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GFBRUL:
          name: '上行保证带宽(千比特/秒)'
          type: integer
          minimum: 0
          maximum: 20000000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GFBRDL:
          name: '下行保证带宽(千比特/秒)'
          type: integer
          minimum: 0
          maximum: 20000000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MFBRUL:
          name: '上行最大带宽(千比特/秒)'
          type: integer
          minimum: 0
          maximum: 20000000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MFBRDL:
          name: '下行最大带宽(千比特/秒)'
          type: integer
          minimum: 0
          maximum: 20000000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_qosglobal_list:
      type: items
      properties:
        QOSPROFILENAME:
          name: 'Qos Profile名'
          type: string
          minLength: 1
          maxLength: 63
          required: false
          description: '配置基于全局的QoS Profile。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        BINDEPSSUBQOS:
          name: '绑定EPS用户QoS'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EPSSUBQOS:
          name: 'EPS用户QoS索引'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BINDSUBQOS5GC:
          name: '绑定5G用户QoS'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SUBQOS5GC:
          name: '5G用户QoS索引'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_qosprofile_list:
      type: items
      properties:
        QOSPROFILENAME:
          name: 'QoS名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '配置QosProfile，并进入Qos实例。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        BINDEPSSUBQOS:
          name: '绑定EPS用户QoS'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        EPSSUBQOS:
          name: 'EPS用户QoS索引'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BINDSUBQOS5GC:
          name: '绑定5G用户QoS'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        SUBQOS5GC:
          name: '5G用户QoS索引'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_5gcqosaction_list:
      type: items
      properties:
        QOSPROFILENAME:
          name: 'QoS Profile名'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '配置5G用户QoS上下行保证带宽门限、最高带宽门限以及带宽超过门限值时对QoS用户的处理动作。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        FIVEQI:
          name: '5QI值'
          type: integer
          minimum: 1
          maximum: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GFBRDL:
          name: '下行保证带宽'
          type: integer
          minimum: 0
          maximum: 20000000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        GFBRDLACTION:
          name: '超过下行保证带宽的处理'
          type: string
          enum:
          - DEGRADE
          - REJECT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DEGRADE
        GFBRUL:
          name: '上行保证带宽'
          type: integer
          minimum: 0
          maximum: 20000000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        GFBRULACTION:
          name: '超过上行保证带宽的处理'
          type: string
          enum:
          - DEGRADE
          - REJECT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DEGRADE
        MFBRDL:
          name: '下行最大带宽'
          type: integer
          minimum: 0
          maximum: 20000000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        MFBRDLACTION:
          name: '超过下行最大带宽的处理'
          type: string
          enum:
          - DEGRADE
          - REJECT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DEGRADE
        MFBRUL:
          name: '上行最大带宽'
          type: integer
          minimum: 0
          maximum: 20000000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        MFBRULACTION:
          name: '超过上行最大带宽的处理'
          type: string
          enum:
          - DEGRADE
          - REJECT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DEGRADE
    add_apn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '配置指定APN实例。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_apnqosattr_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '为该APN实例绑定QOSPROFILE。  如果APN配置了QosProfile，则该APN上全局下的QosProfile不会生效。'
          data_source: '从已配置数据中获取'
          pattern: ''
          default: ''
        HASQOSPROFILE:
          name: '有Qos Profile'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        QOSPROFILENAME:
          name: 'Qos Profile名'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_qci2arp_list:
    - QCI: 1
      ARPPCI: 0
      ARPPL: 1
      ARPPVI: 0
    add_5gcsubqos_list:
    - FIVEQI: 5
      QOS5QIPL: 2
      ARPPL: 2
      AMBRDL: 1111
      AMBRUL: 2222
      SUBQOSINDEX: 203
    set_5gcqoscorrt_list:
    - FIVEQI: 5
      QOS5QIPL: 10
      ARPVALUE: 3
      AMBRDL: 20000
      AMBRUL: 20000
      GFBRUL: 4000
      GFBRDL: 4000
      MFBRUL: 5000
      MFBRDL: 5000
    set_qosglobal_list:
    - QOSPROFILENAME: 'qos2'
      BINDEPSSUBQOS: ENABLE
      EPSSUBQOS: 203
      BINDSUBQOS5GC: ENABLE（使能）
      SUBQOS5GC: 203
    add_qosprofile_list:
    - QOSPROFILENAME: 'qos1'
      BINDEPSSUBQOS: ENABLE
      EPSSUBQOS: 203
      BINDSUBQOS5GC: ENABLE（使能）
      SUBQOS5GC: 203
    add_5gcqosaction_list:
    - QOSPROFILENAME: 'qos1'
      FIVEQI: 2
      GFBRDL: 256bit/s
      GFBRDLACTION: DEGRADE(降级)
      GFBRUL: 128bit/s
      GFBRULACTION: DEGRADE(降级)
      MFBRDL: 384bit/s
      MFBRDLACTION: DEGRADE(降级)
      MFBRUL: 192bit/s
      MFBRULACTION: DEGRADE(降级)
    add_apn_list:
    - APN: 'apn1'
    set_apnqosattr_list:
    - APN: 'apn1'
      HASQOSPROFILE: ENABLE
      QOSPROFILENAME: 'qos1'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 **可选**：更改缺省的ARP和标准5QI的对应关系

```jinja2
{%- if is_optional_change_arp_5qi_mapping -%}
    {%- for item in set_qci2arp_list -%}
        SET QCI2ARP:
        {#- --- 必选参数 --- -#}
        QCI={{item.QCI}},
        {#- --- 可选参数 --- -#}
        {%- if item.ARPPCI is not none -%}
            ARPPCI={{item.ARPPCI}},
        {%- endif -%}
        {%- if item.ARPPL is not none -%}
            ARPPL={{item.ARPPL}},
        {%- endif -%}
        {%- if item.ARPPVI is not none -%}
            ARPPVI={{item.ARPPVI}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 3 **可选**：配置本地签约的QoS信息。

```jinja2
{%- if is_optional_configure_local_qos -%}
    {%- for item in add_5gcsubqos_list -%}
        ADD 5GCSUBQOS:
        {#- --- 必选参数 --- -#}
        FIVEQI={{item.FIVEQI}},
        ARPPL={{item.ARPPL}},
        AMBRDL={{item.AMBRDL}},
        AMBRUL={{item.AMBRUL}},
        SUBQOSINDEX={{item.SUBQOSINDEX}},
        {#- --- 可选参数 --- -#}
        {%- if item.QOS5QIPL is not none -%}
            QOS5QIPL={{item.QOS5QIPL}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 4 配置5G QoS纠错参数。

```jinja2
{%- for item in set_5gcqoscorrt_list -%}
    SET 5GCQOSCORRT:
    {#- --- 可选参数 --- -#}
    {%- if item.FIVEQI is not none -%}
        FIVEQI={{item.FIVEQI}},
    {%- endif -%}
    {%- if item.QOS5QIPL is not none -%}
        QOS5QIPL={{item.QOS5QIPL}},
    {%- endif -%}
    {%- if item.ARPVALUE is not none -%}
        ARPVALUE={{item.ARPVALUE}},
    {%- endif -%}
    {%- if item.AMBRDL is not none -%}
        AMBRDL={{item.AMBRDL}},
    {%- endif -%}
    {%- if item.AMBRUL is not none -%}
        AMBRUL={{item.AMBRUL}},
    {%- endif -%}
    {%- if item.GFBRUL is not none -%}
        GFBRUL={{item.GFBRUL}},
    {%- endif -%}
    {%- if item.GFBRDL is not none -%}
        GFBRDL={{item.GFBRDL}},
    {%- endif -%}
    {%- if item.MFBRUL is not none -%}
        MFBRUL={{item.MFBRUL}},
    {%- endif -%}
    {%- if item.MFBRDL is not none -%}
        MFBRDL={{item.MFBRDL}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 设置全局的QoS信息。

```jinja2
{%- for item in set_qosglobal_list -%}
    SET QOSGLOBAL:
    {#- --- 可选参数 --- -#}
    {%- if item.QOSPROFILENAME is not none -%}
        QOSPROFILENAME="{{item.QOSPROFILENAME}}",
    {%- endif -%}
    {%- if item.BINDEPSSUBQOS is not none -%}
        BINDEPSSUBQOS={{item.BINDEPSSUBQOS}},
    {%- endif -%}
    {%- if item.BINDSUBQOS5GC is not none -%}
        BINDSUBQOS5GC={{item.BINDSUBQOS5GC}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：BINDEPSSUBQOS=ENABLE 时必选 --- -#}
    {%- if item.BINDEPSSUBQOS == 'ENABLE' -%}
        EPSSUBQOS={{item.EPSSUBQOS}},
    {%- endif -%}
    {#- --- 条件必选：BINDSUBQOS5GC=ENABLE 时必选 --- -#}
    {%- if item.BINDSUBQOS5GC == 'ENABLE' -%}
        SUBQOS5GC={{item.SUBQOS5GC}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 6 配置基于APN的QoS策略。

#### 6.1 配置指定APN实例下的QosProfile名称，并进入QoS实例。

```jinja2
{%- for item in add_qosprofile_list -%}
    ADD QOSPROFILE:
    {#- --- 必选参数 --- -#}
    QOSPROFILENAME="{{item.QOSPROFILENAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.BINDEPSSUBQOS is not none -%}
        BINDEPSSUBQOS={{item.BINDEPSSUBQOS}},
    {%- endif -%}
    {%- if item.BINDSUBQOS5GC is not none -%}
        BINDSUBQOS5GC={{item.BINDSUBQOS5GC}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：BINDEPSSUBQOS=ENABLE 时必选 --- -#}
    {%- if item.BINDEPSSUBQOS == 'ENABLE' -%}
        EPSSUBQOS={{item.EPSSUBQOS}},
    {%- endif -%}
    {#- --- 条件必选：BINDSUBQOS5GC=ENABLE 时必选 --- -#}
    {%- if item.BINDSUBQOS5GC == 'ENABLE' -%}
        SUBQOS5GC={{item.SUBQOS5GC}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 6.2 配置5G用户QoS上下行保证带宽门限、最高带宽门限以及带宽超过门限值时对QoS用户的处理动作。

```jinja2
{%- for item in add_5gcqosaction_list -%}
    ADD 5GCQOSACTION:
    {#- --- 必选参数 --- -#}
    QOSPROFILENAME="{{item.QOSPROFILENAME}}",
    FIVEQI={{item.FIVEQI}},
    {#- --- 可选参数 --- -#}
    {%- if item.GFBRDL is not none -%}
        GFBRDL={{item.GFBRDL}},
    {%- endif -%}
    {%- if item.GFBRDLACTION is not none -%}
        GFBRDLACTION={{item.GFBRDLACTION}},
    {%- endif -%}
    {%- if item.GFBRUL is not none -%}
        GFBRUL={{item.GFBRUL}},
    {%- endif -%}
    {%- if item.GFBRULACTION is not none -%}
        GFBRULACTION={{item.GFBRULACTION}},
    {%- endif -%}
    {%- if item.MFBRDL is not none -%}
        MFBRDL={{item.MFBRDL}},
    {%- endif -%}
    {%- if item.MFBRDLACTION is not none -%}
        MFBRDLACTION={{item.MFBRDLACTION}},
    {%- endif -%}
    {%- if item.MFBRUL is not none -%}
        MFBRUL={{item.MFBRUL}},
    {%- endif -%}
    {%- if item.MFBRULACTION is not none -%}
        MFBRULACTION={{item.MFBRULACTION}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 6.3 配置APN实例。

```jinja2
{%- for item in add_apn_list -%}
    ADD APN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    ;
{%- endfor -%}
```

#### 6.4 为APN实例绑定QoS profile。

```jinja2
{%- for item in set_apnqosattr_list -%}
    SET APNQOSATTR:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.HASQOSPROFILE is not none -%}
        HASQOSPROFILE={{item.HASQOSPROFILE}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：HASQOSPROFILE=ENABLE 时必选 --- -#}
    {%- if item.HASQOSPROFILE == 'ENABLE' -%}
        QOSPROFILENAME="{{item.QOSPROFILENAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

