---
id: ''
name: 激活HSS全故障业务保活特性
ne_type: UNC
type: feature
description: 为提升HSS全故障场景下的业务连续性，可以激活本特性。  适用于MME。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","容灾功能","WSFD-206102 HSS全故障业务保活","激活HSS全故障业务保活特性"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
为提升HSS全故障场景下的业务连续性，可以激活本特性。适用于MME。

## 必备事项
前提条件

* 请仔细阅读WSFD-206102 HSS全故障业务保活特性概述。
* 完成加载License。
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
          description: '开启HSS全故障业务保活特性的License开关。'
          data_source: '本端规划'
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
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_hssbypass_list:
      type: items
      properties:
        BPSW:
          name: 'HSS Bypass功能开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: '开启HSS全故障业务保活功能开关，并设置相关策略。  其中，“HSS退出Bypass恢复动作（RECOVERYACT）”用于设置用户退出HSS Bypass状态时MME执行的操作，包括先去注册用户后再标识用户退出HSS Bypass状态、先补齐与HSS的交互流程后再标识用户退出HSS Bypass状态两种方式。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        RECOVERYACT:
          name: '退出Bypass状态恢复动作'
          type: string
          enum:
          - GRACEFUL_DEREG
          - SUPPLEMENT_INTERACT
          - SUPPLEMENT_INTERACT_PRI
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SCANRATE:
          name: '整系统扫描速率(个/秒)'
          type: integer
          minimum: 0
          maximum: 10000
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SCANINTERVAL:
          name: '扫描时间间隔(秒)'
          type: integer
          minimum: 1
          maximum: 600
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        AUTOEXITSW:
          name: 'HSS Bypass自动退出开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: '此处以自动退出HSS Bypass状态举例。如果期望配置不自动退出HSS Bypass状态，则参数值需要配置为“OFF”，后续需要通过手动执行**STR HSSBPEXIT**命令触发用户退出HSS Bypass状态。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IWKSUBEN:
          name: '互操作签约自学习'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: '配置用户在发生Inter MME互操作流程中进入HSS Bypass的状态时，是否支持用户使用互操作时用户已有的会话生成用户最小APN签约信息，用于后续会话重建。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_hssbpapnsub_list:
      type: items
      properties:
        APNSUBIDX:
          name: 'APN本地签约索引'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: '增加HSS Bypass后的最小APN签约数据。HSS全故障后，MME无法从HSS侧获取签约数据，因此必须在MME配置用户签约数据。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        APNNI:
          name: 'APNNI'
          type: string
          maxLength: 62
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PDNTYPE:
          name: 'PDN类型'
          type: string
          enum:
          - IPV4
          - IPV4_AND_IPV6
          - IPV4_OR_IPv6
          - IPV6
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: IPV4
        APNAMBRULK:
          name: '上行APN AMBR （kbps）'
          type: integer
          minimum: 1
          maximum: 65000000
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        APNAMBRDLK:
          name: '下行APN AMBR （kbps）'
          type: integer
          minimum: 1
          maximum: 65000000
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        QCI:
          name: 'QCI'
          type: integer
          minimum: 0
          maximum: 254
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PRIORITY:
          name: '控制优先级'
          type: integer
          minimum: 1
          maximum: 15
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_hssbpapngrp_list:
      type: items
      properties:
        APNGRPID:
          name: 'APN群组ID'
          type: integer
          minimum: 0
          maximum: 511
          required: true
          description: '增加HSS Bypass后的最小APN签约数据群组。HSS全故障后，MME无法从HSS侧获取签约数据，因此必须在MME配置用户签约数据。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        APNSUBIDX:
          name: 'APN本地签约索引'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        DEFAULTAPN:
          name: '是否默认APN'
          type: string
          enum:
          - NO
          - YES
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: NO
    add_hssbpusrsub_list:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - FOREIGN_USER
          - HOME_USER
          - IMSI_PREFIX
          required: true
          description: '增加HSS Bypass后的最小用户签约数据。HSS全故障后，MME无法从HSS侧获取签约数据，因此必须在MME配置用户签约数据。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        APNGRPID:
          name: 'APN群组ID'
          type: integer
          minimum: 0
          maximum: 511
          required: true
          description: ''
          data_source: '本端规划'
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
    add_hssbpfaultcode_list:
      type: items
      properties:
        RANGE:
          name: '生效范围'
          type: string
          enum:
          - ALL
          - KEYWORD
          - OFFICE
          required: true
          description: '当HSS/DRA全故障后，系统收到HSS/DRA返回某个特定原因值时，希望用户进入HSS Bypass状态，可配置该原因值为HSS Bypass原因值。   * 当仅针对部分HSS指定错误码时，可以将“生效范围（RANGE）”设置为“OFFICE（局向）”，并增加“对端主机名（HOSTNAME）”。 * 当需要根据HSS的主机名称中的某些关键字来识别故障的主机，并为其指定错误码时，可以将“生效范围（RANGE）”设置为“KEYWORD（对端主机名关键字）”，并增加“对端主机名关键字（KEYWORD）”。 * “生效范围（RANGE）”的优先级从高到低为：“OFFICE（局向）”，“KEYWORD（对端主机名关键字）”，“ALL（整系统）”。 * “生效范围（RANGE）”的优先级即为命令的优先级。当系统收到HSS/DRA返回某个特定原因值时，按“生效范围（RANGE）”优先级匹配上某条配置后，不论“故障码（FAULTECODE）”是否匹配上，都不会继续向低优先级继续匹配。   说明：  故障码需要与对端HSS/DRA确认后进行配置。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        FAULTCODE:
          name: '故障码'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        KEYWORD:
          name: '对端主机名关键字'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        HOSTNAME:
          name: '对端主机名'
          type: string
          maxLength: 127
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_dmfovercode_list:
      type: items
      properties:
        ERRCODE:
          name: '触发重选路由的错误码'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: '可选，域路由组网方式下，当希望MME收到对端的错误码后进行路由重选时，配置重选路由的错误码。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_hssbpofc_list:
      type: items
      properties:
        HOSTNAME:
          name: '对端主机名'
          type: string
          maxLength: 127
          required: true
          description: '可选，当所有HSS已经故障但MME还未检测到时，可配置故障的HSS，以便使用户可以进入HSS Bypass状态。  当HSS全部故障时，可以将“对端主机名（HOSTNAME）”配置为\*。'
          data_source: '全网规划'
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
          description: '由于链路故障等原因发送Diameter消息失败时，使MME能够接收失败响应并进行响应处理，避免直连DRA故障场景无法触发用户进入HSS Bypass。'
          data_source: '本端规划'
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
    set_softparaofbit_list_3:
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
          description: '可选，配置MME在匹配用户当前安全上下文时，忽略TSC标识。解决由于终端携带TSC错误导致用户安全检查失败而无法接入的问题。'
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
    add_mmecharact_list:
      type: items
      properties:
        RANGE:
          name: '对端设备范围'
          type: string
          enum:
          - ALL_MME
          - COMB_AMF
          - SPECIAL_MME
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPTYPE:
          name: 'IP地址类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_mmecharact_list:
      type: items
      properties:
        RANGE:
          name: '对端设备范围'
          type: string
          enum:
          - ALL_MME
          - COMB_AMF
          - SPECIAL_MME
          required: true
          description: '配置S10/N26接口向MME/AMF传递MSISDN的消息。  说明：  配置“是否在Private Extension信元传递MSISDN”参数前需确认对端AMF/MME为华为设备，且支持私有信元携带MSISDN。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        MSISDNSW:
          name: '是否传递MSISDN'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PVTMSISDNSW:
          name: '是否在Private Extension信元传递MSISDN'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPTYPE:
          name: 'IP地址类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    str_hssbpexit_list:
      type: items
      properties:
        RECOVERYACT:
          name: '退出Bypass状态恢复动作'
          type: string
          enum:
          - FORCED_DEREG
          - GRACEFUL_DEREG
          - SUPPLEMENT_INTERACT
          - SUPPLEMENT_INTERACT_PRI
          required: true
          description: '配置退出HSS Bypass状态的方式。'
          data_source: '全网规划'
          pattern: ''
          default: GRACEFUL_DEREG
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV2HSSBP01'
      SWITCH: ENABLE
    set_hssbypass_list:
    - BPSW: ON
      RECOVERYACT: GRACEFUL_DEREG
      SCANRATE: 0
      SCANINTERVAL: 600
      AUTOEXITSW: ON
      IWKSUBEN: ON
    add_hssbpapnsub_list:
    - APNSUBIDX: 1
      APNNI: 'cmnet'
      PDNTYPE: IPV4
      APNAMBRULK: 1000
      APNAMBRDLK: 1000
      QCI: 9
      PRIORITY: 1
    add_hssbpapngrp_list:
    - APNGRPID: 1
      APNSUBIDX: 1
      DEFAULTAPN: YES
    add_hssbpusrsub_list:
    - SUBRANGE: ALL_USER
      APNGRPID: 1
      IMSIPRE: ''
    add_hssbpfaultcode_list:
    - RANGE: ALL
      FAULTCODE: 3002
      KEYWORD: 'DRA'
      HOSTNAME: ''
    add_dmfovercode_list:
    - ERRCODE: 3002
    add_hssbpofc_list:
    - HOSTNAME: 'HSS_01'
    set_softparaofbit_list:
    - DT: BYTE_EX_B
      PARANUM: 324
      VALUE: VALUE_1
      POSITION: 1
    set_softparaofbit_list_3:
    - DT: BYTE_EX_B
      PARANUM: 47
      VALUE: VALUE_1
      POSITION: 3
    add_mmecharact_list:
    - RANGE: ''
      IPTYPE: ''
    mod_mmecharact_list:
    - RANGE: ALL_MME
      MSISDNSW: YES
      PVTMSISDNSW: YES
      IPTYPE: ''
    str_hssbpexit_list:
    - RECOVERYACT: GRACEFUL_DEREG
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

