---
id: GWFD-020356
name: 激活计费信息实时提醒
ne_type: UDG
type: feature
description: 当运营商部署在线计费用户上网欢迎页面提醒、上网过程流量提醒或者欠费充值提醒业务时，需要激活计费信息实时提醒特性。  适用于SGW-U、PGW-U、UPF。
risk_level: ''
doc_source: ["特性部署","特性指南","UDG特性指南","计费功能","GWFD-020356 计费信息实时提醒","激活计费信息实时提醒"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当运营商部署在线计费用户上网欢迎页面提醒、上网过程流量提醒或者欠费充值提醒业务时，需要激活计费信息实时提醒特性。适用于SGW-U、PGW-U、UPF。

## 必备事项
前提条件

* 请仔细阅读GWFD-110314 计费信息实时提醒。
* 完成**加载license**（如果有需求，请联系华为技术支持工程师处理）。
* 完成激活在线计费。
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
    add_extendedfilter_list:
      type: items
      properties:
        EXTFLTNAME:
          name: '扩展过滤器名字'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '一次重定向的URL白名单列表，匹配上该名单的URL才能触发页面提醒。'
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
    add_redirappendinfo_list:
      type: items
      properties:
        APPENDINFONAME:
          name: '重定向携带信息名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '设置重定向URL中可携带用户的原始请求URL、IMSI、IMEI或MS-IP信息。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        REQURLFLAG:
          name: '请求URL标识'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
        MSISDNFLAG:
          name: 'MSISDN携带标识'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
        IMSIFLAG:
          name: 'IMSI携带标识'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
        IMSIENCRYALGORI:
          name: 'IMSI加密算法'
          type: string
          enum:
          - AES128
          - AES128_CTR
          - AES128_GCM
          - AES256
          - AES256_CTR
          - AES256_GCM
          - BLOWFISH128
          - NONE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: AES256_GCM
        IMEIFLAG:
          name: 'IMEI携带标识'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
        MSIPFLAG:
          name: 'MSIP携带标识'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
        IMEIENCRYALGORI:
          name: 'IMEI加密算法'
          type: string
          enum:
          - AES128
          - AES128_CTR
          - AES128_GCM
          - AES256
          - AES256_CTR
          - AES256_GCM
          - BLOWFISH128
          - NONE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: AES256_GCM
        IMEINAME:
          name: 'IMEI名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'imei'
        IMSISECRETKEY:
          name: 'IMSI密码'
          type: string
          minLength: 1
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMSISECRETKEYCONFIRM:
          name: '确认IMSI密码'
          type: string
          minLength: 1
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IMSINAME:
          name: 'IMSI名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'imsi'
        MSIPENCRYALGORI:
          name: 'MSIP加密算法'
          type: string
          enum:
          - AES128
          - AES128_CTR
          - AES128_GCM
          - AES256
          - AES256_CTR
          - AES256_GCM
          - BLOWFISH128
          - NONE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: AES256_GCM
        MSIPNAME:
          name: 'MSIP名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'msip'
        MSISDNENCRYALGORI:
          name: 'MSISDN加密算法'
          type: string
          enum:
          - AES128
          - AES128_CTR
          - AES128_GCM
          - AES256
          - AES256_CTR
          - AES256_GCM
          - BLOWFISH128
          - NONE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: AES256_GCM
        MSISDNNAME:
          name: 'MSISDN名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'msisdn'
        REQURLNAME:
          name: '请求URL名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'dest_url'
    set_gyoneshot_list:
      type: items
      properties:
        EXTFLTNAME:
          name: '扩展过滤器名字'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '设置重定向动作的名称，已通过**ADD EXTENDEDFILTER**命令配置完成。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        APPENDINFONAME:
          name: '重定向携带信息名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '设置重定向URL中携带的信息，已通过**ADD REDIRAPPENDINFO**命令配置完成。'
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
          description: 'PCC策略组。'
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
    add_filter_list:
      type: items
      properties:
        FILTERNAME:
          name: '过滤器名字'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: 'UDG通过将用户上下行报文匹配filter，实现报文的过滤。'
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
    add_fltbindflowf_list:
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
          name: '过滤器名字'
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PROTOCOLNAME:
          name: '协议名称'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '绑定的七层协议。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        L7FILTERNAME:
          name: '七层过滤器名字'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: '绑定的七层过滤条件已通过**ADD L7FILTER**命令配置。'
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
          description: '重定向页面使用的内容计费规则。'
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
          description: '绑定的PCC策略组已通过**ADD PCCPOLICYGRP**命令配置。'
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
          description: '绑定的FlowFilter已通过**ADD FLOWFILTER**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        POLICYNAME:
          name: '策略名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: ''
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
          description: ''
          data_source: ''
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
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV3G5RCIN01'
      SWITCH: ENABLE
    add_extendedfilter_list:
    - EXTFLTNAME: 'gy-oneshot-url'
      URL: 'www.huawei.com'
    add_redirappendinfo_list:
    - APPENDINFONAME: 'testredirappendinfo'
      REQURLFLAG: ENABLE
      MSISDNFLAG: DISABLE
      IMSIFLAG: ENABLE
      IMSIENCRYALGORI: AES256
      IMEIFLAG: ENABLE
      MSIPFLAG: ENABLE
      IMEIENCRYALGORI: AES256_GCM
      IMEINAME: 'imei'
      IMSISECRETKEY: ''
      IMSISECRETKEYCONFIRM: ''
      IMSINAME: 'imsi'
      MSIPENCRYALGORI: AES256_GCM
      MSIPNAME: 'msip'
      MSISDNENCRYALGORI: AES256_GCM
      MSISDNNAME: 'msisdn'
      REQURLNAME: 'dest_url'
    set_gyoneshot_list:
    - EXTFLTNAME: 'gy-oneshot-url'
      APPENDINFONAME: 'testredirappendinfo'
    add_urr_list:
    - URRNAME: 'urr_red'
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
    - URRGROUPNAME: 'cp_red'
      UPURRNAME1: 'urr_red'
      DOWNURRNAME1: 'urr_red'
    add_pccpolicygrp_list:
    - PCCPOLICYGRPNM: 'cg_red'
      URRGROUPNAME: 'cp_red'
    add_filter_list:
    - FILTERNAME: 'filter_red'
      L34PROTTYPE: STRING
      L34PROTOCOL: TCP
      SVRSTARTPORT: 80
      SVRENDPORT: 80
      L34PROTNUM: ''
    add_l7filter_list:
    - L7FILTERNAME: 'l7-red'
      SUBL7FLTNAME: 'sl7-red'
      URL: '10.13.4.3/*'
      URLTYPE: URL
    add_flowfilter_list:
    - FLOWFILTERNAME: 'fg_red'
    add_fltbindflowf_list:
    - FLOWFILTERNAME: 'fg_red'
      FILTERNAME: 'filter_red'
    add_protbindflowf_list:
    - FLOWFILTERNAME: 'fg_red'
      PROTOCOLNAME: 'http'
      L7FILTERNAME: 'l7-red'
    set_refreshsrv_list:
    - REFRESHTYPE: USERPROFILE
    add_rule_list:
    - RULENAME: 'rule_red'
      POLICYTYPE: PCC
      FILTERINGMODE: FLOWFILTER
      FLOWFILTERNAME: 'fg_red'
      POLICYNAME: 'cg_red'
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
      RULENAME: 'rule_red'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 打开本特性的License配置开关。

### **任务描述**

### 本例中，当用户访问www.huawei.com URL时触发欢迎页面提醒和流量页面提醒，用户账户余额耗尽，访问www.huawei.com页面触发欠费充值提醒。

### 为欢迎提醒和流量提醒的重定向页面规划相同URR ID。

### **脚本**

### //打开本特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 2 配置一次重定向的参数。

### //配置一次重定向的参数。

#### 2.1 配置一次重定向URL白名单列表，匹配上白名单的URL才会触发重定向。

```jinja2
{%- for item in add_extendedfilter_list -%}
    ADD EXTENDEDFILTER:
    {#- --- 必选参数 --- -#}
    EXTFLTNAME="{{item.EXTFLTNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.URL is not none -%}
        URL="{{item.URL}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.2 配置一次重定向携带的用户原始请求URL、IMSI、IMEI或MS-IP信息。

```jinja2
{%- for item in add_redirappendinfo_list -%}
    ADD REDIRAPPENDINFO:
    {#- --- 必选参数 --- -#}
    APPENDINFONAME="{{item.APPENDINFONAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.REQURLFLAG is not none -%}
        REQURLFLAG={{item.REQURLFLAG}},
    {%- endif -%}
    {%- if item.MSISDNFLAG is not none -%}
        MSISDNFLAG={{item.MSISDNFLAG}},
    {%- endif -%}
    {%- if item.IMSIFLAG is not none -%}
        IMSIFLAG={{item.IMSIFLAG}},
    {%- endif -%}
    {%- if item.IMEIFLAG is not none -%}
        IMEIFLAG={{item.IMEIFLAG}},
    {%- endif -%}
    {%- if item.MSIPFLAG is not none -%}
        MSIPFLAG={{item.MSIPFLAG}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IMSIENCRYALGORI=AES128/BLOWFISH128/AES256/AES128_CTR/AES128_GCM/AES256_CTR/AES256_GCM 时必选 --- -#}
    {%- if item.IMSIENCRYALGORI in ['AES128', 'BLOWFISH128', 'AES256', 'AES128_CTR', 'AES128_GCM', 'AES256_CTR', 'AES256_GCM'] -%}
        IMSISECRETKEY="{{item.IMSISECRETKEY}}",
    {%- endif -%}
    {#- --- 条件必选：IMSIENCRYALGORI=AES128/BLOWFISH128/AES256/AES128_CTR/AES128_GCM/AES256_CTR/AES256_GCM 时必选 --- -#}
    {%- if item.IMSIENCRYALGORI in ['AES128', 'BLOWFISH128', 'AES256', 'AES128_CTR', 'AES128_GCM', 'AES256_CTR', 'AES256_GCM'] -%}
        IMSISECRETKEYCONFIRM="{{item.IMSISECRETKEYCONFIRM}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IMSIFLAG=ENABLE 时可选 --- -#}
    {%- if item.IMSIFLAG == 'ENABLE' -%}
        {%- if item.IMSIENCRYALGORI is not none -%}
            IMSIENCRYALGORI={{item.IMSIENCRYALGORI}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IMEIFLAG=ENABLE 时可选 --- -#}
    {%- if item.IMEIFLAG == 'ENABLE' -%}
        {%- if item.IMEIENCRYALGORI is not none -%}
            IMEIENCRYALGORI={{item.IMEIENCRYALGORI}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IMEIFLAG=ENABLE 时可选 --- -#}
    {%- if item.IMEIFLAG == 'ENABLE' -%}
        {%- if item.IMEINAME is not none -%}
            IMEINAME="{{item.IMEINAME}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：IMSIFLAG=ENABLE 时可选 --- -#}
    {%- if item.IMSIFLAG == 'ENABLE' -%}
        {%- if item.IMSINAME is not none -%}
            IMSINAME="{{item.IMSINAME}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：MSIPFLAG=ENABLE 时可选 --- -#}
    {%- if item.MSIPFLAG == 'ENABLE' -%}
        {%- if item.MSIPENCRYALGORI is not none -%}
            MSIPENCRYALGORI={{item.MSIPENCRYALGORI}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：MSIPFLAG=ENABLE 时可选 --- -#}
    {%- if item.MSIPFLAG == 'ENABLE' -%}
        {%- if item.MSIPNAME is not none -%}
            MSIPNAME="{{item.MSIPNAME}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：MSISDNFLAG=ENABLE 时可选 --- -#}
    {%- if item.MSISDNFLAG == 'ENABLE' -%}
        {%- if item.MSISDNENCRYALGORI is not none -%}
            MSISDNENCRYALGORI={{item.MSISDNENCRYALGORI}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：MSISDNFLAG=ENABLE 时可选 --- -#}
    {%- if item.MSISDNFLAG == 'ENABLE' -%}
        {%- if item.MSISDNNAME is not none -%}
            MSISDNNAME="{{item.MSISDNNAME}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：REQURLFLAG=ENABLE 时可选 --- -#}
    {%- if item.REQURLFLAG == 'ENABLE' -%}
        {%- if item.REQURLNAME is not none -%}
            REQURLNAME="{{item.REQURLNAME}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.3 配置一次重定向的URL白名单列表。

```jinja2
{%- for item in set_gyoneshot_list -%}
    SET GYONESHOT:
    {#- --- 可选参数 --- -#}
    {%- if item.EXTFLTNAME is not none -%}
        EXTFLTNAME="{{item.EXTFLTNAME}}",
    {%- endif -%}
    {%- if item.APPENDINFONAME is not none -%}
        APPENDINFONAME="{{item.APPENDINFONAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置一次重定向中重定向页面的计入的URR。

### //配置一次重定向中重定向页面的URR ID。

#### 3.1 配置URR。

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

#### 3.2 配置URR组。

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

#### 3.3 配置PCC策略组，绑定上面配置的URR组。

#### //配置计费PCC策略组。

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

#### 多次执行步骤4.1~步骤4.3，可以分别配置欢迎页面和流量提醒页面的PCC策略组，也可以使用同一PCC策略组，具体根据运营商的需求规划。

#### 3.4 配置三四层过滤条件。

#### //配置三四层和七层信息。

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
    {#- --- 条件必选：L34PROTTYPE=NUMBER 时必选 --- -#}
    {%- if item.L34PROTTYPE == 'NUMBER' -%}
        L34PROTNUM={{item.L34PROTNUM}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 3.5 配置七层过滤条件。

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
    ;
{%- endfor -%}
```

#### 3.6 配置流过滤器。

```jinja2
{%- for item in add_flowfilter_list -%}
    ADD FLOWFILTER:
    {#- --- 必选参数 --- -#}
    FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
    ;
{%- endfor -%}
```

#### 3.7 绑定三四层过滤条件。

```jinja2
{%- for item in add_fltbindflowf_list -%}
    ADD FLTBINDFLOWF:
    {#- --- 必选参数 --- -#}
    FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
    FILTERNAME="{{item.FILTERNAME}}",
    ;
{%- endfor -%}
```

#### 3.8 绑定七层过滤条件。

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

#### 3.9 将新配置的Filter、L7filter置为生效。

```jinja2
{%- for item in set_refreshsrv_list -%}
    SET REFRESHSRV:
    {#- --- 必选参数 --- -#}
    REFRESHTYPE={{item.REFRESHTYPE}},
    ;
{%- endfor -%}
```

#### 3.10 配置重定向页面的内容计费规则。

#### //配置重定向页面的内容计费规则。

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

#### 如果运营商希望基于流过滤器组设置过滤条件时，配置“流过滤器或流过滤器组选择(FILTERINGMODE)”为“FLOWFILTERGRP”，并且使用命令配置流过滤器组。

### 4 配置计费信息实时提醒使用的业务策略组合。

### //配置计费信息实时提醒使用的业务策略组合。

#### 4.1 创建UserProfile。

```jinja2
{%- for item in add_userprofile_list -%}
    ADD USERPROFILE:
    {#- --- 必选参数 --- -#}
    USERPROFILENAME="{{item.USERPROFILENAME}}",
    ;
{%- endfor -%}
```

#### 4.2 将已配置的Rule绑定到UserProfile。

```jinja2
{%- for item in add_rulebinding_list -%}
    ADD RULEBINDING:
    {#- --- 必选参数 --- -#}
    USERPROFILENAME="{{item.USERPROFILENAME}}",
    RULENAME="{{item.RULENAME}}",
    ;
{%- endfor -%}
```

