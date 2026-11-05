---
id: ''
name: 激活DECOR功能
ne_type: UEG
type: feature
description: 本操作指导介绍在运行网络中激活DECOR基础功能的操作过程。  当TOB和TOC用户共用基站时，运营商可以通过DECOR特性将TOC用户重定向至大网核心网，TOB用户接入到园区核心网进行服务。  适用于MME
tags: []
risk_level: ''
doc_source: ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（电力专网，入驻式）","配置基础业务","DECOR功能配置（可选）","激活DECOR功能"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活DECOR基础功能的操作过程。当TOB和TOC用户共用基站时，运营商可以通过DECOR特性将TOC用户重定向至大网核心网，TOB用户接入到园区核心网进行服务。适用于MME

## 必备事项
前提条件

* 请仔细阅读DECOR功能。
* eNodeB的配置已经具备，具体请参见该特性页面的应用场景部分描述。
* 已经加载支持该特性的License，对应的License项为“81202740 LKV2DECOR00 DECOR基础功能”和“82207914 LKV2DECOR01 DECOR”。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_dcn_list:
      type: items
      properties:
        DCNID:
          name: 'DCN ID'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        MCC:
          name: '移动国家代码'
          type: string
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MNC:
          name: '移动网号'
          type: string
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DCNTYPE:
          name: 'DCN类型'
          type: string
          enum:
          - COMMON
          - DEFAULT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: COMMON
        DESC:
          name: '描述'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
    add_dcnmember_list:
      type: items
      properties:
        DCNID:
          name: 'DCN ID'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        MMEGI:
          name: 'MME组识别码'
          type: string
          maxLength: 4
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_dcnmap_list:
      type: items
      properties:
        DCNID:
          name: 'DCN ID'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        BGNUEUSAGETYPE:
          name: '起始UE USAGE TYPE'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENDUEUSAGETYPE:
          name: '终止UE USAGE TYPE'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_dcnctrl_list:
      type: items
      properties:
        RESELECTPLCY:
          name: '重选策略'
          type: string
          enum:
          - DELAY
          - IMMEDIATE
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        CONTAINUEUSGTYPE:
          name: '携带UE Usage Type'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UEUSGTYPECONPLCY:
          name: 'UE USAGE TYPE携带策略'
          type: string
          enum:
          - SUBSCRIBE
          - USED
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NONTAI:
          name: '非广播TAI'
          type: string
          maxLength: 10
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MMEGIQUERYPLCY:
          name: 'MMEGI查询策略'
          type: string
          enum:
          - DNS
          - LOCAL
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DNSROLLBACK:
          name: '域名回退查询'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BACKOFFSW:
          name: 'Backoff Timer分配开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_dcnplcy_list:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - IMSI_PRE
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        DCNSW:
          name: 'DCN开关'
          type: string
          enum:
          - OFF
          - ON
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRUEUSAGETYPE:
          name: '源侧UE USAGE TYPE策略'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
        UEUSAGETYPEPLCY:
          name: 'UE USAGE TYPE获取策略'
          type: string
          enum:
          - HSS
          - LOCAL
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: HSS
        UEUSAGETYPE:
          name: 'UE USAGE TYPE'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GWSELPLCY:
          name: '网关选择策略'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NO
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
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
  examples:
    add_dcn_list:
    - DCNID: 1
      MCC: '123'
      MNC: '03'
      DCNTYPE: COMMON
      DESC: 'eMTC'
    add_dcnmember_list:
    - DCNID: 0
      MMEGI: '0001'
    add_dcnmap_list:
    - DCNID: 0
      BGNUEUSAGETYPE: 0
      ENDUEUSAGETYPE: 10
    set_dcnctrl_list:
    - RESELECTPLCY: IMMEDIATE
      CONTAINUEUSGTYPE: NO
      UEUSGTYPECONPLCY: USED
      NONTAI: '0000000000'
      MMEGIQUERYPLCY: LOCAL
      DNSROLLBACK: MME-0&PGW-0&SGW-0
      BACKOFFSW: OFF
    add_dcnplcy_list:
    - SUBRANGE: ALL_USER
      DCNSW: ON
      SRUEUSAGETYPE: YES
      UEUSAGETYPEPLCY: LOCAL
      UEUSAGETYPE: 10
      GWSELPLCY: NO
      IMSIPRE: '12300630'
    set_licenseswitch_list:
    - LICITEM: 'LKV2DECOR00'
      SWITCH: ENABLE
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 通过本地配置方式按MME粒度规划DCN。

### 运营商可以在本地配置DCN服务的MMEGI的列表。

#### 2.1 为PLMN增加DCN标识

#### ****ADD DCN****

#### 建议为PLMN配置一个默认DCN，从而使接入不到普通DCN的用户接入默认DCN完成业务流程。

