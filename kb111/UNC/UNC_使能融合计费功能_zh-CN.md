---
id: ''
name: 使能融合计费功能
ne_type: UNC
type: feature
description: 融合计费方式的选择有PCF下发、本地配置，其中，PCF下发的优先级最高。SMF本地配置融合计费开关有三种粒度：UserProfile、DNN和计费属性CC，以上优先级依次降低：  * 指定UserProfile使能融合计费开关。 * 指定DNN使能融合计费开关。 * 指定CC使能融合计费开关。  如果网络中部署了PCF控制融合计费方式，则PCF在Npcf\_SMPolicyControl\_Create Response消息中携带online/offline指示是否使能融合计费。根据用户归属属性（本地用户，漫游用户和拜访用户）配置的开关**SET CHARGECTRL**是控制SMF本地配置的融合计费开关是否有效的总开关，当总开关使能了融合计费，其他开关的配置才能生效。默认情况下，总开关同时使能在线/离线/融合计费。使能融合计费功能为SMF的融合计费方式选择图。  **图1** 融合计费方式选择图  适用于SMF。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","计费管理功能","WSFD-011206 支持融合计费","激活支持融合计费","使能融合计费功能"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
融合计费方式的选择有PCF下发、本地配置，其中，PCF下发的优先级最高。SMF本地配置融合计费开关有三种粒度：UserProfile、DNN和计费属性CC，以上优先级依次降低：* 指定UserProfile使能融合计费开关。* 指定DNN使能融合计费开关。* 指定CC使能融合计费开关。如果网络中部署了PCF控制融合计费方式，则PCF在Npcf\_SMPolicyControl\_Create Response消息中携带online/offline指示是否使能融合计费。根据用户归属属性（本地用户，漫游用户和拜访用户）配置的开关**SET CHARGECTRL**是控制SMF本地配置的融合计费开关是否有效的总开关，当总开关使能了融合计费，其他开关的配置才能生效。默认情况下，总开关同时使能在线/离线/融合计费。使能融合计费功能为SMF的融合计费方式选择图。**图1** 融合计费方式选择图适用于SMF。

## 必备事项
前提条件

