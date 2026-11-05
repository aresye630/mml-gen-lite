---
id: ''
name: 创建VPN组（VNRS_VNFC）
ne_type: UEG
type: feature
description: 在网络部署时，通常用户会创建很多VPN实例，当配置将报文重定向到指定的VPN时，如果逐个配置报文重定向，会增加配置的复杂度，通过增加VPN组，将报文重定向到指定的VPN组，实现批量操作，可以使配置操作更加便捷。  NP卡场景下，不支持创建VPN组。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","MEC 特性指南（风筝L）","UEG公共特性指南","IP基本特性","IPFD-020400 IP可靠性","IPFD-020401 QoS","特性配置","复杂流分类配置（VNRS_VNFC）","创建VPN组（VNRS_VNFC）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
在网络部署时，通常用户会创建很多VPN实例，当配置将报文重定向到指定的VPN时，如果逐个配置报文重定向，会增加配置的复杂度，通过增加VPN组，将报文重定向到指定的VPN组，实现批量操作，可以使配置操作更加便捷。NP卡场景下，不支持创建VPN组。

## 必备事项
前提条件

设备加电并正常启动。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_sqosvpngroup_list:
      type: items
      properties:
        VPNGROUPNAME:
          name: 'VPN组名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_sqosvpngroup_list_1:
      type: items
      properties:
        VPNGROUPNAME:
          name: 'VPN组名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_sqosvpngroupmem_list:
      type: items
      properties:
        VPNGROUPNAME:
          name: 'VPN组名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        VPNNAME:
          name: 'VPN名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        VPNPRIORITY:
          name: 'VPN优先级'
          type: integer
          minimum: 1
          maximum: 16
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_sqosvpngroupmem_list_1:
      type: items
      properties:
        VPNGROUPNAME:
          name: 'VPN组名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        VPNNAME:
          name: 'VPN名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        VPNPRIORITY:
          name: 'VPN优先级'
          type: integer
          minimum: 1
          maximum: 16
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    add_sqosvpngroup_list:
    - VPNGROUPNAME: 'test1'
    add_sqosvpngroup_list_1:
    - VPNGROUPNAME: 'test1'
    add_sqosvpngroupmem_list:
    - VPNGROUPNAME: 'test1'
      VPNNAME: 'vpn1'
      VPNPRIORITY: 2
    add_sqosvpngroupmem_list_1:
    - VPNGROUPNAME: 'test1'
      VPNNAME: 'vpn1'
      VPNPRIORITY: 2
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 增加VPN组

### 在“MML命令行-UEG”窗口上执行：

```jinja2
{%- for item in add_sqosvpngroup_list -%}
    ADD SQOSVPNGROUP:
    {#- --- 必选参数 --- -#}
    VPNGROUPNAME="{{item.VPNGROUPNAME}}",
    ;
{%- endfor -%}
```

#### 1.1 //创建VPN组。

```jinja2
{%- for item in add_sqosvpngroup_list_1 -%}
    ADD SQOSVPNGROUP:
    {#- --- 必选参数 --- -#}
    VPNGROUPNAME="{{item.VPNGROUPNAME}}",
    ;
{%- endfor -%}
```

### 2 增加VPN组成员

### 在“MML命令行-UEG”窗口上执行：

```jinja2
{%- for item in add_sqosvpngroupmem_list -%}
    ADD SQOSVPNGROUPMEM:
    {#- --- 必选参数 --- -#}
    VPNGROUPNAME="{{item.VPNGROUPNAME}}",
    VPNNAME="{{item.VPNNAME}}",
    VPNPRIORITY={{item.VPNPRIORITY}},
    ;
{%- endfor -%}
```

#### 2.1 //增加VPN组成员。

```jinja2
{%- for item in add_sqosvpngroupmem_list_1 -%}
    ADD SQOSVPNGROUPMEM:
    {#- --- 必选参数 --- -#}
    VPNGROUPNAME="{{item.VPNGROUPNAME}}",
    VPNNAME="{{item.VPNNAME}}",
    VPNPRIORITY={{item.VPNPRIORITY}},
    ;
{%- endfor -%}
```

