---
id: ''
name: 配置Mp2接口数据
ne_type: UEG
type: feature
description: 当UPF（UEG）与MPF对接时，在UPF上需要配置本页面。
tags: []
risk_level: ''
doc_source:
  - ["网络部署","园区入驻式（仅连接）","5GC toB 部署边缘站点（站点为“风筝S”，入驻式）","虚机容器模式","UEG初始配置（风筝S）","UEG初始配置","参考：详细配置指导","配置主锚点UPF","配置Mp2接口数据"]
  - ["网络部署","园区入驻+地市共享（连接+计算）","5GC toB 部署边缘站点（站点为“风筝S”，带计算）","UEG初始配置（风筝S）","初始配置与调测（入驻式UPF）","初始配置与调测（入驻式边缘UPF，非SDN）","参考：详细配置指导","配置主锚点UPF","配置Mp2接口数据"]
  - ["网络部署","园区入驻+地市共享（连接+计算）","5GC toB 部署边缘站点（站点为“风筝S”，带计算）","UEG初始配置（风筝S）","初始配置与调测（入驻式UPF）","初始配置与调测（入驻式边缘UPF，SDN）","参考：详细配置指导","配置主锚点UPF","配置Mp2接口数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
当UPF（UEG）与MPF对接时，在UPF上需要配置本页面。

## 必备事项
前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录MAE客户端或登录OM Portal）。
* 请了解UEG各类接口的类型及命名规范，具体内容请参见逻辑接口介绍（UPF）（风筝S）。
* UPF的APIGW、MPF各自的CA证书和设备证书需要客户提前申请。
* UPF的APIGW与内部服务之间认证的CA证书和设备证书操作参考加载网元内服务间证书。
```

## 2 输入参数变量定义
<!-- @mml:block= params -->
```yaml
schemas:
  properties:
    set_apiauth_list:
      type: items
      properties:
        ISAUTH:
          name: '鉴权开关'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: '-'
          data_source: '固定取值'
          pattern: ''
          default: ''
    add_vpninst_list:
      type: items
      properties:
        VPNINSTANCE:
          name: 'VPN实例名'
          type: string
          minLength: 0
          maxLength: 31
          required: true
          description: '逻辑接口的VPN一定要与其对应的外联口的VPN相同，否则从逻辑接口发出去的报文会查询路由失败。'
          data_source: '参见“5G Core LLD文档 > 路由设计 > 5G Core路由设计 > VRF设计 > VRF名称(VNF)”。'
          pattern: ''
          default: ''
    add_mpflogicinf_list:
      type: items
      properties:
        NAME:
          name: '逻辑接口名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '配置Mp2逻辑接口名称。'
          data_source: '参见“5G Core LLD文档 > 业务IP对接设计 > 业务IP设计 > 逻辑接口”。'
          pattern: ''
          default: ''
        IPVERSION:
          name: '逻辑接口的IP版本'
          type: string
          enum:
          - IPV4
          - IPV6
          - IPVER_ALL
          required: true
          description: '配置IPv4类型的逻辑接口。  Mp2接口支持IPv4v6双栈，此处以IPv4单栈为例。'
          data_source: '-'
          pattern: ''
          default: ''
        IPV4ADDRESS:
          name: '逻辑接口的IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '参见“5G Core LLD文档 > 业务IP对接设计 > 业务IP设计 > 逻辑接口IP”。'
          pattern: ''
          default: ''
        VPNINSTANCE:
          name: 'VPN实例名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: '接口绑定的VPN实例已通过**ADD VPNINST**命令配置，可以使用**LST VPNINST**命令进行查询。'
          data_source: '参见“5G Core LLD文档 > 路由设计 > 5G Core路由设计 > VRF设计 > VRF名称(VNF)”。'
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
    add_meptlspara_list:
      type: items
      properties:
        TLSPARANAME:
          name: 'TLS参数名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PROTOCOL:
          name: 'TLS协议版本'
          type: string
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        VERIFYPEER:
          name: '校验对端证书'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: '开启内部服务的TLS证书鉴权功能。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        VERIFYDEPTH:
          name: '校验深度'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 10
        DEVCERTSCENE:
          name: '设备证书场景'
          type: string
          enum:
          - INNER_DEV_CERT_SCENE
          - LE_DEV_CERT_SCENE
          - MP1_DEV_CERT_SCENE
          - MP2_DEV_CERT_SCENE
          - NOTIFY_EXTNE_DEV_CERT_SCENE
          - UAC_DEV_CERT_SCENE
          - NGVN_DEV_CERT_SCENE
          required: true
          description: '关联内部服务鉴权证书。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        CACERTSCENE:
          name: 'CA证书场景'
          type: string
          enum:
          - INNER_CA_CERT_SCENE
          - LE_CA_CERT_SCENE
          - MP1_CA_CERT_SCENE
          - MP2_CA_CERT_SCENE
          - NOTIFY_EXTNE_CA_CERT_SCENE
          - UAC_CA_CERT_SCENE
          - NGVN_CA_CERT_SCENE
          required: false
          description: '关联内部服务鉴权证书。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        CIPHERSUITES:
          name: 'TLS算法套件集合'
          type: string
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_meptlspara_list_1:
      type: items
      properties:
        TLSPARANAME:
          name: 'TLS参数名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PROTOCOL:
          name: 'TLS协议版本'
          type: string
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
        VERIFYPEER:
          name: '校验对端证书'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: '开启UPF的TLS证书鉴权功能。'
          data_source: '与对端协商'
          pattern: ''
          default: ''
        VERIFYDEPTH:
          name: '校验深度'
          type: integer
          minimum: 1
          maximum: 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 10
        DEVCERTSCENE:
          name: '设备证书场景'
          type: string
          enum:
          - INNER_DEV_CERT_SCENE
          - LE_DEV_CERT_SCENE
          - MP1_DEV_CERT_SCENE
          - MP2_DEV_CERT_SCENE
          - NOTIFY_EXTNE_DEV_CERT_SCENE
          - UAC_DEV_CERT_SCENE
          - NGVN_DEV_CERT_SCENE
          required: true
          description: '关联CSP Portal在“API网关MP2设备证书”场景上传的TLS证书。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        CACERTSCENE:
          name: 'CA证书场景'
          type: string
          enum:
          - INNER_CA_CERT_SCENE
          - LE_CA_CERT_SCENE
          - MP1_CA_CERT_SCENE
          - MP2_CA_CERT_SCENE
          - NOTIFY_EXTNE_CA_CERT_SCENE
          - UAC_CA_CERT_SCENE
          - NGVN_CA_CERT_SCENE
          required: false
          description: '关联CSP Portal在“API网关MP2接口CA证书”场景上传的TLS证书。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        CIPHERSUITES:
          name: 'TLS算法套件集合'
          type: string
          required: true
          description: '-'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_mepclientcommpara_list:
      type: items
      properties:
        PARANAME:
          name: 'HTTP客户端通信参数名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '通信参数推荐采用默认值。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CONNTIMEOUT:
          name: '与服务端建立连接超时时间'
          type: integer
          minimum: 1
          maximum: 60
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 60
        SENDREQTIMEOUT:
          name: '发送请求超时时间'
          type: integer
          minimum: 1
          maximum: 300
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 60
        WAITRSPTIMEOUT:
          name: '读取服务端响应超时时间'
          type: integer
          minimum: 1
          maximum: 300
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: 60
    add_mephttpclientgrp_list:
      type: items
      properties:
        GROUPNAME:
          name: 'MEP HTTP客户端组名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_mephttpclient_list:
      type: items
      properties:
        CLIENTNAME:
          name: 'MEP HTTP客户端名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MEPHTTPCLIENTGRP:
          name: 'MEP HTTP客户端组'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '用于指定归属的HTTP客户端组，已通过**ADD MEPHTTPCLIENTGRP**配置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CLIENTTYPE:
          name: 'MEP HTTP客户端类型'
          type: string
          enum:
          - TO_CONNECT_EXTERNAL_NE
          - TO_CONNECT_INTERNAL_MES
          required: true
          description: '用于指定UPF作为客户端向内部服务转发消息，选择“TO\_CONNECT\_INTERNAL\_MES”。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        TLSFLG:
          name: '是否启用TLS'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: '必须启用TLS证书鉴权。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        TLSPARANAME:
          name: 'TLS参数名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: '用于指定使用的TLS证书，已通过**ADD MEPTLSPARA**命令配置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CLIENTCOMMPARANAME:
          name: 'HTTP客户端通信参数名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PEERSERVICETAG:
          name: '对端服务标签'
          type: string
          enum:
          - LESERVICE
          - MEPSERVICE
          - MM5SERVICE
          - MP1SERVICE
          - MP2SERVICE
          - NGVNSERVICE
          required: false
          description: '访问的内部服务，本参数选择“MEPSERVICE”。'
          data_source: '固定取值'
          pattern: ''
          default: MP1SERVICE
    add_mepservercommpara_list:
      type: items
      properties:
        PARANAME:
          name: 'HTTP服务端通信参数名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '通信参数推荐采用默认值。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        WAITREQHEADERTIMEOUT:
          name: '读取客户端请求头超时时间'
          type: integer
          minimum: 1
          maximum: 300
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: 60
        WAITREQBODYTIMEOUT:
          name: '读取客户端请求体超时时间'
          type: integer
          minimum: 1
          maximum: 300
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: 60
        SENDRSPTIMEOUT:
          name: '向客户端发送响应超时时间'
          type: integer
          minimum: 1
          maximum: 300
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: 60
        KEEPALIVETIMEOUT:
          name: '连接保活超时时间'
          type: integer
          minimum: 1
          maximum: 7200
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: 75
        KEEPALIVEMAXREQNUM:
          name: '保活连接可处理的最大请求数'
          type: integer
          minimum: 1
          maximum: 100000
          required: false
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: 1000
    add_mephttpservergrp_list:
      type: items
      properties:
        GROUPNAME:
          name: 'MEP HTTP服务端组名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_mephttpserver_list:
      type: items
      properties:
        SERVERNAME:
          name: 'MEP HTTP服务端名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '-'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MEPHTTPSERVERGRP:
          name: 'MEP HTTP服务端组'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '用于指定归属的HTTP服务端组，已通过**ADD MEPHTTPSERVERGRP**命令配置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SERVERTYPE:
          name: 'MEP HTTP服务端类型'
          type: string
          enum:
          - FOR_EXTERNAL_NE
          - FOR_INTERNAL_NOTIFY_MES
          - FOR_INTERNAL_POLICY_MES
          required: true
          description: '用于指定UPF作为服务端向MPF转发消息，选择“FOR\_EXTERNAL\_NE”。'
          data_source: '固定取值'
          pattern: ''
          default: ''
        IPV4:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: '使用Mp2接口IP地址，已通过**ADD MPFLOGICINF**命令配置。'
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
          data_source: '固定取值'
          pattern: ''
          default: ''
        TLSFLG:
          name: '是否启用TLS'
          type: string
          enum:
          - DISABLE
          - ENABLE
          required: true
          description: '必须启用TLS证书鉴权。'
          data_source: '固定取值'
          pattern: ''
          default: ENABLE
        TLSPARANAME:
          name: 'TLS参数名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: '用于指定使用的TLS证书，已通过**ADD MEPTLSPARA**命令配置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SERVERCOMMPARANAME:
          name: 'HTTP服务端通信参数名称'
          type: string
          minLength: 0
          maxLength: 63
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_mepreverseproxy_list:
      type: items
      properties:
        PROXYNAME:
          name: '反向代理名称'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '绑定UPF客户端与服务端，实现MPF向UPF推送动态规则业务。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MEPHTTPSERVERGRP:
          name: 'HTTP服务端索引组'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '用于指定UPF的HTTP服务端组，已通过**ADD MEPHTTPSERVERGRP**配置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        MEPHTTPCLIENTGRP:
          name: 'HTTP客户端索引组'
          type: string
          minLength: 0
          maxLength: 63
          required: true
          description: '用于指定UPF的HTTP客户端组，已通过**ADD MEPHTTPCLIENTGRP**配置。'
          data_source: '本端规划'
          pattern: ''
          default: ''
  examples:
    set_apiauth_list:
    - ISAUTH: DISABLE
    add_vpninst_list:
    - VPNINSTANCE: 'VPN_Mp2'
    add_mpflogicinf_list:
    - NAME: 'capif1/0/0'
      IPVERSION: IPV4
      IPV4ADDRESS: '10.1.10.1'
      VPNINSTANCE: 'VPN_Mp2'
    set_licenseswitch_list:
    - LICITEM: 'LKV3G5APIG01'
      SWITCH: ENABLE
    add_meptlspara_list:
    - TLSPARANAME: 'tls-inner'
      PROTOCOL: TLSv12-1&TLSv13-1
      VERIFYPEER: ENABLE
      VERIFYDEPTH: 10
      DEVCERTSCENE: INNER_DEV_CERT_SCENE
      CACERTSCENE: INNER_CA_CERT_SCENE
      CIPHERSUITES: TLS_AES_128_GCM_SHA256-1&TLS_AES_256_GCM_SHA384-1&TLS_CHACHA20_POLY1305_SHA256-1&TLS_ECDHE_ECDSA_WITH_AES_128_CCM-1&TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8-1&TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256-1&TLS_ECDHE_ECDSA_WITH_AES_256_CCM-1&TLS_ECDHE_ECDSA_WITH_AES_256_CCM_8-1&TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384-1&TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256-1&TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384-1
    add_meptlspara_list_1:
    - TLSPARANAME: 'tls05-mp2server'
      PROTOCOL: TLSv12-1&TLSv13-1
      VERIFYPEER: ENABLE
      VERIFYDEPTH: 10
      DEVCERTSCENE: MP2_DEV_CERT_SCENE
      CACERTSCENE: MP2_CA_CERT_SCENE
      CIPHERSUITES: TLS_AES_128_GCM_SHA256-1&TLS_AES_256_GCM_SHA384-1&TLS_CHACHA20_POLY1305_SHA256-1&TLS_ECDHE_ECDSA_WITH_AES_128_CCM-1&TLS_ECDHE_ECDSA_WITH_AES_128_CCM_8-1&TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256-1&TLS_ECDHE_ECDSA_WITH_AES_256_CCM-1&TLS_ECDHE_ECDSA_WITH_AES_256_CCM_8-1&TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384-1&TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256-1&TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384-1
    add_mepclientcommpara_list:
    - PARANAME: 'DefaultClientPara'
      CONNTIMEOUT: 60
      SENDREQTIMEOUT: 60
      WAITRSPTIMEOUT: 60
    add_mephttpclientgrp_list:
    - GROUPNAME: 'clientgrp01'
    add_mephttpclient_list:
    - CLIENTNAME: 'mp2-inner'
      MEPHTTPCLIENTGRP: 'clientgrp01'
      CLIENTTYPE: TO_CONNECT_INTERNAL_MES
      TLSFLG: ENABLE
      TLSPARANAME: 'tls-inner'
      CLIENTCOMMPARANAME: 'DefaultClientPara'
      PEERSERVICETAG: MEPSERVICE
    add_mepservercommpara_list:
    - PARANAME: 'DefaultServerPara'
      WAITREQHEADERTIMEOUT: 60
      WAITREQBODYTIMEOUT: 60
      SENDRSPTIMEOUT: 60
      KEEPALIVETIMEOUT: 75
      KEEPALIVEMAXREQNUM: 1000
    add_mephttpservergrp_list:
    - GROUPNAME: 'servergrp01'
    add_mephttpserver_list:
    - SERVERNAME: 'mp2-extNE'
      MEPHTTPSERVERGRP: 'servergrp01'
      SERVERTYPE: FOR_EXTERNAL_NE
      IPV4: '10.1.10.1'
      PORT: 8443
      TLSFLG: ENABLE
      TLSPARANAME: 'tls05-mp2server'
      SERVERCOMMPARANAME: 'DefaultServerPara'
    add_mepreverseproxy_list:
    - PROXYNAME: 'proxy-policyMES2UPF'
      MEPHTTPSERVERGRP: 'servergrp01'
      MEPHTTPCLIENTGRP: 'clientgrp01'
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 上传证书文件。

#### 1.1 登录OM Portal。

#### 1.2 选择“安全 > 证书管理 > 证书与证书集管理”，单击“上传证书”，分别上传CA证书和设备证书文件。

#### 1.3 （可选）如果存在CA证书对应的证书吊销列表（CRL文件），则根据需要上传CRL文件。

#### 选择“安全 > 证书管理 > 上传证书吊销列表”，单击“上传证书吊销列表”，上传CRL文件。

#### CA证书与CRL文件一一对应，如果存在多个CA证书，则需要分别上传其对应的CRL文件。

### 2 关联证书业务场景。

#### 2.1 选择“安全 > 证书管理 > 证书应用场景关联”，在证书场景列表中选择证书场景，单击“关联证书”。

#### 2.2 选择需要与该场景关联的证书，比如设备证书场景则选择对应的设备证书进行关联，CA证书场景则选择对应的CA证书和CRL文件进行关联。

#### Mp2接口证书关联场景名称为“API网关MP2设备证书”与“API网关MP2接口CA证书”。

#### CA证书与CRL文件一一对应。当一个证书场景关联了多个CA证书时，如果需要启用CRL功能，那么还需要一一关联这些CA证书所对应的CRL文件。

### 3 进入“MML命令行-UEG”窗口。

### 4 关闭鉴权开关。

```jinja2
{%- for item in set_apiauth_list -%}
    SET APIAUTH:
    {#- --- 必选参数 --- -#}
    ISAUTH={{item.ISAUTH}},
    ;
{%- endfor -%}
```

### 5 配置Mp2逻辑接口所属的VPN实例。

```jinja2
{%- for item in add_vpninst_list -%}
    ADD VPNINST:
    {#- --- 必选参数 --- -#}
    VPNINSTANCE="{{item.VPNINSTANCE}}",
    ;
{%- endfor -%}
```

### 逻辑接口的VPN一定要与其对应的外联口的VPN相同，否则从逻辑接口发出去的报文会查询路由失败。

### 6 配置Mp2逻辑接口。

```jinja2
{%- for item in add_mpflogicinf_list -%}
    ADD MPFLOGICINF:
    {#- --- 必选参数 --- -#}
    NAME="{{item.NAME}}",
    IPVERSION={{item.IPVERSION}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPV4/IPVER_ALL 时必选 --- -#}
    {%- if item.IPVERSION in ['IPV4', 'IPVER_ALL'] -%}
        IPV4ADDRESS="{{item.IPV4ADDRESS}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPVERSION=IPV4/IPV6/IPVER_ALL 时可选 --- -#}
    {%- if item.IPVERSION in ['IPV4', 'IPV6', 'IPVER_ALL'] -%}
        {%- if item.VPNINSTANCE is not none -%}
            VPNINSTANCE="{{item.VPNINSTANCE}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### **ADD MPFLOGICINF**命令中“NAME”仅支持配置为“capif1/0/0” 。

### Mp2接口的默认端口号为8443。

### 7 配置Mp2反向代理功能。

#### 7.1 打开本特性的License配置开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

#### 7.2 配置UPF APIGW与内部服务之间采用的TLS参数。

```jinja2
{%- for item in add_meptlspara_list -%}
    ADD MEPTLSPARA:
    {#- --- 必选参数 --- -#}
    TLSPARANAME="{{item.TLSPARANAME}}",
    PROTOCOL={{item.PROTOCOL}},
    VERIFYPEER={{item.VERIFYPEER}},
    DEVCERTSCENE={{item.DEVCERTSCENE}},
    CIPHERSUITES={{item.CIPHERSUITES}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：VERIFYPEER=ENABLE 时必选 --- -#}
    {%- if item.VERIFYPEER == 'ENABLE' -%}
        VERIFYDEPTH={{item.VERIFYDEPTH}},
    {%- endif -%}
    {#- --- 条件必选：VERIFYPEER=ENABLE 时必选 --- -#}
    {%- if item.VERIFYPEER == 'ENABLE' -%}
        CACERTSCENE={{item.CACERTSCENE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 7.3 配置UPF APIGW与MPF之间采用的TLS参数。

```jinja2
{%- for item in add_meptlspara_list_1 -%}
    ADD MEPTLSPARA:
    {#- --- 必选参数 --- -#}
    TLSPARANAME="{{item.TLSPARANAME}}",
    PROTOCOL={{item.PROTOCOL}},
    VERIFYPEER={{item.VERIFYPEER}},
    DEVCERTSCENE={{item.DEVCERTSCENE}},
    CIPHERSUITES={{item.CIPHERSUITES}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：VERIFYPEER=ENABLE 时必选 --- -#}
    {%- if item.VERIFYPEER == 'ENABLE' -%}
        VERIFYDEPTH={{item.VERIFYDEPTH}},
    {%- endif -%}
    {#- --- 条件必选：VERIFYPEER=ENABLE 时必选 --- -#}
    {%- if item.VERIFYPEER == 'ENABLE' -%}
        CACERTSCENE={{item.CACERTSCENE}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 7.4 配置UPF APIGW作为客户端时，APIGW与服务端的通信参数。推荐采用通信参数默认值。

```jinja2
{%- for item in add_mepclientcommpara_list -%}
    ADD MEPCLIENTCOMMPARA:
    {#- --- 必选参数 --- -#}
    PARANAME="{{item.PARANAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.CONNTIMEOUT is not none -%}
        CONNTIMEOUT={{item.CONNTIMEOUT}},
    {%- endif -%}
    {%- if item.SENDREQTIMEOUT is not none -%}
        SENDREQTIMEOUT={{item.SENDREQTIMEOUT}},
    {%- endif -%}
    {%- if item.WAITRSPTIMEOUT is not none -%}
        WAITRSPTIMEOUT={{item.WAITRSPTIMEOUT}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 7.5 配置UPF APIGW客户端。

```jinja2
{%- for item in add_mephttpclientgrp_list -%}
    ADD MEPHTTPCLIENTGRP:
    {#- --- 必选参数 --- -#}
    GROUPNAME="{{item.GROUPNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_mephttpclient_list -%}
    ADD MEPHTTPCLIENT:
    {#- --- 必选参数 --- -#}
    CLIENTNAME="{{item.CLIENTNAME}}",
    MEPHTTPCLIENTGRP="{{item.MEPHTTPCLIENTGRP}}",
    CLIENTTYPE={{item.CLIENTTYPE}},
    TLSFLG={{item.TLSFLG}},
    {#- --- 可选参数 --- -#}
    {%- if item.CLIENTCOMMPARANAME is not none -%}
        CLIENTCOMMPARANAME="{{item.CLIENTCOMMPARANAME}}",
    {%- endif -%}
    {%- if item.PEERSERVICETAG is not none -%}
        PEERSERVICETAG={{item.PEERSERVICETAG}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：TLSFLG=ENABLE 时必选 --- -#}
    {%- if item.TLSFLG == 'ENABLE' -%}
        TLSPARANAME="{{item.TLSPARANAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 7.6 配置UPF APIGW作为服务端时，APIGW与客户端的通信参数。推荐采用通信参数默认值。

```jinja2
{%- for item in add_mepservercommpara_list -%}
    ADD MEPSERVERCOMMPARA:
    {#- --- 必选参数 --- -#}
    PARANAME="{{item.PARANAME}}",
    {#- --- 可选参数 --- -#}
    {%- if item.WAITREQHEADERTIMEOUT is not none -%}
        WAITREQHEADERTIMEOUT={{item.WAITREQHEADERTIMEOUT}},
    {%- endif -%}
    {%- if item.WAITREQBODYTIMEOUT is not none -%}
        WAITREQBODYTIMEOUT={{item.WAITREQBODYTIMEOUT}},
    {%- endif -%}
    {%- if item.SENDRSPTIMEOUT is not none -%}
        SENDRSPTIMEOUT={{item.SENDRSPTIMEOUT}},
    {%- endif -%}
    {%- if item.KEEPALIVETIMEOUT is not none -%}
        KEEPALIVETIMEOUT={{item.KEEPALIVETIMEOUT}},
    {%- endif -%}
    {%- if item.KEEPALIVEMAXREQNUM is not none -%}
        KEEPALIVEMAXREQNUM={{item.KEEPALIVEMAXREQNUM}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 7.7 配置UPF APIGW服务端，其中服务端IP地址为Mp2接口IP地址。

```jinja2
{%- for item in add_mephttpservergrp_list -%}
    ADD MEPHTTPSERVERGRP:
    {#- --- 必选参数 --- -#}
    GROUPNAME="{{item.GROUPNAME}}",
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_mephttpserver_list -%}
    ADD MEPHTTPSERVER:
    {#- --- 必选参数 --- -#}
    SERVERNAME="{{item.SERVERNAME}}",
    MEPHTTPSERVERGRP="{{item.MEPHTTPSERVERGRP}}",
    SERVERTYPE={{item.SERVERTYPE}},
    TLSFLG={{item.TLSFLG}},
    {#- --- 可选参数 --- -#}
    {%- if item.IPV4 is not none -%}
        IPV4="{{item.IPV4}}",
    {%- endif -%}
    {%- if item.PORT is not none -%}
        PORT={{item.PORT}},
    {%- endif -%}
    {%- if item.SERVERCOMMPARANAME is not none -%}
        SERVERCOMMPARANAME="{{item.SERVERCOMMPARANAME}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：TLSFLG=ENABLE 时必选 --- -#}
    {%- if item.TLSFLG == 'ENABLE' -%}
        TLSPARANAME="{{item.TLSPARANAME}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 7.8 配置反向代理，通过UPF的APIGW完成MPF与UPF内部服务交互。

```jinja2
{%- for item in add_mepreverseproxy_list -%}
    ADD MEPREVERSEPROXY:
    {#- --- 必选参数 --- -#}
    PROXYNAME="{{item.PROXYNAME}}",
    MEPHTTPSERVERGRP="{{item.MEPHTTPSERVERGRP}}",
    MEPHTTPCLIENTGRP="{{item.MEPHTTPCLIENTGRP}}",
    ;
{%- endfor -%}
```

