---
id: ''
name: 去激活GGSN/P-GW信令代理
ne_type: UNC
type: feature
description: 运营商无需GGSN/P-GW承担Proxy的作用，需要去激活GGSN/P-GW信令代理特性。  适用于GGSN、PGW-C
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","漫游管理功能","WSFD-205107 GGSN/P-GW信令代理","去激活GGSN/P-GW信令代理"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
运营商无需GGSN/P-GW承担Proxy的作用，需要去激活GGSN/P-GW信令代理特性。适用于GGSN、PGW-C

## 必备事项
前提条件

* 请仔细阅读WSFD-205107 GGSN/P-GW信令代理。
* 完成激活GGSN/P-GW信令代理
* 已在本地备份配置文件。
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
    rmv_homegrpbindapn_list:
      type: items
      properties:
        APN:
          name: 'APN实例名'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '将home-group绑定到指定的APN'
          data_source: '从已配置数据中获取'
          pattern: ''
          default: ''
        HOMEGROUPINDX:
          name: 'Home group的编号'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_gwproxyfunc_list:
      type: items
      properties:
        PROXYSW:
          name: 'Proxy功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '网关Proxy功能'
          data_source: '本端规划'
          pattern: ''
          default: ''
    rmv_homeip_list:
      type: items
      properties:
        HOMEGROUPINDX:
          name: '组号'
          type: integer
          minimum: 1
          maximum: 128
          required: true
          description: 'Home GGSN/P-GW IP地址信息'
          data_source: '本端规划'
          pattern: ''
          default: ''
        HOMEIPID:
          name: 'home-ip的编号'
          type: integer
          minimum: 1
          maximum: 10
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    rmv_homegroup_list:
      type: items
      properties:
        HOMEGROUPINDX:
          name: 'home group的编号'
          type: integer
          minimum: 1
          maximum: 128
          required: true
          description: 'HomeGroup信息'
          data_source: '本端规划'
          pattern: ''
          default: ''
    rmv_primsimsisdnseg_list:
      type: items
      properties:
        SEGMENTNAME:
          name: 'IMSI/MSISDN号段名称'
          type: string
          minLength: 1
          maxLength: 31
          required: true
          description: 'IMSI/MSISDN号码段信息'
          data_source: '本端规划'
          pattern: ''
          default: ''
    rmv_primsimsisdng_list:
      type: items
      properties:
        SEGGROUPNAME:
          name: 'IMSI/MSISDN号段组名称'
          type: string
          minLength: 1
          maxLength: 31
          required: true
          description: 'IMSI/MSISDN号段组信息'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SEGMENTNAME:
          name: 'IMSI/MSISDN号段名称'
          type: string
          minLength: 1
          maxLength: 31
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    rmv_ccvalue_list:
      type: items
      properties:
        CCGROUPNAME:
          name: '计费特征组名称'
          type: string
          minLength: 1
          maxLength: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CCVALUE:
          name: '计费属性值'
          type: string
          minLength: 1
          maxLength: 6
          required: false
          description: '计费属性值信息'
          data_source: '全网规划'
          pattern: ''
          default: ''
    rmv_ccgroup_list:
      type: items
      properties:
        CCGROUPNAME:
          name: '计费属性组名称'
          type: string
          minLength: 1
          maxLength: 31
          required: true
          description: '计费属性组信息'
          data_source: '本端规划'
          pattern: ''
          default: ''
    rmv_apngwproxyfunc_list:
      type: items
      properties:
        APN:
          name: 'APN'
          type: string
          required: false
          description: '基于APN控制是否打开Proxy功能'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PROXYSW:
          name: '网关Proxy开关'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3W9GPSP11'
      SWITCH: DISABLE
    rmv_homegrpbindapn_list:
    - APN: 'apn-test'
      HOMEGROUPINDX: 1
    set_gwproxyfunc_list:
    - PROXYSW: DISABLE
    rmv_homeip_list:
    - HOMEGROUPINDX: 1
      HOMEIPID: 1
    rmv_homegroup_list:
    - HOMEGROUPINDX: 1
    rmv_primsimsisdnseg_list:
    - SEGMENTNAME: 'msisdn-test'
    rmv_primsimsisdng_list:
    - SEGGROUPNAME: 'group-test'
      SEGMENTNAME: 'msisdn-test'
    rmv_ccvalue_list:
    - CCGROUPNAME: '计费特征组名称'
      CCVALUE: '0x0010'
    rmv_ccgroup_list:
    - CCGROUPNAME: 'cc_group1'
    rmv_apngwproxyfunc_list:
    - APN: apn-test
      PROXYSW: DISABLE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 以下命令在“MML命令行 - UNC”窗口上执行。关闭本特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 2 删除Home group与APN的绑定关系。**RMV HOMEGRPBINDAPN**:APN=APN，HOMEGROUPINDX=Home group的编号；

