---
id: ''
name: 激活NRF主备容灾特性
ne_type: UNC
type: feature
description: 当运营商希望通过地理容灾确保业务所在地发生重大灾难NRF依然能够提供正常的数据业务，保证5GC中各NF业务流程的可靠性时，部署此特性。  本操作指导介绍在运行网络中分别在两个DC新增2台NRF用于设备间地理容灾或者将2个单机运行的NRF改造组成主备容灾的操作过程。  * 适用于NRF。 * NRF容灾部署不建议使用NRF主备容灾，推荐使用NRF双活容灾，NRF双活容灾可靠性更高，也更符合NRF内部容灾的实现原理。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","容灾功能","WSFD-114001 NRF主备容灾","激活NRF主备容灾特性"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当运营商希望通过地理容灾确保业务所在地发生重大灾难NRF依然能够提供正常的数据业务，保证5GC中各NF业务流程的可靠性时，部署此特性。本操作指导介绍在运行网络中分别在两个DC新增2台NRF用于设备间地理容灾或者将2个单机运行的NRF改造组成主备容灾的操作过程。* 适用于NRF。* NRF容灾部署不建议使用NRF主备容灾，推荐使用NRF双活容灾，NRF双活容灾可靠性更高，也更符合NRF内部容灾的实现原理。

## 必备事项
前提条件

前提条件

* 请仔细阅读WSFD-114001 NRF主备容灾特性概述。
* 完成加载License。
* 待改造的2个单机的NRF需要先升级到UNC 20.6.0及后续版本。
* 已按照自身组网完成两个NRF之间的路由配置，对于IPv4组网，各配置场景请参考“初始配置与调测”中自动部署配置动态路由OSPF+BFD组网（IPv4）、配置静态路由+BFD组网（IPv4）、配置BGP over OSPF/静态路由+BFD（IPv4）或手动部署配置动态路由OSPF+BFD组网（IPv4）、配置静态路由+BFD组网（IPv4）、配置BGP over OSPF/静态路由+BFD（IPv4）。
* 已按照自身组网完成两个NRF之间的路由配置，对于IPv6组网，各配置场景请参考“初始配置与调测”中自动部署配置动态路由OSPFv3+BFD组网（IPv6）、配置静态路由+BFD组网（IPv6）、配置BGP over OSPFv3/静态路由+BFD（IPv6）或手动部署配置动态路由OSPFv3+BFD组网（IPv6）、配置静态路由+BFD组网（IPv6）、配置BGP over OSPFv3/静态路由+BFD（IPv6）。
* 各NF已完成配置到两个NRF的数据，对接的2个NRF区分高低优先级。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_drinst_list:
      type: items
      properties:
        DRINSTID:
          name: '容灾实例标识'
          type: integer
          minimum: 0
          maximum: 63
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        DRINSTNAME:
          name: '容灾实例名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_drcomm_list:
      type: items
      properties:
        DRINSTID:
          name: '容灾实例标识'
          type: integer
          minimum: 0
          maximum: 63
          required: true
          description: 'IP地址用于NRF数据同步通道通信，此IP地址为NRF本端规划的。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP版本号'
          type: string
          enum:
          - COMM_IPV4
          - COMM_IPV6
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        COMMIPV4:
          name: '通信IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        VPNNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        COMMIPV6:
          name: 'ipv6通信地址'
          type: string
          maxLength: 39
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
    set_dbsoftpara_list:
      type: items
      properties:
        PARAID:
          name: '参数标识'
          type: integer
          minimum: 0
          maximum: 1023
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PARAVALUE:
          name: '参数值'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_nrfdrrtstasw_list:
      type: items
      properties:
        FCSWITCH:
          name: '双活备份状态忽略开关'
          type: string
          enum:
          - FUNC_ON
          - FUNC_OFF
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_dbsoftpara_list_2:
      type: items
      properties:
        PARAID:
          name: '参数标识'
          type: integer
          minimum: 0
          maximum: 1023
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PARAVALUE:
          name: '参数值'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_nrfdrrtstasw_list_2:
      type: items
      properties:
        FCSWITCH:
          name: '双活备份状态忽略开关'
          type: string
          enum:
          - FUNC_ON
          - FUNC_OFF
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_drinst_list:
    - DRINSTID: 0
      DRINSTNAME: 'nrf1'
    add_drcomm_list:
    - DRINSTID: 0
      IPVERSION: COMM_IPV4
      COMMIPV4: '10.5.5.1'
      VPNNAME: '_public_'
      COMMIPV6: ''
    set_licenseswitch_list:
    - LICITEM: 'LKV2ASNRR01'
      SWITCH: ENABLE
    set_dbsoftpara_list:
    - PARAID: 7
      PARAVALUE: 1
    set_nrfdrrtstasw_list:
    - FCSWITCH: FUNC_ON
    set_dbsoftpara_list_2:
    - PARAID: 7
      PARAVALUE: 0
    set_nrfdrrtstasw_list_2:
    - FCSWITCH: FUNC_OFF
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 在NRF1和NRF2上分别配置容灾组。

