---
id: ''
name: 配置防攻击功能
ne_type: UEG
type: feature
description: 通过配置TCP/IP攻击防范、ARP攻击防范、CP-CAR、ACL、黑白名单、应用层联动等功能保护UEG。
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝S”，入驻式）","裸机容器模式","配置安全数据（风筝S）","安全配置建议","可选配置","网络安全配置","配置防攻击功能"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
通过配置TCP/IP攻击防范、ARP攻击防范、CP-CAR、ACL、黑白名单、应用层联动等功能保护UEG。

## 必备事项
前提条件

* 风筝S场景，请仔细阅读TCP/IP攻击防御、ARP攻击防御和防攻击。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_secpolicy_list:
      type: items
      properties:
        POLICYID:
          name: '安全策略编号'
          type: integer
          minimum: 1
          maximum: 30
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        DESCRIPTION:
          name: '策略描述'
          type: string
          maxLength: 64
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_secpolicyallpktvalue_list:
      type: items
      properties:
        SECPOLICYID:
          name: '安全策略编号'
          type: integer
          minimum: 1
          maximum: 30
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SECRATEVALUE:
          name: '上报速率值（pps）'
          type: integer
          minimum: 2000
          maximum: 20000
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_secpolicyallpktlevel_list:
      type: items
      properties:
        SECPOLICYID:
          name: '安全策略编号'
          type: integer
          minimum: 1
          maximum: 30
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SECRATELEVEL:
          name: '上报速率等级'
          type: string
          enum:
          - high
          - low
          - middle
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_secpolicycar_list:
      type: items
      properties:
        SECPOLICYID:
          name: '安全策略编号'
          type: integer
          minimum: 1
          maximum: 30
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SECPOLICYTYPE:
          name: '安全策略类型'
          type: string
          enum:
          - BlackList
          - Index
          - Protocol
          - Tcpip
          - UserFlow
          - WhiteList
          - WhiteListV6
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SUBTCPIPTYPE:
          name: '安全TCP/IP类型'
          type: string
          enum:
          - FRAGMENT
          - TCPSYN
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SECPOLICYCIR:
          name: '安全策略承诺信息速率'
          type: integer
          minimum: 0
          maximum: 1000000
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SECPOLICYCBS4SH:
          name: '安全策略承诺突发尺寸'
          type: integer
          minimum: 0
          maximum: 9000000
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SECMINPKTLEN:
          name: '安全最小包补偿长度'
          type: integer
          minimum: 64
          maximum: 9600
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 128
    add_secpolicyacl_list:
      type: items
      properties:
        SECPOLICYID:
          name: '安全策略编号'
          type: integer
          minimum: 1
          maximum: 30
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SECPOLICYTYPE:
          name: '安全策略类型'
          type: string
          enum:
          - BlackList
          - IPV6BlackList
          - IPV6UserFlow
          - IPV6WhiteList
          - UserFlow
          - WhiteList
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SECACLNUM:
          name: '安全ACL规则编号'
          type: integer
          minimum: 2000
          maximum: 3999
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SECPOLICYTYPEID:
          name: '安全策略类型编号'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_secpolicyproseq_list:
      type: items
      properties:
        SECPOLICYID:
          name: '安全策略编号'
          type: integer
          minimum: 1
          maximum: 30
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SECPROSEQWL:
          name: '安全白名单匹配顺序'
          type: string
          enum:
          - First
          - Second
          - Third
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SECPROSEQBL:
          name: '安全黑名单匹配顺序'
          type: string
          enum:
          - First
          - Second
          - Third
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SECPROSEQUF:
          name: '安全用户流匹配顺序'
          type: string
          enum:
          - First
          - Second
          - Third
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_secpolicyprio_list:
      type: items
      properties:
        SECPOLICYID:
          name: '安全策略号'
          type: integer
          minimum: 1
          maximum: 30
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SECPOLICYTYPE:
          name: '安全策略类型'
          type: string
          enum:
          - BlackList
          - Index
          - Protocol
          - Tcpip
          - UserFlow
          - WhiteList
          - WhiteListV6
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SUBTCPIPTYPE:
          name: '安全TCP/IP类型'
          type: string
          enum:
          - FRAGMENT
          - TCPSYN
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SECPRIORITY:
          name: '安全优先级'
          type: string
          enum:
          - high
          - low
          - middle
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SECPOLICYTYPEID:
          name: '安全策略类型号'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SUBPROTOTYPE:
          name: '安全协议类型'
          type: string
          enum:
          - arp
          - arp-miss
          - bfd
          - bgp
          - bgpv6
          - dhcp
          - dhcpv6
          - gre
          - icmp
          - icmpv6
          - igmp
          - ipv4-mc-fib-miss
          - ipv4-reserved-mc
          - ipv6-nd-miss
          - ipv6-ndh-miss
          - ipv6-too-big
          - ldp
          - mld
          - na
          - ns
          - ospf
          - ospfv3
          - pim
          - ra
          - rs
          - ssh_client
          - ssh_server
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_secpolicyalarm_list:
      type: items
      properties:
        SECPOLICYID:
          name: '安全策略编号'
          type: integer
          minimum: 1
          maximum: 30
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SECPOLICYTYPE:
          name: '安全策略类型'
          type: string
          enum:
          - APP
          - BlackList
          - Index
          - Tcpip
          - TotalPkt
          - Urpf
          - UserFlow
          - WhiteList
          - WhiteListV6
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SECALARMFLAG:
          name: '安全告警使能'
          type: string
          enum:
          - TRUE
          - FALSE
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SECALARMTHLD:
          name: '安全告警阈值'
          type: integer
          minimum: 1
          maximum: 1000000
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SECALARMINT:
          name: '安全告警时间间隔（秒）'
          type: integer
          minimum: 60
          maximum: 3600
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SECPOLICYTYPEID:
          name: '安全策略类型编号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_secdevurpf_list:
      type: items
      properties:
        SECPOLICYID:
          name: '策略编号'
          type: integer
          minimum: 1
          maximum: 30
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SECURPFLOOSETYPE:
          name: '安全URPF检查类型'
          type: string
          enum:
          - loose
          - strict
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SECENABLEDEFAULTROUTE:
          name: '是否允许缺省路由'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SECURPFENABLE:
          name: '是否允许URPF'
          type: string
          enum:
          - FALSE
          - TRUE
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_secpolicyswitch_list:
      type: items
      properties:
        SECPOLICYID:
          name: '安全策略编号'
          type: integer
          minimum: 1
          maximum: 30
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SECPOLICYTYPE:
          name: '安全策略类型'
          type: string
          enum:
          - APP
          - BlackList
          - Tcpip
          - WhiteList
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SECPOLICYENABLE:
          name: '安全策略使能标记'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SECPOLICYTYPEID:
          name: '安全策略类型编号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SUBTCPIPTYPE:
          name: 'TCP/IP防攻击类型'
          type: string
          enum:
          - ABNORMAL
          - FRAGMENT
          - TCPSYN
          - UDPFLOOD
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_secpolicyapplnk_list:
      type: items
      properties:
        SECPOLICYID:
          name: '策略编号'
          type: integer
          minimum: 1
          maximum: 30
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SECDFTACTION:
          name: '默认处理方式'
          type: string
          enum:
          - Drop
          - Min_to_cp
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_secpolicycfg_list:
      type: items
      properties:
        POLICYID:
          name: '安全策略编号'
          type: integer
          minimum: 1
          maximum: 30
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        RUNAME:
          name: 'RU名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_secarpgrat_list:
      type: items
      properties:
        IFNAME:
          name: '接口名称'
          type: string
          maxLength: 47
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SECENABLE:
          name: '使能标记'
          type: string
          enum:
          - TRUE
          - FALSE
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_secarp_list:
      type: items
      properties:
        RUNAME:
          name: 'RU名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        FASTRLYEN:
          name: '使能标记'
          type: string
          enum:
          - TRUE
          - FALSE
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_secicmpreply_list:
      type: items
      properties:
        RUNAME:
          name: 'RU名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        FASTRLYEN:
          name: '使能标记'
          type: string
          enum:
          - TRUE
          - FALSE
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_secnd_list:
      type: items
      properties:
        FASTRLYEN:
          name: '使能标记'
          type: string
          enum:
          - TRUE
          - FALSE
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    add_secpolicy_list:
    - POLICYID: 1
      DESCRIPTION: 'policyabc'
    set_secpolicyallpktvalue_list:
    - SECPOLICYID: 1
      SECRATEVALUE: 8000
    set_secpolicyallpktlevel_list:
    - SECPOLICYID: 1
      SECRATELEVEL: low
    add_secpolicycar_list:
    - SECPOLICYID: 1
      SECPOLICYTYPE: Tcpip
      SUBTCPIPTYPE: TCPSYN
      SECPOLICYCIR: 2333
      SECPOLICYCBS4SH: 6000
      SECMINPKTLEN: 128
    add_secpolicyacl_list:
    - SECPOLICYID: 1
      SECPOLICYTYPE: whitelist
      SECACLNUM: 2000
      SECPOLICYTYPEID: 1
    add_secpolicyproseq_list:
    - SECPOLICYID: 1
      SECPROSEQWL: Third
      SECPROSEQBL: Second
      SECPROSEQUF: First
    set_secpolicyprio_list:
    - SECPOLICYID: 1
      SECPOLICYTYPE: Tcpip
      SUBTCPIPTYPE: TCPSYN
      SECPRIORITY: low
      SECPOLICYTYPEID: 10
      SUBPROTOTYPE: bfd
    add_secpolicyalarm_list:
    - SECPOLICYID: 1
      SECPOLICYTYPE: Tcpip
      SECALARMFLAG: TRUE
      SECALARMTHLD: 1
      SECALARMINT: 60
      SECPOLICYTYPEID: 1
    set_secdevurpf_list:
    - SECPOLICYID: 1
      SECURPFLOOSETYPE: strict
      SECENABLEDEFAULTROUTE: TRUE
      SECURPFENABLE: TRUE
    set_secpolicyswitch_list:
    - SECPOLICYID: 1
      SECPOLICYTYPE: Tcpip
      SECPOLICYENABLE: TRUE
      SECPOLICYTYPEID: 32
      SUBTCPIPTYPE: TCPSYN
    set_secpolicyapplnk_list:
    - SECPOLICYID: 1
      SECDFTACTION: Min_to_cp
    add_secpolicycfg_list:
    - POLICYID: 1
      RUNAME: 'VNODE_VNRS_VNFC_IPU_0064'
    set_secarpgrat_list:
    - IFNAME: 'Ethernet64/0/2'
      SECENABLE: TRUE
    set_secarp_list:
    - RUNAME: 'VNODE_VNRS_VNFC_IPU_0064'
      FASTRLYEN: TRUE
    set_secicmpreply_list:
    - RUNAME: 'VNODE_VNRS_VNFC_IPU_0064'
      FASTRLYEN: TRUE
    set_secnd_list:
    - FASTRLYEN: TRUE
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 创建防攻击策略。

