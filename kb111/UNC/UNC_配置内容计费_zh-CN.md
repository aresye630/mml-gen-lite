---
id: ''
name: 配置内容计费
ne_type: UNC
type: feature
description: 用户访问园区业务时，智能分流SMF发起园区会话创建，数据流被分流到专网UPF上，需要在专网SMF和专网UPF上针对园区业务配置内容计费规则。  场景一：运营商对于园区业务未规划单独费率，则使用缺省费率（RG= 2000000002）。  场景二：运营商对于园区业务的费率有单独规划，按照运营商规划配置对应的费率；  此配置页面中的内容计费中的URR、PCCPOLICYGRPNM、RULE名称、UP名称等需要与专网SMF中的名称保持一致。
risk_level: ''
doc_source: ["网络部署","业务专题","5G Core 一跳入家解决方案","一跳入家解决方案（基于3GPP接入方案）","业务初始部署与调测","部署移动VPN","配置专用DNN数据","配置UPF","配置内容计费"]
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
          required: false
          description: '配置三四层过滤条件。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        L34PROTTYPE:
          name: '三四层IPv4协议输入类型'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        L34PROTOCOL:
          name: '三四层IPv4协议输入类型'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        MSSTARTPORT:
          name: 'MSSTARTPORT'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MSENDPORT:
          name: 'MSENDPORT'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SVRSTARTPORT:
          name: 'SVRSTARTPORT'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SVRENDPORT:
          name: 'SVRENDPORT'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_filteripv6_list:
      type: items
      properties:
        FILTERNAME:
          name: 'FILTERNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        L34PROTOCOL:
          name: 'L34PROTOCOL'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MSSTARTPORT:
          name: 'MSSTARTPORT'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MSENDPORT:
          name: 'MSENDPORT'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SVRSTARTPORT:
          name: 'SVRSTARTPORT'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SVRENDPORT:
          name: 'SVRENDPORT'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        L34PROTTYPEV6:
          name: 'L34PROTTYPEV6'
          type: string
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
          required: false
          description: '流过滤器。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TETHERDETFLAG:
          name: 'TETHERDETFLAG'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FLOWFILTERTYPE:
          name: 'FLOWFILTERTYPE'
          type: string
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
          required: false
          description: '流过滤器名称已通过**ADD FLOWFILTER**命令配置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        FILTERNAME:
          name: '过滤器名称'
          type: string
          required: false
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
          required: false
          description: '流过滤器。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TETHERDETFLAG:
          name: 'TETHERDETFLAG'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FLOWFILTERTYPE:
          name: 'FLOWFILTERTYPE'
          type: string
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
          required: false
          description: '流过滤器名称已通过**ADD FLOWFILTER**命令配置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        FILTERNAME:
          name: '过滤器名称'
          type: string
          required: false
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
          data_source: '全网规划'
          pattern: ''
          default: ''
        EVENTRSUVALUE:
          name: '事件配额值（次）'
          type: integer
          minimum: 0
          maximum: 5000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        TIMERSUVALUE:
          name: '时间配额值（秒）'
          type: integer
          minimum: 0
          maximum: 3600000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VOLUMERSUVALUE:
          name: '流量配额值（字节）'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MONITORINGKEY:
          name: '监控属性值'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        N40AGESW:
          name: 'N40接口场景下是否允许老化'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ENABLE
        OFCSRVTMPLNAME:
          name: '离线业务模板名'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OFFCOMPOUNDTYPE:
          name: '离线计费标识组成类型'
          type: string
          enum:
          - ONLYRG
          - ONLYSID
          - RGSID
          - UPDOWNSID
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ONLCOMPOUNDTYPE:
          name: '在线计费标识组成类型'
          type: string
          enum:
          - ONLYRG
          - RGSID
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REDIRENDTOKEN:
          name: 'Gy重定向结束Token'
          type: string
          maxLength: 31
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
          maxLength: 31
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPURRNAME1:
          name: '上行发起URR名称1'
          type: string
          maxLength: 31
          required: false
          description: 'URR已通过**ADD URR**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DOWNURRNAME1:
          name: '下行发起URR名称1'
          type: string
          maxLength: 31
          required: false
          description: 'URR已通过**ADD URR**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        UPURRNAME2:
          name: '上行发起URR名称2'
          type: string
          maxLength: 31
          required: false
          description: 'URR已通过**ADD URR**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DOWNURRNAME2:
          name: '下行发起URR名称2'
          type: string
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
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        FUPSESSIONEXC:
          name: 'FUPSESSIONEXC'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SIGNALASSOCIATE:
          name: 'SIGNALASSOCIATE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ADCMUTEFLAG:
          name: 'ADCMUTEFLAG'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HTTP2DEGRADESW:
          name: 'HTTP2DEGRADESW'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TOKENFUNCFLAG:
          name: 'TOKENFUNCFLAG'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        URRGROUPNAME:
          name: 'URR组名称'
          type: string
          required: false
          description: 'URRGroup已经通过**ADD URRGROUP**配置'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SIGURRGRPNAME:
          name: '信令URR组名称'
          type: string
          required: false
          description: 'URRGroup已经通过**ADD URRGROUP**配置'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_rule_list:
      type: items
      properties:
        RULENAME:
          name: '规则名称'
          type: string
          required: false
          description: '配置内容计费规则。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        POLICYTYPE:
          name: '策略类型'
          type: string
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          required: false
          description: '绑定的FlowFilter已通过**ADD FLOWFILTER**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PRIORITY:
          name: 'PRIORITY'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        POLICYNAME:
          name: '策略名称'
          type: string
          required: false
          description: '绑定的PCC策略组已通过**ADD IPFARMSERVER**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        FILTERINGMODE:
          name: '流过滤器或流过滤器组选择'
          type: string
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_userprofile_list:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          required: false
          description: '与SMF上配置的PCC用户模板名称保持一致。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        ALIASMARKFLAG:
          name: 'ALIASMARKFLAG'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DDOSCHECK:
          name: 'DDOSCHECK'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CAPMODETHRES:
          name: 'CAPMODETHRES'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCRPTSWITCH:
          name: 'LOCRPTSWITCH'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TETHERINGMAXNUM:
          name: 'TETHERINGMAXNUM'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        V6TCPMSSVALUE:
          name: 'V6TCPMSSVALUE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        V4TCPMSSVALUE:
          name: 'V4TCPMSSVALUE'
          type: string
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
          maxLength: 63
          required: true
          description: '使用**ADD USERPROFILE**命令定义的用户模板名称。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        RULENAME:
          name: '规则名称'
          type: string
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
          - FUP
          - HEADEN
          - IPREDIR
          - LBO
          - NON_SPECIFIC_TYPE
          - PCC
          - QOS
          - REMARK_FPI
          - SMARTREDIRECT
          - SRV_TRIGGER
          - TRAFFICCLASS
          - ULCL
          - WEBPROXY
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_urrgrpbinding_list:
      type: items
      properties:
        USERPROFILENAME:
          name: 'USERPROFILENAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DFTURRGRPNAME:
          name: 'DFTURRGRPNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DFTSIGURRGNAME:
          name: 'DFTSIGURRGNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_refreshsrv_list:
      type: items
      properties:
        REFRESHTYPE:
          name: 'REFRESHTYPE'
          type: string
          required: false
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
          required: false
          description: '配置三四层过滤条件。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        L34PROTTYPE:
          name: '三四层IPv4协议输入类型'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        L34PROTOCOL:
          name: '三四层IPv4协议输入类型'
          type: string
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        MSSTARTPORT:
          name: 'MSSTARTPORT'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MSENDPORT:
          name: 'MSENDPORT'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SVRSTARTPORT:
          name: 'SVRSTARTPORT'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SVRENDPORT:
          name: 'SVRENDPORT'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_filteripv6_list_1:
      type: items
      properties:
        FILTERNAME:
          name: 'FILTERNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        L34PROTOCOL:
          name: 'L34PROTOCOL'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MSSTARTPORT:
          name: 'MSSTARTPORT'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MSENDPORT:
          name: 'MSENDPORT'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SVRSTARTPORT:
          name: 'SVRSTARTPORT'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SVRENDPORT:
          name: 'SVRENDPORT'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        L34PROTTYPEV6:
          name: 'L34PROTTYPEV6'
          type: string
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
          required: false
          description: '流过滤器。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TETHERDETFLAG:
          name: 'TETHERDETFLAG'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FLOWFILTERTYPE:
          name: 'FLOWFILTERTYPE'
          type: string
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
          required: false
          description: '流过滤器名称已通过**ADD FLOWFILTER**命令配置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        FILTERNAME:
          name: '过滤器名称'
          type: string
          required: false
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
          required: false
          description: '流过滤器。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TETHERDETFLAG:
          name: 'TETHERDETFLAG'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FLOWFILTERTYPE:
          name: 'FLOWFILTERTYPE'
          type: string
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
          required: false
          description: '流过滤器名称已通过**ADD FLOWFILTER**命令配置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        FILTERNAME:
          name: '过滤器名称'
          type: string
          required: false
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
          data_source: '全网规划'
          pattern: ''
          default: ''
        EVENTRSUVALUE:
          name: '事件配额值（次）'
          type: integer
          minimum: 0
          maximum: 5000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 0
        TIMERSUVALUE:
          name: '时间配额值（秒）'
          type: integer
          minimum: 0
          maximum: 3600000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VOLUMERSUVALUE:
          name: '流量配额值（字节）'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MONITORINGKEY:
          name: '监控属性值'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        N40AGESW:
          name: 'N40接口场景下是否允许老化'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ENABLE
        OFCSRVTMPLNAME:
          name: '离线业务模板名'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OFFCOMPOUNDTYPE:
          name: '离线计费标识组成类型'
          type: string
          enum:
          - ONLYRG
          - ONLYSID
          - RGSID
          - UPDOWNSID
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ONLCOMPOUNDTYPE:
          name: '在线计费标识组成类型'
          type: string
          enum:
          - ONLYRG
          - RGSID
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REDIRENDTOKEN:
          name: 'Gy重定向结束Token'
          type: string
          maxLength: 31
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
          maxLength: 31
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPURRNAME1:
          name: '上行发起URR名称1'
          type: string
          maxLength: 31
          required: false
          description: 'URR已通过**ADD URR**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DOWNURRNAME1:
          name: '下行发起URR名称1'
          type: string
          maxLength: 31
          required: false
          description: 'URR已通过**ADD URR**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        UPURRNAME2:
          name: '上行发起URR名称2'
          type: string
          maxLength: 31
          required: false
          description: 'URR已通过**ADD URR**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DOWNURRNAME2:
          name: '下行发起URR名称2'
          type: string
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
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        FUPSESSIONEXC:
          name: 'FUPSESSIONEXC'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SIGNALASSOCIATE:
          name: 'SIGNALASSOCIATE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ADCMUTEFLAG:
          name: 'ADCMUTEFLAG'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HTTP2DEGRADESW:
          name: 'HTTP2DEGRADESW'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TOKENFUNCFLAG:
          name: 'TOKENFUNCFLAG'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        URRGROUPNAME:
          name: 'URR组名称'
          type: string
          required: false
          description: 'URRGroup已经通过**ADD URRGROUP**配置'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SIGURRGRPNAME:
          name: '信令URR组名称'
          type: string
          required: false
          description: 'URRGroup已经通过**ADD URRGROUP**配置'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_rule_list_2:
      type: items
      properties:
        RULENAME:
          name: '规则名称'
          type: string
          required: false
          description: '配置内容计费规则。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        POLICYTYPE:
          name: '策略类型'
          type: string
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          required: false
          description: '绑定的FlowFilter已通过**ADD FLOWFILTER**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PRIORITY:
          name: 'PRIORITY'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        POLICYNAME:
          name: '策略名称'
          type: string
          required: false
          description: '绑定的PCC策略组已通过**ADD IPFARMSERVER**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        FILTERINGMODE:
          name: '流过滤器或流过滤器组选择'
          type: string
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_userprofile_list_1:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          required: false
          description: '与SMF上配置的PCC用户模板名称保持一致。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        ALIASMARKFLAG:
          name: 'ALIASMARKFLAG'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DDOSCHECK:
          name: 'DDOSCHECK'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CAPMODETHRES:
          name: 'CAPMODETHRES'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCRPTSWITCH:
          name: 'LOCRPTSWITCH'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TETHERINGMAXNUM:
          name: 'TETHERINGMAXNUM'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        V6TCPMSSVALUE:
          name: 'V6TCPMSSVALUE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        V4TCPMSSVALUE:
          name: 'V4TCPMSSVALUE'
          type: string
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
          maxLength: 63
          required: true
          description: '使用**ADD USERPROFILE**命令定义的用户模板名称。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        RULENAME:
          name: '规则名称'
          type: string
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
          - FUP
          - HEADEN
          - IPREDIR
          - LBO
          - NON_SPECIFIC_TYPE
          - PCC
          - QOS
          - REMARK_FPI
          - SMARTREDIRECT
          - SRV_TRIGGER
          - TRAFFICCLASS
          - ULCL
          - WEBPROXY
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_urrgrpbinding_list_1:
      type: items
      properties:
        USERPROFILENAME:
          name: 'USERPROFILENAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DFTURRGRPNAME:
          name: 'DFTURRGRPNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DFTSIGURRGNAME:
          name: 'DFTSIGURRGNAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_refreshsrv_list_1:
      type: items
      properties:
        REFRESHTYPE:
          name: 'REFRESHTYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_filter_list:
    - FILTERNAME: any
      L34PROTTYPE: STRING
      L34PROTOCOL: ANY
      MSSTARTPORT: '0'
      MSENDPORT: '65535'
      SVRSTARTPORT: '0'
      SVRENDPORT: '65535'
    add_filteripv6_list:
    - FILTERNAME: any_ipv6
      L34PROTOCOL: ANY
      MSSTARTPORT: '0'
      MSENDPORT: '65535'
      SVRSTARTPORT: '0'
      SVRENDPORT: '65535'
      L34PROTTYPEV6: STRING
    add_flowfilter_list:
    - FLOWFILTERNAME: any_f_f
      TETHERDETFLAG: NONE
      FLOWFILTERTYPE: USERCONFIG
    add_fltbindflowf_list:
    - FLOWFILTERNAME: any_f_f
      FILTERNAME: any
    add_flowfilter_list_1:
    - FLOWFILTERNAME: any_ipv6_f_f
      TETHERDETFLAG: NONE
      FLOWFILTERTYPE: USERCONFIG
    add_fltbindflowf_list_1:
    - FLOWFILTERNAME: any_ipv6_f_f
      FILTERNAME: any_ipv6
    add_urr_list:
    - URRNAME: 'common_01_cbb_online'
      URRID: 2000000002
      USAGERPTMODE: ONLINE
      ONLMETERINGTYPE: VOLUME
      OFFMETERINGTYPE: VOLUME
      EVENTRSUVALUE: ''
      TIMERSUVALUE: ''
      VOLUMERSUVALUE: ''
      MONITORINGKEY: ''
      N40AGESW: ENABLE
      OFCSRVTMPLNAME: ''
      OFFCOMPOUNDTYPE: ''
      ONLCOMPOUNDTYPE: ''
      REDIRENDTOKEN: ''
    add_urrgroup_list:
    - URRGROUPNAME: 'common_01_ch_p'
      UPURRNAME1: 'common_01_cbb_offline'
      DOWNURRNAME1: 'common_01_cbb_offline'
      UPURRNAME2: 'common_01_cbb_online'
      DOWNURRNAME2: 'common_01_cbb_online'
    add_pccpolicygrp_list:
    - PCCPOLICYGRPNM: common_01_pcc_p_g
      FUPSESSIONEXC: DISABLE
      SIGNALASSOCIATE: ENABLE
      ADCMUTEFLAG: ENABLE
      HTTP2DEGRADESW: INHERIT
      TOKENFUNCFLAG: DISABLE
      URRGROUPNAME: common_01_ch_p
      SIGURRGRPNAME: common_01_ch_p
    add_rule_list:
    - RULENAME: common_any
      POLICYTYPE: PCC
      FLOWFILTERNAME: any_f_f
      PRIORITY: '65000'
      POLICYNAME: common_01_pcc_p_g
      FILTERINGMODE: FLOWFILTER
    add_userprofile_list:
    - USERPROFILENAME: u_p_multi_default
      ALIASMARKFLAG: DISABLE
      DDOSCHECK: DISABLE
      CAPMODETHRES: '0'
      LOCRPTSWITCH: INHERIT
      TETHERINGMAXNUM: '255'
      V6TCPMSSVALUE: '0'
      V4TCPMSSVALUE: '0'
    add_rulebinding_list:
    - USERPROFILENAME: 'u_p_multi_default'
      RULENAME: 'common_any'
      POLICYTYPE: PCC
    set_urrgrpbinding_list:
    - USERPROFILENAME: u_p_multi_default
      DFTURRGRPNAME: common_01_ch_p
      DFTSIGURRGNAME: common_01_ch_p
    set_refreshsrv_list:
    - REFRESHTYPE: ALL
    add_filter_list_1:
    - FILTERNAME: any
      L34PROTTYPE: STRING
      L34PROTOCOL: ANY
      MSSTARTPORT: '0'
      MSENDPORT: '65535'
      SVRSTARTPORT: '0'
      SVRENDPORT: '65535'
    add_filteripv6_list_1:
    - FILTERNAME: any_ipv6
      L34PROTOCOL: ANY
      MSSTARTPORT: '0'
      MSENDPORT: '65535'
      SVRSTARTPORT: '0'
      SVRENDPORT: '65535'
      L34PROTTYPEV6: STRING
    add_flowfilter_list_2:
    - FLOWFILTERNAME: any_f_f
      TETHERDETFLAG: NONE
      FLOWFILTERTYPE: USERCONFIG
    add_fltbindflowf_list_2:
    - FLOWFILTERNAME: any_f_f
      FILTERNAME: any
    add_flowfilter_list_3:
    - FLOWFILTERNAME: any_ipv6_f_f
      TETHERDETFLAG: NONE
      FLOWFILTERTYPE: USERCONFIG
    add_fltbindflowf_list_3:
    - FLOWFILTERNAME: any_ipv6_f_f
      FILTERNAME: any_ipv6
    add_urr_list_2:
    - URRNAME: 'multi_01_cbb_online'
      URRID: 2000000003
      USAGERPTMODE: ONLINE
      ONLMETERINGTYPE: VOLUME
      OFFMETERINGTYPE: VOLUME
      EVENTRSUVALUE: ''
      TIMERSUVALUE: ''
      VOLUMERSUVALUE: ''
      MONITORINGKEY: ''
      N40AGESW: ENABLE
      OFCSRVTMPLNAME: ''
      OFFCOMPOUNDTYPE: ''
      ONLCOMPOUNDTYPE: ''
      REDIRENDTOKEN: ''
    add_urrgroup_list_1:
    - URRGROUPNAME: 'multi_01_ch_p'
      UPURRNAME1: 'multi_01_cbb_offline'
      DOWNURRNAME1: 'multi_01_cbb_offline'
      UPURRNAME2: 'multi_01_cbb_online'
      DOWNURRNAME2: 'multi_01_cbb_online'
    add_pccpolicygrp_list_1:
    - PCCPOLICYGRPNM: multi_01_pcc_p_g
      FUPSESSIONEXC: DISABLE
      SIGNALASSOCIATE: ENABLE
      ADCMUTEFLAG: ENABLE
      HTTP2DEGRADESW: INHERIT
      TOKENFUNCFLAG: DISABLE
      URRGROUPNAME: multi_01_ch_p
      SIGURRGRPNAME: multi_01_ch_p
    add_rule_list_2:
    - RULENAME: multi_01_r
      POLICYTYPE: PCC
      FLOWFILTERNAME: any_f_f
      PRIORITY: '10000'
      POLICYNAME: multi_01_pcc_p_g
      FILTERINGMODE: FLOWFILTER
    add_userprofile_list_1:
    - USERPROFILENAME: u_p_01_multi
      ALIASMARKFLAG: DISABLE
      DDOSCHECK: DISABLE
      CAPMODETHRES: '0'
      LOCRPTSWITCH: INHERIT
      TETHERINGMAXNUM: '255'
      V6TCPMSSVALUE: '0'
      V4TCPMSSVALUE: '0'
    add_rulebinding_list_2:
    - USERPROFILENAME: 'u_p_01_multi'
      RULENAME: 'multi_01_r'
      POLICYTYPE: PCC
    set_urrgrpbinding_list_1:
    - USERPROFILENAME: u_p_01_multi
      DFTURRGRPNAME: multi_01_ch_p
      DFTSIGURRGNAME: multi_01_ch_p
    set_refreshsrv_list_1:
    - REFRESHTYPE: ALL
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 场景一. 园区业务未规划单独费率，使用缺省费率。

