---
id: GWFD-030700
name: 漫游场景5G LAN终端互访控制配置
ne_type: UEG
type: feature
description: '* 漫游场景，当运营商禁止终端通过锚点UPF的N9口互访但同一5G LAN组成员存在互访诉求时，可通过本功能允许漫游5G LAN终端与同一5G LAN组的其他终端之间的互访。 * 漫游组网，当运营商禁止终端通过锚点UPF的N9口互访且同一5G LAN组成员不存在互访诉求时，可通过本功能禁止漫游5G LAN终端与同一5G LAN组的其他终端之间的互访。  * 本功能中描述的漫游场景，是指5G LAN终端（主叫或被叫或主叫+被叫）通过I-UPF与锚点UPF交互的场景。 * 同一个层二5G LAN组成员之间默认不禁止互访，同一个层三5G LAN组成员之间默认不禁止互访。'
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","GW-U&UPF特性指南","GWFD-030700 5G LAN基本功能","可选功能","广域5G LAN业务","漫游场景5G LAN终端互访控制","漫游场景5G LAN终端互访控制配置"]
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

* 已完成配置5G LAN基本功能。
* 完成**加载License**（如果有需求，请联系华为技术支持工程师处理）。
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
          description: '该参数采用的是与锚点UPF互通的I-UPF的N9c逻辑接口IP地址。  如允许漫游5G LAN终端通过2个I-UPF与锚点UPF交互，则需要将这2个I-UPF的N9c逻辑接口IP地址均配置到白名单中。'
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
          description: '使用**ADD UEMUTACCWLIST**定义的白名单名称。  可通过**LST UEMUTACCWLIST**命令查询获取。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    set_softpara_list:
      type: items
      properties:
        DT:
          name: '软参记录数据类型'
          type: string
          enum:
          - BIT
          - BYTE
          - DWORD
          - STRING
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BITNUM:
          name: 'Bit索引'
          type: integer
          minimum: 1
          maximum: 3840
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BITVALUE:
          name: 'Bit值'
          type: integer
          minimum: 0
          maximum: 1
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_ngvnuemutacc_list:
    - VNINSTANCE: '000003e9-460-08-01'
      N9AUE2UEUNIPOL: FORBID_FWD
      N9AUE2UEMULPOL: FORBID_FWD
      N9AUE2UEBROPOL: FORBID_FWD
    add_uemutaccwlist_list:
    - WLISTNAME: 'I-UPF-01'
      IPVERSION: IPV4
      IPV4START: '192.168.111.1'
      IPV4END: '192.168.111.1'
    add_ngbinduemutwl_list:
    - VNINSTANCE: '000003e9-460-08-01'
      WLISTNAME: 'I-UPF-01'
    set_softpara_list:
    - DT: BIT
      BITNUM: 2682
      BITVALUE: 1
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 设置5G LAN终端漫游互访控制开关。

```jinja2
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
    ;
{%- endfor -%}
```

### 2 需要基于白名单进行精细化控制时，配置允许5G LAN终端漫游互访的白名单。

#### 2.1 配置白名单。

```jinja2
{%- if is_scenario_whitelist_control -%}
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

#### 2.2 配置白名单和5G LAN组绑定。

```jinja2
{%- if is_scenario_whitelist_control -%}
    {%- for item in add_ngbinduemutwl_list -%}
        ADD NGBINDUEMUTWL:
        {#- --- 必选参数 --- -#}
        VNINSTANCE="{{item.VNINSTANCE}}",
        WLISTNAME="{{item.WLISTNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

### 3 将BIT2682软参设置为1。否则，用户N2/Xn切换后下行业务不通。

```jinja2
{%- for item in set_softpara_list -%}
    SET SOFTPARA:
    {#- --- 必选参数 --- -#}
    DT={{item.DT}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：DT=BIT 时必选 --- -#}
    {%- if item.DT == 'BIT' -%}
        BITNUM={{item.BITNUM}},
    {%- endif -%}
    {#- --- 条件必选：DT=BIT 时必选 --- -#}
    {%- if item.DT == 'BIT' -%}
        BITVALUE={{item.BITVALUE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

