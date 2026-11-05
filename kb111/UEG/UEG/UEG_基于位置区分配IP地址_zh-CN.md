---
id: ''
name: 基于位置区分配IP地址
ne_type: UEG
type: feature
description: 运营商规划UPF为UE分配IP地址，可基于APN/DNN、位置、SMF或其任意组合分配地址，基于位置区分配IP地址的配置方法可参考本章节。  适用于GGSN、PGW-C、SMF、PGW-U、UPF。
tags: []
risk_level: ''
doc_source: ["业务配置","公共业务","MEC 用户IP地址管理（公共）","UPF分配IP地址","激活UPF分配IP地址功能","基于位置区分配IP地址"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
运营商规划UPF为UE分配IP地址，可基于APN/DNN、位置、SMF或其任意组合分配地址，基于位置区分配IP地址的配置方法可参考本章节。适用于GGSN、PGW-C、SMF、PGW-U、UPF。

## 必备事项
前提条件

请仔细阅读UPF分配IP地址流程。
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
          name: 'VPN实例'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '此处绑定的VPN实例与业务APN/DNN绑定的VPN实例一致。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_apn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: 'APN/DNN实例应该全网规划，UPF本端配置的APN/DNN实例应该与SMF配置的APN/DNN实例一致。'
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
          description: '如下三者绑定的VPN实例必须一致。  + 地址池绑定的VPN实例 + 用户激活使用的APN/DNN绑定的VPN实例 + 与PDN/DN连接的Gi/SGi/N6接口的外联口绑定的VPN实例'
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
        VPNINSTANCE:
          name: 'VPN实例名'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '可以使用**LST VPNINST**命令进行查询。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_apnaddressattr_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '已通过**ADD APN**命令配置，可以使用**LST APN**命令进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        SUPPORTIPV4:
          name: '支持IPV4'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '配置指定APN/DNN是否支持IPV4地址。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SUPPORTIPV6:
          name: '支持IPV6'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '配置指定APN/DNN是否支持IPV6地址。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_pool_list:
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
          description: '-'
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
          description: '如下三者绑定的VPN实例必须一致。  + 用户激活使用的APN/DNN绑定的VPN实例 + 地址池绑定的VPN实例 + 与PDN/DN连接的Gi/SGi/N6接口的外联口绑定的VPN实例'
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
    add_section_list:
      type: items
      properties:
        POOLNAME:
          name: '地址池名称'
          type: string
          minLength: 0
          maxLength: 79
          required: true
          description: '可以使用**LST POOL**命令进行查询。'
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
          description: '本地地址池支持IPv4和IPv6类型，如果规划UE IPv4v6双栈地址，则需要配置两种类型的地址池。'
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
          description: '可以使用**LST POOL**命令进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_conflictip_list:
      type: items
      properties:
        POOLNAME:
          name: '地址池名称'
          type: string
          minLength: 0
          maxLength: 79
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPADDRESS:
          name: '冲突IPv4地址'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
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
    set_ipallocbylocglbsw_list:
      type: items
      properties:
        SWITCH:
          name: 'IPv4 开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6SWITCH:
          name: 'IPv6 开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_ipallocbylocsw_list:
      type: items
      properties:
        LOCATIONGRPTYPE:
          name: '位置区组类型'
          type: string
          enum:
          - LAC
          - TAC
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCATIONGRPNAME:
          name: '位置区组名称'
          type: string
          minLength: 0
          maxLength: 32
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_tacgroup_list:
      type: items
      properties:
        TACGROUPNAME:
          name: '指定TAC组名'
          type: string
          minLength: 0
          maxLength: 32
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_s1tacid_list:
      type: items
      properties:
        TACGROUPNAME:
          name: '指定S1TAC组名'
          type: string
          minLength: 0
          maxLength: 32
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TACSECNUM:
          name: 'S1Tac 段编号'
          type: integer
          minimum: 0
          maximum: 15999
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TACSTARTID:
          name: 'S1Tac 起始ID'
          type: string
          minLength: 0
          maxLength: 6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TACENDID:
          name: 'S1TAC截止ID'
          type: string
          minLength: 0
          maxLength: 6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_n2tacid_list:
      type: items
      properties:
        TACGROUPNAME:
          name: '指定N2TAC组名'
          type: string
          minLength: 0
          maxLength: 32
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TACSECNUM:
          name: 'N2Tac 段编号'
          type: integer
          minimum: 0
          maximum: 15999
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TACSTARTID:
          name: 'N2Tac 起始ID'
          type: string
          minLength: 0
          maxLength: 8
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TACENDID:
          name: 'N2TAC截止ID'
          type: string
          minLength: 0
          maxLength: 8
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_lacgroup_list:
      type: items
      properties:
        LACGROUPNAME:
          name: '指定LAC组名'
          type: string
          minLength: 0
          maxLength: 32
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_lacid_list:
      type: items
      properties:
        LACGROUPNAME:
          name: '指定LAC组名'
          type: string
          minLength: 0
          maxLength: 32
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LACSECNUM:
          name: 'LAC段编号'
          type: integer
          minimum: 0
          maximum: 23999
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        LACSTARTID:
          name: 'LAC起始ID'
          type: string
          minLength: 0
          maxLength: 6
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        LACENDID:
          name: 'LAC截止ID'
          type: string
          minLength: 0
          maxLength: 6
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_poolgrpmap_list:
      type: items
      properties:
        MAPPINGNAME:
          name: '映射规则名称'
          type: string
          minLength: 0
          maxLength: 79
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        LOCATIONGRPTYPE:
          name: '位置区组类型'
          type: string
          enum:
          - LAC
          - TAC
          required: false
          description: '可以使用查询命令**LST LACGROUP**进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        LOCATIONGRPNAME:
          name: '位置区组名称'
          type: string
          minLength: 0
          maxLength: 32
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
          description: '可以使用**LST POOLGROUP**命令进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    add_adrlocwhitelst_list:
      type: items
      properties:
        MSISDN:
          name: 'MSISDN号'
          type: string
          minLength: 0
          maxLength: 15
          required: true
          description: '位于白名单中的用户不基于位置区分配IP地址。'
          data_source: '本端规划'
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
    set_apnipallocrule_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ospf_list:
      type: items
      properties:
        PROCID:
          name: 'OSPF进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: '-'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        VRFNAME:
          name: 'VPN实例名'
          type: string
          maxLength: 31
          required: false
          description: '可以使用**LST VPNINST**命令进行查询。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: '_public_'
        SCHEMAROUID:
          name: 'Schema路由器标识'
          type: string
          maxLength: 15
          required: false
          description: '须知：  Router ID必须全网唯一。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_ospfarea_list:
      type: items
      properties:
        PROCID:
          name: 'OSPF进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        AREAID:
          name: '区域号'
          type: string
          maxLength: 15
          required: true
          description: '-'
          data_source: '与对端协商'
          pattern: ''
          default: ''
    add_ospfnetwork_list:
      type: items
      properties:
        PROCID:
          name: 'OSPF进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        AREAID:
          name: '区域号'
          type: string
          maxLength: 15
          required: true
          description: '-'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        IPADDRESS:
          name: 'IP地址'
          type: string
          maxLength: 15
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        WILDCARDMASK:
          name: '反掩码'
          type: string
          maxLength: 15
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_ospfimportroute_list:
      type: items
      properties:
        PROCID:
          name: 'OSPF进程号'
          type: integer
          minimum: 1
          maximum: 4294967295
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TOPOID:
          name: '拓扑标识'
          type: integer
          minimum: 0
          maximum: 0
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: 0
        PROTOCOL:
          name: '协议分类'
          type: string
          enum:
          - BGP
          - Direct
          - OSPF
          - Static
          - wlr
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_addressattr_list:
      type: items
      properties:
        ALLOCPRECEDENCE:
          name: 'UE地址分配属性'
          type: string
          required: false
          description: '配置分配主体为UPF。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_pnfprofile_list:
      type: items
      properties:
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 1
          maxLength: 36
          required: true
          description: '配置SMF对接的UPF实例。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        NFTYPE:
          name: 'NF类型'
          type: string
          enum:
          - NfInvalid
          - NfNRF
          - NfUDM
          - NfAMF
          - NfSMF
          - NfAUSF
          - NfNEF
          - NfPCF
          - NfSMSF
          - NfNSSF
          - NfUDR
          - NfLMF
          - NfGMLC
          - Nf5G_EIR
          - NfSEPP
          - NfUPF
          - NfN3IWF
          - NfAF
          - NfUDSF
          - NfBSF
          - NfCHF
          - NfCUSTOM_OCS
          - NfSCP
          - NfPCSCF
          - NfMBSMF
          - NfUDN
          - NfNWDAF
          - NfSCF
          - NfKMC
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        NFSTATUS:
          name: 'NF状态'
          type: string
          enum:
          - Invalid
          - Registered
          - Suspend
          - DeRegistered
          - UnDiscoverable
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: Registered
        FQDN:
          name: '域名'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPADDRESSTYPE:
          name: 'IP地址类型'
          type: string
          enum:
          - IPTypeV4
          - IPTypeV6
          - IPTypeV4V6
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4ADDRESS1:
          name: 'IPV4地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PORT:
          name: '端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_upnode_list:
      type: items
      properties:
        NFINSTANCENAME:
          name: 'UPF实例名称'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: '该参数需要与**ADD PNFPROFILE**命令的“NF实例标识”参数取值保持一致。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        LOCATION:
          name: 'UPF位置特征'
          type: string
          enum:
          - Local
          - Central
          - CentralOnly
          required: false
          description: '该参数请根据UPF节点的位置特征确定。'
          data_source: '本端规划'
          pattern: ''
          default: Central
        UPFUNCTION:
          name: 'UPF功能'
          type: string
          enum:
          - None
          - UlClAndBp
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: None
        VPNNAME:
          name: 'VPN名称'
          type: string
          minLength: 1
          maxLength: 31
          required: false
          description: '可以使用**LST VPNINST**命令进行查询。'
          data_source: '全网规划'
          pattern: ''
          default: '_public_'
    add_upipdomain_list:
      type: items
      properties:
        UPNODE:
          name: 'UPF节点标识'
          type: string
          minLength: 1
          maxLength: 36
          required: true
          description: '该参数需要与**ADD PNFPROFILE**命令的“NF实例标识”参数取值保持一致。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPDOMAIN:
          name: 'IP地址段归属的域'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        DNNSWITCH:
          name: 'DNN开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        DNN:
          name: '数据网络名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: 'APN/DNN实例应该全网规划，SMF配置的APN/DNN实例应该与UPF配置的APN/DNN实例一致。'
          data_source: '全网规划'
          pattern: ''
          default: ''
  examples:
    add_vpninst_list:
    - VPNINSTANCE: 'vpn1'
    add_apn_list:
    - APN: 'apn-test'
      HASVPN: ENABLE
      VPNINSTANCE: 'vpn1'
    set_apnaddressattr_list:
    - APN: 'apn-test'
      SUPPORTIPV4: ENABLE
      SUPPORTIPV6: ENABLE
    add_pool_list:
    - POOLNAME: 'testpool'
      POOLTYPE: LOCAL
      HASVPN: ENABLE
      VPNINSTANCE: 'vpn1'
    add_section_list:
    - POOLNAME: 'testpool'
      SECTIONNUM: 1
      IPVERSION: IPV4
      V4STARTIP: '10.10.1.11'
      V4ENDIP: '10.10.1.20'
    add_poolgroup_list:
    - POOLGRPNAME: 'poolgroup1'
    add_poolbindgroup_list:
    - POOLGROUPNAME: 'poolgroup1'
      POOLNAME: 'testpool'
    add_conflictip_list:
    - POOLNAME: ''
      IPADDRESS: ''
    set_licenseswitch_list:
    - LICITEM: 'LKV3G5LBAA01'
      SWITCH: ENABLE
    set_ipallocbylocglbsw_list:
    - SWITCH: DISABLE
      IPV6SWITCH: ENABLE
    set_ipallocbylocsw_list:
    - LOCATIONGRPTYPE: ''
      LOCATIONGRPNAME: ''
    add_tacgroup_list:
    - TACGROUPNAME: ''
    add_s1tacid_list:
    - TACGROUPNAME: ''
      TACSECNUM: ''
      TACSTARTID: ''
      TACENDID: ''
    add_n2tacid_list:
    - TACGROUPNAME: ''
      TACSECNUM: ''
      TACSTARTID: ''
      TACENDID: ''
    add_lacgroup_list:
    - LACGROUPNAME: 'lac1'
    add_lacid_list:
    - LACGROUPNAME: 'lac1'
      LACSECNUM: 2
      LACSTARTID: '0x000a'
      LACENDID: '0x000b'
    add_poolgrpmap_list:
    - MAPPINGNAME: 'mapping3'
      LOCATIONGRPTYPE: LAC
      LOCATIONGRPNAME: 'lac1'
      POOLGROUPNAME: 'poolgroup1'
    add_adrlocwhitelst_list:
    - MSISDN: '123456'
    set_ipallocrule_list:
    - FIRSTRULESW: ENABLE
      FIRSTRULE: APN-0&LOCATION-1&SMF-0
      SECONDRULESW: DISABLE
      THIRDRULESW: DISABLE
    set_apnipallocrule_list:
    - APN: ''
    add_ospf_list:
    - PROCID: 100
      VRFNAME: 'vpn1'
      SCHEMAROUID: '10.10.10.1'
    add_ospfarea_list:
    - PROCID: 100
      AREAID: '0.0.0.0'
    add_ospfnetwork_list:
    - PROCID: 100
      AREAID: '0.0.0.0'
      IPADDRESS: '10.13.21.0'
      WILDCARDMASK: '0.0.0.255'
    add_ospfimportroute_list:
    - PROCID: 100
      TOPOID: 0
      PROTOCOL: wlr
    set_addressattr_list:
    - ALLOCPRECEDENCE: UPF_FIRST
    add_pnfprofile_list:
    - NFINSTANCEID: 'upf1'
      NFTYPE: NfUPF
      NFSTATUS: Registered
      FQDN: 'GLUPF001BHW'
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS1: '10.107.65.183'
      PORT: 8080
    add_upnode_list:
    - NFINSTANCENAME: 'upf1'
      LOCATION: Central
      UPFUNCTION: None
      VPNNAME: 'vpn1'
    add_upipdomain_list:
    - UPNODE: 'upf1'
      IPDOMAIN: 'Domain_0'
      DNNSWITCH: ENABLE
      DNN: 'apn-test'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 在UEG上执行如下命令，基于APN/DNN实例使能地址分配属性。

#### 1.1 配置VPN实例。

```jinja2
{%- for item in add_vpninst_list -%}
    ADD VPNINST:
    {#- --- 必选参数 --- -#}
    VPNINSTANCE="{{item.VPNINSTANCE}}",
    ;
{%- endfor -%}
```

#### 1.2 配置APN/DNN实例。

```jinja2
{%- for item in add_apn_list -%}
    ADD APN:
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

#### 1.3 使能该APN/DNN的地址分配属性。

```jinja2
{%- for item in set_apnaddressattr_list -%}
    SET APNADDRESSATTR:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.SUPPORTIPV4 is not none -%}
        SUPPORTIPV4={{item.SUPPORTIPV4}},
    {%- endif -%}
    {%- if item.SUPPORTIPV6 is not none -%}
        SUPPORTIPV6={{item.SUPPORTIPV6}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 配置地址池绑定到地址池组。

#### 2.1 配置LOCAL类型地址池。

```jinja2
{%- for item in add_pool_list -%}
    ADD POOL:
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
    ;
{%- endfor -%}
```

#### 配置本地地址池的时候，选择参数“LOCAL”类型。

#### UPF分配双栈地址时，需要在本地分别规划配置IPv4类型和IPv6类型的POOL。

#### 2.2 配置地址池里的地址段。

```jinja2
{%- for item in add_section_list -%}
    ADD SECTION:
    {#- --- 必选参数 --- -#}
    POOLNAME="{{item.POOLNAME}}",
    SECTIONNUM={{item.SECTIONNUM}},
    IPVERSION={{item.IPVERSION}},
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
```

#### 2.3 配置地址池组。

```jinja2
{%- for item in add_poolgroup_list -%}
    ADD POOLGROUP:
    {#- --- 必选参数 --- -#}
    POOLGRPNAME="{{item.POOLGRPNAME}}",
    ;
{%- endfor -%}
```

#### 2.4 配置地址池绑定到地址池组。

```jinja2
{%- for item in add_poolbindgroup_list -%}
    ADD POOLBINDGROUP:
    {#- --- 必选参数 --- -#}
    POOLGROUPNAME="{{item.POOLGROUPNAME}}",
    POOLNAME="{{item.POOLNAME}}",
    ;
{%- endfor -%}
```

#### 2.5 （可选）配置本地地址池中的冲突IPv4地址，标识为冲突状态的IPv4地址不会分配给用户。

```jinja2
{%- if is_optional_conflict_ipv4 -%}
    {%- for item in add_conflictip_list -%}
        ADD CONFLICTIP:
        {#- --- 必选参数 --- -#}
        IPADDRESS="{{item.IPADDRESS}}",
        POOLNAME="{{item.POOLNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

### 3 配置地址分配维度，配置基于位置区分配地址。

#### 3.1 打开License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

#### 3.2 配置基于位置区分配地址的开关。

##### 3.2.1 配置基于位置区分配地址的全局开关。

```jinja2
{%- for item in set_ipallocbylocglbsw_list -%}
    SET IPALLOCBYLOCGLBSW:
    {#- --- 可选参数 --- -#}
    {%- if item.SWITCH is not none -%}
        SWITCH={{item.SWITCH}},
    {%- endif -%}
    {%- if item.IPV6SWITCH is not none -%}
        IPV6SWITCH={{item.IPV6SWITCH}},
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 3.2.2 （可选）如果某一指定位置区的地址分配开关不同于全局位置区地址分配开关，则需执行配置基于指定位置区分配地址的开关。

```jinja2
{%- if is_optional_location_alloc_switch -%}
    {%- for item in set_ipallocbylocsw_list -%}
        SET IPALLOCBYLOCSW:
        {#- --- 必选参数 --- -#}
        LOCATIONGRPNAME="{{item.LOCATIONGRPNAME}}",
        LOCATIONGRPTYPE={{item.LOCATIONGRPTYPE}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.3 配置位置区。

##### 3.3.1 基于TAC位置区分配地址的时候需要配置本步骤。

###### 3.3.1.1 配置TAC位置区组。

```jinja2
{%- if is_scenario_tac_location -%}
    {%- for item in add_tacgroup_list -%}
        ADD TACGROUP:
        {#- --- 必选参数 --- -#}
        TACGROUPNAME="{{item.TACGROUPNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

###### 3.3.1.2 （可选）在S1TAC组内绑定S1TAC号段。

```jinja2
{%- if is_optional_bind_s1tac_range and is_scenario_tac_location -%}
    {%- for item in add_s1tacid_list -%}
        ADD S1TACID:
        {#- --- 必选参数 --- -#}
        TACSECNUM={{item.TACSECNUM}},
        TACGROUPNAME="{{item.TACGROUPNAME}}",
        TACSTARTID="{{item.TACSTARTID}}",
        TACENDID="{{item.TACENDID}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

###### 3.3.1.3 （可选）在N2TAC组内绑定N2TAC号段。

```jinja2
{%- if is_optional_bind_n2tac_range and is_scenario_tac_location -%}
    {%- for item in add_n2tacid_list -%}
        ADD N2TACID:
        {#- --- 必选参数 --- -#}
        TACSECNUM={{item.TACSECNUM}},
        TACGROUPNAME="{{item.TACGROUPNAME}}",
        TACSTARTID="{{item.TACSTARTID}}",
        TACENDID="{{item.TACENDID}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 3.3.2 基于LAC位置区分配地址的时候需要配置本步骤。

```jinja2
{%- if is_scenario_lac_location -%}
    {%- for item in add_lacgroup_list -%}
        ADD LACGROUP:
        {#- --- 必选参数 --- -#}
        LACGROUPNAME="{{item.LACGROUPNAME}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_scenario_lac_location -%}
    {%- for item in add_lacid_list -%}
        ADD LACID:
        {#- --- 必选参数 --- -#}
        LACGROUPNAME="{{item.LACGROUPNAME}}",
        LACSECNUM={{item.LACSECNUM}},
        LACSTARTID="{{item.LACSTARTID}}",
        LACENDID="{{item.LACENDID}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.4 配置TAC-Group/LAC-Group与地址池组的映射关系。

```jinja2
{%- for item in add_poolgrpmap_list -%}
    ADD POOLGRPMAP:
    {#- --- 必选参数 --- -#}
    MAPPINGNAME="{{item.MAPPINGNAME}}",
    POOLGROUPNAME="{{item.POOLGROUPNAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.LOCATIONGRPTYPE is not none -%}
        LOCATIONGRPTYPE={{item.LOCATIONGRPTYPE}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：LOCATIONGRPTYPE=TAC/LAC 时必选 --- -#}
    {%- if item.LOCATIONGRPTYPE in ['TAC', 'LAC'] -%}
        LOCATIONGRPNAME="{{item.LOCATIONGRPNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 如果要配置基于多个维度分配IP地址，可配置一条映射关系，同时配置DNN、SMF或位置区与地址池组的映射关系。

#### 3.5 配置基于位置区分配IP地址的白名单，在白名单范围中的用户不参与基于位置区的IP地址分配。

```jinja2
{%- for item in add_adrlocwhitelst_list -%}
    ADD ADRLOCWHITELST:
    {#- --- 必选参数 --- -#}
    MSISDN="{{item.MSISDN}}",
    ;
{%- endfor -%}
```

### 4 配置地址分配规则。

### 地址分配规则支持两级控制：基于全局和基于APN/DNN。默认使用全局地址分配规则。如果配置了使用基于APN/DNN的地址分配规则，则使用APN/DNN的地址分配规则。

#### 4.1 配置全局地址分配规则优先级。

```jinja2
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
```

#### 每级优先级规则中所选的条件之间为“与”的关系，表示从所选条件映射的地址范围内分配地址，因此此次设置的规则需要与地址池的映射条件一致。例如此处按照位置区+APN（APN-1&LOCATION-1&SMF-0）设置条件，则规划的地址池组也需绑定LOC&APN。

#### 4.2 （可选）如果某一APN/DNN的地址分配规则不同于全局地址分配规则，则需执行配置基于APN的地址分配规则优先级。

```jinja2
{%- if is_optional_apn_alloc_rule_priority -%}
    {%- for item in set_apnipallocrule_list -%}
        SET APNIPALLOCRULE:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

### 5 配置手机下行路由。

#### 5.1 启动OSPF进程。

```jinja2
{%- for item in add_ospf_list -%}
    ADD OSPF:
    {#- --- 必选参数 --- -#}
    PROCID={{item.PROCID}},
    {#- --- 可选参数 --- -#}
    {%- if item.VRFNAME is not none -%}
        VRFNAME="{{item.VRFNAME}}",
    {%- endif -%}
    {%- if item.SCHEMAROUID is not none -%}
        SCHEMAROUID="{{item.SCHEMAROUID}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 5.2 添加OSPF区域。

```jinja2
{%- for item in add_ospfarea_list -%}
    ADD OSPFAREA:
    {#- --- 必选参数 --- -#}
    PROCID={{item.PROCID}},
    AREAID="{{item.AREAID}}",
    ;
{%- endfor -%}
```

#### 5.3 配置运行OSPF协议的接口。

```jinja2
{%- for item in add_ospfnetwork_list -%}
    ADD OSPFNETWORK:
    {#- --- 必选参数 --- -#}
    PROCID={{item.PROCID}},
    AREAID="{{item.AREAID}}",
    IPADDRESS="{{item.IPADDRESS}}",
    WILDCARDMASK="{{item.WILDCARDMASK}}",
    ;
{%- endfor -%}
```

#### 5.4 引入WLR路由。

```jinja2
{%- for item in add_ospfimportroute_list -%}
    ADD OSPFIMPORTROUTE:
    {#- --- 必选参数 --- -#}
    PROCID={{item.PROCID}},
    PROTOCOL={{item.PROTOCOL}},
    {#- --- 可选参数 --- -#}
    {%- if item.TOPOID is not none -%}
        TOPOID={{item.TOPOID}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 6 在SMF上执行如下命令：配置UPF为IP地址分配主体，同时配置UPF的IPdomain。

#### 6.1 配置UPF优先为UE分配IP地址。

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_addressattr_list的变量区（command: SET ADDRESSATTR） -#}
<!-- MISSING_MACRO: command=SET ADDRESSATTR list_name=set_addressattr_list step_id=6.1 -->
```

#### 6.2 配置SMF对接的UPF实例。

```jinja2
{%- for item in add_pnfprofile_list -%}
    ADD PNFPROFILE:
    {#- --- 必选参数 --- -#}
    NFINSTANCEID="{{item.NFINSTANCEID}}",
    NFTYPE={{item.NFTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.NFSTATUS is not none -%}
        NFSTATUS={{item.NFSTATUS}},
    {%- endif -%}
    {%- if item.IPADDRESSTYPE is not none -%}
        IPADDRESSTYPE={{item.IPADDRESSTYPE}},
    {%- endif -%}
    {%- if item.PORT is not none -%}
        PORT={{item.PORT}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPADDRESSTYPE=IPTypeV4/IPTypeV4V6 时必选 --- -#}
    {%- if item.IPADDRESSTYPE in ['IPTypeV4', 'IPTypeV4V6'] -%}
        IPV4ADDRESS1="{{item.IPV4ADDRESS1}}",
    {%- endif -%}
    {#- --- 条件必选/可选参数 --- -#}
    {#- --- 域名: 条件必选(NF类型=NfUPF) / 条件可选(NF类型=NfNRF|NfUDM|NfAMF|NfSMF|NfAUSF|NfNEF|NfPCF|NfSMSF|NfNSSF|NfUDR|NfLMF|NfGMLC|Nf5G_EIR|NfN3IWF|NfAF|NfUDSF|NfBSF|NfCHF|NfInvalid|NfSEPP|NfSCP) --- -#}
    {%- if (item.NFTYPE == 'NfUPF') -%}
        FQDN="{{item.FQDN}}",
    {%- elif (item.NFTYPE in ['NfNRF', 'NfUDM', 'NfAMF', 'NfSMF', 'NfAUSF', 'NfNEF', 'NfPCF', 'NfSMSF', 'NfNSSF', 'NfUDR', 'NfLMF', 'NfGMLC', 'Nf5G_EIR', 'NfN3IWF', 'NfAF', 'NfUDSF', 'NfBSF', 'NfCHF', 'NfInvalid', 'NfSEPP', 'NfSCP']) -%}
        {%- if item.FQDN is not none -%}
            FQDN="{{item.FQDN}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 6.3 配置SMF对接的UPF节点。

```jinja2
{%- for item in add_upnode_list -%}
    ADD UPNODE:
    {#- --- 必选参数 --- -#}
    NFINSTANCENAME="{{item.NFINSTANCENAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.LOCATION is not none -%}
        LOCATION={{item.LOCATION}},
    {%- endif -%}
    {%- if item.UPFUNCTION is not none -%}
        UPFUNCTION={{item.UPFUNCTION}},
    {%- endif -%}
    {%- if item.VPNNAME is not none -%}
        VPNNAME="{{item.VPNNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 6.4 配置SMF对接的UPF IPdomain。

```jinja2
{%- for item in add_upipdomain_list -%}
    ADD UPIPDOMAIN:
    {#- --- 必选参数 --- -#}
    UPNODE="{{item.UPNODE}}",
    IPDOMAIN="{{item.IPDOMAIN}}",
    DNNSWITCH={{item.DNNSWITCH}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：DNNSWITCH=ENABLE 时必选 --- -#}
    {%- if item.DNNSWITCH == 'ENABLE' -%}
        DNN="{{item.DNN}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

