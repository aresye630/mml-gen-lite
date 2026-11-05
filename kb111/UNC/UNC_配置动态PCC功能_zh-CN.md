---
id: ''
name: 配置动态PCC功能
ne_type: UNC
type: feature
description: 当网络中有PCRF，用户激活为PCC用户，需要为用户或用户业务提供灵活策略控制时，需要开启动态PCC功能，并根据业务情况来部署预定义规则/预定义规则组或动态规则。  * 预定义规则/预定义规则组    当需要对报文进行七层解析或业务规划时针对用户的规则内容在用户激活前可以预先确定，建议采用预定义规则方式，以减少GGSN/PGW-C与PCRF之间的交互和对缓存资源的占用。即相应的QoS管理、计费控制策略等在GGSN/PGW-C上通过rule或者UserProfile配置，PCRF上只配置预定义规则名称/预定义规则组名称。 * 动态规则    当用户激活前用户的规则内容无法确定，需要根据用户访问业务时的协商结果由AF（应用服务器）或其他网元发送请求给PCRF，请求建立动态规则时，建议采用动态规则方式。即GGSN/PGW-C上只需开启PCC功能开关，相应的QoS管理、计费控制策略等均在PCRF上配置。  GGSN/PGW-C可以基于APN、特定号段、全局选择PCRF组，并触发PCC功能，GGSN/PGW-C上基于不同粒度开启PCC功能的规划如表1所示。  **表1** PCRF选择原则  | 选择的PCRF组 | 全局PCC功能（**SET PCCFUNC**） | APN下的PCC功能（**SET APNPCCFUNC**） | 说明 | | --- | --- | --- | --- | | 选择APN下绑定的PCRF组 | ENABLE | ENABLE | 指定APN下绑定PCRF组。 | | 选择指定号段绑定的PCRF组 | ENABLE | INHERIT | 指定号段绑定PCRF组。 | | 选择全局缺省的PCRF组 | ENABLE | INHERIT | 指定全局缺省的PCRF组，且指定号段未绑定PCRF组。 |  适用于GGSN、PGW-C。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","智能PCC解决方案","WSFD-109101 PCC基本功能","PCC基本功能（2G/3G/4G，基于Gx接口）","激活PCC基本功能","配置动态PCC功能"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当网络中有PCRF，用户激活为PCC用户，需要为用户或用户业务提供灵活策略控制时，需要开启动态PCC功能，并根据业务情况来部署预定义规则/预定义规则组或动态规则。* 预定义规则/预定义规则组  当需要对报文进行七层解析或业务规划时针对用户的规则内容在用户激活前可以预先确定，建议采用预定义规则方式，以减少GGSN/PGW-C与PCRF之间的交互和对缓存资源的占用。即相应的QoS管理、计费控制策略等在GGSN/PGW-C上通过rule或者UserProfile配置，PCRF上只配置预定义规则名称/预定义规则组名称。* 动态规则  当用户激活前用户的规则内容无法确定，需要根据用户访问业务时的协商结果由AF（应用服务器）或其他网元发送请求给PCRF，请求建立动态规则时，建议采用动态规则方式。即GGSN/PGW-C上只需开启PCC功能开关，相应的QoS管理、计费控制策略等均在PCRF上配置。GGSN/PGW-C可以基于APN、特定号段、全局选择PCRF组，并触发PCC功能，GGSN/PGW-C上基于不同粒度开启PCC功能的规划如表1所示。**表1** PCRF选择原则| 选择的PCRF组 | 全局PCC功能（**SET PCCFUNC**） | APN下的PCC功能（**SET APNPCCFUNC**） | 说明 || --- | --- | --- | --- || 选择APN下绑定的PCRF组 | ENABLE | ENABLE | 指定APN下绑定PCRF组。 || 选择指定号段绑定的PCRF组 | ENABLE | INHERIT | 指定号段绑定PCRF组。 || 选择全局缺省的PCRF组 | ENABLE | INHERIT | 指定全局缺省的PCRF组，且指定号段未绑定PCRF组。 |适用于GGSN、PGW-C。