#### 如果组网上是多PLMN共享MME，则在MME上为每个PLMN配置部署的DCN。例如12303在MME上部署DCN1，12301在MME上部署DCN2，则需要执行如下命令：

#### //增加DCN。

```jinja2
{%- for item in add_dcn_list -%}
    ADD DCN:
    {#- --- 必选参数 --- -#}
    DCNID={{item.DCNID}},
    MCC="{{item.MCC}}",
    MNC="{{item.MNC}}",
    {#- --- 可选参数 --- -#}
    {%- if item.DCNTYPE is not none -%}
        DCNTYPE={{item.DCNTYPE}},
    {%- endif -%}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.2 为DCN添加成员列表。

#### 按DCN的网络规划范围，为DCN添加MMEGI成员。如果DCN包含多个MME POOL，则多次执行此步骤。

#### ****ADD DCNMEMBER****

#### //为DCN增加MME群组成员记录。

```jinja2
{%- for item in add_dcnmember_list -%}
    ADD DCNMEMBER:
    {#- --- 必选参数 --- -#}
    DCNID={{item.DCNID}},
    MMEGI="{{item.MMEGI}}",
    ;
{%- endfor -%}
```

#### 2.3 配置DCN与UE Usage Type的映射关系。

#### ****ADD DCNMAP****

#### //配置DCN与UE Usage Type的映射关系。

```jinja2
{%- for item in add_dcnmap_list -%}
    ADD DCNMAP:
    {#- --- 必选参数 --- -#}
    DCNID={{item.DCNID}},
    BGNUEUSAGETYPE={{item.BGNUEUSAGETYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.ENDUEUSAGETYPE is not none -%}
        ENDUEUSAGETYPE={{item.ENDUEUSAGETYPE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.4 配置MMEGI查询策略以及相关控制参数。

#### 通过此步骤设置用本地配置查询MMEGI。

#### ****SET DCNCTRL****

#### //配置DCN控制参数。

```jinja2
{%- for item in set_dcnctrl_list -%}
    SET DCNCTRL:
    {#- --- 可选参数 --- -#}
    {%- if item.RESELECTPLCY is not none -%}
        RESELECTPLCY={{item.RESELECTPLCY}},
    {%- endif -%}
    {%- if item.CONTAINUEUSGTYPE is not none -%}
        CONTAINUEUSGTYPE={{item.CONTAINUEUSGTYPE}},
    {%- endif -%}
    {%- if item.NONTAI is not none -%}
        NONTAI="{{item.NONTAI}}",
    {%- endif -%}
    {%- if item.MMEGIQUERYPLCY is not none -%}
        MMEGIQUERYPLCY={{item.MMEGIQUERYPLCY}},
    {%- endif -%}
    {%- if item.DNSROLLBACK is not none -%}
        DNSROLLBACK={{item.DNSROLLBACK}},
    {%- endif -%}
    {%- if item.BACKOFFSW is not none -%}
        BACKOFFSW={{item.BACKOFFSW}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：CONTAINUEUSGTYPE=YES 时可选 --- -#}
    {%- if item.CONTAINUEUSGTYPE == 'YES' -%}
        {%- if item.UEUSGTYPECONPLCY is not none -%}
            UEUSGTYPECONPLCY={{item.UEUSGTYPECONPLCY}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 打开DCN开关并配置DCN业务相关参数。

### //配置DCN业务相关参数，配置园区基于号段全关闭。

```jinja2
{%- for item in add_dcnplcy_list -%}
    ADD DCNPLCY:
    {#- --- 必选参数 --- -#}
    SUBRANGE={{item.SUBRANGE}},
    DCNSW={{item.DCNSW}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：UEUSAGETYPEPLCY=LOCAL 时必选 --- -#}
    {%- if item.UEUSAGETYPEPLCY == 'LOCAL' -%}
        UEUSAGETYPE={{item.UEUSAGETYPE}},
    {%- endif -%}
    {#- --- 条件必选：SUBRANGE=IMSI_PRE 时必选 --- -#}
    {%- if item.SUBRANGE == 'IMSI_PRE' -%}
        IMSIPRE="{{item.IMSIPRE}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：DCNSW=ON 时可选 --- -#}
    {%- if item.DCNSW == 'ON' -%}
        {%- if item.SRUEUSAGETYPE is not none -%}
            SRUEUSAGETYPE={{item.SRUEUSAGETYPE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：DCNSW=ON 时可选 --- -#}
    {%- if item.DCNSW == 'ON' -%}
        {%- if item.UEUSAGETYPEPLCY is not none -%}
            UEUSAGETYPEPLCY={{item.UEUSAGETYPEPLCY}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：DCNSW=ON 时可选 --- -#}
    {%- if item.DCNSW == 'ON' -%}
        {%- if item.GWSELPLCY is not none -%}
            GWSELPLCY={{item.GWSELPLCY}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### //打开本功能的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

