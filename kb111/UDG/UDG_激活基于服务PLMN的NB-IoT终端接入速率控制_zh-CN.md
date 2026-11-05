---
id: GWFD-110612
name: 激活基于服务PLMN的NB-IoT终端接入速率控制
ne_type: UDG
type: feature
description: 在UDG上激活基于服务PLMN的NB-IoT终端接入速率控制，PGW-U根据MME发来的速率控制信息，对数据包的转发速率进行控制。对于超过门限的数据包，PGW-U进行丢包处理，未超过门限的数据包进行正常的转发处理。  适用于SGW-U、PGW-U。
risk_level: ''
doc_source: ["特性部署","特性指南","UDG特性指南","物联网功能","NB-IoT","GWFD-110612 基于服务PLMN的NB-IoT终端接入速率控制","激活基于服务PLMN的NB-IoT终端接入速率控制"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
在UDG上激活基于服务PLMN的NB-IoT终端接入速率控制，PGW-U根据MME发来的速率控制信息，对数据包的转发速率进行控制。对于超过门限的数据包，PGW-U进行丢包处理，未超过门限的数据包进行正常的转发处理。适用于SGW-U、PGW-U。

## 必备事项
前提条件

* 请仔细阅读GWFD-110612 基于服务PLMN的NB-IoT终端接入速率控制。
* 已开启NB-IoT基本接入功能（详见激活NB-IoT终端标准接入）。
* 完成激活基于信令面的数据传输。
* 完成加载License（本特性完整的功能需要同时在SGW-U/PGW-U和MME上开启对应License，如果有需求，请联系华为技术支持工程师处理）。
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
    add_apn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '如果需要配置APN下的基于服务PLMN的终端接入速率控制，则配置该APN，否则仅打开License即可。APN配置需要与控制面保持一致。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3G5PNRC01'
      SWITCH: ENABLE
    add_apn_list:
    - APN: 'apnplmn'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 打开本特性的License控制开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 2 **可选：**配置基于服务PLMN的NB-IoT终端接入速率控制使用的APN。

```jinja2
{%- if is_optional_configure_apn -%}
    {%- for item in add_apn_list -%}
        ADD APN:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

### 本特性需要同时在MME、SGW-C/PGW-C进行配置以确保能够生效，在MME上可配置速率控制参数，在SGW-C/PGW-C上可以配置如下相关内容：

### APN下的基于服务PLMN的终端接入速率控制开关：打开后，当UE使用特定的APN接入且位于特定的PLMN下时，该特性生效。

### 全局基于服务PLMN的终端接入速率控制开关：打开后，当UE位于特定的PLMN下时，该特性生效。

### Serving PLMN Rate Control相关信息。

### 详情请查阅相关产品文档。

