---
id: ''
name: 公共参数配置
ne_type: UEG
type: feature
description: 本页面涉及的公共参数均有默认值，请根据网设LLD规划的值进行调整。  网设LLD中未描述的参数，一般情况下是使用系统初始值。如有疑问，请联系华为技术支持工程师。对于使用系统初始值的参数，为了避免被误修改，建议参考本页面重新配置。
tags: []
risk_level: ''
doc_source:
  - ["网络部署","园区入驻+地市共享（连接+计算）","5GC toB 部署边缘站点（站点为“风筝S”，带计算）","UEG初始配置（风筝S）","初始配置与调测（MPF）","初始配置与调测（MPF，非SDN）","参考：详细配置指导","基础数据配置","公共参数配置"]
  - ["网络部署","园区入驻+地市共享（连接+计算）","5GC toB 部署边缘站点（站点为“风筝S”，带计算）","UEG初始配置（风筝S）","初始配置与调测（MPF）","初始配置与调测（MPF，SDN）","参考：详细配置指导","基础数据配置","公共参数配置"]
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
    set_ipv6fragplcy_list:
    - INNERIPV4FRAGPLCY: OUTERFRAG
      INNERIPV6FRAGPLCY: OUTERFRAG
    set_tz_list:
    - TZONE: E0800
      DST: NO
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 设置IPv6报文分片策略。

### “INNERIPV4FRAGPLCY”参数系统初始值为“OUTERFRAG”；“INNERIPV6FRAGPLCY”参数系统初始值为“TOOBIG\_PKTDROP”。

### “INNERIPV6FRAGPLCY”参数值为“TOOBIG\_PKTDROP”时，若MPF处理并封装报文后，报文长度大于MTU值，则丢弃该报文，并回复Too big报文。MPF封装后的报文长度大于MTU值的场景，需要执行如下脚本，由MPF对报文做外层IPv6分片，避免业务异常。

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

### 2 配置时区。

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

