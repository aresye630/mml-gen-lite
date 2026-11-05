---
id: ''
name: 配置AMF服务化接口数据（N8/N11/N12）
ne_type: UEG
type: feature
description: AMF的服务化接口为Namf，与参考点的对应关系如下。参考点是指5G系统服务化架构映射到传统架构后，对应传统网元之间点对点的接口，用来代表NF之间交互的参考模型，并不是真实的接口。  **表1** 服务化接口与参考点模式对应关系  | 参考点 | 网元间的交互 | 服务化接口 | | --- | --- | --- | | N8 | AMF<->UDM | Namf、Nudm | | N11 | AMF<->SMF | Namf、Nsmf | | N12 | AMF<->AUSF | Nausf、Namf |  园区风筝M有两种运行模式：  * 正常模式：中心侧AMF对接中心侧UDM/AUSF。 * 应急模式：应急AMF与园区内本地DC的UDM/AUSF对接，使用园区统一规划的IP地址，VRF。数据在园区内封闭传输。  本文配置仅关注应急AMF的配置。  **图1** 服务化接口协议栈图  服务化接口间采用相同的协议栈，传输层统一采用HTTP/2协议，应用层携带不同的服务消息。因为底层的传输方式相同，所有的服务化接口就可以在同一总线上进行传输，支撑业务灵活上线。  HTTP/2（HyperText Transport Protocol 2.0）：下一代超文本传输协议。基于HTTP协议的信息交换分为四个过程：建立连接、发送请求信息、发送响应信息、关闭连接。  TLS（Transport Layer Security）：安全传输层协议。在两个通信应用程序之间提供保密性和数据完整性。  **配置建议**  * AMF的服务化接口业务IP地址不能和AMF其他接口业务IP地址共用。 * AMF的服务化接口端口号没有明确时，使用HTTP知名端口号8080。 * 一个NF类型需要配置一个HTTP本端端点组和对应的HTTP本端端点，然后根据实际部署NF数量配置分别配置对应的SBI端点并绑定对应的HTTP本端端点组。  以下配置数据以及步骤均以UEG双DC组网场景的配置规划为例进行介绍。
tags: []
risk_level: ''
doc_source: ["网络部署","园区入驻+地市共享（连接+计算）","5GC toB 部署边缘站点（站点为“风筝M”，带计算）","UEG初始配置（风筝M）","参考：详细配置指导","配置AMF","配置AMF服务化接口数据（N8/N11/N12）"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
AMF的服务化接口为Namf，与参考点的对应关系如下。参考点是指5G系统服务化架构映射到传统架构后，对应传统网元之间点对点的接口，用来代表NF之间交互的参考模型，并不是真实的接口。**表1** 服务化接口与参考点模式对应关系| 参考点 | 网元间的交互 | 服务化接口 || --- | --- | --- || N8 | AMF<->UDM | Namf、Nudm || N11 | AMF<->SMF | Namf、Nsmf || N12 | AMF<->AUSF | Nausf、Namf |园区风筝M有两种运行模式：* 正常模式：中心侧AMF对接中心侧UDM/AUSF。* 应急模式：应急AMF与园区内本地DC的UDM/AUSF对接，使用园区统一规划的IP地址，VRF。数据在园区内封闭传输。本文配置仅关注应急AMF的配置。**图1** 服务化接口协议栈图服务化接口间采用相同的协议栈，传输层统一采用HTTP/2协议，应用层携带不同的服务消息。因为底层的传输方式相同，所有的服务化接口就可以在同一总线上进行传输，支撑业务灵活上线。HTTP/2（HyperText Transport Protocol 2.0）：下一代超文本传输协议。基于HTTP协议的信息交换分为四个过程：建立连接、发送请求信息、发送响应信息、关闭连接。TLS（Transport Layer Security）：安全传输层协议。在两个通信应用程序之间提供保密性和数据完整性。**配置建议*** AMF的服务化接口业务IP地址不能和AMF其他接口业务IP地址共用。* AMF的服务化接口端口号没有明确时，使用HTTP知名端口号8080。* 一个NF类型需要配置一个HTTP本端端点组和对应的HTTP本端端点，然后根据实际部署NF数量配置分别配置对应的SBI端点并绑定对应的HTTP本端端点组。以下配置数据以及步骤均以UEG双DC组网场景的配置规划为例进行介绍。

## 必备事项
前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020/MAE客户端或登录OM Portal）。

* 已完成部署组网路由配置。

* 如果本接口采用IPv6组网，则需要开通逻辑接口支持IPv6特性，即加载对应的License项“81203214 LKV3G5V6LI01 逻辑接口支持IPv6”。
* 已经获取网设LLD文档。


本文以IPv4组网为例说明。

* 如果是IPv6组网，请将逻辑接口地址规划为IPv6地址。
* 如果是IPv4v6双栈组网，则对逻辑接口配置双栈地址即可。

**如下数据仅为举例，请注意修改成局点规划的数据。**

* AMF服务化接口数据

  | 类别 | 参数名称 | DC1取值样例 | DC2取值样例 | 获取方法 | 说明 |
  | --- | --- | --- | --- | --- | --- |
  | **ADD LOGICIP** | 逻辑IP地址类型（IPVERSION） | IPV4 |  | 参见“水平网设LLD文档 -> 5G Core业务IP对接设计”。 | 配置Namf接口的逻辑IP地址。 |
  |  | 逻辑IPv4地址（LOGICIPV4） | 172.16.1.3  172.16.1.4 | 172.16.1.5  172.16.1.6 |  | 服务化接口规划两个IP地址，AMF作为客户端一个，作为服务端一个。 |
  |  | VPN实例名称（VPNINSTNAME） | VPN\_CN |  |  | UEG风筝形态内部接口组网时，使用园区统一规划的VPN。 |
  |  | 描述（DESC） | FOR Server SBI  FOR Client SBI |  | 本端规划 | - |
  | **ADD HTTPLEGRP** | 索引（INDEX） | 1 |  | 本端规划 | 配置Namf接口的HTTP本端实体组。 |
  |  | DESC（描述） | AMF |  | 本端规划 |  |
  | **ADD HTTPLE** | HTTPLE本端实体索引（INDEX） | 1  2 |  | 本端规划 | 配置Namf接口分别作为HTTP服务的服务端和客户端的本端端点信息。 |
  |  | 本端实体类型（LETYPE） | SERVER  CLIENT |  | 全网规划 |  |
  |  | HTTP本端实体组标识（HTTPLEGRPIDX） | 1 |  | 本端规划 | 已通过**ADD HTTPLEGRP**配置，可以通过**LST HTTPLEGRP**查询。 |
  |  | 端口号（PORT） | 8080  - |  | 全网规划 | - |
  |  | 是否启用TLS（TLSFLG） | NO |  | 全网规划 |  |
  |  | IP类型（IPTYPE） | IPv4 |  | 全网规划 | 与**ADD LOGICIP**命令中配置的IP地址需保持一致。 |
  |  | IPv4地址（IPv4） | 172.16.1.3  172.16.1.4 | 172.16.1.5  172.16.1.6 | 全网规划 |  |
  |  | VPN名称（VPNNAME） | VPN\_CN |  | 本端规划 | - |
  |  | DESC（描述） | AMF Server  AMF Client |  | 本端规划 | - |
  | **ADD SBIAPLE** | 索引（INDEX） | 1 |  | 全网规划 | 配置Namf接入点信息。 |
  |  | HttpLEGRP索引（HTTPLEGRPIDX） | 1 |  | 全网规划 | 已通过**ADD HTTPLEGRP**配置，可以通过**LST HTTPLEGRP**查询。 |
  |  | NF类型（NFTYPE） | NFTypeAMF |  | 全网规划 | - |
  |  | DESCRIPTION（描述） | AMF |  | 本端规划 | - |
* 到AUSF的数据

  | 类别 | 参数名称 | DC1取值样例 | DC2取值样例 | 获取方法 | 说明 |
  | --- | --- | --- | --- | --- | --- |
  | **ADD PNFPROFILE** | NF实例标识（NFINSTANCEID） | AUSF\_Instance\_0 | AUSF\_Instance\_1 | 参见“水平网设LLD文档 -> 5G Core业务IP对接设计”。 | 配置AUSF的Profile信息。  园区双DC组网，本DC的应急AMF仅连接本DC内的AUSF，因此本DC内配置仅有一个对端实例。 |
  |  | NF类型（NFTYPE） | NfAUSF |  |  | - |
  |  | NF状态（NFSTATUS） | Registered |  |  |  |
  |  | IP地址类型（IPADDRESSTYPE） | IPTypeV4 |  |  | 配置对接的对端AUSF的IP地址。 |
  |  | IPV4地址1（IPV4ADDRESS1） | 10.255.255.181 | 10.255.255.182 |  |  |
  |  | 端口号（PORT） | 8080 |  |  | - |
  |  | 优先级（PRIORITY） | 1 | 10 |  | - |
  | **ADD PNFSERVICE** | NF实例标识（NFINSTANCEID） | AUSF\_Instance\_0 | AUSF\_Instance\_1 | 全网规划 | 配置AUSF的服务信息。 |
  |  | 服务实例标识（SRVINSTANCEID） | Service\_Instance\_0 |  | 全网规划 |  |
  |  | 服务名称（SERVICENAME） | NausfAuth |  | 全网规划 |  |
  |  | 协议模式（SCHEMA） | http |  | 全网规划 |  |
  |  | 服务实例状态（NFSERVICESTATUS） | REGISTERED |  | 全网规划 |  |
  | **ADD PNFPLMN** | NF实例标识（NFINSTANCEID） | AUSF\_Instance\_0 | AUSF\_Instance\_1 | 全网规划 | 配置对端AUSF的实例信息，可以基于PLMN发现AUSF。 |
  |  | 移动国家码（MCC） | 123 |  | 全网规划 |  |
  |  | 移动网号（MNC） | 03 |  | 全网规划 |  |
  | **ADD PNFROUTEIND** | NF实例标识（NFINSTANCEID） | AUSF\_Instance\_0 | AUSF\_Instance\_1 | 全网规划 | 配置对端AUSF的路由指示信息。路由指示器是SUCI组成的一部分，用于使用SUCI进行AUSF和UDM的选择。 |
  |  | 路由指示（ROUTINGIND） | 0000 |  | 本端规划 |  |
  | **ADD PNFSUPI** | 索引（INDEX） | 1 |  | 本端规划 | 配置对端AUSF支持的SUPI信息，可以基于SUPI选择AUSF。 |
  |  | NF实例标识（NFINSTANCEID） | AUSF\_Instance\_0 | AUSF\_Instance\_1 | 全网规划 |  |
  |  | 查询方式（QUERYTYPE） | START\_END |  | 全网规划 |  |
  |  | 起始号段（RANGESTART） | 123031200100001 |  | 全网规划 |  |
  |  | 终止号段（RANGEEND） | 123031200100100 |  | 全网规划 |  |
* 到UDM的数据

  UEG中AMF和SMF共部署，如果在配置SMF的时候已经配置和UDM的对接配置，则本步骤无需重复配置。

  | 类别 | 参数名称 | DC1取值样例 | DC2取值样例 | 获取方法 | 说明 |
  | --- | --- | --- | --- | --- | --- |
  | **ADD PNFPROFILE** | NF实例标识（NFINSTANCEID） | UDM\_Instance\_0 | UDM\_Instance\_1 | 参见“水平网设LLD文档 -> 5G Core业务IP对接设计”。 | 配置UDM的Profile信息。  园区双DC组网，本DC的应急AMF仅连接本DC内的UDM，因此本DC内配置仅有一个对端实例。 |
  |  | NF类型（NFTYPE） | NfUDM |  |  | - |
  |  | NF状态（NFSTATUS） | Registered |  |  |  |
  |  | IP地址类型（IPADDRESSTYPE） | IPTypeV4 |  |  | 配置对接的对端UDM的IP地址。 |
  |  | IPV4地址1（IPV4ADDRESS1） | 10.255.255.183 | 10.255.255.184 |  |  |
  |  | 端口号（PORT） | 8080 |  |  | - |
  |  | 优先级（PRIORITY） | 1 | 10 |  | - |
  | **ADD PNFSERVICE** | NF实例标识（NFINSTANCEID） | UDM\_Instance\_0 | UDM\_Instance\_1 | 全网规划 | 配置对端UDM的服务信息。 |
  |  | 服务实例标识（SRVINSTANCEID） | Service\_Instance\_0 | Service\_Instance\_1 | 全网规划 |  |
  |  | 服务名称（SERVICENAME） | NudmSdm  NudmUecm |  | 全网规划 |  |
  |  | 协议模式（SCHEMA） | http |  | 全网规划 |  |
  |  | 服务实例状态（NFSERVICESTATUS） | REGISTERED |  | 全网规划 |  |
  | **ADD PNFPLMN** | NF实例标识（NFINSTANCEID） | UDM\_Instance\_0 | UDM\_Instance\_1 | 全网规划 | 配置对端UDM的实例信息，可以基于PLMN选择UDM。 |
  |  | 移动国家码（MCC） | 123 |  | 全网规划 |  |
  |  | 移动网号（MNC） | 03 |  | 全网规划 |  |
  | **ADD PNFSUPI** | 索引（INDEX） | 1 |  | 本端规划 | 配置对端UDM支持的SUPI信息，可以基于SUPI选择UDM。 |
  |  | NF实例标识（NFINSTANCEID） | UDM\_Instance\_0 | UDM\_Instance\_1 | 全网规划 |  |
  |  | 查询方式（QUERYTYPE） | START\_END |  | 全网规划 |  |
  |  | 起始号段（RANGESTART） | 123031200100001 |  | 全网规划 |  |
  |  | 终止号段（RANGEEND） | 123031200100100 |  | 全网规划 |  |
* 到SMF的数据

  | 类别 | 参数名称 | DC1取值样例 | DC2取值样例 | 获取方法 | 说明 |
  | --- | --- | --- | --- | --- | --- |
  | **ADD PNFPROFILE** | NF实例标识（NFINSTANCEID） | SMF\_Instance\_0 | SMF\_Instance\_1 | 参见“水平网设LLD文档 -> 5G Core业务IP对接设计”。 | 配置SMF的Profile信息。  园区双DC组网，本DC的应急AMF仅连接本DC内的SMF，因此本DC内配置仅有一个对端实例。 |
  |  | NF类型（NFTYPE） | NfSMF |  |  |  |
  |  | NF状态（NFSTATUS） | Registered |  |  |  |
  |  | IP地址类型（IPADDRESSTYPE） | IPTypeV4 |  |  |  |
  |  | IPV4地址1（IPV4ADDRESS1） | 172.16.0.5 | 172.16.0.6 |  |  |
  |  | 端口号（PORT） | 8080 |  |  |  |
  | **ADD PNFSERVICE** | NF实例标识（NFINSTANCEID） | SMF\_Instance\_0 | SMF\_Instance\_1 | 全网规划 | 配置SMF的服务信息。 |
  |  | 服务实例标识（SRVINSTANCEID） | Service\_Instance\_4 | Service\_Instance\_5 | 全网规划 |  |
  |  | 服务名称（SERVICENAME） | NsmfPduSes  NsmfEventExp |  | 全网规划 |  |
  |  | 协议模式（SCHEMA） | http |  | 全网规划 |  |
  |  | 服务实例状态（NFSERVICESTATUS） | REGISTERED |  | 全网规划 |  |
  | **ADD PNFPLMN** | NF实例标识（NFINSTANCEID） | SMF\_Instance\_0 | SMF\_Instance\_1 | 全网规划 | 配置对端SMF实例支持的PLMN，可以基于该PLMN选择SMF。 |
  |  | 移动国家码（MCC） | 123 |  | 全网规划 |  |
  |  | 移动网号（MNC） | 03 |  | 全网规划 |  |
  | **ADD PNFDNN** | 索引（INDEX） | 1 |  | 全网规划 | 配置对端SMF实例支持的DNN，可以基于DNN选择SMF。 |
  |  | NF实例标识（NFINSTANCEID） | SMF\_Instance\_0 | SMF\_Instance\_1 | 全网规划 |  |
  |  | DNN（数据网络名称） | huawei.com |  | 本端规划 |  |
  | **ADD PNFNS** | 索引（INDEX） | 1 |  | 本端规划 | 配置对端SMF实例支持的服务切片信息，可以基于切片选择SMF。 |
  |  | NF实例标识（NFINSTANCEID） | SMF\_Instance\_0 | SMF\_Instance\_1 | 全网规划 |  |
  |  | 切片/服务类型（SST） | 1 |  | 全网规划 |  |
  |  | 切片分类器（SD） | 010101 |  | 全网规划 |  |
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
          description: '配置Namf接口的逻辑IP地址。'
          data_source: '参见“水平网设LLD文档 -> 5G Core业务IP对接设计”。'
          pattern: ''
          default: ''
        LOGICIPV4:
          name: '逻辑IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: '服务化接口规划两个IP地址，AMF作为客户端一个，作为服务端一个。'
          data_source: ''
          pattern: ''
          default: ''
        VPNINSTNAME:
          name: 'VPN实例名称'
          type: string
          minLength: 1
          maxLength: 31
          required: false
          description: 'UEG风筝形态内部接口组网时，使用园区统一规划的VPN。'
          data_source: ''
          pattern: ''
          default: ''
        DESC:
          name: '描述'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_httplegrp_list:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 1
          maximum: 64
          required: true
          description: '配置Namf接口的HTTP本端实体组。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        DESC:
          name: '描述'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_httple_list:
      type: items
      properties:
        INDEX:
          name: 'HTTPLE本端实体索引'
          type: integer
          minimum: 1
          maximum: 128
          required: true
          description: '配置Namf接口分别作为HTTP服务的服务端和客户端的本端端点信息。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        HTTPLEGRPIDX:
          name: 'HTTP本端实体组标识'
          type: integer
          minimum: 1
          maximum: 64
          required: true
          description: '已通过**ADD HTTPLEGRP**配置，可以通过**LST HTTPLEGRP**查询。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        LETYPE:
          name: '本端实体类型'
          type: string
          enum:
          - SERVER
          - CLIENT
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPTYPE:
          name: 'IP类型'
          type: string
          enum:
          - IPv4
          - IPv6
          required: true
          description: '与**ADD LOGICIP**命令中配置的IP地址需保持一致。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        IPV4:
          name: 'IPv4地址'
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
          minimum: 1
          maximum: 65535
          required: false
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        VPNNAME:
          name: 'VPN名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        TLSFLG:
          name: '是否启用TLS'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: YES
        DESC:
          name: '描述'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_sbiaple_list:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 1
          maximum: 128
          required: true
          description: '配置Namf接入点信息。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        HTTPLEGRPIDX:
          name: 'HttpLEGRP索引'
          type: integer
          minimum: 1
          maximum: 64
          required: true
          description: '已通过**ADD HTTPLEGRP**配置，可以通过**LST HTTPLEGRP**查询。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        NFTYPE:
          name: 'NF类型'
          type: string
          enum:
          - INVALID
          - NFTypeNRF
          - NFTypeUDM
          - NFTypeAMF
          - NFTypeSMF
          - NFTypeAUSF
          - NFTypeNEF
          - NFTypePCF
          - NFTypeSMSF
          - NFTypeNSSF
          - NFTypeUDR
          - NFTypeLMF
          - NFTypeGMLC
          - NFType5GEIR
          - NFTypeSEPP
          - NFTypeUPF
          - NFTypeN3IWF
          - NFTypeAF
          - NFTypeUDSF
          - NFTypeBSF
          - NFTypeCHF
          - NFTypeCUSTOM_OCS
          - NFTypeSCP
          - NFTypeMBSMF
          - NFTypeNWDAF
          - NFTypeUDN
          - NFTypeSFC
          - NFTypeUCBC
          - NFTypeCBE
          - NFTypeNEFEx
          - NFTypeSCF
          - NFTypeKMC
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        DESCRIPTION:
          name: '描述'
          type: string
          minLength: 0
          maxLength: 255
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    set_httpconf_list:
      type: items
      properties:
        SERVERRCVBDTMT:
          name: '服务端接收HTTP请求消息体超时时间(s)'
          type: integer
          minimum: 1
          maximum: 20
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SERVERSNDRSPTMT:
          name: '服务端回复HTTP响应消息超时时间(s)'
          type: integer
          minimum: 1
          maximum: 20
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MAXBODYSIZE:
          name: '最大消息体大小(MBytes)'
          type: integer
          minimum: 2
          maximum: 16
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MAXJSONLEAFNUM:
          name: 'JSON数据最多叶子节点个数'
          type: integer
          minimum: 16000
          maximum: 512000
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
          description: '配置AUSF的Profile信息。  园区双DC组网，本DC的应急AMF仅连接本DC内的AUSF，因此本DC内配置仅有一个对端实例。'
          data_source: '参见“水平网设LLD文档 -> 5G Core业务IP对接设计”。'
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
          data_source: ''
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
        IPADDRESSTYPE:
          name: 'IP地址类型'
          type: string
          enum:
          - IPTypeV4
          - IPTypeV6
          - IPTypeV4V6
          required: false
          description: '配置对接的对端AUSF的IP地址。'
          data_source: ''
          pattern: ''
          default: ''
        IPV4ADDRESS1:
          name: 'IPV4地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PORT:
          name: '端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: '-'
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
          default: ''
    add_pnfservice_list:
      type: items
      properties:
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: '配置AUSF的服务信息。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SRVINSTANCEID:
          name: '服务实例标识'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SERVICENAME:
          name: '服务名称'
          type: string
          enum:
          - NrfNfm
          - NnrfDisc
          - NudmSdm
          - NudmUecm
          - NudmUeau
          - NudmEe
          - NudmPp
          - NamfComm
          - NamfEvts
          - NamfMt
          - NamfLoc
          - NsmfPduSes
          - NsmfEventExp
          - NausfAuth
          - NausfSorprot
          - NnefPfdMgnt
          - NpcfAmPlcCtrl
          - NpcfSmplcCtrl
          - NpcfPlcAuth
          - NpcfBdtplcCtrl
          - NpcfEventEx
          - NpcfUePcy
          - NsmsfSms
          - NnssfNsSel
          - NnssfNssaiAvai
          - NudrDr
          - NlmfLoc
          - N5gEirEic
          - NbsfMgnt
          - NchfSpdlmtCtrl
          - NchfConvCharg
          - NnwdafEvntSubs
          - NnwdafAnalInfo
          - NocsSpdLmtCtrl
          - NocsConvCharg
          - NgmlcLoc
          - SrvNameINVALID
          - SrvNameMAX
          - NamfMbsBroadcast
          - NmbSmfTmgi
          - NmbSmfMbssession
          - NudnDm
          - NnefSmCtx
          - NnwdafDataManagement
          - NscfSenseService
          - NscfSenseTask
          - NnefAuthentication
          - NkmcSign
          - NpcfUeExpPlcCtrl
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SCHEMA:
          name: '协议模式'
          type: string
          enum:
          - UriSchemeINVALID
          - http
          - https
          - UriSchemeMAX
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        NFSERVICESTATUS:
          name: '服务实例状态'
          type: string
          enum:
          - INVALID
          - REGISTERED
          - SUSPENDED
          - DEREGISTERED
          - UNDISCOVERABLE
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: REGISTERED
    add_pnfplmn_list:
      type: items
      properties:
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: '配置对端AUSF的实例信息，可以基于PLMN发现AUSF。'
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
          data_source: '全网规划'
          pattern: ''
          default: ''
        MNC:
          name: '移动网号'
          type: string
          minLength: 2
          maxLength: 3
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_pnfrouteind_list:
      type: items
      properties:
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 0
          maxLength: 36
          required: true
          description: '配置对端AUSF的路由指示信息。路由指示器是SUCI组成的一部分，用于使用SUCI进行AUSF和UDM的选择。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        ROUTINGIND:
          name: '路由指示'
          type: string
          minLength: 0
          maxLength: 4
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_pnfsupi_list:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: '配置对端AUSF支持的SUPI信息，可以基于SUPI选择AUSF。'
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
        QUERYTYPE:
          name: '查询方式'
          type: string
          enum:
          - START_END
          - PATTERN
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        RANGESTART:
          name: '起始号段'
          type: string
          minLength: 5
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        RANGEEND:
          name: '终止号段'
          type: string
          minLength: 5
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    mod_ngusrsecpara_list:
      type: items
      properties:
        SUBRANGE:
          name: '用户范围'
          type: string
          enum:
          - ALL_USER
          - IMSI_PREFIX
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTHEVENT:
          name: '鉴权事件'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTHPERIOD:
          name: '鉴权周期(h)'
          type: integer
          minimum: 0
          maximum: 24
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_pnfprofile_list_2:
      type: items
      properties:
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 1
          maxLength: 36
          required: true
          description: '配置UDM的Profile信息。  园区双DC组网，本DC的应急AMF仅连接本DC内的UDM，因此本DC内配置仅有一个对端实例。'
          data_source: '参见“水平网设LLD文档 -> 5G Core业务IP对接设计”。'
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
          data_source: ''
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
        IPADDRESSTYPE:
          name: 'IP地址类型'
          type: string
          enum:
          - IPTypeV4
          - IPTypeV6
          - IPTypeV4V6
          required: false
          description: '配置对接的对端UDM的IP地址。'
          data_source: ''
          pattern: ''
          default: ''
        IPV4ADDRESS1:
          name: 'IPV4地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PORT:
          name: '端口号'
          type: integer
          minimum: 0
          maximum: 65535
          required: false
          description: '-'
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
          default: ''
    add_pnfservice_list_2:
      type: items
      properties:
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: '配置对端UDM的服务信息。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SRVINSTANCEID:
          name: '服务实例标识'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SERVICENAME:
          name: '服务名称'
          type: string
          enum:
          - NrfNfm
          - NnrfDisc
          - NudmSdm
          - NudmUecm
          - NudmUeau
          - NudmEe
          - NudmPp
          - NamfComm
          - NamfEvts
          - NamfMt
          - NamfLoc
          - NsmfPduSes
          - NsmfEventExp
          - NausfAuth
          - NausfSorprot
          - NnefPfdMgnt
          - NpcfAmPlcCtrl
          - NpcfSmplcCtrl
          - NpcfPlcAuth
          - NpcfBdtplcCtrl
          - NpcfEventEx
          - NpcfUePcy
          - NsmsfSms
          - NnssfNsSel
          - NnssfNssaiAvai
          - NudrDr
          - NlmfLoc
          - N5gEirEic
          - NbsfMgnt
          - NchfSpdlmtCtrl
          - NchfConvCharg
          - NnwdafEvntSubs
          - NnwdafAnalInfo
          - NocsSpdLmtCtrl
          - NocsConvCharg
          - NgmlcLoc
          - SrvNameINVALID
          - SrvNameMAX
          - NamfMbsBroadcast
          - NmbSmfTmgi
          - NmbSmfMbssession
          - NudnDm
          - NnefSmCtx
          - NnwdafDataManagement
          - NscfSenseService
          - NscfSenseTask
          - NnefAuthentication
          - NkmcSign
          - NpcfUeExpPlcCtrl
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SCHEMA:
          name: '协议模式'
          type: string
          enum:
          - UriSchemeINVALID
          - http
          - https
          - UriSchemeMAX
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        NFSERVICESTATUS:
          name: '服务实例状态'
          type: string
          enum:
          - INVALID
          - REGISTERED
          - SUSPENDED
          - DEREGISTERED
          - UNDISCOVERABLE
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: REGISTERED
    add_pnfplmn_list_2:
      type: items
      properties:
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: '配置对端UDM的实例信息，可以基于PLMN选择UDM。'
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
          data_source: '全网规划'
          pattern: ''
          default: ''
        MNC:
          name: '移动网号'
          type: string
          minLength: 2
          maxLength: 3
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_pnfsupi_list_2:
      type: items
      properties:
        INDEX:
          name: '索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: '配置对端UDM支持的SUPI信息，可以基于SUPI选择UDM。'
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
        QUERYTYPE:
          name: '查询方式'
          type: string
          enum:
          - START_END
          - PATTERN
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        RANGESTART:
          name: '起始号段'
          type: string
          minLength: 5
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        RANGEEND:
          name: '终止号段'
          type: string
          minLength: 5
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_pnfprofile_list_4:
      type: items
      properties:
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 1
          maxLength: 36
          required: true
          description: '配置SMF的Profile信息。  园区双DC组网，本DC的应急AMF仅连接本DC内的SMF，因此本DC内配置仅有一个对端实例。'
          data_source: '参见“水平网设LLD文档 -> 5G Core业务IP对接设计”。'
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
          data_source: ''
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
        IPADDRESSTYPE:
          name: 'IP地址类型'
          type: string
          enum:
          - IPTypeV4
          - IPTypeV6
          - IPTypeV4V6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4ADDRESS1:
          name: 'IPV4地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
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
    add_pnfservice_list_6:
      type: items
      properties:
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: '配置SMF的服务信息。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        SRVINSTANCEID:
          name: '服务实例标识'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SERVICENAME:
          name: '服务名称'
          type: string
          enum:
          - NrfNfm
          - NnrfDisc
          - NudmSdm
          - NudmUecm
          - NudmUeau
          - NudmEe
          - NudmPp
          - NamfComm
          - NamfEvts
          - NamfMt
          - NamfLoc
          - NsmfPduSes
          - NsmfEventExp
          - NausfAuth
          - NausfSorprot
          - NnefPfdMgnt
          - NpcfAmPlcCtrl
          - NpcfSmplcCtrl
          - NpcfPlcAuth
          - NpcfBdtplcCtrl
          - NpcfEventEx
          - NpcfUePcy
          - NsmsfSms
          - NnssfNsSel
          - NnssfNssaiAvai
          - NudrDr
          - NlmfLoc
          - N5gEirEic
          - NbsfMgnt
          - NchfSpdlmtCtrl
          - NchfConvCharg
          - NnwdafEvntSubs
          - NnwdafAnalInfo
          - NocsSpdLmtCtrl
          - NocsConvCharg
          - NgmlcLoc
          - SrvNameINVALID
          - SrvNameMAX
          - NamfMbsBroadcast
          - NmbSmfTmgi
          - NmbSmfMbssession
          - NudnDm
          - NnefSmCtx
          - NnwdafDataManagement
          - NscfSenseService
          - NscfSenseTask
          - NnefAuthentication
          - NkmcSign
          - NpcfUeExpPlcCtrl
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SCHEMA:
          name: '协议模式'
          type: string
          enum:
          - UriSchemeINVALID
          - http
          - https
          - UriSchemeMAX
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        NFSERVICESTATUS:
          name: '服务实例状态'
          type: string
          enum:
          - INVALID
          - REGISTERED
          - SUSPENDED
          - DEREGISTERED
          - UNDISCOVERABLE
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: REGISTERED
    add_pnfplmn_list_4:
      type: items
      properties:
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 0
          maxLength: 50
          required: true
          description: '配置对端SMF实例支持的PLMN，可以基于该PLMN选择SMF。'
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
          data_source: '全网规划'
          pattern: ''
          default: ''
        MNC:
          name: '移动网号'
          type: string
          minLength: 2
          maxLength: 3
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_pnfsmfinfo_list:
      type: items
      properties:
        NFINSTANCEID:
          name: 'NF实例标识'
          type: string
          minLength: 0
          maxLength: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PGWFQDN:
          name: 'PGW域名'
          type: string
          minLength: 0
          maxLength: 255
          required: true
          description: ''
          data_source: ''
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
          description: '配置对端SMF实例支持的DNN，可以基于DNN选择SMF。'
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
          data_source: '本端规划'
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
          description: '配置对端SMF实例支持的服务切片信息，可以基于切片选择SMF。'
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
  examples:
    add_logicip_list:
    - IPVERSION: IPv4
      LOGICIPV4: '172.16.1.3'
      VPNINSTNAME: 'VPN_CN'
      DESC: 'FOR Server SBI'
    - IPVERSION: IPv4
      LOGICIPV4: '172.16.1.5'
      VPNINSTNAME: 'VPN_CN'
      DESC: 'FOR Server SBI'
    add_httplegrp_list:
    - INDEX: 1
      DESC: 'AMF'
    - INDEX: 1
      DESC: 'AMF'
    add_httple_list:
    - INDEX: 1
      HTTPLEGRPIDX: 1
      LETYPE: SERVER
      IPTYPE: IPv4
      IPV4: '172.16.1.3'
      PORT: 8080
      VPNNAME: 'VPN_CN'
      TLSFLG: NO
      DESC: 'AMF Server'
    - INDEX: 1
      HTTPLEGRPIDX: 1
      LETYPE: SERVER
      IPTYPE: IPv4
      IPV4: '172.16.1.5'
      PORT: 8080
      VPNNAME: 'VPN_CN'
      TLSFLG: NO
      DESC: 'AMF Server'
    add_sbiaple_list:
    - INDEX: 1
      HTTPLEGRPIDX: 1
      NFTYPE: NFTypeAMF
      DESCRIPTION: 'AMF'
    - INDEX: 1
      HTTPLEGRPIDX: 1
      NFTYPE: NFTypeAMF
      DESCRIPTION: 'AMF'
    set_httpconf_list:
    - SERVERRCVBDTMT: 15
      SERVERSNDRSPTMT: 15
      MAXBODYSIZE: 15
      MAXJSONLEAFNUM: 100000
    - SERVERRCVBDTMT: 15
      SERVERSNDRSPTMT: 15
      MAXBODYSIZE: 15
      MAXJSONLEAFNUM: 100000
    add_pnfprofile_list:
    - NFINSTANCEID: 'AUSF_Instance_0'
      NFTYPE: NfAUSF
      NFSTATUS: Registered
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS1: '10.255.255.181'
      PORT: 8080
      PRIORITY: 10
    - NFINSTANCEID: 'AUSF_Instance_1'
      NFTYPE: NfAUSF
      NFSTATUS: Registered
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS1: '10.255.255.182'
      PORT: 8080
      PRIORITY: 10
    add_pnfservice_list:
    - NFINSTANCEID: 'AUSF_Instance_0'
      SRVINSTANCEID: 'Service_Instance_0'
      SERVICENAME: NausfAuth
      SCHEMA: http
      NFSERVICESTATUS: REGISTERED
    - NFINSTANCEID: 'AUSF_Instance_1'
      SRVINSTANCEID: 'Service_Instance_0'
      SERVICENAME: NausfAuth
      SCHEMA: http
      NFSERVICESTATUS: REGISTERED
    add_pnfplmn_list:
    - NFINSTANCEID: 'AUSF_Instance_0'
      MCC: '123'
      MNC: '03'
    - NFINSTANCEID: 'AUSF_Instance_1'
      MCC: '123'
      MNC: '03'
    add_pnfrouteind_list:
    - NFINSTANCEID: 'AUSF_Instance_0'
      ROUTINGIND: '0000'
    - NFINSTANCEID: 'AUSF_Instance_1'
      ROUTINGIND: '0000'
    add_pnfsupi_list:
    - INDEX: 1
      NFINSTANCEID: 'AUSF_Instance_0'
      QUERYTYPE: START_END
      RANGESTART: '123031200100001'
      RANGEEND: '123031200100100'
    - INDEX: 1
      NFINSTANCEID: 'AUSF_Instance_1'
      QUERYTYPE: START_END
      RANGESTART: '123031200100001'
      RANGEEND: '123031200100100'
    mod_ngusrsecpara_list:
    - SUBRANGE: ALL_USER
      AUTHEVENT: INIT_REG-1&MOBL_INTRA_REG-0&MOBL_INTER_REG-1&PROD_REG-0&REG_AFT_INTRAHO-0&REG_AFT_INTERHO-0&IDLE_SYSCHG_REG-1&CONN_SYSCHG_REG-0&DEREGISTRATION-0&SERVICE_REQUEST-0&CONNECT_MOD-0
      AUTHPERIOD: 0
    - SUBRANGE: ALL_USER
      AUTHEVENT: INIT_REG-1&MOBL_INTRA_REG-0&MOBL_INTER_REG-1&PROD_REG-0&REG_AFT_INTRAHO-0&REG_AFT_INTERHO-0&IDLE_SYSCHG_REG-1&CONN_SYSCHG_REG-0&DEREGISTRATION-0&SERVICE_REQUEST-0&CONNECT_MOD-0
      AUTHPERIOD: 0
    add_pnfprofile_list_2:
    - NFINSTANCEID: 'UDM_Instance_0'
      NFTYPE: NfUDM
      NFSTATUS: Registered
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS1: '10.255.255.183'
      PORT: 8080
      PRIORITY: 10
    - NFINSTANCEID: 'UDM_Instance_1'
      NFTYPE: NfUDM
      NFSTATUS: Registered
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS1: '10.255.255.184'
      PORT: 8080
      PRIORITY: 10
    add_pnfservice_list_2:
    - NFINSTANCEID: 'UDM_Instance_0'
      SRVINSTANCEID: 'Service_Instance_0'
      SERVICENAME: NudmSdm
      SCHEMA: http
      NFSERVICESTATUS: REGISTERED
    - NFINSTANCEID: 'UDM_Instance_1'
      SRVINSTANCEID: 'Service_Instance_0'
      SERVICENAME: NudmSdm
      SCHEMA: http
      NFSERVICESTATUS: REGISTERED
    add_pnfplmn_list_2:
    - NFINSTANCEID: 'UDM_Instance_0'
      MCC: '123'
      MNC: '03'
    - NFINSTANCEID: 'UDM_Instance_1'
      MCC: '123'
      MNC: '03'
    add_pnfsupi_list_2:
    - INDEX: 1
      NFINSTANCEID: 'UDM_Instance_0'
      QUERYTYPE: START_END
      RANGESTART: '123031200100001'
      RANGEEND: '123031200100100'
    - INDEX: 1
      NFINSTANCEID: 'UDM_Instance_1'
      QUERYTYPE: START_END
      RANGESTART: '123031200100001'
      RANGEEND: '123031200100100'
    add_pnfprofile_list_4:
    - NFINSTANCEID: 'SMF_Instance_0'
      NFTYPE: NfSMF
      NFSTATUS: Registered
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS1: '172.16.0.5'
      PORT: 8080
    - NFINSTANCEID: 'SMF_Instance_1'
      NFTYPE: NfSMF
      NFSTATUS: Registered
      IPADDRESSTYPE: IPTypeV4
      IPV4ADDRESS1: '172.16.0.6'
      PORT: 8080
    add_pnfservice_list_6:
    - NFINSTANCEID: 'SMF_Instance_0'
      SRVINSTANCEID: 'Service_Instance_0'
      SERVICENAME: NsmfPduSes
      SCHEMA: http
      NFSERVICESTATUS: REGISTERED
    - NFINSTANCEID: 'SMF_Instance_1'
      SRVINSTANCEID: 'Service_Instance_0'
      SERVICENAME: NsmfPduSes
      SCHEMA: http
      NFSERVICESTATUS: REGISTERED
    add_pnfplmn_list_4:
    - NFINSTANCEID: 'SMF_Instance_0'
      MCC: '123'
      MNC: '03'
    - NFINSTANCEID: 'SMF_Instance_1'
      MCC: '123'
      MNC: '03'
    add_pnfsmfinfo_list:
    - NFINSTANCEID: 'SMF_Instance_0'
      PGWFQDN: 'huawei.com.apn.epc.mnc001.mcc123.3gppnetwork.org'
    - NFINSTANCEID: 'SMF_Instance_1'
      PGWFQDN: 'huawei.com.apn.epc.mnc001.mcc123.3gppnetwork.org'
    add_pnfdnn_list:
    - INDEX: 1
      NFINSTANCEID: 'SMF_Instance_0'
      DNN: 'huawei.com'
    - INDEX: 1
      NFINSTANCEID: 'SMF_Instance_1'
      DNN: 'huawei.com'
    add_pnfns_list:
    - INDEX: 1
      NFINSTANCEID: 'SMF_Instance_0'
      SST: 1
      SD: '010101'
    - INDEX: 1
      NFINSTANCEID: 'SMF_Instance_1'
      SST: 1
      SD: '010101'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 **配置****AMF服务化接口数据**

### 如果要配置IPv4v6双栈类型的服务化接口，该服务化接口的业务逻辑IP地址需要配置IPv4和IPv6类型的IP地址（通过**ADD LOGICIP**配置），相应的HTTP链路也需要配置IPv4和IPv6类型的IP地址（通过**ADD HTTPLE**配置）。

### 当本端以及对端都配置了IPv4v6双栈类型的IP地址时，UNC侧可以通过将软参**DWORD1 BIT24**设置为**“1”**来确保在业务流程中优选IPv6地址进行建链。

#### 1.1 增加AMF服务化接口的IP地址。

##### 1.1.1 //DC1

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

#### 1.2 配置AMF服务化接口的HTTP信息。

##### 1.2.1 配置HTTP本端端点组信息。

###### 1.2.1.1 //DC1

```jinja2
{%- for item in add_httplegrp_list -%}
    ADD HTTPLEGRP:
    {#- --- 必选参数 --- -#}
    INDEX={{item.INDEX}},
    {#- --- 可选参数 --- -#}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 1.2.2 配置分别作为HTTP服务的服务端和客户端的本端端点信息。

###### 1.2.2.1 //DC1

```jinja2
{%- for item in add_httple_list -%}
    ADD HTTPLE:
    {#- --- 必选参数 --- -#}
    INDEX={{item.INDEX}},
    HTTPLEGRPIDX={{item.HTTPLEGRPIDX}},
    LETYPE={{item.LETYPE}},
    IPTYPE={{item.IPTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.VPNNAME is not none -%}
        VPNNAME="{{item.VPNNAME}}",
    {%- endif -%}
    {%- if item.DESC is not none -%}
        DESC="{{item.DESC}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPTYPE=IPv4 时必选 --- -#}
    {%- if item.IPTYPE == 'IPv4' -%}
        IPV4="{{item.IPV4}}",
    {%- endif -%}
    {#- --- 条件必选：LETYPE=SERVER 时必选 --- -#}
    {%- if item.LETYPE == 'SERVER' -%}
        TLSFLG={{item.TLSFLG}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：LETYPE=SERVER 时可选 --- -#}
    {%- if item.LETYPE == 'SERVER' -%}
        {%- if item.PORT is not none -%}
            PORT={{item.PORT}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.3 配置AMF服务化接口的接入点信息。

##### 1.3.1 //DC1

```jinja2
{%- for item in add_sbiaple_list -%}
    ADD SBIAPLE:
    {#- --- 必选参数 --- -#}
    INDEX={{item.INDEX}},
    HTTPLEGRPIDX={{item.HTTPLEGRPIDX}},
    NFTYPE={{item.NFTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.DESCRIPTION is not none -%}
        DESCRIPTION="{{item.DESCRIPTION}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 1.4 配置HTTP属性。在超大报文场景下，可以通过合理设置接收HTTP响应/请求消息体的超时时间、HTTP响应/请求消息体的最大大小、请求消息中JSON数据的最大叶子节点个数等参数，避免发送/请求报文不完整，导致业务处理异常。

##### 1.4.1 //DC1

```jinja2
{%- for item in set_httpconf_list -%}
    SET HTTPCONF:
    {#- --- 可选参数 --- -#}
    {%- if item.SERVERRCVBDTMT is not none -%}
        SERVERRCVBDTMT={{item.SERVERRCVBDTMT}},
    {%- endif -%}
    {%- if item.SERVERSNDRSPTMT is not none -%}
        SERVERSNDRSPTMT={{item.SERVERSNDRSPTMT}},
    {%- endif -%}
    {%- if item.MAXBODYSIZE is not none -%}
        MAXBODYSIZE={{item.MAXBODYSIZE}},
    {%- endif -%}
    {%- if item.MAXJSONLEAFNUM is not none -%}
        MAXJSONLEAFNUM={{item.MAXJSONLEAFNUM}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 **配置到AUSF的对接数据**

#### 2.1 配置到AUSF的数据，包括AUSF的Profile、Service、路由信息、PLMN等信息。

#### AMF可以基于基于DNN、DNAI、切片、TAI、PLMN、SUPI、RouteID选择AUSF，园区可以基于规划的选择条件进行配置，此处以PLMN、RouteID为例说明配置过程。

##### 2.1.2 //和本DC内AUSF对接

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
    {%- if item.PRIORITY is not none -%}
        PRIORITY={{item.PRIORITY}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPADDRESSTYPE=IPTypeV4/IPTypeV4V6 时必选 --- -#}
    {%- if item.IPADDRESSTYPE in ['IPTypeV4', 'IPTypeV4V6'] -%}
        IPV4ADDRESS1="{{item.IPV4ADDRESS1}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_pnfservice_list -%}
    ADD PNFSERVICE:
    {#- --- 必选参数 --- -#}
    NFINSTANCEID="{{item.NFINSTANCEID}}",
    SRVINSTANCEID="{{item.SRVINSTANCEID}}",
    SERVICENAME={{item.SERVICENAME}},
    SCHEMA={{item.SCHEMA}},
    {#- --- 可选参数 --- -#}
    {%- if item.NFSERVICESTATUS is not none -%}
        NFSERVICESTATUS={{item.NFSERVICESTATUS}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_pnfplmn_list -%}
    ADD PNFPLMN:
    {#- --- 必选参数 --- -#}
    NFINSTANCEID="{{item.NFINSTANCEID}}",
    MCC="{{item.MCC}}",
    MNC="{{item.MNC}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_pnfrouteind_list -%}
    ADD PNFROUTEIND:
    {#- --- 必选参数 --- -#}
    NFINSTANCEID="{{item.NFINSTANCEID}}",
    ROUTINGIND="{{item.ROUTINGIND}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_pnfsupi_list -%}
    ADD PNFSUPI:
    {#- --- 必选参数 --- -#}
    INDEX={{item.INDEX}},
    NFINSTANCEID="{{item.NFINSTANCEID}}",
    QUERYTYPE={{item.QUERYTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：QUERYTYPE=START_END 时必选 --- -#}
    {%- if item.QUERYTYPE == 'START_END' -%}
        RANGESTART="{{item.RANGESTART}}",
    {%- endif -%}
    {#- --- 条件必选：QUERYTYPE=START_END 时必选 --- -#}
    {%- if item.QUERYTYPE == 'START_END' -%}
        RANGEEND="{{item.RANGEEND}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.2 关闭周期性鉴权。

##### 2.2.1 //DC1

```jinja2
{%- for item in mod_ngusrsecpara_list -%}
    MOD NGUSRSECPARA:
    {#- --- 必选参数 --- -#}
    SUBRANGE={{item.SUBRANGE}},
    {#- --- 可选参数 --- -#}
    {%- if item.AUTHEVENT is not none -%}
        AUTHEVENT={{item.AUTHEVENT}},
    {%- endif -%}
    {%- if item.AUTHPERIOD is not none -%}
        AUTHPERIOD={{item.AUTHPERIOD}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 **配置到UDM的对接数据**

#### 3.1 配置到UDM的数据，包括UDM的Profile、Service、PLMN信息、支持的SUPI范围等信息。

#### UEG中AMF和SMF共部署，如果在配置SMF的时候已经配置和UDM的对接配置，则本步骤无需重复配置。

#### AMF可以基于基于DNN、DNAI、切片、TAI、PLMN、SUPI、GroupID选择UDM，园区可以基于规划的选择条件进行配置，此处以PLMN、SUPI为例说明配置过程。

##### 3.1.2 //和本DC内的UDM对接

```jinja2
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
    {%- if item.PRIORITY is not none -%}
        PRIORITY={{item.PRIORITY}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPADDRESSTYPE=IPTypeV4/IPTypeV4V6 时必选 --- -#}
    {%- if item.IPADDRESSTYPE in ['IPTypeV4', 'IPTypeV4V6'] -%}
        IPV4ADDRESS1="{{item.IPV4ADDRESS1}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_pnfservice_list_2 -%}
    ADD PNFSERVICE:
    {#- --- 必选参数 --- -#}
    NFINSTANCEID="{{item.NFINSTANCEID}}",
    SRVINSTANCEID="{{item.SRVINSTANCEID}}",
    SERVICENAME={{item.SERVICENAME}},
    SCHEMA={{item.SCHEMA}},
    {#- --- 可选参数 --- -#}
    {%- if item.NFSERVICESTATUS is not none -%}
        NFSERVICESTATUS={{item.NFSERVICESTATUS}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_pnfplmn_list_2 -%}
    ADD PNFPLMN:
    {#- --- 必选参数 --- -#}
    NFINSTANCEID="{{item.NFINSTANCEID}}",
    MCC="{{item.MCC}}",
    MNC="{{item.MNC}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_pnfsupi_list_2 -%}
    ADD PNFSUPI:
    {#- --- 必选参数 --- -#}
    INDEX={{item.INDEX}},
    NFINSTANCEID="{{item.NFINSTANCEID}}",
    QUERYTYPE={{item.QUERYTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：QUERYTYPE=START_END 时必选 --- -#}
    {%- if item.QUERYTYPE == 'START_END' -%}
        RANGESTART="{{item.RANGESTART}}",
    {%- endif -%}
    {#- --- 条件必选：QUERYTYPE=START_END 时必选 --- -#}
    {%- if item.QUERYTYPE == 'START_END' -%}
        RANGEEND="{{item.RANGEEND}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 **配置到SMF的对接数据**

#### 4.1 配置到SMF的数据，包括SMF的Profile、Service、PLMN信息、支持的DNN、支持的切片实例等信息。

#### AMF可以基于基于DNN、DNAI、切片、TAI、PLMN、服务区域、PGW域名信息选择SMF，园区可以基于规划的选择条件进行配置，此处以PLMN、DNN、切片为例说明配置过程。

##### 4.1.2 //和本DC内SMF对接

```jinja2
{%- for item in add_pnfprofile_list_4 -%}
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
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_pnfservice_list_6 -%}
    ADD PNFSERVICE:
    {#- --- 必选参数 --- -#}
    NFINSTANCEID="{{item.NFINSTANCEID}}",
    SRVINSTANCEID="{{item.SRVINSTANCEID}}",
    SERVICENAME={{item.SERVICENAME}},
    SCHEMA={{item.SCHEMA}},
    {#- --- 可选参数 --- -#}
    {%- if item.NFSERVICESTATUS is not none -%}
        NFSERVICESTATUS={{item.NFSERVICESTATUS}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_pnfplmn_list_4 -%}
    ADD PNFPLMN:
    {#- --- 必选参数 --- -#}
    NFINSTANCEID="{{item.NFINSTANCEID}}",
    MCC="{{item.MCC}}",
    MNC="{{item.MNC}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_pnfsmfinfo_list -%}
    ADD PNFSMFINFO:
    {#- --- 必选参数 --- -#}
    NFINSTANCEID="{{item.NFINSTANCEID}}",
    PGWFQDN="{{item.PGWFQDN}}",
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
    ;
{%- endfor -%}
```

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