#### 1.1 配置L34Filter，如果设备中已经按照运营商规范配置（执行LST FILTER:FILTERNAME="any";以及LST FILTER:FILTERNAME="any\_ipv6";命令查询），无需重复执行。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_filter_list的变量区（command: ADD FILTER） -#}
<!-- MISSING_MACRO: command=ADD FILTER list_name=add_filter_list step_id=1.1 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_filteripv6_list的变量区（command: ADD FILTERIPV6） -#}
<!-- MISSING_MACRO: command=ADD FILTERIPV6 list_name=add_filteripv6_list step_id=1.1 -->
```

#### 1.2 配置Flowfilter并与L34Filter绑定，如果设备中已经按照运营商规范配置（执行LST FLOWFILTER:FLOWFILTERNAME ="any\_f\_f";以及LST FLOWFILTER:FLOWFILTERNAME ="any\_ipv6\_f\_f";命令），无需重复执行。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_flowfilter_list的变量区（command: ADD FLOWFILTER） -#}
<!-- MISSING_MACRO: command=ADD FLOWFILTER list_name=add_flowfilter_list step_id=1.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_fltbindflowf_list的变量区（command: ADD FLTBINDFLOWF） -#}
<!-- MISSING_MACRO: command=ADD FLTBINDFLOWF list_name=add_fltbindflowf_list step_id=1.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_flowfilter_list_1的变量区（command: ADD FLOWFILTER） -#}
<!-- MISSING_MACRO: command=ADD FLOWFILTER list_name=add_flowfilter_list_1 step_id=1.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_fltbindflowf_list_1的变量区（command: ADD FLTBINDFLOWF） -#}
<!-- MISSING_MACRO: command=ADD FLTBINDFLOWF list_name=add_fltbindflowf_list_1 step_id=1.2 -->
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
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：USAGERPTMODE=MONITORINGKEY 时必选 --- -#}
        {%- if item.USAGERPTMODE == 'MONITORINGKEY' -%}
            MONITORINGKEY="{{item.MONITORINGKEY}}",
        {%- endif -%}
        {#- --- 条件必选：USAGERPTMODE=OFFLINE 时必选 --- -#}
        {%- if item.USAGERPTMODE == 'OFFLINE' -%}
            OFFCOMPOUNDTYPE={{item.OFFCOMPOUNDTYPE}},
        {%- endif -%}
        {#- --- 条件必选：USAGERPTMODE=ONLINE 时必选 --- -#}
        {%- if item.USAGERPTMODE == 'ONLINE' -%}
            ONLCOMPOUNDTYPE={{item.ONLCOMPOUNDTYPE}},
        {%- endif -%}
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
        {#- --- 条件可选：ONLMETERINGTYPE=EVENT/EVENT_TIME/EVENT_VOLUME/EVENT_VOLUME_TIME 时可选 --- -#}
        {%- if item.ONLMETERINGTYPE in ['EVENT', 'EVENT_TIME', 'EVENT_VOLUME', 'EVENT_VOLUME_TIME'] -%}
            {%- if item.EVENTRSUVALUE is not none -%}
                EVENTRSUVALUE={{item.EVENTRSUVALUE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：USAGERPTMODE=OFFLINE/ONLINE 时可选 --- -#}
        {%- if item.USAGERPTMODE in ['OFFLINE', 'ONLINE'] -%}
            {%- if item.N40AGESW is not none -%}
                N40AGESW={{item.N40AGESW}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：USAGERPTMODE=OFFLINE 时可选 --- -#}
        {%- if item.USAGERPTMODE == 'OFFLINE' -%}
            {%- if item.OFCSRVTMPLNAME is not none -%}
                OFCSRVTMPLNAME="{{item.OFCSRVTMPLNAME}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：USAGERPTMODE=ONLINE 时可选 --- -#}
        {%- if item.USAGERPTMODE == 'ONLINE' -%}
            {%- if item.REDIRENDTOKEN is not none -%}
                REDIRENDTOKEN="{{item.REDIRENDTOKEN}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ONLMETERINGTYPE=TIME/VOLUME_TIME/EVENT_TIME/EVENT_VOLUME_TIME 时可选 --- -#}
        {%- if item.ONLMETERINGTYPE in ['TIME', 'VOLUME_TIME', 'EVENT_TIME', 'EVENT_VOLUME_TIME'] -%}
            {%- if item.TIMERSUVALUE is not none -%}
                TIMERSUVALUE={{item.TIMERSUVALUE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ONLMETERINGTYPE=VOLUME/VOLUME_TIME/EVENT_VOLUME/EVENT_VOLUME_TIME 时可选 --- -#}
        {%- if item.ONLMETERINGTYPE in ['VOLUME', 'VOLUME_TIME', 'EVENT_VOLUME', 'EVENT_VOLUME_TIME'] -%}
            {%- if item.VOLUMERSUVALUE is not none -%}
                VOLUMERSUVALUE={{item.VOLUMERSUVALUE}},
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
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_pccpolicygrp_list的变量区（command: ADD PCCPOLICYGRP） -#}
<!-- MISSING_MACRO: command=ADD PCCPOLICYGRP list_name=add_pccpolicygrp_list step_id=1.4 -->
```