```jinja2
{%- for item in rmv_homegrpbindapn_list -%}
    RMV HOMEGRPBINDAPN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.HOMEGROUPINDX is not none -%}
        HOMEGROUPINDX={{item.HOMEGROUPINDX}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 关闭网关的Proxy功能

```jinja2
{%- for item in set_gwproxyfunc_list -%}
    SET GWPROXYFUNC:
    {#- --- 可选参数 --- -#}
    {%- if item.PROXYSW is not none -%}
        PROXYSW={{item.PROXYSW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 删除在Home group下配置的归属P-GW的IP地址。

```jinja2
{%- for item in rmv_homeip_list -%}
    RMV HOMEIP:
    {#- --- 必选参数 --- -#}
    HOMEGROUPINDX={{item.HOMEGROUPINDX}},
    {#- --- 可选参数 --- -#}
    {%- if item.HOMEIPID is not none -%}
        HOMEIPID={{item.HOMEIPID}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 删除Home group。

```jinja2
{%- for item in rmv_homegroup_list -%}
    RMV HOMEGROUP:
    {#- --- 必选参数 --- -#}
    HOMEGROUPINDX={{item.HOMEGROUPINDX}},
    ;
{%- endfor -%}
```

### 6 **可选：**删除将要对其进行信令代理操作IMSI/MSISDN号码段和号码段组。

#### 6.1 删除IMSI/MSISDN号码段。

```jinja2
{%- if is_optional_imsi_msisdn_segment_and_group -%}
    {%- for item in rmv_primsimsisdnseg_list -%}
        RMV PRIMSIMSISDNSEG:
        {#- --- 必选参数 --- -#}
        SEGMENTNAME="{{item.SEGMENTNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 6.2 删除IMSI/MSISDN号码段组。

```jinja2
{%- if is_optional_imsi_msisdn_segment_and_group -%}
    {%- for item in rmv_primsimsisdng_list -%}
        RMV PRIMSIMSISDNG:
        {#- --- 必选参数 --- -#}
        SEGGROUPNAME="{{item.SEGGROUPNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.SEGMENTNAME is not none -%}
            SEGMENTNAME="{{item.SEGMENTNAME}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 7 **可选：**删除将要对其进行信令代理操作的计费属性信息。

#### 7.1 删除指定计费属性组的计费属性值。

```jinja2
{%- if is_optional_charging_attribute -%}
    {%- for item in rmv_ccvalue_list -%}
        RMV CCVALUE:
        {#- --- 必选参数 --- -#}
        CCGROUPNAME="{{item.CCGROUPNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.CCVALUE is not none -%}
            CCVALUE="{{item.CCVALUE}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 7.2 删除计费属性组。

```jinja2
{%- if is_optional_charging_attribute -%}
    {%- for item in rmv_ccgroup_list -%}
        RMV CCGROUP:
        {#- --- 必选参数 --- -#}
        CCGROUPNAME="{{item.CCGROUPNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

### 8 关闭APN的proxy功能。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该rmv_apngwproxyfunc_list的变量区（command: RMV APNGWPROXYFUNC） -#}
<!-- MISSING_MACRO: command=RMV APNGWPROXYFUNC list_name=rmv_apngwproxyfunc_list step_id=8 -->
```