### 2 配置HSS Bypass功能开关和策略。

```jinja2
{%- for item in set_hssbypass_list -%}
    SET HSSBYPASS:
    {#- --- 可选参数 --- -#}
    {%- if item.BPSW is not none -%}
        BPSW={{item.BPSW}},
    {%- endif -%}
    {%- if item.RECOVERYACT is not none -%}
        RECOVERYACT={{item.RECOVERYACT}},
    {%- endif -%}
    {%- if item.SCANRATE is not none -%}
        SCANRATE={{item.SCANRATE}},
    {%- endif -%}
    {%- if item.SCANINTERVAL is not none -%}
        SCANINTERVAL={{item.SCANINTERVAL}},
    {%- endif -%}
    {%- if item.AUTOEXITSW is not none -%}
        AUTOEXITSW={{item.AUTOEXITSW}},
    {%- endif -%}
    {%- if item.IWKSUBEN is not none -%}
        IWKSUBEN={{item.IWKSUBEN}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 增加HSS Bypass后的最小签约数据。

```jinja2
{%- for item in add_hssbpapnsub_list -%}
    ADD HSSBPAPNSUB:
    {#- --- 必选参数 --- -#}
    APNSUBIDX={{item.APNSUBIDX}},
    APNNI="{{item.APNNI}}",
    APNAMBRULK={{item.APNAMBRULK}},
    APNAMBRDLK={{item.APNAMBRDLK}},
    QCI={{item.QCI}},
    PRIORITY={{item.PRIORITY}},
    {#- --- 可选参数 --- -#}
    {%- if item.PDNTYPE is not none -%}
        PDNTYPE={{item.PDNTYPE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_hssbpapngrp_list -%}
    ADD HSSBPAPNGRP:
    {#- --- 必选参数 --- -#}
    APNGRPID={{item.APNGRPID}},
    APNSUBIDX={{item.APNSUBIDX}},
    DEFAULTAPN={{item.DEFAULTAPN}},
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_hssbpusrsub_list -%}
    ADD HSSBPUSRSUB:
    {#- --- 必选参数 --- -#}
    SUBRANGE={{item.SUBRANGE}},
    APNGRPID={{item.APNGRPID}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
    {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
        IMSIPRE="{{item.IMSIPRE}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 当希望HSS/DRA全故障后，系统收到HSS/DRA返回某个特定原因值时，用户进入HSS Bypass状态，可通过此命令配置该原因值为HSS Bypass原因值，需配置该原因值为HSS Bypass原因值。

```jinja2
{%- for item in add_hssbpfaultcode_list -%}
    ADD HSSBPFAULTCODE:
    {#- --- 必选参数 --- -#}
    RANGE={{item.RANGE}},
    FAULTCODE={{item.FAULTCODE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：RANGE=KEYWORD 时必选 --- -#}
    {%- if item.RANGE == 'KEYWORD' -%}
        KEYWORD="{{item.KEYWORD}}",
    {%- endif -%}
    {#- --- 条件必选：RANGE=OFFICE 时必选 --- -#}
    {%- if item.RANGE == 'OFFICE' -%}
        HOSTNAME="{{item.HOSTNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 （可选）域路由组网方式下，当希望MME收到对端的错误码后进行路由重选时，需要配置触发重选路由的错误码。

```jinja2
{%- if is_optional_config_reroute_error_code and is_scenario_domain_routing -%}
    {%- for item in add_dmfovercode_list -%}
        ADD DMFOVERCODE:
        {#- --- 必选参数 --- -#}
        ERRCODE={{item.ERRCODE}},
        ;
    {%- endfor -%}
{%- endif -%}
```

### 6 （可选）当所有HSS已经故障但MME还未检测到时，可配置故障的HSS。

```jinja2
{%- if is_optional_config_fault_hss and is_scenario_manual_hss_fault -%}
    {%- for item in add_hssbpofc_list -%}
        ADD HSSBPOFC:
        {#- --- 必选参数 --- -#}
        HOSTNAME="{{item.HOSTNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

### 7 由于链路故障等原因发送Diameter消息失败时，开启软参BYTE\_EX\_B324 bit1使MME能够接收失败响应并进行响应处理，避免直连DRA故障场景无法触发用户进入HSS Bypass。

```jinja2
{%- for item in set_softparaofbit_list -%}
    SET SOFTPARAOFBIT:
    {#- --- 必选参数 --- -#}
    DT={{item.DT}},
    PARANUM={{item.PARANUM}},
    VALUE={{item.VALUE}},
    POSITION={{item.POSITION}},
    ;
{%- endfor -%}
```

### 8 （可选）开启软参BYTE\_EX\_B47 bit3，配置MME在匹配用户当前安全上下文时，忽略TSC标识。解决由于终端携带TSC错误导致用户安全检查失败而无法接入的问题。

```jinja2
{%- if is_optional_enable_ignore_tsc -%}
    {%- for item in set_softparaofbit_list_3 -%}
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

### 9 配置S10/N26接口向MME/AMF传递MSISDN的消息。

```jinja2
{%- for item in add_mmecharact_list -%}
    ADD MMECHARACT:
    {#- --- 必选参数 --- -#}
    RANGE={{item.RANGE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：RANGE=SPECIAL_MME 时必选 --- -#}
    {%- if item.RANGE == 'SPECIAL_MME' -%}
        IPTYPE={{item.IPTYPE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in mod_mmecharact_list -%}
    MOD MMECHARACT:
    {#- --- 必选参数 --- -#}
    RANGE={{item.RANGE}},
    {#- --- 可选参数 --- -#}
    {%- if item.MSISDNSW is not none -%}
        MSISDNSW={{item.MSISDNSW}},
    {%- endif -%}
    {%- if item.PVTMSISDNSW is not none -%}
        PVTMSISDNSW={{item.PVTMSISDNSW}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：RANGE=SPECIAL_MME 时必选 --- -#}
    {%- if item.RANGE == 'SPECIAL_MME' -%}
        IPTYPE={{item.IPTYPE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 10 手动触发用户退出HSS Bypass状态。

```jinja2
{%- for item in str_hssbpexit_list -%}
    STR HSSBPEXIT:
    {#- --- 必选参数 --- -#}
    RECOVERYACT={{item.RECOVERYACT}},
    ;
{%- endfor -%}
```

