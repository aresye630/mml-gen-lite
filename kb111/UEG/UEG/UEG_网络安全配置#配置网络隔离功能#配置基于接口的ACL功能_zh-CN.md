---
id: ''
name: 配置基于接口的ACL功能
ne_type: UEG
type: feature
description: 为提高安全性，需要禁止非法地址或者网络对FENIX的访问。通过在接口上应用ACL策略，仅允许符合条件的报文通过（或拒绝符合条件的报文通过）。ACL可以与流分类功能配合使用，以实现数据包过滤等功能。
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝S”，入驻式）","裸机容器模式","配置安全数据（风筝S）","安全配置建议","可选配置","网络安全配置","配置网络隔离功能","配置基于接口的ACL功能"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
为提高安全性，需要禁止非法地址或者网络对FENIX的访问。通过在接口上应用ACL策略，仅允许符合条件的报文通过（或拒绝符合条件的报文通过）。ACL可以与流分类功能配合使用，以实现数据包过滤等功能。

## 必备事项
前提条件

该操作无需具备特殊条件。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_mqcbehavior_list:
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
    add_qosactrdrnhp_list:
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
        IPVERSION:
          name: 'IP协议版本'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: IPv4
        NEXTHOP:
          name: '下一跳地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_qosactfilter_list:
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
        FILTER:
          name: '行为状态'
          type: string
          enum:
          - deny
          - permit
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_qosactrdrpolicy_list:
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
        POLICYNAME:
          name: '策略名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_mqcclassifier_list:
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
    add_qosruleacl_list:
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
        IPVERSION:
          name: 'IP协议版本'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ACLTYPE:
          name: 'ACL类型'
          type: string
          enum:
          - acl-name
          - acl-number
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ACLNAME:
          name: 'ACL名称'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ACLNUM:
          name: 'ACL编号'
          type: integer
          minimum: 2000
          maximum: 4999
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_mqcpolicy_list:
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
    add_mqcpolicynode_list:
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
    add_qosapplication_list:
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
  examples:
    add_mqcbehavior_list:
    - BEHAVIORNAME: '行为名称'
    add_qosactrdrnhp_list:
    - BEHAVIORNAME: '流行为名称'
      IPVERSION: IPv4
      NEXTHOP: '下一跳地址'
    set_qosactfilter_list:
    - BEHAVIORNAME: '行为名称'
      FILTER: deny
    add_qosactrdrpolicy_list:
    - BEHAVIORNAME: '行为名称'
      POLICYNAME: '策略名称'
    add_mqcclassifier_list:
    - CLASSIFIERNAME: '分类名称'
    add_qosruleacl_list:
    - CLASSIFIERNAME: '分类名称'
      IPVERSION: IPv4
      ACLTYPE: ACL类型
      ACLNAME: 'ACL名称'
      ACLNUM: ACL编号
    add_mqcpolicy_list:
    - POLICYNAME: '策略名称'
    add_mqcpolicynode_list:
    - POLICYNAME: '策略名称'
      CLASSIFIERNAME: '分类名称'
      BEHAVIORNAME: '行为名称'
    add_qosapplication_list:
    - POLICYNAME: '策略名称'
      IFNAME: '接口名称'
      DIRECTION: 报文方向
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 配置ACL。详细步骤请参考激活支持ACL。

### 2 增加流行为。

### 在“MML命令行-UEG”窗口上执行：

```jinja2
{%- for item in add_mqcbehavior_list -%}
    ADD MQCBEHAVIOR:
    {#- --- 必选参数 --- -#}
    BEHAVIORNAME="{{item.BEHAVIORNAME}}",
    ;
{%- endfor -%}
```

### 3 增加对应的流动作。

### 在“MML命令行-UEG”窗口上执行：

### 配置重定向下一跳动作：

```jinja2
{%- for item in add_qosactrdrnhp_list -%}
    ADD QOSACTRDRNHP:
    {#- --- 必选参数 --- -#}
    BEHAVIORNAME="{{item.BEHAVIORNAME}}",
    IPVERSION={{item.IPVERSION}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPv4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv4' -%}
        NEXTHOP="{{item.NEXTHOP}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 配置Deny动作：

```jinja2
{%- for item in set_qosactfilter_list -%}
    SET QOSACTFILTER:
    {#- --- 必选参数 --- -#}
    BEHAVIORNAME="{{item.BEHAVIORNAME}}",
    FILTER={{item.FILTER}},
    ;
{%- endfor -%}
```

### 配置级联流策略动作：

```jinja2
{%- for item in add_qosactrdrpolicy_list -%}
    ADD QOSACTRDRPOLICY:
    {#- --- 必选参数 --- -#}
    BEHAVIORNAME="{{item.BEHAVIORNAME}}",
    POLICYNAME="{{item.POLICYNAME}}",
    ;
{%- endfor -%}
```

### 流动作permit可以和其他动作共存，其他都是互斥的。

### 4 增加流分类。

### 在“MML命令行-UEG”窗口上执行：

```jinja2
{%- for item in add_mqcclassifier_list -%}
    ADD MQCCLASSIFIER:
    {#- --- 必选参数 --- -#}
    CLASSIFIERNAME="{{item.CLASSIFIERNAME}}",
    ;
{%- endfor -%}
```

### 5 流分类绑定ACL规则。

### 在“MML命令行-UEG”窗口上执行：

#### 5.1 绑定基于名称和编号的ACL规则：

```jinja2
{%- for item in add_qosruleacl_list -%}
    ADD QOSRULEACL:
    {#- --- 必选参数 --- -#}
    CLASSIFIERNAME="{{item.CLASSIFIERNAME}}",
    IPVERSION={{item.IPVERSION}},
    ACLTYPE={{item.ACLTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：ACLTYPE=acl-name 时必选 --- -#}
    {%- if item.ACLTYPE == 'acl-name' -%}
        ACLNAME="{{item.ACLNAME}}",
    {%- endif -%}
    {#- --- 条件必选：ACLTYPE=acl-number 时必选 --- -#}
    {%- if item.ACLTYPE == 'acl-number' -%}
        ACLNUM={{item.ACLNUM}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 6 增加流策略，并绑定流行为和流分类。

### 在“MML命令行-UEG”窗口上执行：

#### 6.1 增加流策略：

```jinja2
{%- for item in add_mqcpolicy_list -%}
    ADD MQCPOLICY:
    {#- --- 必选参数 --- -#}
    POLICYNAME="{{item.POLICYNAME}}",
    ;
{%- endfor -%}
```

#### 6.2 绑定流分类和流行为：

```jinja2
{%- for item in add_mqcpolicynode_list -%}
    ADD MQCPOLICYNODE:
    {#- --- 必选参数 --- -#}
    POLICYNAME="{{item.POLICYNAME}}",
    CLASSIFIERNAME="{{item.CLASSIFIERNAME}}",
    BEHAVIORNAME="{{item.BEHAVIORNAME}}",
    ;
{%- endfor -%}
```

### 7 将流策略应用到指定的接口视图。

### 在“MML命令行-UEG”窗口上执行：

```jinja2
{%- for item in add_qosapplication_list -%}
    ADD QOSAPPLICATION:
    {#- --- 必选参数 --- -#}
    POLICYNAME="{{item.POLICYNAME}}",
    IFNAME="{{item.IFNAME}}",
    DIRECTION={{item.DIRECTION}},
    ;
{%- endfor -%}
```

