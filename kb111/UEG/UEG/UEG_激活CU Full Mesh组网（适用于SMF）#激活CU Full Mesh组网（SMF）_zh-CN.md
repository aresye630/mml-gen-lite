---
id: GWFD-021701
name: 激活CU Full Mesh组网（SMF）
ne_type: UEG
type: feature
description: '* 新建CU FullMesh组网。 * 已有网络新改造成CU FullMesh组网。'
tags: []
risk_level: ''
doc_source: ["业务配置","风筝S","MEC 特性指南（风筝S）","UEG特性指南","分布式网络功能","GWFD-021701 CU Full Mesh组网","SMF&UPF容灾方案","新建部署","激活CU Full Mesh组网（适用于SMF）","激活CU Full Mesh组网（SMF）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
* 新建CU FullMesh组网。* 已有网络新改造成CU FullMesh组网。

## 必备事项
前提条件

* 请仔细阅读SMF&UPF容灾方案。
* 完成加载License。
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
    set_addressattr_list:
      type: items
      properties:
        ALLOCPRECEDENCE:
          name: 'AllocPrecedence'
          type: string
          required: false
          description: '设置UE地址分配方式。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_upipdomain_list:
      type: items
      properties:
        UPNODE:
          name: 'UpNode'
          type: string
          minLength: 1
          maxLength: 36
          required: true
          description: '设置UP Node和地址池绑定关系。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPDOMAIN:
          name: 'IpDomain'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        DNNSWITCH:
          name: 'DnnSwitch'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        DNN:
          name: '数据网络名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_smffunc_list:
      type: items
      properties:
        FAULTUPRESEL:
          name: '故障原因值重选UPF功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '配置是否基于故障原因值重选UPF。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_reselectupcause_list:
      type: items
      properties:
        FAULTCAUSE:
          name: '故障原因值'
          type: integer
          minimum: 1
          maximum: 255
          required: true
          description: '配置UPF重选的故障原因值。'
          data_source: '全网规划'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV2CUFMN01'
      SWITCH: ENABLE
    set_addressattr_list:
    - ALLOCPRECEDENCE: UPF_FIRST
    add_upipdomain_list:
    - UPNODE: 'IPv4+192.168.0.20'
      IPDOMAIN: 'Ipdomain-a'
      DNNSWITCH: DISABLE
      DNN: 'data'
    set_smffunc_list:
    - FAULTUPRESEL: ENABLE
    add_reselectupcause_list:
    - FAULTCAUSE: 75
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 打开本特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 2 配置地址分配方式。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_addressattr_list的变量区（command: SET ADDRESSATTR） -#}
<!-- MISSING_MACRO: command=SET ADDRESSATTR list_name=set_addressattr_list step_id=2 -->
```

### 3 **可选：**配置UPF/PGW-U和地址池的绑定关系。

```jinja2
{%- if is_optional_upf_pgwu_address_pool_binding -%}
    {%- for item in add_upipdomain_list -%}
        ADD UPIPDOMAIN:
        {#- --- 必选参数 --- -#}
        UPNODE="{{item.UPNODE}}",
        IPDOMAIN="{{item.IPDOMAIN}}",
        DNNSWITCH={{item.DNNSWITCH}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：DNNSWITCH=ENABLE 时必选 --- -#}
        {%- if item.DNNSWITCH == 'ENABLE' -%}
            DNN="{{item.DNN}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 在U面分配地址的场景下，如果不同UPF/PGW-U上配置的地址池存在地址重叠，为避免SMF带给PCF的用户地址冲突，导致用户会话创建失败，需要将不同UPF/PGW-U绑到不同的IP Domain。

### 4 配置是否基于故障原因值重选UPF。

```jinja2
{%- for item in set_smffunc_list -%}
    SET SMFFUNC:
    {#- --- 可选参数 --- -#}
    {%- if item.FAULTUPRESEL is not none -%}
        FAULTUPRESEL={{item.FAULTUPRESEL}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 该功能不适用于U面分配用户地址时的AAA鉴权场景。

### 5 配置UPF重选的故障原因值。

```jinja2
{%- for item in add_reselectupcause_list -%}
    ADD RESELECTUPCAUSE:
    {#- --- 必选参数 --- -#}
    FAULTCAUSE={{item.FAULTCAUSE}},
    ;
{%- endfor -%}
```

