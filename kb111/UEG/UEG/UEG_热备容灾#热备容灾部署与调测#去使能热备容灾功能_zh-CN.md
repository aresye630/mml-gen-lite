---
id: ''
name: 去使能热备容灾功能
ne_type: UEG
type: feature
description: 去使能热备容灾功能时（比如进行网元卸载、容灾模式改造等），需要参考本页面进行配置。  * 本页面中的命令均为高危命令，请在华为工程师指导下执行。否则可能导致业务受损。 * 按照本章节操作去使能热备容灾功能后，由于2台UEG的业务IP依然相同，备用UEG重启后，会导致主用UEG无法正常工作。因此必须先规划好备用UEG的目标业务IP，在运行状态为“备用”的UEG上去使能热备容灾功能后，必须将该UEG的业务IP更改成目标业务IP，才能重启备用UEG。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","UEG容灾方案介绍（风筝L）","热备容灾","热备容灾部署与调测","去使能热备容灾功能"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
去使能热备容灾功能时（比如进行网元卸载、容灾模式改造等），需要参考本页面进行配置。* 本页面中的命令均为高危命令，请在华为工程师指导下执行。否则可能导致业务受损。* 按照本章节操作去使能热备容灾功能后，由于2台UEG的业务IP依然相同，备用UEG重启后，会导致主用UEG无法正常工作。因此必须先规划好备用UEG的目标业务IP，在运行状态为“备用”的UEG上去使能热备容灾功能后，必须将该UEG的业务IP更改成目标业务IP，才能重启备用UEG。

## 必备事项
前提条件

前提条件

两套UEG已完成热备容灾功能配置。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_drgroupablement_list:
      type: items
      properties:
        DRGROUPABLEMENT:
          name: '是否使能热备容灾组'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: true
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        ISAUTOACTIVE:
          name: '是否自动升主'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
    rmv_drdci_list:
      type: items
      properties:
        DRGROUPID:
          name: '容灾组标识'
          type: integer
          minimum: 1
          maximum: 8
          required: true
          description: '已通过**ADD DRDCI**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP版本号'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        LDCIP:
          name: '本端DC通信IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PDCIP:
          name: '对端DC通信IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        VPNINSTANCE:
          name: 'VPN实例名称'
          type: string
          minLength: 1
          maxLength: 31
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        LDCIPV6:
          name: '本端DC通信IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PDCIPV6:
          name: '对端DC通信IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    rmv_drgroupinfo_list:
      type: items
      properties:
        DRGROUPID:
          name: '容灾组标识'
          type: integer
          minimum: 1
          maximum: 8
          required: true
          description: '已通过**ADD DRGROUPINFO**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    set_drkeynf_list:
      type: items
      properties:
        UPF:
          name: '是否监控UPF服务'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: '去使能热备容灾功能时需要将监控的服务信息恢复成默认配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: NO
    rmv_vpninst_list:
      type: items
      properties:
        VPNINSTANCE:
          name: 'VPN实例名'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_drgroupablement_list:
    - DRGROUPABLEMENT: DISABLE
      ISAUTOACTIVE: TRUE
    rmv_drdci_list:
    - DRGROUPID: 1
      IPVERSION: IPv6
      LDCIP: '10.10.198.8'
      PDCIP: '10.10.199.8'
      VPNINSTANCE: 'VRF_PS_Signal'
      LDCIPV6: 'FC00::10:10:198:8'
      PDCIPV6: 'FC00::10:10:199:8'
    rmv_drgroupinfo_list:
    - DRGROUPID: 1
    set_drkeynf_list:
    - UPF: NO
    rmv_vpninst_list:
    - VPNINSTANCE: 'VRF_PS_Signal'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 在主用UEG进行去使能操作，进入“MML命令行-UEG”窗口。

### 2 去使能热备容灾组。说明：参数“ISAUTOACTIVE”仅25.0及以上的版本支持，低版本不需要配置该参数。

```jinja2
{%- for item in set_drgroupablement_list -%}
    SET DRGROUPABLEMENT:
    {#- --- 必选参数 --- -#}
    DRGROUPABLEMENT={{item.DRGROUPABLEMENT}},
    {#- --- 可选参数 --- -#}
    {%- if item.ISAUTOACTIVE is not none -%}
        ISAUTOACTIVE={{item.ISAUTOACTIVE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 删除容灾控制通道相关信息。

```jinja2
{%- for item in rmv_drdci_list -%}
    RMV DRDCI:
    {#- --- 必选参数 --- -#}
    DRGROUPID={{item.DRGROUPID}},
    IPVERSION={{item.IPVERSION}},
    VPNINSTANCE="{{item.VPNINSTANCE}}",
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV4' -%}
        LDCIP="{{item.LDCIP}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV4' -%}
        PDCIP="{{item.PDCIP}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV6' -%}
        PDCIPV6="{{item.PDCIPV6}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV6' -%}
        LDCIPV6="{{item.LDCIPV6}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 删除容灾组信息。

```jinja2
{%- for item in rmv_drgroupinfo_list -%}
    RMV DRGROUPINFO:
    {#- --- 必选参数 --- -#}
    DRGROUPID={{item.DRGROUPID}},
    ;
{%- endfor -%}
```

### 5 将监控的服务信息恢复成默认配置。

```jinja2
{%- for item in set_drkeynf_list -%}
    SET DRKEYNF:
    {#- --- 可选参数 --- -#}
    {%- if item.UPF is not none -%}
        UPF={{item.UPF}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 6 （可选）删除DRDCI仲裁/数据通道对应VPN实例。说明：仅风筝S场景需要删除。

```jinja2
{%- if is_optional_remove_drdci_vpn_instance and is_scenario_kite_s -%}
    {%- for item in rmv_vpninst_list -%}
        RMV VPNINST:
        {#- --- 必选参数 --- -#}
        VPNINSTANCE="{{item.VPNINSTANCE}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

### 7 在备用UEG进行去使能操作，与主用UEG的去使能步骤相同。

### 8 规划修改主、备UEG的逻辑接口地址、UE地址池地址段，使主、备UEG的逻辑接口地址不同、UE地址池地址段不同。

### 9 整机重启主、备UEG。

