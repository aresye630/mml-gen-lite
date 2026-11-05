---
id: ''
name: 配置N26接口数据
ne_type: UEG
type: feature
description: 当运营商在部署分组交换网，新增MME时，在配置完成MME到AMF的路由数据后，可通过配置N26接口数据建立MME到AMF的逻辑连接。  N26接口是AMF与MME之间的接口，提供AMF与MME之间的信令消息隧道，用于协助完成5G网络和LTE网络之间的互操作。  **图1** N26接口协议栈  MME上N26接口与S10接口共用一个S10接口实现，而AMF上N26接口与MME上的N26接口IP地址可以合一配置，也可以独立配置。  * 合一配置场景下，AMF上的N26接口配置复用MME上N26接口的数据配置。如果MME上已经完成N26接口配置，则AMF上无需执行N26接口配置，可执行后续MME选择参数等必配内容。接口IP地址使用MME的**ADD GTPCLE**配置。 * 独立配置场景下，需要分别完成AMF上N26接口配置和MME上N26接口的数据配置。AMF上N26接口的IP地址使用**ADD GTPCLEGRPMEM**配置，MME上N26接口的IP地址使用**ADD GTPCLE**配置。  以下配置数据以及步骤均以UEG双DC组网场景的配置规划为例进行介绍。  双DC组网场景下，MME不仅需要和本DC内的AMF对接，也需要和另外一个DC的AMF对接。
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝L”，入驻式）","UEG初始配置（风筝L）","参考：详细配置指导","配置MME","配置N26接口数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
当运营商在部署分组交换网，新增MME时，在配置完成MME到AMF的路由数据后，可通过配置N26接口数据建立MME到AMF的逻辑连接。N26接口是AMF与MME之间的接口，提供AMF与MME之间的信令消息隧道，用于协助完成5G网络和LTE网络之间的互操作。**图1** N26接口协议栈MME上N26接口与S10接口共用一个S10接口实现，而AMF上N26接口与MME上的N26接口IP地址可以合一配置，也可以独立配置。* 合一配置场景下，AMF上的N26接口配置复用MME上N26接口的数据配置。如果MME上已经完成N26接口配置，则AMF上无需执行N26接口配置，可执行后续MME选择参数等必配内容。接口IP地址使用MME的**ADD GTPCLE**配置。* 独立配置场景下，需要分别完成AMF上N26接口配置和MME上N26接口的数据配置。AMF上N26接口的IP地址使用**ADD GTPCLEGRPMEM**配置，MME上N26接口的IP地址使用**ADD GTPCLE**配置。以下配置数据以及步骤均以UEG双DC组网场景的配置规划为例进行介绍。双DC组网场景下，MME不仅需要和本DC内的AMF对接，也需要和另外一个DC的AMF对接。

## 必备事项
前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020/MAE客户端或登录OM Portal）。
* 已完成组网路由配置。

