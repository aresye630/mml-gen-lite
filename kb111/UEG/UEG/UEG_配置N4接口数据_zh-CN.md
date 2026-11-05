---
id: ''
name: 配置N4接口数据
ne_type: UEG
type: feature
description: '**接口介绍**  N4接口是SMF与UPF之间的接口，用于传输SMF和UPF间的控制面及用户面信息，通过该接口使控制面和用户面配合完成用户面规则下发和隧道建立功能。  N4接口协议栈如图1所示。  **图1** N4接口协议栈  * PFCP（Packet Forwarding Control Protocol）：SMF与UPF间控制面的数据转发协议。 * GTP-U（GPRS Tunnelling Protocol for the user plane）：利用隧道协议在骨干网的GSN间传输用户数据，使用隧道协议传输数据，屏蔽上层协议影响，同时提供会话级的双向快速传输通道。GTP协议用户面除数据包外，还包括数据传输出错指示、支持的扩展头列表等用户面传输辅助信令。'
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻+地市共享（连接+计算）","5GC toB 部署边缘站点（站点为“风筝M”，带计算）","UEG初始配置（风筝M）","参考：详细配置指导","配置SMF","配置N4接口数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
**接口介绍**N4接口是SMF与UPF之间的接口，用于传输SMF和UPF间的控制面及用户面信息，通过该接口使控制面和用户面配合完成用户面规则下发和隧道建立功能。N4接口协议栈如图1所示。**图1** N4接口协议栈* PFCP（Packet Forwarding Control Protocol）：SMF与UPF间控制面的数据转发协议。* GTP-U（GPRS Tunnelling Protocol for the user plane）：利用隧道协议在骨干网的GSN间传输用户数据，使用隧道协议传输数据，屏蔽上层协议影响，同时提供会话级的双向快速传输通道。GTP协议用户面除数据包外，还包括数据传输出错指示、支持的扩展头列表等用户面传输辅助信令。

## 必备事项
前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020/MAE客户端或登录OM Portal）。

* 已完成部署组网路由配置。

