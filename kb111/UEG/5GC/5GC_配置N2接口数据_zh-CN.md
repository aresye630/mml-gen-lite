---
id: ''
name: 配置N2接口数据
ne_type: UEG
type: feature
description: '**接口介绍**  N2接口是5G系统中(R)AN和AMF之间的控制面接口，N2接口的信令连接功能为无线网络信令提供可靠的传输。  N2接口协议栈如图1所示。  **图1** N2接口协议栈图  * NG-AP（NG Application Protocol）：gNodeB与AMF之间的应用层协议。 * SCTP（Stream Control Transmission Protocol）：此协议用于保证gNodeB与AMF之间的信令消息传送。 * N2接口支持IPSec（Internet Protocol Security）和DTLS（Datagram Transport Layer Security），以保证数据传输的安全。 * N2接口支持SCTP数据绑定，把多个接口消息组合在一个SCTP包中发给gNodeB，减少寻呼消息数。  **配置建议**  AMF的N2接口业务IP地址不能和AMF其他接口业务IP地址共用（除S1接口）。  以下配置数据以及步骤均以UEG双DC组网场景的配置规划为例进行介绍。'
tags: []
risk_level: ''
doc_source:
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网煤矿场景，入驻式）","软件安装与开站","UEG软件安装与开站","UEG初始配置","参考：详细配置指导","配置AMF","配置N2接口数据"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网核电场景，入驻式）","软件安装与开站","UEG软件安装与开站","UEG初始配置","参考：详细配置指导","配置AMF","配置N2接口数据"]
  - ["专网（仅连接，园区入驻式）","网络部署","5GC toB 部署边缘站点（一号通专网通用场景，入驻式）","软件安装与开站","UEG软件安装与开站","UEG初始配置","参考：详细配置指导","配置AMF","配置N2接口数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block= annotations -->
```text
## 操作场景
**接口介绍**N2接口是5G系统中(R)AN和AMF之间的控制面接口，N2接口的信令连接功能为无线网络信令提供可靠的传输。N2接口协议栈如图1所示。**图1** N2接口协议栈图* NG-AP（NG Application Protocol）：gNodeB与AMF之间的应用层协议。* SCTP（Stream Control Transmission Protocol）：此协议用于保证gNodeB与AMF之间的信令消息传送。* N2接口支持IPSec（Internet Protocol Security）和DTLS（Datagram Transport Layer Security），以保证数据传输的安全。* N2接口支持SCTP数据绑定，把多个接口消息组合在一个SCTP包中发给gNodeB，减少寻呼消息数。**配置建议**AMF的N2接口业务IP地址不能和AMF其他接口业务IP地址共用（除S1接口）。以下配置数据以及步骤均以UEG双DC组网场景的配置规划为例进行介绍。

## 必备事项
前提条件

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
          description: '配置N2接口的业务IP地址。'
          data_source: '参见“水平网设LLD文档 -> 5G Core业务IP对接设计”。'
          pattern: ''
          default: IPv4
        SERVICEIPV4:
          name: '业务IPv4地址'
          type: string
          maxLength: 15
          required: false
          description: '当AMF与SMF共部署时，N2接口与N4接口的业务IP地址不能相同。  **ADD SERVICEIP**与**ADD SCTPLE**命令中配置的IP地址需保持一致，且不能与HTTP客户端/服务端的地址相同。  由于N2接口传输层的SCTP协议支持多连接，且同一连接也存在多路径，可以配置多个业务IP地址支持多条链路，此处以两个业务IP地址为例。  说明：  对于热备场景，DC1和DC2的“业务IPv4地址”需保持一致。'
          data_source: ''
          pattern: ''
          default: ''
        VPNINSTNAME:
          name: 'VPN实例名称'
          type: string
          maxLength: 31
          required: false
          description: 'UEG风筝形态对外接口组网时，需运营商统一规划IP，VPN。'
          data_source: ''
          pattern: ''
          default: ''
    add_cpsctppara_list:
      type: items
      properties:
        SCTPPARAINDEX:
          name: 'SCTP协议参数索引'
          type: integer
          minimum: 0
          maximum: 65534
          required: true
          description: '配置SCTP协议参数及本端实体。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        CHKSUMTX:
          name: '发送消息时是否计算校验和'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: YES
        CHKSUMRX:
          name: '接收消息时是否计算校验和'
          type: string
          enum:
          - NO
          - YES
          required: false
          description: ''
          data_source: '本端规划'
          pattern: ''
          default: YES
    add_sctplegrp_list:
      type: items
      properties:
        SCTPGROUPID:
          name: 'SCTP本地实体组标识'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: '配置SCTP本端实体组。'
          data_source: '本端规划'
          pattern: ''
          default: ''
    add_sctple_list:
      type: items
      properties:
        SCTPLEIDX:
          name: 'SCTP本端实体索引'
          type: integer
          minimum: 0
          maximum: 1023
          required: true
          description: '配置SCTP协议参数及本端实体。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SCTPGROUPID:
          name: 'SCTP本地实体组标识'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: '与**ADD SCTPLEGRP**中“SCTPGROUPID”的取值保持一致。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        IPVERSION:
          name: 'IP地址版本'
          type: string
          enum:
          - IPV4
          - IPV6
          required: true
          description: '与**ADD SERVICEIP**命令中配置的IP地址需保持一致，且不能与HTTP客户端/服务端的地址相同。'
          data_source: '全网规划'
          pattern: ''
          default: ''
        LOCALIPV41:
          name: '本地IPv4地址1'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: ''
        LOCALIPV42:
          name: '本地IPv4地址2'
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
          minimum: 1024
          maximum: 65535
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: 38412
        SCTPPARAIDX:
          name: 'SCTP协议参数索引'
          type: integer
          minimum: 0
          maximum: 4294967295
          required: false
          description: '与**ADD CPSCTPPARA**中“SCTPPARAINDEX”的取值保持一致。'
          data_source: '全网规划'
          pattern: ''
          default: ''
    add_ngappara_list:
      type: items
      properties:
        NGAPPARAIDX:
          name: 'NGAP协议参数索引'
          type: integer
          minimum: 0
          maximum: 31
          required: true
          description: '配置NGAP协议参数**。**'
          data_source: '本端规划'
          pattern: ''
          default: ''
        AMFCFGUPTTMR:
          name: 'AMF Configuration Update消息超时定时器(s)'
          type: integer
          minimum: 1
          maximum: 65534
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: 20
        AMFCFGUPTCNT:
          name: 'AMF Configuration Update消息重发次数 (times)'
          type: integer
          minimum: 1
          maximum: 3
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: 3
        RESETTMR:
          name: 'Reset超时定时器(s)'
          type: integer
          minimum: 1
          maximum: 65534
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: 20
        RESETCNT:
          name: 'Reset消息重发次数 (times)'
          type: integer
          minimum: 1
          maximum: 3
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: 3
        TIMETOWAITFLG:
          name: '等待时间指示器'
          type: string
          enum:
          - Yes
          - No
          required: false
          description: ''
          data_source: '与对端协商'
          pattern: ''
          default: No
        TIMETOWAITTMR:
          name: '重发NG SETUP REQUEST时长 (s)'
          type: string
          enum:
          - One
          - Two
          - Five
          - Ten
          - Twenty
          - Sixty
          required: false
          description: ''
          data_source: '全网规划'
          pattern: ''
          default: Sixty
    add_ngaple_list:
      type: items
      properties:
        NGAPLEIDX:
          name: 'NGAP本端实体索引'
          type: integer
          minimum: 0
          maximum: 1023
          required: true
          description: '配置NGAP本端实体及本端地址。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        SCTPGROUPID:
          name: 'SCTP本端实体组标识'
          type: integer
          minimum: 0
          maximum: 255
          required: true
          description: '与**ADD SCTPLEGRP**中“SCTPGROUPID”的取值保持一致。'
          data_source: '本端规划'
          pattern: ''
          default: ''
        NGAPPARAIDX:
          name: 'NGAP参数索引'
          type: integer
          minimum: 0
          maximum: 31
          required: false
          description: '与**ADD NGAPPARA**中“NGAPPARAIDX”的取值保持一致。'
          data_source: '本端规划'
          pattern: ''
          default: 0
    set_ngmmfunc_list:
      type: items
      properties:
        NOUECTXOPTSW:
          name: '无用户上下文处理基站消息增强开关'
          type: string
          enum:
          - OFF
          - ON
          required: false
          description: '开启此开关后，AMF对于无相关上下文的用户释放无线连接，将用户转为空闲态，后续用户通过Service Request流程重新注册到AMF上。'
          data_source: '全网规划'
          pattern: ''
          default: ''
  examples:
    add_serviceip_list:
    - IPVERSION: IPv4
      SERVICEIPV4: '172.16.2.3'
      VPNINSTNAME: 'VRF_Access'
    - IPVERSION: IPv4
      SERVICEIPV4: '172.16.2.5'
      VPNINSTNAME: 'VRF_Access'
    add_cpsctppara_list:
    - SCTPPARAINDEX: 0
      CHKSUMTX: YES
      CHKSUMRX: YES
    - SCTPPARAINDEX: 0
      CHKSUMTX: YES
      CHKSUMRX: YES
    add_sctplegrp_list:
    - SCTPGROUPID: 1
    - SCTPGROUPID: 1
    add_sctple_list:
    - SCTPLEIDX: 0
      SCTPGROUPID: 1
      IPVERSION: IPV4
      LOCALIPV41: '172.16.2.3'
      LOCALIPV42: '172.16.2.4'
      PORT: 38412
      SCTPPARAIDX: 0
    - SCTPLEIDX: 0
      SCTPGROUPID: 1
      IPVERSION: IPV4
      LOCALIPV41: '172.16.2.5'
      LOCALIPV42: '172.16.2.6'
      PORT: 38412
      SCTPPARAIDX: 0
    add_ngappara_list:
    - NGAPPARAIDX: 1
      AMFCFGUPTTMR: 20
      AMFCFGUPTCNT: 3
      RESETTMR: 20
      RESETCNT: 3
      TIMETOWAITFLG: Yes
      TIMETOWAITTMR: Sixty
    - NGAPPARAIDX: 1
      AMFCFGUPTTMR: 20
      AMFCFGUPTCNT: 3
      RESETTMR: 20
      RESETCNT: 3
      TIMETOWAITFLG: Yes
      TIMETOWAITTMR: Sixty
    add_ngaple_list:
    - NGAPLEIDX: 1
      SCTPGROUPID: 1
      NGAPPARAIDX: 1
    - NGAPLEIDX: 1
      SCTPGROUPID: 1
      NGAPPARAIDX: 1
    set_ngmmfunc_list:
    - NOUECTXOPTSW: ON
    - NOUECTXOPTSW: ON
```

## 3 命令模板定义
<!-- @mml:block= commands -->

### 1 配置N2接口业务IP地址。

#### 1.1 //DC1

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

### 2 配置SCTP协议参数及SCTP本端实体。

#### 2.1 //DC1

```jinja2
{%- for item in add_cpsctppara_list -%}
    ADD CPSCTPPARA:
    {#- --- 必选参数 --- -#}
    SCTPPARAINDEX={{item.SCTPPARAINDEX}},
    {#- --- 可选参数 --- -#}
    {%- if item.CHKSUMTX is not none -%}
        CHKSUMTX={{item.CHKSUMTX}},
    {%- endif -%}
    {%- if item.CHKSUMRX is not none -%}
        CHKSUMRX={{item.CHKSUMRX}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_sctplegrp_list -%}
    ADD SCTPLEGRP:
    {#- --- 必选参数 --- -#}
    SCTPGROUPID={{item.SCTPGROUPID}},
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_sctple_list -%}
    ADD SCTPLE:
    {#- --- 必选参数 --- -#}
    SCTPLEIDX={{item.SCTPLEIDX}},
    SCTPGROUPID={{item.SCTPGROUPID}},
    IPVERSION={{item.IPVERSION}},
    {#- --- 可选参数 --- -#}
    {%- if item.PORT is not none -%}
        PORT={{item.PORT}},
    {%- endif -%}
    {%- if item.SCTPPARAIDX is not none -%}
        SCTPPARAIDX={{item.SCTPPARAIDX}},
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPVERSION=IPV4 时必选 --- -#}
    {%- if item.IPVERSION == 'IPV4' -%}
        LOCALIPV41="{{item.LOCALIPV41}}",
    {%- endif -%}
    {#- --- 条件可选参数 --- -#}
    {#- --- 条件可选：IPVERSION=IPV4 时可选 --- -#}
    {%- if item.IPVERSION == 'IPV4' -%}
        {%- if item.LOCALIPV42 is not none -%}
            LOCALIPV42="{{item.LOCALIPV42}}",
        {%- endif -%}
    {%- endif -%}
    ;
{%- endfor -%}
```

### 3 配置NGAP本端实体。

#### 3.1 //DC1

```jinja2
{%- for item in add_ngappara_list -%}
    ADD NGAPPARA:
    {#- --- 必选参数 --- -#}
    NGAPPARAIDX={{item.NGAPPARAIDX}},
    {#- --- 可选参数 --- -#}
    {%- if item.AMFCFGUPTTMR is not none -%}
        AMFCFGUPTTMR={{item.AMFCFGUPTTMR}},
    {%- endif -%}
    {%- if item.AMFCFGUPTCNT is not none -%}
        AMFCFGUPTCNT={{item.AMFCFGUPTCNT}},
    {%- endif -%}
    {%- if item.RESETTMR is not none -%}
        RESETTMR={{item.RESETTMR}},
    {%- endif -%}
    {%- if item.RESETCNT is not none -%}
        RESETCNT={{item.RESETCNT}},
    {%- endif -%}
    {%- if item.TIMETOWAITFLG is not none -%}
        TIMETOWAITFLG={{item.TIMETOWAITFLG}},
    {%- endif -%}
    {%- if item.TIMETOWAITTMR is not none -%}
        TIMETOWAITTMR={{item.TIMETOWAITTMR}},
    {%- endif -%}
    ;
{%- endfor -%}
```

```jinja2
{%- for item in add_ngaple_list -%}
    ADD NGAPLE:
    {#- --- 必选参数 --- -#}
    NGAPLEIDX={{item.NGAPLEIDX}},
    SCTPGROUPID={{item.SCTPGROUPID}},
    {#- --- 可选参数 --- -#}
    {%- if item.NGAPPARAIDX is not none -%}
        NGAPPARAIDX={{item.NGAPPARAIDX}},
    {%- endif -%}
    ;
{%- endfor -%}
```

### 4 开启无用户上下文处理基站消息增强开关。

#### 4.1 //DC1

```jinja2
{%- for item in set_ngmmfunc_list -%}
    SET NGMMFUNC:
    {#- --- 可选参数 --- -#}
    {%- if item.NOUECTXOPTSW is not none -%}
        NOUECTXOPTSW={{item.NOUECTXOPTSW}},
    {%- endif -%}
    ;
{%- endfor -%}
```

