---
id: ''
name: 公共参数配置
ne_type: UEG
type: feature
description: 本页面涉及的公共参数均有默认值，请根据网设LLD规划的值进行调整。  网设LLD中未描述的参数，一般情况下是使用系统初始值。如有疑问，请联系华为技术支持工程师。对于使用系统初始值的参数，为了避免被误修改，建议参考本页面重新配置。
tags: []
risk_level: ''
doc_source:
  - ["网络部署","地市共享式（仅连接）","5GC toB 部署边缘站点（站点为“风筝S”，共享式）","UEG初始配置（风筝S）","参考：详细配置指导","基础数据配置","公共参数配置"]
  - ["网络部署","园区入驻+地市共享（连接+计算）","5GC toB 部署边缘站点（站点为“风筝S”，带计算）","UEG初始配置（风筝S）","初始配置与调测（共享式UPF）","初始配置与调测（共享式边缘UPF，非SDN）","参考：详细配置指导","基础数据配置","公共参数配置"]
  - ["网络部署","园区入驻+地市共享（连接+计算）","5GC toB 部署边缘站点（站点为“风筝S”，带计算）","UEG初始配置（风筝S）","初始配置与调测（共享式UPF）","初始配置与调测（共享式边缘UPF，SDN）","参考：详细配置指导","基础数据配置","公共参数配置"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本页面涉及的公共参数均有默认值，请根据网设LLD规划的值进行调整。网设LLD中未描述的参数，一般情况下是使用系统初始值。如有疑问，请联系华为技术支持工程师。对于使用系统初始值的参数，为了避免被误修改，建议参考本页面重新配置。

## 必备事项
前提条件

具备管理员权限的操作人员已经登录华为操作维护系统（登录MAE客户端或登录OM Portal）。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
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
          - E1245
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
          required: true
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
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 配置N4接口PFCP协议信令报文的DSCP值。

### 设置的DSCP值，用于UEG填充报文中的ToS字段。

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

### 2 配置UEG发送的UDP报文中是否携带CheckSum。

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

### 7 虚机容器场景，配置时区。

### 此处以东八区，不执行夏令时为例。

```jinja2
{%- for item in set_tz_list -%}
    SET TZ:
    {#- --- 必选参数 --- -#}
    TZONE={{item.TZONE}},
    DST={{item.DST}},
    ;
{%- endfor -%}
```

