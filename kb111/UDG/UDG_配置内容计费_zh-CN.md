---
id: ''
name: 配置内容计费
ne_type: UDG
type: feature
description: 用户访问园区业务时，智能分流SMF发起园区会话创建，数据流被分流到专网UPF上，需要在专网SMF和专网UPF上针对园区业务配置内容计费规则。  场景一：运营商对于园区业务未规划单独费率，则使用缺省费率（RG= 2000000002）。  场景二：运营商对于园区业务的费率有单独规划，按照运营商规划配置对应的费率；  此配置页面中的内容计费中的URR、PCCPOLICYGRPNM、RULE名称、UP名称等需要与专网SMF中的名称保持一致。
risk_level: ''
doc_source: ["特性部署","业务专题","5G Core 一跳入家解决方案","一跳入家解决方案（基于3GPP接入方案）","业务初始部署与调测","部署移动VPN","配置专用DNN数据","配置UPF","配置内容计费"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
用户访问园区业务时，智能分流SMF发起园区会话创建，数据流被分流到专网UPF上，需要在专网SMF和专网UPF上针对园区业务配置内容计费规则。场景一：运营商对于园区业务未规划单独费率，则使用缺省费率（RG= 2000000002）。场景二：运营商对于园区业务的费率有单独规划，按照运营商规划配置对应的费率；此配置页面中的内容计费中的URR、PCCPOLICYGRPNM、RULE名称、UP名称等需要与专网SMF中的名称保持一致。

## 必备事项
前提条件

前提条件

已参考运营商配置规范完成网元的基本配置。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_filter_list:
      type: items
      properties:
        FILTERNAME:
          name: '过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '配置三四层过滤条件。'
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
          name: '三四层IPv4协议输入类型'
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
          description: ''
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
          description: ''
          data_source: ''
          pattern: ''
          default: ANY
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
        L34PROTTYPEV6:
          name: '三四层IPv6协议输入类型'
          type: string
          enum:
          - NUMBER
          - STRING
          required: true
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
        FILTERGRPNAME:
          name: '过滤器组名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: ''
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
          description: '流过滤器名称已通过**ADD FLOWFILTER**命令配置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        FILTERNAME:
          name: '过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '过滤器名称已通过**ADD FILTER**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
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
        FILTERGRPNAME:
          name: '过滤器组名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: ''
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
          description: '流过滤器名称已通过**ADD FLOWFILTER**命令配置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        FILTERNAME:
          name: '过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '过滤器名称已通过**ADD FILTER**命令配置。'
          data_source: '已配置数据中获取'
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
          description: '配置URR，需要与SMF保持一致'
          data_source: '全网规划'
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
          data_source: '全网规划'
          pattern: ''
          default: VOLUME
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
          data_source: '全网规划'
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
          description: 'URR已通过**ADD URR**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DOWNURRNAME1:
          name: '下行发起URR名称1'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: 'URR已通过**ADD URR**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        UPURRNAME2:
          name: '上行发起URR名称2'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: 'URR已通过**ADD URR**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DOWNURRNAME2:
          name: '下行发起URR名称2'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: 'URR已通过**ADD URR**命令配置。'
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
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        FUPSESSIONEXC:
          name: 'Session级FUP累计标识'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        SIGNALASSOCIATE:
          name: '信令关联计费标识'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ENABLE
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
        HTTP2DEGRADESW:
          name: 'HTTP2.0协议回落开关'
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
        TOKENFUNCFLAG:
          name: 'Token检测功能标识'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        URRGROUPNAME:
          name: 'URR组名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: 'URRGroup已经通过**ADD URRGROUP**配置'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SIGURRGRPNAME:
          name: '信令URR组名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: 'URRGroup已经通过**ADD URRGROUP**配置'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        TOKENENCRYALG:
          name: 'Token加密算法'
          type: string
          enum:
          - MD5
          - SHA256
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: SHA256
        TOKENSECRETKEY:
          name: 'Token密钥'
          type: string
          minLength: 1
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TOKENSECRETKEYCONFIRM:
          name: '确认Token密钥'
          type: string
          minLength: 1
          maxLength: 63
          required: false
          description: ''
          data_source: ''
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
          description: '配置内容计费规则。'
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
        POLICYNAME:
          name: '策略名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: '绑定的PCC策略组已通过**ADD IPFARMSERVER**命令配置。'
          data_source: '已配置数据中获取'
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
          description: '与SMF上配置的PCC用户模板名称保持一致。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        ALIASMARKFLAG:
          name: 'Alias Marking使能标记'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        DDOSCHECK:
          name: '防DDOS攻击标记'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        CAPMODETHRES:
          name: 'Captive模式时间阈值（分）'
          type: integer
          minimum: 0
          maximum: 60
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        LOCRPTSWITCH:
          name: '实时位置上报开关'
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
        TETHERINGMAXNUM:
          name: 'Tethering用户下最多可接入后台终端的数量'
          type: integer
          minimum:
          - 0
          - 255
          maximum:
          - 20
          - 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 255
        V6TCPMSSVALUE:
          name: 'IPv6 TCP报文长度（字节）'
          type: integer
          minimum:
          - 0
          - 496
          maximum:
          - 0
          - 1500
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        V4TCPMSSVALUE:
          name: 'IPv4 TCP报文长度（字节）'
          type: integer
          minimum:
          - 0
          - 496
          maximum:
          - 0
          - 1500
          required: false
          description: ''
          data_source: ''
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
          description: '使用**ADD USERPROFILE**命令定义的用户模板名称。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        RULENAME:
          name: '规则名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: 'Rule名称已经通过**ADD RULE**配置'
          data_source: '已配置数据中获取'
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DFTURRGRPNAME:
          name: '缺省URR组名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DFTSIGURRGNAME:
          name: '缺省信令URR组名称'
          type: string
          minLength: 0
          maxLength: 31
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
    add_filter_list_1:
      type: items
      properties:
        FILTERNAME:
          name: '过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '配置三四层过滤条件。'
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
          name: '三四层IPv4协议输入类型'
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
    add_filteripv6_list_1:
      type: items
      properties:
        FILTERNAME:
          name: '过滤器名字'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
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
          description: ''
          data_source: ''
          pattern: ''
          default: ANY
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
        L34PROTTYPEV6:
          name: '三四层IPv6协议输入类型'
          type: string
          enum:
          - NUMBER
          - STRING
          required: true
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
    add_flowfilter_list_2:
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
        FILTERGRPNAME:
          name: '过滤器组名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_fltbindflowf_list_2:
      type: items
      properties:
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '流过滤器名称已通过**ADD FLOWFILTER**命令配置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        FILTERNAME:
          name: '过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '过滤器名称已通过**ADD FILTER**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_flowfilter_list_3:
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
        FILTERGRPNAME:
          name: '过滤器组名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_fltbindflowf_list_3:
      type: items
      properties:
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '流过滤器名称已通过**ADD FLOWFILTER**命令配置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        FILTERNAME:
          name: '过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '过滤器名称已通过**ADD FILTER**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_urr_list_2:
      type: items
      properties:
        URRNAME:
          name: '使用量上报规则名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '配置URR，需要与SMF保持一致'
          data_source: '全网规划'
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
          data_source: '全网规划'
          pattern: ''
          default: VOLUME
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
          data_source: '全网规划'
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
    add_urrgroup_list_1:
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
          description: 'URR已通过**ADD URR**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DOWNURRNAME1:
          name: '下行发起URR名称1'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: 'URR已通过**ADD URR**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        UPURRNAME2:
          name: '上行发起URR名称2'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: 'URR已通过**ADD URR**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DOWNURRNAME2:
          name: '下行发起URR名称2'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: 'URR已通过**ADD URR**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_pccpolicygrp_list_1:
      type: items
      properties:
        PCCPOLICYGRPNM:
          name: 'PCC策略组名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        FUPSESSIONEXC:
          name: 'Session级FUP累计标识'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        SIGNALASSOCIATE:
          name: '信令关联计费标识'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ENABLE
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
        HTTP2DEGRADESW:
          name: 'HTTP2.0协议回落开关'
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
        TOKENFUNCFLAG:
          name: 'Token检测功能标识'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        URRGROUPNAME:
          name: 'URR组名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: 'URRGroup已经通过**ADD URRGROUP**配置'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SIGURRGRPNAME:
          name: '信令URR组名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: 'URRGroup已经通过**ADD URRGROUP**配置'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        TOKENENCRYALG:
          name: 'Token加密算法'
          type: string
          enum:
          - MD5
          - SHA256
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: SHA256
        TOKENSECRETKEY:
          name: 'Token密钥'
          type: string
          minLength: 1
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TOKENSECRETKEYCONFIRM:
          name: '确认Token密钥'
          type: string
          minLength: 1
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_rule_list_2:
      type: items
      properties:
        RULENAME:
          name: '规则名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '配置内容计费规则。'
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
        POLICYNAME:
          name: '策略名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: '绑定的PCC策略组已通过**ADD IPFARMSERVER**命令配置。'
          data_source: '已配置数据中获取'
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
    add_userprofile_list_1:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '与SMF上配置的PCC用户模板名称保持一致。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        ALIASMARKFLAG:
          name: 'Alias Marking使能标记'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        DDOSCHECK:
          name: '防DDOS攻击标记'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        CAPMODETHRES:
          name: 'Captive模式时间阈值（分）'
          type: integer
          minimum: 0
          maximum: 60
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        LOCRPTSWITCH:
          name: '实时位置上报开关'
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
        TETHERINGMAXNUM:
          name: 'Tethering用户下最多可接入后台终端的数量'
          type: integer
          minimum:
          - 0
          - 255
          maximum:
          - 20
          - 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 255
        V6TCPMSSVALUE:
          name: 'IPv6 TCP报文长度（字节）'
          type: integer
          minimum:
          - 0
          - 496
          maximum:
          - 0
          - 1500
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        V4TCPMSSVALUE:
          name: 'IPv4 TCP报文长度（字节）'
          type: integer
          minimum:
          - 0
          - 496
          maximum:
          - 0
          - 1500
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_rulebinding_list_2:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '使用**ADD USERPROFILE**命令定义的用户模板名称。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        RULENAME:
          name: '规则名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: 'Rule名称已经通过**ADD RULE**配置'
          data_source: '已配置数据中获取'
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
    set_urrgrpbinding_list_1:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DFTURRGRPNAME:
          name: '缺省URR组名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DFTSIGURRGNAME:
          name: '缺省信令URR组名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_refreshsrv_list_1:
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
    - FILTERNAME: 'any'
      L34PROTTYPE: STRING
      L34PROTOCOL: ANY
      MSSTARTPORT: 0
      MSENDPORT: 65535
      SVRSTARTPORT: 0
      SVRENDPORT: 65535
      L34PROTNUM: ''
    add_filteripv6_list:
    - FILTERNAME: 'any_ipv6'
      L34PROTOCOL: ANY
      MSSTARTPORT: 0
      MSENDPORT: 65535
      SVRSTARTPORT: 0
      SVRENDPORT: 65535
      L34PROTTYPEV6: STRING
      L34PROTNUM: ''
    add_flowfilter_list:
    - FLOWFILTERNAME: 'any_f_f'
      TETHERDETFLAG: NONE
      FLOWFILTERTYPE: USERCONFIG
      FILTERGRPNAME: ''
    add_fltbindflowf_list:
    - FLOWFILTERNAME: 'any_f_f'
      FILTERNAME: 'any'
    add_flowfilter_list_1:
    - FLOWFILTERNAME: 'any_ipv6_f_f'
      TETHERDETFLAG: NONE
      FLOWFILTERTYPE: USERCONFIG
      FILTERGRPNAME: ''
    add_fltbindflowf_list_1:
    - FLOWFILTERNAME: 'any_ipv6_f_f'
      FILTERNAME: 'any_ipv6'
    add_urr_list:
    - URRNAME: 'common_01_cbb_online'
      URRID: 2000000002
      USAGERPTMODE: ONLINE
      ONLMETERINGTYPE: VOLUME
      OFFMETERINGTYPE: VOLUME
      DFTQUOTAPARA: Byte
      DFTQUOTATIME: ''
      DFTQUOTAVOLUME: ''
      RG: ''
      SID: ''
    add_urrgroup_list:
    - URRGROUPNAME: 'common_01_ch_p'
      UPURRNAME1: 'common_01_cbb_offline'
      DOWNURRNAME1: 'common_01_cbb_offline'
      UPURRNAME2: 'common_01_cbb_online'
      DOWNURRNAME2: 'common_01_cbb_online'
    add_pccpolicygrp_list:
    - PCCPOLICYGRPNM: 'common_01_pcc_p_g'
      FUPSESSIONEXC: DISABLE
      SIGNALASSOCIATE: ENABLE
      ADCMUTEFLAG: ENABLE
      HTTP2DEGRADESW: INHERIT
      TOKENFUNCFLAG: DISABLE
      URRGROUPNAME: 'common_01_ch_p'
      SIGURRGRPNAME: 'common_01_ch_p'
      TOKENENCRYALG: SHA256
      TOKENSECRETKEY: ''
      TOKENSECRETKEYCONFIRM: ''
    add_rule_list:
    - RULENAME: 'common_any'
      POLICYTYPE: PCC
      FLOWFILTERNAME: 'any_f_f'
      PRIORITY: 65000
      POLICYNAME: 'common_01_pcc_p_g'
      FILTERINGMODE: FLOWFILTER
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
    - USERPROFILENAME: 'u_p_multi_default'
      ALIASMARKFLAG: DISABLE
      DDOSCHECK: DISABLE
      CAPMODETHRES: 0
      LOCRPTSWITCH: INHERIT
      TETHERINGMAXNUM: 255
      V6TCPMSSVALUE: 0
      V4TCPMSSVALUE: 0
    add_rulebinding_list:
    - USERPROFILENAME: 'u_p_multi_default'
      RULENAME: 'common_any'
      POLICYTYPE: PCC
    set_urrgrpbinding_list:
    - USERPROFILENAME: 'u_p_multi_default'
      DFTURRGRPNAME: 'common_01_ch_p'
      DFTSIGURRGNAME: 'common_01_ch_p'
    set_refreshsrv_list:
    - REFRESHTYPE: ALL
    add_filter_list_1:
    - FILTERNAME: 'any'
      L34PROTTYPE: STRING
      L34PROTOCOL: ANY
      MSSTARTPORT: 0
      MSENDPORT: 65535
      SVRSTARTPORT: 0
      SVRENDPORT: 65535
      L34PROTNUM: ''
    add_filteripv6_list_1:
    - FILTERNAME: 'any_ipv6'
      L34PROTOCOL: ANY
      MSSTARTPORT: 0
      MSENDPORT: 65535
      SVRSTARTPORT: 0
      SVRENDPORT: 65535
      L34PROTTYPEV6: STRING
      L34PROTNUM: ''
    add_flowfilter_list_2:
    - FLOWFILTERNAME: 'any_f_f'
      TETHERDETFLAG: NONE
      FLOWFILTERTYPE: USERCONFIG
      FILTERGRPNAME: ''
    add_fltbindflowf_list_2:
    - FLOWFILTERNAME: 'any_f_f'
      FILTERNAME: 'any'
    add_flowfilter_list_3:
    - FLOWFILTERNAME: 'any_ipv6_f_f'
      TETHERDETFLAG: NONE
      FLOWFILTERTYPE: USERCONFIG
      FILTERGRPNAME: ''
    add_fltbindflowf_list_3:
    - FLOWFILTERNAME: 'any_ipv6_f_f'
      FILTERNAME: 'any_ipv6'
    add_urr_list_2:
    - URRNAME: 'multi_01_cbb_online'
      URRID: 2000000003
      USAGERPTMODE: ONLINE
      ONLMETERINGTYPE: VOLUME
      OFFMETERINGTYPE: VOLUME
      DFTQUOTAPARA: Byte
      DFTQUOTATIME: ''
      DFTQUOTAVOLUME: ''
      RG: ''
      SID: ''
    add_urrgroup_list_1:
    - URRGROUPNAME: 'multi_01_ch_p'
      UPURRNAME1: 'multi_01_cbb_offline'
      DOWNURRNAME1: 'multi_01_cbb_offline'
      UPURRNAME2: 'multi_01_cbb_online'
      DOWNURRNAME2: 'multi_01_cbb_online'
    add_pccpolicygrp_list_1:
    - PCCPOLICYGRPNM: 'multi_01_pcc_p_g'
      FUPSESSIONEXC: DISABLE
      SIGNALASSOCIATE: ENABLE
      ADCMUTEFLAG: ENABLE
      HTTP2DEGRADESW: INHERIT
      TOKENFUNCFLAG: DISABLE
      URRGROUPNAME: 'multi_01_ch_p'
      SIGURRGRPNAME: 'multi_01_ch_p'
      TOKENENCRYALG: SHA256
      TOKENSECRETKEY: ''
      TOKENSECRETKEYCONFIRM: ''
    add_rule_list_2:
    - RULENAME: 'multi_01_r'
      POLICYTYPE: PCC
      FLOWFILTERNAME: 'any_f_f'
      PRIORITY: 10000
      POLICYNAME: 'multi_01_pcc_p_g'
      FILTERINGMODE: FLOWFILTER
      FLWFLTRGRPNAME: ''
      ADCMUTEFLAG: ENABLE
      ALGSWITCH: DISABLE
      RDSTRIGGERFLAG: DISABLE
      REDIRIPVERFLAG: ''
      REMARKFPISEL: REMARK
      SRVLBOFLAG: DISABLE
      WORKERNAME: ''
      WORKERPARA: ''
    add_userprofile_list_1:
    - USERPROFILENAME: 'u_p_01_multi'
      ALIASMARKFLAG: DISABLE
      DDOSCHECK: DISABLE
      CAPMODETHRES: 0
      LOCRPTSWITCH: INHERIT
      TETHERINGMAXNUM: 255
      V6TCPMSSVALUE: 0
      V4TCPMSSVALUE: 0
    add_rulebinding_list_2:
    - USERPROFILENAME: 'u_p_01_multi'
      RULENAME: 'multi_01_r'
      POLICYTYPE: PCC
    set_urrgrpbinding_list_1:
    - USERPROFILENAME: 'u_p_01_multi'
      DFTURRGRPNAME: 'multi_01_ch_p'
      DFTSIGURRGNAME: 'multi_01_ch_p'
    set_refreshsrv_list_1:
    - REFRESHTYPE: ALL
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 场景一. 园区业务未规划单独费率，使用缺省费率。

#### 1.1 配置L34Filter，如果设备中已经按照运营商规范配置（执行LST FILTER:FILTERNAME="any";以及LST FILTER:FILTERNAME="any\_ipv6";命令查询），无需重复执行。

```jinja2
{%- if is_scenario_default_rate -%}
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
{%- endif -%}
```

```jinja2
{%- if is_scenario_default_rate -%}
    {%- for item in add_filteripv6_list -%}
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
{%- endif -%}
```

#### 1.2 配置Flowfilter并与L34Filter绑定，如果设备中已经按照运营商规范配置（执行LST FLOWFILTER:FLOWFILTERNAME ="any\_f\_f";以及LST FLOWFILTER:FLOWFILTERNAME ="any\_ipv6\_f\_f";命令），无需重复执行。

```jinja2
{%- if is_scenario_default_rate -%}
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
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：FLOWFILTERTYPE=USERCONFIG 时可选 --- -#}
        {%- if item.FLOWFILTERTYPE == 'USERCONFIG' -%}
            {%- if item.FILTERGRPNAME is not none -%}
                FILTERGRPNAME="{{item.FILTERGRPNAME}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_default_rate -%}
    {%- for item in add_fltbindflowf_list -%}
        ADD FLTBINDFLOWF:
        {#- --- 必选参数 --- -#}
        FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
        FILTERNAME="{{item.FILTERNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_default_rate -%}
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
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：FLOWFILTERTYPE=USERCONFIG 时可选 --- -#}
        {%- if item.FLOWFILTERTYPE == 'USERCONFIG' -%}
            {%- if item.FILTERGRPNAME is not none -%}
                FILTERGRPNAME="{{item.FILTERGRPNAME}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_default_rate -%}
    {%- for item in add_fltbindflowf_list_1 -%}
        ADD FLTBINDFLOWF:
        {#- --- 必选参数 --- -#}
        FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
        FILTERNAME="{{item.FILTERNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 1.3 配置计费策略组，如果设备中已经按照运营商规范配置，无需重复执行。

```jinja2
{%- if is_scenario_default_rate -%}
    {%- for item in add_urr_list -%}
        ADD URR:
        {#- --- 必选参数 --- -#}
        URRNAME="{{item.URRNAME}}",
        URRID={{item.URRID}},
        USAGERPTMODE={{item.USAGERPTMODE}},
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：USAGERPTMODE=ONLINE 时可选 --- -#}
        {%- if item.USAGERPTMODE == 'ONLINE' -%}
            {%- if item.ONLMETERINGTYPE is not none -%}
                ONLMETERINGTYPE={{item.ONLMETERINGTYPE}},
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
{%- endif -%}
```

```jinja2
{%- if is_scenario_default_rate -%}
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
{%- endif -%}
```

#### 1.4 配置pcc策略组并绑定计费策略组，如果设备中已经按照运营商规范配置，无需重复执行。

```jinja2
{%- if is_scenario_default_rate -%}
    {%- for item in add_pccpolicygrp_list -%}
        ADD PCCPOLICYGRP:
        {#- --- 必选参数 --- -#}
        PCCPOLICYGRPNM="{{item.PCCPOLICYGRPNM}}",
        {#- --- 可选参数 --- -#}
        {%- if item.FUPSESSIONEXC is not none -%}
            FUPSESSIONEXC={{item.FUPSESSIONEXC}},
        {%- endif -%}
        {%- if item.SIGNALASSOCIATE is not none -%}
            SIGNALASSOCIATE={{item.SIGNALASSOCIATE}},
        {%- endif -%}
        {%- if item.ADCMUTEFLAG is not none -%}
            ADCMUTEFLAG={{item.ADCMUTEFLAG}},
        {%- endif -%}
        {%- if item.HTTP2DEGRADESW is not none -%}
            HTTP2DEGRADESW={{item.HTTP2DEGRADESW}},
        {%- endif -%}
        {%- if item.TOKENFUNCFLAG is not none -%}
            TOKENFUNCFLAG={{item.TOKENFUNCFLAG}},
        {%- endif -%}
        {%- if item.URRGROUPNAME is not none -%}
            URRGROUPNAME="{{item.URRGROUPNAME}}",
        {%- endif -%}
        {%- if item.SIGURRGRPNAME is not none -%}
            SIGURRGRPNAME="{{item.SIGURRGRPNAME}}",
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：TOKENFUNCFLAG=ENABLE 时必选 --- -#}
        {%- if item.TOKENFUNCFLAG == 'ENABLE' -%}
            TOKENSECRETKEY="{{item.TOKENSECRETKEY}}",
        {%- endif -%}
        {#- --- 条件必选：TOKENFUNCFLAG=ENABLE 时必选 --- -#}
        {%- if item.TOKENFUNCFLAG == 'ENABLE' -%}
            TOKENSECRETKEYCONFIRM="{{item.TOKENSECRETKEYCONFIRM}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：TOKENFUNCFLAG=ENABLE 时可选 --- -#}
        {%- if item.TOKENFUNCFLAG == 'ENABLE' -%}
            {%- if item.TOKENENCRYALG is not none -%}
                TOKENENCRYALG={{item.TOKENENCRYALG}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 1.5 配置rule，如果设备中已经按照运营商规范配置，无需重复执行。

```jinja2
{%- if is_scenario_default_rate -%}
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
{%- endif -%}
```

#### 如果UPF已有大网的缺省User Profile（u\_p\_xxx\_common），则使用ADD RULE命令配置的园区规则的优先级PRIORITY需要高于u\_p\_xxx\_common下所有规则的优先级，按局点的实际情况规划。

#### 建议在专网PCF上为专用DNN策略配置隔离条件组，对专网会话仅下发专网业务，不下发大网业务，专网UPF独立部署时也不需要配置大网的User Profile。

#### 当以下两个条件都满足时，在专网UPF上参考第6步使用ADD USERPROFILE配置大网的缺省User Profile（u\_p\_xxx\_common）以及园区用户要使用的大网的User Profile （两个user profile可以不绑定任何规则）：

#### -专网PCF上没有配置隔离条件组或者专网PCF为20.11.2之前版本不支持配置隔离条件组功能

#### -专网PCF上大网策略没有将common.dnn通用DNN作为过滤条件

#### 通过上述操作，可以在专网UPF上增加大网相关User Profile，避免业务失败。原因是，当专网SMF使用专用DNN向专网PCF请求策略时，专网PCF会将大网User Profile策略一同下发，包括大网的缺省User Profile以及专网PCF上为园区用户配置了其它的大网User Profile。

#### 当PCF下发缺省的内容计费规则对应的用户模板时，添加园区缺省计费规则对应的UserProfile，需要配置如下步骤6、7、8。USERPROFILE的名称统一规划，保证在PCF、SMF、UPF间名称一致。不一致时PCF下发的策略无法生效。

#### 1.6 配置User Profile。

```jinja2
{%- if is_scenario_default_rate -%}
    {%- for item in add_userprofile_list -%}
        ADD USERPROFILE:
        {#- --- 必选参数 --- -#}
        USERPROFILENAME="{{item.USERPROFILENAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.ALIASMARKFLAG is not none -%}
            ALIASMARKFLAG={{item.ALIASMARKFLAG}},
        {%- endif -%}
        {%- if item.DDOSCHECK is not none -%}
            DDOSCHECK={{item.DDOSCHECK}},
        {%- endif -%}
        {%- if item.CAPMODETHRES is not none -%}
            CAPMODETHRES={{item.CAPMODETHRES}},
        {%- endif -%}
        {%- if item.LOCRPTSWITCH is not none -%}
            LOCRPTSWITCH={{item.LOCRPTSWITCH}},
        {%- endif -%}
        {%- if item.TETHERINGMAXNUM is not none -%}
            TETHERINGMAXNUM={{item.TETHERINGMAXNUM}},
        {%- endif -%}
        {%- if item.V6TCPMSSVALUE is not none -%}
            V6TCPMSSVALUE={{item.V6TCPMSSVALUE}},
        {%- endif -%}
        {%- if item.V4TCPMSSVALUE is not none -%}
            V4TCPMSSVALUE={{item.V4TCPMSSVALUE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 1.7 绑定User Profile。

```jinja2
{%- if is_scenario_default_rate -%}
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
{%- endif -%}
```

#### 1.8 设置用户模板的URR组绑定关系。

```jinja2
{%- if is_scenario_default_rate -%}
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
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 【注意】每个userprofile都要增加缺省URR组以及缺省信令URR组，如果都未配置可能会导致无法计费。

#### 1.9 业务生效。

```jinja2
{%- if is_scenario_default_rate -%}
    {%- for item in set_refreshsrv_list -%}
        SET REFRESHSRV:
        {#- --- 必选参数 --- -#}
        REFRESHTYPE={{item.REFRESHTYPE}},
        ;
    {%- endfor -%}
{%- endif -%}
```

### 2 场景二. 园区业务规划单独费率，以2000000003为例进行配置。

#### 2.1 配置L34Filter，如果设备中已经按照运营商规范配置（执行LST FILTER:FILTERNAME="any";以及LST FILTER:FILTERNAME="any\_ipv6";命令查询），无需重复执行。

```jinja2
{%- if is_scenario_planned_rate -%}
    {%- for item in add_filter_list_1 -%}
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
{%- endif -%}
```

```jinja2
{%- if is_scenario_planned_rate -%}
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
{%- endif -%}
```

#### 2.2 配置Flowfilter并与L34Filter绑定，如果设备中已经按照运营商规范配置（执行LST FLOWFILTER:FLOWFILTERNAME ="any\_f\_f";以及LST FLOWFILTER:FLOWFILTERNAME ="any\_ipv6\_f\_f";命令），无需重复执行。

```jinja2
{%- if is_scenario_planned_rate -%}
    {%- for item in add_flowfilter_list_2 -%}
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
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：FLOWFILTERTYPE=USERCONFIG 时可选 --- -#}
        {%- if item.FLOWFILTERTYPE == 'USERCONFIG' -%}
            {%- if item.FILTERGRPNAME is not none -%}
                FILTERGRPNAME="{{item.FILTERGRPNAME}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_planned_rate -%}
    {%- for item in add_fltbindflowf_list_2 -%}
        ADD FLTBINDFLOWF:
        {#- --- 必选参数 --- -#}
        FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
        FILTERNAME="{{item.FILTERNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_planned_rate -%}
    {%- for item in add_flowfilter_list_3 -%}
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
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：FLOWFILTERTYPE=USERCONFIG 时可选 --- -#}
        {%- if item.FLOWFILTERTYPE == 'USERCONFIG' -%}
            {%- if item.FILTERGRPNAME is not none -%}
                FILTERGRPNAME="{{item.FILTERGRPNAME}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_planned_rate -%}
    {%- for item in add_fltbindflowf_list_3 -%}
        ADD FLTBINDFLOWF:
        {#- --- 必选参数 --- -#}
        FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
        FILTERNAME="{{item.FILTERNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.3 配置计费策略组。

```jinja2
{%- if is_scenario_planned_rate -%}
    {%- for item in add_urr_list_2 -%}
        ADD URR:
        {#- --- 必选参数 --- -#}
        URRNAME="{{item.URRNAME}}",
        URRID={{item.URRID}},
        USAGERPTMODE={{item.USAGERPTMODE}},
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：USAGERPTMODE=ONLINE 时可选 --- -#}
        {%- if item.USAGERPTMODE == 'ONLINE' -%}
            {%- if item.ONLMETERINGTYPE is not none -%}
                ONLMETERINGTYPE={{item.ONLMETERINGTYPE}},
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
{%- endif -%}
```

```jinja2
{%- if is_scenario_planned_rate -%}
    {%- for item in add_urrgroup_list_1 -%}
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
{%- endif -%}
```

#### 2.4 配置pcc策略组并绑定计费策略组。

```jinja2
{%- if is_scenario_planned_rate -%}
    {%- for item in add_pccpolicygrp_list_1 -%}
        ADD PCCPOLICYGRP:
        {#- --- 必选参数 --- -#}
        PCCPOLICYGRPNM="{{item.PCCPOLICYGRPNM}}",
        {#- --- 可选参数 --- -#}
        {%- if item.FUPSESSIONEXC is not none -%}
            FUPSESSIONEXC={{item.FUPSESSIONEXC}},
        {%- endif -%}
        {%- if item.SIGNALASSOCIATE is not none -%}
            SIGNALASSOCIATE={{item.SIGNALASSOCIATE}},
        {%- endif -%}
        {%- if item.ADCMUTEFLAG is not none -%}
            ADCMUTEFLAG={{item.ADCMUTEFLAG}},
        {%- endif -%}
        {%- if item.HTTP2DEGRADESW is not none -%}
            HTTP2DEGRADESW={{item.HTTP2DEGRADESW}},
        {%- endif -%}
        {%- if item.TOKENFUNCFLAG is not none -%}
            TOKENFUNCFLAG={{item.TOKENFUNCFLAG}},
        {%- endif -%}
        {%- if item.URRGROUPNAME is not none -%}
            URRGROUPNAME="{{item.URRGROUPNAME}}",
        {%- endif -%}
        {%- if item.SIGURRGRPNAME is not none -%}
            SIGURRGRPNAME="{{item.SIGURRGRPNAME}}",
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：TOKENFUNCFLAG=ENABLE 时必选 --- -#}
        {%- if item.TOKENFUNCFLAG == 'ENABLE' -%}
            TOKENSECRETKEY="{{item.TOKENSECRETKEY}}",
        {%- endif -%}
        {#- --- 条件必选：TOKENFUNCFLAG=ENABLE 时必选 --- -#}
        {%- if item.TOKENFUNCFLAG == 'ENABLE' -%}
            TOKENSECRETKEYCONFIRM="{{item.TOKENSECRETKEYCONFIRM}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：TOKENFUNCFLAG=ENABLE 时可选 --- -#}
        {%- if item.TOKENFUNCFLAG == 'ENABLE' -%}
            {%- if item.TOKENENCRYALG is not none -%}
                TOKENENCRYALG={{item.TOKENENCRYALG}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.5 配置rule。

```jinja2
{%- if is_scenario_planned_rate -%}
    {%- for item in add_rule_list_2 -%}
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

#### 如果UPF已有大网的缺省User Profile（u\_p\_xxx\_common），则使用ADD RULE命令配置的园区规则的优先级PRIORITY需要高于u\_p\_xxx\_common下所有规则的优先级，按局点的实际情况规划。

#### 建议在专网PCF上为专用DNN策略配置隔离条件组，对专网会话仅下发专网业务，不下发大网业务，专网UPF独立部署时也不需要配置大网的User Profile。

#### 当以下两个条件都满足时，在专网UPF上参考第6步使用ADD USERPROFILE配置大网的缺省User Profile（u\_p\_xxx\_common）以及园区用户要使用的大网的User Profile （两个user profile可以不绑定任何规则）：

#### -专网PCF上没有配置隔离条件组或者专网PCF为20.11.2之前版本不支持配置隔离条件组功能

#### -专网PCF上大网策略没有将common.dnn通用DNN作为过滤条件

#### 通过上述操作，可以在专网UPF上增加大网相关User Profile，避免业务失败。原因是，当专网SMF使用专用DNN向专网PCF请求策略时，专网PCF会将大网User Profile策略一同下发，包括大网的缺省User Profile以及专网PCF上为园区用户配置了其它的大网User Profile。

#### 2.6 配置User Profile。

```jinja2
{%- if is_scenario_planned_rate -%}
    {%- for item in add_userprofile_list_1 -%}
        ADD USERPROFILE:
        {#- --- 必选参数 --- -#}
        USERPROFILENAME="{{item.USERPROFILENAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.ALIASMARKFLAG is not none -%}
            ALIASMARKFLAG={{item.ALIASMARKFLAG}},
        {%- endif -%}
        {%- if item.DDOSCHECK is not none -%}
            DDOSCHECK={{item.DDOSCHECK}},
        {%- endif -%}
        {%- if item.CAPMODETHRES is not none -%}
            CAPMODETHRES={{item.CAPMODETHRES}},
        {%- endif -%}
        {%- if item.LOCRPTSWITCH is not none -%}
            LOCRPTSWITCH={{item.LOCRPTSWITCH}},
        {%- endif -%}
        {%- if item.TETHERINGMAXNUM is not none -%}
            TETHERINGMAXNUM={{item.TETHERINGMAXNUM}},
        {%- endif -%}
        {%- if item.V6TCPMSSVALUE is not none -%}
            V6TCPMSSVALUE={{item.V6TCPMSSVALUE}},
        {%- endif -%}
        {%- if item.V4TCPMSSVALUE is not none -%}
            V4TCPMSSVALUE={{item.V4TCPMSSVALUE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.7 绑定User Profile。

```jinja2
{%- if is_scenario_planned_rate -%}
    {%- for item in add_rulebinding_list_2 -%}
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
{%- endif -%}
```

#### 2.8 设置用户模板的URR组绑定关系。

```jinja2
{%- if is_scenario_planned_rate -%}
    {%- for item in set_urrgrpbinding_list_1 -%}
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
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.9 业务生效。

```jinja2
{%- if is_scenario_planned_rate -%}
    {%- for item in set_refreshsrv_list_1 -%}
        SET REFRESHSRV:
        {#- --- 必选参数 --- -#}
        REFRESHTYPE={{item.REFRESHTYPE}},
        ;
    {%- endfor -%}
{%- endif -%}
```

