---
id: ''
name: 配置SMF和“UL CL UPF+辅锚点UPF”对接
ne_type: UEG
type: feature
description: 本操作指导介绍部署基于预定义规则的分流策略控制特性的操作过程。  3GPP针对于5G用户面的数据分流定义了UL CL(Uplink Classifier)功能，通过上行分流器（即UL CL UPF）实现根据用户业务流特征将访问本地网络的数据分流到本地DN，将访问Internet数据分流到公网，从而实现对用户本地业务数据的分流控制。  当UE会话激活或位置发生变化时，SMF基于用户的DNN、位置区以及DNAI（Data Network Access Identifier）等信息判定是否需要将用户数据分流到本地DN，如需分流则为用户选择UL CL UPF和辅锚点UPF，将UL CL UPF和辅锚点UPF插入当前的会话中并对UL CL UPF下发相应的分流规则来实现对用户本地数据的分流控制。  DNAI（DN Access Identifier）是3GPP定义用于标识DN网络接入点。DNN表示DN的名称，DNAI则表示DN的具体网络接入点，带有一定的物理属性。例如网络中规划了一个DN，其DNN为abc，该DN有A城和B城两个接入点，则A、B城对应的DNAI可以命名为abc.A和abc.B。在UL CL分流场景下，DNAI则用于标识边缘侧的PDU会话锚点，即辅锚点UPF。  如前所述本特性仅支持UL CL UPF和辅锚点UPF合一部署场景，前面原理描述中主锚点PSA0 UPF和“UL CL UPF+辅锚点UPF”是分离部署的。但是在现网实际使用过程中可能出现“UL CL UPF+辅锚点UPF”和主锚点PSA0 UPF共部署场景，华为SMF支持和这种UL CL和主、辅锚点UPF合一部署形态的UPF进行对接并实现UL CL分流，详细如表1所示。  **表1** SMF与UL CL和主、辅锚点UPF共部署形态的UPF的组网对接介绍  | 场景 | 原理描述 | | --- | --- | | 为某工业园区建分流网络，希望最大限度节约成本，将UL CL和主、辅锚点UPF共部署。接入园区的用户访问公网以及本地DN都使用该合一形态的UPF。 | 此时SMF需要和UPF间创建两个N4会话，一个主锚点N4会话，一个辅锚点N4会话。UPF根据SMF下发的DNAI和本地规划的VPN的绑定关系来识别辅锚点N4会话。  SMF上需要打开**ADD UPNODE**命令中“ UPF共享开关”才能使能该使用场景。同时还需要配置命令**ADD VIRTUALUPFID**和**ADD VUPFIDBINDDNAI**来指定辅锚点会话的DNAI。 |
tags: []
risk_level: ''
doc_source: ["业务配置","风筝S","MEC 特性指南（风筝S）","UNC特性指南","WSFD-108002 基于预定义规则的分流策略控制","配置SMF和“UL CL UPF+辅锚点UPF”对接"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
本操作指导介绍部署基于预定义规则的分流策略控制特性的操作过程。3GPP针对于5G用户面的数据分流定义了UL CL(Uplink Classifier)功能，通过上行分流器（即UL CL UPF）实现根据用户业务流特征将访问本地网络的数据分流到本地DN，将访问Internet数据分流到公网，从而实现对用户本地业务数据的分流控制。当UE会话激活或位置发生变化时，SMF基于用户的DNN、位置区以及DNAI（Data Network Access Identifier）等信息判定是否需要将用户数据分流到本地DN，如需分流则为用户选择UL CL UPF和辅锚点UPF，将UL CL UPF和辅锚点UPF插入当前的会话中并对UL CL UPF下发相应的分流规则来实现对用户本地数据的分流控制。DNAI（DN Access Identifier）是3GPP定义用于标识DN网络接入点。DNN表示DN的名称，DNAI则表示DN的具体网络接入点，带有一定的物理属性。例如网络中规划了一个DN，其DNN为abc，该DN有A城和B城两个接入点，则A、B城对应的DNAI可以命名为abc.A和abc.B。在UL CL分流场景下，DNAI则用于标识边缘侧的PDU会话锚点，即辅锚点UPF。如前所述本特性仅支持UL CL UPF和辅锚点UPF合一部署场景，前面原理描述中主锚点PSA0 UPF和“UL CL UPF+辅锚点UPF”是分离部署的。但是在现网实际使用过程中可能出现“UL CL UPF+辅锚点UPF”和主锚点PSA0 UPF共部署场景，华为SMF支持和这种UL CL和主、辅锚点UPF合一部署形态的UPF进行对接并实现UL CL分流，详细如表1所示。**表1** SMF与UL CL和主、辅锚点UPF共部署形态的UPF的组网对接介绍| 场景 | 原理描述 || --- | --- || 为某工业园区建分流网络，希望最大限度节约成本，将UL CL和主、辅锚点UPF共部署。接入园区的用户访问公网以及本地DN都使用该合一形态的UPF。 | 此时SMF需要和UPF间创建两个N4会话，一个主锚点N4会话，一个辅锚点N4会话。UPF根据SMF下发的DNAI和本地规划的VPN的绑定关系来识别辅锚点N4会话。  SMF上需要打开**ADD UPNODE**命令中“ UPF共享开关”才能使能该使用场景。同时还需要配置命令**ADD VIRTUALUPFID**和**ADD VUPFIDBINDDNAI**来指定辅锚点会话的DNAI。 |

## 必备事项
前提条件

请仔细阅读WSFD-108002 基于预定义规则的分流策略控制特性概述特性原理概述。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_pnfprofile_list:
      type: items
      properties:
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 1
          maxLength: 36
          required: true
          description: '**SMF本端添加UL CL UPF**。'
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
          data_source: ''
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
          data_source: ''
          pattern: ''
          default: ''
    add_pnfns_list:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: '**配置用户面支持的服务切片信息**。'
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
          data_source: ''
          pattern: ''
          default: ''
        SD:
          name: '切片分类器'
          type: string
          minLength: 0
          maxLength: 8
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'FFFFFF'
    add_pnfdnn_list:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: '**配置“UL CL UPF+辅锚点UPF”的DNN属性，用于在用户会话激活时基于用户的DNN选择UL CL UPF。**'
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
          data_source: ''
          pattern: ''
          default: ''
    add_pnfdnai_list:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: '**为“UL CL UPF+辅锚点UPF”添加DNAI信息。**'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 1
          maxLength: 36
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        DNAI:
          name: '数据网络访问标识'
          type: string
          minLength: 0
          maxLength: 50
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        PNFDNNINDEX:
          name: '对端NF的DNN索引'
          type: integer
          minimum: 0
          maximum: 4294967295
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
          description: '**配置UL CL UPF的属性。**  “UPF共享开关”用于控制UPF是否作为主、辅锚点共享UPF使用。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        LOCATION:
          name: 'UP位置特征'
          type: string
          enum:
          - Local
          - Central
          - CentralOnly
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: Central
        UPFUNCTION:
          name: 'UP支持功能'
          type: string
          enum:
          - None
          - UlClAndBp
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: None
        SHAREDUPFSW:
          name: 'UPF共享开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: DISABLE
    add_virtualupfid_list:
      type: items
      properties:
        UPFINSTANCEID:
          name: 'UPF实例标识'
          type: string
          minLength: 1
          maxLength: 36
          required: true
          description: '配置虚拟UPF实例标识和DNAI的绑定关系。  UPF作为主、辅锚点和UL CL共部署体时通过将UPF划分为虚拟UPF，并和DNAI绑定来辅助用户面区分不同的辅锚点。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        VUPFINSTANCEID:
          name: '虚拟UPF实例标识'
          type: string
          minLength: 1
          maxLength: 36
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_vupfidbinddnai_list:
      type: items
      properties:
        VUPFINSTANCEID:
          name: '虚拟UPF实例标识'
          type: string
          minLength: 1
          maxLength: 36
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        DNAI:
          name: '数据网络访问标识'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_uparea_list:
      type: items
      properties:
        AREANAME:
          name: 'UP位置区名称'
          type: string
          minLength: 1
          maxLength: 255
          required: true
          description: '**配置用于SMF本端判定UL CL UPF归属区域的区域类型，如TA类型。**'
          data_source: '全网规划'
          pattern: ''
          default: ''
        AREATYPE:
          name: 'AREA类型'
          type: string
          enum:
          - S1TAI
          - N2TAI
          - LAI
          required: true
          description: ''
          data_source: ''
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
          description: '**为UPAREA1添加区域范围。**'
          data_source: '全网规划'
          pattern: ''
          default: ''
        N2BEGINTAI:
          name: 'N2TAI范围开始值'
          type: string
          minLength: 11
          maxLength: 12
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        N2ENDTAI:
          name: 'N2TAI范围结束值'
          type: string
          minLength: 11
          maxLength: 12
          required: true
          description: ''
          data_source: ''
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
          description: '**SMF本端配置UL CL UPF所覆盖的区域，用于在用户会话激活时基于用户位置区选择UL CL UPF。**'
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
    add_pnftai_list:
      type: items
      properties:
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 1
          maxLength: 50
          required: true
          description: '配置园区UPF覆盖的TAI区域信息。  **ADD PNFTAI**用于单个TAI的配置，**ADD PNFTAIRANGE**则可用来添加一个TAI范围。具体使用**ADD PNFTAI**还是**ADD PNFTAIRANGE**取决于园区范围的分布情况。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        TAI:
          name: '跟踪区标识'
          type: string
          minLength: 1
          maxLength: 50
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_pnftairange_list:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: ''
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
        MCC:
          name: '移动国家码'
          type: string
          minLength: 3
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MNC:
          name: '移动网号'
          type: string
          minLength: 2
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        QUERYTYPE:
          name: '查询方式'
          type: string
          enum:
          - START_END
          - PATTERN
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RANGESTART:
          name: '起始号段'
          type: string
          minLength: 4
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        RANGEEND:
          name: '终止号段'
          type: string
          minLength: 4
          maxLength: 6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_iupfapndpmode_list:
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
  examples:
    add_pnfprofile_list:
    - NFINSTANCEID: 'UPF_Instance_0'
      NFTYPE: NfUPF
      NFSTATUS: Registered
      FQDN: 'upf00.node.mnc003.mcc123.3gppnetwork.org'
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS1: '192.168.126.11'
    add_pnfns_list:
    - INDEX: 3
      NFINSTANCEID: 'UPF_Instance_0'
      SST: 1
      SD: '000001'
    add_pnfdnn_list:
    - INDEX: 3
      NFINSTANCEID: 'UPF_Instance_0'
      DNN: 'Huawei1.com'
    add_pnfdnai_list:
    - INDEX: 1
      NFINSTANCEID: 'UPF_Instance_0'
      DNAI: 'testdnai'
      PNFDNNINDEX: 3
    add_upnode_list:
    - NFINSTANCENAME: 'UPF_Instance_0'
      LOCATION: Local
      UPFUNCTION: UlClAndBp
      SHAREDUPFSW: ENABLE
    add_virtualupfid_list:
    - UPFINSTANCEID: 'UPF_Instance_0'
      VUPFINSTANCEID: 'v_UPF_Instance_0'
    add_vupfidbinddnai_list:
    - VUPFINSTANCEID: 'v_UPF_Instance_0'
      DNAI: 'testdnai'
    add_uparea_list:
    - AREANAME: 'UPAREA1'
      AREATYPE: N2TAI
    add_upareabindn2tai_list:
    - AREANAME: 'UPAREA1'
      N2BEGINTAI: '12303260101'
      N2ENDTAI: '12303260103'
    add_pnfsmfserarea_list:
    - NFINSTANCEID: 'UPF_Instance_0'
      SMFSERVINGAREA: 'UPAREA1'
    add_pnftai_list:
    - NFINSTANCEID: 'UPF_Instance_0'
      TAI: '12303260105'
    add_pnftairange_list:
    - INDEX: 1
      NFINSTANCEID: 'UPF_Instance_0'
      MCC: '460'
      MNC: '03'
      QUERYTYPE: START_END
      RANGESTART: '12303260101'
      RANGEEND: '12303260103'
    add_iupfapndpmode_list:
    - APN: ''
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 **SMF本端添加UL CL UPF**。

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

### 3 **配置用户面支持的服务切片信息**。

```jinja2
{%- for item in add_pnfns_list -%}
    ADD PNFNS:
    {#- --- 必选参数 --- -#}
    INDEX={{item.INDEX}},
    NFINSTANCEID="{{item.NFINSTANCEID}}",
    SST={{item.SST}},
    {#- --- 可选参数 --- -#}
    {%- if item.SD is not none -%}
        SD="{{item.SD}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 **配置UL CL UPF的DNN属性**。

```jinja2
{%- for item in add_pnfdnn_list -%}
    ADD PNFDNN:
    {#- --- 必选参数 --- -#}
    INDEX={{item.INDEX}},
    NFINSTANCEID="{{item.NFINSTANCEID}}",
    DNN="{{item.DNN}}",
    ;
{%- endfor -%}
```

### 5 **为UL CL UPF添加DNAI信息。**

```jinja2
{%- for item in add_pnfdnai_list -%}
    ADD PNFDNAI:
    {#- --- 必选参数 --- -#}
    INDEX={{item.INDEX}},
    NFINSTANCEID="{{item.NFINSTANCEID}}",
    {#- --- 可选参数 --- -#}
    {%- if item.DNAI is not none -%}
        DNAI="{{item.DNAI}}",
    {%- endif -%}
    {%- if item.PNFDNNINDEX is not none -%}
        PNFDNNINDEX={{item.PNFDNNINDEX}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 6 **配置UL CL UPF的属性。**

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
    {%- if item.SHAREDUPFSW is not none -%}
        SHAREDUPFSW={{item.SHAREDUPFSW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 7 **（可选）配置虚拟UPF实例标识和DNAI的绑定关系。**如果UPF为主、辅锚点共部署实体，可配置此步骤。

#### 7.1 **配置虚拟UPF实例**。

```jinja2
{%- if is_optional_virtual_upf_dnai_binding -%}
    {%- for item in add_virtualupfid_list -%}
        ADD VIRTUALUPFID:
        {#- --- 必选参数 --- -#}
        UPFINSTANCEID="{{item.UPFINSTANCEID}}",
        VUPFINSTANCEID="{{item.VUPFINSTANCEID}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 7.2 **配置虚拟UPF实例和DNAI的绑定关系。**

```jinja2
{%- if is_optional_virtual_upf_dnai_binding -%}
    {%- for item in add_vupfidbinddnai_list -%}
        ADD VUPFIDBINDDNAI:
        {#- --- 必选参数 --- -#}
        DNAI="{{item.DNAI}}",
        VUPFINSTANCEID="{{item.VUPFINSTANCEID}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

### 8 **（可选）配置UPF服务区域。**如果园区UPF规划了UPF服务区域，可通过此步骤绑定其对应的TAI。

#### 8.1 **配置用于SMF本端判定UL CL UPF归属区域的区域类型**。

```jinja2
{%- if is_optional_upf_service_area and is_scenario_upf_service_area_planned -%}
    {%- for item in add_uparea_list -%}
        ADD UPAREA:
        {#- --- 必选参数 --- -#}
        AREANAME="{{item.AREANAME}}",
        AREATYPE={{item.AREATYPE}},
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 8.2 **配置UL CL UPF归属区域对应的区域范围。**

```jinja2
{%- if is_optional_upf_service_area and is_scenario_upf_service_area_planned -%}
    {%- for item in add_upareabindn2tai_list -%}
        ADD UPAREABINDN2TAI:
        {#- --- 必选参数 --- -#}
        AREANAME="{{item.AREANAME}}",
        N2BEGINTAI="{{item.N2BEGINTAI}}",
        N2ENDTAI="{{item.N2ENDTAI}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 8.3 **SMF本端配置UL CL UPF所覆盖的区域**。

```jinja2
{%- if is_optional_upf_service_area and is_scenario_upf_service_area_planned -%}
    {%- for item in add_pnfsmfserarea_list -%}
        ADD PNFSMFSERAREA:
        {#- --- 必选参数 --- -#}
        NFINSTANCEID="{{item.NFINSTANCEID}}",
        SMFSERVINGAREA="{{item.SMFSERVINGAREA}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

### 9 **（可选）配置园区UPF覆盖的TAI区域信息。**如果园区UPF未规划UPF服务区域，可通过此步骤添加其对应的TAI。

#### 9.1 （可选）园区范围处于某单个TAI内，配置园区UPF和TAI的关系。

```jinja2
{%- if is_optional_campus_upf_tai_info and is_scenario_upf_service_area_unplanned and is_scenario_single_tai -%}
    {%- for item in add_pnftai_list -%}
        ADD PNFTAI:
        {#- --- 必选参数 --- -#}
        NFINSTANCEID="{{item.NFINSTANCEID}}",
        TAI="{{item.TAI}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 9.2 （可选）园区范围跨了若干个TAI，配置园区UPF和TAI范围的关系。

```jinja2
{%- if is_optional_campus_upf_tai_info and is_scenario_upf_service_area_unplanned and is_scenario_multi_tai -%}
    {%- for item in add_pnftairange_list -%}
        ADD PNFTAIRANGE:
        {#- --- 必选参数 --- -#}
        QUERYTYPE={{item.QUERYTYPE}},
        MNC="{{item.MNC}}",
        MCC="{{item.MCC}}",
        INDEX={{item.INDEX}},
        NFINSTANCEID="{{item.NFINSTANCEID}}",
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：QUERYTYPE=START_END 时必选 --- -#}
        {%- if item.QUERYTYPE == 'START_END' -%}
            RANGEEND="{{item.RANGEEND}}",
        {%- endif -%}
        {#- --- 条件必选：QUERYTYPE=START_END 时必选 --- -#}
        {%- if item.QUERYTYPE == 'START_END' -%}
            RANGESTART="{{item.RANGESTART}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 10 **（可选）用户在园区外通过专用DNN访问园区业务时，若不允许插入I-UPF对数据报文进行转接，可配置专用DNN下不允许插入I-UPF**。

```jinja2
{%- if is_optional_no_iupf_insertion -%}
    {%- for item in add_iupfapndpmode_list -%}
        ADD IUPFAPNDPMODE:
        {#- --- 必选参数 --- -#}
        APN="{{item.APN}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

### **NGDEPLOYMODE**参数若设置为NOIUPF，会导致终端移动到园区外时拒绝接入。

