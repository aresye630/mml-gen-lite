---
id: ''
name: 配置ACL防止UE或用户PDN/DN对运营商网络设备攻击
ne_type: UEG
type: feature
description: 如果UE所属APN绑定的VPN与UEG的PDN/DN侧接口绑定的VPN相同，UE激活后存在攻击UEG以及与UEG的PDN/DN侧接口相连的路由器设备的可能性。另外如果VPN配置错误，恶意用户了解运营商网络设备IP地址的情况下，可能发起非法行访问或恶意攻击。组网如图1所示。  **图1** 防止UE对运营商网络设备的攻击示意图  禁止UE访问的运营商网络设备范围包括：  * UPF周边对接网元，网络数据参考水平网设文档。 * NFVI基础设施层，网络数据参考垂直网设文档。 * 日志服务器、NTP服务器等其他网络设备，网络数据需要根据运营商实际部署情况确定。  为防止恶意用户的以上攻击行为，收集以上运营商网络设备的网络数据，需要采取如下至少一种措施阻断恶意用户访问行为。  * 在外部PDN/DN网络和运营商网络设备之间部署防火墙，禁止用户访问运营商网络设备。 * 在UEG上配置包过滤策略，禁止用户访问运营商网络设备。过滤报文目的地址为：本运营商范围内与UE所属APN绑定同一VPN的接口可达的所有网段。  适用于SGW-U、PGW-U、UPF。
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻+地市共享（连接+计算）","5GC toB 部署边缘站点（站点为“风筝M”，带计算）","配置安全数据（风筝M）","安全配置（虚机容器）","安全配置建议","可选配置","业务安全配置","配置ACL防止UE或用户PDN/DN对运营商网络设备攻击"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
如果UE所属APN绑定的VPN与UEG的PDN/DN侧接口绑定的VPN相同，UE激活后存在攻击UEG以及与UEG的PDN/DN侧接口相连的路由器设备的可能性。另外如果VPN配置错误，恶意用户了解运营商网络设备IP地址的情况下，可能发起非法行访问或恶意攻击。组网如图1所示。**图1** 防止UE对运营商网络设备的攻击示意图禁止UE访问的运营商网络设备范围包括：* UPF周边对接网元，网络数据参考水平网设文档。* NFVI基础设施层，网络数据参考垂直网设文档。* 日志服务器、NTP服务器等其他网络设备，网络数据需要根据运营商实际部署情况确定。为防止恶意用户的以上攻击行为，收集以上运营商网络设备的网络数据，需要采取如下至少一种措施阻断恶意用户访问行为。* 在外部PDN/DN网络和运营商网络设备之间部署防火墙，禁止用户访问运营商网络设备。* 在UEG上配置包过滤策略，禁止用户访问运营商网络设备。过滤报文目的地址为：本运营商范围内与UE所属APN绑定同一VPN的接口可达的所有网段。适用于SGW-U、PGW-U、UPF。

## 必备事项
前提条件

前提条件