#### 1.5 配置rule，如果设备中已经按照运营商规范配置，无需重复执行。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_rule_list的变量区（command: ADD RULE） -#}
<!-- MISSING_MACRO: command=ADD RULE list_name=add_rule_list step_id=1.5 -->
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
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_userprofile_list的变量区（command: ADD USERPROFILE） -#}
<!-- MISSING_MACRO: command=ADD USERPROFILE list_name=add_userprofile_list step_id=1.6 -->
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
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_urrgrpbinding_list的变量区（command: SET URRGRPBINDING） -#}
<!-- MISSING_MACRO: command=SET URRGRPBINDING list_name=set_urrgrpbinding_list step_id=1.8 -->
```

#### 【注意】每个userprofile都要增加缺省URR组以及缺省信令URR组，如果都未配置可能会导致无法计费。

#### 1.9 业务生效。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_refreshsrv_list的变量区（command: SET REFRESHSRV） -#}
<!-- MISSING_MACRO: command=SET REFRESHSRV list_name=set_refreshsrv_list step_id=1.9 -->
```

### 2 场景二. 园区业务规划单独费率，以2000000003为例进行配置。

#### 2.1 配置L34Filter，如果设备中已经按照运营商规范配置（执行LST FILTER:FILTERNAME="any";以及LST FILTER:FILTERNAME="any\_ipv6";命令查询），无需重复执行。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_filter_list_1的变量区（command: ADD FILTER） -#}
<!-- MISSING_MACRO: command=ADD FILTER list_name=add_filter_list_1 step_id=2.1 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_filteripv6_list_1的变量区（command: ADD FILTERIPV6） -#}
<!-- MISSING_MACRO: command=ADD FILTERIPV6 list_name=add_filteripv6_list_1 step_id=2.1 -->
```

#### 2.2 配置Flowfilter并与L34Filter绑定，如果设备中已经按照运营商规范配置（执行LST FLOWFILTER:FLOWFILTERNAME ="any\_f\_f";以及LST FLOWFILTER:FLOWFILTERNAME ="any\_ipv6\_f\_f";命令），无需重复执行。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_flowfilter_list_2的变量区（command: ADD FLOWFILTER） -#}
<!-- MISSING_MACRO: command=ADD FLOWFILTER list_name=add_flowfilter_list_2 step_id=2.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_fltbindflowf_list_2的变量区（command: ADD FLTBINDFLOWF） -#}
<!-- MISSING_MACRO: command=ADD FLTBINDFLOWF list_name=add_fltbindflowf_list_2 step_id=2.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_flowfilter_list_3的变量区（command: ADD FLOWFILTER） -#}
<!-- MISSING_MACRO: command=ADD FLOWFILTER list_name=add_flowfilter_list_3 step_id=2.2 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_fltbindflowf_list_3的变量区（command: ADD FLTBINDFLOWF） -#}
<!-- MISSING_MACRO: command=ADD FLTBINDFLOWF list_name=add_fltbindflowf_list_3 step_id=2.2 -->
```