#### 1.1 配置容灾实例。

```jinja2
{%- for item in add_drinst_list -%}
    ADD DRINST:
    {#- --- 必选参数 --- -#}
    DRINSTID={{item.DRINSTID}},
    {#- --- 可选参数 --- -#}
    {%- if item.DRINSTNAME is not none -%}
        DRINSTNAME="{{item.DRINSTNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.2 配置主备NRF容灾实例通信地址信息，用于数据同步通道建立。

```jinja2
{%- for item in add_drcomm_list -%}
    ADD DRCOMM:
    {#- --- 必选参数 --- -#}
    DRINSTID={{item.DRINSTID}},
    IPVERSION={{item.IPVERSION}},
    VPNNAME="{{item.VPNNAME}}",
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=COMM_IPV4 时必选 --- -#}
    {%- if item.IPVERSION == 'COMM_IPV4' -%}
        COMMIPV4="{{item.COMMIPV4}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=COMM_IPV6 时必选 --- -#}
    {%- if item.IPVERSION == 'COMM_IPV6' -%}
        COMMIPV6="{{item.COMMIPV6}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 此命令针对每个NRF需要配置两次，分别为本端NRF实例通信地址信息和对端NRF实例通信地址信息，并且需要先配置本端NRF实例通信地址信息。

### 2 NRF1和NRF2上的1都完成后，在NRF1和NRF2上分别打开主备容灾的License开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 3 **可选：**NRF1和NRF2上的2都完成后，在NRF1和NRF2上分别先关闭容灾通道开关，打开主备备份状态忽略开关。

### 如果是新建的2个NRF组成主备NRF，则不需要执行此步骤。

#### 3.1 初始先关闭容灾通道开关。

```jinja2
{%- if is_optional_close_dr_channel_open_backup_ignore -%}
    {%- for item in set_dbsoftpara_list -%}
        SET DBSOFTPARA:
        {#- --- 必选参数 --- -#}
        PARAID={{item.PARAID}},
        PARAVALUE={{item.PARAVALUE}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.2 打开主备备份状态忽略开关，忽略数据备份状态，NRF允许直接处理业务。

```jinja2
{%- if is_optional_close_dr_channel_open_backup_ignore -%}
    {%- for item in set_nrfdrrtstasw_list -%}
        SET NRFDRRTSTASW:
        {#- --- 必选参数 --- -#}
        FCSWITCH={{item.FCSWITCH}},
        ;
    {%- endfor -%}
{%- endif -%}
```

### 4 **可选：**在NRF1和NRF2上分别再打开容灾通道开关，关闭主备备份状态忽略开关，触发NRF间数据同步。

### 如果是新建的2个NRF组成主备NRF，则不需要执行此步骤。

#### 4.1 对同一个NRF，请在3.a执行关闭容灾通道开关1分钟后，打开容灾通道开关，数据可以实时同步。

```jinja2
{%- if is_optional_open_dr_channel_close_backup_ignore -%}
    {%- for item in set_dbsoftpara_list_2 -%}
        SET DBSOFTPARA:
        {#- --- 必选参数 --- -#}
        PARAID={{item.PARAID}},
        PARAVALUE={{item.PARAVALUE}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.2 关闭主备备份状态忽略开关，NRF进入实时备份状态时，才允许处理业务。

```jinja2
{%- if is_optional_open_dr_channel_close_backup_ignore -%}
    {%- for item in set_nrfdrrtstasw_list_2 -%}
        SET NRFDRRTSTASW:
        {#- --- 必选参数 --- -#}
        FCSWITCH={{item.FCSWITCH}},
        ;
    {%- endfor -%}
{%- endif -%}
```

