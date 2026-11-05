---
id: ''
name: 去激活QoS复杂流分类功能（VNRS_VNFC）
ne_type: UEG
type: feature
description: 本操作指导介绍如何在运行网络中去激活QoS复杂流分类功能特性。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝S","MEC 特性指南（风筝S）","UEG特性指南","IP基本特性","IPFD-020400 IP可靠性","IPFD-020401 QoS","特性配置","复杂流分类配置（VNRS_VNFC）","去激活QoS复杂流分类功能（VNRS_VNFC）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍如何在运行网络中去激活QoS复杂流分类功能特性。

## 必备事项
前提条件

* 操作人员已经登录网络管理系统NMS（Network Management System）。
* QoS复杂流分类功能已经激活。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    rmv_qosapplication_list:
      type: items
      properties:
        IFNAME:
          name: '接口名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DIRECTION:
          name: '报文方向'
          type: string
          enum:
          - inbound
          - outbound
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    rmv_mqcpolicynode_list:
      type: items
      properties:
        POLICYNAME:
          name: '策略名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CLASSIFIERNAME:
          name: '分类名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BEHAVIORNAME:
          name: '行为名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    rmv_mqcpolicy_list:
      type: items
      properties:
        POLICYNAME:
          name: '策略名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    rmv_mqcclassifier_list:
      type: items
      properties:
        CLASSIFIERNAME:
          name: '分类名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    rmv_qosactrdrnhp_list:
      type: items
      properties:
        BEHAVIORNAME:
          name: '流行为名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    rmv_sqosremark_list:
      type: items
      properties:
        BEHAVIORNAME:
          name: '流行为名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    rmv_qosactrdrpolicy_list:
      type: items
      properties:
        BEHAVIORNAME:
          name: '行为名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    rmv_sqosrdrvpngroup_list:
      type: items
      properties:
        BEHAVIORNAME:
          name: '行为名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    rmv_sqosurpf_list:
      type: items
      properties:
        BEHAVIORNAME:
          name: '流行为名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    rmv_sqoscar_list:
      type: items
      properties:
        BEHAVIORNAME:
          name: '流行为名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    rmv_mqcbehavior_list:
      type: items
      properties:
        BEHAVIORNAME:
          name: '行为名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    rtr_sqospolicystc_list:
      type: items
      properties:
        IFNAME:
          name: '接口名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DIRECTION:
          name: '方向'
          type: string
          enum:
          - inbound
          - outbound
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    rmv_qosapplication_list:
    - IFNAME: '接口名称'
      DIRECTION: 报文方向
    rmv_mqcpolicynode_list:
    - POLICYNAME: '策略名称'
      CLASSIFIERNAME: '分类名称'
      BEHAVIORNAME: '行为名称'
    rmv_mqcpolicy_list:
    - POLICYNAME: '策略名称'
    rmv_mqcclassifier_list:
    - CLASSIFIERNAME: '分类名称'
    rmv_qosactrdrnhp_list:
    - BEHAVIORNAME: '行为名称'
    rmv_sqosremark_list:
    - BEHAVIORNAME: '流行为名称'
    rmv_qosactrdrpolicy_list:
    - BEHAVIORNAME: '行为名称'
    rmv_sqosrdrvpngroup_list:
    - BEHAVIORNAME: '行为名称'
    rmv_sqosurpf_list:
    - BEHAVIORNAME: '流行为名称'
    rmv_sqoscar_list:
    - BEHAVIORNAME: '流行为名称'
    rmv_mqcbehavior_list:
    - BEHAVIORNAME: '行为名称'
    rtr_sqospolicystc_list:
    - IFNAME: '接口名称'
      DIRECTION: 方向
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 删除接口出方向绑定流策略。

### 在“MML命令行-UEG”窗口上执行：

```jinja2
{%- for item in rmv_qosapplication_list -%}
    RMV QOSAPPLICATION:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    DIRECTION={{item.DIRECTION}},
    ;
{%- endfor -%}
```

### 2 删除绑定的流分类和流行为。

### 在“MML命令行-UEG”窗口上执行：

