---
id: ''
name: 去使能容灾模式（1+1主备）
ne_type: UEG
type: feature
description: 去使能1+1主备容灾模式时（比如进行网元卸载、容灾模式改造等），需要参考本页面进行配置。  本页面中的命令均为高危命令，请在华为工程师指导下执行。否则可能导致业务受损。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","UEG容灾方案介绍（风筝L）","1+1主备容灾原理","1+1主备容灾部署与调测","1+1主备容灾模式","去使能容灾模式（1+1主备）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
去使能1+1主备容灾模式时（比如进行网元卸载、容灾模式改造等），需要参考本页面进行配置。本页面中的命令均为高危命令，请在华为工程师指导下执行。否则可能导致业务受损。

## 必备事项
前提条件

两套UEG已完成1+1主备容灾模式配置。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_amfsoftparaofbit_list:
      type: items
      properties:
        DT:
          name: '数据类型'
          type: string
          enum:
          - Dw
          - Byte
          required: true
          description: '去使能AMF服务主备容灾功能。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        DWORDNUM:
          name: 'DWORD索引'
          type: integer
          minimum: 1
          maximum: 1500
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        VALUE:
          name: '软参记录值'
          type: string
          enum:
          - VALUE_0
          - VALUE_1
          required: true
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        POSITION:
          name: '比特位'
          type: integer
          minimum: 1
          maximum: 32
          required: true
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
    set_softparaofbit_list:
      type: items
      properties:
        DT:
          name: '参数类型'
          type: string
          enum:
          - BYTE
          - BYTE_EX
          - BYTE_EX_B
          - DWORD
          - DWORD_EX
          - DWORD_EX_B
          required: true
          description: '去使能MME服务主备容灾功能。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        PARANUM:
          name: '参数索引'
          type: integer
          minimum: 1
          maximum: 512
          required: true
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        VALUE:
          name: '软参值'
          type: string
          enum:
          - VALUE_0
          - VALUE_1
          required: true
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        POSITION:
          name: '比特位'
          type: integer
          minimum: 1
          maximum: 32
          required: true
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
    set_upsoftpara_list:
      type: items
      properties:
        DT:
          name: '软参记录数据类型'
          type: string
          enum:
          - BIT
          - BYTE
          - DWORD
          - STRING
          required: true
          description: '去使能UPF服务主备容灾功能。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        BITNUM:
          name: 'Bit索引'
          type: integer
          minimum: 1
          maximum: 3840
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        BITVALUE:
          name: 'Bit值'
          type: integer
          minimum: 0
          maximum: 1
          required: false
          description: ''
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
        MME:
          name: '是否监控MME服务'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: '去使能1+1主备容灾模式时需要将这些参数的值设置为“NO”。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: NO
        AMF:
          name: '是否监控AMF服务'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: NO
        HSS:
          name: '是否监控HSS服务'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: NO
        UDM:
          name: '是否监控UDM服务'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: NO
        SMF:
          name: '是否监控SMF服务'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: NO
        GWC:
          name: '是否监控GW-C服务'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: NO
        PCF:
          name: '是否监控PCF服务'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: NO
        PCRF:
          name: '是否监控PCRF服务'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: NO
        UPF:
          name: '是否监控UPF服务'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: NO
        UDR:
          name: '是否监控UDR服务'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: NO
  examples:
    set_amfsoftparaofbit_list:
    - DT: Dw
      DWORDNUM: 400
      VALUE: VALUE_0
      POSITION: 1
    set_softparaofbit_list:
    - DT: DWORD_EX_B
      PARANUM: 61
      VALUE: VALUE_0
      POSITION: 1
    set_upsoftpara_list:
    - DT: BIT
      BITNUM: 3001
      BITVALUE: 0
    rmv_drdci_list:
    - DRGROUPID: 1
      IPVERSION: IPV4
      LDCIP: '10.10.198.8'
      PDCIP: '10.10.199.8'
      VPNINSTANCE: 'VPN_DCI'
      LDCIPV6: 'FC00::10:10:198:8'
      PDCIPV6: 'FC00::10:10:199:8'
    - DRGROUPID: 1
      IPVERSION: IPV4
      LDCIP: '10.10.199.8'
      PDCIP: '10.10.199.8'
      VPNINSTANCE: 'VPN_DCI'
      LDCIPV6: ''
      PDCIPV6: ''
    rmv_drgroupinfo_list:
    - DRGROUPID: 1
    - DRGROUPID: 1
    set_drkeynf_list:
    - MME: NO
      AMF: NO
      HSS: NO
      UDM: NO
      SMF: NO
      GWC: NO
      PCF: NO
      PCRF: NO
      UPF: NO
      UDR: NO
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 将使能主备容灾功能的软参设置为不使能。

```jinja2
{%- for item in set_amfsoftparaofbit_list -%}
    SET AMFSOFTPARAOFBIT:
    {#- --- 必选参数 --- -#}
    DT={{item.DT}},
    VALUE={{item.VALUE}},
    POSITION={{item.POSITION}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：DT=Dw 时必选 --- -#}
    {%- if item.DT == 'Dw' -%}
        DWORDNUM={{item.DWORDNUM}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in set_softparaofbit_list -%}
    SET SOFTPARAOFBIT:
    {#- --- 必选参数 --- -#}
    DT={{item.DT}},
    PARANUM={{item.PARANUM}},
    VALUE={{item.VALUE}},
    POSITION={{item.POSITION}},
    ;
{%- endfor -%}
```

```jinja2
{%- for item in set_upsoftpara_list -%}
    SET UPSOFTPARA:
    {#- --- 必选参数 --- -#}
    DT={{item.DT}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：DT=BIT 时必选 --- -#}
    {%- if item.DT == 'BIT' -%}
        BITNUM={{item.BITNUM}},
    {%- endif -%}
    {#- --- 条件必选：DT=BIT 时必选 --- -#}
    {%- if item.DT == 'BIT' -%}
        BITVALUE={{item.BITVALUE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 删除容灾控制通道相关信息。

#### 3.1 //DC1：

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

#### 4.1 //DC1：

```jinja2
{%- for item in rmv_drgroupinfo_list -%}
    RMV DRGROUPINFO:
    {#- --- 必选参数 --- -#}
    DRGROUPID={{item.DRGROUPID}},
    ;
{%- endfor -%}
```

### 5 将监控的服务都设置为不监控。

```jinja2
{%- for item in set_drkeynf_list -%}
    SET DRKEYNF:
    {#- --- 可选参数 --- -#}
    {%- if item.MME is not none -%}
        MME={{item.MME}},
    {%- endif -%}
    {%- if item.AMF is not none -%}
        AMF={{item.AMF}},
    {%- endif -%}
    {%- if item.HSS is not none -%}
        HSS={{item.HSS}},
    {%- endif -%}
    {%- if item.UDM is not none -%}
        UDM={{item.UDM}},
    {%- endif -%}
    {%- if item.SMF is not none -%}
        SMF={{item.SMF}},
    {%- endif -%}
    {%- if item.GWC is not none -%}
        GWC={{item.GWC}},
    {%- endif -%}
    {%- if item.PCF is not none -%}
        PCF={{item.PCF}},
    {%- endif -%}
    {%- if item.PCRF is not none -%}
        PCRF={{item.PCRF}},
    {%- endif -%}
    {%- if item.UPF is not none -%}
        UPF={{item.UPF}},
    {%- endif -%}
    {%- if item.UDR is not none -%}
        UDR={{item.UDR}},
    {%- endif -%}
    ;
{%- endfor -%}
```

