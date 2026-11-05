---
id: ''
name: 激活VoLTE紧急呼叫（适用于MME）
ne_type: UEG
type: feature
description: 本操作指导介绍在运行网络中激活VoLTE紧急呼叫特性的操作过程。  适用于MME。
tags: []
risk_level: ''
doc_source:
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网煤矿场景，入驻式）","配置基础业务","在UEG上配置业务数据","语音功能配置","MME&AMF&GW-C&SMF配置","VoLTE基本功能","激活VoLTE紧急呼叫（适用于MME）"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网核电场景，入驻式）","配置基础业务","在UEG上配置业务数据","语音功能配置","MME&AMF&GW-C&SMF配置","VoLTE基本功能","激活VoLTE紧急呼叫（适用于MME）"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网通用场景，入驻式）","配置基础业务","在UEG上配置业务数据","语音功能配置","MME&AMF&GW-C&SMF配置","VoLTE基本功能","激活VoLTE紧急呼叫（适用于MME）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活VoLTE紧急呼叫特性的操作过程。适用于MME。

## 必备事项
前提条件

* 请仔细阅读GWFD-025403 VoLTE紧急呼叫。
* 已完成加载License。
* 部署VoLTE紧急呼叫特性需要在MME、SGW-C、PGW-C、MSC、eNodeB等网元上首先完成基本业务的数据配置。
* 运营商已经通过**ADD HPLMN**、**ADD MVNONET**或**ADD CONNECTPLMN**配置了运营商标识（MNOID/MVNOID/NOID）。
* VOLTE紧急呼叫号码下发会影响终端存储的紧急呼叫号码列表，当终端回落到2/3G发起紧急呼叫时，需要MSC配置紧急呼叫类型和对应号码的映射关系，详细配置请咨询MSC技术支持。
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
    set_mmfunc_list:
      type: items
      properties:
        EMNUM:
          name: '是否支持紧急号码'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: '开启紧急呼叫功能。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_emgcnum_list:
      type: items
      properties:
        MCC:
          name: '移动国家码'
          type: string
          maxLength: 3
          required: true
          description: '配置紧急号码信息。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ESC:
          name: '紧急服务分类'
          type: string
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NUM:
          name: '紧急呼叫号码'
          type: string
          maxLength: 80
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_softparaofbit_list:
      type: items
      properties:
        DT:
          name: '参数类型'
          type: string
          enum:
          - BYTE
          - BYTE_EX
          - BYTE_EX_B
          - DWORD
          - DWORD_EX
          - DWORD_EX_B
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PARANUM:
          name: '参数索引'
          type: integer
          minimum: 1
          maximum: 512
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VALUE:
          name: '参数值'
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
          name: '比特位'
          type: integer
          minimum: 1
          maximum: 32
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_softparaofbit_list_1:
      type: items
      properties:
        DT:
          name: '参数类型'
          type: string
          enum:
          - BYTE
          - BYTE_EX
          - BYTE_EX_B
          - DWORD
          - DWORD_EX
          - DWORD_EX_B
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PARANUM:
          name: '参数索引'
          type: integer
          minimum: 1
          maximum: 512
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VALUE:
          name: '参数值'
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
          name: '比特位'
          type: integer
          minimum: 1
          maximum: 32
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_emgcfg_list:
      type: items
      properties:
        NOID:
          name: '运营商标识'
          type: integer
          minimum:
          - 0
          - 128
          maximum:
          - 64
          - 254
          required: true
          description: '配置紧急呼叫功能参数。  该NOID必须已经通过****ADD MNO****的“MNOID”或者****ADD MVNO****的“MVNOID”配置。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        EMGMODE:
          name: '紧急承载创建模式'
          type: string
          enum:
          - ALLUE
          - AUTHUE
          - IMSIUE
          - VALIDUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: AUTHUE
        EMGAPN:
          name: '紧急APN'
          type: string
          maxLength: 62
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ULAPNAMBR:
          name: '紧急APN的上行APN AMBR速率（kbit/s）'
          type: integer
          minimum: 1
          maximum: 256000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 500
        DLAPNAMBR:
          name: '紧急APN的下行APN AMBR速率（kbit/s）'
          type: integer
          minimum: 1
          maximum: 256000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 500
        QCI:
          name: '紧急承载的QCI'
          type: integer
          minimum: 5
          maximum: 9
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 5
        ARPPRL:
          name: '紧急ARP优先级级别'
          type: integer
          minimum: 1
          maximum: 15
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ARPPCI:
          name: '紧急ARP的Pre-emption Capability'
          type: string
          enum:
          - NO
          - YES
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ARPPVI:
          name: '紧急ARP的Pre-emption Vulnerability'
          type: string
          enum:
          - NO
          - YES
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_pgwestnsr_list:
      type: items
      properties:
        IPT:
          name: 'PGW的IP地址类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: '配置E-STN-SR和PGW-C关系。  与华为MSC设备对接才需要配置。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PGWIPV4:
          name: 'PGW的IPV4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4MSK:
          name: 'PGW的IPV4地址掩码'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ESTNSR:
          name: 'SRVCC的紧急会话转移号码'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_emm_list:
      type: items
      properties:
        HPT3413:
          name: '高优先级业务的T3413（s）'
          type: integer
          minimum: 1
          maximum: 12
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HPN3413:
          name: '高优先级业务的N3413（times）'
          type: integer
          minimum: 0
          maximum: 10
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HPPAGINGDELTA:
          name: '高优先级业务的重寻呼间隔递增值（s）'
          type: integer
          minimum: 0
          maximum: 20
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_s1imeicfg_list:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - IMSI_PREFIX
          - IMSI_RANGE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GETIMEIPLC:
          name: 'IMEI获取策略'
          type: string
          enum:
          - IMEI
          - IMEISV
          - NO
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
    mod_hplmn_list:
      type: items
      properties:
        MCC:
          name: '移动国家码'
          type: string
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MNC:
          name: '移动网号'
          type: string
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EMCBS:
          name: '是否允许紧急呼叫业务'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_connectplmn_list:
      type: items
      properties:
        MCC:
          name: '移动国家码'
          type: string
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MNC:
          name: '移动网号'
          type: string
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EMCBS:
          name: '是否允许紧急呼叫业务'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    rmv_mvnonet_list:
      type: items
      properties:
        MVNOID:
          name: 'MVNO标识'
          type: integer
          minimum: 1
          maximum: 64
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_mvnonet_list:
      type: items
      properties:
        MVNOMCC:
          name: 'MVNO移动国家码'
          type: string
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MVNOMNC:
          name: 'MVNO移动网号'
          type: string
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MATCHIMSI:
          name: '匹配IMSI'
          type: string
          maxLength: 10
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MVNOCC:
          name: 'MVNO 国家码'
          type: string
          maxLength: 6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MVNOID:
          name: 'MVNO标识'
          type: integer
          minimum: 1
          maximum: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EMCBS:
          name: '是否允许紧急呼叫业务'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV2VLEC01'
      SWITCH: ENABLE
    set_mmfunc_list:
    - EMNUM: YES
    add_emgcnum_list:
    - MCC: '123'
      ESC: POLICE-0&AMBULANCE-0&FIREBRIGADE-1&MARINEGUARD-0&MOUNTAIN-0
      NUM: '119'
    set_softparaofbit_list:
    - DT: DWORD_EX
      PARANUM: 6
      VALUE: VALUE_0
      POSITION: 10
    set_softparaofbit_list_1:
    - DT: DWORD_EX
      PARANUM: 6
      VALUE: VALUE_0
      POSITION: 11
    add_emgcfg_list:
    - NOID: 128
      EMGMODE: ALLUE
      EMGAPN: 'EMG'
      ULAPNAMBR: 10000
      DLAPNAMBR: 10000
      QCI: 5
      ARPPRL: 1
      ARPPCI: YES
      ARPPVI: NO
    add_pgwestnsr_list:
    - IPT: IPV4
      PGWIPV4: '10.10.10.10'
      IPV4MSK: '255.255.255.255'
      ESTNSR: '11111'
    set_emm_list:
    - HPT3413: 2
      HPN3413: 4
      HPPAGINGDELTA: 0
    add_s1imeicfg_list:
    - SUBRANGE: IMSI_PREFIX
      IMSIPRE: '123456'
      GETIMEIPLC: IMEISV
    mod_hplmn_list:
    - MCC: '123'
      MNC: '00'
      EMCBS: NO
    mod_connectplmn_list:
    - MCC: '123'
      MNC: '00'
      EMCBS: NO
    rmv_mvnonet_list:
    - MVNOID: 1
    add_mvnonet_list:
    - MVNOMCC: '123'
      MVNOMNC: '00'
      MATCHIMSI: '111'
      MVNOCC: '860'
      MVNOID: 1
      EMCBS: NO
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

