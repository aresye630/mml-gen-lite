---
id: ''
name: 配置4G网络基于指定区域的策略控制（SGW-C/PGW-C）
ne_type: UNC
type: feature
description: 本操作指导介绍在运行网络中激活基于指定区域的策略控制的操作过程。  基于指定区域的策略控制特性是指基于运营商订阅的PRA（Presence Report Area）区域，当用户进入或离开这些区域时，UNC获得用户当前位置信息并向PCRF/PCF上报，PCRF/PCF根据用户位置状态进行策略决策并发起策略更新，执行不同的服务策略（如特殊计费、套餐、信息推送等），满足运营商基于位置信息的差异化和定制化需求，用户通过签约享受相应服务。  适用于SGW-C、PGW-C。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","智能PCC解决方案","基于指定区域的策略控制","4G网络基于指定区域的策略控制","配置4G网络基于指定区域的策略控制（SGW-C/PGW-C）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活基于指定区域的策略控制的操作过程。基于指定区域的策略控制特性是指基于运营商订阅的PRA（Presence Report Area）区域，当用户进入或离开这些区域时，UNC获得用户当前位置信息并向PCRF/PCF上报，PCRF/PCF根据用户位置状态进行策略决策并发起策略更新，执行不同的服务策略（如特殊计费、套餐、信息推送等），满足运营商基于位置信息的差异化和定制化需求，用户通过签约享受相应服务。适用于SGW-C、PGW-C。

## 必备事项
前提条件

* 请仔细阅读4G网络基于指定区域的策略控制。
* 已完成加载License。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_pcrf_list:
      type: items
      properties:
        HOSTNAME:
          name: 'PCRF主机名'
          type: string
          maxLength: 127
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REALMNAME:
          name: 'PCRF域名'
          type: string
          maxLength: 127
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SUPFEANEGOSW:
          name: 'Supported-Features动态协商开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        CARRYSUPFEASW:
          name: 'Supported-Feature AVP携带开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ENABLE
        FEATURELIST:
          name: 'Feature列表'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_realmbindapn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        APPLICATION:
          name: 'Diameter应用'
          type: string
          enum:
          - GX
          - GY
          - S6B
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CONSTBYIMSISW:
          name: '根据IMSI构造归属地Realm开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SUPFTNEGOSW:
          name: 'Supported-Features动态协商开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        FEATURELIST:
          name: 'Feature列表'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CARRYSUPFEASW:
          name: 'Supported-Feature AVP携带开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ENABLE
        REALMNAME:
          name: 'Realm名'
          type: string
          maxLength: 127
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_smffunc_list:
      type: items
      properties:
        AOI:
          name: '兴趣区'
          type: string
          enum:
          - NotSupport
          - Support
          required: false
          description: '配置SGW-C/PGW-C支持兴趣区。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_smfsoftparaofbit_list:
      type: items
      properties:
        DT:
          name: '数据类型'
          type: string
          enum:
          - Dw
          - Byte
          required: true
          description: '配置SGW-C/PGW-C支持处理PRA信元。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        DWORDNUM:
          name: 'Dword索引'
          type: integer
          minimum: 1
          maximum: 1500
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VALUE:
          name: '软件记录值'
          type: string
          enum:
          - VALUE_0
          - VALUE_1
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        POSITION:
          name: '比值位'
          type: integer
          minimum: 1
          maximum: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BYTENUM:
          name: 'Byte索引'
          type: integer
          minimum: 1
          maximum: 1200
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BYTEPOSITION:
          name: 'Byte软参比特位'
          type: integer
          minimum: 1
          maximum: 8
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_pcrf_list:
    - HOSTNAME: 'pcrf1'
      REALMNAME: 'www.huawei.com'
      SUPFEANEGOSW: DISABLE
      CARRYSUPFEASW: ENABLE
      FEATURELIST: CNO_ULI-1&RELEASE8-1
    add_realmbindapn_list:
    - APN: 'cmnet'
      APPLICATION: GX
      CONSTBYIMSISW: ENABLE
      SUPFTNEGOSW: DISABLE
      FEATURELIST: CNO_ULI-1&RELEASE8-1
      CARRYSUPFEASW: ENABLE
      REALMNAME: ''
    set_smffunc_list:
    - AOI: Support
    set_smfsoftparaofbit_list:
    - DT: Dw
      DWORDNUM: 1001
      VALUE: VALUE_1
      POSITION: 9
      BYTENUM: ''
      BYTEPOSITION: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 配置基于指定区域的策略控制功能。