* 如果本接口采用IPv6组网，则需要开通逻辑接口支持IPv6特性，即加载对应的License项“81203214 LKV3G5V6LI01 逻辑接口支持IPv6”。
* 在双DC部署场景下如果两个DC的UEG内的UPF采用主、备模式组网，SMF需要和两个DC内的UPF FullMesh组网，需要开通FullMesh相关特性，需要加载对应的License项“82209861 LKV3G5CUFM01 CU FullMesh组网”。
* 已经获取网设LLD文档。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_logicip_list:
      type: items
      properties:
        IPVERSION:
          name: '逻辑IP地址类型'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: '配置N4接口的逻辑IP地址。'
          data_source: '参见“水平网设LLD文档 -> 5G Core业务IP对接设计”。'
          pattern: ''
          default: ''
        LOGICIPV4:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VPNINSTNAME:
          name: 'VPN实例名称'
          type: string
          minLength: 1
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DESC:
          name: '描述'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_cpnode_list:
      type: items
      properties:
        CPNODEINDEX:
          name: 'CP节点索引'
          type: integer
          minimum: 0
          maximum: 0
          required: true
          description: '配置控制面SMF的端点信息。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        NODEIDTYPE:
          name: 'CP节点ID类型'
          type: string
          enum:
          - CpIPv4
          - CpIPv6
          - CpFqdn
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        NODEIDIPV4VALUE:
          name: 'CP节点ID类型为IPv4时的IPv4的值'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        CPFUNCTION:
          name: 'CP节点功能'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: '当前产品暂未实现协议定义的负载控制等相关功能，建议配置为0即可。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_cppoint_list:
      type: items
      properties:
        CPPOINTINDEX:
          name: 'CPPOINT索引'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CPNODEINDEX:
          name: 'CPNODE索引'
          type: integer
          minimum: 0
          maximum: 0
          required: true
          description: '一个CP端点归属于一个CP节点，一个CP节点下可以有多个CP端点。该参数用于指定这个CP端点所属的CP节点，只支持CP节点索引固定取值为0。  已通过**ADD CPNODE**配置，可以通过**LST CPNODE**查询。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP版本'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPV4:
          name: 'IPV4值'
          type: string
          maxLength: 15
          required: false
          description: 'CP节点中的IPv4地址和**ADD CPNODE**中的IPv4地址需要相同。'
          data_source: '已配置数据中获取'
          pattern: ''
          default: ''
        VPNNAME:
          name: 'VPN名称'
          type: string
          minLength: 1
          maxLength: 31
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: '_public_'
    add_pnfprofile_list:
      type: items
      properties:
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 1
          maxLength: 36
          required: true
          description: '增加对端UPF实例概述信息。  盒式部署形态下，SMF只连接本DC UEG内的业务网元，不跨UEG与对接DC的业务网元对接。因此这种模式下，仅有一个对端实例。'
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
          description: '-'
          data_source: '固定取值'
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
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: Registered
        FQDN:
          name: '域名'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: '-'
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
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4ADDRESS1:
          name: 'IP地址'
          type: string
          maxLength: 15
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PORT:
          name: '端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: '**配置建议**  N4接口端口没有明确时，使用协议推荐端口8080。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        CAPACITY:
          name: '容量'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: '说明：  双DC组网场景下“容量”参数可以用于配置SMF和UPF的组网模式：  * 负荷分担：无需配置“容量”参数，或者将两个DC UPF的“容量”参数配置相同取值。 * 主备模式：主UPF“容量”参数设置为非0，备UPF的“容量”参数设置为0，这样只有在主UPF故障场景下SMF才会才会选择备UPF。'
          data_source: '全网规划'
          pattern: ''
          default: 100
    add_pnfprofile_list_2:
      type: items
      properties:
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 1
          maxLength: 36
          required: true
          description: '增加对端UPF实例概述信息。  盒式部署形态下，SMF只连接本DC UEG内的业务网元，不跨UEG与对接DC的业务网元对接。因此这种模式下，仅有一个对端实例。'
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
          description: '-'
          data_source: '固定取值'
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
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: Registered
        FQDN:
          name: '域名'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: '-'
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
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4ADDRESS1:
          name: 'IP地址'
          type: string
          maxLength: 15
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        PORT:
          name: '端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: '**配置建议**  N4接口端口没有明确时，使用协议推荐端口8080。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        CAPACITY:
          name: '容量'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: '说明：  双DC组网场景下“容量”参数可以用于配置SMF和UPF的组网模式：  * 负荷分担：无需配置“容量”参数，或者将两个DC UPF的“容量”参数配置相同取值。 * 主备模式：主UPF“容量”参数设置为非0，备UPF的“容量”参数设置为0，这样只有在主UPF故障场景下SMF才会才会选择备UPF。'
          data_source: '全网规划'
          pattern: ''
          default: 100
    add_pnfns_list:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: '配置用户面支持的服务切片信息，可以基于切片选择UPF/GW-U。'
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
        SD:
          name: '切片分类器'
          type: string
          minLength: 0
          maxLength: 8
          required: false
          description: ''
          data_source: '全网规划'
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
          description: '配置对端UPF支持的园区DNN信息，可以基于DNN选择UPF/GW-U。'
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
    add_upnode_list:
      type: items
      properties:
        NFINSTANCENAME:
          name: 'UPF实例名称'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: '已通过命令**ADD PNFPROFILE**配置。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        VPNNAME:
          name: 'VPN名称'
          type: string
          minLength: 1
          maxLength: 31
          required: false
          description: '一个UPF只归属于一个VPN。  UPF的“VPNNAME”需要与**LST CPPOINT**中的查询结果一致。'
          data_source: '全网规划'
          pattern: ''
          default: '_public_'
        PDUESTWITHOUTN9:
          name: '是否支持UPF无N9逻辑接口地址时作为主锚点激活'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: false
          description: '当参数“**PDUESTWITHOUTN9**”配置为“ENABLE”时，SMF选择该UPF作为主锚点时不会判断该UPF是否支持N9接口。'
          data_source: '全网规划'
          pattern: ''
          default: DISABLE
    add_pnfsmfserarea_list:
      type: items
      properties:
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: '配置对端UPF支持的服务区域，可以基于服务区域选择UPF/GW-U。'
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
          data_source: '全网规划'
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
          data_source: '已配置数据中获取'
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
          data_source: '已配置数据中获取'
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
  examples:
    add_logicip_list:
    - IPVERSION: IPv4
      LOGICIPV4: '10.26.0.5'
      VPNINSTNAME: 'VRF_CN'
      DESC: 'FOR N4 Interface'
    - IPVERSION: IPv4
      LOGICIPV4: '10.26.0.6'
      VPNINSTNAME: 'VRF_CN'
      DESC: 'FOR N4 Interface'
    add_cpnode_list:
    - CPNODEINDEX: 0
      NODEIDTYPE: CpIPv4
      NODEIDIPV4VALUE: '10.26.0.5'
      CPFUNCTION: 0
    - CPNODEINDEX: 0
      NODEIDTYPE: CpIPv4
      NODEIDIPV4VALUE: '10.26.0.6'
      CPFUNCTION: 0
    add_cppoint_list:
    - CPPOINTINDEX: 0
      CPNODEINDEX: 0
      IPVERSION: IPv4
      IPV4: '10.26.0.5'
      VPNNAME: 'VRF_CN'
    - CPPOINTINDEX: 0
      CPNODEINDEX: 0
      IPVERSION: IPv4
      IPV4: '10.26.0.6'
      VPNNAME: 'VRF_CN'
    add_pnfprofile_list:
    - NFINSTANCEID: 'UPF_Instance_0'
      NFTYPE: NfUPF
      NFSTATUS: Registered
      FQDN: 'upf01.node.mnc003.mcc123.3gppnetwork.org'
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS1: '192.168.126.10'
      PORT: 8080
      CAPACITY: 1
    - NFINSTANCEID: 'UPF_Instance_1'
      NFTYPE: NfUPF
      NFSTATUS: Registered
      FQDN: 'upf02.node.mnc003.mcc123.3gppnetwork.org'
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS1: '192.168.126.11'
      PORT: 8080
      CAPACITY: 0
    add_pnfprofile_list_2:
    - NFINSTANCEID: 'UPF_Instance_0'
      NFTYPE: NfUPF
      NFSTATUS: Registered
      FQDN: 'upf01.node.mnc003.mcc123.3gppnetwork.org'
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS1: '192.168.126.10'
      PORT: 8080
      CAPACITY: 1
    - NFINSTANCEID: 'UPF_Instance_1'
      NFTYPE: NfUPF
      NFSTATUS: Registered
      FQDN: 'upf02.node.mnc003.mcc123.3gppnetwork.org'
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS1: '192.168.126.11'
      PORT: 8080
      CAPACITY: 1
    add_pnfns_list:
    - INDEX: 3
      NFINSTANCEID: 'UPF_Instance_0'
      SST: 1
      SD: '000001'
    - INDEX: 4
      NFINSTANCEID: 'UPF_Instance_1'
      SST: 1
      SD: '000001'
    add_pnfdnn_list:
    - INDEX: 3
      NFINSTANCEID: 'UPF_Instance_0'
      DNN: 'huawei.com'
      PNFNSINDEX: 3
    - INDEX: 4
      NFINSTANCEID: 'UPF_Instance_1'
      DNN: 'huawei.com'
      PNFNSINDEX: 4
    add_upnode_list:
    - NFINSTANCENAME: 'UPF_Instance_0'
      VPNNAME: 'VRF_CN'
      PDUESTWITHOUTN9: ENABLE
    - NFINSTANCENAME: 'UPF_Instance_1'
      VPNNAME: 'VRF_CN'
      PDUESTWITHOUTN9: ENABLE
    add_pnfsmfserarea_list:
    - NFINSTANCEID: 'UPF_Instance_0'
      SMFSERVINGAREA: 'UPAREA1'
    - NFINSTANCEID: 'UPF_Instance_1'
      SMFSERVINGAREA: 'UPAREA1'
    add_uparea_list:
    - AREANAME: 'UPAREA1'
      AREATYPE: N2TAI
    - AREANAME: 'UPAREA1'
      AREATYPE: N2TAI
    add_upareabindn2tai_list:
    - AREANAME: 'UPAREA1'
      N2BEGINTAI: '12303260101'
      N2ENDTAI: '12303260102'
    - AREANAME: 'UPAREA1'
      N2BEGINTAI: '12303260101'
      N2ENDTAI: '12303260102'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 配置N4接口的IP地址。

