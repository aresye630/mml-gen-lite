---
id: ''
name: 激活支持GRE
ne_type: UNC
type: feature
description: 本操作指导介绍在运行网络中创建GRE隧道的操作过程。  通用路由封装GRE（Generic Routing Encapsulation）是对某些网络层协议的报文进行封装，使这些被封装的报文能够在另一网络层协议（如IP）中传输。GRE可以作为VPN的第三层隧道协议，为VPN数据提供透明传输通道。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","IP基本功能","IPFD-015002 GRE","特性配置","激活支持GRE"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中创建GRE隧道的操作过程。通用路由封装GRE（Generic Routing Encapsulation）是对某些网络层协议的报文进行封装，使这些被封装的报文能够在另一网络层协议（如IP）中传输。GRE可以作为VPN的第三层隧道协议，为VPN数据提供透明传输通道。

## 必备事项
前提条件

* 隧道源端口和目的端口已路由可达。
* 待创建的GRE隧道不存在。
* 如果运营商规划采用VPN组网方式，则操作员在执行本操作前应已创建了相应的VPN实例。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_interface_list:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_ifipv4address_list:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IFIPADDR:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SUBNETMASK:
          name: 'IPv4地址掩码'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ADDRTYPE:
          name: 'IPv4地址类型'
          type: string
          enum:
          - main
          - sub
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: main
    add_interface_list_1:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_ifipv4address_list_1:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IFIPADDR:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SUBNETMASK:
          name: 'IPv4地址掩码'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ADDRTYPE:
          name: 'IPv4地址类型'
          type: string
          enum:
          - main
          - sub
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: main
    add_gretunnel_list:
      type: items
      properties:
        TNLNAME:
          name: '隧道名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        TNLTYPE:
          name: '隧道类型'
          type: string
          enum:
          - gre
          - gre6
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SRCTYPE:
          name: 'IPv4源类型'
          type: string
          enum:
          - if_name
          - ip_address
          - no_type
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: no_type
        SRCIPADDR:
          name: '源IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DSTIPADDR:
          name: '目的IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '对端规划'
          pattern: ''
          default: ''
        SRCTYPE6:
          name: 'IPv6源类型'
          type: string
          enum:
          - if_name
          - ip_address
          - no_type
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: no_type
        SRCIFNAME:
          name: '源接口名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DSTIPV6ADDR:
          name: '目的IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRCIPV6ADDR:
          name: '源IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REDUNDANCYEN:
          name: '使能备份隧道功能'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
    add_ifipv4address_list_3:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IFIPADDR:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SUBNETMASK:
          name: 'IPv4地址掩码'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ADDRTYPE:
          name: 'IPv4地址类型'
          type: string
          enum:
          - main
          - sub
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: main
    add_gretunnel_list_1:
      type: items
      properties:
        TNLNAME:
          name: '隧道名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        TNLTYPE:
          name: '隧道类型'
          type: string
          enum:
          - gre
          - gre6
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SRCTYPE:
          name: 'IPv4源类型'
          type: string
          enum:
          - if_name
          - ip_address
          - no_type
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: no_type
        SRCIFNAME:
          name: '源接口名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DSTIPADDR:
          name: '目的IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '对端规划'
          pattern: ''
          default: ''
        SRCTYPE6:
          name: 'IPv6源类型'
          type: string
          enum:
          - if_name
          - ip_address
          - no_type
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: no_type
        DSTIPV6ADDR:
          name: '目的IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRCIPADDR:
          name: '源IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRCIPV6ADDR:
          name: '源IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REDUNDANCYEN:
          name: '使能备份隧道功能'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
    add_ifipv4address_list_4:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IFIPADDR:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SUBNETMASK:
          name: 'IPv4地址掩码'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ADDRTYPE:
          name: 'IPv4地址类型'
          type: string
          enum:
          - main
          - sub
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: main
    add_gretunnel_list_2:
      type: items
      properties:
        TNLNAME:
          name: '隧道名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        TNLTYPE:
          name: '隧道类型'
          type: string
          enum:
          - gre
          - gre6
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        SRCTYPE:
          name: 'IPv4源类型'
          type: string
          enum:
          - if_name
          - ip_address
          - no_type
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: no_type
        SRCIFNAME:
          name: '源接口名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DSTIPADDR:
          name: '目的IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '对端规划'
          pattern: ''
          default: ''
        SRCTYPE6:
          name: 'IPv6源类型'
          type: string
          enum:
          - if_name
          - ip_address
          - no_type
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: no_type
        DSTIPV6ADDR:
          name: '目的IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRCIPADDR:
          name: '源IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRCIPV6ADDR:
          name: '源IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REDUNDANCYEN:
          name: '使能备份隧道功能'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
    add_ifipv4address_list_5:
      type: items
      properties:
        IFNAME:
          name: '接口名'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        IFIPADDR:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        SUBNETMASK:
          name: 'IPv4地址掩码'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        ADDRTYPE:
          name: 'IPv4地址类型'
          type: string
          enum:
          - main
          - sub
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: main
    add_srroute_list:
      type: items
      properties:
        AFTYPE:
          name: '地址族'
          type: string
          enum:
          - ipv4unicast
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PREFIX:
          name: '路由前缀'
          type: string
          maxLength: 15
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MASKLENGTH:
          name: '路由掩码长度'
          type: integer
          minimum: 0
          maximum: 32
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IFNAME:
          name: '路由出接口名字'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_gretunnel_list_3:
      type: items
      properties:
        TNLNAME:
          name: '隧道名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        TNLTYPE:
          name: '隧道类型'
          type: string
          enum:
          - gre
          - gre6
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        CHECKSUMEN:
          name: '使能端到端校验功能'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        SRCTYPE6:
          name: 'IPv6源类型'
          type: string
          enum:
          - if_name
          - ip_address
          - no_type
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: no_type
        SRCIFNAME:
          name: '源接口名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DSTIPV6ADDR:
          name: '目的IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRCTYPE:
          name: 'IPv4源类型'
          type: string
          enum:
          - if_name
          - ip_address
          - no_type
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: no_type
        SRCIPV6ADDR:
          name: '源IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DSTIPADDR:
          name: '目的IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REDUNDANCYEN:
          name: '使能备份隧道功能'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
    mod_gretunnel_list:
      type: items
      properties:
        TNLNAME:
          name: '隧道名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TNLTYPE:
          name: '隧道类型'
          type: string
          enum:
          - gre
          - gre6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CHECKSUMEN:
          name: '使能端到端校验功能'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DSTIPADDR:
          name: '目的IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DSTIPV6ADDR:
          name: '目的IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REDUNDANCYEN:
          name: '使能备份隧道功能'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRCTYPE:
          name: 'IPv4源类型'
          type: string
          enum:
          - if_name
          - ip_address
          - no_type
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRCTYPE6:
          name: 'IPv6源类型'
          type: string
          enum:
          - if_name
          - ip_address
          - no_type
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_gretunnel_list_4:
      type: items
      properties:
        TNLNAME:
          name: '隧道名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        TNLTYPE:
          name: '隧道类型'
          type: string
          enum:
          - gre
          - gre6
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        GREKEYEN:
          name: '使能识别关键字功能'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        GREKEY:
          name: '识别关键字'
          type: string
          maxLength: 268
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRCTYPE6:
          name: 'IPv6源类型'
          type: string
          enum:
          - if_name
          - ip_address
          - no_type
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: no_type
        SRCIFNAME:
          name: '源接口名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DSTIPV6ADDR:
          name: '目的IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRCTYPE:
          name: 'IPv4源类型'
          type: string
          enum:
          - if_name
          - ip_address
          - no_type
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: no_type
        SRCIPV6ADDR:
          name: '源IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DSTIPADDR:
          name: '目的IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REDUNDANCYEN:
          name: '使能备份隧道功能'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
    mod_gretunnel_list_2:
      type: items
      properties:
        TNLNAME:
          name: '隧道名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TNLTYPE:
          name: '隧道类型'
          type: string
          enum:
          - gre
          - gre6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GREKEYEN:
          name: '使能识别关键字功能'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GREKEY:
          name: '识别关键字'
          type: string
          maxLength: 268
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DSTIPADDR:
          name: '目的IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DSTIPV6ADDR:
          name: '目的IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REDUNDANCYEN:
          name: '使能备份隧道功能'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRCTYPE:
          name: 'IPv4源类型'
          type: string
          enum:
          - if_name
          - ip_address
          - no_type
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRCTYPE6:
          name: 'IPv6源类型'
          type: string
          enum:
          - if_name
          - ip_address
          - no_type
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_gretunnel_list_5:
      type: items
      properties:
        TNLNAME:
          name: '隧道名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        TNLTYPE:
          name: '隧道类型'
          type: string
          enum:
          - gre
          - gre6
          required: true
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: ''
        KEEPALVEN:
          name: '使能Keepalive功能'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
        KEEPALVPERIOD:
          name: 'Keepalive报文发送周期'
          type: integer
          minimum: 1
          maximum: 32767
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 5
        KEEPALVRETRYCNT:
          name: '不可达计数器参数'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 3
        SRCTYPE6:
          name: 'IPv6源类型'
          type: string
          enum:
          - if_name
          - ip_address
          - no_type
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: no_type
        SRCIFNAME:
          name: '源接口名称'
          type: string
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DSTIPV6ADDR:
          name: '目的IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRCTYPE:
          name: 'IPv4源类型'
          type: string
          enum:
          - if_name
          - ip_address
          - no_type
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: no_type
        SRCIPV6ADDR:
          name: '源IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DSTIPADDR:
          name: '目的IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REDUNDANCYEN:
          name: '使能备份隧道功能'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: FALSE
    mod_gretunnel_list_4:
      type: items
      properties:
        TNLNAME:
          name: '隧道名称'
          type: string
          maxLength: 63
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TNLTYPE:
          name: '隧道类型'
          type: string
          enum:
          - gre
          - gre6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        KEEPALVEN:
          name: '使能Keepalive功能'
          type: string
          enum:
          - FALSE
          - TRUE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        KEEPALVPERIOD:
          name: 'Keepalive报文发送周期'
          type: integer
          minimum: 1
          maximum: 32767
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        KEEPALVRETRYCNT:
          name: '不可达计数器参数'
          type: integer
          minimum: 1
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DSTIPADDR:
          name: '目的IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DSTIPV6ADDR:
          name: '目的IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        REDUNDANCYEN:
          name: '使能备份隧道功能'
          type: string
          enum:
          - TRUE
          - FALSE
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRCTYPE:
          name: 'IPv4源类型'
          type: string
          enum:
          - if_name
          - ip_address
          - no_type
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SRCTYPE6:
          name: 'IPv6源类型'
          type: string
          enum:
          - if_name
          - ip_address
          - no_type
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_interface_list:
    - IFNAME: 'LoopBack1'
    add_ifipv4address_list:
    - IFNAME: 'LoopBack1'
      IFIPADDR: '10.3.3.11'
      SUBNETMASK: '255.255.255.255'
      ADDRTYPE: main
    add_interface_list_1:
    - IFNAME: 'LoopBack1'
    add_ifipv4address_list_1:
    - IFNAME: 'LoopBack1'
      IFIPADDR: '10.3.3.11'
      SUBNETMASK: '255.255.255.255'
      ADDRTYPE: main
    add_gretunnel_list:
    - TNLNAME: 'Tunnel1'
      TNLTYPE: gre
      SRCTYPE: if_name
      SRCIPADDR: '源IPv4地址'
      DSTIPADDR: '10.4.4.11'
      SRCTYPE6: no_type
      SRCIFNAME: 'LoopBack1'
      DSTIPV6ADDR: '2001:db8::100'
      SRCIPV6ADDR: ''
      REDUNDANCYEN: FALSE
    add_ifipv4address_list_3:
    - IFNAME: 'LoopBack1'
      IFIPADDR: '10.3.3.11'
      SUBNETMASK: '255.255.255.255'
      ADDRTYPE: main
    add_gretunnel_list_1:
    - TNLNAME: 'Tunnel1'
      TNLTYPE: gre
      SRCTYPE: if_name
      SRCIFNAME: 'LoopBack1'
      DSTIPADDR: '10.4.4.11'
      SRCTYPE6: no_type
      DSTIPV6ADDR: '2001:db8::100'
      SRCIPADDR: ''
      SRCIPV6ADDR: ''
      REDUNDANCYEN: FALSE
    add_ifipv4address_list_4:
    - IFNAME: 'Tunnel1'
      IFIPADDR: '10.10.1.201'
      SUBNETMASK: '255.255.255.0'
      ADDRTYPE: main
    add_gretunnel_list_2:
    - TNLNAME: 'Tunnel1'
      TNLTYPE: gre
      SRCTYPE: if_name
      SRCIFNAME: 'LoopBack1'
      DSTIPADDR: '10.3.3.11'
      SRCTYPE6: no_type
      DSTIPV6ADDR: '2001:db8::100'
      SRCIPADDR: ''
      SRCIPV6ADDR: ''
      REDUNDANCYEN: FALSE
    add_ifipv4address_list_5:
    - IFNAME: 'Tunnel1'
      IFIPADDR: '10.10.1.202'
      SUBNETMASK: '255.255.255.0'
      ADDRTYPE: main
    add_srroute_list:
    - AFTYPE: 地址族
      PREFIX: '路由前缀'
      MASKLENGTH: 路由掩码长度
      IFNAME: '路由接口名字'
    add_gretunnel_list_3:
    - TNLNAME: 'Tunnel1'
      TNLTYPE: gre
      CHECKSUMEN: 使能端到端校验功能
      SRCTYPE6: no_type
      SRCIFNAME: 'LoopBack1'
      DSTIPV6ADDR: '2001:db8::100'
      SRCTYPE: no_type
      SRCIPV6ADDR: ''
      DSTIPADDR: ''
      REDUNDANCYEN: FALSE
    mod_gretunnel_list:
    - TNLNAME: 'Tunnel1'
      TNLTYPE: gre
      CHECKSUMEN: TRUE
      DSTIPADDR: ''
      DSTIPV6ADDR: ''
      REDUNDANCYEN: ''
      SRCTYPE: ''
      SRCTYPE6: ''
    add_gretunnel_list_4:
    - TNLNAME: 'Tunnel1'
      TNLTYPE: gre
      GREKEYEN: 使能识别关键字功能
      GREKEY: '识别关键字'
      SRCTYPE6: no_type
      SRCIFNAME: 'LoopBack1'
      DSTIPV6ADDR: '2001:db8::100'
      SRCTYPE: no_type
      SRCIPV6ADDR: ''
      DSTIPADDR: ''
      REDUNDANCYEN: FALSE
    mod_gretunnel_list_2:
    - TNLNAME: 'Tunnel1'
      TNLTYPE: gre
      GREKEYEN: TRUE
      GREKEY: '123'
      DSTIPADDR: ''
      DSTIPV6ADDR: ''
      REDUNDANCYEN: ''
      SRCTYPE: ''
      SRCTYPE6: ''
    add_gretunnel_list_5:
    - TNLNAME: 'Tunnel1'
      TNLTYPE: gre
      KEEPALVEN: 使能Keepalive功能
      KEEPALVPERIOD: Keepalive报文发送周期
      KEEPALVRETRYCNT: 不可达计数器参数
      SRCTYPE6: no_type
      SRCIFNAME: 'LoopBack1'
      DSTIPV6ADDR: '2001:db8::100'
      SRCTYPE: no_type
      SRCIPV6ADDR: ''
      DSTIPADDR: ''
      REDUNDANCYEN: FALSE
    mod_gretunnel_list_4:
    - TNLNAME: 'Tunnel1'
      TNLTYPE: gre
      KEEPALVEN: TRUE
      KEEPALVPERIOD: 5
      KEEPALVRETRYCNT: 3
      DSTIPADDR: ''
      DSTIPV6ADDR: ''
      REDUNDANCYEN: ''
      SRCTYPE: ''
      SRCTYPE6: ''
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置LoopBack接口。

