---
id: ''
name: 改造业务
ne_type: UNC
type: feature
description: 本操作指导适用于描述4G现网演进成MME Pool的配置过程。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","容灾功能","MME容灾方案","改造部署","4G现网演进成MME Pool","改造业务"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导适用于描述4G现网演进成MME Pool的配置过程。

## 必备事项
前提条件

已经完成MME Pool用户迁移。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
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
        ZONE:
          name: 'ZONE'
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
    - FQDN: 'TAC-LB04.TAC-HB31.TAC.EPC.MNC003.MCC123.3GPPNETWORK.ORG'
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
      ZONE: MNC0000.MCC0123.gprs
      DOMAIN: TAC-LB04.TAC-HB31.TAC.EPC
      IP: 10.166.155.2
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置准备阶段

#### 1.1 割接前一周，检查待组建Pool的各MME的MML脚本，进行割接前的事项检查，确认无误后，备份各MME的MML脚本。

#### 1.2 割接前3天，提前准备以下脚本，并完成和华为技术支持的审核确认。

##### 1.2.1 各MME与待割接的eNodeB的新建S1接口配置脚本

##### 1.2.2 各MME上的Pool配置相关脚本

##### 1.2.3 DNS Server（可能是客户设备）上的配置脚本

#### 待割接的eNodeB1当前所连接的MME上已经有此eNodeB1关的配置数据，不用新增，只需在其他MME上配置eNodeB1相关数据。

### 2 配置同步阶段

#### 2.1 割接前一天或当晚，在各MME上，加载License文件，“MME Pool”(LKV2POOL02)、“Subscriber Migration in MME Pool”（可选，LKV2MMEMG02）功能。

#### 2.2 割接前一天或当晚，在U2020/MAE上，加载支持MME Pool管理的License文件。

#### 2.3 各MME配置参数同步。因为在改造之前，各MME上的配置可能有一些差别，如移动性管理和会话管理的相关配置，在组建Pool之后，需要保持一致。

### 3 Pool参数配置阶段。

### 根据场景描述中的网络规划规则，对网络进行规划，为每一台设备分配规划数据。

### 此配置举例以配置MME1为例，MME2、MME3配置类似。

#### 3.1 **可选：**修改MMEID，比如需要将MME Code(Begin)从6修改为8，请参见MME ID调整。

#### 修改MMEID会导致用户在一段时间内导致业务失败。

#### 3.2 在MME1上配置本MME的权重信息。

#### 3.3 **可选：**在使用UNC作为融合节点同时支持SGSN Pool功能和MME Pool功能的场景下，如果MME需要通过S1接口下发LTE GUMMEI和Mapped GUMMEI，需要进行如下操作。

##### 3.3.1 没有规划TA和LA对应关系。

```jinja2
{%- if is_optional_send_guemmei and is_scenario_no_ta_la_mapping -%}
    {%- for item in add_poolla_list -%}
        ADD POOLLA:
        {#- --- 必选参数 --- -#}
        LAC="{{item.LAC}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 3.3.2 规划了TA和LA的对应关系。

```jinja2
{%- if is_optional_send_guemmei and is_scenario_ta_la_mapping -%}
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

#### 3.4 重复步骤3中步骤 3.a~步骤 3.c，配置其他MME的Pool参数，本例中需要配置MME2、MME3的数据。

#### 3.5 参数配置完成后，需要进行数据配置一致性检查。

#### **表1** Pool参数配置阶段Checklist

#### | 数据配置的一致性检查 | 要求结果 |

#### | --- | --- |

#### | MMEID | 一致 |

#### | 权重信息 | 一致 |

#### | 建立待割接的所有TAI的性能测量任务 | 已经建立 |

### 4 割接阶段。

#### 4.1 在大容量局点，推荐首次割接或预割接时必须同时有2个eNodeB节点，目的是预割接时充分验证2个eNodeB节点的Pool负荷分担效果以及Pool内Guti分配效果。

#### 4.2 割接阶段就是将eNodeB逐个接入Pool的过程，此配置举例以割接eNodeB1为例，eNodeB2和eNodeB3割接过程类似。

### 第一次割接(预割接)的2个或1个eNodeB，按照如下几个方面进行操作：

#### 4.3 按照之前准备的脚本，配置新增连接的eNodeB与MME之间的链路数据，调通S1链路通信。

##### 4.3.1 核心网侧：在各MME上，分别配置与各个待割接的eNodeB的S1接口IP链路数据，然后调通各接口通信。

##### 4.3.2 无线侧：在各个待割接的eNodeB上，分别配置与各个MME之间的S1接口链路数据，然后调通各接口通信。

#### 4.4 核心网MME（非eNodeB1原直连的MME（MME2、MME3））侧：

##### 4.4.1 检查4G的PAGING表是否上报。

##### 4G的PAGING表是自动上报的，链路配置完成之后，使用命令检查LST S1PAGING，查询TA上报是否符合规划。

##### 4.4.2 可选：如果TA对应的S-GW的域名解析使用DNS Server配置，可以跳过此步。如果TA对应S-GW的域名解析使用的是MME上的hostfile，需要在MME上配置对应S-GW的域名解析。

###### 4.4.2.1 增加IPV4DNSH解析