无。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_filter_list:
      type: items
      properties:
        FILTERNAME:
          name: '过滤器名字'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '**ADD FILTER**'
          data_source: '本端规划'
          pattern: ''
          default: ''
        L34PROTTYPE:
          name: '三四层IPv4协议输入类型'
          type: string
          enum:
          - NUMBER
          - STRING
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        L34PROTOCOL:
          name: '三四层协议类型'
          type: string
          enum:
          - ANY
          - GRE
          - ICMP
          - TCP
          - UDP
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ANY
        MSIPMODE:
          name: '手机IP地址配置模式'
          type: string
          enum:
          - IP
          - IPLIST
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        MSIP:
          name: '手机IP地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        MSIPMASKTYPE:
          name: '手机IP地址掩码类型'
          type: string
          enum:
          - IPTYPE
          - LENGTHTYPE
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        MSIPMASK:
          name: '手机IP地址反掩码'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SVRIPMODE:
          name: '服务器IP地址配置模式'
          type: string
          enum:
          - DOMAIN
          - HOSTNAME
          - IP
          - IPLIST
          required: false
          description: '核心网侧服务器的IP地址及反掩码。 **ADD FILTER**'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SVRIP:
          name: '服务器IP地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SVRIPMASKTYPE:
          name: '服务器IP地址掩码类型'
          type: string
          enum:
          - IPTYPE
          - LENGTHTYPE
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SVRIPMASK:
          name: '服务器IP地址反掩码'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_refreshsrv_list:
      type: items
      properties:
        REFRESHTYPE:
          name: '刷新类型'
          type: string
          enum:
          - ACL
          - ALL
          - USERPROFILE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_aclnode_list:
      type: items
      properties:
        ACLNODENAME:
          name: 'ACL节点名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '**ADD ACLNODE**'
          data_source: '本端规划'
          pattern: ''
          default: ''
        FILTERNAME:
          name: '过滤器名字'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '已通过**ADD FILTER**命令配置完成，可以使用**LST FILTER**命令进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        ACTIONTYPE:
          name: '动作类型'
          type: string
          enum:
          - GATE
          - REDIRECT
          required: true
          description: '**ADD ACLNODE**'
          data_source: '本端规划'
          pattern: ''
          default: ''
        GATEACTION:
          name: '门控动作'
          type: string
          enum:
          - DISCARD
          - PASS
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: PASS
    add_acl_list:
      type: items
      properties:
        ACLNAME:
          name: 'ACL名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '**ADD ACL**'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MATCHORDER:
          name: '匹配方式'
          type: string
          enum:
          - AUTO
          - CONFIG
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_aclnodebindacl_list:
      type: items
      properties:
        ACLNAME:
          name: 'ACL名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '已通过**ADD ACL**命令配置完成，可以使用**LST ACL**命令进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        ACLNODENAME:
          name: 'ACL节点名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '已通过**ADD ACLNODE**命令配置完成，可以使用**LST ACLNODE**命令进行查询。'
          data_source: '已配置数据中获取'
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
          description: '已通过**ADD APN**命令配置完成，可以使用**LST APN**命令进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        HASVPN:
          name: '绑定VPN'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        HASVPNIPV6:
          name: '绑定IPv6 VPN'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        RESTORPGWSWITCH:
          name: '故障重启业务恢复功能PGW开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: INHERIT
    add_aclbindapn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '已通过**ADD APN**命令配置完成，可以使用**LST APN**命令进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DIRECTION:
          name: '方向'
          type: string
          enum:
          - DOWNIN
          - DOWNOUT
          - UPIN
          - UPOUT
          required: true
          description: '**ADD ACLBINDAPN**'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ACLNAME:
          name: 'ACL名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '已通过**ADD ACL**命令配置完成，可以使用**LST ACL**命令进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    set_refreshsrv_list_2:
      type: items
      properties:
        REFRESHTYPE:
          name: '刷新类型'
          type: string
          enum:
          - ACL
          - ALL
          - USERPROFILE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_filter_list:
    - FILTERNAME: 'to-cn'
      L34PROTTYPE: STRING
      L34PROTOCOL: UDP
      MSIPMODE: IP
      MSIP: '10.57.90.1'
      MSIPMASKTYPE: IPTYPE
      MSIPMASK: '0.0.0.31'
      SVRIPMODE: IP
      SVRIP: '192.168.95.67'
      SVRIPMASKTYPE: IPTYPE
      SVRIPMASK: '0.0.0.31'
    set_refreshsrv_list:
    - REFRESHTYPE: USERPROFILE
    add_aclnode_list:
    - ACLNODENAME: 'node-upflow-cn'
      FILTERNAME: 'to-cn'
      ACTIONTYPE: GATE
      GATEACTION: DISCARD
    add_acl_list:
    - ACLNAME: 'acl-upflow'
      MATCHORDER: AUTO
    add_aclnodebindacl_list:
    - ACLNAME: 'acl-upflow'
      ACLNODENAME: 'node-upflow-cn'
    add_apn_list:
    - APN: 'apn-test'
      HASVPN: DISABLE
      HASVPNIPV6: DISABLE
      RESTORPGWSWITCH: INHERIT
    add_aclbindapn_list:
    - APN: 'apn-test'
      DIRECTION: UPIN
      ACLNAME: 'acl-upflow'
    set_refreshsrv_list_2:
    - REFRESHTYPE: ACL
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 在“MML命令行-UEG”窗口上配置ACL节点使用的过滤规则。

#### 1.1 配置三四层的过滤规则。

