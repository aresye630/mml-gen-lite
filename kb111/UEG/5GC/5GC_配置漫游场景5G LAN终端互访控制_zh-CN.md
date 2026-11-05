---
id: ''
name: 配置漫游场景5G LAN终端互访控制
ne_type: UEG
type: feature
description: '* 漫游场景，当运营商禁止终端通过锚点UPF的N9口互访但同一5G LAN组成员存在互访诉求时，可通过本功能允许漫游5G LAN终端与同一5G LAN组的其他终端之间的互访。 * 漫游组网，当运营商禁止终端通过锚点UPF的N9口互访且同一5G LAN组成员不存在互访诉求时，可通过本功能禁止漫游5G LAN终端与同一5G LAN组的其他终端之间的互访。  * 本功能中描述的漫游场景，是指5G LAN终端（主叫或被叫或主叫+被叫）通过I-UPF与锚点UPF交互的场景。 * 同一个层二5G LAN组成员之间默认不禁止互访，同一个层三5G LAN组成员之间默认不禁止互访。'
tags: []
risk_level: ''
doc_source: ["专线（仅连接，地市共享式）","网络部署","5GC toB 部署边缘站点（广域5G LAN，共享式）","配置广域5G LAN","运营商侧配置","核心网侧广域5G LAN业务配置","广域5G LAN增量配置（可选）","配置漫游场景5G LAN终端互访控制"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
* 漫游场景，当运营商禁止终端通过锚点UPF的N9口互访但同一5G LAN组成员存在互访诉求时，可通过本功能允许漫游5G LAN终端与同一5G LAN组的其他终端之间的互访。* 漫游组网，当运营商禁止终端通过锚点UPF的N9口互访且同一5G LAN组成员不存在互访诉求时，可通过本功能禁止漫游5G LAN终端与同一5G LAN组的其他终端之间的互访。* 本功能中描述的漫游场景，是指5G LAN终端（主叫或被叫或主叫+被叫）通过I-UPF与锚点UPF交互的场景。* 同一个层二5G LAN组成员之间默认不禁止互访，同一个层三5G LAN组成员之间默认不禁止互访。

## 必备事项
前提条件

前提条件

前提条件

已完成配置UPF数据（VXLAN隧道方案）。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_ngvnuemutacc_list:
      type: items
      properties:
        VNINSTANCE:
          name: '5G LAN组名称'
          type: string
          minLength: 0
          maxLength: 37
          required: true
          description: '使用配置5G LAN基本功能中的5G LAN组名称。  可通过**LST NGVNINSTANCE**命令查询获取。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        N9AUE2UEUNIPOL:
          name: 'N9A口单播互访控制策略'
          type: string
          enum:
          - ALLOW_FWD
          - FORBID_FWD
          - WHITELIST_FWD
          required: false
          description: '该参数用于控制互访的单播报文，此处以允许互访为例。   * 禁止互访时，需设置为FORBID\_FWD。 * 基于白名单允许互访时，需设置为WHITELIST\_FWD。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        N9AUE2UEMULPOL:
          name: 'N9A口组播互访控制策略'
          type: string
          enum:
          - ALLOW_FWD
          - FORBID_FWD
          - WHITELIST_FWD
          required: false
          description: '该参数用于控制互访的组播报文，此处以允许互访为例。   * 禁止互访时，需设置为FORBID\_FWD。 * 基于白名单允许互访时，需设置为WHITELIST\_FWD。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        N9AUE2UEBROPOL:
          name: 'N9A口广播互访控制策略'
          type: string
          enum:
          - ALLOW_FWD
          - FORBID_FWD
          - WHITELIST_FWD
          required: false
          description: '该参数用于控制互访的广播报文，此处以允许互访为例。   * 禁止互访时，需设置为FORBID\_FWD。 * 基于白名单允许互访时，需设置为WHITELIST\_FWD。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        N19UE2UESW:
          name: '发往N19接口报文的UE互访开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
    set_ngvnuemutacc_list_1:
      type: items
      properties:
        VNINSTANCE:
          name: '5G LAN组名称'
          type: string
          minLength: 0
          maxLength: 37
          required: true
          description: '使用配置5G LAN基本功能中的5G LAN组名称。  可通过**LST NGVNINSTANCE**命令查询获取。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        N9AUE2UEUNIPOL:
          name: 'N9A口单播互访控制策略'
          type: string
          enum:
          - ALLOW_FWD
          - FORBID_FWD
          - WHITELIST_FWD
          required: false
          description: '该参数用于控制互访的单播报文，此处以允许互访为例。   * 禁止互访时，需设置为FORBID\_FWD。 * 基于白名单允许互访时，需设置为WHITELIST\_FWD。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        N9AUE2UEMULPOL:
          name: 'N9A口组播互访控制策略'
          type: string
          enum:
          - ALLOW_FWD
          - FORBID_FWD
          - WHITELIST_FWD
          required: false
          description: '该参数用于控制互访的组播报文，此处以允许互访为例。   * 禁止互访时，需设置为FORBID\_FWD。 * 基于白名单允许互访时，需设置为WHITELIST\_FWD。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        N9AUE2UEBROPOL:
          name: 'N9A口广播互访控制策略'
          type: string
          enum:
          - ALLOW_FWD
          - FORBID_FWD
          - WHITELIST_FWD
          required: false
          description: '该参数用于控制互访的广播报文，此处以允许互访为例。   * 禁止互访时，需设置为FORBID\_FWD。 * 基于白名单允许互访时，需设置为WHITELIST\_FWD。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        N19UE2UESW:
          name: '发往N19接口报文的UE互访开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
    set_ngvnuemutacc_list_2:
      type: items
      properties:
        VNINSTANCE:
          name: '5G LAN组名称'
          type: string
          minLength: 0
          maxLength: 37
          required: true
          description: '使用配置5G LAN基本功能中的5G LAN组名称。  可通过**LST NGVNINSTANCE**命令查询获取。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        N9AUE2UEUNIPOL:
          name: 'N9A口单播互访控制策略'
          type: string
          enum:
          - ALLOW_FWD
          - FORBID_FWD
          - WHITELIST_FWD
          required: false
          description: '该参数用于控制互访的单播报文，此处以允许互访为例。   * 禁止互访时，需设置为FORBID\_FWD。 * 基于白名单允许互访时，需设置为WHITELIST\_FWD。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        N9AUE2UEMULPOL:
          name: 'N9A口组播互访控制策略'
          type: string
          enum:
          - ALLOW_FWD
          - FORBID_FWD
          - WHITELIST_FWD
          required: false
          description: '该参数用于控制互访的组播报文，此处以允许互访为例。   * 禁止互访时，需设置为FORBID\_FWD。 * 基于白名单允许互访时，需设置为WHITELIST\_FWD。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        N9AUE2UEBROPOL:
          name: 'N9A口广播互访控制策略'
          type: string
          enum:
          - ALLOW_FWD
          - FORBID_FWD
          - WHITELIST_FWD
          required: false
          description: '该参数用于控制互访的广播报文，此处以允许互访为例。   * 禁止互访时，需设置为FORBID\_FWD。 * 基于白名单允许互访时，需设置为WHITELIST\_FWD。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        N19UE2UESW:
          name: '发往N19接口报文的UE互访开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
    add_uemutaccwlist_list:
      type: items
      properties:
        WLISTNAME:
          name: '白名单名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '存在多条数据时，该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP协议版本'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: '该参数采用的是与锚点UPF互通的I-UPF的N9c逻辑接口IP地址。可通过**LST LOGICINF**命令查询获取。  如允许漫游5G LAN终端通过2个I-UPF与锚点UPF交互，则需要将这2个I-UPF的N9c逻辑接口IP地址均配置到白名单中。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4START:
          name: 'IPv4起始地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        IPV4END:
          name: 'IPv4截止地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
    add_ngbinduemutwl_list:
      type: items
      properties:
        VNINSTANCE:
          name: '5G LAN组名称'
          type: string
          minLength: 0
          maxLength: 37
          required: true
          description: '使用配置5G LAN基本功能中的5G LAN组名称。  可通过**LST NGVNINSTANCE**命令查询获取。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        WLISTNAME:
          name: '白名单名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '使用**ADD UWMUTACCWLIST**定义的白名单名称。  可通过**LST UWMUTACCWLIST**命令查询获取。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
  examples:
    set_ngvnuemutacc_list:
    - VNINSTANCE: '000003e9-460-08-01'
      N9AUE2UEUNIPOL: FORBID_FWD
      N9AUE2UEMULPOL: FORBID_FWD
      N9AUE2UEBROPOL: FORBID_FWD
      N19UE2UESW: ENABLE
    set_ngvnuemutacc_list_1:
    - VNINSTANCE: '000003e9-460-08-01'
      N9AUE2UEUNIPOL: ALLOW_FWD
      N9AUE2UEMULPOL: ALLOW_FWD
      N9AUE2UEBROPOL: ALLOW_FWD
      N19UE2UESW: DISABLE
    set_ngvnuemutacc_list_2:
    - VNINSTANCE: '000003e9-460-08-01'
      N9AUE2UEUNIPOL: WHITELIST_FWD
      N9AUE2UEMULPOL: WHITELIST_FWD
      N9AUE2UEBROPOL: WHITELIST_FWD
      N19UE2UESW: ENABLE
    add_uemutaccwlist_list:
    - WLISTNAME: 'I-UPF-01'
      IPVERSION: IPV4
      IPV4START: '192.168.111.1'
      IPV4END: '192.168.111.1'
    - WLISTNAME: 'I-UPF-02'
      IPVERSION: IPV4
      IPV4START: '192.168.112.1'
      IPV4END: '192.168.112.1'
    add_ngbinduemutwl_list:
    - VNINSTANCE: '000003e9-460-08-01'
      WLISTNAME: 'I-UPF-01'
    - VNINSTANCE: '000003e9-460-08-01'
      WLISTNAME: 'I-UPF-02'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 **//任务示例1**

#### 1.1 //此处以禁止漫游5G LAN终端与该5G LAN组中的其他终端互访为例，禁止所有漫游互访的报文（单播、组播、广播）。（“N19UE2UESW”参数仅在负荷分担场景时需要配置，主备容灾场景下无需配置）

```jinja2
{%- if is_scenario_forbid_access -%}
    {%- for item in set_ngvnuemutacc_list -%}
        SET NGVNUEMUTACC:
        {#- --- 必选参数 --- -#}
        VNINSTANCE="{{item.VNINSTANCE}}",
        {#- --- 可选参数 --- -#}
        {%- if item.N9AUE2UEUNIPOL is not none -%}
            N9AUE2UEUNIPOL={{item.N9AUE2UEUNIPOL}},
        {%- endif -%}
        {%- if item.N9AUE2UEMULPOL is not none -%}
            N9AUE2UEMULPOL={{item.N9AUE2UEMULPOL}},
        {%- endif -%}
        {%- if item.N9AUE2UEBROPOL is not none -%}
            N9AUE2UEBROPOL={{item.N9AUE2UEBROPOL}},
        {%- endif -%}
        {%- if item.N19UE2UESW is not none -%}
            N19UE2UESW={{item.N19UE2UESW}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 2 **//任务示例2**

#### 2.1 //此处以允许漫游5G LAN终端与该5G LAN组中的其他终端互访，互访报文包括单播、组播和广播为例。请根据局点实际业务规划允许哪类报文。（“N19UE2UESW”参数仅在负荷分担场景时需要配置，主备容灾场景下无需配置）

```jinja2
{%- if is_scenario_allow_access -%}
    {%- for item in set_ngvnuemutacc_list_1 -%}
        SET NGVNUEMUTACC:
        {#- --- 必选参数 --- -#}
        VNINSTANCE="{{item.VNINSTANCE}}",
        {#- --- 可选参数 --- -#}
        {%- if item.N9AUE2UEUNIPOL is not none -%}
            N9AUE2UEUNIPOL={{item.N9AUE2UEUNIPOL}},
        {%- endif -%}
        {%- if item.N9AUE2UEMULPOL is not none -%}
            N9AUE2UEMULPOL={{item.N9AUE2UEMULPOL}},
        {%- endif -%}
        {%- if item.N9AUE2UEBROPOL is not none -%}
            N9AUE2UEBROPOL={{item.N9AUE2UEBROPOL}},
        {%- endif -%}
        {%- if item.N19UE2UESW is not none -%}
            N19UE2UESW={{item.N19UE2UESW}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 3 **//任务示例3**

#### 3.1 //此处以基于5G LAN组+白名单方案允许漫游5G LAN终端与该5G LAN组中的其他终端互访，互访报文包括单播、组播和广播为例。（“N19UE2UESW”参数仅在负荷分担场景时需要配置，主备容灾场景下无需配置）

```jinja2
{%- if is_scenario_whitelist_access -%}
    {%- for item in set_ngvnuemutacc_list_2 -%}
        SET NGVNUEMUTACC:
        {#- --- 必选参数 --- -#}
        VNINSTANCE="{{item.VNINSTANCE}}",
        {#- --- 可选参数 --- -#}
        {%- if item.N9AUE2UEUNIPOL is not none -%}
            N9AUE2UEUNIPOL={{item.N9AUE2UEUNIPOL}},
        {%- endif -%}
        {%- if item.N9AUE2UEMULPOL is not none -%}
            N9AUE2UEMULPOL={{item.N9AUE2UEMULPOL}},
        {%- endif -%}
        {%- if item.N9AUE2UEBROPOL is not none -%}
            N9AUE2UEBROPOL={{item.N9AUE2UEBROPOL}},
        {%- endif -%}
        {%- if item.N19UE2UESW is not none -%}
            N19UE2UESW={{item.N19UE2UESW}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.2 //此处以允许漫游5G LAN终端通过2个I-UPF的N9口与锚点UPF交互为例，实际请根据局点实际业务规划配置白名单。

```jinja2
{%- if is_scenario_whitelist_access -%}
    {%- for item in add_uemutaccwlist_list -%}
        ADD UEMUTACCWLIST:
        {#- --- 必选参数 --- -#}
        WLISTNAME="{{item.WLISTNAME}}",
        IPVERSION={{item.IPVERSION}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
        {%- if item.IPVERSION == 'IPV4' -%}
            IPV4START="{{item.IPV4START}}",
        {%- endif -%}
        {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
        {%- if item.IPVERSION == 'IPV4' -%}
            IPV4END="{{item.IPV4END}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_whitelist_access -%}
    {%- for item in add_ngbinduemutwl_list -%}
        ADD NGBINDUEMUTWL:
        {#- --- 必选参数 --- -#}
        VNINSTANCE="{{item.VNINSTANCE}}",
        WLISTNAME="{{item.WLISTNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

