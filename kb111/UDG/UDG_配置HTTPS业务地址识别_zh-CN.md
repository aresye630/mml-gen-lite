---
id: GWFD-110203
name: 配置HTTPS业务地址识别
ne_type: UDG
type: feature
description: 适用于PGW-U、UPF。  当用户访问的业务采用HTTPS协议承载时，需要部署HTTPS业务地址识别特性，对业务实施计费与策略控制。  UDG SSL/TLS证书识别HTTPS应用不需要配置，版本默认支持。
risk_level: ''
doc_source: ["特性部署","特性指南","UDG特性指南","业务感知功能","GWFD-110203 HTTPS业务地址识别","配置HTTPS业务地址识别"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
适用于PGW-U、UPF。当用户访问的业务采用HTTPS协议承载时，需要部署HTTPS业务地址识别特性，对业务实施计费与策略控制。UDG SSL/TLS证书识别HTTPS应用不需要配置，版本默认支持。

## 必备事项
前提条件

* 请仔细阅读GWFD-110203 HTTPS业务地址识别。
* 完成加载license（如果有需求，请联系华为技术支持工程师处理）。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    set_licenseswitch_list:
      type: items
      properties:
        LICITEM:
          name: 'License项'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SWITCH:
          name: '开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_urr_list:
      type: items
      properties:
        URRNAME:
          name: '使用量上报规则名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '使用量上报规则信息，要求UDG和CG两端的费率标识的粒度和取值要一致。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        URRID:
          name: 'URR标识'
          type: integer
          minimum: 0
          maximum: 2147483646
          required: true
          description: ''
          data_source: '全网规划'
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
          data_source: '全网规划'
          pattern: ''
          default: ''
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
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPURRNAME1:
          name: '上行发起URR名称1'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '上行业务触发使用的URRName，已通过**ADD URR**命令配置完成。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DOWNURRNAME1:
          name: '下行发起URR名称1'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '下行业务触发使用的URRName，已通过**ADD URR**命令配置完成。'
          data_source: '已配置数据中获取'
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
          description: 'PCC策略组。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        URRGROUPNAME:
          name: '使用量上报规则组名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: 'PCC策略组绑定的使用量上报规则组，已通过**ADD URRGROUP**命令配置完成。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_host_list:
      type: items
      properties:
        HOSTNAME:
          name: 'Host配置名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '配置Host后，UDG会解析DNS响应报文，得到Host中的Domain和Server IP的对应关系，然后把Filter中的Host替换成真正的Server IP，用于后续业务数据流匹配。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DOMAINVALUE:
          name: '域名'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
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
          description: '三四层过滤条件。  其中Host配置由**ADD HOST**命令配置。'
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
        HOSTNAME:
          name: 'Host配置名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SVRSTARTPORT:
          name: '服务器起始端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 0
        SVRENDPORT:
          name: '服务器结束端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: '本端规划'
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
        SVRIP:
          name: '服务器IP地址'
          type: string
          maxLength: 15
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
        SVRIPMASKTYPE:
          name: '服务器IP地址掩码类型'
          type: string
          enum:
          - IPTYPE
          - LENGTHTYPE
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
          description: '流分类器。'
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
          description: '绑定的流过滤器已通过**ADD FLOWFILTER**命令配置'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        FILTERNAME:
          name: '过滤器名字'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '绑定的三四层过滤条件已通过**ADD FILTER**命令配置，可以通过**LST FILTER**命令查询。'
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
          description: '业务策略规则。'
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
          data_source: '本端规划'
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
          description: '绑定的-FlowFilter已通过**ADD FLOWFILTER**命令配置，可以通过**LST FLOWFILTER**命令查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        POLICYNAME:
          name: '策略名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: '绑定的PCC策略组已通过**ADD PCCPOLICYGRP**命令配置，可以通过**LST PCCPOLICYGRP**命令查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PRIORITY:
          name: '全局优先级'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
          description: '指定Rule的优先级。'
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
    add_filter_list_1:
      type: items
      properties:
        FILTERNAME:
          name: '过滤器名字'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '三四层过滤条件。'
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
        SVRSTARTPORT:
          name: '服务器起始端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 0
        SVRENDPORT:
          name: '服务器结束端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: '本端规划'
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
          description: '七层过滤条件。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SUBL7FLTNAME:
          name: '子七层过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        URL:
          name: 'URL'
          type: string
          minLength: 0
          maxLength: 119
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        URLTYPE:
          name: 'URL类型'
          type: string
          enum:
          - HOST
          - URL
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: URL
    add_flowfilter_list_1:
      type: items
      properties:
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '流分类器。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_fltbindflowf_list_1:
      type: items
      properties:
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '绑定的流过滤器已通过**ADD FLOWFILTER**命令配'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        FILTERNAME:
          name: '过滤器名字'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '绑定的三四层过滤条件已通过**ADD FILTER**命令配置，可以通过**LST FILTER**命令查询。'
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
          description: '用于将指定L7Filter绑定到指定的FlowFilter。  使用的“FLOWFILTERNAME”，已通过**ADD FLOWFILTER**命令配置完成。'
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
          description: '绑定的七层过滤条件已通过**ADD L7FILTER**命令配置，可以通过**LST L7FILTER**命令查询。'
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
          description: '业务策略规则。'
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
          data_source: '本端规划'
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
          description: '绑定的FlowFilter已通过**ADD FLOWFILTER**命令配置，可以通过**LST FLOWFILTER**命令查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        POLICYNAME:
          name: '策略名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: '绑定的PCC策略组已通过**ADD PCCPOLICYGRP**命令配置，可以通过**LST PCCPOLICYGRP**命令查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PRIORITY:
          name: '全局优先级'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
          description: '指定Rule的优先级。'
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
    add_wellknownport_list:
      type: items
      properties:
        IDENPROTNAME:
          name: '知名端口名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '通过知名端口进行协议识别。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PROTOCOLNAME:
          name: '协议名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PORTOP:
          name: '端口范围操作码'
          type: string
          enum:
          - EQUAL
          - GT
          - LT
          - RANGE
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        STARTPORT:
          name: '起始端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 1
          maximum: 65535
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ENDPORT:
          name: '结束端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    lod_signaturedb_list:
      type: items
      properties:
        LOADMODE:
          name: '特征库加载模式'
          type: string
          enum:
          - LATEST
          - REFRESH
          - SPECIFIC
          required: true
          description: '加载协议识别特征库。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        VERSION:
          name: '特征库版本号'
          type: string
          minLength: 0
          maxLength: 16
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    lod_parserdb_list:
      type: items
      properties:
        LOADMODE:
          name: '解析库加载模式'
          type: string
          enum:
          - LATEST
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_usrrelateiden_list:
      type: items
      properties:
        PROTOCOLNAME:
          name: '协议名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '指定开启用户关联识别功能的协议。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        USRRLTIDENSW:
          name: '用户关联识别开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: ''
          data_source: '本端规划'
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
          description: '-'
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
          description: '-'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        RULENAME:
          name: '规则名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: 'User Profile绑定的业务规则，已通过**ADD RULE**命令配置完成。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3G5HSAP01'
      SWITCH: ENABLE
    add_urr_list:
    - URRNAME: 'urr_https'
      URRID: 300
      USAGERPTMODE: OFFLINE
      DFTQUOTAPARA: Byte
      DFTQUOTATIME: ''
      DFTQUOTAVOLUME: ''
      OFFMETERINGTYPE: VOLUME
      ONLMETERINGTYPE: VOLUME
      RG: ''
      SID: ''
    add_urrgroup_list:
    - URRGROUPNAME: 'urrgp_https'
      UPURRNAME1: 'urr_https'
      DOWNURRNAME1: 'urr_https'
    add_pccpolicygrp_list:
    - PCCPOLICYGRPNM: 'pccpg_https'
      URRGROUPNAME: 'urrgp_https'
    add_host_list:
    - HOSTNAME: 'ht_https'
      DOMAINVALUE: 'www.example.com'
    add_filter_list:
    - FILTERNAME: 'filter_https'
      L34PROTTYPE: STRING
      L34PROTOCOL: ANY
      SVRIPMODE: HOSTNAME
      HOSTNAME: 'ht_https'
      SVRSTARTPORT: 443
      SVRENDPORT: 443
      L34PROTNUM: ''
      DOMAINVALUE: ''
      HOSTPRIORITY: ''
      SVRIP: ''
      SVRIPLISTNAME: ''
      SVRIPMASKTYPE: ''
    add_flowfilter_list:
    - FLOWFILTERNAME: 'ff_https'
    add_fltbindflowf_list:
    - FLOWFILTERNAME: 'ff_https'
      FILTERNAME: 'filter_https'
    add_rule_list:
    - RULENAME: 'rule_https'
      POLICYTYPE: PCC
      FILTERINGMODE: FLOWFILTER
      FLOWFILTERNAME: 'ff_https'
      POLICYNAME: 'pccpg_https'
      PRIORITY: 120
      FLWFLTRGRPNAME: ''
      ADCMUTEFLAG: ENABLE
      ALGSWITCH: DISABLE
      RDSTRIGGERFLAG: DISABLE
      REDIRIPVERFLAG: ''
      REMARKFPISEL: REMARK
      SRVLBOFLAG: DISABLE
      WORKERNAME: ''
      WORKERPARA: ''
    add_filter_list_1:
    - FILTERNAME: 'filter_dns'
      L34PROTTYPE: STRING
      L34PROTOCOL: UDP
      SVRSTARTPORT: 53
      SVRENDPORT: 53
      L34PROTNUM: ''
    add_l7filter_list:
    - L7FILTERNAME: 'l7f_dns'
      SUBL7FLTNAME: 'sl7_test'
      URL: '*/*'
      URLTYPE: URL
    add_flowfilter_list_1:
    - FLOWFILTERNAME: 'ff_dns'
    add_fltbindflowf_list_1:
    - FLOWFILTERNAME: 'ff_dns'
      FILTERNAME: 'filter_dns'
    add_protbindflowf_list:
    - FLOWFILTERNAME: 'ff_dns'
      PROTOCOLNAME: 'dns'
      L7FILTERNAME: 'l7f_dns'
    add_rule_list_1:
    - RULENAME: 'rule_dns'
      POLICYTYPE: PCC
      FILTERINGMODE: FLOWFILTER
      FLOWFILTERNAME: 'ff_dns'
      POLICYNAME: 'pccpg_https'
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
    set_refreshsrv_list:
    - REFRESHTYPE: USERPROFILE
    add_wellknownport_list:
    - IDENPROTNAME: 'port_dns'
      PROTOCOLNAME: 'dns'
      PORTOP: EQUAL
      STARTPORT: 53
      PRIORITY: 20
      ENDPORT: ''
    lod_signaturedb_list:
    - LOADMODE: LATEST
      VERSION: ''
    lod_parserdb_list:
    - LOADMODE: LATEST
    add_usrrelateiden_list:
    - PROTOCOLNAME: 'facebook'
      USRRLTIDENSW: ENABLE
    add_userprofile_list:
    - USERPROFILENAME: 'up_test'
    add_rulebinding_list:
    - USERPROFILENAME: 'up_test'
      RULENAME: 'rule_https'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 打开本特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 2 配置HTTPS报文的PCC策略组。

#### 2.1 配置URR。

```jinja2
{%- for item in add_urr_list -%}
    ADD URR:
    {#- --- 必选参数 --- -#}
    URRNAME="{{item.URRNAME}}",
    URRID={{item.URRID}},
    USAGERPTMODE={{item.USAGERPTMODE}},
    {#- --- 条件可选参数 --- -#}
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

#### 2.2 配置使用量上报组属性URRGROUP，包括上下行发起的业务对应的URR。

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
    ;
{%- endfor -%}
```

#### 2.3 配置PCC策略组，绑定步骤 2.b配置的使用量上报规则组。

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

### 3 配置HTTPS报文的解析规则。

#### 3.1 配置HTTPS业务的域名信息。

```jinja2
{%- for item in add_host_list -%}
    ADD HOST:
    {#- --- 必选参数 --- -#}
    HOSTNAME="{{item.HOSTNAME}}",
    DOMAINVALUE="{{item.DOMAINVALUE}}",
    ;
{%- endfor -%}
```

#### 3.2 配置三四层过滤条件。

```jinja2
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
    {#- --- 条件必选：SVRIPMODE=HOSTNAME/DOMAIN 时必选 --- -#}
    {%- if item.SVRIPMODE in ['HOSTNAME', 'DOMAIN'] -%}
        HOSTNAME="{{item.HOSTNAME}}",
    {%- endif -%}
    {#- --- 条件必选：SVRIPMODE=DOMAIN 时必选 --- -#}
    {%- if item.SVRIPMODE == 'DOMAIN' -%}
        DOMAINVALUE="{{item.DOMAINVALUE}}",
    {%- endif -%}
    {#- --- 条件必选：L34PROTTYPE=NUMBER 时必选 --- -#}
    {%- if item.L34PROTTYPE == 'NUMBER' -%}
        L34PROTNUM={{item.L34PROTNUM}},
    {%- endif -%}
    {#- --- 条件必选：SVRIPMODE=IP 时必选 --- -#}
    {%- if item.SVRIPMODE == 'IP' -%}
        SVRIP="{{item.SVRIP}}",
    {%- endif -%}
    {#- --- 条件必选：SVRIPMODE=IPLIST 时必选 --- -#}
    {%- if item.SVRIPMODE == 'IPLIST' -%}
        SVRIPLISTNAME="{{item.SVRIPLISTNAME}}",
    {%- endif -%}
    {#- --- 条件必选：SVRIPMODE=IP 时必选 --- -#}
    {%- if item.SVRIPMODE == 'IP' -%}
        SVRIPMASKTYPE={{item.SVRIPMASKTYPE}},
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

#### 如果能预先获取HTTPS Server IP列表，在三四层filter中配置端口和Server IP可实现HTTPS地址识别功能。这种情况下就无需配置步骤 4。

#### 3.3 配置FlowFilter。

```jinja2
{%- for item in add_flowfilter_list -%}
    ADD FLOWFILTER:
    {#- --- 必选参数 --- -#}
    FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
    ;
{%- endfor -%}
```

#### 3.4 绑定三四层过滤条件。

```jinja2
{%- for item in add_fltbindflowf_list -%}
    ADD FLTBINDFLOWF:
    {#- --- 必选参数 --- -#}
    FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
    FILTERNAME="{{item.FILTERNAME}}",
    ;
{%- endfor -%}
```

#### 3.5 配置HTTPS解析规则。

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

#### 如果运营商希望基于流过滤器组设置过滤条件时，配置“流过滤器或流过滤器组选择(FILTERINGMODE)”为“FLOWFILTERGRP”，并且使用**ADD FLOWFILTERGRP**命令配置流过滤器组。

### 4 **可选：**配置DNS报文的解析规则。

### 若能预先获取HTTPS Server的IP列表，则无需配置DNS报文的解析规则；若不能预先获取HTTPS Server IP列表，只能获取域名信息，则需要配置DNS报文解析规则。

#### 4.1 配置三四层过滤条件。

```jinja2
{%- if is_optional_dns_parsing_rule -%}
    {%- for item in add_filter_list_1 -%}
        ADD FILTER:
        {#- --- 必选参数 --- -#}
        FILTERNAME="{{item.FILTERNAME}}",
        L34PROTTYPE={{item.L34PROTTYPE}},
        {#- --- 可选参数 --- -#}
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
{%- endif -%}
```

#### 4.2 配置七层过滤条件。

```jinja2
{%- if is_optional_dns_parsing_rule -%}
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
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.3 配置FlowFilter。

```jinja2
{%- if is_optional_dns_parsing_rule -%}
    {%- for item in add_flowfilter_list_1 -%}
        ADD FLOWFILTER:
        {#- --- 必选参数 --- -#}
        FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.4 绑定三四层过滤条件。

```jinja2
{%- if is_optional_dns_parsing_rule -%}
    {%- for item in add_fltbindflowf_list_1 -%}
        ADD FLTBINDFLOWF:
        {#- --- 必选参数 --- -#}
        FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
        FILTERNAME="{{item.FILTERNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.5 绑定七层过滤条件。

```jinja2
{%- if is_optional_dns_parsing_rule -%}
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
{%- endif -%}
```

#### 4.6 配置DNS解析规则。

```jinja2
{%- if is_optional_dns_parsing_rule -%}
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
{%- endif -%}
```

#### 如果运营商希望基于流过滤器组设置过滤条件时，配置“流过滤器或流过滤器组选择(FILTERINGMODE)”为“FLOWFILTERGRP”，并且使用**ADD FLOWFILTERGRP**命令配置流过滤器组。

#### 4.7 将新配置的Filter、L7Filter置为生效。

```jinja2
{%- if is_optional_dns_parsing_rule -%}
    {%- for item in set_refreshsrv_list -%}
        SET REFRESHSRV:
        {#- --- 必选参数 --- -#}
        REFRESHTYPE={{item.REFRESHTYPE}},
        ;
    {%- endfor -%}
{%- endif -%}
```

### 5 配置UDG的协议识别库和协议解析库。

#### 5.1 配置知名端口。

```jinja2
{%- for item in add_wellknownport_list -%}
    ADD WELLKNOWNPORT:
    {#- --- 必选参数 --- -#}
    IDENPROTNAME="{{item.IDENPROTNAME}}",
    PORTOP={{item.PORTOP}},
    PRIORITY={{item.PRIORITY}},
    PROTOCOLNAME="{{item.PROTOCOLNAME}}",
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：PORTOP=LT/RANGE 时必选 --- -#}
    {%- if item.PORTOP in ['LT', 'RANGE'] -%}
        ENDPORT={{item.ENDPORT}},
    {%- endif -%}
    {#- --- 条件必选：PORTOP=EQUAL/GT/RANGE 时必选 --- -#}
    {%- if item.PORTOP in ['EQUAL', 'GT', 'RANGE'] -%}
        STARTPORT={{item.STARTPORT}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 5.2 加载特定的知识库文件。如已加载，请跳过该步骤。

```jinja2
{%- for item in lod_signaturedb_list -%}
    LOD SIGNATUREDB:
    {#- --- 必选参数 --- -#}
    LOADMODE={{item.LOADMODE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：LOADMODE=SPECIFIC 时必选 --- -#}
    {%- if item.LOADMODE == 'SPECIFIC' -%}
        VERSION="{{item.VERSION}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 5.3 加载协议解析库。如已加载，请跳过该步骤。

```jinja2
{%- for item in lod_parserdb_list -%}
    LOD PARSERDB:
    {#- --- 必选参数 --- -#}
    LOADMODE={{item.LOADMODE}},
    ;
{%- endfor -%}
```

### 6 **可选：**配置用户关联识别功能。

```jinja2
{%- if is_optional_user_association_identification -%}
    {%- for item in add_usrrelateiden_list -%}
        ADD USRRELATEIDEN:
        {#- --- 必选参数 --- -#}
        PROTOCOLNAME="{{item.PROTOCOLNAME}}",
        USRRLTIDENSW={{item.USRRLTIDENSW}},
        ;
    {%- endfor -%}
{%- endif -%}
```

### 7 配置HTTPS报文和DNS报文使用的业务策略组合。

### 配置User Profile分别绑定HTTPS业务规则和DNS报文解析规则。DNS报文解析规则优先级最高。

#### 7.1 配置UserProfile。

```jinja2
{%- for item in add_userprofile_list -%}
    ADD USERPROFILE:
    {#- --- 必选参数 --- -#}
    USERPROFILENAME="{{item.USERPROFILENAME}}",
    ;
{%- endfor -%}
```

#### 7.2 将配置的Rule绑定到UserProfile。

```jinja2
{%- for item in add_rulebinding_list -%}
    ADD RULEBINDING:
    {#- --- 必选参数 --- -#}
    USERPROFILENAME="{{item.USERPROFILENAME}}",
    RULENAME="{{item.RULENAME}}",
    ;
{%- endfor -%}
```

#### 多次执行步骤 7.b，把配置的https、dns使用的规则绑定到UserProfile。

