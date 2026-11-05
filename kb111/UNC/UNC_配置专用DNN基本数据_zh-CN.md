---
id: ''
name: 配置专用DNN基本数据
ne_type: UNC
type: feature
description: 本操作用于指导在专网SMF上开启通用DNN漫游分流特性，配置专用DNN下的专用UPF属性等基本数据。
risk_level: ''
doc_source: ["网络部署","业务专题","5G Core 一跳入家解决方案","一跳入家解决方案（基于3GPP接入方案）","业务初始部署与调测","部署移动VPN","配置专用DNN数据","配置SMF","配置专用DNN基本数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作用于指导在专网SMF上开启通用DNN漫游分流特性，配置专用DNN下的专用UPF属性等基本数据。

## 必备事项
前提条件

已参考运营商配置规范完成网元的基本配置。
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
          description: '该参数用于指定需要开通的License项。'
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
          description: '该参数用于表示License项的配置开关是否已经打开。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_vpninst_list:
      type: items
      properties:
        VPNINSTANCE:
          name: 'VPN实例名'
          type: string
          minLength: 1
          maxLength: 31
          required: true
          description: '增加VPN实例名。建议该VPN实例与专网UPF的N6接口新开专线的VPN实例保持一致。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_apn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '增加APN，该APN为用户签约的专用DNN。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        HASVPN:
          name: '绑定VPN'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: '将专用DNN绑定VPN实例。'
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
        VPNINSTANCE:
          name: 'VPN实例名'
          type: string
          minLength: 1
          maxLength: 31
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        HASVPNIPV6:
          name: '绑定IPv6 VPN'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
        VPNINSTANCEIPV6:
          name: 'IPv6 VPN实例名'
          type: string
          minLength: 1
          maxLength: 31
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    mod_apn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '参数“APN”已在**ADD APN**中定义。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        LOCREPORT:
          name: '位置上报'
          type: string
          enum:
          - INHERIT
          - ENABLE
          - DISABLE
          required: false
          description: '通用DNN漫游分流方案约束，专用会话不支持AOI，PRA，实时位置上报等特性，因此参数“LOCREPORT”、“LADN”、“AOI”取值分别为“DISABLE”、“NotSupport”、“NotSupport”。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        LADN:
          name: '局域数据网络'
          type: string
          enum:
          - Support
          - NotSupport
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_smffunc_list:
      type: items
      properties:
        AOI:
          name: '兴趣区'
          type: string
          enum:
          - NotSupport
          - Support
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_apnidletime_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '参数“APN”已在**ADD APN**中定义。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        INHERIT:
          name: '继承默认开关'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: '专用会话使用自定义的IDLETIMER配置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        HCTXCHKSW:
          name: 'H-SMF空闲上下文核查开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SMFSESIDLETIMER:
          name: 'SMF会话空闲定时器时长'
          type: integer
          minimum: 5
          maximum: 12000
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        BEARERTIMER:
          name: '承载定时器(min)'
          type: integer
          minimum: 5
          maximum: 12000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DFTBEARPOLICY:
          name: '缺省承载和默认GBR的定时器'
          type: string
          enum:
          - ONEDAY
          - OFF
          - USEBEARERTIMER
          - USESPECIFICVAL
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DFTBRPLCYGGSN:
          name: 'GGSN一次激活上下文定时器'
          type: string
          enum:
          - ONEDAY
          - OFF
          - USEBEARERTIMER
          - USESPECIFICVAL
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GCTXCHKSW:
          name: 'GGSN空闲上下文检查开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GULTIMERLEVEL:
          name: 'GUL承载级别参数'
          type: string
          enum:
          - SESSION
          - BEARER
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HCTXINACHKSW:
          name: 'H-SMF不活动上下文核查开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HSMFTIMERLEVEL:
          name: 'H-SMF空闲上下文核查级别'
          type: string
          enum:
          - SESSION
          - QOSFLOW
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ICTXCHKSW:
          name: 'I-SMF/V-SMF空闲上下文核查开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ICTXINACHKSW:
          name: 'I-SMF/V-SMF不活动上下文核查开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IDLEUPDATEMSG:
          name: '空闲超时发送更新消息'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PCTXCHKSW:
          name: 'PGW-C和SGW-C/PGW-C空闲上下文检查开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PROS8CTXCHKSW:
          name: 'Proxy-SMF S8空闲上下文核查开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PROXYSMFCHKSW:
          name: 'Proxy-SMF 空闲上下文核查开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SCTXCHKSW:
          name: 'SGW-C空闲上下文核查开关'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SESSIONTIMER:
          name: '会话定时器时长(min)'
          type: integer
          minimum: 5
          maximum: 12000
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SMFSESINATIMER:
          name: 'SMF会话不活动定时器时长(min)'
          type: integer
          minimum: 5
          maximum: 12000
          required: false
          description: ''
          data_source: ''
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
          description: '* 增加DNN切片绑定关系。 * 参数“NSIDX”由命令**LST NSDNN**查询结果中的“网络切片索引”获取。当存在切片发放场景时，此参数引用切片发放对应的参数。 * 参数“DNN”已在**ADD APN**中定义。'
          data_source: '已配置数据中获取'
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
    add_pnfdnn_list:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: '配置专网UPF的DNN属性，若部署容灾模式，此处涉及两个UPF。   * 参数“NFINSTANCEID”通过**LST PNFPROFILE**查询。 * 参数“DNN”已在**ADD APN**中定义。 * 参数“PNFNSINDEX”通过**LST PNFNS**查询，当存在切片发放场景时，此参数引用切片发放对应的参数。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 0
          maxLength: 38
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        DNN:
          name: '数据网络名称'
          type: string
          minLength: 0
          maxLength: 66
          required: true
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        PNFNSINDEX:
          name: '对端NF的切片索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: ''
          data_source: '已配置数据中获取'
          pattern: ''
          default: 0
    add_apnupfinfo_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: '配置专网UPF在专用DNN下的位置特征。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        UPFINSTANCEID:
          name: 'UPF实例标识'
          type: string
          minLength: 1
          maxLength: 36
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        LOCATION:
          name: 'UPF的位置特征'
          type: string
          enum:
          - INHERIT
          - BOTH
          - LOCALONLY
          - CENTERONLY
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: INHERIT
        PSACOMBINEULCL:
          name: '主锚点与分流节点合设功能'
          type: string
          enum:
          - INHERIT
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: INHERIT
    set_apnpccfunc_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          maxLength: 63
          required: true
          description: '配置专用DNN用户的动态PCC规则开关。'
          data_source: '全网规划'
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
          data_source: '对端协商'
          pattern: ''
          default: ''
    set_srvnoderatpri_list:
      type: items
      properties:
        NODETYPE:
          name: '网元类型'
          type: string
          enum:
          - GGSN
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FIRSTPRIORITY:
          name: 'RAT类型的第一优先级'
          type: string
          enum:
          - RAT
          - SGSN_IP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SECONDPRIORITY:
          name: 'RAT类型的第二优先级'
          type: string
          enum:
          - RAT
          - SGSN_IP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_srvnoderat_list:
      type: items
      properties:
        IPVERSION:
          name: 'IP地址版本类型'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRVNODESTARTV4:
          name: 'Service Node的起始IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRVNODEENDV4:
          name: 'Service Node的结束IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RATTYPE:
          name: 'RAT类型'
          type: string
          enum:
          - UTRAN
          - GERAN
          - WLAN
          - GAN
          - EUTRAN
          - 'NULL'
          - EUTRAN_NB_IOT
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRVNODESTARTV6:
          name: 'Service Node的起始IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRVNODEENDV6:
          name: 'Service Node的结束IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    lck_apn_list:
      type: items
      properties:
        APN:
          name: 'APN名称'
          type: string
          minLength: 1
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LOCKED:
          name: '锁定'
          type: string
          enum:
          - ENABLE
          - DISABLE
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LCKRATTYPE:
          name: '锁定的RAT类型'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'UTRAN-1&GERAN-1&WLAN-1&GAN-1&HSPA-1&EUTRAN-1&VIRTUAL-1&EUTRAN_NB_IoT-1&LTE_M-1&NR-1&REDCAP-1'
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV2ASLSR02'
      SWITCH: ENABLE
    add_vpninst_list:
    - VPNINSTANCE: 'VRF_N6_Local_2B_APP'
    add_apn_list:
    - APN: 'stjwt.gd'
      HASVPN: ENABLE
      VPNINSTANCE: 'VRF_N6_Local_2B_APP'
      HASVPNIPV6: ENABLE
      VPNINSTANCEIPV6: 'VRF_N6_Local_2B_APP'
    mod_apn_list:
    - APN: 'stjwt.gd'
      LOCREPORT: DISABLE
      LADN: NotSupport
    set_smffunc_list:
    - AOI: NotSupport
    set_apnidletime_list:
    - APN: 'stjwt.gd'
      INHERIT: NO
      HCTXCHKSW: DISABLE
      SMFSESIDLETIMER: 2880
      BEARERTIMER: ''
      DFTBEARPOLICY: ''
      DFTBRPLCYGGSN: ''
      GCTXCHKSW: ''
      GULTIMERLEVEL: ''
      HCTXINACHKSW: ''
      HSMFTIMERLEVEL: ''
      ICTXCHKSW: ''
      ICTXINACHKSW: ''
      IDLEUPDATEMSG: ''
      PCTXCHKSW: ''
      PROS8CTXCHKSW: ''
      PROXYSMFCHKSW: ''
      SCTXCHKSW: ''
      SESSIONTIMER: ''
      SMFSESINATIMER: ''
    add_nsdnn_list:
    - NSIDX: 0
      DNN: 'stjwt.gd'
    add_pnfdnn_list:
    - INDEX: 100
      NFINSTANCEID: '5EA7F228-47CC-2032-03A3-0E1313000001'
      DNN: 'stjwt.gd'
      PNFNSINDEX: 3
    add_apnupfinfo_list:
    - APN: 'stjwt.gd'
      UPFINSTANCEID: '5EA7F228-47CC-2032-03A3-0E1313000001'
      LOCATION: CENTERONLY
      PSACOMBINEULCL: INHERIT
    set_apnpccfunc_list:
    - APN: 'stjwt.gd'
      HOMEPCCSWITCH: ENABLE
    set_srvnoderatpri_list:
    - NODETYPE: GGSN
      FIRSTPRIORITY: SGSN_IP
      SECONDPRIORITY: RAT
    add_srvnoderat_list:
    - IPVERSION: IPV4
      SRVNODESTARTV4: '10.1.1.1'
      SRVNODEENDV4: '255.255.255.255'
      RATTYPE: UTRAN
      SRVNODESTARTV6: '0000:0000:0000:0000:0000:0000:0000:0001'
      SRVNODEENDV6: 'FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF:FFFF'
    lck_apn_list:
    - APN: 'stjwt.gd'
      LOCKED: ENABLE
      LCKRATTYPE: UTRAN-1&GERAN-1&WLAN-0&GAN-0&HSPA-0&EUTRAN-0&VIRTUAL-0&EUTRAN_NB_IoT-0&LTE_M-0&NR-0
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 打开“跨域互联互通-SMF”的License配置开关，当UE进行跨区域移动超出SMF的服务范围可插入I-SMF为UE提供服务。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

### 2 配置VPN和DNN，如已完成VPN和专用DNN创建，请跳过本步骤。建议该VPN实例与专网UPF的N6接口VPN实例保持一致。

```jinja2
{%- for item in add_vpninst_list -%}
    ADD VPNINST:
    {#- --- 必选参数 --- -#}
    VPNINSTANCE="{{item.VPNINSTANCE}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_apn_list -%}
    ADD APN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.HASVPN is not none -%}
        HASVPN={{item.HASVPN}},
    {%- endif -%}
    {%- if item.HASVPNIPV6 is not none -%}
        HASVPNIPV6={{item.HASVPNIPV6}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：HASVPN=ENABLE 时必选 --- -#}
    {%- if item.HASVPN == 'ENABLE' -%}
        VPNINSTANCE="{{item.VPNINSTANCE}}",
    {%- endif -%}
    {#- --- 条件必选：HASVPNIPV6=ENABLE 时必选 --- -#}
    {%- if item.HASVPNIPV6 == 'ENABLE' -%}
        VPNINSTANCEIPV6="{{item.VPNINSTANCEIPV6}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 特性约束专用会话不支持AOI，PRA，实时位置上报等特性，设置专用DNN不支持位置上报，设置专用SMF不支持兴趣区。请使用LST SMFFUNC查询系统是否有该配置记录，若无记录请配置SET SMFFUNC命令，若已有记录请按照SET SMFFUNC命令参数核查并调整。

```jinja2
{%- for item in mod_apn_list -%}
    MOD APN:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.LOCREPORT is not none -%}
        LOCREPORT={{item.LOCREPORT}},
    {%- endif -%}
    {%- if item.LADN is not none -%}
        LADN={{item.LADN}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in set_smffunc_list -%}
    SET SMFFUNC:
    {#- --- 可选参数 --- -#}
    {%- if item.AOI is not none -%}
        AOI={{item.AOI}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 关闭APN空闲上下文定时器配置。

### 如果是一跳入家场景，且开启业务触发专用DNN分流会话时，需要打开APN空闲上下文定时器配置。

```jinja2
{%- for item in set_apnidletime_list -%}
    SET APNIDLETIME:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.INHERIT is not none -%}
        INHERIT={{item.INHERIT}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：INHERIT=NO 时可选 --- -#}
    {%- if item.INHERIT == 'NO' -%}
        {%- if item.HCTXCHKSW is not none -%}
            HCTXCHKSW={{item.HCTXCHKSW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：INHERIT=NO 时可选 --- -#}
    {%- if item.INHERIT == 'NO' -%}
        {%- if item.BEARERTIMER is not none -%}
            BEARERTIMER={{item.BEARERTIMER}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：INHERIT=NO 时可选 --- -#}
    {%- if item.INHERIT == 'NO' -%}
        {%- if item.DFTBEARPOLICY is not none -%}
            DFTBEARPOLICY={{item.DFTBEARPOLICY}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：INHERIT=NO 时可选 --- -#}
    {%- if item.INHERIT == 'NO' -%}
        {%- if item.DFTBRPLCYGGSN is not none -%}
            DFTBRPLCYGGSN={{item.DFTBRPLCYGGSN}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：INHERIT=NO 时可选 --- -#}
    {%- if item.INHERIT == 'NO' -%}
        {%- if item.GCTXCHKSW is not none -%}
            GCTXCHKSW={{item.GCTXCHKSW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：INHERIT=NO 时可选 --- -#}
    {%- if item.INHERIT == 'NO' -%}
        {%- if item.GULTIMERLEVEL is not none -%}
            GULTIMERLEVEL={{item.GULTIMERLEVEL}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：INHERIT=NO 时可选 --- -#}
    {%- if item.INHERIT == 'NO' -%}
        {%- if item.HCTXINACHKSW is not none -%}
            HCTXINACHKSW={{item.HCTXINACHKSW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：INHERIT=NO 时可选 --- -#}
    {%- if item.INHERIT == 'NO' -%}
        {%- if item.HSMFTIMERLEVEL is not none -%}
            HSMFTIMERLEVEL={{item.HSMFTIMERLEVEL}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：INHERIT=NO 时可选 --- -#}
    {%- if item.INHERIT == 'NO' -%}
        {%- if item.ICTXCHKSW is not none -%}
            ICTXCHKSW={{item.ICTXCHKSW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：INHERIT=NO 时可选 --- -#}
    {%- if item.INHERIT == 'NO' -%}
        {%- if item.ICTXINACHKSW is not none -%}
            ICTXINACHKSW={{item.ICTXINACHKSW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：INHERIT=NO 时可选 --- -#}
    {%- if item.INHERIT == 'NO' -%}
        {%- if item.IDLEUPDATEMSG is not none -%}
            IDLEUPDATEMSG={{item.IDLEUPDATEMSG}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：INHERIT=NO 时可选 --- -#}
    {%- if item.INHERIT == 'NO' -%}
        {%- if item.PCTXCHKSW is not none -%}
            PCTXCHKSW={{item.PCTXCHKSW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：INHERIT=NO 时可选 --- -#}
    {%- if item.INHERIT == 'NO' -%}
        {%- if item.PROS8CTXCHKSW is not none -%}
            PROS8CTXCHKSW={{item.PROS8CTXCHKSW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：INHERIT=NO 时可选 --- -#}
    {%- if item.INHERIT == 'NO' -%}
        {%- if item.PROXYSMFCHKSW is not none -%}
            PROXYSMFCHKSW={{item.PROXYSMFCHKSW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：INHERIT=NO 时可选 --- -#}
    {%- if item.INHERIT == 'NO' -%}
        {%- if item.SCTXCHKSW is not none -%}
            SCTXCHKSW={{item.SCTXCHKSW}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：INHERIT=NO 时可选 --- -#}
    {%- if item.INHERIT == 'NO' -%}
        {%- if item.SESSIONTIMER is not none -%}
            SESSIONTIMER={{item.SESSIONTIMER}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：INHERIT=NO 时可选 --- -#}
    {%- if item.INHERIT == 'NO' -%}
        {%- if item.SMFSESIDLETIMER is not none -%}
            SMFSESIDLETIMER={{item.SMFSESIDLETIMER}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：INHERIT=NO 时可选 --- -#}
    {%- if item.INHERIT == 'NO' -%}
        {%- if item.SMFSESINATIMER is not none -%}
            SMFSESINATIMER={{item.SMFSESINATIMER}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 配置专用DNN下的切片信息，建议专网业务使用通用DNN的切片策略。

#### 5.1 如果专网SMF和公网SMF合一部署，配置专网SMF在专用DNN下支持的切片时，请使用LST NSDNN查询公用DNN下网络切片索引并通过ADD NSDNN配置。如果专网SMF独立部署，没有配置common.dnn，则使用LST NFNS命令查询切片索引再通过ADD NSDNN配置。

```jinja2
{%- for item in add_nsdnn_list -%}
    ADD NSDNN:
    {#- --- 必选参数 --- -#}
    NSIDX={{item.NSIDX}},
    DNN="{{item.DNN}}",
    ;
{%- endfor -%}
```

#### 5.2 配置专网UPF在专用DNN下支持的切片。请使用LST PNFPROFILE查询专网UPF的实例，LST PNFNS查询专网UPF支持的切片索引。并通过ADD PNFDNN配置。

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
    ;
{%- endfor -%}
```

### 6 配置专网UPF在专用DNN下的属性。

```jinja2
{%- for item in add_apnupfinfo_list -%}
    ADD APNUPFINFO:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    UPFINSTANCEID="{{item.UPFINSTANCEID}}",
    {#- --- 可选参数 --- -#}
    {%- if item.LOCATION is not none -%}
        LOCATION={{item.LOCATION}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：LOCATION=CENTERONLY/BOTH 时可选 --- -#}
    {%- if item.LOCATION in ['CENTERONLY', 'BOTH'] -%}
        {%- if item.PSACOMBINEULCL is not none -%}
            PSACOMBINEULCL={{item.PSACOMBINEULCL}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 7 配置DNN用户的动态PCC规则开关。

```jinja2
{%- for item in set_apnpccfunc_list -%}
    SET APNPCCFUNC:
    {#- --- 必选参数 --- -#}
    APN="{{item.APN}}",
    {#- --- 可选参数 --- -#}
    {%- if item.HOMEPCCSWITCH is not none -%}
        HOMEPCCSWITCH={{item.HOMEPCCSWITCH}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 8 （条件必选）如果未完成2/3/4G融合，需要配置本步骤，限制ratType为2G/3G的用户接入。如果已完成2/3/4G融合，不需要配置本步骤。

### SGSN IPv4地址举例为10.1.1.1，IPv6地址举例为0000:0000:0000:0000:0000:0000:0000:0001。

```jinja2
{%- if is_optional_restrict_rat_access -%}
    {%- for item in set_srvnoderatpri_list -%}
        SET SRVNODERATPRI:
        {#- --- 必选参数 --- -#}
        NODETYPE={{item.NODETYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.FIRSTPRIORITY is not none -%}
            FIRSTPRIORITY={{item.FIRSTPRIORITY}},
        {%- endif -%}
        {%- if item.SECONDPRIORITY is not none -%}
            SECONDPRIORITY={{item.SECONDPRIORITY}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_optional_restrict_rat_access -%}
    {%- for item in add_srvnoderat_list -%}
        ADD SRVNODERAT:
        {#- --- 必选参数 --- -#}
        IPVERSION={{item.IPVERSION}},
        RATTYPE={{item.RATTYPE}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
        {%- if item.IPVERSION == 'IPV4' -%}
            SRVNODESTARTV4="{{item.SRVNODESTARTV4}}",
        {%- endif -%}
        {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
        {%- if item.IPVERSION == 'IPV4' -%}
            SRVNODEENDV4="{{item.SRVNODEENDV4}}",
        {%- endif -%}
        {#- --- 条件必选：IPVERSION=IPV6 时必选 --- -#}
        {%- if item.IPVERSION == 'IPV6' -%}
            SRVNODESTARTV6="{{item.SRVNODESTARTV6}}",
        {%- endif -%}
        {#- --- 条件必选：IPVERSION=IPV6 时必选 --- -#}
        {%- if item.IPVERSION == 'IPV6' -%}
            SRVNODEENDV6="{{item.SRVNODEENDV6}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_optional_restrict_rat_access -%}
    {%- for item in lck_apn_list -%}
        LCK APN:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        LOCKED={{item.LOCKED}},
        {#- --- 可选参数 --- -#}
        {%- if item.LCKRATTYPE is not none -%}
            LCKRATTYPE={{item.LCKRATTYPE}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

