---
id: ''
name: 激活NSA用户QoS管理
ne_type: UNC
type: feature
description: 华为UNC支持DCNR用户使用扩展QoS接入基本功能，可以保证签约的DCNR用户扩展QoS接入网络并使用业务。  适用于SGW-C、PGW-C。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","NSA业务基本功能","WSFD-011521 NSA用户QoS管理","激活NSA用户QoS管理"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
华为UNC支持DCNR用户使用扩展QoS接入基本功能，可以保证签约的DCNR用户扩展QoS接入网络并使用业务。适用于SGW-C、PGW-C。

## 必备事项
前提条件

* 请仔细阅读WSFD-011521 NSA 用户QoS管理特性概述。
* 完成配置普通APN**ADD APN**。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_ofccdrpara_list:
      type: items
      properties:
        SGWLOTVQOSEXT:
          name: 'SGW-CDR流量容器携带扩展Qos参数开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '配置离线计费话单参数'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        PGWLOTVQOSEXT:
          name: 'PGW-CDR流量容器携带扩展Qos参数开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PGWLOSDQOSEXT:
          name: 'PGW-CDR业务容器携带扩展Qos参数开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_diamdictpath_list:
      type: items
      properties:
        APPLICATION:
          name: 'Diameter应用'
          type: string
          enum:
          - GX
          - GY
          - S6B
          required: true
          description: '配置Diameter字典加载路径'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DICTNO:
          name: '字典序号'
          type: integer
          minimum: 1
          maximum: 2
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DICTPATH:
          name: '字典加载路径'
          type: string
          enum:
          - CUSTOM1
          - CUSTOM2
          - EPC970_STANDARD
          - EPC_STANDARD
          - GU_STANDARD
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    lod_diamdict_list:
      type: items
      properties:
        DICTFILESELECT:
          name: '字典文件选择'
          type: string
          enum:
          - ALL
          required: true
          description: '加载Diameter字典文件'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_pcrf_list:
      type: items
      properties:
        HOSTNAME:
          name: 'PCRF主机名'
          type: string
          maxLength: 127
          required: true
          description: '增加PCRF的基本信息  说明：  “FEATURELIST”需要同时配置为“RELEASE8”和“EXTENDED\_BW\_NR”。'
          data_source: '本端规划'
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
        FEATURELIST:
          name: 'Feature列表'
          type: string
          required: false
          description: ''
          data_source: '与对端协商'
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
          data_source: '对端协商'
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
    add_glbdiamrealm_list:
      type: items
      properties:
        APPLICATION:
          name: 'Diameter应用'
          type: string
          enum:
          - GX
          - GY
          - S6B
          required: true
          description: '增加全局Diameter域  说明：  “FEATURELIST”需要同时配置为“RELEASE8”和“EXTENDED\_BW\_NR”。'
          data_source: '全网规划'
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
        REALM:
          name: 'Diameter域名'
          type: string
          maxLength: 127
          required: false
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
          data_source: '与对端协商'
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
    add_realmbindapn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          maxLength: 63
          required: true
          description: '设置APN与Diameter Realm关联关系 说明：  可使用  ****LST APN****查询APN名称.  “FEATURELIST”需要同时配置为“RELEASE8”和“EXTENDED\_BW\_NR”。'
          data_source: '全网规划'
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
          data_source: '与对端协商'
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
          data_source: '全网规划'
          pattern: ''
          default: ''
        REALMNAME:
          name: 'Realm名'
          type: string
          maxLength: 127
          required: false
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
          data_source: '与对端协商'
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
  examples:
    set_ofccdrpara_list:
    - SGWLOTVQOSEXT: ENABLE
      PGWLOTVQOSEXT: ENABLE
      PGWLOSDQOSEXT: ENABLE
    mod_diamdictpath_list:
    - APPLICATION: GX
      DICTNO: 1
      DICTPATH: CUSTOM1
    lod_diamdict_list:
    - DICTFILESELECT: ALL
    add_pcrf_list:
    - HOSTNAME: 'pcrf1'
      REALMNAME: 'pcrf.huawei.com'
      FEATURELIST: EXTENDED_BW_NR-1&RELEASE8-1
      SUPFEANEGOSW: ENABLE
      CARRYSUPFEASW: ENABLE
    add_glbdiamrealm_list:
    - APPLICATION: GX
      CONSTBYIMSISW: DISABLE
      REALM: 'pcrf.huawei.com'
      SUPFTNEGOSW: ENABLE
      FEATURELIST: EXTENDED_BW_NR-1&RELEASE8-1
      CARRYSUPFEASW: ENABLE
    add_realmbindapn_list:
    - APN: 'isp'
      APPLICATION: GX
      CONSTBYIMSISW: DISABLE
      REALMNAME: 'pcrf.huawei.com'
      SUPFTNEGOSW: ENABLE
      FEATURELIST: EXTENDED_BW_NR-1&RELEASE8-1
      CARRYSUPFEASW: ENABLE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 配置PGW-CDR/SGW-CDR容器携带扩展QoS参数。