```jinja2
{%- if is_optional_config_sgw_dns -%}
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

###### 4.4.2.2 增加DNSN解析

```jinja2
{%- if is_optional_config_sgw_dns -%}
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

###### 如果S-GW使用的是MME的hostfile解析，增加TA到MME对应S-GW的域名解析。如果S-GW是使用DNS Server解析，跳过。

##### 4.4.3 增加TALIST配置

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

#### 4.5 **可选：**增加TAILAI配置。

```jinja2
{%- if is_optional_add_tailai -%}
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
{%- endif -%}
```

#### 如有CSFB部署的场景，对于新增TA，根据规划增加TAILAI配置 。

#### 4.6 配置Pool内TA区对应Pool内MME的域名解析。

#### 为了保证从Pool外MME到Pool内MME的切换分摊均匀，需要在DNS Server或Hostfile上针对所有Pool内TA区增加Pool内其他MME的IP。

#### 配置MME的域名解析有两种方式：

##### 4.6.1 方式一：DNS配置方式。

##### 4.6.2 方式二：Hostfile配置方式。

#### 对于Hostfile配置方式，需要在Pool区外周边TA区对应的MME上配置。

#### 本例中，对于域名“TAC-LB04.TAC-HB31.TAC.EPC.MNC003.MCC123.3GPPNETWORK.ORG”，将在DNS上将eNodeB1的路由区域名解析成为MME1、MME2和MME3的GTPC地址。

#### 通常地，本网内有一个本地DNS Server，上一级DNS Server不在本地。这种情况下，当核心网内多个MME改造成Pool后，该DNS Server可以视作Pool外的DNS Server，也可以视作Pool内的DNS Server，它除了保留原有的域名解析数据、解析功能外，还需要为MME Pool增加TA对应的IP地址配置。

#### 以华为DNS Server为例：

##### 4.6.3 方式一：在华为DNS Server的LMT上配置，主备均需要：

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该add_resrec_list的变量区（command: ADD RESREC） -#}
<!-- MISSING_MACRO: command=ADD RESREC list_name=add_resrec_list step_id=4.6.3 -->
```

##### 4.6.4 方式二：在不带LMT的DNS Server上，在named.ra文件中增加A记录（详细参见《DNS产品文档》）：

##### TAC-LB04.TAC-HB31.TAC.EPC                       IN       A        10.166.155.2

##### TAC-LB04.TAC-HB31.TAC.EPC                       IN       A        10.166.151.3

###### 4.6.4.1 如果本网的运营商除了本地DNS Server外，还有上一级的DNS Server也在本地，在改造成MME Pool后，PooL内有一个DNS Server A，Pool外还有一个上级的DNS Server B，则，TA对应IP地址的数据配置就需要在DNS Server B上完成。这种情况比较少见。

###### 4.6.4.2 修改了DNS Server的记录，需要清除各MME上的cash记录

#### 4.7 核心网配置检查，上述全部操作（MME侧、DNS Server、eNodeB侧）完成后，在割接当晚执行该步骤。

#### **表2** 核心网配置检查Checklist

#### | 核心网配置检查 | 要求结果 |

#### | --- | --- |

#### | S1 Paging表 | 查询结果中包含割接eNodeB的TA信息 |

#### | TA LIST | 查询结果中包含割接eNodeB的TA信息 |

#### | TA对应S-GW解析 | 查询结果中包含割接eNodeB的TA信息 |

#### | DNS Server配置 | 与规划的一致 |

#### 4.8 接入网络测试（对割接入的eNodeB进行业务拨测）。

##### 4.8.1 基本上网业务拨测。

##### 4.8.2 Pool功能业务拨测。

##### 如果拨测失败且无法定位，Pool基本功能验证失败，需收集各设备上的配置信息和相关，进行Pool回退，参见回退业务。

##### 4.8.3 拨测成功后，观察网络运行状况。

###### 4.8.3.1 观察割接后MME的话统指标，在各个MME侧观察激活成功率，附着成功率，路由更新成功率的指标，其指标应该与割接前基本保持一致，以及BSC侧的话统结果。如果指标明显异常，需要倒回，参见回退业务。

###### 4.8.3.2 观察各MME和U2020/MAE上的告警。

###### 4.8.3.3 在U2020/MAE上组建MME Pool，将已进入Pool运行状态的各个MME纳入MME Pool，进行后续MME Pool管理。

##### 4.8.4 在割接后的第二天及一周内观察和分析相应数据是否正常。

##### 割接后话统明显异常，需要启动倒回流程，参见回退业务。

#### 4.9 重复步骤a~e，以相同的方式割接剩余的eNodeB，本例中为eNodeB2、eNodeB3。

### 5 **可选：**执行用户迁移保证负荷均衡。

### 请参见《U2020 MBB网络管理系统 虚拟化产品文档》（“操作与维护 > 核心网管理 > MME Pool管理 > MME Pool日常维护 > 均衡MME Pool负荷 > 手工迁移MME Pool用户”章节）/《iMaster MAE产品文档》（“操作与维护 > MAE-Access操作与维护 > 核心网管理 > MME Pool管理 > MME Pool日常维护 > 均衡MME Pool负荷 > 手工迁移MME Pool用户”章节）。

