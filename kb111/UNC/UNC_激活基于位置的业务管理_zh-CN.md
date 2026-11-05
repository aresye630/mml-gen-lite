---
id: ''
name: 激活基于位置的业务管理
ne_type: UNC
type: feature
description: 当运营商期望根据用户所在位置采取差异化策略（基于用户的位置分配IP地址或性能统计数据上报）时，可以配置基于位置的业务管理功能。  适用于GGSN、PGW-C、SMF。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","智能PCC解决方案","WSFD-109105 基于位置的业务管理","激活基于位置的业务管理"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当运营商期望根据用户所在位置采取差异化策略（基于用户的位置分配IP地址或性能统计数据上报）时，可以配置基于位置的业务管理功能。适用于GGSN、PGW-C、SMF。

## 必备事项
前提条件

* 请仔细阅读WSFD-109105 基于位置的业务管理。
* 完成加载License（如果有需求，请联系华为技术支持工程师处理）。
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
    add_racgroup_list:
      type: items
      properties:
        RACGROUPNAME:
          name: 'RAC组名'
          type: string
          minLength: 1
          maxLength: 32
          required: true
          description: 'UNC作为GGSN时，需要RAC作为位置信息时需要规划。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_racid_list:
      type: items
      properties:
        RACSECNUM:
          name: 'RAC段编号'
          type: integer
          minimum: 0
          maximum: 2047
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        RACSTARTID:
          name: 'RAC起始ID'
          type: string
          minLength: 4
          maxLength: 4
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        RACENDID:
          name: 'RAC截止ID'
          type: string
          minLength: 4
          maxLength: 4
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        RACGROUPNAME:
          name: 'RAC组名'
          type: string
          minLength: 1
          maxLength: 32
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_lacgroup_list:
      type: items
      properties:
        LACGROUPNAME:
          name: 'LAC组名'
          type: string
          minLength: 0
          maxLength: 32
          required: true
          description: 'UNC作为GGSN时，需要LAC作为位置信息时需要规划。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_lacid_list:
      type: items
      properties:
        LACSECNUM:
          name: 'LAC段编号'
          type: integer
          minimum: 0
          maximum: 23999
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        LACSTARTID:
          name: 'LAC起始ID'
          type: string
          minLength: 6
          maxLength: 6
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        LACENDID:
          name: 'LAC截止ID'
          type: string
          minLength: 6
          maxLength: 6
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        LACGROUPNAME:
          name: 'LAC组名'
          type: string
          minLength: 1
          maxLength: 32
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_tacgroup_list:
      type: items
      properties:
        TACGROUPNAME:
          name: 'TAC组名'
          type: string
          minLength: 0
          maxLength: 32
          required: true
          description: 'UNC作为PGW-C/SMF时，需要TAC作为位置信息时需要规划。  UNC作为PGW-C时，TACTYPE设置为  S1Tac；  UNC作为SMF时，TACTYPE设置为  N2Tac。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TACTYPE:
          name: 'TAC类型'
          type: string
          enum:
          - S1Tac
          - N2Tac
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_s1tacid_list:
      type: items
      properties:
        TACSECNUM:
          name: 'TAC组编号'
          type: integer
          minimum: 0
          maximum: 15999
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        TACSTARTID:
          name: 'TAC起始ID'
          type: string
          minLength: 3
          maxLength: 6
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        TACENDID:
          name: 'TAC截止ID'
          type: string
          minLength: 3
          maxLength: 6
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        TACGROUPNAME:
          name: 'TAC组名'
          type: string
          minLength: 1
          maxLength: 32
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_n2tacid_list:
      type: items
      properties:
        TACSECNUM:
          name: 'TAC组编号'
          type: integer
          minimum: 0
          maximum: 15999
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        TACSTARTID:
          name: 'TAC起始ID'
          type: string
          minLength: 3
          maxLength: 8
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        TACENDID:
          name: 'TAC截止ID'
          type: string
          minLength: 3
          maxLength: 8
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        TACGROUPNAME:
          name: 'TAC组名'
          type: string
          minLength: 1
          maxLength: 32
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_srvnodegroup_list:
      type: items
      properties:
        GROUPNAME:
          name: 'Serving Node Group名称'
          type: string
          minLength: 1
          maxLength: 32
          required: true
          description: 'UNC作为GGSN/PGW-C，需要SGSN IP/SGW IP/PCF IP/HSGW IP/TWAN IP/ePDG IP作为位置信息时需要规划。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_srvnodeip_list:
      type: items
      properties:
        GROUPNAME:
          name: 'Serving Node Group名称'
          type: string
          minLength: 0
          maxLength: 32
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IPSECTIONID:
          name: 'Serving Node IP地址段编号'
          type: integer
          minimum: 0
          maximum: 2999
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP版本'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV4ADDRSTART:
          name: 'Serving Node IPV4地址段的起始地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4ADDREND:
          name: 'Serving Node IPV4地址段的结束地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV6ADDREND:
          name: '服务节点IPV6地址段的结束地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6ADDRSTART:
          name: '服务节点IPV6地址段的起始地址'
          type: string
          maxLength: 39
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
          description: '规划虚拟APN。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VIRTUALAPN:
          name: '虚拟APN'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
    add_virtualapnrule_list:
      type: items
      properties:
        VIRTUALAPN:
          name: '虚拟APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '-'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        MAPPINGTYPE:
          name: '映射方式'
          type: string
          enum:
          - IMSI
          - MSISDN
          - RAT
          - PCO
          - RADIUS
          - LOAD_BALANCE
          - CHARGE_CHAR
          - REDUNDANCY
          - VDEFAULT_APN
          - IMEI
          - LAC_GROUP
          - TAC_GROUP
          - RAC_GROUP
          - PLMN
          - SERVING_GROUP
          - ROAMING
          - MULTIPARA
          - SELECTION_MODE
          - NS
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: '该参数用于指定配置的映射规则的优先级。   * 值越小优先级越高，不允许指定相同的优先级。 * 如果priority参数没有配置，表明优先级最低。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MAPPINGVALUE:
          name: '映射值'
          type: string
          minLength: 0
          maxLength: 95
          required: false
          description: '用于指定所选映射值。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        REALAPN:
          name: '真实APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: '用于表示配置的规则对应的APN。该APN必须是系统已经配置的APN。  已通过**ADD APN**命令配置，可以使用**LST APN**命令进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        REALAPNSWITCH:
          name: '真实APN开关'
          type: string
          enum:
          - Disable
          - Enable
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CCMODE:
          name: '计费属性模式'
          type: string
          enum:
          - Normal
          - Hotbilling
          - Prepaid
          - FlatBilling
          - Specific
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMEI:
          name: 'IMEI'
          type: string
          minLength: 1
          maxLength: 16
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMSI:
          name: 'IMSI'
          type: string
          minLength: 1
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LACGROUP:
          name: 'LAC组名'
          type: string
          minLength: 0
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MSISDN:
          name: 'MSISDN'
          type: string
          minLength: 1
          maxLength: 17
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PCOSWITCH:
          name: 'PCO开关'
          type: string
          enum:
          - Disable
          - Enable
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PLMN:
          name: 'PLMN'
          type: string
          minLength: 5
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RACGROUP:
          name: 'RAC组名'
          type: string
          minLength: 0
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RATTYPE:
          name: '无线接入类型'
          type: string
          enum:
          - Utran
          - Geran
          - Wlan
          - Gan
          - Eutran
          - EutranNbIoT
          - Ngran
          - Redcap
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ROAMING:
          name: '漫游状态'
          type: string
          enum:
          - Home
          - Roaming
          - Visiting
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SD:
          name: '切片细分标识'
          type: string
          minLength: 6
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SELECTIONMODE:
          name: '选择模式'
          type: string
          enum:
          - MsNetProApn
          - MsProApn
          - NetProApn
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRVNODEGROUP:
          name: 'Serving Node组名称'
          type: string
          minLength: 0
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SST:
          name: '切片业务类型'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TACGROUP:
          name: 'TAC组名'
          type: string
          minLength: 0
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3WPLBSM11'
      SWITCH: ENABLE
    add_racgroup_list:
    - RACGROUPNAME: 'CityA'
    add_racid_list:
    - RACSECNUM: 0
      RACSTARTID: '0x11'
      RACENDID: '0x20'
      RACGROUPNAME: 'CityA'
    add_lacgroup_list:
    - LACGROUPNAME: 'CityA'
    add_lacid_list:
    - LACSECNUM: 1
      LACSTARTID: '0x0121'
      LACENDID: '0x0130'
      LACGROUPNAME: 'CityA'
    add_tacgroup_list:
    - TACGROUPNAME: 'CityB'
      TACTYPE: S1Tac
    add_s1tacid_list:
    - TACSECNUM: 3
      TACSTARTID: '0x0136'
      TACENDID: '0x0140'
      TACGROUPNAME: 'CityB'
    add_n2tacid_list:
    - TACSECNUM: 3
      TACSTARTID: '0x0136'
      TACENDID: '0x0140'
      TACGROUPNAME: 'CityB'
    add_srvnodegroup_list:
    - GROUPNAME: 'CityD'
    add_srvnodeip_list:
    - GROUPNAME: 'CityD'
      IPSECTIONID: 1
      IPVERSION: IPV4
      IPV4ADDRSTART: '192.168.1.10'
      IPV4ADDREND: '192.168.1.120'
      IPV6ADDREND: ''
      IPV6ADDRSTART: ''
    add_apn_list:
    - APN: 'example.com'
      VIRTUALAPN: ENABLE
    add_virtualapnrule_list:
    - VIRTUALAPN: 'example.com'
      MAPPINGTYPE: RAC_GROUP
      PRIORITY: 1
      MAPPINGVALUE: 'CityA'
      REALAPN: 'huawei.com'
      REALAPNSWITCH: ''
      CCMODE: ''
      IMEI: ''
      IMSI: ''
      LACGROUP: ''
      MSISDN: ''
      PCOSWITCH: ''
      PLMN: ''
      RACGROUP: ''
      RATTYPE: ''
      ROAMING: ''
      SD: ''
      SELECTIONMODE: ''
      SRVNODEGROUP: ''
      SST: ''
      TACGROUP: ''
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

