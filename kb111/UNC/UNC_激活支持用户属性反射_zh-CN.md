---
id: ''
name: 激活支持用户属性反射
ne_type: UNC
type: feature
description: 当需要将用户接入属性映射到话单信息中时，需要激活接入用户属性反射功能。  适用于GGSN、PGW-C、SMF。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","计费管理功能","WSFD-011309 支持用户属性反射","激活支持用户属性反射"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当需要将用户接入属性映射到话单信息中时，需要激活接入用户属性反射功能。适用于GGSN、PGW-C、SMF。

## 必备事项
前提条件

请仔细阅读WSFD-011309 支持用户属性反射。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_srvnoderatpri_list:
      type: items
      properties:
        FIRSTPRIORITY:
          name: 'RAT类型的第一优先级'
          type: string
          enum:
          - RAT
          - SGSN_IP
          required: false
          description: '配置获取RAT Type的两种方式的优先级，两个参数的配置不能相同。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SECONDPRIORITY:
          name: 'RAT类型的第二优先级'
          type: string
          enum:
          - RAT
          - SGSN_IP
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        NODETYPE:
          name: '网元类型'
          type: string
          enum:
          - GGSN
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_srvnoderat_list:
      type: items
      properties:
        IPVERSION:
          name: 'IP地址版本类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SRVNODESTARTV4:
          name: 'Service Node的起始IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SRVNODEENDV4:
          name: 'Service Node的结束IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        RATTYPE:
          name: 'RAT类型'
          type: string
          enum:
          - UTRAN
          - GERAN
          - WLAN
          - GAN
          - EUTRAN
          - 'NULL'
          - EUTRAN_NB_IOT
          required: true
          description: '配置SGSN/SGW的IP地址段与RAT类型间的映射关系表。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SRVNODEENDV6:
          name: 'Service Node的结束IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRVNODESTARTV6:
          name: 'Service Node的起始IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_dftsrvnoderat_list:
      type: items
      properties:
        RATTYPE:
          name: 'RAT类型'
          type: string
          enum:
          - NONE
          - UTRAN
          - GERAN
          - WLAN
          - GAN
          - EUTRAN
          - UNSPECIFIED
          - EUTRAN_NB_IOT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NODETYPE:
          name: '网元类型'
          type: string
          enum:
          - GGSN
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_cdrfieldtemp_list:
      type: items
      properties:
        TEMPLATENAME:
          name: '话单字段模板名'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RATTYPE:
          name: 'rat-type'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '配置话单中携带的字段，只有SGSN/S-GW和GGSN/PGW-C/SMF都支持携带rat-type字段，在话单格式里配置此字段才会生效，否则配置无效。'
          data_source: '与对端协商'
          pattern: ''
          default: ENABLE
        ULI:
          name: 'user-location-information'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ENABLE
        MSTIMEZONE:
          name: 'ms-time-zone'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ENABLE
        ULIWLAN:
          name: 'ULI携带WLAN地址信息'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
    add_apn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SERVINGNODERAT:
          name: '根据SGSN/SGW映射RAT'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: '配置使用SGSN/S-GW IP映射方式来获取RAT类型的开关。'
          data_source: '本端规划'
          pattern: ''
          default: ENABLE
    set_apnchargectrl_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GCDRTEMPLATE:
          name: 'G-CDR话单字段模板名'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PGWCDRTEMPLATE:
          name: 'PGW-CDR话单字段模板名'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SGWCDRTEMPLATE:
          name: 'SGW-CDR话单字段模板名'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_srvnoderatpri_list:
    - FIRSTPRIORITY: RAT
      SECONDPRIORITY: SGSN_IP
      NODETYPE: GGSN
    add_srvnoderat_list:
    - IPVERSION: IPV4
      SRVNODESTARTV4: '192.168.1.1'
      SRVNODEENDV4: '192.168.2.2'
      RATTYPE: UTRAN
      SRVNODEENDV6: ''
      SRVNODESTARTV6: ''
    set_dftsrvnoderat_list:
    - RATTYPE: UTRAN
      NODETYPE: GGSN
    add_cdrfieldtemp_list:
    - TEMPLATENAME: 'cdr-field-test'
      RATTYPE: ENABLE
      ULI: ENABLE
      MSTIMEZONE: ENABLE
      ULIWLAN: DISABLE
    add_apn_list:
    - APN: 'apn-test'
      SERVINGNODERAT: ENABLE
    set_apnchargectrl_list:
    - APN: 'apn-test'
      GCDRTEMPLATE: 'cdr-field-test'
      PGWCDRTEMPLATE: 'cdr-field-test'
      SGWCDRTEMPLATE: 'cdr-field-test'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 配置获取RAT Type的两种方式的优先级。

