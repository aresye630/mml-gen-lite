---
id: ''
name: 配置VXLAN隧道及分流规则
ne_type: UEG
type: feature
description: UEG作为主锚点UPF或辅锚点UPF，与MPF对接时，需要配置VXLAN隧道及分流规则（分流到MPF的规则）。  UPF与MPF通过VXLAN（VXLAN-GPE）隧道互通。为简化描述，使用VXLAN替代VXLAN-GPE。
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝M”，入驻式）","UEG初始配置（风筝M）","参考：详细配置指导","配置UL CL UPF + 辅锚点UPF","配置VXLAN隧道及分流规则"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
UEG作为主锚点UPF或辅锚点UPF，与MPF对接时，需要配置VXLAN隧道及分流规则（分流到MPF的规则）。UPF与MPF通过VXLAN（VXLAN-GPE）隧道互通。为简化描述，使用VXLAN替代VXLAN-GPE。

## 必备事项
前提条件

前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录MAE客户端或登录OM Portal）。
* 请了解UEG各类接口的类型及命名规范，具体内容请参见逻辑接口介绍（UPF）。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_vxlangrp_list:
      type: items
      properties:
        GRPNAME:
          name: 'VXLAN隧道组名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: 'VXLAN链路组名称，网元内不能重复。  此处规划的vxlan_grp01用于和APN绑定，vxlan_grp02用于和rule绑定。  rule绑定的VXLAN链路组优先级高于APN绑定的VXLAN链路组。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SRCINTF:
          name: 'VXLAN隧道源接口'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: 'UPF与MPF互通场景，此处使用的是UPF上Nxuc接口。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        HEARTBEAT:
          name: '健康检查开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '使能心跳检查功能。'
          data_source: '本端规划'
          pattern: ''
          default: ENABLE
        TIMETHRESHOLD:
          name: '时间阈值（秒）'
          type: integer
          minimum: 3
          maximum: 60
          required: false
          description: '两次心跳检测间的时间阈值。'
          data_source: '本端规划'
          pattern: ''
          default: 6
        HEARTSUCCLIMIT:
          name: '心跳检查成功次数'
          type: integer
          minimum: 1
          maximum: 10
          required: false
          description: '设置隧道状态为up所需的心跳检测连续成功次数。'
          data_source: '本端规划'
          pattern: ''
          default: 3
        HEARTFAILLIMIT:
          name: '心跳检查失败次数'
          type: integer
          minimum: 1
          maximum: 10
          required: false
          description: '设置隧道状态为down所需的心跳检测连续失败次数。'
          data_source: '本端规划'
          pattern: ''
          default: 3
        TIMEOUT:
          name: 'Ping探测超时时长（秒）'
          type: integer
          minimum: 1
          maximum: 59
          required: false
          description: '设置心跳检测的超时时长，该值需要小于TimeThreshold。'
          data_source: '本端规划'
          pattern: ''
          default: 2
    add_vtep_list:
      type: items
      properties:
        VTEPNAME:
          name: 'VXLAN隧道端点名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: 'VXLAN隧道端点名称，网元内不能重复。  此处规划的VTEP1用于和vxlan_grp01绑定，VTEP2用于和vxlan_grp02绑定。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP协议版本'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: 'UPF与MPF互通场景，此处使用的是MPF上Nxua逻辑接口的IP地址。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VTEPIPV4:
          name: '隧道端点的IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
    add_vtepbindgrp_list:
      type: items
      properties:
        VXLANGRPNAME:
          name: 'VXLAN组名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: 'VTEP绑定VXLAN隧道组。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        VTEPNAME:
          name: 'VTEP名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PRIFLAG:
          name: '主备用类型'
          type: string
          enum:
          - PRIMARY
          - SECONDARY
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: PRIMARY
    add_vxlanbindapn_list:
      type: items
      properties:
        APN:
          name: 'APN'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '基于APN绑定一个链路组。UPF与MPF互通场景，UPF将命中Rule的报文发送到MPF的Nxua接口。  可选数据，使用APN绑定的VXLAN隧道转发数据时需要规划。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        VXLANGRPNAME:
          name: 'VXLAN组名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_vpnvnimap_list:
      type: items
      properties:
        VPNINSTANCE:
          name: 'VPN实例'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '与APN绑定的VPN实例相同。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        RULESWITCH:
          name: 'Rule开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: '基于用户VPN映射到VNI时设置为“DISABLE”；基于VPN+RULE映射到VNI时设置为“ENABLE”。'
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
        VNI:
          name: 'VNI'
          type: integer
          minimum: 0
          maximum: 16777215
          required: true
          description: '配置VxLan隧道标识。  如需了解VXLAN-GPE报文格式，请跳转到VXLAN-GPE。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        RULENAME:
          name: '规格名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: '基于VPN+RULE映射到VNI时需要设置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_filter_list:
      type: items
      properties:
        FILTERNAME:
          name: '过滤器名字'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '配置三四层过滤条件。该IP地址是APP服务器的IP地址。  此处的分流到MPF的规则，以三四层条件中的服务器地址完全匹配为例进行介绍。  访问此处指定的APP服务器（192.168.1.1/192.168.1.2）时，流量将通过VXLAN隧道发送到MPF；访问此处没有指定的APP服务器（如192.168.2.2）时，则流量不经过MPF。'
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
        SVRIPMODE:
          name: '服务器IP地址配置模式'
          type: string
          enum:
          - DOMAIN
          - HOSTNAME
          - IP
          - IPLIST
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SVRIP:
          name: '服务器IP地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '已配置数据中获取'
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
          data_source: '本端规划'
          pattern: ''
          default: ''
        SVRIPMASKLEN:
          name: '服务器IP地址掩码长度'
          type: integer
          minimum: 0
          maximum: 32
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SVRSTARTPORT:
          name: '服务器起始端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        SVRENDPORT:
          name: '服务器结束端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 65535
    add_flowfilter_list:
      type: items
      properties:
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '流过滤器。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TETHERDETFLAG:
          name: 'Tethering检测标识'
          type: string
          enum:
          - DETECT_ONLY
          - FILTER
          - NONE
          - NOT_FILTER
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NONE
        FLOWFILTERTYPE:
          name: 'FlowFilter类型'
          type: string
          enum:
          - EXTEROTTDB
          - USERCONFIG
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: USERCONFIG
    add_fltbindflowf_list:
      type: items
      properties:
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '绑定的三四层过滤条件已通过**ADD FILTER**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        FILTERNAME:
          name: '过滤器名字'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_rule_list:
      type: items
      properties:
        RULENAME:
          name: '规则名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '转发规则。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        POLICYTYPE:
          name: '策略类型'
          type: string
          enum:
          - ADC
          - BWM
          - FIREWALL
          - HEADEN
          - IPREDIR
          - LBO
          - PCC
          - QOS
          - REMARK_FPI
          - SMARTREDIRECT
          - SRV_TRIGGER
          - TRAFFICCLASS
          - WEBPROXY
          - WORKER
          required: true
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        FILTERINGMODE:
          name: '流过滤器或流过滤器组选择'
          type: string
          enum:
          - FLOWFILTER
          - FLOWFILTERGRP
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: '绑定的FlowFilter已通过**ADD FLOWFILTER**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PRIORITY:
          name: '全局优先级'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 4294967295
        WORKERNAME:
          name: '通用Rule子策略名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '必须使用样例值。UPF依赖该配置将命中规则的数据报文通过VXLAN隧道转发到MPF。'
          data_source: '固定取值'
          pattern: ''
          default: ''
    add_userprofile_list:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '该参数与SMF上的PCC类型的Userprofile名称必须相同。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_rulebinding_list:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '已通过**ADD USERPROFILE**配置完成。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        RULENAME:
          name: '规则名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: 'UserProfile绑定的业务规则，已通过**ADD RULE**命令配置完成。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    set_apntrafdfunc_list:
      type: items
      properties:
        APN:
          name: 'APN'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '-'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        TRAFFICFDSW:
          name: '流量转发开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
    add_vxlangrp_list_1:
      type: items
      properties:
        GRPNAME:
          name: 'VXLAN隧道组名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: 'VXLAN链路组名称，网元内不能重复。  此处规划的vxlan_grp01用于和APN绑定，vxlan_grp02用于和rule绑定。  rule绑定的VXLAN链路组优先级高于APN绑定的VXLAN链路组。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SRCINTF:
          name: 'VXLAN隧道源接口'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: 'UPF与MPF互通场景，此处使用的是UPF上Nxuc接口。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        HEARTBEAT:
          name: '健康检查开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '使能心跳检查功能。'
          data_source: '本端规划'
          pattern: ''
          default: ENABLE
        TIMETHRESHOLD:
          name: '时间阈值（秒）'
          type: integer
          minimum: 3
          maximum: 60
          required: false
          description: '两次心跳检测间的时间阈值。'
          data_source: '本端规划'
          pattern: ''
          default: 6
        HEARTSUCCLIMIT:
          name: '心跳检查成功次数'
          type: integer
          minimum: 1
          maximum: 10
          required: false
          description: '设置隧道状态为up所需的心跳检测连续成功次数。'
          data_source: '本端规划'
          pattern: ''
          default: 3
        HEARTFAILLIMIT:
          name: '心跳检查失败次数'
          type: integer
          minimum: 1
          maximum: 10
          required: false
          description: '设置隧道状态为down所需的心跳检测连续失败次数。'
          data_source: '本端规划'
          pattern: ''
          default: 3
        TIMEOUT:
          name: 'Ping探测超时时长（秒）'
          type: integer
          minimum: 1
          maximum: 59
          required: false
          description: '设置心跳检测的超时时长，该值需要小于TimeThreshold。'
          data_source: '本端规划'
          pattern: ''
          default: 2
    add_vtep_list_1:
      type: items
      properties:
        VTEPNAME:
          name: 'VXLAN隧道端点名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: 'VXLAN隧道端点名称，网元内不能重复。  此处规划的VTEP1用于和vxlan_grp01绑定，VTEP2用于和vxlan_grp02绑定。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP协议版本'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: 'UPF与MPF互通场景，此处使用的是MPF上Nxua逻辑接口的IP地址。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VTEPIPV4:
          name: '隧道端点的IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
    add_vtepbindgrp_list_1:
      type: items
      properties:
        VXLANGRPNAME:
          name: 'VXLAN组名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: 'VTEP绑定VXLAN隧道组。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        VTEPNAME:
          name: 'VTEP名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PRIFLAG:
          name: '主备用类型'
          type: string
          enum:
          - PRIMARY
          - SECONDARY
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: PRIMARY
    add_filter_list_1:
      type: items
      properties:
        FILTERNAME:
          name: '过滤器名字'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '配置三四层过滤条件。该IP地址是APP服务器的IP地址。  此处的分流到MPF的规则，以三四层条件中的服务器地址完全匹配为例进行介绍。  访问此处指定的APP服务器（192.168.1.1/192.168.1.2）时，流量将通过VXLAN隧道发送到MPF；访问此处没有指定的APP服务器（如192.168.2.2）时，则流量不经过MPF。'
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
        SVRIPMODE:
          name: '服务器IP地址配置模式'
          type: string
          enum:
          - DOMAIN
          - HOSTNAME
          - IP
          - IPLIST
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SVRIP:
          name: '服务器IP地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '已配置数据中获取'
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
          data_source: '本端规划'
          pattern: ''
          default: ''
        SVRIPMASKLEN:
          name: '服务器IP地址掩码长度'
          type: integer
          minimum: 0
          maximum: 32
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SVRSTARTPORT:
          name: '服务器起始端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        SVRENDPORT:
          name: '服务器结束端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 65535
    add_flowfilter_list_1:
      type: items
      properties:
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '流过滤器。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TETHERDETFLAG:
          name: 'Tethering检测标识'
          type: string
          enum:
          - DETECT_ONLY
          - FILTER
          - NONE
          - NOT_FILTER
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: NONE
        FLOWFILTERTYPE:
          name: 'FlowFilter类型'
          type: string
          enum:
          - EXTEROTTDB
          - USERCONFIG
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: USERCONFIG
    add_fltbindflowf_list_1:
      type: items
      properties:
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '绑定的三四层过滤条件已通过**ADD FILTER**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        FILTERNAME:
          name: '过滤器名字'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_rule_list_1:
      type: items
      properties:
        RULENAME:
          name: '规则名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '转发规则。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        POLICYTYPE:
          name: '策略类型'
          type: string
          enum:
          - ADC
          - BWM
          - FIREWALL
          - HEADEN
          - IPREDIR
          - LBO
          - PCC
          - QOS
          - REMARK_FPI
          - SMARTREDIRECT
          - SRV_TRIGGER
          - TRAFFICCLASS
          - WEBPROXY
          - WORKER
          required: true
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        FILTERINGMODE:
          name: '流过滤器或流过滤器组选择'
          type: string
          enum:
          - FLOWFILTER
          - FLOWFILTERGRP
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: '绑定的FlowFilter已通过**ADD FLOWFILTER**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PRIORITY:
          name: '全局优先级'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 4294967295
        WORKERNAME:
          name: '通用Rule子策略名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '必须使用样例值。UPF依赖该配置将命中规则的数据报文通过VXLAN隧道转发到MPF。'
          data_source: '固定取值'
          pattern: ''
          default: ''
    add_userprofile_list_1:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '该参数与SMF上的PCC类型的Userprofile名称必须相同。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_rulebinding_list_1:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '已通过**ADD USERPROFILE**配置完成。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        RULENAME:
          name: '规则名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: 'UserProfile绑定的业务规则，已通过**ADD RULE**命令配置完成。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_vxlanbindrule_list:
      type: items
      properties:
        RULENAME:
          name: '规则名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '使用**ADD RULE**命令定义的规则名称。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        VXLANGRPNAME:
          name: 'VXLAN组名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '使用**ADD VXLANGRP**命令定义的VXLAN组名称。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_vpnvnimap_list_1:
      type: items
      properties:
        VPNINSTANCE:
          name: 'VPN实例'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '与APN绑定的VPN实例相同。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        RULESWITCH:
          name: 'Rule开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: '基于用户VPN映射到VNI时设置为“DISABLE”；基于VPN+RULE映射到VNI时设置为“ENABLE”。'
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
        RULENAME:
          name: '规格名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: '基于VPN+RULE映射到VNI时需要设置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VNI:
          name: 'VNI'
          type: integer
          minimum: 0
          maximum: 16777215
          required: true
          description: '配置VxLan隧道标识。  如需了解VXLAN-GPE报文格式，请跳转到VXLAN-GPE。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_apntrafdfunc_list_1:
      type: items
      properties:
        APN:
          name: 'APN'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '-'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        TRAFFICFDSW:
          name: '流量转发开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
  examples:
    add_vxlangrp_list:
    - GRPNAME: 'vxlan_grp01'
      SRCINTF: 'Nxucif1/1/0'
      HEARTBEAT: ENABLE
      TIMETHRESHOLD: 6
      HEARTSUCCLIMIT: 3
      HEARTFAILLIMIT: 3
      TIMEOUT: 2
    add_vtep_list:
    - VTEPNAME: 'VTEP1'
      IPVERSION: IPV4
      VTEPIPV4: '10.10.100.1'
    add_vtepbindgrp_list:
    - VXLANGRPNAME: 'vxlan_grp01'
      VTEPNAME: 'VTEP1'
      PRIFLAG: PRIMARY
    add_vxlanbindapn_list:
    - APN: 'apn-op'
      VXLANGRPNAME: 'vxlan_grp01'
    add_vpnvnimap_list:
    - VPNINSTANCE: 'VPN_LocalDN01'
      RULESWITCH: DISABLE
      VNI: 1
      RULENAME: '-'
    add_filter_list:
    - FILTERNAME: 'filter_trafficfwd01'
      L34PROTTYPE: STRING
      L34PROTOCOL: ANY
      SVRIPMODE: IP
      SVRIP: '192.168.1.1'
      SVRIPMASKTYPE: LENGTHTYPE
      SVRIPMASKLEN: 32
      SVRSTARTPORT: 0
      SVRENDPORT: 65535
    add_flowfilter_list:
    - FLOWFILTERNAME: 'FlowFilter_trafficfwd01'
      TETHERDETFLAG: NONE
      FLOWFILTERTYPE: USERCONFIG
    add_fltbindflowf_list:
    - FLOWFILTERNAME: 'FlowFilter_trafficfwd01'
      FILTERNAME: 'filter_trafficfwd01'
    add_rule_list:
    - RULENAME: 'rule_trafficfwd01'
      POLICYTYPE: WORKER
      FILTERINGMODE: FLOWFILTER
      FLOWFILTERNAME: 'FlowFilter_trafficfwd01'
      PRIORITY: 65535
      WORKERNAME: 'traffic-fd'
    add_userprofile_list:
    - USERPROFILENAME: 'up_test'
    add_rulebinding_list:
    - USERPROFILENAME: 'up_test'
      RULENAME: 'rule_trafficfwd01'
    set_apntrafdfunc_list:
    - APN: 'apn-op'
      TRAFFICFDSW: ENABLE
    add_vxlangrp_list_1:
    - GRPNAME: 'vxlan_grp02'
      SRCINTF: 'Nxucif1/1/0'
      HEARTBEAT: ENABLE
      TIMETHRESHOLD: 6
      HEARTSUCCLIMIT: 3
      HEARTFAILLIMIT: 3
      TIMEOUT: 2
    add_vtep_list_1:
    - VTEPNAME: 'VTEP2'
      IPVERSION: IPV4
      VTEPIPV4: '10.10.100.2'
    add_vtepbindgrp_list_1:
    - VXLANGRPNAME: 'vxlan_grp02'
      VTEPNAME: 'VTEP2'
      PRIFLAG: PRIMARY
    add_filter_list_1:
    - FILTERNAME: 'filter_trafficfwd02'
      L34PROTTYPE: STRING
      L34PROTOCOL: ANY
      SVRIPMODE: IP
      SVRIP: '192.168.1.2'
      SVRIPMASKTYPE: LENGTHTYPE
      SVRIPMASKLEN: 32
      SVRSTARTPORT: 0
      SVRENDPORT: 65535
    add_flowfilter_list_1:
    - FLOWFILTERNAME: 'FlowFilter_trafficfwd02'
      TETHERDETFLAG: NONE
      FLOWFILTERTYPE: USERCONFIG
    add_fltbindflowf_list_1:
    - FLOWFILTERNAME: 'FlowFilter_trafficfwd02'
      FILTERNAME: 'filter_trafficfwd02'
    add_rule_list_1:
    - RULENAME: 'rule_trafficfwd02'
      POLICYTYPE: WORKER
      FILTERINGMODE: FLOWFILTER
      FLOWFILTERNAME: 'FlowFilter_trafficfwd02'
      PRIORITY: 65535
      WORKERNAME: 'traffic-fd'
    add_userprofile_list_1:
    - USERPROFILENAME: 'up_test'
    add_rulebinding_list_1:
    - USERPROFILENAME: 'up_test'
      RULENAME: 'rule_trafficfwd02'
    add_vxlanbindrule_list:
    - RULENAME: 'rule_trafficfwd02'
      VXLANGRPNAME: 'vxlan_grp02'
    add_vpnvnimap_list_1:
    - VPNINSTANCE: 'VPN_LocalDN01'
      RULESWITCH: ENABLE
      RULENAME: 'rule_trafficfwd02'
      VNI: 2
    set_apntrafdfunc_list_1:
    - APN: 'apn-op'
      TRAFFICFDSW: ENABLE
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 配置VXLAN隧道（UPF）\_基于APN绑定隧道

