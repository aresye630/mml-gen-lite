---
id: ''
name: 激活SBI IMR信令上报
ne_type: UNC
type: feature
description: 本操作指导介绍在运行网络中激活SBI IMR信令上报过程。  SBI IMR信令上报是指网元支持将SBI接口解密后的原始信令使用IMR（initial message record）机制发送给单据服务器（如CloudUDN），单据服务器将原始信令通过xDR流北向接口发送给服务探针/SEQ系统/第三方服务器等。  * 当已实例化的UNC不带vProbe服务时，需要上线vProbe，具体流程参见《UNC软件安装》手册 > 安装vProbe服务。 * 完成UNC上IP路由数据的配置，具体流程参见《UNC初始配置与调测》手册>配置VNF侧IP路由数据。 * 安装SBI信令软采扩展包，具体流程参见《支持SBI信令软采扩展包安装指导书》手册 > 安装SBI信令软采扩展包。 * (可选)安装部署IPSec，建议部署IPSec保证传输通道安全、数据安全。 * 配置vProbe与单据服务器对接数据。  **图1** 操作过程
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","软探针数据采集功能","WSFD-220002 SBI IMR信令上报","激活SBI IMR信令上报"]
refs: []
metadata:
  DepOnLiveCfg: true
allowed-tools:
- getParameterValue('DSP VPROBELNKSTAT')
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导介绍在运行网络中激活SBI IMR信令上报过程。SBI IMR信令上报是指网元支持将SBI接口解密后的原始信令使用IMR（initial message record）机制发送给单据服务器（如CloudUDN），单据服务器将原始信令通过xDR流北向接口发送给服务探针/SEQ系统/第三方服务器等。* 当已实例化的UNC不带vProbe服务时，需要上线vProbe，具体流程参见《UNC软件安装》手册 > 安装vProbe服务。* 完成UNC上IP路由数据的配置，具体流程参见《UNC初始配置与调测》手册>配置VNF侧IP路由数据。* 安装SBI信令软采扩展包，具体流程参见《支持SBI信令软采扩展包安装指导书》手册 > 安装SBI信令软采扩展包。* (可选)安装部署IPSec，建议部署IPSec保证传输通道安全、数据安全。* 配置vProbe与单据服务器对接数据。**图1** 操作过程

## 必备事项
前提条件

前提条件

请仔细阅读WSFD-220002 SBI IMR信令上报特性概述。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_vprobeip_list:
      type: items
      properties:
        INDEX:
          name: '索引号'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: true
          description: '配置vProbe报表本地IP资源池、vProbe报表使用的协议类型、vProbe报表地址的端口号等信息。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        PROTOCOLTYPE:
          name: '协议类型'
          type: string
          enum:
          - TCP
          - SFTP
          - UDP
          required: true
          description: ''
          data_source: ''
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
          data_source: ''
          pattern: ''
          default: ''
        IPV4:
          name: 'IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PORTSTART:
          name: '起始端口号'
          type: integer
          minimum: 1025
          maximum: 65534
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PORTEND:
          name: '结束端口号'
          type: integer
          minimum: 1025
          maximum: 65534
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        VPNNAME:
          name: 'VPN名称'
          type: string
          minLength: 0
          maxLength: 31
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: '_public_'
        IPV6:
          name: 'IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_vprobesvrip_list:
      type: items
      properties:
        PROTOCOLTYPE:
          name: '协议类型'
          type: string
          enum:
          - TCP
          - SFTP
          - UDP
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ACCESSNAME:
          name: '接入点名称'
          type: string
          minLength: 0
          maxLength: 32
          required: true
          description: '配置vProbe报表服务器（单据服务器）的接入点IP地址、服务器类型、协议类型等信息。 说明：  单据服务器地址和vProbe报表本地IP资源池不能在同一网段。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        VPROBESVRNAME:
          name: '报表服务器名称'
          type: string
          minLength: 0
          maxLength: 32
          required: true
          description: ''
          data_source: ''
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
          data_source: ''
          pattern: ''
          default: ''
        IPV4:
          name: '报表服务器IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SVRPORT:
          name: '报表服务器端口号'
          type: integer
          minimum: 0
          maximum: 65534
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SVRPATH:
          name: '报表服务器上传路径'
          type: string
          minLength: 0
          maxLength: 512
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6:
          name: '报表服务器IPv6地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        AUTHMODE:
          name: '报表服务器认证方式'
          type: string
          enum:
          - NOAUTH
          - PUBLICKEY
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        PWD:
          name: '报表服务器密码'
          type: string
          minLength: 1
          maxLength: 432
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        USER:
          name: '报表服务器用户名'
          type: string
          minLength: 0
          maxLength: 64
          required: false
          description: ''
          data_source: ''
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
  examples:
    add_vprobeip_list:
    - INDEX: 1
      PROTOCOLTYPE: TCP
      IPTYPE: IPv4
      IPV4: '10.185.23.253'
      PORTSTART: 6000
      PORTEND: 6031
      VPNNAME: 'public1'
      IPV6: ''
    add_vprobesvrip_list:
    - PROTOCOLTYPE: TCP
      ACCESSNAME: 'ACCESS1'
      VPROBESVRNAME: 'VPROBESVR1'
      IPTYPE: IPv4
      IPV4: '10.180.211.254'
      SVRPORT: 10500
      SVRPATH: '/opt/imr'
      IPV6: ''
      AUTHMODE: ''
      PWD: ''
      USER: ''
    set_licenseswitch_list:
    - LICITEM: 'LKV2IMRSDRSM01'
      SWITCH: ENABLE
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 准备阶段：动态上线vProbe，以及配置UNC和单据服务器IP路由数据。