* 如果本接口采用IPv6组网，则需要开通逻辑接口支持IPv6特性，即加载对应的License项“81203214 LKV3G5V6LI01 逻辑接口支持IPv6”。
* 已经获取网设LLD文档。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    add_serviceip_list:
      type: items
      properties:
        IPVERSION:
          name: 'IP版本'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: '配置业务IP参数'
          data_source: '参见“水平网设LLD文档 ”。'
          pattern: ''
          default: IPv4
        SERVICEIPV4:
          name: '业务IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: '-'
          data_source: ''
          pattern: ''
          default: ''
        VPNINSTNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: 'UEG风筝形态内部接口组网时，使用园区统一规划的VPN。'
          data_source: ''
          pattern: ''
          default: ''
    add_gtpcle_list:
      type: items
      properties:
        GROUPID:
          name: '组号'
          type: integer
          minimum: 0
          maximum: 32
          required: false
          description: '配置GTP-C本地实体。'
          data_source: ''
          pattern: ''
          default: 0
        IPTYPE:
          name: 'IP地址类型'
          type: string
          enum:
          - TPTADDR_TYPE_IPV4
          - TPTADDR_TYPE_IPV6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LEIPV4:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VPNNAME:
          name: 'VPN名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_ugtp_list:
      type: items
      properties:
        ICI:
          name: '空闲计数器扫描间隔（秒）'
          type: integer
          minimum: 60
          maximum: 1800
          required: false
          description: '配置GTP路径管理参数。'
          data_source: ''
          pattern: ''
          default: ''
        SSI:
          name: 'SM信令路径空闲计数器'
          type: integer
          minimum: 10
          maximum: 200
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MSI:
          name: 'MM信令路径空闲计数器'
          type: integer
          minimum: 10
          maximum: 200
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PATHVERCHKINT:
          name: '路径版本探测扫描周期（分钟）'
          type: integer
          minimum: 1
          maximum: 2400
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_gtpcle_list_2:
      type: items
      properties:
        GROUPID:
          name: '组号'
          type: integer
          minimum: 0
          maximum: 32
          required: false
          description: '配置GTP-C本地实体。'
          data_source: ''
          pattern: ''
          default: 0
        IPTYPE:
          name: 'IP地址类型'
          type: string
          enum:
          - TPTADDR_TYPE_IPV4
          - TPTADDR_TYPE_IPV6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LEIPV4:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VPNNAME:
          name: 'VPN名称'
          type: string
          maxLength: 31
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_ugtp_list_2:
      type: items
      properties:
        ICI:
          name: '空闲计数器扫描间隔（秒）'
          type: integer
          minimum: 60
          maximum: 1800
          required: false
          description: '配置GTP路径管理参数。'
          data_source: ''
          pattern: ''
          default: ''
        SSI:
          name: 'SM信令路径空闲计数器'
          type: integer
          minimum: 10
          maximum: 200
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MSI:
          name: 'MM信令路径空闲计数器'
          type: integer
          minimum: 10
          maximum: 200
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PATHVERCHKINT:
          name: '路径版本探测扫描周期（分钟）'
          type: integer
          minimum: 1
          maximum: 2400
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_gtpcintfattr_list:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - SPECIAL_IMSIPRE
          - SPECIAL_NOID
          required: true
          description: '配置N26接口分离。'
          data_source: ''
          pattern: ''
          default: ''
        INTFTP:
          name: '接口类型'
          type: string
          enum:
          - ALL_INTERFACE
          - GN-GGSN/GP
          - GN-SGSN/S16
          - S10
          - S11
          - S3
          - S4
          - SV
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GRPID:
          name: '组号'
          type: integer
          minimum: 1
          maximum: 32
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_ipv4dnsh_list:
      type: items
      properties:
        HSINDEX:
          name: '主机名索引'
          type: integer
          minimum: 1
          maximum: 1024
          required: true
          description: '* 配置AMF的解析数据。 * 如果运营商在DNS Server上配置域名解析，不需要配置本地Hostfile方式，则不需要配置****ADD IPV4DNSH****和****ADD DNSN****。 * 如果采用IPv6组网，则使用****ADD IPV6DNSH****命令替代****ADD IPV4DNSH****命令。'
          data_source: ''
          pattern: ''
          default: ''
        HOSTNAME:
          name: '主机名'
          type: string
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ADDRSECTION:
          name: '地址区间号'
          type: string
          enum:
          - SECTION1
          - SECTION2
          - SECTION3
          - SECTION4
          - SECTION5
          - SECTION6
          - SECTION7
          - SECTION8
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4ADDR1:
          name: 'IPv4地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4ADDR2:
          name: 'IPv4地址2'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_dnsn_list:
      type: items
      properties:
        FQDN:
          name: 'FQDN'
          type: string
          maxLength: 255
          required: true
          description: '-'
          data_source: ''
          pattern: ''
          default: ''
        HSINDEX:
          name: '主机名索引'
          type: integer
          minimum: 1
          maximum: 2048
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENTITY:
          name: '网元类型'
          type: string
          enum:
          - AMF
          - GGSN
          - IWS
          - MME
          - MSC
          - PGW
          - SGSN
          - SGW
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        INTYPE:
          name: '接口类型'
          type: string
          enum:
          - Gn
          - Gp
          - N26
          - S10
          - S102
          - S11
          - S16
          - S3
          - S4
          - S5
          - S8
          - Sdup
          - Sv
          required: true
          description: 'MME上N26接口与S10接口共用一个S10接口实现。'
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: '-'
          data_source: ''
          pattern: ''
          default: 0
        WEIGHT:
          name: '权重'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 100
    add_ipv4dnsh_list_2:
      type: items
      properties:
        HSINDEX:
          name: '主机名索引'
          type: integer
          minimum: 1
          maximum: 1024
          required: true
          description: '* 配置AMF的解析数据。 * 如果运营商在DNS Server上配置域名解析，不需要配置本地Hostfile方式，则不需要配置****ADD IPV4DNSH****和****ADD DNSN****。 * 如果采用IPv6组网，则使用****ADD IPV6DNSH****命令替代****ADD IPV4DNSH****命令。'
          data_source: ''
          pattern: ''
          default: ''
        HOSTNAME:
          name: '主机名'
          type: string
          maxLength: 255
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ADDRSECTION:
          name: '地址区间号'
          type: string
          enum:
          - SECTION1
          - SECTION2
          - SECTION3
          - SECTION4
          - SECTION5
          - SECTION6
          - SECTION7
          - SECTION8
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4ADDR1:
          name: 'IPv4地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4ADDR2:
          name: 'IPv4地址2'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_dnsn_list_4:
      type: items
      properties:
        FQDN:
          name: 'FQDN'
          type: string
          maxLength: 255
          required: true
          description: '-'
          data_source: ''
          pattern: ''
          default: ''
        HSINDEX:
          name: '主机名索引'
          type: integer
          minimum: 1
          maximum: 2048
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENTITY:
          name: '网元类型'
          type: string
          enum:
          - AMF
          - GGSN
          - IWS
          - MME
          - MSC
          - PGW
          - SGSN
          - SGW
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        INTYPE:
          name: '接口类型'
          type: string
          enum:
          - Gn
          - Gp
          - N26
          - S10
          - S102
          - S11
          - S16
          - S3
          - S4
          - S5
          - S8
          - Sdup
          - Sv
          required: true
          description: 'MME上N26接口与S10接口共用一个S10接口实现。'
          data_source: ''
          pattern: ''
          default: ''
        PRIORITY:
          name: '优先级'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: '-'
          data_source: ''
          pattern: ''
          default: 0
        WEIGHT:
          name: '权重'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 100
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
    set_softparaofbit_list:
      type: items
      properties:
        DT:
          name: '参数类型'
          type: string
          enum:
          - BYTE
          - BYTE_EX
          - BYTE_EX_B
          - DWORD
          - DWORD_EX
          - DWORD_EX_B
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PARANUM:
          name: '参数索引'
          type: integer
          minimum: 1
          maximum: 512
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VALUE:
          name: '参数值'
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
    add_n26iwkplcy_list:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - FOREIGN_USER
          - HOME_USER
          - IMSI_PREFIX
          required: true
          description: '配置LTE和5G网络互操作策略。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IS5GCALLOW:
          name: '是否支持接入5GC'
          type: string
          enum:
          - NO
          - YES
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ISNRALLOW:
          name: '是否允许接入5GS的NR'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: YES
        SMFSELPLCY:
          name: '融合SMF+PGW-C选择策略'
          type: string
          enum:
          - CNR
          - N1CAP
          - N1CAP_CNR
          - RESV_PLCY1
          - RESV_PLCY2
          - RESV_PLCY3
          - RESV_PLCY4
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: N1CAP_CNR
    set_dns_list:
      type: items
      properties:
        NON5GSEL:
          name: 'NON5GSEL'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_s1cmpt_list:
      type: items
      properties:
        NRRIN5GS:
          name: '是否携带NR Restriction in 5GS信元'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: '配置S1接口兼容性参数。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        CNR:
          name: '是否携带Core Network Type Restrictions信元'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_mmecharact_list:
      type: items
      properties:
        RANGE:
          name: '对端设备范围'
          type: string
          enum:
          - ALL_MME
          - COMB_AMF
          - SPECIAL_MME
          required: true
          description: '增加对端MME属性信息，配置S10接口兼容性参数。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        UENRSECCAP:
          name: '是否携带UE NR安全能力'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: NO
    set_softparaofbit_list_2:
      type: items
      properties:
        DT:
          name: '参数类型'
          type: string
          enum:
          - BYTE
          - BYTE_EX
          - BYTE_EX_B
          - DWORD
          - DWORD_EX
          - DWORD_EX_B
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PARANUM:
          name: '参数索引'
          type: integer
          minimum: 1
          maximum: 512
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VALUE:
          name: '参数值'
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
  examples:
    add_serviceip_list:
    - IPVERSION: IPv4
      SERVICEIPV4: '192.168.140.17'
      VPNINSTNAME: 'VPN_CN'
    - IPVERSION: IPv4
      SERVICEIPV4: '192.168.140.18'
      VPNINSTNAME: 'VPN_CN'
    add_gtpcle_list:
    - GROUPID: 0
      IPTYPE: TPTADDR_TYPE_IPV4
      LEIPV4: '192.168.140.17'
      VPNNAME: 'VPN_CN'
    - GROUPID: 0
      IPTYPE: TPTADDR_TYPE_IPV4
      LEIPV4: '192.168.140.18'
      VPNNAME: 'VPN_CN'
    set_ugtp_list:
    - ICI: 180
      SSI: 60
      MSI: 60
      PATHVERCHKINT: 60
    - ICI: 180
      SSI: 60
      MSI: 60
      PATHVERCHKINT: 60
    add_gtpcle_list_2:
    - GROUPID: 3
      IPTYPE: TPTADDR_TYPE_IPV4
      LEIPV4: '192.168.140.17'
      VPNNAME: 'VPN_CN'
    - GROUPID: 3
      IPTYPE: TPTADDR_TYPE_IPV4
      LEIPV4: '192.168.140.18'
      VPNNAME: 'VPN_CN'
    set_ugtp_list_2:
    - ICI: 180
      SSI: 60
      MSI: 60
      PATHVERCHKINT: 60
    - ICI: 180
      SSI: 60
      MSI: 60
      PATHVERCHKINT: 60
    add_gtpcintfattr_list:
    - SUBRANGE: ALL_USER
      INTFTP: S10
      GRPID: 3
    - SUBRANGE: ALL_USER
      INTFTP: S10
      GRPID: 3
    add_ipv4dnsh_list:
    - HSINDEX: 4
      HOSTNAME: 'topon.eth4.mmec12.mmegi8001.mme'
      ADDRSECTION: SECTION1
      IPV4ADDR1: '10.10.1.1'
      IPV4ADDR2: '10.10.1.2'
    - HSINDEX: 4
      HOSTNAME: 'topon.eth4.mmec14.mmegi8001.mme'
      ADDRSECTION: SECTION1
      IPV4ADDR1: '10.10.1.1'
      IPV4ADDR2: '10.10.1.2'
    add_dnsn_list:
    - FQDN: 'MMEC12.MMEGI8001.MME.EPC.MNC001.MCC123.3GPPNETWORK.ORG'
      HSINDEX: 4
      ENTITY: MME
      INTYPE: S10
      PRIORITY: 18
      WEIGHT: 112
    - FQDN: 'MMEC14.MMEGI8001.MME.EPC.MNC001.MCC123.3GPPNETWORK.ORG'
      HSINDEX: 4
      ENTITY: MME
      INTYPE: S10
      PRIORITY: 18
      WEIGHT: 112
    add_ipv4dnsh_list_2:
    - HSINDEX: 6
      HOSTNAME: 'topon.eth6.mmec12.mmegi8001.mme'
      ADDRSECTION: SECTION1
      IPV4ADDR1: '10.11.1.3'
      IPV4ADDR2: '10.11.1.4'
    - HSINDEX: 6
      HOSTNAME: 'topon.eth6.mmec12.mmegi8001.mme'
      ADDRSECTION: SECTION1
      IPV4ADDR1: '10.11.1.3'
      IPV4ADDR2: '10.11.1.4'
    add_dnsn_list_4:
    - FQDN: 'MMEC14.MMEGI8001.MME.EPC.MNC001.MCC123.3GPPNETWORK.ORG'
      HSINDEX: 6
      ENTITY: MME
      INTYPE: S10
      PRIORITY: 20
      WEIGHT: 114
    - FQDN: 'MMEC12.MMEGI8001.MME.EPC.MNC001.MCC123.3GPPNETWORK.ORG'
      HSINDEX: 6
      ENTITY: MME
      INTYPE: S10
      PRIORITY: 20
      WEIGHT: 114
    set_licenseswitch_list:
    - LICITEM: 'LKV2NRBL5'
      SWITCH: ENABLE
    - LICITEM: 'LKV2NRBL5'
      SWITCH: ENABLE
    set_softparaofbit_list:
    - DT: BYTE_EX_B
      PARANUM: 5
      VALUE: VALUE_1
      POSITION: 8
    - DT: BYTE_EX_B
      PARANUM: 5
      VALUE: VALUE_1
      POSITION: 8
    add_n26iwkplcy_list:
    - SUBRANGE: ALL_USER
      IS5GCALLOW: YES
      ISNRALLOW: YES
      SMFSELPLCY: N1CAP_CNR
    - SUBRANGE: ALL_USER
      IS5GCALLOW: YES
      ISNRALLOW: YES
      SMFSELPLCY: N1CAP_CNR
    set_dns_list:
    - NON5GSEL: NO
    - NON5GSEL: NO
    set_s1cmpt_list:
    - NRRIN5GS: YES
      CNR: YES
    - NRRIN5GS: YES
      CNR: YES
    add_mmecharact_list:
    - RANGE: ALL_MME
      UENRSECCAP: YES
    - RANGE: ALL_MME
      UENRSECCAP: YES
    set_softparaofbit_list_2:
    - DT: BYTE_EX_B
      PARANUM: 331
      VALUE: VALUE_1
      POSITION: 3
    - DT: BYTE_EX_B
      PARANUM: 331
      VALUE: VALUE_1
      POSITION: 3
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 进入“MML命令行-UEG”窗口。

