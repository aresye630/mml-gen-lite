---
id: GWFD-112001
name: 镜像SIP信令功能
ne_type: UDG
type: feature
description: 合一ProxyUPF/ProxySGW-U/PGW-U支持镜像SIP信令功能，该功能支持重定向VPN和SIP报文 IPV6大包按照固定MTU分片。重定向VPN是指配置路由到GRE隧道，将SIP报文重定向到GRE隧道并发送到指定服务器。重定向VPN需要单独规划。
risk_level: ''
doc_source: ["特性部署","特性指南","UDG特性指南","移动性管理功能","GWFD-112001 Proxy UPF漫游功能","GWFD-112001 Proxy UPF漫游功能","安装部署","镜像SIP信令功能"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
合一ProxyUPF/ProxySGW-U/PGW-U支持镜像SIP信令功能，该功能支持重定向VPN和SIP报文 IPV6大包按照固定MTU分片。重定向VPN是指配置路由到GRE隧道，将SIP报文重定向到GRE隧道并发送到指定服务器。重定向VPN需要单独规划。

## 必备事项
前提条件

* 网元运行正常，且处于运行状态。
* 已规划好重定向VPN的底层组网业务配置。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_vpninst_list:
      type: items
      properties:
        VPNINSTANCE:
          name: 'VPN实例名'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_sipsigmirrorpara_list:
      type: items
      properties:
        SWITCH:
          name: '镜像功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: '-'
          data_source: '固定值'
          pattern: ''
          default: ''
        IPV6FRAGMTU:
          name: '内层IPv6报文分片MTU'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: '控制镜像SIP信令功能发送IPV6报文分片MTU。   * 该参数取值为0，表示不开启报文分片。 * 该参数取值小于IPV6报文MTU最小值1280时，按最小值1280字节控制分片MTU，大于9600时，按9600字节控制分片MTU。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        RDRVPN:
          name: '重定向VPN'
          type: string
          minLength: 1
          maxLength: 31
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_softpara_list:
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
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        BYTENUM:
          name: 'Byte索引'
          type: integer
          minimum: 1
          maximum: 1200
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        BYTEVALUE:
          name: 'Byte值'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        BITNUM:
          name: 'Bit索引'
          type: integer
          minimum: 1
          maximum: 3840
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BITVALUE:
          name: 'Bit值'
          type: integer
          minimum: 0
          maximum: 1
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DWORDNUM:
          name: 'DWord索引'
          type: integer
          minimum: 1
          maximum: 180
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DWORDVALUE:
          name: 'Dword值'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        STRINGNUM:
          name: 'String索引'
          type: integer
          minimum: 1
          maximum: 30
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        STRINGVALUE:
          name: 'String值'
          type: string
          minLength: 0
          maxLength: 64
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_vpninst_list:
    - VPNINSTANCE: 'SIP_OM'
    set_sipsigmirrorpara_list:
    - SWITCH: ENABLE
      IPV6FRAGMTU: 1800
      RDRVPN: 'SIP_OM'
    set_softpara_list:
    - DT: BYTE
      BYTENUM: 1116
      BYTEVALUE: 72
      BITNUM: ''
      BITVALUE: ''
      DWORDNUM: ''
      DWORDVALUE: ''
      STRINGNUM: ''
      STRINGVALUE: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 安装镜像SIP信令功能插件，完成插件安装后再进行配置操作。请联系华为技术支持获取《UDG镜像SIP信令操作指导》。

### 2 设置镜像SIP信令功能开启，并设置IPv6报文分片值。

```jinja2
{%- for item in add_vpninst_list -%}
    ADD VPNINST:
    {#- --- 必选参数 --- -#}
    VPNINSTANCE="{{item.VPNINSTANCE}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in set_sipsigmirrorpara_list -%}
    SET SIPSIGMIRRORPARA:
    {#- --- 必选参数 --- -#}
    SWITCH={{item.SWITCH}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：SWITCH=ENABLE 时可选 --- -#}
    {%- if item.SWITCH == 'ENABLE' -%}
        {%- if item.IPV6FRAGMTU is not none -%}
            IPV6FRAGMTU={{item.IPV6FRAGMTU}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SWITCH=ENABLE 时可选 --- -#}
    {%- if item.SWITCH == 'ENABLE' -%}
        {%- if item.RDRVPN is not none -%}
            RDRVPN="{{item.RDRVPN}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 使能镜像SIP信令惯性运行功能。

```jinja2
{%- for item in set_softpara_list -%}
    SET SOFTPARA:
    {#- --- 必选参数 --- -#}
    DT={{item.DT}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：DT=BYTE 时必选 --- -#}
    {%- if item.DT == 'BYTE' -%}
        BYTENUM={{item.BYTENUM}},
    {%- endif -%}
    {#- --- 条件必选：DT=BYTE 时必选 --- -#}
    {%- if item.DT == 'BYTE' -%}
        BYTEVALUE={{item.BYTEVALUE}},
    {%- endif -%}
    {#- --- 条件必选：DT=BIT 时必选 --- -#}
    {%- if item.DT == 'BIT' -%}
        BITNUM={{item.BITNUM}},
    {%- endif -%}
    {#- --- 条件必选：DT=BIT 时必选 --- -#}
    {%- if item.DT == 'BIT' -%}
        BITVALUE={{item.BITVALUE}},
    {%- endif -%}
    {#- --- 条件必选：DT=DWORD 时必选 --- -#}
    {%- if item.DT == 'DWORD' -%}
        DWORDNUM={{item.DWORDNUM}},
    {%- endif -%}
    {#- --- 条件必选：DT=DWORD 时必选 --- -#}
    {%- if item.DT == 'DWORD' -%}
        DWORDVALUE={{item.DWORDVALUE}},
    {%- endif -%}
    {#- --- 条件必选：DT=STRING 时必选 --- -#}
    {%- if item.DT == 'STRING' -%}
        STRINGNUM={{item.STRINGNUM}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：DT=STRING 时可选 --- -#}
    {%- if item.DT == 'STRING' -%}
        {%- if item.STRINGVALUE is not none -%}
            STRINGVALUE="{{item.STRINGVALUE}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

