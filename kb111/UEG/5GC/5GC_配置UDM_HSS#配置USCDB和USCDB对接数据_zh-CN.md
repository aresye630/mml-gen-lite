---
id: ''
name: 配置USCDB和USCDB对接数据
ne_type: UEG
type: feature
description: 风筝L双DC部署，为了提升可靠性，需要USCDB之间实现实时数据同步。因此，开局时，配置DC间的USCDB与USCDB的对接数据。
tags: []
risk_level: ''
doc_source: ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（火电专网，入驻式）","部署配置指导","中心园区部署入驻式UEG-L","初始配置与调测","参考：详细配置指导","配置UDM/HSS","配置USCDB和USCDB对接数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
风筝L双DC部署，为了提升可靠性，需要USCDB之间实现实时数据同步。因此，开局时，配置DC间的USCDB与USCDB的对接数据。

## 必备事项
前提条件

* 已完成配置USCDB基础数据。
* 已完成配置UDM基础数据。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_rlocation_list:
      type: items
      properties:
        RLOCID:
          name: '远端Location标识'
          type: integer
          minimum: 1
          maximum: 512
          required: true
          description: '表示远端Location标识，在远端“MML-USCDB”下使用LST LOCATION命令查询。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        RMT:
          name: '远端网元类型'
          type: string
          maxLength: 128
          required: true
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        LP:
          name: '位置ID优先级值'
          type: integer
          minimum: 1
          maximum: 512
          required: true
          description: '优先级值越小，对接的USCDB的优先级越高。  仅两个UEG间的BE和BE对接，该参数没有意义。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        REDUNFLAG:
          name: '是否容灾关系'
          type: string
          enum:
          - No
          - Yes
          required: true
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
    add_rdsg_list:
      type: items
      properties:
        RLOCID:
          name: '远端Location标识'
          type: integer
          minimum: 1
          maximum: 512
          required: true
          description: '该参数须在对接的远端USCDB网元中先定义，然后在本端网元通过ADD RLOCATION命令配置后，才能在此处索引。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        RDSGMID:
          name: '远端DSG模块号'
          type: integer
          minimum: 1
          maximum: 2047
          required: true
          description: '在远端“MML-USCDB”下使用“LST MODULE: MT=DSG;”查询。  “RDSGST”为“HSS9860”、“UPCF”、“UPCF-SESSION”时，“RDSGMID”值不能重复。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        RDSGST:
          name: '远端DSG业务类型'
          type: string
          maxLength: 128
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        RDSGTYPE:
          name: '远端DSG类型'
          type: string
          enum:
          - DSG
          - DBS
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: DSG
    add_ripaddr_list:
      type: items
      properties:
        RLOCID:
          name: '远端Location标识'
          type: integer
          minimum: 1
          maximum: 512
          required: true
          description: '该参数须在对接的远端USCDB网元中先定义，然后在本端网元通过ADD RLOCATION命令配置后，才能在此处索引。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        ID:
          name: '远端DPU模块号/远端IP的VPN索引'
          type: integer
          minimum: 1
          maximum: 4080
          required: true
          description: '该参数须在对接的远端USCDB网元由ADD SRVIPADDR先定义。'
          data_source: '已规划数据中获取'
          pattern: ''
          default: ''
        IPVER:
          name: 'IP类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: '本页面以IPv4地址为例。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4IP1:
          name: '远端Location IPV4地址1'
          type: string
          maxLength: 15
          required: false
          description: '这个地址必须在对接的远端USCDB网元中已经配置完毕。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4IP2:
          name: '远端Location IPV4地址2'
          type: string
          maxLength: 15
          required: false
          description: '这个地址必须在对接的远端USCDB网元中已经配置完毕。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        RDPUST:
          name: '远端IP地址业务类型'
          type: string
          maxLength: 128
          required: true
          description: '通过LOD FEPLUG命令加载UDM/UPCF插件后在此引用。'
          data_source: '固定取值'
          pattern: ''
          default: ''
    act_ipdisp_list:
      type: items
      properties: {}
  examples:
    add_rlocation_list:
    - RLOCID: 16
      RMT: 'USCDB'
      LP: 10
      REDUNFLAG: Yes
    - RLOCID: 14
      RMT: 'USCDB'
      LP: 5
      REDUNFLAG: Yes
    add_rdsg_list:
    - RLOCID: 16
      RDSGMID: 17
      RDSGST: 'HSS9860'
      RDSGTYPE: DSG
    - RLOCID: 14
      RDSGMID: 17
      RDSGST: 'HSS9860'
      RDSGTYPE: DSG
    add_ripaddr_list:
    - RLOCID: 16
      ID: 1
      IPVER: IPV4
      IPV4IP1: '10.201.200.32'
      IPV4IP2: '10.201.200.33'
      RDPUST: 'HSS9860'
    - RLOCID: 14
      ID: 1
      IPVER: IPV4
      IPV4IP1: '10.200.200.32'
      IPV4IP2: '10.200.200.33'
      RDPUST: 'HSS9860'
    act_ipdisp_list:
    - {}
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 登录“USCDB MML命令”界面。

### 2 增加远端Location信息。

#### 2.1 //DC1：

```jinja2
{%- for item in add_rlocation_list -%}
    ADD RLOCATION:
    {#- --- 必选参数 --- -#}
    RLOCID={{item.RLOCID}},
    RMT="{{item.RMT}}",
    LP={{item.LP}},
    REDUNFLAG={{item.REDUNFLAG}},
    ;
{%- endfor -%}
```

### 3 增加远端DSG。

### 参数“RDSGMID”通过在“MML-USCDB”下使用“LST MODULE: MT=DSG;”查询。

#### 3.1 //DC1：

```jinja2
{%- for item in add_rdsg_list -%}
    ADD RDSG:
    {#- --- 必选参数 --- -#}
    RLOCID={{item.RLOCID}},
    RDSGMID={{item.RDSGMID}},
    RDSGST="{{item.RDSGST}}",
    {#- --- 可选参数 --- -#}
    {%- if item.RDSGTYPE is not none -%}
        RDSGTYPE={{item.RDSGTYPE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 增加远端网元IP地址。

#### 4.1 //DC1：

```jinja2
{%- for item in add_ripaddr_list -%}
    ADD RIPADDR:
    {#- --- 必选参数 --- -#}
    RLOCID={{item.RLOCID}},
    ID={{item.ID}},
    IPVER={{item.IPVER}},
    RDPUST="{{item.RDPUST}}",
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVER=IPV4 时必选 --- -#}
    {%- if item.IPVER == 'IPV4' -%}
        IPV4IP1="{{item.IPV4IP1}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPVER=IPV4 时可选 --- -#}
    {%- if item.IPVER == 'IPV4' -%}
        {%- if item.IPV4IP2 is not none -%}
            IPV4IP2="{{item.IPV4IP2}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 登录“USCDB MML命令”界面。执行如下命令，激活IP链路。

```jinja2
ACT IPDISP:
;
```

