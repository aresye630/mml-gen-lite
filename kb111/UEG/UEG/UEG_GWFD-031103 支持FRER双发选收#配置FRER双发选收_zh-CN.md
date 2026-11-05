---
id: GWFD-031103
name: 配置FRER双发选收
ne_type: UEG
type: feature
description: 工业应用中，存在高可靠性要求的行业应用时需要部署。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝S","MEC 特性指南（风筝S）","UEG特性指南","5G LAN基本功能","可选功能","GWFD-031103 支持FRER双发选收","配置FRER双发选收"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
工业应用中，存在高可靠性要求的行业应用时需要部署。

## 必备事项
前提条件

* 已完成配置5G LAN基本功能。
* 完成**加载License**（如果有需求，请联系华为技术支持工程师处理）。
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
    set_ngdfsrfunc_list:
      type: items
      properties:
        VNINSTANCE:
          name: '5G LAN组名称'
          type: string
          minLength: 0
          maxLength: 37
          required: true
          description: '5G LAN组标识，不同5G LAN组的VNINSTANCE取值不能重复。  对于同一个5G LAN组，UDM、SMF和UPF上配置的5G LAN组标识必须一致。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DFSRSWITCH:
          name: '双发选收功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: '默认值为DISABLE。  基于5G LAN组粒度配置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_dfsrattr_list:
      type: items
      properties:
        NEPRIFLAG:
          name: '网元主备标识'
          type: string
          enum:
          - PRIMARY
          - SECONDARY
          required: false
          description: '主备冷备部署时需要配置该参数。此处的主用UPF，是SMF选择的高优先级UPF；备用UPF，是SMF选择的低优先级UPF。   * 主用UPF上需要设置为“PRIMARY”。 * 备用UPF上需要设置为“SECONDARY”。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PAIRUEACTTIME:
          name: '双发选收结对内用户激活时长'
          type: integer
          minimum: 3
          maximum: 300
          required: false
          description: '指定备用UPF上双发选收结对内两个成员（如CPE）激活的最大时间间隔（单位是秒），当激活间隔超过配置的时长时，备用UPF会主动去活先激活的成员。  该参数在“NEPRIFLAG”配置为“SECONDARY”时需要配置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_dfsrpair_list:
      type: items
      properties:
        DFSRPAIRID:
          name: '双发选收结对ID'
          type: integer
          minimum: 1
          maximum: 2048
          required: true
          description: '同一UPF内不能重复。  取值范围1~2048。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DFSRPAIRMODE:
          name: '双发选收模式'
          type: string
          enum:
          - FRER_SRC_MAC
          - FRER_PAIR
          required: true
          description: '* FRER\_SRC\_MAC：基于源MAC的FRER双发选收模式。 * FRER\_PAIR：基于结对的FRER双发选收模式。   与工业冗余协议交换机上配置的双发选收模式一致，此处以“FRER\_PAIR”为例。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PAIRDESCRIPTION:
          name: '结对描述信息'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: '用于方便了解结对信息。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_dfsrpairmem_list:
      type: items
      properties:
        DFSRPAIRID:
          name: '双发选收结对ID'
          type: integer
          minimum: 1
          maximum: 2048
          required: true
          description: '采用**ADD DFSRPAIR**命令定义的DFSRPAIRID。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IMSI:
          name: 'IMSI'
          type: string
          minLength: 0
          maxLength: 16
          required: true
          description: '单个结对最大配置两个IMSI。'
          data_source: '从对端获取'
          pattern: ''
          default: ''
    add_ngbinddfsrpair_list:
      type: items
      properties:
        VNINSTANCE:
          name: '5G LAN实例名称'
          type: string
          minLength: 0
          maxLength: 37
          required: true
          description: '采用**ADD NGVNINSTANCE**命令定义的VNINSTANCE。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DFSRPAIRID:
          name: '双发选收结对ID'
          type: integer
          minimum: 1
          maximum: 2048
          required: true
          description: '采用**ADD DFSRPAIR**命令定义的DFSRPAIRID。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3G5LADFSR'
      SWITCH: ENABLE
    - LICITEM: 'LKV3G5LADFSR'
      SWITCH: ENABLE
    set_ngdfsrfunc_list:
    - VNINSTANCE: '000003e9-460-08-01'
      DFSRSWITCH: ENABLE
    - VNINSTANCE: '000003e9-460-08-01'
      DFSRSWITCH: ENABLE
    set_dfsrattr_list:
    - NEPRIFLAG: PRIMARY
      PAIRUEACTTIME: 30
    add_dfsrpair_list:
    - DFSRPAIRID: 10
      DFSRPAIRMODE: FRER_PAIR
      PAIRDESCRIPTION: 'pair'
    add_dfsrpairmem_list:
    - DFSRPAIRID: 10
      IMSI: '460123123456789'
    add_ngbinddfsrpair_list:
    - VNINSTANCE: '000003e9-460-08-01'
      DFSRPAIRID: 10
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 打开本特性的License配置开关。

#### 1.1 //在主用UPF上开启本特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 2 为指定5G LAN组开启双发选收开关。

#### 2.1 //在主用UPF上进行如下配置：

```jinja2
{%- for item in set_ngdfsrfunc_list -%}
    SET NGDFSRFUNC:
    {#- --- 必选参数 --- -#}
    VNINSTANCE="{{item.VNINSTANCE}}",
    DFSRSWITCH={{item.DFSRSWITCH}},
    ;
{%- endfor -%}
```

### 3 设置双发选收属性。

```jinja2
{%- for item in set_dfsrattr_list -%}
    SET DFSRATTR:
    {#- --- 可选参数 --- -#}
    {%- if item.NEPRIFLAG is not none -%}
        NEPRIFLAG={{item.NEPRIFLAG}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：NEPRIFLAG=SECONDARY 时必选 --- -#}
    {%- if item.NEPRIFLAG == 'SECONDARY' -%}
        PAIRUEACTTIME={{item.PAIRUEACTTIME}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 增加双发选收结对。

```jinja2
{%- for item in add_dfsrpair_list -%}
    ADD DFSRPAIR:
    {#- --- 必选参数 --- -#}
    DFSRPAIRID={{item.DFSRPAIRID}},
    DFSRPAIRMODE={{item.DFSRPAIRMODE}},
    {#- --- 可选参数 --- -#}
    {%- if item.PAIRDESCRIPTION is not none -%}
        PAIRDESCRIPTION="{{item.PAIRDESCRIPTION}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 添加双发选收结对成员。

```jinja2
{%- for item in add_dfsrpairmem_list -%}
    ADD DFSRPAIRMEM:
    {#- --- 必选参数 --- -#}
    DFSRPAIRID={{item.DFSRPAIRID}},
    IMSI="{{item.IMSI}}",
    ;
{%- endfor -%}
```

### 6 将双发选收结对绑定到5G LAN组。

```jinja2
{%- for item in add_ngbinddfsrpair_list -%}
    ADD NGBINDDFSRPAIR:
    {#- --- 必选参数 --- -#}
    VNINSTANCE="{{item.VNINSTANCE}}",
    DFSRPAIRID={{item.DFSRPAIRID}},
    ;
{%- endfor -%}
```

