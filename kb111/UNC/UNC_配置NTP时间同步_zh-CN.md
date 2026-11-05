---
id: ''
name: 配置NTP时间同步
ne_type: UNC
type: feature
description: 网元可以同时从FusionStage和NTP服务器同步时间信息，这样当一路故障后，另一路仍然可以正常运行，可以保证时间同步的可靠性，如图1所示。  **图1** 网元同时从FusionStage和外部NTP服务器同步时间信息  * 从FusionStage同步时间：当FusionStage在“系统管理 > 系统配置 > 时间管理”页面时，将“支持夏令时时钟”设置为“是”，同时在“应用管理 > MML”执行**SET TZ**命令，将“是否执行夏令时”设置为“YES(是)”，并将相关时区和夏令时参数和FusionStage设置一致。 * 从NTP服务器同步时间：对于计费类网元（UAMF、USMF），直接配置和NTP服务器对接即可。对于非计费类网元（NRF、NSSF、SMSF），需要和OMC对接，OMC最终和NTP服务器对接来实现时间同步。
risk_level: ''
doc_source: ["网络部署","初始配置","UNC初始配置与调测","基础数据配置","配置NTP时间同步"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
网元可以同时从FusionStage和NTP服务器同步时间信息，这样当一路故障后，另一路仍然可以正常运行，可以保证时间同步的可靠性，如图1所示。**图1** 网元同时从FusionStage和外部NTP服务器同步时间信息* 从FusionStage同步时间：当FusionStage在“系统管理 > 系统配置 > 时间管理”页面时，将“支持夏令时时钟”设置为“是”，同时在“应用管理 > MML”执行**SET TZ**命令，将“是否执行夏令时”设置为“YES(是)”，并将相关时区和夏令时参数和FusionStage设置一致。* 从NTP服务器同步时间：对于计费类网元（UAMF、USMF），直接配置和NTP服务器对接即可。对于非计费类网元（NRF、NSSF、SMSF），需要和OMC对接，OMC最终和NTP服务器对接来实现时间同步。

## 必备事项
前提条件

* 已登录网元OM Portal。
* 已获取NTP服务器信息。
* 已获取FusionStage夏令时配置信息。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_ntpsvr_list:
      type: items
      properties:
        SVRNAME:
          name: 'NTP服务器名'
          type: string
          maxLength: 32
          required: true
          description: '* 对于计费类网元（UAMF、USMF），直接配置NTP服务器的IP地址。 * 对于非计费类网元（NRF、NSSF、SMSF）则配置OMC的IP地址。'
          data_source: '从对端NTP服务器获取'
          pattern: ''
          default: ''
        IPTYPE:
          name: 'IP地址类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: IPV4
        IPADDRESS:
          name: 'IPV4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PROTOCOLVERSION:
          name: 'NTP协议版本'
          type: string
          enum:
          - NTPV4
          - NTPV3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: NTPV4
        AUTHFLAG:
          name: '身份验证标志'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: YES
        KEYID:
          name: '身份验证密钥号'
          type: integer
          minimum: 1
          maximum: 65533
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SHASTRING:
          name: '密钥类型'
          type: string
          enum:
          - SHA256
          - SHA1
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: SHA256
        KEYSTRING:
          name: '密钥串'
          type: string
          minLength: 40
          maxLength: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPADDRESS6:
          name: 'IPV6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_tz_list:
      type: items
      properties:
        TF:
          name: '标准时类型'
          type: string
          enum:
          - GMT
          - UTC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: GMT
        TZONE:
          name: '时区'
          type: string
          enum:
          - E0000
          - E0100
          - E0200
          - E0300
          - E0330
          - E0400
          - E0430
          - E0500
          - E0530
          - E0545
          - E0600
          - E0630
          - E0700
          - E0800
          - E0845
          - E0900
          - E0930
          - E1000
          - E1030
          - E1100
          - E1200
          - E1300
          - E1400
          - W0100
          - W0200
          - W0300
          - W0330
          - W0400
          - W0500
          - W0600
          - W0700
          - W0800
          - W0900
          - W0930
          - W1000
          - W1100
          required: false
          description: '-'
          data_source: '与FusionStage保持一致'
          pattern: ''
          default: ''
        DST:
          name: '是否执行夏令时'
          type: string
          enum:
          - NO
          - YES
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SM:
          name: '日期输入方式'
          type: string
          enum:
          - Date
          - Week
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SMONTH:
          name: '开始月份'
          type: string
          enum:
          - Jan
          - Feb
          - Mar
          - Apr
          - May
          - Jun
          - Jul
          - Aug
          - Sep
          - Oct
          - Nov
          - Dec
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SDAY:
          name: '开始日'
          type: integer
          minimum: 1
          maximum: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ST:
          name: '开始时间'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'HH&MM'
        EMONTH:
          name: '结束月份'
          type: string
          enum:
          - Jan
          - Feb
          - Mar
          - Apr
          - May
          - Jun
          - Jul
          - Aug
          - Sep
          - Oct
          - Nov
          - Dec
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EDAY:
          name: '结束日'
          type: integer
          minimum: 1
          maximum: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ET:
          name: '结束时间'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'HH&MM'
        TO:
          name: '时间偏移量（分钟）'
          type: integer
          minimum: 1
          maximum: 120
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EWEEK:
          name: '结束星期'
          type: string
          enum:
          - Sun
          - Mon
          - Tue
          - Wed
          - Thu
          - Fri
          - Sat
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EWSEQ:
          name: '结束的第几个星期'
          type: string
          enum:
          - FIRST
          - SECOND
          - THIRD
          - FOURTH
          - LAST
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SWEEK:
          name: '开始星期'
          type: string
          enum:
          - Sun
          - Mon
          - Tue
          - Wed
          - Thu
          - Fri
          - Sat
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SWSEQ:
          name: '开始的第几个星期'
          type: string
          enum:
          - FIRST
          - SECOND
          - THIRD
          - FOURTH
          - LAST
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TZONEU:
          name: '时区'
          type: string
          enum:
          - E0000
          - E0100
          - E0200
          - E0300
          - E0330
          - E0400
          - E0430
          - E0500
          - E0530
          - E0545
          - E0600
          - E0630
          - E0700
          - E0800
          - E0845
          - E0900
          - E0930
          - E1000
          - E1030
          - E1100
          - E1200
          - E1300
          - E1400
          - W0100
          - W0200
          - W0300
          - W0330
          - W0400
          - W0500
          - W0600
          - W0700
          - W0800
          - W0900
          - W0930
          - W1000
          - W1100
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_ntpsvr_list:
    - SVRNAME: 'NTPServer1'
      IPTYPE: IPV4
      IPADDRESS: '10.10.10.100'
      PROTOCOLVERSION: NTPV4
      AUTHFLAG: YES
      KEYID: 1
      SHASTRING: SHA256
      KEYSTRING: '*****'
      IPADDRESS6: ''
    set_tz_list:
    - TF: GMT
      TZONE: E0000
      DST: YES
      SM: Date
      SMONTH: Jun
      SDAY: 1
      ST: '00&00'
      EMONTH: Sep
      EDAY: 25
      ET: '18&00'
      TO: 3
      EWEEK: ''
      EWSEQ: ''
      SWEEK: ''
      SWSEQ: ''
      TZONEU: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 登录网元OM Portal，选择“应用管理 > MML”。

### 2 执行**ADD NTPSVR**配置对接NTP服务器信息。

```jinja2
{%- for item in add_ntpsvr_list -%}
    ADD NTPSVR:
    {#- --- 必选参数 --- -#}
    SVRNAME="{{item.SVRNAME}}",
    IPTYPE={{item.IPTYPE}},
    PROTOCOLVERSION={{item.PROTOCOLVERSION}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPTYPE=IPV4 时必选 --- -#}
    {%- if item.IPTYPE == 'IPV4' -%}
        IPADDRESS="{{item.IPADDRESS}}",
    {%- endif -%}
    {#- --- 条件必选：PROTOCOLVERSION=NTPV4 时必选 --- -#}
    {%- if item.PROTOCOLVERSION == 'NTPV4' -%}
        AUTHFLAG={{item.AUTHFLAG}},
    {%- endif -%}
    {#- --- 条件必选：AUTHFLAG=YES 时必选 --- -#}
    {%- if item.AUTHFLAG == 'YES' -%}
        KEYID={{item.KEYID}},
    {%- endif -%}
    {#- --- 条件必选：AUTHFLAG=YES 时必选 --- -#}
    {%- if item.AUTHFLAG == 'YES' -%}
        SHASTRING={{item.SHASTRING}},
    {%- endif -%}
    {#- --- 条件必选：AUTHFLAG=YES 时必选 --- -#}
    {%- if item.AUTHFLAG == 'YES' -%}
        KEYSTRING="{{item.KEYSTRING}}",
    {%- endif -%}
    {#- --- 条件必选：IPTYPE=IPV6 时必选 --- -#}
    {%- if item.IPTYPE == 'IPV6' -%}
        IPADDRESS6="{{item.IPADDRESS6}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 执行**SET TZ**配置时区和夏令时信息与FusionStage一致。

```jinja2
{%- for item in set_tz_list -%}
    SET TZ:
    {#- --- 必选参数 --- -#}
    DST={{item.DST}},
    {#- --- 可选参数 --- -#}
    {%- if item.TF is not none -%}
        TF={{item.TF}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：TF=GMT 时必选 --- -#}
    {%- if item.TF == 'GMT' -%}
        TZONE={{item.TZONE}},
    {%- endif -%}
    {#- --- 条件必选：DST=YES 时必选 --- -#}
    {%- if item.DST == 'YES' -%}
        SM={{item.SM}},
    {%- endif -%}
    {#- --- 条件必选：SM=Date/Week 时必选 --- -#}
    {%- if item.SM in ['Date', 'Week'] -%}
        SMONTH={{item.SMONTH}},
    {%- endif -%}
    {#- --- 条件必选：SM=Date 时必选 --- -#}
    {%- if item.SM == 'Date' -%}
        SDAY={{item.SDAY}},
    {%- endif -%}
    {#- --- 条件必选：SM=Date/Week 时必选 --- -#}
    {%- if item.SM in ['Date', 'Week'] -%}
        ST={{item.ST}},
    {%- endif -%}
    {#- --- 条件必选：SM=Date/Week 时必选 --- -#}
    {%- if item.SM in ['Date', 'Week'] -%}
        EMONTH={{item.EMONTH}},
    {%- endif -%}
    {#- --- 条件必选：SM=Date 时必选 --- -#}
    {%- if item.SM == 'Date' -%}
        EDAY={{item.EDAY}},
    {%- endif -%}
    {#- --- 条件必选：SM=Date/Week 时必选 --- -#}
    {%- if item.SM in ['Date', 'Week'] -%}
        ET={{item.ET}},
    {%- endif -%}
    {#- --- 条件必选：SM=Date/Week 时必选 --- -#}
    {%- if item.SM in ['Date', 'Week'] -%}
        TO={{item.TO}},
    {%- endif -%}
    {#- --- 条件必选：SM=Week 时必选 --- -#}
    {%- if item.SM == 'Week' -%}
        EWEEK={{item.EWEEK}},
    {%- endif -%}
    {#- --- 条件必选：SM=Week 时必选 --- -#}
    {%- if item.SM == 'Week' -%}
        EWSEQ={{item.EWSEQ}},
    {%- endif -%}
    {#- --- 条件必选：SM=Week 时必选 --- -#}
    {%- if item.SM == 'Week' -%}
        SWEEK={{item.SWEEK}},
    {%- endif -%}
    {#- --- 条件必选：SM=Week 时必选 --- -#}
    {%- if item.SM == 'Week' -%}
        SWSEQ={{item.SWSEQ}},
    {%- endif -%}
    {#- --- 条件必选：TF=UTC 时必选 --- -#}
    {%- if item.TF == 'UTC' -%}
        TZONEU={{item.TZONEU}},
    {%- endif -%}
    ;
{%- endfor -%}
```