### 3 配置紧急号码信息。

### 紧急呼叫号码必须是运营商已经规划的号码，需要正确配置。配置错误可能导致UE的紧急呼叫接入错误，例如：

### 将非紧急呼叫号码配置为紧急呼叫号码，用户被接入至政府部门。

### 紧急服务分类配置错误，用户被错误接入其他政府部门。

### VOLTE紧急呼叫号码下发会影响终端存储的紧急呼叫号码列表，当终端回落到2/3G发起紧急呼叫时，需要MSC配置紧急呼叫类型和对应号码的映射关系，详细配置请咨询MSC技术支持。

```jinja2
{%- for item in set_mmfunc_list -%}
    SET MMFUNC:
    {#- --- 可选参数 --- -#}
    {%- if item.EMNUM is not none -%}
        EMNUM={{item.EMNUM}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_emgcnum_list -%}
    ADD EMGCNUM:
    {#- --- 必选参数 --- -#}
    MCC="{{item.MCC}}",
    ESC={{item.ESC}},
    NUM="{{item.NUM}}",
    ;
{%- endfor -%}
```

### 4 配置下发紧急号码。

#### 4.1 需要在GPRS/UMTS网络下发紧急号码时，设置软参DWORD\_EX6 BIT10为0。

```jinja2
{%- if is_scenario_gprs_umts -%}
    {%- for item in set_softparaofbit_list -%}
        SET SOFTPARAOFBIT:
        {#- --- 必选参数 --- -#}
        DT={{item.DT}},
        PARANUM={{item.PARANUM}},
        VALUE={{item.VALUE}},
        POSITION={{item.POSITION}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.2 需要在EPS网络下发紧急号码时：

##### 4.2.1 如果仅对支持VoLTE语音业务的用户下发紧急呼叫号码，则将DWORD\_EX6 BIT11配置为0，将DWORD\_EX12 BIT16配置为1。

```jinja2
{%- if is_scenario_eps and is_scenario_volte_users_only -%}
    {%- for item in set_softparaofbit_list_1 -%}
        SET SOFTPARAOFBIT:
        {#- --- 必选参数 --- -#}
        DT={{item.DT}},
        PARANUM={{item.PARANUM}},
        VALUE={{item.VALUE}},
        POSITION={{item.POSITION}},
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 4.2.2 如果对EPS网络下的所有用户下发紧急呼叫号码，则将DWORD\_EX6 BIT11配置为0。

### 5 配置紧急呼叫功能参数。

```jinja2
{%- for item in add_emgcfg_list -%}
    ADD EMGCFG:
    {#- --- 必选参数 --- -#}
    NOID={{item.NOID}},
    EMGAPN="{{item.EMGAPN}}",
    ARPPRL={{item.ARPPRL}},
    ARPPCI={{item.ARPPCI}},
    ARPPVI={{item.ARPPVI}},
    {#- --- 可选参数 --- -#}
    {%- if item.EMGMODE is not none -%}
        EMGMODE={{item.EMGMODE}},
    {%- endif -%}
    {%- if item.ULAPNAMBR is not none -%}
        ULAPNAMBR={{item.ULAPNAMBR}},
    {%- endif -%}
    {%- if item.DLAPNAMBR is not none -%}
        DLAPNAMBR={{item.DLAPNAMBR}},
    {%- endif -%}
    {%- if item.QCI is not none -%}
        QCI={{item.QCI}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 6 **可选：**配置E-STN-SR和PGW-C关系。

```jinja2
{%- if is_optional_estnsr_pgw_c_relation -%}
    {%- for item in add_pgwestnsr_list -%}
        ADD PGWESTNSR:
        {#- --- 必选参数 --- -#}
        IPT={{item.IPT}},
        ESTNSR="{{item.ESTNSR}}",
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IPT=IPV4 时必选 --- -#}
        {%- if item.IPT == 'IPV4' -%}
            PGWIPV4="{{item.PGWIPV4}}",
        {%- endif -%}
        {#- --- 条件必选：IPT=IPV4 时必选 --- -#}
        {%- if item.IPT == 'IPV4' -%}
            IPV4MSK="{{item.IPV4MSK}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 与华为MSC设备对接才需要配置此步骤。

### 7 **可选：**配置优化的寻呼参数。

```jinja2
{%- if is_optional_optimized_paging_params -%}
    {%- for item in set_emm_list -%}
        SET EMM:
        {#- --- 可选参数 --- -#}
        {%- if item.HPT3413 is not none -%}
            HPT3413={{item.HPT3413}},
        {%- endif -%}
        {%- if item.HPN3413 is not none -%}
            HPN3413={{item.HPN3413}},
        {%- endif -%}
        {%- if item.HPPAGINGDELTA is not none -%}
            HPPAGINGDELTA={{item.HPPAGINGDELTA}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 紧急呼叫的寻呼重发采用优化的寻呼参数，详情参见特性GWFD-025401 VoLTE基础语音业务。

### 8 **可选：**获取紧急呼叫用户IMEI信息。

```jinja2
{%- if is_optional_get_imei_info -%}
    {%- for item in add_s1imeicfg_list -%}
        ADD S1IMEICFG:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        {#- --- 可选参数 --- -#}
        {%- if item.GETIMEIPLC is not none -%}
            GETIMEIPLC={{item.GETIMEIPLC}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
        {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
            IMSIPRE="{{item.IMSIPRE}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 为保证“有USIM卡的受限用户”在鉴权失败的场景下紧急呼叫的SRVCC切换成功，建议MME开启获取IMEI信息功能。

### 9 **可选：**配置PLMN的用户禁止使用VoLTE紧急呼叫业务。

### 如果某PLMN的用户在PS域无法完成VoLTE紧急呼叫，需要配置此步骤使该类用户在CS域重新发起紧急呼叫业务。否则跳过此步骤。

#### 9.1 如果是归属地PLMN的用户，则执行如下命令配置。

```jinja2
{%- if is_optional_plmn_volte_emergency_restriction and is_scenario_home_plmn -%}
    {%- for item in mod_hplmn_list -%}
        MOD HPLMN:
        {#- --- 必选参数 --- -#}
        MCC="{{item.MCC}}",
        MNC="{{item.MNC}}",
        {#- --- 可选参数 --- -#}
        {%- if item.EMCBS is not none -%}
            EMCBS={{item.EMCBS}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 9.2 如果是互联PLMN的用户，则执行如下命令配置。

```jinja2
{%- if is_optional_plmn_volte_emergency_restriction and is_scenario_interconnect_plmn -%}
    {%- for item in mod_connectplmn_list -%}
        MOD CONNECTPLMN:
        {#- --- 必选参数 --- -#}
        MCC="{{item.MCC}}",
        MNC="{{item.MNC}}",
        {#- --- 可选参数 --- -#}
        {%- if item.EMCBS is not none -%}
            EMCBS={{item.EMCBS}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 9.3 如果是MVNO网络的用户，则执行如下命令配置。

```jinja2
{%- if is_optional_plmn_volte_emergency_restriction and is_scenario_mvno -%}
    {%- for item in rmv_mvnonet_list -%}
        RMV MVNONET:
        {#- --- 可选参数 --- -#}
        {%- if item.MVNOID is not none -%}
            MVNOID={{item.MVNOID}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_optional_plmn_volte_emergency_restriction and is_scenario_mvno -%}
    {%- for item in add_mvnonet_list -%}
        ADD MVNONET:
        {#- --- 必选参数 --- -#}
        MVNOMCC="{{item.MVNOMCC}}",
        MVNOMNC="{{item.MVNOMNC}}",
        MVNOCC="{{item.MVNOCC}}",
        MVNOID={{item.MVNOID}},
        {#- --- 可选参数 --- -#}
        {%- if item.MATCHIMSI is not none -%}
            MATCHIMSI="{{item.MATCHIMSI}}",
        {%- endif -%}
        {%- if item.EMCBS is not none -%}
            EMCBS={{item.EMCBS}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

