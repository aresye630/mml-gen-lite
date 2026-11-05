---
id: ''
name: 扩容业务
ne_type: UNC
type: feature
description: 本操作指导Pool区通过新建MME3来扩容MME侧的配置过程。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","容灾功能","MME容灾方案","扩容部署","新建MME割入Pool","扩容业务"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导Pool区通过新建MME3来扩容MME侧的配置过程。

## 必备事项
前提条件

* 操作人员已经登录华为操作维护系统。
* 已经完成MME Pool用户迁移。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_mmeid_list:
      type: items
      properties:
        MCC:
          name: '移动国家码'
          type: string
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MNC:
          name: '移动网号'
          type: string
          maxLength: 3
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MMEGI:
          name: 'MME组识别码'
          type: string
          maxLength: 4
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MMEC:
          name: 'MME编码（起始值）'
          type: string
          maxLength: 2
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MMECNUM:
          name: 'MME编码数目'
          type: integer
          minimum: 1
          maximum: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 1
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
    set_sys_list:
      type: items
      properties:
        CAP:
          name: '设备能力'
          type: integer
          minimum: 0
          maximum: 255
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_poolla_list:
      type: items
      properties:
        LAC:
          name: '位置区域码'
          type: string
          maxLength: 4
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_poolla_list_3:
      type: items
      properties:
        BGNTAI:
          name: '起始TAI'
          type: string
          maxLength: 10
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENDTAI:
          name: '终止TAI'
          type: string
          maxLength: 10
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LAC:
          name: '位置区域码'
          type: string
          maxLength: 4
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
    add_tailai_list:
      type: items
      properties:
        BGNTAI:
          name: '起始TAI'
          type: string
          maxLength: 10
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        ENDTAI:
          name: '终止TAI'
          type: string
          maxLength: 10
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        LAI:
          name: 'LAI'
          type: string
          maxLength: 10
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
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
    add_mmeid_list:
    - MCC: '123'
      MNC: '03'
      MMEGI: '8001'
      MMEC: '8'
      MMECNUM: 1
    set_licenseswitch_list:
    - LICITEM: 'LKV2MMEMG02'
      SWITCH: ENABLE
    set_sys_list:
    - CAP: 100
    add_poolla_list:
    - LAC: '1011'
    add_poolla_list_3:
    - BGNTAI: '123033101'
      ENDTAI: '123033105'
      LAC: '1011'
    add_ipv4dnsh_list:
    - HSINDEX: 20
      HOSTNAME: 'TOPON.SGW.SGW1.NODES.EPC.ENVID50.MNC03.MCC123.3GPPNETWORK.ORG'
      ADDRSECTION: SECTION1
      IPV4ADDR1: '10.168.163.1'
    add_dnsn_list:
    - FQDN: 'TAC-LBTAC-LB04.TAC-HB31.TAC.EPC.MNC03.MCC123.3GPPNETWORK.ORG'
      HSINDEX: 20
      ENTITY: SGW
      INTYPE: S11
      S5PROTOCOL: GTP
      S8PROTOCOL: GTP
    add_talst_list:
    - TALISTID: 0
      TAI: '123033101'
    add_tailai_list:
    - BGNTAI: '123033101'
      ENDTAI: '123033105'
      LAI: '123031011'
    add_resrec_list:
    - TYPE: A
      NAME: MNC0000.MCC0123.gprs
      DOMAIN: TAC-LB04.TAC-HB31.TAC.EPC
      IP: 10.168.153.1
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 路由准备和配置同步阶段。

#### 1.1 申请并加载License，“MME Pool”(LKV2POOL02)、“Subscriber Migration in MME Pool”（可选，LKV2MMEMG02）。

#### 1.2 链路准备阶段。 准备S1接口的路由配置脚本。

#### 1.3 各MME配置参数同步。

### 2 Pool参数配置阶段。

### 配置新建MME3的Pool参数。

#### 2.1 在MME3上增加MMEID。

