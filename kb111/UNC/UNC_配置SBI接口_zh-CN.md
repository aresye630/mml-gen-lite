---
id: ''
name: 配置SBI接口
ne_type: UNC
type: feature
description: '**接口介绍**  NRF的服务化接口为Nnrf。  **图1** 服务化接口协议栈图  服务化接口间采用相同的协议栈，传输层统一采用HTTP/2协议，应用层携带不同的服务消息。因为底层的传输方式相同，所有的服务化接口就可以在同一总线上进行传输，支撑业务灵活上线。  HTTP/2（HyperText Transport Protocol 2.0）：下一代超文本传输协议。基于HTTP协议的信息交换分为四个过程：建立连接、发送请求信息、发送响应信息、关闭连接。  TLS（Transport Layer Security）：安全传输层协议。在两个通信应用程序之间提供保密性和数据完整性。  **配置建议**  * NRF的服务化接口端口号没有明确时，使用HTTP知名端口号80。 * 一个NF类型需要配置一个HTTP本端端点组和对应的HTTP本端端点，然后根据实际部署NF数量配置分别配置对应的SBI端点并绑定对应的HTTP本端端点组。'
risk_level: ''
doc_source: ["网络部署","初始配置","UNC初始配置与调测","组网对接配置","配置NRF","配置SBI接口"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
**接口介绍**NRF的服务化接口为Nnrf。**图1** 服务化接口协议栈图服务化接口间采用相同的协议栈，传输层统一采用HTTP/2协议，应用层携带不同的服务消息。因为底层的传输方式相同，所有的服务化接口就可以在同一总线上进行传输，支撑业务灵活上线。HTTP/2（HyperText Transport Protocol 2.0）：下一代超文本传输协议。基于HTTP协议的信息交换分为四个过程：建立连接、发送请求信息、发送响应信息、关闭连接。TLS（Transport Layer Security）：安全传输层协议。在两个通信应用程序之间提供保密性和数据完整性。**配置建议*** NRF的服务化接口端口号没有明确时，使用HTTP知名端口号80。* 一个NF类型需要配置一个HTTP本端端点组和对应的HTTP本端端点，然后根据实际部署NF数量配置分别配置对应的SBI端点并绑定对应的HTTP本端端点组。

## 必备事项
前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020/MAE客户端或登录OM Portal）。

* UNC软件安装已完成。

* 请了解UNC各类接口的类型及协议，具体内容请参见业务组网与逻辑接口介绍。
* 对于IPv4组网，已完成自动部署配置动态路由OSPF+BFD组网（IPv4）、配置静态路由+BFD组网（IPv4）、配置BGP over OSPF/静态路由+BFD（IPv4）或手动部署配置动态路由OSPF+BFD组网（IPv4）、配置静态路由+BFD组网（IPv4）、配置BGP over OSPF/静态路由+BFD（IPv4）。
* 对于IPv6组网，已完成自动部署配置动态路由OSPFv3+BFD组网（IPv6）、配置静态路由+BFD组网（IPv6）、配置BGP over OSPFv3/静态路由+BFD（IPv6）或手动部署配置动态路由OSPFv3+BFD组网（IPv6）、配置静态路由+BFD组网（IPv6）、配置BGP over OSPFv3/静态路由+BFD（IPv6）。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
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
          description: '配置Nnrf接口的逻辑IP地址。'
          data_source: '参见“水平网设LLD文档 -> 5G Core业务IP对接设计”。'
          pattern: ''
          default: ''
        LOGICIPV4:
          name: '逻辑IPv4地址'
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
        IPV4MTU:
          name: 'IPv4 MTU'
          type: integer
          minimum: 328
          maximum: 9600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1500
        IPV6MTU:
          name: 'IPv6 MTU值'
          type: integer
          minimum: 1280
          maximum: 9600
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1500
        LOGICIPV6:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
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
          description: '配置Nnrf接口的HTTP本端端点组信息。'
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
          data_source: ''
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
          description: '配置作为HTTP服务的服务端和客户端的本端端点信息。'
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
          description: '-'
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
          description: ''
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
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        VPNNAME:
          name: 'VPN名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TLSIDX:
          name: 'TLS索引'
          type: integer
          minimum: 1
          maximum: 128
          required: false
          description: ''
          data_source: ''
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
          description: '配置Nnrf接入点信息。'
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CHFPEERNFTYPE:
          name: 'CHF的目的NF类型'
          type: string
          enum:
          - Nnrf
          - Nocs
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERNFTYPE:
          name: '目的NF类型'
          type: string
          enum:
          - Nchf
          - Nupf
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_httpconf_list:
      type: items
      properties:
        CLIENTRCVRSPTMT:
          name: '客户端接收HTTP响应消息超时时间(s)'
          type: integer
          minimum: 1
          maximum: 20
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
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
  examples:
    add_logicip_list:
    - IPVERSION: IPv4
      LOGICIPV4: '172.16.0.7'
      VPNINSTNAME: 'VRF_SBI'
      DESC: 'FOR Server SBI'
      IPV4MTU: 1500
      IPV6MTU: 1500
      LOGICIPV6: ''
    add_httplegrp_list:
    - INDEX: 3
      DESC: 'NRF'
    add_httple_list:
    - INDEX: 5
      HTTPLEGRPIDX: 3
      LETYPE: SERVER
      IPTYPE: IPv4
      IPV4: '172.16.0.7'
      PORT: 8080
      VPNNAME: 'VRF_SBI'
      TLSFLG: NO
      DESC: 'NRF Server'
      IPV6: ''
      TLSIDX: ''
    add_sbiaple_list:
    - INDEX: 3
      HTTPLEGRPIDX: 3
      NFTYPE: NFTypeNRF
      DESCRIPTION: 'NRF'
      CHFPEERNFTYPE: ''
      PEERNFTYPE: ''
    set_httpconf_list:
    - CLIENTRCVRSPTMT: 15
      SERVERRCVBDTMT: 15
      SERVERSNDRSPTMT: 15
      MAXBODYSIZE: 10
      MAXJSONLEAFNUM: 100000
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 **可选：**增加NRF服务化接口的IP地址。当需要通过FQDN信息获取其他NF的IP信息时，无需配置此步骤。

```jinja2
{%- if is_optional_add_nrf_sbi_ip -%}
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
        {#- --- 条件必选：IPVERSION=IPv6 时必选 --- -#}
        {%- if item.IPVERSION == 'IPv6' -%}
            LOGICIPV6="{{item.LOGICIPV6}}",
        {%- endif -%}
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：IPVERSION=IPv4 时可选 --- -#}
        {%- if item.IPVERSION == 'IPv4' -%}
            {%- if item.IPV4MTU is not none -%}
                IPV4MTU={{item.IPV4MTU}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：IPVERSION=IPv6 时可选 --- -#}
        {%- if item.IPVERSION == 'IPv6' -%}
            {%- if item.IPV6MTU is not none -%}
                IPV6MTU={{item.IPV6MTU}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 3 配置NRF服务化接口的HTTP信息。

#### 3.1 配置HTTP本端端点组信息。

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

#### 3.2 配置分别作为HTTP服务的服务端和客户端的本端端点信息。

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
    {#- --- 条件必选：IPTYPE=IPv6 时必选 --- -#}
    {%- if item.IPTYPE == 'IPv6' -%}
        IPV6="{{item.IPV6}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：LETYPE=SERVER 时可选 --- -#}
    {%- if item.LETYPE == 'SERVER' -%}
        {%- if item.PORT is not none -%}
            PORT={{item.PORT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件必选/可选参数 --- -#}
    {#- --- TLS索引: 条件必选(是否启用TLS=YES) / 条件可选(本端实体类型=CLIENT) --- -#}
    {%- if (item.TLSFLG == 'YES') -%}
        TLSIDX={{item.TLSIDX}},
    {%- elif (item.LETYPE == 'CLIENT') -%}
        {%- if item.TLSIDX is not none -%}
            TLSIDX={{item.TLSIDX}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 配置NRF服务化接口的接入点信息。

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
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：NFTYPE=NFTypeCHF 时可选 --- -#}
    {%- if item.NFTYPE == 'NFTypeCHF' -%}
        {%- if item.CHFPEERNFTYPE is not none -%}
            CHFPEERNFTYPE={{item.CHFPEERNFTYPE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：NFTYPE=NFTypeSMF/NFTypeSMSF/NFTypeNWDAF/NFTypeUDN 时可选 --- -#}
    {%- if item.NFTYPE in ['NFTypeSMF', 'NFTypeSMSF', 'NFTypeNWDAF', 'NFTypeUDN'] -%}
        {%- if item.PEERNFTYPE is not none -%}
            PEERNFTYPE={{item.PEERNFTYPE}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 **可选：**配置HTTP属性。在超大报文场景下，可以通过合理设置接收HTTP响应/请求消息体的超时时间、HTTP响应/请求消息体的最大大小、请求消息中JSON数据的最大叶子节点个数等参数，避免发送/请求报文不完整，导致业务处理异常。

```jinja2
{%- if is_optional_config_http_property -%}
    {%- for item in set_httpconf_list -%}
        SET HTTPCONF:
        {#- --- 可选参数 --- -#}
        {%- if item.CLIENTRCVRSPTMT is not none -%}
            CLIENTRCVRSPTMT={{item.CLIENTRCVRSPTMT}},
        {%- endif -%}
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
{%- endif -%}
```

