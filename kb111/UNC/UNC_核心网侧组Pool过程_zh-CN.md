---
id: ''
name: 核心网侧组Pool过程
ne_type: UNC
type: feature
description: 本操作指导描述核心网组Pool配置过程。
risk_level: ''
doc_source: ["网络部署","特性部署","UNC特性指南","容灾功能","SGSN容灾方案","新建部署","激活业务","典型场景：SGSN Pool新建","全网新建","核心网侧组Pool过程"]
refs: []
metadata:
  DepOnLiveCfg: false
allowed-tools: []
---
<!-- @mml:block=annotations -->
```text
## 操作场景
本操作指导描述核心网组Pool配置过程。

## 必备事项
前提条件

Pool功能预设置已经配置完成。
```

## 2 输入参数变量定义
<!-- @mml:block=params -->
```yaml
schemas:
  properties:
    add_pool_list:
      type: items
      properties:
        POOLID:
          name: 'POOL标识'
          type: integer
          minimum: 0
          maximum: 4095
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NRILENGTH:
          name: 'NRI长度'
          type: integer
          minimum: 1
          maximum: 10
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_localnri_list:
      type: items
      properties:
        POOLID:
          name: 'POOL区标识'
          type: integer
          minimum: 0
          maximum: 4095
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NRIVBGN:
          name: 'NRI起始值'
          type: integer
          minimum: 0
          maximum: 1023
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NRINUM:
          name: 'NRI个数'
          type: integer
          minimum: 1
          maximum: 64
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_sys_list:
      type: items
      properties:
        MCC:
          name: '移动国家码'
          type: string
          maxLength: 3
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        MNC:
          name: '移动网号'
          type: string
          maxLength: 3
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        CNID:
          name: '核心网标识'
          type: integer
          minimum:
          - 0
          - 65535
          maximum:
          - 4095
          - 65535
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_poolnri_list:
      type: items
      properties:
        POOLID:
          name: 'POOL区标识'
          type: integer
          minimum: 0
          maximum: 4095
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NRIV:
          name: 'NRI值'
          type: integer
          minimum: 0
          maximum: 1023
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPTYPE:
          name: 'IP类型'
          type: string
          enum:
          - IPV4
          - IPV4V6
          - IPV6
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4:
          name: 'SGSN信令面地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SGSNN:
          name: 'SGSN名称'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
        ALTERNATIVE:
          name: 'SGSN信令面地址2'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6:
          name: 'SGSN信令面地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    add_nonrai_list:
      type: items
      properties:
        NONRAI:
          name: '路由区标识'
          type: string
          maxLength: 12
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPTYPE:
          name: 'IP类型'
          type: string
          enum:
          - IPV4
          - IPV4V6
          - IPV6
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV4:
          name: 'SGSN IPv4信令面地址'
          type: string
          maxLength: 15
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        SGSNN:
          name: 'SGSN名称'
          type: string
          maxLength: 32
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: 'noname'
        ALTERNATIVE:
          name: 'SGSN IPv6信令面地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IPV6:
          name: 'SGSN IPv6信令面地址'
          type: string
          maxLength: 39
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    rst_nodebatch_list:
      type: items
      properties:
        APPID:
          name: '网元ID'
          type: integer
          minimum: 0
          maximum: 65535
          required: true
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_rnc_list:
      type: items
      properties:
        RNCX:
          name: 'RNCX'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        IU\_FLEX:
          name: 'IU\_FLEX'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_nse_list:
      type: items
      properties:
        NSEI:
          name: 'NSEI'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GB\_FLEX:
          name: 'GB\_FLEX'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    mod_gbnsecfgpara_list:
      type: items
      properties:
        PARAINDEX:
          name: 'PARAINDEX'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        GB\_FLEX:
          name: 'GB\_FLEX'
          type: string
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
    set_offloadinf_list:
      type: items
      properties:
        OFFLOADTMR:
          name: '迁移模式周期路由更新定时器（s）'
          type: integer
          minimum: 2
          maximum: 60
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        FIRSTTM:
          name: '第一阶段迁移时间（min）'
          type: integer
          minimum: 0
          maximum: 432
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NONRAI:
          name: '非广播 RAI'
          type: string
          maxLength: 12
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        POOLID:
          name: 'POOL区标识'
          type: integer
          minimum: 0
          maximum: 4095
          required: false
          description: ''
          data_source: ''
          pattern: ''
          default: ''
        NULLNRIV:
          name: 'NULL NRI值'
          type: integer
          minimum: 0
          maximum: 1023
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
  examples:
    add_pool_list:
    - POOLID: 0
      NRILENGTH: 5
    add_localnri_list:
    - POOLID: 0
      NRIVBGN: 1
      NRINUM: 1
    set_sys_list:
    - MCC: '123'
      MNC: '00'
      CNID: 1
    add_poolnri_list:
    - POOLID: 0
      NRIV: 2
      IPTYPE: IPV4
      IPV4: '10.2.155.2'
      SGSNN: 'SGSN2'
      ALTERNATIVE: ''
      IPV6: ''
    - POOLID: 0
      NRIV: 3
      IPTYPE: IPV4
      IPV4: '10.2.151.3'
      SGSNN: 'SGSN3'
      ALTERNATIVE: ''
      IPV6: ''
    add_nonrai_list:
    - NONRAI: '12300615555'
      IPTYPE: IPV4
      IPV4: '10.2.155.2'
      SGSNN: 'SGSN2'
      ALTERNATIVE: ''
      IPV6: ''
    - NONRAI: '12300616666'
      IPTYPE: IPV4
      IPV4: '10.2.151.3'
      SGSNN: 'SGSN3'
      ALTERNATIVE: ''
      IPV6: ''
    rst_nodebatch_list:
    - APPID: 0
    mod_rnc_list:
    - RNCX: '0'
      IU\_FLEX: YES
    mod_nse_list:
    - NSEI: '0'
      GB\_FLEX: YES
    mod_gbnsecfgpara_list:
    - PARAINDEX: '1'
      GB\_FLEX: YES
    set_offloadinf_list:
    - OFFLOADTMR: 4
      FIRSTTM: 54
      NONRAI: '12300614444'
      POOLID: 0
      NULLNRIV: 10
    add_poolla_list:
    - LAC: '0001'
    add_poolla_list_3:
    - BGNTAI: '123033101'
      ENDTAI: '123033105'
      LAC: '0001'
```