```jinja2
{%- for item in add_filter_list -%}
    ADD FILTER:
    {#- --- 必选参数 --- -#}
    FILTERNAME="{{item.FILTERNAME}}",
    L34PROTTYPE={{item.L34PROTTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.MSIPMODE is not none -%}
        MSIPMODE={{item.MSIPMODE}},
    {%- endif -%}
    {%- if item.SVRIPMODE is not none -%}
        SVRIPMODE={{item.SVRIPMODE}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：L34PROTTYPE=STRING 时必选 --- -#}
    {%- if item.L34PROTTYPE == 'STRING' -%}
        L34PROTOCOL={{item.L34PROTOCOL}},
    {%- endif -%}
    {#- --- 条件必选：MSIPMODE=IP 时必选 --- -#}
    {%- if item.MSIPMODE == 'IP' -%}
        MSIP="{{item.MSIP}}",
    {%- endif -%}
    {#- --- 条件必选：MSIPMODE=IP 时必选 --- -#}
    {%- if item.MSIPMODE == 'IP' -%}
        MSIPMASKTYPE={{item.MSIPMASKTYPE}},
    {%- endif -%}
    {#- --- 条件必选：MSIPMASKTYPE=IPTYPE 时必选 --- -#}
    {%- if item.MSIPMASKTYPE == 'IPTYPE' -%}
        MSIPMASK="{{item.MSIPMASK}}",
    {%- endif -%}
    {#- --- 条件必选：SVRIPMODE=IP 时必选 --- -#}
    {%- if item.SVRIPMODE == 'IP' -%}
        SVRIP="{{item.SVRIP}}",
    {%- endif -%}
    {#- --- 条件必选：SVRIPMODE=IP 时必选 --- -#}
    {%- if item.SVRIPMODE == 'IP' -%}
        SVRIPMASKTYPE={{item.SVRIPMASKTYPE}},
    {%- endif -%}
    {#- --- 条件必选：SVRIPMASKTYPE=IPTYPE 时必选 --- -#}
    {%- if item.SVRIPMASKTYPE == 'IPTYPE' -%}
        SVRIPMASK="{{item.SVRIPMASK}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.2 将新配置的filter置为生效。

```jinja2
{%- for item in set_refreshsrv_list -%}
    SET REFRESHSRV:
    {#- --- 必选参数 --- -#}
    REFRESHTYPE={{item.REFRESHTYPE}},
    ;
{%- endfor -%}
```

### 2 在“MML命令行-UEG”窗口上配置ACL节点，并绑定到ACL。

#### 2.1 配置ACL节点，即配置三四层过滤规则对应的动作。

```jinja2
{%- for item in add_aclnode_list -%}
    ADD ACLNODE:
    {#- --- 必选参数 --- -#}
    ACLNODENAME="{{item.ACLNODENAME}}",
    FILTERNAME="{{item.FILTERNAME}}",
    ACTIONTYPE={{item.ACTIONTYPE}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：ACTIONTYPE=GATE 时可选 --- -#}
    {%- if item.ACTIONTYPE == 'GATE' -%}
        {%- if item.GATEACTION is not none -%}
            GATEACTION={{item.GATEACTION}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.2 配置ACL名称、排序方式。

```jinja2
{%- for item in add_acl_list -%}
    ADD ACL:
    {#- --- 必选参数 --- -#}
    ACLNAME="{{item.ACLNAME}}",
    MATCHORDER={{item.MATCHORDER}},
    ;
{%- endfor -%}
```

#### 2.3 配置绑定ACL节点到ACL下。

```jinja2
{%- for item in add_aclnodebindacl_list -%}
    ADD ACLNODEBINDACL:
    {#- --- 必选参数 --- -#}
    ACLNAME="{{item.ACLNAME}}",
    ACLNODENAME="{{item.ACLNODENAME}}",
    ;
{%- endfor -%}
```

### 3 在“MML命令行-UEG”窗口上配置ACL与APN的绑定关系。

#### 3.1 配置APN名称。

```jinja2
{%- for item in add_apn_list -%}
    ADD APN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.HASVPN is not none -%}
        HASVPN={{item.HASVPN}},
    {%- endif -%}
    {%- if item.HASVPNIPV6 is not none -%}
        HASVPNIPV6={{item.HASVPNIPV6}},
    {%- endif -%}
    {%- if item.RESTORPGWSWITCH is not none -%}
        RESTORPGWSWITCH={{item.RESTORPGWSWITCH}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 3.2 配置ACL绑定到APN下。

```jinja2
{%- for item in add_aclbindapn_list -%}
    ADD ACLBINDAPN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    DIRECTION={{item.DIRECTION}},
    ACLNAME="{{item.ACLNAME}}",
    ;
{%- endfor -%}
```

#### 3.3 将新配置的ACL和ACL节点置为生效。

```jinja2
{%- for item in set_refreshsrv_list_2 -%}
    SET REFRESHSRV:
    {#- --- 必选参数 --- -#}
    REFRESHTYPE={{item.REFRESHTYPE}},
    ;
{%- endfor -%}
```

