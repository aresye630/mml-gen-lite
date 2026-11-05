---
id: ''
name: 部署UPF
ne_type: UNC
type: feature
description: 当前移动网络上承载的业务越来越丰富，运营商为了不断优化自身的服务及提升网络安全性，要求UPF能够根据数据包的分析（包括34层和7层的内容），按照预先定义的规则执行业务管理。UPF上该能力由SMF下发的Rule（规则）实现。  内容计费的配置需要做好规划，在PCF、SMF、UPF网元上统一进行配置，保证网元间配置的一致性。PCF、SMF、UPF上的配置及对应关系如图1所示。  **图1** PCF/SMF/UPF配置对应关系
risk_level: ''
doc_source: ["网络部署","业务专题","5G Core 计费解决方案","计费解决方案概述","计费方案部署与调测","方案一：未部署NCG的计费解决方案","部署UPF"]
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
          data_source: ''
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
          description: '配置URRGROUP。  说明：  URRGROUP下必须配置在线URR和离线URR，只配置一种计费模式且计费模式和用户的计费模式不匹配时无法计费。以下特殊场景除外：  当SMF使用融合计费时，SMF上的**SET USRPROFCHARGE** 、**SET APNCHARGECTRL**、**ADD CHARGEMETHOD**命令的“RGAPPLIED”配置为“DEFAULT”时，不能同时配置RG相同的离线和在线URR，否则会导致计费冲突。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        UPURRNAME1:
          name: '上行发起URR名称1'
          type: string
          maxLength: 31
          required: false
          description: '上下行业务触发使用的离线URR，已通过**ADD URR**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DOWNURRNAME1:
          name: '下行发起URR名称1'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UPURRNAME2:
          name: '上行发起URR名称2'
          type: string
          maxLength: 31
          required: false
          description: '上下行业务触发使用的在线URR，已通过**ADD URR**命令配置。'
          data_source: ''
          pattern: ''
          default: ''
        DOWNURRNAME2:
          name: '下行发起URR名称2'
          type: string
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
          required: false
          description: '配置PCC业务策略组。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        URRGROUPNAME:
          name: 'URR组名称'
          type: string
          required: false
          description: '已通过**ADD URRGROUP**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SIGURRGRPNAME:
          name: '信令URR组名称'
          type: string
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
          required: false
          description: '配置过滤器名字。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        L34PROTTYPE:
          name: '三四层IPv4协议输入类型'
          type: string
          required: false
          description: '字符串类型。'
          data_source: ''
          pattern: ''
          default: ''
        L34PROTOCOL:
          name: '三四层协议类型'
          type: string
          required: false
          description: '任意三四层协议。'
          data_source: ''
          pattern: ''
          default: ''
        MSSTARTPORT:
          name: '手机起始端口号'
          type: string
          required: false
          description: '设置手机起始端口号。该参数不大于手机结束端口号。'
          data_source: ''
          pattern: ''
          default: ''
        MSENDPORT:
          name: '手机结束端口号'
          type: string
          required: false
          description: '设置手机结束端口号。该参数不小于手机起始端口号。'
          data_source: ''
          pattern: ''
          default: ''
        SVRSTARTPORT:
          name: '服务器起始端口号'
          type: string
          required: false
          description: '设置服务器起始端口号。该参数不大于服务器结束端口号。'
          data_source: ''
          pattern: ''
          default: ''
        SVRENDPORT:
          name: '服务器结束端口号'
          type: string
          required: false
          description: '设置服务器结束端口号。该参数不小于服务器起始端口号。'
          data_source: ''
          pattern: ''
          default: ''
    add_filteripv6_list:
      type: items
      properties:
        FILTERNAME:
          name: '过滤器名字'
          type: string
          required: false
          description: '配置过滤器名字。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        L34PROTTYPEV6:
          name: '三四层IPv6协议输入类型'
          type: string
          required: false
          description: '字符串类型。'
          data_source: ''
          pattern: ''
          default: ''
        L34PROTOCOL:
          name: '三四层协议类型'
          type: string
          required: false
          description: '任意三四层协议。'
          data_source: ''
          pattern: ''
          default: ''
        SVRIPMODE:
          name: '服务器IP地址配置模式'
          type: string
          required: false
          description: '参数取值取决于服务器侧的IP地址配置模式。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        MSSTARTPORT:
          name: '手机起始端口号'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MSENDPORT:
          name: '手机结束端口号'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SVRSTARTPORT:
          name: '服务器起始端口号'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SVRENDPORT:
          name: '服务器结束端口号'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SVRIPV6:
          name: '服务器IPv6地址'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SVRIPV6MASKTYPE:
          name: '服务器IPv6地址掩码类型'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SVRIPV6MASKLEN:
          name: '服务器IPv6地址掩码长度'
          type: string
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
          required: false
          description: '配置七层过滤器。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SUBL7FLTNAME:
          name: '子七层过滤器名称'
          type: string
          required: false
          description: '配置该L7Filter的子七层过滤器名称。'
          data_source: ''
          pattern: ''
          default: ''
        URLTYPE:
          name: 'URL类型'
          type: string
          required: false
          description: '指定七层URL配置类型。  防欺诈功能开启时，RULE下绑定URL类型的7层filter时必须同时绑定三四层filter；防欺诈未开启时，RULE下可仅绑定URL类型的7层filter。'
          data_source: ''
          pattern: ''
          default: ''
        URL:
          name: 'URL'
          type: string
          required: false
          description: '-'
          data_source: ''
          pattern: ''
          default: ''
    add_flowfilter_list:
      type: items
      properties:
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
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
          required: false
          description: '绑定的流过滤器已通过**ADD FLOWFILTER**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        FILTERNAME:
          name: '过滤器名称'
          type: string
          required: false
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
          required: false
          description: '绑定的流过滤器已通过**ADD FLOWFILTER**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PROTOCOLNAME:
          name: '协议名称'
          type: string
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        L7FILTERNAME:
          name: '七层过滤器名字'
          type: string
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
          required: false
          description: '配置规则。SMF、UPF上RuleName以及RULE下配置的POLICYTYPE、POLICYNAME需要保持一致。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        POLICYTYPE:
          name: '策略类型'
          type: string
          required: false
          description: '-'
          data_source: ''
          pattern: ''
          default: ''
        FILTERINGMODE:
          name: '流过滤器或流过滤器组选择'
          type: string
          required: false
          description: '-'
          data_source: ''
          pattern: ''
          default: ''
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          required: false
          description: '使用的Flow Filter已通过**ADD FLOWFILTER**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        POLICYNAME:
          name: '策略名称'
          type: string
          required: false
          description: '使用的PCC策略组已通过**ADD PCCPOLICYGRP**命令配置。'
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: string
          required: false
          description: '数字越小优先级越高。只绑定三四层filter的RULE的优先级应该低于绑定7层filter的RULE的优先级。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_userprofile_list:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          maxLength: 63
          required: true
          description: 'USERPROFILE的名称统一规划，保证在PCF、SMF、UPF间名称一致。不一致时PCF下发的策略无法生效。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPTYPE:
          name: '用户模板类型'
          type: string
          enum:
          - PCC
          - ULCL
          - UPSELECT
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: PCC
        PROFILERANGE:
          name: '模板生效范围'
          type: string
          enum:
          - ALL
          - CENTRAL
          - LOCAL
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ALL
    add_rulebinding_list:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          maxLength: 63
          required: true
          description: '已通过**ADD USERPROFILE**命令配置。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        RULENAME:
          name: '规则名称'
          type: string
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
          name: '用户模板名称'
          type: string
          required: false
          description: '已通过**ADD USERPROFILE**命令配置生成。  说明：  USERPROFILE需要将缺省业务和缺省信令的URR组都配置完整，不配置时按照RULE没有匹配到URR的报文无法计费。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DFTURRGRPNAME:
          name: '缺省URR组名称'
          type: string
          required: false
          description: '已通过**ADD URRGROUP**命令配置生成。'
          data_source: ''
          pattern: ''
          default: ''
        DFTSIGURRGNAME:
          name: '缺省信令URR组名称'
          type: string
          required: false
          description: '已通过**ADD URRGROUP**命令配置生成。'
          data_source: ''
          pattern: ''
          default: ''
        GLBDFTURRGSW:
          name: '继承全局缺省URR组配置开关'
          type: string
          required: false
          description: '已通过**SET SPECTRAFURRGRP**命令配置生成。'
          data_source: ''
          pattern: ''
          default: ''
        GLBDFTSIGURRGSW:
          name: '继承全局缺省信令URR组开关'
          type: string
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
          required: false
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
          required: false
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
          required: false
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
    - URRGROUPNAME: 'UrrGp_URL'
      UPURRNAME1: 'urr_offline_URL'
      DOWNURRNAME1: 'urr_offline_URL'
      UPURRNAME2: 'urr_online_URL'
      DOWNURRNAME2: 'urr_online_URL'
    add_pccpolicygrp_list:
    - PCCPOLICYGRPNM: PPG_URL
      URRGROUPNAME: UrrGp_URL
      SIGURRGRPNAME: UrrGp_abnormal
    add_filter_list:
    - FILTERNAME: L34_any
      L34PROTTYPE: STRING
      L34PROTOCOL: ANY
      MSSTARTPORT: '0'
      MSENDPORT: '65535'
      SVRSTARTPORT: '0'
      SVRENDPORT: '65535'
    add_filteripv6_list:
    - FILTERNAME: ipv6_ims
      L34PROTTYPEV6: STRING
      L34PROTOCOL: ANY
      SVRIPMODE: IP
      MSSTARTPORT: '0'
      MSENDPORT: '65535'
      SVRSTARTPORT: '0'
      SVRENDPORT: '65535'
      SVRIPV6: fc00:8028:5002:10D::181
      SVRIPV6MASKTYPE: LENGTHTYPE
      SVRIPV6MASKLEN: '128'
    add_l7filter_list:
    - L7FILTERNAME: L7_URL
      SUBL7FLTNAME: http
      URLTYPE: URL
      URL: www.huawei.com
    add_flowfilter_list:
    - FLOWFILTERNAME: 'ff_L7'
    add_fltbindflowf_list:
    - FLOWFILTERNAME: ff_L7
      FILTERNAME: L34_any
    add_protbindflowf_list:
    - FLOWFILTERNAME: ff_L7
      PROTOCOLNAME: http
      L7FILTERNAME: L7_URL
    add_rule_list:
    - RULENAME: Rule001_url
      POLICYTYPE: PCC
      FILTERINGMODE: FLOWFILTER
      FLOWFILTERNAME: ff_L7
      POLICYNAME: PPG_URL
      PRIORITY: '100'
    add_userprofile_list:
    - USERPROFILENAME: 'userprofile001'
      UPTYPE: PCC
      PROFILERANGE: ALL
    add_rulebinding_list:
    - USERPROFILENAME: 'userprofile001'
      RULENAME: 'Rule001_url'
      POLICYTYPE: PCC
    set_urrgrpbinding_list:
    - USERPROFILENAME: userprofile001
      DFTURRGRPNAME: UrrGp_any
      DFTSIGURRGNAME: UrrGp_abnormal
      GLBDFTURRGSW: ENABLE
      GLBDFTSIGURRGSW: ENABLE
    set_spectrafurrgrp_list:
    - URRGROUPNAME: UrrGp_abnormal
    add_specurrgrplist_list:
    - URRGROUPNAME: UrrGp_URL
    set_refreshsrv_list:
    - REFRESHTYPE: ALL
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置使用量上报规则组属性。