## 3 命令模板定义
<!-- @mml:block=commands -->

### 1 配置新建的SGSN1的Pool参数。

#### 1.1 设置SGSN1的Pool ID和NRI长度。

```jinja2
{%- for item in add_pool_list -%}
    ADD POOL:
    {#- --- 必选参数 --- -#}
    POOLID={{item.POOLID}},
    NRILENGTH={{item.NRILENGTH}},
    ;
{%- endfor -%}
```

#### 目前NRI长度等于7bit仅在中国部署。在海外部署时，NRI长度采用5bit。

#### 1.2 配置SGSN1的本局NRI，SGSN1在P-TMSI分配时将使用此处设定的NRI值。

```jinja2
{%- for item in add_localnri_list -%}
    ADD LOCALNRI:
    {#- --- 必选参数 --- -#}
    POOLID={{item.POOLID}},
    NRIVBGN={{item.NRIVBGN}},
    NRINUM={{item.NRINUM}},
    ;
{%- endfor -%}
```

#### 1.3 配置SGSN1的全球CN标识（Global CN ID）。

#### 配置SGSN的全球CN标识（Global CN ID），使用Iu-flex功能时，SGSN给RAN发送的某些消息中需要带有Global CN ID，RAN侧会在SGSN主动触发的流程比如Reset流程、Relocation Request流程中，使用Global CN ID标识SGSN。

```jinja2
{%- for item in set_sys_list -%}
    SET SYS:
    {#- --- 可选参数 --- -#}
    {%- if item.MCC is not none -%}
        MCC="{{item.MCC}}",
    {%- endif -%}
    {%- if item.MNC is not none -%}
        MNC="{{item.MNC}}",
    {%- endif -%}
    {%- if item.CNID is not none -%}
        CNID={{item.CNID}},
    {%- endif -%}
    ;
{%- endfor -%}
```

#### 假设SGSN移动国家代码为123，移动网号为00。

#### 1.4 设置Pool区内其它SGSN的NRI信息。一般情况下，建议在DNS Server中配置，如果运营商采用POOLNRI配置，则命令如下：