```jinja2
{%- for item in add_mmeid_list -%}
    ADD MMEID:
    {#- --- 必选参数 --- -#}
    MCC="{{item.MCC}}",
    MNC="{{item.MNC}}",
    MMEGI="{{item.MMEGI}}",
    MMEC="{{item.MMEC}}",
    {#- --- 可选参数 --- -#}
    {%- if item.MMECNUM is not none -%}
        MMECNUM={{item.MMECNUM}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.2 在MME上打开Pool开关。

```jinja2
{%- for item in set_licenseswitch_list -%}
    SET LICENSESWITCH:
    {#- --- 必选参数 --- -#}
    LICITEM="{{item.LICITEM}}",
    SWITCH={{item.SWITCH}},
    ;
{%- endfor -%}
```

#### 2.3 在MME3上配置本MME3的权重信息。

```jinja2
{%- for item in set_sys_list -%}
    SET SYS:
    {#- --- 可选参数 --- -#}
    {%- if item.CAP is not none -%}
        CAP={{item.CAP}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 2.4 DNS Server上增加MME3的域名解析。

#### 本例中，对于域名“MMEC8.MMEGI8001.MME.EPC.MNC03.MCC123.3GPPNETWORK.ORG”，将在DNS上配置成为MME3的GTPC地址。

#### 2.5 **可选：**在使用UNC作为融合节点同时支持SGSN Pool功能和MME Pool功能的场景下，如果MME3需要通过S1接口下发LTE GUMMEI和Mapped GUMMEI，需要进行如下操作。

##### 2.5.1 没有规划TA和LA对应关系。

```jinja2
{%- if is_optional_lte_gummei_and_mapped_gummei and is_scenario_no_ta_la_mapping -%}
    {%- for item in add_poolla_list -%}
        ADD POOLLA:
        {#- --- 必选参数 --- -#}
        LAC="{{item.LAC}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 2.5.2 规划了TA和LA的对应关系。

```jinja2
{%- if is_optional_lte_gummei_and_mapped_gummei and is_scenario_ta_la_mapping -%}
    {%- for item in add_poolla_list_3 -%}
        ADD POOLLA:
        {#- --- 必选参数 --- -#}
        LAC="{{item.LAC}}",
        {#- --- 可选参数 --- -#}
        {%- if item.BGNTAI is not none -%}
            BGNTAI="{{item.BGNTAI}}",
        {%- endif -%}
        {%- if item.ENDTAI is not none -%}
            ENDTAI="{{item.ENDTAI}}",
        {%- endif -%}
        ;
    {%- endfor -%}
{%- endif -%}
```

#### 2.6 Pool参数配置完成后，需要进行数据配置一致性检查。

#### **表1** Pool参数配置阶段Checklist

#### | 数据配置的一致性检查 | 要求结果 | 检查结果 | 备注 |

#### | --- | --- | --- | --- |

#### | MMEID | 一致 | - | - |

#### | 权重信息 | 一致 | - | - |

#### | POOLLA | 一致 | - | - |

#### | 建立待割接的第一个enodeB的所有TAI的性能测量任务 | 已经建立 | - | - |

### 3 链路配置阶段。

### 在eNodeB和MME之间路由互通。

### 4 割接阶段。

#### 4.1 将eNodeB1连接到新的MME3上。

##### 4.1.1 根据之前准备的脚本进行链路配置，将S1接口配通。本步骤具体配置请参考《UNC初始配置与调测》。

##### 4.1.2 配置eNodeB1到MME3的相关信令和链路数据。

###### 4.1.2.1 在eNodeB上检查MME3的MMEID和权重是否正确。

###### 4.1.2.2 在MME3上检查4G的PAGING表是否上报。

##### 4.1.3 **可选：**如果TA对应的SGW的域名解析使用DNS Server配置，可以跳过此步。如果TA对应SGW的域名解析使用的是MME上的hostfile，需要在MME对应SGW的域名解析。

###### 4.1.3.1 增加IPV4DNSH解析

```jinja2
{%- if is_optional_mme_sgw_domain_resolution -%}
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

###### 4.1.3.2 增加DNSN解析

```jinja2
{%- if is_optional_mme_sgw_domain_resolution -%}
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

##### 4.1.4 在MME1上配置eNodeB1相关的TALIST。

```jinja2
{%- for item in add_talst_list -%}
    ADD TALST:
    {#- --- 必选参数 --- -#}
    TALISTID={{item.TALISTID}},
    TAI="{{item.TAI}}",
    ;
{%- endfor -%}
```

##### 在进行eNodeB割接时同一个TALIST下的所有eNodeB需要同时割接，不能分批进行割接。

##### 4.1.5 增加TAILAI配置。

```jinja2
{%- for item in add_tailai_list -%}
    ADD TAILAI:
    {#- --- 必选参数 --- -#}
    BGNTAI="{{item.BGNTAI}}",
    LAI="{{item.LAI}}",
    {#- --- 可选参数 --- -#}
    {%- if item.ENDTAI is not none -%}
        ENDTAI="{{item.ENDTAI}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 如有CSFB部署的场景，对于新增TA，根据规划增加TAILAI配置 。

##### 4.1.6 DNS Server上增加MME IP

##### 为了保证从Pool外MME到Pool内MME的切换分摊均匀，需要在DNS Server上针对所有Pool内TA区增加本MME的IP。

##### 本例中，对于域名“TAC-LB04.TAC-HB31.TAC.EPC.MNC03.MCC123.3GPPNETWORK.ORG”，将在DNS上将eNodeB1的路由区域名解析成为MME1、MME2和MME3的GTPC地址。并通知与该eNodeB1覆盖范围相邻的非本MME Pool的其他MME做相应的数据修改。

##### 通常地，本网内有一个本地DNS Server，上一级DNS Server不在本地。这种情况下，当核心网内多个MME改造成Pool后，该DNS Server可以视作Pool外的DNS Server，也可以视作Pool内的DNS Server，它除了保留原有的域名解析数据、解析功能外，还需要为MME Pool增加TA对应的IP地址配置。 以华为DNS Server为例

###### 4.1.6.1 方式一：在华为DNS Server的LMT上配置，主备均需要：

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_resrec_list的变量区（command: ADD RESREC） -#}
<!-- MISSING_MACRO: command=ADD RESREC list_name=add_resrec_list step_id=4.1.6.1 -->
```

###### 4.1.6.2 方式二：在不带LMT的DNS Server上，在named.ra文件中增加A记录（详细参见《DNS产品文档》）：

###### TAC-LB04.TAC-HB31.TAC.EPC                 IN       A        10.168.153.1

###### TAC-LB04.TAC-HB31.TAC.EPC                 IN       A        10.168.155.2

###### TAC-LB04.TAC-HB31.TAC.EPC                 IN       A        10.168.151.3

##### 1. 如果本网的运营商除了本地DNS Server外，还有上一级的DNS Server也在本地，在改造成MME Pool后，Pool内有一个DNS Server A，Pool外还有一个上级的DNS Server B，则，TA对应IP地址的数据配置就需要在DNS Server B上完成。这种情况比较少见。

##### 2. 如果修改了DNS Server的数据，需要清除各MME上的cash配置。

##### 4.1.7 进行业务拨测。

##### 重复步骤3，步骤4，以相同的方式割接剩余的eNodeB。

### 5 **可选：**执行用户迁移保证负荷均衡。

### 当出现负荷不均衡告警时可执行本步骤，请参见《U2020 MBB网络管理系统 虚拟化产品文档》（“操作与维护 > 核心网管理 > MME Pool管理 > MME Pool日常维护 > 均衡MME Pool负荷 > 手工迁移MME Pool用户”章节）/《iMaster MAE产品文档》（“操作与维护 > MAE-Access操作与维护 > 核心网管理 > MME Pool管理 > MME Pool日常维护 > 均衡MME Pool负荷 > 手工迁移MME Pool用户”章节）。