#### 1.1 配置URR。

```jinja2
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
```

#### 1.2 配置URR组。

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

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_pccpolicygrp_list的变量区（command: ADD PCCPOLICYGRP） -#}
<!-- MISSING_MACRO: command=ADD PCCPOLICYGRP list_name=add_pccpolicygrp_list step_id=2 -->
```

### 3 配置过滤条件。

#### 3.1 配置三四层过滤条件。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_filter_list的变量区（command: ADD FILTER） -#}
<!-- MISSING_MACRO: command=ADD FILTER list_name=add_filter_list step_id=3.1 -->
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_filteripv6_list的变量区（command: ADD FILTERIPV6） -#}
<!-- MISSING_MACRO: command=ADD FILTERIPV6 list_name=add_filteripv6_list step_id=3.1 -->
```

#### 3.2 配置七层过滤条件。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_l7filter_list的变量区（command: ADD L7FILTER） -#}
<!-- MISSING_MACRO: command=ADD L7FILTER list_name=add_l7filter_list step_id=3.2 -->
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
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_fltbindflowf_list的变量区（command: ADD FLTBINDFLOWF） -#}
<!-- MISSING_MACRO: command=ADD FLTBINDFLOWF list_name=add_fltbindflowf_list step_id=5.1 -->
```

#### 5.2 将已配置的七层过滤条件、协议与流过滤器绑定。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_protbindflowf_list的变量区（command: ADD PROTBINDFLOWF） -#}
<!-- MISSING_MACRO: command=ADD PROTBINDFLOWF list_name=add_protbindflowf_list step_id=5.2 -->
```

