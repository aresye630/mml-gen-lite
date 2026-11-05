---
id: ''
name: 容灾配置
ne_type: UEG
type: feature
description: 用于配置DC内负荷分担，DC间整体主备容灾场景下SMF与UPF的配置。  此场景下UPF无需特殊配置。
tags: []
risk_level: ''
doc_source: ["专网（仅连接，园区入驻式）","业务原理","5GC toB 容灾机制（专网，入驻式）","容灾方案","DC内负荷分担，DC间整体主备容灾","容灾配置"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
用于配置DC内负荷分担，DC间整体主备容灾场景下SMF与UPF的配置。此场景下UPF无需特殊配置。

## 必备事项
前提条件

SMF与UPF已完成基础配置。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_apn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '增加APN信息。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_nsdnn_list:
      type: items
      properties:
        NSIDX:
          name: '网络切片索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: '* 增加DNN切片绑定关系。 * 参数“NSIDX”由命令**LST NFNS**查询结果中的“网络切片索引”获取。当存在切片发放场景时，此参数引用切片发放对应的参数。 * 参数“DNN”已在**ADD APN**中定义。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DNN:
          name: '数据网络名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
    set_apnpccfunc_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          maxLength: 63
          required: true
          description: '关闭本地用户、漫游用户、拜访地用户动态PCC功能，参数“APN”已在**ADD APN**中定义。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        HOMEPCCSWITCH:
          name: '本地用户动态PCC功能'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        ROAMPCCSWITCH:
          name: '漫游用户动态PCC功能'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        VISITPCCSWITCH:
          name: '拜访用户动态PCC功能'
          type: string
          enum:
          - DISABLE
          - ENABLE
          - INHERIT
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_apnusrprofg_list:
      type: items
      properties:
        APN:
          name: 'APN'
          type: string
          maxLength: 63
          required: true
          description: '配置将UserProfile Group绑定到APN。参数“APN”已在**ADD APN**中定义，参数“USERPROFGNAME”已在PCC业务配置的**ADD USRPROFGROUP**命令中定义。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        USERPROFGNAME:
          name: '用户模板组名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_apnaddressattr_list:
      type: items
      properties:
        ALLOCWITHOUTPCO:
          name: 'ALLOCWITHOUTPCO'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ANTISPOOFINGDI:
          name: 'ANTISPOOFINGDI'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ANTISPOOFINGUI:
          name: 'ANTISPOOFINGUI'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FRAMEDROUTE:
          name: 'FRAMEDROUTE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IGNORECONFLICT:
          name: 'IGNORECONFLICT'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4ALLOCTYPE:
          name: 'IPV4ALLOCTYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4RADIUSPRIOR:
          name: 'IPV4RADIUSPRIOR'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6ALLOCTYPE:
          name: 'IPV6ALLOCTYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6RADIUSPRIOR:
          name: 'IPV6RADIUSPRIOR'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6RAINTV:
          name: 'IPV6RAINTV'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6RAOFLAG:
          name: 'IPV6RAOFLAG'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RADIUSIPROUTE:
          name: 'RADIUSIPROUTE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DHCPIPROUTE:
          name: 'DHCPIPROUTE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        STATICIP:
          name: 'STATICIP'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        STATICIPROUTE:
          name: 'STATICIPROUTE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SUPPORTIPV4:
          name: 'SUPPORTIPV4'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SUPPORTIPV6:
          name: 'SUPPORTIPV6'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SUPPORTPRIOR:
          name: 'SUPPORTPRIOR'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        APN:
          name: 'APN'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPTYPEFORDUALIP:
          name: 'IPTYPEFORDUALIP'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SINGLEADDRCAUSE:
          name: 'SINGLEADDRCAUSE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4ALLOCPRIALG:
          name: 'IPV4ALLOCPRIALG'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6ALLOCPRIALG:
          name: 'IPV6ALLOCPRIALG'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RDSSVRCTRL:
          name: 'RDSSVRCTRL'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6RAMTUSW:
          name: 'IPV6RAMTUSW'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6MTU:
          name: 'IPV6MTU'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6RALIFETIME:
          name: 'IPV6RALIFETIME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6RATIMES:
          name: 'IPV6RATIMES'
          type: string
          required: false
          description: ''
          data_source: ''
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
          description: 'SMF本端添加UPF。'
          data_source: '本端规划'
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
          data_source: '本端规划'
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
          data_source: '本端规划'
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
          name: 'IP地址'
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
          data_source: ''
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
          description: '配置UPF的属性。'
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
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: Central
        UPFUNCTION:
          name: 'UPF支持功能'
          type: string
          enum:
          - None
          - UlClAndBp
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: None
        LOCK:
          name: 'UPF锁'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: FALSE
        APSAMIGFUNC:
          name: '辅锚点UPF故障迁移功能开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        ADDRALLOCMODE:
          name: '地址分配属性'
          type: string
          enum:
          - INHERIT
          - SMF_ALLOC
          - UPF_FIRST
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: INHERIT
        SHAREDUPFSW:
          name: 'UPF共享开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        VPNNAME:
          name: 'VPN名称'
          type: string
          minLength: 1
          maxLength: 31
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: '_public_'
        SUPATSSS:
          name: '是否支持作为ATSSS UPF'
          type: string
          enum:
          - Enable
          - Disable
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: Disable
        IPV6NDPLCY:
          name: 'IPv6 ND信息携带方式'
          type: string
          enum:
          - PRIVATE
          - STANDARD
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: PRIVATE
        IOSWITCH:
          name: '惯性运行开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        CAMPUSSW:
          name: '园区UPF开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        ULCLFWDTNLSW:
          name: 'ULCL UPF间创建转发隧道开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        PDUESTWITHOUTN9:
          name: '是否支持UPF无N9逻辑接口地址时作为主锚点激活'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
        NGLANSW:
          name: '是否支持5G LAN'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: DISABLE
    add_pnfns_list:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: '配置用户面支持的服务切片信息。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SST:
          name: '切片/服务类型'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_pnfdnn_list:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: '配置UPF的DNN属性，用于在用户会话激活时基于用户的DNN选择UPF。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 0
          maxLength: 38
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        DNN:
          name: '数据网络名称'
          type: string
          minLength: 0
          maxLength: 66
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        PNFNSINDEX:
          name: '对端NF的切片索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 0
        PRISWITCH:
          name: '优先级功能开关'
          type: string
          enum:
          - INHERIT
          - SPECIFIC
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: INHERIT
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        CAPSWITCH:
          name: '容量功能开关'
          type: string
          enum:
          - INHERIT
          - SPECIFIC
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: INHERIT
    set_apnupselply_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '设置APN粒度的优选UPF的开关'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PRIORITYFLAG:
          name: '基于位置条件优选锚点UPF的开关配置'
          type: string
          enum:
          - INHERIT
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
        COMBINEDSELSTG:
          name: '选择合一UPF的优先级策略'
          type: string
          enum:
          - TAIPRI
          - APNPRI
          required: false
          description: ''
          data_source: '固定取值'
          pattern: ''
          default: ''
    add_uparea_list:
      type: items
      properties:
        AREANAME:
          name: '位置区名称'
          type: string
          minLength: 1
          maxLength: 255
          required: true
          description: '与**ADD PNFSMFSERAREA**中“SMFSERVINGAREA”的取值一致。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        AREATYPE:
          name: 'ARE类型'
          type: string
          enum:
          - S1TAI
          - N2TAI
          - LAI
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_upareabindn2tai_list:
      type: items
      properties:
        AREANAME:
          name: 'UP位置区名称'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: '已通过命令**ADD UPAREA**配置。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        N2BEGINTAI:
          name: 'N2TAI范围开始值'
          type: string
          minLength: 11
          maxLength: 12
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        N2ENDTAI:
          name: 'N2TAI范围结束值'
          type: string
          minLength: 11
          maxLength: 12
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_pnfsmfserarea_list:
      type: items
      properties:
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: 'SMF本端配置UPF所覆盖的区域，用于在用户会话激活时基于用户位置区选择UPF。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SMFSERVINGAREA:
          name: 'SMF服务区域'
          type: string
          minLength: 1
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_apn_list:
    - APN: 'APN1'
    add_nsdnn_list:
    - NSIDX: 0
      DNN: 'APN1'
    set_apnpccfunc_list:
    - APN: 'APN1'
      HOMEPCCSWITCH: DISABLE
      ROAMPCCSWITCH: DISABLE
      VISITPCCSWITCH: DISABLE
    add_apnusrprofg_list:
    - APN: 'APN1'
      USERPROFGNAME: 'up_group_cmcc_cmnet'
    set_apnaddressattr_list:
    - ALLOCWITHOUTPCO: ENABLE
      ANTISPOOFINGDI: ENABLE
      ANTISPOOFINGUI: ENABLE
      FRAMEDROUTE: DISABLE
      IGNORECONFLICT: ENABLE
      IPV4ALLOCTYPE: RADIUS
      IPV4RADIUSPRIOR: ENABLE
      IPV6ALLOCTYPE: RADIUS
      IPV6RADIUSPRIOR: ENABLE
      IPV6RAINTV: '14400'
      IPV6RAOFLAG: ENABLE
      RADIUSIPROUTE: ENABLE
      DHCPIPROUTE: ENABLE
      STATICIP: ENABLE
      STATICIPROUTE: ENABLE
      SUPPORTIPV4: ENABLE
      SUPPORTIPV6: ENABLE
      SUPPORTPRIOR: IPV4
      APN: APN1
      IPTYPEFORDUALIP: IPV4V6
      SINGLEADDRCAUSE: NETWORK_PREFER
      IPV4ALLOCPRIALG: DISABLE
      IPV6ALLOCPRIALG: DISABLE
      RDSSVRCTRL: ENABLE
      IPV6RAMTUSW: DISABLE
      IPV6MTU: '1800'
      IPV6RALIFETIME: '65535'
      IPV6RATIMES: '0'
    add_pnfprofile_list:
    - NFINSTANCEID: 'UPF_Instance_1'
      NFTYPE: NfUPF
      NFSTATUS: Registered
      FQDN: 'upf01.node'
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS1: '192.168.10.2'
      PORT: 8805
    add_upnode_list:
    - NFINSTANCENAME: 'UPF_Instance_1'
      LOCATION: Central
      UPFUNCTION: None
      LOCK: FALSE
      APSAMIGFUNC: DISABLE
      ADDRALLOCMODE: INHERIT
      SHAREDUPFSW: DISABLE
      VPNNAME: 'VRF_CP'
      SUPATSSS: Disable
      IPV6NDPLCY: PRIVATE
      IOSWITCH: DISABLE
      CAMPUSSW: DISABLE
      ULCLFWDTNLSW: DISABLE
      PDUESTWITHOUTN9: DISABLE
      NGLANSW: DISABLE
    add_pnfns_list:
    - INDEX: 1
      NFINSTANCEID: 'UPF_Instance_1'
      SST: 1
    add_pnfdnn_list:
    - INDEX: 1
      NFINSTANCEID: 'UPF_Instance_1'
      DNN: 'APN1'
      PNFNSINDEX: 1
      PRISWITCH: SPECIFIC
      PRIORITY: 1
      CAPSWITCH: INHERIT
    set_apnupselply_list:
    - APN: 'APN1'
      PRIORITYFLAG: ENABLE
      COMBINEDSELSTG: APNPRI
    add_uparea_list:
    - AREANAME: 'UPAREA1'
      AREATYPE: N2TAI
    add_upareabindn2tai_list:
    - AREANAME: 'UPAREA1'
      N2BEGINTAI: '46011000BB8'
      N2ENDTAI: '46011000BB8'
    add_pnfsmfserarea_list:
    - NFINSTANCEID: 'UPF_Instance_1'
      SMFSERVINGAREA: 'UPAREA1'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 （SMF配置）配置APN及相关信息。

```jinja2
{%- for item in add_apn_list -%}
    ADD APN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_nsdnn_list -%}
    ADD NSDNN:
    {#- --- 必选参数 --- -#}
    NSIDX={{item.NSIDX}},
    DNN="{{item.DNN}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in set_apnpccfunc_list -%}
    SET APNPCCFUNC:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.HOMEPCCSWITCH is not none -%}
        HOMEPCCSWITCH={{item.HOMEPCCSWITCH}},
    {%- endif -%}
    {%- if item.ROAMPCCSWITCH is not none -%}
        ROAMPCCSWITCH={{item.ROAMPCCSWITCH}},
    {%- endif -%}
    {%- if item.VISITPCCSWITCH is not none -%}
        VISITPCCSWITCH={{item.VISITPCCSWITCH}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_apnusrprofg_list -%}
    ADD APNUSRPROFG:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    USERPROFGNAME="{{item.USERPROFGNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_apnaddressattr_list的变量区（command: SET APNADDRESSATTR） -#}
<!-- MISSING_MACRO: command=SET APNADDRESSATTR list_name=set_apnaddressattr_list step_id=1 -->
```

### 2 （SMF配置）配置用户面节点实例。配置Profile实例。

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

### 3 （SMF配置）配置用户面节点的位置特征和分流能力。

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
    {%- if item.LOCK is not none -%}
        LOCK={{item.LOCK}},
    {%- endif -%}
    {%- if item.APSAMIGFUNC is not none -%}
        APSAMIGFUNC={{item.APSAMIGFUNC}},
    {%- endif -%}
    {%- if item.ADDRALLOCMODE is not none -%}
        ADDRALLOCMODE={{item.ADDRALLOCMODE}},
    {%- endif -%}
    {%- if item.SHAREDUPFSW is not none -%}
        SHAREDUPFSW={{item.SHAREDUPFSW}},
    {%- endif -%}
    {%- if item.VPNNAME is not none -%}
        VPNNAME="{{item.VPNNAME}}",
    {%- endif -%}
    {%- if item.SUPATSSS is not none -%}
        SUPATSSS={{item.SUPATSSS}},
    {%- endif -%}
    {%- if item.IPV6NDPLCY is not none -%}
        IPV6NDPLCY={{item.IPV6NDPLCY}},
    {%- endif -%}
    {%- if item.IOSWITCH is not none -%}
        IOSWITCH={{item.IOSWITCH}},
    {%- endif -%}
    {%- if item.CAMPUSSW is not none -%}
        CAMPUSSW={{item.CAMPUSSW}},
    {%- endif -%}
    {%- if item.ULCLFWDTNLSW is not none -%}
        ULCLFWDTNLSW={{item.ULCLFWDTNLSW}},
    {%- endif -%}
    {%- if item.PDUESTWITHOUTN9 is not none -%}
        PDUESTWITHOUTN9={{item.PDUESTWITHOUTN9}},
    {%- endif -%}
    {%- if item.NGLANSW is not none -%}
        NGLANSW={{item.NGLANSW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 （SMF配置）配置用户面节点支持的切片与DNN信息。

```jinja2
{%- for item in add_pnfns_list -%}
    ADD PNFNS:
    {#- --- 必选参数 --- -#}
    INDEX={{item.INDEX}},
    NFINSTANCEID="{{item.NFINSTANCEID}}",
    SST={{item.SST}},
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_pnfdnn_list -%}
    ADD PNFDNN:
    {#- --- 必选参数 --- -#}
    INDEX={{item.INDEX}},
    NFINSTANCEID="{{item.NFINSTANCEID}}",
    DNN="{{item.DNN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.PNFNSINDEX is not none -%}
        PNFNSINDEX={{item.PNFNSINDEX}},
    {%- endif -%}
    {%- if item.PRISWITCH is not none -%}
        PRISWITCH={{item.PRISWITCH}},
    {%- endif -%}
    {%- if item.CAPSWITCH is not none -%}
        CAPSWITCH={{item.CAPSWITCH}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：PRISWITCH=SPECIFIC 时必选 --- -#}
    {%- if item.PRISWITCH == 'SPECIFIC' -%}
        PRIORITY={{item.PRIORITY}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 （SMF配置）配置APN粒度的优选UPF的开关。

```jinja2
{%- for item in set_apnupselply_list -%}
    SET APNUPSELPLY:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.PRIORITYFLAG is not none -%}
        PRIORITYFLAG={{item.PRIORITYFLAG}},
    {%- endif -%}
    {%- if item.COMBINEDSELSTG is not none -%}
        COMBINEDSELSTG={{item.COMBINEDSELSTG}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 6 （SMF配置）配置用户面节点的位置区信息，将位置区与TAI绑定。

```jinja2
{%- for item in add_uparea_list -%}
    ADD UPAREA:
    {#- --- 必选参数 --- -#}
    AREANAME="{{item.AREANAME}}",
    AREATYPE={{item.AREATYPE}},
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_upareabindn2tai_list -%}
    ADD UPAREABINDN2TAI:
    {#- --- 必选参数 --- -#}
    AREANAME="{{item.AREANAME}}",
    N2BEGINTAI="{{item.N2BEGINTAI}}",
    N2ENDTAI="{{item.N2ENDTAI}}",
    ;
{%- endfor -%}
```

### 7 （SMF配置）配置用户面节点支持的为SMF提供服务区域的信息。

```jinja2
{%- for item in add_pnfsmfserarea_list -%}
    ADD PNFSMFSERAREA:
    {#- --- 必选参数 --- -#}
    NFINSTANCEID="{{item.NFINSTANCEID}}",
    SMFSERVINGAREA="{{item.SMFSERVINGAREA}}",
    ;
{%- endfor -%}
```

