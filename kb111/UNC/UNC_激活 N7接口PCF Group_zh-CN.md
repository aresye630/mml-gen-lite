---
id: ''
name: 激活 N7接口PCF Group
ne_type: UNC
type: feature
description: '* 新建PCF Group组网。 * 已有网络新改造成PCF Group组网。  适用于SMF。'
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","可靠性功能","WSFD-213002 NF业务可靠性保障","激活 N7接口PCF Group"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
* 新建PCF Group组网。* 已有网络新改造成PCF Group组网。适用于SMF。

## 必备事项
前提条件

前提条件

* 请仔细阅读WSFD-213002 NF业务可靠性保障特性概述。
* 完成加载License。
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
    set_pccfunc_list:
      type: items
      properties:
        PCFLBPARA:
          name: 'PCF负荷分担参数'
          type: string
          enum:
          - GROUPID
          - PRIORITY
          required: false
          description: '配置SMF选择PCF的负荷分担参数。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
    add_pnfgroupid_list:
      type: items
      properties:
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: '本地配置对端NF实例的群组信息。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        GROUPID:
          name: '群组标识'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_nfdiscplcy_list:
      type: items
      properties:
        POLICY:
          name: '服务发现策略'
          type: string
          enum:
          - LOCAL_FIRST
          - LOCAL_ONLY
          - REMOTE_ONLY
          - REMOTE_FIRST
          required: false
          description: '指定服务发现策略。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_pccfailaction_list:
      type: items
      properties:
        UPDATEFAILACT:
          name: 'Update流程故障处理动作'
          type: string
          enum:
          - CONTINUE
          - ROLLBACK
          - TERMINATE
          required: false
          description: '设置PCC故障处理动作。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        UPDFAILLOCPCC:
          name: 'Update流程故障回滚为Local PCC用户类型'
          type: string
          enum:
          - INHERIT_PCC
          - LOCAL_PCC
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV2NFSRA01'
      SWITCH: ENABLE
    set_pccfunc_list:
    - PCFLBPARA: GROUPID
    add_pnfgroupid_list:
    - NFINSTANCEID: 'PCF_Instance_0'
      GROUPID: 'GROUP01'
    set_nfdiscplcy_list:
    - POLICY: LOCAL_FIRST
    set_pccfailaction_list:
    - UPDATEFAILACT: ROLLBACK
      UPDFAILLOCPCC: LOCAL_PCC
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

### 3 配置SMF选择PCF的负荷分担参数。

```jinja2
{%- for item in set_pccfunc_list -%}
    SET PCCFUNC:
    {#- --- 可选参数 --- -#}
    {%- if item.PCFLBPARA is not none -%}
        PCFLBPARA={{item.PCFLBPARA}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 增加本地配置的对端NF实例的群组信息。

```jinja2
{%- for item in add_pnfgroupid_list -%}
    ADD PNFGROUPID:
    {#- --- 必选参数 --- -#}
    NFINSTANCEID="{{item.NFINSTANCEID}}",
    GROUPID="{{item.GROUPID}}",
    ;
{%- endfor -%}
```

### 5 指定服务发现策略。

```jinja2
{%- for item in set_nfdiscplcy_list -%}
    SET NFDISCPLCY:
    {#- --- 可选参数 --- -#}
    {%- if item.POLICY is not none -%}
        POLICY={{item.POLICY}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 6 设置PCC故障处理动作。

```jinja2
{%- for item in set_pccfailaction_list -%}
    SET PCCFAILACTION:
    {#- --- 可选参数 --- -#}
    {%- if item.UPDATEFAILACT is not none -%}
        UPDATEFAILACT={{item.UPDATEFAILACT}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：UPDATEFAILACT=ROLLBACK 时可选 --- -#}
    {%- if item.UPDATEFAILACT == 'ROLLBACK' -%}
        {%- if item.UPDFAILLOCPCC is not none -%}
            UPDFAILLOCPCC={{item.UPDFAILLOCPCC}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

