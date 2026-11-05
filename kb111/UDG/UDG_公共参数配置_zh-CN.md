---
id: ''
name: 公共参数配置
ne_type: UDG
type: feature
description: 本页面涉及的公共参数均有默认值，请根据网设LLD规划的值进行调整。  网设LLD中未描述的参数，一般情况下是使用系统初始值。如有疑问，请联系华为技术支持工程师。对于使用系统初始值的参数，为了避免被误修改，建议参考本页面重新配置。
risk_level: ''
doc_source: ["网络部署","初始配置","UDG初始配置与调测","基础数据配置","公共参数配置"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本页面涉及的公共参数均有默认值，请根据网设LLD规划的值进行调整。网设LLD中未描述的参数，一般情况下是使用系统初始值。如有疑问，请联系华为技术支持工程师。对于使用系统初始值的参数，为了避免被误修改，建议参考本页面重新配置。

## 必备事项
前提条件

具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020/MAE客户端或登录OM Portal）。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_sigdscp_list:
      type: items
      properties:
        PROTOCOL:
          name: '信令协议'
          type: string
          enum:
          - GTP_SIGNALING
          - L2TP_SIGNALING
          - PFCP
          - PPP_SIGNALING
          - TM
          - SIP
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DSCPV:
          name: 'DSCP值'
          type: integer
          minimum: 0
          maximum: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_udpchecksum_list:
      type: items
      properties:
        UDPTYPE:
          name: 'UDP Type'
          type: string
          enum:
          - L2TP_CTRL
          - L2TP_DATA
          - PFCP
          - SIP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SWITCH:
          name: 'Checksum 开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_srvcommonpara_list:
      type: items
      properties:
        FDMAXNUM:
          name: '用户session的五元组节点最大数量'
          type: integer
          minimum: 1
          maximum: 2550
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_qoscar_list:
      type: items
      properties:
        USERTYPE:
          name: '用户漫游类型'
          type: string
          enum:
          - HOME
          - ROAMING
          - VISITING
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ULRAT:
          name: '上行RAT类型'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DLRAT:
          name: '下行RAT类型'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_ipv6fragplcy_list:
      type: items
      properties:
        INNERIPV4FRAGPLCY:
          name: '内层为IPv4的分片策略'
          type: string
          enum:
          - INNERFRAG
          - OUTERFRAG
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        INNERIPV6FRAGPLCY:
          name: '内层为IPv6的分片策略'
          type: string
          enum:
          - OUTERFRAG
          - TOOBIG_PKTDROP
          - TOOBIG_PKTFWD
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_cpteidualloc_list:
      type: items
      properties:
        SWITCH:
          name: '开关标识'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_tz_list:
      type: items
      properties:
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
          description: ''
          data_source: ''
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
    set_antifraud_list:
      type: items
      properties:
        ISNULLRECEN:
          name: '空记录DNS防欺诈开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ISTEXTEN:
          name: '文本记录DNS防欺诈开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ISHEURISTICEN:
          name: '启发式DNS防欺诈开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FUIAFSWITCH:
          name: 'FUI防欺诈开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HTTPAFSWITCH:
          name: 'HTTP防欺诈总开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        URLREDAFSWITCH:
          name: 'URL重定向防欺诈开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_fwdpara_list:
      type: items
      properties:
        RSTIME:
          name: '报文重组超时时长（秒）'
          type: integer
          minimum: 2
          maximum: 60
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6RSTIME:
          name: 'IPv6报文重组超时时长（秒）'
          type: integer
          minimum: 2
          maximum: 60
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FWDSWITCH:
          name: '分片报文转板开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_headenglbpara_list:
      type: items
      properties:
        RC4KEYMD5EN:
          name: 'RC4的密钥MD5 Hash使能标识'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MSISDNMINLEN:
          name: 'MSISDN字段最小长度'
          type: integer
          minimum: 0
          maximum: 17
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RSANODEAGETIME:
          name: 'RSA加密节点老化时间（分）'
          type: integer
          minimum: 1
          maximum: 1440
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RSAEXPIREDALM:
          name: 'RSA证书过期告警'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RSACERTEXPALMDAYS:
          name: 'RSA证书过期告警提前天数'
          type: integer
          minimum: 0
          maximum: 365
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HEADENSALTTYPE:
          name: '头增强插入盐值生成方法类型'
          type: string
          enum:
          - RANDNUM
          - TIMESTAMP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_msfaultalarm_list:
      type: items
      properties:
        SUPPRESSENABLE:
          name: '告警抑制使能开关'
          type: string
          enum:
          - TRUE
          - FALSE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SUPPRESSTIME:
          name: '告警抑制时间(秒)'
          type: integer
          minimum: 1
          maximum: 42949672
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 300
  examples:
    set_sigdscp_list:
    - PROTOCOL: PFCP
      DSCPV: 46
    set_udpchecksum_list:
    - UDPTYPE: PFCP
      SWITCH: ENABLE
    set_srvcommonpara_list:
    - FDMAXNUM: 1000
    set_qoscar_list:
    - USERTYPE: HOME
      ULRAT: eutran-1&eutran_nb_iot-1&gan-1&geran-1&hspae-1&lte_m-1&nr-1&unknown-1&utran-1&wlan-1
      DLRAT: eutran-1&eutran_nb_iot-1&gan-1&geran-1&hspae-1&nr-1&unknown-1&utran-1&wlan-1
    - USERTYPE: ROAMING
      ULRAT: eutran-1&eutran_nb_iot-1&gan-1&geran-1&hspae-1&lte_m-1&nr-1&unknown-1&utran-1&wlan-1
      DLRAT: eutran-1&eutran_nb_iot-1&gan-1&geran-1&hspae-1&nr-1&unknown-1&utran-1&wlan-1
    - USERTYPE: VISITING
      ULRAT: eutran-1&eutran_nb_iot-1&gan-1&geran-1&hspae-1&lte_m-1&nr-1&unknown-1&utran-1&wlan-1
      DLRAT: eutran-1&eutran_nb_iot-1&gan-1&geran-1&hspae-1&nr-1&unknown-1&utran-1&wlan-1
    set_ipv6fragplcy_list:
    - INNERIPV4FRAGPLCY: OUTERFRAG
      INNERIPV6FRAGPLCY: OUTERFRAG
    set_cpteidualloc_list:
    - SWITCH: DISABLE
    set_tz_list:
    - TZONE: E0800
      DST: NO
      TF: GMT
      SM: ''
    set_antifraud_list:
    - ISNULLRECEN: DISABLE
      ISTEXTEN: DISABLE
      ISHEURISTICEN: DISABLE
      FUIAFSWITCH: DISABLE
      HTTPAFSWITCH: ENABLE
      URLREDAFSWITCH: DISABLE
    set_fwdpara_list:
    - RSTIME: 6
      IPV6RSTIME: 6
      FWDSWITCH: ON
    set_headenglbpara_list:
    - RC4KEYMD5EN: DISABLE
      MSISDNMINLEN: 0
      RSANODEAGETIME: 10
      RSAEXPIREDALM: ENABLE
      RSACERTEXPALMDAYS: 30
      HEADENSALTTYPE: TIMESTAMP
    set_msfaultalarm_list:
    - SUPPRESSENABLE: TRUE
      SUPPRESSTIME: 300
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置N4接口PFCP协议信令报文的DSCP值。

### 设置的DSCP值，用于UDG填充报文中的ToS字段。

### 系统初始值为“46”。

```jinja2
{%- for item in set_sigdscp_list -%}
    SET SIGDSCP:
    {#- --- 必选参数 --- -#}
    PROTOCOL={{item.PROTOCOL}},
    DSCPV={{item.DSCPV}},
    ;
{%- endfor -%}
```

### 2 配置UDG发送的UDP报文中是否携带CheckSum。

### IPv6报文时须设置为“ENABLE”。此处以携带CheckSum为例。

### 系统初始值为“DISABLE”。

```jinja2
{%- for item in set_udpchecksum_list -%}
    SET UDPCHECKSUM:
    {#- --- 可选参数 --- -#}
    {%- if item.UDPTYPE is not none -%}
        UDPTYPE={{item.UDPTYPE}},
    {%- endif -%}
    {%- if item.SWITCH is not none -%}
        SWITCH={{item.SWITCH}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 设置每用户的最大五元组个数。

### 此处以每用户的最大五元组个数为1000且其他参数使用系统初始值为例。

### 系统初始值为“600”。

```jinja2
{%- for item in set_srvcommonpara_list -%}
    SET SRVCOMMONPARA:
    {#- --- 可选参数 --- -#}
    {%- if item.FDMAXNUM is not none -%}
        FDMAXNUM={{item.FDMAXNUM}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 设置QoS CAR。

### RAT类型后的-1代表使能这个RAT类型用户的QoS CAR功能，-0代表不使能。

### 系统初始值为“NULL”，表示不使能所有RAT类型。

#### 4.1 //配置本地用户的上下行CAR功能。

```jinja2
{%- for item in set_qoscar_list -%}
    SET QOSCAR:
    {#- --- 必选参数 --- -#}
    USERTYPE={{item.USERTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.ULRAT is not none -%}
        ULRAT={{item.ULRAT}},
    {%- endif -%}
    {%- if item.DLRAT is not none -%}
        DLRAT={{item.DLRAT}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 设置IPv6报文分片策略。

### “INNERIPV4FRAGPLCY”参数系统初始值为“OUTERFRAG”；“INNERIPV6FRAGPLCY”参数系统初始值为“TOOBIG\_PKTDROP”。

### “INNERIPV6FRAGPLCY”参数值为“TOOBIG\_PKTDROP”时，若UPF处理并封装报文后，报文长度大于MTU值，则丢弃该报文，并回复Too big报文。UPF封装后的报文长度大于MTU值的场景，需要执行如下脚本，由UPF对报文做外层IPv6分片，避免业务异常。

```jinja2
{%- for item in set_ipv6fragplcy_list -%}
    SET IPV6FRAGPLCY:
    {#- --- 可选参数 --- -#}
    {%- if item.INNERIPV4FRAGPLCY is not none -%}
        INNERIPV4FRAGPLCY={{item.INNERIPV4FRAGPLCY}},
    {%- endif -%}
    {%- if item.INNERIPV6FRAGPLCY is not none -%}
        INNERIPV6FRAGPLCY={{item.INNERIPV6FRAGPLCY}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 6 配置用户面支持分配F-TEID。

### 不同CP分配给同一个UP的TEID-U可能重复，因此需要将“SWITCH”设置为“DISABLE”，由用户面分配TEID-U。

### 系统初始值为“DISABLE”。

```jinja2
{%- for item in set_cpteidualloc_list -%}
    SET CPTEIDUALLOC:
    {#- --- 必选参数 --- -#}
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 7 配置时区。

### 此处以东八区，不执行夏令时为例。

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
    ;
{%- endfor -%}
```

### 8 设置防欺诈配置。

### 此处以运营商不希望开启FUI防欺诈功能，希望开启HTTP防欺诈功能，其他参数为系统初始值为例。

```jinja2
{%- for item in set_antifraud_list -%}
    SET ANTIFRAUD:
    {#- --- 可选参数 --- -#}
    {%- if item.ISNULLRECEN is not none -%}
        ISNULLRECEN={{item.ISNULLRECEN}},
    {%- endif -%}
    {%- if item.ISTEXTEN is not none -%}
        ISTEXTEN={{item.ISTEXTEN}},
    {%- endif -%}
    {%- if item.ISHEURISTICEN is not none -%}
        ISHEURISTICEN={{item.ISHEURISTICEN}},
    {%- endif -%}
    {%- if item.FUIAFSWITCH is not none -%}
        FUIAFSWITCH={{item.FUIAFSWITCH}},
    {%- endif -%}
    {%- if item.HTTPAFSWITCH is not none -%}
        HTTPAFSWITCH={{item.HTTPAFSWITCH}},
    {%- endif -%}
    {%- if item.URLREDAFSWITCH is not none -%}
        URLREDAFSWITCH={{item.URLREDAFSWITCH}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 9 设置转发参数。

### 该命令属于高危命令，操作不当会导致业务故障，请谨慎使用并联系华为技术支持协助操作。

### 报文重组超时时长设置过小，分片可能不完整；设置过大，会降低设备的性能。

### 系统初始值为“3”。

```jinja2
{%- for item in set_fwdpara_list -%}
    SET FWDPARA:
    {#- --- 可选参数 --- -#}
    {%- if item.RSTIME is not none -%}
        RSTIME={{item.RSTIME}},
    {%- endif -%}
    {%- if item.IPV6RSTIME is not none -%}
        IPV6RSTIME={{item.IPV6RSTIME}},
    {%- endif -%}
    {%- if item.FWDSWITCH is not none -%}
        FWDSWITCH={{item.FWDSWITCH}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 10 设置头增强全局参数。

### 此处以“HEADENSALTTYPE”参数设置为“TIMESTAMP”，其他参数为系统初始值为例。

### “HEADENSALTTYPE”参数系统初始值为“RANDNUM”。

```jinja2
{%- for item in set_headenglbpara_list -%}
    SET HEADENGLBPARA:
    {#- --- 可选参数 --- -#}
    {%- if item.RC4KEYMD5EN is not none -%}
        RC4KEYMD5EN={{item.RC4KEYMD5EN}},
    {%- endif -%}
    {%- if item.MSISDNMINLEN is not none -%}
        MSISDNMINLEN={{item.MSISDNMINLEN}},
    {%- endif -%}
    {%- if item.RSANODEAGETIME is not none -%}
        RSANODEAGETIME={{item.RSANODEAGETIME}},
    {%- endif -%}
    {%- if item.RSAEXPIREDALM is not none -%}
        RSAEXPIREDALM={{item.RSAEXPIREDALM}},
    {%- endif -%}
    {%- if item.RSACERTEXPALMDAYS is not none -%}
        RSACERTEXPALMDAYS={{item.RSACERTEXPALMDAYS}},
    {%- endif -%}
    {%- if item.HEADENSALTTYPE is not none -%}
        HEADENSALTTYPE={{item.HEADENSALTTYPE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 11 设置告警开关。

### “SUPPRESSENABLE”参数系统初始值为“TRUE”；“SUPPRESSTIME”参数系统初始值为“300”。

```jinja2
{%- for item in set_msfaultalarm_list -%}
    SET MSFAULTALARM:
    {#- --- 必选参数 --- -#}
    SUPPRESSENABLE={{item.SUPPRESSENABLE}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：SUPPRESSENABLE=TRUE 时可选 --- -#}
    {%- if item.SUPPRESSENABLE == 'TRUE' -%}
        {%- if item.SUPPRESSTIME is not none -%}
            SUPPRESSTIME={{item.SUPPRESSTIME}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

