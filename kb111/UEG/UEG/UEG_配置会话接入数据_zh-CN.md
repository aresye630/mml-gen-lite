---
id: ''
name: 配置会话接入数据
ne_type: UEG
type: feature
description: 客户部署MEC本地分流或4G/5G互操作网络时，UEG作为UL CL UPF + 辅锚点UPF或者主锚点UPF时均需要配置会话接入数据，才能使用户完成激活流程并接入网络。
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝L”，入驻式）","UEG初始配置（风筝L）","参考：详细配置指导","配置UPF","配置会话接入数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools:
- getParameterValue('ADD UPPOOL')
---
<!-- @mml:block= annotations -->
```text
## 操作场景
客户部署MEC本地分流或4G/5G互操作网络时，UEG作为UL CL UPF + 辅锚点UPF或者主锚点UPF时均需要配置会话接入数据，才能使用户完成激活流程并接入网络。

## 必备事项
前提条件

* 请阅读并熟悉特性GWFD-020805 用户面地址分配。
* 请阅读并熟悉特性GWFD-023101 基于位置的地址分配。
* 具备管理员权限的操作人员已经登录华为操作维护系统（登录MAE客户端或登录OM Portal）。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_vpninst_list:
      type: items
      properties:
        VPNINSTANCE:
          name: 'VPN实例名'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '规划的VPN用于和APN绑定。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_upapn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: 'APN/DNN实例应该全网规划，UEG本端配置的APN/DNN实例应该与C面（SMF/SGW-C/PGW-C）配置的APN/DNN实例一致。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        HASVPN:
          name: '绑定VPN'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '业务APN绑定的VPN必须与UEG到PDN/DN互通的外联口绑定的VPN一致。  可使用**LST VPNINST**命令进行查询。'
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
        VPNINSTANCE:
          name: 'VPN实例名'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    set_apnsglpass_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '可执行**LST UPAPN**命令进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SWITCH:
          name: '开关标识'
          type: string
          enum:
          - PF_ACT_DISABLE
          - PF_ACT_ENABLE
          required: true
          description: '一般使用样例值即可。  对于一些特殊业务，例如NB-IoT解决方案中的抄表业务，只有上行流量，没有下行流量，则需要设置为“PF\_ACT\_DISABLE”，关闭对应APN的单通故障检测功能。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_uppool_list:
      type: items
      properties:
        POOLNAME:
          name: '地址池名称'
          type: string
          minLength: 1
          maxLength: 79
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        POOLTYPE:
          name: '地址池类型'
          type: string
          enum:
          - EXTERNAL
          - LOCAL
          required: false
          description: 'UEG作为主锚点UPF给UE分配IP地址时，该参数设置为“LOCAL”；其他网元给UE分配IP地址时，该参数设置为“EXTERNAL”。  UEG作为UL CL UPF + 辅锚点UPF时，该参数设置为“EXTERNAL”。'
          data_source: '本端规划'
          pattern: ''
          default: LOCAL
        HASVPN:
          name: '绑定VPN'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '如下三者绑定的VPN实例必须一致。   * 用户激活使用的APN绑定的VPN实例 * 地址池绑定的VPN实例 * 与PDN/DN连接的Gi/SGi/N6接口的外联口绑定的VPN实例'
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
        VPNINSTANCE:
          name: 'VPN实例名'
          type: string
          minLength: 1
          maxLength: 31
          required: false
          description: '可以使用**LST VPNINST**命令进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP地址类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: false
          description: '本地地址池支持IPv4和IPv6类型，如果规划UE IPv4v6双栈地址，则需要配置两种类型的地址池。'
          data_source: '本端规划'
          pattern: ''
          default: IPV4
    add_section_list:
      type: items
      properties:
        POOLNAME:
          name: '地址池名称'
          type: string
          minLength: 0
          maxLength: 79
          required: true
          description: '可以使用**LST UPPOOL**命令进行查询。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SECTIONNUM:
          name: '地址段号'
          type: integer
          minimum: 0
          maximum: 63
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP地址类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        V4STARTIP:
          name: '地址段的起始IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: '本地地址池支持IPv4和IPv6类型，如果规划UE IPv4v6双栈地址，则需要配置两种类型的地址池。  给用户分配的IP地址，不能与外联口IP或逻辑接口IP在同一网段。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        V4ENDIP:
          name: '地址段的终止IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        MASK:
          name: '掩码'
          type: integer
          minimum: 5
          maximum: 15
          required: false
          description: '开启上下行入不转板功能或下行入不转板功能时，需要规划“掩码（MASK）”参数。其他场景不需要规划。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_poolgroup_list:
      type: items
      properties:
        POOLGRPNAME:
          name: '地址池组名称'
          type: string
          minLength: 0
          maxLength: 79
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV4ALLOCPRIALG:
          name: 'IPV4基于地址池优先级分配地址算法'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '若使用IPv4地址池优先级功能，则必须使能本参数。'
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
        IPV6ALLOCPRIALG:
          name: 'IPV6基于地址池优先级分配地址算法'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '若使用IPv6地址池优先级功能，则必须使能本参数。'
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
    add_poolbindgroup_list:
      type: items
      properties:
        POOLGROUPNAME:
          name: '地址池组名称'
          type: string
          minLength: 0
          maxLength: 79
          required: true
          description: '可以使用**LST POOLGROUP**命令进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        POOLNAME:
          name: '地址池名称'
          type: string
          minLength: 0
          maxLength: 79
          required: true
          description: '可以使用**LST UPPOOL**命令进行查询。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 1
          maximum: 16
          required: false
          description: '地址池组下绑定多个地址池时，支持按地址池优先级分配地址。只有同类地址池之间才有优先级比较，不同类型的地址池间（IPv4和IPv6）没有优先级比较。'
          data_source: '本端规划'
          pattern: ''
          default: 16
    add_poolgrpmap_list:
      type: items
      properties:
        MAPPINGNAME:
          name: '映射规则名称'
          type: string
          minLength: 0
          maxLength: 79
          required: true
          description: '配置给指定APN/DNN下的用户分配地址时使用哪个地址池组中的IP地址。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        POOLGROUPNAME:
          name: '地址池组名称'
          type: string
          minLength: 0
          maxLength: 79
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    set_ipallocrule_list:
      type: items
      properties:
        FIRSTRULESW:
          name: '第一级规则开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '第一规则优先级默认使能。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        FIRSTRULE:
          name: '第一级规则'
          type: string
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SECONDRULESW:
          name: '第二级规则开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '第二规则优先级默认不使能。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        THIRDRULESW:
          name: '第三级规则开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '第三规则优先级默认不使能。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_uppool_list_1:
      type: items
      properties:
        POOLNAME:
          name: '地址池名称'
          type: string
          minLength: 1
          maxLength: 79
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        POOLTYPE:
          name: '地址池类型'
          type: string
          enum:
          - EXTERNAL
          - LOCAL
          required: false
          description: 'UEG作为主锚点UPF给UE分配IP地址时，该参数设置为“LOCAL”；其他网元给UE分配IP地址时，该参数设置为“EXTERNAL”。  UEG作为UL CL UPF + 辅锚点UPF时，该参数设置为“EXTERNAL”。'
          data_source: '本端规划'
          pattern: ''
          default: LOCAL
        IPVERSION:
          name: 'IP地址类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: false
          description: '本地地址池支持IPv4和IPv6类型，如果规划UE IPv4v6双栈地址，则需要配置两种类型的地址池。'
          data_source: '本端规划'
          pattern: ''
          default: IPV4
        CHECKIPVALID:
          name: '检查地址合法性'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        HASVPN:
          name: '绑定VPN'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '如下三者绑定的VPN实例必须一致。   * 用户激活使用的APN绑定的VPN实例 * 地址池绑定的VPN实例 * 与PDN/DN连接的Gi/SGi/N6接口的外联口绑定的VPN实例'
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
        VPNINSTANCE:
          name: 'VPN实例名'
          type: string
          minLength: 1
          maxLength: 31
          required: false
          description: '可以使用**LST VPNINST**命令进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        IMSSW:
          name: 'IMS开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ENABLE
        REDUNDFUNC:
          name: '冗余备份功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
    add_section_list_1:
      type: items
      properties:
        POOLNAME:
          name: '地址池名称'
          type: string
          minLength: 0
          maxLength: 79
          required: true
          description: '可以使用**LST UPPOOL**命令进行查询。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SECTIONNUM:
          name: '地址段号'
          type: integer
          minimum: 0
          maximum: 63
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP地址类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        V4STARTIP:
          name: '地址段的起始IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: '本地地址池支持IPv4和IPv6类型，如果规划UE IPv4v6双栈地址，则需要配置两种类型的地址池。  给用户分配的IP地址，不能与外联口IP或逻辑接口IP在同一网段。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        V4ENDIP:
          name: '地址段的终止IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        MASK:
          name: '掩码'
          type: integer
          minimum: 5
          maximum: 15
          required: false
          description: '开启上下行入不转板功能或下行入不转板功能时，需要规划“掩码（MASK）”参数。其他场景不需要规划。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_poolgroup_list_1:
      type: items
      properties:
        POOLGRPNAME:
          name: '地址池组名称'
          type: string
          minLength: 0
          maxLength: 79
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV4ALLOCPRIALG:
          name: 'IPV4基于地址池优先级分配地址算法'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '若使用IPv4地址池优先级功能，则必须使能本参数。'
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
        IPV6ALLOCPRIALG:
          name: 'IPV6基于地址池优先级分配地址算法'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '若使用IPv6地址池优先级功能，则必须使能本参数。'
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
    add_poolbindgroup_list_1:
      type: items
      properties:
        POOLGROUPNAME:
          name: '地址池组名称'
          type: string
          minLength: 0
          maxLength: 79
          required: true
          description: '可以使用**LST POOLGROUP**命令进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        POOLNAME:
          name: '地址池名称'
          type: string
          minLength: 0
          maxLength: 79
          required: true
          description: '可以使用**LST UPPOOL**命令进行查询。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 1
          maximum: 16
          required: false
          description: '地址池组下绑定多个地址池时，支持按地址池优先级分配地址。只有同类地址池之间才有优先级比较，不同类型的地址池间（IPv4和IPv6）没有优先级比较。'
          data_source: '本端规划'
          pattern: ''
          default: 16
    add_poolgrpmap_list_1:
      type: items
      properties:
        MAPPINGNAME:
          name: '映射规则名称'
          type: string
          minLength: 0
          maxLength: 79
          required: true
          description: '配置给指定APN/DNN下的用户分配地址时使用哪个地址池组中的IP地址。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        POOLGROUPNAME:
          name: '地址池组名称'
          type: string
          minLength: 0
          maxLength: 79
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_cpnodeid_list:
      type: items
      properties:
        CPNAME:
          name: 'SMF 名称'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: '该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CPNODEIDTYPE:
          name: 'CP NodeID 类型'
          type: string
          enum:
          - FQDN
          - IPV4
          - IPV6
          required: false
          description: 'CP NodeID类型支持IPV4、IPv6或FQDN。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4NODEID:
          name: 'IPv4地址类型的Node Id'
          type: string
          maxLength: 15
          required: false
          description: '“CPNODEIDTYPE”设置为“IPV4”时需要规划。  采用应急SMF的N4接口IP。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        LOCALEMERNODE:
          name: '本地应急接入节点'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: '规划的是应急SMF的NODE信息时，该参数必须设置为“TRUE”。  采用应急SMF的FQDN。'
          data_source: '本端规划'
          pattern: ''
          default: FALSE
    add_cpnodeid_list_1:
      type: items
      properties:
        CPNAME:
          name: 'SMF 名称'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: '该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CPNODEIDTYPE:
          name: 'CP NodeID 类型'
          type: string
          enum:
          - FQDN
          - IPV4
          - IPV6
          required: false
          description: 'CP NodeID类型支持IPV4、IPv6或FQDN。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV6NODEID:
          name: 'IPv6地址类型的Node Id'
          type: string
          maxLength: 39
          required: false
          description: '“CPNODEIDTYPE”设置为“IPV6”时需要规划。  采用应急SMF的N4接口IP。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        LOCALEMERNODE:
          name: '本地应急接入节点'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: '规划的是应急SMF的NODE信息时，该参数必须设置为“TRUE”。  采用应急SMF的FQDN。'
          data_source: '本端规划'
          pattern: ''
          default: FALSE
    add_cpnodeid_list_2:
      type: items
      properties:
        CPNAME:
          name: 'SMF 名称'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: '该参数不能重复。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CPNODEIDTYPE:
          name: 'CP NodeID 类型'
          type: string
          enum:
          - FQDN
          - IPV4
          - IPV6
          required: false
          description: 'CP NodeID类型支持IPV4、IPv6或FQDN。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        FQDNNODEID:
          name: 'FQDN类型的Node Id'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: '“CPNODEIDTYPE”设置为“FQDN”时需要规划。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        LOCALEMERNODE:
          name: '本地应急接入节点'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: '规划的是应急SMF的NODE信息时，该参数必须设置为“TRUE”。  采用应急SMF的FQDN。'
          data_source: '本端规划'
          pattern: ''
          default: FALSE
  examples:
    add_vpninst_list:
    - VPNINSTANCE: 'VPN_Internet'
    add_upapn_list:
    - APN: 'apn-op'
      HASVPN: ENABLE
      VPNINSTANCE: 'VPN_Internet'
    set_apnsglpass_list:
    - APN: 'apn-op'
      SWITCH: PF_ACT_ENABLE
    add_uppool_list:
    - POOLNAME: 'testpool'
      POOLTYPE: LOCAL
      HASVPN: ENABLE
      VPNINSTANCE: 'VPN_Internet'
      IPVERSION: IPV4
    add_section_list:
    - POOLNAME: 'testpool'
      SECTIONNUM: 1
      IPVERSION: IPV4
      V4STARTIP: '10.10.1.1'
      V4ENDIP: '10.10.1.254'
      MASK: 5
    add_poolgroup_list:
    - POOLGRPNAME: 'poolgroup1'
      IPV4ALLOCPRIALG: ENABLE
      IPV6ALLOCPRIALG: ENABLE
    add_poolbindgroup_list:
    - POOLGROUPNAME: 'poolgroup1'
      POOLNAME: 'testpool'
      PRIORITY: 10
    add_poolgrpmap_list:
    - MAPPINGNAME: 'mapping1'
      APN: 'apn-op'
      POOLGROUPNAME: 'poolgroup1'
    set_ipallocrule_list:
    - FIRSTRULESW: ENABLE
      FIRSTRULE: APN-1&LOCATION-0&SMF-0
      SECONDRULESW: DISABLE
      THIRDRULESW: DISABLE
    add_uppool_list_1:
    - POOLNAME: 'testpool'
      POOLTYPE: EXTERNAL
      IPVERSION: IPV4
      CHECKIPVALID: ENABLE
      HASVPN: ENABLE
      VPNINSTANCE: 'VPN_Internet'
      IMSSW: DISABLE
      REDUNDFUNC: ENABLE
    add_section_list_1:
    - POOLNAME: 'testpool'
      SECTIONNUM: 1
      IPVERSION: IPV4
      V4STARTIP: '10.10.1.1'
      V4ENDIP: '10.10.1.254'
      MASK: 5
    add_poolgroup_list_1:
    - POOLGRPNAME: 'poolgroup1'
      IPV4ALLOCPRIALG: ENABLE
      IPV6ALLOCPRIALG: ENABLE
    add_poolbindgroup_list_1:
    - POOLGROUPNAME: 'poolgroup1'
      POOLNAME: 'testpool'
      PRIORITY: 10
    add_poolgrpmap_list_1:
    - MAPPINGNAME: 'mapping1'
      APN: 'apn-op'
      POOLGROUPNAME: 'poolgroup1'
    add_cpnodeid_list:
    - CPNAME: 'smfnode1'
      CPNODEIDTYPE: IPV4
      IPV4NODEID: '10.0.0.1'
      LOCALEMERNODE: TRUE
    add_cpnodeid_list_1:
    - CPNAME: 'smfnode2'
      CPNODEIDTYPE: IPV6
      IPV6NODEID: 'FC00:0:0:0:10:0:0:1'
      LOCALEMERNODE: TRUE
    add_cpnodeid_list_2:
    - CPNAME: 'smfnode3'
      CPNODEIDTYPE: FQDN
      FQDNNODEID: 'consumer.huawei.com'
      LOCALEMERNODE: TRUE
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 配置APN实例。

```jinja2
{%- for item in add_vpninst_list -%}
    ADD VPNINST:
    {#- --- 必选参数 --- -#}
    VPNINSTANCE="{{item.VPNINSTANCE}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_upapn_list -%}
    ADD UPAPN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.HASVPN is not none -%}
        HASVPN={{item.HASVPN}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：HASVPN=ENABLE 时必选 --- -#}
    {%- if item.HASVPN == 'ENABLE' -%}
        VPNINSTANCE="{{item.VPNINSTANCE}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 业务APN绑定的VPN必须与UEG到PDN/DN互通的外联口绑定的VPN一致。

### 3 指定APN的用户存在上行数据和下行数据时，开启APN单通检测功能。

```jinja2
{%- for item in set_apnsglpass_list -%}
    SET APNSGLPASS:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 指定APN的用户只存在上行数据或只存在下行数据时，需设置为“DISABLE”，关闭APN单通检测功能。

### UEG作为主锚点且给UE分配IP地址时，请执行4，不需要执行5。

### UEG作为辅锚点 + UL CL UPF等非主锚点UPF或UEG作为主锚点UPF且外部NF给UE分配地址时，若采用动态路由发布用户下行路由，请执行5，不需要执行4；若采用静态路由方式时，则仅需在对端设备上配置到用户的下行路由，可不执行5。

### 4 （本地分配地址场景）UEG作为主锚点且给UE分配IP地址时，配置用户面分配地址。

#### 4.1 配置“LOCAL”类型地址池。

```jinja2
{%- if is_scenario_local_ip_allocation -%}
    {%- for item in add_uppool_list -%}
        ADD UPPOOL:
        {#- --- 必选参数 --- -#}
        POOLNAME="{{item.POOLNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.POOLTYPE is not none -%}
            POOLTYPE={{item.POOLTYPE}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：HASVPN=ENABLE 时必选 --- -#}
        {%- if item.HASVPN == 'ENABLE' -%}
            VPNINSTANCE="{{item.VPNINSTANCE}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：POOLTYPE=LOCAL/EXTERNAL 时可选 --- -#}
        {%- if item.POOLTYPE in ['LOCAL', 'EXTERNAL'] -%}
            {%- if item.HASVPN is not none -%}
                HASVPN={{item.HASVPN}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：POOLTYPE=LOCAL/EXTERNAL 时可选 --- -#}
        {%- if item.POOLTYPE in ['LOCAL', 'EXTERNAL'] -%}
            {%- if item.IPVERSION is not none -%}
                IPVERSION={{item.IPVERSION}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### UEG给UE分配IP地址时，“POOLTYPE”设置为“LOCAL”。

#### 4.2 配置地址池里的地址段。

```jinja2
{%- if is_scenario_local_ip_allocation -%}
    {%- for item in add_section_list -%}
        ADD SECTION:
        {#- --- 必选参数 --- -#}
        POOLNAME="{{item.POOLNAME}}",
        SECTIONNUM={{item.SECTIONNUM}},
        IPVERSION={{item.IPVERSION}},
        {#- --- 可选参数 --- -#}
        {%- if item.MASK is not none -%}
            MASK={{item.MASK}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
        {%- if item.IPVERSION == 'IPV4' -%}
            V4STARTIP="{{item.V4STARTIP}}",
        {%- endif -%}
        {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
        {%- if item.IPVERSION == 'IPV4' -%}
            V4ENDIP="{{item.V4ENDIP}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.3 配置地址池组。

```jinja2
{%- if is_scenario_local_ip_allocation -%}
    {%- for item in add_poolgroup_list -%}
        ADD POOLGROUP:
        {#- --- 必选参数 --- -#}
        POOLGRPNAME="{{item.POOLGRPNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.IPV4ALLOCPRIALG is not none -%}
            IPV4ALLOCPRIALG={{item.IPV4ALLOCPRIALG}},
        {%- endif -%}
        {%- if item.IPV6ALLOCPRIALG is not none -%}
            IPV6ALLOCPRIALG={{item.IPV6ALLOCPRIALG}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.4 配置地址池绑定到地址池组。

```jinja2
{%- if is_scenario_local_ip_allocation -%}
    {%- for item in add_poolbindgroup_list -%}
        ADD POOLBINDGROUP:
        {#- --- 必选参数 --- -#}
        POOLGROUPNAME="{{item.POOLGROUPNAME}}",
        POOLNAME="{{item.POOLNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.PRIORITY is not none -%}
            PRIORITY={{item.PRIORITY}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.5 配置APN/DNN实例与地址池组的映射关系。

```jinja2
{%- if is_scenario_local_ip_allocation -%}
    {%- for item in add_poolgrpmap_list -%}
        ADD POOLGRPMAP:
        {#- --- 必选参数 --- -#}
        MAPPINGNAME="{{item.MAPPINGNAME}}",
        POOLGROUPNAME="{{item.POOLGROUPNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.APN is not none -%}
            APN="{{item.APN}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 4.6 配置全局地址分配规则。

```jinja2
{%- if is_scenario_local_ip_allocation -%}
    {%- for item in set_ipallocrule_list -%}
        SET IPALLOCRULE:
        {#- --- 可选参数 --- -#}
        {%- if item.FIRSTRULESW is not none -%}
            FIRSTRULESW={{item.FIRSTRULESW}},
        {%- endif -%}
        {%- if item.SECONDRULESW is not none -%}
            SECONDRULESW={{item.SECONDRULESW}},
        {%- endif -%}
        {%- if item.THIRDRULESW is not none -%}
            THIRDRULESW={{item.THIRDRULESW}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：FIRSTRULESW=ENABLE 时必选 --- -#}
        {%- if item.FIRSTRULESW == 'ENABLE' -%}
            FIRSTRULE={{item.FIRSTRULE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 5 （外部分配地址场景）UEG作为辅锚点 + UL CL UPF等非主锚点UPF或UEG作为主锚点UPF且外部NF给UE分配地址时，配置地址池数据。

#### 5.1 配置“EXTERNAL”类型地址池。

```jinja2
{%- if is_scenario_external_ip_allocation -%}
    {%- for item in add_uppool_list_1 -%}
        ADD UPPOOL:
        {#- --- 必选参数 --- -#}
        POOLNAME="{{item.POOLNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.POOLTYPE is not none -%}
            POOLTYPE={{item.POOLTYPE}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：HASVPN=ENABLE 时必选 --- -#}
        {%- if item.HASVPN == 'ENABLE' -%}
            VPNINSTANCE="{{item.VPNINSTANCE}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：POOLTYPE=LOCAL/EXTERNAL 时可选 --- -#}
        {%- if item.POOLTYPE in ['LOCAL', 'EXTERNAL'] -%}
            {%- if item.IPVERSION is not none -%}
                IPVERSION={{item.IPVERSION}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：POOLTYPE=EXTERNAL 时可选 --- -#}
        {%- if item.POOLTYPE == 'EXTERNAL' -%}
            {%- if item.CHECKIPVALID is not none -%}
                CHECKIPVALID={{item.CHECKIPVALID}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：POOLTYPE=LOCAL/EXTERNAL 时可选 --- -#}
        {%- if item.POOLTYPE in ['LOCAL', 'EXTERNAL'] -%}
            {%- if item.HASVPN is not none -%}
                HASVPN={{item.HASVPN}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：POOLTYPE=LOCAL/EXTERNAL 时可选 --- -#}
        {%- if item.POOLTYPE in ['LOCAL', 'EXTERNAL'] -%}
            {%- if item.IMSSW is not none -%}
                IMSSW={{item.IMSSW}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：POOLTYPE=EXTERNAL 时可选 --- -#}
        {%- if item.POOLTYPE == 'EXTERNAL' -%}
            {%- if item.REDUNDFUNC is not none -%}
                REDUNDFUNC={{item.REDUNDFUNC}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### UDM等外部设备给UE分配IP地址时，“POOLTYPE”设置为“EXTERNAL”。

#### 5.2 配置地址池里的地址段。

```jinja2
{%- if is_scenario_external_ip_allocation -%}
    {%- for item in add_section_list_1 -%}
        ADD SECTION:
        {#- --- 必选参数 --- -#}
        POOLNAME="{{item.POOLNAME}}",
        SECTIONNUM={{item.SECTIONNUM}},
        IPVERSION={{item.IPVERSION}},
        {#- --- 可选参数 --- -#}
        {%- if item.MASK is not none -%}
            MASK={{item.MASK}},
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
        {%- if item.IPVERSION == 'IPV4' -%}
            V4STARTIP="{{item.V4STARTIP}}",
        {%- endif -%}
        {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
        {%- if item.IPVERSION == 'IPV4' -%}
            V4ENDIP="{{item.V4ENDIP}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### ADD UPPOOL命令中的“CHECKIPVALID”参数设置为“ENABLE”时，需要执行5.c~5.e，否则不需要。

#### 5.3 配置地址池组。

```jinja2
{%- set ADD_UPPOOL=getParameterValue('ADD UPPOOL') -%}
{%- if is_scenario_external_ip_allocation and ADD_UPPOOL -%}
    {%- for item in add_poolgroup_list_1 -%}
        ADD POOLGROUP:
        {#- --- 必选参数 --- -#}
        POOLGRPNAME="{{item.POOLGRPNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.IPV4ALLOCPRIALG is not none -%}
            IPV4ALLOCPRIALG={{item.IPV4ALLOCPRIALG}},
        {%- endif -%}
        {%- if item.IPV6ALLOCPRIALG is not none -%}
            IPV6ALLOCPRIALG={{item.IPV6ALLOCPRIALG}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 5.4 配置地址池绑定到地址池组。

```jinja2
{%- if is_scenario_external_ip_allocation and ADD_UPPOOL -%}
    {%- for item in add_poolbindgroup_list_1 -%}
        ADD POOLBINDGROUP:
        {#- --- 必选参数 --- -#}
        POOLGROUPNAME="{{item.POOLGROUPNAME}}",
        POOLNAME="{{item.POOLNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.PRIORITY is not none -%}
            PRIORITY={{item.PRIORITY}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 5.5 配置APN/DNN实例与地址池组的映射关系。

```jinja2
{%- if is_scenario_external_ip_allocation and ADD_UPPOOL -%}
    {%- for item in add_poolgrpmap_list_1 -%}
        ADD POOLGRPMAP:
        {#- --- 必选参数 --- -#}
        MAPPINGNAME="{{item.MAPPINGNAME}}",
        POOLGROUPNAME="{{item.POOLGROUPNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.APN is not none -%}
            APN="{{item.APN}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 6 **可选：**配置用户下行路由。

### UEG到PDN/DN的互通采用OSPF/OSPFv3动态路由方式时，到PDN/DN互通的外联口如已配置**ADD OSPFIMPORTROUTE**/**ADD OSPFV3IMPORTROUTE**且“PROTOCOL”设置为“wlr”，则表明已配置动态发布用户下行路由。

### UEG到PDN/DN的互通采用BGP over静态路由方式时，到PDN/DN互通的外联口如已配置**ADD IMPORTROUTE**且“PROTOCOL”设置为“wlr”，则表明已配置动态发布用户下行路由。

### UEG到PDN/DN的互通采用静态路由方式时，需要在对端设备上配置到用户的下行路由。在对端设备上配置的静态路由的目的地址和掩码对应UE IP所在网段，下一跳是每个ISU/IPU VMIPU上对应的外联口的IP。

### 7 （风筝L）配置应急SMF的NODE信息。

#### 7.1 //“CPNODEIDTYPE”设置为“IPV4”时：

```jinja2
{%- if is_scenario_kite_l and is_scenario_cpnodeidtype_ipv4 -%}
    {%- for item in add_cpnodeid_list -%}
        ADD CPNODEID:
        {#- --- 必选参数 --- -#}
        CPNAME="{{item.CPNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.CPNODEIDTYPE is not none -%}
            CPNODEIDTYPE={{item.CPNODEIDTYPE}},
        {%- endif -%}
        {%- if item.LOCALEMERNODE is not none -%}
            LOCALEMERNODE={{item.LOCALEMERNODE}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：CPNODEIDTYPE=IPV4 时可选 --- -#}
        {%- if item.CPNODEIDTYPE == 'IPV4' -%}
            {%- if item.IPV4NODEID is not none -%}
                IPV4NODEID="{{item.IPV4NODEID}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 7.2 //“CPNODEIDTYPE”设置为“IPV6”时：

```jinja2
{%- if is_scenario_kite_l and is_scenario_cpnodeidtype_ipv6 -%}
    {%- for item in add_cpnodeid_list_1 -%}
        ADD CPNODEID:
        {#- --- 必选参数 --- -#}
        CPNAME="{{item.CPNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.CPNODEIDTYPE is not none -%}
            CPNODEIDTYPE={{item.CPNODEIDTYPE}},
        {%- endif -%}
        {%- if item.LOCALEMERNODE is not none -%}
            LOCALEMERNODE={{item.LOCALEMERNODE}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：CPNODEIDTYPE=IPV6 时可选 --- -#}
        {%- if item.CPNODEIDTYPE == 'IPV6' -%}
            {%- if item.IPV6NODEID is not none -%}
                IPV6NODEID="{{item.IPV6NODEID}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 7.3 //“CPNODEIDTYPE”设置为“FQDN”时：

```jinja2
{%- if is_scenario_kite_l and is_scenario_cpnodeidtype_fqdn -%}
    {%- for item in add_cpnodeid_list_2 -%}
        ADD CPNODEID:
        {#- --- 必选参数 --- -#}
        CPNAME="{{item.CPNAME}}",
        {#- --- 可选参数 --- -#}
        {%- if item.CPNODEIDTYPE is not none -%}
            CPNODEIDTYPE={{item.CPNODEIDTYPE}},
        {%- endif -%}
        {%- if item.LOCALEMERNODE is not none -%}
            LOCALEMERNODE={{item.LOCALEMERNODE}},
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：CPNODEIDTYPE=FQDN 时可选 --- -#}
        {%- if item.CPNODEIDTYPE == 'FQDN' -%}
            {%- if item.FQDNNODEID is not none -%}
                FQDNNODEID="{{item.FQDNNODEID}}",
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