## 必备事项
前提条件

* 请仔细阅读PCC基本功能（2G/3G/4G，基于Gx接口）。
* 完成配置与PCRF对接数据。
* 完成**加载license**（如果有需求，请联系华为技术支持工程师处理）
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
    add_imsimsisdnseg_list:
      type: items
      properties:
        SEGMENTNAME:
          name: 'IMSI/MSISDN号段名称'
          type: string
          maxLength: 31
          required: true
          description: '配置IMSI/MSISDN号码段'
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
        WILDCARDSEG:
          name: '通配号段字符串'
          type: string
          maxLength: 47
          required: false
          description: ''
          data_source: ''
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
          description: '“pcrf\_1”和“pcrf\_2”属于“pcrf\_group\_1”，“pcrf\_group\_1”内的PCRF按配置的百分比进行负荷分担。“pcrf\_3”和“pcrf\_4”属于“pcrf\_group\_2”，“pcrf\_group\_2”内的PCRF为主备模式，且“pcrf\_3”为主用PCRF。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        REALMNAME:
          name: 'PCRF域名'
          type: string
          maxLength: 127
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_pcrfgroup_list:
      type: items
      properties:
        PCRFGRPNAME:
          name: 'PCRF组名称'
          type: string
          maxLength: 128
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        LOADBALANCEMODE:
          name: '负荷分担模式'
          type: string
          enum:
          - LOAD_BALANCE
          - MASTER_SLAVE
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: MASTER_SLAVE
    add_pcrfbindgrp_list:
      type: items
      properties:
        PCRFGRPNAME:
          name: 'PCRF组名称'
          type: string
          maxLength: 128
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PCRFHOSTNAME:
          name: 'PCRF主机名称'
          type: string
          maxLength: 127
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        WEIGHT:
          name: 'PCRF权重'
          type: integer
          minimum: 1
          maximum: 100
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_masterpcrf_list:
      type: items
      properties:
        PCRFGRPNAME:
          name: 'PCRF组名称'
          type: string
          maxLength: 128
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MASTERPCRF:
          name: '主用PCRF主机名'
          type: string
          maxLength: 127
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_glbpcrfgroup_list:
      type: items
      properties:
        IMSIMSISDNSEG:
          name: 'IMSI/MSISDN号段名称'
          type: string
          maxLength: 31
          required: true
          description: '全局PCRF分组及PCC开关。  号段“msisdnseg1”与PCRF分组“pcrf\_group\_1”绑定，优先级为“1”。  号段“msisdnseg2”与PCRF分组“pcrf\_group\_2”绑定，优先级为“2”。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PCRFGRPNAME:
          name: 'PCRF组名称'
          type: string
          maxLength: 128
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 1
          maximum: 65535
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_pccpcrfmsgattr_list:
      type: items
      properties: {}
    set_dftglbpcrfgrp_list:
      type: items
      properties:
        PCRFGRPNAME:
          name: 'PCRF组名称'
          type: string
          maxLength: 128
          required: false
          description: '指定全局缺省的PCRF分组。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    set_pccfunc_list:
      type: items
      properties:
        HOMEPCCSWITCH:
          name: '本地用户PCC功能'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '使能GGSN/PGW-C上的全局用户的PCC功能。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ROAMPCCSWITCH:
          name: '漫游用户PCC功能'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        VISITPCCSWITCH:
          name: '拜访用户PCC功能'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        COMPOLICY:
          name: '公共策略'
          type: string
          enum:
          - LOCALAAA
          - PCRFPCF
          required: false
          description: '此处以基于LOCALAAA实现公共策略为例。'
          data_source: '对端协商'
          pattern: ''
          default: ''
    add_pcrfgrpbndapn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          maxLength: 63
          required: true
          description: 'APN绑定的PCRF分组。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DEFAULTFLAG:
          name: '缺省标记'
          type: string
          enum:
          - DEFAULT
          - IMSI_MSISDN_SEG
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PCRFGRPNAME:
          name: 'PCRF组名称'
          type: string
          maxLength: 128
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IMSIMSISDNSEG:
          name: 'IMSI/MSISDN号段名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_pcctemplate_list:
      type: items
      properties:
        PCCTEMPNAME:
          name: 'PCC模板名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_apnpccfunc_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          maxLength: 63
          required: true
          description: 'APN绑定的PCC开关。  “apn-test1”下的PCC开关为“ENABLE”，“apn-test2”下的PCC开关为“INHERIT”。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        HOMEPCCSWITCH:
          name: '本地用户PCC功能'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        ROAMPCCSWITCH:
          name: '漫游用户PCC功能'
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
        VISITPCCSWITCH:
          name: '拜访用户PCC功能'
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
    add_specificapnval_list:
      type: items
      properties:
        SUBSCRIBERAPN:
          name: '用户APN'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_rule_list:
      type: items
      properties:
        RULENAME:
          name: '规则名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        POLICYTYPE:
          name: '策略类型'
          type: string
          enum:
          - ADC
          - BWM
          - FIREWALL
          - FUP
          - HEADEN
          - IPREDIR
          - LBO
          - NON_SPECIFIC_TYPE
          - PCC
          - QOS
          - REMARK_FPI
          - SMARTREDIRECT
          - SRV_TRIGGER
          - TRAFFICCLASS
          - ULCL
          - WEBPROXY
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        POLICYNAME:
          name: '策略名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PROTODESCDL:
          name: '下行协议描述参数'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PROTODESCUL:
          name: '上行协议描述参数'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RULERANGE:
          name: '规则生效范围'
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
    add_rulebinddnai_list:
      type: items
      properties:
        RULENAME:
          name: '预定义规则名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DNAI:
          name: '数据网络访问标识符'
          type: string
          minLength: 1
          maxLength: 63
          required: true
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
          description: ''
          data_source: ''
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
          data_source: ''
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
    add_usrprobinddnai_list:
      type: items
      properties:
        USRPRONAME:
          name: '用户模板名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DNAI:
          name: '数据网络访问标识符'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_rulebinding_list:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RULENAME:
          name: '规则名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3W9SPCC11'
      SWITCH: ENABLE
    add_imsimsisdnseg_list:
    - SEGMENTNAME: 'msisdnseg1'
      SEGMENTTYPE: MSISDN
      SEGSTART: '18900000000'
      SEGEND: '18949999999'
      WILDCARDSEG: ''
    add_pcrf_list:
    - HOSTNAME: 'pcrf_1'
      REALMNAME: 'pcrf.huawei.com'
    add_pcrfgroup_list:
    - PCRFGRPNAME: 'pcrf_group_1'
      LOADBALANCEMODE: LOAD_BALANCE
    add_pcrfbindgrp_list:
    - PCRFGRPNAME: 'pcrf_group_1'
      PCRFHOSTNAME: 'pcrf_1'
      WEIGHT: 40
    set_masterpcrf_list:
    - PCRFGRPNAME: ''
      MASTERPCRF: ''
    add_glbpcrfgroup_list:
    - IMSIMSISDNSEG: 'msisdnseg1'
      PCRFGRPNAME: 'pcrf_group_1'
      PRIORITY: 1
    set_pccpcrfmsgattr_list:
    - {}
    set_dftglbpcrfgrp_list:
    - PCRFGRPNAME: 'pcrf_group_1'
    set_pccfunc_list:
    - HOMEPCCSWITCH: ENABLE
      ROAMPCCSWITCH: ENABLE
      VISITPCCSWITCH: ENABLE
      COMPOLICY: LOCALAAA
    add_pcrfgrpbndapn_list:
    - APN: 'apn-test1'
      DEFAULTFLAG: DEFAULT
      PCRFGRPNAME: 'pcrf_group_2'
      IMSIMSISDNSEG: 'msisdnseg1'
      PRIORITY: ''
    add_pcctemplate_list:
    - PCCTEMPNAME: ''
    set_apnpccfunc_list:
    - APN: 'apn-test1'
      HOMEPCCSWITCH: ENABLE
      ROAMPCCSWITCH: ENABLE
      VISITPCCSWITCH: ENABLE
    add_specificapnval_list:
    - SUBSCRIBERAPN: ''
    add_rule_list:
    - RULENAME: ''
      POLICYTYPE: ''
      FLOWFILTERNAME: ''
      POLICYNAME: ''
      PROTODESCDL: ''
      PROTODESCUL: ''
      RULERANGE: ALL
    add_rulebinddnai_list:
    - RULENAME: ''
      DNAI: ''
    add_userprofile_list:
    - USERPROFILENAME: ''
      UPTYPE: PCC
      PROFILERANGE: ALL
    add_usrprobinddnai_list:
    - USRPRONAME: ''
      DNAI: ''
    add_rulebinding_list:
    - USERPROFILENAME: ''
      RULENAME: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

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