```jinja2
{%- for item in set_ofccdrpara_list -%}
    SET OFCCDRPARA:
    {#- --- 可选参数 --- -#}
    {%- if item.SGWLOTVQOSEXT is not none -%}
        SGWLOTVQOSEXT={{item.SGWLOTVQOSEXT}},
    {%- endif -%}
    {%- if item.PGWLOTVQOSEXT is not none -%}
        PGWLOTVQOSEXT={{item.PGWLOTVQOSEXT}},
    {%- endif -%}
    {%- if item.PGWLOSDQOSEXT is not none -%}
        PGWLOSDQOSEXT={{item.PGWLOSDQOSEXT}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 设置Diameter字典加载路径。

```jinja2
{%- for item in mod_diamdictpath_list -%}
    MOD DIAMDICTPATH:
    {#- --- 必选参数 --- -#}
    APPLICATION={{item.APPLICATION}},
    DICTNO={{item.DICTNO}},
    DICTPATH={{item.DICTPATH}},
    ;
{%- endfor -%}
```

### 加载Diameter字典。

```jinja2
{%- for item in lod_diamdict_list -%}
    LOD DIAMDICT:
    {#- --- 必选参数 --- -#}
    DICTFILESELECT={{item.DICTFILESELECT}},
    ;
{%- endfor -%}
```

### UNC主机软件加载时，会自动加载Diameter控制文件。如果文件不存在，或者文件加载失败，也可以通过命令**LOD DIAMDICT**手工加载Diameter控制文件。

### 4 配置PCRF的域信息，并使能动态协商参数及扩展QoS功能。

```jinja2
{%- for item in add_pcrf_list -%}
    ADD PCRF:
    {#- --- 必选参数 --- -#}
    HOSTNAME="{{item.HOSTNAME}}",
    REALMNAME="{{item.REALMNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.FEATURELIST is not none -%}
        FEATURELIST={{item.FEATURELIST}},
    {%- endif -%}
    {%- if item.SUPFEANEGOSW is not none -%}
        SUPFEANEGOSW={{item.SUPFEANEGOSW}},
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
```

### 5 基于IMSI/MSISDN号段或全局配置Realm，并使能动态协商参数及扩展QoS功能。

```jinja2
{%- for item in add_glbdiamrealm_list -%}
    ADD GLBDIAMREALM:
    {#- --- 必选参数 --- -#}
    APPLICATION={{item.APPLICATION}},
    CONSTBYIMSISW={{item.CONSTBYIMSISW}},
    {#- --- 可选参数 --- -#}
    {%- if item.FEATURELIST is not none -%}
        FEATURELIST={{item.FEATURELIST}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：CONSTBYIMSISW=DISABLE 时必选 --- -#}
    {%- if item.CONSTBYIMSISW == 'DISABLE' -%}
        REALM="{{item.REALM}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：APPLICATION=GX 时可选 --- -#}
    {%- if item.APPLICATION == 'GX' -%}
        {%- if item.SUPFTNEGOSW is not none -%}
            SUPFTNEGOSW={{item.SUPFTNEGOSW}},
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
```

### 6 配置APN对应的Diameter域信息，并使能动态协商参数及扩展QoS功能。

```jinja2
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
```

