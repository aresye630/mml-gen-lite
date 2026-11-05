---
id: ''
name: 部署UPF
ne_type: UDG
type: feature
description: 当前移动网络上承载的业务越来越丰富，运营商为了不断优化自身的服务及提升网络安全性，要求UPF能够根据数据包的分析（包括34层和7层的内容），按照预先定义的规则执行业务管理。UPF上该能力由SMF下发的Rule（规则）实现。  内容计费的配置需要做好规划，在PCF、SMF、UPF网元上统一进行配置，保证网元间配置的一致性。PCF、SMF、UPF上的配置及对应关系如图1所示。  **图1** PCF/SMF/UPF配置对应关系
risk_level: ''
doc_source: ["特性部署","业务专题","5G Core 计费解决方案","计费解决方案概述","计费方案部署与调测","方案五：部署NCG且融合接口计费组网方案（N40接口+传统Ga/Gy接口）","部署UPF"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当前移动网络上承载的业务越来越丰富，运营商为了不断优化自身的服务及提升网络安全性，要求UPF能够根据数据包的分析（包括34层和7层的内容），按照预先定义的规则执行业务管理。UPF上该能力由SMF下发的Rule（规则）实现。内容计费的配置需要做好规划，在PCF、SMF、UPF网元上统一进行配置，保证网元间配置的一致性。PCF、SMF、UPF上的配置及对应关系如图1所示。**图1** PCF/SMF/UPF配置对应关系

## 必备事项
前提条件

* 请仔细阅读融合计费原理。
* 完成加载License。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_urr_list:
      type: items
      properties:
        URRNAME:
          name: '使用量上报规则名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '配置业务离线计费URR。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        URRID:
          name: 'URR标识'
          type: integer
          minimum: 0
          maximum: 2147483646
          required: true
          description: 'URRID、USAGERPTMODE、OFFMETERINGTYPE在SMF和UPF上的配置需要保持一致。  此处以按流量计费为例。'
          data_source: ''
          pattern: ''
          default: ''
        USAGERPTMODE:
          name: '使用量上报模式'
          type: string
          enum:
          - MONITORINGKEY
          - OFFLINE
          - ONLINE
          - QOS
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OFFMETERINGTYPE:
          name: '离线计费统计类型'
          type: string
          enum:
          - EVENT
          - EVENT_TIME
          - EVENT_VOLUME
          - EVENT_VOLUME_TIME
          - FREE
          - TIME
          - VOLUME
          - VOLUME_TIME
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: VOLUME
        ONLMETERINGTYPE:
          name: '在线计费统计类型'
          type: string
          enum:
          - EVENT
          - EVENT_TIME
          - EVENT_VOLUME
          - EVENT_VOLUME_TIME
          - FREE
          - TIME
          - VOLUME
          - VOLUME_TIME
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: VOLUME
        DFTQUOTAPARA:
          name: '默认流量配额的单位'
          type: string
          enum:
          - Byte
          - KByte
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: Byte
        DFTQUOTATIME:
          name: '默认时长配额（秒）'
          type: integer
          minimum:
          - 0
          - 4294967295
          maximum:
          - 3600
          - 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DFTQUOTAVOLUME:
          name: '默认流量配额'
          type: integer
          minimum:
          - 0
          - 1000
          maximum:
          - 0
          - 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RG:
          name: '计费组'
          type: integer
          minimum: 0
          maximum: 4294967294
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SID:
          name: '业务标识'
          type: integer
          minimum: 0
          maximum: 4294967294
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_urrgroup_list:
      type: items
      properties:
        URRGROUPNAME:
          name: '使用量上报规则组名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '配置URRGROUP。  说明：  URRGROUP下必须配置在线URR和离线URR，只配置一种计费模式且计费模式和用户的计费模式不匹配时无法计费。以下特殊场景除外：  当SMF使用融合计费时，SMF上的**SET USRPROFCHARGE** 、**SET APNCHARGECTRL**、**ADD CHARGEMETHOD**命令的“RGAPPLIED”配置为“DEFAULT”时，不能同时配置RG相同的离线和在线URR，否则会导致计费冲突。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        UPURRNAME1:
          name: '上行发起URR名称1'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '上下行业务触发使用的离线URR，已通过**ADD URR**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DOWNURRNAME1:
          name: '下行发起URR名称1'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UPURRNAME2:
          name: '上行发起URR名称2'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '上下行业务触发使用的在线URR，已通过**ADD URR**命令配置。'
          data_source: ''
          pattern: ''
          default: ''
        DOWNURRNAME2:
          name: '下行发起URR名称2'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_pccpolicygrp_list:
      type: items
      properties:
        PCCPOLICYGRPNM:
          name: 'PCC策略组名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '配置PCC业务策略组。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        URRGROUPNAME:
          name: 'URR组名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '已通过**ADD URRGROUP**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_pccpolicygrp_list_2:
      type: items
      properties:
        PCCPOLICYGRPNM:
          name: 'PCC策略组名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '配置PCC业务策略组。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        URRGROUPNAME:
          name: 'URR组名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '已通过**ADD URRGROUP**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SIGURRGRPNAME:
          name: '信令URR组名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '已通过**ADD URRGROUP**命令配置。'
          data_source: '已配置数据中获取'
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
          description: '配置过滤器名字。'
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
          description: '字符串类型。'
          data_source: ''
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
          description: '任意三四层协议。'
          data_source: ''
          pattern: ''
          default: ANY
        MSSTARTPORT:
          name: '手机起始端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: '设置手机起始端口号。该参数不大于手机结束端口号。'
          data_source: ''
          pattern: ''
          default: 0
        MSENDPORT:
          name: '手机结束端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: '设置手机结束端口号。该参数不小于手机起始端口号。'
          data_source: ''
          pattern: ''
          default: 65535
        SVRSTARTPORT:
          name: '服务器起始端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: '设置服务器起始端口号。该参数不大于服务器结束端口号。'
          data_source: ''
          pattern: ''
          default: 0
        SVRENDPORT:
          name: '服务器结束端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: '设置服务器结束端口号。该参数不小于服务器起始端口号。'
          data_source: ''
          pattern: ''
          default: 65535
        L34PROTNUM:
          name: '三四层协议数字类型'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_filteripv6_list:
      type: items
      properties:
        FILTERNAME:
          name: '过滤器名字'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '配置过滤器名字。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        L34PROTTYPEV6:
          name: '三四层IPv6协议输入类型'
          type: string
          enum:
          - NUMBER
          - STRING
          required: true
          description: '字符串类型。'
          data_source: ''
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
          description: '任意三四层协议。'
          data_source: ''
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
          description: '参数取值取决于服务器侧的IP地址配置模式。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        MSSTARTPORT:
          name: '手机起始端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        MSENDPORT:
          name: '手机结束端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 65535
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
        SVRIPV6:
          name: '服务器IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SVRIPV6MASKTYPE:
          name: '服务器IPv6地址掩码类型'
          type: string
          enum:
          - IPTYPE
          - LENGTHTYPE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SVRIPV6MASKLEN:
          name: '服务器IPv6地址掩码长度'
          type: integer
          minimum: 0
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        L34PROTNUM:
          name: '三四层协议数字类型'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DOMAINVALUE:
          name: '域名'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HOSTNAME:
          name: 'Host配置名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HOSTPRIORITY:
          name: 'Host优先级'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SVRIPLISTNAME:
          name: '服务器IP列表名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SVRIPV6MASK:
          name: '服务器IPv6地址反掩码'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_filteripv6_list_1:
      type: items
      properties:
        FILTERNAME:
          name: '过滤器名字'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '配置IPv6 any to any过滤器名字。UPF通过将用户上下行报文匹配filter，实现报文的过滤。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        L34PROTTYPEV6:
          name: '三四层IPv6协议输入类型'
          type: string
          enum:
          - NUMBER
          - STRING
          required: true
          description: '字符串类型。'
          data_source: ''
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
          description: '任意三四层协议。'
          data_source: ''
          pattern: ''
          default: ANY
        MSSTARTPORT:
          name: '手机起始端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: '设置手机起始端口号。该参数不大于手机结束端口号。'
          data_source: ''
          pattern: ''
          default: 0
        MSENDPORT:
          name: '手机结束端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: '设置手机结束端口号。该参数不小于手机起始端口号。'
          data_source: ''
          pattern: ''
          default: 65535
        SVRSTARTPORT:
          name: '服务器起始端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: '设置服务器起始端口号。该参数不大于服务器结束端口号。'
          data_source: ''
          pattern: ''
          default: 0
        SVRENDPORT:
          name: '服务器结束端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: '设置服务器结束端口号。该参数不小于服务器起始端口号。'
          data_source: ''
          pattern: ''
          default: 65535
        L34PROTNUM:
          name: '三四层协议数字类型'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_l7filter_list:
      type: items
      properties:
        L7FILTERNAME:
          name: '七层过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '配置七层过滤器。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SUBL7FLTNAME:
          name: '子七层过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '配置该L7Filter的子七层过滤器名称。'
          data_source: ''
          pattern: ''
          default: ''
        URLTYPE:
          name: 'URL类型'
          type: string
          enum:
          - HOST
          - URL
          required: false
          description: '指定七层URL配置类型。  防欺诈功能开启时，RULE下绑定URL类型的7层filter时必须同时绑定三四层filter；防欺诈未开启时，RULE下可仅绑定URL类型的7层filter。'
          data_source: ''
          pattern: ''
          default: URL
        URL:
          name: 'URL'
          type: string
          minLength: 0
          maxLength: 119
          required: false
          description: '-'
          data_source: ''
          pattern: ''
          default: ''
        HOST:
          name: 'HOST'
          type: string
          minLength: 0
          maxLength: 119
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_flowfilter_list:
      type: items
      properties:
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '配置流过滤器。FLOWFILTER必须绑定过滤条件，否则该FLOWFILTER匹配失败，对应的Rule为无效配置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_fltbindflowf_list:
      type: items
      properties:
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '绑定的流过滤器已通过**ADD FLOWFILTER**命令配置。'
          data_source: ''
          pattern: ''
          default: ''
        FILTERNAME:
          name: '过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '绑定的三四层过滤条件已通过**ADD FILTER**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_protbindflowf_list:
      type: items
      properties:
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '绑定的流过滤器已通过**ADD FLOWFILTER**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PROTOCOLNAME:
          name: '协议名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        L7FILTERNAME:
          name: '七层过滤器名字'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: '绑定的流过滤器已通过**ADD L7FILTER**命令配置。'
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
          description: '配置规则。SMF、UPF上RuleName以及RULE下配置的POLICYTYPE、POLICYNAME需要保持一致。'
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
          data_source: ''
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
          data_source: ''
          pattern: ''
          default: ''
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: '使用的Flow Filter已通过**ADD FLOWFILTER**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        POLICYNAME:
          name: '策略名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: '使用的PCC策略组已通过**ADD PCCPOLICYGRP**命令配置。'
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
          description: '数字越小优先级越高。只绑定三四层filter的RULE的优先级应该低于绑定7层filter的RULE的优先级。'
          data_source: '本端规划'
          pattern: ''
          default: 4294967295
        FLWFLTRGRPNAME:
          name: '流过滤器组名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ADCMUTEFLAG:
          name: 'ADC静默通知标识'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ENABLE
        ALGSWITCH:
          name: 'ALG功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        RDSTRIGGERFLAG:
          name: 'Radius消息触发标识'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        REDIRIPVERFLAG:
          name: 'IP重定向虚拟IP协议版本'
          type: string
          enum:
          - IPV4
          - IPV6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REMARKFPISEL:
          name: '重标记、FPI或SAI选择'
          type: string
          enum:
          - FPI
          - REMARK
          - REMARKANDFPI
          - SAI
          - REMARKANDSAI
          - FPIANDSAI
          - RMKFPISAI
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: REMARK
        SRVLBOFLAG:
          name: '本地业务分流标识'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        WORKERNAME:
          name: '通用Rule子策略名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        WORKERPARA:
          name: '通用策略参数'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: ''
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
          description: 'USERPROFILE的名称统一规划，保证在PCF、SMF、UPF间名称一致。不一致时PCF下发的策略无法生效。'
          data_source: '本端规划'
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
          description: '已通过**ADD USERPROFILE**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        RULENAME:
          name: '规则名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '已通过**ADD RULE**命令配置。  SMF、UPF上USERPROFILE下绑定的RULENAME、POLICYTYPE需要保持一致。不一致策略无法按照预期生效。'
          data_source: ''
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
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_urrgrpbinding_list:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '已通过**ADD USERPROFILE**命令配置生成。  说明：  USERPROFILE需要将缺省业务和缺省信令的URR组都配置完整，不配置时按照RULE没有匹配到URR的报文无法计费。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DFTURRGRPNAME:
          name: '缺省URR组名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '已通过**ADD URRGROUP**命令配置生成。'
          data_source: ''
          pattern: ''
          default: ''
        DFTSIGURRGNAME:
          name: '缺省信令URR组名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '已通过**ADD URRGROUP**命令配置生成。'
          data_source: ''
          pattern: ''
          default: ''
        GLBDFTURRGSW:
          name: '继承全局缺省URR组配置开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '已通过**SET SPECTRAFURRGRP**命令配置生成。'
          data_source: ''
          pattern: ''
          default: ''
        GLBDFTSIGURRGSW:
          name: '继承全局缺省信令URR组开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '已通过**SET SPECTRAFURRGRP**命令配置生成。'
          data_source: ''
          pattern: ''
          default: ''
    set_spectrafurrgrp_list:
      type: items
      properties:
        URRGROUPNAME:
          name: '特殊流量使用量上报规则组名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '该参数使用**ADD URRGROUP**命令配置生成。  说明：  * BIT1232软参值设置为1时，特殊流量通过该规则组进行计费。特殊流量是指当某些业务报文丢失，未能完成七层精确匹配时，已经转发的流量。 例如，在线计费用户下线时，业务流只有信令报文，没有业务报文。在这种场景下，已经转发的信令报文的流量称为特殊流量。 * 对于没有配置任何URR的业务场景，通过该URR组进行计费。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_specurrgrplist_list:
      type: items
      properties:
        URRGROUPNAME:
          name: 'URR组名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '配置防欺诈URR列表。对有欺诈风险的费率，将费率加入防欺诈费率列表。'
          data_source: '已配置数据中获取'
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
          description: '刷新Filter。'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    add_urr_list:
    - URRNAME: 'urr_offline_URL'
      URRID: 12500
      USAGERPTMODE: OFFLINE
      OFFMETERINGTYPE: VOLUME
      ONLMETERINGTYPE: VOLUME
      DFTQUOTAPARA: Byte
      DFTQUOTATIME: ''
      DFTQUOTAVOLUME: ''
      RG: ''
      SID: ''
    - URRNAME: 'urr_offline_IMS'
      URRID: 13500
      USAGERPTMODE: OFFLINE
      OFFMETERINGTYPE: VOLUME
      ONLMETERINGTYPE: VOLUME
      DFTQUOTAPARA: ''
      DFTQUOTATIME: ''
      DFTQUOTAVOLUME: ''
      RG: ''
      SID: ''
    - URRNAME: 'urr_offline_any'
      URRID: 11500
      USAGERPTMODE: OFFLINE
      OFFMETERINGTYPE: VOLUME
      ONLMETERINGTYPE: VOLUME
      DFTQUOTAPARA: ''
      DFTQUOTATIME: ''
      DFTQUOTAVOLUME: ''
      RG: ''
      SID: ''
    - URRNAME: 'URR_abnormal_offline'
      URRID: 14500
      USAGERPTMODE: OFFLINE
      OFFMETERINGTYPE: FREE
      ONLMETERINGTYPE: FREE
      DFTQUOTAPARA: ''
      DFTQUOTATIME: ''
      DFTQUOTAVOLUME: ''
      RG: ''
      SID: ''
    add_urrgroup_list:
    - URRGROUPNAME: 'UrrGp_URL'
      UPURRNAME1: 'urr_offline_URL'
      DOWNURRNAME1: 'urr_offline_URL'
      UPURRNAME2: 'urr_online_URL'
      DOWNURRNAME2: 'urr_online_URL'
    - URRGROUPNAME: 'UrrGp_IMS'
      UPURRNAME1: 'urr_offline_IMS'
      DOWNURRNAME1: 'urr_offline_IMS'
      UPURRNAME2: 'urr_online_IMS'
      DOWNURRNAME2: 'urr_online_IMS'
    - URRGROUPNAME: 'UrrGp_any'
      UPURRNAME1: 'urr_offline_any'
      DOWNURRNAME1: 'urr_offline_any'
      UPURRNAME2: 'urr_online_any'
      DOWNURRNAME2: 'urr_online_any'
    - URRGROUPNAME: 'UrrGp_abnormal'
      UPURRNAME1: 'URR_abnormal_offline'
      DOWNURRNAME1: 'URR_abnormal_offline'
      UPURRNAME2: 'URR_abnormal_online'
      DOWNURRNAME2: 'URR_abnormal_online'
    add_pccpolicygrp_list:
    - PCCPOLICYGRPNM: 'PPG_URL'
      URRGROUPNAME: 'UrrGp_URL'
    - PCCPOLICYGRPNM: 'PPG_IMS'
      URRGROUPNAME: 'UrrGp_IMS'
    add_pccpolicygrp_list_2:
    - PCCPOLICYGRPNM: 'PPG_any'
      URRGROUPNAME: 'UrrGp_any'
      SIGURRGRPNAME: 'UrrGp_abnormal'
    add_filter_list:
    - FILTERNAME: 'L34_any'
      L34PROTTYPE: STRING
      L34PROTOCOL: ANY
      MSSTARTPORT: 0
      MSENDPORT: 65535
      SVRSTARTPORT: 0
      SVRENDPORT: 65535
      L34PROTNUM: ''
    add_filteripv6_list:
    - FILTERNAME: 'ipv6_ims'
      L34PROTTYPEV6: STRING
      L34PROTOCOL: ANY
      SVRIPMODE: IP
      MSSTARTPORT: 0
      MSENDPORT: 65535
      SVRSTARTPORT: 0
      SVRENDPORT: 65535
      SVRIPV6: 'fc00:8028:5002:10D::181'
      SVRIPV6MASKTYPE: LENGTHTYPE
      SVRIPV6MASKLEN: 128
      L34PROTNUM: ''
      DOMAINVALUE: ''
      HOSTNAME: ''
      HOSTPRIORITY: ''
      SVRIPLISTNAME: ''
      SVRIPV6MASK: ''
    add_filteripv6_list_1:
    - FILTERNAME: 'L34_any_ipv6'
      L34PROTTYPEV6: STRING
      L34PROTOCOL: ANY
      MSSTARTPORT: 0
      MSENDPORT: 65535
      SVRSTARTPORT: 0
      SVRENDPORT: 65535
      L34PROTNUM: ''
    add_l7filter_list:
    - L7FILTERNAME: 'L7_URL'
      SUBL7FLTNAME: 'http'
      URLTYPE: URL
      URL: 'www.huawei.com'
      HOST: ''
    add_flowfilter_list:
    - FLOWFILTERNAME: 'ff_L7'
    add_fltbindflowf_list:
    - FLOWFILTERNAME: 'ff_L7'
      FILTERNAME: 'L34_any'
    add_protbindflowf_list:
    - FLOWFILTERNAME: 'ff_L7'
      PROTOCOLNAME: 'http'
      L7FILTERNAME: 'L7_URL'
    add_rule_list:
    - RULENAME: 'Rule001_url'
      POLICYTYPE: PCC
      FILTERINGMODE: FLOWFILTER
      FLOWFILTERNAME: 'ff_L7'
      POLICYNAME: 'PPG_URL'
      PRIORITY: 100
      FLWFLTRGRPNAME: ''
      ADCMUTEFLAG: ENABLE
      ALGSWITCH: DISABLE
      RDSTRIGGERFLAG: DISABLE
      REDIRIPVERFLAG: ''
      REMARKFPISEL: REMARK
      SRVLBOFLAG: DISABLE
      WORKERNAME: ''
      WORKERPARA: ''
    add_userprofile_list:
    - USERPROFILENAME: 'userprofile001'
    add_rulebinding_list:
    - USERPROFILENAME: 'userprofile001'
      RULENAME: 'Rule001_url'
      POLICYTYPE: PCC
    set_urrgrpbinding_list:
    - USERPROFILENAME: 'userprofile001'
      DFTURRGRPNAME: 'UrrGp_any'
      DFTSIGURRGNAME: 'UrrGp_abnormal'
      GLBDFTURRGSW: ENABLE
      GLBDFTSIGURRGSW: ENABLE
    set_spectrafurrgrp_list:
    - URRGROUPNAME: 'UrrGp_abnormal'
    add_specurrgrplist_list:
    - URRGROUPNAME: 'UrrGp_URL'
    set_refreshsrv_list:
    - REFRESHTYPE: ALL
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置使用量上报规则组属性。

#### 1.1 配置URR。

##### 1.1.1 //配置网址是www.huawei.com的网站业务的URR。

```jinja2
{%- for item in add_urr_list -%}
    ADD URR:
    {#- --- 必选参数 --- -#}
    URRNAME="{{item.URRNAME}}",
    URRID={{item.URRID}},
    USAGERPTMODE={{item.USAGERPTMODE}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：USAGERPTMODE=OFFLINE 时可选 --- -#}
    {%- if item.USAGERPTMODE == 'OFFLINE' -%}
        {%- if item.OFFMETERINGTYPE is not none -%}
            OFFMETERINGTYPE={{item.OFFMETERINGTYPE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：USAGERPTMODE=ONLINE 时可选 --- -#}
    {%- if item.USAGERPTMODE == 'ONLINE' -%}
        {%- if item.ONLMETERINGTYPE is not none -%}
            ONLMETERINGTYPE={{item.ONLMETERINGTYPE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：USAGERPTMODE=ONLINE 时可选 --- -#}
    {%- if item.USAGERPTMODE == 'ONLINE' -%}
        {%- if item.DFTQUOTAPARA is not none -%}
            DFTQUOTAPARA={{item.DFTQUOTAPARA}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：USAGERPTMODE=ONLINE 时可选 --- -#}
    {%- if item.USAGERPTMODE == 'ONLINE' -%}
        {%- if item.DFTQUOTATIME is not none -%}
            DFTQUOTATIME={{item.DFTQUOTATIME}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：USAGERPTMODE=ONLINE 时可选 --- -#}
    {%- if item.USAGERPTMODE == 'ONLINE' -%}
        {%- if item.DFTQUOTAVOLUME is not none -%}
            DFTQUOTAVOLUME={{item.DFTQUOTAVOLUME}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：USAGERPTMODE=ONLINE/OFFLINE 时可选 --- -#}
    {%- if item.USAGERPTMODE in ['ONLINE', 'OFFLINE'] -%}
        {%- if item.RG is not none -%}
            RG={{item.RG}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：USAGERPTMODE=ONLINE/OFFLINE 时可选 --- -#}
    {%- if item.USAGERPTMODE in ['ONLINE', 'OFFLINE'] -%}
        {%- if item.SID is not none -%}
            SID={{item.SID}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.2 配置URR组。

##### 1.2.1 //配置网址是www.huawei.com的网站的URRGROUP。

```jinja2
{%- for item in add_urrgroup_list -%}
    ADD URRGROUP:
    {#- --- 必选参数 --- -#}
    URRGROUPNAME="{{item.URRGROUPNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.UPURRNAME1 is not none -%}
        UPURRNAME1="{{item.UPURRNAME1}}",
    {%- endif -%}
    {%- if item.DOWNURRNAME1 is not none -%}
        DOWNURRNAME1="{{item.DOWNURRNAME1}}",
    {%- endif -%}
    {%- if item.UPURRNAME2 is not none -%}
        UPURRNAME2="{{item.UPURRNAME2}}",
    {%- endif -%}
    {%- if item.DOWNURRNAME2 is not none -%}
        DOWNURRNAME2="{{item.DOWNURRNAME2}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 配置PCC策略组，并与PCC动作属性、URR组绑定。

#### 2.1 //配置网址是www.huawei.com的网站的PCC业务策略组，绑定URRGROUP。

```jinja2
{%- for item in add_pccpolicygrp_list -%}
    ADD PCCPOLICYGRP:
    {#- --- 必选参数 --- -#}
    PCCPOLICYGRPNM="{{item.PCCPOLICYGRPNM}}",
    {#- --- 可选参数 --- -#}
    {%- if item.URRGROUPNAME is not none -%}
        URRGROUPNAME="{{item.URRGROUPNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.3 //访问除了上述两种情况外的基础业务的PCC业务策略组，绑定URRGROUP。

```jinja2
{%- for item in add_pccpolicygrp_list_2 -%}
    ADD PCCPOLICYGRP:
    {#- --- 必选参数 --- -#}
    PCCPOLICYGRPNM="{{item.PCCPOLICYGRPNM}}",
    {#- --- 可选参数 --- -#}
    {%- if item.URRGROUPNAME is not none -%}
        URRGROUPNAME="{{item.URRGROUPNAME}}",
    {%- endif -%}
    {%- if item.SIGURRGRPNAME is not none -%}
        SIGURRGRPNAME="{{item.SIGURRGRPNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置过滤条件。

#### 3.1 配置三四层过滤条件。

```jinja2
{%- for item in add_filter_list -%}
    ADD FILTER:
    {#- --- 必选参数 --- -#}
    FILTERNAME="{{item.FILTERNAME}}",
    L34PROTTYPE={{item.L34PROTTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.MSSTARTPORT is not none -%}
        MSSTARTPORT={{item.MSSTARTPORT}},
    {%- endif -%}
    {%- if item.MSENDPORT is not none -%}
        MSENDPORT={{item.MSENDPORT}},
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
    {#- --- 条件必选：L34PROTTYPE=NUMBER 时必选 --- -#}
    {%- if item.L34PROTTYPE == 'NUMBER' -%}
        L34PROTNUM={{item.L34PROTNUM}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_filteripv6_list -%}
    ADD FILTERIPV6:
    {#- --- 必选参数 --- -#}
    FILTERNAME="{{item.FILTERNAME}}",
    L34PROTTYPEV6={{item.L34PROTTYPEV6}},
    {#- --- 可选参数 --- -#}
    {%- if item.SVRIPMODE is not none -%}
        SVRIPMODE={{item.SVRIPMODE}},
    {%- endif -%}
    {%- if item.MSSTARTPORT is not none -%}
        MSSTARTPORT={{item.MSSTARTPORT}},
    {%- endif -%}
    {%- if item.MSENDPORT is not none -%}
        MSENDPORT={{item.MSENDPORT}},
    {%- endif -%}
    {%- if item.SVRSTARTPORT is not none -%}
        SVRSTARTPORT={{item.SVRSTARTPORT}},
    {%- endif -%}
    {%- if item.SVRENDPORT is not none -%}
        SVRENDPORT={{item.SVRENDPORT}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：L34PROTTYPEV6=STRING 时必选 --- -#}
    {%- if item.L34PROTTYPEV6 == 'STRING' -%}
        L34PROTOCOL={{item.L34PROTOCOL}},
    {%- endif -%}
    {#- --- 条件必选：SVRIPMODE=IP 时必选 --- -#}
    {%- if item.SVRIPMODE == 'IP' -%}
        SVRIPV6="{{item.SVRIPV6}}",
    {%- endif -%}
    {#- --- 条件必选：SVRIPMODE=IP 时必选 --- -#}
    {%- if item.SVRIPMODE == 'IP' -%}
        SVRIPV6MASKTYPE={{item.SVRIPV6MASKTYPE}},
    {%- endif -%}
    {#- --- 条件必选：SVRIPV6MASKTYPE=LENGTHTYPE 时必选 --- -#}
    {%- if item.SVRIPV6MASKTYPE == 'LENGTHTYPE' -%}
        SVRIPV6MASKLEN={{item.SVRIPV6MASKLEN}},
    {%- endif -%}
    {#- --- 条件必选：SVRIPMODE=DOMAIN 时必选 --- -#}
    {%- if item.SVRIPMODE == 'DOMAIN' -%}
        DOMAINVALUE="{{item.DOMAINVALUE}}",
    {%- endif -%}
    {#- --- 条件必选：SVRIPMODE=HOSTNAME/DOMAIN 时必选 --- -#}
    {%- if item.SVRIPMODE in ['HOSTNAME', 'DOMAIN'] -%}
        HOSTNAME="{{item.HOSTNAME}}",
    {%- endif -%}
    {#- --- 条件必选：L34PROTTYPEV6=NUMBER 时必选 --- -#}
    {%- if item.L34PROTTYPEV6 == 'NUMBER' -%}
        L34PROTNUM={{item.L34PROTNUM}},
    {%- endif -%}
    {#- --- 条件必选：SVRIPMODE=IPLIST 时必选 --- -#}
    {%- if item.SVRIPMODE == 'IPLIST' -%}
        SVRIPLISTNAME="{{item.SVRIPLISTNAME}}",
    {%- endif -%}
    {#- --- 条件必选：SVRIPV6MASKTYPE=IPTYPE 时必选 --- -#}
    {%- if item.SVRIPV6MASKTYPE == 'IPTYPE' -%}
        SVRIPV6MASK="{{item.SVRIPV6MASK}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：SVRIPMODE=DOMAIN 时可选 --- -#}
    {%- if item.SVRIPMODE == 'DOMAIN' -%}
        {%- if item.HOSTPRIORITY is not none -%}
            HOSTPRIORITY={{item.HOSTPRIORITY}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_filteripv6_list_1 -%}
    ADD FILTERIPV6:
    {#- --- 必选参数 --- -#}
    FILTERNAME="{{item.FILTERNAME}}",
    L34PROTTYPEV6={{item.L34PROTTYPEV6}},
    {#- --- 可选参数 --- -#}
    {%- if item.MSSTARTPORT is not none -%}
        MSSTARTPORT={{item.MSSTARTPORT}},
    {%- endif -%}
    {%- if item.MSENDPORT is not none -%}
        MSENDPORT={{item.MSENDPORT}},
    {%- endif -%}
    {%- if item.SVRSTARTPORT is not none -%}
        SVRSTARTPORT={{item.SVRSTARTPORT}},
    {%- endif -%}
    {%- if item.SVRENDPORT is not none -%}
        SVRENDPORT={{item.SVRENDPORT}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：L34PROTTYPEV6=STRING 时必选 --- -#}
    {%- if item.L34PROTTYPEV6 == 'STRING' -%}
        L34PROTOCOL={{item.L34PROTOCOL}},
    {%- endif -%}
    {#- --- 条件必选：L34PROTTYPEV6=NUMBER 时必选 --- -#}
    {%- if item.L34PROTTYPEV6 == 'NUMBER' -%}
        L34PROTNUM={{item.L34PROTNUM}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 3.2 配置七层过滤条件。

```jinja2
{%- for item in add_l7filter_list -%}
    ADD L7FILTER:
    {#- --- 必选参数 --- -#}
    L7FILTERNAME="{{item.L7FILTERNAME}}",
    SUBL7FLTNAME="{{item.SUBL7FLTNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.URLTYPE is not none -%}
        URLTYPE={{item.URLTYPE}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：URLTYPE=URL 时可选 --- -#}
    {%- if item.URLTYPE == 'URL' -%}
        {%- if item.URL is not none -%}
            URL="{{item.URL}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：URLTYPE=HOST 时可选 --- -#}
    {%- if item.URLTYPE == 'HOST' -%}
        {%- if item.HOST is not none -%}
            HOST="{{item.HOST}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 配置流过滤器。

```jinja2
{%- for item in add_flowfilter_list -%}
    ADD FLOWFILTER:
    {#- --- 必选参数 --- -#}
    FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
    ;
{%- endfor -%}
```

### 5 将流过滤器与过滤条件绑定。

#### 5.1 将已配置的三四层过滤条件与流过滤器绑定。

```jinja2
{%- for item in add_fltbindflowf_list -%}
    ADD FLTBINDFLOWF:
    {#- --- 必选参数 --- -#}
    FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
    FILTERNAME="{{item.FILTERNAME}}",
    ;
{%- endfor -%}
```

#### 5.2 将已配置的七层过滤条件、协议与流过滤器绑定。

```jinja2
{%- for item in add_protbindflowf_list -%}
    ADD PROTBINDFLOWF:
    {#- --- 必选参数 --- -#}
    FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
    PROTOCOLNAME="{{item.PROTOCOLNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.L7FILTERNAME is not none -%}
        L7FILTERNAME="{{item.L7FILTERNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 6 添加规则，并与PCC策略组和流过滤器绑定。

#### 6.1 //只绑定三四层filter的RULE的优先级应该低于绑定7层filter的RULE的优先级。过滤条件为any的RULE，优先级设置为最低。

```jinja2
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
    {#- --- 条件必选：POLICYTYPE=PCC/BWM/HEADEN/SMARTREDIRECT/TRAFFICCLASS/FIREWALL/QOS/WEBPROXY 时必选 --- -#}
    {%- if item.POLICYTYPE in ['PCC', 'BWM', 'HEADEN', 'SMARTREDIRECT', 'TRAFFICCLASS', 'FIREWALL', 'QOS', 'WEBPROXY'] -%}
        POLICYNAME="{{item.POLICYNAME}}",
    {%- endif -%}
    {#- --- 条件必选：POLICYTYPE=ADC 时必选 --- -#}
    {%- if item.POLICYTYPE == 'ADC' -%}
        ADCMUTEFLAG={{item.ADCMUTEFLAG}},
    {%- endif -%}
    {#- --- 条件必选：FILTERINGMODE=FLOWFILTERGRP 时必选 --- -#}
    {%- if item.FILTERINGMODE == 'FLOWFILTERGRP' -%}
        FLWFLTRGRPNAME="{{item.FLWFLTRGRPNAME}}",
    {%- endif -%}
    {#- --- 条件必选：POLICYTYPE=SRV_TRIGGER 时必选 --- -#}
    {%- if item.POLICYTYPE == 'SRV_TRIGGER' -%}
        RDSTRIGGERFLAG={{item.RDSTRIGGERFLAG}},
    {%- endif -%}
    {#- --- 条件必选：POLICYTYPE=IPREDIR 时必选 --- -#}
    {%- if item.POLICYTYPE == 'IPREDIR' -%}
        REDIRIPVERFLAG={{item.REDIRIPVERFLAG}},
    {%- endif -%}
    {#- --- 条件必选：POLICYTYPE=REMARK_FPI 时必选 --- -#}
    {%- if item.POLICYTYPE == 'REMARK_FPI' -%}
        REMARKFPISEL={{item.REMARKFPISEL}},
    {%- endif -%}
    {#- --- 条件必选：POLICYTYPE=LBO 时必选 --- -#}
    {%- if item.POLICYTYPE == 'LBO' -%}
        SRVLBOFLAG={{item.SRVLBOFLAG}},
    {%- endif -%}
    {#- --- 条件必选：POLICYTYPE=WORKER 时必选 --- -#}
    {%- if item.POLICYTYPE == 'WORKER' -%}
        WORKERNAME="{{item.WORKERNAME}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：POLICYTYPE=WEBPROXY 时可选 --- -#}
    {%- if item.POLICYTYPE == 'WEBPROXY' -%}
        {%- if item.ALGSWITCH is not none -%}
            ALGSWITCH={{item.ALGSWITCH}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：POLICYTYPE=WORKER 时可选 --- -#}
    {%- if item.POLICYTYPE == 'WORKER' -%}
        {%- if item.WORKERPARA is not none -%}
            WORKERPARA="{{item.WORKERPARA}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 7 添加User Profile。

```jinja2
{%- for item in add_userprofile_list -%}
    ADD USERPROFILE:
    {#- --- 必选参数 --- -#}
    USERPROFILENAME="{{item.USERPROFILENAME}}",
    ;
{%- endfor -%}
```

### 8 将规则与User Profile绑定。

```jinja2
{%- for item in add_rulebinding_list -%}
    ADD RULEBINDING:
    {#- --- 必选参数 --- -#}
    USERPROFILENAME="{{item.USERPROFILENAME}}",
    RULENAME="{{item.RULENAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.POLICYTYPE is not none -%}
        POLICYTYPE={{item.POLICYTYPE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 9 配置缺省URR组。

```jinja2
{%- for item in set_urrgrpbinding_list -%}
    SET URRGRPBINDING:
    {#- --- 必选参数 --- -#}
    USERPROFILENAME="{{item.USERPROFILENAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.DFTURRGRPNAME is not none -%}
        DFTURRGRPNAME="{{item.DFTURRGRPNAME}}",
    {%- endif -%}
    {%- if item.DFTSIGURRGNAME is not none -%}
        DFTSIGURRGNAME="{{item.DFTSIGURRGNAME}}",
    {%- endif -%}
    {%- if item.GLBDFTURRGSW is not none -%}
        GLBDFTURRGSW={{item.GLBDFTURRGSW}},
    {%- endif -%}
    {%- if item.GLBDFTSIGURRGSW is not none -%}
        GLBDFTSIGURRGSW={{item.GLBDFTSIGURRGSW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 10 配置全局缺省URR组。

```jinja2
{%- for item in set_spectrafurrgrp_list -%}
    SET SPECTRAFURRGRP:
    {#- --- 必选参数 --- -#}
    URRGROUPNAME="{{item.URRGROUPNAME}}",
    ;
{%- endfor -%}
```

### 11 配置防欺诈URR列表。

```jinja2
{%- for item in add_specurrgrplist_list -%}
    ADD SPECURRGRPLIST:
    {#- --- 必选参数 --- -#}
    URRGROUPNAME="{{item.URRGROUPNAME}}",
    ;
{%- endfor -%}
```

### 12 将新配置的Filter置为生效。

```jinja2
{%- for item in set_refreshsrv_list -%}
    SET REFRESHSRV:
    {#- --- 必选参数 --- -#}
    REFRESHTYPE={{item.REFRESHTYPE}},
    ;
{%- endfor -%}
```