#### 2.3 配置计费策略组。

```jinja2
{%- if is_scenario_separate_rate -%}
    {%- for item in add_urr_list_2 -%}
        ADD URR:
        {#- --- 必选参数 --- -#}
        URRNAME="{{item.URRNAME}}",
        URRID={{item.URRID}},
        USAGERPTMODE={{item.USAGERPTMODE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：USAGERPTMODE=MONITORINGKEY 时必选 --- -#}
        {%- if item.USAGERPTMODE == 'MONITORINGKEY' -%}
            MONITORINGKEY="{{item.MONITORINGKEY}}",
        {%- endif -%}
        {#- --- 条件必选：USAGERPTMODE=OFFLINE 时必选 --- -#}
        {%- if item.USAGERPTMODE == 'OFFLINE' -%}
            OFFCOMPOUNDTYPE={{item.OFFCOMPOUNDTYPE}},
        {%- endif -%}
        {#- --- 条件必选：USAGERPTMODE=ONLINE 时必选 --- -#}
        {%- if item.USAGERPTMODE == 'ONLINE' -%}
            ONLCOMPOUNDTYPE={{item.ONLCOMPOUNDTYPE}},
        {%- endif -%}
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
        {#- --- 条件可选：ONLMETERINGTYPE=EVENT/EVENT_TIME/EVENT_VOLUME/EVENT_VOLUME_TIME 时可选 --- -#}
        {%- if item.ONLMETERINGTYPE in ['EVENT', 'EVENT_TIME', 'EVENT_VOLUME', 'EVENT_VOLUME_TIME'] -%}
            {%- if item.EVENTRSUVALUE is not none -%}
                EVENTRSUVALUE={{item.EVENTRSUVALUE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：USAGERPTMODE=OFFLINE/ONLINE 时可选 --- -#}
        {%- if item.USAGERPTMODE in ['OFFLINE', 'ONLINE'] -%}
            {%- if item.N40AGESW is not none -%}
                N40AGESW={{item.N40AGESW}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：USAGERPTMODE=OFFLINE 时可选 --- -#}
        {%- if item.USAGERPTMODE == 'OFFLINE' -%}
            {%- if item.OFCSRVTMPLNAME is not none -%}
                OFCSRVTMPLNAME="{{item.OFCSRVTMPLNAME}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：USAGERPTMODE=ONLINE 时可选 --- -#}
        {%- if item.USAGERPTMODE == 'ONLINE' -%}
            {%- if item.REDIRENDTOKEN is not none -%}
                REDIRENDTOKEN="{{item.REDIRENDTOKEN}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ONLMETERINGTYPE=TIME/VOLUME_TIME/EVENT_TIME/EVENT_VOLUME_TIME 时可选 --- -#}
        {%- if item.ONLMETERINGTYPE in ['TIME', 'VOLUME_TIME', 'EVENT_TIME', 'EVENT_VOLUME_TIME'] -%}
            {%- if item.TIMERSUVALUE is not none -%}
                TIMERSUVALUE={{item.TIMERSUVALUE}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ONLMETERINGTYPE=VOLUME/VOLUME_TIME/EVENT_VOLUME/EVENT_VOLUME_TIME 时可选 --- -#}
        {%- if item.ONLMETERINGTYPE in ['VOLUME', 'VOLUME_TIME', 'EVENT_VOLUME', 'EVENT_VOLUME_TIME'] -%}
            {%- if item.VOLUMERSUVALUE is not none -%}
                VOLUMERSUVALUE={{item.VOLUMERSUVALUE}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_separate_rate -%}
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
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_pccpolicygrp_list_1的变量区（command: ADD PCCPOLICYGRP） -#}
<!-- MISSING_MACRO: command=ADD PCCPOLICYGRP list_name=add_pccpolicygrp_list_1 step_id=2.4 -->
```

