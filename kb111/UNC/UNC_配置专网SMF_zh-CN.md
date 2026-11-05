---
id: ''
name: 配置专网SMF
ne_type: UNC
type: feature
description: 该任务旨在指导操作人员完成专网SMF一跳入家解决方案的配置。
risk_level: ''
doc_source: ["网络部署","业务专题","5G Core 一跳入家解决方案","一跳入家解决方案（基于非3GPP接入方案）","业务初始部署与调测","部署一跳入家","配置专网SMF"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
该任务旨在指导操作人员完成专网SMF一跳入家解决方案的配置。

## 必备事项
前提条件

前提条件

* 已完成一跳入家依赖功能的License加载。
* 已经完成与专网UPF的基础对接配置。
* 已完成一跳入家要求的移动VPN相关配置。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    mod_upnode_list:
      type: items
      properties:
        NFINSTANCENAME:
          name: 'UPF实例名称'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        TOHPSASW:
          name: '是否支持作为智家随行场景To Home会话主锚点'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '主UPF需要配置此开关参数为“ENABLE”。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_apnupselply_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '开通一跳入家业务的Home DNN。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PRIORITYFLAG:
          name: '基于优先级优选UPF开关'
          type: string
          enum:
          - INHERIT
          - DISABLE
          - ENABLE
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    mod_pnfdnn_list:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PRISWITCH:
          name: '优先级功能开关'
          type: string
          enum:
          - INHERIT
          - SPECIFIC
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: '值越小优先级越高。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_apnuprecover_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '开通一跳入家业务的Home DNN。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        MASTERUPFID:
          name: '主UPF实例名称'
          type: string
          minLength: 1
          maxLength: 255
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        HANDLINGMODE:
          name: 'UP链路故障恢复处理模式'
          type: string
          enum:
          - NOHANDLING
          - BACKMIGRATION
          required: true
          description: '设置为“BACKMIGRATION”，SMF检测到主UPF故障恢复后将Home DNN下的会话从备UPF回迁到主UPF。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        BACKUPFID:
          name: '备UPF实例名称'
          type: string
          minLength: 1
          maxLength: 255
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_apntohctrl_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '开通一跳入家业务的Home DNN。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        TOHSW:
          name: '智家随行会话开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_smffunc_list:
      type: items
      properties:
        VNGROUPDATASW:
          name: '5G LAN会话是否向UDM查询VnGroupData'
          type: string
          enum:
          - NotSupport
          - Support
          required: false
          description: '当“智家随行会话开关”配置为“ENABLE”时，此开关参数必须设置为“Support”。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_pfcppvtext_list:
      type: items
      properties:
        FEATURE:
          name: '特性名称'
          type: string
          enum:
          - QER_TYPE
          - BWM
          - UPA
          - SESSION_ROLE_TYPE
          - DNAI
          - QCI
          - ARP
          - URR_CHARGING_TYPE
          - RG
          - SID
          - HW_EVENT_MEASUREMENT
          - S_NSSAI
          - SELF_SEID
          - SGW_STATE_INFO
          - NGLAN
          - L2TP_TNL
          - L2TP_PCO
          - MultiDNN_Type
          - MultiDNN_DNN
          - MultiDNN_Snssai
          - MultiDNN_IP_Address
          - MultiDNN_Rat_Type
          - MultiDNN_DNS_Filter
          - MultiDNN_Filter_Indication
          - URR_PERF_TYPE
          - AUTH_CLASS
          - CHARGING_TYPE
          - Qos_Analysis
          - EXTEND_ROAMING_TYPE
          - EXTEND_PROXY_TYPE
          - Session_Delete_Cause
          - Qos_Experience
          - Feature_Rule
          - Qos_Quality_Indicate
          - IPE_Indicate
          - Default_Qos_Flag
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SWITCH:
          name: '私有信元携带开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '当“UP链路故障恢复处理模式”配置为“BACKMIGRATION”时，此开关参数必须设置为“ENABLE”。'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    mod_upnode_list:
    - NFINSTANCENAME: 'upf_instance_1'
      TOHPSASW: ENABLE
    set_apnupselply_list:
    - APN: 'home.area1.dnn'
      PRIORITYFLAG: ENABLE
    mod_pnfdnn_list:
    - INDEX: 1
      PRISWITCH: SPECIFIC
      PRIORITY: 1
    add_apnuprecover_list:
    - APN: 'home.area1.dnn'
      MASTERUPFID: 'upf_instance_1'
      HANDLINGMODE: BACKMIGRATION
      BACKUPFID: 'upf_instance_2'
    add_apntohctrl_list:
    - APN: 'home.area1.dnn'
      TOHSW: ENABLE
    set_smffunc_list:
    - VNGROUPDATASW: Support
    set_pfcppvtext_list:
    - FEATURE: Session_Delete_Cause
      SWITCH: ENABLE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 在SMF上使能专网UPF的一跳入家功能：设置upf\_instance\_1和upf\_instance\_2“是否支持作为智家随行场景To Home会话主锚点”参数为“使能”。

```jinja2
{%- for item in mod_upnode_list -%}
    MOD UPNODE:
    {#- --- 必选参数 --- -#}
    NFINSTANCENAME="{{item.NFINSTANCENAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.TOHPSASW is not none -%}
        TOHPSASW={{item.TOHPSASW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 配置SMF进行UPF选择时，优先选择主UPF：设置upf\_instance\_1和upf\_instance\_2“优先级功能开关”参数为“指定”，且upf\_instance\_1的“优先级”取值比upf\_instance\_2的小。

```jinja2
{%- for item in set_apnupselply_list -%}
    SET APNUPSELPLY:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.PRIORITYFLAG is not none -%}
        PRIORITYFLAG={{item.PRIORITYFLAG}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in mod_pnfdnn_list -%}
    MOD PNFDNN:
    {#- --- 必选参数 --- -#}
    INDEX={{item.INDEX}},
    {#- --- 可选参数 --- -#}
    {%- if item.PRISWITCH is not none -%}
        PRISWITCH={{item.PRISWITCH}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：PRISWITCH=SPECIFIC 时必选 --- -#}
    {%- if item.PRISWITCH == 'SPECIFIC' -%}
        PRIORITY={{item.PRIORITY}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置主UPF故障恢复后，SMF回迁业务会话至主UPF。**注意此处的主备UPF务必和2中定义的主备UPF保持一致，否则会导致无法回迁。**

```jinja2
{%- for item in add_apnuprecover_list -%}
    ADD APNUPRECOVER:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    MASTERUPFID="{{item.MASTERUPFID}}",
    HANDLINGMODE={{item.HANDLINGMODE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：HANDLINGMODE=BACKMIGRATION 时必选 --- -#}
    {%- if item.HANDLINGMODE == 'BACKMIGRATION' -%}
        BACKUPFID="{{item.BACKUPFID}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 打开SMF上的一跳入家功能开关。注意“APN”值已经在**ADD APN**中配置。

```jinja2
{%- for item in add_apntohctrl_list -%}
    ADD APNTOHCTRL:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.TOHSW is not none -%}
        TOHSW={{item.TOHSW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 设置SMF向UDM查询家庭组ID对应的VnGroupData。用户会话建立时，当UDM返回的签约数据中包括家庭组ID和SharedDataID，SMF会基于SharedDataID向UDM发送一次查询消息来再次确认该家庭组ID对应的VnGroupData，以确保家庭组ID的准确性。

```jinja2
{%- for item in set_smffunc_list -%}
    SET SMFFUNC:
    {#- --- 可选参数 --- -#}
    {%- if item.VNGROUPDATASW is not none -%}
        VNGROUPDATASW={{item.VNGROUPDATASW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 6 打开SMF上一跳入家相关的私有信元开关。

```jinja2
{%- for item in set_pfcppvtext_list -%}
    SET PFCPPVTEXT:
    {#- --- 必选参数 --- -#}
    FEATURE={{item.FEATURE}},
    {#- --- 可选参数 --- -#}
    {%- if item.SWITCH is not none -%}
        SWITCH={{item.SWITCH}},
    {%- endif -%}
    ;
{%- endfor -%}
```

