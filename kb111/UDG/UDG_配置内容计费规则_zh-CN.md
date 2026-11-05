---
id: ''
name: 配置内容计费规则
ne_type: UDG
type: feature
description: 媒体中继业务中，UPF需要识别DNS请求中是否携带OTT规划的relay域名来作DNS代理，此时需要在UPF上配置对应的业务计费规则。
risk_level: ''
doc_source: ["特性部署","业务专题","5G Core 媒体中继解决方案","媒体中继业务配置","新建媒体中继基础配置","配置UPF","增加媒体服务商配置（基于OTT应用）","配置内容计费规则"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
媒体中继业务中，UPF需要识别DNS请求中是否携带OTT规划的relay域名来作DNS代理，此时需要在UPF上配置对应的业务计费规则。

## 必备事项
前提条件

已参考增加媒体服务商基础配置~配置点播业务的安全认证策略完成媒体中继业务相关配置。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_flowfilter_list:
      type: items
      properties:
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '-'
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
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: NONE
        FLOWFILTERTYPE:
          name: 'FlowFilter类型'
          type: string
          enum:
          - EXTEROTTDB
          - USERCONFIG
          required: false
          description: '-'
          data_source: '固定取值'
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
    add_host_list:
      type: items
      properties:
        HOSTNAME:
          name: 'Host配置名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DOMAINVALUE:
          name: '域名'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '与OTT厂商规划的域名保持一致。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: 65535
    add_filter_list:
      type: items
      properties:
        FILTERNAME:
          name: '过滤器名字'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '-'
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
          data_source: '固定取值'
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
          data_source: '固定取值'
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
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        HOSTNAME:
          name: 'Host配置名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: '已通过**ADD HOST**命令完成配置。'
          data_source: '已配置数据中获取'
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
    add_filteripv6_list:
      type: items
      properties:
        FILTERNAME:
          name: '过滤器名字'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '-'
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
          description: '-'
          data_source: '固定取值'
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
          data_source: '固定取值'
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
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        HOSTNAME:
          name: 'Host配置名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: '已通过**ADD HOST**命令完成配置。'
          data_source: '已配置数据中获取'
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
    add_fltbindflowf_list:
      type: items
      properties:
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '已通过  **ADD FLOWFILTER**  命令完成配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        FILTERNAME:
          name: '过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '已通过  **ADD FILTER**  或**ADD FILTERIPV6**命令完成配置。'
          data_source: '已配置数据中获取'
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
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SUBL7FLTNAME:
          name: '子七层过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '-'
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
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: URL
        URL:
          name: 'URL'
          type: string
          minLength: 0
          maxLength: 119
          required: false
          description: '根据OTT厂商规划的域名进行配置。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        METHODTYPE:
          name: '方法类型'
          type: string
          required: false
          description: '-'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        ISREFEREREN:
          name: 'Referer关联计费开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
        MMSBLURMATCH:
          name: '彩信模糊匹配'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
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
    add_protbindflowf_list:
      type: items
      properties:
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '已通过  **ADD FLOWFILTER**  命令完成配置。'
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
          data_source: '固定取值'
          pattern: ''
          default: ''
        L7FILTERNAME:
          name: '七层过滤器名字'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: '已通过**ADD L7FILTER**命令完成配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_host_list_1:
      type: items
      properties:
        HOSTNAME:
          name: 'Host配置名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DOMAINVALUE:
          name: '域名'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '与OTT厂商规划的域名保持一致。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: 65535
    add_filter_list_1:
      type: items
      properties:
        FILTERNAME:
          name: '过滤器名字'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '-'
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
          data_source: '固定取值'
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
          data_source: '固定取值'
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
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        HOSTNAME:
          name: 'Host配置名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: '已通过**ADD HOST**命令完成配置。'
          data_source: '已配置数据中获取'
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
    add_filteripv6_list_1:
      type: items
      properties:
        FILTERNAME:
          name: '过滤器名字'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '-'
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
          description: '-'
          data_source: '固定取值'
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
          data_source: '固定取值'
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
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
        HOSTNAME:
          name: 'Host配置名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: '已通过**ADD HOST**命令完成配置。'
          data_source: '已配置数据中获取'
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
    add_fltbindflowf_list_4:
      type: items
      properties:
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '已通过  **ADD FLOWFILTER**  命令完成配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        FILTERNAME:
          name: '过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '已通过  **ADD FILTER**  或**ADD FILTERIPV6**命令完成配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_l7filter_list_2:
      type: items
      properties:
        L7FILTERNAME:
          name: '七层过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SUBL7FLTNAME:
          name: '子七层过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '-'
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
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: URL
        URL:
          name: 'URL'
          type: string
          minLength: 0
          maxLength: 119
          required: false
          description: '根据OTT厂商规划的域名进行配置。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        METHODTYPE:
          name: '方法类型'
          type: string
          required: false
          description: '-'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        ISREFEREREN:
          name: 'Referer关联计费开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
        MMSBLURMATCH:
          name: '彩信模糊匹配'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
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
    add_protbindflowf_list_2:
      type: items
      properties:
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '已通过  **ADD FLOWFILTER**  命令完成配置。'
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
          data_source: '固定取值'
          pattern: ''
          default: ''
        L7FILTERNAME:
          name: '七层过滤器名字'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: '已通过**ADD L7FILTER**命令完成配置。'
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
          description: '配置媒体中继的费率。如已存在对应费率，则不需要重复配置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        URRID:
          name: 'URR标识'
          type: integer
          minimum: 0
          maximum: 2147483646
          required: true
          description: '由运营商提供，UPF与SMF侧配置值需保持一致。'
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
          description: '-'
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
          description: '-'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DOWNURRNAME1:
          name: '下行发起URR名称1'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '-'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        UPURRNAME2:
          name: '上行发起URR名称2'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '-'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DOWNURRNAME2:
          name: '下行发起URR名称2'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '-'
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
          description: '-'
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
          description: '已通过  **ADD FLOWFILTER**  命令完成配置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PRIORITY:
          name: '全局优先级'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: 4294967295
        POLICYNAME:
          name: '策略名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: '已通过**ADD PCCPOLICYGRP**命令完成配置。'
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
    add_rulebinding_list:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '已通过**ADD USERPROFILE**命令完成配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        RULENAME:
          name: '规则名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '已通过**ADD RULE**命令完成配置。'
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
          description: '-'
          data_source: '固定取值'
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
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
  examples:
    add_flowfilter_list:
    - FLOWFILTERNAME: 'sp_relay_00_f_f_h_001'
      TETHERDETFLAG: NONE
      FLOWFILTERTYPE: USERCONFIG
      FILTERGRPNAME: ''
    add_host_list:
    - HOSTNAME: 'sp_relay_live_001_h_100'
      DOMAINVALUE: 'relay.spliving.com'
      PRIORITY: 33800
    add_filter_list:
    - FILTERNAME: 'sp_relay_live_001_f_100'
      L34PROTTYPE: STRING
      L34PROTOCOL: ANY
      SVRIPMODE: HOSTNAME
      HOSTNAME: 'sp_relay_live_001_h_100'
      MSSTARTPORT: 0
      MSENDPORT: 65535
      SVRSTARTPORT: 0
      SVRENDPORT: 65535
      L34PROTNUM: ''
      DOMAINVALUE: ''
      HOSTPRIORITY: ''
      SVRIP: ''
      SVRIPLISTNAME: ''
      SVRIPMASKTYPE: ''
    add_filteripv6_list:
    - FILTERNAME: 'ipv6_sp_relay_live_001_f_100'
      L34PROTTYPEV6: STRING
      L34PROTOCOL: ANY
      SVRIPMODE: HOSTNAME
      HOSTNAME: 'sp_relay_live_001_h_100'
      MSSTARTPORT: 0
      MSENDPORT: 65535
      SVRSTARTPORT: 0
      SVRENDPORT: 65535
      L34PROTNUM: ''
      DOMAINVALUE: ''
      HOSTPRIORITY: ''
      SVRIPLISTNAME: ''
      SVRIPV6: ''
      SVRIPV6MASKTYPE: ''
    add_fltbindflowf_list:
    - FLOWFILTERNAME: 'sp_relay_00_f_f_h_001'
      FILTERNAME: 'sp_relay_live_001_f_100'
    add_l7filter_list:
    - L7FILTERNAME: 'sp_relay_00_l7_f_001'
      SUBL7FLTNAME: 'sp_relay_00_sl7_f_100'
      URLTYPE: URL
      URL: '*relay.spliving.com/*'
      METHODTYPE: CONNECT-1&DELETE-1&GET-1&HEAD-1&OPTIONS-1&POST-1&PUT-1&TRACE-1
      ISREFEREREN: DISABLE
      MMSBLURMATCH: DISABLE
      HOST: ''
    add_protbindflowf_list:
    - FLOWFILTERNAME: 'sp_relay_00_f_f_h_001'
      PROTOCOLNAME: 'http'
      L7FILTERNAME: 'sp_relay_00_l7_f_001'
    add_host_list_1:
    - HOSTNAME: 'sp_relay_vod_001_h_100'
      DOMAINVALUE: 'relay.spvod.com'
      PRIORITY: 33900
    add_filter_list_1:
    - FILTERNAME: 'sp_relay_vod_001_f_100'
      L34PROTTYPE: STRING
      L34PROTOCOL: ANY
      SVRIPMODE: HOSTNAME
      HOSTNAME: 'sp_relay_vod_001_h_100'
      MSSTARTPORT: 0
      MSENDPORT: 65535
      SVRSTARTPORT: 0
      SVRENDPORT: 65535
      L34PROTNUM: ''
      DOMAINVALUE: ''
      HOSTPRIORITY: ''
      SVRIP: ''
      SVRIPLISTNAME: ''
      SVRIPMASKTYPE: ''
    add_filteripv6_list_1:
    - FILTERNAME: 'ipv6_sp_relay_vod_001_f_100'
      L34PROTTYPEV6: STRING
      L34PROTOCOL: ANY
      SVRIPMODE: HOSTNAME
      HOSTNAME: 'sp_relay_vod_001_h_100'
      MSSTARTPORT: 0
      MSENDPORT: 65535
      SVRSTARTPORT: 0
      SVRENDPORT: 65535
      L34PROTNUM: ''
      DOMAINVALUE: ''
      HOSTPRIORITY: ''
      SVRIPLISTNAME: ''
      SVRIPV6: ''
      SVRIPV6MASKTYPE: ''
    add_fltbindflowf_list_4:
    - FLOWFILTERNAME: 'sp_relay_00_f_f_h_003'
      FILTERNAME: 'sp_relay_vod_001_f_100'
    add_l7filter_list_2:
    - L7FILTERNAME: 'sp_relay_00_l7_f_100'
      SUBL7FLTNAME: 'sp_relay_00_sl7_f_100'
      URLTYPE: URL
      URL: '*relay.spvod.com/*'
      METHODTYPE: CONNECT-1&DELETE-1&GET-1&HEAD-1&OPTIONS-1&POST-1&PUT-1&TRACE-1
      ISREFEREREN: DISABLE
      MMSBLURMATCH: DISABLE
      HOST: ''
    add_protbindflowf_list_2:
    - FLOWFILTERNAME: 'sp_relay_00_f_f_h_003'
      PROTOCOLNAME: 'http'
      L7FILTERNAME: 'sp_relay_00_l7_f_100'
    add_urr_list:
    - URRNAME: 'sp_relay_00_cbb_offline'
      URRID: 1750010088
      USAGERPTMODE: OFFLINE
      OFFMETERINGTYPE: FREE
      ONLMETERINGTYPE: FREE
      DFTQUOTAPARA: Byte
      DFTQUOTATIME: ''
      DFTQUOTAVOLUME: ''
      RG: ''
      SID: ''
    add_urrgroup_list:
    - URRGROUPNAME: 'sp_relay_00_ch_p'
      UPURRNAME1: 'sp_relay_00_cbb_offline'
      DOWNURRNAME1: 'sp_relay_00_cbb_offline'
      UPURRNAME2: 'sp_relay_00_cbb_online'
      DOWNURRNAME2: 'sp_relay_00_cbb_online'
    add_pccpolicygrp_list:
    - PCCPOLICYGRPNM: 'sp_relay_00_pcc_p_g'
      FUPSESSIONEXC: DISABLE
      SIGNALASSOCIATE: ENABLE
      ADCMUTEFLAG: ENABLE
      HTTP2DEGRADESW: INHERIT
      TOKENFUNCFLAG: DISABLE
      URRGROUPNAME: 'sp_relay_00_ch_p'
      TOKENENCRYALG: SHA256
      TOKENSECRETKEY: ''
      TOKENSECRETKEYCONFIRM: ''
    add_rule_list:
    - RULENAME: 'sp_relay_00_r_h_001'
      POLICYTYPE: PCC
      FILTERINGMODE: FLOWFILTER
      FLOWFILTERNAME: 'sp_relay_00_f_f_h_001'
      PRIORITY: 30280
      POLICYNAME: 'sp_relay_00_pcc_p_g'
      FLWFLTRGRPNAME: ''
      ADCMUTEFLAG: ENABLE
      ALGSWITCH: DISABLE
      RDSTRIGGERFLAG: DISABLE
      REDIRIPVERFLAG: ''
      REMARKFPISEL: REMARK
      SRVLBOFLAG: DISABLE
      WORKERNAME: ''
      WORKERPARA: ''
    add_rulebinding_list:
    - USERPROFILENAME: 'testuserprofilename'
      RULENAME: 'sp_relay_00_r_h_001'
      POLICYTYPE: PCC
    set_refreshsrv_list:
    - REFRESHTYPE: USERPROFILE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 //配置FlowFilter

```jinja2
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
```

### 2 //针对直播业务，配置L34 HOST规则绑定到FlowFilter，配置L7层匹配规则绑定到FlowFilter。

```jinja2
{%- for item in add_host_list -%}
    ADD HOST:
    {#- --- 必选参数 --- -#}
    HOSTNAME="{{item.HOSTNAME}}",
    DOMAINVALUE="{{item.DOMAINVALUE}}",
    {#- --- 可选参数 --- -#}
    {%- if item.PRIORITY is not none -%}
        PRIORITY={{item.PRIORITY}},
    {%- endif -%}
    ;
{%- endfor -%}
```

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
    {#- --- 条件必选：SVRIPMODE=HOSTNAME/DOMAIN 时必选 --- -#}
    {%- if item.SVRIPMODE in ['HOSTNAME', 'DOMAIN'] -%}
        HOSTNAME="{{item.HOSTNAME}}",
    {%- endif -%}
    {#- --- 条件必选：SVRIPMODE=DOMAIN 时必选 --- -#}
    {%- if item.SVRIPMODE == 'DOMAIN' -%}
        DOMAINVALUE="{{item.DOMAINVALUE}}",
    {%- endif -%}
    {#- --- 条件必选：L34PROTTYPEV6=NUMBER 时必选 --- -#}
    {%- if item.L34PROTTYPEV6 == 'NUMBER' -%}
        L34PROTNUM={{item.L34PROTNUM}},
    {%- endif -%}
    {#- --- 条件必选：SVRIPMODE=IPLIST 时必选 --- -#}
    {%- if item.SVRIPMODE == 'IPLIST' -%}
        SVRIPLISTNAME="{{item.SVRIPLISTNAME}}",
    {%- endif -%}
    {#- --- 条件必选：SVRIPMODE=IP 时必选 --- -#}
    {%- if item.SVRIPMODE == 'IP' -%}
        SVRIPV6="{{item.SVRIPV6}}",
    {%- endif -%}
    {#- --- 条件必选：SVRIPMODE=IP 时必选 --- -#}
    {%- if item.SVRIPMODE == 'IP' -%}
        SVRIPV6MASKTYPE={{item.SVRIPV6MASKTYPE}},
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
{%- for item in add_fltbindflowf_list -%}
    ADD FLTBINDFLOWF:
    {#- --- 必选参数 --- -#}
    FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
    FILTERNAME="{{item.FILTERNAME}}",
    ;
{%- endfor -%}
```

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
    {%- if item.METHODTYPE is not none -%}
        METHODTYPE={{item.METHODTYPE}},
    {%- endif -%}
    {%- if item.ISREFEREREN is not none -%}
        ISREFEREREN={{item.ISREFEREREN}},
    {%- endif -%}
    {%- if item.MMSBLURMATCH is not none -%}
        MMSBLURMATCH={{item.MMSBLURMATCH}},
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

### 3 //针对点播业务，配置L34 HOST规则绑定到FlowFilter，配置L7层匹配规则绑定到FlowFilter。

```jinja2
{%- for item in add_host_list_1 -%}
    ADD HOST:
    {#- --- 必选参数 --- -#}
    HOSTNAME="{{item.HOSTNAME}}",
    DOMAINVALUE="{{item.DOMAINVALUE}}",
    {#- --- 可选参数 --- -#}
    {%- if item.PRIORITY is not none -%}
        PRIORITY={{item.PRIORITY}},
    {%- endif -%}
    ;
{%- endfor -%}
```

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
    {#- --- 条件必选：SVRIPMODE=HOSTNAME/DOMAIN 时必选 --- -#}
    {%- if item.SVRIPMODE in ['HOSTNAME', 'DOMAIN'] -%}
        HOSTNAME="{{item.HOSTNAME}}",
    {%- endif -%}
    {#- --- 条件必选：SVRIPMODE=DOMAIN 时必选 --- -#}
    {%- if item.SVRIPMODE == 'DOMAIN' -%}
        DOMAINVALUE="{{item.DOMAINVALUE}}",
    {%- endif -%}
    {#- --- 条件必选：L34PROTTYPEV6=NUMBER 时必选 --- -#}
    {%- if item.L34PROTTYPEV6 == 'NUMBER' -%}
        L34PROTNUM={{item.L34PROTNUM}},
    {%- endif -%}
    {#- --- 条件必选：SVRIPMODE=IPLIST 时必选 --- -#}
    {%- if item.SVRIPMODE == 'IPLIST' -%}
        SVRIPLISTNAME="{{item.SVRIPLISTNAME}}",
    {%- endif -%}
    {#- --- 条件必选：SVRIPMODE=IP 时必选 --- -#}
    {%- if item.SVRIPMODE == 'IP' -%}
        SVRIPV6="{{item.SVRIPV6}}",
    {%- endif -%}
    {#- --- 条件必选：SVRIPMODE=IP 时必选 --- -#}
    {%- if item.SVRIPMODE == 'IP' -%}
        SVRIPV6MASKTYPE={{item.SVRIPV6MASKTYPE}},
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
{%- for item in add_fltbindflowf_list_4 -%}
    ADD FLTBINDFLOWF:
    {#- --- 必选参数 --- -#}
    FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
    FILTERNAME="{{item.FILTERNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_l7filter_list_2 -%}
    ADD L7FILTER:
    {#- --- 必选参数 --- -#}
    L7FILTERNAME="{{item.L7FILTERNAME}}",
    SUBL7FLTNAME="{{item.SUBL7FLTNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.URLTYPE is not none -%}
        URLTYPE={{item.URLTYPE}},
    {%- endif -%}
    {%- if item.METHODTYPE is not none -%}
        METHODTYPE={{item.METHODTYPE}},
    {%- endif -%}
    {%- if item.ISREFEREREN is not none -%}
        ISREFEREREN={{item.ISREFEREREN}},
    {%- endif -%}
    {%- if item.MMSBLURMATCH is not none -%}
        MMSBLURMATCH={{item.MMSBLURMATCH}},
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

```jinja2
{%- for item in add_protbindflowf_list_2 -%}
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

### 4 //增加内容计费费率（未单独规划费率时，不需要新配置，复用原有费率）

### 如果需要增加计费费率配置时，需要同步在SMF上增加对应的URR费率等相关配置，避免出现SMF与UPF的计费配置不一致，触发告警。

```jinja2
{%- if is_optional_add_billing_rate -%}
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
{%- endif -%}
```

```jinja2
{%- if is_optional_add_billing_rate -%}
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

```jinja2
{%- if is_optional_add_billing_rate -%}
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

### 5 //配置业务匹配规则并绑定到媒体中继签约套餐。

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

### 6 //执行配置刷新操作，生效媒体中继业务匹配规则。

```jinja2
{%- for item in set_refreshsrv_list -%}
    SET REFRESHSRV:
    {#- --- 必选参数 --- -#}
    REFRESHTYPE={{item.REFRESHTYPE}},
    ;
{%- endfor -%}
```

