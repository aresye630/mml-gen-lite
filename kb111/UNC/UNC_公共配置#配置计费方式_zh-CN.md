---
id: ''
name: 配置计费方式
ne_type: UNC
type: feature
description: 本指导用于描述UNC同时支持离线计费和在线计费的操作过程。  **GGSN-C/PGW-C/SMF**  对于SMF，计费方式的选择有PCF下发和本地配置，PCF下发的优先级高于本地配置。对于GGSN-C/PGW-C，计费方式的选择有PCRF下发、RADIUS Server下发和本地配置，优先级从高到低依次为：PCRF下发>RADIUS Server下发>本地配置。  GGSN-C/PGW-C/SMF本地配置计费方式开关有三种粒度：User Profile、DNN和计费属性，优先级依次降低。  根据用户归属属性（本地用户，漫游用户和拜访用户）配置的开关**SET CHARGECTRL**是控制GGSN-C/PGW-C/SMF本地配置的计费开关是否有效的总开关，当总开关使能了某种计费，其他开关的配置才能生效。默认情况下，总开关同时使能在线/离线/融合计费。  **SGW-C**  对于SGW-C，计费方式要通过本地进行配置。SGW-C本地配置计费开关有三种粒度：IMSI/MSISDN号段组、APN和计费属性，优先级依次降低。根据用户归属属性（本地用户，漫游用户和拜访用户）配置的开关**SET SGWCHARGECFG**是控制SGW-C本地配置的计费开关是否有效的总开关，当总开关使能了离线计费，其他开关的配置才能生效。默认情况下，漫游用户和拜访用户使能离线计费，本地用户不使能离线计费。
risk_level: ''
doc_source: ["网络部署","业务专题","5G Core 计费解决方案","计费解决方案概述","计费方案部署与调测","方案二：部署NCG且基于传统Ga/Gy接口计费组网方案","SMF配置","公共配置","配置计费方式"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本指导用于描述UNC同时支持离线计费和在线计费的操作过程。**GGSN-C/PGW-C/SMF**对于SMF，计费方式的选择有PCF下发和本地配置，PCF下发的优先级高于本地配置。对于GGSN-C/PGW-C，计费方式的选择有PCRF下发、RADIUS Server下发和本地配置，优先级从高到低依次为：PCRF下发>RADIUS Server下发>本地配置。GGSN-C/PGW-C/SMF本地配置计费方式开关有三种粒度：User Profile、DNN和计费属性，优先级依次降低。根据用户归属属性（本地用户，漫游用户和拜访用户）配置的开关**SET CHARGECTRL**是控制GGSN-C/PGW-C/SMF本地配置的计费开关是否有效的总开关，当总开关使能了某种计费，其他开关的配置才能生效。默认情况下，总开关同时使能在线/离线/融合计费。**SGW-C**对于SGW-C，计费方式要通过本地进行配置。SGW-C本地配置计费开关有三种粒度：IMSI/MSISDN号段组、APN和计费属性，优先级依次降低。根据用户归属属性（本地用户，漫游用户和拜访用户）配置的开关**SET SGWCHARGECFG**是控制SGW-C本地配置的计费开关是否有效的总开关，当总开关使能了离线计费，其他开关的配置才能生效。默认情况下，漫游用户和拜访用户使能离线计费，本地用户不使能离线计费。

## 必备事项
前提条件

* 请仔细阅读Ga/Gy接口离线/在线计费。
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HOMEONLINE:
          name: '归属地在线用户计费控制'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '开启GGSN-C/PGW-C/SMF计费总开关，配置漫游用户、拜访用户、本地用户均开启在线计费和离线计费，不开启融合计费。'
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
        VISITONLINE:
          name: '拜访地在线计费用户计费控制'
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
        VISITCONVERGED:
          name: '拜访地融合计费用户计费控制'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ROAMONLINE:
          name: '漫游在线计费用户计费控制'
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
        ROAMCONVERGED:
          name: '漫游融合计费用户计费控制'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_usrprofcharge_list:
      type: items
      properties:
        USRPROFNAME:
          name: '用户模板名称'
          type: string
          maxLength: 63
          required: true
          description: '（可选）基于用户模板配置GGSN-C/PGW-C/SMF的计费方式。在全局配置不能满足业务要求时，可执行本命令基于用户模板配置计费方式。  说明：  * “ONLINESW”和“OFFLINESW”配置“INHERIT”，表示计费方式继承基于DNN的配置。 * 本示例配置User Profile为up-test的用户在线计费开关和离线计费开关继承上一级配置，不开启融合计费。请根据业务实际需要进行配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        ONLINESW:
          name: '在线计费开关'
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
        OFFLINESW:
          name: '离线计费开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: ''
          data_source: ''
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
          data_source: ''
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
        RGAPPLIED:
          name: '业务申请上报模式'
          type: string
          enum:
          - DEFAULT
          - NOCHG
          - OFFLINERGONLY
          - ONLINERGONLY
          required: false
          description: ''
          data_source: ''
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
          description: '（可选）基于DNN配置GGSN-C/PGW-C/SMF的计费方式。在全局配置不能满足业务要求时，可执行本命令基于DNN配置计费方式。  说明：  * “ONLINESW”和“OFFLINESW”配置“INHERIT”，表示计费方式继承基于计费属性的配置。 * 本示例配置APN为apn-test的用户在线计费开关、离线计费开关均继承上一级配置，融合计费开关关闭。请根据业务实际需要进行配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        ONLINESW:
          name: '在线计费开关'
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
        OFFLINESW:
          name: '离线计费开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: ''
          data_source: ''
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
          data_source: ''
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
        RGAPPLIED:
          name: '业务申请上报模式'
          type: string
          enum:
          - DEFAULT
          - NOCHG
          - OFFLINERGONLY
          - ONLINERGONLY
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
          description: '（可选）基于用户计费属性配置GGSN-C/PGW-C/SMF的计费方式。在全局配置不能满足业务要求时，可执行本命令基于计费属性配置计费方式。  说明：  本示例配置计费属性为0x0400的用户在线计费开关、离线计费开关和融合计费开关均使能，融合计费开关不使能。请根据业务实际需要进行配置。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        CCVALUE:
          name: '计费属性值'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: ''
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
        ONLINE:
          name: '在线计费开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        OFFLINE:
          name: '离线计费开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ENABLE
        CONVERGED:
          name: '融合计费开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ENABLE
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
        RGAPPLIED:
          name: '业务申请上报模式'
          type: string
          enum:
          - DEFAULT
          - NOCHG
          - OFFLINERGONLY
          - ONLINERGONLY
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DEFAULT
    set_sgwchargecfg_list:
      type: items
      properties:
        HOMEOFFLINE:
          name: '本地用户离线计费开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '基于用户的漫游属性配置SGW-C的计费开关。  说明：  本示例配置本地用户不使能离线计费 ，漫游和拜访用户使能离线计费。 一般对于本地用户，在PGW-C计费的情况下，SGW-C可以不使能离线计费。对于漫游用户和拜访用户，SGW-C使能离线计费用于运营商之间进行费用结算。请根据业务实际需要进行配置。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ROAMOFFLINE:
          name: '漫游用户离线计费开关'
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
          name: '拜访用户离线计费开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_sgwchgmeth_list:
      type: items
      properties:
        CHARGECHAR:
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
          description: '（可选）基于用户的计费属性配置SGW-C的计费开关。  说明：  本示例配置计费属性为0x0800的用户使能离线计费。请根据业务实际需要进行配置。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        CHARGECHARVALUE:
          name: '计费属性值'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CCMASK:
          name: '计费属性掩码'
          type: string
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CCPRIORITY:
          name: '计费属性优先级'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OFFLINEFLAG:
          name: '是否离线计费'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_sgwapnchgmeth_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          maxLength: 63
          required: true
          description: '（可选）基于APN配置SGW-C的计费开关。  说明：  本示例配置APN为apn-test的用户离线开关继承上一级配置。请根据业务实际需要进行配置。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        OFFLINE:
          name: 'APN离线计费开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_sgwseggchgmeth_list:
      type: items
      properties:
        SEGGROUPNAME:
          name: 'IMSI/MSISDN号段组名称'
          type: string
          maxLength: 31
          required: true
          description: '（可选）基于用户的IMSI/MSISDN号段组配置SGW-C的计费开关。  说明：  本示例配置在号段组segment1中的用户使能离线计费 。请根据业务实际需要进行配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PRIORITY:
          name: 'IMSI/MSISDN号段组优先级'
          type: integer
          minimum: 1
          maximum: 65535
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        OFFLINEFLAG:
          name: 'IMSI/MSISDN号段组离线计费开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_chargectrl_list:
    - HOMECONVERGED: DISABLE
      HOMEONLINE: ENABLE
      HOMEOFFLINE: ENABLE
      VISITONLINE: ENABLE
      VISITOFFLINE: ENABLE
      VISITCONVERGED: DISABLE
      ROAMONLINE: ENABLE
      ROAMOFFLINE: ENABLE
      ROAMCONVERGED: DISABLE
    set_usrprofcharge_list:
    - USRPROFNAME: 'up-test'
      ONLINESW: INHERIT
      OFFLINESW: INHERIT
      CONVERGEDSW: DISABLE
      QBCSW: ''
      RGAPPLIED: ''
    set_apnchargectrl_list:
    - APN: 'apn-test'
      ONLINESW: INHERIT
      OFFLINESW: INHERIT
      CONVERGEDSW: DISABLE
      QBCSW: ''
      RGAPPLIED: ''
    add_chargemethod_list:
    - CHARGECHARACT: SPECIFIC_VALUE
      CCVALUE: '0x0400'
      MASK: '0xFFFF'
      PRIORITY: 1
      ONLINE: ENABLE
      OFFLINE: ENABLE
      CONVERGED: DISABLE
      QBCSW: ENABLE
      RGAPPLIED: DEFAULT
    set_sgwchargecfg_list:
    - HOMEOFFLINE: DISABLE
      ROAMOFFLINE: ENABLE
      VISITOFFLINE: ENABLE
    set_sgwchgmeth_list:
    - CHARGECHAR: SPECIFIC_VALUE
      CHARGECHARVALUE: '0x0800'
      CCMASK: '0xFFFF'
      CCPRIORITY: 1
      OFFLINEFLAG: ENABLE
    set_sgwapnchgmeth_list:
    - APN: 'apn-test'
      OFFLINE: INHERIT
    add_sgwseggchgmeth_list:
    - SEGGROUPNAME: 'segment1'
      PRIORITY: 1
      OFFLINEFLAG: ENABLE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 基于用户归属属性配置GGSN-C/PGW-C/SMF的计费方式。

```jinja2
{%- for item in set_chargectrl_list -%}
    SET CHARGECTRL:
    {#- --- 可选参数 --- -#}
    {%- if item.HOMECONVERGED is not none -%}
        HOMECONVERGED={{item.HOMECONVERGED}},
    {%- endif -%}
    {%- if item.HOMEONLINE is not none -%}
        HOMEONLINE={{item.HOMEONLINE}},
    {%- endif -%}
    {%- if item.HOMEOFFLINE is not none -%}
        HOMEOFFLINE={{item.HOMEOFFLINE}},
    {%- endif -%}
    {%- if item.VISITONLINE is not none -%}
        VISITONLINE={{item.VISITONLINE}},
    {%- endif -%}
    {%- if item.VISITOFFLINE is not none -%}
        VISITOFFLINE={{item.VISITOFFLINE}},
    {%- endif -%}
    {%- if item.VISITCONVERGED is not none -%}
        VISITCONVERGED={{item.VISITCONVERGED}},
    {%- endif -%}
    {%- if item.ROAMONLINE is not none -%}
        ROAMONLINE={{item.ROAMONLINE}},
    {%- endif -%}
    {%- if item.ROAMOFFLINE is not none -%}
        ROAMOFFLINE={{item.ROAMOFFLINE}},
    {%- endif -%}
    {%- if item.ROAMCONVERGED is not none -%}
        ROAMCONVERGED={{item.ROAMCONVERGED}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### **SET CHARGECTRL**根据用户漫游属性设置计费方式，**ADD CHARGEMETHOD**根据计费属性设置计费方式，针对同一个用户，两者规划的计费方式要一致，否则用户计费会出错。例如，针对计费属性是normal的本地用户，如果设置本地用户进行在线计费，又设置normal用户进行离线计费，那用户最终计费结果将出错。

### 2 **可选：**基于User Profile配置GGSN-C/PGW-C/SMF的计费方式。

```jinja2
{%- if is_optional_user_profile_billing -%}
    {%- for item in set_usrprofcharge_list -%}
        SET USRPROFCHARGE:
        {#- --- 必选参数 --- -#}
        USRPROFNAME="{{item.USRPROFNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.ONLINESW is not none -%}
            ONLINESW={{item.ONLINESW}},
        {%- endif -%}
        {%- if item.OFFLINESW is not none -%}
            OFFLINESW={{item.OFFLINESW}},
        {%- endif -%}
        {%- if item.CONVERGEDSW is not none -%}
            CONVERGEDSW={{item.CONVERGEDSW}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：CONVERGEDSW=ENABLE 时可选 --- -#}
        {%- if item.CONVERGEDSW == 'ENABLE' -%}
            {%- if item.QBCSW is not none -%}
                QBCSW={{item.QBCSW}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：CONVERGEDSW=ENABLE 时可选 --- -#}
        {%- if item.CONVERGEDSW == 'ENABLE' -%}
            {%- if item.RGAPPLIED is not none -%}
                RGAPPLIED={{item.RGAPPLIED}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 3 **可选：**基于DNN配置GGSN-C/PGW-C/SMF的计费方式。

```jinja2
{%- if is_optional_dnn_billing -%}
    {%- for item in set_apnchargectrl_list -%}
        SET APNCHARGECTRL:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        {#- --- 可选参数 --- -#}
        {%- if item.ONLINESW is not none -%}
            ONLINESW={{item.ONLINESW}},
        {%- endif -%}
        {%- if item.OFFLINESW is not none -%}
            OFFLINESW={{item.OFFLINESW}},
        {%- endif -%}
        {%- if item.CONVERGEDSW is not none -%}
            CONVERGEDSW={{item.CONVERGEDSW}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：CONVERGEDSW=ENABLE 时可选 --- -#}
        {%- if item.CONVERGEDSW == 'ENABLE' -%}
            {%- if item.QBCSW is not none -%}
                QBCSW={{item.QBCSW}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：CONVERGEDSW=ENABLE 时可选 --- -#}
        {%- if item.CONVERGEDSW == 'ENABLE' -%}
            {%- if item.RGAPPLIED is not none -%}
                RGAPPLIED={{item.RGAPPLIED}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 4 **可选：**基于用户计费属性配置GGSN-C/PGW-C/SMF的计费方式。

```jinja2
{%- if is_optional_charge_attribute_billing -%}
    {%- for item in add_chargemethod_list -%}
        ADD CHARGEMETHOD:
        {#- --- 必选参数 --- -#}
        CHARGECHARACT={{item.CHARGECHARACT}},
        {#- --- 可选参数 --- -#}
        {%- if item.ONLINE is not none -%}
            ONLINE={{item.ONLINE}},
        {%- endif -%}
        {%- if item.OFFLINE is not none -%}
            OFFLINE={{item.OFFLINE}},
        {%- endif -%}
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
            {%- if item.QBCSW is not none -%}
                QBCSW={{item.QBCSW}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：CONVERGED=ENABLE 时可选 --- -#}
        {%- if item.CONVERGED == 'ENABLE' -%}
            {%- if item.RGAPPLIED is not none -%}
                RGAPPLIED={{item.RGAPPLIED}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 5 配置基于用户的漫游属性配置SGW-C的计费开关。

```jinja2
{%- for item in set_sgwchargecfg_list -%}
    SET SGWCHARGECFG:
    {#- --- 可选参数 --- -#}
    {%- if item.HOMEOFFLINE is not none -%}
        HOMEOFFLINE={{item.HOMEOFFLINE}},
    {%- endif -%}
    {%- if item.ROAMOFFLINE is not none -%}
        ROAMOFFLINE={{item.ROAMOFFLINE}},
    {%- endif -%}
    {%- if item.VISITOFFLINE is not none -%}
        VISITOFFLINE={{item.VISITOFFLINE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 6 **可选：**基于用户的计费属性配置SGW-C的计费开关。

```jinja2
{%- if is_optional_sgw_charge_attribute -%}
    {%- for item in set_sgwchgmeth_list -%}
        SET SGWCHGMETH:
        {#- --- 必选参数 --- -#}
        CHARGECHAR={{item.CHARGECHAR}},
        OFFLINEFLAG={{item.OFFLINEFLAG}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：CHARGECHAR=SPECIFIC_VALUE 时必选 --- -#}
        {%- if item.CHARGECHAR == 'SPECIFIC_VALUE' -%}
            CHARGECHARVALUE="{{item.CHARGECHARVALUE}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：CHARGECHAR=SPECIFIC_VALUE 时可选 --- -#}
        {%- if item.CHARGECHAR == 'SPECIFIC_VALUE' -%}
            {%- if item.CCMASK is not none -%}
                CCMASK="{{item.CCMASK}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：CHARGECHAR=SPECIFIC_VALUE 时可选 --- -#}
        {%- if item.CHARGECHAR == 'SPECIFIC_VALUE' -%}
            {%- if item.CCPRIORITY is not none -%}
                CCPRIORITY={{item.CCPRIORITY}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 7 **可选：**基于APN配置SGW-C的计费开关。

```jinja2
{%- if is_optional_sgw_apn_billing -%}
    {%- for item in set_sgwapnchgmeth_list -%}
        SET SGWAPNCHGMETH:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        OFFLINE={{item.OFFLINE}},
        ;
    {%- endfor -%}
{%- endif -%}
```

### 8 **可选：**基于用户的IMSI/MSISDN号段组配置SGW-C的计费开关。

```jinja2
{%- if is_optional_sgw_segment_group -%}
    {%- for item in add_sgwseggchgmeth_list -%}
        ADD SGWSEGGCHGMETH:
        {#- --- 必选参数 --- -#}
        SEGGROUPNAME="{{item.SEGGROUPNAME}}",
        PRIORITY={{item.PRIORITY}},
        OFFLINEFLAG={{item.OFFLINEFLAG}},
        ;
    {%- endfor -%}
{%- endif -%}
```

