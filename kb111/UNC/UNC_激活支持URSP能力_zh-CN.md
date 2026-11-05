---
id: ''
name: 激活支持URSP能力
ne_type: UNC
type: feature
description: 当希望辅助用户为上行流量选择合适的路由，在PDU会话建立后产生的上行流量能定时被路由到指定DNN，而不是运营商定义的通用DNN时，需要激活URSP功能。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","网络切片功能","WSFD-211102 支持URSP能力","激活支持URSP能力"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当希望辅助用户为上行流量选择合适的路由，在PDU会话建立后产生的上行流量能定时被路由到指定DNN，而不是运营商定义的通用DNN时，需要激活URSP功能。

## 必备事项
前提条件

* 请仔细阅读WSFD-211102 支持URSP能力。
* 完成激活PCC基本功能相关操作。
* 参考UPCF产品文档中特性《WHFD-611068 N15接口(使用HTTP协议)策略控制》，在PCF上完成UE策略关联配置。
* 完成加载License。
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
    mod_amueplcyctrl_list:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - HOME_USER
          - FOREIGN_USER
          - IMSI_PREFIX
          - MSISDN_PREFIX
          required: true
          description: '在AMF上配置AM策略和UE策略控制参数的用户范围。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        NSGRPID:
          name: '网络切片群组标识'
          type: integer
          minimum: 0
          maximum: 16
          required: false
          description: '0用于表示无效的网络切片群组，即不按照网络切片对AM策略或者UE策略进行控制。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ISUEASSOC:
          name: '是否建立UE策略偶联'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: '针对指定的5G用户应用网络侧规划的UE策略时，设置为“YES”。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        DNNUEPLCYSW:
          name: '基于DNN的创建UE策略偶联开关'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: '控制AMF是否支持基于特定DNN关键字建立UE策略偶联。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        DNNUEPLCYKEYWD:
          name: 'UE策略的DNN关键字'
          type: string
          minLength: 1
          maxLength: 63
          required: false
          description: '设置建立UE策略的特定DNN关键字。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        DESC:
          name: '描述信息'
          type: string
          minLength: 0
          maxLength: 32
          required: false
          description: '描述配置AM策略和UE策略控制参数的用户（群），便于记忆。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IMSIPRE:
          name: 'IMSI前缀'
          type: string
          minLength: 5
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MSISDNPRE:
          name: 'MSISDN前缀'
          type: string
          minLength: 1
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_amfplcyfunc_list:
      type: items
      properties:
        OLDUEPLCY:
          name: 'N14接口是否传递UE策略'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: '控制inter-AMF移动性注册（切换）时，老侧AMF是否给新侧AMF传递UE策略信息。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    set_amfsbicmpt_list:
      type: items
      properties:
        SBITYPE:
          name: '服务化接口类型'
          type: string
          enum:
          - N8
          - N11
          - N12
          - N14
          - N15
          - N17
          - N20
          - N22
          - N50
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OLDPCFID:
          name: 'N14接口是否携带pcfId'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OLDUEPLCYURI:
          name: 'N14接口是否携带pcfUePolicyUri'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: '控制inter-AMF移动性注册（切换）时，老侧AMF是否携带pcfUePolicyUri信元给新侧AMF。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        OLDUEPLCYTRIG:
          name: 'N14接口是否携带uePolicyReqTriggerList'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: '控制inter-AMF移动性注册（切换）时，老侧AMF是否携带uePolicyReqTriggerList信元给新侧AMF。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        AMPCFNI:
          name: '是否携带动态NI'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EVTGNBLST:
          name: 'N14接口是否携带GlobalGnbIdList'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        EVTPERIOD:
          name: 'N14接口是否携带repPeriod'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        HAMPCFID:
          name: 'N15接口是否携带hpcfId'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        N11MSGTYPE:
          name: 'N11接口消息类型'
          type: string
          enum:
          - UPDATE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OLDAMPLCYTRIG:
          name: 'N14接口是否携带amPolicyReqTriggerList'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OLDAMPLCYURI:
          name: 'N14接口是否携带pcfAmPolicyUri'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OLDHPCFID:
          name: 'N14接口是否携带hpcfId'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OLDPCFSETID:
          name: 'N14接口是否携带pcfSetId'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        OLDSMFSELINFO:
          name: 'N14接口是否携带smfSelInfo'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RADIOCAPPAGING:
          name: '是否携带UE Radio Capability for Paging'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SNDPCFRFSP:
          name: '是否携带PcfRfsp'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SNDPEIPSINFO:
          name: 'N14接口是否携带PEIPS信元以及寻呼分组标识'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SNDPRVEDRXINFO:
          name: '是否携带eDRX私有信元'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SNDRATTYPE:
          name: '是否给SMSF携带RATTYPE'
          type: string
          enum:
          - YES
          - NO
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SNDREDCAPIND:
          name: '是否携带RedCap指示'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SUBRSPN2CLASS:
          name: '是否携带N2InformationClass'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_amfsoftparaofbit_list:
      type: items
      properties:
        DT:
          name: '数据类型'
          type: string
          enum:
          - Dw
          - Byte
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DWORDNUM:
          name: 'Dword索引'
          type: integer
          minimum: 1
          maximum: 1500
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VALUE:
          name: '软参记录值'
          type: string
          enum:
          - VALUE_0
          - VALUE_1
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        POSITION:
          name: '比特位'
          type: integer
          minimum: 1
          maximum: 32
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_amfsoftparaofbit_list_1:
      type: items
      properties:
        DT:
          name: '数据类型'
          type: string
          enum:
          - Dw
          - Byte
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DWORDNUM:
          name: 'Dword索引'
          type: integer
          minimum: 1
          maximum: 1500
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VALUE:
          name: '软参记录值'
          type: string
          enum:
          - VALUE_0
          - VALUE_1
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        POSITION:
          name: '比特位'
          type: integer
          minimum: 1
          maximum: 32
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_amfpeerselfunc_list:
      type: items
      properties:
        NFLOCATION:
          name: '支持使用Location的对端NF类型'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    set_licenseswitch_list:
    - LICITEM: 'LKV2URSPAM01'
      SWITCH: ENABLE
    mod_amueplcyctrl_list:
    - SUBRANGE: HOME_USER
      NSGRPID: 0
      ISUEASSOC: YES
      DNNUEPLCYSW: YES
      DNNUEPLCYKEYWD: 'dnn-test'
      DESC: 'Enable UE URSP for Subscribers'
      IMSIPRE: ''
      MSISDNPRE: ''
    set_amfplcyfunc_list:
    - OLDUEPLCY: YES
    set_amfsbicmpt_list:
    - SBITYPE: N14
      OLDPCFID: YES
      OLDUEPLCYURI: YES
      OLDUEPLCYTRIG: YES
      AMPCFNI: ''
      EVTGNBLST: ''
      EVTPERIOD: ''
      HAMPCFID: ''
      N11MSGTYPE: ''
      OLDAMPLCYTRIG: ''
      OLDAMPLCYURI: ''
      OLDHPCFID: ''
      OLDPCFSETID: ''
      OLDSMFSELINFO: ''
      RADIOCAPPAGING: ''
      SNDPCFRFSP: ''
      SNDPEIPSINFO: ''
      SNDPRVEDRXINFO: ''
      SNDRATTYPE: ''
      SNDREDCAPIND: ''
      SUBRSPN2CLASS: ''
    set_amfsoftparaofbit_list:
    - DT: Dw
      DWORDNUM: 68
      VALUE: VALUE_1
      POSITION: 31
    set_amfsoftparaofbit_list_1:
    - DT: Dw
      DWORDNUM: 71
      VALUE: VALUE_1
      POSITION: 25
    set_amfpeerselfunc_list:
    - NFLOCATION: PCF-1
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置AMF的URSP功能。