#### 1.1 //DC1

```jinja2
{%- for item in add_logicip_list -%}
    ADD LOGICIP:
    {#- --- 必选参数 --- -#}
    IPVERSION={{item.IPVERSION}},
    {#- --- 可选参数 --- -#}
    {%- if item.VPNINSTNAME is not none -%}
        VPNINSTNAME="{{item.VPNINSTNAME}}",
    {%- endif -%}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPv4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv4' -%}
        LOGICIPV4="{{item.LOGICIPV4}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 配置控制面节点实例。

#### 2.1 //DC1

```jinja2
{%- for item in add_cpnode_list -%}
    ADD CPNODE:
    {#- --- 必选参数 --- -#}
    CPNODEINDEX={{item.CPNODEINDEX}},
    NODEIDTYPE={{item.NODEIDTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.CPFUNCTION is not none -%}
        CPFUNCTION={{item.CPFUNCTION}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：NODEIDTYPE=CpIPv4 时必选 --- -#}
    {%- if item.NODEIDTYPE == 'CpIPv4' -%}
        NODEIDIPV4VALUE="{{item.NODEIDIPV4VALUE}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_cppoint_list -%}
    ADD CPPOINT:
    {#- --- 必选参数 --- -#}
    CPPOINTINDEX={{item.CPPOINTINDEX}},
    CPNODEINDEX={{item.CPNODEINDEX}},
    IPVERSION={{item.IPVERSION}},
    {#- --- 可选参数 --- -#}
    {%- if item.VPNNAME is not none -%}
        VPNNAME="{{item.VPNNAME}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPv4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv4' -%}
        IPV4="{{item.IPV4}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置用户面节点实例。

### 可根据实际组网场景选择。

#### 3.1 UPF主备组网场景下，配置Profile实例。

##### 3.1.1 //DC1

```jinja2
{%- if is_scenario_upf_master_backup -%}
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
        {%- if item.CAPACITY is not none -%}
            CAPACITY={{item.CAPACITY}},
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
{%- endif -%}
```

#### 3.2 UPF负荷分担组网场景下，配置Profile实例。

#### UPF负荷分担容灾组网时，园区应急SMF仅连接本DC的UPF。

##### 3.2.1 //DC1

```jinja2
{%- if is_scenario_upf_load_sharing -%}
    {%- for item in add_pnfprofile_list_2 -%}
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
        {%- if item.CAPACITY is not none -%}
            CAPACITY={{item.CAPACITY}},
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
{%- endif -%}
```

#### 3.3 配置用户面节点支持的切片与DNN信息，SMF可以基于切片、DNN选择UPF。

##### 3.3.1 //DC1

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

### 4 配置用户面节点的位置特征和分流能力。

#### 4.1 //DC1

```jinja2
{%- for item in add_upnode_list -%}
    ADD UPNODE:
    {#- --- 必选参数 --- -#}
    NFINSTANCENAME="{{item.NFINSTANCENAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.VPNNAME is not none -%}
        VPNNAME="{{item.VPNNAME}}",
    {%- endif -%}
    {%- if item.PDUESTWITHOUTN9 is not none -%}
        PDUESTWITHOUTN9={{item.PDUESTWITHOUTN9}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 配置用户面支持的为SMF提供服务区域的信息，并将服务区与位置区TAI绑定，SMF可以基于位置信息选择UPF。

#### 5.1 //DC1

```jinja2
{%- for item in add_pnfsmfserarea_list -%}
    ADD PNFSMFSERAREA:
    {#- --- 必选参数 --- -#}
    NFINSTANCEID="{{item.NFINSTANCEID}}",
    SMFSERVINGAREA="{{item.SMFSERVINGAREA}}",
    ;
{%- endfor -%}
```

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