#### 2.5 配置rule。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_rule_list_2的变量区（command: ADD RULE） -#}
<!-- MISSING_MACRO: command=ADD RULE list_name=add_rule_list_2 step_id=2.5 -->
```

#### 如果UPF已有大网的缺省User Profile（u\_p\_xxx\_common），则使用ADD RULE命令配置的园区规则的优先级PRIORITY需要高于u\_p\_xxx\_common下所有规则的优先级，按局点的实际情况规划。

#### 建议在专网PCF上为专用DNN策略配置隔离条件组，对专网会话仅下发专网业务，不下发大网业务，专网UPF独立部署时也不需要配置大网的User Profile。

#### 当以下两个条件都满足时，在专网UPF上参考第6步使用ADD USERPROFILE配置大网的缺省User Profile（u\_p\_xxx\_common）以及园区用户要使用的大网的User Profile （两个user profile可以不绑定任何规则）：

#### -专网PCF上没有配置隔离条件组或者专网PCF为20.11.2之前版本不支持配置隔离条件组功能

#### -专网PCF上大网策略没有将common.dnn通用DNN作为过滤条件

#### 通过上述操作，可以在专网UPF上增加大网相关User Profile，避免业务失败。原因是，当专网SMF使用专用DNN向专网PCF请求策略时，专网PCF会将大网User Profile策略一同下发，包括大网的缺省User Profile以及专网PCF上为园区用户配置了其它的大网User Profile。

#### 2.6 配置User Profile。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_userprofile_list_1的变量区（command: ADD USERPROFILE） -#}
<!-- MISSING_MACRO: command=ADD USERPROFILE list_name=add_userprofile_list_1 step_id=2.6 -->
```

#### 2.7 绑定User Profile。

```jinja2
{%- if is_scenario_separate_rate -%}
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
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_urrgrpbinding_list_1的变量区（command: SET URRGRPBINDING） -#}
<!-- MISSING_MACRO: command=SET URRGRPBINDING list_name=set_urrgrpbinding_list_1 step_id=2.8 -->
```

#### 2.9 业务生效。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_refreshsrv_list_1的变量区（command: SET REFRESHSRV） -#}
<!-- MISSING_MACRO: command=SET REFRESHSRV list_name=set_refreshsrv_list_1 step_id=2.9 -->
```