* 请仔细阅读融合计费原理。
* 完成加载License。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_chargectrl_list:
      type: items
      properties:
        HOMECONVERGED:
          name: '归属地融合用户计费控制'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '用来控制是否基于用户漫游、拜访、本地属性来提供融合计费。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        VISITCONVERGED:
          name: '拜访地融合计费用户计费控制'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ROAMCONVERGED:
          name: '漫游融合计费用户计费控制'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        HOMEOFFLINE:
          name: '归属地离线用户计费控制'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VISITOFFLINE:
          name: '拜访地离线计费用户计费控制'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ROAMOFFLINE:
          name: '漫游离线计费用户计费控制'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_userprofile_list:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          maxLength: 63
          required: true
          description: '配置UserProflie。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        UPTYPE:
          name: '用户模板类型'
          type: string
          enum:
          - PCC
          - ULCL
          - UPSELECT
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: PCC
        PROFILERANGE:
          name: '模板生效范围'
          type: string
          enum:
          - ALL
          - CENTRAL
          - LOCAL
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ALL
    set_usrprofcharge_list:
      type: items
      properties:
        USRPROFNAME:
          name: '用户模板名称'
          type: string
          maxLength: 63
          required: true
          description: '配置User Profile实例的计费方式。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        CONVERGEDSW:
          name: '融合计费开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        RGAPPLIED:
          name: '业务申请上报模式'
          type: string
          enum:
          - DEFAULT
          - NOCHG
          - OFFLINERGONLY
          - ONLINERGONLY
          required: false
          description: '说明：  * 当“RGAPPLIED”配置为“DEFAULT”时，当URRGROUP下同时配置离线和在线URR，会优先选择在线URR。 * 当“RGAPPLIED”配置为“ONLINERGONLY”或“OFFLINERGONLY”时，URRGROUP下建议同时配置离线和在线URR。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        QBCSW:
          name: 'QBC计费开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_apn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '配置DNN。可通过**LST APN**命令查询已经配置的DNN。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_apnchargectrl_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          maxLength: 63
          required: true
          description: '配置DNN实例的融合计费方式。在DNN中配置INHERIT则计费方式继承基于计费属性的配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        CONVERGEDSW:
          name: '融合计费开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        RGAPPLIED:
          name: '业务申请上报模式'
          type: string
          enum:
          - DEFAULT
          - NOCHG
          - OFFLINERGONLY
          - ONLINERGONLY
          required: false
          description: '说明：  * 当“RGAPPLIED”配置为“DEFAULT”时，当URRGROUP下同时配置离线和在线URR，会优先选择在线URR。 * 当“RGAPPLIED”配置为“ONLINERGONLY”或“OFFLINERGONLY”时，URRGROUP下建议同时配置离线和在线URR。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        QBCSW:
          name: 'QBC计费开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_chargemethod_list:
      type: items
      properties:
        CHARGECHARACT:
          name: '计费属性'
          type: string
          enum:
          - DEFAULT
          - FLAT_BILLING
          - HOT_BILLING
          - NORMAL
          - PREPAID
          - SPECIFIC_VALUE
          required: true
          description: '基于用户计费属性配置融合计费。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        CCVALUE:
          name: '计费属性值'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        MASK:
          name: '计费属性掩码'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY:
          name: '计费属性优先级'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CONVERGED:
          name: '融合计费开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ENABLE
        RGAPPLIED:
          name: '业务申请上报模式'
          type: string
          enum:
          - DEFAULT
          - NOCHG
          - OFFLINERGONLY
          - ONLINERGONLY
          required: false
          description: '说明：  * 当“RGAPPLIED”配置为“DEFAULT”时，当URRGROUP下同时配置离线和在线URR，会优先选择在线URR。 * 当“RGAPPLIED”配置为“ONLINERGONLY”或“OFFLINERGONLY”时，URRGROUP下建议同时配置离线和在线URR。'
          data_source: '全网规划'
          pattern: ''
          default: DEFAULT
        QBCSW:
          name: 'QBC计费开关'
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
    set_chargectrl_list:
    - HOMECONVERGED: ENABLE
      VISITCONVERGED: ENABLE
      ROAMCONVERGED: ENABLE
      HOMEOFFLINE: ENABLE
      VISITOFFLINE: ENABLE
      ROAMOFFLINE: ENABLE
    add_userprofile_list:
    - USERPROFILENAME: 'up-test'
      UPTYPE: PCC
      PROFILERANGE: ALL
    set_usrprofcharge_list:
    - USRPROFNAME: 'up-test'
      CONVERGEDSW: ENABLE
      RGAPPLIED: ONLINERGONLY
      QBCSW: ''
    add_apn_list:
    - APN: 'apn-test'
    set_apnchargectrl_list:
    - APN: 'apn-test'
      CONVERGEDSW: ENABLE
      RGAPPLIED: ONLINERGONLY
      QBCSW: ''
    add_chargemethod_list:
    - CHARGECHARACT: SPECIFIC_VALUE
      CCVALUE: '0x400'
      MASK: '0x400'
      PRIORITY: 2
      CONVERGED: ENABLE
      RGAPPLIED: ONLINERGONLY
      QBCSW: ENABLE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 基于用户归属属性配置计费方式。