```jinja2
{%- if is_optional_region_based_policy_control and is_scenario_direct_pcrf -%}
    {%- for item in add_pcrf_list -%}
        ADD PCRF:
        {#- --- 必选参数 --- -#}
        HOSTNAME="{{item.HOSTNAME}}",
        REALMNAME="{{item.REALMNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.SUPFEANEGOSW is not none -%}
            SUPFEANEGOSW={{item.SUPFEANEGOSW}},
        {%- endif -%}
        {%- if item.FEATURELIST is not none -%}
            FEATURELIST={{item.FEATURELIST}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：SUPFEANEGOSW=DISABLE 时可选 --- -#}
        {%- if item.SUPFEANEGOSW == 'DISABLE' -%}
            {%- if item.CARRYSUPFEASW is not none -%}
                CARRYSUPFEASW={{item.CARRYSUPFEASW}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_optional_region_based_policy_control and is_scenario_via_dra -%}
    {%- for item in add_realmbindapn_list -%}
        ADD REALMBINDAPN:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        APPLICATION={{item.APPLICATION}},
        CONSTBYIMSISW={{item.CONSTBYIMSISW}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：CONSTBYIMSISW=DISABLE 时必选 --- -#}
        {%- if item.CONSTBYIMSISW == 'DISABLE' -%}
            REALMNAME="{{item.REALMNAME}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：APPLICATION=GX 时可选 --- -#}
        {%- if item.APPLICATION == 'GX' -%}
            {%- if item.SUPFTNEGOSW is not none -%}
                SUPFTNEGOSW={{item.SUPFTNEGOSW}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：APPLICATION=GX 时可选 --- -#}
        {%- if item.APPLICATION == 'GX' -%}
            {%- if item.FEATURELIST is not none -%}
                FEATURELIST={{item.FEATURELIST}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：SUPFTNEGOSW=DISABLE 时可选 --- -#}
        {%- if item.SUPFTNEGOSW == 'DISABLE' -%}
            {%- if item.CARRYSUPFEASW is not none -%}
                CARRYSUPFEASW={{item.CARRYSUPFEASW}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 3 配置SGW-C/PGW-C支持兴趣区。

```jinja2
{%- for item in set_smffunc_list -%}
    SET SMFFUNC:
    {#- --- 可选参数 --- -#}
    {%- if item.AOI is not none -%}
        AOI={{item.AOI}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 配置SGW-C/PGW-C支持处理PRA信元，设置软参DWORD1001 BIT9值为1。

```jinja2
{%- for item in set_smfsoftparaofbit_list -%}
    SET SMFSOFTPARAOFBIT:
    {#- --- 必选参数 --- -#}
    DT={{item.DT}},
    VALUE={{item.VALUE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：DT=Dw 时必选 --- -#}
    {%- if item.DT == 'Dw' -%}
        DWORDNUM={{item.DWORDNUM}},
    {%- endif -%}
    {#- --- 条件必选：DT=Dw 时必选 --- -#}
    {%- if item.DT == 'Dw' -%}
        POSITION={{item.POSITION}},
    {%- endif -%}
    {#- --- 条件必选：DT=Byte 时必选 --- -#}
    {%- if item.DT == 'Byte' -%}
        BYTENUM={{item.BYTENUM}},
    {%- endif -%}
    {#- --- 条件必选：DT=Byte 时必选 --- -#}
    {%- if item.DT == 'Byte' -%}
        BYTEPOSITION={{item.BYTEPOSITION}},
    {%- endif -%}
    ;
{%- endfor -%}
```