```jinja2
{%- for item in rmv_mqcpolicynode_list -%}
    RMV MQCPOLICYNODE:
    {#- --- 必选参数 --- -#}
    POLICYNAME="{{item.POLICYNAME}}",
    CLASSIFIERNAME="{{item.CLASSIFIERNAME}}",
    BEHAVIORNAME="{{item.BEHAVIORNAME}}",
    ;
{%- endfor -%}
```

### 3 删除流策略。

### 在“MML命令行-UEG”窗口上执行：

```jinja2
{%- for item in rmv_mqcpolicy_list -%}
    RMV MQCPOLICY:
    {#- --- 必选参数 --- -#}
    POLICYNAME="{{item.POLICYNAME}}",
    ;
{%- endfor -%}
```

### 4 当需要删除流分类绑定ACL规则。

### 5 删除流分类。

### 在“MML命令行-UEG”窗口上执行：

```jinja2
{%- for item in rmv_mqcclassifier_list -%}
    RMV MQCCLASSIFIER:
    {#- --- 必选参数 --- -#}
    CLASSIFIERNAME="{{item.CLASSIFIERNAME}}",
    ;
{%- endfor -%}
```

### 6 **可选：**当需要删除流动作。

#### 6.1 当需要删除重定向下一跳动作：

#### 在“MML命令行-UEG”窗口上执行：

```jinja2
{%- if is_optional_delete_flow_action -%}
    {%- for item in rmv_qosactrdrnhp_list -%}
        RMV QOSACTRDRNHP:
        {#- --- 必选参数 --- -#}
        BEHAVIORNAME="{{item.BEHAVIORNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 6.2 当需要删除重标记：

#### 在“MML命令行-UEG”窗口上执行：

```jinja2
{%- if is_optional_delete_flow_action -%}
    {%- for item in rmv_sqosremark_list -%}
        RMV SQOSREMARK:
        {#- --- 必选参数 --- -#}
        BEHAVIORNAME="{{item.BEHAVIORNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 6.3 当需要删除级联流策略：

#### 在“MML命令行-UEG”窗口上执行：

```jinja2
{%- if is_optional_delete_flow_action -%}
    {%- for item in rmv_qosactrdrpolicy_list -%}
        RMV QOSACTRDRPOLICY:
        {#- --- 必选参数 --- -#}
        BEHAVIORNAME="{{item.BEHAVIORNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 6.4 当需要删除重定向VPN组：

#### 在“MML命令行-UEG”窗口上执行：

```jinja2
{%- if is_optional_delete_flow_action -%}
    {%- for item in rmv_sqosrdrvpngroup_list -%}
        RMV SQOSRDRVPNGROUP:
        {#- --- 必选参数 --- -#}
        BEHAVIORNAME="{{item.BEHAVIORNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 6.5 当需要删除安全URPF：

#### 在“MML命令行-UEG”窗口上执行：

```jinja2
{%- if is_optional_delete_flow_action -%}
    {%- for item in rmv_sqosurpf_list -%}
        RMV SQOSURPF:
        {#- --- 必选参数 --- -#}
        BEHAVIORNAME="{{item.BEHAVIORNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 6.6 当需要删除CAR配置：

#### 在“MML命令行-UEG”窗口上执行：

```jinja2
{%- if is_optional_delete_flow_action -%}
    {%- for item in rmv_sqoscar_list -%}
        RMV SQOSCAR:
        {#- --- 必选参数 --- -#}
        BEHAVIORNAME="{{item.BEHAVIORNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

### 7 删除流行为。

### 在“MML命令行-UEG”窗口上执行：

```jinja2
{%- for item in rmv_mqcbehavior_list -%}
    RMV MQCBEHAVIOR:
    {#- --- 必选参数 --- -#}
    BEHAVIORNAME="{{item.BEHAVIORNAME}}",
    ;
{%- endfor -%}
```

### 8 **可选：**清除端口流量策略报文统计。

### 在“MML命令行-UEG”窗口上执行：

```jinja2
{%- if is_optional_clear_port_policy_statistics -%}
    {%- for item in rtr_sqospolicystc_list -%}
        RTR SQOSPOLICYSTC:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        DIRECTION={{item.DIRECTION}},
        ;
    {%- endfor -%}
{%- endif -%}
```