### 在“MML命令行-UEG”窗口上执行：

```jinja2
{%- for item in add_secpolicy_list -%}
    ADD SECPOLICY:
    {#- --- 必选参数 --- -#}
    POLICYID={{item.POLICYID}},
    {#- --- 可选参数 --- -#}
    {%- if item.DESCRIPTION is not none -%}
        DESCRIPTION="{{item.DESCRIPTION}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 配置防攻击策略参数

#### 2.1 配置上送报文总体速率值和速率等级。

#### 在“MML命令行-UEG”窗口上执行：

```jinja2
{%- for item in set_secpolicyallpktvalue_list -%}
    SET SECPOLICYALLPKTVALUE:
    {#- --- 必选参数 --- -#}
    SECPOLICYID={{item.SECPOLICYID}},
    SECRATEVALUE={{item.SECRATEVALUE}},
    ;
{%- endfor -%}
```

```jinja2
{%- for item in set_secpolicyallpktlevel_list -%}
    SET SECPOLICYALLPKTLEVEL:
    {#- --- 必选参数 --- -#}
    SECPOLICYID={{item.SECPOLICYID}},
    SECRATELEVEL={{item.SECRATELEVEL}},
    ;
{%- endfor -%}
```

#### 2.2 增加安全防攻击CAR规则

#### 在“MML命令行-UEG”窗口上执行：

```jinja2
{%- for item in add_secpolicycar_list -%}
    ADD SECPOLICYCAR:
    {#- --- 必选参数 --- -#}
    SECPOLICYID={{item.SECPOLICYID}},
    SECPOLICYTYPE={{item.SECPOLICYTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.SECPOLICYCIR is not none -%}
        SECPOLICYCIR={{item.SECPOLICYCIR}},
    {%- endif -%}
    {%- if item.SECPOLICYCBS4SH is not none -%}
        SECPOLICYCBS4SH={{item.SECPOLICYCBS4SH}},
    {%- endif -%}
    {%- if item.SECMINPKTLEN is not none -%}
        SECMINPKTLEN={{item.SECMINPKTLEN}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：SECPOLICYTYPE=Tcpip 时必选 --- -#}
    {%- if item.SECPOLICYTYPE == 'Tcpip' -%}
        SUBTCPIPTYPE={{item.SUBTCPIPTYPE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 只有SECPOLICYTYPE=Tcpip的时候SUBTCPIPTYPE才有意义。

#### 2.3 增加安全策略ACL规则

#### 在“MML命令行-UEG”窗口上执行：

```jinja2
{%- for item in add_secpolicyacl_list -%}
    ADD SECPOLICYACL:
    {#- --- 必选参数 --- -#}
    SECPOLICYID={{item.SECPOLICYID}},
    SECPOLICYTYPE={{item.SECPOLICYTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：SECPOLICYTYPE=WhiteList/BlackList/IPV6BlackList/IPV6WhiteList/UserFlow/IPV6UserFlow 时必选 --- -#}
    {%- if item.SECPOLICYTYPE in ['WhiteList', 'BlackList', 'IPV6BlackList', 'IPV6WhiteList', 'UserFlow', 'IPV6UserFlow'] -%}
        SECACLNUM={{item.SECACLNUM}},
    {%- endif -%}
    {#- --- 条件必选：SECPOLICYTYPE=UserFlow/IPV6UserFlow 时必选 --- -#}
    {%- if item.SECPOLICYTYPE in ['UserFlow', 'IPV6UserFlow'] -%}
        SECPOLICYTYPEID={{item.SECPOLICYTYPEID}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.4 配置安全策略匹配顺序

#### 在“MML命令行-UEG”窗口上执行：

```jinja2
{%- for item in add_secpolicyproseq_list -%}
    ADD SECPOLICYPROSEQ:
    {#- --- 必选参数 --- -#}
    SECPOLICYID={{item.SECPOLICYID}},
    SECPROSEQWL={{item.SECPROSEQWL}},
    SECPROSEQBL={{item.SECPROSEQBL}},
    SECPROSEQUF={{item.SECPROSEQUF}},
    ;
{%- endfor -%}
```

#### 2.5 配置报文上送优先级

#### 在“MML命令行-UEG”窗口上执行：

```jinja2
{%- for item in set_secpolicyprio_list -%}
    SET SECPOLICYPRIO:
    {#- --- 必选参数 --- -#}
    SECPOLICYID={{item.SECPOLICYID}},
    SECPOLICYTYPE={{item.SECPOLICYTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：SECPOLICYTYPE=Tcpip 时必选 --- -#}
    {%- if item.SECPOLICYTYPE == 'Tcpip' -%}
        SUBTCPIPTYPE={{item.SUBTCPIPTYPE}},
    {%- endif -%}
    {#- --- 条件必选：SECPOLICYTYPE=Protocol/Tcpip/UserFlow/WhiteList/BlackList/WhiteListV6/Index 时必选 --- -#}
    {%- if item.SECPOLICYTYPE in ['Protocol', 'Tcpip', 'UserFlow', 'WhiteList', 'BlackList', 'WhiteListV6', 'Index'] -%}
        SECPRIORITY={{item.SECPRIORITY}},
    {%- endif -%}
    {#- --- 条件必选：SECPOLICYTYPE=Protocol 时必选 --- -#}
    {%- if item.SECPOLICYTYPE == 'Protocol' -%}
        SUBPROTOTYPE={{item.SUBPROTOTYPE}},
    {%- endif -%}
    {#- --- 条件必选：SECPOLICYTYPE=UserFlow/Index 时必选 --- -#}
    {%- if item.SECPOLICYTYPE in ['UserFlow', 'Index'] -%}
        SECPOLICYTYPEID={{item.SECPOLICYTYPEID}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.6 增加安全策略告警

#### 在“MML命令行-UEG”窗口上执行：

```jinja2
{%- for item in add_secpolicyalarm_list -%}
    ADD SECPOLICYALARM:
    {#- --- 必选参数 --- -#}
    SECPOLICYID={{item.SECPOLICYID}},
    SECPOLICYTYPE={{item.SECPOLICYTYPE}},
    SECALARMFLAG={{item.SECALARMFLAG}},
    SECALARMTHLD={{item.SECALARMTHLD}},
    SECALARMINT={{item.SECALARMINT}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：SECPOLICYTYPE=Index/UserFlow 时必选 --- -#}
    {%- if item.SECPOLICYTYPE in ['Index', 'UserFlow'] -%}
        SECPOLICYTYPEID={{item.SECPOLICYTYPEID}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.7 使能设备URPF

#### 在“MML命令行-UEG”窗口上执行：

```jinja2
{%- for item in set_secdevurpf_list -%}
    SET SECDEVURPF:
    {#- --- 必选参数 --- -#}
    SECPOLICYID={{item.SECPOLICYID}},
    SECURPFENABLE={{item.SECURPFENABLE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：SECURPFENABLE=TRUE 时必选 --- -#}
    {%- if item.SECURPFENABLE == 'TRUE' -%}
        SECURPFLOOSETYPE={{item.SECURPFLOOSETYPE}},
    {%- endif -%}
    {#- --- 条件必选：SECURPFLOOSETYPE=strict 时必选 --- -#}
    {%- if item.SECURPFLOOSETYPE == 'strict' -%}
        SECENABLEDEFAULTROUTE={{item.SECENABLEDEFAULTROUTE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.8 使能非法报文以及黑名单、白名单防御机制

#### 在“MML命令行-UEG”窗口上执行：

```jinja2
{%- for item in set_secpolicyswitch_list -%}
    SET SECPOLICYSWITCH:
    {#- --- 必选参数 --- -#}
    SECPOLICYID={{item.SECPOLICYID}},
    SECPOLICYTYPE={{item.SECPOLICYTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：SECPOLICYTYPE=Tcpip/WhiteList/BlackList/APP 时必选 --- -#}
    {%- if item.SECPOLICYTYPE in ['Tcpip', 'WhiteList', 'BlackList', 'APP'] -%}
        SECPOLICYENABLE={{item.SECPOLICYENABLE}},
    {%- endif -%}
    {#- --- 条件必选：SECPOLICYTYPE=Tcpip/WhiteList/BlackList/APP 时必选 --- -#}
    {%- if item.SECPOLICYTYPE in ['Tcpip', 'WhiteList', 'BlackList', 'APP'] -%}
        SECPOLICYTYPEID={{item.SECPOLICYTYPEID}},
    {%- endif -%}
    {#- --- 条件必选：SECPOLICYTYPE=Tcpip 时必选 --- -#}
    {%- if item.SECPOLICYTYPE == 'Tcpip' -%}
        SUBTCPIPTYPE={{item.SUBTCPIPTYPE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.9 设置应用联动默认动作

#### 在“MML命令行-UEG”窗口上执行：

```jinja2
{%- for item in set_secpolicyapplnk_list -%}
    SET SECPOLICYAPPLNK:
    {#- --- 必选参数 --- -#}
    SECPOLICYID={{item.SECPOLICYID}},
    SECDFTACTION={{item.SECDFTACTION}},
    ;
{%- endfor -%}
```

### 3 将防攻击策略绑定到对应的资源单元上。

### 在“MML命令行-UEG”窗口上执行：

```jinja2
{%- for item in add_secpolicycfg_list -%}
    ADD SECPOLICYCFG:
    {#- --- 必选参数 --- -#}
    POLICYID={{item.POLICYID}},
    RUNAME="{{item.RUNAME}}",
    ;
{%- endfor -%}
```

### 4 （可选）使能免费ARP报文过滤。

### 在“MML命令行-UEG”窗口上执行：

```jinja2
{%- if is_optional_free_arp_filter -%}
    {%- for item in set_secarpgrat_list -%}
        SET SECARPGRAT:
        {#- --- 必选参数 --- -#}
        IFNAME="{{item.IFNAME}}",
        SECENABLE={{item.SECENABLE}},
        ;
    {%- endfor -%}
{%- endif -%}
```

### 5 （可选）使能ARP快回。

### 在“MML命令行-UEG”窗口上执行：

```jinja2
{%- if is_optional_arp_fast_reply -%}
    {%- for item in set_secarp_list -%}
        SET SECARP:
        {#- --- 必选参数 --- -#}
        RUNAME="{{item.RUNAME}}",
        FASTRLYEN={{item.FASTRLYEN}},
        ;
    {%- endfor -%}
{%- endif -%}
```

### 6 （可选）使能ICMP快回

### 在“MML命令行-UEG”窗口上执行：

```jinja2
{%- if is_optional_icmp_fast_reply -%}
    {%- for item in set_secicmpreply_list -%}
        SET SECICMPREPLY:
        {#- --- 必选参数 --- -#}
        RUNAME="{{item.RUNAME}}",
        FASTRLYEN={{item.FASTRLYEN}},
        ;
    {%- endfor -%}
{%- endif -%}
```

### 7 （可选）使能ND快回。

### 在“MML命令行-UEG”窗口上执行：

```jinja2
{%- if is_optional_nd_fast_reply -%}
    {%- for item in set_secnd_list -%}
        SET SECND:
        {#- --- 必选参数 --- -#}
        FASTRLYEN={{item.FASTRLYEN}},
        ;
    {%- endfor -%}
{%- endif -%}
```

