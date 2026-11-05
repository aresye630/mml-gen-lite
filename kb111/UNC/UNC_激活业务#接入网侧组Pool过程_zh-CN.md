---
id: ''
name: 接入网侧组Pool过程
ne_type: UNC
type: feature
description: 本配置指导描述新建MME Pool时接入网侧组Pool的配置过程。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","容灾功能","MME容灾方案","新建部署","全网新建Pool","激活业务","接入网侧组Pool过程"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本配置指导描述新建MME Pool时接入网侧组Pool的配置过程。

## 必备事项
前提条件

* 数据规划已完成。
* 网元基础数据配置完成。
* Pool功能预设置完成。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_talst_list:
      type: items
      properties:
        TALISTID:
          name: 'TA List 标号'
          type: integer
          minimum: 0
          maximum: 65534
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        TAI:
          name: 'TAI'
          type: string
          maxLength: 10
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
    add_dnsn_list:
      type: items
      properties:
        FQDN:
          name: 'FQDN'
          type: string
          maxLength: 255
          required: true
          description: ''
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
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        S5PROTOCOL:
          name: 'S5接口协议类型'
          type: string
          enum:
          - GTP
          - GTP_PMIP
          - PMIP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: GTP
        S8PROTOCOL:
          name: 'S8接口协议类型'
          type: string
          enum:
          - GTP
          - GTP_PMIP
          - PMIP
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: GTP
    add_resrec_list:
      type: items
      properties:
        TYPE:
          name: 'TYPE'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NAME:
          name: 'NAME'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        DOMAIN:
          name: 'DOMAIN'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IP:
          name: 'IP'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
  examples:
    add_talst_list:
    - TALISTID: 0
      TAI: '123033101'
    add_ipv4dnsh_list:
    - HSINDEX: 20
      HOSTNAME: 'TOPON.SGW.SGW1.NODES.EPC.ENVID50.MNC03.MCC123.3GPPNETWORK.ORG'
      ADDRSECTION: SECTION1
      IPV4ADDR1: '10.168.163.1'
    add_dnsn_list:
    - FQDN: 'TAC-LB04.TAC-HB31.TAC.EPC.MNC003.MCC123.3GPPNETWORK.ORG'
      HSINDEX: 20
      ENTITY: SGW
      INTYPE: S11
      S5PROTOCOL: GTP
      S8PROTOCOL: GTP
    add_resrec_list:
    - TYPE: A
      NAME: MNC0000.MCC0123.gprs
      DOMAIN: TAC-LB04.TAC-HB31.TAC.EPC
      IP: 10.168.155.2
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 按照之前准备的脚本，配置新增连接的eNodeB1与MME1之间的链路数据，调通S1链路。

### 2 配置MME1数据。

### 将一个eNodeB1加入到MME1。具体操作过程参考《UNC初始配置与调测》中“到MME的数据配置”。

### 3 配置eNodeB1到MME1的相关信令和链路数据。

#### 3.1 在eNodeB1上检查MME1的MMEID和权重是否正确。

#### 3.2 在MME1上配置eNodeB1相关的TALIST。

```jinja2
{%- for item in add_talst_list -%}
    ADD TALST:
    {#- --- 必选参数 --- -#}
    TALISTID={{item.TALISTID}},
    TAI="{{item.TAI}}",
    ;
{%- endfor -%}
```

#### 3.3 在MME1上检查4G的PAGING表是否上报。

#### 4G的PAGING表是自动上报的，链路配置完成之后，使用命令检查LST S1PAGING，查询TA上报是否符合规划。

### 4 配置eNodeB1到其他MME（MME2，MME3）的相关信令和链路数据。

### 5 **可选：**如果TA（eNodeB1）对应的S-GW的域名解析使用DNS Server配置，可以跳过此步。如果TA对应S-GW的域名解析使用的是MME（MME1，MME2，MME3）上的hostfile，需要在MME（MME1，MME2，MME3）对应S-GW的域名解析。

#### 5.1 增加IPV4DNSH解析。

```jinja2
{%- if is_optional_sgw_domain_resolution -%}
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
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 5.2 增加DNSN解析。

```jinja2
{%- if is_optional_sgw_domain_resolution -%}
    {%- for item in add_dnsn_list -%}
        ADD DNSN:
        {#- --- 必选参数 --- -#}
        FQDN="{{item.FQDN}}",
        HSINDEX={{item.HSINDEX}},
        ENTITY={{item.ENTITY}},
        INTYPE={{item.INTYPE}},
        {#- --- 条件可选参数 --- -#}
        {#- --- 条件可选：ENTITY=SGW/PGW 时可选 --- -#}
        {%- if item.ENTITY in ['SGW', 'PGW'] -%}
            {%- if item.S5PROTOCOL is not none -%}
                S5PROTOCOL={{item.S5PROTOCOL}},
            {%- endif -%}
        {%- endif -%}
        {#- --- 条件可选：ENTITY=SGW/PGW 时可选 --- -#}
        {%- if item.ENTITY in ['SGW', 'PGW'] -%}
            {%- if item.S8PROTOCOL is not none -%}
                S8PROTOCOL={{item.S8PROTOCOL}},
            {%- endif -%}
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

### 6 配置Pool内TA区对应Pool内MME的域名解析。

### 为了保证从Pool外MME到Pool内MME的切换分摊均匀，需要在DNS Server或Hostfile上针对所有Pool内TA区增加Pool内MME（MME1，MME2，MME3）的IP。

### 配置MME的域名解析有两种方式：

#### 6.1 方式一：DNS配置方式。

#### 6.2 方式二：Hostfile配置方式。

### 对于Hostfile配置方式，需要在Pool区外周边TA区对应的MME上配置。

### 本例中，对于域名“TAC-LB04.TAC-HB31.TAC.EPC.MNC003.MCC123.3GPPNETWORK.ORG”，将在DNS上将eNodeB1的路由区域名解析成为扩展MME1、MME2和MME3的GTPC地址。并通知与该eNodeB1覆盖范围相邻的非本MME Pool的其他MME做相应的数据修改。

### 通常地，本网内有一个本地DNS Server，上一级DNS Server不在本地。这种情况下，当核心网内多个MME改造成Pool后，该DNS Server可以视作Pool外的DNS Server，也可以视作Pool内的DNS Server，它除了保留原有的域名解析数据、解析功能外，还需要为MME Pool增加TA对应的IP地址配置。

### 以华为为例：

#### 6.3 方式一：在华为DNS Server的LMT上配置，主备均需要：

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_resrec_list的变量区（command: ADD RESREC） -#}
<!-- MISSING_MACRO: command=ADD RESREC list_name=add_resrec_list step_id=6.3 -->
```

#### 6.4 方式二：在不带LMT的DNS Server上，在named.ra文件中增加A记录（详细参见《DNS产品文档》）：

#### TAC-LB04.TAC-HB31.TAC.EPC IN A 10.166.155.2

#### TAC-LB04.TAC-HB31.TAC.EPC IN A 10.166.155.2

#### 6.5 如果本网的运营商除了本地DNS Server外，还有上一级的DNS Server也在本地，在改造成MME Pool后，Pool内有一个DNS Server A，Pool外还有一个上级的DNS Server B，则，TA对应IP地址的数据配置就需要在DNS Server B上完成。这种情况比较少见。

#### 6.6 如果修改了DNS Server的数据，需要清除各MME的cash数据。

### 7 重复步骤 1~步骤 6，完成其他eNodeB（eNodeB2，eNodeB3）的配置。