### 根据UE选择转发给哪个MPF时需要配置，如APP Server跨站点负荷分担部署时可使用该方案。

#### 1.1 配置VXLAN隧道组。

```jinja2
{%- if is_scenario_apn_binding -%}
    {%- for item in add_vxlangrp_list -%}
        ADD VXLANGRP:
        {#- --- 必选参数 --- -#}
        GRPNAME="{{item.GRPNAME}}",
        SRCINTF="{{item.SRCINTF}}",
        {#- --- 可选参数 --- -#}
        {%- if item.HEARTBEAT is not none -%}
            HEARTBEAT={{item.HEARTBEAT}},
        {%- endif -%}
        {%- if item.TIMETHRESHOLD is not none -%}
            TIMETHRESHOLD={{item.TIMETHRESHOLD}},
        {%- endif -%}
        {%- if item.HEARTSUCCLIMIT is not none -%}
            HEARTSUCCLIMIT={{item.HEARTSUCCLIMIT}},
        {%- endif -%}
        {%- if item.HEARTFAILLIMIT is not none -%}
            HEARTFAILLIMIT={{item.HEARTFAILLIMIT}},
        {%- endif -%}
        {%- if item.TIMEOUT is not none -%}
            TIMEOUT={{item.TIMEOUT}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 1.2 配置VXLAN隧道端点（VTEP）。

```jinja2
{%- if is_scenario_apn_binding -%}
    {%- for item in add_vtep_list -%}
        ADD VTEP:
        {#- --- 必选参数 --- -#}
        VTEPNAME="{{item.VTEPNAME}}",
        IPVERSION={{item.IPVERSION}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
        {%- if item.IPVERSION == 'IPV4' -%}
            VTEPIPV4="{{item.VTEPIPV4}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 1.3 配置VXLAN端点绑定VXLAN隧道组。

```jinja2
{%- if is_scenario_apn_binding -%}
    {%- for item in add_vtepbindgrp_list -%}
        ADD VTEPBINDGRP:
        {#- --- 必选参数 --- -#}
        VXLANGRPNAME="{{item.VXLANGRPNAME}}",
        VTEPNAME="{{item.VTEPNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.PRIFLAG is not none -%}
            PRIFLAG={{item.PRIFLAG}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 1.4 配置VXLAN隧道组绑定APN。

```jinja2
{%- if is_scenario_apn_binding -%}
    {%- for item in add_vxlanbindapn_list -%}
        ADD VXLANBINDAPN:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        VXLANGRPNAME="{{item.VXLANGRPNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 1.5 配置VPN到VNI的映射。

```jinja2
{%- if is_scenario_apn_binding -%}
    {%- for item in add_vpnvnimap_list -%}
        ADD VPNVNIMAP:
        {#- --- 必选参数 --- -#}
        VPNINSTANCE="{{item.VPNINSTANCE}}",
        RULESWITCH={{item.RULESWITCH}},
        VNI={{item.VNI}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：RULESWITCH=ENABLE 时必选 --- -#}
        {%- if item.RULESWITCH == 'ENABLE' -%}
            RULENAME="{{item.RULENAME}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 2 配置分流到MPF的规则（UPF）\_基于APN绑定隧道

### 根据UE选择转发给哪个MPF时需要配置，如APP Server跨站点负荷分担部署时可使用该方案。

#### 2.1 配置过滤器。

```jinja2
{%- if is_scenario_apn_binding -%}
    {%- for item in add_filter_list -%}
        ADD FILTER:
        {#- --- 必选参数 --- -#}
        FILTERNAME="{{item.FILTERNAME}}",
        L34PROTTYPE={{item.L34PROTTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.SVRIPMODE is not none -%}
            SVRIPMODE={{item.SVRIPMODE}},
        {%- endif -%}
        {%- if item.SVRSTARTPORT is not none -%}
            SVRSTARTPORT={{item.SVRSTARTPORT}},
        {%- endif -%}
        {%- if item.SVRENDPORT is not none -%}
            SVRENDPORT={{item.SVRENDPORT}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：L34PROTTYPE=STRING 时必选 --- -#}
        {%- if item.L34PROTTYPE == 'STRING' -%}
            L34PROTOCOL={{item.L34PROTOCOL}},
        {%- endif -%}
        {#- --- 条件必选：SVRIPMODE=IP 时必选 --- -#}
        {%- if item.SVRIPMODE == 'IP' -%}
            SVRIP="{{item.SVRIP}}",
        {%- endif -%}
        {#- --- 条件必选：SVRIPMODE=IP 时必选 --- -#}
        {%- if item.SVRIPMODE == 'IP' -%}
            SVRIPMASKTYPE={{item.SVRIPMASKTYPE}},
        {%- endif -%}
        {#- --- 条件必选：SVRIPMASKTYPE=LENGTHTYPE 时必选 --- -#}
        {%- if item.SVRIPMASKTYPE == 'LENGTHTYPE' -%}
            SVRIPMASKLEN={{item.SVRIPMASKLEN}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.2 配置流过滤器。

```jinja2
{%- if is_scenario_apn_binding -%}
    {%- for item in add_flowfilter_list -%}
        ADD FLOWFILTER:
        {#- --- 必选参数 --- -#}
        FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.TETHERDETFLAG is not none -%}
            TETHERDETFLAG={{item.TETHERDETFLAG}},
        {%- endif -%}
        {%- if item.FLOWFILTERTYPE is not none -%}
            FLOWFILTERTYPE={{item.FLOWFILTERTYPE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.3 配置过滤器和流过滤器绑定。

```jinja2
{%- if is_scenario_apn_binding -%}
    {%- for item in add_fltbindflowf_list -%}
        ADD FLTBINDFLOWF:
        {#- --- 必选参数 --- -#}
        FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
        FILTERNAME="{{item.FILTERNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.4 配置规则。

```jinja2
{%- if is_scenario_apn_binding -%}
    {%- for item in add_rule_list -%}
        ADD RULE:
        {#- --- 必选参数 --- -#}
        RULENAME="{{item.RULENAME}}",
        POLICYTYPE={{item.POLICYTYPE}},
        FILTERINGMODE={{item.FILTERINGMODE}},
        {#- --- 可选参数 --- -#}
        {%- if item.PRIORITY is not none -%}
            PRIORITY={{item.PRIORITY}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：FILTERINGMODE=FLOWFILTER 时必选 --- -#}
        {%- if item.FILTERINGMODE == 'FLOWFILTER' -%}
            FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
        {%- endif -%}
        {#- --- 条件必选：POLICYTYPE=WORKER 时必选 --- -#}
        {%- if item.POLICYTYPE == 'WORKER' -%}
            WORKERNAME="{{item.WORKERNAME}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.5 配置Userprofile。

```jinja2
{%- if is_scenario_apn_binding -%}
    {%- for item in add_userprofile_list -%}
        ADD USERPROFILE:
        {#- --- 必选参数 --- -#}
        USERPROFILENAME="{{item.USERPROFILENAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.6 配置规则绑定Userprofile。

```jinja2
{%- if is_scenario_apn_binding -%}
    {%- for item in add_rulebinding_list -%}
        ADD RULEBINDING:
        {#- --- 必选参数 --- -#}
        USERPROFILENAME="{{item.USERPROFILENAME}}",
        RULENAME="{{item.RULENAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.7 开启流量转发开关。

```jinja2
{%- if is_scenario_apn_binding -%}
    {%- for item in set_apntrafdfunc_list -%}
        SET APNTRAFDFUNC:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        TRAFFICFDSW={{item.TRAFFICFDSW}},
        ;
    {%- endfor -%}
{%- endif -%}
```

### 3 配置VXLAN隧道（UPF）\_基于Rule绑定隧道

### 根据UE访问的目的IP选择转发给哪个MPF时需要配置，如APP Server跨站点主备部署，且MPF只能访问本DC的APP Server时可使用该方案。

#### 3.1 配置VXLAN隧道组。

```jinja2
{%- if is_scenario_rule_binding -%}
    {%- for item in add_vxlangrp_list_1 -%}
        ADD VXLANGRP:
        {#- --- 必选参数 --- -#}
        GRPNAME="{{item.GRPNAME}}",
        SRCINTF="{{item.SRCINTF}}",
        {#- --- 可选参数 --- -#}
        {%- if item.HEARTBEAT is not none -%}
            HEARTBEAT={{item.HEARTBEAT}},
        {%- endif -%}
        {%- if item.TIMETHRESHOLD is not none -%}
            TIMETHRESHOLD={{item.TIMETHRESHOLD}},
        {%- endif -%}
        {%- if item.HEARTSUCCLIMIT is not none -%}
            HEARTSUCCLIMIT={{item.HEARTSUCCLIMIT}},
        {%- endif -%}
        {%- if item.HEARTFAILLIMIT is not none -%}
            HEARTFAILLIMIT={{item.HEARTFAILLIMIT}},
        {%- endif -%}
        {%- if item.TIMEOUT is not none -%}
            TIMEOUT={{item.TIMEOUT}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.2 配置VXLAN隧道端点（VTEP）。

```jinja2
{%- if is_scenario_rule_binding -%}
    {%- for item in add_vtep_list_1 -%}
        ADD VTEP:
        {#- --- 必选参数 --- -#}
        VTEPNAME="{{item.VTEPNAME}}",
        IPVERSION={{item.IPVERSION}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
        {%- if item.IPVERSION == 'IPV4' -%}
            VTEPIPV4="{{item.VTEPIPV4}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.3 配置VXLAN端点绑定VXLAN隧道组。

```jinja2
{%- if is_scenario_rule_binding -%}
    {%- for item in add_vtepbindgrp_list_1 -%}
        ADD VTEPBINDGRP:
        {#- --- 必选参数 --- -#}
        VXLANGRPNAME="{{item.VXLANGRPNAME}}",
        VTEPNAME="{{item.VTEPNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.PRIFLAG is not none -%}
            PRIFLAG={{item.PRIFLAG}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 4 配置分流到MPF的规则（UPF）\_基于Rule绑定隧道

### 根据UE访问的目的IP选择转发给哪个MPF时需要配置，如APP Server跨站点主备部署，且MPF只能访问本DC的APP Server时可使用该方案。

#### 4.1 配置过滤器。

```jinja2
{%- if is_scenario_rule_binding -%}
    {%- for item in add_filter_list_1 -%}
        ADD FILTER:
        {#- --- 必选参数 --- -#}
        FILTERNAME="{{item.FILTERNAME}}",
        L34PROTTYPE={{item.L34PROTTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.SVRIPMODE is not none -%}
            SVRIPMODE={{item.SVRIPMODE}},
        {%- endif -%}
        {%- if item.SVRSTARTPORT is not none -%}
            SVRSTARTPORT={{item.SVRSTARTPORT}},
        {%- endif -%}
        {%- if item.SVRENDPORT is not none -%}
            SVRENDPORT={{item.SVRENDPORT}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：L34PROTTYPE=STRING 时必选 --- -#}
        {%- if item.L34PROTTYPE == 'STRING' -%}
            L34PROTOCOL={{item.L34PROTOCOL}},
        {%- endif -%}
        {#- --- 条件必选：SVRIPMODE=IP 时必选 --- -#}
        {%- if item.SVRIPMODE == 'IP' -%}
            SVRIP="{{item.SVRIP}}",
        {%- endif -%}
        {#- --- 条件必选：SVRIPMODE=IP 时必选 --- -#}
        {%- if item.SVRIPMODE == 'IP' -%}
            SVRIPMASKTYPE={{item.SVRIPMASKTYPE}},
        {%- endif -%}
        {#- --- 条件必选：SVRIPMASKTYPE=LENGTHTYPE 时必选 --- -#}
        {%- if item.SVRIPMASKTYPE == 'LENGTHTYPE' -%}
            SVRIPMASKLEN={{item.SVRIPMASKLEN}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.2 配置流过滤器。

```jinja2
{%- if is_scenario_rule_binding -%}
    {%- for item in add_flowfilter_list_1 -%}
        ADD FLOWFILTER:
        {#- --- 必选参数 --- -#}
        FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.TETHERDETFLAG is not none -%}
            TETHERDETFLAG={{item.TETHERDETFLAG}},
        {%- endif -%}
        {%- if item.FLOWFILTERTYPE is not none -%}
            FLOWFILTERTYPE={{item.FLOWFILTERTYPE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.3 配置过滤器和流过滤器绑定。

```jinja2
{%- if is_scenario_rule_binding -%}
    {%- for item in add_fltbindflowf_list_1 -%}
        ADD FLTBINDFLOWF:
        {#- --- 必选参数 --- -#}
        FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
        FILTERNAME="{{item.FILTERNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.4 配置规则。

```jinja2
{%- if is_scenario_rule_binding -%}
    {%- for item in add_rule_list_1 -%}
        ADD RULE:
        {#- --- 必选参数 --- -#}
        RULENAME="{{item.RULENAME}}",
        POLICYTYPE={{item.POLICYTYPE}},
        FILTERINGMODE={{item.FILTERINGMODE}},
        {#- --- 可选参数 --- -#}
        {%- if item.PRIORITY is not none -%}
            PRIORITY={{item.PRIORITY}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：FILTERINGMODE=FLOWFILTER 时必选 --- -#}
        {%- if item.FILTERINGMODE == 'FLOWFILTER' -%}
            FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
        {%- endif -%}
        {#- --- 条件必选：POLICYTYPE=WORKER 时必选 --- -#}
        {%- if item.POLICYTYPE == 'WORKER' -%}
            WORKERNAME="{{item.WORKERNAME}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.5 配置Userprofile。如已配置，请跳过本步骤。

```jinja2
{%- if is_scenario_rule_binding -%}
    {%- for item in add_userprofile_list_1 -%}
        ADD USERPROFILE:
        {#- --- 必选参数 --- -#}
        USERPROFILENAME="{{item.USERPROFILENAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.6 配置规则绑定Userprofile。

```jinja2
{%- if is_scenario_rule_binding -%}
    {%- for item in add_rulebinding_list_1 -%}
        ADD RULEBINDING:
        {#- --- 必选参数 --- -#}
        USERPROFILENAME="{{item.USERPROFILENAME}}",
        RULENAME="{{item.RULENAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.7 配置VXLAN隧道组绑定rule。

```jinja2
{%- if is_scenario_rule_binding -%}
    {%- for item in add_vxlanbindrule_list -%}
        ADD VXLANBINDRULE:
        {#- --- 必选参数 --- -#}
        RULENAME="{{item.RULENAME}}",
        VXLANGRPNAME="{{item.VXLANGRPNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.8 配置VPN+RULE到VNI的映射。

```jinja2
{%- if is_scenario_rule_binding -%}
    {%- for item in add_vpnvnimap_list_1 -%}
        ADD VPNVNIMAP:
        {#- --- 必选参数 --- -#}
        VPNINSTANCE="{{item.VPNINSTANCE}}",
        RULESWITCH={{item.RULESWITCH}},
        VNI={{item.VNI}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：RULESWITCH=ENABLE 时必选 --- -#}
        {%- if item.RULESWITCH == 'ENABLE' -%}
            RULENAME="{{item.RULENAME}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.9 开启流量转发开关。

```jinja2
{%- if is_scenario_rule_binding -%}
    {%- for item in set_apntrafdfunc_list_1 -%}
        SET APNTRAFDFUNC:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        TRAFFICFDSW={{item.TRAFFICFDSW}},
        ;
    {%- endfor -%}
{%- endif -%}
```

