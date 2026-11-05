---
id: ''
name: 创建VPN组（VNRS）
ne_type: UNC
type: feature
description: 在网络部署时，通常用户会创建很多VPN实例，当配置将报文重定向到指定的VPN时，如果逐个配置报文重定向，会增加配置的复杂度，通过增加VPN组，将报文重定向到指定的VPN组，实现批量操作，可以使配置操作更加便捷。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","IP基本功能","IPFD-012001 QoS","特性配置","复杂流分类配置（VNRS）","创建VPN组（VNRS）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
在网络部署时，通常用户会创建很多VPN实例，当配置将报文重定向到指定的VPN时，如果逐个配置报文重定向，会增加配置的复杂度，通过增加VPN组，将报文重定向到指定的VPN组，实现批量操作，可以使配置操作更加便捷。

## 必备事项
前提条件

设备加电并正常启动。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
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
  examples:
    add_sqosvpngroup_list:
    - VPNGROUPNAME: 'test1'
    add_sqosvpngroupmem_list:
    - VPNGROUPNAME: 'test1'
      VPNNAME: 'vpn1'
      VPNPRIORITY: 2
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 增加VPN组

### 在“MML命令行-UNC”窗口上执行：

```jinja2
{%- for item in add_sqosvpngroup_list -%}
    ADD SQOSVPNGROUP:
    {#- --- 必选参数 --- -#}
    VPNGROUPNAME="{{item.VPNGROUPNAME}}",
    ;
{%- endfor -%}
```

### 2 增加VPN组成员

### 在“MML命令行-UNC”窗口上执行：

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