##### 1.4.1 //设置SGSN2的NRI信息

```jinja2
{%- for item in add_poolnri_list -%}
    ADD POOLNRI:
    {#- --- 必选参数 --- -#}
    POOLID={{item.POOLID}},
    NRIV={{item.NRIV}},
    IPTYPE={{item.IPTYPE}},
    {#- --- 可选参数 --- -#}
    {%- if item.SGSNN is not none -%}
        SGSNN="{{item.SGSNN}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPTYPE=IPV4/IPV4V6 时必选 --- -#}
    {%- if item.IPTYPE in ['IPV4', 'IPV4V6'] -%}
        IPV4="{{item.IPV4}}",
    {%- endif -%}
    {#- --- 条件必选：IPTYPE=IPV4V6 时必选 --- -#}
    {%- if item.IPTYPE == 'IPV4V6' -%}
        ALTERNATIVE="{{item.ALTERNATIVE}}",
    {%- endif -%}
    {#- --- 条件必选：IPTYPE=IPV6 时必选 --- -#}
    {%- if item.IPTYPE == 'IPV6' -%}
        IPV6="{{item.IPV6}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 1.4.2 该Pool区内其它SGSN的NRI信息，主要是在Inter RAU流程时，根据NRI与IP地址的对应关系获取对端SGSN的地址信息。一个NRI对应一个SGSN，是一一对应的。

##### 如果对端SGSN存在多个GTPC地址时，通过**ADD POOLNRI**命令配置其中一个即可。为了实现对端SGSN不同GTPC IP之间的负载均衡，可通过本命令配置对端SGSN不同的GTPC IP。

#### 1.5 设置Pool区内其它SGSN的非广播路由区信息。一般情况下，建议在DNS Server中配置，如果运营商采用NONRAI配置，则命令如下：

##### 1.5.1 //设置SGSN2的非广播路由区信息

```jinja2
{%- for item in add_nonrai_list -%}
    ADD NONRAI:
    {#- --- 必选参数 --- -#}
    NONRAI="{{item.NONRAI}}",
    {#- --- 可选参数 --- -#}
    {%- if item.IPTYPE is not none -%}
        IPTYPE={{item.IPTYPE}},
    {%- endif -%}
    {%- if item.SGSNN is not none -%}
        SGSNN="{{item.SGSNN}}",
    {%- endif -%}
    {#- --- 条件必选参数 --- -#}
    {#- --- 条件必选：IPTYPE=IPV4/IPV4V6 时必选 --- -#}
    {%- if item.IPTYPE in ['IPV4', 'IPV4V6'] -%}
        IPV4="{{item.IPV4}}",
    {%- endif -%}
    {#- --- 条件必选：IPTYPE=IPV4V6 时必选 --- -#}
    {%- if item.IPTYPE == 'IPV4V6' -%}
        ALTERNATIVE="{{item.ALTERNATIVE}}",
    {%- endif -%}
    {#- --- 条件必选：IPTYPE=IPV6 时必选 --- -#}
    {%- if item.IPTYPE == 'IPV6' -%}
        IPV6="{{item.IPV6}}",
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 1.5.2 该Pool区内其它SGSN的非广播路由区信息，主要是在Inter RAU流程时，根据非广播路由区与IP地址的对应关系获取对端SGSN的地址信息。一个非广播路由区对应一个SGSN，是一一对应的。

##### 如果对端SGSN存在多个GTPC地址时，通过**ADD NONRAI**命令配置其中一个即可。为了实现对端SGSN不同GTPC IP之间的负载均衡，可通过本命令配置对端SGSN不同的GTPC IP。

#### 1.6 复位SGSN1，使得Pool相关参数的设置生效。

```jinja2
{%- for item in rst_nodebatch_list -%}
    RST NODEBATCH:
    {#- --- 必选参数 --- -#}
    APPID={{item.APPID}},
    ;
{%- endfor -%}
```

#### 1.7 在SGSN1上打开需要加入Pool的RNC/BSC的Flex开关。

#### Iu-Flex：**MOD RNC**: RNCX=0, IU\_FLEX=YES;

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该mod_rnc_list的变量区（command: MOD RNC） -#}
<!-- MISSING_MACRO: command=MOD RNC list_name=mod_rnc_list step_id=1.7 -->
```

#### Gb-Flex：

##### 1.7.1 Gb接口静态配置：**MOD NSE**: NSEI=0, GB\_FLEX=YES;

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该mod_nse_list的变量区（command: MOD NSE） -#}
<!-- MISSING_MACRO: command=MOD NSE list_name=mod_nse_list step_id=1.7.1 -->
```

##### 1.7.2 Gb接口动态自动配置：**MOD GBNSECFGPARA**: PARAINDEX=1, GB\_FLEX=YES;

```jinja2
{#- 需人工查询macro中是否存在该command并且包含parameters参数的命令，确认后人工填写jinja模板并优化该mod_gbnsecfgpara_list的变量区（command: MOD GBNSECFGPARA） -#}
<!-- MISSING_MACRO: command=MOD GBNSECFGPARA list_name=mod_gbnsecfgpara_list step_id=1.7.2 -->
```

#### 1.8 配置本局迁移参数信息。

##### 1.8.1 //设置本SGSN的迁移参数信息

```jinja2
{%- for item in set_offloadinf_list -%}
    SET OFFLOADINF:
    {#- --- 可选参数 --- -#}
    {%- if item.OFFLOADTMR is not none -%}
        OFFLOADTMR={{item.OFFLOADTMR}},
    {%- endif -%}
    {%- if item.FIRSTTM is not none -%}
        FIRSTTM={{item.FIRSTTM}},
    {%- endif -%}
    {%- if item.NONRAI is not none -%}
        NONRAI="{{item.NONRAI}}",
    {%- endif -%}
    {%- if item.POOLID is not none -%}
        POOLID={{item.POOLID}},
    {%- endif -%}
    {%- if item.NULLNRIV is not none -%}
        NULLNRIV={{item.NULLNRIV}},
    {%- endif -%}
    ;
{%- endfor -%}
```

##### 迁移参数信息只在进行迁移流程才使用，该脚本含义为设置SGSN容量为100K，迁移模式周期路由区更新定时器时长为4s，第一阶段迁移时间为54min，非广播路由区为：12300614444，所迁移用户Pool区标识为0，NULL NRI值为10。

#### 1.9 **可选：**在使用UNC作为融合节点同时支持SGSN POOL功能和MME POOL功能的场景下，如果MME需要通过S1接口下发LTE GUMMEI和Mapped GUMMEI，需要进行如下操作。

##### 1.9.1 没有规划TA和LA对应关系

```jinja2
{%- if is_optional_mme_gummei_config and is_scenario_no_ta_la_mapping -%}
    {%- for item in add_poolla_list -%}
        ADD POOLLA:
        {#- --- 必选参数 --- -#}
        LAC="{{item.LAC}}",
        ;
    {%- endfor -%}
{%- endif -%}
```

##### 1.9.2 规划了TA和LA的对应关系

```jinja2
{%- if is_optional_mme_gummei_config and is_scenario_ta_la_mapping -%}
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

### 2 配置SGSN2、SGSN3数据

### 与配置SGSN1数据步骤和过程类似，请参见配置新建的SGSN1的Pool参数。

### 3 数据配置完成后，需要进行数据配置一致性检查、Flex功能检查、核心网配置检查，具体检查项如表1所示。

### **表1** 数据配置检查Checklist

### | 数据配置检查项 | 要求结果 |

### | --- | --- |

### | Pool ID | 一致 |

### | NRI长度 | 一致 |

### | Local NRI | 不重复，与规划数据一致。 |

### | CN ID | 不一致 |

### | Pool NRI | 所有SGSN均配置了Pool内其他SGSN的NRI和IP地址的对应关系，且IP地址配置一致。 |

### | 建立待割接的第一个RNC的所有RAI的性能测量任务 | 已经建立 |

### | LICENSESWITCH配置 | Iu-flex/Gb-flex开启 |

### | 鉴权开关（Inter RAU 、PDP激活鉴权、Attach、签名不匹配、无签名等） | 打开 |

### | POOLLA | 与规划一致 |

### | RNC/BSC | Flex开关已打开 |

### | Iu Paging | 查询结果中包含割接RNC的RAI信息。 |