#### 1.1 **非SDN组网**：

##### 1.1.1 动态上线vProbe，具体流程参见《UNC软件安装》手册>基于VNF LCM安装UNC（非SDN）>动态上线VPROBE服务（非SDN）或《UNC软件安装》手册>基于NFVO安装UNC（非SDN）>动态上线VPROBE服务（非SDN）。

##### 1.1.2 完成UNC上IP路由数据的配置，具体流程参见《UNC初始配置与调测》手册>配置VNF侧IP路由数据（非SDN）。

#### 1.2 **SDN组网**：

##### 1.2.1 动态上线vProbe，具体流程参见《UNC软件安装》手册>基于NFVO安装UNC(SDN组网)>动态上线VPROBE服务（SDN）。

##### 1.2.2 完成UNC上IP路由数据的配置，具体流程参见《UNC初始配置与调测》手册>配置VNF侧IP路由数据(SDN)。

### 2 安装SBI信令软采扩展包。

### 流程参见《支持SBI信令软采扩展包安装指导书》手册>安装SBI信令软采扩展包。

### 3 (可选)安装部署IPSec。

#### 3.1 安装IPSec服务，具体流程参见《UNC软件安装》手册 > 安装可选服务 > 安装IPSec服务。

#### 3.2 配置IPSec，具体参见《UNC安全配置》手册 > 可选配置 > 网络安全配置 > 配置IPSec。

### 4 配置vProbe和单据服务器对接数据。

#### 4.1 进入“MML命令行-UNC”窗口

#### 4.2 配置vProbe报表本地IP资源池。

```jinja2
{%- for item in add_vprobeip_list -%}
    ADD VPROBEIP:
    {#- --- 必选参数 --- -#}
    INDEX={{item.INDEX}},
    PROTOCOLTYPE={{item.PROTOCOLTYPE}},
    IPTYPE={{item.IPTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.VPNNAME is not none -%}
        VPNNAME="{{item.VPNNAME}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPTYPE=IPv4 时必选 --- -#}
    {%- if item.IPTYPE == 'IPv4' -%}
        IPV4="{{item.IPV4}}",
    {%- endif -%}
    {#- --- 条件必选：PROTOCOLTYPE=TCP/SFTP/UDP 时必选 --- -#}
    {%- if item.PROTOCOLTYPE in ['TCP', 'SFTP', 'UDP'] -%}
        PORTSTART={{item.PORTSTART}},
    {%- endif -%}
    {#- --- 条件必选：PROTOCOLTYPE=TCP/SFTP/UDP 时必选 --- -#}
    {%- if item.PROTOCOLTYPE in ['TCP', 'SFTP', 'UDP'] -%}
        PORTEND={{item.PORTEND}},
    {%- endif -%}
    {#- --- 条件必选：IPTYPE=IPv6 时必选 --- -#}
    {%- if item.IPTYPE == 'IPv6' -%}
        IPV6="{{item.IPV6}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 4.3 配置vProbe报表服务器接入点IP地址等信息。

```jinja2
{%- for item in add_vprobesvrip_list -%}
    ADD VPROBESVRIP:
    {#- --- 必选参数 --- -#}
    PROTOCOLTYPE={{item.PROTOCOLTYPE}},
    ACCESSNAME="{{item.ACCESSNAME}}",
    VPROBESVRNAME="{{item.VPROBESVRNAME}}",
    IPTYPE={{item.IPTYPE}},
    SVRPORT={{item.SVRPORT}},
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPTYPE=IPv4 时必选 --- -#}
    {%- if item.IPTYPE == 'IPv4' -%}
        IPV4="{{item.IPV4}}",
    {%- endif -%}
    {#- --- 条件必选：PROTOCOLTYPE=SFTP 时必选 --- -#}
    {%- if item.PROTOCOLTYPE == 'SFTP' -%}
        AUTHMODE={{item.AUTHMODE}},
    {%- endif -%}
    {#- --- 条件必选：IPTYPE=IPv6 时必选 --- -#}
    {%- if item.IPTYPE == 'IPv6' -%}
        IPV6="{{item.IPV6}}",
    {%- endif -%}
    {#- --- 条件必选：PROTOCOLTYPE=SFTP 时必选 --- -#}
    {%- if item.PROTOCOLTYPE == 'SFTP' -%}
        PWD="{{item.PWD}}",
    {%- endif -%}
    {#- --- 条件必选：PROTOCOLTYPE=SFTP 时必选 --- -#}
    {%- if item.PROTOCOLTYPE == 'SFTP' -%}
        SVRPATH="{{item.SVRPATH}}",
    {%- endif -%}
    {#- --- 条件必选：PROTOCOLTYPE=SFTP 时必选 --- -#}
    {%- if item.PROTOCOLTYPE == 'SFTP' -%}
        USER="{{item.USER}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 4.4 查询vProbe与报表服务器之间的链路状态。

#### 4.5 vProbe部署完成，且链路正常后，打开本特性的License配置开关。

```jinja2
{%- set DSP_VPROBELNKSTAT=getParameterValue('DSP VPROBELNKSTAT') -%}
{%- if DSP_VPROBELNKSTAT=='正常' -%}
    {%- for item in set_licenseswitch_list -%}
        SET LICENSESWITCH:
        {#- --- 必选参数 --- -#}
        LICITEM="{{item.LICITEM}}",
        SWITCH={{item.SWITCH}},
        ;
    {%- endfor -%}
{%- endif -%}
```

