---
id: ''
name: 激活HTTPS头增强
ne_type: UDG
type: feature
description: 当需要将用户信息（如APN、IMEI等）中的一个或多个信息添加到HTTPS报文头并传递给Web Server时，需要完成HTTPS报文头的内容增强处理。  适用于PGW-U、UPF。
risk_level: ''
doc_source: ["特性部署","业务专题","UDG头增强功能专题","HTTPS头增强功能","激活HTTPS头增强"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当需要将用户信息（如APN、IMEI等）中的一个或多个信息添加到HTTPS报文头并传递给Web Server时，需要完成HTTPS报文头的内容增强处理。适用于PGW-U、UPF。

## 必备事项
前提条件

* 请仔细阅读HTTPS头增强原理描述。
* 操作员已经获取到运营商对使用HTTPS头增强特性的插入字段、字段前缀名称以及需要HTTPS头增强信息的Web Server的IP地址、SNI等信息。
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
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SWITCH:
          name: '开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: true
          description: '-'
          data_source: '本端规划'
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
    add_filter_list:
      type: items
      properties:
        FILTERNAME:
          name: '过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '不同过滤器之间，该参数不能重复。'
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
          description: '-'
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
          description: '-'
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
          description: '支持基于IP、主机名和IP地址列表三种方式，此处以IP为例。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SVRIP:
          name: '服务器IP地址'
          type: string
          maxLength: 15
          required: false
          description: 'Web Server的IP地址。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        SVRIPMASKTYPE:
          name: '服务器IP地址掩码类型'
          type: string
          enum:
          - IPTYPE
          - LENGTHTYPE
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SVRIPMASK:
          name: '服务器IP地址反掩码'
          type: string
          maxLength: 15
          required: false
          description: 'Web Server的IP地址掩码反码。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        SVRSTARTPORT:
          name: '服务器起始端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: 'Web Server接收HTTPS报文的端口号。'
          data_source: '与对端协商'
          pattern: ''
          default: 0
        SVRENDPORT:
          name: '服务器结束端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: '与对端协商'
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
          description: '系统自动在60s后将配置的L7Filter置为生效。如果需要将新配置的L7Filter立即生效，可执行本此命令。'
          data_source: '本端规划'
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
          description: '不同的七层过滤器，其名称不能相同。  仅采用基于HTTPS协议时，不需要规划该数据。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SUBL7FLTNAME:
          name: '子七层过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '同一个七层过滤器包含的多个子七层过滤器名称不能相同。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        URL:
          name: 'URL'
          type: string
          minLength: 0
          maxLength: 119
          required: false
          description: '触发HTTPS头增强的SNI，根据Web Server规划。  仅采用基于HTTPS协议时，不需要规划该参数。'
          data_source: '与对端协商'
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
    add_protbindflowf_list:
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
        PROTOCOLNAME:
          name: '协议名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '使用样例值。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        L7FILTERNAME:
          name: '七层过滤器名字'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: '使用**ADD L7FILTER**命令定义的七层过滤器名称。  采用基于SNI时，需要规划；仅采用基于HTTPS协议时，不需要规划该参数。'
          data_source: '已配置数据中获取'
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
          description: '系统自动在60s后将配置的L7Filter置为生效。如果需要将新配置的L7Filter立即生效，可执行本此命令。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_protbindflowf_list_1:
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
        PROTOCOLNAME:
          name: '协议名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '使用样例值。'
          data_source: '本端规划'
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
          description: '系统自动在60s后将配置的L7Filter置为生效。如果需要将新配置的L7Filter立即生效，可执行本此命令。'
          data_source: '本端规划'
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
          description: '存在多条数据时，该参数不能相同。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PROTOCOLNAME:
          name: '协议名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '-'
          data_source: '固定取值'
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
          description: '根据Web Server的端口情况进行规划。  优先级取值越小，优先级越高。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        STARTPORT:
          name: '起始端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 1
          maximum: 65535
          required: true
          description: ''
          data_source: '与对端协商'
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
          description: '如无特殊需求，使用样例值即可。'
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
          description: '如无特殊需求，使用样例值即可。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_tlsheaden_list:
      type: items
      properties:
        HEADERENNAME:
          name: '头增强名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DATATYPE:
          name: '数据类型'
          type: string
          enum:
          - APN
          - BILLINGTYPE
          - CHGCHAR1
          - CHGCHAR2
          - CHGCHAR3
          - CHGID
          - GGSNIP1
          - GGSNIP2
          - GGSNIP3
          - IMEI1
          - IMEI2
          - IMEI3
          - IMSI1
          - IMSI2
          - IMSI3
          - MCC
          - MNC
          - MSIP1
          - MSIP2
          - MSIP3
          - MSISDN1
          - MSISDN2
          - MSISDN3
          - RANDNUM
          - RAT1
          - RAT2
          - RAT3
          - ROAMING1
          - ROAMING2
          - ROAMING3
          - SESSIONID
          - SGSNIP1
          - SGSNIP2
          - SGSNIP3
          - SGSN_MCC_MNC1
          - SGSN_MCC_MNC2
          - SGSN_MCC_MNC3
          - SUBPROFILE1
          - SUBPROFILE2
          - SUBPROFILE3
          - TIMESTAMP1
          - TIMESTAMP2
          - TIMESTAMP3
          - ULI1
          - ULI2
          - ULI3
          - UPIPV4
          - UPIPV6
          - USERDEF1
          - USERDEF2
          - USERDEF3
          - USERDEF4
          - USERPROFALIAS
          - ZONEID
          required: true
          description: '根据Web Server业务需求规划。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TLSTYPEVAL:
          name: 'TLS报文头域的TLS Type值'
          type: integer
          minimum: 0
          maximum: 65534
          required: false
          description: '说明：  * 开启HTTPS头增强功能必须配置“TLSTYPEVAL”参数。 * 当插入多个字段时，为方便观察插入的头增强字段，建议不同字段配置不同的“TLSTYPEVAL”参数值。具体值根据Web Server能力规划。 * 如果将多个字段插入在同一个头增强动作中，且“TLSTYPEVAL”相同时，则需要配置“SUBTLSTYPEVAL”参数值。具体值根据Web Server能力规划。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SUBTLSTYPEVAL:
          name: 'TLS报文头域的Sub TLS Type值'
          type: integer
          minimum: 0
          maximum: 254
          required: false
          description: '根据Web Server能力规划。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        ENCRYALGORI:
          name: '加密算法标识'
          type: string
          enum:
          - AES128
          - AES128_CTR
          - AES128_GCM
          - AES256
          - AES256_CTR
          - AES256_GCM
          - MD5
          - NONE
          - RC4
          - SHA256
          required: false
          description: '根据Web Server能力规划。建议使用安全的加密算法。'
          data_source: '与对端协商'
          pattern: ''
          default: AES128_GCM
        ANTIFRAUD:
          name: '防欺诈标识'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        CCFORMAT:
          name: 'Charge Characteristic格式'
          type: string
          enum:
          - DECIMAL
          - HEX
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DECIMAL
        ERRFGSUBTLSTP:
          name: 'HomeZone功能TLS报文头域的Sub Type值'
          type: integer
          minimum: 0
          maximum: 254
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ERRFLGTLSTP:
          name: 'HomeZone功能TLS报文头域的TLS Type值'
          type: integer
          minimum: 0
          maximum: 65534
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GRAYLIST:
          name: '灰名单'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        HEADERFLDLEN:
          name: '头域长度'
          type: integer
          minimum: 31
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMEITYPE:
          name: 'IMEI类型'
          type: string
          enum:
          - IMEI
          - TAC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: IMEI
        REMOVEDMCC:
          name: '需去除的移动国家码'
          type: string
          minLength: 0
          maxLength: 4
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TSPRECISION:
          name: '时间精度'
          type: string
          enum:
          - MILLISECOND
          - SECOND
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USERDEFINEVAL:
          name: '用户自定义值'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CIPHERTXTENCODE:
          name: '头增强密文编码方式'
          type: string
          enum:
          - ASCII
          - BASE64
          - INHERIT
          - NONE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: INHERIT
        PSWDKEY:
          name: '密钥'
          type: string
          minLength: 1
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PSWDKEYCONFIRM:
          name: '确认密钥'
          type: string
          minLength: 1
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RC4KEYMD5EN:
          name: 'RC4的密钥MD5 Hash使能标识'
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
        SALTSW:
          name: '是否添加盐值'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ENABLE
    add_urr_list:
      type: items
      properties:
        URRNAME:
          name: '使用量上报规则名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '-'
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
          description: '已在该配置任务中通过命令**ADD URR**配置。'
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
          description: '存在多条数据时，该参数不能相同。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        URRGROUPNAME:
          name: 'URR组名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: 'PCC策略组绑定的URR组，已通过**ADD URRGROUP**命令配置完成。'
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
          description: '存在多条数据时，该参数+策略类型不能完全相同。'
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
        POLICYNAME:
          name: '策略名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: '使用**ADD TLSHEADEN**命令定义的头增强名称。'
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
    add_rule_list_1:
      type: items
      properties:
        RULENAME:
          name: '规则名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '存在多条数据时，该参数+策略类型不能完全相同。'
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
          description: 'UserProfile绑定的业务规则，已通过**ADD RULE**命令配置完成。  与SMF上配置的规则名称保持一致。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3G5HTSE01'
      SWITCH: ENABLE
    add_flowfilter_list:
    - FLOWFILTERNAME: 'flowfilter_test'
    add_filter_list:
    - FILTERNAME: 'filter_test1'
      L34PROTTYPE: STRING
      L34PROTOCOL: TCP
      SVRIPMODE: IP
      SVRIP: '10.10.10.10'
      SVRIPMASKTYPE: IPTYPE
      SVRIPMASK: '0.0.0.0'
      SVRSTARTPORT: 443
      SVRENDPORT: 443
      L34PROTNUM: ''
      SVRIPMASKLEN: ''
      DOMAINVALUE: ''
      HOSTNAME: ''
      HOSTPRIORITY: ''
      SVRIPLISTNAME: ''
    add_fltbindflowf_list:
    - FLOWFILTERNAME: 'flowfilter_test'
      FILTERNAME: 'filter_test1'
    set_refreshsrv_list:
    - REFRESHTYPE: ALL
    add_l7filter_list:
    - L7FILTERNAME: 'l7filter_test'
      SUBL7FLTNAME: 'sl7_test_1'
      URL: 'www.huawei.com/*'
      URLTYPE: URL
    add_protbindflowf_list:
    - FLOWFILTERNAME: 'flowfilter_test'
      PROTOCOLNAME: 'https'
      L7FILTERNAME: 'l7filter_test'
    set_refreshsrv_list_1:
    - REFRESHTYPE: ALL
    add_protbindflowf_list_1:
    - FLOWFILTERNAME: 'flowfilter_test'
      PROTOCOLNAME: 'https'
    set_refreshsrv_list_2:
    - REFRESHTYPE: ALL
    add_wellknownport_list:
    - IDENPROTNAME: 'https_443'
      PROTOCOLNAME: 'https'
      PORTOP: EQUAL
      STARTPORT: 443
      PRIORITY: 10
      ENDPORT: ''
    lod_signaturedb_list:
    - LOADMODE: LATEST
      VERSION: ''
    lod_parserdb_list:
    - LOADMODE: LATEST
    add_tlsheaden_list:
    - HEADERENNAME: 'header_test'
      DATATYPE: APN
      TLSTYPEVAL: 1000
      SUBTLSTYPEVAL: 10
      ENCRYALGORI: NONE
      ANTIFRAUD: DISABLE
      CCFORMAT: DECIMAL
      ERRFGSUBTLSTP: ''
      ERRFLGTLSTP: ''
      GRAYLIST: DISABLE
      HEADERFLDLEN: ''
      IMEITYPE: IMEI
      REMOVEDMCC: ''
      TSPRECISION: ''
      USERDEFINEVAL: ''
      CIPHERTXTENCODE: INHERIT
      PSWDKEY: ''
      PSWDKEYCONFIRM: ''
      RC4KEYMD5EN: INHERIT
      SALTSW: ENABLE
    add_urr_list:
    - URRNAME: 'urr01'
      URRID: 1000
      USAGERPTMODE: OFFLINE
      DFTQUOTAPARA: Byte
      DFTQUOTATIME: ''
      DFTQUOTAVOLUME: ''
      OFFMETERINGTYPE: VOLUME
      ONLMETERINGTYPE: VOLUME
      RG: ''
      SID: ''
    add_urrgroup_list:
    - URRGROUPNAME: 'cp_test'
      UPURRNAME1: 'urr01'
      DOWNURRNAME1: 'urr01'
    add_pccpolicygrp_list:
    - PCCPOLICYGRPNM: 'pg_test'
      URRGROUPNAME: 'cp_test'
    add_rule_list:
    - RULENAME: 'rule_test1'
      POLICYTYPE: HEADEN
      FILTERINGMODE: FLOWFILTER
      FLOWFILTERNAME: 'flowfilter_test'
      POLICYNAME: 'header_test'
      FLWFLTRGRPNAME: ''
      ADCMUTEFLAG: ENABLE
      ALGSWITCH: DISABLE
      RDSTRIGGERFLAG: DISABLE
      REDIRIPVERFLAG: ''
      REMARKFPISEL: REMARK
      SRVLBOFLAG: DISABLE
      WORKERNAME: ''
      WORKERPARA: ''
    add_rule_list_1:
    - RULENAME: 'rule_test2'
      POLICYTYPE: PCC
      FILTERINGMODE: FLOWFILTER
      FLOWFILTERNAME: 'flowfilter_test'
      PRIORITY: 20
      POLICYNAME: 'pg_test'
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
    - USERPROFILENAME: 'up_test'
    add_rulebinding_list:
    - USERPROFILENAME: 'up_test'
      RULENAME: 'rule_test1'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 //打开本特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 2 //配置流过滤器。

```jinja2
{%- for item in add_flowfilter_list -%}
    ADD FLOWFILTER:
    {#- --- 必选参数 --- -#}
    FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
    ;
{%- endfor -%}
```

### 3 //配置基于特定IP地址触发HTTPS头增强，使用的三四层过滤条件。使用UE IP地址、Web Server IP地址、三四层协议类型、手机端口号或服务器端口号作为过滤条件。仅采用七层过滤条件时请跳过该脚本。

```jinja2
{%- if is_scenario_l34_ip -%}
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
        {#- --- 条件必选：SVRIPMASKTYPE=IPTYPE 时必选 --- -#}
        {%- if item.SVRIPMASKTYPE == 'IPTYPE' -%}
            SVRIPMASK="{{item.SVRIPMASK}}",
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
        {#- --- 条件必选：SVRIPMASKTYPE=LENGTHTYPE 时必选 --- -#}
        {%- if item.SVRIPMASKTYPE == 'LENGTHTYPE' -%}
            SVRIPMASKLEN={{item.SVRIPMASKLEN}},
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
{%- endif -%}
```

```jinja2
{%- if is_scenario_l34_ip -%}
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
{%- if is_scenario_l34_ip -%}
    {%- for item in set_refreshsrv_list -%}
        SET REFRESHSRV:
        {#- --- 必选参数 --- -#}
        REFRESHTYPE={{item.REFRESHTYPE}},
        ;
    {%- endfor -%}
{%- endif -%}
```

### 4 //配置基于特定SNI和HTTPS协议触发HTTPS头增强，使用七层过滤条件。可配置知名端口+特征库方式识别，也可仅使用特征库识别。仅采用三四层过滤条件时请跳过该脚本。

#### 4.1 //配置HTTPS头增强的七层过滤条件（SNI）。仅采用三四层过滤条件时请跳过该脚本。仅采用七层过滤条件（HTTPS协议）过滤时请跳过该脚本。

```jinja2
{%- if is_scenario_l7 and is_scenario_l7_sni -%}
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

```jinja2
{%- if is_scenario_l7 and is_scenario_l7_sni -%}
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

```jinja2
{%- if is_scenario_l7 and is_scenario_l7_sni -%}
    {%- for item in set_refreshsrv_list_1 -%}
        SET REFRESHSRV:
        {#- --- 必选参数 --- -#}
        REFRESHTYPE={{item.REFRESHTYPE}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.2 //配置HTTPS头增强的七层过滤条件（HTTPS协议）。仅采用三四层过滤条件时请跳过该脚本。采用七层过滤条件（SNI）过滤时请跳过该脚本。

```jinja2
{%- if is_scenario_l7 and is_scenario_l7_https -%}
    {%- for item in add_protbindflowf_list_1 -%}
        ADD PROTBINDFLOWF:
        {#- --- 必选参数 --- -#}
        FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
        PROTOCOLNAME="{{item.PROTOCOLNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_l7 and is_scenario_l7_https -%}
    {%- for item in set_refreshsrv_list_2 -%}
        SET REFRESHSRV:
        {#- --- 必选参数 --- -#}
        REFRESHTYPE={{item.REFRESHTYPE}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.3 //配置知名端口识别HTTPS协议。同时配置知名端口识别协议和特征库识别协议时，UDG通过知名端口识别协议成功后，再通过特征库识别协议。不配置知名端口识别协议时，直接通过特征库识别协议。

```jinja2
{%- if is_scenario_l7 -%}
    {%- for item in add_wellknownport_list -%}
        ADD WELLKNOWNPORT:
        {#- --- 必选参数 --- -#}
        IDENPROTNAME="{{item.IDENPROTNAME}}",
        PROTOCOLNAME="{{item.PROTOCOLNAME}}",
        PORTOP={{item.PORTOP}},
        PRIORITY={{item.PRIORITY}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：PORTOP=EQUAL/GT/RANGE 时必选 --- -#}
        {%- if item.PORTOP in ['EQUAL', 'GT', 'RANGE'] -%}
            STARTPORT={{item.STARTPORT}},
        {%- endif -%}
        {#- --- 条件必选：PORTOP=LT/RANGE 时必选 --- -#}
        {%- if item.PORTOP in ['LT', 'RANGE'] -%}
            ENDPORT={{item.ENDPORT}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.4 //配置报文特征库识别协议。推荐采用特征库识别协议。

```jinja2
{%- if is_scenario_l7 -%}
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
{%- endif -%}
```

```jinja2
{%- if is_scenario_l7 -%}
    {%- for item in lod_parserdb_list -%}
        LOD PARSERDB:
        {#- --- 必选参数 --- -#}
        LOADMODE={{item.LOADMODE}},
        ;
    {%- endfor -%}
{%- endif -%}
```

### 5 //配置HTTPS头增强动作属性。头增强字段为APN、IMSI1、MSIP1、MSISDN1。

```jinja2
{%- for item in add_tlsheaden_list -%}
    ADD TLSHEADEN:
    {#- --- 必选参数 --- -#}
    HEADERENNAME="{{item.HEADERENNAME}}",
    DATATYPE={{item.DATATYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：DATATYPE=USERDEF1/USERDEF2/USERDEF3/USERDEF4/APN/BILLINGTYPE/CHGCHAR1/CHGCHAR2/CHGCHAR3/CHGID/GGSNIP1/GGSNIP2/GGSNIP3/IMEI1/IMEI2/IMEI3/IMSI1/IMSI2/IMSI3/MCC/MNC/MSIP1/MSISDN1/MSISDN2/MSISDN3/RAT1/RAT2/RAT3/ROAMING1/ROAMING2/ROAMING3/SESSIONID/SGSNIP1/SGSNIP2/SGSNIP3/SGSN_MCC_MNC1/SGSN_MCC_MNC2/SGSN_MCC_MNC3/SUBPROFILE1/SUBPROFILE2/SUBPROFILE3/ULI1/ULI2/ULI3/USERPROFALIAS/ZONEID/TIMESTAMP1/TIMESTAMP2/TIMESTAMP3/MSIP2/MSIP3/UPIPV4/UPIPV6/RANDNUM 时必选 --- -#}
    {%- if item.DATATYPE in ['USERDEF1', 'USERDEF2', 'USERDEF3', 'USERDEF4', 'APN', 'BILLINGTYPE', 'CHGCHAR1', 'CHGCHAR2', 'CHGCHAR3', 'CHGID', 'GGSNIP1', 'GGSNIP2', 'GGSNIP3', 'IMEI1', 'IMEI2', 'IMEI3', 'IMSI1', 'IMSI2', 'IMSI3', 'MCC', 'MNC', 'MSIP1', 'MSISDN1', 'MSISDN2', 'MSISDN3', 'RAT1', 'RAT2', 'RAT3', 'ROAMING1', 'ROAMING2', 'ROAMING3', 'SESSIONID', 'SGSNIP1', 'SGSNIP2', 'SGSNIP3', 'SGSN_MCC_MNC1', 'SGSN_MCC_MNC2', 'SGSN_MCC_MNC3', 'SUBPROFILE1', 'SUBPROFILE2', 'SUBPROFILE3', 'ULI1', 'ULI2', 'ULI3', 'USERPROFALIAS', 'ZONEID', 'TIMESTAMP1', 'TIMESTAMP2', 'TIMESTAMP3', 'MSIP2', 'MSIP3', 'UPIPV4', 'UPIPV6', 'RANDNUM'] -%}
        TLSTYPEVAL={{item.TLSTYPEVAL}},
    {%- endif -%}
    {#- --- 条件必选：ENCRYALGORI=MD5/RC4/AES128/AES256/SHA256/AES128_CTR/AES128_GCM/AES256_CTR/AES256_GCM 时必选 --- -#}
    {%- if item.ENCRYALGORI in ['MD5', 'RC4', 'AES128', 'AES256', 'SHA256', 'AES128_CTR', 'AES128_GCM', 'AES256_CTR', 'AES256_GCM'] -%}
        PSWDKEY="{{item.PSWDKEY}}",
    {%- endif -%}
    {#- --- 条件必选：ENCRYALGORI=MD5/RC4/AES128/AES256/SHA256/AES128_CTR/AES128_GCM/AES256_CTR/AES256_GCM 时必选 --- -#}
    {%- if item.ENCRYALGORI in ['MD5', 'RC4', 'AES128', 'AES256', 'SHA256', 'AES128_CTR', 'AES128_GCM', 'AES256_CTR', 'AES256_GCM'] -%}
        PSWDKEYCONFIRM="{{item.PSWDKEYCONFIRM}}",
    {%- endif -%}
    {#- --- 条件必选：DATATYPE=USERDEF1/USERDEF2/USERDEF3/USERDEF4 时必选 --- -#}
    {%- if item.DATATYPE in ['USERDEF1', 'USERDEF2', 'USERDEF3', 'USERDEF4'] -%}
        USERDEFINEVAL="{{item.USERDEFINEVAL}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：DATATYPE=MSISDN1/MSISDN2/MSISDN3/IMSI1/IMSI2/IMSI3/IMEI1/IMEI2/IMEI3/SGSNIP1/SGSNIP2/SGSNIP3/SUBPROFILE1/SUBPROFILE2/SUBPROFILE3/CHGCHAR1/CHGCHAR2/CHGCHAR3/MSIP1/APN/ZONEID/BILLINGTYPE/RAT1/RAT2/RAT3/ULI1/ULI2/ULI3/CHGID/ROAMING1/ROAMING2/ROAMING3/SGSN_MCC_MNC1/SGSN_MCC_MNC2/SGSN_MCC_MNC3/USERDEF1/USERDEF2/USERDEF3/USERDEF4/USERPROFALIAS/MCC/MNC/SESSIONID/GGSNIP1/GGSNIP2/GGSNIP3/TIMESTAMP1/TIMESTAMP2/TIMESTAMP3/MSIP2/MSIP3/UPIPV4/UPIPV6/RANDNUM 时可选 --- -#}
    {%- if item.DATATYPE in ['MSISDN1', 'MSISDN2', 'MSISDN3', 'IMSI1', 'IMSI2', 'IMSI3', 'IMEI1', 'IMEI2', 'IMEI3', 'SGSNIP1', 'SGSNIP2', 'SGSNIP3', 'SUBPROFILE1', 'SUBPROFILE2', 'SUBPROFILE3', 'CHGCHAR1', 'CHGCHAR2', 'CHGCHAR3', 'MSIP1', 'APN', 'ZONEID', 'BILLINGTYPE', 'RAT1', 'RAT2', 'RAT3', 'ULI1', 'ULI2', 'ULI3', 'CHGID', 'ROAMING1', 'ROAMING2', 'ROAMING3', 'SGSN_MCC_MNC1', 'SGSN_MCC_MNC2', 'SGSN_MCC_MNC3', 'USERDEF1', 'USERDEF2', 'USERDEF3', 'USERDEF4', 'USERPROFALIAS', 'MCC', 'MNC', 'SESSIONID', 'GGSNIP1', 'GGSNIP2', 'GGSNIP3', 'TIMESTAMP1', 'TIMESTAMP2', 'TIMESTAMP3', 'MSIP2', 'MSIP3', 'UPIPV4', 'UPIPV6', 'RANDNUM'] -%}
        {%- if item.SUBTLSTYPEVAL is not none -%}
            SUBTLSTYPEVAL={{item.SUBTLSTYPEVAL}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：DATATYPE=MSISDN1/MSISDN2/MSISDN3/IMSI1/IMSI2/IMSI3/IMEI1/IMEI2/IMEI3/SGSNIP1/SGSNIP2/SGSNIP3/SUBPROFILE1/SUBPROFILE2/SUBPROFILE3/CHGCHAR1/CHGCHAR2/CHGCHAR3/MSIP1/APN/RAT1/RAT2/RAT3/ULI1/ULI2/ULI3/ROAMING1/ROAMING2/ROAMING3/SGSN_MCC_MNC1/SGSN_MCC_MNC2/SGSN_MCC_MNC3/GGSNIP1/GGSNIP2/GGSNIP3/TIMESTAMP1/TIMESTAMP2/TIMESTAMP3/MSIP2/MSIP3/UPIPV4/UPIPV6 时可选 --- -#}
    {%- if item.DATATYPE in ['MSISDN1', 'MSISDN2', 'MSISDN3', 'IMSI1', 'IMSI2', 'IMSI3', 'IMEI1', 'IMEI2', 'IMEI3', 'SGSNIP1', 'SGSNIP2', 'SGSNIP3', 'SUBPROFILE1', 'SUBPROFILE2', 'SUBPROFILE3', 'CHGCHAR1', 'CHGCHAR2', 'CHGCHAR3', 'MSIP1', 'APN', 'RAT1', 'RAT2', 'RAT3', 'ULI1', 'ULI2', 'ULI3', 'ROAMING1', 'ROAMING2', 'ROAMING3', 'SGSN_MCC_MNC1', 'SGSN_MCC_MNC2', 'SGSN_MCC_MNC3', 'GGSNIP1', 'GGSNIP2', 'GGSNIP3', 'TIMESTAMP1', 'TIMESTAMP2', 'TIMESTAMP3', 'MSIP2', 'MSIP3', 'UPIPV4', 'UPIPV6'] -%}
        {%- if item.ENCRYALGORI is not none -%}
            ENCRYALGORI={{item.ENCRYALGORI}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：DATATYPE=MSISDN1/MSISDN2/MSISDN3/IMSI1/IMSI2/IMSI3/IMEI1/IMEI2/IMEI3/SGSNIP1/SGSNIP2/SGSNIP3/SUBPROFILE1/SUBPROFILE2/SUBPROFILE3/CHGCHAR1/CHGCHAR2/CHGCHAR3/MSIP1/APN/ZONEID/BILLINGTYPE/RAT1/RAT2/RAT3/ULI1/ULI2/ULI3/CHGID/ROAMING1/ROAMING2/ROAMING3/SGSN_MCC_MNC1/SGSN_MCC_MNC2/SGSN_MCC_MNC3/USERDEF1/USERDEF2/USERDEF3/USERDEF4/USERPROFALIAS/MCC/MNC/SESSIONID/GGSNIP1/GGSNIP2/GGSNIP3/TIMESTAMP1/TIMESTAMP2/TIMESTAMP3/MSIP2/MSIP3/UPIPV4/UPIPV6/RANDNUM 时可选 --- -#}
    {%- if item.DATATYPE in ['MSISDN1', 'MSISDN2', 'MSISDN3', 'IMSI1', 'IMSI2', 'IMSI3', 'IMEI1', 'IMEI2', 'IMEI3', 'SGSNIP1', 'SGSNIP2', 'SGSNIP3', 'SUBPROFILE1', 'SUBPROFILE2', 'SUBPROFILE3', 'CHGCHAR1', 'CHGCHAR2', 'CHGCHAR3', 'MSIP1', 'APN', 'ZONEID', 'BILLINGTYPE', 'RAT1', 'RAT2', 'RAT3', 'ULI1', 'ULI2', 'ULI3', 'CHGID', 'ROAMING1', 'ROAMING2', 'ROAMING3', 'SGSN_MCC_MNC1', 'SGSN_MCC_MNC2', 'SGSN_MCC_MNC3', 'USERDEF1', 'USERDEF2', 'USERDEF3', 'USERDEF4', 'USERPROFALIAS', 'MCC', 'MNC', 'SESSIONID', 'GGSNIP1', 'GGSNIP2', 'GGSNIP3', 'TIMESTAMP1', 'TIMESTAMP2', 'TIMESTAMP3', 'MSIP2', 'MSIP3', 'UPIPV4', 'UPIPV6', 'RANDNUM'] -%}
        {%- if item.ANTIFRAUD is not none -%}
            ANTIFRAUD={{item.ANTIFRAUD}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：DATATYPE=CHGCHAR1/CHGCHAR2/CHGCHAR3 时可选 --- -#}
    {%- if item.DATATYPE in ['CHGCHAR1', 'CHGCHAR2', 'CHGCHAR3'] -%}
        {%- if item.CCFORMAT is not none -%}
            CCFORMAT={{item.CCFORMAT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ENCRYALGORI=MD5/RC4/AES128/AES256/SHA256/AES128_CTR/AES128_GCM/AES256_CTR/AES256_GCM 时可选 --- -#}
    {%- if item.ENCRYALGORI in ['MD5', 'RC4', 'AES128', 'AES256', 'SHA256', 'AES128_CTR', 'AES128_GCM', 'AES256_CTR', 'AES256_GCM'] -%}
        {%- if item.CIPHERTXTENCODE is not none -%}
            CIPHERTXTENCODE={{item.CIPHERTXTENCODE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：DATATYPE=ZONEID 时可选 --- -#}
    {%- if item.DATATYPE == 'ZONEID' -%}
        {%- if item.ERRFGSUBTLSTP is not none -%}
            ERRFGSUBTLSTP={{item.ERRFGSUBTLSTP}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：DATATYPE=ZONEID 时可选 --- -#}
    {%- if item.DATATYPE == 'ZONEID' -%}
        {%- if item.ERRFLGTLSTP is not none -%}
            ERRFLGTLSTP={{item.ERRFLGTLSTP}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：DATATYPE=MSISDN1/MSISDN2/MSISDN3/IMSI1/IMSI2/IMSI3/IMEI1/IMEI2/IMEI3/SGSNIP1/SGSNIP2/SGSNIP3/SUBPROFILE1/SUBPROFILE2/SUBPROFILE3/CHGCHAR1/CHGCHAR2/CHGCHAR3/MSIP1/APN/ZONEID/BILLINGTYPE/RAT1/RAT2/RAT3/ULI1/ULI2/ULI3/CHGID/ROAMING1/ROAMING2/ROAMING3/SGSN_MCC_MNC1/SGSN_MCC_MNC2/SGSN_MCC_MNC3/USERDEF1/USERDEF2/USERDEF3/USERDEF4/USERPROFALIAS/MCC/MNC/SESSIONID/GGSNIP1/GGSNIP2/GGSNIP3/TIMESTAMP1/TIMESTAMP2/TIMESTAMP3/MSIP2/MSIP3/UPIPV4/UPIPV6 时可选 --- -#}
    {%- if item.DATATYPE in ['MSISDN1', 'MSISDN2', 'MSISDN3', 'IMSI1', 'IMSI2', 'IMSI3', 'IMEI1', 'IMEI2', 'IMEI3', 'SGSNIP1', 'SGSNIP2', 'SGSNIP3', 'SUBPROFILE1', 'SUBPROFILE2', 'SUBPROFILE3', 'CHGCHAR1', 'CHGCHAR2', 'CHGCHAR3', 'MSIP1', 'APN', 'ZONEID', 'BILLINGTYPE', 'RAT1', 'RAT2', 'RAT3', 'ULI1', 'ULI2', 'ULI3', 'CHGID', 'ROAMING1', 'ROAMING2', 'ROAMING3', 'SGSN_MCC_MNC1', 'SGSN_MCC_MNC2', 'SGSN_MCC_MNC3', 'USERDEF1', 'USERDEF2', 'USERDEF3', 'USERDEF4', 'USERPROFALIAS', 'MCC', 'MNC', 'SESSIONID', 'GGSNIP1', 'GGSNIP2', 'GGSNIP3', 'TIMESTAMP1', 'TIMESTAMP2', 'TIMESTAMP3', 'MSIP2', 'MSIP3', 'UPIPV4', 'UPIPV6'] -%}
        {%- if item.GRAYLIST is not none -%}
            GRAYLIST={{item.GRAYLIST}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：DATATYPE=USERPROFALIAS 时可选 --- -#}
    {%- if item.DATATYPE == 'USERPROFALIAS' -%}
        {%- if item.HEADERFLDLEN is not none -%}
            HEADERFLDLEN={{item.HEADERFLDLEN}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：DATATYPE=IMEI1/IMEI2/IMEI3 时可选 --- -#}
    {%- if item.DATATYPE in ['IMEI1', 'IMEI2', 'IMEI3'] -%}
        {%- if item.IMEITYPE is not none -%}
            IMEITYPE={{item.IMEITYPE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ENCRYALGORI=RC4 时可选 --- -#}
    {%- if item.ENCRYALGORI == 'RC4' -%}
        {%- if item.RC4KEYMD5EN is not none -%}
            RC4KEYMD5EN={{item.RC4KEYMD5EN}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：DATATYPE=MSISDN1/MSISDN2/MSISDN3 时可选 --- -#}
    {%- if item.DATATYPE in ['MSISDN1', 'MSISDN2', 'MSISDN3'] -%}
        {%- if item.REMOVEDMCC is not none -%}
            REMOVEDMCC="{{item.REMOVEDMCC}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：ENCRYALGORI=MD5/SHA256 时可选 --- -#}
    {%- if item.ENCRYALGORI in ['MD5', 'SHA256'] -%}
        {%- if item.SALTSW is not none -%}
            SALTSW={{item.SALTSW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：DATATYPE=TIMESTAMP1/TIMESTAMP2/TIMESTAMP3 时可选 --- -#}
    {%- if item.DATATYPE in ['TIMESTAMP1', 'TIMESTAMP2', 'TIMESTAMP3'] -%}
        {%- if item.TSPRECISION is not none -%}
            TSPRECISION={{item.TSPRECISION}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 6 //配置HTTPS头增强使用的计费属性。

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

### 7 //配置HTTPS头增强使用的PCC动作策略组。

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

### 8 //配置HTTPS头增强使用的规则。

```jinja2
{%- for item in add_rule_list -%}
    ADD RULE:
    {#- --- 必选参数 --- -#}
    RULENAME="{{item.RULENAME}}",
    POLICYTYPE={{item.POLICYTYPE}},
    FILTERINGMODE={{item.FILTERINGMODE}},
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

### 9 //配置计费规则。

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

### 10 //配置HTTPS头增强使用的业务策略组合（规则与用户模板的绑定关系）。

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

