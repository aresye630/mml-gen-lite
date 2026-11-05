---
id: ''
name: 配置NBNS
ne_type: UNC
type: feature
description: NetBIOS是Network Basic Input/Output System的简称，是一个网络协议。运行在TCP上的NetBIOS又称为NetBIOS Over TCP，简称NBT，NBT可以提供三种不同的服务：  * 名字服务（NetBIOS Name Service），**即NBNS**，提供网络节点名称或IP地址查询服务，类似于TCP/IP协议中的DNS，负责查找目标节点的节点IP地址，并赋予其一个NetBIOS名称。 * 数据包服务（NetBIOS Datagram Service），提供基于UDP的不可靠的无连接的数据包传输服务。 * 会话服务（NetBIOS Session Service），提供可靠的基于TCP连接的数据包传输服务。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","组网功能","支持NBNS（NetBIOS Name Server）","配置NBNS"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
NetBIOS是Network Basic Input/Output System的简称，是一个网络协议。运行在TCP上的NetBIOS又称为NetBIOS Over TCP，简称NBT，NBT可以提供三种不同的服务：* 名字服务（NetBIOS Name Service），**即NBNS**，提供网络节点名称或IP地址查询服务，类似于TCP/IP协议中的DNS，负责查找目标节点的节点IP地址，并赋予其一个NetBIOS名称。* 数据包服务（NetBIOS Datagram Service），提供基于UDP的不可靠的无连接的数据包传输服务。* 会话服务（NetBIOS Session Service），提供可靠的基于TCP连接的数据包传输服务。

## 必备事项
前提条件

已掌握NBNS相关原理。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_apn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '* 可选配置，如果现网已配置所需的APN实例，执行**LST APN**查询获取即可，无需重复配置。 * APN实例的相关属性（是否为虚拟APN，是否绑定VPN等）可根据实际情况配置。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_apnnbns_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '配置指定APN实例的NBNS信息。'
          data_source: '通过**LST APN**查询获取'
          pattern: ''
          default: ''
        IPV4PRIMARYIP:
          name: '主NBNS'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4PRIORFIRST:
          name: '第一优先级'
          type: string
          enum:
          - LOCAL
          - RADIUS
          - DHCP
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4SECONDARYIP:
          name: '备NBNS'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_globalnbns_list:
      type: items
      properties:
        NBNSSWITCH:
          name: 'NBNS功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '配置全局缺省的NBNS信息。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        MNBNSSERVER:
          name: '主NBNS服务器IP'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        BNBNSSERVER:
          name: '备NBNS服务器IP'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        FIRSTMODE:
          name: '第一优先级服务器属性'
          type: string
          enum:
          - LOCAL
          - RADIUS
          - DHCP
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SECONDMODE:
          name: '第二优先级服务器属性'
          type: string
          enum:
          - LOCAL
          - RADIUS
          - DHCP
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        THIRDMODE:
          name: '第三优先级服务器属性'
          type: string
          enum:
          - LOCAL
          - RADIUS
          - DHCP
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
  examples:
    add_apn_list:
    - APN: 'apn1'
    add_apnnbns_list:
    - APN: 'apn1'
      IPV4PRIMARYIP: '192.168.5.2'
      IPV4PRIORFIRST: LOCAL
      IPV4SECONDARYIP: '192.168.5.3'
    set_globalnbns_list:
    - NBNSSWITCH: ENABLE
      MNBNSSERVER: '10.1.1.1'
      BNBNSSERVER: '10.2.2.2'
      FIRSTMODE: LOCAL
      SECONDMODE: RADIUS
      THIRDMODE: DHCP
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 配置APN实例。

```jinja2
{%- for item in add_apn_list -%}
    ADD APN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    ;
{%- endfor -%}
```

### 3 配置指定APN实例的NBNS信息，包括NBNS主备地址及优先级。

```jinja2
{%- for item in add_apnnbns_list -%}
    ADD APNNBNS:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.IPV4PRIMARYIP is not none -%}
        IPV4PRIMARYIP="{{item.IPV4PRIMARYIP}}",
    {%- endif -%}
    {%- if item.IPV4PRIORFIRST is not none -%}
        IPV4PRIORFIRST={{item.IPV4PRIORFIRST}},
    {%- endif -%}
    {%- if item.IPV4SECONDARYIP is not none -%}
        IPV4SECONDARYIP="{{item.IPV4SECONDARYIP}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 配置全局缺省的NBNS信息，包括NBNS主备地址及优先级。

```jinja2
{%- for item in set_globalnbns_list -%}
    SET GLOBALNBNS:
    {#- --- 可选参数 --- -#}
    {%- if item.NBNSSWITCH is not none -%}
        NBNSSWITCH={{item.NBNSSWITCH}},
    {%- endif -%}
    {%- if item.MNBNSSERVER is not none -%}
        MNBNSSERVER="{{item.MNBNSSERVER}}",
    {%- endif -%}
    {%- if item.BNBNSSERVER is not none -%}
        BNBNSSERVER="{{item.BNBNSSERVER}}",
    {%- endif -%}
    {%- if item.FIRSTMODE is not none -%}
        FIRSTMODE={{item.FIRSTMODE}},
    {%- endif -%}
    {%- if item.SECONDMODE is not none -%}
        SECONDMODE={{item.SECONDMODE}},
    {%- endif -%}
    {%- if item.THIRDMODE is not none -%}
        THIRDMODE={{item.THIRDMODE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

