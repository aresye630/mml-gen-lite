---
id: ''
name: 开启本地流量详单功能
ne_type: UEG
type: feature
description: 风筝L部署本地流量详单功能，进行用户级流量统计。
tags: []
risk_level: ''
doc_source: ["业务配置","风筝L","UEG 流量统计详单功能（风筝L）","本地流量统计详单功能（风筝L）","开启本地流量详单功能"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
风筝L部署本地流量详单功能，进行用户级流量统计。

## 必备事项
前提条件

请仔细阅读本地流量详单功能概述。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_ucfip_list:
      type: items
      properties:
        INDEX:
          name: '索引号'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: '该参数用于标识记录索引号。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PROTOCOLTYPE:
          name: '协议类型'
          type: string
          enum:
          - TCP
          - SFTP
          - FTP
          - UDP
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPTYPE:
          name: 'IP类型'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: '* 主备UCF IP需规划成不同的IP。 * 该值需从运营商处获取。'
          data_source: '对端协商'
          pattern: ''
          default: ''
        PORTSTART:
          name: '起始端口号'
          type: integer
          minimum: 1025
          maximum: 65534
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PORTEND:
          name: '结束端口号'
          type: integer
          minimum: 1025
          maximum: 65534
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        VPNNAME:
          name: 'VPN名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: '_public_'
        DESC:
          name: '描述'
          type: string
          minLength: 0
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ucfsvrip_list:
      type: items
      properties:
        PROTOCOLTYPE:
          name: '协议类型'
          type: string
          enum:
          - TCP
          - SFTP
          - FTP
          - UDP
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ACCESSNAME:
          name: '接入点名称'
          type: string
          minLength: 0
          maxLength: 32
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        UCFSVRNAME:
          name: 'UCF服务器名称'
          type: string
          minLength: 0
          maxLength: 32
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPTYPE:
          name: 'IP类型'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SVRPORT:
          name: 'UCF服务器端口号'
          type: integer
          minimum: 0
          maximum: 65534
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        USER:
          name: '服务器用户名'
          type: string
          minLength: 0
          maxLength: 64
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PWD:
          name: '服务器密码'
          type: string
          minLength: 1
          maxLength: 432
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        AUTHMODE:
          name: '服务器认证方式'
          type: string
          enum:
          - NOAUTH
          - PUBLICKEY
          required: false
          description: ''
          data_source: '本地规划'
          pattern: ''
          default: ''
        SVRPATH:
          name: '服务器上传路径'
          type: string
          minLength: 0
          maxLength: 512
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_chargectrl_list:
      type: items
      properties:
        HOMECONVERGED:
          name: '归属地融合用户计费控制'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        VISITCONVERGED:
          name: '拜访地融合计费用户计费控制'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ROAMCONVERGED:
          name: '漫游融合计费用户计费控制'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_apnchargectrl_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        CONVERGEDSW:
          name: '融合计费开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        RGAPPLIED:
          name: '业务申请上报模式'
          type: string
          enum:
          - DEFAULT
          - NOCHG
          - OFFLINERGONLY
          - ONLINERGONLY
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_cpurr_list:
      type: items
      properties:
        URRNAME:
          name: '使用量上报规则名称'
          type: string
          maxLength: 31
          required: true
          description: ''
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
          data_source: '本端规划'
          pattern: ''
          default: ''
        RG:
          name: '离线计费组'
          type: integer
          minimum: 0
          maximum: 4294967294
          required: false
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
          data_source: '本地规划'
          pattern: ''
          default: ''
    add_cpurrgroup_list:
      type: items
      properties:
        URRGROUPNAME:
          name: '使用量上报规则组名称'
          type: string
          maxLength: 31
          required: true
          description: ''
          data_source: '本地规划'
          pattern: ''
          default: ''
        UPURRNAME1:
          name: '上行发起URR名称1'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: '本地规划'
          pattern: ''
          default: ''
        DOWNURRNAME1:
          name: '下行发起URR名称1'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: '本地规划'
          pattern: ''
          default: ''
    mod_cppccpolicygrp_list:
      type: items
      properties:
        PCCPOLICYGRPNM:
          name: 'PCC策略组名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        URRGROUPNAME:
          name: '使用量上报规则组名'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_cct_list:
      type: items
      properties:
        CCTMPLTNAME:
          name: '融合计费模板名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PDUVOLUMELIMIT:
          name: 'PDU流量阈值(MB)'
          type: integer
          minimum: 0
          maximum: 2147483647
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 500
        PDUTIMELIMIT:
          name: 'PDU时长阈值(分钟)'
          type: integer
          minimum: 0
          maximum: 1440
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 30
    set_apnchargectrl_list_1:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        CCTEMPLATE:
          name: '融合计费模板'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_edgetrafficstat_list:
      type: items
      properties:
        SWITCH:
          name: '本地流量详单功能功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: '该参数用于设置本地流量统计详单功能开关。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ANONYMIZATION:
          name: '本地流量详单功能匿名化开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '* 该参数在SWITCH配置为ENABLE时为可选参数。 * 开启匿名化可能导致第三方工具解析失败，所以默认设置为关闭。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    mod_ngpeiplcy_list:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - IMSI_PREFIX
          - IMSI
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        GETPEIPLCY:
          name: 'PEI获取策略'
          type: string
          enum:
          - NOGET
          - GETIMEI
          - GETIMEISV
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    mod_s1imeicfg_list:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - IMSI_PREFIX
          - IMSI_RANGE
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        GETIMEIPLC:
          name: 'IMEI获取策略'
          type: string
          enum:
          - IMEI
          - IMEISV
          - NO
          required: false
          description: ''
          data_source: '全网规划'
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
          description: ''
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
          name: '离线计费统计类'
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
    add_urrgroup_list:
      type: items
      properties:
        URRGROUPNAME:
          name: '使用量上报规则组名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: ''
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
    add_pccpolicygrp_list:
      type: items
      properties:
        PCCPOLICYGRPNM:
          name: 'PCC策略组名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        URRGROUPNAME:
          name: 'URR组名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
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
          description: '使用**ADD FILTER**命令定义的过滤器名称。'
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
          description: ''
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
  examples:
    add_ucfip_list:
    - INDEX: 1
      PROTOCOLTYPE: SFTP
      IPTYPE: IPv4
      IPV4: '172.16.10.1'
      PORTSTART: 1025
      PORTEND: 1029
      VPNNAME: 'VRF_N6_Local_2B'
      DESC: 'EDR'
    add_ucfsvrip_list:
    - PROTOCOLTYPE: SFTP
      ACCESSNAME: 'EDRServer'
      UCFSVRNAME: 'EDRFTPClient'
      IPTYPE: IPv4
      IPV4: '172.16.8.48'
      SVRPORT: 21
      USER: 'ftptest'
      PWD: '*****'
      AUTHMODE: NOAUTH
      SVRPATH: '/data/files/csv'
    set_chargectrl_list:
    - HOMECONVERGED: ENABLE
      VISITCONVERGED: ENABLE
      ROAMCONVERGED: ENABLE
    set_apnchargectrl_list:
    - APN: 'apn-test'
      CONVERGEDSW: ENABLE
      RGAPPLIED: OFFLINERGONLY
    add_cpurr_list:
    - URRNAME: 'offlineURR'
      URRID: 1000
      USAGERPTMODE: OFFLINE
      OFFCOMPOUNDTYPE: ONLYRG
      RG: 1300
      OFFMETERINGTYPE: VOLUME_TIME
    add_cpurrgroup_list:
    - URRGROUPNAME: 'urrgroup1'
      UPURRNAME1: 'offlineURR'
      DOWNURRNAME1: 'offlineURR'
    mod_cppccpolicygrp_list:
    - PCCPOLICYGRPNM: 'ppg_global_service'
      URRGROUPNAME: 'urrgroup1'
    add_cct_list:
    - CCTMPLTNAME: 'cct_offline'
      PDUVOLUMELIMIT: 200
      PDUTIMELIMIT: 30
    set_apnchargectrl_list_1:
    - APN: 'apn-test'
      CCTEMPLATE: 'cct_offline'
    set_edgetrafficstat_list:
    - SWITCH: ENABLE
      ANONYMIZATION: DISABLE
    mod_ngpeiplcy_list:
    - SUBRANGE: ALL_USER
      GETPEIPLCY: GETIMEI
    mod_s1imeicfg_list:
    - SUBRANGE: ALL_USER
      GETIMEIPLC: IMEI
    add_urr_list:
    - URRNAME: 'offlineURR'
      URRID: 1000
      USAGERPTMODE: OFFLINE
      OFFMETERINGTYPE: VOLUME_TIME
    add_urrgroup_list:
    - URRGROUPNAME: 'urrgroup1'
      UPURRNAME1: 'offlineURR'
      DOWNURRNAME1: 'offlineURR'
    add_pccpolicygrp_list:
    - PCCPOLICYGRPNM: 'cg-offline'
      URRGROUPNAME: 'urrgroup1'
    add_filter_list:
    - FILTERNAME: 'filter_offline'
      L34PROTTYPE: STRING
      L34PROTOCOL: TCP
      SVRSTARTPORT: 80
      SVRENDPORT: 80
    add_flowfilter_list:
    - FLOWFILTERNAME: 'fg_offline'
    add_fltbindflowf_list:
    - FLOWFILTERNAME: 'fg_offline'
      FILTERNAME: 'filter_offline'
    add_rule_list:
    - RULENAME: 'Rule001'
      POLICYTYPE: PCC
      FILTERINGMODE: FLOWFILTER
      FLOWFILTERNAME: 'fg_offline'
      POLICYNAME: 'cg-offline'
      PRIORITY: 110
    set_refreshsrv_list:
    - REFRESHTYPE: USERPROFILE
    add_userprofile_list:
    - USERPROFILENAME: 'up_test'
    add_rulebinding_list:
    - USERPROFILENAME: 'up_test'
      RULENAME: 'Rule001'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 配置EDR Client端的链路配置

#### 2.1 配置UT-EDR业务本端SFTP Client端IP

```jinja2
{%- for item in add_ucfip_list -%}
    ADD UCFIP:
    {#- --- 必选参数 --- -#}
    INDEX={{item.INDEX}},
    PROTOCOLTYPE={{item.PROTOCOLTYPE}},
    IPTYPE={{item.IPTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.VPNNAME is not none -%}
        VPNNAME="{{item.VPNNAME}}",
    {%- endif -%}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPTYPE=IPv4 时必选 --- -#}
    {%- if item.IPTYPE == 'IPv4' -%}
        IPV4="{{item.IPV4}}",
    {%- endif -%}
    {#- --- 条件必选：PROTOCOLTYPE=TCP/SFTP/UDP 时必选 --- -#}
    {%- if item.PROTOCOLTYPE in ['TCP', 'SFTP', 'UDP'] -%}
        PORTSTART={{item.PORTSTART}},
    {%- endif -%}
    {#- --- 条件必选：PROTOCOLTYPE=TCP/SFTP/UDP 时必选 --- -#}
    {%- if item.PROTOCOLTYPE in ['TCP', 'SFTP', 'UDP'] -%}
        PORTEND={{item.PORTEND}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.2 配置UT-EDR业务对端SFTP Server端IP。

```jinja2
{%- for item in add_ucfsvrip_list -%}
    ADD UCFSVRIP:
    {#- --- 必选参数 --- -#}
    PROTOCOLTYPE={{item.PROTOCOLTYPE}},
    ACCESSNAME="{{item.ACCESSNAME}}",
    UCFSVRNAME="{{item.UCFSVRNAME}}",
    IPTYPE={{item.IPTYPE}},
    SVRPORT={{item.SVRPORT}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPTYPE=IPv4 时必选 --- -#}
    {%- if item.IPTYPE == 'IPv4' -%}
        IPV4="{{item.IPV4}}",
    {%- endif -%}
    {#- --- 条件必选：PROTOCOLTYPE=SFTP/FTP 时必选 --- -#}
    {%- if item.PROTOCOLTYPE in ['SFTP', 'FTP'] -%}
        USER="{{item.USER}}",
    {%- endif -%}
    {#- --- 条件必选：PROTOCOLTYPE=SFTP/FTP 时必选 --- -#}
    {%- if item.PROTOCOLTYPE in ['SFTP', 'FTP'] -%}
        PWD="{{item.PWD}}",
    {%- endif -%}
    {#- --- 条件必选：PROTOCOLTYPE=SFTP/FTP 时必选 --- -#}
    {%- if item.PROTOCOLTYPE in ['SFTP', 'FTP'] -%}
        AUTHMODE={{item.AUTHMODE}},
    {%- endif -%}
    {#- --- 条件必选：PROTOCOLTYPE=SFTP/FTP 时必选 --- -#}
    {%- if item.PROTOCOLTYPE in ['SFTP', 'FTP'] -%}
        SVRPATH="{{item.SVRPATH}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 SMF网元配置

#### 3.1 使能流量统计

```jinja2
{%- for item in set_chargectrl_list -%}
    SET CHARGECTRL:
    {#- --- 可选参数 --- -#}
    {%- if item.HOMECONVERGED is not none -%}
        HOMECONVERGED={{item.HOMECONVERGED}},
    {%- endif -%}
    {%- if item.VISITCONVERGED is not none -%}
        VISITCONVERGED={{item.VISITCONVERGED}},
    {%- endif -%}
    {%- if item.ROAMCONVERGED is not none -%}
        ROAMCONVERGED={{item.ROAMCONVERGED}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 3.2 基于APN配置使能流量详单功能控制配置

```jinja2
{%- for item in set_apnchargectrl_list -%}
    SET APNCHARGECTRL:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.CONVERGEDSW is not none -%}
        CONVERGEDSW={{item.CONVERGEDSW}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：CONVERGEDSW=ENABLE 时可选 --- -#}
    {%- if item.CONVERGEDSW == 'ENABLE' -%}
        {%- if item.RGAPPLIED is not none -%}
            RGAPPLIED={{item.RGAPPLIED}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 3.3 配置URR

```jinja2
{%- for item in add_cpurr_list -%}
    ADD CPURR:
    {#- --- 必选参数 --- -#}
    URRNAME="{{item.URRNAME}}",
    URRID={{item.URRID}},
    USAGERPTMODE={{item.USAGERPTMODE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：USAGERPTMODE=OFFLINE 时必选 --- -#}
    {%- if item.USAGERPTMODE == 'OFFLINE' -%}
        OFFCOMPOUNDTYPE={{item.OFFCOMPOUNDTYPE}},
    {%- endif -%}
    {#- --- 条件必选：OFFCOMPOUNDTYPE=ONLYRG/RGSID 时必选 --- -#}
    {%- if item.OFFCOMPOUNDTYPE in ['ONLYRG', 'RGSID'] -%}
        RG={{item.RG}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：USAGERPTMODE=OFFLINE 时可选 --- -#}
    {%- if item.USAGERPTMODE == 'OFFLINE' -%}
        {%- if item.OFFMETERINGTYPE is not none -%}
            OFFMETERINGTYPE={{item.OFFMETERINGTYPE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_cpurrgroup_list -%}
    ADD CPURRGROUP:
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

#### 3.4 绑定URR和PCCPOLICYGroup

```jinja2
{%- for item in mod_cppccpolicygrp_list -%}
    MOD CPPCCPOLICYGRP:
    {#- --- 必选参数 --- -#}
    PCCPOLICYGRPNM="{{item.PCCPOLICYGRPNM}}",
    {#- --- 可选参数 --- -#}
    {%- if item.URRGROUPNAME is not none -%}
        URRGROUPNAME="{{item.URRGROUPNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 3.5 配置模板

```jinja2
{%- for item in add_cct_list -%}
    ADD CCT:
    {#- --- 必选参数 --- -#}
    CCTMPLTNAME="{{item.CCTMPLTNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.PDUVOLUMELIMIT is not none -%}
        PDUVOLUMELIMIT={{item.PDUVOLUMELIMIT}},
    {%- endif -%}
    {%- if item.PDUTIMELIMIT is not none -%}
        PDUTIMELIMIT={{item.PDUTIMELIMIT}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 3.6 绑定模板到指定APN下

```jinja2
{%- for item in set_apnchargectrl_list_1 -%}
    SET APNCHARGECTRL:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.CCTEMPLATE is not none -%}
        CCTEMPLATE="{{item.CCTEMPLATE}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 3.7 使能流量统计

```jinja2
{%- for item in set_edgetrafficstat_list -%}
    SET EDGETRAFFICSTAT:
    {#- --- 必选参数 --- -#}
    SWITCH={{item.SWITCH}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：SWITCH=ENABLE 时可选 --- -#}
    {%- if item.SWITCH == 'ENABLE' -%}
        {%- if item.ANONYMIZATION is not none -%}
            ANONYMIZATION={{item.ANONYMIZATION}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 3.8 使能注册流程网络侧主动获取设备标识。

```jinja2
{%- if is_optional_device_id_fetch -%}
    {%- for item in mod_ngpeiplcy_list -%}
        MOD NGPEIPLCY:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        {#- --- 可选参数 --- -#}
        {%- if item.GETPEIPLCY is not none -%}
            GETPEIPLCY={{item.GETPEIPLCY}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_optional_device_id_fetch -%}
    {%- for item in mod_s1imeicfg_list -%}
        MOD S1IMEICFG:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        {#- --- 可选参数 --- -#}
        {%- if item.GETIMEIPLC is not none -%}
            GETIMEIPLC={{item.GETIMEIPLC}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 4 **UPF****网元部件配置**

#### 4.1 配置URR

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
    ;
{%- endfor -%}
```

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

#### 4.2 配置三四层信息

```jinja2
{%- for item in add_filter_list -%}
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
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_flowfilter_list -%}
    ADD FLOWFILTER:
    {#- --- 必选参数 --- -#}
    FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_fltbindflowf_list -%}
    ADD FLTBINDFLOWF:
    {#- --- 必选参数 --- -#}
    FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
    FILTERNAME="{{item.FILTERNAME}}",
    ;
{%- endfor -%}
```

#### 4.3 配置流量统计规则

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
    ;
{%- endfor -%}
```

```jinja2
{%- for item in set_refreshsrv_list -%}
    SET REFRESHSRV:
    {#- --- 必选参数 --- -#}
    REFRESHTYPE={{item.REFRESHTYPE}},
    ;
{%- endfor -%}
```

#### 4.4 配置规则绑定用户模板

```jinja2
{%- for item in add_userprofile_list -%}
    ADD USERPROFILE:
    {#- --- 必选参数 --- -#}
    USERPROFILENAME="{{item.USERPROFILENAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_rulebinding_list -%}
    ADD RULEBINDING:
    {#- --- 必选参数 --- -#}
    USERPROFILENAME="{{item.USERPROFILENAME}}",
    RULENAME="{{item.RULENAME}}",
    ;
{%- endfor -%}
```

