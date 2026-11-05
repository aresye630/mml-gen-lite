---
id: ''
name: 配置内容计费
ne_type: UNC
type: feature
description: 用户访问园区业务时，智能分流SMF发起园区专网会话创建，数据流被分流到专网UPF上，需要在专网SMF和专网UPF上针对园区业务配置内容计费规则。  场景一：运营商对于园区业务未规划单独费率，则使用缺省费率（RG= 2000000002）。  场景二：运营商对于园区业务的费率有单独规划，按照运营商规划配置对应的费率。  此配置页面内容计费中的URR、PCCPOLICYGRPNM（PCC策略组名称）、RULENAME（规则名称）、USERPROFILENAME（用户模板名称）等需要与专网UPF和PCF中的名称保持一致。  UPF的相关配置参见配置内容计费，PCF的相关配置参见配置专用DNN策略数据。
risk_level: ''
doc_source: ["网络部署","业务专题","5G Core 一跳入家解决方案","一跳入家解决方案（基于3GPP接入方案）","业务初始部署与调测","部署移动VPN","配置专用DNN数据","配置SMF","配置内容计费"]
refs: []
metadata:
  DepOnLiveCfg: true
allowed-tools:
- getParameterValue('LST URRGROUP')
- getParameterValue('LST PCCPOLICYGRP')
- getParameterValue('LST RULE')
---
<!-- @mml:block=annotations -->
```text
## 操作场景
用户访问园区业务时，智能分流SMF发起园区专网会话创建，数据流被分流到专网UPF上，需要在专网SMF和专网UPF上针对园区业务配置内容计费规则。场景一：运营商对于园区业务未规划单独费率，则使用缺省费率（RG= 2000000002）。场景二：运营商对于园区业务的费率有单独规划，按照运营商规划配置对应的费率。此配置页面内容计费中的URR、PCCPOLICYGRPNM（PCC策略组名称）、RULENAME（规则名称）、USERPROFILENAME（用户模板名称）等需要与专网UPF和PCF中的名称保持一致。UPF的相关配置参见配置内容计费，PCF的相关配置参见配置专用DNN策略数据。

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
    add_urrgroup_list:
      type: items
      properties:
        URRGROUPNAME:
          name: '使用量上报规则组名称'
          type: string
          maxLength: 31
          required: true
          description: '内容计费规则：URR组。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPURRNAME1:
          name: '上行发起URR名称1'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        DOWNURRNAME1:
          name: '下行发起URR名称1'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPURRNAME2:
          name: '上行发起URR名称2'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        DOWNURRNAME2:
          name: '下行发起URR名称2'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        NOCHARGINGFLAG:
          name: '不计费标记'
          type: string
          enum:
          - DOWNLINK
          - NONE
          - UPLINK
          - UPLINK_DOWNLINK
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
          maxLength: 63
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        URRGROUPNAME:
          name: 'URR组名称'
          type: string
          maxLength: 31
          required: false
          description: '使用**ADD URRGROUP**命令定义的“URRGROUPNAME”。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        FUPSESSIONEXC:
          name: 'Session级FUP累计标识'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
    add_rule_list:
      type: items
      properties:
        RULENAME:
          name: '规则名称'
          type: string
          maxLength: 63
          required: true
          description: 'SMF配置的Rule名称需要和UPF配置的Rule名称一致，且与PCF下发的PCC规则保持一致。'
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
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PRIORITY:
          name: '全局优先级'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
          description: 'Rule优先级需要和UPF的 Rule优先级一致，'
          data_source: '本端规划'
          pattern: ''
          default: 4294967295
        POLICYNAME:
          name: '策略名称'
          type: string
          maxLength: 63
          required: false
          description: '使用**ADD URRGROUP**命令定义的“URRGROUPNAME”。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PROTODESCDL:
          name: '下行协议描述参数'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PROTODESCUL:
          name: '上行协议描述参数'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RULERANGE:
          name: '规则生效范围'
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
    add_userprofile_list:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          maxLength: 63
          required: true
          description: 'PCF下发的PCC规则需要和SMF、UPF上配置UserProfileName的一致。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        FREESERONLCHG:
          name: '免费业务在线计费标识'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ENABLE
        FREESEROFFCHG:
          name: '免费业务离线计费标识'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ENABLE
        UPTYPE:
          name: '用户模板类型'
          type: string
          enum:
          - PCC
          - ULCL
          - UPSELECT
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: PCC
        FREESERCVGCHG:
          name: '免费业务融合计费标识'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ENABLE
        FREEONLFLAGSW:
          name: '免费在线业务携带在线相关标识开关'
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
          description: '使用**ADD USERPROFILE**令定义的“USERPROFILENAME”。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        RULENAME:
          name: '规则名称'
          type: string
          maxLength: 63
          required: true
          description: '使用**ADD RULE**令定义的“RULENAME”。'
          data_source: '本端规划'
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
          description: '该命令配置一个URR规则，同一个RG对在线计费需要配置在线计费的URR ID，对离线计费需要配置离线计费的URR ID。  同一个RG对应的在线、离线计费URR ID取值必须不同。可以按照在线计费URRID=RG，离线计费URRID=RG+10000做映射。'
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
        ONLCOMPOUNDTYPE:
          name: '在线计费标识组成类型'
          type: string
          enum:
          - ONLYRG
          - RGSID
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ONLINERG:
          name: '在线计费组'
          type: integer
          minimum: 0
          maximum: 4294967294
          required: false
          description: ''
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
          data_source: '全网规划'
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
          data_source: '全网规划'
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
          data_source: '全网规划'
          pattern: ''
          default: ''
        DOWNSID:
          name: '离线下行业务标识'
          type: integer
          minimum: 0
          maximum: 4294967294
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SID:
          name: '离线业务标识'
          type: integer
          minimum: 0
          maximum: 4294967294
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        UPSID:
          name: '离线上行业务标识'
          type: integer
          minimum: 0
          maximum: 4294967294
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ONLINESID:
          name: '在线业务标识'
          type: integer
          minimum: 0
          maximum: 4294967294
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
          description: '该命令配置一个URR组。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPURRNAME1:
          name: '上行发起URR名称1'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        DOWNURRNAME1:
          name: '下行发起URR名称1'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPURRNAME2:
          name: '上行发起URR名称2'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        DOWNURRNAME2:
          name: '下行发起URR名称2'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_pccpolicygrp_list_1:
      type: items
      properties:
        PCCPOLICYGRPNM:
          name: 'PCC策略组名称'
          type: string
          maxLength: 63
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        URRGROUPNAME:
          name: 'URR组名称'
          type: string
          maxLength: 31
          required: false
          description: '使用**ADD URRGROUP**命令定义的“URRGROUPNAME”。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_rule_list_2:
      type: items
      properties:
        RULENAME:
          name: '规则名称'
          type: string
          maxLength: 63
          required: true
          description: 'SMF配置的Rule名称需要和UPF配置的Rule名称一致，且与PCF下发的PCC规则保持一致。'
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
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PRIORITY:
          name: '全局优先级'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: false
          description: 'Rule优先级需要和UPF的 Rule优先级一致，'
          data_source: '本端规划'
          pattern: ''
          default: 4294967295
        POLICYNAME:
          name: '策略名称'
          type: string
          maxLength: 63
          required: false
          description: '使用**ADD URRGROUP**命令定义的“URRGROUPNAME”。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        FLOWFILTERNAME:
          name: '流过滤器名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PROTODESCDL:
          name: '下行协议描述参数'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PROTODESCUL:
          name: '上行协议描述参数'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RULERANGE:
          name: '规则生效范围'
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
    add_userprofile_list_1:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          maxLength: 63
          required: true
          description: 'PCF下发的PCC规则需要和SMF、UPF上配置UserProfileName的一致。'
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
          data_source: '全网规划'
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
    add_rulebinding_list_2:
      type: items
      properties:
        USERPROFILENAME:
          name: '用户模板名称'
          type: string
          maxLength: 63
          required: true
          description: '使用**ADD USERPROFILE**令定义的“USERPROFILENAME”。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        RULENAME:
          name: '规则名称'
          type: string
          maxLength: 63
          required: true
          description: '使用**ADD RULE**令定义的“RULENAME”。'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    add_urrgroup_list:
    - URRGROUPNAME: 'common_01_ch_p'
      UPURRNAME1: 'common_01_cbb_online'
      DOWNURRNAME1: 'common_01_cbb_online'
      UPURRNAME2: 'common_01_cbb_offline'
      DOWNURRNAME2: 'common_01_cbb_offline'
      NOCHARGINGFLAG: NONE
    add_pccpolicygrp_list:
    - PCCPOLICYGRPNM: 'common_01_pcc_p_g'
      URRGROUPNAME: 'common_01_ch_p'
      FUPSESSIONEXC: DISABLE
    add_rule_list:
    - RULENAME: 'common_any'
      POLICYTYPE: PCC
      PRIORITY: 65000
      POLICYNAME: 'common_01_pcc_p_g'
      FLOWFILTERNAME: ''
      PROTODESCDL: ''
      PROTODESCUL: ''
      RULERANGE: ALL
    add_userprofile_list:
    - USERPROFILENAME: 'u_p_multi_default'
      FREESERONLCHG: ENABLE
      FREESEROFFCHG: ENABLE
      UPTYPE: PCC
      FREESERCVGCHG: ENABLE
      FREEONLFLAGSW: INHERIT
      PROFILERANGE: ALL
    add_rulebinding_list:
    - USERPROFILENAME: 'u_p_multi_default'
      RULENAME: 'common_any'
    add_urr_list:
    - URRNAME: 'multi_01_cbb_online'
      URRID: 2000000003
      USAGERPTMODE: ONLINE
      ONLCOMPOUNDTYPE: ONLYRG
      ONLINERG: 2000000003
      ONLMETERINGTYPE: VOLUME
      OFFCOMPOUNDTYPE: ONLYRG
      RG: 2000000003
      OFFMETERINGTYPE: VOLUME
      DOWNSID: ''
      SID: ''
      UPSID: ''
      ONLINESID: ''
      EVENTRSUVALUE: ''
      TIMERSUVALUE: ''
      VOLUMERSUVALUE: ''
      MONITORINGKEY: ''
      N40AGESW: ENABLE
      OFCSRVTMPLNAME: ''
      REDIRENDTOKEN: ''
    add_urrgroup_list_1:
    - URRGROUPNAME: 'multi_01_ch_p'
      UPURRNAME1: 'multi_01_cbb_online'
      DOWNURRNAME1: 'multi_01_cbb_online'
      UPURRNAME2: 'multi_01_cbb_offline'
      DOWNURRNAME2: 'multi_01_cbb_offline'
    add_pccpolicygrp_list_1:
    - PCCPOLICYGRPNM: 'multi_01_pcc_p_g'
      URRGROUPNAME: 'multi_01_ch_p'
    add_rule_list_2:
    - RULENAME: 'multi_01_r'
      POLICYTYPE: PCC
      PRIORITY: 60000
      POLICYNAME: 'multi_01_pcc_p_g'
      FLOWFILTERNAME: ''
      PROTODESCDL: ''
      PROTODESCUL: ''
      RULERANGE: ALL
    add_userprofile_list_1:
    - USERPROFILENAME: 'u_p_01_multi'
      UPTYPE: PCC
      PROFILERANGE: ALL
    add_rulebinding_list_2:
    - USERPROFILENAME: 'u_p_01_multi'
      RULENAME: 'multi_01_r'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 任务一： 园区业务未规划单独费率，使用缺省费率。

#### 1.1 假设5GC设备使用common\_01\_cbb\_online和common\_01\_cbb\_offline两个URR作为使用量上报规则，执行LST URR:URRNAME="common\_01\_cbb\_online";和LST URR:URRNAME="common\_01\_cbb\_offline";命令查询设备是否已经配置缺省费率。如下，查询的结果中若包含如下红色字体，则说明已经配置缺省费率（部分省份可能使用的URRNAME稍有差异，可以在配置中搜索RG=2000000002，找到对应的缺省费率规则组）。

#### %%LST URR:URRNAME="common_01_cbb_online";%%

#### RETCODE = 0  操作成功

#### 使用量上报规则信息：

#### --------------------

#### 使用量上报规则名称  =  common_01_cbb_online

#### URR标识  =  2000000002

#### 使用量上报模式  =  在线计费

#### 离线计费标识组成类型  =  费率组

#### 离线计费组  =  4294967295

#### 离线业务标识  =  4294967295

#### 离线上行业务标识  =  4294967295

#### 离线下行业务标识  =  4294967295

#### 离线计费统计类型  =  流量

#### 离线业务模板名  =  NULL

#### 在线计费标识组成类型  =  费率组

#### 在线计费组  =  2000000002

#### 在线业务标识  =  4294967295

#### 在线计费统计类型  =  流量

#### 流量配额值（字节）  =  0

#### 时间配额值（秒）  =  0

#### Gy重定向结束Token  =  NULL

#### 监控属性值  =  NULL

#### 事件配额值（次）  =  0

#### (结果个数 = 1)

#### ---    END

#### %%LST URR:URRNAME="common_01_cbb_offline";%%

#### RETCODE = 0  操作成功

#### 使用量上报规则信息：

#### --------------------

#### 使用量上报规则名称  =  common_01_cbb_offline

#### URR标识  =  2000010002

#### 使用量上报模式  =  离线计费

#### 离线计费标识组成类型  =  费率组

#### 离线计费组  =  2000000002

#### 离线业务标识  =  4294967295

#### 离线上行业务标识  =  4294967295

#### 离线下行业务标识  =  4294967295

#### 离线计费统计类型  =  流量

#### 离线业务模板名  =  NULL

#### 在线计费标识组成类型  =  费率组

#### 在线计费组  =  4294967295

#### 在线业务标识  =  4294967295

#### 在线计费统计类型  =  流量

#### 流量配额值（字节）  =  0

#### 时间配额值（秒）  =  0

#### Gy重定向结束Token  =  NULL

#### 监控属性值  =  NULL

#### 事件配额值（次）  =  0

#### (结果个数 = 1)

#### ---    END

#### 1.2 配置缺省计费规则/用户模板。

##### 1.2.1 场景一：当PCF下缺省内容计费对应的规则时，请执行以下脚本：

###### 1.2.1.1 一般会使用common\_01\_ch\_p作为缺省费率的URRGROUP，使用LST URRGROUP:URRGROUPNAME="common\_01\_ch\_p";命令查询。

###### %%LST URRGROUP:URRGROUPNAME="common_01_ch_p";%%

###### RETCODE = 0  操作成功

###### URR组信息：

###### -----------

###### 使用量上报规则组名称  =  common_01_ch_p上行发起URR名称1  =  common_01_cbb_online上行发起URR名称2  =  common_01_cbb_offline

###### 上行发起URR名称3  =  NULL

###### 下行发起URR名称1  =  common_01_cbb_online下行发起URR名称2  =  common_01_cbb_offline

###### 下行发起URR名称3  =  NULL

###### 不计费标记  =  无

###### (结果个数 = 1)

###### ---    END

###### 若无查询结果，则执行以下命令添加对应的URRGROUP。

```jinja2
{%- set LST_URRGROUP=getParameterValue('LST URRGROUP') -%}
{%- if is_scenario_default_rate and is_scenario_pcf_rule and LST_URRGROUP=='' -%}
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
        {%- if item.NOCHARGINGFLAG is not none -%}
            NOCHARGINGFLAG={{item.NOCHARGINGFLAG}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

###### 1.2.1.2 一般会使用common\_01\_pcc\_p\_g"作为缺省费率的PCCPOLICYGRP，使用LST PCCPOLICYGRP:PCCPOLICYGRPNM="common\_01\_pcc\_p\_g";命令查询。

###### %%LST PCCPOLICYGRP:PCCPOLICYGRPNM="common_01_pcc_p_g";%%

###### RETCODE = 0  操作成功

###### PCC策略组信息

###### PCC策略组名称  =  common_01_pcc_p_g使用量上报规则组名称  =  common_01_ch_p

###### QoS属性名称  =  NULL

###### Session级FUP累计标识  =  不使能

###### (结果个数 = 1)

###### 若无查询结果，则执行以下命令添加对应的PCCPOLICYGRP。

```jinja2
{%- set LST_PCCPOLICYGRP=getParameterValue('LST PCCPOLICYGRP') -%}
{%- if is_scenario_default_rate and is_scenario_pcf_rule and LST_PCCPOLICYGRP=='' -%}
    {%- for item in add_pccpolicygrp_list -%}
        ADD PCCPOLICYGRP:
        {#- --- 必选参数 --- -#}
        PCCPOLICYGRPNM="{{item.PCCPOLICYGRPNM}}",
        {#- --- 可选参数 --- -#}
        {%- if item.URRGROUPNAME is not none -%}
            URRGROUPNAME="{{item.URRGROUPNAME}}",
        {%- endif -%}
        {%- if item.FUPSESSIONEXC is not none -%}
            FUPSESSIONEXC={{item.FUPSESSIONEXC}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

###### 1.2.1.3 一般会使用common\_any和common\_any\_ipv6\_r作为兜底的计费规则，使用LST RULE:RULENAME="common\_any";和LST RULE:RULENAME="common\_any\_ipv6\_r";命令查询。

###### %%LST RULE:RULENAME="common_any";%%

###### RETCODE = 0  操作成功

###### 规则信息

###### 规则名称  =  common_any

###### 全局优先级  =  65000

###### 策略类型  =  PCC

###### 策略名称  =  common_01_pcc_p_g

###### 流过滤器名称  =  NULL

###### (结果个数 = 1)

###### %%LST RULE:RULENAME="common_any_ipv6_r";%%

###### RETCODE = 0  操作成功

###### 规则信息

###### 规则名称  =  common_any_ipv6_r

###### 全局优先级  =  65010

###### 策略类型  =  PCC

###### 策略名称  =  common_01_pcc_p_g

###### 流过滤器名称  =  NULL

###### (结果个数 = 1)

###### 若无查询结果，则执行以下命令添加兜底的计费规则。SMF、UPF上RULENAME以及RULE下配置的POLICYTYPE、POLICYNAME需要保持一致。

```jinja2
{%- set LST_RULE=getParameterValue('LST RULE') -%}
{%- if is_scenario_default_rate and is_scenario_pcf_rule and LST_RULE=='' -%}
    {%- for item in add_rule_list -%}
        ADD RULE:
        {#- --- 必选参数 --- -#}
        RULENAME="{{item.RULENAME}}",
        POLICYTYPE={{item.POLICYTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.PRIORITY is not none -%}
            PRIORITY={{item.PRIORITY}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：POLICYTYPE=PCC/ULCL/QOS 时必选 --- -#}
        {%- if item.POLICYTYPE in ['PCC', 'ULCL', 'QOS'] -%}
            POLICYNAME="{{item.POLICYNAME}}",
        {%- endif -%}
        {#- --- 条件必选：POLICYTYPE=ULCL 时必选 --- -#}
        {%- if item.POLICYTYPE == 'ULCL' -%}
            FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：POLICYTYPE=PCC/QOS 时可选 --- -#}
        {%- if item.POLICYTYPE in ['PCC', 'QOS'] -%}
            {%- if item.PROTODESCDL is not none -%}
                PROTODESCDL="{{item.PROTODESCDL}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：POLICYTYPE=PCC/QOS 时可选 --- -#}
        {%- if item.POLICYTYPE in ['PCC', 'QOS'] -%}
            {%- if item.PROTODESCUL is not none -%}
                PROTODESCUL="{{item.PROTODESCUL}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：POLICYTYPE=PCC/QOS 时可选 --- -#}
        {%- if item.POLICYTYPE in ['PCC', 'QOS'] -%}
            {%- if item.RULERANGE is not none -%}
                RULERANGE={{item.RULERANGE}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 1.2.2 场景二：当PCF下缺省的内容计费对应的用户模板时，添加园区缺省计费规则对应的UserProfile。USERPROFILE的名称统一规划，保证在PCF、SMF、UPF间名称一致。不一致时PCF下发的策略无法生效。

```jinja2
{%- if is_scenario_default_rate and is_scenario_pcf_userprofile -%}
    {%- for item in add_userprofile_list -%}
        ADD USERPROFILE:
        {#- --- 必选参数 --- -#}
        USERPROFILENAME="{{item.USERPROFILENAME}}",
        UPTYPE={{item.UPTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.FREESERONLCHG is not none -%}
            FREESERONLCHG={{item.FREESERONLCHG}},
        {%- endif -%}
        {%- if item.FREESEROFFCHG is not none -%}
            FREESEROFFCHG={{item.FREESEROFFCHG}},
        {%- endif -%}
        {%- if item.FREESERCVGCHG is not none -%}
            FREESERCVGCHG={{item.FREESERCVGCHG}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：FREESERCVGCHG=ENABLE 时可选 --- -#}
        {%- if item.FREESERCVGCHG == 'ENABLE' -%}
            {%- if item.FREEONLFLAGSW is not none -%}
                FREEONLFLAGSW={{item.FREEONLFLAGSW}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：UPTYPE=PCC 时可选 --- -#}
        {%- if item.UPTYPE == 'PCC' -%}
            {%- if item.PROFILERANGE is not none -%}
                PROFILERANGE={{item.PROFILERANGE}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 当PCF同时下发园区业务内容计费对应的规则及用户模板时，以上脚本均需要执行。

#### 1.3 （条件必选）当同时配置了步骤2中的场景一和场景二时，需要执行此步骤。配置园区业务使用的Rule和园区业务的User Profile绑定关系。如果配置需要和UPF上配置的UserProfile的名称保持一致。

```jinja2
{%- if is_scenario_default_rate and is_scenario_pcf_rule and is_scenario_pcf_userprofile -%}
    {%- for item in add_rulebinding_list -%}
        ADD RULEBINDING:
        {#- --- 必选参数 --- -#}
        USERPROFILENAME="{{item.USERPROFILENAME}}",
        RULENAME="{{item.RULENAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

### 2 任务二： 园区业务规划单独费率，以2000000003为例进行配置。

#### 2.1 配置园区业务对应的URR。以下脚本假设园区费率为2000000003为例进行配置。

```jinja2
{%- if is_scenario_planned_rate -%}
    {%- for item in add_urr_list -%}
        ADD URR:
        {#- --- 必选参数 --- -#}
        URRNAME="{{item.URRNAME}}",
        URRID={{item.URRID}},
        USAGERPTMODE={{item.USAGERPTMODE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：USAGERPTMODE=ONLINE 时必选 --- -#}
        {%- if item.USAGERPTMODE == 'ONLINE' -%}
            ONLCOMPOUNDTYPE={{item.ONLCOMPOUNDTYPE}},
        {%- endif -%}
        {#- --- 条件必选：ONLCOMPOUNDTYPE=RGSID/ONLYRG 时必选 --- -#}
        {%- if item.ONLCOMPOUNDTYPE in ['RGSID', 'ONLYRG'] -%}
            ONLINERG={{item.ONLINERG}},
        {%- endif -%}
        {#- --- 条件必选：USAGERPTMODE=OFFLINE 时必选 --- -#}
        {%- if item.USAGERPTMODE == 'OFFLINE' -%}
            OFFCOMPOUNDTYPE={{item.OFFCOMPOUNDTYPE}},
        {%- endif -%}
        {#- --- 条件必选：OFFCOMPOUNDTYPE=ONLYRG/RGSID 时必选 --- -#}
        {%- if item.OFFCOMPOUNDTYPE in ['ONLYRG', 'RGSID'] -%}
            RG={{item.RG}},
        {%- endif -%}
        {#- --- 条件必选：OFFCOMPOUNDTYPE=UPDOWNSID 时必选 --- -#}
        {%- if item.OFFCOMPOUNDTYPE == 'UPDOWNSID' -%}
            DOWNSID={{item.DOWNSID}},
        {%- endif -%}
        {#- --- 条件必选：USAGERPTMODE=MONITORINGKEY 时必选 --- -#}
        {%- if item.USAGERPTMODE == 'MONITORINGKEY' -%}
            MONITORINGKEY="{{item.MONITORINGKEY}}",
        {%- endif -%}
        {#- --- 条件必选：ONLCOMPOUNDTYPE=RGSID 时必选 --- -#}
        {%- if item.ONLCOMPOUNDTYPE == 'RGSID' -%}
            ONLINESID={{item.ONLINESID}},
        {%- endif -%}
        {#- --- 条件必选：OFFCOMPOUNDTYPE=ONLYSID/RGSID 时必选 --- -#}
        {%- if item.OFFCOMPOUNDTYPE in ['ONLYSID', 'RGSID'] -%}
            SID={{item.SID}},
        {%- endif -%}
        {#- --- 条件必选：OFFCOMPOUNDTYPE=UPDOWNSID 时必选 --- -#}
        {%- if item.OFFCOMPOUNDTYPE == 'UPDOWNSID' -%}
            UPSID={{item.UPSID}},
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

#### 2.2 配置园区计费规则/用户模板。

##### 2.2.1 场景一：当PCF下发园区业务内容计费对应的规则时，请执行以下脚本：

###### 2.2.1.1 配置园区业务流量对应URR Group。

```jinja2
{%- if is_scenario_planned_rate and is_scenario_pcf_rule -%}
    {%- for item in add_urrgroup_list_1 -%}
        ADD URRGROUP:
        {#- --- 必选参数 --- -#}
        URRGROUPNAME="{{item.URRGROUPNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.UPURRNAME1 is not none -%}
            UPURRNAME1="{{item.UPURRNAME1}}",
        {%- endif -%}
        {%- if item.UPURRNAME2 is not none -%}
            UPURRNAME2="{{item.UPURRNAME2}}",
        {%- endif -%}
        {%- if item.DOWNURRNAME1 is not none -%}
            DOWNURRNAME1="{{item.DOWNURRNAME1}}",
        {%- endif -%}
        {%- if item.DOWNURRNAME2 is not none -%}
            DOWNURRNAME2="{{item.DOWNURRNAME2}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

###### 2.2.1.2 配置园区业务内容计费规则对应的PCC策略组名并和URR Group绑定。

```jinja2
{%- if is_scenario_planned_rate and is_scenario_pcf_rule -%}
    {%- for item in add_pccpolicygrp_list_1 -%}
        ADD PCCPOLICYGRP:
        {#- --- 必选参数 --- -#}
        PCCPOLICYGRPNM="{{item.PCCPOLICYGRPNM}}",
        {#- --- 可选参数 --- -#}
        {%- if item.URRGROUPNAME is not none -%}
            URRGROUPNAME="{{item.URRGROUPNAME}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

###### 2.2.1.3 配置园区业务内容计费对应的Rule。SMF、UPF上RULENAME以及RULE下配置的POLICYTYPE、POLICYNAME需要保持一致。

```jinja2
{%- if is_scenario_planned_rate and is_scenario_pcf_rule -%}
    {%- for item in add_rule_list_2 -%}
        ADD RULE:
        {#- --- 必选参数 --- -#}
        RULENAME="{{item.RULENAME}}",
        POLICYTYPE={{item.POLICYTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.PRIORITY is not none -%}
            PRIORITY={{item.PRIORITY}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：POLICYTYPE=PCC/ULCL/QOS 时必选 --- -#}
        {%- if item.POLICYTYPE in ['PCC', 'ULCL', 'QOS'] -%}
            POLICYNAME="{{item.POLICYNAME}}",
        {%- endif -%}
        {#- --- 条件必选：POLICYTYPE=ULCL 时必选 --- -#}
        {%- if item.POLICYTYPE == 'ULCL' -%}
            FLOWFILTERNAME="{{item.FLOWFILTERNAME}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：POLICYTYPE=PCC/QOS 时可选 --- -#}
        {%- if item.POLICYTYPE in ['PCC', 'QOS'] -%}
            {%- if item.PROTODESCDL is not none -%}
                PROTODESCDL="{{item.PROTODESCDL}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：POLICYTYPE=PCC/QOS 时可选 --- -#}
        {%- if item.POLICYTYPE in ['PCC', 'QOS'] -%}
            {%- if item.PROTODESCUL is not none -%}
                PROTODESCUL="{{item.PROTODESCUL}}",
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：POLICYTYPE=PCC/QOS 时可选 --- -#}
        {%- if item.POLICYTYPE in ['PCC', 'QOS'] -%}
            {%- if item.RULERANGE is not none -%}
                RULERANGE={{item.RULERANGE}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 2.2.2 场景二：当PCF下发园区业务内容计费对应的用户模板时，添加园区业务内容计费对应的UserProfile。USERPROFILE的名称统一规划，保证在PCF、SMF、UPF间名称一致。不一致时PCF下发的策略无法生效。

```jinja2
{%- if is_scenario_planned_rate and is_scenario_pcf_userprofile -%}
    {%- for item in add_userprofile_list_1 -%}
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
{%- endif -%}
```

##### 当PCF同时下发园区业务内容计费对应的规则及用户模板时，以上脚本均需要执行。

#### 2.3 （条件必选）当同时配置了步骤2中的场景一和场景二时，需要执行此步骤。配置园区业务使用的Rule和园区业务的UserProfile绑定关系。如果配置需要和UPF上配置的UserProfile的名称保持一致。

```jinja2
{%- if is_scenario_planned_rate and is_scenario_pcf_rule and is_scenario_pcf_userprofile -%}
    {%- for item in add_rulebinding_list_2 -%}
        ADD RULEBINDING:
        {#- --- 必选参数 --- -#}
        USERPROFILENAME="{{item.USERPROFILENAME}}",
        RULENAME="{{item.RULENAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