### 在“MML命令行-UNC”窗口上执行：

```jinja2
{%- for item in add_interface_list -%}
    ADD INTERFACE:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_ifipv4address_list -%}
    ADD IFIPV4ADDRESS:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    IFIPADDR="{{item.IFIPADDR}}",
    SUBNETMASK="{{item.SUBNETMASK}}",
    {#- --- 可选参数 --- -#}
    {%- if item.ADDRTYPE is not none -%}
        ADDRTYPE={{item.ADDRTYPE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_interface_list_1 -%}
    ADD INTERFACE:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_ifipv4address_list_1 -%}
    ADD IFIPV4ADDRESS:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    IFIPADDR="{{item.IFIPADDR}}",
    SUBNETMASK="{{item.SUBNETMASK}}",
    {#- --- 可选参数 --- -#}
    {%- if item.ADDRTYPE is not none -%}
        ADDRTYPE={{item.ADDRTYPE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 2 配置Tunnel接口。

### 在“MML命令行-UNC”窗口上执行：

```jinja2
{%- for item in add_gretunnel_list -%}
    ADD GRETUNNEL:
    {#- --- 必选参数 --- -#}
    TNLNAME="{{item.TNLNAME}}",
    TNLTYPE={{item.TNLTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：TNLTYPE=gre 时必选 --- -#}
    {%- if item.TNLTYPE == 'gre' -%}
        SRCTYPE={{item.SRCTYPE}},
    {%- endif -%}
    {#- --- 条件必选：SRCTYPE=ip_address 时必选 --- -#}
    {%- if item.SRCTYPE == 'ip_address' -%}
        SRCIPADDR="{{item.SRCIPADDR}}",
    {%- endif -%}
    {#- --- 条件必选：SRCTYPE=if_name 时必选 --- -#}
    {%- if item.SRCTYPE == 'if_name' -%}
        SRCIFNAME="{{item.SRCIFNAME}}",
    {#- --- 条件必选：SRCTYPE6=if_name 时必选 --- -#}
    {%- elif item.SRCTYPE6 == 'if_name' -%}
        SRCIFNAME="{{item.SRCIFNAME}}",
    {%- endif -%}
    {#- --- 条件必选：SRCTYPE6=ip_address 时必选 --- -#}
    {%- if item.SRCTYPE6 == 'ip_address' -%}
        SRCIPV6ADDR="{{item.SRCIPV6ADDR}}",
    {%- endif -%}
    {#- --- 条件必选：TNLTYPE=gre6 时必选 --- -#}
    {%- if item.TNLTYPE == 'gre6' -%}
        SRCTYPE6={{item.SRCTYPE6}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：TNLTYPE=gre 时可选 --- -#}
    {%- if item.TNLTYPE == 'gre' -%}
        {%- if item.DSTIPADDR is not none -%}
            DSTIPADDR="{{item.DSTIPADDR}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TNLTYPE=gre6 时可选 --- -#}
    {%- if item.TNLTYPE == 'gre6' -%}
        {%- if item.DSTIPV6ADDR is not none -%}
            DSTIPV6ADDR="{{item.DSTIPV6ADDR}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TNLTYPE=gre/gre6 时可选 --- -#}
    {%- if item.TNLTYPE in ['gre', 'gre6'] -%}
        {%- if item.REDUNDANCYEN is not none -%}
            REDUNDANCYEN={{item.REDUNDANCYEN}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_ifipv4address_list_3 -%}
    ADD IFIPV4ADDRESS:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    IFIPADDR="{{item.IFIPADDR}}",
    SUBNETMASK="{{item.SUBNETMASK}}",
    {#- --- 可选参数 --- -#}
    {%- if item.ADDRTYPE is not none -%}
        ADDRTYPE={{item.ADDRTYPE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 为了不影响GRE隧道收发报文性能，建议使用**MOD INTERFACE**命令配置GRE Tunnel的MTU值，该MTU值小于等于（出接口的MTU值-GRE头的长度），GRE头封装格式为：GRE header + 外层IP header。

```jinja2
{%- for item in add_gretunnel_list_1 -%}
    ADD GRETUNNEL:
    {#- --- 必选参数 --- -#}
    TNLNAME="{{item.TNLNAME}}",
    TNLTYPE={{item.TNLTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：TNLTYPE=gre 时必选 --- -#}
    {%- if item.TNLTYPE == 'gre' -%}
        SRCTYPE={{item.SRCTYPE}},
    {%- endif -%}
    {#- --- 条件必选：SRCTYPE=if_name 时必选 --- -#}
    {%- if item.SRCTYPE == 'if_name' -%}
        SRCIFNAME="{{item.SRCIFNAME}}",
    {#- --- 条件必选：SRCTYPE6=if_name 时必选 --- -#}
    {%- elif item.SRCTYPE6 == 'if_name' -%}
        SRCIFNAME="{{item.SRCIFNAME}}",
    {%- endif -%}
    {#- --- 条件必选：SRCTYPE=ip_address 时必选 --- -#}
    {%- if item.SRCTYPE == 'ip_address' -%}
        SRCIPADDR="{{item.SRCIPADDR}}",
    {%- endif -%}
    {#- --- 条件必选：SRCTYPE6=ip_address 时必选 --- -#}
    {%- if item.SRCTYPE6 == 'ip_address' -%}
        SRCIPV6ADDR="{{item.SRCIPV6ADDR}}",
    {%- endif -%}
    {#- --- 条件必选：TNLTYPE=gre6 时必选 --- -#}
    {%- if item.TNLTYPE == 'gre6' -%}
        SRCTYPE6={{item.SRCTYPE6}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：TNLTYPE=gre 时可选 --- -#}
    {%- if item.TNLTYPE == 'gre' -%}
        {%- if item.DSTIPADDR is not none -%}
            DSTIPADDR="{{item.DSTIPADDR}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TNLTYPE=gre6 时可选 --- -#}
    {%- if item.TNLTYPE == 'gre6' -%}
        {%- if item.DSTIPV6ADDR is not none -%}
            DSTIPV6ADDR="{{item.DSTIPV6ADDR}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TNLTYPE=gre/gre6 时可选 --- -#}
    {%- if item.TNLTYPE in ['gre', 'gre6'] -%}
        {%- if item.REDUNDANCYEN is not none -%}
            REDUNDANCYEN={{item.REDUNDANCYEN}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_ifipv4address_list_4 -%}
    ADD IFIPV4ADDRESS:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    IFIPADDR="{{item.IFIPADDR}}",
    SUBNETMASK="{{item.SUBNETMASK}}",
    {#- --- 可选参数 --- -#}
    {%- if item.ADDRTYPE is not none -%}
        ADDRTYPE={{item.ADDRTYPE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_gretunnel_list_2 -%}
    ADD GRETUNNEL:
    {#- --- 必选参数 --- -#}
    TNLNAME="{{item.TNLNAME}}",
    TNLTYPE={{item.TNLTYPE}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：TNLTYPE=gre 时必选 --- -#}
    {%- if item.TNLTYPE == 'gre' -%}
        SRCTYPE={{item.SRCTYPE}},
    {%- endif -%}
    {#- --- 条件必选：SRCTYPE=if_name 时必选 --- -#}
    {%- if item.SRCTYPE == 'if_name' -%}
        SRCIFNAME="{{item.SRCIFNAME}}",
    {#- --- 条件必选：SRCTYPE6=if_name 时必选 --- -#}
    {%- elif item.SRCTYPE6 == 'if_name' -%}
        SRCIFNAME="{{item.SRCIFNAME}}",
    {%- endif -%}
    {#- --- 条件必选：SRCTYPE=ip_address 时必选 --- -#}
    {%- if item.SRCTYPE == 'ip_address' -%}
        SRCIPADDR="{{item.SRCIPADDR}}",
    {%- endif -%}
    {#- --- 条件必选：SRCTYPE6=ip_address 时必选 --- -#}
    {%- if item.SRCTYPE6 == 'ip_address' -%}
        SRCIPV6ADDR="{{item.SRCIPV6ADDR}}",
    {%- endif -%}
    {#- --- 条件必选：TNLTYPE=gre6 时必选 --- -#}
    {%- if item.TNLTYPE == 'gre6' -%}
        SRCTYPE6={{item.SRCTYPE6}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：TNLTYPE=gre 时可选 --- -#}
    {%- if item.TNLTYPE == 'gre' -%}
        {%- if item.DSTIPADDR is not none -%}
            DSTIPADDR="{{item.DSTIPADDR}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TNLTYPE=gre6 时可选 --- -#}
    {%- if item.TNLTYPE == 'gre6' -%}
        {%- if item.DSTIPV6ADDR is not none -%}
            DSTIPV6ADDR="{{item.DSTIPV6ADDR}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TNLTYPE=gre/gre6 时可选 --- -#}
    {%- if item.TNLTYPE in ['gre', 'gre6'] -%}
        {%- if item.REDUNDANCYEN is not none -%}
            REDUNDANCYEN={{item.REDUNDANCYEN}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_ifipv4address_list_5 -%}
    ADD IFIPV4ADDRESS:
    {#- --- 必选参数 --- -#}
    IFNAME="{{item.IFNAME}}",
    IFIPADDR="{{item.IFIPADDR}}",
    SUBNETMASK="{{item.SUBNETMASK}}",
    {#- --- 可选参数 --- -#}
    {%- if item.ADDRTYPE is not none -%}
        ADDRTYPE={{item.ADDRTYPE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置隧道间静态路由

### 在“MML命令行-UNC”窗口上执行：

```jinja2
{%- for item in add_srroute_list -%}
    ADD SRROUTE:
    {#- --- 必选参数 --- -#}
    AFTYPE={{item.AFTYPE}},
    PREFIX="{{item.PREFIX}}",
    MASKLENGTH={{item.MASKLENGTH}},
    {#- --- 可选参数 --- -#}
    {%- if item.IFNAME is not none -%}
        IFNAME="{{item.IFNAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 当配置GRE隧道时，需要使能隧道端到端校验功能：

### 在“MML命令行-UNC”窗口上执行：

```jinja2
{%- for item in add_gretunnel_list_3 -%}
    ADD GRETUNNEL:
    {#- --- 必选参数 --- -#}
    TNLNAME="{{item.TNLNAME}}",
    TNLTYPE={{item.TNLTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.CHECKSUMEN is not none -%}
        CHECKSUMEN={{item.CHECKSUMEN}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：SRCTYPE=if_name 时必选 --- -#}
    {%- if item.SRCTYPE == 'if_name' -%}
        SRCIFNAME="{{item.SRCIFNAME}}",
    {#- --- 条件必选：SRCTYPE6=if_name 时必选 --- -#}
    {%- elif item.SRCTYPE6 == 'if_name' -%}
        SRCIFNAME="{{item.SRCIFNAME}}",
    {%- endif -%}
    {#- --- 条件必选：SRCTYPE6=ip_address 时必选 --- -#}
    {%- if item.SRCTYPE6 == 'ip_address' -%}
        SRCIPV6ADDR="{{item.SRCIPV6ADDR}}",
    {%- endif -%}
    {#- --- 条件必选：TNLTYPE=gre 时必选 --- -#}
    {%- if item.TNLTYPE == 'gre' -%}
        SRCTYPE={{item.SRCTYPE}},
    {%- endif -%}
    {#- --- 条件必选：TNLTYPE=gre6 时必选 --- -#}
    {%- if item.TNLTYPE == 'gre6' -%}
        SRCTYPE6={{item.SRCTYPE6}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：TNLTYPE=gre 时可选 --- -#}
    {%- if item.TNLTYPE == 'gre' -%}
        {%- if item.DSTIPADDR is not none -%}
            DSTIPADDR="{{item.DSTIPADDR}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TNLTYPE=gre6 时可选 --- -#}
    {%- if item.TNLTYPE == 'gre6' -%}
        {%- if item.DSTIPV6ADDR is not none -%}
            DSTIPV6ADDR="{{item.DSTIPV6ADDR}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TNLTYPE=gre/gre6 时可选 --- -#}
    {%- if item.TNLTYPE in ['gre', 'gre6'] -%}
        {%- if item.REDUNDANCYEN is not none -%}
            REDUNDANCYEN={{item.REDUNDANCYEN}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in mod_gretunnel_list -%}
    MOD GRETUNNEL:
    {#- --- 必选参数 --- -#}
    TNLNAME="{{item.TNLNAME}}",
    TNLTYPE={{item.TNLTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.CHECKSUMEN is not none -%}
        CHECKSUMEN={{item.CHECKSUMEN}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：TNLTYPE=gre 时可选 --- -#}
    {%- if item.TNLTYPE == 'gre' -%}
        {%- if item.DSTIPADDR is not none -%}
            DSTIPADDR="{{item.DSTIPADDR}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TNLTYPE=gre6 时可选 --- -#}
    {%- if item.TNLTYPE == 'gre6' -%}
        {%- if item.DSTIPV6ADDR is not none -%}
            DSTIPV6ADDR="{{item.DSTIPV6ADDR}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TNLTYPE=gre/gre6 时可选 --- -#}
    {%- if item.TNLTYPE in ['gre', 'gre6'] -%}
        {%- if item.REDUNDANCYEN is not none -%}
            REDUNDANCYEN={{item.REDUNDANCYEN}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TNLTYPE=gre 时可选 --- -#}
    {%- if item.TNLTYPE == 'gre' -%}
        {%- if item.SRCTYPE is not none -%}
            SRCTYPE={{item.SRCTYPE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TNLTYPE=gre6 时可选 --- -#}
    {%- if item.TNLTYPE == 'gre6' -%}
        {%- if item.SRCTYPE6 is not none -%}
            SRCTYPE6={{item.SRCTYPE6}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 5 当配置GRE隧道时，需要使能隧道识别关键字验证功能：

### 在“MML命令行-UNC”窗口上执行：

```jinja2
{%- for item in add_gretunnel_list_4 -%}
    ADD GRETUNNEL:
    {#- --- 必选参数 --- -#}
    TNLNAME="{{item.TNLNAME}}",
    TNLTYPE={{item.TNLTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.GREKEYEN is not none -%}
        GREKEYEN={{item.GREKEYEN}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：GREKEYEN=TRUE 时必选 --- -#}
    {%- if item.GREKEYEN == 'TRUE' -%}
        GREKEY="{{item.GREKEY}}",
    {%- endif -%}
    {#- --- 条件必选：SRCTYPE=if_name 时必选 --- -#}
    {%- if item.SRCTYPE == 'if_name' -%}
        SRCIFNAME="{{item.SRCIFNAME}}",
    {#- --- 条件必选：SRCTYPE6=if_name 时必选 --- -#}
    {%- elif item.SRCTYPE6 == 'if_name' -%}
        SRCIFNAME="{{item.SRCIFNAME}}",
    {%- endif -%}
    {#- --- 条件必选：SRCTYPE6=ip_address 时必选 --- -#}
    {%- if item.SRCTYPE6 == 'ip_address' -%}
        SRCIPV6ADDR="{{item.SRCIPV6ADDR}}",
    {%- endif -%}
    {#- --- 条件必选：TNLTYPE=gre 时必选 --- -#}
    {%- if item.TNLTYPE == 'gre' -%}
        SRCTYPE={{item.SRCTYPE}},
    {%- endif -%}
    {#- --- 条件必选：TNLTYPE=gre6 时必选 --- -#}
    {%- if item.TNLTYPE == 'gre6' -%}
        SRCTYPE6={{item.SRCTYPE6}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：TNLTYPE=gre 时可选 --- -#}
    {%- if item.TNLTYPE == 'gre' -%}
        {%- if item.DSTIPADDR is not none -%}
            DSTIPADDR="{{item.DSTIPADDR}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TNLTYPE=gre6 时可选 --- -#}
    {%- if item.TNLTYPE == 'gre6' -%}
        {%- if item.DSTIPV6ADDR is not none -%}
            DSTIPV6ADDR="{{item.DSTIPV6ADDR}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TNLTYPE=gre/gre6 时可选 --- -#}
    {%- if item.TNLTYPE in ['gre', 'gre6'] -%}
        {%- if item.REDUNDANCYEN is not none -%}
            REDUNDANCYEN={{item.REDUNDANCYEN}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 如果在隧道两端设置识别关键字，则必须指定相同的识别关键字；或隧道两端都不设置识别关键字。

```jinja2
{%- for item in mod_gretunnel_list_2 -%}
    MOD GRETUNNEL:
    {#- --- 必选参数 --- -#}
    TNLNAME="{{item.TNLNAME}}",
    TNLTYPE={{item.TNLTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.GREKEYEN is not none -%}
        GREKEYEN={{item.GREKEYEN}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：GREKEYEN=TRUE 时必选 --- -#}
    {%- if item.GREKEYEN == 'TRUE' -%}
        GREKEY="{{item.GREKEY}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：TNLTYPE=gre 时可选 --- -#}
    {%- if item.TNLTYPE == 'gre' -%}
        {%- if item.DSTIPADDR is not none -%}
            DSTIPADDR="{{item.DSTIPADDR}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TNLTYPE=gre6 时可选 --- -#}
    {%- if item.TNLTYPE == 'gre6' -%}
        {%- if item.DSTIPV6ADDR is not none -%}
            DSTIPV6ADDR="{{item.DSTIPV6ADDR}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TNLTYPE=gre/gre6 时可选 --- -#}
    {%- if item.TNLTYPE in ['gre', 'gre6'] -%}
        {%- if item.REDUNDANCYEN is not none -%}
            REDUNDANCYEN={{item.REDUNDANCYEN}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TNLTYPE=gre 时可选 --- -#}
    {%- if item.TNLTYPE == 'gre' -%}
        {%- if item.SRCTYPE is not none -%}
            SRCTYPE={{item.SRCTYPE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TNLTYPE=gre6 时可选 --- -#}
    {%- if item.TNLTYPE == 'gre6' -%}
        {%- if item.SRCTYPE6 is not none -%}
            SRCTYPE6={{item.SRCTYPE6}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 6 当配置GRE隧道时，需要使能隧道Keepalive功能：

### 在“MML命令行-UNC”窗口上执行：

```jinja2
{%- for item in add_gretunnel_list_5 -%}
    ADD GRETUNNEL:
    {#- --- 必选参数 --- -#}
    TNLNAME="{{item.TNLNAME}}",
    TNLTYPE={{item.TNLTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.KEEPALVEN is not none -%}
        KEEPALVEN={{item.KEEPALVEN}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：SRCTYPE=if_name 时必选 --- -#}
    {%- if item.SRCTYPE == 'if_name' -%}
        SRCIFNAME="{{item.SRCIFNAME}}",
    {#- --- 条件必选：SRCTYPE6=if_name 时必选 --- -#}
    {%- elif item.SRCTYPE6 == 'if_name' -%}
        SRCIFNAME="{{item.SRCIFNAME}}",
    {%- endif -%}
    {#- --- 条件必选：SRCTYPE6=ip_address 时必选 --- -#}
    {%- if item.SRCTYPE6 == 'ip_address' -%}
        SRCIPV6ADDR="{{item.SRCIPV6ADDR}}",
    {%- endif -%}
    {#- --- 条件必选：TNLTYPE=gre 时必选 --- -#}
    {%- if item.TNLTYPE == 'gre' -%}
        SRCTYPE={{item.SRCTYPE}},
    {%- endif -%}
    {#- --- 条件必选：TNLTYPE=gre6 时必选 --- -#}
    {%- if item.TNLTYPE == 'gre6' -%}
        SRCTYPE6={{item.SRCTYPE6}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：KEEPALVEN=TRUE 时可选 --- -#}
    {%- if item.KEEPALVEN == 'TRUE' -%}
        {%- if item.KEEPALVPERIOD is not none -%}
            KEEPALVPERIOD={{item.KEEPALVPERIOD}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：KEEPALVEN=TRUE 时可选 --- -#}
    {%- if item.KEEPALVEN == 'TRUE' -%}
        {%- if item.KEEPALVRETRYCNT is not none -%}
            KEEPALVRETRYCNT={{item.KEEPALVRETRYCNT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TNLTYPE=gre 时可选 --- -#}
    {%- if item.TNLTYPE == 'gre' -%}
        {%- if item.DSTIPADDR is not none -%}
            DSTIPADDR="{{item.DSTIPADDR}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TNLTYPE=gre6 时可选 --- -#}
    {%- if item.TNLTYPE == 'gre6' -%}
        {%- if item.DSTIPV6ADDR is not none -%}
            DSTIPV6ADDR="{{item.DSTIPV6ADDR}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TNLTYPE=gre/gre6 时可选 --- -#}
    {%- if item.TNLTYPE in ['gre', 'gre6'] -%}
        {%- if item.REDUNDANCYEN is not none -%}
            REDUNDANCYEN={{item.REDUNDANCYEN}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 若不填写参数KEEPALVPERIOD，则Keepalive报文发送周期默认为5秒。

### 若不填写参数KEEPALVRETRYCNT，则不可达计数器参数默认为3次。

```jinja2
{%- for item in mod_gretunnel_list_4 -%}
    MOD GRETUNNEL:
    {#- --- 必选参数 --- -#}
    TNLNAME="{{item.TNLNAME}}",
    TNLTYPE={{item.TNLTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.KEEPALVEN is not none -%}
        KEEPALVEN={{item.KEEPALVEN}},
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：KEEPALVEN=TRUE 时可选 --- -#}
    {%- if item.KEEPALVEN == 'TRUE' -%}
        {%- if item.KEEPALVPERIOD is not none -%}
            KEEPALVPERIOD={{item.KEEPALVPERIOD}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：KEEPALVEN=TRUE 时可选 --- -#}
    {%- if item.KEEPALVEN == 'TRUE' -%}
        {%- if item.KEEPALVRETRYCNT is not none -%}
            KEEPALVRETRYCNT={{item.KEEPALVRETRYCNT}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TNLTYPE=gre 时可选 --- -#}
    {%- if item.TNLTYPE == 'gre' -%}
        {%- if item.DSTIPADDR is not none -%}
            DSTIPADDR="{{item.DSTIPADDR}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TNLTYPE=gre6 时可选 --- -#}
    {%- if item.TNLTYPE == 'gre6' -%}
        {%- if item.DSTIPV6ADDR is not none -%}
            DSTIPV6ADDR="{{item.DSTIPV6ADDR}}",
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TNLTYPE=gre/gre6 时可选 --- -#}
    {%- if item.TNLTYPE in ['gre', 'gre6'] -%}
        {%- if item.REDUNDANCYEN is not none -%}
            REDUNDANCYEN={{item.REDUNDANCYEN}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TNLTYPE=gre 时可选 --- -#}
    {%- if item.TNLTYPE == 'gre' -%}
        {%- if item.SRCTYPE is not none -%}
            SRCTYPE={{item.SRCTYPE}},
        {%- endif -%}
    {%- endif -%}
    {#- --- 条件可选：TNLTYPE=gre6 时可选 --- -#}
    {%- if item.TNLTYPE == 'gre6' -%}
        {%- if item.SRCTYPE6 is not none -%}
            SRCTYPE6={{item.SRCTYPE6}},
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