### 6 添加规则，并与PCC策略组和流过滤器绑定。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_rule_list的变量区（command: ADD RULE） -#}
<!-- MISSING_MACRO: command=ADD RULE list_name=add_rule_list step_id=6 -->
```

### 7 添加User Profile。

```jinja2
{%- for item in add_userprofile_list -%}
    ADD USERPROFILE:
    {#- --- 必选参数 --- -#}
    USERPROFILENAME="{{item.USERPROFILENAME}}",
    UPTYPE={{item.UPTYPE}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：UPTYPE=PCC 时可选 --- -#}
    {%- if item.UPTYPE == 'PCC' -%}
        {%- if item.PROFILERANGE is not none -%}
            PROFILERANGE={{item.PROFILERANGE}},
        {%- endif -%}
    {%- endif -%}
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
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_urrgrpbinding_list的变量区（command: SET URRGRPBINDING） -#}
<!-- MISSING_MACRO: command=SET URRGRPBINDING list_name=set_urrgrpbinding_list step_id=9 -->
```

### 10 配置全局缺省URR组。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_spectrafurrgrp_list的变量区（command: SET SPECTRAFURRGRP） -#}
<!-- MISSING_MACRO: command=SET SPECTRAFURRGRP list_name=set_spectrafurrgrp_list step_id=10 -->
```

### 11 配置防欺诈URR列表。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_specurrgrplist_list的变量区（command: ADD SPECURRGRPLIST） -#}
<!-- MISSING_MACRO: command=ADD SPECURRGRPLIST list_name=add_specurrgrplist_list step_id=11 -->
```

### 12 将新配置的Filter置为生效。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_refreshsrv_list的变量区（command: SET REFRESHSRV） -#}
<!-- MISSING_MACRO: command=SET REFRESHSRV list_name=set_refreshsrv_list step_id=12 -->
```