#### 1.1 进入“MML命令行-UNC”窗口。

#### 1.2 打开License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

#### 1.3 配置应用网络侧规划的AM策略/UE策略的用户群。默认不使用网络侧规划的AM策略/UE策略。

```jinja2
{%- for item in mod_amueplcyctrl_list -%}
    MOD AMUEPLCYCTRL:
    {#- --- 必选参数 --- -#}
    SUBRANGE={{item.SUBRANGE}},
    {#- --- 可选参数 --- -#}
    {%- if item.ISUEASSOC is not none -%}
        ISUEASSOC={{item.ISUEASSOC}},
    {%- endif -%}
    {%- if item.DNNUEPLCYSW is not none -%}
        DNNUEPLCYSW={{item.DNNUEPLCYSW}},
    {%- endif -%}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：SUBRANGE=ALL_USER 时必选 --- -#}
    {%- if item.SUBRANGE == 'ALL_USER' -%}
        NSGRPID={{item.NSGRPID}},
    {%- endif -%}
    {#- --- 条件必选：DNNUEPLCYSW=YES 时必选 --- -#}
    {%- if item.DNNUEPLCYSW == 'YES' -%}
        DNNUEPLCYKEYWD="{{item.DNNUEPLCYKEYWD}}",
    {%- endif -%}
    {#- --- 条件必选：SUBRANGE=IMSI_PREFIX 时必选 --- -#}
    {%- if item.SUBRANGE == 'IMSI_PREFIX' -%}
        IMSIPRE="{{item.IMSIPRE}}",
    {%- endif -%}
    {#- --- 条件必选：SUBRANGE=MSISDN_PREFIX 时必选 --- -#}
    {%- if item.SUBRANGE == 'MSISDN_PREFIX' -%}
        MSISDNPRE="{{item.MSISDNPRE}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 支持基于DNN创建UE策略时，将“DNNUEPLCYSW”设置为“YES”，并提供DNN关键字。

#### 1.4 允许N14接口传递UE策略。

```jinja2
{%- for item in set_amfplcyfunc_list -%}
    SET AMFPLCYFUNC:
    {#- --- 可选参数 --- -#}
    {%- if item.OLDUEPLCY is not none -%}
        OLDUEPLCY={{item.OLDUEPLCY}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.5 允许N14接口消息携带“pcfUePolicyUri”和“uePolicyReqTriggerList”。

```jinja2
{%- for item in set_amfsbicmpt_list -%}
    SET AMFSBICMPT:
    {#- --- 必选参数 --- -#}
    SBITYPE={{item.SBITYPE}},
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：SBITYPE=N14 时可选 --- -#}
    {%- if item.SBITYPE == 'N14' -%}
        {%- if item.OLDPCFID is not none -%}
            OLDPCFID={{item.OLDPCFID}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SBITYPE=N14 时可选 --- -#}
    {%- if item.SBITYPE == 'N14' -%}
        {%- if item.OLDUEPLCYURI is not none -%}
            OLDUEPLCYURI={{item.OLDUEPLCYURI}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SBITYPE=N14 时可选 --- -#}
    {%- if item.SBITYPE == 'N14' -%}
        {%- if item.OLDUEPLCYTRIG is not none -%}
            OLDUEPLCYTRIG={{item.OLDUEPLCYTRIG}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SBITYPE=N14 时可选 --- -#}
    {%- if item.SBITYPE == 'N14' -%}
        {%- if item.AMPCFNI is not none -%}
            AMPCFNI={{item.AMPCFNI}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SBITYPE=N14 时可选 --- -#}
    {%- if item.SBITYPE == 'N14' -%}
        {%- if item.EVTGNBLST is not none -%}
            EVTGNBLST={{item.EVTGNBLST}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SBITYPE=N14 时可选 --- -#}
    {%- if item.SBITYPE == 'N14' -%}
        {%- if item.EVTPERIOD is not none -%}
            EVTPERIOD={{item.EVTPERIOD}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SBITYPE=N15 时可选 --- -#}
    {%- if item.SBITYPE == 'N15' -%}
        {%- if item.HAMPCFID is not none -%}
            HAMPCFID={{item.HAMPCFID}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SBITYPE=N11 时可选 --- -#}
    {%- if item.SBITYPE == 'N11' -%}
        {%- if item.N11MSGTYPE is not none -%}
            N11MSGTYPE={{item.N11MSGTYPE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SBITYPE=N14 时可选 --- -#}
    {%- if item.SBITYPE == 'N14' -%}
        {%- if item.OLDAMPLCYTRIG is not none -%}
            OLDAMPLCYTRIG={{item.OLDAMPLCYTRIG}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SBITYPE=N14 时可选 --- -#}
    {%- if item.SBITYPE == 'N14' -%}
        {%- if item.OLDAMPLCYURI is not none -%}
            OLDAMPLCYURI={{item.OLDAMPLCYURI}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SBITYPE=N14 时可选 --- -#}
    {%- if item.SBITYPE == 'N14' -%}
        {%- if item.OLDHPCFID is not none -%}
            OLDHPCFID={{item.OLDHPCFID}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SBITYPE=N14 时可选 --- -#}
    {%- if item.SBITYPE == 'N14' -%}
        {%- if item.OLDPCFSETID is not none -%}
            OLDPCFSETID={{item.OLDPCFSETID}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SBITYPE=N14 时可选 --- -#}
    {%- if item.SBITYPE == 'N14' -%}
        {%- if item.OLDSMFSELINFO is not none -%}
            OLDSMFSELINFO={{item.OLDSMFSELINFO}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SBITYPE=N14 时可选 --- -#}
    {%- if item.SBITYPE == 'N14' -%}
        {%- if item.RADIOCAPPAGING is not none -%}
            RADIOCAPPAGING={{item.RADIOCAPPAGING}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SBITYPE=N14 时可选 --- -#}
    {%- if item.SBITYPE == 'N14' -%}
        {%- if item.SNDPCFRFSP is not none -%}
            SNDPCFRFSP={{item.SNDPCFRFSP}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SBITYPE=N14 时可选 --- -#}
    {%- if item.SBITYPE == 'N14' -%}
        {%- if item.SNDPEIPSINFO is not none -%}
            SNDPEIPSINFO={{item.SNDPEIPSINFO}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SBITYPE=N14 时可选 --- -#}
    {%- if item.SBITYPE == 'N14' -%}
        {%- if item.SNDPRVEDRXINFO is not none -%}
            SNDPRVEDRXINFO={{item.SNDPRVEDRXINFO}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SBITYPE=N20 时可选 --- -#}
    {%- if item.SBITYPE == 'N20' -%}
        {%- if item.SNDRATTYPE is not none -%}
            SNDRATTYPE={{item.SNDRATTYPE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SBITYPE=N14 时可选 --- -#}
    {%- if item.SBITYPE == 'N14' -%}
        {%- if item.SNDREDCAPIND is not none -%}
            SNDREDCAPIND={{item.SNDREDCAPIND}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：SBITYPE=N50 时可选 --- -#}
    {%- if item.SBITYPE == 'N50' -%}
        {%- if item.SUBRSPN2CLASS is not none -%}
            SUBRSPN2CLASS={{item.SUBRSPN2CLASS}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.6 若希望在UDM故障重选时，AMF支持创建UE策略偶联，请将如下软参值设置为1。

```jinja2
{%- for item in set_amfsoftparaofbit_list -%}
    SET AMFSOFTPARAOFBIT:
    {#- --- 必选参数 --- -#}
    DT={{item.DT}},
    VALUE={{item.VALUE}},
    POSITION={{item.POSITION}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：DT=Dw 时必选 --- -#}
    {%- if item.DT == 'Dw' -%}
        DWORDNUM={{item.DWORDNUM}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.7 若希望在AMF内移动性注册更新和基于N2接口切换后的移动性注册更新流程中创建UE策略偶联，请将如下软参值设置为1。

```jinja2
{%- for item in set_amfsoftparaofbit_list_1 -%}
    SET AMFSOFTPARAOFBIT:
    {#- --- 必选参数 --- -#}
    DT={{item.DT}},
    VALUE={{item.VALUE}},
    POSITION={{item.POSITION}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：DT=Dw 时必选 --- -#}
    {%- if item.DT == 'Dw' -%}
        DWORDNUM={{item.DWORDNUM}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.8 配置AMF支持使用PCF通过Location信元携带的地址进行通信。

```jinja2
{%- for item in set_amfpeerselfunc_list -%}
    SET AMFPEERSELFUNC:
    {#- --- 可选参数 --- -#}
    {%- if item.NFLOCATION is not none -%}
        NFLOCATION={{item.NFLOCATION}},
    {%- endif -%}
    ;
{%- endfor -%}
```