### 2 配置N26接口业务IP。

#### 2.1 //DC1

```jinja2
{%- for item in add_serviceip_list -%}
    ADD SERVICEIP:
    {#- --- 必选参数 --- -#}
    IPVERSION={{item.IPVERSION}},
    {#- --- 可选参数 --- -#}
    {%- if item.VPNINSTNAME is not none -%}
        VPNINSTNAME="{{item.VPNINSTNAME}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPv4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPv4' -%}
        SERVICEIPV4="{{item.SERVICEIPV4}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置GTP数据。

#### 3.1 配置N26接口与其他GTPC接口共部署时，GTPC本端实体对应的组号配置为0。

##### 3.1.1 配置MME在N26接口的GTPC IP。

###### 3.1.1.1 //DC1

```jinja2
{%- if is_scenario_gtpc_co_deployment -%}
    {%- for item in add_gtpcle_list -%}
        ADD GTPCLE:
        {#- --- 必选参数 --- -#}
        IPTYPE={{item.IPTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.GROUPID is not none -%}
            GROUPID={{item.GROUPID}},
        {%- endif -%}
        {%- if item.VPNNAME is not none -%}
            VPNNAME="{{item.VPNNAME}}",
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IPTYPE=TPTADDR_TYPE_IPV4 时必选 --- -#}
        {%- if item.IPTYPE == 'TPTADDR_TYPE_IPV4' -%}
            LEIPV4="{{item.LEIPV4}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 3.1.2 配置GTP路径管理参数。

###### 3.1.2.1 //DC1

```jinja2
{%- if is_scenario_gtpc_co_deployment -%}
    {%- for item in set_ugtp_list -%}
        SET UGTP:
        {#- --- 可选参数 --- -#}
        {%- if item.ICI is not none -%}
            ICI={{item.ICI}},
        {%- endif -%}
        {%- if item.SSI is not none -%}
            SSI={{item.SSI}},
        {%- endif -%}
        {%- if item.MSI is not none -%}
            MSI={{item.MSI}},
        {%- endif -%}
        {%- if item.PATHVERCHKINT is not none -%}
            PATHVERCHKINT={{item.PATHVERCHKINT}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 3.2 当需要将N26接口与其他GTPC接口分离部署时，配置N26接口分离。此时将GTPC本端实体对应的组号配置为非0，同步增加接口属性配置，通过组号的关联，用于组网规划不同接口。

##### 3.2.1 配置MME在N26接口的GTPC IP。

###### 3.2.1.1 //DC1

```jinja2
{%- if is_scenario_gtpc_separate_deployment -%}
    {%- for item in add_gtpcle_list_2 -%}
        ADD GTPCLE:
        {#- --- 必选参数 --- -#}
        IPTYPE={{item.IPTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.GROUPID is not none -%}
            GROUPID={{item.GROUPID}},
        {%- endif -%}
        {%- if item.VPNNAME is not none -%}
            VPNNAME="{{item.VPNNAME}}",
        {%- endif -%}
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：IPTYPE=TPTADDR_TYPE_IPV4 时必选 --- -#}
        {%- if item.IPTYPE == 'TPTADDR_TYPE_IPV4' -%}
            LEIPV4="{{item.LEIPV4}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 3.2.2 配置GTP路径管理参数。

###### 3.2.2.1 //DC1

```jinja2
{%- if is_scenario_gtpc_separate_deployment -%}
    {%- for item in set_ugtp_list_2 -%}
        SET UGTP:
        {#- --- 可选参数 --- -#}
        {%- if item.ICI is not none -%}
            ICI={{item.ICI}},
        {%- endif -%}
        {%- if item.SSI is not none -%}
            SSI={{item.SSI}},
        {%- endif -%}
        {%- if item.MSI is not none -%}
            MSI={{item.MSI}},
        {%- endif -%}
        {%- if item.PATHVERCHKINT is not none -%}
            PATHVERCHKINT={{item.PATHVERCHKINT}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 3.2.3 配置GTPC接口属性。

###### 3.2.3.1 //DC1

```jinja2
{%- if is_scenario_gtpc_separate_deployment -%}
    {%- for item in add_gtpcintfattr_list -%}
        ADD GTPCINTFATTR:
        {#- --- 必选参数 --- -#}
        SUBRANGE={{item.SUBRANGE}},
        GRPID={{item.GRPID}},
        {#- --- 条件必选参数 --- -#}
        {#- --- 条件必选：SUBRANGE=ALL_USER 时必选 --- -#}
        {%- if item.SUBRANGE == 'ALL_USER' -%}
            INTFTP={{item.INTFTP}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 4 **可选：**配置本端MME的解析数据，包含在Inter Attach/TAU流程中根据GUTI值选择MME使用的DNS记录及在Inter Handover流程中根据TAI值选择MME使用的DNS记录。

#### 4.1 //DC1

```jinja2
{%- if is_optional_local_mme_dns_data -%}
    {%- for item in add_ipv4dnsh_list -%}
        ADD IPV4DNSH:
        {#- --- 必选参数 --- -#}
        HSINDEX={{item.HSINDEX}},
        HOSTNAME="{{item.HOSTNAME}}",
        ADDRSECTION={{item.ADDRSECTION}},
        {#- --- 可选参数 --- -#}
        {%- if item.IPV4ADDR1 is not none -%}
            IPV4ADDR1="{{item.IPV4ADDR1}}",
        {%- endif -%}
        {%- if item.IPV4ADDR2 is not none -%}
            IPV4ADDR2="{{item.IPV4ADDR2}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_optional_local_mme_dns_data -%}
    {%- for item in add_dnsn_list -%}
        ADD DNSN:
        {#- --- 必选参数 --- -#}
        FQDN="{{item.FQDN}}",
        HSINDEX={{item.HSINDEX}},
        ENTITY={{item.ENTITY}},
        INTYPE={{item.INTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.PRIORITY is not none -%}
            PRIORITY={{item.PRIORITY}},
        {%- endif -%}
        {%- if item.WEIGHT is not none -%}
            WEIGHT={{item.WEIGHT}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 5 **可选：**配置对端AMF的解析数据，包含在Inter Attach/TAU流程中根据GUTI值选择AMF使用的DNS记录及在Inter Handover流程中根据TAI值选择AMF使用的DNS记录。

#### 5.1 //DC1

```jinja2
{%- if is_optional_peer_amf_dns_data -%}
    {%- for item in add_ipv4dnsh_list_2 -%}
        ADD IPV4DNSH:
        {#- --- 必选参数 --- -#}
        HSINDEX={{item.HSINDEX}},
        HOSTNAME="{{item.HOSTNAME}}",
        ADDRSECTION={{item.ADDRSECTION}},
        {#- --- 可选参数 --- -#}
        {%- if item.IPV4ADDR1 is not none -%}
            IPV4ADDR1="{{item.IPV4ADDR1}}",
        {%- endif -%}
        {%- if item.IPV4ADDR2 is not none -%}
            IPV4ADDR2="{{item.IPV4ADDR2}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

```jinja2
{%- if is_optional_peer_amf_dns_data -%}
    {%- for item in add_dnsn_list_4 -%}
        ADD DNSN:
        {#- --- 必选参数 --- -#}
        FQDN="{{item.FQDN}}",
        HSINDEX={{item.HSINDEX}},
        ENTITY={{item.ENTITY}},
        INTYPE={{item.INTYPE}},
        {#- --- 可选参数 --- -#}
        {%- if item.PRIORITY is not none -%}
            PRIORITY={{item.PRIORITY}},
        {%- endif -%}
        {%- if item.WEIGHT is not none -%}
            WEIGHT={{item.WEIGHT}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 6 配置支持UE在LTE与5G SA网络间互操作。

#### 6.1 打开LTE与5G SA网络互操作特性的License配置开关。

##### 6.1.1 //DC1

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

#### 6.2 设置本特性必选软件参数。

##### 6.2.1 //DC1

```jinja2
{%- for item in set_softparaofbit_list -%}
    SET SOFTPARAOFBIT:
    {#- --- 必选参数 --- -#}
    DT={{item.DT}},
    PARANUM={{item.PARANUM}},
    VALUE={{item.VALUE}},
    POSITION={{item.POSITION}},
    ;
{%- endfor -%}
```

#### 6.3 配置LTE和5G网络互操作策略。

##### 6.3.1 增加互操作本地策略。

###### 6.3.1.1 //DC1

```jinja2
{%- for item in add_n26iwkplcy_list -%}
    ADD N26IWKPLCY:
    {#- --- 必选参数 --- -#}
    SUBRANGE={{item.SUBRANGE}},
    IS5GCALLOW={{item.IS5GCALLOW}},
    {#- --- 可选参数 --- -#}
    {%- if item.SMFSELPLCY is not none -%}
        SMFSELPLCY={{item.SMFSELPLCY}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IS5GCALLOW=YES 时可选 --- -#}
    {%- if item.IS5GCALLOW == 'YES' -%}
        {%- if item.ISNRALLOW is not none -%}
            ISNRALLOW={{item.ISNRALLOW}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 6.3.2 **可选：**如果需要限制非5G用户接入融合网关SMF+PGW-C，执行本步骤。

###### 6.3.2.1 //DC1

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该set_dns_list的变量区（command: SET DNS） -#}
<!-- MISSING_MACRO: command=SET DNS list_name=set_dns_list step_id=6.3.2.1 -->
```

#### 6.4 **可选：**配置S1接口兼容性参数。

##### 6.4.1 //DC1

```jinja2
{%- if is_optional_s1_compatibility_params -%}
    {%- for item in set_s1cmpt_list -%}
        SET S1CMPT:
        {#- --- 可选参数 --- -#}
        {%- if item.NRRIN5GS is not none -%}
            NRRIN5GS={{item.NRRIN5GS}},
        {%- endif -%}
        {%- if item.CNR is not none -%}
            CNR={{item.CNR}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 6.5 **可选：**增加对端MME属性信息，配置S10接口兼容性参数。

##### 6.5.1 //DC1

```jinja2
{%- if is_optional_peer_mme_attributes -%}
    {%- for item in add_mmecharact_list -%}
        ADD MMECHARACT:
        {#- --- 必选参数 --- -#}
        RANGE={{item.RANGE}},
        {#- --- 可选参数 --- -#}
        {%- if item.UENRSECCAP is not none -%}
            UENRSECCAP={{item.UENRSECCAP}},
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 6.6 **可选：**在LTE和5G网络间重选的过程中需要优选AMF与MME融合部署的AMF时，设置如下软参取值为“1”。

##### 6.6.1 //DC1

```jinja2
{%- if is_optional_prefer_codeployed_amf -%}
    {%- for item in set_softparaofbit_list_2 -%}
        SET SOFTPARAOFBIT:
        {#- --- 必选参数 --- -#}
        DT={{item.DT}},
        PARANUM={{item.PARANUM}},
        VALUE={{item.VALUE}},
        POSITION={{item.POSITION}},
        ;
    {%- endfor -%}
{%- endif -%}
```

