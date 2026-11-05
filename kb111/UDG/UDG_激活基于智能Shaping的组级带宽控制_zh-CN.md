---
id: GWFD-110313
name: 激活基于智能Shaping的组级带宽控制
ne_type: UDG
type: feature
description: 当基于整形的业务流量控制想要得到公平丢包率时，请进行本节操作。
risk_level: ''
doc_source: ["特性部署","特性指南","UDG特性指南","智能策略控制功能","GWFD-110313 基于智能Shaping的组级带宽控制","激活基于智能Shaping的组级带宽控制"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当基于整形的业务流量控制想要得到公平丢包率时，请进行本节操作。

## 必备事项
前提条件

* UDG与网络实体之间的网络环境已经构建完成。
* 本特性License项依赖于其他特性，需开启依赖特性后才能开启本特性。详细仔细阅读GWFD-020354 基于业务的Shaping。
* 请仔细阅读GWFD-110313 基于智能Shaping的组级带宽控制。
* 已加载特征库和解析库。
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
    add_bwmcontroller_list:
      type: items
      properties:
        BWMCNAME:
          name: '带宽管理控制器名称'
          type: string
          maxLength: 31
          required: true
          description: '用于表示带宽管理控制器的名字。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        CTRLTYPE:
          name: '带宽管理控制类型'
          type: string
          enum:
          - CAR
          - SHAPING
          required: false
          description: '用于表示带宽管理控制类型。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        RATE:
          name: '速率（千比特/秒）'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
          description: '用于表示SHAPING速率，报文将被控制按该速率平稳转发出去。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        QUEDEPTH:
          name: '队列深度（包）'
          type: integer
          minimum: 1
          maximum: 9600000
          required: false
          description: '用于表示SHAPING缓存队列深度。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SRVLEVELSPEC:
          name: '业务等级规格'
          type: integer
          minimum: 1
          maximum: 30
          required: false
          description: '用于表示该带宽管理控制器最大可支持的业务等级规格。'
          data_source: '全网规划'
          pattern: ''
          default: 2
        USERFAIREN:
          name: '用户公平使能'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '表示该带宽管理控制器在组级带宽管理时是否支持用户级公平调度功能使能。'
          data_source: '全网规划'
          pattern: ''
          default: DISABLE
        WORKMODE:
          name: '工作模式'
          type: string
          enum:
          - MANUAL
          - AUTO
          required: false
          description: '用于表示该带宽管理控制器在执行组级带宽控制策略时的工作模式为自动模式还是手动模式。'
          data_source: '全网规划'
          pattern: ''
          default: MANUAL
        MAXPKTLOSTRATE:
          name: '最大丢包率'
          type: string
          required: false
          description: '用于表示此带宽控制器允许的最大丢包比率。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PKTLOSTRATEDTL:
          name: '丢包率差值'
          type: string
          required: false
          description: '用于表示此带宽控制器两个有数据的ServiceLevel之间的丢包率差值'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ASSUREMODE:
          name: '保障模式'
          type: string
          required: false
          description: '用于表示该带宽管理控制器的在自动计算每个ServiceLevel的丢包率时，出现最大丢包率和带宽控制器出口速率仅能满足一个条件时的优先保障模式。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        CBS:
          name: '承诺突发能缓存信息的数量（字节）'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CIR:
          name: '承诺信息速率（千比特/秒）'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        COLORISAWARE:
          name: 'BWM CAR颜色是否敏感'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        GREEN:
          name: '绿色'
          type: string
          enum:
          - DISCARD
          - PASS
          - REMARK
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: PASS
        PBS:
          name: '峰值突发能缓存信息的数量（字节）'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PIR:
          name: '峰值信息速率（千比特/秒）'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIORITYISAWARE:
          name: 'BWM CAR优先级是否敏感'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        RED:
          name: '红色'
          type: string
          enum:
          - DISCARD
          - PASS
          - REMARK
          required: false
          description: ''
          data_source: ''
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
          data_source: ''
          pattern: ''
          default: PASS
    add_bcsrvlevelply_list:
      type: items
      properties:
        BWMCNAME:
          name: '带宽管理控制器名称'
          type: string
          maxLength: 31
          required: true
          description: '用于表示带宽管理控制器的名字。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SERVICELEVEL:
          name: '业务级别'
          type: integer
          minimum: 1
          maximum: 30
          required: true
          description: '用于指定使用同一控制器的不同业务流间的优先级，值越小优先级越高。如果配置优先级，优先保证高优先级的带宽。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SHAPRATE:
          name: '整形速率'
          type: integer
          minimum: 0
          maximum: 10000
          required: false
          description: '用于表示此业务等级的最高峰值带宽比例，实际承诺信息速率相当于ShapRate\* RATE（BwmController命令）。'
          data_source: '全网规划'
          pattern: ''
          default: 0
        MAXPKTLOSTRATE:
          name: '最大丢包率'
          type: integer
          minimum: 0
          maximum: 10000
          required: false
          description: '用于表示此带宽控制器允许的最大丢包比率。'
          data_source: '全网规划'
          pattern: ''
          default: 10000
        MAXINCRDELAY:
          name: '最大增加时延'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: '用于表示此业务等级因Shaping队列缓存的最大增加时延。'
          data_source: '全网规划'
          pattern: ''
          default: 65535
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3G5FSHP01'
      SWITCH: ENABLE
    add_bwmcontroller_list:
    - BWMCNAME: 'bc1'
      CTRLTYPE: SHAPING
      RATE: 400
      QUEDEPTH: 25
      SRVLEVELSPEC: 10
      USERFAIREN: ENABLE
      WORKMODE: MANUAL
      MAXPKTLOSTRATE: '10000'
      PKTLOSTRATEDTL: '50'
      ASSUREMODE: EXPFIRST
      CBS: ''
      CIR: ''
      COLORISAWARE: DISABLE
      GREEN: PASS
      PBS: ''
      PIR: ''
      PRIORITYISAWARE: DISABLE
      RED: PASS
      YELLOW: PASS
    add_bcsrvlevelply_list:
    - BWMCNAME: 'bc1'
      SERVICELEVEL: 2
      SHAPRATE: 100
      MAXPKTLOSTRATE: 10000
      MAXINCRDELAY: 100
```

## 3 命令模板定义
<!-- @mml:block=commands -->

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

### 2 设置支持用户级公平调度功能。

### **ADD BwmController**

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
    {#- --- 条件必选：CTRLTYPE=SHAPING 时必选 --- -#}
    {%- if item.CTRLTYPE == 'SHAPING' -%}
        RATE={{item.RATE}},
    {%- endif -%}
    {#- --- 条件必选：CTRLTYPE=SHAPING 时必选 --- -#}
    {%- if item.CTRLTYPE == 'SHAPING' -%}
        QUEDEPTH={{item.QUEDEPTH}},
    {%- endif -%}
    {#- --- 条件必选：CTRLTYPE=CAR 时必选 --- -#}
    {%- if item.CTRLTYPE == 'CAR' -%}
        CIR={{item.CIR}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：CTRLTYPE=CAR/SHAPING 时可选 --- -#}
    {%- if item.CTRLTYPE in ['CAR', 'SHAPING'] -%}
        {%- if item.SRVLEVELSPEC is not none -%}
            SRVLEVELSPEC={{item.SRVLEVELSPEC}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CTRLTYPE=SHAPING 时可选 --- -#}
    {%- if item.CTRLTYPE == 'SHAPING' -%}
        {%- if item.USERFAIREN is not none -%}
            USERFAIREN={{item.USERFAIREN}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CTRLTYPE=SHAPING 时可选 --- -#}
    {%- if item.CTRLTYPE == 'SHAPING' -%}
        {%- if item.WORKMODE is not none -%}
            WORKMODE={{item.WORKMODE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：WORKMODE=AUTO 时可选 --- -#}
    {%- if item.WORKMODE == 'AUTO' -%}
        {%- if item.MAXPKTLOSTRATE is not none -%}
            MAXPKTLOSTRATE={{item.MAXPKTLOSTRATE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：WORKMODE=AUTO 时可选 --- -#}
    {%- if item.WORKMODE == 'AUTO' -%}
        {%- if item.PKTLOSTRATEDTL is not none -%}
            PKTLOSTRATEDTL={{item.PKTLOSTRATEDTL}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：WORKMODE=AUTO 时可选 --- -#}
    {%- if item.WORKMODE == 'AUTO' -%}
        {%- if item.ASSUREMODE is not none -%}
            ASSUREMODE={{item.ASSUREMODE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CTRLTYPE=CAR 时可选 --- -#}
    {%- if item.CTRLTYPE == 'CAR' -%}
        {%- if item.CBS is not none -%}
            CBS={{item.CBS}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CTRLTYPE=CAR 时可选 --- -#}
    {%- if item.CTRLTYPE == 'CAR' -%}
        {%- if item.COLORISAWARE is not none -%}
            COLORISAWARE={{item.COLORISAWARE}},
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
        {%- if item.PBS is not none -%}
            PBS={{item.PBS}},
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
        {%- if item.PRIORITYISAWARE is not none -%}
            PRIORITYISAWARE={{item.PRIORITYISAWARE}},
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
        {%- if item.YELLOW is not none -%}
            YELLOW={{item.YELLOW}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置带宽管理控制器业务等级策略。

```jinja2
{%- for item in add_bcsrvlevelply_list -%}
    ADD BCSRVLEVELPLY:
    {#- --- 必选参数 --- -#}
    BWMCNAME="{{item.BWMCNAME}}",
    SERVICELEVEL={{item.SERVICELEVEL}},
    {#- --- 可选参数 --- -#}
    {%- if item.SHAPRATE is not none -%}
        SHAPRATE={{item.SHAPRATE}},
    {%- endif -%}
    {%- if item.MAXPKTLOSTRATE is not none -%}
        MAXPKTLOSTRATE={{item.MAXPKTLOSTRATE}},
    {%- endif -%}
    {%- if item.MAXINCRDELAY is not none -%}
        MAXINCRDELAY={{item.MAXINCRDELAY}},
    {%- endif -%}
    ;
{%- endfor -%}
```