### 步骤 3～步骤 6几个步骤之间相互独立，可以单个参数作为位置信息，也可以多个参数的组合作为位置信息。请根据实际规划配置。

### 3 UNC作为GGSN时，配置位置信息（RAC作为位置信息）。

#### 3.1 增加RAC组。

```jinja2
{%- if is_scenario_rac -%}
    {%- for item in add_racgroup_list -%}
        ADD RACGROUP:
        {#- --- 必选参数 --- -#}
        RACGROUPNAME="{{item.RACGROUPNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.2 增加RAC段。

```jinja2
{%- if is_scenario_rac -%}
    {%- for item in add_racid_list -%}
        ADD RACID:
        {#- --- 必选参数 --- -#}
        RACSECNUM={{item.RACSECNUM}},
        RACSTARTID="{{item.RACSTARTID}}",
        RACENDID="{{item.RACENDID}}",
        RACGROUPNAME="{{item.RACGROUPNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

### 4 UNC作为GGSN时，配置位置信息（LAC作为位置信息）。

#### 4.1 增加LAC组。

```jinja2
{%- if is_scenario_lac -%}
    {%- for item in add_lacgroup_list -%}
        ADD LACGROUP:
        {#- --- 必选参数 --- -#}
        LACGROUPNAME="{{item.LACGROUPNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.2 增加LAC段。

```jinja2
{%- if is_scenario_lac -%}
    {%- for item in add_lacid_list -%}
        ADD LACID:
        {#- --- 必选参数 --- -#}
        LACSECNUM={{item.LACSECNUM}},
        LACSTARTID="{{item.LACSTARTID}}",
        LACENDID="{{item.LACENDID}}",
        LACGROUPNAME="{{item.LACGROUPNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

### 5 UNC作为PGW-C/SMF时，配置位置信息（TAC作为位置信息）。

#### 5.1 增加TAC组。

```jinja2
{%- if is_scenario_tac -%}
    {%- for item in add_tacgroup_list -%}
        ADD TACGROUP:
        {#- --- 必选参数 --- -#}
        TACGROUPNAME="{{item.TACGROUPNAME}}",
        TACTYPE={{item.TACTYPE}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 5.2 增加TAC段。

##### 5.2.1 UNC作为PGW-C：**ADD S1TACID**

```jinja2
{%- if is_scenario_tac and is_scenario_pgw_c -%}
    {%- for item in add_s1tacid_list -%}
        ADD S1TACID:
        {#- --- 必选参数 --- -#}
        TACSECNUM={{item.TACSECNUM}},
        TACSTARTID="{{item.TACSTARTID}}",
        TACENDID="{{item.TACENDID}}",
        TACGROUPNAME="{{item.TACGROUPNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 5.2.2 UNC作为SMF：**ADD N2TACID**

```jinja2
{%- if is_scenario_tac and is_scenario_smf -%}
    {%- for item in add_n2tacid_list -%}
        ADD N2TACID:
        {#- --- 必选参数 --- -#}
        TACENDID="{{item.TACENDID}}",
        TACGROUPNAME="{{item.TACGROUPNAME}}",
        TACSECNUM={{item.TACSECNUM}},
        TACSTARTID="{{item.TACSTARTID}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

### 6 UNC作为GGSN/PGW-C时，配置位置信息（SGSN IP/SGW IP/ePDG IP作为位置信息）。

#### 6.1 增加服务节点组。

```jinja2
{%- if is_scenario_srvnode_ip -%}
    {%- for item in add_srvnodegroup_list -%}
        ADD SRVNODEGROUP:
        {#- --- 必选参数 --- -#}
        GROUPNAME="{{item.GROUPNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 6.2 增加服务节点IP地址段。

```jinja2
{%- if is_scenario_srvnode_ip -%}
    {%- for item in add_srvnodeip_list -%}
        ADD SRVNODEIP:
        {#- --- 必选参数 --- -#}
        GROUPNAME="{{item.GROUPNAME}}",
        IPSECTIONID={{item.IPSECTIONID}},
        IPVERSION={{item.IPVERSION}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
        {%- if item.IPVERSION == 'IPV4' -%}
            IPV4ADDRSTART="{{item.IPV4ADDRSTART}}",
        {%- endif -%}
        {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
        {%- if item.IPVERSION == 'IPV4' -%}
            IPV4ADDREND="{{item.IPV4ADDREND}}",
        {%- endif -%}
        {#- --- 条件必选：IPVERSION=IPV6 时必选 --- -#}
        {%- if item.IPVERSION == 'IPV6' -%}
            IPV6ADDREND="{{item.IPV6ADDREND}}",
        {%- endif -%}
        {#- --- 条件必选：IPVERSION=IPV6 时必选 --- -#}
        {%- if item.IPVERSION == 'IPV6' -%}
            IPV6ADDRSTART="{{item.IPV6ADDRSTART}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 7 配置APN，开启虚拟APN功能。

```jinja2
{%- for item in add_apn_list -%}
    ADD APN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.VIRTUALAPN is not none -%}
        VIRTUALAPN={{item.VIRTUALAPN}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 8 配置虚拟APN与真实APN的映射规则。

```jinja2
{%- for item in add_virtualapnrule_list -%}
    ADD VIRTUALAPNRULE:
    {#- --- 必选参数 --- -#}
    VIRTUALAPN="{{item.VIRTUALAPN}}",
    MAPPINGTYPE={{item.MAPPINGTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：MAPPINGTYPE=IMSI/IMEI/MSISDN/LAC_GROUP/TAC_GROUP/RAC_GROUP/PLMN/SERVING_GROUP 时必选 --- -#}
    {%- if item.MAPPINGTYPE in ['IMSI', 'IMEI', 'MSISDN', 'LAC_GROUP', 'TAC_GROUP', 'RAC_GROUP', 'PLMN', 'SERVING_GROUP'] -%}
        MAPPINGVALUE="{{item.MAPPINGVALUE}}",
    {%- endif -%}
    {#- --- 条件必选：MAPPINGTYPE=CHARGE_CHAR/IMSI/IMEI/MSISDN/LAC_GROUP/TAC_GROUP/RAC_GROUP/PLMN/SERVING_GROUP/SELECTION_MODE/MULTIPARA/RAT/LOAD_BALANCE/ROAMING/REDUNDANCY/VDEFAULT_APN/NS 时必选 --- -#}
    {%- if item.MAPPINGTYPE in ['CHARGE_CHAR', 'IMSI', 'IMEI', 'MSISDN', 'LAC_GROUP', 'TAC_GROUP', 'RAC_GROUP', 'PLMN', 'SERVING_GROUP', 'SELECTION_MODE', 'MULTIPARA', 'RAT', 'LOAD_BALANCE', 'ROAMING', 'REDUNDANCY', 'VDEFAULT_APN', 'NS'] -%}
        REALAPN="{{item.REALAPN}}",
    {#- --- 条件必选：REALAPNSWITCH=Enable 时必选 --- -#}
    {%- elif item.REALAPNSWITCH == 'Enable' -%}
        REALAPN="{{item.REALAPN}}",
    {%- endif -%}
    {#- --- 条件必选：MAPPINGTYPE=PCO 时必选 --- -#}
    {%- if item.MAPPINGTYPE == 'PCO' -%}
        REALAPNSWITCH={{item.REALAPNSWITCH}},
    {%- endif -%}
    {#- --- 条件必选：MAPPINGTYPE=NS 时必选 --- -#}
    {%- if item.MAPPINGTYPE == 'NS' -%}
        SST={{item.SST}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：MAPPINGTYPE=MULTIPARA 时可选 --- -#}
    {%- if item.MAPPINGTYPE == 'MULTIPARA' -%}
        {%- if item.IMEI is not none -%}
            IMEI="{{item.IMEI}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：MAPPINGTYPE=MULTIPARA 时可选 --- -#}
    {%- if item.MAPPINGTYPE == 'MULTIPARA' -%}
        {%- if item.IMSI is not none -%}
            IMSI="{{item.IMSI}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：MAPPINGTYPE=MULTIPARA 时可选 --- -#}
    {%- if item.MAPPINGTYPE == 'MULTIPARA' -%}
        {%- if item.LACGROUP is not none -%}
            LACGROUP="{{item.LACGROUP}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：MAPPINGTYPE=MULTIPARA 时可选 --- -#}
    {%- if item.MAPPINGTYPE == 'MULTIPARA' -%}
        {%- if item.MSISDN is not none -%}
            MSISDN="{{item.MSISDN}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：MAPPINGTYPE=MULTIPARA 时可选 --- -#}
    {%- if item.MAPPINGTYPE == 'MULTIPARA' -%}
        {%- if item.PCOSWITCH is not none -%}
            PCOSWITCH={{item.PCOSWITCH}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：MAPPINGTYPE=MULTIPARA 时可选 --- -#}
    {%- if item.MAPPINGTYPE == 'MULTIPARA' -%}
        {%- if item.PLMN is not none -%}
            PLMN="{{item.PLMN}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：MAPPINGTYPE=MULTIPARA 时可选 --- -#}
    {%- if item.MAPPINGTYPE == 'MULTIPARA' -%}
        {%- if item.RACGROUP is not none -%}
            RACGROUP="{{item.RACGROUP}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：MAPPINGTYPE=NS 时可选 --- -#}
    {%- if item.MAPPINGTYPE == 'NS' -%}
        {%- if item.SD is not none -%}
            SD="{{item.SD}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：MAPPINGTYPE=MULTIPARA 时可选 --- -#}
    {%- if item.MAPPINGTYPE == 'MULTIPARA' -%}
        {%- if item.SRVNODEGROUP is not none -%}
            SRVNODEGROUP="{{item.SRVNODEGROUP}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：MAPPINGTYPE=MULTIPARA 时可选 --- -#}
    {%- if item.MAPPINGTYPE == 'MULTIPARA' -%}
        {%- if item.TACGROUP is not none -%}
            TACGROUP="{{item.TACGROUP}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件必选/可选参数 --- -#}
    {#- --- 优先级: 条件必选(映射方式=MULTIPARA) / 条件可选(映射方式=RADIUS|CHARGE_CHAR|IMSI|IMEI|MSISDN|LAC_GROUP|TAC_GROUP|RAC_GROUP|PLMN|SERVING_GROUP|PCO|SELECTION_MODE|RAT|LOAD_BALANCE|ROAMING|REDUNDANCY) --- -#}
    {%- if (item.MAPPINGTYPE == 'MULTIPARA') -%}
        PRIORITY={{item.PRIORITY}},
    {%- elif (item.MAPPINGTYPE in ['RADIUS', 'CHARGE_CHAR', 'IMSI', 'IMEI', 'MSISDN', 'LAC_GROUP', 'TAC_GROUP', 'RAC_GROUP', 'PLMN', 'SERVING_GROUP', 'PCO', 'SELECTION_MODE', 'RAT', 'LOAD_BALANCE', 'ROAMING', 'REDUNDANCY']) -%}
        {%- if item.PRIORITY is not none -%}
            PRIORITY={{item.PRIORITY}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 计费属性模式: 条件必选(映射方式=CHARGE_CHAR) / 条件可选(映射方式=MULTIPARA) --- -#}
    {%- if (item.MAPPINGTYPE == 'CHARGE_CHAR') -%}
        CCMODE={{item.CCMODE}},
    {%- elif (item.MAPPINGTYPE == 'MULTIPARA') -%}
        {%- if item.CCMODE is not none -%}
            CCMODE={{item.CCMODE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 无线接入类型: 条件必选(映射方式=RAT) / 条件可选(映射方式=MULTIPARA) --- -#}
    {%- if (item.MAPPINGTYPE == 'RAT') -%}
        RATTYPE={{item.RATTYPE}},
    {%- elif (item.MAPPINGTYPE == 'MULTIPARA') -%}
        {%- if item.RATTYPE is not none -%}
            RATTYPE={{item.RATTYPE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 漫游状态: 条件必选(映射方式=ROAMING) / 条件可选(映射方式=MULTIPARA) --- -#}
    {%- if (item.MAPPINGTYPE == 'ROAMING') -%}
        ROAMING={{item.ROAMING}},
    {%- elif (item.MAPPINGTYPE == 'MULTIPARA') -%}
        {%- if item.ROAMING is not none -%}
            ROAMING={{item.ROAMING}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 选择模式: 条件必选(映射方式=SELECTION_MODE) / 条件可选(映射方式=MULTIPARA) --- -#}
    {%- if (item.MAPPINGTYPE == 'SELECTION_MODE') -%}
        SELECTIONMODE={{item.SELECTIONMODE}},
    {%- elif (item.MAPPINGTYPE == 'MULTIPARA') -%}
        {%- if item.SELECTIONMODE is not none -%}
            SELECTIONMODE={{item.SELECTIONMODE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

