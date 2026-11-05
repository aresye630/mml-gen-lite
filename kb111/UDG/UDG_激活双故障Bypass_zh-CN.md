---
id: GWFD-112000
name: 激活双故障Bypass
ne_type: UDG
type: feature
description: 在UDG上激活双故障Bypass功能，降低PCF/PCRF双故障对用户业务的影响。  适用于PGW-U、UPF。
risk_level: ''
doc_source: ["特性部署","特性指南","UDG特性指南","语音功能","GWFD-112000 双故障Bypass","激活双故障Bypass"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
在UDG上激活双故障Bypass功能，降低PCF/PCRF双故障对用户业务的影响。适用于PGW-U、UPF。

## 必备事项
前提条件

* 请仔细阅读GWFD-112000 双故障Bypass。
* 依赖的特性已完成配置，相关特性参见与其他特性的交互。
* 已完成APN、User Profile、User Profile group创建，以及三者之间的关系绑定。
* 完成**加载license**，对应的License项见License支持。
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
          name: '过滤器名字'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '配置any to any过滤器名字。UPF通过将用户上下行报文匹配filter，实现报文的过滤。'
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
          description: '任意三四层协议。'
          data_source: '本端规划'
          pattern: ''
          default: ANY
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
          description: '任意三四层协议。'
          data_source: '本端规划'
          pattern: ''
          default: ANY
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
          description: '不同流过滤器之间，该参数不能重复。'
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
          description: '使用**ADD FLOWFILTER**命令定义的流过滤器名称。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        FILTERNAME:
          name: '过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '使用**ADD FILTER**、**ADD FILTERIPV6**命令定义的过滤器名称。'
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
          description: '增加使用量上报规则信息。存在多条记录时，使用量上报规则名称不能重复。  “URRID”在所有URR内唯一。  使用量上报模式、计费标识组成类型、计费组以及计费统计类型请根据业务规划进行配置。'
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
          data_source: '本端规划'
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
          data_source: '本端规划'
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
          data_source: '本端规划'
          pattern: ''
          default: VOLUME
        RG:
          name: '计费组'
          type: integer
          minimum: 0
          maximum: 4294967294
          required: false
          description: '该参数用于设置计费组。报表功能开启，软参bit1557开启，则需要配置此参数，同时参数值需要与SMF保持一致，否则报表上报的RG与实际计费的RG不一致。'
          data_source: '本端规划'
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
          data_source: '本端规划'
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
          description: '增加使用量上报规则组。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPURRNAME1:
          name: '上行发起URR名称1'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        DOWNURRNAME1:
          name: '下行发起URR名称1'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPURRNAME2:
          name: '上行发起URR名称2'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        DOWNURRNAME2:
          name: '下行发起URR名称2'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: '本端规划'
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
          description: '存在多条数据时，该参数不能相同。'
          data_source: '本端规划'
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
        URRGROUPNAME:
          name: '使用量上报规则组名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '使用**ADD URRGROUP**定义的使用量上报规则组。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        EVENTCHARGEFLAG:
          name: '事件计费标识'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        EVENTCHGPOINT:
          name: '事件计费点'
          type: string
          enum:
          - FINISH
          - REQUEST
          - RESPONSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: RESPONSE
        MMSCHARGETYPE:
          name: '彩信计费类型'
          type: string
          enum:
          - MULTI
          - SINGLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: SINGLE
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
          description: '存在多条数据时，该参数+策略类型不能完全相同。  与SMF上配置的规则名称相同。'
          data_source: '与对端协商'
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
          description: '使用样例值。'
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
          description: '使用**ADD FLOWFILTER**命令定义的流过滤器名称。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PRIORITY:
          name: '全局优先级'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
          description: '* 仅对PCC用户生效。优先级值越小，优先级越高。 * PCF下发的用于创建语音专有QoS Flow/专有承载的规则的优先级高于本地配置的用于创建语音专有QoS Flow/专有承载的规则；本地配置的用于创建语音专有QoS Flow/专有承载的规则优先级高于PCF下发的any to any的动态规则和本地配置的any to any的预定义规则。 * 以实际规划为准。'
          data_source: '与对端协商'
          pattern: ''
          default: 4294967295
        POLICYNAME:
          name: '策略名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: '使用**ADD PCCPOLICYGRP**命令定义的PCC策略组名称。'
          data_source: '已配置数据中获取'
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
          description: '与SMF上配置的用户模板名称保持一致。'
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
          description: '使用**ADD RULE**命令定义的规则名称。'
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
          data_source: '与对端协商'
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
          description: 'UDG通过将用户上下行报文匹配Filter，实现三四层报文的分析，从而过滤出会触发的数据报文。'
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
          name: '服务器IP地址'
          type: string
          enum:
          - DOMAIN
          - HOSTNAME
          - IP
          - IPLIST
          required: false
          description: 'SVRIP的取值需和现网SBC-Uip（媒体面IP）地址规划一致。SBC-Uip（媒体面IP）地址有多个时需要配置多条。'
          data_source: '本端规划'
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
        SVRIPMASKLEN:
          name: '服务器IP地址掩码长度'
          type: integer
          minimum: 0
          maximum: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MSSTARTPORT:
          name: '手机起始端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: '设置手机起始端口号。该参数不大于手机结束端口号。'
          data_source: '本端规划'
          pattern: ''
          default: 0
        MSENDPORT:
          name: '手机结束端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: '设置手机结束端口号。该参数不小于手机起始端口号。'
          data_source: '本端规划'
          pattern: ''
          default: 65535
        SVRSTARTPORT:
          name: '服务器起始端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: '设置服务器起始端口号。该参数不大于服务器结束端口号。'
          data_source: '本端规划'
          pattern: ''
          default: 0
        SVRENDPORT:
          name: '服务器结束端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: '设置服务器结束端口号。该参数不小于服务器起始端口号。'
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
        SVRIPMASK:
          name: '服务器IP地址反掩码'
          type: string
          maxLength: 15
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
    add_filteripv6_list_1:
      type: items
      properties:
        FILTERNAME:
          name: '过滤器名字'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '配置过滤器名字。UPF通过将用户上下行报文匹配filter，实现报文的过滤。'
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
          description: '任意三四层协议。'
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
          data_source: ''
          pattern: ''
          default: ''
        MSSTARTPORT:
          name: '手机起始端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: '设置手机起始端口号。该参数不大于手机结束端口号。'
          data_source: '本端规划'
          pattern: ''
          default: 0
        MSENDPORT:
          name: '手机结束端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: '设置手机结束端口号。该参数不小于手机起始端口号。'
          data_source: '本端规划'
          pattern: ''
          default: 65535
        SVRSTARTPORT:
          name: '服务器起始端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: '设置服务器起始端口号。该参数不大于服务器结束端口号。'
          data_source: '本端规划'
          pattern: ''
          default: 0
        SVRENDPORT:
          name: '服务器结束端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: '设置服务器结束端口号。该参数不小于服务器起始端口号。'
          data_source: '本端规划'
          pattern: ''
          default: 65535
        SVRIPV6:
          name: '服务器IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: 'SVRIP的取值需和现网SBC-Uip（媒体面IP）地址规划一致。SBC-Uip（媒体面IP）地址有多个时需要配置多条。'
          data_source: '本端规划'
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
    add_fltbindflowf_list_2:
      type: items
      properties:
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FILTERNAME:
          name: '过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
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
    add_urr_list_2:
      type: items
      properties:
        URRNAME:
          name: '使用量上报规则名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '增加使用量上报规则信息。存在多条记录时，使用量上报规则名称不能重复。  “URRID”在所有URR内唯一。  使用量上报模式、计费标识组成类型、计费组以及计费统计类型请根据业务规划进行配置。'
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
          data_source: '本端规划'
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
          data_source: '本端规划'
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
          data_source: '本端规划'
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
          data_source: '本端规划'
          pattern: ''
          default: VOLUME
        RG:
          name: '计费组'
          type: integer
          minimum: 0
          maximum: 4294967294
          required: false
          description: '该参数用于设置计费组。报表功能开启，软参bit1557开启，则需要配置此参数，同时参数值需要与SMF保持一致，否则报表上报的RG与实际计费的RG不一致。'
          data_source: '本端规划'
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
          description: '增加使用量上报规则组。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPURRNAME1:
          name: '上行发起URR名称1'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        DOWNURRNAME1:
          name: '下行发起URR名称1'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPURRNAME2:
          name: '上行发起URR名称2'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        DOWNURRNAME2:
          name: '下行发起URR名称2'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_qosprop_list:
      type: items
      properties:
        QOSPROPNAME:
          name: 'Qos属性名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '配置静态PCC策略的QoS参数。存在多条记录时，QoS属性名称不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        GBRUPLKVALUE:
          name: '保证的上行比特率'
          type: integer
          minimum: 0
          maximum: 20000000
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        GBRDNLKVALUE:
          name: '保证的下行比特率'
          type: integer
          minimum: 0
          maximum: 20000000
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        MBRUPLKVALUE:
          name: '最大上行比特率'
          type: integer
          minimum: 0
          maximum: 20000000
          required: false
          description: 'PCF正常时，MBR\GBR是由UE携带给SBC网元，然后由SBC网元根据UE请求的带宽以及和UE协商的音频编解码方式的带宽要求等下发，并且GBR和MBR的UL/DL带宽按照相同值下发。  PCF故障bypass期间，创建专有QoSFlow/专有承载时，使用SMF上配置的MBR\GBR。参考IMS音频编解码带宽要求，建议按照64Kbit/s，不影响语音业务体验。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MBRDNLKVALUE:
          name: '最大下行比特率'
          type: integer
          minimum: 0
          maximum: 20000000
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        QOSURRNAME:
          name: 'QoS使用量上报规则名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '该业务可以抢占已经分配给其他低优先级业务流的资源时，设置为ENABLE。此处以抢占为例。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DECOUPLINGSW:
          name: '上下行解耦开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        KEYFLOWDETECTSW:
          name: '关键流检测开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        KEYFLOWSPEED:
          name: '关键流速率（千比特每秒）'
          type: integer
          minimum: 1
          maximum: 2048
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 50
        KEYFLOWTIME:
          name: '关键流时长（秒）'
          type: integer
          minimum: 5
          maximum: 60
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 5
    add_pccpolicygrp_list_1:
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
        QOSPROPNAME:
          name: 'Qos属性名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: 'QoS参数，已通过**ADD QOSPROP**命令配置完成。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
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
        URRGROUPNAME:
          name: '使用量上报规则组名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '使用**ADD URRGROUP**定义的使用量上报规则组。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        EVENTCHARGEFLAG:
          name: '事件计费标识'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        EVENTCHGPOINT:
          name: '事件计费点'
          type: string
          enum:
          - FINISH
          - REQUEST
          - RESPONSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: RESPONSE
        MMSCHARGETYPE:
          name: '彩信计费类型'
          type: string
          enum:
          - MULTI
          - SINGLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: SINGLE
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
    add_rule_list_1:
      type: items
      properties:
        RULENAME:
          name: '规则名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '-'
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
        PRIORITY:
          name: '全局优先级'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
          description: '* PCF下发的用于创建语音专有QoS Flow/专有承载的规则的优先级高于本地配置的用于创建语音专有QoS Flow/专有承载的规则；本地配置的用于创建语音专有QoS Flow/专有承载的规则优先级高于PCF下发的any to any的动态规则和本地配置的any to any的预定义规则。 * 以实际规划为准。'
          data_source: '与对端协商'
          pattern: ''
          default: 4294967295
        POLICYNAME:
          name: '策略名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: '绑定的PCC策略组已通过**ADD PCCPOLICYGRP**命令配置，可以通过**ADD PCCPOLICYGRP**命令查询。'
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
    add_rulebinding_list_1:
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
        RULENAME:
          name: '规则名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: 'UserProfile绑定的业务规则，已通过**ADD RULE**  命令配置完成。'
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
    set_refreshsrv_list_3:
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
          data_source: '与对端协商'
          pattern: ''
          default: ''
    add_apnimssigfltr_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '已通过命令**ADD APN**进行配置，可以使用命令查询APN配置（LST APN）查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 1
          maximum: 64
          required: true
          description: '* IMS信令专用上下文的Filter。 * 若动态规则所关联的APN已配置IMS业务（可通过**LST APNIMSSIGFLTR**命令查询），则需要配置该命令，否则无需该命令。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP地址版本'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SRCIPV4SPECTYPE:
          name: '源IPv4地址指定方式'
          type: string
          enum:
          - ANY
          - SPECIFY
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SRCIPV4ADDR:
          name: '源IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SRCIPV4MASKLEN:
          name: '源IPv4地址掩码长度'
          type: integer
          minimum: 0
          maximum: 32
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SRCPORTSPECTYPE:
          name: '源端口指定方式'
          type: string
          enum:
          - ANY
          - SPECIFY
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        DSTIPV4SPECTYPE:
          name: '目的IPv4地址指定方式'
          type: string
          enum:
          - ANY
          - SPECIFY
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        DSTPORTSPECTYPE:
          name: '目的端口指定方式'
          type: string
          enum:
          - ANY
          - SPECIFY
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PROSPECTYPE:
          name: '协议指定方式'
          type: string
          enum:
          - ANY
          - SPECIFY
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SRCIPV6ADDR:
          name: '源IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SRCIPV6SPECTYPE:
          name: '源IPv6地址指定方式'
          type: string
          enum:
          - ANY
          - SPECIFY
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        DSTIPV6SPECTYPE:
          name: '目的IPv6地址指定方式'
          type: string
          enum:
          - ANY
          - SPECIFY
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SRCIPV6PREFLEN:
          name: '源IPv6地址前缀长度'
          type: integer
          minimum: 0
          maximum: 128
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        DSTIPV4ADDR:
          name: '目的IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DSTIPV4MASKLEN:
          name: '目的IPv4地址掩码长度'
          type: integer
          minimum: 0
          maximum: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DSTIPV6ADDR:
          name: '目的IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DSTIPV6PREFLEN:
          name: '目的IPv6地址前缀长度'
          type: integer
          minimum: 0
          maximum: 128
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DSTPORTEND:
          name: '目的端口号结束'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DSTPORTSTART:
          name: '目的端口号开始'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PROTOCOL:
          name: '协议类型'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRCPORTEND:
          name: '源端口号结束'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRCPORTSTART:
          name: '源端口号开始'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_softpara_list:
      type: items
      properties:
        DT:
          name: '软参记录数据类型'
          type: string
          enum:
          - BIT
          - BYTE
          - DWORD
          - STRING
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        BYTENUM:
          name: 'Byte索引'
          type: integer
          minimum: 1
          maximum: 1200
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        BYTEVALUE:
          name: 'Byte值'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        BITNUM:
          name: 'Bit索引'
          type: integer
          minimum: 1
          maximum: 3840
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        BITVALUE:
          name: 'Bit值'
          type: integer
          minimum: 0
          maximum: 1
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DWORDNUM:
          name: 'DWord索引'
          type: integer
          minimum: 1
          maximum: 180
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DWORDVALUE:
          name: 'Dword值'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        STRINGNUM:
          name: 'String索引'
          type: integer
          minimum: 1
          maximum: 30
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        STRINGVALUE:
          name: 'String值'
          type: string
          minLength: 0
          maxLength: 64
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_imsbypass_list:
      type: items
      properties:
        IMSBYPASSSW:
          name: 'IMS Bypass开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: '该参数用于设置IMS Bypass开关。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        QOSURRFLOWRPT:
          name: 'QoSURR上报流信息方式'
          type: string
          enum:
          - FILTER
          - FLOW
          required: false
          description: '该参数用于设置IMS业务触发QoSURR时流信息的填充方式。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        QOSURRHYSTIMER:
          name: 'QoSURR的迟滞时间（秒）'
          type: integer
          minimum: 0
          maximum: 3600
          required: false
          description: '该参数用于配置QoS类型URR Stop上报迟滞时间。  整机老化时间是APN老化时长和QoSURR的迟滞时间之和。APN老化时间通过****LST APNFLOWAGETIME****或****LST FLOWAGETIME****查询**。**'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    add_filter_list:
    - FILTERNAME: 'filter_test'
      L34PROTTYPE: STRING
      L34PROTOCOL: ANY
      L34PROTNUM: ''
    add_filteripv6_list:
    - FILTERNAME: 'filter_testV6'
      L34PROTTYPEV6: STRING
      L34PROTOCOL: ANY
      L34PROTNUM: ''
    add_flowfilter_list:
    - FLOWFILTERNAME: 'flowfilter_test'
    add_fltbindflowf_list:
    - FLOWFILTERNAME: 'flowfilter_test'
      FILTERNAME: 'filter_test'
    add_urr_list:
    - URRNAME: 'urr_signaling_offline'
      URRID: 2005
      USAGERPTMODE: OFFLINE
      OFFMETERINGTYPE: VOLUME
      RG: 20
      ONLMETERINGTYPE: VOLUME
      DFTQUOTAPARA: Byte
      DFTQUOTATIME: ''
      DFTQUOTAVOLUME: ''
      SID: ''
    add_urrgroup_list:
    - URRGROUPNAME: 'urrg_signaling_01'
      UPURRNAME1: 'urr_signaling_offline'
      DOWNURRNAME1: 'urr_signaling_offline'
      UPURRNAME2: 'urr_signaling_online'
      DOWNURRNAME2: 'urr_signaling_online'
    add_pccpolicygrp_list:
    - PCCPOLICYGRPNM: 'pccpolicygrp_signaling'
      FUPSESSIONEXC: DISABLE
      TOKENFUNCFLAG: DISABLE
      SIGNALASSOCIATE: ENABLE
      ADCMUTEFLAG: ENABLE
      HTTP2DEGRADESW: INHERIT
      URRGROUPNAME: 'urrg_signaling_01'
      EVENTCHARGEFLAG: DISABLE
      EVENTCHGPOINT: RESPONSE
      MMSCHARGETYPE: SINGLE
      TOKENENCRYALG: SHA256
      TOKENSECRETKEY: ''
      TOKENSECRETKEYCONFIRM: ''
    add_rule_list:
    - RULENAME: 'rule_ims_signaling'
      POLICYTYPE: PCC
      FILTERINGMODE: FLOWFILTER
      FLOWFILTERNAME: 'flowfilter_test'
      PRIORITY: 241
      POLICYNAME: 'pccpolicygrp_signaling'
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
    - USERPROFILENAME: 'up_ims'
      ALIASMARKFLAG: DISABLE
      DDOSCHECK: DISABLE
      LOCRPTSWITCH: INHERIT
    add_rulebinding_list:
    - USERPROFILENAME: 'up_ims'
      RULENAME: 'rule_ims_signaling'
    set_refreshsrv_list:
    - REFRESHTYPE: ALL
    add_filter_list_1:
    - FILTERNAME: 'filter_bypass'
      L34PROTTYPE: STRING
      L34PROTOCOL: ANY
      SVRIPMODE: IP
      SVRIP: '192.168.10.67'
      SVRIPMASKTYPE: LENGTHTYPE
      SVRIPMASKLEN: 32
      MSSTARTPORT: 0
      MSENDPORT: 65535
      SVRSTARTPORT: 0
      SVRENDPORT: 65535
      L34PROTNUM: ''
      SVRIPMASK: ''
      DOMAINVALUE: ''
      HOSTNAME: ''
      HOSTPRIORITY: ''
      SVRIPLISTNAME: ''
    add_filteripv6_list_1:
    - FILTERNAME: 'filterV6_bypass'
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
    add_flowfilter_list_1:
    - FLOWFILTERNAME: 'flowfilter_bypass'
      TETHERDETFLAG: NONE
    add_fltbindflowf_list_2:
    - FLOWFILTERNAME: 'flowfilter_bypass'
      FILTERNAME: 'filter_bypass'
    set_refreshsrv_list_1:
    - REFRESHTYPE: USERPROFILE
    add_urr_list_2:
    - URRNAME: 'urr_qos_01'
      URRID: 1006
      USAGERPTMODE: QOS
      OFFMETERINGTYPE: VOLUME
      ONLMETERINGTYPE: VOLUME
      RG: 10
      DFTQUOTAPARA: Byte
      DFTQUOTATIME: ''
      DFTQUOTAVOLUME: ''
      SID: ''
    add_urrgroup_list_1:
    - URRGROUPNAME: 'urrg_voice_01'
      UPURRNAME1: 'urr_voice_offline'
      DOWNURRNAME1: 'urr_voice_offline'
      UPURRNAME2: 'urr_voice_online'
      DOWNURRNAME2: 'urr_voice_online'
    add_qosprop_list:
    - QOSPROPNAME: 'qosprop_voice'
      GBRUPLKVALUE: 64
      GBRDNLKVALUE: 64
      MBRUPLKVALUE: 64
      MBRDNLKVALUE: 64
      QOSURRNAME: 'urr_qos_01'
      DECOUPLINGSW: DISABLE
      KEYFLOWDETECTSW: DISABLE
      KEYFLOWSPEED: 50
      KEYFLOWTIME: 5
    add_pccpolicygrp_list_1:
    - PCCPOLICYGRPNM: 'pccpolicygrp_voice'
      FUPSESSIONEXC: DISABLE
      TOKENFUNCFLAG: DISABLE
      SIGNALASSOCIATE: ENABLE
      ADCMUTEFLAG: ENABLE
      QOSPROPNAME: 'qosprop_voice'
      HTTP2DEGRADESW: INHERIT
      URRGROUPNAME: 'urrg_voice_01'
      EVENTCHARGEFLAG: DISABLE
      EVENTCHGPOINT: RESPONSE
      MMSCHARGETYPE: SINGLE
      TOKENENCRYALG: SHA256
      TOKENSECRETKEY: ''
      TOKENSECRETKEYCONFIRM: ''
    add_rule_list_1:
    - RULENAME: 'rule_ims_voice'
      POLICYTYPE: PCC
      FILTERINGMODE: FLOWFILTER
      FLOWFILTERNAME: 'flowfilter_bypass'
      PRIORITY: 240
      POLICYNAME: 'pccpolicygrp_voice'
      FLWFLTRGRPNAME: ''
      ADCMUTEFLAG: ENABLE
      ALGSWITCH: DISABLE
      RDSTRIGGERFLAG: DISABLE
      REDIRIPVERFLAG: ''
      REMARKFPISEL: REMARK
      SRVLBOFLAG: DISABLE
      WORKERNAME: ''
      WORKERPARA: ''
    add_rulebinding_list_1:
    - USERPROFILENAME: 'up_ims'
      RULENAME: 'rule_ims_voice'
      POLICYTYPE: PCC
    set_refreshsrv_list_3:
    - REFRESHTYPE: ALL
    add_apnimssigfltr_list:
    - APN: 'ims'
      PRIORITY: 1
      IPVERSION: IPV4
      SRCIPV4SPECTYPE: SPECIFY
      SRCIPV4ADDR: '192.168.10.67'
      SRCIPV4MASKLEN: 24
      SRCPORTSPECTYPE: ANY
      DSTIPV4SPECTYPE: ANY
      DSTPORTSPECTYPE: ANY
      PROSPECTYPE: ANY
      SRCIPV6ADDR: 'fc00:8028:5002:10D::181'
      SRCIPV6SPECTYPE: SPECIFY
      DSTIPV6SPECTYPE: ANY
      SRCIPV6PREFLEN: 120
      DSTIPV4ADDR: ''
      DSTIPV4MASKLEN: ''
      DSTIPV6ADDR: ''
      DSTIPV6PREFLEN: ''
      DSTPORTEND: ''
      DSTPORTSTART: ''
      PROTOCOL: ''
      SRCPORTEND: ''
      SRCPORTSTART: ''
    set_softpara_list:
    - DT: BYTE
      BYTENUM: 1124
      BYTEVALUE: 3
      BITNUM: ''
      BITVALUE: ''
      DWORDNUM: ''
      DWORDVALUE: ''
      STRINGNUM: ''
      STRINGVALUE: ''
    set_imsbypass_list:
    - IMSBYPASSSW: ENABLE
      QOSURRFLOWRPT: FLOW
      QOSURRHYSTIMER: 0
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置语音缺省QoS Flow/缺省承载静态PCC策略。配置三四层过滤条件。

### 仅当局点未配置语音缺省QoS Flow/缺省承载静态PCC策略时，执行本步骤。否则，跳过本步骤。

#### 1.1 配置三四层过滤条件。

```jinja2
{%- if is_optional_default_static_pcc_policy -%}
    {%- for item in add_filter_list -%}
        ADD FILTER:
        {#- --- 必选参数 --- -#}
        FILTERNAME="{{item.FILTERNAME}}",
        L34PROTTYPE={{item.L34PROTTYPE}},
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
{%- if is_optional_default_static_pcc_policy -%}
    {%- for item in add_filteripv6_list -%}
        ADD FILTERIPV6:
        {#- --- 必选参数 --- -#}
        FILTERNAME="{{item.FILTERNAME}}",
        L34PROTTYPEV6={{item.L34PROTTYPEV6}},
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

#### 1.2 配置流过滤器。

```jinja2
{%- if is_optional_default_static_pcc_policy -%}
    {%- for item in add_flowfilter_list -%}
        ADD FLOWFILTER:
        {#- --- 必选参数 --- -#}
        FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 流过滤器必须至少绑定一个filter或一个l7filter，否则所有报文都匹配不上该流过滤器。

#### 1.3 配置三四层过滤条件与流过滤器的绑定关系。

```jinja2
{%- if is_optional_default_static_pcc_policy -%}
    {%- for item in add_fltbindflowf_list -%}
        ADD FLTBINDFLOWF:
        {#- --- 必选参数 --- -#}
        FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
        FILTERNAME="{{item.FILTERNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 1.4 增加使用量上报规则信息。

```jinja2
{%- if is_optional_default_static_pcc_policy -%}
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
        {#- --- 条件可选：USAGERPTMODE=ONLINE/OFFLINE 时可选 --- -#}
        {%- if item.USAGERPTMODE in ['ONLINE', 'OFFLINE'] -%}
            {%- if item.RG is not none -%}
                RG={{item.RG}},
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
            {%- if item.SID is not none -%}
                SID={{item.SID}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 1.5 配置上行和下行业务对应的URR。

```jinja2
{%- if is_optional_default_static_pcc_policy -%}
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

#### 1.6 配置PCC策略组。

```jinja2
{%- if is_optional_default_static_pcc_policy -%}
    {%- for item in add_pccpolicygrp_list -%}
        ADD PCCPOLICYGRP:
        {#- --- 必选参数 --- -#}
        PCCPOLICYGRPNM="{{item.PCCPOLICYGRPNM}}",
        {#- --- 可选参数 --- -#}
        {%- if item.FUPSESSIONEXC is not none -%}
            FUPSESSIONEXC={{item.FUPSESSIONEXC}},
        {%- endif -%}
        {%- if item.TOKENFUNCFLAG is not none -%}
            TOKENFUNCFLAG={{item.TOKENFUNCFLAG}},
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
        {%- if item.URRGROUPNAME is not none -%}
            URRGROUPNAME="{{item.URRGROUPNAME}}",
        {%- endif -%}
        {%- if item.EVENTCHARGEFLAG is not none -%}
            EVENTCHARGEFLAG={{item.EVENTCHARGEFLAG}},
        {%- endif -%}
        {%- if item.EVENTCHGPOINT is not none -%}
            EVENTCHGPOINT={{item.EVENTCHGPOINT}},
        {%- endif -%}
        {%- if item.MMSCHARGETYPE is not none -%}
            MMSCHARGETYPE={{item.MMSCHARGETYPE}},
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

#### 1.7 配置规则。

```jinja2
{%- if is_optional_default_static_pcc_policy -%}
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

#### 1.8 创建UserProfile。

#### 如果已配置了APN ims使用的用户模板，则跳过本步骤。

```jinja2
{%- if is_optional_default_static_pcc_policy and is_optional_create_userprofile -%}
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
        {%- if item.LOCRPTSWITCH is not none -%}
            LOCRPTSWITCH={{item.LOCRPTSWITCH}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 1.9 将已配置的rule绑定到UserProfile。

```jinja2
{%- if is_optional_default_static_pcc_policy -%}
    {%- for item in add_rulebinding_list -%}
        ADD RULEBINDING:
        {#- --- 必选参数 --- -#}
        USERPROFILENAME="{{item.USERPROFILENAME}}",
        RULENAME="{{item.RULENAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 1.10 将新配置的Filter跟UserProfile置为生效。

```jinja2
{%- if is_optional_default_static_pcc_policy -%}
    {%- for item in set_refreshsrv_list -%}
        SET REFRESHSRV:
        {#- --- 必选参数 --- -#}
        REFRESHTYPE={{item.REFRESHTYPE}},
        ;
    {%- endfor -%}
{%- endif -%}
```

### 2 配置语音专有QoS Flow/专有承载静态PCC策略。

#### 2.1 配置三四层过滤条件。

```jinja2
{%- for item in add_filter_list_1 -%}
    ADD FILTER:
    {#- --- 必选参数 --- -#}
    FILTERNAME="{{item.FILTERNAME}}",
    L34PROTTYPE={{item.L34PROTTYPE}},
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
    {#- --- 条件必选：SVRIPMODE=DOMAIN 时必选 --- -#}
    {%- if item.SVRIPMODE == 'DOMAIN' -%}
        DOMAINVALUE="{{item.DOMAINVALUE}}",
    {%- endif -%}
    {#- --- 条件必选：SVRIPMODE=HOSTNAME/DOMAIN 时必选 --- -#}
    {%- if item.SVRIPMODE in ['HOSTNAME', 'DOMAIN'] -%}
        HOSTNAME="{{item.HOSTNAME}}",
    {%- endif -%}
    {#- --- 条件必选：L34PROTTYPE=NUMBER 时必选 --- -#}
    {%- if item.L34PROTTYPE == 'NUMBER' -%}
        L34PROTNUM={{item.L34PROTNUM}},
    {%- endif -%}
    {#- --- 条件必选：SVRIPMODE=IPLIST 时必选 --- -#}
    {%- if item.SVRIPMODE == 'IPLIST' -%}
        SVRIPLISTNAME="{{item.SVRIPLISTNAME}}",
    {%- endif -%}
    {#- --- 条件必选：SVRIPMASKTYPE=IPTYPE 时必选 --- -#}
    {%- if item.SVRIPMASKTYPE == 'IPTYPE' -%}
        SVRIPMASK="{{item.SVRIPMASK}}",
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

#### 2.2 配置流过滤器。

```jinja2
{%- for item in add_flowfilter_list_1 -%}
    ADD FLOWFILTER:
    {#- --- 必选参数 --- -#}
    FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.TETHERDETFLAG is not none -%}
        TETHERDETFLAG={{item.TETHERDETFLAG}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.3 配置三四层过滤条件与流过滤器的绑定关系。

```jinja2
{%- for item in add_fltbindflowf_list_2 -%}
    ADD FLTBINDFLOWF:
    {#- --- 必选参数 --- -#}
    FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
    FILTERNAME="{{item.FILTERNAME}}",
    ;
{%- endfor -%}
```

#### 2.4 将新配置的Filter置为生效。

```jinja2
{%- for item in set_refreshsrv_list_1 -%}
    SET REFRESHSRV:
    {#- --- 必选参数 --- -#}
    REFRESHTYPE={{item.REFRESHTYPE}},
    ;
{%- endfor -%}
```

#### 2.5 增加使用量上报规则信息。

```jinja2
{%- for item in add_urr_list_2 -%}
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
    {#- --- 条件可选：USAGERPTMODE=ONLINE/OFFLINE 时可选 --- -#}
    {%- if item.USAGERPTMODE in ['ONLINE', 'OFFLINE'] -%}
        {%- if item.RG is not none -%}
            RG={{item.RG}},
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
        {%- if item.SID is not none -%}
            SID={{item.SID}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.6 增加使用量上报规则组。

```jinja2
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
```

#### 2.7 配置静态PCC策略的QoS参数。

```jinja2
{%- for item in add_qosprop_list -%}
    ADD QOSPROP:
    {#- --- 必选参数 --- -#}
    QOSPROPNAME="{{item.QOSPROPNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.GBRUPLKVALUE is not none -%}
        GBRUPLKVALUE={{item.GBRUPLKVALUE}},
    {%- endif -%}
    {%- if item.GBRDNLKVALUE is not none -%}
        GBRDNLKVALUE={{item.GBRDNLKVALUE}},
    {%- endif -%}
    {%- if item.MBRUPLKVALUE is not none -%}
        MBRUPLKVALUE={{item.MBRUPLKVALUE}},
    {%- endif -%}
    {%- if item.MBRDNLKVALUE is not none -%}
        MBRDNLKVALUE={{item.MBRDNLKVALUE}},
    {%- endif -%}
    {%- if item.QOSURRNAME is not none -%}
        QOSURRNAME="{{item.QOSURRNAME}}",
    {%- endif -%}
    {%- if item.DECOUPLINGSW is not none -%}
        DECOUPLINGSW={{item.DECOUPLINGSW}},
    {%- endif -%}
    {%- if item.KEYFLOWDETECTSW is not none -%}
        KEYFLOWDETECTSW={{item.KEYFLOWDETECTSW}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：KEYFLOWDETECTSW=ENABLE 时可选 --- -#}
    {%- if item.KEYFLOWDETECTSW == 'ENABLE' -%}
        {%- if item.KEYFLOWSPEED is not none -%}
            KEYFLOWSPEED={{item.KEYFLOWSPEED}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：KEYFLOWDETECTSW=ENABLE 时可选 --- -#}
    {%- if item.KEYFLOWDETECTSW == 'ENABLE' -%}
        {%- if item.KEYFLOWTIME is not none -%}
            KEYFLOWTIME={{item.KEYFLOWTIME}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.8 配置PCC策略组。

```jinja2
{%- for item in add_pccpolicygrp_list_1 -%}
    ADD PCCPOLICYGRP:
    {#- --- 必选参数 --- -#}
    PCCPOLICYGRPNM="{{item.PCCPOLICYGRPNM}}",
    {#- --- 可选参数 --- -#}
    {%- if item.FUPSESSIONEXC is not none -%}
        FUPSESSIONEXC={{item.FUPSESSIONEXC}},
    {%- endif -%}
    {%- if item.TOKENFUNCFLAG is not none -%}
        TOKENFUNCFLAG={{item.TOKENFUNCFLAG}},
    {%- endif -%}
    {%- if item.SIGNALASSOCIATE is not none -%}
        SIGNALASSOCIATE={{item.SIGNALASSOCIATE}},
    {%- endif -%}
    {%- if item.ADCMUTEFLAG is not none -%}
        ADCMUTEFLAG={{item.ADCMUTEFLAG}},
    {%- endif -%}
    {%- if item.QOSPROPNAME is not none -%}
        QOSPROPNAME="{{item.QOSPROPNAME}}",
    {%- endif -%}
    {%- if item.HTTP2DEGRADESW is not none -%}
        HTTP2DEGRADESW={{item.HTTP2DEGRADESW}},
    {%- endif -%}
    {%- if item.URRGROUPNAME is not none -%}
        URRGROUPNAME="{{item.URRGROUPNAME}}",
    {%- endif -%}
    {%- if item.EVENTCHARGEFLAG is not none -%}
        EVENTCHARGEFLAG={{item.EVENTCHARGEFLAG}},
    {%- endif -%}
    {%- if item.EVENTCHGPOINT is not none -%}
        EVENTCHGPOINT={{item.EVENTCHGPOINT}},
    {%- endif -%}
    {%- if item.MMSCHARGETYPE is not none -%}
        MMSCHARGETYPE={{item.MMSCHARGETYPE}},
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
```

#### 2.9 配置业务策略规则。

```jinja2
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
```

#### 2.10 将已配置的Rule绑定到UserProfile。

```jinja2
{%- for item in add_rulebinding_list_1 -%}
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

#### 2.11 将新配置的Filter和UserProfile置为生效。

```jinja2
{%- for item in set_refreshsrv_list_3 -%}
    SET REFRESHSRV:
    {#- --- 必选参数 --- -#}
    REFRESHTYPE={{item.REFRESHTYPE}},
    ;
{%- endfor -%}
```

#### 2.12 基于APN配置IMS业务。

```jinja2
{%- for item in add_apnimssigfltr_list -%}
    ADD APNIMSSIGFLTR:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    PRIORITY={{item.PRIORITY}},
    IPVERSION={{item.IPVERSION}},
    {#- --- 可选参数 --- -#}
    {%- if item.SRCPORTSPECTYPE is not none -%}
        SRCPORTSPECTYPE={{item.SRCPORTSPECTYPE}},
    {%- endif -%}
    {%- if item.DSTPORTSPECTYPE is not none -%}
        DSTPORTSPECTYPE={{item.DSTPORTSPECTYPE}},
    {%- endif -%}
    {%- if item.PROSPECTYPE is not none -%}
        PROSPECTYPE={{item.PROSPECTYPE}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：SRCIPV4SPECTYPE=SPECIFY 时必选 --- -#}
    {%- if item.SRCIPV4SPECTYPE == 'SPECIFY' -%}
        SRCIPV4ADDR="{{item.SRCIPV4ADDR}}",
    {%- endif -%}
    {#- --- 条件必选：SRCIPV4SPECTYPE=SPECIFY 时必选 --- -#}
    {%- if item.SRCIPV4SPECTYPE == 'SPECIFY' -%}
        SRCIPV4MASKLEN={{item.SRCIPV4MASKLEN}},
    {%- endif -%}
    {#- --- 条件必选：SRCIPV6SPECTYPE=SPECIFY 时必选 --- -#}
    {%- if item.SRCIPV6SPECTYPE == 'SPECIFY' -%}
        SRCIPV6ADDR="{{item.SRCIPV6ADDR}}",
    {%- endif -%}
    {#- --- 条件必选：SRCIPV6SPECTYPE=SPECIFY 时必选 --- -#}
    {%- if item.SRCIPV6SPECTYPE == 'SPECIFY' -%}
        SRCIPV6PREFLEN={{item.SRCIPV6PREFLEN}},
    {%- endif -%}
    {#- --- 条件必选：DSTIPV4SPECTYPE=SPECIFY 时必选 --- -#}
    {%- if item.DSTIPV4SPECTYPE == 'SPECIFY' -%}
        DSTIPV4ADDR="{{item.DSTIPV4ADDR}}",
    {%- endif -%}
    {#- --- 条件必选：DSTIPV4SPECTYPE=SPECIFY 时必选 --- -#}
    {%- if item.DSTIPV4SPECTYPE == 'SPECIFY' -%}
        DSTIPV4MASKLEN={{item.DSTIPV4MASKLEN}},
    {%- endif -%}
    {#- --- 条件必选：DSTIPV6SPECTYPE=SPECIFY 时必选 --- -#}
    {%- if item.DSTIPV6SPECTYPE == 'SPECIFY' -%}
        DSTIPV6ADDR="{{item.DSTIPV6ADDR}}",
    {%- endif -%}
    {#- --- 条件必选：DSTIPV6SPECTYPE=SPECIFY 时必选 --- -#}
    {%- if item.DSTIPV6SPECTYPE == 'SPECIFY' -%}
        DSTIPV6PREFLEN={{item.DSTIPV6PREFLEN}},
    {%- endif -%}
    {#- --- 条件必选：DSTPORTSPECTYPE=SPECIFY 时必选 --- -#}
    {%- if item.DSTPORTSPECTYPE == 'SPECIFY' -%}
        DSTPORTEND={{item.DSTPORTEND}},
    {%- endif -%}
    {#- --- 条件必选：DSTPORTSPECTYPE=SPECIFY 时必选 --- -#}
    {%- if item.DSTPORTSPECTYPE == 'SPECIFY' -%}
        DSTPORTSTART={{item.DSTPORTSTART}},
    {%- endif -%}
    {#- --- 条件必选：PROSPECTYPE=SPECIFY 时必选 --- -#}
    {%- if item.PROSPECTYPE == 'SPECIFY' -%}
        PROTOCOL={{item.PROTOCOL}},
    {%- endif -%}
    {#- --- 条件必选：SRCPORTSPECTYPE=SPECIFY 时必选 --- -#}
    {%- if item.SRCPORTSPECTYPE == 'SPECIFY' -%}
        SRCPORTEND={{item.SRCPORTEND}},
    {%- endif -%}
    {#- --- 条件必选：SRCPORTSPECTYPE=SPECIFY 时必选 --- -#}
    {%- if item.SRCPORTSPECTYPE == 'SPECIFY' -%}
        SRCPORTSTART={{item.SRCPORTSTART}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPVERSION=IPV4 时可选 --- -#}
    {%- if item.IPVERSION == 'IPV4' -%}
        {%- if item.SRCIPV4SPECTYPE is not none -%}
            SRCIPV4SPECTYPE={{item.SRCIPV4SPECTYPE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVERSION=IPV4 时可选 --- -#}
    {%- if item.IPVERSION == 'IPV4' -%}
        {%- if item.DSTIPV4SPECTYPE is not none -%}
            DSTIPV4SPECTYPE={{item.DSTIPV4SPECTYPE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVERSION=IPV6 时可选 --- -#}
    {%- if item.IPVERSION == 'IPV6' -%}
        {%- if item.SRCIPV6SPECTYPE is not none -%}
            SRCIPV6SPECTYPE={{item.SRCIPV6SPECTYPE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IPVERSION=IPV6 时可选 --- -#}
    {%- if item.IPVERSION == 'IPV6' -%}
        {%- if item.DSTIPV6SPECTYPE is not none -%}
            DSTIPV6SPECTYPE={{item.DSTIPV6SPECTYPE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置PCF bypas条件。

```jinja2
{%- for item in set_softpara_list -%}
    SET SOFTPARA:
    {#- --- 必选参数 --- -#}
    DT={{item.DT}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：DT=BYTE 时必选 --- -#}
    {%- if item.DT == 'BYTE' -%}
        BYTENUM={{item.BYTENUM}},
    {%- endif -%}
    {#- --- 条件必选：DT=BYTE 时必选 --- -#}
    {%- if item.DT == 'BYTE' -%}
        BYTEVALUE={{item.BYTEVALUE}},
    {%- endif -%}
    {#- --- 条件必选：DT=BIT 时必选 --- -#}
    {%- if item.DT == 'BIT' -%}
        BITNUM={{item.BITNUM}},
    {%- endif -%}
    {#- --- 条件必选：DT=BIT 时必选 --- -#}
    {%- if item.DT == 'BIT' -%}
        BITVALUE={{item.BITVALUE}},
    {%- endif -%}
    {#- --- 条件必选：DT=DWORD 时必选 --- -#}
    {%- if item.DT == 'DWORD' -%}
        DWORDNUM={{item.DWORDNUM}},
    {%- endif -%}
    {#- --- 条件必选：DT=DWORD 时必选 --- -#}
    {%- if item.DT == 'DWORD' -%}
        DWORDVALUE={{item.DWORDVALUE}},
    {%- endif -%}
    {#- --- 条件必选：DT=STRING 时必选 --- -#}
    {%- if item.DT == 'STRING' -%}
        STRINGNUM={{item.STRINGNUM}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：DT=STRING 时可选 --- -#}
    {%- if item.DT == 'STRING' -%}
        {%- if item.STRINGVALUE is not none -%}
            STRINGVALUE="{{item.STRINGVALUE}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in set_imsbypass_list -%}
    SET IMSBYPASS:
    {#- --- 必选参数 --- -#}
    IMSBYPASSSW={{item.IMSBYPASSSW}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IMSBYPASSSW=ENABLE 时可选 --- -#}
    {%- if item.IMSBYPASSSW == 'ENABLE' -%}
        {%- if item.QOSURRFLOWRPT is not none -%}
            QOSURRFLOWRPT={{item.QOSURRFLOWRPT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IMSBYPASSSW=ENABLE 时可选 --- -#}
    {%- if item.IMSBYPASSSW == 'ENABLE' -%}
        {%- if item.QOSURRHYSTIMER is not none -%}
            QOSURRHYSTIMER={{item.QOSURRHYSTIMER}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

