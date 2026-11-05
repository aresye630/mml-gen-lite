---
id: ''
name: 配置惯性运行&本地应急接入数据
ne_type: UEG
type: feature
description: 为保证在边缘网络与中心网络传输中断时用户能保持惯性运行、业务不中断，新用户能在本地应急接入，需要开启本特性，并设置相应控制参数。
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝M”，入驻式）","配置业务数据（风筝M）","配置业务数据（UEG）","惯性运行&本地应急接入配置","配置惯性运行&本地应急接入数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools:
- getParameterValue('SET EMERGAUTHTIMER')
---
<!-- @mml:block= annotations -->
```text
## 操作场景
为保证在边缘网络与中心网络传输中断时用户能保持惯性运行、业务不中断，新用户能在本地应急接入，需要开启本特性，并设置相应控制参数。

## 必备事项
前提条件

* 请仔细阅读GWFD-023901 本地应急接入。
* 完成UPF、应急AMF、应急SMF、应急UDM与周边网元的对接配置及基础全局数据配置，具体配置见《初始配置与调测》。
* 完成License加载。
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
          name: 'LICITEM'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: '开启本地应急接入特性License开关。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SWITCH:
          name: 'SWITCH'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_ngmmfunc_list:
      type: items
      properties:
        NOUECTXOPTSW:
          name: '无用户上下文处理基站消息增强开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: '开启无用户上下文处理基站消息增强开关。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_inertialoper_list:
      type: items
      properties:
        IDLEUSRIGNORE:
          name: '数据面非连接态用户是否支持惯性运行功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '建议非连接态用户不进入惯性运行。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DELAYTIME:
          name: 'PFCP路径断后进入惯性运行状态时长（秒）'
          type: integer
          minimum: 0
          maximum: 300
          required: false
          description: 'PFCP路径断超过30秒后连接态用户进入惯性运行状态。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NON5GUSRIGNORE:
          name: '非5G用户是否支持惯性运行功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '非5G用户支持惯性运行功能。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_emergauthtimer_list:
      type: items
      properties:
        SWITCH:
          name: '惯性运行/应急接入授权开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: '与运营商协商授权用户保持惯性运行/应急接入的时长。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        HOURS:
          name: '小时'
          type: integer
          minimum: 1
          maximum: 1024
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_cpnodeid_list:
      type: items
      properties:
        CPNAME:
          name: 'SMF 名称'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: '该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CPNODEIDTYPE:
          name: 'CP NodeID 类型'
          type: string
          enum:
          - FQDN
          - IPV4
          - IPV6
          required: false
          description: 'CP NodeID类型支持IPV4、IPv6或FQDN。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4NODEID:
          name: 'IPv4地址类型的Node Id'
          type: string
          maxLength: 15
          required: false
          description: '“CPNODEIDTYPE”设置为“IPV4”时需要规划。  采用应急SMF的N4接口IP。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        LOCALEMERNODE:
          name: '本地应急接入节点'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: '规划的是应急SMF的NODE信息时，该参数必须设置为“TRUE”。  采用应急SMF的FQDN。'
          data_source: '本端规划'
          pattern: ''
          default: FALSE
    add_cpnodeid_list_1:
      type: items
      properties:
        CPNAME:
          name: 'SMF 名称'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: '该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CPNODEIDTYPE:
          name: 'CP NodeID 类型'
          type: string
          enum:
          - FQDN
          - IPV4
          - IPV6
          required: false
          description: 'CP NodeID类型支持IPV4、IPv6或FQDN。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV6NODEID:
          name: 'IPv6地址类型的Node Id'
          type: string
          maxLength: 39
          required: false
          description: '“CPNODEIDTYPE”设置为“IPV6”时需要规划。  采用应急SMF的N4接口IP。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        LOCALEMERNODE:
          name: '本地应急接入节点'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: '规划的是应急SMF的NODE信息时，该参数必须设置为“TRUE”。  采用应急SMF的FQDN。'
          data_source: '本端规划'
          pattern: ''
          default: FALSE
    add_cpnodeid_list_2:
      type: items
      properties:
        CPNAME:
          name: 'SMF 名称'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: '该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CPNODEIDTYPE:
          name: 'CP NodeID 类型'
          type: string
          enum:
          - FQDN
          - IPV4
          - IPV6
          required: false
          description: 'CP NodeID类型支持IPV4、IPv6或FQDN。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        FQDNNODEID:
          name: 'FQDN类型的Node Id'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: '“CPNODEIDTYPE”设置为“FQDN”时需要规划。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        LOCALEMERNODE:
          name: '本地应急接入节点'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: '规划的是应急SMF的NODE信息时，该参数必须设置为“TRUE”。  采用应急SMF的FQDN。'
          data_source: '本端规划'
          pattern: ''
          default: FALSE
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3G5IOIF01'
      SWITCH: ENABLE
    set_ngmmfunc_list:
    - NOUECTXOPTSW: ON
    set_inertialoper_list:
    - IDLEUSRIGNORE: ENABLE
      DELAYTIME: 30
      NON5GUSRIGNORE: DISABLE
    set_emergauthtimer_list:
    - SWITCH: ENABLE
      HOURS: 48
    add_cpnodeid_list:
    - CPNAME: 'smfnode1'
      CPNODEIDTYPE: IPV4
      IPV4NODEID: '10.0.0.1'
      LOCALEMERNODE: TRUE
    add_cpnodeid_list_1:
    - CPNAME: 'smfnode2'
      CPNODEIDTYPE: IPV6
      IPV6NODEID: 'FC00:0:0:0:10:0:0:1'
      LOCALEMERNODE: TRUE
    add_cpnodeid_list_2:
    - CPNAME: 'smfnode3'
      CPNODEIDTYPE: FQDN
      FQDNNODEID: 'consumer.huawei.com'
      LOCALEMERNODE: TRUE
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 打开本地应急接入特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 3 配置应急AMF在收到基站消息，本地无用户上下文时的处理策略。

```jinja2
{%- for item in set_ngmmfunc_list -%}
    SET NGMMFUNC:
    {#- --- 可选参数 --- -#}
    {%- if item.NOUECTXOPTSW is not none -%}
        NOUECTXOPTSW={{item.NOUECTXOPTSW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 配置惯性运行功能对数据面非连接态用户不生效，PFCP路径断后连接态用户进入惯性运行状态的等待时长和非5G用户支持惯性运行。

```jinja2
{%- for item in set_inertialoper_list -%}
    SET INERTIALOPER:
    {#- --- 可选参数 --- -#}
    {%- if item.IDLEUSRIGNORE is not none -%}
        IDLEUSRIGNORE={{item.IDLEUSRIGNORE}},
    {%- endif -%}
    {%- if item.DELAYTIME is not none -%}
        DELAYTIME={{item.DELAYTIME}},
    {%- endif -%}
    {%- if item.NON5GUSRIGNORE is not none -%}
        NON5GUSRIGNORE={{item.NON5GUSRIGNORE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 （可选）设置惯性运行/应急接入授权开关及时长，避免用户在边缘网络与中心网络恢复后长期在边缘应急控制面接入运行。

```jinja2
{%- if is_optional_emergency_auth_timer -%}
    {%- for item in set_emergauthtimer_list -%}
        SET EMERGAUTHTIMER:
        {#- --- 必选参数 --- -#}
        SWITCH={{item.SWITCH}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SWITCH=ENABLE 时必选 --- -#}
        {%- if item.SWITCH == 'ENABLE' -%}
            HOURS={{item.HOURS}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 6 5中“惯性运行/应急接入授权开关（SWITCH）”参数设置为“ENABLE”时，配置应急SMF的NODE信息。

#### 6.1 //“CPNODEIDTYPE”设置为“IPV4”时：

```jinja2
{%- set SET_EMERGAUTHTIMER=getParameterValue('SET EMERGAUTHTIMER') -%}
{%- if is_scenario_ipv4 and SET_EMERGAUTHTIMER -%}
    {%- for item in add_cpnodeid_list -%}
        ADD CPNODEID:
        {#- --- 必选参数 --- -#}
        CPNAME="{{item.CPNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.CPNODEIDTYPE is not none -%}
            CPNODEIDTYPE={{item.CPNODEIDTYPE}},
        {%- endif -%}
        {%- if item.LOCALEMERNODE is not none -%}
            LOCALEMERNODE={{item.LOCALEMERNODE}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：CPNODEIDTYPE=IPV4 时可选 --- -#}
        {%- if item.CPNODEIDTYPE == 'IPV4' -%}
            {%- if item.IPV4NODEID is not none -%}
                IPV4NODEID="{{item.IPV4NODEID}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 6.2 //“CPNODEIDTYPE”设置为“IPV6”时：

```jinja2
{%- if is_scenario_ipv6 and SET_EMERGAUTHTIMER -%}
    {%- for item in add_cpnodeid_list_1 -%}
        ADD CPNODEID:
        {#- --- 必选参数 --- -#}
        CPNAME="{{item.CPNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.CPNODEIDTYPE is not none -%}
            CPNODEIDTYPE={{item.CPNODEIDTYPE}},
        {%- endif -%}
        {%- if item.LOCALEMERNODE is not none -%}
            LOCALEMERNODE={{item.LOCALEMERNODE}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：CPNODEIDTYPE=IPV6 时可选 --- -#}
        {%- if item.CPNODEIDTYPE == 'IPV6' -%}
            {%- if item.IPV6NODEID is not none -%}
                IPV6NODEID="{{item.IPV6NODEID}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 6.3 //“CPNODEIDTYPE”设置为“FQDN”时：

```jinja2
{%- if is_scenario_fqdn and SET_EMERGAUTHTIMER -%}
    {%- for item in add_cpnodeid_list_2 -%}
        ADD CPNODEID:
        {#- --- 必选参数 --- -#}
        CPNAME="{{item.CPNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.CPNODEIDTYPE is not none -%}
            CPNODEIDTYPE={{item.CPNODEIDTYPE}},
        {%- endif -%}
        {%- if item.LOCALEMERNODE is not none -%}
            LOCALEMERNODE={{item.LOCALEMERNODE}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：CPNODEIDTYPE=FQDN 时可选 --- -#}
        {%- if item.CPNODEIDTYPE == 'FQDN' -%}
            {%- if item.FQDNNODEID is not none -%}
                FQDNNODEID="{{item.FQDNNODEID}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