```jinja2
{%- for item in set_srvnoderatpri_list -%}
    SET SRVNODERATPRI:
    {#- --- 必选参数 --- -#}
    NODETYPE={{item.NODETYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.FIRSTPRIORITY is not none -%}
        FIRSTPRIORITY={{item.FIRSTPRIORITY}},
    {%- endif -%}
    {%- if item.SECONDPRIORITY is not none -%}
        SECONDPRIORITY={{item.SECONDPRIORITY}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置SGSN/S-GW IP与RAT类型间的映射关系表。

```jinja2
{%- for item in add_srvnoderat_list -%}
    ADD SRVNODERAT:
    {#- --- 必选参数 --- -#}
    IPVERSION={{item.IPVERSION}},
    RATTYPE={{item.RATTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV4' -%}
        SRVNODESTARTV4="{{item.SRVNODESTARTV4}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV4' -%}
        SRVNODEENDV4="{{item.SRVNODEENDV4}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV6' -%}
        SRVNODEENDV6="{{item.SRVNODEENDV6}}",
    {%- endif -%}
    {#- --- 条件必选：IPVERSION=IPV6 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV6' -%}
        SRVNODESTARTV6="{{item.SRVNODESTARTV6}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 配置SGSN/S-GW默认RAT类型。

```jinja2
{%- for item in set_dftsrvnoderat_list -%}
    SET DFTSRVNODERAT:
    {#- --- 必选参数 --- -#}
    NODETYPE={{item.NODETYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.RATTYPE is not none -%}
        RATTYPE={{item.RATTYPE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### SGSN/S-GW IP地址段与RAT类型的映射表配有默认项，当SGSN/S-GW IP在表中没有匹配项时，会用默认的RAT类型作为它对应的RAT类型。当要配置默认表项时，使用**ADD DFTSRVNODERAT**命令。

### 5 配置话单中携带的字段。

```jinja2
{%- for item in add_cdrfieldtemp_list -%}
    ADD CDRFIELDTEMP:
    {#- --- 必选参数 --- -#}
    TEMPLATENAME="{{item.TEMPLATENAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.RATTYPE is not none -%}
        RATTYPE={{item.RATTYPE}},
    {%- endif -%}
    {%- if item.ULI is not none -%}
        ULI={{item.ULI}},
    {%- endif -%}
    {%- if item.MSTIMEZONE is not none -%}
        MSTIMEZONE={{item.MSTIMEZONE}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：ULI=ENABLE 时可选 --- -#}
    {%- if item.ULI == 'ENABLE' -%}
        {%- if item.ULIWLAN is not none -%}
            ULIWLAN={{item.ULIWLAN}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 6 配置APN实例，设置是否允许此APN下的用户通过SGSN/S-GW-IP映射方式来获取RAT Type。

```jinja2
{%- for item in add_apn_list -%}
    ADD APN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.SERVINGNODERAT is not none -%}
        SERVINGNODERAT={{item.SERVINGNODERAT}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 7 配置APN实例绑定话单字段模板。

```jinja2
{%- for item in set_apnchargectrl_list -%}
    SET APNCHARGECTRL:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.GCDRTEMPLATE is not none -%}
        GCDRTEMPLATE="{{item.GCDRTEMPLATE}}",
    {%- endif -%}
    {%- if item.PGWCDRTEMPLATE is not none -%}
        PGWCDRTEMPLATE="{{item.PGWCDRTEMPLATE}}",
    {%- endif -%}
    {%- if item.SGWCDRTEMPLATE is not none -%}
        SGWCDRTEMPLATE="{{item.SGWCDRTEMPLATE}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

