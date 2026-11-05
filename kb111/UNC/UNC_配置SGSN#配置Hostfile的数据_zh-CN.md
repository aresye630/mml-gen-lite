---
id: ''
name: 配置Hostfile的数据
ne_type: UNC
type: feature
description: 当运营商在部署分组交换网，新增SGSN时，可通过配置Hostfile数据，用于SGSN在以下流程中进行域名解析：  * 在PDP激活时根据APN解析GGSN IP地址。 * Inter RAU时根据RAI解析对端SGSN IP地址。 * Relocation时根据目的RNC ID解析对端SGSN IP地址。 * SGSN Pool寻址时通过Default SGSN或者NRI+RAI解析SGSN IP地址。  进行域名解析可以使用三种手段：使用DNS服务器、通过Cache查询或使用本地主机信息表（Hostfile），通常主要使用DNS服务器进行域名解析，Hostfile作为辅助手段。其中：  * DNS服务器是网络中专门提供域名解析服务的服务器。 * DNS Cache是DNS服务器解析到的域名和IP地址在UNC的缓存，用于快速解析域名，以减少访问DNS服务器的次数，其记录具有一定的生命周期，生命周期结束后，该记录失效。生命周期由DNS响应消息中的TTL携带。 * 本地主机信息表Hostfile则保存在本地SGSN中，包含的记录比较少。  SGSN进行域名解析时默认按照以下顺序进行：首先查找HOSTFILE中的主机信息记录；如果没有相应的记录，则查找DNS Cache中的记录。如果没有相应的记录，向DNS服务器发送解析请求进行解析。
risk_level: ''
doc_source: ["网络部署","初始配置","UNC初始配置与调测","组网对接配置","配置AMF&MME&SGSN","配置SGSN","配置Hostfile的数据"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
当运营商在部署分组交换网，新增SGSN时，可通过配置Hostfile数据，用于SGSN在以下流程中进行域名解析：* 在PDP激活时根据APN解析GGSN IP地址。* Inter RAU时根据RAI解析对端SGSN IP地址。* Relocation时根据目的RNC ID解析对端SGSN IP地址。* SGSN Pool寻址时通过Default SGSN或者NRI+RAI解析SGSN IP地址。进行域名解析可以使用三种手段：使用DNS服务器、通过Cache查询或使用本地主机信息表（Hostfile），通常主要使用DNS服务器进行域名解析，Hostfile作为辅助手段。其中：* DNS服务器是网络中专门提供域名解析服务的服务器。* DNS Cache是DNS服务器解析到的域名和IP地址在UNC的缓存，用于快速解析域名，以减少访问DNS服务器的次数，其记录具有一定的生命周期，生命周期结束后，该记录失效。生命周期由DNS响应消息中的TTL携带。* 本地主机信息表Hostfile则保存在本地SGSN中，包含的记录比较少。SGSN进行域名解析时默认按照以下顺序进行：首先查找HOSTFILE中的主机信息记录；如果没有相应的记录，则查找DNS Cache中的记录。如果没有相应的记录，向DNS服务器发送解析请求进行解析。

## 必备事项
前提条件

* 具备管理员权限的操作人员已经登录华为操作维护系统（登录U2020客户端或登录OM Portal）。

* UNC软件安装已完成。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_ipv4dnsh_list:
      type: items
      properties:
        HSINDEX:
          name: '主机名索引'
          type: integer
          minimum: 1
          maximum: 1024
          required: true
          description: '配置Hostfile解析记录。'
          data_source: '参见“水平网设LLD文档 ”。'
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
    add_ipv4dnsh_list_2:
      type: items
      properties:
        HSINDEX:
          name: '主机名索引'
          type: integer
          minimum: 1
          maximum: 1024
          required: true
          description: '配置Hostfile解析记录。'
          data_source: '参见“水平网设LLD文档 ”。'
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
    add_ipv4dnsh_list_3:
      type: items
      properties:
        HSINDEX:
          name: '主机名索引'
          type: integer
          minimum: 1
          maximum: 1024
          required: true
          description: ''
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
  examples:
    add_ipv4dnsh_list:
    - HSINDEX: 1
      HOSTNAME: 'CMNET.MNC000.MCC460.GPRS'
      ADDRSECTION: SECTION1
      IPV4ADDR1: '192.168.31.2'
      IPV4ADDR2: '192.168.32.5'
    add_ipv4dnsh_list_2:
    - HSINDEX: 1
      HOSTNAME: 'CMNET.MNC000.MCC460.GPRS'
      ADDRSECTION: SECTION1
      IPV4ADDR1: '192.168.31.2'
    add_ipv4dnsh_list_3:
    - HSINDEX: 4
      HOSTNAME: 'RNC0450.MNC0000.MCC0460.GPRS'
      ADDRSECTION: SECTION1
      IPV4ADDR1: '172.25.6.53'
      IPV4ADDR2: '172.25.6.54'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 进入“MML命令行-UNC”窗口。

### 2 **可选：**配置PDP激活上下文时GGSN的DNS记录。

```jinja2
{%- if is_optional_pdp_ggsn_dns_record -%}
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

### 3 **可选：**配置RAU时SGSN的DNS记录。

```jinja2
{%- if is_optional_rau_sgsn_dns_record -%}
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
        ;
    {%- endfor -%}
{%- endif -%}
```

### 4 **可选：**配置RELOCATION时GGSN的DNS记录。

```jinja2
{%- if is_optional_relocation_ggsn_dns_record -%}
    {%- for item in add_ipv4dnsh_list_3 -%}
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