```jinja2
{%- for item in set_chargectrl_list -%}
    SET CHARGECTRL:
    {#- --- 可选参数 --- -#}
    {%- if item.HOMECONVERGED is not none -%}
        HOMECONVERGED={{item.HOMECONVERGED}},
    {%- endif -%}
    {%- if item.VISITCONVERGED is not none -%}
        VISITCONVERGED={{item.VISITCONVERGED}},
    {%- endif -%}
    {%- if item.ROAMCONVERGED is not none -%}
        ROAMCONVERGED={{item.ROAMCONVERGED}},
    {%- endif -%}
    {%- if item.HOMEOFFLINE is not none -%}
        HOMEOFFLINE={{item.HOMEOFFLINE}},
    {%- endif -%}
    {%- if item.VISITOFFLINE is not none -%}
        VISITOFFLINE={{item.VISITOFFLINE}},
    {%- endif -%}
    {%- if item.ROAMOFFLINE is not none -%}
        ROAMOFFLINE={{item.ROAMOFFLINE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### **SET CHARGECTRL**根据用户漫游属性设置计费方式，**ADD CHARGEMETHOD**根据CC属性设置计费方式，针对同一个用户，两者规划的计费方式要一致，否则用户计费会出错。例如，针对CC是normal的本地用户，如果设置本地用户进行在线计费，又设置normal用户进行离线计费，那用户最终计费结果将出错。

### 2 基于UserProfile配置计费方式。

```jinja2
{%- for item in add_userprofile_list -%}
    ADD USERPROFILE:
    {#- --- 必选参数 --- -#}
    USERPROFILENAME="{{item.USERPROFILENAME}}",
    UPTYPE={{item.UPTYPE}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：UPTYPE=PCC 时可选 --- -#}
    {%- if item.UPTYPE == 'PCC' -%}
        {%- if item.PROFILERANGE is not none -%}
            PROFILERANGE={{item.PROFILERANGE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in set_usrprofcharge_list -%}
    SET USRPROFCHARGE:
    {#- --- 必选参数 --- -#}
    USRPROFNAME="{{item.USRPROFNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.CONVERGEDSW is not none -%}
        CONVERGEDSW={{item.CONVERGEDSW}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：CONVERGEDSW=ENABLE 时可选 --- -#}
    {%- if item.CONVERGEDSW == 'ENABLE' -%}
        {%- if item.RGAPPLIED is not none -%}
            RGAPPLIED={{item.RGAPPLIED}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CONVERGEDSW=ENABLE 时可选 --- -#}
    {%- if item.CONVERGEDSW == 'ENABLE' -%}
        {%- if item.QBCSW is not none -%}
            QBCSW={{item.QBCSW}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 基于DNN配置计费方式。

```jinja2
{%- for item in add_apn_list -%}
    ADD APN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in set_apnchargectrl_list -%}
    SET APNCHARGECTRL:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.CONVERGEDSW is not none -%}
        CONVERGEDSW={{item.CONVERGEDSW}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：CONVERGEDSW=ENABLE 时可选 --- -#}
    {%- if item.CONVERGEDSW == 'ENABLE' -%}
        {%- if item.RGAPPLIED is not none -%}
            RGAPPLIED={{item.RGAPPLIED}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CONVERGEDSW=ENABLE 时可选 --- -#}
    {%- if item.CONVERGEDSW == 'ENABLE' -%}
        {%- if item.QBCSW is not none -%}
            QBCSW={{item.QBCSW}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 基于用户计费属性配置计费方式。

```jinja2
{%- for item in add_chargemethod_list -%}
    ADD CHARGEMETHOD:
    {#- --- 必选参数 --- -#}
    CHARGECHARACT={{item.CHARGECHARACT}},
    {#- --- 可选参数 --- -#}
    {%- if item.CONVERGED is not none -%}
        CONVERGED={{item.CONVERGED}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：CHARGECHARACT=SPECIFIC_VALUE 时必选 --- -#}
    {%- if item.CHARGECHARACT == 'SPECIFIC_VALUE' -%}
        CCVALUE="{{item.CCVALUE}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：CHARGECHARACT=SPECIFIC_VALUE 时可选 --- -#}
    {%- if item.CHARGECHARACT == 'SPECIFIC_VALUE' -%}
        {%- if item.MASK is not none -%}
            MASK="{{item.MASK}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CHARGECHARACT=SPECIFIC_VALUE 时可选 --- -#}
    {%- if item.CHARGECHARACT == 'SPECIFIC_VALUE' -%}
        {%- if item.PRIORITY is not none -%}
            PRIORITY={{item.PRIORITY}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CONVERGED=ENABLE 时可选 --- -#}
    {%- if item.CONVERGED == 'ENABLE' -%}
        {%- if item.RGAPPLIED is not none -%}
            RGAPPLIED={{item.RGAPPLIED}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：CONVERGED=ENABLE 时可选 --- -#}
    {%- if item.CONVERGED == 'ENABLE' -%}
        {%- if item.QBCSW is not none -%}
            QBCSW={{item.QBCSW}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