### 3 **可选：**配置IMSI或MSISDN号码段。

```jinja2
{%- if is_optional_imsi_msisdn_segment -%}
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
        {#- --- 条件必选：SEGMENTTYPE=IMSIWILDCARD/MSISDNWILDCARD 时必选 --- -#}
        {%- if item.SEGMENTTYPE in ['IMSIWILDCARD', 'MSISDNWILDCARD'] -%}
            WILDCARDSEG="{{item.WILDCARDSEG}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 规划特定号段的用户触发PCC功能时需要配置。

### 4 配置PCRF分组信息。

#### 4.1 配置PCRF。

```jinja2
{%- for item in add_pcrf_list -%}
    ADD PCRF:
    {#- --- 必选参数 --- -#}
    HOSTNAME="{{item.HOSTNAME}}",
    REALMNAME="{{item.REALMNAME}}",
    ;
{%- endfor -%}
```

#### 4.2 配置PCRF分组。

```jinja2
{%- for item in add_pcrfgroup_list -%}
    ADD PCRFGROUP:
    {#- --- 必选参数 --- -#}
    PCRFGRPNAME="{{item.PCRFGRPNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.LOADBALANCEMODE is not none -%}
        LOADBALANCEMODE={{item.LOADBALANCEMODE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 4.3 添加指定的PCRF到指定的PCRF分组中。

```jinja2
{%- for item in add_pcrfbindgrp_list -%}
    ADD PCRFBINDGRP:
    {#- --- 必选参数 --- -#}
    PCRFGRPNAME="{{item.PCRFGRPNAME}}",
    PCRFHOSTNAME="{{item.PCRFHOSTNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.WEIGHT is not none -%}
        WEIGHT={{item.WEIGHT}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 4.4 **可选：**如果PCRF组的工作模式为主备模式，可使用如下命令修改PCRF分组内的缺省主用PCRF。

```jinja2
{%- if is_optional_modify_default_master_pcrf -%}
    {%- for item in set_masterpcrf_list -%}
        SET MASTERPCRF:
        {#- --- 必选参数 --- -#}
        MASTERPCRF="{{item.MASTERPCRF}}",
        PCRFGRPNAME="{{item.PCRFGRPNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.5 **可选：**基于IMSI号段选择PCRF分组时，需要将指定的PCRF分组绑定到指定的号码段。

```jinja2
{%- if is_optional_bind_pcrf_group_segment -%}
    {%- for item in add_glbpcrfgroup_list -%}
        ADD GLBPCRFGROUP:
        {#- --- 必选参数 --- -#}
        IMSIMSISDNSEG="{{item.IMSIMSISDNSEG}}",
        PCRFGRPNAME="{{item.PCRFGRPNAME}}",
        PRIORITY={{item.PRIORITY}},
        ;
    {%- endfor -%}
{%- endif -%}
```

### 5 **可选：**配置基于整机粒度控制在激活过程中根据PCRF返回的重定向指示重选PCRF。缺省不支持。

```jinja2
{%- if is_optional_redirect_reselect_pcrf -%}
    SET PCCPCRFMSGATTR:
    ;
{%- endif -%}
```

### 6 开启全局缺省PCC开关。

#### 6.1 设置全局缺省的PCRF分组的名称。

```jinja2
{%- for item in set_dftglbpcrfgrp_list -%}
    SET DFTGLBPCRFGRP:
    {#- --- 可选参数 --- -#}
    {%- if item.PCRFGRPNAME is not none -%}
        PCRFGRPNAME="{{item.PCRFGRPNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 6.2 针对全局配置PCC使能开关。

```jinja2
{%- for item in set_pccfunc_list -%}
    SET PCCFUNC:
    {#- --- 可选参数 --- -#}
    {%- if item.HOMEPCCSWITCH is not none -%}
        HOMEPCCSWITCH={{item.HOMEPCCSWITCH}},
    {%- endif -%}
    {%- if item.ROAMPCCSWITCH is not none -%}
        ROAMPCCSWITCH={{item.ROAMPCCSWITCH}},
    {%- endif -%}
    {%- if item.VISITPCCSWITCH is not none -%}
        VISITPCCSWITCH={{item.VISITPCCSWITCH}},
    {%- endif -%}
    {%- if item.COMPOLICY is not none -%}
        COMPOLICY={{item.COMPOLICY}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 缺省REPORTLEVEL、缺省METERMETHOD和PCC用户激活时Common Policy的选择原则为可选配置，缺省使用默认值。

### 7 开启APN下的PCC开关，并将指定的PCRF分组绑定到该APN下。

#### 7.1 将指定的PCRF分组及号段信息绑定到指定APN。

```jinja2
{%- for item in add_pcrfgrpbndapn_list -%}
    ADD PCRFGRPBNDAPN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    DEFAULTFLAG={{item.DEFAULTFLAG}},
    PCRFGRPNAME="{{item.PCRFGRPNAME}}",
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：DEFAULTFLAG=IMSI_MSISDN_SEG 时必选 --- -#}
    {%- if item.DEFAULTFLAG == 'IMSI_MSISDN_SEG' -%}
        IMSIMSISDNSEG="{{item.IMSIMSISDNSEG}}",
    {%- endif -%}
    {#- --- 条件必选：DEFAULTFLAG=IMSI_MSISDN_SEG 时必选 --- -#}
    {%- if item.DEFAULTFLAG == 'IMSI_MSISDN_SEG' -%}
        PRIORITY={{item.PRIORITY}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 号段信息为可选配置。APN下只允许配置一个不带号段信息的PcrfGroup。

#### 7.2 **可选：**添加PCC模板，配置在激活过程中根据PCRF返回的重定向指示重选PCRF；配置缺省REPORTLEVEL和缺省METERMETHOD，缺省使用默认值。

```jinja2
{%- if is_optional_add_pcc_template -%}
    {%- for item in add_pcctemplate_list -%}
        ADD PCCTEMPLATE:
        {#- --- 必选参数 --- -#}
        PCCTEMPNAME="{{item.PCCTEMPNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 7.3 针对指定的APN配置PCC使能开关，并将PccTemplate绑定到APN下。

```jinja2
{%- for item in set_apnpccfunc_list -%}
    SET APNPCCFUNC:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.HOMEPCCSWITCH is not none -%}
        HOMEPCCSWITCH={{item.HOMEPCCSWITCH}},
    {%- endif -%}
    {%- if item.ROAMPCCSWITCH is not none -%}
        ROAMPCCSWITCH={{item.ROAMPCCSWITCH}},
    {%- endif -%}
    {%- if item.VISITPCCSWITCH is not none -%}
        VISITPCCSWITCH={{item.VISITPCCSWITCH}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 8 **可选：**配置specific APN。

```jinja2
{%- if is_optional_config_specific_apn -%}
    {%- for item in add_specificapnval_list -%}
        ADD SPECIFICAPNVAL:
        {#- --- 必选参数 --- -#}
        SUBSCRIBERAPN="{{item.SUBSCRIBERAPN}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

### GGSN/PGW-C向PCRF上报APN时，不仅能携带Request APN/Service APN，GGSN/PGW-C支持上报指定的APN，该APN可以是系统中配置的任一APN实例名称或者APN别名名称。

### 当配置了specific APN，在上报APN时，specific APN优先级最高，其次是别名APN、虚拟APN、真实APN。

### 9 PCRF下发预定义规则时，需要在GGSN/PGW-C上配置预定义规则对应的本地业务规则。

```jinja2
{%- for item in add_rule_list -%}
    ADD RULE:
    {#- --- 必选参数 --- -#}
    POLICYTYPE={{item.POLICYTYPE}},
    RULENAME="{{item.RULENAME}}",
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：POLICYTYPE=ULCL 时必选 --- -#}
    {%- if item.POLICYTYPE == 'ULCL' -%}
        FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
    {%- endif -%}
    {#- --- 条件必选：POLICYTYPE=PCC/ULCL/QOS 时必选 --- -#}
    {%- if item.POLICYTYPE in ['PCC', 'ULCL', 'QOS'] -%}
        POLICYNAME="{{item.POLICYNAME}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：POLICYTYPE=PCC/QOS 时可选 --- -#}
    {%- if item.POLICYTYPE in ['PCC', 'QOS'] -%}
        {%- if item.PROTODESCDL is not none -%}
            PROTODESCDL="{{item.PROTODESCDL}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：POLICYTYPE=PCC/QOS 时可选 --- -#}
    {%- if item.POLICYTYPE in ['PCC', 'QOS'] -%}
        {%- if item.PROTODESCUL is not none -%}
            PROTODESCUL="{{item.PROTODESCUL}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：POLICYTYPE=PCC/QOS 时可选 --- -#}
    {%- if item.POLICYTYPE in ['PCC', 'QOS'] -%}
        {%- if item.RULERANGE is not none -%}
            RULERANGE={{item.RULERANGE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 10 **可选：**配置rule和DNAI关联。可选配置，将rule下发给指定DNAI的辅锚点PGW-U时需要配置。

```jinja2
{%- if is_optional_rule_dnai_association -%}
    {%- for item in add_rulebinddnai_list -%}
        ADD RULEBINDDNAI:
        {#- --- 必选参数 --- -#}
        DNAI="{{item.DNAI}}",
        RULENAME="{{item.RULENAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

### 11 PCRF下发预定义规则组时，需要在GGSN/PGW-C上配置预定义规则组对应的本地业务策略组合。

#### 11.1 配置UserProfile。

```jinja2
{%- for item in add_userprofile_list -%}
    ADD USERPROFILE:
    {#- --- 必选参数 --- -#}
    UPTYPE={{item.UPTYPE}},
    USERPROFILENAME="{{item.USERPROFILENAME}}",
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

#### 11.2 **可选：**配置UserProfile和DNAI关联。可选配置，将UserProfile下发给指定DNAI的辅锚点PGW-U时需要配置。

```jinja2
{%- if is_optional_userprofile_dnai_association -%}
    {%- for item in add_usrprobinddnai_list -%}
        ADD USRPROBINDDNAI:
        {#- --- 必选参数 --- -#}
        DNAI="{{item.DNAI}}",
        USRPRONAME="{{item.USRPRONAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 11.3 将已配置的rule绑定到UserProfile。

```jinja2
{%- for item in add_rulebinding_list -%}
    ADD RULEBINDING:
    {#- --- 必选参数 --- -#}
    RULENAME="{{item.RULENAME}}",
    USERPROFILENAME="{{item.USERPROFILENAME}}",
    ;
{%- endfor -%}
```

